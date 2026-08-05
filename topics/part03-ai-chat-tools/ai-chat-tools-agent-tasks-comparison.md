---
title: "主要AIチャットツールのエージェント機能・スケジュールタスク比較(ChatGPT Agent/Tasks・Gemini Spark・Copilot Cowork・Claude Cowork)"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [AIエージェント, スケジュールタスク, ChatGPT Agent, Gemini Spark, Copilot Cowork, Claude Cowork, ツール比較]
created: 2026-07-07
updated: 2026-07-27
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

- **OpenAI**: 2025年1月の「Operator」(ブラウザ操作)と「Deep Research」(調査)を2025年7月に統合し「ChatGPT Agent」に一本化していたが、**2026年7月9日、独自ブラウザ「ChatGPT Atlas」の機能も取り込む形で「ChatGPT Agent」は「ChatGPT Work」に統合・改称された**。同時にGPT-5.6世代のモデルが投入され、ChatGPT自体もChat(通常会話)・Work(自律実行)・Codex(開発)の3モード構成に再編、旧デスクトップアプリは「ChatGPT Classic」に呼び方が変わった。スケジュール実行は引き続き「**Tasks**」という別機能のまま存続している([詳細](./chatgpt-agent-mode-feature.md)参照)
- **Google**: 2025年6月に軽量な「**Scheduled actions(スケジュール機能)**」をGemini appに追加。その約1年後、2026年5月のGoogle I/Oで、Gmail・カレンダー・Driveなどに24時間365日常駐して複数ステップの作業を代行する重量級エージェント「**Gemini Spark**」を発表(旧Project Mariner系のブラウザ操作機能を統合)。当初は米国のGoogle AI Ultra契約者限定だったが、**2026年7月16日に日本語対応が始まり日本からも利用可能になった**。さらに同月下旬(7月23日前後)からは米国のGoogle AI Pro契約者にも対象を拡大し始めており、他国のPro契約者にも「順次」広げるとされている(EEA・英国・スイス・ナイジェリアなどは2026年7月時点でなお対象外)([Google I/O 2026関連報道](https://www.techtimes.com/articles/317144/20260525/gemini-spark-googles-24-7-cloud-ai-agent-now-executes-tasks-third-party-apps.htm)、[GIGAZINE: Gemini Spark日本語対応](https://gigazine.net/gsc_news/en/20260716-gemini-spark-japanese/)、[9to5Google: Gemini Spark rolling out to Google AI Pro](https://9to5google.com/2026/07/23/gemini-spark-google-ai-pro-us/))
- **Microsoft**: Microsoft 365 Copilotに組み込まれた調査特化の「**Researcher**」(OpenAIのdeep researchモデルを利用)、データ分析特化の「**Analyst**」(推論モデルによるライブPython実行)が2025年半ばに一般提供。2026年2月にこの2つを定期実行できる「**Copilot Tasks**」タブがプレビュー開始し、2026年7月には(予定通り)全ユーザー向けのデフォルト画面となりオプトアウトのトグルも廃止された。エージェントモードの本命である「**Copilot Cowork**」は2026年6月16日に一般提供開始(要Microsoft 365 Copilotライセンス)し、**同日以降は使用量課金(Copilot Credit、1クレジット$0.01)へ完全移行**、移行猶予のあったテナントも2026年7月1日で猶予が終了し、課金設定をしていないテナントはCowork自体が使えなくなった。個人のWeb閲覧を代行する機能は「**Copilot Actions(Browse with Copilot)**」、企業のIT部門が許可したサイトに限定して動く法人版は「**Agent Mode for Edge for Business**」という別の名称になっている
- **Anthropic**: 開発者向けにはターミナルで動く「Claude Code」とその上の「**Claude Agent SDK**」「Computer Use(画面操作API)」が先行。2026年2月、非エンジニアでも使えるデスクトップ版の自律実行エージェント「**Claude Cowork**」をリリースし、同月末にはCowork内で使える軽量な「**スケジュールタスク**」機能も追加。2026年4月には、クラウド上で常時稼働し、PCの電源を切っても動き続ける開発者向けの「**Claude Code Routines**」(スケジュール/API/GitHubイベントの3種のトリガーに対応)も追加された。**2026年7月7日には、Coworkそのものがデスクトップに加えてWeb・モバイルでも使えるようベータ展開を開始**(Maxプランから先行し、他プランへ順次拡大)。この「リモートセッション」化により、PC本体の電源を切っても作業やスケジュールタスクが継続し、スマホから進捗確認・成果物受け取りができるようになった。**7月21日には、画面操作を1回録画するだけで再利用可能な手順(スキル)に変換する「Record a Skill」機能**(Pro・Max・Team向け)も追加され、同時期にMicrosoft 365(Outlookでのメール送信・予定登録、OneDrive/SharePointのファイル操作)への書き込み連携も加わった。ブラウザ操作は「**Claude in Chrome**」という拡張機能(ベータ)で提供

「Cowork」という名前がAnthropic(Claude Cowork)とMicrosoft(Copilot Cowork)の両方で使われている点は、単純な検索や社内会話で混同しやすいので要注意(詳細は後述の注意点)。

## 使いどころ・使い分け

### 4社の機能名・対応表(2026年7月27日時点)

| 項目 | ChatGPT(OpenAI) | Gemini(Google) | Microsoft Copilot | Claude(Anthropic) |
|---|---|---|---|---|
| エージェントモード(自律実行)の名称 | **ChatGPT Work**(2026年7月9日に「ChatGPT Agent」から改称・独自ブラウザ「ChatGPT Atlas」の機能も統合) | Gemini Spark | Copilot Cowork(個人のブラウザ操作は「Copilot Actions/Browse with Copilot」、法人ブラウザは「Agent Mode for Edge for Business」) | Claude Cowork(デスクトップ+Web/モバイル〈ベータ、2026年7月〜〉)/Claude in Chrome(ブラウザ、ベータ)/Computer Use・Claude Agent SDK(開発者向け) |
| スケジュールタスク(定期実行)の名称 | Tasks(Work統合後も別機能として存続) | Scheduled actions | Copilot Tasksタブ(Researcher/Analystの定期実行。2026年7月に全ユーザーのデフォルト画面へ、オプトアウト不可) | Cowork内のスケジュールタスク/Claude Code Routines(開発者向け、クラウド常駐) |
| 主な対応プラン | Plus・Pro・Business・Enterprise・Edu(Web/モバイル版。Free・Goは対象外。デスクトップアプリは全プランで利用可) | Spark: Google AI Ultra(個人アカウント限定、月$100/$200)に加え、2026年7月下旬から米国のGoogle AI Pro(月$20)にも拡大開始(他国は順次)。法人のWorkspaceアカウントは非対応。Scheduled actions: Google AI Pro・Ultra、対象Workspace法人プラン | Cowork: Microsoft 365 Copilotライセンス(USL)必須。2026年6月16日のGA以降は使用量課金(Copilot Credit、$0.01/クレジット)に一本化、2026年7月1日以降は課金設定必須(未設定テナントは利用不可)。Actions in Edge: 個人の無料Copilotでも一部利用可 | Cowork・Routines: Pro・Max・Team・Enterprise(Freeは不可)。Web/モバイル版はベータでMaxプランから展開中(他プランは順次)。Claude in ChromeはProも含む全有償プラン(Proのみモデルがhaiku 4.5に固定) |
| 日本からの利用 | 可(日本語対応) | Scheduled actionsは可。**Gemini Sparkは2026年7月16日に日本語対応が始まり利用可能に**(ただし個人のGoogle AI Ultra契約が必須で、会社のGoogle Workspaceアカウントでは使えない) | 可(日本語のMicrosoft 365テナントでも利用可) | 可(日本語対応) |
| 主な外部連携 | Gmail・Googleカレンダー・Drive・GitHub・Outlook・SharePoint・Dropbox・Box・HubSpot・Linear・Teams等(「アプリ」経由) | Gmail・カレンダー・Drive・Docs・Sheets・Slides・YouTube・Google マップを標準連携。MCP経由でCanva・OpenTable・Instacart等 | Microsoft Graph経由で自分の権限内のメール・ファイル・会議データ。Copilot Studioでカスタムコネクタも追加可能 | MCPコネクタ経由でSlack・Google Calendar・Gmail・Google Docs・GitHub等に加え、2026年7月からMicrosoft 365(Outlookのメール送信・予定登録、OneDrive/SharePointのファイル操作)への書き込みにも対応 |

### 判断の目安

1. **「今すぐ1回、複数ステップの作業を代行してほしい」か「同じ依頼を定期的に繰り返したい」か**: 前者はエージェントモード(ChatGPT Work/Gemini Spark/Copilot Cowork/Claude Cowork)、後者はスケジュールタスク(Tasks/Scheduled actions/Copilot Tasks/Cowork内スケジュール・Routines)
2. **すでに契約しているツールのエコシステムに、扱いたいデータがあるか**: Gmail・Googleカレンダー中心の業務ならGemini、Word/Excel/Outlook中心ならCopilot、社内の技術文書・コードベース中心ならClaude、といった「データがどこにあるか」による選択が現実的
3. **日本から使えるか、どのアカウント種別で使えるか**: Gemini Sparkは2026年7月に日本語対応したが、個人のGoogle AI Ultra(または米国先行のGoogle AI Pro)契約が前提で、会社のGoogle Workspaceアカウントでは使えない。「日本で使えるようになった」という報道と「自分の契約・アカウントで使える」は別問題なので、導入検討の前に対象地域とアカウント種別の両方を確認する
4. **開発者が使うか、非エンジニアが使うか**: Claude Agent SDK・Computer Use・Claude Code Routinesは開発者向けの構築部品。非エンジニアが画面から使うならChatGPT Work・Gemini Spark・Copilot Cowork・Claude Coworkのような完成品アプリを選ぶ

## 実務での使い方

### コピペで使える指示例(ツール共通で応用可能)

**スケジュールタスク向け(定型調査の自動化)**

```
毎週月曜日の朝9時に、直近1週間の生成AI関連の主要ニュースをWeb検索で調べて、
3行以内の日本語サマリーで送ってください。個別の製品リリースよりも、
業務での使い方に影響しそうな話題を優先してください。
```

- ChatGPT: Tasksとして保存(サイドバーの時計アイコン、または依頼文に日時・周期を明示)。2026年7月の「ChatGPT Work」統合後も、Tasksは引き続き別機能として使える
- Gemini: Gemini appでScheduled actionsを設定(入力欄付近の「スケジュール」アイコン、Pro/Ultra必須)
- Copilot: Microsoft 365 Copilot Chat/CopilotのTasksタブから「定期」を選択(Researcher/Analystいずれかのモードで実行。2026年7月からこのタブが全ユーザーの初期表示になった)
- Claude: Cowork内で依頼文に日時・周期を明示、または開発者はClaude Code Routinesの`/schedule`で同様のcronベース定期実行を作成可能。2026年7月以降はWeb・モバイル版(ベータ)からも、PCの電源を切ったままスケジュールタスクを継続実行できる

**エージェントモード向け(価格モニタリング・競合調査)**

```
主要な競合3社の直近の価格改定と新機能をWebで調べて、比較表と3行サマリー付きの
レポートをスプレッドシートにまとめてください。有料資料のダウンロードや
アカウント登録が必要な場面では、実行を止めて私に確認してください。
```

- ChatGPT Work: 画面上部の「Work」タブを選択(2026年7月9日に「エージェントモード」ボタンから改称)
- Gemini Spark: Google AI Ultra(日本を含む対象国)またはGoogle AI Pro(米国先行)の個人アカウントで、Gemini appの「Spark」を選択
- Copilot Cowork: Microsoft 365環境でCoworkにタスクを渡す(実行ごとにCopilot Creditを消費する使用量課金)
- Claude Cowork: Claude Desktop・Web・モバイル(Web/モバイルはベータ、Maxプランから先行)のいずれかで「Cowork」モードに切り替えて依頼

### 料金・利用量の考え方

| ツール | 課金の仕組み |
|---|---|
| ChatGPT Work/Tasks | 2026年7月の改称以降はCodexと共通の「エージェント利用枠」を消費。Plus/Proは5時間ごとのローカルメッセージ数と同じ枠を共有し、超過分は追加クレジットの購入で継続利用できる。Business/Enterprise/Eduは追加のワークスペースクレジットを購入可能(詳細は[ChatGPTのエージェント機能とTasks](./chatgpt-agent-mode-feature.md)) |
| Gemini Spark/Scheduled actions | Sparkは月$100/$200のGoogle AI Ultra、または2026年7月拡大分の月$20のGoogle AI Pro(対象国のみ)に含まれる形(個別の実行回数上限は公式に細かく開示されていない)。Scheduled actionsはPro/Ultraの利用量枠の中で動く |
| Copilot Cowork/Tasks | Microsoft 365 Copilotライセンス(法人向けアドオン)が前提。2026年6月16日のGA以降は実行ごとにCopilot Credit(1クレジット$0.01)を消費する使用量課金(PayGo)、または事前コミット型の割引プラン「P3」のいずれかに一本化された。軽いタスクで約125クレジット($1〜3)、重いタスクで約2,500クレジット以上($7〜)との実例が報告されている。2026年7月1日以降、使用量課金を設定していないテナントはCowork自体が利用不可になる点に注意 |
| Claude Cowork/Routines | claude.aiのPro以上のサブスクリプション利用量を消費。2026年7月開始のWeb/モバイル版(ベータ)はリモートセッションとして動作し、端末がオフラインでもタスクやスケジュール実行が継続する。Routinesはこれに加えて1日あたりのアカウント単位の実行回数上限がある(研究プレビュー段階で今後変更の可能性あり) |

## 注意点・よくある誤解

- **「Cowork」という名前がAnthropicとMicrosoftの両方に存在する**: Anthropicの個人向けデスクトップ(+Web/モバイル)エージェント「Claude Cowork」と、Microsoft 365 Copilotの法人向け自律実行エージェント「Copilot Cowork」は無関係の別製品。検索結果や社内チャットで「Coworkが使えるようになった」と言われたら、まずどちらの会社の機能かを確認する
- **Gemini Sparkは「日本で使える」=「自分のアカウントで使える」ではない**: 2026年7月16日に日本語対応が始まり、日本からもGemini Sparkにアクセスできるようになったが、対象は個人のGoogle AI Ultra(または同月拡大分のGoogle AI Pro、米国先行)契約者のみで、会社のGoogle Workspaceアカウントでは利用できない。「Gemini Sparkが日本語対応した」というニュースだけを見て、会社のアカウントですぐ使えると誤解しないよう注意
- **プロンプトインジェクションのリスクは、エージェントモードほど大きい**: ブラウザ・PCを操作するエージェントモード(ChatGPT Work、Gemini Spark、Copilot Cowork/Actions、Claude Cowork/Claude in Chrome)は、閲覧先のページや受信メールに埋め込まれた悪意ある指示に誘導される「間接的プロンプトインジェクション」のリスクを構造的に抱えている。特に「機密データへのアクセス」「信頼できない外部コンテンツへの接触」「外部への送信・実行手段」の3つが同時に揃う使い方は危険度が高い。詳しい仕組み・悪の三要素(lethal trifecta)による判断基準は[プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md)を参照。軽量なスケジュールタスク(Web検索程度の範囲)はこのリスクが相対的に小さい。Claude Coworkのように端末がオフラインでも動くリモートセッション型の機能は、実行中に何をしているか気づきにくくなる点にも留意する
- **製品名・提供形態の変更が非常に速い**: OperatorはChatGPT Agentに統合され、そのChatGPT Agentも2026年7月に独自ブラウザ「Atlas」ごと「ChatGPT Work」へ改称、Project MarinerはGemini Sparkに、それぞれ1年前後で統合・終了している。Copilot Tasksのように「プレビュー→デフォルト機能化」を数ヶ月で駆け足で進める例もある。本ページの機能名・対応プランは今後も変わるため、導入直前には必ず各社の公式ヘルプで最新情報を確認する
- **Copilot Coworkは2026年7月から「使わないと損」ではなく「設定しないと止まる」課金に変わった**: 2026年6月16日のGAで使用量課金(Copilot Credit)へ移行し、それまで無償トライアル的に使えていたテナントも2026年7月1日を境に、管理者が課金設定(PayGo/P3)を済ませていないとCowork自体にアクセスできなくなった。すでに社内でCoworkを使っている場合は、Microsoft 365管理センターで課金設定が完了しているかを確認する
- **エージェントモードは通常のチャットよりコストが跳ねやすい**: 1つの依頼で「検索→クリック→確認」を何ステップも繰り返すため、消費するクレジット・トークン量が数倍〜数十倍になりやすい。重要でない検証にエージェントモードを多用すると、月間の利用量をあっという間に使い切ってしまう
- **本ページと[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)の違い**: あちらは「エージェントとワークフローの違い」「エージェントループ」「導入すべきかの判断軸」といったベンダー横断の**概念**を扱う。本ページは「今使っているツールでは、その機能が何と呼ばれ、どこにあり、いくらか」という**ツール機能としての見取り図**であり、実際に画面を開いて設定する際にはこちらを、社内で導入方針を議論する際にはあちらを参照するとよい

## 最初の一歩

まず自分が普段使っているツール(ChatGPT・Gemini・Copilot・Claudeのいずれか)で、上記の対応表から「自分のツールのスケジュールタスク機能」を1つ特定し、送信・購買などを含まない軽い定型調査(業界ニュースの週次要約など)を1件登録してみる。エージェントモードを試す場合は、必ず後戻りしにくい操作(注文・送信)を含まない依頼から始める。

## 関連トピック

- [ChatGPTのエージェント機能(ChatGPT Agent)とスケジュールタスク(Tasks)](./chatgpt-agent-mode-feature.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)
- [Google Geminiの基本](./google-gemini-basics.md)
- [Microsoft Copilotの基本](./microsoft-copilot-basics.md)
- [Claude(Anthropic)の基本](./claude-basics.md)

## 更新履歴

### 2026-07-27: ChatGPT Agentの「ChatGPT Work」改称、Gemini Spark日本語対応、Copilot Coworkの使用量課金移行、Claude CoworkのWeb/モバイル展開を反映
- **内容**: (1)2026年7月9日にChatGPT Agentが独自ブラウザAtlasと統合の上「ChatGPT Work」に改称(Tasksは別機能として存続、ChatGPT自体もChat/Work/Codexの3モード構成に再編)、(2)Gemini Sparkが2026年7月16日に日本語対応・日本から利用可能になったが個人のGoogle AI Ultra契約が前提で法人Workspaceは非対応である点、同月下旬から米国のGoogle AI Proにも対象拡大している点、(3)Copilot Coworkが2026年6月16日のGA以降Copilot Creditによる使用量課金に一本化され2026年7月1日以降は課金設定必須になった点・Copilot Tasksタブが全ユーザーのデフォルトになった点、(4)Claude Coworkが2026年7月7日からWeb・モバイル(ベータ、Maxプラン先行)に拡大しリモートセッション化した点、7月21日の「Record a Skill」機能追加とMicrosoft 365書き込み連携の追加、をそれぞれ比較表・本文・料金表に反映して全体を最新化
- **出典**: [MacRumors: OpenAI Debuts ChatGPT Work Agent and New GPT-5.6 Models](https://www.macrumors.com/2026/07/09/openai-chatgpt-work/)、[Bloomberg: OpenAI Unveils ChatGPT Work Agent](https://www.bloomberg.com/news/articles/2026-07-09/openai-unveils-chatgpt-work-agent-to-field-tasks-for-hours)、[PYMNTS: OpenAI Launches ChatGPT Agent That Executes Complex Workflows](https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-chatgpt-agent-that-executes-complex-workflows/)、[ppc.land: OpenAI kills Atlas browser, folds it into new ChatGPT Work agent](https://ppc.land/openai-kills-atlas-browser-folds-it-into-new-chatgpt-work-agent/)、[OpenAI Help Center: Using credits for flexible usage in ChatGPT](https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro)、[GIGAZINE: Google's 24/7 AI agent, Gemini Spark, is now available in Japanese](https://gigazine.net/gsc_news/en/20260716-gemini-spark-japanese/)、[note: Gemini Sparkの日本での使い方まとめ](https://note.com/csfive/n/nfe5b97fbfef2?hl=en)、[9to5Google: Gemini Spark rolling out to Google AI Pro users in the US](https://9to5google.com/2026/07/23/gemini-spark-google-ai-pro-us/)、[Digital Trends: Gemini Spark is no longer restricted to Google's priciest Ultra tier](https://www.digitaltrends.com/computing/gemini-spark-is-no-longer-restricted-to-googles-priciest-ultra-tier/)、[Microsoft 365 Blog: Copilot Cowork is now generally available](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/)、[Arraya Solutions: Microsoft Copilot Cowork Is Moving to Paid](https://www.arrayasolutions.com/insights/blog/2026/microsoft-copilot-cowork-is-moving-to-paid-what-it-and-business-leaders-need-to-know-before-july-1/)、[Quisitive: Copilot Cowork Pricing 2026](https://quisitive.com/copilot-cowork-pricing-2026-how-usage-based-billing-works/)、[TechCrunch: Claude Cowork expands to mobile and web](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/)、[NBC News: Anthropic will make Claude Cowork available to users via the cloud](https://www.nbcnews.com/tech/tech-news/anthropic-will-make-claude-cowork-available-users-cloud-rcna353218)、[Claude Help Center: Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)、[ExplainX: Claude Cowork Record a Skill — July 2026](https://www.explainx.ai/blog/claude-cowork-record-a-skill-screen-recording-july-2026)

### 2026-07-07: 初版執筆
- **内容**: ChatGPT Agent/Tasks、Gemini Spark/Scheduled actions、Copilot Cowork・Copilot Actions・Agent Mode for Edge for Business・Copilot Tasks、Claude Cowork・Claude in Chrome・Claude Code Routinesの4社比較表を作成。エージェントモードとスケジュールタスクの構造的な違い、対応プラン・料金の仕組み、日本からの利用可否(Gemini Sparkが2026年7月時点で日本未提供である点)、「Cowork」という名称がAnthropicとMicrosoftで重複している点、プロンプトインジェクションリスクの度合いの違いを整理
- **出典**: [OpenAI: Introducing ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/)、[ChatGPT agent | OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent)、[Scheduled tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)、[TechTimes: Gemini Spark: Google's 24/7 Cloud AI Agent](https://www.techtimes.com/articles/317144/20260525/gemini-spark-googles-24-7-cloud-ai-agent-now-executes-tasks-third-party-apps.htm)、[TechTimes: Google Cuts AI Ultra to $100, Launches Gemini Spark Agent](https://www.techtimes.com/articles/316853/20260519/google-cuts-ai-ultra-100-launches-gemini-spark-agent-android-xr-glasses-i-o-2026.htm)、[Google: Gemini app launches scheduled actions](https://blog.google/products-and-platforms/products/gemini/scheduled-actions-gemini-app/)、[Google Support: Gemini Apps limits & upgrades](https://support.google.com/gemini/answer/16275805?hl=en)、[AI Agents Library: Gemini Spark Availability](https://www.aiagentslibrary.com/blog/gemini-spark-availability/)、[Microsoft 365 Blog: Copilot Cowork is now generally available](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/)、[TestingCatalog: Microsoft tests Researcher and Analyst agents in Copilot Tasks](https://www.testingcatalog.com/microsoft-tests-researcher-and-analyst-agents-in-copilot-tasks/)、[Microsoft Support: Browse with Copilot(Copilot Actions in Edge)](https://support.microsoft.com/en-us/topic/copilot-actions-in-edge-5ed5e17e-42df-40a3-984a-20420eba86e2)、[Windows Blog: Protect your enterprise from shadow AI(RSAC 2026、Agent Mode for Edge for Business)](https://blogs.windows.com/msedgedev/2026/03/23/protect-your-enterprise-from-shadow-ai-and-more-announcements-at-rsac-2026/)、[Anthropic: Claude Cowork](https://www.anthropic.com/product/claude-cowork)、[VentureBeat: Anthropic launches Cowork, a Claude Desktop agent](https://venturebeat.com/technology/anthropic-launches-cowork-a-claude-desktop-agent-that-works-in-your-files-no)、[Claude Code Docs: Automate work with routines](https://code.claude.com/docs/en/routines)、[Claude Help Center: Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
