# Culture Characters — Workshop Preview制作・採用手順

## 共通構図（2026-10-04承認済み）

このModは **AMJ共通シリーズの表紙** を使う。Projectの [WorkshopCoverStyle](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/WorkshopCoverStyle.md) と [WorkshopCoverPipeline](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/GoldenPaths/WorkshopCoverPipeline.md) が共通フォーマットの正本であり、本書はCharactersの固有要素だけを補足する。

- **左約40％：変更不可。** 承認済み共通の薄い和紙色の背景、`Ancient & / Medieval / Japan` のタイトル、区切り線・花飾りを原本から**画素ごと**再使用する。Mod名だけ指定スロットに `Characters` を入れる。
- **右約60％：Characters固有の絵。** 中世日本の人物の**経歴や特性を象徴する道具・身の回りの品**を、2～5程度の大きく見やすいモチーフで表現する。人物の顔・立ち絵・職業カードや架空のゲームUIを描かない。右側の細かな絵柄・道具選択は案ごとに監査し、採用前に固定しない。
- **全体を分割パネルやカード列にしない。** 左右は一続きの落ち着いた背景と余白でつなぎ、濃い区切り枠・派手な装飾・右側への共通タイトルの移動を禁止する。
- 承認済みの共通部分を**画像生成で描き直さない**。前案の右側黒色タイトルパネルと人物4カード案は不採用で、再利用しない。
- この構図は **AMJ共通シリーズに限定**。独立CCTO・CCTO for VPE・独立QoLへの強制適用をしない。

本書の前版（Characters PR #53）にある「共通レイアウトを適用しない」「人物を主題とする」「640×360を原則とする」という記述は、既承認のシリーズ構図・元画像と矛盾していたため**取り消す**。左側のフォーマットを自由に変更する権限はない。

## Characters固有のモチーフ条件

- 実装の中心は **元の背景126件の改稿、通常生成制限135件、新規の通常候補背景12件、酒に関する新特性2件**。職能や幼少期、生活史を象徴する物品を描いても、衣装・設備・武器・アイテム・新職業そのものをゲームに追加するModと誤認させない。
- 漁労・手仕事・農耕・旅装などの史実に合う物品を**候補として**検討できるが、実装された新道具だと宣伝しない。人物の職業名を小さなラベルで並べる説明カードは作らない。
- 126件の**改稿**と12件の**通常候補新規追加**を混同した数値宣伝をしない。新規定義14件中2件は通常生成から除外される。件数をPreviewに書く必然性はない。
- 過剰な和風記号（装飾用の鳥居、富士山、桜、家紋、武士等）を使わない。共通の小さな花飾りのみ承認済み原本を維持する。
- 色彩・太さ・情報量はProjectの承認済み実画像と照合し、サムネイル表示で各モチーフが読めることを優先する。

## 元画像・サイズ・合成

1. Projectの `Art/Sources/Workshop/AMJ_WorkshopCover_Core_Approved_Reference.jpg`、`AMJ_WorkshopCover_CommonBase.png`、`AMJ_WorkshopCover_VariableMask.png` を**実際に取得・開いて比較**し、[登録済みハッシュ](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/blob/main/Docs/References/AMJ_WorkshopCover_Manifest.md) と照合する。参照できない場合は想像による代替制作をしない。
2. 生成・描画するのは**右側の可変イラストのみ**。共通左側やタイトル、背景、装飾は生成対象に含めない。
3. Project `Scripts/build_workshop_cover.py` で既存マスター・マスクと合成し、`Scripts/validate_workshop_cover.py` で保護範囲の不変性を確認する。変更可能なのは右側可変領域と左側のMod名スロットのみ。
4. 共通画像の正式な制作キャンバスは **960×540 px、16:9**。提出物は通常 `About/Preview.png` のPNG、1 MiB未満。640×360や1280×720に勝手に縮小・拡大して**固定画素を変更しない**。
5. 配布ZIPや重複した配布ステージングは作らない。採用後はMod本体 `About/Preview.png` に含め、[ReleaseChecklist](../ReleaseChecklist.md) に従う。

## 候補の監査と採用

1. 制作前に、Characters `Docs/Design.md`・`README.md`・実製品 `Defs/`/`Patches/` と、Projectの承認済み表紙を照合する。
2. まずモチーフの歴史的妥当性、固有Modの機能との関係、右60％で成立する**構図の強弱・視線・余白**を判断する。不適切な構図は作画せず棄却する。
3. 画像候補が作れたら**毎回**、元画像・承認済み参照と比較し、形状・画風・背景の透過・サイズと比率・輪郭・文字・縮小視認性・右側の構図について監査し、採否と具体的な理由を示す。客観的に失敗した候補は作者への提示前に除外する。
4. 表示と同時に未監査結果が公開される生成ツールを使う場合、提示前監査を済ませたとは主張しない。候補の表示は作者の採用承認を意味しない。
5. **最終的な美術採用は作者判断。** 承認前に採用済みPreviewやSteam公開済みと扱わない。採用後、元データと完成PNGを保存し、GitHubのトピックブランチ→PR→mainに統合する。
6. 公開前に承認済みの原本との一致・サイズ・現在のREADME/Workshop文面との整合を再確認する。Steam初回公開は別途承認が必要。

2026-10-22現在、Charactersの `About/Preview.png` は未作成・未採用。ここで復元するのは**制作規則のみ**。
