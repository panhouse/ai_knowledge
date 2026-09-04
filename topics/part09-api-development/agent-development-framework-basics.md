---
title: エージェント開発フレームワークの基本(OpenAI Agents SDK・Claude Agent SDK・LangGraph等)
part: 9
chapter: 第4章 MCP・エージェント連携
tags: [AIエージェント, OpenAI Agents SDK, Claude Agent SDK, LangGraph, Google ADK, CrewAI, マルチエージェント]
created: 2026-08-22
updated: 2026-08-22
---

# エージェント開発フレームワークの基本(OpenAI Agents SDK・Claude Agent SDK・LangGraph等)

## これは何か

「ゴールを渡すと自分で計画し、ツールを使いながら実行し切るAI」であるAIエージェントを、既製品として導入するのではなく自社で組み立てたい場合、ゼロからコードを書くのは非効率になりやすい。「次にどのツールを呼ぶか」「途中で失敗したらどう立て直すか」「複数のエージェントにどう分担させるか」といった処理は、どのエージェントを作る場合でも共通して必要になる部品だからだ。エージェント開発フレームワーク(Agent Framework)は、この「エージェントの頭の中の設計」に相当する共通部品(実行ループ・ツール呼び出し・状態管理・複数エージェントの分業)をあらかじめ用意しておき、開発者がゼロから作り直さずに済むようにするソフトウェア開発キット(SDK)群を指す。OpenAIのAgents SDK、AnthropicのClaude Agent SDK、LangChain社のLangGraph、GoogleのAgent Development Kit(ADK)、MicrosoftのAgent Framework、CrewAIなどが2026年8月時点の主なプレイヤーである。

このページはあくまで「開発者がコードでエージェントを組み立てる際に、どのSDKを選ぶか」という設計層を扱う。似た名前が並ぶ関連トピックとの境界は次のとおり。

- **[MCP(Model Context Protocol)の基本](mcp-basics.md)**: エージェントが外部のツール・データに「つながる配線の規格」。本ページのフレームワークは、その配線(MCP)を使う側の「頭脳・実行ループ」を組み立てる道具であり、両者は競合ではなく併用するものである
- **[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)**: Claude Code・ChatGPT Work・Salesforce Agentforceのような、すでに完成した「委任型の既製品」を導入して使う話。本ページは、それらの裏側にある仕組みを自社で一から作る側の視点である

## 仕組み・背景

エージェント開発フレームワークが提供する機能は、ベンダーが違ってもおおむね同じ部品に分解できる。

- **エージェントループ(agent loop)**: 「LLMに考えさせる→必要ならツールを呼ぶ→結果を見てまた考えさせる」を、ゴール達成か規定ステップ数までループさせる実行エンジン。フレームワークを使わないと、この繰り返し処理・エラー時の再試行・無限ループ防止などを自前で書く必要がある
- **ツール(Tools)**: LLMに使わせる関数・API・MCPサーバーの登録。[Function Calling(Tool Calling)の基本](function-calling-basics.md)がその土台になっている
- **ハンドオフ・サブエージェント(multi-agent orchestration)**: 1つのエージェントに全部を任せず、「調査担当」「執筆担当」「レビュー担当」のように役割を分けた複数のエージェントに処理を委任する仕組み。委任の設計思想がフレームワークごとに異なり、後述の比較表で最も差が出るポイントになる
- **状態・記憶(State/Memory/Sessions)**: 会話の履歴、中間結果、承認待ちの状態などを保持し、複数ターン・複数エージェントをまたいで引き継ぐ仕組み
- **ガードレール・人間承認(Guardrails/Human-in-the-loop)**: 危険な操作の前に処理を止めて人間の確認を挟む、入出力を検証するといった安全装置
- **可観測性(Tracing/Observability)**: エージェントが何を考え、どのツールをどの順で呼んだかを後から追跡できるログ機能。本番運用では実質必須の機能とされる

これらの部品を「最小限の抽象化で素早く組みたいか」「複雑な分岐・状態管理を厳密に制御したいか」のどちらに重心を置くかで、フレームワークの設計思想が分かれている。

## 使いどころ・使い分け

### 主要フレームワークの比較(2026年8月時点)

| フレームワーク | 提供元 | 言語 | ライセンス・料金 | 設計思想 | 向いている場面 |
|---|---|---|---|---|---|
| **OpenAI Agents SDK** | OpenAI | Python / TypeScript | MIT(OSS)。SDK自体は無料、実行時のモデルAPI課金のみ | 「Agents・Handoffs・Guardrails・Sessions・Tracing」の5つの原始的な部品に絞った軽量設計。2026年4月にサンドボックス実行・長時間タスク(long-horizon)対応を追加 | OpenAIのモデルを主軸に、シンプルな受け渡し型のマルチエージェントを素早く組みたい場合 |
| **Claude Agent SDK** | Anthropic | Python / TypeScript(コミュニティ版でGo・Rust・C++・Swiftも) | MIT(OSS)。SDK自体は無料、Claude APIのトークン課金のみ | Claude Codeの内部エンジン(hooks・subagents・sessions・組み込みツール・MCP統合)をそのままアプリ開発に開放したもの。2026年初頭に「Claude Code SDK」から改称 | ファイル編集・bash実行・Web検索など「Claude Codeが得意な作業」を、自社アプリに組み込みたい場合 |
| **LangGraph**(LangChain社) | LangChain | Python / TypeScript | コアはMIT(OSS)で無料。LangGraph Platformは月額35ドル〜、観測ツールLangSmithは無料〜1席39ドル/月 | 処理をノード(処理単位)とエッジ(遷移)からなるグラフとして明示的に設計し、状態(State)をグラフ全体で共有。分岐・リトライ・永続化を細かく制御できる | 条件分岐・人間承認・リトライを含む複雑な本番ワークフローを、モデルを問わず厳密に制御したい場合 |
| **Google ADK**(Agent Development Kit) | Google | Python / Java | Apache 2.0(OSS)。無料。Google Cloud上でホスティングする場合は別途利用料 | 親エージェントが子エージェントに委任する階層型マルチエージェントが標準。LiteLLM経由でAnthropic・Meta等のモデルも利用可、A2A・MCPをネイティブ対応 | Google Cloud / Gemini Enterprise上で、複数の専門エージェントを階層的に組織したい場合 |
| **Microsoft Agent Framework**(旧AutoGen+Semantic Kernel) | Microsoft | Python / .NET | MIT(OSS)。無料。Azure AI Foundry上でのホスティングは従量課金 | AutoGenの「エージェント同士の対話」という発想と、Semantic Kernelの企業向け機能(型安全・ミドルウェア・テレメトリ)を統合し、グラフ型ワークフローに統一。2026年4月にv1.0がGA(一般提供) | すでにAzure/.NET/Semantic Kernelの資産があり、企業向けガバナンス機能込みで作りたい場合 |
| **CrewAI** | CrewAI, Inc. | Python | コアはMIT(OSS)で無料。Enterprise版(CrewAI AMP/Factory)は個別見積もり | 「役割(Role)+タスク(Task)」で人間のチームのようにエージェント群を編成する、学習コストの低いオーケストレーション | 少人数のプロトタイプで、役割分担された定型フローを素早く試したい場合 |

**すでに退場・統合されたプレイヤー**: OpenAIの初期の実験的フレームワーク「Swarm」はAgents SDKに統合済み(移行推奨)。MicrosoftのAutoGenは2026年にメンテナンスモード(バグ修正のみ)へ移行し、後継のMicrosoft Agent Frameworkへの移行が公式に案内されている。この分野はまだ「統廃合が起きて当然」の段階にあると理解しておくとよい。

### 判断基準

1. **主力のLLMベンダー・既存のクラウド資産で決める**: OpenAIのモデルが主軸ならAgents SDK、Claudeの組み込みツールをそのまま使いたいならClaude Agent SDK、Azure/.NETの資産があるならMicrosoft Agent Framework、Google Cloud上で運用するならADK、というのが最も摩擦の少ない選び方(いずれもモデル横断で他社モデルを呼べるが、実際は自社モデルの機能が最も手厚い)
2. **ワークフローの複雑さで決める**: 単純な受け渡し・プロトタイプならAgents SDKやCrewAI、条件分岐・リトライ・厳密な状態管理が必要な本番システムならLangGraphが向く
3. **非エンジニアも設定に関わるか**: ノーコードでエージェントを組みたい場合はこのページの対象外で、[DifyでのAIエージェント構築](../part10-nocode-lowcode/nocode-ai-agent-building.md)を参照する方が近道
4. **既製品の導入で足りないか、まず確認する**: 定型業務の代行であれば、自作せずに[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)で紹介する既製品(Claude Cowork、Salesforce Agentforce等)の導入で足りることも多い。自社の業務ロジックに深く食い込む・既製品にない組み合わせが必要な場合に自作を検討する

## 実務での使い方

### 概念のツール横断対応表

同じ概念でもフレームワークごとに呼び方が違うため、ドキュメントを読む際の対応表として使える。

| 概念 | OpenAI Agents SDK | Claude Agent SDK | LangGraph | Google ADK | Microsoft Agent Framework | CrewAI |
|---|---|---|---|---|---|---|
| 単体のエージェント | `Agent` | SDK呼び出し自体(メインループ) | グラフの1ノード | `LlmAgent`等の`Agent` | `AIAgent` | `Agent`(role指定) |
| 別エージェントへの委任 | `Handoffs` | サブエージェント(subagents) | 別ノードへの遷移・サブグラフ | 階層的なサブエージェント委任 | ワークフロー内でのAgent呼び出し | タスク単位の委任(Crew内のTask割り当て) |
| ツール呼び出し | `Tools`(関数・MCPサーバー) | 組み込みツール(ファイル編集・bash等)+ MCP | Toolノード | `Tools`(関数・OpenAPI・MCP) | Tools/Functions | Tools |
| 状態・記憶 | `Sessions` | Sessions(会話の永続化) | `State`(グラフ全体で共有) | State/Memoryサービス | Thread/State | Memory(短期・長期) |
| 安全装置 | `Guardrails` | Hooks(実行の各局面で介入) | 条件分岐エッジで人間承認を挟む | Callbacks | Middleware | タスク単位のGuardrails |
| 可観測性 | `Tracing`(組み込み) | 外部ログ + OpenTelemetry連携 | LangSmith | Cloud Trace連携 | テレメトリ(OpenTelemetry) | CrewAI AMPの監視画面 |

### コピペで試せる最小コード例(OpenAI Agents SDK, Python)

```python
# pip install openai-agents
from agents import Agent, Runner

agent = Agent(
    name="Assistant",
    instructions="あなたは親切な日本語アシスタントです。ツールが必要な時だけ使ってください。",
    # tools=[...]  # 関数ツールやMCPサーバーをここに登録する
)

result = Runner.run_sync(agent, "東京の今日の天気を調べて一言で教えて")
print(result.final_output)
```

Claude Agent SDK(TypeScript)も発想は同じで、`@anthropic-ai/claude-agent-sdk`をインストールし、システムプロンプトと使わせたいツール(Claude Code同様のファイル編集・bash実行・MCPサーバー等)を指定してループを起動する形になる。どのフレームワークでも「指示(instructions)」「使わせるツール」「実行を回すランナー」の3点を用意する、という骨格は共通している。

### 料金・導入コストの考え方

- **SDK自体はほぼ無料**: 上表のとおり主要フレームワークはいずれもOSS(MIT/Apache 2.0)であり、SDKの利用に直接の licenses費用はかからない
- **実際のコストはモデルAPIの従量課金**: エージェントは1つのゴール達成のために何度もLLMを呼び出すため、単発チャットより消費トークンが大きくなりやすい([主要LLM APIの横断比較](llm-api-cross-tool-comparison.md)を参照)
- **観測・管理プラットフォームは別料金**: 本番運用では可観測性(トレーシング)が実質必須になり、LangSmith(無料〜1席39ドル/月)、LangGraph Platform(月額35ドル〜)、CrewAI Enterprise(個別見積もり)、Azure AI Foundryのホスティングなど、フレームワーク本体とは別の管理レイヤーに料金が発生することが多い

## 注意点・よくある誤解

- **バージョンがまだ荒い分野**: OpenAI Agents SDKはリリースから1年以上経ってもv0.x台で毎週のように更新が続いているなど、主要フレームワークの多くがまだ安定版(v1.0)に達していないか、達したばかりの段階にある。破壊的変更(既存コードが動かなくなる仕様変更)が起きる前提でバージョンを固定し、更新時は必ず変更内容を確認する
- **統廃合が起きやすい**: MicrosoftはAutoGenをメンテナンスモードにしてAgent Frameworkへ一本化し、OpenAIはSwarmをAgents SDKに統合した。特定フレームワークの独自機能に深く依存しすぎるとサービス終了時の移行コストが大きくなるため、MCPやOpenAPIのような標準規格に依存する部分を厚くし、フレームワーク固有の書き方に依存する部分は薄く保つ設計が安全
- **フレームワーク選びとモデル選びは別問題だが、実際には一致させた方が楽**: どのフレームワークも「他社モデルも呼べる」ことをうたっているが、実装が最も手厚くバグが少ないのは提供元自身のモデルとの組み合わせであることが多い
- **フレームワークを入れても、ガバナンス・評価は自動でついてこない**: 権限設計・承認フロー・監査ログといった運用面の論点は、既製品のAIエージェントと同様に必要になる。[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)の「注意点」で扱っている過大な権限付与・プロンプトインジェクションのリスクは、自作フレームワークでも同じように発生する
- **MCPと役割を混同しやすい**: 本ページのフレームワークは「エージェントの頭の中(計画・ツール呼び出しの制御・複数エージェントの分業)」を組み立てる道具であり、MCPは「その手前でどのツール・データにつながるかを標準化する配線」である。多くのフレームワークはMCPクライアントとしても動作し、両者は組み合わせて使うのが前提になっている

## 最初の一歩

すでに使っているAI APIのベンダー(OpenAIまたはAnthropic)に合わせて、公式クイックスタートに従い、1つの関数ツール(例: 現在時刻を返す関数)だけを登録した最小のエージェントをローカルで動かしてみる。ループが1周する感覚をつかめれば、複数ツール・複数エージェントへの拡張は同じ骨格の延長で理解できる。

## 関連トピック

- [MCP(Model Context Protocol)の基本](mcp-basics.md)
- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [Anthropic API(Claude API)の基本](anthropic-api-basics.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [DifyでのAIエージェント構築](../part10-nocode-lowcode/nocode-ai-agent-building.md)
- [A2A(Agent2Agent)プロトコルの基本](a2a-protocol-basics.md)

## 更新履歴

### 2026-08-22: 初版執筆
- **内容**: エージェント開発フレームワークの定義とMCP・Part11既製品との境界を整理し、OpenAI Agents SDK・Claude Agent SDK・LangGraph・Google ADK・Microsoft Agent Framework・CrewAIの6つを言語/ライセンス/料金/設計思想/向いている場面で比較。エージェントループ・ハンドオフ・状態・ガードレール・可観測性という共通部品の説明、フレームワーク横断の用語対応表、OpenAI Agents SDKの最小コード例、選定の判断基準、バージョンの不安定さ・統廃合リスクなどの注意点をまとめた
- **出典**: [OpenAI: The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/), [TechCrunch: OpenAI updates its Agents SDK to help enterprises build safer, more capable agents](https://techcrunch.com/2026/04/15/openai-updates-its-agents-sdk-to-help-enterprises-build-safer-more-capable-agents/), [OpenAI Agents SDK (Python) 公式ドキュメント](https://openai.github.io/openai-agents-python/), [Anthropic Claude Agent SDK Docs: Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview), [GitHub: anthropics/claude-agent-sdk-python](https://github.com/anthropics/claude-agent-sdk-python), [LangChain: LangGraph Platform pricing](https://www.truefoundry.com/blog/langgraph-pricing), [Google Developers Blog: Agent Development Kit - Making it easy to build multi-agent applications](https://developers.googleblog.com/en/agent-development-kit-easy-to-build-multi-agent-applications/), [GitHub: google/adk-python](https://github.com/google/adk-python), [Microsoft Learn: Microsoft Agent Framework Overview](https://learn.microsoft.com/en-us/agent-framework/overview/), [InfoQ: Microsoft Agent Framework Harness and Hosted Agents Reach General Availability](https://www.infoq.com/news/2026/08/agent-framework-harness-ga/), [AgentMarketCap: Microsoft Retires AutoGen](https://agentmarketcap.ai/blog/2026/04/13/microsoft-autogen-maintenance-mode-agent-framework-sunset-2026), [techjacksolutions: CrewAI Pricing - Open Source vs Enterprise Plans (2026)](https://techjacksolutions.com/ai-tools/crewai/crewai-pricing/)
