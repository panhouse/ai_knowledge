---
title: "動画生成AIの基本(Sora・Runway・Luma Dream Machine・Klingなどの選び方)"
part: 8
chapter: 第3章 画像・動画・音声の生成AI
tags: [動画生成AI, Sora, Runway, Luma Dream Machine, Kling AI, Text-to-Video, Image-to-Video]
created: 2026-07-06
updated: 2026-09-05
---

# 動画生成AIの基本(Sora・Runway・Luma Dream Machine・Klingなどの選び方)

## これは何か

動画生成AI(Text-to-Video / Image-to-Video AI)は、文章の指示(プロンプト)や1枚の静止画から、数秒〜十数秒の動画クリップを自動生成するAIである。カメラ・出演者・撮影スタジオを用意しなくても、SNS広告やプロモーション素材の「たたき台」がその場で作れるようになった。

困りごとは「ツールが多すぎて何を選べばいいかわからない」ことだ。OpenAIのSora、RunwayのGenシリーズ、Luma AIのDream Machine、中国・快手(Kuaishou)のKling AIなど主要サービスが競い合っており、性能も料金体系も規約もサービスごとに異なる。しかもSoraのように**サービス自体の提供終了が既に発表され、しかも終了日が目前に迫っているケース**もあり、「今どれを選ぶべきか」の判断には最新動向の確認が欠かせない。本ページは2026年9月時点の主要ツールを比較し、業務での選び方と注意点(特に著作権・肖像権)を整理する。

## 仕組み・背景

動画生成AIの多くは、画像生成AIと同じ「拡散モデル(Diffusion Model、ノイズから少しずつ画像を復元していく仕組み)」を時間方向に拡張したもので、コマ(フレーム)ごとの絵柄の一貫性と、物体の動き(物理的な自然さ)を同時に学習させている。入力の与え方には主に2種類ある。

- **Text-to-Video**: 文章のプロンプトだけから動画を生成する。ゼロから世界観を作れるが、狙った絵にするための言語化力が要る
- **Image-to-Video**: 1枚の静止画(自社の商品写真など)を渡し、そこに動きを付ける。見た目のブレを抑えやすく、業務利用では扱いやすい

2024〜2025年は「数秒間、破綻なく動く」こと自体が競争点だったが、2026年に入ってからは音声(セリフ・環境音・BGM)の同時生成、実在する自分の姿を登録して動画に出演させる機能(OpenAI Soraの「Cameo」など)、複数カット(ショット)をまたいで人物・背景の一貫性を保つ「マルチショット生成」(Kling AIなど)、継ぎ目なしで30秒級の長尺クリップを1回で生成する機能(ByteDance Seedance 2.5)に競争軸が移っている。編集の主戦場も広がっており、Runwayは2026年5月21日に「Aleph 2.0」と新UI「Edit Studio」を公開し、既に撮影済みの実写映像を最大30秒・1080pまで自然言語の指示だけで書き換えられるようにした。さらに同年7月23日には、用途(コスト・速度・品質)に応じて自社・他社モデルを自動選択するAPI「Media Router」を発表するなど、「どのモデルを選ぶか」自体をツール側に任せる動きも出てきた。

## 使いどころ・使い分け

### 主要ツール比較(2026年9月時点)

| ツール | 提供元 | 最新モデル | 得意なこと | 特徴・向いている用途 | 個人向け料金の入口 |
|---|---|---|---|---|---|
| Sora | OpenAI(米) | Sora 2 / Sora 2 Pro | Text/Image→Video、音声同時生成、Cameo(本人同意の上で自分の姿を出演させる機能) | **2026年4月26日にアプリ提供終了。API自体も2026年9月24日に提供終了予定で、本ページ執筆時点(9月5日)では残り3週間を切っている。Disneyとの10億ドル規模のキャラクターライセンス提携(2025年12月発表)もサービス終了に伴い解消済み。新規導入の選択肢からは除外し、既存利用者は月内(9月24日まで)にデータのエクスポートと移行を完了させる必要がある** | ChatGPT Plus 20ドル/月・Pro 200ドル/月に内包(提供終了まで)。API 720pで1秒0.10ドル(Pro版0.30ドル)〜 |
| Runway | Runway(米) | Gen-4.5(Gen-4も継続提供)、編集はAleph 2.0+Edit Studio、演技転写はAct-Two | Text/Image→Video、Act-Two(人の演技を別キャラクターに転写)、Aleph 2.0(実写動画を自然言語だけで最大30秒・1080pまで書き換え)、Media Router(2026年7月23日公開。用途に応じ自社・他社モデルをAPIが自動選択) | 自社モデルに加え、Google Veo・Kling・Seedance・GPT Image 2・ElevenLabsなど**他社モデルも同一画面/APIから呼び出せるハブ型**。2026年5月にStandardプラン以上で全モデルへのアクセスを解放。プロ・代理店の本番制作、開発者のAPI統合の双方に強い | Standard 12ドル/月(年払い、月払いは15ドル程度)〜、Pro 28ドル/月〜、Max 76ドル/月〜。Gen-4.5はアプリ内12クレジット/秒、API従量は1秒0.12ドル |
| Luma Dream Machine | Luma AI(米) | Ray3 / Ray3.14(2026年1月。Ray3初期版比で生成速度4倍・コスト約1/3) | Text/Image→Video、HDR・EXR形式での出力、Ray3 Modify(参照画像・キャラクター指定によるVideo-to-Video編集) | 映像制作パイプライン(VFX・色調整)との連携を意識した設計。物理的に自然な動きとHDR画質の評価が高い | Lite 9.99ドル/月、Plus 29.99ドル/月、Pro 90ドル/月、Ultra 300ドル/月 |
| Kling AI | 快手(Kuaishou、中国) | Kling 3.0(2026年2月投入。Kling 3.0 Omni〈マルチモーダル統合〉、Kling 3.0 Motion Control〈動き指定〉の3ライン展開) | Text/Image→Video、リップシンク付き音声(5言語)、最大6カットのマルチショット生成、Director Mode、4K/60fps、モバイルアプリ対応 | コストパフォーマンスが高く、SNS向けショート動画の量産に強い。**中国企業提供のため、機密性の高い素材投入は社内規定を確認** | 無料(1日66クレジット、24時間で失効)、Standard 10ドル/月前後(660クレジット)、Pro 30〜37ドル/月前後(3,000クレジット)、Premier 90ドル/月前後(8,000クレジット)、Ultra 180ドル/月(2026年1月に128ドルから値上げ)。年払いで実質3割程度安くなるプランもある |
| (参考)Google Veo 3.1 / Gemini Omni | Google(米) | 開発者・本番向け: Veo 3.1 / 一般ユーザー向け: Gemini Omni Flash(2026年5月19日〜) | Text/Image→Video、音声同期、真の4K(3840×2160)・最大60fpsでの出力、チャットでの指示だけで動画を編集(Gemini Omni) | Geminiアプリ・Google Flow・YouTube Shortsでは2026年5月19日にVeoからGemini Omni Flashへ標準モデルが切り替わった(対話的に編集可能。YouTube Shorts/Createでは無料)。Vertex AI・Gemini API経由の本番用途では引き続きVeo 3.1を利用でき、解像度ごとに複数の品質ティア(Lite/Fast/標準)がある | Google AI Plus 7.99ドル/月〜(Omni Flash込み)、Pro 19.99ドル/月〜、Ultra 249.99ドル/月。API(Vertex AI)はVeo 3.1 Liteが1秒0.05ドル〜、標準/音声ありは1秒0.4〜0.75ドル程度 |

(参考として、Runway等のハブ型サービス内で使える第三者モデルの存在感も増している。ByteDanceのSeedance 2.5は2026年6月に発表・7月に一般公開され、継ぎ目〈スティッチ〉なしで最大30秒・ネイティブ4Kのクリップを1回で生成でき、画像・動画・音声を合わせて最大50点の参照素材を1つの生成に取り込める。xAIの「Grok Imagine Video 1.5」(2026年5月31日投入、X/Grokアプリに内蔵)は720p・音声付きの6〜15秒クリップを低コストで量産でき、SNSでバズる短尺動画の大量生成に強い。Pika Labsの「Pika 2.5」は効果音の自動生成やストーリーボード機能を備え、Adobe Fireflyの動画モデルはAdobe Stock由来の学習データで権利関係が明確なため、企業のブランド利用・広告代理店案件で選ばれやすい。特定モデルに固定せず、複数モデルを試して選ぶ、あるいはRunwayのようなハブ経由で使い分けるのが2026年時点の実務的なやり方になっている)

### 選び方の判断軸

| 状況 | 向いている選択 |
|---|---|
| SNS広告用の短尺動画を低コストで量産したい | Kling AI(クレジット単価が安く、image-to-videoの精度が高い) |
| ブランドCM・プロモーション映像でキャラクターの一貫性や演技表現が欲しい | Runway(Act-Twoでの演技転写、複数モデルを併用できるハブ型) |
| 実写合成・VFXパイプラインの一部として使いたい(色空間・HDRを保持したい) | Luma Dream Machine(EXR/HDR出力に対応) |
| 音声付きの動画を1回の生成で完結させたい、チャットで手軽に編集したい | Google Gemini Omni Flash(Geminiアプリ・Flow・YouTube Shorts) |
| API連携で本番システムに組み込みたい、Google系ツールと連携したい | Google Veo 3.1(Vertex AI・Gemini API) |
| 複数モデルを比較しながら使いたい、特定ベンダーに縛られたくない | Runway(Media Router経由でGen-4.5・Veo・Kling・Seedanceなどを1つのAPIから呼び分け) |
| 実写素材を「撮り直さずに」編集したい(背景・時間帯・アングルの変更など) | Runway Aleph 2.0 + Edit Studio(最大30秒・1080pまで自然言語だけで書き換え) |
| SNS(X/Grok)発の短尺動画を音声付きで大量・低コストに作りたい | xAI Grok Imagine Video 1.5(X/Grokアプリ内蔵、720p・音声付き6〜15秒に強い) |
| 権利処理が明確な素材が必要(広告代理店・エンタープライズのブランド利用) | Adobe Firefly動画モデル(Adobe Stock由来の学習データで商用利用の権利関係がクリア、Creative Cloud統合) |
| これから新規に動画生成AIを業務導入したい | **Soraは選ばない**(2026年9月24日にAPIも提供終了予定で、既に終了間近のため)。他社を優先して検討する |
| 社内の機密性が高い商品画像・非公開素材を使う | 提供元の国・データ保管方針を確認し、契約前に情報システム部門やセキュリティ担当に確認する |

## 実務での使い方

### 想定される業務シーン

- **SNS広告・ショート動画**: 商品写真をimage-to-videoで動かし、Instagram Reels・TikTok用の縦型動画素材にする
- **プロモーション動画のたたき台**: 実写撮影前に「こんな画作りにしたい」というイメージ動画(プレビズ)を作り、制作会社への発注仕様を固める
- **簡易な社内動画**: 研修動画のオープニング、社内イベントの告知動画など、外注コストをかけにくい用途
- **既存動画の編集・スタイル変換**: RunwayのAleph 2.0のように、実写で撮った素材の背景や画風だけをAIで変更する

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

いずれのサービスも「月額サブスクの中に一定量のクレジットが含まれ、動画の長さ・解像度・使用モデルに応じてクレジットを消費する」課金モデルが基本である。目安として、5秒程度の標準品質クリップ1本あたりの実質コストは、Kling AIで0.15〜0.6ドル程度(プラン・解像度により幅がある)、Runway Gen-4.5でAPI従量なら1秒0.12ドル(5秒で0.6ドル程度)、アプリ内サブスク換算では1〜1.5ドル程度、Luma Ray3.14で1ドル程度(720p)、Google Veo 3.1(Vertex AI)はLite/Fastなら1秒0.05〜0.10ドル、標準・音声ありは1秒0.4〜0.75ドル程度と幅が大きい。無料プランは商用利用が認められない、または透かし(ウォーターマーク)が入るケースが多く、業務で使う素材には有料プランが前提になる。契約前に必ず各社の最新の価格ページで確認すること(価格・クレジット付与量は変更が頻繁)。

## 注意点・よくある誤解

- **「1回の生成で完成品ができる」は誤解**: 手指の変形、文字の崩れ、物理的にありえない動きなど破綻が起きやすく、実務では複数パターン生成してベストショットを選ぶ運用が前提になる。歩留まり(採用率)を見込んで予算・時間を確保すること
- **肖像権・著作権への配慮が必須**: 実在の有名人・キャラクター名をプロンプトに入れて生成すると、肖像権侵害やパブリシティ権侵害、著作権侵害のリスクがある。OpenAIはSora 2の公開後、俳優・遺族からの抗議を受けて「本人の同意がない実在人物・著作権付きキャラクターの生成を禁止し、本人が明示的に登録(opt-in)した場合のみ利用可能」とする方針に修正した経緯がある。他社ツールでも同様のリスクがあるため、実在の人物・ブランド・作品名をプロンプトに含めないことを社内ルール化するとよい
- **Soraは新規導入の選択肢から外す**: 2026年4月26日にWeb/アプリ提供が終了しており、API自体も2026年9月24日に提供終了予定と発表されている。本ページ執筆時点(9月5日)で残り3週間を切っており、既にSoraを使っている場合はsora.chatgpt.com/sunsetから至急コンテンツをエクスポートし、月内に他社ツールへの移行を完了させる必要がある
- **無料・低価格プランの商用利用制限**: 多くのサービスで無料プランは「個人利用のみ」「透かし付き」に限定される。広告や社内配布に使う素材は、契約プランの利用規約で商用利用が明記されているかを必ず確認する
- **海外(特に中国系)サービスのデータ取り扱い**: Kling AIのように中国企業が提供するサービスに未公開の商品画像や社内資料をアップロードする場合、データの保管場所・利用規約を確認し、機密性の高い素材は避けるか情報システム部門に確認してから使う
- **生成された音声・BGMの権利リスク**: 音声同時生成に対応したツールでは、既存の楽曲や声優の声に類似した音声が生成される可能性がある。商用利用前に既存作品との類似性を確認する
- **モデル名・提供形態の変更が頻繁**: Googleは2026年5月19日、Geminiアプリ・Flow・YouTube Shorts上の標準モデルを「Veo」から対話編集対応の「Gemini Omni Flash」に切り替えた(本番用途のAPI・Vertex AIでは引き続きVeo 3.1)。RunwayはAlephを5月に「2.0」へ刷新し、Kling AIは3.0を1本ではなく「無印/Omni/Motion Control」の3ライン展開に組み替えた。Sora終了に伴いDisneyとの提携も履行前に解消されるなど、大型提携ですら数か月単位で覆ることがある。社内の利用ガイドラインには「モデル名」ではなく「提供元・用途・契約プラン」を軸に記録しておくと陳腐化しにくい
- **生成量の急増によるコンテンツの粗製濫造リスク**: xAIのGrok Imagineは2026年1月だけで12億本超の動画を生成したと報じられるなど、生成コストの低下でSNS上のAI動画の総量が急増している。自社発信に使う場合も「量産できる=品質担保が不要」ではない点に留意し、公開前のレビュー体制を保つ

## 最初の一歩

まずは無料または低価格プラン(Kling AIの無料枠、またはRunway Standardの体験)で、実際に使う予定の1シーン(自社商品の写真をimage-to-videoで5秒動かす、など)を試し、生成時間と仕上がり品質を体感してから、本格導入の予算を検討するとよい。社内でSoraを利用中であれば、この確認より先に、2026年9月24日のAPI終了に向けたデータのエクスポートと移行を最優先で片付けること。

## 関連トピック

- [生成AIと著作権のリスク](../part04-risk-security/copyright-risks-in-generative-ai.md)
- [ChatGPTの画像生成機能](../part03-ai-chat-tools/chatgpt-image-generation-feature.md)

## 更新履歴

### 2026-09-05: 主要ツールの最新動向を反映し比較表・使い分け・注意点を更新
- **内容**: Sora API終了(2026年9月24日)が本ページ執筆時点で3週間を切ったことを踏まえ、移行の緊急性を全編で強調。Runway Aleph 2.0とEdit Studio(2026年5月21日公開、実写動画を最大30秒・1080pまで自然言語で書き換え)の詳細、Gen-4.5の実クレジット単価(アプリ内12クレジット/秒、API 1秒0.12ドル)を追記。Kling 3.0が「無印/Omni/Motion Control」の3ライン展開であることと料金レンジ(Standard 10ドル前後〜Ultra 180ドル/月)を更新。Google Veo 3.1の真の4K(3840×2160)・60fps対応、Gemini AI Plus($7.99/月〜)の存在を追記。参考枠にByteDance Seedance 2.5(最大50点の参照素材対応)、xAI Grok Imagine Video 1.5(2026年5月31日投入、X/Grok内蔵の低コスト短尺動画)、Pika 2.5、Adobe Firefly動画モデル(権利関係が明確)を新規追加し、判断軸の表とプロンプト前の注意点に反映した
- **出典**: [What to know about the Sora discontinuation - OpenAI Help Center](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation), [Runway News: Introducing Aleph 2.0 and Edit Studio](https://runway.com/news/introducing-aleph-2-and-edit-studio), [Runway Gen-4.5 Pricing: Plans, Credits & Free Trial Explained (2026) - Magic Hour](https://magichour.ai/blog/runway-gen-45-pricing), [Runway AI pricing in 2026 - eesel AI](https://www.eesel.ai/blog/runway-ai-pricing), [Kling 3.0とは？機能、プロンプトのコツ、ユースケースを解説 - Morphic](https://morphic.com/jp/resources/how-to/kling-3.0-guide), [Kling AI Pricing (2026): Free vs Paid Plans & Real Video Costs - Atlas Cloud](https://www.atlascloud.ai/blog/tips/kling-ai-pricing), [Kling AI pricing (2026) - eesel AI](https://www.eesel.ai/blog/kling-ai-pricing), [Best AI Video Generators 2026: Sora 2 vs Veo 3.1 vs Kling 3.0 vs Runway - Get AI Perks](https://www.getaiperks.com/en/blogs/44-best-ai-video-generators-2026), [Google Vertex AI pricing in 2026 - CloudZero](https://www.cloudzero.com/blog/google-vertex-ai-pricing/), [Google's Gemini Omni turns images, audio, and text into video - TechCrunch](https://techcrunch.com/2026/05/19/googles-gemini-omni-turns-images-audio-and-text-into-video-and-thats-just-the-start/), [ByteDance launches Seedance 2.5 video-generation model - TechNode](https://technode.com/2026/07/31/bytedance-launches-seedance-2-5-video-generation-model/), [ByteDance unveils Seedance 2.5 - TheNextWeb](https://thenextweb.com/news/bytedance-seedance-2-5-ai-video-4k-30-seconds), [Grok Imagine: xAI Image & Video Generation Guide (2026) - Atlas Cloud](https://www.atlascloud.ai/blog/guides/grok-imagine), [Can Grok Generate Videos? Grok Imagine Video 1.5 - PixVerse](https://pixverse.ai/en/blog/grok-imagine-video-generation-capabilities-2026), [Pika AI Review 2026 - WeShop AI](https://www.weshop.ai/blog/pika-ai-review-2026-still-the-king-of-creative-ai-video-generation/), [Adobe Firefly Video Pricing 2026 - ToolColumn](https://www.toolcolumn.com/learn/adobe-firefly-video-pricing)

### 2026-07-27: 主要ツールの最新動向を反映し比較表・使い分けを更新
- **内容**: Runwayが2026年7月23日に発表した「Media Router」(自社・他社モデルを自動選択するAPI)とAleph 2.0への改称、Kling AIの料金体系の詳細(Premier・Ultraの追加、Ultraの値上げ)、Luma Ray3.14の性能改善(生成速度4倍・コスト約1/3)とRay3 Modify、GoogleがGeminiアプリ等の標準モデルをVeoから対話編集対応の「Gemini Omni Flash」へ切り替えた一方でAPI・Vertex AIはVeo 3.1を継続提供している点、ByteDance Seedance 2.5(継ぎ目なし30秒生成、2026年7月一般公開)の台頭、Sora終了に伴うDisneyとの10億ドル規模の提携解消を追記。判断軸の表に「複数モデルを使い分けたい」「API連携で本番導入したい」の行を追加し、注意点に「モデル名・提供形態の変更が頻繁」の項目を新設した
- **出典**: [Runway launches AI model router as generative media gets crowded - TechCrunch](https://techcrunch.com/2026/07/23/runway-bets-on-ai-model-routing-as-generative-media-gets-crowded/), [Introducing Runway Media Router - Runway](https://runway.com/news/company-news/introducing-runway-media-router), [Runway AI pricing in 2026 - eesel AI](https://www.eesel.ai/blog/runway-ai-pricing), [Kling AI pricing (2026) - eesel AI](https://www.eesel.ai/blog/kling-ai-pricing), [Kling Video 3.0 Features & Director Mode Guide](https://kling.ai/blog/kling-video-3-0-ai-director-features-guide), [Luma AI upgrades Ray3 model with faster, cheaper 1080p generative video - CSI Magazine](https://www.csimagazine.com/csi/Luma%20AI-upgrades-Ray3-model.php), [Plans & Pricing - Luma](https://lumalabs.ai/pricing), [Introducing Gemini Omni - Google Blog](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni/), [Google launches Gemini Omni Flash - TheNextWeb](https://thenextweb.com/news/google-gemini-omni-flash-video-model-io-2026), [ByteDance Seedance 2.5: Native 30-Second AI Video, No Stitching Required - Tech Times](https://www.techtimes.com/articles/318975/20260624/bytedance-seedance-25-native-30-second-ai-video-no-stitching-required.htm), [Why OpenAI and Disney Ended Their Deal - Variety](https://variety.com/2026/digital/news/why-openai-disney-ended-sora-deal-bob-iger-1236698901/)

### 2026-07-06: 初版執筆
- **内容**: Sora・Runway・Luma Dream Machine・Kling AI(参考としてGoogle Veo 3.1)の最新モデル・料金・得意分野を比較する初版を執筆。Soraのアプリ提供終了(2026年4月26日)・API提供終了予定(2026年9月24日)という重要な最新動向、Sora 2のCameo機能を巡る肖像権トラブルと規約変更の経緯、業務での使い分け基準、コピペ用プロンプト例、著作権・肖像権・データ取り扱いの注意点をまとめた
- **出典**: [What to know about the Sora discontinuation - OpenAI Help Center](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation), [Sora 2 pricing: A complete guide to OpenAI's video model costs in 2026 - eesel AI](https://www.eesel.ai/blog/sora-2-pricing), [Sora 2 Bans Celebrity Deepfakes—but People Found a Loophole - Newsweek](https://www.newsweek.com/sora-2-openai-bans-celebrity-deepfakes-but-people-found-loophole-10912528), [Runway AI Pricing - Runway](https://runwayml.com/pricing), [API Pricing & Costs - Runway API docs](https://docs.dev.runwayml.com/guides/pricing/), [Dream Machine Plans: Pricing and Credits - Luma Labs](https://lumalabs.ai/learning-hub/dream-machine-support-pricing-information), [Plans & Pricing - Luma](https://lumalabs.ai/pricing), [Kling AI Membership Plans](https://kling.ai/app/membership/membership-plan), [Kling AI pricing (2026) - eesel AI](https://www.eesel.ai/blog/kling-ai-pricing), [Build with Veo 3.1 Lite - Google Blog](https://blog.google/innovation-and-ai/technology/ai/veo-3-1-lite/)
