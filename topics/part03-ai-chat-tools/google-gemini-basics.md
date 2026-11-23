---
title: Google Geminiの基本
part: 3
chapter: 第5章 主要ツール各論
tags: [Gemini, Google, Gem, NotebookLM, Gemini Notebook, Gemini 4, Gemini Task]
created: 2026-07-04
updated: 2026-11-23
---

# Google Geminiの基本

## これは何か

Google Geminiは、ChatGPTと並ぶ代表的な生成AIだが、モデルの世代や周辺機能(Gem、NotebookLM改め「Gemini Notebook」、旧Gemini Spark改め「Task」)の呼び方がGoogle独自で分かりにくい。しかも2026年秋には、それまでの「Gemini 3.x Flash/Pro」という命名をやめて、元素名で呼ぶ**Gemini 4ファミリー(Hydrogen・Neon・Carbonなど)**へ一気に世代交代した。以前Geminiを触ったことがある人ほど「Proはどこへ行った?」と戸惑いやすい。ここではGeminiのラインナップと周辺機能の関係を、2026年11月時点の最新状態で整理する。

## 仕組み・背景

### Gemini 4ファミリー(2026年11月時点)

Gemini 4は2026年9月30日に最初のモデル「Argon」が発表され(当初は一部のサイバーセキュリティパートナー向け)、11月に入って上位・普及版・中位のモデルが相次いで投入された。Geminiアプリのモデル選択メニューでは、モデル名ではなく用途名で表示される点に注意する。

| モデル | 位置づけ | Geminiアプリでの表示と対象プラン | API価格(100万トークンあたり) |
|---|---|---|---|
| **Gemini 4 Hydrogen**(2026年11月12日) | 日常使い・エージェント処理向けの普及モデル。Flash系の後継にあたる | 「Everyday help」。有料プランはメニューから選べる。無料版は自動選択で振り分けられたときだけ使われる | 入力$1.50/出力$7.50、コンテキスト窓100万トークン |
| **Gemini 4 Neon**(2026年11月18日) | HydrogenとCarbonの中間。複雑なコーディング・分析・ナレッジワーク向けの主力 | 「Deeper analysis」。Google AI Pro・Ultra | 入力$3/出力$15、コンテキスト窓100万トークン |
| **Gemini 4 Carbon**(2026年11月10日にアプリ提供開始) | 最上位。最も難しい多段階の調査・コーディング・法務/金融などの高精度業務向け | 「Code & complex work」。Google AI Ultra | 入力$2/出力$10の導入価格(2026年11月30日まで)、以降は入力$4/出力$20 |
| Gemini 4 Argon(2026年9月30日発表) | ファミリー最初のモデル。コード・分析向け | 一時はPro以上で提供されたが、アプリではNeonに置き換えられた | Carbonと同じ価格体系 |

あわせて、長くフラッグシップだった**Gemini 3.1 ProはGeminiアプリから外れた**。次期モデルとして予告されていた「Gemini 3.5 Pro」は、Googleの広報担当者が「リリース計画を取りやめた」と説明しており(ロイター報道、2026年10月)、今後出てくることはない。ネット上の「3.5 Proの使い方」といった記事は古い情報として扱ってよい。

### 無料版は「自動選択」に一本化

2026年10月9日から、有料プランなしのGeminiアプリでは**手動でのモデル切り替えができなくなり、「Auto(自動選択)」だけ**になった。Googleの説明では、多くのプロンプトは最速のFlash-Liteで処理され、深い推論が必要なものだけが上位モデルに回される。自動選択をオフにすると、無料版ではすべての応答がFlash-Liteになる。あわせて推論の深さを「低・中・高」の3段階で選べるようになった(高いほど利用枠を多く消費する)。つまり**無料版で上位モデルを確実に使う方法はない**。精度が必要な業務で使うなら、有料プランが前提になる。

画像生成は「Nano Banana」シリーズという名称で展開されている。2026年2月26日にGeminiアプリの既定画像生成モデルが「Nano Banana 2」(Gemini 3.1 Flash Image、高速・低コスト重視)に切り替わり、より高精度な文字入れ・複雑な構図・実データに基づいた描写が必要な場合は上位モデルの「Nano Banana Pro」(Gemini 3 Pro Image、2026年6月一般提供)を使う、という2段構成になっている。両モデルとも一般提供が完了しており、動画ファイルやYouTube URLを入力してサムネイル・映画風ポスター・要約インフォグラフィックを生成する「動画→画像」機能が追加されたほか、Nano Banana 2で作った1枚絵をVeo 3.1に渡してその構図のまま動画化する、という画像・動画モデルの連携もできるようになっている。

Geminiアプリには自律実行エージェントも組み込まれている。2026年5月に「Gemini Spark」として発表された機能は、10月に**「Task」へ改称されて通常のチャット画面に統合**され、入力欄付近の「Chat/Task」の切り替えで呼び出す形になった。Gmail・Googleカレンダー・ドキュメント・スプレッドシートなどを横断して作業を進め、送信・購入などの前には必ず確認を求める。Google公式ヘルプでは、日本・米国など6か国では有料プランなしでも使えると案内されている(上位プランほど利用上限が大きい)。詳細は[Gemini Task(旧Gemini Spark)の基本](gemini-spark-basics.md)を参照。

モデル・製品名の世代交代は非常に速く、2026年7月には音声・文書系ツールの「NotebookLM」が「Gemini Notebook」に、10月には「Gemini Spark」が「Task」に改称されるなど、名前自体が変わることもある。記事や社内資料に具体的なモデル名・製品名を書く場合は、必ず[Google公式のGeminiリリースノート](https://gemini.google/release-notes/)で最新の呼称を確認することを推奨する。

## 使いどころ・使い分け

| 用途 | 向いているモデル・機能 |
|---|---|
| 簡単な質問・チャット | 自動選択(無料版はこれのみ)/有料版は「Everyday help」(Gemini 4 Hydrogen) |
| 複雑な分析・資料作成・コーディング | 「Deeper analysis」(Gemini 4 Neon、Pro以上) |
| 最難関の調査・高精度が求められる専門業務 | 「Code & complex work」(Gemini 4 Carbon、Ultra限定) |
| 高速・低コストの画像生成 | Nano Banana 2 |
| 高精度な文字入れ・複雑な構図の画像生成 | Nano Banana Pro |
| メール・カレンダー・資料をまたいだ作業を丸ごと任せたい | Task(旧Gemini Spark。日本では有料プランなしでも利用可) |
| 手元の資料だけを根拠に正確に調べたい | Gemini Notebook(旧NotebookLM) |
| 幅広い一般知識も使って発想を広げたい | Geminiアプリ本体 |

GeminiアプリとGemini Notebook(旧NotebookLM)の使い分けが特によく混同される。**Geminiアプリは「外の世界の知識」も使う汎用AI**であるのに対し、**Gemini Notebookは「ユーザーが渡した資料だけ」を根拠に回答するリサーチ特化ツール**という違いがある。手元の資料から正確に情報を引き出したいならGemini Notebook、既存資料を踏まえつつ新しいアイデアを広げたいならGeminiアプリ、という選び方になる。なお2026年4月以降はGeminiアプリのサイドバーに「Notebooks」セクションが新設され、Geminiアプリを離れずにノートブックの作成・参照ができるようになっているため、両者はほぼシームレスに行き来できる。

## 実務での使い方

### 個人向けプラン(2026年11月時点の目安)

月額は2026年5〜6月に公表された日本の価格(Plusは6月の値下げ後)、各プランで使えるモデルは2026年11月時点のGoogle公式プランページの記載にもとづく。

| プラン | 月額目安(日本) | 特徴 |
|---|---|---|
| 無料 | ¥0 | モデルは自動選択のみ(多くはFlash-Lite)。Gemsは回数制限付きで作成・利用可。Task(旧Spark)も日本では利用可 |
| Google AI Plus | ¥725(2026年6月に¥1,200から値下げ) | ストレージ400GB。Gemini 4 Hydrogenをメニューから選択可、Deep Research、Taskの利用枠拡大 |
| Google AI Pro | ¥2,900 | ストレージ5TB。GeminiアプリでGemini 4 Neonが使える、Deep Research・Taskの利用枠拡大、エージェント型IDE「Antigravity」など |
| Google AI Ultra(5x) | ¥14,500(月払いのみ) | ストレージ20TB。Gemini 4 Carbon、Neonの上限拡大、Taskの上限引き上げ |
| Google AI Ultra(20x) | ¥32,000 | ストレージ30TB。5xよりさらに大きな利用上限 |

Ultraは以前は単一プラン(月額36,400円)だったが、2026年5月にエントリー帯(5x)と最上位帯(20x)の2階層に再編され、最上位帯はむしろ値下げされた。料金は今後も変更される可能性が高いため、契約前に必ず[Google公式のプランページ](https://one.google.com/about/google-ai-plans/)で最新の金額を確認すること。なお、Gemini APIを自社システムやノーコードツールから従量課金で呼び出す場合の料金は、これらの個人向けサブスクとは別契約になる。詳しくは[Google Gemini APIの基本](../part09-api-development/google-gemini-api-basics.md)を参照。

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

- **モデル名・製品名・料金の変更頻度が非常に高い**: 2026年夏はFlash系が6週間で3回更新され、秋にはGemini 4ファミリーへ命名ごと切り替わった。本ページの数値・名称は目安に過ぎない。契約前・執筆前に必ず公式サイトで確認すること。
- **「Pro」はプラン名であってモデル名ではなくなった**: 以前は「Gemini 3.1 Pro」というモデルがあったため、「Proプラン=Proモデル」と覚えていた人が多い。いまはGoogle AI Proプランで使える上位モデルはGemini 4 Neonで、「Gemini 3.5 Pro」は出ないことが決まっている。社内資料のモデル名は書き換えが必要。
- **アプリの表示名とモデル名が違う**: モデル選択メニューには「Everyday help」「Deeper analysis」のような用途名が並ぶ。マニュアルを作るときは「Deeper analysis(Gemini 4 Neon)」のように両方を併記すると、表示が変わっても追いやすい。
- **無料版で上位モデルを指定することはできない**: 2026年10月9日以降、無料版は自動選択のみで、多くの質問はFlash-Liteで処理される。「無料版で試したら精度がいまひとつだった」という評価は、有料版の実力とは別物と考える。
- **「NotebookLM」「Gemini Spark」の名前はもう使われていない**: それぞれ「Gemini Notebook」(2026年7月〜)、「Task」(2026年10月〜)に改称された。過去の資料や検索結果には旧名が多く残っているため、社内資料では新旧両方を併記しておくと親切。
- **API料金にも期限付きの導入価格がある**: Gemini 4 Carbon・Argonは2026年11月30日までの導入価格が終わると単価が2倍になる。API経由で業務システムに組み込む場合は、導入価格前提で予算を組まない。

## 最初の一歩

手元にある社内マニュアルやプロジェクト資料を1つGemini Notebook(旧NotebookLM)に読み込ませ、内容についての質問を投げて、根拠付きで答えが返ってくる感覚を試してみる。

## 関連トピック

- [ChatGPTのプラン比較](../part03-ai-chat-tools/chatgpt-plan-comparison.md)
- [Gemini Task(旧Gemini Spark)の基本](gemini-spark-basics.md)
- [Google Gemini APIの基本](../part09-api-development/google-gemini-api-basics.md)

## 更新履歴

### 2026-11-23: Google AI Plusの月額の誤りを訂正
- **内容**: 同日の改訂でGoogle AI Plusの月額を¥1,200としていたが、2026年6月に¥725へ値下げされている(既存ユーザーも次回更新から適用)ため訂正
- **出典**: [ケータイ Watch: 「Google AI Plus」が月額725円に値下げ、ストレージは400GBに倍増](https://k-tai.watch.impress.co.jp/docs/news/2115643.html)

### 2026-11-23: Gemini 4ファミリーへの世代交代・無料版の自動選択化・Task改称を反映して最新化
- **内容**: モデル解説をGemini 3.x系からGemini 4ファミリー(Hydrogen・Neon・Carbon、Argon)に全面的に書き換え、Geminiアプリでの表示名・対象プラン・API価格を一覧化。Gemini 3.1 Proのアプリからの撤去とGemini 3.5 Proのリリース中止、2026年10月9日からの無料版の自動選択一本化(多くはFlash-Lite)を追記。Gemini SparkのTaskへの改称と日本での有料プランなし提供を反映。プラン表をGoogle公式プランページの記載に合わせて更新。陳腐化した3.6/3.7/3.8 Flash・Deep Thinkの記述を削除
- **出典**: [Google公式ブログ: Introducing Gemini 4 Hydrogen](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/)、[Google公式ブログ: Gemini 4 Neon を発表](https://blog.google/intl/ja-jp/company-news/technology/introducing-gemini-4-neon/)、[9to5Google: Google launches Gemini 4 Neon(2026年11月18日)](https://9to5google.com/2026/11/18/gemini-4-neon-announcement/)、[9to5Google: Gemini 4 Carbon rolling out to Gemini app for AI Ultra(2026年11月10日)](https://9to5google.com/2026/11/10/gemini-app-4-carbon/)、[Khaleej Times(ロイター配信): Google announces Gemini 4 flagship AI model after months of delays](https://www.khaleejtimes.com/business/google-announces-gemini-4-flagship-ai-model-after-months-of-delays-2)、[9to5Google: Gemini free users move to Auto(2026年10月9日)](https://9to5google.com/2026/10/09/gemini-auto-free-users/)、[Google One: Google AI プラン](https://one.google.com/intl/ja_jp/about/google-ai-plans/)、[PC Watch: Google AI Ultra 5x新設とUltraの値下げ](https://pc.watch.impress.co.jp/docs/news/2110129.html)、[Gemini Apps ヘルプ: Manage your tasks & workflows](https://support.google.com/gemini/answer/17094507?hl=en)

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
