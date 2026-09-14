---
title: "ChatGPTの画像生成機能"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [ChatGPT, 画像生成, GPT Image, DALL-E, マルチモーダル, デザイン, プレゼン資料]
created: 2026-07-06
updated: 2026-09-13
---

# ChatGPTの画像生成機能

## これは何か

「バナー広告のイメージ画像が欲しい」「プレゼン資料に添える挿絵がない」という場面で、外部のデザインツールを開いたり、デザイナーに依頼して数日待ったりしなくても、ChatGPTに文章で頼むだけでその場で画像を作れる機能。以前は「DALL-E 3」という別モデルを呼び出す形だったが、現在はChatGPT本体のモデルに画像生成が組み込まれており、チャットの延長として「もう少し明るく」「文字を大きく」と会話しながら画像を仕上げていける点が最大の特徴になっている。2026年9月時点の最新モデルは「GPT Image 2.5」(消費者向けの呼び名は「ChatGPT Images 2.5」)で、無料プランを含む全プランに展開されている。

ラフなアイデア出し・チラシやSNS画像の下書き・アイコンやロゴのたたき台作りなど、「完璧な最終品ではなく、まず形にして検討を進める」用途に向いている。

## 仕組み・背景

### DALL-E 3からGPT Imageシリーズへ

2025年3月まで、ChatGPTの画像生成は「DALL-E 3」という画像専用の別モデルにテキストプロンプトを渡す仕組みだった。ChatGPT本体(GPT-4oなど)がプロンプトを解釈し、それを別モデルに引き渡して画像を作らせるため、指示の細部(文字の配置、人数、位置関係など)が生成過程で失われやすいという弱点があった。

2025年3月に登場した「GPT Image 1」以降、画像生成はChatGPT本体のモデルに統合された「ネイティブなマルチモーダル生成」に変わった。文章を書くのと同じ理屈で、画像も「トークン」を連ねるように生成する仕組みになっており、プロンプトの意図がそのまま画像に反映されやすくなっている。これにより、以前のDALL-E 3では苦手だった「看板やロゴに正確な文字を入れる」「複数の要素の位置関係を細かく指定する」といった作業の精度が大きく上がった。

その後のモデル更新の流れは以下の通り。

- **2025年12月: GPT Image 1.5** — 高速化・低コスト化した後継モデル。Free・Plus・Pro・Business・Enterpriseの全プランのデフォルトに切り替わった
- **2026年4月21日: GPT Image 2(ChatGPT Images 2.0)** — 解像度が最大2K相当、アスペクト比が3:1(横長)〜1:3(縦長)まで対応。日本語・韓国語・中国語などの非ラテン文字系言語の文字描写精度が向上。生成前に構図やテキストの正確性を内部で検討してから描く「推論(Thinking)」の仕組みが初めて組み込まれ、人物・物体の見た目を保った状態のまま最大8枚程度をまとめて生成できるようになった
- **2026年5月12日: DALL-E 3の完全提供終了** — APIも含めて提供が終了し、ChatGPT上でDALL-E系列を選ぶことはできなくなった
- **2026年9月8日: GPT Image 2.5(ChatGPT Images 2.5)** — 2026年9月時点の最新モデル。ChatGPT・ChatGPT Work・Codexの全プラン(無料プランを含む)に展開された。Images 2.0比で生成速度が最大50%向上し、参照写真として渡した被写体(人物・商品など)の見た目を保ったまま、指定した箇所だけを変える局所編集の精度が上がった(例: 空だけ差し替えて他の構図は保持する)。複数回にわたって編集を重ねても一貫性が崩れにくく、文字・グラフ・図表など実世界の情報を含む画像の精度も向上している。解像度は最長辺3840px(両辺は16の倍数、総画素数はおおむね65万5,360〜829万4,400ピクセルの範囲)まで対応し、アスペクト比は引き続き1:3〜3:1の範囲、参照画像は最大10枚まで使用できる

### GPT Image 2.5で加わった編集ツール

GPT Image 2.5(ChatGPT Images 2.5)では、画像そのものの精度向上に加えて、ChatGPTの画面上で使える編集ツールが増えた(2026年9月時点)。

- **Sketch(スケッチ)**: 入力欄で「@」を入力してメニューから「Sketch」を選び、タッチパネル・マウス・スタイラスでラフな構図を手描きし、それを参考画像として文章の指示と一緒に送信すると、その構図を土台にした画像を生成できる。現時点ではモバイルアプリでの提供が中心
- **テンプレート**: 「ポスター」「グッズ」「商品写真」「ロゴ」など定型フォーマットの雛形を選ぶと、スタイル(例: 「Clean Studio」「Editorial」など)や掲載したい情報を質問形式で答えていくだけで下書きができる
- **画像へのコメント**: 生成済みの画像の特定の箇所にコメントを置いて修正依頼を書き込むと、そこだけをピンポイントで編集できる(画像全体を作り直さずに済む)
- **プロンプト共有**: 使ったプロンプトを他の人と共有し、別の写真や条件で同じ作り方を再現してもらえる

### 会話形式での編集(反復修正)

一度生成した画像に対して、同じスレッド内で「背景をもう少し明るくして」「人物を中央に配置して」のように追加で指示すると、ゼロから作り直すのではなく直前の画像を土台に修正した画像を返してくる。これは画像生成が通常のチャットの会話履歴(コンテキスト)の一部として扱われているためで、Photoshopのようなレイヤー編集ツールを使わずに、対話だけで細部を詰めていけるのが実務上の強みになる。GPT Image 2.5では、この反復編集を何度繰り返しても被写体や構図の一貫性が崩れにくくなっている。

### 出所の証明(C2PA)

ChatGPTで生成した画像には、C2PA(Coalition for Content Provenance and Authenticity、コンテンツの出所を証明するための業界標準規格)のメタデータが自動的に埋め込まれる。画像ファイルのプロパティを専用ツールで確認すると「ChatGPTで生成された」という情報を検証できる仕組みで、SNSにアップロードした際にAI生成であることが分かるラベルが表示される場合もある。

## 使いどころ・使い分け

| 状況 | 向いている選択 |
|---|---|
| 社内プレゼンの挿絵、ブログ記事のアイキャッチ、SNS広告の下書きをすぐ欲しい | ChatGPTの画像生成で十分。数十秒〜数分で複数パターンを試せる |
| 資料内の図に日本語ラベル・数値を正確に入れたい | GPT Image 2.5は文字・図表の精度がさらに上がったが、重要な文字は生成後に目視確認・必要なら別ツールで修正するのが安全 |
| 商品カタログ用の高精細な写真、印刷物のような高解像度出力が必要 | Gemini(Nano Banana Pro)など高解像度対応モデルや、プロ向けツールを検討 |
| ブランドの世界観を作り込む、アート性の高いキービジュアルが欲しい | Midjourneyなど画作りに特化したツールの方が完成度が高い場合が多い |
| ロゴ・商標として実際に登録・商用展開する最終アセットが欲しい | AI生成のみで完結させず、デザイナーによる仕上げ・商標調査を挟む(著作権・商標のリスクは後述) |
| 実在の人物の写真を加工・別人化したい | 実在の人物と分かる形の生成はポリシー上ブロックされることが多く、そもそも避けるべき用途 |
| 手描きのラフや紙のレイアウト案をそのまま画像化したい | Sketch機能で構図を描いて渡すと、文章だけで説明するより意図が伝わりやすい |

判断基準は「たたき台・下書きとして素早く形にする」か「最終的にそのまま出す完成品」かという点。前者はChatGPTの画像生成が最も手軽で、後者は専用ツールや人の手による仕上げを挟む方が安全。

## 実務での使い方

### 呼び出し方(2026年9月時点)

1. ChatGPT(chatgpt.comまたはアプリ)にログインし、通常のチャット入力欄に作りたい画像の内容を文章で書いて送信する。「画像生成」ボタンを別途押す必要はなく、「〜の画像を作って」「〜のイラストを描いて」と頼むだけでモデルが画像生成に切り替わる
2. 生成された画像が気に入らない場合は、そのまま会話を続けて「もっとシンプルに」「配色を青系に変えて」など修正指示を出す
3. 既存の画像(自社のロゴ、商品写真など)を入力欄の「+」(ファイル添付)からアップロードし、「この画像の背景を消して」「このロゴのアイコン版を作って」のように指示すれば、その画像を土台にした編集もできる
4. 手描きのラフを参考にしたい場合は、入力欄で「@」を入力してメニューから「Sketch」を選び、構図を手描きしてから文章の指示を添えて送信する(2026年9月時点ではモバイルアプリでの提供が中心)
5. ポスターや商品写真など定型フォーマットを作りたい場合は、テンプレート機能からベースを選び、スタイル・掲載したい情報を質問形式で答えていくと下書きができる
6. 生成済みの画像の一部だけを直したい場合は、画像上にコメントを置いて修正依頼を書き込むと、その範囲だけがピンポイントで編集される
7. 有料プランでは、生成前に構図やレイアウトを内部で検討してから描く挙動(モデル選択欄で「Thinking」と表示される場合がある)が働き、複数枚のバリエーションをまとめて出したい時や、より作り込んだ構図が欲しい時に使う
8. 生成した画像は画面上で右クリック(またはダウンロードアイコン)から保存する

### プラン別の利用可否・上限(2026年9月時点の目安)

| プラン | 画像生成 | 目安の上限 |
|---|---|---|
| Free(無料) | GPT Image 2.5が全プランに展開されたことで、無料プランでも標準で利用可能 | OpenAIは具体的な回数を公表していない。目安として24時間あたり数枚程度とする報告が多いが、情報源によって「2〜3枚」から「20枚前後」まで幅があり、変動も大きい |
| Go(月額$8程度・日本では月額1,400円前後) | 利用可能 | Freeより緩やかとされるが具体的な上限は非公開。目安として1日あたり20〜50枚程度とする報告がある |
| Plus(月額$20) | 利用可能。Sketch・テンプレート・画像へのコメントなどの編集機能もフル活用できる | ローリングウィンドウ(直近の利用状況に応じて変動する)方式で、目安として3時間あたり数十枚程度 |
| Pro(月額$100/$200の2段階) | 利用可能 | 実質無制限(高速・高品質。OpenAIの不正利用防止ガードレールの範囲内) |
| Business・Enterprise | 利用可能 | 契約内容・管理設定による。実務上は「ほぼ無制限」の扱い |

プラン別の上限はOpenAIが正式な数値を公表しておらず、コミュニティの実測値も情報源によってばらつきが大きい。実務では、ChatGPTの画面上に表示される「残り◯回」といった案内を都度確認するのが最も確実。プラン全体の違いは[ChatGPTのプラン比較](chatgpt-plan-comparison.md)を参照。

### API経由で使う場合の課金

Zapierなどの自動化ツールやカスタムGPTs、自社システムからOpenAIのAPIを直接呼び出す場合は、ChatGPTのサブスク料金とは別に課金が発生する。2026年9月時点では、`gpt-image-2.5-flare`(高速・大量生成向け)と`gpt-image-2.5-sunburst`(精密な編集・高い再現性が必要な作業向け)の2種類のAPIモデルが提供されており、両者の価格は同一。課金はトークン単位で、目安は以下の通り。

- テキスト入力: 100万トークンあたり$5
- 画像入力: 100万トークンあたり$8(キャッシュ済み入力は$2)
- 画像出力: 100万トークンあたり$30

1024×1024程度の画像1枚に換算すると、画質設定(low〜max)に応じておおむね数円〜数十円(0.006〜0.2ドル程度)が目安になる。この料金体系が旧モデル(GPT Image 2)からの実質的な値上げか据え置きかは情報源によって説明が割れているため、API連携を検討する場合は契約前に[OpenAI公式のAPI Pricingページ](https://openai.com/api/pricing/)で当日時点のトークン単価を必ず確認すること。ChatGPTの画面上で使う分にはこの課金は意識しなくてよい。詳しくは[OpenAI APIの基本](../part09-api-development/openai-api-basics.md)を参照。

### コピペで使えるプロンプト例

**例1: プレゼン資料の挿絵**

```
新製品発表のプレゼン資料の表紙に使う画像を作ってください。
テーマ: クラウド型の勤怠管理サービス
雰囲気: 明るく信頼感のあるビジネス向け、フラットデザイン
配色: 青と白を基調
要素: ノートPCとチェックマークのアイコンを組み合わせたイメージ
アスペクト比: 16:9
テキストは入れないでください
```

**例2: SNS広告のバナー下書き(A/Bテスト用に複数パターン)**

```
夏季セールを告知するInstagram広告用のバナー画像を3パターン作ってください。
商品: 女性向けスキンケアクリーム
キャッチコピー(画像内に日本語で表示): 「夏の乾燥対策、今すぐ」
雰囲気: 涼しげで清潔感のあるトーン
アスペクト比: 1:1(Instagramフィード用)
3パターンはそれぞれ背景の色味を変えて提案してください
```

**例3: アイコン・ロゴのたたき台**

```
社内ツール「タスク管理くん」のアプリアイコンのたたき台を作ってください。
テイスト: ミニマルなフラットデザイン、角丸の正方形
モチーフ: チェックリストと矢印を組み合わせたシンプルなマーク
配色: 単色系(緑系)で1案、単色系(オレンジ系)で1案の2パターン
背景は透過(単色背景でも可)にしてください
```

生成後は「もう少し線を太く」「文字サイズを大きく」のように、同じスレッドで会話を続けて微調整するのがコツ。1回で完璧な指示を書くより、荒い指示→修正の繰り返しの方が早く狙った仕上がりに近づく。細部だけを直したい場合は、文章で指示し直すよりも画像上にコメントを置く方がピンポイントで伝わりやすい。

### 他ツールでの同等機能との対応

| ツール | 画像生成機能の呼び名 | 使う場所 | 位置づけ |
|---|---|---|---|
| ChatGPT | 画像生成(モデル: GPT Image 2.5 / ChatGPT Images 2.5) | 通常のチャット入力欄 | 会話ベースの反復編集が強み。文章生成と同じスレッドで完結する |
| Gemini(Google) | Nano Banana(Nano Banana 2 / Nano Banana Pro) | Gemini通常チャット | 高解像度・写実性で評価が高く、無料プランでも一定枚数使える |
| Microsoft Copilot | Image Creator(Designer) | copilot.microsoft.com、Copilotアプリ、Bing Image Creator | 無料で使いやすく、1日あたりのブースト枚数消化後も低速で生成可能 |
| Midjourney | Midjourney(Discord上のBotまたは専用Web版) | Discordコマンドまたは公式サイト | ビジュアルの完成度・アート性を最優先するならこちらが定番。チャットAIとしての会話機能は持たない |

「文章の作成・要約と同じ流れで画像も片付けたい」ならChatGPT、「高解像度・写実性を最優先」ならGemini、「無料で気軽に試したい」ならCopilot、「アート性の高い最終ビジュアルが欲しい」ならMidjourney、という大まかな使い分けになる。

## 注意点・よくある誤解

- **著作権は自動的にクリアではない**: OpenAIの利用規約上、生成した画像の利用権はユーザーに帰属し、商用利用も可能とされている。ただし米国など一部の法域ではAIのみが生成した作品は「人間の創作性」が認められず著作権登録自体ができないとされており、権利関係は法域によって扱いが異なる。実在のブランドロゴ・キャラクター・著名人に似た画像を生成・利用すると、著作権よりも商標権・パブリシティ権(肖像や氏名を無断で商業利用されない権利)の侵害リスクが先に問題になりやすい。詳しくは[生成AIの著作権リスクと実務での注意点](../part04-risk-security/copyright-risks-in-generative-ai.md)を参照
- **実在の人物の顔をそのまま生成することはブロックされる**: なりすまし・ディープフェイク対策のため、実在の著名人や、アップロードした顔写真に似せた画像の生成はポリシー上拒否されることが多い。社員やお客様の写真をイラスト化するような用途も、本人の同意なしに行うと肖像権上のトラブルになりかねないため注意する
- **文字は「精度が上がった」だけで「完璧」ではない**: GPT Image 2以降、GPT Image 2.5でも日本語を含む文字描写は改善が続いているが、看板の文言や数値など重要な文字情報は生成結果をそのまま資料に使わず、必ず目視確認する
- **新機能の一部はモバイルアプリ中心**: Sketchなど2.5で加わった機能の中には、2026年9月時点でモバイルアプリでの提供が先行し、PC版では使えない・使いにくいものがある。使いたい機能がある場合はプラットフォームを確認する
- **無料・Goプランの上限は情報源により差がある**: GPT Image 2.5が無料プランにも展開されたことで以前より使いやすくなったが、OpenAIは具体的な上限回数を公表しておらず、コミュニティの実測値も数枚〜20枚前後まで報告に幅がある。業務で日常的に使うならPlus以上への切り替えを検討する
- **「DALL-E」という名前はもう選べない**: 2026年5月12日にDALL-E 3のAPI提供が完全終了し、ChatGPT上でも画像生成はGPT Image系列に一本化された。古い記事や社内マニュアルに「DALL-E 3を選ぶ」という手順が残っていたら削除・書き換えが必要
- **API料金の解説は情報源によって食い違う**: GPT Image 2.5のAPI課金(トークン単価)について「旧モデルと同水準」「実質値上げ」の両方の解説がネット上に存在する。API連携のコスト試算をする場合は、必ずOpenAI公式のAPI Pricingページで当日時点の単価を確認してから見積もる
- **最終アセットとして使う前に確認を挟む**: ロゴ・パッケージデザインなど対外的に公開する最終物は、AI生成のたたき台をデザイナーが仕上げる、または商標調査を行う工程を挟むと安全

## 最初の一歩

ChatGPTのチャット欄に「(自分の業務でよく使う資料の種類)の表紙に使う画像を、テーマは◯◯、配色は◯◯で作って」と具体的な条件を入れて1枚生成し、続けて「もう少し明るく」のように会話で1回修正してみることで、反復編集の感覚をつかめる。

## 関連トピック

- [ChatGPTのプラン比較](chatgpt-plan-comparison.md)
- [ChatGPTのCanvas機能](chatgpt-canvas-feature.md)
- [生成AIの著作権リスクと実務での注意点](../part04-risk-security/copyright-risks-in-generative-ai.md)
- [生成AIによるプレゼン資料・ドキュメント作成の実務活用](../part12-business-practice/ai-presentation-and-document-creation.md)
- [Microsoft Copilotの基本](microsoft-copilot-basics.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [OpenAI APIの基本](../part09-api-development/openai-api-basics.md)

## 更新履歴

### 2026-09-13: GPT Image 2.5(ChatGPT Images 2.5)へのモデル更新を反映

- **内容**: 2026年9月8日公開の最新モデル「GPT Image 2.5」(ChatGPT Images 2.5)の情報に本文を全面更新。生成速度(Images 2.0比最大50%高速化)、被写体保持・局所編集精度の向上、解像度(最長辺3840px、両辺16の倍数)・アスペクト比(1:3〜3:1)・参照画像最大10枚の仕様、新機能のSketch(手描き参考画像、モバイル中心)・テンプレート・画像へのコメント・プロンプト共有を追記。無料プランを含む全プランへの展開を反映してプラン別上限表を見直し、API課金をトークン単価(`gpt-image-2.5-flare`/`gpt-image-2.5-sunburst`)ベースに更新し、API料金の解説が情報源で食い違う点を注意点に追加
- **出典**: [OpenAI: Introducing ChatGPT Images 2.5](https://openai.com/index/introducing-chatgpt-images-2-5/)、[TechRadar: ChatGPT Images 2.5 is out — I've been testing it for 24 hours](https://www.techradar.com/ai-platforms-assistants/chatgpt/chatgpt-images-2-5-is-out-ive-been-testing-it-for-24-hours-and-these-are-the-3-new-features-youll-actually-use)、[AndroidHeadlines: ChatGPT Images 2.5 Arrives with Sketch Support, Guided Templates, and Faster Speeds](https://www.androidheadlines.com/2026/09/openai-launches-chatgpt-images-2-5-sketch-editing-tools.html)、[eesel AI: ChatGPT Images 2.5: features, API models, and pricing](https://www.eesel.ai/blog/chatgpt-images-2-5)、[datastudios.org: OpenAI Launches ChatGPT Images 2.5](https://www.datastudios.org/post/openai-chatgpt-images-2-5-flare-sunburst-api-pricing)、[morphic.com: GPT Image 2.5 (ChatGPT Images 2.5): Specs and Access](https://morphic.com/resources/models/gpt-image-2-5)

### 2026-07-27: モデル世代・DALL-E完全終了・プラン別上限を最新化

- **内容**: 画像生成モデルの系譜を更新(2025年12月のGPT Image 1.5、2026年4月21日のGPT Image 2/ChatGPT Images 2.0、2026年5月12日のDALL-E 3完全提供終了)。解像度・アスペクト比の対応範囲(最大2K、3:1〜1:3)とThinkingモードの詳細を追記。プラン別の利用可否・上限表を見直し、Free/Goでの画像生成の可否について情報源間で記述が割れている点を明記。API(`gpt-image-2`)経由で使う場合のトークン課金の目安を新設。DALL-E系列がもう選べない旨を注意点に追加
- **出典**: [OpenAI: Introducing ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)、[Axios: Images in ChatGPT are getting a major update](https://www.axios.com/2026/04/21/chatgpt-images-major-update)、[TechCrunch: ChatGPT's new Images 2.0 model is surprisingly good at generating text](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/)、[Fello AI: OpenAI Launched GPT-Image-1.5](https://felloai.com/the-gpt-image-1-5-update-that-changes-everything/)、[Genra.ai: DALL-E Is Dead: OpenAI Retires Its Image Models on May 12](https://genra.ai/blog/dall-e-retired-may-2026-what-replaces-it)、[neurohive: ChatGPT Images 2.0 launches with reasoning, 2K resolution, and multilingual text](https://neurohive.io/en/news/chatgpt-images-2-0-openai-launches-image-generation-model-with-reasoning-2k-resolution-and-multilingual-text/)、[promptlibrary.space: AI Image API Pricing in 2026](https://www.promptlibrary.space/blog/ai-image-api-pricing-in-2026-cost-per-image-for-gpt-image-2-grok-imagine-nano-ba)、社内既存ページ[ChatGPTのプラン比較](chatgpt-plan-comparison.md)(2026-07-19時点でPlus以上限定と記載されており、Free/Goの扱いに関する情報源間の差異のクロスチェックに使用)

### 2026-07-06: 初版執筆
- **内容**: ChatGPTの画像生成機能(DALL-E 3からGPT Image 1・GPT Image 2/ChatGPT Images 2.0へのネイティブマルチモーダル化の経緯)、会話形式での反復編集、C2PAによる出所証明、プラン別の利用可否・上限、業務シーン別のコピペ用プロンプト例、Gemini/Copilot/Midjourneyとのツール横断比較、著作権・肖像権上の注意点を整理
- **出典**: [OpenAI: Introducing ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)、[TechCrunch: ChatGPT's new Images 2.0 model is surprisingly good at generating text](https://techcrunch.com/2026/04/21/chatgpts-new-images-2-0-model-is-surprisingly-good-at-generating-text/)、[OpenAI Help Center: C2PA in ChatGPT images](https://help.openai.com/ja-jp/articles/8912793-c2pa-in-chatgpt-images)、[OpenAI Developer Community: Image and Text Message Limits on ChatGPT Free account](https://community.openai.com/t/image-and-text-message-limits-on-chatgpt-free-account/950207)、[Microsoft: AI Art Improvements with DALL-E 3 | Microsoft Copilot](https://www.microsoft.com/en-us/microsoft-copilot/for-individuals/do-more-with-ai/ai-art-and-creativity/image-creator-improvements-dall-e-3)、[xda-developers: I compared ChatGPT Images 2.0 and Gemini Nano Banana, and one easily wins](https://www.xda-developers.com/compared-chatgpt-images-2-0-and-gemini-nano-banana/)、社内既存ページ[ChatGPTのプラン比較](chatgpt-plan-comparison.md)・[Google Geminiの基本](google-gemini-basics.md)(料金・プラン情報のクロスチェック)
