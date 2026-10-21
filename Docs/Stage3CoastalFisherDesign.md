# P3 沿岸の漁師 — 確定仕様（2026-10-20）

**正本の内容:** 2026-10-20に本文と数値を承認。AMJ Culture – Characters の成人背景として実装し、既存9件へ追加して新規P3合計10件（成人8件、幼少期2件）とする。正式Defは `Defs/BackstoryDefs/Stage3HistoricalBackgrounds.xml`、翻訳正本は `Languages/Japanese/DefInjected/BackstoryDef/Stage3HistoricalBackgrounds.xml`。

| 属性 | 確定値 |
|---|---|
| ID | `AMJC_CoastalFisherAdult` |
| Slot | `Adulthood` |
| 名／略称 | 沿岸の漁師／漁師 |
| 技能 | `Animals +5` のみ |
| 生成カテゴリ | `Outlander`, `Tribal`, `Civil`, `MedievalCommon` |
| 強制Trait／作業禁止／所持品 | なし |
| 必須DLC・釣りMod／MO | なし |

## 承認済み日本語

> [PAWN_nameDef]は海辺の村で漁を生業とし、潮の満ち引きや魚の集まる場所を見極めながら、釣りや網漁で魚を獲ってきた。網や釣具の手入れも欠かさず、漁獲を浜へ運ぶ仕事にも慣れていた。

日本語の `baseDesc` と `description` は完全一致。英語Defの `title` = `coastal fisher`、`titleShort` = `fisher`。男女共通。

## ゲーム上の役割

沿岸漁の経験を既存の `Animals` で表現する。Odysseyの釣りでは動物技能が漁獲と速度に寄与する。専用の `Fishing` スキル、釣り仕事、漁具、沿岸居住や船の制約、強制Traitは追加しない。Odyssey・釣りModがなくても背景として出現可能であり、`Animals` は本来の動物仕事にも働く。既存の陸上狩猟経験（山野の猟師）や狩人家庭の幼少期とは職業・年齢枠が異なる。

## 先行実装と互換

既存の [Stage3ExistingModAudit](Stage3ExistingModAudit.md) はVanilla/MO、VE Vanilla Backstories Expanded、非VEのHistorical Backstories／Shavius／Medieval Backstories等を比較済み。追加の釣り機能ではなく日本沿岸の人物史1件を独立Defで表現するため、それらへの新規依存・互換パッチは不要。一般的な漁師の既存例まで存在しないと断言するものではない。

## 検証境界

**2026-10-20 実ゲーム受入：PASS。** [Project Actions #39417930528](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39417930528) でRimWorld原本1.7 English + Culture/Charactersの1シナリオを実行。新規 `AMJC_CoastalFisherAdult` のLoadedDef、成人枠、`Animals +5`のみ、カテゴリ `Outlander/Tribal/Civil/MedievalCommon`、強制Traitなし、英語題名を確認（`AMJ_CULTURE_P3_COASTAL_FISHER_OK` 1回）。同時に既存7件、織物職人、焼き物師のLoadedDefもPASS。Pickle1/1、ERROR0、FMOD0、exit0。明細・原ログ出典は [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md)。日本語原文はXML静的照合済みだが、**このEnglish 1.7テストは日本語画面表示の証拠ではない**。10件各々の自然抽選・頻度、MO側での最新3件、Odysseyの実釣り、元セーブ、Steamの承認は未実施。

**先行文書との整合:** `Docs/Design.md` の「漁師候補の技能整理（未実装）」は、この2026-10-20承認と本製品XMLの実装により**置換された過去の状態**とする。製塩の働き手は後日の2026-10-21承認により新規背景 `AMJC_SaltMakerAdult` として実装済み。沿岸漁の動物技能ともMOの採掘塩とも区別する。現行仕様は [Design.md](Design.md) および製品XMLを参照。

**2026-10-20 current binary acceptance:** [RimWorld 1.7 Japanese #39425746547](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39425746547) and [RimWorld 1.6 + original MO 1.6.2.2 English #39426497606](https://github.com/sucRo-RimWorld/Ancient-Medieval-Japan-Project/actions/runs/39426497606) both PASS with latest rebuilt Characters version-specific DLLs (Pickle1/1, Unity ERROR0, exit0), including loaded `AMJC_CoastalFisherAdult` adulthood/`Animals +5`/categories/no forced Trait and the other nine P3 histories. 1.7 loads approved Japanese text exactly; 1.6 runs original MO through disposable PCM-WAV audio. Neither run measures a fisher randomly selected nor screenshots its Japanese title, tests real Odyssey fishing, checks unmodified-MP3 audio, legacy saves or Steam. Authoritative exact source pins/markers: [Stage3NativeAcceptance.md](Stage3NativeAcceptance.md).

