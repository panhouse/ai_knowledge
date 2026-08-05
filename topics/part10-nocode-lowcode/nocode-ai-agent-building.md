---
title: ノーコードでのAIエージェント構築(Dify・n8n・Makeでの実務例)
part: 10
chapter: 第4章 AIエージェント構築
tags: [AIエージェント, Dify, n8n, Make, ノーコード, ツール呼び出し]
created: 2026-07-06
updated: 2026-07-06
---

# ノーコードでのAIエージェント構築(Dify・n8n・Makeでの実務例)

## これは何か

[「AIエージェントとは何か」](../part11-ai-agents/ai-agent-basics.md)で触れた「LLM(大規模言語モデル)が自分でツールの呼び出し方を都度決めるループ」を、プログラミングなしで自社の業務に組み込みたい——このニーズに応えるのが、Dify・n8n・Makeといったノーコード・ローコードツールに搭載された「AIエージェント」機能である。これらのツールでは、あらかじめ決めた手順を順番に実行する「ワークフロー」と、状況に応じてAI自身がツールの使用順序・使用回数を判断する「エージェント」を、同じ画面上のパーツとして組み合わせられる。本ページは、[Difyワークフローの主要ノードと組み立て方](dify-workflow-nodes.md)・[n8nの基本](n8n-basics.md)・[Makeの基本](make-basics.md)で扱った各ツールの基礎知識を前提に、「エージェントをどう組み立て、どう業務に落とし込むか」に絞って解説する。

## 仕組み・背景

ノーコードツールにおける「エージェント」は、どのツールでもおおむね次の3点セットで構成される。

1. **頭脳(LLM)**: 判断・計画を担うAIモデル(GPT・Claude・Gemini等)
2. **ツール(Tool)**: エージェントが呼び出せる「部品」。Web検索、社内API呼び出し、ナレッジベース検索、他のワークフロー・シナリオなど
3. **停止条件**: 目的を達成した、またはあらかじめ決めた上限(反復回数など)に達したら処理を止めるしくみ

この3点が揃うと、「開始→A→B→終了」のように処理順序が固定されたワークフローとは異なり、「ゴールだけを渡すと、AIが状況に応じてA・Bどちらを先に使うか、何度使うかを自分で決める」動作になる。これがワークフローとエージェントの本質的な違いである。

### Dify: Agentアプリ/Agentノード

Difyには「Agent」という専用のアプリタイプがあり、ダッシュボードから直接作成できるほか、2025年以降は通常のワークフロー内に「エージェント」ノードとして組み込むこともできる。内部の推論方式(エージェント戦略)は「Function Calling(モデルが構造化されたツール呼び出しを直接出力する方式)」と「ReAct(Think→Act→Observeを明示的に繰り返す方式。Function Calling非対応のモデルでも使える)」の2種類をMarketplaceからインストールして選択できる。エージェントが使えるツールは、Dify組み込みツール(Web検索など50種類以上)・HTTPリクエストで登録したカスタムツール・他のワークフローを「ツールとして公開」したものの3系統があり、暴走防止のための「Maximum Iterations(最大反復回数)」を既定値5・最大50の範囲で設定できる。

### n8n: AI Agentノード(Tools Agent)

n8nでは、LangChain(LLMアプリ構築用のOSSフレームワーク)をベースにした「AI Agent」ノードがエージェントの入れ物になる。このノードには最低1つの「Tool」サブノードを接続する必要があり、組み込みのHTTP Request ToolやCode Toolに加えて、既存のワークフロー全体を丸ごと「Sub-workflow(サブワークフロー)」としてツール化することもできる。さらに、別のAI Agentノードを「AI Agent Tool」として子エージェントに見立て、親エージェントが役割ごとに複数の子エージェントへ処理を振り分ける「マルチエージェント構成」も可能である。会話の文脈を保持したい場合は、Buffer Memory(発言をそのまま保持)やBuffer Window Memory(直近N件のみ保持)といったMemoryサブノードを接続する。

### Make: AI Agents

Makeは従来、シナリオ内の1ステップとしてAIモジュール(OpenAI・Anthropicなど)を呼ぶだけで、自律的な判断はできなかった。2025年4月に発表された「Make AI Agents」機能により、通常のシナリオを作るキャンバスと統合された専用の「AI Agents」ビルダーでエージェントを作成できるようになった。最大の特徴は、既存のMakeモジュールやシナリオをそのまま「ツール」として即席登録できる「Module Tools」機能と、エージェントがどのツールをなぜ選んだかをステップごとに可視化する「Reasoning Panel(推論パネル)」で、2026年に入ってからはこのビルダー自体が複数シナリオ・複数チームで共有できる次世代版に刷新されている。

## 使いどころ・使い分け

**エージェントの組み立て方の違い(2026年7月時点)**

| 観点 | Dify | n8n | Make |
|---|---|---|---|
| エージェントの入れ物 | Agentアプリ(単独)/ワークフロー内のAgentノード | ワークフロー内のAI Agentノード | 専用の「AI Agents」ビルダー(シナリオと連携) |
| ツールの追加方法 | 組み込みツール・カスタムツール・他ワークフローの「ツール化」 | Toolサブノードを接続(HTTP/Code/Sub-workflow/他Agent) | 既存モジュール・シナリオをそのまま「ツール」として登録(Module Tools) |
| 推論方式の選択 | Function Calling / ReAct を選択可能 | LangChainベースのTools Agent(内部でFunction Calling相当) | 内部処理は非公開だが、Reasoning Panelで判断過程を可視化 |
| ループ上限の設定 | Maximum Iterations(既定5・上限50)を明示的に設定 | 明示的な上限設定は薄く、ツール数・プロンプト設計で制御 | 明示的な上限設定は薄く、Reasoning Panelで挙動を確認しながら調整 |
| 強み | RAG(社内文書検索)との統合が深く、社内知識ベース連携エージェントに向く | 1,500以上のSaaS連携ノードを横断するエージェントを組みやすい | 既存のシナリオ資産をそのままツール化できる速さ、GUIの分かりやすさ |

**どのツールで作るべきかの判断軸**

- 社内文書・マニュアルに基づいた回答が主目的 → Dify(知識取得ノードをそのままエージェントのツールにできる)
- 連携先の業務SaaSが多数あり、複雑なデータ加工も必要 → n8n(Codeノードでの加工とAI Agentノードを組み合わせやすい)
- すでにMakeでシナリオ資産があり、それをそのままエージェントのツールとして再利用したい、GUIの分かりやすさを優先したい → Make

なお「そもそもエージェント化すべきか」という判断軸(ステップ数・外部実行の必要性・失敗時の被害の大きさ)は、ツール選びより前に検討すべき事項であり、[「AIエージェントとは何か」](../part11-ai-agents/ai-agent-basics.md)の「使いどころ・使い分け」を参照。手順が固定できる業務は、エージェント化せず通常のワークフロー(条件分岐)で組む方が、コストも安く動作も安定する。

## 実務での使い方

### Dify: Agentアプリ/Agentノードの作り方

1. Difyのダッシュボードで「最初から作成」→ アプリタイプ「Agent」を選ぶ(既存のワークフローに追加する場合はノード一覧から「エージェント」をキャンバスにドラッグする)
2. 設定パネルでモデルを選び、「エージェント戦略」からFunction CallingまたはReActをMarketplaceよりインストールして選択する
3. 「ツール」欄で、組み込みツール・HTTPリクエストで登録したカスタムツール・他のワークフローを公開した「ツール」を追加する
4. 「Maximum Iterations」を業務内容に応じて設定する(ツール呼び出しが多いタスクほど値を上げる。既定は5)
5. 画面右のプレビューでテスト実行し、どのツールが何回呼ばれたかのログを確認する
6. 問題なければ「公開する」で本番反映する

### n8n: AI Agentノードの作り方

1. 新規ワークフローで起点となるトリガーノード(Chat Trigger、Webhook等)を配置する
2. 「+」から「AI Agent」ノードを追加する
3. ノード内の「Chat Model」欄にモデルサブノード(OpenAI・Anthropic Chat Model・Google Gemini等)を接続する
4. 「Tool」欄に最低1つのToolサブノードを接続する(HTTP Request Tool、既存ワークフローをSub-workflow Toolとして登録、または別のAI Agentノードを「AI Agent Tool」として子エージェントに接続する、のいずれか)
5. 会話の文脈を保持したい場合は「Memory」欄にBuffer Window Memory等を接続する
6. 「Execute Workflow」でテスト実行し、エージェントがどのToolを何回呼んだかのログ(実行結果パネル)を確認する
7. 問題なければ画面右上のトグルで「Active」にする

### Make: AI Agentsの作り方

1. 左メニューの「AI Agents」→「Create agent」をクリックする
2. AIプロバイダー(OpenAI・Anthropic・Gemini等)を接続し、エージェントの「頭脳」となるモデルを設定する
3. システムプロンプトの欄に、エージェントの役割・振る舞い・トーンを記述する
4. 必要であれば「Knowledge」にファイルをアップロードし、参照させる社内資料を登録する
5. 「Add tool」から既存のシナリオ、または「Module Tools」で個別のモジュールをそのままツールとして登録する
6. Reasoning Panelでテスト実行し、エージェントがどのツールをどの順で選んだか、その理由をステップごとに確認する
7. 既存シナリオの「Run an Agent」モジュールから呼び出すか、チャットUIとして公開する

### 実務例1: 問い合わせの自動振り分け(ルーティング)エージェント

問い合わせフォーム・メール・チャットで受け付けた内容を、単純なカテゴリ分類だけでなく「まず何を試すべきか」までエージェントに判断させる構成。n8nで組む場合、以下のツールをAI Agentノードに接続する。

- **ナレッジ検索Tool**: 社内FAQ・マニュアルを検索するHTTP Request Tool(またはDifyの知識取得ワークフローをAPI経由で呼び出すもの)
- **CRM登録Tool**: 問い合わせ内容をCRM(Salesforce・HubSpot等)にチケット登録するHTTP Request Tool
- **Slack通知Tool**: 担当チームへの通知を送るSlackノードをツール化したもの

**AI Agentのシステムプロンプト例(コピペ可)**

```
あなたは問い合わせ対応の一次窓口エージェントです。
ユーザーからの問い合わせ本文を読み、次の手順で対応してください。

1. まずナレッジ検索Toolで、問い合わせ内容に対応するFAQ・マニュアルが
   既にあるか確認する
2. 十分な回答が見つかった場合は、その内容をもとに返信文を作成して終了する
3. 見つからない場合、またはクレーム・契約変更など個別対応が必要な内容の場合は
   CRM登録Toolでチケットを作成し、Slack通知Toolで担当チームに概要を知らせる
4. どのツールも使わずに自分の知識だけで回答してはいけない
   (事実確認できない内容は「確認します」と回答すること)
```

分類だけを行う従来の質問分類器ノード([Difyワークフローの主要ノードと組み立て方](dify-workflow-nodes.md)参照)と異なり、「まずナレッジを検索し、見つからなければ初めてチケットを起票する」という条件次第で手順そのものが変わる判断を、AI自身に任せられる点がエージェント化のメリットになる。

### 実務例2: 社内ITヘルプデスクエージェント

「パスワードをリセットしたい」「VPNに繋がらない」といった社内からの問い合わせに対応する、Difyで組むエージェント構成の例。

- **知識取得(ツール化)**: 社内Wiki・IT運用手順のナレッジベースを検索するツール
- **チケット発行Tool**: ITSM(IT Service Management)システムのAPIをHTTPリクエストツールとして登録
- **エスカレーション通知Tool**: 対応不能な内容をSlack/Teamsの担当チャンネルに通知するツール

**Agentのシステムプロンプト例(コピペ可)**

```
あなたは社内ITヘルプデスクのエージェントです。
社員からの問い合わせに対して、次の方針で対応してください。

- パスワードリセット・アカウントロック解除など手順が確立している内容は、
  知識取得ツールで手順を検索し、その場で回答する
- 手順を検索しても解決しない、または個別の設定変更が必要な内容は、
  チケット発行Toolで担当部署宛にチケットを作成する
- セキュリティインシデントの疑いがある内容(不審なログイン通知など)は、
  即座にエスカレーション通知Toolを使い、自分で解決しようとしない
```

いずれの例も、「AIに何を自律判断させ、どこで人間・システムに引き渡すか」をシステムプロンプトで明文化しておくことが、精度と安全性の両方を左右する。

## 注意点・よくある誤解

- **ツールを増やすほどコストとレイテンシが跳ねる**: エージェントは1回の依頼で「どのツールを使うか」の判断そのものにもLLM呼び出しを使うため、ツール呼び出し1回ごとにDifyのメッセージクレジット・Makeのクレジット・n8nの実行回数が積み上がる。ツールは業務に必要な最小限に絞る。
- **ループ上限を必ず設定する**: DifyのMaximum Iterations(既定5)のような上限を設けないと、ツールの結果が期待通りでない場合にエージェントが同じ判断を繰り返す「暴走」が起きやすい。n8n・Makeでも、システムプロンプトに「最大◯回試して解決しなければ人間にエスカレーションする」旨を明記し、事実上の上限を設けておく。
- **手順が固定できる業務はエージェント化しない**: 「必ずA→B→Cの順で処理する」と決まっている業務にエージェントを使うと、判断のブレによる誤動作リスクが増えるだけでコストも上がる。条件分岐で書けるものは通常のワークフローノード(IF/ELSE、ルーター)で組む。
- **ツールの説明文(description)が精度を左右する**: エージェントはツール名と説明文だけを見て「今この場面で使うべきか」を判断する。説明文が曖昧だと、本来使うべきでないツールを誤って呼び出す。「いつ使うべきか」「何を渡すと何が返るか」をツールごとに明記する。
- **本番のCRUD権限をそのまま持たせない**: 試作段階のエージェントに、削除・更新系のAPIをそのままツールとして持たせると、判断ミス1回で実害が出る。[「AIエージェントとは何か」](../part11-ai-agents/ai-agent-basics.md)の「承認不要な操作/承認必須な操作」の考え方をツール設計にも適用し、送信・削除・決済系のツールは人間の承認ステップを挟む構成にする。
- **デバッグの難易度が上がる**: MakeのReasoning Panelのように判断過程が可視化されるツールもあるが、複雑なツール構成になるほど「なぜその判断をしたか」の追跡が難しくなる。まずツール1〜2個の最小構成で動作確認し、問題なければツールを増やしていく。

## 最初の一歩

いま使っているツール(Dify・n8n・Makeのいずれか)で、ツールを1つだけ接続した最小のエージェントを1つ作り、「ツールを使うべきか、使わずに回答すべきか」をAI自身に判断させてみる。うまく判断が割れる境界のケースを2〜3個試すと、システムプロンプトやツールの説明文をどう書き換えるべきかが見えてくる。

## 関連トピック

- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [Difyワークフローの主要ノードと組み立て方](dify-workflow-nodes.md)
- [n8nの基本](n8n-basics.md)
- [Makeの基本](make-basics.md)
- [Function Calling(関数呼び出し)の基本](../part09-api-development/function-calling-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: ワークフローとエージェントの違いを「頭脳・ツール・停止条件」の3点セットで整理し、Dify(Agentアプリ/Agentノード、Function Calling/ReAct戦略、Maximum Iterations)・n8n(AI Agentノード、Toolサブノード、Sub-workflow Tool、AI Agent Toolによるマルチエージェント、Memoryサブノード)・Make(AI Agents、Module Tools、Reasoning Panel)それぞれのエージェント構築方法と画面操作手順、ツール選びの判断軸、問い合わせ自動振り分け・社内ITヘルプデスクの実務例(コピペ可能なシステムプロンプト付き)、ツール数とコスト・ループ上限・権限設計などの注意点を整理
- **出典**: [Dify Docs: Agent](https://docs.dify.ai/en/use-dify/nodes/agent)、[Dify Docs: Key Concepts](https://docs.dify.ai/en/use-dify/getting-started/key-concepts)、[Dify Blog: Agent Node Introduction](https://dify.ai/blog/dify-agent-node-introduction-when-workflows-learn-autonomous-reasoning)、[n8n Docs: AI Agent node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)、[n8n Docs: Tools Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent)、[n8n Docs: AI Agent Tool node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent)、[n8n Docs: Simple Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow)、[Make: AI Agents](https://www.make.com/en/ai-agents)、[Make Help Center: Step 1. Set up the AI agent](https://help.make.com/step-1-set-up-the-ai-agent)、[Make Help Center: Step 2. Create the AI agent's tools](https://help.make.com/step-2-create-the-ai-agents-tools)、[Make Blog: Introducing the visual next generation of Make AI Agents](https://www.make.com/en/blog/next-generation-make-AI-agents)
