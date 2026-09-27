---
title: ノーコードでのAIエージェント構築(Dify・n8n・Makeでの実務例)
part: 10
chapter: 第4章 AIエージェント構築
tags: [AIエージェント, Dify, n8n, Make, ノーコード, ツール呼び出し, MCP]
created: 2026-07-06
updated: 2026-09-27
---

# ノーコードでのAIエージェント構築(Dify・n8n・Makeでの実務例)

## これは何か

[「AIエージェントとは何か」](../part11-ai-agents/ai-agent-basics.md)で触れた「LLM(大規模言語モデル)が自分でツールの呼び出し方を都度決めるループ」を、プログラミングなしで自社の業務に組み込みたい——このニーズに応えるのが、Dify・n8n・Makeといったノーコード・ローコードツールに搭載された「AIエージェント」機能である。これらのツールでは、あらかじめ決めた手順を順番に実行する「ワークフロー」と、状況に応じてAI自身がツールの使用順序・使用回数を判断する「エージェント」を、同じ画面上のパーツとして組み合わせられる。本ページは、[Difyワークフローの主要ノードと組み立て方](dify-workflow-nodes.md)・[n8nの基本](n8n-basics.md)・[Makeの基本](make-basics.md)で扱った各ツールの基礎知識を前提に、「エージェントをどう組み立て、どう業務に落とし込むか」に絞って解説する。

## 仕組み・背景

ノーコードツールにおける「エージェント」は、どのツールでもおおむね次の3点セットで構成される。

1. **頭脳(LLM)**: 判断・計画を担うAIモデル(GPT・Claude・Gemini等)
2. **ツール(Tool)**: エージェントが呼び出せる「部品」。Web検索、社内API呼び出し、ナレッジベース検索、他のワークフロー・シナリオ、MCPサーバーなど
3. **停止条件**: 目的を達成した、またはあらかじめ決めた上限(反復回数・実行時間など)に達したら処理を止めるしくみ

この3点が揃うと、「開始→A→B→終了」のように処理順序が固定されたワークフローとは異なり、「ゴールだけを渡すと、AIが状況に応じてA・Bどちらを先に使うか、何度使うかを自分で決める」動作になる。これがワークフローとエージェントの本質的な違いである。

### Dify: 「クラシックAgentノード」と新しい独立型「Agent」(ベータ)の2本立て

2026年9月時点のDifyには、性格の異なる2つのエージェント構築手段が併存している。

- **クラシックAgentノード**: 従来からある方式で、通常のワークフロー内に「エージェント」ノードとして組み込むか、単独の「Agentアプリ」として使う。内部の推論方式(エージェント戦略)は「Function Calling(モデルが構造化されたツール呼び出しを直接出力する方式)」と「ReAct(Think→Act→Observeを明示的に繰り返す方式。Function Calling非対応のモデルでも使える)」の2種類が公式プラグインとして提供され、Marketplaceの「Agent Strategies」からインストールして選ぶ。暴走防止のための「Maximum Iterations(最大反復回数)」を既定値5・最大50・最小1の範囲で設定できる仕組みは変わっていない。
- **新しい独立型「Agent」(ベータ)**: 2026年7月17日のv1.16.0でオープンベータとしてデフォルト有効化され、8月27日の公式発表「Introducing New Agent」で本格的に打ち出された刷新版。エージェントをワークフローに従属させず、モデル・プロンプト・ツール・ファイル設定を1か所にまとめた「独立したアプリ、または使い回せる部品」として作る設計に変わった。チャット形式で目的を伝える「Buildモード」を使うと、AIが設定を進めながら`build_note.md`という変更履歴ファイルを自動生成し、対話の中で得た手順を再利用可能な「スキル」として書き出す(手動でプロンプト・ツール・ファイルを直接編集することも可能)。スキルには、ワークスペース全体で共有する「ライブラリスキル」(1エージェントにつき最大20件)と、エージェント固有の`.zip`/`.skill`パッケージとして埋め込む「埋め込みスキル」(既定で最大50MB)の2種類がある。ツール・ナレッジ・MCPサーバーはワークスペースの「ツール」欄からそのまま追加でき、加えてv1.17.0(8月25日)で選択可能になったE2B(クラウド型)サンドボックスを含むLinuxサンドボックス内で、エージェントがセッション中にCLIツールをその場でインストールして一時的に使うこともできる。暴走防止の考え方もクラシック版のMaximum Iterationsとは異なり、既定で「1回の実行あたり最大500回のモデル呼び出し」「1時間で自動停止」という上限になっている。会社としてのDifyの全体像(ライセンス・料金プラン・MCP対応・可観測性など)は[Difyとは何か](dify-basics.md)を参照。

### n8n: AI Agentノード(Tools Agent)+ Human-in-the-Loop・MCP連携

n8nでは、LangChain(LLMアプリ構築用のOSSフレームワーク)をベースにした「AI Agent」ノード(現行はv3)がエージェントの入れ物になる。このノードには最低1つの「Tool」サブノードを接続する必要があり、組み込みのHTTP Request ToolやCode Toolに加えて、既存のワークフロー全体を丸ごと「Sub-workflow(サブワークフロー)」としてツール化することもできる。さらに、別のAI Agentノードを「AI Agent Tool」として子エージェントに見立て、親エージェントが役割ごとに複数の子エージェントへ処理を振り分ける「マルチエージェント構成」も可能である。会話の文脈を保持したい場合は、Buffer Memory(発言をそのまま保持)やBuffer Window Memory(直近N件のみ保持)、Redis・PostgreSQLなど外部ストアへの永続化に対応したMemoryサブノードを接続する。2026年に入ってからはLangChainをよりネイティブに統合したアップデート(通称「n8n 2.0」)によりAI関連ノードが70種類以上に拡充され、直近ではAI Agent/Agent Tool(いずれもv3)に「Force Tool Call on First Iteration(最初の応答では必ずツールを呼び出させる)」というオプションが追加された。プロンプトだけで動く小型・非準拠モデルが、ツールを使わず散文で答えてしまう問題への対策で、2回目以降の応答は制限を外し最終回答も返せるようにする設計になっている。また「MCP Client Tool」ノードを使えば、外部のMCPサーバー(Model Context Protocol対応のツール群)が提供する機能をそのままAI Agentのツールとして呼び出せる。もう1つの実務的な進化がHuman-in-the-Loop(人間による承認、以下HITL)で、AI Agentノードに接続した個々のツールに「実行前に人間の承認を必須にする」設定ができ、エージェントがメール送信・DB更新・Slack投稿といった重要な処理をしようとすると、Slack・Telegram・n8nのChatノード等に承認依頼が飛び、人間が承認するまで実行が止まる。なお2025年末の大型アップデートでCodeノードの実行がデフォルトで隔離環境(タスクランナー)上に限定され、Execute Command Nodeなど危険度の高いノードが既定で無効化されている点も継続している(詳細は[n8nの基本](n8n-basics.md)を参照)。

### Make: AI Agent(New)

Makeは従来、シナリオ内の1ステップとしてAIモジュール(OpenAI・Anthropicなど)を呼ぶだけで、自律的な判断はできなかった。2025年4月に発表された「Make AI Agents」機能に続き、2026年2月2日には作り直された新版「Make AI Agent(New)」がオープンベータで公開され、通常のシナリオを作るキャンバスと統合された専用ビルダーでエージェントを組み立てられるようになった。最大の特徴は、既存のMakeモジュールやシナリオをそのまま「ツール」として即席登録できる「Module Tools」機能と、エージェントがどのツールをなぜ選んだかをステップごとに可視化する「Reasoning Panel(推論パネル)」で、完成したエージェントは複数のシナリオ・チームをまたいで共有できる。2026年6月頃には有料プラン全体で一般提供(GA)されたと報じられているが、機能ごとに仕上がりにばらつきがあり、料金ページ上も一部機能に「ベータ」表示が残っている状態が2026年9月時点でも続いている。クレジット消費は、Make組み込みのAIプロバイダーを使う場合「エージェントの実行: 1操作=1クレジット+AIトークン量に応じた追加クレジット」「チャット: 1操作分+呼び出したツールの操作分+AIトークン量に応じた追加クレジット」「ナレッジ(PDF/DOCXの読み込み): 1操作分+1ページあたり10トークン相当」という組み合わせで決まる一方、OpenAIやAnthropic Claudeなど自分のAPIキーで接続する「カスタムAIプロバイダー」を選んだ場合はMake側のクレジット消費が1操作=1クレジットのみになり、見積りが立てやすい。カスタムAIプロバイダー接続は2025年11月6日以降、Coreプランを含むすべての有料プランで選択できる(詳細は[Makeの基本](make-basics.md)を参照)。

なお、Zapierも2025年に「Zapier Agents」を一般提供し、既存の9,000以上のアプリ連携をエージェントのツールとしてそのまま使えるようになっている。Zapier Agentsは2026年に入り、通常のZap(タスク課金)とは切り離された独立アドオン製品として再編され、課金単位も「アクティビティ(エージェントがツールを実行する・Web検索する・ナレッジを参照するなど1つ行動するたびに1件)」という専用の指標に変わった(Free 400アクティビティ/月、Pro 1,500アクティビティ/月で年払い約$33.33/月など)。Zapierの詳細・料金は[Zapierの基本](zapier-basics.md)を参照。「既にZapierで大量のZapを運用している」場合は、乗り換えずZapier Agentsで小さく試す選択肢も検討に値する。

## 使いどころ・使い分け

**エージェントの組み立て方の違い(2026年9月時点)**

| 観点 | Dify | n8n | Make |
|---|---|---|---|
| エージェントの入れ物 | クラシックAgentノード(ワークフロー内/単独アプリ)または新しい独立型「Agent」(ベータ) | ワークフロー内のAI Agentノード(v3) | 専用の「AI Agent(New)」ビルダー(シナリオのキャンバスと統合) |
| ツールの追加方法 | 組み込みツール・カスタムツール・他ワークフローの「ツール化」/新Agentはワークスペースの「ツール」欄・スキル・セッション内CLIインストール | Toolサブノードを接続(HTTP/Code/Sub-workflow/他Agent/MCP Client Tool) | 既存モジュール・シナリオをそのまま「ツール」として登録(Module Tools) |
| 推論方式・実行モデル | クラシック: Function Calling / ReAct を選択。新Agent: スキル・サンドボックスを備えた「1体のワーカー」として振る舞う設計 | LangChainベースのTools Agent(v3。小型モデル向けの「Force Tool Call on First Iteration」オプションあり) | 内部処理は非公開だが、Reasoning Panelで判断過程を可視化 |
| ループ・実行時間の上限 | クラシック: Maximum Iterations(既定5・上限50)。新Agent: 1回の実行で最大500回のモデル呼び出し、既定1時間で自動停止 | 明示的な上限設定は薄く、ツール数・プロンプト設計・HITL承認で制御 | 明示的な上限設定は薄く、Reasoning Panelで挙動を確認しながら調整 |
| 課金の考え方 | メッセージクレジット制(ツール呼び出しの都度消費) | ワークフロー実行(execution)回数制(1回の実行内なら追加課金なし) | クレジット制(操作1回分+ツール呼び出し・トークン消費量に応じた追加。カスタムAIプロバイダー接続なら1操作=1クレジットのみ) |
| 強み | RAG(社内文書検索)との統合が深く、新Agentはスキル・build_noteで「育てながら使い回す」エージェントを作りやすい | Human-in-the-Loop承認ゲート・MCP Client Toolで、重要操作の安全弁と外部ツール接続を柔軟に組める | 既存のシナリオ資産をそのままツール化できる速さ、GUIの分かりやすさ、Reasoning Panelでの可視化 |

**どのツールで作るべきかの判断軸**

- 社内文書・マニュアルに基づいた回答が主目的 → Dify(知識取得ノードをそのままエージェントのツールにできる)
- 1つのエージェントを育てながら複数の業務・ワークフローで使い回したい → Dify(新しい独立型Agent。スキル・build_noteで設定が可視化・再利用しやすい)
- 連携先の業務SaaSが多数あり、複雑なデータ加工も必要 → n8n(Codeノードでの加工とAI Agentノードを組み合わせやすい)
- 重要操作(送信・更新・削除・決済)の前に必ず人の承認を挟みたい → n8n(AI AgentノードのHuman-in-the-Loop機能が標準搭載)
- すでにMakeでシナリオ資産があり、それをそのままエージェントのツールとして再利用したい、GUIの分かりやすさを優先したい → Make

なお「そもそもエージェント化すべきか」という判断軸(ステップ数・外部実行の必要性・失敗時の被害の大きさ)は、ツール選びより前に検討すべき事項であり、[「AIエージェントとは何か」](../part11-ai-agents/ai-agent-basics.md)の「使いどころ・使い分け」を参照。手順が固定できる業務は、エージェント化せず通常のワークフロー(条件分岐)で組む方が、コストも安く動作も安定する。また、社内業務に組み込む「エージェント製品」全体の中での本ページの位置づけ(自作エディタ内エージェントか、既製の委任型エージェントか)は[主要AIエージェントの比較と選び方](../part11-ai-agents/ai-agent-tools-comparison.md)を参照。

## 実務での使い方

### Dify: クラシックAgentノード/Agentアプリの作り方

1. Difyのダッシュボードで「最初から作成」→ アプリタイプ「Agent」を選ぶ(既存のワークフローに追加する場合はノード一覧から「エージェント」をキャンバスにドラッグする)
2. 設定パネルでモデルを選び、「エージェント戦略」からFunction CallingまたはReActをMarketplaceよりインストールして選択する
3. 「ツール」欄で、組み込みツール・HTTPリクエストで登録したカスタムツール・他のワークフローを公開した「ツール」を追加する
4. 「Maximum Iterations」を業務内容に応じて設定する(ツール呼び出しが多いタスクほど値を上げる。既定は5)
5. 画面右のプレビューでテスト実行し、どのツールが何回呼ばれたかのログを確認する
6. 問題なければ「公開する」で本番反映する

### Dify: 新しい独立型「Agent」(ベータ)の作り方

1. 左メニューの「Agents」→「Create」→「Create from Blank」で新規作成する(既存のDSLファイルをインポートして始めることもできる)
2. エージェントの名前・役割(例:「リサーチアシスタント」)・説明を設定する
3. 「Configure」パネルでプロンプト・ツール・ファイルを手動で設定するか、「Build」モードでチャット形式に目的を伝え、AIに設定を進めさせる(進行中の変更は`build_note.md`に自動記録される)
4. 対話の中で得られた手順は「スキル」として自動生成される。ワークスペース共有の「ライブラリスキル」(最大20件)か、エージェント固有の「埋め込みスキル」(.zip/.skillパッケージ、既定50MB)を必要に応じて追加登録する
5. 「ツール」欄からMarketplace拡張・カスタムAPI・MCPサーバー・既存ワークフローの「ツール化」したものを追加する
6. テスト会話で動作を確認し、問題なければ「公開する」でWebアプリ化・API公開・他ワークフローからの再利用が可能な状態にする

### n8n: AI Agentノードの作り方

1. 新規ワークフローで起点となるトリガーノード(Chat Trigger、Webhook等)を配置する
2. 「+」から「AI Agent」ノードを追加する
3. ノード内の「Chat Model」欄にモデルサブノード(OpenAI・Anthropic Chat Model・Google Gemini等)を接続する
4. 「Tool」欄に最低1つのToolサブノードを接続する(HTTP Request Tool、既存ワークフローをSub-workflow Toolとして登録、外部MCPサーバーをMCP Client Toolとして接続、または別のAI Agentノードを「AI Agent Tool」として子エージェントに接続する、のいずれか)
5. 会話の文脈を保持したい場合は「Memory」欄にBuffer Window Memory等を接続する
6. メール送信・DB更新・決済など取り返しの付かない処理をツールとして接続する場合は、そのツールの設定で「人による承認を必須にする」(Human-in-the-Loop)をオンにする。承認依頼はSlack・Telegram・n8nのChatノード等に届く
7. 「Execute Workflow」でテスト実行し、エージェントがどのToolを何回呼んだかのログ(実行結果パネル)を確認する
8. 問題なければ画面右上のトグルで「Active」にする

### Make: AI Agent(New)の作り方

1. 左メニューの「AI Agents」→「Create agent」をクリックする
2. AIプロバイダー(Make組み込み、またはOpenAI・Anthropic・Gemini等を自分のAPIキーで接続する「カスタムAIプロバイダー」)を設定し、エージェントの「頭脳」となるモデルを選ぶ
3. システムプロンプトの欄に、エージェントの役割・振る舞い・トーンを記述する
4. 必要であれば「Knowledge」にファイルをアップロードし、参照させる社内資料を登録する
5. 「Add tool」から既存のシナリオ、または「Module Tools」で個別のモジュールをそのままツールとして登録する
6. Reasoning Panelでテスト実行し、エージェントがどのツールをどの順で選んだか、その理由をステップごとに確認する
7. 既存シナリオの「Run an Agent」モジュールから呼び出すか、チャットUIとして公開する

クレジット消費を予測しやすくしたい場合は、手順2でカスタムAIプロバイダー接続を選ぶと、Make側のクレジット消費が「1操作=1クレジット」のみに単純化できる(AIモデルの利用料はLLMベンダー側に別途発生)。

### 料金の目安(2026年9月時点)

エージェント機能そのものの利用料は原則プラン価格に含まれるが、「ツール呼び出しの回数」が実質的なコストを左右する点は3ツール共通である。目安は以下の通り(為替・キャンペーンで変動するため契約前に必ず公式ページで最新価格を確認すること)。

| ツール | 無料枠 | 有料プランの目安(月額・年払い時) | エージェント実行時に課金対象になるもの |
|---|---|---|---|
| Dify Cloud | Sandbox: トライアル用に200メッセージ(恒久無料枠ではない) | Professional $59〜(月5,000メッセージ)/ Team $159〜(月10,000メッセージ) | ツール呼び出し1回ごとにメッセージクレジットを消費(自社のLLM APIキーを登録するBYOK構成ならメッセージクレジットは原則消費しない) |
| n8n Cloud | 2026年に恒久無料プランを廃止(14日間の無料トライアルのみ、クレジットカード登録不要) | Starter 約$20〜(月2,500実行)/ Pro 約$50〜(月10,000実行)/ Business 約$800〜(月40,000実行、従業員20名未満は割引申請可) | ワークフロー実行(execution)単位で課金。1回の実行内で複数ツールを呼んでも追加課金は無い。チャットでワークフローを自動生成する「AI Workflow Builder」機能のクレジット(Starterで約2,300、Proで約5,700〜13,700)は別枠で、AI Agentノード自体の実行費用とは別勘定 |
| Make | Free: 月1,000クレジット | Core 約$9〜(月10,000クレジット〜)/ Pro 約$16〜/ Teams 約$29〜 | 標準モジュールは実行1回=1クレジットが基本だが、AI Agent(New)は操作クレジットに加え、呼び出したツール1回ごとの追加クレジット、消費トークン量に応じた追加クレジットが上乗せされるハイブリッド課金(カスタムAIプロバイダー接続時は1操作=1クレジットのみ) |

なお、Zapier Agentsは2026年にZap本体のタスク課金から独立したアドオン製品として再編され、「アクティビティ」という専用単位で課金される(Free 400アクティビティ/月、Pro 1,500アクティビティ/月で年払い約$33.33/月、Enterprise個別見積り)。既存のZapタスク枠とは別枠なので、「Zapierを契約していればAgentsも追加料金なしで使える」と誤解しないこと。詳細は[Zapierの基本](zapier-basics.md)を参照。

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

分類だけを行う従来の質問分類器ノード([Difyワークフローの主要ノードと組み立て方](dify-workflow-nodes.md)参照)と異なり、「まずナレッジを検索し、見つからなければ初めてチケットを起票する」という条件次第で手順そのものが変わる判断を、AI自身に任せられる点がエージェント化のメリットになる。CRM登録・通知のように実害の小さい操作は自動実行のままでよいが、返信の自動送信までエージェントに任せる場合は、n8nのHITL機能でいったん人の確認を挟む設計にすると安全である。

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

このような「手順が固まった業務知識」を、Difyの新しい独立型Agentで一度スキルとして書き出しておくと、同じ手順を他のワークフロー・別部署向けのエージェントからも呼び出して使い回せる。いずれの例も、「AIに何を自律判断させ、どこで人間・システムに引き渡すか」をシステムプロンプトで明文化しておくことが、精度と安全性の両方を左右する。

## 注意点・よくある誤解

- **Difyの「エージェント」は2系統あることを踏まえて情報を読む**: 2026年9月時点、Difyには推論方式(Function Calling/ReAct)を選ぶ従来の「クラシックAgentノード」と、スキル・サンドボックス・build_noteを備えた新しい独立型「Agent」(ベータ)が併存する。ネット上のチュートリアルや過去のブログ記事がどちらを指しているかで手順・設定項目が大きく異なるため、参照している情報がいつ時点の・どちらの機能の説明かを確認してから作業する。
- **ツールを増やすほどコストとレイテンシが跳ねる**: エージェントは1回の依頼で「どのツールを使うか」の判断そのものにもLLM呼び出しを使うため、ツール呼び出し1回ごとにDifyのメッセージクレジット・Makeのクレジット・n8nの実行回数が積み上がる。特にMakeはAI Agent(New)の操作1回分のクレジットに加え、ツール呼び出し回数・消費トークン量に応じた追加クレジットが二重に加算される課金体系になっているため、テスト段階でReasoning Panelを見ながら想定クレジット数を必ず概算しておく(カスタムAIプロバイダー接続にすると1操作=1クレジットに単純化できる)。ツールは業務に必要な最小限に絞る。
- **無料枠だけで本番検証はできない前提で計画する**: n8n Cloudは2026年に恒久無料プランを廃止しており(現在は14日間の無料トライアルのみ)、まとまった検証にはStarter以上の契約か、自前サーバーへのセルフホスト(Community Editionは無料)が必要になる。Difyの無料枠(Sandbox)も200メッセージのトライアル用途で、継続利用には有料プランへの切り替えが要る。
- **ループ・実行時間の上限を必ず確認する**: DifyのクラシックAgentノードはMaximum Iterations(既定5)、新しい独立型Agentは「1回の実行あたり最大500回のモデル呼び出し・既定1時間で自動停止」という異なる仕組みで暴走を防ぐ。n8n・Makeでも、システムプロンプトに「最大◯回試して解決しなければ人間にエスカレーションする」旨を明記し、事実上の上限を設けておく。
- **手順が固定できる業務はエージェント化しない**: 「必ずA→B→Cの順で処理する」と決まっている業務にエージェントを使うと、判断のブレによる誤動作リスクが増えるだけでコストも上がる。条件分岐で書けるものは通常のワークフローノード(IF/ELSE、ルーター)で組む。
- **ツールの説明文(description)が精度を左右する**: エージェントはツール名と説明文だけを見て「今この場面で使うべきか」を判断する。説明文が曖昧だと、本来使うべきでないツールを誤って呼び出す。「いつ使うべきか」「何を渡すと何が返るか」をツールごとに明記する。
- **本番のCRUD権限をそのまま持たせない**: 試作段階のエージェントに、削除・更新系のAPIをそのままツールとして持たせると、判断ミス1回で実害が出る。n8nならAI AgentノードのHuman-in-the-Loop設定で送信・削除・決済系のツールに承認ゲートを挟めるので、まずこの機能の利用を検討する。Difyの新しいAgentはサンドボックス内でCLIツールを自由にインストールできる分、公式にも「信頼できる利用者向け」と注意喚起されており、社外の不特定多数に触らせる用途には向かない。
- **デバッグの難易度が上がる**: MakeのReasoning Panel、Difyの`build_note.md`のように判断・設定変更の過程が可視化される仕組みも増えてきたが、複雑なツール構成になるほど「なぜその判断をしたか」の追跡は難しくなる。まずツール1〜2個の最小構成で動作確認し、問題なければツールを増やしていく。
- **n8nはツール側の実行環境の既定値が厳しくなっている**: Code Tool含むCodeノードの実行はデフォルトで隔離環境(タスクランナー)上に限定され、Execute Command NodeやLocalFileTriggerノードなど危険度の高いノードは既定で無効化される。既存のエージェント用ワークフローをアップグレードする際は、無効化されたノードに依存していないかを事前に確認する。

## 最初の一歩

いま使っているツール(Dify・n8n・Makeのいずれか)で、ツールを1つだけ接続した最小のエージェントを1つ作り、「ツールを使うべきか、使わずに回答すべきか」をAI自身に判断させてみる。Difyなら、まず新しい独立型Agent(ベータ)を1つ作り、チャットで目的を伝えるBuildモードを試してみると、スキル生成の感覚がつかみやすい。うまく判断が割れる境界のケースを2〜3個試すと、システムプロンプトやツールの説明文をどう書き換えるべきかが見えてくる。

## 関連トピック

- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [主要AIエージェントの比較と選び方](../part11-ai-agents/ai-agent-tools-comparison.md)
- [Difyとは何か](dify-basics.md)
- [Difyワークフローの主要ノードと組み立て方](dify-workflow-nodes.md)
- [n8nの基本](n8n-basics.md)
- [Makeの基本](make-basics.md)
- [Zapierの基本](zapier-basics.md)
- [Microsoft Copilot Studioによるカスタムエージェント作成の基本](../part06-custom-ai/copilot-agent-builder-basics.md)
- [Function Calling(関数呼び出し)の基本](../part09-api-development/function-calling-basics.md)

## 更新履歴

### 2026-09-27: Difyの新しい独立型Agent(ベータ)、n8nのHITL・MCP Client Tool、Make AI Agent(New)を反映して最新化
- **内容**: Difyの2系統のエージェント構築手段(従来のクラシックAgentノード=Function Calling/ReAct戦略・Maximum Iterations と、2026年7月のv1.16.0でベータ導入され8月27日の「Introducing New Agent」で本格発表された独立型「Agent」=Buildモードでの対話構築・build_note.md・ライブラリ/埋め込みスキル・E2Bサンドボックス・1回500回呼び出し/1時間タイムアウトの上限)を新設して整理。n8nの節にAI Agent/Agent Tool v3の「Force Tool Call on First Iteration」オプション、MCP Client Toolノード、Human-in-the-Loop(ツール実行前の人間承認)を反映し、実務手順・注意点・実務例にも組み込んだ。Make AI Agentsを「Make AI Agent(New)」(2026年2月2日公開、2026年6月頃に有料プラン全体でGAも一部機能はベータ表示継続)に更新し、クレジット消費ルール(カスタムAIプロバイダー接続時は1操作=1クレジット)を明記。料金目安の表をn8n・Makeの各基本ページの最新数値(n8n Starter/Pro/Business、Makeの月額・クレジット数)に合わせて更新し、Zapier Agentsの独立アドオン課金(アクティビティ単位)の記述も最新化。関連トピックに[主要AIエージェントの比較と選び方](../part11-ai-agents/ai-agent-tools-comparison.md)と[Microsoft Copilot Studioによるカスタムエージェント作成の基本](../part06-custom-ai/copilot-agent-builder-basics.md)への相互リンクを追加
- **出典**: [Dify Blog: Introducing New Agent](https://dify.ai/blog/introducing-new-dify-agent)、[Dify Blog: A New Chapter for Dify Agent](https://dify.ai/blog/a-new-chapter-for-dify-agent)、[Dify Docs: Build an Agent](https://docs.dify.ai/en/self-host/use-dify/build/new-agent/build)、[Dify Docs: Agent(クラシックノード)](https://docs.dify.ai/en/use-dify/nodes/agent)、[langgenius/dify Releases(v1.16.0/v1.17.0/v1.17.1)](https://github.com/langgenius/dify/releases)、[n8n Docs: Release notes](https://docs.n8n.io/release-notes)、[Make Help Center: Introduction to Make AI Agents (New)](https://help.make.com/introduction-to-make-ai-agents-new)、[Make Help Center: Credit usage for AI agents](https://help.make.com/credit-usage-for-ai-agents)、[Make: Announcing the next generation of Make AI Agents](https://www.make.com/en/blog/announcing-next-generation-make-ai-agents)、[Zapier Pricing 公式](https://zapier.com/pricing)、[n8nの基本(社内ページ、2026-08-20更新)](n8n-basics.md)、[Makeの基本(社内ページ、2026-09-23更新)](make-basics.md)、[Zapierの基本(社内ページ、2026-09-16更新)](zapier-basics.md)

### 2026-08-01: 料金・セキュリティ既定値・他ツール動向を最新化
- **内容**: Dify(Sandbox/Professional 59ドル/Team 159ドルのメッセージクレジット制)・n8n(Starter/Pro/Businessの実行回数制課金、2026年の恒久無料プラン廃止、AI Workflow Builderクレジットとの別勘定)・Make(2025年8月のオペレーション→クレジット制移行とAI Agentsのハイブリッド課金)の料金比較表を新設。n8n 2.0(2025年末)によるCodeノードの隔離実行既定化・危険ノードの既定無効化、n8nのAI Agent Toolでの子エージェント呼び出し改善を反映。Zapier Agents(2025年一般提供)への言及と関連ページへの導線を追加
- **出典**: [Dify Pricing(Comparedge)](https://comparedge.com/tools/dify-ai/pricing)、[Dify Pricing Teardown 2026(DEV Community)](https://dev.to/beton/dify-pricing-teardown-2026-42g5)、[Dify Docs: Agent](https://docs.dify.ai/en/use-dify/nodes/agent)、[langgenius/dify GitHub Issue #10382: Maximum Iterations](https://github.com/langgenius/dify/issues/10382)、[n8n Pricing(公式)](https://n8n.io/pricing/)、[n8n Blog: Introducing n8n 2.0](https://blog.n8n.io/introducing-n8n-2-0/)、[n8n Docs: Release notes 2.x](https://docs.n8n.io/changelog/release-notes-2.x)、[n8n Docs: Tools Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent)、[Make Help Center: Credit usage for AI agents](https://help.make.com/credit-usage-for-ai-agents)、[Make Pricing(公式)](https://www.make.com/en/pricing)、[Make: AI Agents](https://www.make.com/en/ai-agents)、[Zapier: AI Agents](https://zapier.com/agents)

### 2026-07-06: 初版執筆
- **内容**: ワークフローとエージェントの違いを「頭脳・ツール・停止条件」の3点セットで整理し、Dify(Agentアプリ/Agentノード、Function Calling/ReAct戦略、Maximum Iterations)・n8n(AI Agentノード、Toolサブノード、Sub-workflow Tool、AI Agent Toolによるマルチエージェント、Memoryサブノード)・Make(AI Agents、Module Tools、Reasoning Panel)それぞれのエージェント構築方法と画面操作手順、ツール選びの判断軸、問い合わせ自動振り分け・社内ITヘルプデスクの実務例(コピペ可能なシステムプロンプト付き)、ツール数とコスト・ループ上限・権限設計などの注意点を整理
- **出典**: [Dify Docs: Agent](https://docs.dify.ai/en/use-dify/nodes/agent)、[Dify Docs: Key Concepts](https://docs.dify.ai/en/use-dify/getting-started/key-concepts)、[Dify Blog: Agent Node Introduction](https://dify.ai/blog/dify-agent-node-introduction-when-workflows-learn-autonomous-reasoning)、[n8n Docs: AI Agent node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)、[n8n Docs: Tools Agent](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent/tools-agent)、[n8n Docs: AI Agent Tool node](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolaiagent)、[n8n Docs: Simple Memory](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.memorybufferwindow)、[Make: AI Agents](https://www.make.com/en/ai-agents)、[Make Help Center: Step 1. Set up the AI agent](https://help.make.com/step-1-set-up-the-ai-agent)、[Make Help Center: Step 2. Create the AI agent's tools](https://help.make.com/step-2-create-the-ai-agents-tools)、[Make Blog: Introducing the visual next generation of Make AI Agents](https://www.make.com/en/blog/next-generation-make-AI-agents)
