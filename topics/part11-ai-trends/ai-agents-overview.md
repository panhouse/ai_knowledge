---
title: 「AIエージェント」とは何か(チャットボットとの違いと代表製品)
part: 11
chapter: 第1章 AI市場の動向
tags: [AIエージェント, ChatGPT Agent, Claude Agent SDK, Computer Use, Gemini, Manus, Devin, 自律型AI]
created: 2026-07-06
updated: 2026-07-06
---

# 「AIエージェント」とは何か(チャットボットとの違いと代表製品)

## これは何か

「AIエージェント」は2025〜2026年にかけてOpenAI・Google・Anthropicが揃って主力機能に据えているキーワードだが、「結局チャットボットと何が違うのか」が曖昧なまま導入を検討すると、期待外れに終わったり、逆に権限を与えすぎて事故につながったりする。AIエージェントとは、一言でいえば「ゴールだけを与えると、AIが自分でタスクを分解し、ブラウザ操作やコード実行などの**ツール利用**(AIが外部のアプリ・API・ファイルなどを実際に操作すること)を繰り返しながら、人が逐一指示しなくても最後まで作業を完了する仕組み」である。1問1答で終わるチャットボットとは、途中の「計画」「実行」「振り返り」を誰が担うかという点で根本的に異なる。

## 仕組み・背景

従来のチャットボットは「入力(質問)→出力(回答)」の1往復で完結し、次に何をするかは常に人間が決める。これに対しAIエージェントは、以下のような**ループ**(反復処理)を自分の判断で回す。

1. **認識・計画**: ゴールを読み取り、達成に必要な手順に分解する(タスク分解)
2. **ツール利用・実行**: ブラウザ操作、コード実行、ファイル編集、社内システムへのAPI呼び出しなど、実際に環境に働きかける
3. **振り返り・判断**: 実行結果を確認し、ゴールに近づいたか、次に何をすべきか(継続・修正・完了)を自分で判断する
4. 1〜3をゴールに到達するか、あらかじめ決めた回数・時間の上限に達するまで繰り返す

Anthropicはこの違いを「**ワークフロー**(人があらかじめ決めた手順通りにAIとツールを呼び出す仕組み)」と「**エージェント**(LLMが自分でツールの呼び出し方を都度決めるループ)」という対比で整理しており、最近は「エージェント=LLMがループの中で自律的にツールを使うこと」というシンプルな定義に落ち着きつつある([Anthropic: Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents))。ここでいう**自律性**とは、次の一手を人間ではなくAI自身が選ぶ度合いのことで、自律性が高いほど成果は柔軟になる一方、想定外の行動や誤りが途中で連鎖するリスクも増える。

エージェントが外部ツールを呼び出す際の「つなぎ方」を標準化する規格として、Anthropicが提唱した**MCP(Model Context Protocol)**のように、AIとツール・データソースを共通の作法で接続する仕組みも普及が進んでいる。どのベンダーのエージェントも、突き詰めれば「LLMの判断力」×「使えるツールの種類」×「安全に自律実行させるための制御(ガードレール)」の掛け算で性能が決まる。

## 使いどころ・使い分け

### チャットボットとAIエージェントの違い

| 観点 | 従来のチャットボット | AIエージェント |
|---|---|---|
| 入出力パターン | 1問1答(質問→回答)の単発対話 | ゴールを1回渡すと、複数ステップを自律的に実行して最終成果物を返す |
| 主体 | 次に何をするかは常に人間が指示 | 次の一手(どのツールを使うか等)をAI自身が判断 |
| 使うツール | 基本的にテキスト生成のみ(検索・画像生成程度の補助機能) | ブラウザ操作・コード実行・ファイル編集・社内システムAPI呼び出しなど実環境への操作 |
| 典型的な使いどころ | 文章のドラフト作成、質問への回答、要約 | 複数サイトを回っての情報収集と資料作成、フォーム入力、コードの実装〜PR作成 |
| 失敗時の挙動 | 誤った回答をその場で返すだけ(被害は限定的) | 誤った判断のまま次のステップに進み、被害が実環境(誤送信・誤操作)に及ぶ可能性がある |
| 人の関与 | 毎回のやり取りに人が介在 | 完了報告や要所の承認のみ人が確認する「監督」型に変わる |

### エージェント方式を使うべきか、チャットで十分か

| 判断軸 | チャット(単発の指示)で十分 | AIエージェントの導入を検討 |
|---|---|---|
| ステップ数 | 1〜2手で完結する | 複数システム・複数サイトをまたぐ多段階作業 |
| 成功basisの明確さ | 都度、人が良し悪しを判断したい | 「完了条件」を事前に言語化できる(例:3社の料金を表にまとめる) |
| 誤りの影響範囲 | 誤ってもすぐ気づいて直せる | 誤ると実害が出る(誤送信・誤発注・誤ったコードのデプロイ等)→承認フローが必須 |
| 反復性 | 一度きりの作業 | 定型的に繰り返す作業で、自動化の投資対効果が見込める |

不可逆的な最終判断(契約締結、対外発信、資金移動、人事評価など)は、たとえエージェントが実行できても人の最終承認を必須にする。エージェントは「下準備を高速化する」段階で使い、意思決定そのものは人に残すのが基本線。

## 実務での使い方

### 代表的なAIエージェント製品・機能(2026年7月時点)

| 提供元 | 製品・機能名 | できること(一言) |
|---|---|---|
| OpenAI | ChatGPT Agent(旧Operator。2025年8月にOperatorはChatGPT Agentへ統合) | ブラウザ操作・コード実行・ファイル/スプレッドシート編集を組み合わせ、Webサイト上での申込・比較・資料作成などを1つの指示で最後まで実行。ChatGPT Plus/Pro/Business/Enterpriseで利用可([OpenAI: Introducing ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/)) |
| Anthropic | Claude Computer Use / Claude Agent SDK | Computer Useはパソコン画面を認識してマウス・キーボード操作を行う機能(Claude Cowork/Claude Codeで利用可)。Agent SDKはClaude Codeと同じ基盤を使い、開発者が自社業務向けの自律エージェントを組み込むためのライブラリ([Anthropic: Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview)) |
| Google | Gemini Agent(旧Project Mariner。2026年5月に統合終了) / Gemini Enterprise(旧Agentspace) | Gemini AgentはChromeに統合されたブラウザ自動操作機能。Gemini Enterpriseは企業向けにエージェント基盤(旧Vertex AI/Agentspace)を統合したプラットフォーム([Google Cloud Next 2026報道](https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era)) |
| Manus(中国発のスタートアップ) | Manus(汎用自律エージェント) | サンドボックス化された仮想マシン上でブラウザ・ターミナル・ファイルシステムを実際に操作し、リサーチから資料作成まで1つの指示で並行実行。無料枠と従量制クレジット制のPro/Teamプランがある([Manus AI Pricing 2026](https://www.nocode.mba/articles/manus-ai-pricing)) |
| Cognition AI | Devin | コーディング専業の自律エージェント。開発チケットを受け取り、実装・テスト・デバッグ・PR作成までを人手を介さず実行することを狙った製品(月額500ドル、コードベースへのアクセスが前提)([2026 AI Agent比較記事](https://mcplato.com/en/blog/ai-agent-2026-comparison/)) |
| Perplexity | Comet(エージェント機能を内蔵したブラウザ) | Chromiumベースのブラウザに検索AIとエージェント機能を統合し、ページ要約・複数タブをまたいだ調査・フォーム入力や予約などの多段階操作を自動化。基本無料でデスクトップ/Android/iOS/Macに対応([Perplexity Comet 2026レビュー](https://nohacks.co/blog/agentic-browser-landscape-2026)) |

短期間でも製品名・提供形態が頻繁に変わる(OperatorがChatGPT Agentへ、Project MarinerがGemini Agentへ吸収されるなど)ため、ブランド名を覚えるより「どのツールを、どこまで自律的に使わせられるか」という機能軸で製品を見る方が実務では使いやすい。

### 業務での使いどころの例

- **競合・市場リサーチ**: 「競合A・B・Cの料金ページを見て比較表をスプレッドシートにまとめて」とChatGPT AgentやManusに指示し、複数サイト巡回とドキュメント作成を任せる
- **定型フォーム入力・申請業務**: 社内システムへの繰り返し入力や、複数サイトへの同一情報の転記をエージェントに任せ、最終送信前だけ人が確認する
- **コーディング業務の下準備**: バグチケットや軽微な機能追加をDevinやClaude Agent SDKベースの開発エージェントに渡し、PRのドラフトまで作らせてからレビューする
- **経費精算・データ突合**: 領収書ファイルの読み取りと会計システムへの入力をエージェントに任せ、金額不一致だけ人がチェックする

### 使い始める際の画面の場所(例)

- **ChatGPT**: メッセージ入力欄付近のツール選択メニューから「エージェントモード」を選択(Plus以上のプラン)
- **Claude**: Claude Cowork、またはClaude Code上でComputer Use/Agent SDKの機能を有効化(Pro/Max向け。2026年6月15日以降、Agent SDKの非対話実行は通常の対話利用分と別枠の月次クレジットで管理される)
- **Gemini**: Gemini Appの「Gemini Agent」機能、または法人向けはGemini Enterprise(旧Agentspace)経由

## 注意点・よくある誤解

- **「自律的=丸投げしてよい」ではない**: 自律性が高いほど、途中の誤りが次のステップに連鎖しやすい。特に複数ステップにまたがるタスクでは、1ステップ目の誤認識がそのまま最終成果物の誤りにつながる。重要な操作(送信・決済・公開)の直前には必ず人の承認ステップを挟む。
- **Webページ経由の「プロンプトインジェクション」に注意**: ブラウザ操作型のエージェントは、閲覧したWebページに埋め込まれた悪意ある指示文をそのまま実行してしまうリスクが指摘されている。エージェントに渡すログイン情報や権限は必要最小限にする。
- **コスト管理を忘れない**: エージェントは1回の指示で何十回もツール呼び出し・モデル推論を行うため、単発チャットに比べてトークン消費・クレジット消費が大きい。Manusのようなクレジット制サービスや、Claude Agent SDKの専用クレジット枠のように、通常の対話利用とは別会計になっている場合があるため、料金体系を事前に確認する。
- **製品の統廃合が早いことを前提に選定する**: OperatorはChatGPT Agentに、Project MarinerはGemini Agentに、それぞれ1年前後で統合・終了している。特定製品への過度な作り込みは避け、標準的なインターフェース(ブラウザ操作・ファイル操作・API連携)を軸に業務フローを設計する。
- **「エージェント」の定義はベンダーによって幅がある**: 単純な手順通りの自動化(ワークフロー)を「エージェント」と呼んで売っている製品もあれば、真に自律的にツール選択を行う製品もある。導入検討時は「次の一手を誰が決めるのか」を必ず確認する。

## 最初の一歩

リスクの低い定型リサーチ業務(例:「競合3社の料金ページを比較して表にまとめて」)をChatGPT AgentかClaude、Manusのいずれかに一度任せてみて、途中の判断過程(どのサイトを見て、何を根拠に結論を出したか)を実際に確認する。そこで信頼度を見極めてから、権限を要する業務(送信・決済・システム更新)への適用を検討する。

## 関連トピック

- [生成AIに向く業務・向かない業務の切り分け](../part10-business-practice/ai-task-suitability.md)
- [Difyとは何か](../part09-nocode-lowcode/dify-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: チャットボットとAIエージェントの違い(自律性・タスク分解・ツール利用・振り返りループ)、現在の代表的なAIエージェント製品(ChatGPT Agent、Claude Computer Use/Agent SDK、Gemini Agent/Gemini Enterprise、Manus、Devin、Perplexity Comet)の一覧、業務での使いどころとリスクを整理
- **出典**: [OpenAI: Introducing ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/), [OpenAI: Introducing Operator](https://openai.com/index/introducing-operator/), [Anthropic: Claude Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview), [Anthropic: Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8), [Anthropic: Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents), [TheNextWeb: Google Cloud Next 2026](https://thenextweb.com/news/google-cloud-next-ai-agents-agentic-era), [AndroidHeadlines: Project Mariner is Over](https://www.androidheadlines.com/2026/05/google-shuts-down-project-mariner-ai-agent.html), [No Code MBA: Manus AI Pricing 2026](https://www.nocode.mba/articles/manus-ai-pricing), [MCPlato: 2026 AI Agent Selection Guide](https://mcplato.com/en/blog/ai-agent-2026-comparison/), [No Hacks: The Agentic Browser Landscape in 2026](https://nohacks.co/blog/agentic-browser-landscape-2026)
