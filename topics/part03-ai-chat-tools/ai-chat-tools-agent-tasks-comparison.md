---
title: "主要AIチャットツールのエージェント機能・スケジュールタスク比較(ChatGPT Work/Tasks・Gemini Spark・Copilot Cowork・Claude Cowork)"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [AIエージェント, スケジュールタスク, ChatGPT Work, Gemini Spark, Copilot Cowork, Claude Cowork, ツール比較]
created: 2026-07-07
updated: 2026-09-07
---

# 主要AIチャットツールのエージェント機能・スケジュールタスク比較(ChatGPT Work/Tasks・Gemini Spark・Copilot Cowork・Claude Cowork)

## これは何か

ChatGPT・Gemini・Microsoft Copilot・Claudeは、いずれも2025〜2026年にかけて「自律的にブラウザ・PCを操作して複数ステップの作業をやり切る**エージェントモード**」と「決まった周期・イベントで同じ依頼を自動的に繰り返す**スケジュールタスク**」の2種類の自律実行系機能を追加した。ところが各社の呼び方がまったく異なり(ChatGPT Work、Gemini Spark、Copilot Cowork、Claude Cowork……)、しかも「Cowork」のようにベンダーをまたいで同じ名前が使われているケースまであるため、「うちの会社はGeminiなのに、ネット記事に出てくるChatGPT Workの話がそのまま当てはまるのか」が非常に分かりにくい。本ページは、4社の機能名・対応プラン・できること/できないことを1枚の対応表に整理し、「自分が使っているツールでは何をどう呼ぶか」をすぐ調べられるようにする。

なお、個々のツールの詳しい仕組み・確認プロンプト・料金の内訳は各社の専用ページ([ChatGPTのエージェント機能とTasks](./chatgpt-agent-mode-feature.md)など)に譲り、本ページはツール横断の「見取り図」に徹する。

## 仕組み・背景

### 「エージェントモード」と「スケジュールタスク」は別物、ただし境界は溶け始めている

各社とも、次の2つを別の機能として用意してきた(名前の付け方は違うが、構造はほぼ共通)。

- **エージェントモード(自律実行)**: 仮想ブラウザ・PC環境の中でAIが実際にクリック・入力・ファイル作成まで行い、目標(ゴール)を渡すと最後までやり切る。1回の依頼で数分〜数十分かかる、重量級の機能
- **スケジュールタスク(定期実行)**: 「毎週月曜9時に◯◯して」のように、決まった日時・周期でプロンプトを自動的に再実行するだけの軽量な機能。多くはブラウザ操作を伴わず、Web検索程度の範囲で完結する

2026年8月前後からは、この2つの中間にあたる**イベント駆動トリガー**(「メールが届いたら」「Slackにメッセージが来たら」「PRがマージされたら」実行する仕組み)が各社で相次いで追加され、スケジュールタスク側がエージェントモードに近い判断力を持ち始めている。ChatGPTは2026年8月25日にGmail・Slack・GitHubのWebhookトリガーを追加し、Microsoft CopilotはCowork内の「Scheduled」タブを「**Automations**」に改称してOutlookメール・Teamsメッセージのイベントトリガーを統合、Claude Coworkのスケジュールタスクもファイル出現・アプリ状態変化・外部Webhookをトリガーにできるようになっている。それでも「仮想ブラウザ・PC環境を都度立ち上げて何十ステップも操作するか」「軽い判定・要約だけで完結するか」という計算コストの差は残っており、エージェントモードには依然として確認プロンプト(後戻りしにくい操作の前に人間の許可を求める仕組み)などの安全機構が重ねてある。

### 各社の機能の成り立ち(2026年9月時点)

- **OpenAI**: 2025年1月の「Operator」(ブラウザ操作)と「Deep Research」(調査)を2025年7月に統合し「ChatGPT Agent」に一本化していたが、2026年7月9日、独自ブラウザ「ChatGPT Atlas」の機能も取り込む形で「ChatGPT Agent」は「**ChatGPT Work**」に統合・改称された。この名称は2026年9月時点でも継続しており、再改称はない。2026年9月3日には新フラッグシップモデル「**GPT-6 Astra**」が発表され、ブラウザ操作・コンピュータ操作・ソフトウェア開発で従来最高性能をうたう(Plus・Pro・Business・Enterprise・APIへ順次展開)。スケジュール実行は引き続き「**Tasks**」という別機能のまま存続しているが、**2026年8月25〜26日にGmail・Slack・GitHubの新着イベントをトリガーにできる機能が有料プラン(Plus/Pro/Business/Enterprise)向けに追加**され、同時に無料プラン・Go向けにも(Webhookトリガーなしの)スケジュール機能が解放された([詳細](./chatgpt-agent-mode-feature.md)参照)
- **Google**: 2025年6月に軽量な「Scheduled actions(スケジュール機能)」をGemini appに追加。2026年5月のGoogle I/Oで、Gmail・カレンダー・Driveなどに24時間365日常駐して複数ステップの作業を代行する重量級エージェント「**Gemini Spark**」を発表し、同時にGoogle AI Ultraの価格を月$249.99から**月$99.99へ約6割値下げ**してSparkの主契約プランとした。当初は米国のGoogle AI Ultra契約者限定だったが、2026年7月16日に日本語対応が始まり日本からも利用可能になり、**2026年7月29日には米国・日本ともにGoogle AI Pro契約者(米国$19.99/月・日本¥2,900/月)にも対象を段階的に拡大**した(法人のGoogle Workspaceアカウントは2026年9月時点でも非対応)。Sparkが標準連携するのはGmail・カレンダー・Docs・Sheets・Drive・Keepで、MCP(Model Context Protocol)経由の外部連携も2026年夏の時点で30以上に拡大しているが、Outlook・Slack・Notionなど非Google系ツール中心の業務では依然として手薄
- **Microsoft**: Microsoft 365 Copilotに組み込まれた調査特化の「Researcher」(OpenAIのdeep researchモデルを利用)、データ分析特化の「Analyst」(推論モデルによるライブPython実行)は2025年半ばに一般提供済み。エージェントモードの本命である「**Copilot Cowork**」は2026年6月16日に一般提供開始(要Microsoft 365 Copilotライセンス)し、同日以降は使用量課金(Copilot Credit、1クレジット$0.01)へ完全移行、2026年7月1日以降は課金設定をしていないテナントはCowork自体が使えなくなった。**2026年8月には、Cowork内でResearcher・Analystの定期実行を管理していた「Scheduled」タブが「Automations」タブに改称**され、時刻指定の定期実行に加えてOutlookメールの受信・Teamsチャンネルやチャットのメッセージ・自分宛てのメンションをトリガーにするイベント駆動タスクも同じ画面で扱えるようになった。さらに**2026年8月中旬(モバイル・Web)〜9月中旬(Windows・Mac)にかけて、個人向けCopilotアプリと企業向けMicrosoft 365 Copilotアプリが1つのアプリ(単一の名称・アイコン・URL)に統合**されている最中で、Coworkへの入り口も順次このアプリに一本化されつつある。個人のWeb閲覧を代行する機能は「Copilot Actions(Browse with Copilot)」、企業のIT部門が許可したサイトに限定して動く法人版は「Agent Mode for Edge for Business」という別の名称のまま
- **Anthropic**: 開発者向けにはターミナルで動く「Claude Code」とその上の「Claude Agent SDK」「Computer Use(画面操作API)」が先行。2026年2月、非エンジニアでも使えるデスクトップ版の自律実行エージェント「**Claude Cowork**」をリリース。**2026年4月9日にはCowork内で使える「スケジュールタスク」機能が追加**され、時刻指定の定期実行に加えて、フォルダへのファイル出現・アプリの状態変化・外部Webhookをトリガーにする実行にも対応した。開発者向けにクラウド上で常時稼働する「Claude Code Routines」(スケジュール/APIのWebhook/GitHubイベントの3種のトリガー)も並行して提供されている。**2026年7月7日には、Coworkそのものがデスクトップに加えてWeb・モバイルでも使えるようベータ展開を開始**(Maxプランから先行し、Pro・Team・管理者が有効化したEnterpriseへ順次拡大中で、2026年9月時点でもなおベータの位置づけ)。この「リモートセッション」化により、PC本体の電源を切っても作業やスケジュールタスクが継続し、スマホから進捗確認・成果物受け取りができるようになった。7月21日には画面操作を1回録画するだけで再利用可能な手順(スキル)に変換する「Record a Skill」機能(Pro・Max・Team向け)も追加され、Microsoft 365向けの連携も単一の「Claude for Microsoft 365」アドインに統合された上でOutlookでのメール送信・予定登録、OneDrive/SharePointのファイル操作といった書き込み権限が加わっている。ブラウザ操作は「Claude in Chrome」という拡張機能(ベータ)で提供

「Cowork」という名前がAnthropic(Claude Cowork)とMicrosoft(Copilot Cowork)の両方で使われている点は、単純な検索や社内会話で混同しやすいので要注意(詳細は後述の注意点)。

## 使いどころ・使い分け

### 4社の機能名・対応表(2026年9月7日時点)

| 項目 | ChatGPT(OpenAI) | Gemini(Google) | Microsoft Copilot | Claude(Anthropic) |
|---|---|---|---|---|
| エージェントモード(自律実行)の名称 | **ChatGPT Work**(2026年7月9日に「ChatGPT Agent」から改称・独自ブラウザ「ChatGPT Atlas」の機能も統合。2026年9月3日以降はGPT-6 Astraが順次搭載) | Gemini Spark | Copilot Cowork(個人のブラウザ操作は「Copilot Actions/Browse with Copilot」、法人ブラウザは「Agent Mode for Edge for Business」) | Claude Cowork(デスクトップ+Web/モバイル〈ベータ〉)/Claude in Chrome(ブラウザ、ベータ)/Computer Use・Claude Agent SDK(開発者向け) |
| スケジュールタスク(定期実行+イベント駆動)の名称 | Tasks(Work統合後も別機能として存続。2026年8月25日にGmail/Slack/GitHubのイベントトリガーを追加) | Scheduled actions | Cowork内「Automations」タブ(2026年8月に「Scheduled」タブから改称し、Outlookメール・Teamsメッセージのイベントトリガーを統合。Researcher/Analystの定期実行もここで管理) | Cowork内のスケジュールタスク(2026年4月〜、ファイル出現・アプリ状態変化・外部Webhookのイベントトリガー対応)/Claude Code Routines(開発者向け、クラウド常駐) |
| 主な対応プラン | Work: Plus・Pro・Business・Enterprise・Edu(Free・Goは対象外)。Tasks: 全プラン(Free・Goは最大3件・イベントトリガー不可/Plusは最大5件/Business・Eduは最大10件/Pro・Enterpriseは最大15件、いずれもイベントトリガーはPlus以上) | Spark: Google AI Ultra(月$99.99〜、2026年5月に旧$249.99から値下げ)に加え、2026年7月29日から米国・日本のGoogle AI Pro(米国$19.99・日本¥2,900/月)にも拡大。法人のWorkspaceアカウントは非対応。Scheduled actions: Google AI Pro・Ultra、対象Workspace法人プラン(最大同時10件) | Cowork: Microsoft 365 Copilotライセンス(USL)必須。2026年6月16日のGA以降は使用量課金(Copilot Credit、$0.01/クレジット)に一本化、2026年7月1日以降は課金設定必須(未設定テナントは利用不可)。Actions in Edge: 個人の無料Copilotでも一部利用可 | Cowork・スケジュールタスク: Pro・Max・Team・Enterprise(Freeは不可)。Web/モバイル版はベータでMaxプランから展開中、他プランへ順次拡大。Claude in ChromeはProも含む全有償プラン(Proのみモデルがhaiku 4.5に固定) |
| 日本からの利用 | 可(日本語対応) | Scheduled actionsは可。Gemini Sparkは2026年7月16日に日本語対応、7月29日から日本のGoogle AI Proにも展開開始(会社のGoogle Workspaceアカウントでは依然利用不可) | 可(日本語のMicrosoft 365テナントでも利用可) | 可(日本語対応) |
| 主な外部連携 | Gmail・Googleカレンダー・Drive・GitHub・Outlook・SharePoint・Dropbox・Box・HubSpot・Linear・Teams等(「アプリ」経由。TasksのイベントトリガーはGmail・Slack・GitHubの3種) | Gmail・カレンダー・Drive・Docs・Sheets・Keepを標準連携。MCP経由でCanva・OpenTable・Instacart等30以上(2026年夏時点) | Microsoft Graph経由で自分の権限内のメール・ファイル・会議データ。CoworkのAutomationsはOutlookメール・Teamsメッセージ/メンションをイベントトリガーに利用可。Copilot Studioでカスタムコネクタも追加可能 | MCPコネクタ経由でSlack・Google Calendar・Gmail・Google Docs・GitHub等に加え、単一化された「Claude for Microsoft 365」アドイン経由でOutlook(メール送信・予定登録)・OneDrive/SharePoint(ファイル操作)への書き込みにも対応 |

### 判断の目安

1. **「今すぐ1回、複数ステップの作業を代行してほしい」か「同じ依頼を定期的・イベント駆動で繰り返したい」か**: 前者はエージェントモード(ChatGPT Work/Gemini Spark/Copilot Cowork/Claude Cowork)、後者はスケジュールタスク(Tasks/Scheduled actions/Cowork内Automations・Routines)。2026年8月以降は各社ともスケジュールタスク側にイベント駆動トリガー(メール受信・チャットメッセージ・Webhook等)が加わっているため、「毎回同じ操作」だけでなく「条件が揃ったら動く」使い方も軽量な側で実現しやすくなっている
2. **すでに契約しているツールのエコシステムに、扱いたいデータがあるか**: Gmail・Googleカレンダー中心の業務ならGemini、Word/Excel/Outlook中心ならCopilot、社内の技術文書・コードベース中心ならClaude、といった「データがどこにあるか」による選択が現実的
3. **日本から使えるか、どのアカウント種別で使えるか**: Gemini Sparkは2026年7月に日本語対応し、同年7月29日以降は個人のGoogle AI Ultraに加えてGoogle AI Pro契約でも使えるようになったが、会社のGoogle Workspaceアカウントでは依然使えない。「日本で使えるようになった」という報道と「自分の契約・アカウントで使える」は別問題なので、導入検討の前に対象地域とアカウント種別の両方を確認する
4. **開発者が使うか、非エンジニアが使うか**: Claude Agent SDK・Computer Use・Claude Code Routinesは開発者向けの構築部品。非エンジニアが画面から使うならChatGPT Work・Gemini Spark・Copilot Cowork・Claude Coworkのような完成品アプリを選ぶ

## 実務での使い方

### コピペで使える指示例(ツール共通で応用可能)

**スケジュールタスク向け(定型調査の自動化)**

```
毎週月曜日の朝9時に、直近1週間の生成AI関連の主要ニュースをWeb検索で調べて、
3行以内の日本語サマリーで送ってください。個別の製品リリースよりも、
業務での使い方に影響しそうな話題を優先してください。
```

- ChatGPT: Tasksとして保存(サイドバーの時計アイコン、または依頼文に日時・周期を明示)。無料プラン・Goでも最大3件まで登録可能(イベントトリガーはPlus以上限定)
- Gemini: Gemini appでScheduled actionsを設定(入力欄付近の「スケジュール」アイコン、Pro/Ultra必須、最大10件まで同時登録可能)
- Copilot: Microsoft 365 Copilot ChatまたはCowork内の「Automations」タブ(2026年8月に「Scheduled」タブから改称)から「定期」を選択(Researcher/Analystいずれかのモードで実行)
- Claude: Cowork内で依頼文に日時・周期を明示、または開発者はClaude Code Routinesの`/schedule`で同様のcronベース定期実行を作成可能。Web・モバイル版(ベータ)からも、PCの電源を切ったままスケジュールタスクを継続実行できる

**イベント駆動タスク向け(受信をきっかけに動かす、2026年8月以降の新パターン)**

```
特定の取引先(例: ◯◯株式会社)からメールが届いたら、内容を3行で要約し、
返信の下書き案を1つ作成してください。契約・金額に関わる内容の場合は、
下書きを作らず「要確認」とだけ通知してください。
```

- ChatGPT: Tasksの新規作成画面でGmail/Slack/GitHubのいずれかを接続し、トリガー条件(送信者・件名・チャンネル・ラベル等)を指定(Plus以上、2026年8月25日以降)
- Copilot: Cowork内Automationsタブで「イベント」を選び、Outlookメールの受信条件、またはTeamsチャンネル・チャット・自分宛てメンションを指定
- Claude: Coworkのスケジュールタスク作成画面で、時刻指定の代わりに「ファイル出現」「アプリの状態変化」「外部Webhook」をトリガーに選択
- Gemini: 2026年9月時点、Scheduled actionsは時刻・周期指定が中心で、Gmail等の着信そのものをトリガーにする機能は正式提供されていない(結果をGmailへ送る、はできる)

**エージェントモード向け(価格モニタリング・競合調査)**

```
主要な競合3社の直近の価格改定と新機能をWebで調べて、比較表と3行サマリー付きの
レポートをスプレッドシートにまとめてください。有料資料のダウンロードや
アカウント登録が必要な場面では、実行を止めて私に確認してください。
```

- ChatGPT Work: 画面上部の「Work」タブを選択(2026年9月3日以降、対応アカウントから順次GPT-6 Astraで動作)
- Gemini Spark: Google AI Ultra(日本を含む対象国)またはGoogle AI Pro(2026年7月29日拡大分、米国・日本)の個人アカウントで、Gemini appの「Spark」を選択
- Copilot Cowork: Microsoft 365環境でCoworkにタスクを渡す(実行ごとにCopilot Creditを消費する使用量課金)
- Claude Cowork: Claude Desktop・Web・モバイル(Web/モバイルはベータ、Maxプランから先行)のいずれかで「Cowork」モードに切り替えて依頼

### 料金・利用量の考え方

| ツール | 課金の仕組み |
|---|---|
| ChatGPT Work/Tasks | 2026年7月の改称以降はCodexと共通の「エージェント利用枠」を消費。Plus/Proは5時間ごとのローカルメッセージ数と同じ枠を共有し、超過分は追加クレジットの購入で継続利用できる。Business/Enterprise/Eduは追加のワークスペースクレジットを購入可能。TasksはFree/Go(月額固定料金の範囲内)から使えるが、イベントトリガー付きタスクはPlus以上が前提(詳細は[ChatGPTのエージェント機能とTasks](./chatgpt-agent-mode-feature.md)) |
| Gemini Spark/Scheduled actions | Sparkは月$99.99〜(2026年5月に旧$249.99から値下げ)のGoogle AI Ultra、または2026年7月29日拡大分の月$19.99(日本¥2,900)のGoogle AI Pro(対象国のみ)に含まれる形(個別の実行回数上限は公式に細かく開示されていない)。Scheduled actionsはPro/Ultraの利用量枠の中で動き、同時登録は最大10件 |
| Copilot Cowork/Automations | Microsoft 365 Copilotライセンス(法人向けアドオン)が前提。2026年6月16日のGA以降は実行ごとにCopilot Credit(1クレジット$0.01)を消費する使用量課金(PayGo)、または事前コミット型の割引プラン「P3」のいずれかに一本化された。軽いタスクで約125クレジット($1〜3)、重いタスクで約2,500クレジット以上($7〜)との実例が報告されている。2026年7月1日以降、使用量課金を設定していないテナントはCowork自体が利用不可になる点に注意 |
| Claude Cowork/Routines | claude.aiのPro以上のサブスクリプション利用量を消費。2026年7月開始のWeb/モバイル版(ベータ)はリモートセッションとして動作し、端末がオフラインでもタスクやスケジュール実行が継続する。Routinesはこれに加えて1日あたりのアカウント単位の実行回数上限がある(研究プレビュー段階で今後変更の可能性あり) |

## 注意点・よくある誤解

- **「Cowork」という名前がAnthropicとMicrosoftの両方に存在する**: Anthropicの個人向けデスクトップ(+Web/モバイル)エージェント「Claude Cowork」と、Microsoft 365 Copilotの法人向け自律実行エージェント「Copilot Cowork」は無関係の別製品。検索結果や社内チャットで「Coworkが使えるようになった」と言われたら、まずどちらの会社の機能かを確認する
- **Gemini Sparkは「日本で使える」=「自分のアカウントで使える」ではない**: 2026年7月16日に日本語対応が始まり、7月29日からは日本のGoogle AI Pro契約者にも対象が広がったが、会社のGoogle Workspaceアカウントでは依然利用できない。「Gemini Sparkが日本語対応した」というニュースだけを見て、会社のアカウントですぐ使えると誤解しないよう注意
- **軽量なスケジュールタスクにもイベント駆動トリガーが付き、境界が曖昧になっている**: 2026年8月前後にChatGPT Tasks・Copilot CoworkのAutomations・Claude Coworkのスケジュールタスクが相次いでメール受信・チャットメッセージ・Webhookをトリガーにできるようになった。これらは「軽量」な位置づけのままだが、機密メールの内容をトリガー条件やAI応答の材料にするため、後述のプロンプトインジェクション対策の対象として扱う必要がある(「軽いから安全」と思い込まない)
- **プロンプトインジェクションのリスクは、エージェントモードほど大きい**: ブラウザ・PCを操作するエージェントモード(ChatGPT Work、Gemini Spark、Copilot Cowork/Actions、Claude Cowork/Claude in Chrome)は、閲覧先のページや受信メールに埋め込まれた悪意ある指示に誘導される「間接的プロンプトインジェクション」のリスクを構造的に抱えている。特に「機密データへのアクセス」「信頼できない外部コンテンツへの接触」「外部への送信・実行手段」の3つが同時に揃う使い方は危険度が高い。詳しい仕組み・悪の三要素(lethal trifecta)による判断基準は[プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md)を参照。Claude Coworkのように端末がオフラインでも動くリモートセッション型の機能は、実行中に何をしているか気づきにくくなる点にも留意する
- **製品名・提供形態の変更が非常に速い**: OperatorはChatGPT Agentに統合され、そのChatGPT Agentも2026年7月に独自ブラウザ「Atlas」ごと「ChatGPT Work」へ改称、Project MarinerはGemini Sparkに、それぞれ1年前後で統合・終了している。Copilotの「Scheduled」タブは1年経たずに「Automations」へ改称され、さらに個人向けCopilotアプリと企業向けMicrosoft 365 Copilotアプリの統合(2026年8〜9月)も進行中。本ページの機能名・対応プランは今後も変わるため、導入直前には必ず各社の公式ヘルプで最新情報を確認する
- **Copilot Coworkは2026年7月から「使わないと損」ではなく「設定しないと止まる」課金に変わった**: 2026年6月16日のGAで使用量課金(Copilot Credit)へ移行し、それまで無償トライアル的に使えていたテナントも2026年7月1日を境に、管理者が課金設定(PayGo/P3)を済ませていないとCowork自体にアクセスできなくなった。すでに社内でCoworkを使っている場合は、Microsoft 365管理センターで課金設定が完了しているかを確認する
- **エージェントモードは通常のチャットよりコストが跳ねやすい**: 1つの依頼で「検索→クリック→確認」を何ステップも繰り返すため、消費するクレジット・トークン量が数倍〜数十倍になりやすい。重要でない検証にエージェントモードを多用すると、月間の利用量をあっという間に使い切ってしまう
- **本ページと[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)の違い**: あちらは「エージェントとワークフローの違い」「エージェントループ」「導入すべきかの判断軸」といったベンダー横断の**概念**を扱う。本ページは「今使っているツールでは、その機能が何と呼ばれ、どこにあり、いくらか」という**ツール機能としての見取り図**であり、実際に画面を開いて設定する際にはこちらを、社内で導入方針を議論する際にはあちらを参照するとよい

## 最初の一歩

まず自分が普段使っているツール(ChatGPT・Gemini・Copilot・Claudeのいずれか)で、上記の対応表から「自分のツールのスケジュールタスク機能」を1つ特定し、送信・購買などを含まない軽い定型調査(業界ニュースの週次要約など)を1件登録してみる。エージェントモードを試す場合は、必ず後戻りしにくい操作(注文・送信)を含まない依頼から始める。

## 関連トピック

- [ChatGPTのエージェント機能(ChatGPT Work)とスケジュールタスク(Tasks)](./chatgpt-agent-mode-feature.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)
- [Google Geminiの基本](./google-gemini-basics.md)
- [Microsoft Copilotの基本](./microsoft-copilot-basics.md)
- [Claude(Anthropic)の基本](./claude-basics.md)

## 更新履歴

### 2026-09-07: ChatGPT Tasksのイベントトリガー追加、Gemini SparkのGoogle AI Pro拡大・Ultra値下げ、Copilot Coworkの「Automations」改称、GPT-6 Astra登場を反映して全体を最新化
- **内容**: (1)ChatGPTが2026年8月25〜26日にTasksへGmail/Slack/GitHubのイベントトリガーを追加し、無料プラン・Goにもスケジュール機能(最大3件、イベントトリガーは不可)を解放した点、(2)Gemini Sparkが2026年5月のGoogle AI Ultra値下げ(月$249.99→$99.99)とセットで登場し、2026年7月29日から米国・日本のGoogle AI Pro契約者(米国$19.99・日本¥2,900)にも対象拡大した点、(3)Copilot Cowork内の「Scheduled」タブが2026年8月に「Automations」へ改称されOutlookメール・Teamsメッセージのイベントトリガーを統合した点、および個人向けCopilotアプリとMicrosoft 365 Copilotアプリの統合(2026年8〜9月)、(4)2026年9月3日に発表されたGPT-6 Astra(ChatGPT Workの新モデル基盤)、(5)Claude Coworkのスケジュールタスクが2026年4月9日追加でファイル出現・アプリ状態変化・外部Webhookのイベントトリガーに対応済みである点とWeb/モバイルベータの継続状況を、それぞれ比較表・本文・料金表・実務例に反映。あわせてタイトル・タグの「ChatGPT Agent」表記を「ChatGPT Work」に修正(改称自体は2026年7月に発生済みだが表記の反映漏れがあったため)
- **出典**: [OpenAI: ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex)、[TechBriefly: OpenAI brings ChatGPT scheduling tool to free accounts](https://techbriefly.com/2026/08/26/openai-chatgpt-scheduling-tool-free-accounts/)、[Dataconomy: OpenAI Brings ChatGPT Scheduling Tool To Free Users](https://dataconomy.com/2026/08/26/openai-chatgpt-scheduling-tool-free-users/)、[claypier: ChatGPT Scheduled Tasks Come to Free Accounts, With Gmail, Slack and GitHub Event Triggers](https://claypier.com/en/chatgpt-scheduled-tasks-free-tier/)、[CNBC: OpenAI announces rollout of GPT-6 Astra model](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)、[9to5Mac: OpenAI releasing major upgrade to ChatGPT and Codex with GPT-6 Astra](https://9to5mac.com/2026/09/04/openai-releasing-major-upgrade-to-chatgpt-and-codex-with-gpt-6-astra-details-here/)、[Engadget: The Google AI Ultra plan now starts at $100 a month](https://www.engadget.com/2176060/the-google-ai-ultra-plan-now-starts-at-100-a-month/)、[Google Japan Blog: Gemini Sparkが日本のGoogle AI Proユーザーにも展開](https://blog.google/intl/ja-jp/company-news/technology/gemini-spark-comes-to-japan/)、[HelenTech: Google、Gemini SparkをGoogle AI Proユーザーにも展開](https://helentech.jp/news-gemini-spark-pro-japan-89365/)、[usecarly: Gemini Connectors: Every App It Connects To in 2026](https://www.usecarly.com/blog/gemini-connectors/)、[Microsoft Community Hub: What's New in Microsoft Copilot | August 2026](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/what%e2%80%99s-new-in-microsoft-copilot--august-2026/4551960)、[agentandcopilot: Copilot Cowork Gains New Triggers, Automations](https://agentandcopilot.com/ai-and-copilots/copilot-cowork-gains-new-triggers-automations-to-help-manage-complex-tasks/)、[futurework.blog: Microsoft Copilot app – one app, new name, new icon, new URL](https://futurework.blog/2026/08/14/microsoft-copilot-app-one-app-new-name-new-icon-new-url/)、[Microsoft 365 Blog: Copilot Cowork is now generally available](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/)、[hatchworks: Building Agents with Claude: From Skills to Scheduled Tasks and Routines](https://hatchworks.com/blog/claude/building-agents-with-claude/)、[Claude Help Center: Schedule recurring tasks in Claude Cowork](https://support.claude.com/en/articles/13854387-schedule-recurring-tasks-in-claude-cowork)、[usecarly: Claude for Microsoft 365: What's Actually Available in 2026](https://www.usecarly.com/blog/claude-for-microsoft-365/)

### 2026-07-27: ChatGPT Agentの「ChatGPT Work」改称、Gemini Spark日本語対応、Copilot Coworkの使用量課金移行、Claude CoworkのWeb/モバイル展開を反映
- **内容**: (1)2026年7月9日にChatGPT Agentが独自ブラウザAtlasと統合の上「ChatGPT Work」に改称(Tasksは別機能として存続、ChatGPT自体もChat/Work/Codexの3モード構成に再編)、(2)Gemini Sparkが2026年7月16日に日本語対応・日本から利用可能になったが個人のGoogle AI Ultra契約が前提で法人Workspaceは非対応である点、同月下旬から米国のGoogle AI Proにも対象拡大している点、(3)Copilot Coworkが2026年6月16日のGA以降Copilot Creditによる使用量課金に一本化され2026年7月1日以降は課金設定必須になった点・Copilot Tasksタブが全ユーザーのデフォルトになった点、(4)Claude Coworkが2026年7月7日からWeb・モバイル(ベータ、Maxプラン先行)に拡大しリモートセッション化した点、7月21日の「Record a Skill」機能追加とMicrosoft 365書き込み連携の追加、をそれぞれ比較表・本文・料金表に反映して全体を最新化
- **出典**: [MacRumors: OpenAI Debuts ChatGPT Work Agent and New GPT-5.6 Models](https://www.macrumors.com/2026/07/09/openai-chatgpt-work/)、[Bloomberg: OpenAI Unveils ChatGPT Work Agent](https://www.bloomberg.com/news/articles/2026-07-09/openai-unveils-chatgpt-work-agent-to-field-tasks-for-hours)、[PYMNTS: OpenAI Launches ChatGPT Agent That Executes Complex Workflows](https://www.pymnts.com/news/artificial-intelligence/2026/openai-launches-chatgpt-agent-that-executes-complex-workflows/)、[ppc.land: OpenAI kills Atlas browser, folds it into new ChatGPT Work agent](https://ppc.land/openai-kills-atlas-browser-folds-it-into-new-chatgpt-work-agent/)、[OpenAI Help Center: Using credits for flexible usage in ChatGPT](https://help.openai.com/en/articles/12642688-using-credits-for-flexible-usage-in-chatgpt-freegopluspro)、[GIGAZINE: Google's 24/7 AI agent, Gemini Spark, is now available in Japanese](https://gigazine.net/gsc_news/en/20260716-gemini-spark-japanese/)、[note: Gemini Sparkの日本での使い方まとめ](https://note.com/csfive/n/nfe5b97fbfef2?hl=en)、[9to5Google: Gemini Spark rolling out to Google AI Pro users in the US](https://9to5google.com/2026/07/23/gemini-spark-google-ai-pro-us/)、[Digital Trends: Gemini Spark is no longer restricted to Google's priciest Ultra tier](https://www.digitaltrends.com/computing/gemini-spark-is-no-longer-restricted-to-googles-priciest-ultra-tier/)、[Microsoft 365 Blog: Copilot Cowork is now generally available](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/)、[Arraya Solutions: Microsoft Copilot Cowork Is Moving to Paid](https://www.arrayasolutions.com/insights/blog/2026/microsoft-copilot-cowork-is-moving-to-paid-what-it-and-business-leaders-need-to-know-before-july-1/)、[Quisitive: Copilot Cowork Pricing 2026](https://quisitive.com/copilot-cowork-pricing-2026-how-usage-based-billing-works/)、[TechCrunch: Claude Cowork expands to mobile and web](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/)、[NBC News: Anthropic will make Claude Cowork available to users via the cloud](https://www.nbcnews.com/tech/tech-news/anthropic-will-make-claude-cowork-available-users-cloud-rcna353218)、[Claude Help Center: Use Claude Cowork on web, desktop, and mobile](https://support.claude.com/en/articles/15520349-use-claude-cowork-on-web-desktop-and-mobile)、[ExplainX: Claude Cowork Record a Skill — July 2026](https://www.explainx.ai/blog/claude-cowork-record-a-skill-screen-recording-july-2026)

### 2026-07-07: 初版執筆
- **内容**: ChatGPT Agent/Tasks、Gemini Spark/Scheduled actions、Copilot Cowork・Copilot Actions・Agent Mode for Edge for Business・Copilot Tasks、Claude Cowork・Claude in Chrome・Claude Code Routinesの4社比較表を作成。エージェントモードとスケジュールタスクの構造的な違い、対応プラン・料金の仕組み、日本からの利用可否(Gemini Sparkが2026年7月時点で日本未提供である点)、「Cowork」という名称がAnthropicとMicrosoftで重複している点、プロンプトインジェクションリスクの度合いの違いを整理
- **出典**: [OpenAI: Introducing ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/)、[ChatGPT agent | OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent)、[Scheduled tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)、[TechTimes: Gemini Spark: Google's 24/7 Cloud AI Agent](https://www.techtimes.com/articles/317144/20260525/gemini-spark-googles-24-7-cloud-ai-agent-now-executes-tasks-third-party-apps.htm)、[TechTimes: Google Cuts AI Ultra to $100, Launches Gemini Spark Agent](https://www.techtimes.com/articles/316853/20260519/google-cuts-ai-ultra-100-launches-gemini-spark-agent-android-xr-glasses-i-o-2026.htm)、[Google: Gemini app launches scheduled actions](https://blog.google/products-and-platforms/products/gemini/scheduled-actions-gemini-app/)、[Google Support: Gemini Apps limits & upgrades](https://support.google.com/gemini/answer/16275805?hl=en)、[AI Agents Library: Gemini Spark Availability](https://www.aiagentslibrary.com/blog/gemini-spark-availability/)、[Microsoft 365 Blog: Copilot Cowork is now generally available](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/)、[TestingCatalog: Microsoft tests Researcher and Analyst agents in Copilot Tasks](https://www.testingcatalog.com/microsoft-tests-researcher-and-analyst-agents-in-copilot-tasks/)、[Microsoft Support: Browse with Copilot(Copilot Actions in Edge)](https://support.microsoft.com/en-us/topic/copilot-actions-in-edge-5ed5e17e-42df-40a3-984a-20420eba86e2)、[Windows Blog: Protect your enterprise from shadow AI(RSAC 2026、Agent Mode for Edge for Business)](https://blogs.windows.com/msedgedev/2026/03/23/protect-your-enterprise-from-shadow-ai-and-more-announcements-at-rsac-2026/)、[Anthropic: Claude Cowork](https://www.anthropic.com/product/claude-cowork)、[VentureBeat: Anthropic launches Cowork, a Claude Desktop agent](https://venturebeat.com/technology/anthropic-launches-cowork-a-claude-desktop-agent-that-works-in-your-files-no)、[Claude Code Docs: Automate work with routines](https://code.claude.com/docs/en/routines)、[Claude Help Center: Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
