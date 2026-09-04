---
title: Google Geminiの基本
part: 3
chapter: 第5章 主要ツール各論
tags: [Gemini, Google, Gem, NotebookLM, Gemini Notebook]
created: 2026-07-04
updated: 2026-09-04
---

# Google Geminiの基本

## これは何か

Google Geminiは、ChatGPTと並ぶ代表的な生成AIだが、モデルの世代(Flash/Pro等)や周辺機能(Gem、NotebookLM改め「Gemini Notebook」)の呼び方がGoogle独自で分かりにくい。しかもFlash系モデルだけでも2026年7月21日(3.6)→8月13日(3.7)→9月2日(3.8)と、Google自身が「6週間で3回目のFlash更新」と語るほどのペースで刷新されており、他社よりモデルの入れ替わりが速い。ChatGPTを使い慣れた人はもちろん、以前Geminiを触ったことがある人でも「あれ、前と名前が違う」と戸惑いやすい。ここではGeminiのラインナップと周辺機能の関係を、2026年9月時点の最新状態で整理する。

## 仕組み・背景

2026年9月時点でのGeminiのモデルラインナップは「Gemini 3」世代が中心で、性能・速度のバランスで複数段階に分かれている。

- **Gemini 3.5 Flash-Lite**: 低遅延・高頻度処理向けの最軽量モデル
- **Gemini 3.6 Flash**(2026年7月21日公開): 無料版の既定モデル。従来の3.5 Flashより出力トークンを最大17%削減しつつ性能を底上げした汎用モデルで、2026年9月時点でも無料版ではこれが既定のまま
- **Gemini 3.7 Flash**(2026年8月13日一般提供): 3.6 Flashをコーディング・エージェント用途に寄せた改良版。API(Google AI Studio)や自律実行エージェント「Gemini Spark」経由での利用が中心だった
- **Gemini 3.8 Flash**(2026年9月2日一般提供): 3.7 Flashからさらにソフトウェア開発・エージェント処理・多段推論を強化した最新のワークホースモデル。入出力とも1Mトークンのコンテキスト窓(出力上限6.4万トークン)を持ち、API上の価格は3.7 Flashと同水準(2026年内は入力$0.75/出力$3.75の導入価格、2027年1月から2倍に改定予定)。Google AI Pro・Ultra契約者はGeminiアプリのチャットからも直接利用できるが、無料版では引き続き3.6 Flashが既定のまま
- **Gemini 3.8 Flash Cyber**: サイバーセキュリティの脆弱性発見・修正に特化したモデル。旧「3.5 Flash Cyber」を置き換える形で登場し、新設の「Fairwind Program」を通じた信頼できるテスター向け限定提供にとどまる
- **Gemini 3.1 Pro**: 現行のフラッグシップモデル(2026年2月公開)。複雑なタスク・専門用途向けで、応答時に「思考レベル」をLOW/MEDIUM/HIGHの3段階から選べ、HIGHにすると簡易版の並列推論モード(通称「Deep Think Mini」)として振る舞う
- **Deep Think**: Google AI Ultra限定の最上位モード。Gemini 3.1 Proをベースにした本格的な並列推論で、国際数学オリンピック(IMO)金メダル相当のスコアを記録するなど、最も難しい調査・エンジニアリング用途向け

次期フラッグシップの「Gemini 3.5 Pro」は2026年5月のGoogle I/Oで予告されたものの、コーディング性能が社内基準に届かなかったことを理由に一般提供が繰り返し延期されており、2026年9月2日時点で6月・7月中旬・8月上旬の3回の目標時期をいずれも見送ったまま、モデルID・価格・提供時期のいずれも未公表の段階が続いている。さらに2026年7月21日には次々世代「Gemini 4」の事前学習を開始したことも公表されたが、2026年9月2日時点でもAPI・Vertex AIのモデル一覧に「gemini-4」の項目はなく、公開ドキュメントも存在しない(海外メディアは過去の投入間隔から「2026年11〜12月頃」と予想するにとどまる)。「Gemini 3.5 Proがもう使える」「Gemini 4が出た」といった記事も出回っているが、Google公式のアナウンスが出るまでは未確定情報として扱うのが安全。

画像生成は「Nano Banana」シリーズという名称で展開されている。2026年2月26日にGeminiアプリの既定画像生成モデルが「Nano Banana 2」(Gemini 3.1 Flash Image、高速・低コスト重視)に切り替わり、より高精度な文字入れ・複雑な構図・実データに基づいた描写が必要な場合は上位モデルの「Nano Banana Pro」(Gemini 3 Pro Image、2026年6月一般提供)を使う、という2段構成になっている。両モデルとも一般提供が完了しており、動画ファイルやYouTube URLを入力してサムネイル・映画風ポスター・要約インフォグラフィックを生成する「動画→画像」機能が追加されたほか、Nano Banana 2で作った1枚絵をVeo 3.1に渡してその構図のまま動画化する、という画像・動画モデルの連携もできるようになっている。

Geminiアプリ本体にも大きな新機能が加わった。「Gemini Spark」は、Gmail・Googleカレンダー・ドキュメント・スプレッドシートなどを横断してタスクを自律的に進める常駐エージェントで、当初はGoogle AI Ultra限定だったが、2026年7月29日にGoogle AI Pro(月額2,900円、米国から順次)にも提供が拡大された。以降も改良が続いており、処理速度が旧版比50%以上向上したほか、Googleドキュメント・スプレッドシート・スライドの共有ファイルに直接画像を追加・編集できるようになった。2026年8月にはGemini Liveにも「Personal Intelligence」「Daily Brief」といった新機能が加わり、話しかけるだけで1日の予定確認や受信トレイの整理をハンズフリーで任せられるようになっている。詳細は[Gemini Spark(Google)の基本](gemini-spark-basics.md)を参照。

モデル・製品名の世代交代は非常に速く、2026年7月には音声・文書系ツールの「NotebookLM」が「Gemini Notebook」に改称されるなど、名前自体が変わることもある。記事や社内資料に具体的なモデル名・製品名を書く場合は、必ず[Google公式のGeminiリリースノート](https://gemini.google/release-notes/)で最新の呼称を確認することを推奨する。

## 使いどころ・使い分け

| 用途 | 向いているモデル・機能 |
|---|---|
| 簡単な質問・チャット | Gemini 3.6 Flash(無料版の既定モデル) |
| 複雑な分析・専門的なタスク | Gemini 3.1 Pro |
| 最難関の調査・研究・エンジニアリング | Deep Think(Ultra限定) |
| コーディング・自律的なエージェント処理 | Gemini 3.8 Flash(Pro/Ultra契約者はアプリからも、それ以外はAPI・Gemini Spark経由) |
| 大量・高頻度の軽い処理 | Gemini 3.5 Flash-Lite |
| 高速・低コストの画像生成 | Nano Banana 2 |
| 高精度な文字入れ・複雑な構図の画像生成 | Nano Banana Pro |
| メール・カレンダー・資料をまたいだ作業を丸ごと任せたい | Gemini Spark(Pro以上) |
| 手元の資料だけを根拠に正確に調べたい | Gemini Notebook(旧NotebookLM) |
| 幅広い一般知識も使って発想を広げたい | Geminiアプリ本体 |

GeminiアプリとGemini Notebook(旧NotebookLM)の使い分けが特によく混同される。**Geminiアプリは「外の世界の知識」も使う汎用AI**であるのに対し、**Gemini Notebookは「ユーザーが渡した資料だけ」を根拠に回答するリサーチ特化ツール**という違いがある。手元の資料から正確に情報を引き出したいならGemini Notebook、既存資料を踏まえつつ新しいアイデアを広げたいならGeminiアプリ、という選び方になる。なお2026年4月以降はGeminiアプリのサイドバーに「Notebooks」セクションが新設され、Geminiアプリを離れずにノートブックの作成・参照ができるようになっているため、両者はほぼシームレスに行き来できる。

## 実務での使い方

### 個人向けプラン(2026年9月時点の目安)

2026年5月のGoogle I/Oで再編されたプラン体系は、9月時点でも同水準の価格で続いている。以下は執筆時点の目安。

| プラン | 月額目安(日本) | 特徴 |
|---|---|---|
| 無料 | ¥0 | Gemini 3.6 Flashが既定モデル。Gemsも無料版で作成・利用可(回数制限あり)。Deep Researchは月5回程度まで、画像生成は1日あたり上限あり |
| Google AI Plus | ¥725 | 無料版の2倍程度の利用枠、コンテキスト窓12.8万トークン、Omni Flashによる動画生成、Gemini Notebookの利用枠拡大など |
| Google AI Pro | ¥2,900 | Gemini 3.1 Pro、Geminiアプリのチャットからも使えるGemini 3.8 Flash、Nano Banana Pro、Veo 3.1 Fast、Deep Research(1日20回目安)、Gemini Notebookの利用枠拡大、自律実行エージェント「Gemini Spark」(2026年7月29日提供開始、以降も高速化・機能拡張が継続中)、コーディングエージェント「Jules」、エージェント型IDE「Antigravity」などフロンティア機能一式 |
| Google AI Ultra(5x) | ¥14,500 | ストレージ20TB。Proの5倍の利用量上限、Deep Research 1日120回目安 |
| Google AI Ultra(20x) | ¥32,000 | ストレージ30TB。Proの20倍の利用量上限、Deep Think、Veo 3.1のフル機能、Project Mariner(エージェント型ブラウザ操作)、YouTube Premium同梱など最上位機能 |

Ultraは以前は単一プランだったが、I/O 2026でエントリー帯(5x)と最上位帯(20x)の2階層に再編され、最上位帯はむしろ値下げされた。料金は今後も変更される可能性が高いため、契約前に必ず[Google公式のプランページ](https://one.google.com/about/google-ai-plans/)で最新の金額を確認すること。なお、Gemini APIを自社システムやノーコードツールから従量課金で呼び出す場合の料金は、これらの個人向けサブスクとは別契約になる。詳しくは[Google Gemini APIの基本](../part09-api-development/google-gemini-api-basics.md)を参照。

### Gem機能(ChatGPTのGPTsに相当)

Gemは「どんなトピックにも対応できる自分専用のカスタムAI」で、毎回の会話で前提説明を繰り返す手間を省ける。2026年時点では無料版でも基本的なGem作成・利用ができるが、利用回数や使えるモデルの性能は有料プランほど広くなる。

作成手順の目安:
1. gemini.google.com を開き、左側メニューの「Gemを表示」をクリック
2. 「Gemを作成」を選択し、名前を付ける
3. 指示欄に、ペルソナ(役割・口調)・タスク(してほしいこと)・コンテキスト(背景情報)・出力形式を書く(「Geminiを使用」ボタンで簡単な目的文を詳しい指示文に自動リライトさせることも可能)
4. 右側のプレビューで確認しながら「保存」

作成したGemはGeminiモバイルアプリやGoogle Workspaceのサイドパネルからも呼び出せる。

### Gemini Notebook(旧NotebookLM)

2026年7月16日、Googleは長らく「NotebookLM」の名称で提供してきたリサーチツールを「Gemini Notebook」に改称した。スタンドアロンのツールとして存続しつつ、Geminiアプリ・Google検索(AIモード)との連携が強化されている。同時に、各ノートブックに専用の「セキュアなクラウドコンピュータ」が付与され、アップロードした資料をもとにコードを書いて実行し、複雑なデータ分析まで行えるようになった。手元の資料を読み込ませて質問すると、根拠となる該当箇所を示しながら回答してくれる点は従来どおり。URL・料金プランは改称の前後で変わっていない。

利用上限の仕組みも2026年9月2日から変更されている。従来は「動画解説」「音声解説」「インフォグラフィック」など機能ごとに1日単位で上限が決まっていたが、Geminiアプリと同じ「コンピューティング量に基づく上限」に一本化され、上限のリセット間隔も24時間から5時間へ大幅に短縮された。あわせて、動画解説のように負荷の高いタスクの実行時間を指定できるスケジュール機能も追加されている。

### 法人向け(Google Workspace with Gemini)

個人向けプランとは別に、法人向けは「Google Workspace with Gemini」という名称で提供されている。GmailやGoogleドキュメント、スプレッドシート、Meetなど業務ツール群にGeminiが統合されており、Business Starterプラン(月額目安800〜950円/ユーザー)からも標準で利用できる(上位プランほど利用できる範囲が広がる)。ただしBusiness Starterで使えるのはGmailのサイドパネルでの文章作成支援など限定的な範囲にとどまり、大量の資料を読み込ませる用途には向かない。Microsoft 365のCopilotのように追加課金が必要な構成ではなく、対象プランであれば追加費用なしでGemini機能が使える点が特徴。

## 注意点・よくある誤解

- **モデル名・製品名・料金の変更頻度が非常に高い**: Flash系だけでも2026年7月21日(3.6 Flash)→8月13日(3.7 Flash)→9月2日(3.8 Flash)と6週間で3回更新されており、本ページの数値・名称は目安に過ぎない。契約前・執筆前に必ず公式サイトで確認すること。
- **「NotebookLM」の名前はもう存在しない**: 2026年7月16日以降、公式には「Gemini Notebook」に統一されている。過去の資料や検索結果には旧名の「NotebookLM」が数多く残っているため、社内資料を書く際はどちらの名前でも通じるよう両方併記しておくと親切。
- **「Gemini 3.5 Pro」「Gemini 4」を混同しない**: どちらも未リリースだが状況は異なる。3.5 Proは2026年6月・7月中旬・8月上旬と3回投入目標を逃した末に9月時点でもモデルID・価格とも未公表なのに対し、Gemini 4は2026年7月に事前学習を開始した段階に過ぎず、リリース時期の見込みすら公表されていない。ブログ記事の中には未確定の噂を確定情報のように書いているものもあるため注意。
- **無料版の既定モデルは変わっていない**: 3.7 Flash・3.8 Flashが登場しても、無料版のGeminiアプリで使えるのは引き続きGemini 3.6 Flash。3.8 FlashをGeminiアプリのチャットから直接使えるのはGoogle AI Pro・Ultra契約者のみで、それ以外はAPIやGemini Spark経由での利用が中心になる。「最新モデルが使えない」と感じたら、まず自分の契約プランと提供経路を確認する。
- **無料版でGemが使えるかどうかは要確認**: 無料版でも基本的なGem作成・利用は可能になったが、利用回数や使えるモデルの性能には上限がある。実際の挙動は公式ヘルプで確認するのが確実。

## 最初の一歩

手元にある社内マニュアルやプロジェクト資料を1つGemini Notebook(旧NotebookLM)に読み込ませ、内容についての質問を投げて、根拠付きで答えが返ってくる感覚を試してみる。

## 関連トピック

- [ChatGPTのプラン比較](../part03-ai-chat-tools/chatgpt-plan-comparison.md)
- [Gemini Spark(Google)の基本](gemini-spark-basics.md)
- [Google Gemini APIの基本](../part09-api-development/google-gemini-api-basics.md)

## 更新履歴

### 2026-09-04: モデルラインナップとGemini Notebookの利用上限を2026年9月時点に更新
- **内容**: Flash系モデルの最新版として2026年9月2日一般提供の「Gemini 3.8 Flash」(コンテキスト窓1Mトークン、API価格は3.7 Flashと同水準、Google AI Pro/Ultra契約者はGeminiアプリからも利用可)と「Gemini 3.8 Flash Cyber」(Fairwind Programの信頼できるテスター向け限定提供)を反映し、無料版の既定モデルは引き続きGemini 3.6 Flashであることを明記。Gemini 3.5 Proが6月・7月中旬・8月上旬の3回投入目標を逃したまま未公表が続いていること、Gemini 4はAPI・Vertex AIにまだ項目が存在せず海外報道は2026年11〜12月頃の投入を予想するにとどまることを追記。Nano Banana 2/Proが一般提供完了し「動画→画像」生成やVeo 3.1との連携が可能になったこと、Gemini Sparkの高速化・Docs/Sheets/Slidesへの画像編集対応・Gemini Liveの新機能(Personal Intelligence/Daily Brief)、Gemini Notebookの利用上限が2026年9月2日から「コンピューティング量ベース・5時間ごとリセット」に変更されたことを反映
- **出典**: [Google公式ブログ: Introducing Gemini 3.8 Flash and 3.8 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/3-8-flash-and-3-8-flash-cyber/)、[9to5google: Gemini 3.8 Flash rolling out three weeks after last release](https://9to5google.com/2026/09/02/gemini-3-8-flash-launch/)、[The Register: With Gemini 3.8 Flash, Google reminds everyone it's still in the race](https://www.theregister.com/ai-and-ml/2026/09/02/with-gemini-38-flash-google-reminds-everyone-its-still-in-the-race/5294049)、[codersera.com: Gemini 3.5 Pro Release Date: Still Unreleased (Aug 2026)](https://codersera.com/blog/gemini-3-5-pro-launch-guide-2026/)、[emergent.sh: Gemini 4 Release Date](https://emergent.sh/news/gemini-4-release-date)、[9to5google: Google's agentic AI Gemini Spark expands to AI Pro/Ultra](https://chromeunboxed.com/googles-agentic-ai-gemini-spark-is-now-available-on-the-20-pro-tier-in-the-us/)、[9to5google: Gemini Spark Workspace upgrades](https://9to5google.com/2026/07/15/gemini-spark-workspace-upgrades/)、[Google公式ブログ: Nano Banana Pro (Gemini 3 Pro Image)](https://blog.google/innovation-and-ai/products/nano-banana-pro/)、[窓の杜: 「Gemini Notebook」の利用上限が変更、5時間ごとにリセット](https://forest.watch.impress.co.jp/docs/news/2137172.html)、[eesel AI: Google Gemini 3 pricing 2026](https://www.eesel.ai/blog/google-gemini-3-pricing)
- **注記**: Google公式サイト(blog.google、one.google.com、gemini.google.com)は今回もネットワーク制約により直接アクセスできず、複数の第三者情報の突き合わせに基づく目安。特に料金・回数上限・提供範囲は変動が速いため、正確な最新値は公式サイトで要確認

### 2026-08-15: モデルラインナップ・Gemini Sparkの拡大・Gemini 3.5 Pro/Gemini 4の状況を最新化
- **内容**: Flash系モデルをGemini 3.6 Flash(2026年7月21日公開)・Gemini 3.7 Flash(2026年8月13日一般提供、API/Spark経由が中心)・Gemini 3.5 Flash Cyber(限定提供)へ更新、Gemini 3.5 Proが2026年8月時点でもパートナーテスト段階にとどまることと、2026年7月21日公表のGemini 4事前学習開始(未発表段階)を追記、自律実行エージェント「Gemini Spark」が2026年7月29日にGoogle AI Proへ提供拡大されたことを反映し独立ページへの相互リンクを追加、Gemini Notebook・Workspace・プラン料金の記述を2026年8月時点の状態に更新
- **出典**: [techno-edge.net: Gemini 3.7 Flash発表](https://www.techno-edge.net/article/2026/08/14/5392.html)、[Google公式ブログ: Gemini 3.7 Flashを発表](https://blog.google/intl/ja-jp/company-news/technology/gemini-37-flash/)、[9to5google: Gemini 3.6 Flash launch](https://9to5google.com/2026/07/21/gemini-3-6-flash-launch/)、[TechCrunch: Google releases three new Gemini models — but no 3.5 Pro](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)、[cryptorank.io: Gemini 3.6 Flash / 3.5 Pro delay](https://cryptorank.io/news/feed/85004-google-deepmind-gemini-models-3-6-flash-3-5-pro-delay)、[aidaim.co.jp: Gemini SparkがGoogle AI Proへ拡大](https://aidaim.co.jp/gemini-spark/)
- **注記**: Google公式サイト(gemini.google.com、one.google.com)への直接アクセスができず複数の第三者情報の突き合わせに基づく目安。特に料金・回数上限・提供範囲は変動が速いため、正確な最新値は公式サイトで要確認

### 2026-07-19: プラン体系・モデル名・NotebookLM改称を最新化
- **内容**: 2026年5月のGoogle I/OによるGoogle AI Plus/Pro/Ultraのプラン再編と価格(Ultraの5x/20x2階層化、Plusの値下げ、Proのストレージ増量)、モデルラインナップをGemini 3.1 Pro/Deep Think/Gemini 3.5 Pro(未リリース)中心に更新、画像生成をNano Banana 2/Nano Banana Proの2段構成に修正、2026年7月16日のNotebookLM→「Gemini Notebook」への改称を反映
- **出典**: [9to5google: NotebookLM is now Gemini Notebook](https://9to5google.com/2026/07/16/notebooklm-gemini-notebook/)、[窓の杜: 「NotebookLM」が「Gemini Notebook」へ改称](https://forest.watch.impress.co.jp/docs/news/2125948.html)、[9to5google: Google AI Plus price drop](https://9to5google.com/2026/06/08/google-ai-plus-price-drop/)、[PC Watch: Google AI Ultraに月額1万4,500円の新プラン](https://pc.watch.impress.co.jp/docs/news/2110129.html)、[Google DeepMind: Gemini 3.1 Pro](https://deepmind.google/models/gemini/pro/)、[Google Blog: Nano Banana Pro (Gemini 3 Pro Image)](https://blog.google/technology/ai/nano-banana-pro/)、[romptn Magazine: Gemini Deep Researchの回数制限](https://romptn.com/article/97411)
- **注記**: Google公式サイト(gemini.google.com、one.google.com)への直接アクセスができず複数の第三者情報の突き合わせに基づく目安。特に料金・ストレージ容量・回数上限は変動が速いため、正確な最新値は公式サイトで要確認

### 2026-07-04: 初版執筆
- **内容**: Geminiのモデルラインナップ(Flash-Lite/Flash/Pro)、個人向け・法人向けプランの概要、Gem機能の作成手順、NotebookLMとの使い分けを整理
- **出典**: [Google Blog: Gemini Omni Flash / Nano Banana 2発表](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)、[Google公式ヘルプ: カスタムGem作成のヒント](https://support.google.com/gemini/answer/15235603?hl=ja)、[マネーフォワード クラウド: Google Workspace with Gemini解説](https://biz.moneyforward.com/ai/basic/863/)、[アイスマイリー: GeminiとNotebookLMの違い](https://aismiley.co.jp/ai_news/gemini-notebooklm/)
- **注記**: Google公式サイトへの直接アクセスができなかったため、料金・モデル名の一部は複数の第三者情報の突き合わせに基づく目安。正確な最新値は公式サイトで要確認
