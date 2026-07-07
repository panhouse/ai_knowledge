---
title: "主要AIチャットツールのエージェント機能・スケジュールタスク比較(ChatGPT Agent/Tasks・Gemini Spark・Copilot Cowork・Claude Cowork)"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [AIエージェント, スケジュールタスク, ChatGPT Agent, Gemini Spark, Copilot Cowork, Claude Cowork, ツール比較]
created: 2026-07-07
updated: 2026-07-07
---

# 主要AIチャットツールのエージェント機能・スケジュールタスク比較(ChatGPT Agent/Tasks・Gemini Spark・Copilot Cowork・Claude Cowork)

## これは何か

ChatGPT・Gemini・Microsoft Copilot・Claudeは、いずれも2025〜2026年にかけて「自律的にブラウザ・PCを操作して複数ステップの作業をやり切る**エージェントモード**」と「決まった周期で同じ依頼を自動的に繰り返す**スケジュールタスク**」の2種類の自律実行系機能を追加した。ところが各社の呼び方がまったく異なり(ChatGPT Agent、Gemini Spark、Copilot Cowork、Claude Cowork……)、しかも「Cowork」のようにベンダーをまたいで同じ名前が使われているケースまであるため、「うちの会社はGeminiなのに、ネット記事に出てくるChatGPT Agentの話がそのまま当てはまるのか」が非常に分かりにくい。本ページは、4社の機能名・対応プラン・できること/できないことを1枚の対応表に整理し、「自分が使っているツールでは何をどう呼ぶか」をすぐ調べられるようにする。

なお、個々のツールの詳しい仕組み・確認プロンプト・料金の内訳は各社の専用ページ([ChatGPTのエージェント機能とTasks](./chatgpt-agent-mode-feature.md)など)に譲り、本ページはツール横断の「見取り図」に徹する。

## 仕組み・背景

### 「エージェントモード」と「スケジュールタスク」は別物

各社とも、次の2つを別の機能として用意している(名前の付け方は違うが、構造はほぼ共通)。

- **エージェントモード(自律実行)**: 仮想ブラウザ・PC環境の中でAIが実際にクリック・入力・ファイル作成まで行い、目標(ゴール)を渡すと最後までやり切る。1回の依頼で数分〜数十分かかる、重量級の機能
- **スケジュールタスク(定期実行)**: 「毎週月曜9時に◯◯して」のように、決まった日時・周期でプロンプトを自動的に再実行するだけの軽量な機能。多くはブラウザ操作を伴わず、Web検索程度の範囲で完結する

この2つが分かれているのは技術的な理由がある。仮想ブラウザ・PC環境を都度立ち上げるエージェントモードは計算コストが高く、確認プロンプト(後戻りしにくい操作の前に人間の許可を求める仕組み)などの安全機構も必要になる。一方スケジュールタスクは「同じ質問を時間差で投げ直す」だけなので軽く、無人で定期実行しても事故のリスクが小さい。そのため各社ともUI上も別の入り口・別のプラン条件になっていることが多い。

### 各社の機能の成り立ち(2026年7月時点)

- **OpenAI**: 2025年1月の「Operator」(ブラウザ操作)と「Deep Research」(調査)を2025年7月に統合し「**ChatGPT Agent**」に一本化。スケジュール実行は「**Tasks**」という別機能([詳細](./chatgpt-agent-mode-feature.md)参照)
- **Google**: 2025年6月に軽量な「**Scheduled actions(スケジュール機能)**」をGemini appに追加。その約1年後、2026年5月のGoogle I/Oで、Gmail・カレンダー・Driveなどに24時間365日常駐して複数ステップの作業を代行する重量級エージェント「**Gemini Spark**」を発表(旧Project Mariner系のブラウザ操作機能を統合)([Google I/O 2026関連報道](https://www.techtimes.com/articles/317144/20260525/gemini-spark-googles-24-7-cloud-ai-agent-now-executes-tasks-third-party-apps.htm))
- **Microsoft**: Microsoft 365 Copilotに組み込まれた調査特化の「**Researcher**」(OpenAIのdeep researchモデルを利用)、データ分析特化の「**Analyst**」(推論モデルによるライブPython実行)が2025年半ばに一般提供。2026年2月にこの2つを定期実行できる「**Copilot Tasks**」タブがプレビュー開始、2026年6月16日には、より本格的な長時間・複数ツールの自律作業を行う「**Copilot Cowork**」が一般提供開始(要Microsoft 365 Copilotライセンス)。個人のWeb閲覧を代行する機能は「**Copilot Actions(Browse with Copilot)**」、企業のIT部門が許可したサイトに限定して動く法人版は「**Agent Mode for Edge for Business**」という別の名称になっている
- **Anthropic**: 開発者向けにはターミナルで動く「Claude Code」とその上の「**Claude Agent SDK**」「Computer Use(画面操作API)」が先行。2026年2月、非エンジニアでも使えるデスクトップ版の自律実行エージェント「**Claude Cowork**」をリリースし、同月末にはCowork内で使える軽量な「**スケジュールタスク**」機能も追加。2026年4月には、クラウド上で常時稼働し、PCの電源を切っても動き続ける開発者向けの「**Claude Code Routines**」(スケジュール/API/GitHubイベントの3種のトリガーに対応)も追加された。ブラウザ操作は「**Claude in Chrome**」という拡張機能(ベータ)で提供

「Cowork」という名前がAnthropic(Claude Cowork)とMicrosoft(Copilot Cowork)の両方で使われている点は、単純な検索や社内会話で混同しやすいので要注意(詳細は後述の注意点)。

## 使いどころ・使い分け

### 4社の機能名・対応表(2026年7月時点)

| 項目 | ChatGPT(OpenAI) | Gemini(Google) | Microsoft Copilot | Claude(Anthropic) |
|---|---|---|---|---|
| エージェントモード(自律実行)の名称 | ChatGPT Agent | Gemini Spark | Copilot Cowork(個人のブラウザ操作は「Copilot Actions/Browse with Copilot」、法人ブラウザは「Agent Mode for Edge for Business」) | Claude Cowork(デスクトップ)/Claude in Chrome(ブラウザ、ベータ)/Computer Use・Claude Agent SDK(開発者向け) |
| スケジュールタスク(定期実行)の名称 | Tasks | Scheduled actions | Copilot Tasks(Researcher/Analystの定期実行、2026年7月にデフォルト表示化) | Cowork内のスケジュールタスク/Claude Code Routines(開発者向け、クラウド常駐) |
| 主な対応プラン | Plus・Pro・Business・Enterprise・Edu(Free・Goは不可) | Spark: Google AI Ultra(月$100/$200)のみ。Scheduled actions: Google AI Pro・Ultra、対象Workspace法人プラン | Cowork: Microsoft 365 Copilotライセンス必須(法人向けアドオン)。Actions in Edge: 個人の無料Copilotでも一部利用可 | Cowork・Routines: Pro・Max・Team・Enterprise(Freeは不可)。Claude in ChromeはProも含む全有償プラン(Proのみモデルがhaiku 4.5に固定) |
| 日本からの利用 | 可(日本語対応) | Scheduled actionsは可。**Gemini Sparkは2026年7月時点で日本を含む多数の国で未提供**(米国先行) | 可(日本語のMicrosoft 365テナントでも利用可) | 可(日本語対応) |
| 主な外部連携 | Gmail・Googleカレンダー・Drive・GitHub・Outlook・SharePoint・Dropbox・Box・HubSpot・Linear・Teams等(「アプリ」経由) | Gmail・カレンダー・Drive・Docs・Sheets・Slides・YouTube・Google マップを標準連携。MCP経由でCanva・OpenTable・Instacart等 | Microsoft Graph経由で自分の権限内のメール・ファイル・会議データ。Copilot Studioでカスタムコネクタも追加可能 | MCPコネクタ経由でSlack・Google Calendar・Gmail・Google Docs・GitHub等 |

### 判断の目安

1. **「今すぐ1回、複数ステップの作業を代行してほしい」か「同じ依頼を定期的に繰り返したい」か**: 前者はエージェントモード(ChatGPT Agent/Gemini Spark/Copilot Cowork/Claude Cowork)、後者はスケジュールタスク(Tasks/Scheduled actions/Copilot Tasks/Cowork内スケジュール・Routines)
2. **すでに契約しているツールのエコシステムに、扱いたいデータがあるか**: Gmail・Googleカレンダー中心の業務ならGemini、Word/Excel/Outlook中心ならCopilot、社内の技術文書・コードベース中心ならClaude、といった「データがどこにあるか」による選択が現実的
3. **日本から使えるか**: Gemini Sparkのように、発表はされていても日本でまだ使えない機能がある。導入検討の前に必ず対象地域を確認する
4. **開発者が使うか、非エンジニアが使うか**: Claude Agent SDK・Computer Use・Claude Code Routinesは開発者向けの構築部品。非エンジニアが画面から使うならChatGPT Agent・Gemini Spark・Copilot Cowork・Claude Coworkのような完成品アプリを選ぶ

## 実務での使い方

### コピペで使える指示例(ツール共通で応用可能)

**スケジュールタスク向け(定型調査の自動化)**

```
毎週月曜日の朝9時に、直近1週間の生成AI関連の主要ニュースをWeb検索で調べて、
3行以内の日本語サマリーで送ってください。個別の製品リリースよりも、
業務での使い方に影響しそうな話題を優先してください。
```

- ChatGPT: Tasksとして保存(サイドバーの時計アイコン、または依頼文に日時・周期を明示)
- Gemini: Gemini appでScheduled actionsを設定(入力欄付近の「スケジュール」アイコン、Pro/Ultra必須)
- Copilot: Microsoft 365 Copilot Chat/CopilotのTasksタブから「定期」を選択(Researcher/Analystいずれかのモードで実行)
- Claude: Cowork内で依頼文に日時・周期を明示、または開発者はClaude Code Routinesの`/schedule`で同様のcronベース定期実行を作成可能

**エージェントモード向け(価格モニタリング・競合調査)**

```
主要な競合3社の直近の価格改定と新機能をWebで調べて、比較表と3行サマリー付きの
レポートをスプレッドシートにまとめてください。有料資料のダウンロードや
アカウント登録が必要な場面では、実行を止めて私に確認してください。
```

- ChatGPT Agent: 「+」ボタンから「エージェントモード」を選択
- Gemini Spark: Google AI Ultraでベータ利用可能な地域のみ、Gemini appで「Spark」を選択
- Copilot Cowork: Microsoft 365環境でCoworkにタスクを渡す(実行ごとにCopilot Creditを消費)
- Claude Cowork: Claude Desktopアプリで「Cowork」モードに切り替えて依頼

### 料金・利用量の考え方

| ツール | 課金の仕組み |
|---|---|
| ChatGPT Agent/Tasks | 全社共通の「クレジット」制。プラン別に月間付与量が異なり、Tasksは同時に有効化できる件数にも上限がある(詳細は[ChatGPTのエージェント機能とTasks](./chatgpt-agent-mode-feature.md)) |
| Gemini Spark/Scheduled actions | Sparkは月$100/$200のGoogle AI Ultraプランに含まれる形(個別の実行回数上限は公式に細かく開示されていない)。Scheduled actionsはPro/Ultraの利用量枠の中で動く |
| Copilot Cowork/Tasks | Microsoft 365 Copilotライセンス(法人向けアドオン)が前提。実行ごとにCopilot Credit(1クレジット$0.01)を消費する従量課金で、軽いタスクで約125クレジット($1〜3)、重いタスクで約2,500クレジット以上($7〜)との実例が報告されている |
| Claude Cowork/Routines | claude.aiのPro以上のサブスクリプション利用量を消費。Routinesはこれに加えて1日あたりのアカウント単位の実行回数上限がある(研究プレビュー段階で今後変更の可能性あり) |

## 注意点・よくある誤解

- **「Cowork」という名前がAnthropicとMicrosoftの両方に存在する**: Anthropicの個人向けデスクトップエージェント「Claude Cowork」と、Microsoft 365 Copilotの法人向け自律実行エージェント「Copilot Cowork」は無関係の別製品。検索結果や社内チャットで「Coworkが使えるようになった」と言われたら、まずどちらの会社の機能かを確認する
- **Gemini Sparkは2026年7月時点で日本から使えない**: 発表時点(2026年5月)では米国のGoogle AI Ultra契約者限定で、その後も日本・EEA(欧州経済領域)・英国・オーストラリア・カナダ・香港・インド・韓国・スイスなどは対象外とされている。「Gemini Sparkが便利らしい」という記事を読んでも、日本から契約してすぐ使えるとは限らない点に注意
- **プロンプトインジェクションのリスクは、エージェントモードほど大きい**: ブラウザ・PCを操作するエージェントモード(ChatGPT Agent、Gemini Spark、Copilot Cowork/Actions、Claude Cowork/Claude in Chrome)は、閲覧先のページや受信メールに埋め込まれた悪意ある指示に誘導される「間接的プロンプトインジェクション」のリスクを構造的に抱えている。特に「機密データへのアクセス」「信頼できない外部コンテンツへの接触」「外部への送信・実行手段」の3つが同時に揃う使い方は危険度が高い。詳しい仕組み・悪の三要素(lethal trifecta)による判断基準は[プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md)を参照。軽量なスケジュールタスク(Web検索程度の範囲)はこのリスクが相対的に小さい
- **製品名・提供形態の変更が非常に速い**: OperatorはChatGPT Agentに、Project MarinerはGemini Sparkに、それぞれ1年前後で統合・終了している。Copilot Tasksのように「プレビュー→デフォルト機能化」を数ヶ月で駆け足で進める例もある。本ページの機能名・対応プランは今後も変わるため、導入直前には必ず各社の公式ヘルプで最新情報を確認する
- **エージェントモードは通常のチャットよりコストが跳ねやすい**: 1つの依頼で「検索→クリック→確認」を何ステップも繰り返すため、消費するクレジット・トークン量が数倍〜数十倍になりやすい。重要でない検証にエージェントモードを多用すると、月間の利用量をあっという間に使い切ってしまう
- **本ページと[AIエージェントとは何か](../part12-ai-trends/ai-agent-basics.md)の違い**: あちらは「エージェントとワークフローの違い」「エージェントループ」「導入すべきかの判断軸」といったベンダー横断の**概念**を扱う。本ページは「今使っているツールでは、その機能が何と呼ばれ、どこにあり、いくらか」という**ツール機能としての見取り図**であり、実際に画面を開いて設定する際にはこちらを、社内で導入方針を議論する際にはあちらを参照するとよい

## 最初の一歩

まず自分が普段使っているツール(ChatGPT・Gemini・Copilot・Claudeのいずれか)で、上記の対応表から「自分のツールのスケジュールタスク機能」を1つ特定し、送信・購買などを含まない軽い定型調査(業界ニュースの週次要約など)を1件登録してみる。エージェントモードを試す場合は、必ず後戻りしにくい操作(注文・送信)を含まない依頼から始める。

## 関連トピック

- [ChatGPTのエージェント機能(ChatGPT Agent)とスケジュールタスク(Tasks)](./chatgpt-agent-mode-feature.md)
- [AIエージェントとは何か](../part12-ai-trends/ai-agent-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)
- [Google Geminiの基本](./google-gemini-basics.md)
- [Microsoft Copilotの基本](./microsoft-copilot-basics.md)
- [Claude(Anthropic)の基本](./claude-basics.md)

## 更新履歴

### 2026-07-07: 初版執筆
- **内容**: ChatGPT Agent/Tasks、Gemini Spark/Scheduled actions、Copilot Cowork・Copilot Actions・Agent Mode for Edge for Business・Copilot Tasks、Claude Cowork・Claude in Chrome・Claude Code Routinesの4社比較表を作成。エージェントモードとスケジュールタスクの構造的な違い、対応プラン・料金の仕組み、日本からの利用可否(Gemini Sparkが2026年7月時点で日本未提供である点)、「Cowork」という名称がAnthropicとMicrosoftで重複している点、プロンプトインジェクションリスクの度合いの違いを整理
- **出典**: [OpenAI: Introducing ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/)、[ChatGPT agent | OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent)、[Scheduled tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)、[TechTimes: Gemini Spark: Google's 24/7 Cloud AI Agent](https://www.techtimes.com/articles/317144/20260525/gemini-spark-googles-24-7-cloud-ai-agent-now-executes-tasks-third-party-apps.htm)、[TechTimes: Google Cuts AI Ultra to $100, Launches Gemini Spark Agent](https://www.techtimes.com/articles/316853/20260519/google-cuts-ai-ultra-100-launches-gemini-spark-agent-android-xr-glasses-i-o-2026.htm)、[Google: Gemini app launches scheduled actions](https://blog.google/products-and-platforms/products/gemini/scheduled-actions-gemini-app/)、[Google Support: Gemini Apps limits & upgrades](https://support.google.com/gemini/answer/16275805?hl=en)、[AI Agents Library: Gemini Spark Availability](https://www.aiagentslibrary.com/blog/gemini-spark-availability/)、[Microsoft 365 Blog: Copilot Cowork is now generally available](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/)、[TestingCatalog: Microsoft tests Researcher and Analyst agents in Copilot Tasks](https://www.testingcatalog.com/microsoft-tests-researcher-and-analyst-agents-in-copilot-tasks/)、[Microsoft Support: Browse with Copilot(Copilot Actions in Edge)](https://support.microsoft.com/en-us/topic/copilot-actions-in-edge-5ed5e17e-42df-40a3-984a-20420eba86e2)、[Windows Blog: Protect your enterprise from shadow AI(RSAC 2026、Agent Mode for Edge for Business)](https://blogs.windows.com/msedgedev/2026/03/23/protect-your-enterprise-from-shadow-ai-and-more-announcements-at-rsac-2026/)、[Anthropic: Claude Cowork](https://www.anthropic.com/product/claude-cowork)、[VentureBeat: Anthropic launches Cowork, a Claude Desktop agent](https://venturebeat.com/technology/anthropic-launches-cowork-a-claude-desktop-agent-that-works-in-your-files-no)、[Claude Code Docs: Automate work with routines](https://code.claude.com/docs/en/routines)、[Claude Help Center: Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
