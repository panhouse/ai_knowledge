---
title: "動画生成AIの基本(Sora・Runway・Luma Dream Machine・Klingなどの選び方)"
part: 8
chapter: 第3章 画像・動画・音声の生成AI
tags: [動画生成AI, Sora, Runway, Luma Dream Machine, Kling AI, Text-to-Video, Image-to-Video]
created: 2026-07-06
updated: 2026-07-06
---

# 動画生成AIの基本(Sora・Runway・Luma Dream Machine・Klingなどの選び方)

## これは何か

動画生成AI(Text-to-Video / Image-to-Video AI)は、文章の指示(プロンプト)や1枚の静止画から、数秒〜十数秒の動画クリップを自動生成するAIである。カメラ・出演者・撮影スタジオを用意しなくても、SNS広告やプロモーション素材の「たたき台」がその場で作れるようになった。

困りごとは「ツールが多すぎて何を選べばいいかわからない」ことだ。OpenAIのSora、RunwayのGenシリーズ、Luma AIのDream Machine、中国・快手(Kuaishou)のKling AIなど主要サービスが競い合っており、性能も料金体系も規約もサービスごとに異なる。しかもSoraのように**サービス自体の提供終了が既に発表されているケース**もあり、「今どれを選ぶべきか」の判断には最新動向の確認が欠かせない。本ページは2026年7月時点の主要ツールを比較し、業務での選び方と注意点(特に著作権・肖像権)を整理する。

## 仕組み・背景

動画生成AIの多くは、画像生成AIと同じ「拡散モデル(Diffusion Model、ノイズから少しずつ画像を復元していく仕組み)」を時間方向に拡張したもので、コマ(フレーム)ごとの絵柄の一貫性と、物体の動き(物理的な自然さ)を同時に学習させている。入力の与え方には主に2種類ある。

- **Text-to-Video**: 文章のプロンプトだけから動画を生成する。ゼロから世界観を作れるが、狙った絵にするための言語化力が要る
- **Image-to-Video**: 1枚の静止画(自社の商品写真など)を渡し、そこに動きを付ける。見た目のブレを抑えやすく、業務利用では扱いやすい

2024〜2025年は「数秒間、破綻なく動く」こと自体が競争点だったが、2026年に入ってからは音声(セリフ・環境音・BGM)の同時生成、実在する自分の姿を登録して動画に出演させる機能(OpenAI Soraの「Cameo」など)、複数カット(ショット)をまたいで人物・背景の一貫性を保つ「マルチショット生成」(Kling AIのKling 3.0など)に競争軸が移っている。

## 使いどころ・使い分け

### 主要ツール比較(2026年7月時点)

| ツール | 提供元 | 最新モデル | 得意なこと | 特徴・向いている用途 | 個人向け料金の入口 |
|---|---|---|---|---|---|
| Sora | OpenAI(米) | Sora 2 / Sora 2 Pro | Text/Image→Video、音声同時生成、Cameo(本人同意の上で自分の姿を出演させる機能) | **2026年4月26日にアプリ提供終了、API自体も2026年9月24日に提供終了予定と発表済み。新規導入は非推奨、既存利用者は移行計画が必要** | ChatGPT Plus 20ドル/月・Pro 200ドル/月に内包。API 720pで1秒0.10ドル(Pro版0.30ドル)〜 |
| Runway | Runway(米) | Gen-4.5(Gen-4も継続提供) | Text/Image→Video、Act-Two(人の演技を別キャラクターに転写)、Aleph(既存動画の編集・スタイル変換) | 自社モデルに加え、Google Veo・Kling・Seedanceなど**他社モデルも同一画面から呼び出せるハブ型**。プロ・代理店の本番制作に強い | Standard 12ドル/月(年払い、月払いは15ドル程度)〜、Pro 28ドル/月〜、Max 76ドル/月〜 |
| Luma Dream Machine | Luma AI(米) | Ray3 / Ray3.14(2026年1月) | Text/Image→Video、HDR・EXR形式での出力 | 映像制作パイプライン(VFX・色調整)との連携を意識した設計。物理的に自然な動きの評価が高い | Lite 9.99ドル/月、Plus 29.99ドル/月、Pro 90ドル/月、Ultra 300ドル/月 |
| Kling AI | 快手(Kuaishou、中国) | Kling 3.0(Omni Oneアーキテクチャ) | Text/Image→Video、リップシンク付き音声、最大6カットのマルチショット生成、4K/60fps | コストパフォーマンスが高く、SNS向けショート動画の量産に強い。**中国企業提供のため、機密性の高い素材投入は社内規定を確認** | 無料(1日66クレジット、繰越不可)、Standard 6.99ドル/月〜、Pro 25.99ドル/月〜 |
| (参考)Google Veo 3.1 | Google(米) | Veo 3.1 / Lite / Fast | Text/Image→Video、音声同期 | Gemini・Flow・Vertex AI経由で利用。Google Workspaceとの連携や、Runway経由での利用も可能 | Google AI Pro 19.99ドル/月(月1,000クレジット) |

(参考として、ByteDanceのSeedance 2.0など、Runway等のハブ型サービス内で使える第三国発モデルも増えている。特定モデルに固定せず、複数モデルを試して選ぶのが2026年時点の実務的なやり方になっている)

### 選び方の判断軸

| 状況 | 向いている選択 |
|---|---|
| SNS広告用の短尺動画を低コストで量産したい | Kling AI(クレジット単価が安く、image-to-videoの精度が高い) |
| ブランドCM・プロモーション映像でキャラクターの一貫性や演技表現が欲しい | Runway(Act-Twoでの演技転写、複数モデルを併用できるハブ型) |
| 実写合成・VFXパイプラインの一部として使いたい(色空間・HDRを保持したい) | Luma Dream Machine(EXR/HDR出力に対応) |
| 音声付きの動画を1回の生成で完結させたい、Google系ツールと連携したい | Google Veo 3.1 |
| これから新規に動画生成AIを業務導入したい | **Soraは選ばない**(サービス終了スケジュールが既に確定しているため)。他の3社を優先して検討する |
| 社内の機密性が高い商品画像・非公開素材を使う | 提供元の国・データ保管方針を確認し、契約前に情報システム部門やセキュリティ担当に確認する |

## 実務での使い方

### 想定される業務シーン

- **SNS広告・ショート動画**: 商品写真をimage-to-videoで動かし、Instagram Reels・TikTok用の縦型動画素材にする
- **プロモーション動画のたたき台**: 実写撮影前に「こんな画作りにしたい」というイメージ動画(プレビズ)を作り、制作会社への発注仕様を固める
- **簡易な社内動画**: 研修動画のオープニング、社内イベントの告知動画など、外注コストをかけにくい用途
- **既存動画の編集・スタイル変換**: Runwayの Aleph のように、実写で撮った素材の背景や画風だけをAIで変更する

### 操作の流れ(Runwayを例に)

1. runwayml.com にログイン → 左上の「Generate」または「+ New」からプロジェクトを作成
2. 上部タブで「Text to Video」または「Image to Video」を選択(画像を使う場合はここで写真をアップロード)
3. プロンプト欄に指示文を入力し、アスペクト比(16:9・9:16など)と動画の長さを選択
4. 「Generate」を押すと数十秒〜数分でクリップが生成される。気に入らない場合はプロンプトを微調整して再生成(1回ごとにクレジットを消費)
5. 気に入ったクリップをダウンロード、または編集画面でトリミング・音声追加を行う

他社ツールもおおむね同じ流れで、「Text to Video」「Image to Video」の呼称はほぼ共通している。Kling AIは公式サイト(kling.ai)の「AI Video」タブから、Luma Dream MachineはWebアプリ(dream-machine.lumalabs.ai)から同様に操作できる。

### コピペで使えるプロンプト例(商品プロモーション動画・image-to-video)

```
[被写体]の写真を使い、以下の指示で動かしてください。

- 動き: カメラがゆっくり左から右にパンしながら、[被写体]に近づく
- 背景: [背景の説明。例: 明るいスタジオの白背景]
- 照明: 柔らかい自然光、逆光にならないように
- 質感の変化: [被写体]の質感(光沢・素材感)が分かるように、光の反射を強調
- 雰囲気: 高級感のある、落ち着いたトーン
- 尺: 5秒程度、ループしても違和感がないように
```

### 料金の考え方

いずれのサービスも「月額サブスクの中に一定量のクレジットが含まれ、動画の長さ・解像度・使用モデルに応じてクレジットを消費する」課金モデルが基本である。目安として、5秒程度の標準品質クリップ1本あたりの実質コストは、Kling AIで0.35〜0.6ドル程度、Runway Gen-4.5で1〜1.5ドル程度(25クレジット/秒)、Luma Ray3.14で1ドル程度(720p)となる。無料プランは商用利用が認められない、または透かし(ウォーターマーク)が入るケースが多く、業務で使う素材には有料プランが前提になる。契約前に必ず各社の最新の価格ページで確認すること(価格・クレジット付与量は変更が頻繁)。

## 注意点・よくある誤解

- **「1回の生成で完成品ができる」は誤解**: 手指の変形、文字の崩れ、物理的にありえない動きなど破綻が起きやすく、実務では複数パターン生成してベストショットを選ぶ運用が前提になる。歩留まり(採用率)を見込んで予算・時間を確保すること
- **肖像権・著作権への配慮が必須**: 実在の有名人・キャラクター名をプロンプトに入れて生成すると、肖像権侵害やパブリシティ権侵害、著作権侵害のリスクがある。OpenAIはSora 2の公開後、俳優・遺族からの抗議を受けて「本人の同意がない実在人物・著作権付きキャラクターの生成を禁止し、本人が明示的に登録(opt-in)した場合のみ利用可能」とする方針に修正した経緯がある。他社ツールでも同様のリスクがあるため、実在の人物・ブランド・作品名をプロンプトに含めないことを社内ルール化するとよい
- **Soraは新規導入の選択肢から外す**: 2026年4月26日にWeb/アプリ提供が終了、API自体も2026年9月24日に提供終了予定と発表されている。既にSoraを使っている場合は、他社ツールへの移行計画を早めに立てる必要がある
- **無料・低価格プランの商用利用制限**: 多くのサービスで無料プランは「個人利用のみ」「透かし付き」に限定される。広告や社内配布に使う素材は、契約プランの利用規約で商用利用が明記されているかを必ず確認する
- **海外(特に中国系)サービスのデータ取り扱い**: Kling AIのように中国企業が提供するサービスに未公開の商品画像や社内資料をアップロードする場合、データの保管場所・利用規約を確認し、機密性の高い素材は避けるか情報システム部門に確認してから使う
- **生成された音声・BGMの権利リスク**: 音声同時生成に対応したツールでは、既存の楽曲や声優の声に類似した音声が生成される可能性がある。商用利用前に既存作品との類似性を確認する

## 最初の一歩

まずは無料または低価格プラン(Kling AIの無料枠、またはRunway Standardの体験)で、実際に使う予定の1シーン(自社商品の写真をimage-to-videoで5秒動かす、など)を試し、生成時間と仕上がり品質を体感してから、本格導入の予算を検討するとよい。

## 関連トピック

- [生成AIと著作権のリスク](../part04-risk-security/copyright-risks-in-generative-ai.md)
- [ChatGPTの画像生成機能](../part03-ai-chat-tools/chatgpt-image-generation-feature.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: Sora・Runway・Luma Dream Machine・Kling AI(参考としてGoogle Veo 3.1)の最新モデル・料金・得意分野を比較する初版を執筆。Soraのアプリ提供終了(2026年4月26日)・API提供終了予定(2026年9月24日)という重要な最新動向、Sora 2のCameo機能を巡る肖像権トラブルと規約変更の経緯、業務での使い分け基準、コピペ用プロンプト例、著作権・肖像権・データ取り扱いの注意点をまとめた
- **出典**: [What to know about the Sora discontinuation - OpenAI Help Center](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation), [Sora 2 pricing: A complete guide to OpenAI's video model costs in 2026 - eesel AI](https://www.eesel.ai/blog/sora-2-pricing), [Sora 2 Bans Celebrity Deepfakes—but People Found a Loophole - Newsweek](https://www.newsweek.com/sora-2-openai-bans-celebrity-deepfakes-but-people-found-loophole-10912528), [Runway AI Pricing - Runway](https://runwayml.com/pricing), [API Pricing & Costs - Runway API docs](https://docs.dev.runwayml.com/guides/pricing/), [Dream Machine Plans: Pricing and Credits - Luma Labs](https://lumalabs.ai/learning-hub/dream-machine-support-pricing-information), [Plans & Pricing - Luma](https://lumalabs.ai/pricing), [Kling AI Membership Plans](https://kling.ai/app/membership/membership-plan), [Kling AI pricing (2026) - eesel AI](https://www.eesel.ai/blog/kling-ai-pricing), [Build with Veo 3.1 Lite - Google Blog](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/)
