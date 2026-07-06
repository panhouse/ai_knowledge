---
title: MCP(Model Context Protocol)の基本
part: 8
chapter: 第4章 MCP
tags: [MCP, Model Context Protocol, AIエージェント, ツール連携, コネクタ]
created: 2026-07-06
updated: 2026-07-06
---

# MCP(Model Context Protocol)の基本

## これは何か

AIチャットに「Slackの未読を要約して」「Google Driveのこの資料を読んで」と頼んでも、そのままでは何もできない。ChatGPT・Claude・Geminiなど、AIの種類ごと・接続先(Slack、Notion、社内DB…)ごとに、バラバラな方法で「つなぎ込み」のコードを書く必要があったからだ。MCP(Model Context Protocol、モデルコンテキストプロトコル)は、この「AIと外部のツール・データを接続する方法」を統一するために2024年11月にAnthropicが公開したオープンな規格で、今ではOpenAI・Google・Microsoftなど主要ベンダーも対応を表明している業界標準になりつつある。よく「AIにとってのUSB-C(どの機器にも挿さる共通端子)」と例えられる。

MCPが解決するのは「N個のAIツール × M個の接続先」の組み合わせぶんだけ個別に連携コードを書かなければならない、という組み合わせ爆発の問題。MCP対応のAIとMCP対応の接続先さえあれば、間の配線は規格として共通化されている。

## 仕組み・背景

MCPの登場人物は3つに整理できる。

- **MCPホスト(Host)**: ユーザーが実際に使うAIアプリ本体(Claude Desktop、Claude Code、対応したIDE、ChatGPTデスクトップアプリなど)
- **MCPクライアント(Client)**: ホストの内部にいて、AIモデルからの要求をMCPの通信形式に変換し、MCPサーバーとやり取りする仲介役
- **MCPサーバー(Server)**: Slack・Google Drive・GitHub・社内DB・自社APIなど、外部のデータやツールを「MCPの作法で話せる」ように公開する側のプログラム

つまり「MCPサーバーを立てておけば、それに対応したどのAIアプリ(MCPクライアント)からでも同じやり方でつながる」という一対多の関係が作れるのが最大の利点である。サーバー1つ作れば、Claude・ChatGPT・各種IDEなど複数のAIアプリから使い回せる。

MCPサーバーが外部に公開する機能は主に3種類(MCPの「プリミティブ」と呼ばれる)。

- **Tools(ツール)**: AIが呼び出せる操作(例: 「Slackにメッセージを送る」「チケットを起票する」)
- **Resources(リソース)**: AIが参照できるデータ(例: 「このファイルの中身」「このDBのレコード」)
- **Prompts(プロンプト)**: よく使う指示のテンプレート

### Function Callingとの違い

このリポジトリでは[Function Calling(Tool Calling)の基本](function-calling-basics.md)を別トピックで扱っているが、両者は競合する技術ではなく、担っている層が異なる。

- **Function Calling**は、モデルが「この関数をこの引数で呼びたい」という意思表示を返す仕組みそのもの。1つのアプリの中で、モデルとツールをどう「会話」させるかという部分を担う。
- **MCP**は、その「呼び出す先のツール・データ」を、どのAIアプリからでも同じ手順でつなげられるように標準化した「配線・接続の規格」。

言い換えると、MCPサーバーの内部では最終的にモデルがFunction Calling(またはそれに相当する仕組み)でツールを呼び出しており、MCPはその手前の「接続そのもの」を毎回作り直さなくて済むようにする役割を持つ。「Function Callingは呼び出しの文法、MCPはその文法を使う相手(サーバー)を毎回開発しなくて済むようにする配線」とイメージすると整理しやすい。両者の違いを表にすると次のようになる。

| 観点 | Function Calling(Tool Calling) | MCP(Model Context Protocol) |
|---|---|---|
| 担っている層 | モデルとツールの「会話の文法」(モデルが呼び出し要求を返す仕組みそのもの) | AIアプリと外部サービスをつなぐ「配線・接続の規格」 |
| 主語 | 1つのAIモデル・1つのアプリの中で完結する仕組み | 複数のAIアプリ(クライアント)と複数の接続先(サーバー)をまたいで使い回せる仕組み |
| 実装単位 | ツール(関数)ごとにアプリ側でスキーマ定義・実行コードを書く | 接続先ごとに「MCPサーバー」を1つ用意すれば、対応する全クライアントから使い回せる |
| 再利用性 | 基本的にそのアプリ専用(他のAIアプリに移植するには作り直しが必要) | サーバーを1回作れば、Claude・ChatGPT・対応IDEなど複数クライアントから流用できる |
| 決める人 | 各AI開発元(OpenAI・Anthropic・Google)がAPI仕様を個別に決める | オープンな共通規格(2025年12月にAgentic AI Foundationへ移管され、特定企業に依存しない中立的なガバナンスに) |
| 組み合わせ数 | AIアプリ×接続先の数だけ個別実装が必要になりやすい(組み合わせ爆発) | AIアプリ・接続先とも「MCP対応」でありさえすれば配線は共通化される |

なお、2025年12月9日にAnthropicはMCPをLinux Foundation傘下の新組織「Agentic AI Foundation(AAIF)」に寄贈し、OpenAI・Block(共同創設)、Google・Microsoft・AWS・Cloudflare・Bloomberg(支援)が参加する、特定企業に依存しないガバナンス体制に移行した。これによりMCPは「Anthropicの規格」から「業界共通のオープンスタンダード」としての位置づけがより明確になっている。

## 使いどころ・使い分け

| 状況 | 向いている選択 |
|---|---|
| 1回だけChatGPTに質問して終わる、資料をその都度手動でアップロードして要約させる | MCP不要。通常のチャット操作で十分 |
| 社内チャットボットを、複数のAIアプリ(Claude・ChatGPT・自社IDEなど)から同じ社内システムにつなぎたい | MCP向き。サーバーを1つ整備すれば複数クライアントから使い回せる |
| Slack・Google Drive・GitHubなど、すでに世の中にMCPサーバーが用意されている定番SaaSと連携したい | MCP向き。既製のMCPサーバー(コネクタ)を有効化するだけで済むことが多い |
| 自社独自のDB・基幹システムなど、まだMCPサーバーが存在しない接続先と連携したい | MCPサーバーを自社で開発する必要がある(エンジニアの工数が発生) |
| 1つのAIアプリの中だけで完結する、単発の関数呼び出し(天気を調べる等)を実装したい | Function Callingで直接実装する方がシンプルな場合が多い |

判断基準は「複数のAIアプリ・複数の利用者にまたがって、同じ外部接続を繰り返し使い回すか」。使い回す予定がない一回限りの用途では、MCPサーバーを新規に作るコストに見合わないことが多い。

## 実務での使い方

### 主なMCPサーバー・クライアントの例(2026年7月時点)

- **クライアント(MCP対応のAIアプリ)**: Claude Desktop、Claude Code、ChatGPTデスクトップアプリ・ChatGPT Apps(2025年9月対応、2025年後半にはChatGPT本体にもMCPクライアント機能が本格搭載)、OpenAIのAgents SDK、Google Gemini(2026年半ばに自社サービス向けの公式MCP対応とGemini向けのマネージドリモートサーバーを提供開始)、Microsoft Copilot、各種AI対応IDE(Cursor、VS Code等)
- **サーバー(接続先の例)**: Slack、Google Drive/Google Workspace、GitHub(公式サーバーがGo言語で提供されリポジトリ・Issue・PR・CI/CD操作に対応)、Notion、Git、Postgres、Puppeteer(ブラウザ操作)など。Anthropicが公開する参照実装リポジトリ(`modelcontextprotocol/servers`)には、ファイル操作・Web取得・時刻変換など汎用的なサーバーの例が揃っている
- **公式MCPレジストリ**: 2025年9月に公開された公式レジストリ(`registry.modelcontextprotocol.io`)には、2026年5月時点で約9,600件のサーバー、バージョン違いを含めると約29,000件が登録されている。プロトコル自体は2025年12月にAnthropicからLinux Foundation傘下の「Agentic AI Foundation(AAIF)」に寄贈され、OpenAI・Block(共同創設)、Google・Microsoft・AWS・Cloudflare・Bloomberg(支援)が参加する中立的なガバナンス体制になった
- Claudeの「Connectors Directory(コネクタ ディレクトリ)」には、2026年7月時点で500件を超えるMCP連携が登録されている。また2026年1月には、Figma・Slackなど外部サービスのUIプレビューやインタラクティブ要素をチャット内に直接表示できる拡張仕様「MCP Apps」への対応も始まっている

### 非エンジニアがClaudeで既存コネクタを有効にする手順(画面操作のみ、コード不要)

1. claude.ai にログインし、画面左下のアカウントアイコン → 「設定」→ 「コネクタ」を開く
2. 「コネクタを参照」をクリックすると、Slack・Google Drive・Notionなど接続できるアプリの一覧が表示される。名前検索・カテゴリ絞り込みができる
3. 使いたいアプリを選ぶと、そのアプリ自体のログイン画面に遷移するので、普段使っているアカウントでログインし、Claudeからのアクセスを許可する
4. 設定が終わると、チャット画面の「+」メニューからいつでもそのコネクタを呼び出せる。プロンプト中でアプリ名(例:「Google Driveの◯◯という資料を見て」)を伝えるだけでも、Claudeが自動的にコネクタを使って応答する

自社独自のサーバー(社内APIなど)や、ディレクトリに載っていないリモートMCPサーバーを使いたい場合は、同じ「コネクタ」画面の「カスタムコネクタを追加」からMCPサーバーのURLを入力して接続する(こちらは事前にエンジニアがMCPサーバー自体を用意している必要がある)。

Claude Code(開発者向けCLIツール)からMCPサーバーに接続する設定は、コマンドラインでの登録が必要になるため開発者向けの作業になる。

### 料金・コストの考え方

MCP自体の利用に追加のライセンス料はかからないオープン規格だが、実際にはつなぐ先のサービス(Slack・GitHub等)の契約プランや、AIアプリ側のプラン(コネクタ機能が使えるのは有料プラン以上、というケースが多い)によって使える範囲が変わる。また、AIエージェントがMCP経由で何度もツールを呼び出す使い方をすると、その分APIのトークン消費・利用量が増える点も踏まえておく。

## 注意点・よくある誤解

- **MCP対応=安全とは限らない**: MCPサーバーに与える権限(読み取りだけか、書き込み・削除までできるか)は接続先ごとに異なる。特に社外で公開されている非公式のMCPサーバーを安易に信頼して認証情報を渡すと、データ漏えいや意図しない操作のリスクがある。信頼できる提供元(公式・大手ベンダー)のサーバーを優先し、権限は必要最小限に絞る
- **プロンプトインジェクションの新しい入口になる**: MCPの最大のセキュリティ課題は、[プロンプトインジェクション](../part03-risk-security/prompt-injection-basics.md)(AIに対して悪意ある指示を紛れ込ませ、意図しない動作をさせる攻撃)の攻撃面がMCP経由で大きく広がる点にある。代表的な手口は次の3つ。
  - **ツールポイズニング(tool poisoning)**: 一見普通のMCPサーバーが、ツールの説明文(description)の中に人間には見えにくい悪意ある指示を埋め込んでおき、AIがそれを「正規の指示」として実行してしまう
  - **ラグプル攻撃(rug pull)**: 導入時には安全なツール説明だったのに、利用者が承認した後でサーバー側がこっそり説明文を書き換え、危険な指示に差し替える
  - **confused deputy(混乱した代理人)問題**: 高い権限を持つAIエージェントが、外部から読み込んだ文書(例: GitHubのIssueやチケットの本文)に仕込まれた指示に従わされ、本来アクセスすべきでない社外の第三者に対して権限を「代理行使」させられてしまう(例: 公開Issueの内容がきっかけで非公開リポジトリの情報が外部に送信される)
  - 対策としては、MCPサーバーの提供元を信頼できる相手に限定する、ツールに渡す権限をタスクに必要な最小限にする、重要な操作(送信・削除・決済など)の前に人間の承認を挟む、可能であればツールの説明文やレスポンス内容を事前にレビュー・監視する、といった多層防御が推奨されている
- **「MCPを入れれば何でもできる」ではない**: MCPは接続の規格にすぎず、実際に何ができるかは接続先のMCPサーバーが何のToolsやResourcesを公開しているかに依存する。欲しい連携のMCPサーバーがまだ存在しなければ、自社で開発するかカスタムコードで対応するしかない
- **Function Callingと同じものだと誤解しやすい**: 前述のとおり、MCPは「接続の標準化」、Function Callingは「モデルがツールを呼び出す仕組み」で役割が異なる。両者は排他的ではなく、MCPサーバーの内部でFunction Calling相当の仕組みが動いていると理解するとよい
- **進化が非常に速い分野**: 2024年11月の登場から1年強でOpenAI・Google・Microsoftなど主要ベンダーが相次いで対応を表明し、2025年12月にはガバナンスもAgentic AI Foundationへ移管された。仕様・対応状況・利用可能なコネクタの一覧は数か月単位で更新されているため、導入判断の前には必ず公式情報で最新状況を確認する

## 最初の一歩

すでにClaudeの有料プランを使っているなら、「設定→コネクタ→コネクタを参照」から、普段使っているSlackかGoogle Driveのコネクタを1つ有効化し、「(接続したアプリ名)の最近の内容を教えて」と聞いてみることで、MCP経由の連携がどんな感覚かを体験できる。

## 関連トピック

- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [OpenAI APIの基本](openai-api-basics.md)
- [Claude(Anthropic)の基本](../part07-other-llm-tools/claude-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part03-risk-security/prompt-injection-basics.md)

## 更新履歴

### 2026-07-06: Function Callingとの比較表・ガバナンス動向・セキュリティ節を追加
- **内容**: Function CallingとMCPの違いを表形式で整理し、2025年12月にAnthropicがMCPをLinux Foundation傘下の「Agentic AI Foundation(AAIF)」に寄贈しOpenAI・Google・Microsoft等が参加する中立ガバナンスに移行したこと、公式MCPレジストリの登録件数(2026年5月時点で約9,600サーバー)、ChatGPT・Geminiの公式MCP対応状況、MCP Apps拡張を追記。「注意点」にツールポイズニング・ラグプル攻撃・confused deputy問題などプロンプトインジェクション関連のMCP固有リスクと対策を追加し、関連トピックにプロンプトインジェクションページへのリンクを追加
- **出典**: [Linux Foundation: Announces the Formation of the Agentic AI Foundation (AAIF)](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), [Anthropic: Donating the Model Context Protocol and establishing the Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation), [TechCrunch: OpenAI, Anthropic, and Block join new Linux Foundation effort](https://techcrunch.com/2025/12/09/openai-anthropic-and-block-join-new-linux-foundation-effort-to-standardize-the-ai-agent-era/), [OpenAI: OpenAI co-founds the Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/), [WorkOS: Everything your team needs to know about MCP in 2026](https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026), [Checkmarx Zero: 11 Emerging AI Security Risks with MCP](https://checkmarx.com/zero-post/11-emerging-ai-security-risks-with-mcp-model-context-protocol/), [Aptible: Prompt injection in MCP - how tool poisoning works](https://www.aptible.com/mcp-security/mcp-prompt-injection), [Invariant Labs: MCP Security Notification - Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks), [OWASP: MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning), [Simon Willison: Model Context Protocol has prompt injection security problems](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)

### 2026-07-06: 初版執筆
- **内容**: MCP(Model Context Protocol)の定義、ホスト・クライアント・サーバーの三者構成、Function Callingとの役割の違い(接続の標準化 vs 呼び出しの仕組み)、使いどころの判断基準、ClaudeでのMCPコネクタの有効化手順(画面操作)、主なMCPサーバー・クライアントの例、セキュリティ面の注意点を整理
- **出典**: [Model Context Protocol公式: What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro), [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), [OpenAI Developers: MCP and Connectors](https://developers.openai.com/api/docs/guides/tools-connectors-mcp), [Claude Help Center: Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities), [Google Cloud: What is Model Context Protocol (MCP)? A guide](https://cloud.google.com/discover/what-is-model-context-protocol), [GitHub: modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
