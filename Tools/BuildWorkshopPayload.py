#!/usr/bin/env python3
"""Create a deterministic Workshop subscriber ZIP from the Culture Characters source.

This script only stages local bytes. It never invokes Steam or changes a
Workshop item. Missing an approved About/Preview.png blocks a release ZIP;
--audit-only still reports an incomplete source inventory.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
import sys
import xml.etree.ElementTree as ET
import zipfile

MOD_NAME = 'Ancient & Medieval Japan - Culture Characters（中世日本 - 文化・人物）'
PACKAGE_ID = 'sucro.ancientmedievaljapan.culture.characters'
MANDATORY = (
    'LoadFolders.xml', 'LICENSE', 'About/About.xml', 'About/Manifest.xml',
    'About/Changelog.txt', 'About/WorkshopTags.xml',
    '1.6/Assemblies/AMJ.Culture.Characters.dll',
    '1.7/Assemblies/AMJ.Culture.Characters.dll',
)
CONTENT_DIRS = ('Defs', 'Languages', 'Patches')
PREVIEW = 'About/Preview.png'
VERSION_PATTERN = re.compile(r'^[0-9]+(?:\.[0-9]+){1,3}$')


def sha256(contents: bytes) -> str:
    return hashlib.sha256(contents).hexdigest()


def parse_xml(file: Path) -> ET.Element:
    try:
        return ET.parse(file).getroot()
    except ET.ParseError as exc:
        raise ValueError(f'Invalid XML {file}: {exc}') from exc


def source_inventory(root: Path) -> tuple[dict[str, bytes], dict]:
    if not root.is_dir():
        raise ValueError(f'Missing source directory: {root}')
    all_files: list[str] = list(MANDATORY)
    for folder in CONTENT_DIRS:
        base = root / folder
        if not base.is_dir():
            raise ValueError(f'Missing content directory: {base}')
        children = sorted(p for p in base.rglob('*') if p.is_file())
        if not children:
            raise ValueError(f'No content files in: {base}')
        for file in children:
            if file.suffix.lower() != '.xml':
                raise ValueError(f'Unexpected content file outside XML whitelist: {file}')
            all_files.append(file.relative_to(root).as_posix())
    preview_file = root / PREVIEW
    has_preview = preview_file.is_file()
    if has_preview:
        all_files.append(PREVIEW)
    files: dict[str, bytes] = {}
    for path in sorted(all_files):
        file = root / path
        if file.is_symlink() or not file.is_file():
            raise ValueError(f'Missing or symbolic-link subscriber file: {path}')
        files[path] = file.read_bytes()

    for path in files:
        if path.endswith('.xml'):
            parse_xml(root / path)
    about = parse_xml(root / 'About/About.xml')
    manifest = parse_xml(root / 'About/Manifest.xml')
    tags = parse_xml(root / 'About/WorkshopTags.xml')
    version = about.findtext('modVersion')
    if not version or not VERSION_PATTERN.fullmatch(version):
        raise ValueError(f'About version not a final dotted version: {version!r}')
    if manifest.findtext('version') != version:
        raise ValueError('Manifest version differs from About modVersion')
    if manifest.findtext('identifier') != 'AncientMedievalJapanCultureCharacters':
        raise ValueError('Unexpected stable Manifest identifier')
    if about.findtext('name') != MOD_NAME or about.findtext('packageId') != PACKAGE_ID:
        raise ValueError('Unexpected Mod name or packageId')
    versions = sorted(x.text for x in about.findall('./supportedVersions/li'))
    if versions != ['1.6', '1.7']:
        raise ValueError('Supported RimWorld versions must be 1.6 and 1.7')
    if 'brrainz.harmony' not in [x.text for x in about.findall('./modDependencies/li/packageId')]:
        raise ValueError('Required Harmony dependency missing')
    note = files['About/Changelog.txt'].decode('utf-8-sig')
    headings = [line for line in note.splitlines() if line.strip() and not line.lstrip().startswith('#')]
    if not headings or not re.match(r'^' + re.escape(version) + r'(?![.\d])\s', headings[0]):
        raise ValueError('Current version is not the first changelog heading')
    selected = [li.text for li in tags.findall('./li')]
    if tags.tag != 'WorkshopTags' or selected != ['Gameplay', 'Storytelling']:
        raise ValueError('Unexpected candidate Workshop tag selection')
    if has_preview:
        data = files[PREVIEW]
        if len(data) < 24 or not data.startswith(b'\x89PNG\r\n\x1a\n'):
            raise ValueError('Preview.png is not a PNG file')
    manifest_data = {
        'package_id': PACKAGE_ID,
        'version': version,
        'preview_present': has_preview,
        'payload_inputs_complete': has_preview,
        'entry_count': len(files),
        'entries': [
            {'path': path, 'size': len(data), 'sha256': sha256(data)}
            for path, data in sorted(files.items())
        ],
    }
    return files, manifest_data


def write_archive(files: dict[str, bytes], output: Path) -> str:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, mode='w', compression=zipfile.ZIP_STORED) as archive:
        for name, contents in sorted(files.items()):
            entry = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_STORED
            entry.create_system = 3
            entry.external_attr = (0o100644 << 16)
            archive.writestr(entry, contents)
    with zipfile.ZipFile(output) as archive:
        if archive.testzip() is not None or archive.namelist() != sorted(files):
            raise ValueError('Archive verification failed')
    return sha256(output.read_bytes())


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--audit-only', action='store_true', help='Check staging inventory without writing ZIP')
    parser.add_argument('--output', type=Path, help='Output ZIP path for an approved complete candidate')
    parser.add_argument('--lock-output', type=Path, help='Output JSON with entry hashes and archive digest')
    args = parser.parse_args()
    if not args.audit_only and args.output is None:
        parser.error('--output is required without --audit-only')
    if args.audit_only and (args.output or args.lock_output):
        parser.error('--audit-only does not write files')
    try:
        files, report = source_inventory(args.root.resolve())
        if not args.audit_only:
            if not report['preview_present']:
                raise ValueError('Missing About/Preview.png; add only author-approved artwork; refusing release ZIP')
            output = args.output.resolve()
            if output.is_relative_to(args.root.resolve()):
                raise ValueError('Output ZIP must be outside the source tree')
            report['archive_sha256'] = write_archive(files, output)
            report['archive_path'] = str(output)
            if args.lock_output:
                args.lock_output.parent.mkdir(parents=True, exist_ok=True)
                args.lock_output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    except (ValueError, OSError, UnicodeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
