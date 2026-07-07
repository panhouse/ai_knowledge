---
title: "A2A(Agent2Agent)プロトコルの基本"
part: 9
chapter: 第4章 MCP・エージェント連携
tags: [A2A, Agent2Agent, MCP, AIエージェント, マルチエージェント]
created: 2026-07-07
updated: 2026-07-07
---

# A2A(Agent2Agent)プロトコルの基本

## これは何か

自社の受発注AIエージェントと、取引先が使う在庫管理AIエージェントを直接やり取りさせたい——このように**組織やベンダーをまたいだAIエージェント同士**を連携させようとすると、開発元も作り方も異なるエージェント同士をどう「握手」させるかが問題になる。A2A(Agent2Agent Protocol、エージェント間プロトコル)は、この「エージェント対エージェント」の連携を標準化するためにGoogleが2025年4月9日に発表したオープンな規格で、現在はLinux Foundation傘下のプロジェクトとして企業に依存しない形で運営されている。

似た名前が挙がりやすい[MCP(Model Context Protocol)の基本](mcp-basics.md)は「AIとツール・データをつなぐ」規格であり、A2Aは「AIエージェント同士をつなぐ」規格である。両者は競合ではなく、実務では組み合わせて使うことを前提に設計されている。

## 仕組み・背景

A2Aの登場人物は2つに整理できる。

- **クライアントエージェント(Client Agent)**: ユーザーの依頼を受け、他のエージェントに仕事を依頼する側
- **リモートエージェント(Remote Agent)**: 依頼を受けて実際にタスクをこなす側(社外の販売代理店エージェント、他部門の専門エージェントなど)

MCPの「ホスト・クライアント・サーバー」という上下関係と違い、A2Aの2者は基本的に**対等**な関係にある。「AIとツールをつなぐ」MCPが縦方向(モデル→ツール・データ)の接続だとすれば、A2Aは横方向(エージェント→エージェント)の接続だとイメージすると整理しやすい。

### Agent Card(エージェント名刺)による能力の公開

リモートエージェントは、自分が「何ができるか」を`Agent Card`と呼ばれるJSON形式のファイルで公開する。名前・説明・対応言語やデータ形式、実行できる作業(スキル)の一覧、必要な認証方式などが書かれた、いわば「エージェント版の名刺・スペック表」である。

Agent Cardは`https://(エージェントのドメイン)/.well-known/agent-card.json`という決まった場所(well-known URI)に置くのが標準的な公開方法で、クライアントエージェントはこのURLにアクセスするだけで、初対面のエージェントが何をしてくれるかを機械的に把握できる。2026年3月のv1.0では、このAgent Cardに電子署名を付けられる「Signed Agent Cards」が追加され、なりすましでない本物の提供元が発行したカードかどうかを検証できるようになった。

### タスクのライフサイクル

A2Aでは、依頼した仕事を`Task(タスク)`という単位で管理する。タスクには一意のIDが振られ、次のような状態を遷移していく。

`submitted(受付)` → `working(処理中)` → `input-required(追加情報待ち)` → `completed(完了)` / `failed(失敗)` / `canceled(取消)` / `rejected(拒否)`

クライアントエージェントは、このタスクの状態を定期的に問い合わせる(ポーリング)か、SSE(Server-Sent Events)というリアルタイム更新の仕組みで進捗を受け取り、完了時には成果物(artifact、例: 見積書・レポートなど)を受け取る。旅行の手配を丸ごと1回のやり取りで終わらせるのではなく、時間のかかる作業や、途中でエージェント側から「あと1つ情報がほしい」と聞き返される作業にも対応できるように設計されている。

通信の基盤にはHTTP(S)とJSON-RPCという標準的な技術が使われており、独自の通信方式を新たに覚える必要がない点もMCPと共通する設計思想である。

### ガバナンスの経緯

- 2025年4月9日: Googleが50社以上の技術・サービス企業とともにA2Aを発表
- 2025年6月23日: GoogleがA2Aの仕様・SDK・開発ツールをLinux Foundationに寄贈し、AWS・Cisco・Google・Microsoft・Salesforce・SAP・ServiceNowなどが参加する「Agent2Agentプロジェクト」として発足
- 2026年3月: v1.0(安定版)をリリース。Signed Agent Cards、支払いに関する拡張仕様「AP2(Agent Payments Protocol)」などが追加
- 2026年4月9日: 発足1周年時点で、対応組織150社超、GitHubスター22,000超、Python・JavaScript・Java・Go・.NETの5言語SDKが揃い、Microsoft Copilot Studio・Azure AI Foundry・Amazon Bedrock AgentCoreでの正式サポートを発表
- 2026年4月22日: Google Cloud Next 2026にてv1.2を発表

なお、MCPは2025年12月にAnthropicからLinux Foundation傘下の別組織「Agentic AI Foundation(AAIF)」に寄贈されている。A2AとMCPは同じLinux Foundationの傘の下にはあるが、**別々のプロジェクトとして並走して開発が進んでいる**規格であり、統合された単一の規格ではない点に注意したい。

## 使いどころ・使い分け

MCPとA2Aは役割が異なるため、どちらか一方を選ぶというより「どちらをどこに使うか」で考えるのが実務的である。

| 観点 | MCP(Model Context Protocol) | A2A(Agent2Agent Protocol) |
|---|---|---|
| つなぐもの | 1つのAIモデル・エージェント ⇔ ツール・データ(縦方向) | エージェント ⇔ エージェント(横方向、対等) |
| 典型的な使いどころ | Slack・Google Drive・社内DBなど「道具」への接続 | 他部門・他社・他ベンダーの「別のエージェント」への仕事の依頼 |
| 主な情報単位 | Tools(操作)・Resources(データ)・Prompts(定型指示) | Agent Card(能力の公開)・Task(依頼した仕事の単位) |
| 想定する相手の性質 | 受け身の道具・データソース | 自律的に判断し、追加確認や成果物の返送までこなす別のエージェント |
| 決める人 | Agentic AI Foundation(旧Anthropic主導、2025年12月移管) | Linux Foundation傘下のAgent2Agentプロジェクト(旧Google主導、2025年6月移管) |
| 2026年7月時点の普及度 | 業界標準として定着しつつある(登録サーバー数万件規模) | 大手ベンダーの対応は進むが、MCPほど広くは普及していない発展途上の規格 |

判断基準はシンプルで、「相手が受け身の道具・データか、それとも自律的に動く別のエージェントか」で選ぶ。実際の構築では、1つのエージェントの中でMCPを使って自社ツールに接続しつつ、そのエージェント自体をA2A経由で他部門・他社のエージェントから呼び出せるようにする、という**二層構成**が2026年時点でのエンタープライズ設計の定番になりつつある。

逆に、「社内の1つのAIアシスタントが複数のツールを使いこなせればよい」だけなら、A2Aを導入する必要はなくMCPだけで十分なケースが多い。

## 実務での使い方

### 2026年7月時点の対応状況

- **クラウド・プラットフォーム**: Microsoft Copilot Studio・Azure AI Foundry、Amazon Bedrock AgentCoreがA2Aを正式サポート(2026年4月時点でGA)。Google CloudのAgent Engine・Agentspace等もA2Aに対応
- **対応を表明・参加する企業**: Google、Microsoft、AWS、Salesforce、SAP、ServiceNow、Cisco、Workday、IBMなど150社超(2026年4月時点)
- **開発言語SDK**: Python、JavaScript、Java、Go、.NETの5言語で公式SDKが提供されている
- **業種別の活用例として紹介されているもの**: サプライチェーン(発注エージェント同士のやり取り)、金融・保険(審査・見積もりの自動化)、IT運用(複数の運用エージェントの連携)など

### エージェント連携を検討する際の確認ポイント(非エンジニア向け)

自社で直接A2Aサーバーを実装することは基本的にエンジニアの仕事だが、ビジネス側が業務システムやベンダーを選定する際には、次のような観点で会話できると選定・交渉で有利になる。

1. 導入を検討しているAIエージェント製品・SaaSが「A2A対応」「Agent Card」「エージェント間連携」といった言葉を製品資料で使っているかを確認する
2. 「他社・他ベンダーのエージェントと将来つなぐ予定があるか」を整理し、あるならA2A対応を選定基準に加える(社内で完結するなら必須ではない)
3. ベンダーに「MCPだけでなくA2Aにも対応しているか」「対応時期はいつか」を質問し、両対応のロードマップを持つベンダーかどうかを比較材料にする
4. 契約前に、連携するエージェント同士の間でどこまで自律的に判断・実行してよいか(承認フロー・権限の範囲)を確認する。これはA2Aの規格自体では決まらず、導入企業側の運用設計に委ねられる部分である

### 料金・コストの考え方

A2A自体はMCPと同様にオープンな規格であり、規格の利用そのものに追加ライセンス料はかからない。ただし、A2A対応のエージェント基盤(Azure AI Foundry、Bedrock AgentCore等)を使う場合はそのクラウド・プラットフォームの利用料がかかり、エージェント同士のやり取りが増えるほどAPI呼び出し・トークン消費のコストも増える点はMCPと同じ考え方で見積もる必要がある。

## 注意点・よくある誤解

- **「MCPとA2Aはどちらか1つを選ぶもの」という誤解**: 両者は担っている層が違う(道具への接続 vs エージェント同士の接続)ため、実務では併用が前提になる。どちらかで置き換えられるものではない
- **普及度はMCPほど高くない**: 2026年7月時点で対応ベンダー数・GitHubスター数は伸びているものの、MCPに比べると導入事例・対応ツールの層はまだ薄い。「A2Aさえ入れれば他社のどんなエージェントとも即連携できる」というのは楽観的すぎる期待で、実際には接続したい相手側もA2Aに対応している必要がある
- **実装・運用コストへの懐疑的な見方もある**: MCPが提供する機能(長時間タスクの管理、状態を持ったやり取りなど)とA2Aが目指す機能に重なりがあるとの指摘があり、「MCPに加えてA2A用の通信層まで二重に管理するコストに見合うか」を疑問視する声も出ている。導入前に自社のユースケースで本当に組織横断の対等なエージェント連携が必要かを見極めることが重要
- **ガバナンス移管とAnthropic側のMCPの移管を混同しない**: A2AはGoogle主導からLinux Foundation傘下の「Agent2Agentプロジェクト」(2025年6月移管)、MCPはAnthropic主導からLinux Foundation傘下の別組織「Agentic AI Foundation」(2025年12月移管)へと、それぞれ別の経緯・別の組織に移管されている。「同じ組織が両方を管理している」わけではない
- **Agent Card=安全性の保証ではない**: 署名付きAgent Card(Signed Agent Cards)は「本物の提供元が発行したカードか」を検証する仕組みであり、そのエージェント自体の振る舞いが安全であることまでは保証しない。連携するエージェントに与える権限(取引の実行範囲、参照できるデータの範囲など)は別途、自社の運用ルールとして設計する必要がある

## 最初の一歩

自社や取引先で「複数のAIエージェントを連携させたい」という構想が出てきたら、まずはベンダーの製品資料や導入担当者に「MCPとA2Aのどちらに、どこまで対応していますか」と一言聞いてみることから始めるとよい。答え方でそのベンダーがエージェント連携をどこまで見据えて設計しているかが見えてくる。

## 関連トピック

- [MCP(Model Context Protocol)の基本](mcp-basics.md)
- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [AIエージェントの基本](../part12-ai-trends/ai-agent-basics.md)

## 更新履歴

### 2026-07-07: 初版執筆
- **内容**: A2A(Agent2Agent Protocol)の定義、Googleによる2025年4月の発表からLinux Foundationへの移管(2025年6月)、Agent Cardとタスクのライフサイクル(submitted〜completed等)という仕組みの概要、MCPとの役割分担(縦方向のツール接続 vs 横方向のエージェント間連携)を軸にした比較表、2026年4月時点の対応ベンダー・GitHubスター数などの普及状況、A2Aの普及がMCPほど進んでいない現状と実装コストへの懐疑的な見方を整理
- **出典**: [Google Developers Blog: A2A – a new era of agent interoperability](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/), [Linux Foundation: Linux Foundation Launches the Agent2Agent Protocol Project](https://www.linuxfoundation.org/press/linux-foundation-launches-the-agent2agent-protocol-project-to-enable-secure-intelligent-communication-between-ai-agents), [Linux Foundation: A2A Protocol Surpasses 150 Organizations, Lands in Major Cloud Platforms](https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year), [Forbes: Key Tech Firms Unite As Google Donates A2A To Linux Foundation](https://www.forbes.com/sites/janakirammsv/2025/06/25/key-tech-firms-unite-as-google-donates-a2a-to-linux-foundation/), [A2A Protocol公式仕様: Agent Discovery](https://a2a-protocol.org/latest/topics/agent-discovery/), [A2A Protocol公式仕様: Specification](https://a2a-protocol.org/latest/specification/), [IBM: What Is Agent2Agent (A2A) Protocol?](https://www.ibm.com/think/topics/agent2agent-protocol), [Credal: What happened to A2A Protocol?](https://www.credal.ai/blog/what-happened-to-a2a-protocol)
