---
title: "n8nの基本"
part: 10
chapter: 第3章 自動化・連携ツール
tags: [n8n, ワークフロー自動化, ノーコード, セルフホスト, AIエージェント, 統合, MCP]
created: 2026-07-06
updated: 2026-07-23
---

# n8nの基本

## これは何か

「Gmailに新着メールが来たら内容をAIに要約させ、その結果をSlackに自動投稿したい」「CRMとGoogleスプレッドシートと社内システムをつないで、AIによる判断を1ステップだけ挟みたい」——こうした「複数の業務ツールをつなぐ自動化に、AIの処理を1パーツとして組み込みたい」というニーズに応えるのがn8n(エヌエイトエヌ)である。ノードと呼ばれる処理ブロックを画面上でつなぐビジュアル型のワークフロー自動化ツールで、Gmail・Slack・Google スプレッドシート・Notion・各種CRMなど1,500以上のサービスとの連携ノードを標準搭載し、OpenAI・Anthropic・GeminiなどのLLM(大規模言語モデル)を呼び出すAIノードも組み込みで使える。[Dify](./dify-basics.md)がAIチャットボット・RAGアプリづくりに特化したエンジンであるのに対し、n8nは「AIも使える汎用の業務自動化ツール」という位置づけが基本的な違いになる。2026年に入りLangChain(LLMアプリ構築用のOSSフレームワーク)をコア機能として統合し直す大型アップデートが進み、単なる連携ハブから「AIエージェントを組み立てる基盤」としての性格を強めている。

## 仕組み・背景

n8nはキャンバス上に「トリガー(処理の起点。例: 新着メール受信、スケジュール実行、Webhook受信)」と「アクション(実際の処理。例: Slackに投稿、スプレッドシートに書き込み、LLMを呼び出す)」のノードを配置し、線でつないで実行順序を定義する。この基本構造はDifyのワークフローと似ているが、n8nはもともと「多数の業務システムをつなぐ統合ハブ」として作られており、連携できるサービスの数と種類の広さが最大の特徴になっている。

n8nは2019年創業のドイツ発スタートアップが開発するOSS(オープンソースソフトウェア)で、ライセンスは独自の「Sustainable Use License(サステナブル・ユース・ライセンス)」という"fair-code(フェアコード)"モデルを採用している。ソースコードは誰でも閲覧・自社利用でき、社内の業務自動化に使う分には制限がないが、n8nの機能価値がそのまま製品価値になるような「n8nを丸ごとホスティングして転売する」といった使い方は禁止されている点がApache/MIT系の完全なオープンソースとは異なる。2025年3月に約60億円(6,000万ドル)、同年10月にはシリーズCで約270億円(1.8億ドル)を調達して評価額2,500億円(25億ドル)規模となり、2026年5月にはSAPが戦略出資して評価額が5,200億円(52億ドル)規模に達したと報じられるなど、資金調達面でも急拡大が続いている企業である。

### AI関連の仕組み

2023年以降、n8nはAIワークフロー機能を強化し、LangChainをベースにした「AI Agent(AIエージェント)」ノードを搭載している。2026年に入ってからはLangChainをよりネイティブに統合したアップデート(通称「n8n 2.0」)が投入され、AI関連ノードの種類が70以上に拡充されたと報じられている。AIエージェントワークフローは通常、次の要素で構成される。

- **トリガーノード**: Webhook・スケジューラー・チャットトリガーなどが処理の起点になる
- **AI Agentノード**: LangChainベースの推論で、状況に応じてどのツールを使うか自律的に判断する中核ノード。構造化ツール呼び出し(意図しない無限ループを防ぐ仕組み)や、途中の思考過程を実行ログに表示する「ReAct(推論と行動を交互に行う手法)」実行モードが利用できる
- **モデルノード(サブノード)**: AI Agentノードに接続する形でOpenAI(GPT-4o等)・Anthropic(Claude 3.5 Sonnet/Haiku等)・Google(Gemini)・Mistral・Groq・Ollama経由のローカルモデルなど、任意のLLMを選択できる
- **メモリノード**: 会話や処理の文脈を保持する。インメモリのほか、Redis・PostgreSQLなど外部ストアに永続化する選択肢も用意されている
- **ツールノード**: Web検索・社内API・他のワークフローなど、エージェントが呼び出せる外部機能を追加する

単発でLLMを呼ぶだけなら、AI Agentノードを使わずに「OpenAI」「Anthropic Chat Model」などの単体ノードをワークフローの1ステップとして組み込むだけでもよい。「毎回同じ手順を実行するワークフロー」と「AIが状況判断しながらツールを選ぶエージェント」の両方を、同じキャンバス上で組み合わせられるのがn8nのAI活用の特徴である。

**MCP(Model Context Protocol、AIとツール・データソースをつなぐ標準規格)への対応**も実務上のポイントになっている。n8nには「MCP Server Trigger」ノード(n8nのワークフローそのものをMCPサーバーとして外部のAIアシスタント・エージェントに公開する)と「MCP Client Tool」ノード(n8nのAI Agentから外部のMCPサーバーが提供するツールを呼び出す)が標準搭載されており、社内で作ったワークフローをClaude DesktopやCursorなど他のAIツールから呼び出したり、逆に外部のMCPサーバーが持つツール群をn8nのエージェントに使わせたりできる。

もう1つの実務的な進化が**Human-in-the-Loop(人間による承認、以下HITL)**の強化である。AI Agentノードに接続した個々のツールに「実行前に人間の承認を必須にする」設定ができ、エージェントがメール送信・DB更新・Slack投稿といった重要な処理をしようとすると、Slack・Telegram・n8nのChatノードなどに承認依頼が飛び、人間が承認するまで実行が止まる。AIエージェントを「見張りなしで本番運用する」ことへの不安に対する具体的な回答の1つになっている。

## 使いどころ・使い分け

| やりたいこと | 向いているツール |
|---|---|
| 複数のSaaS・DB・社内システムをつなぎ、AIをその中の1ステップとして使いたい | n8n |
| AIチャットボット・社内RAG検索アプリなど「AI利用そのもの」が主目的 | [Dify](./dify-basics.md)(RAG・プロンプト管理・チャットUIが標準装備) |
| プログラミング知識がないメンバーが直感的に自動化を組みたい | [Zapier](./zapier-basics.md)・[Make](./make-basics.md)(GUIがシンプルで学習コストが低い) |
| セキュリティ・データ主権を重視し自社サーバーで運用したい | n8n(セルフホスト無料。Make・Zapierはクラウド専用) |
| 複雑な条件分岐やコードによる細かいデータ加工が必要 | n8n(Code ノードでJavaScript/Pythonを直接実行できる) |
| 自社のワークフローを他のAIツール(Claude DesktopやCursor等)からも呼び出したい/外部のMCPツールをエージェントに使わせたい | n8n(MCP Server Trigger・MCP Client Toolノードが標準搭載) |
| AIエージェントに重要な操作(送信・更新・決済等)をさせる前に必ず人の承認を挟みたい | n8n(AI AgentノードのHuman-in-the-Loop機能) |

比較表(2026年7月時点の目安。料金・仕様は変更されやすいため各公式サイトで最終確認すること)

| 項目 | n8n | Dify | Zapier | Make |
|---|---|---|---|---|
| 主な用途 | 汎用ワークフロー自動化(AIは機能の1つ) | AIチャットボット/RAGアプリ構築 | 汎用ワークフロー自動化 | 汎用ワークフロー自動化 |
| AI機能 | AI Agentノード、主要LLM全対応、LangChainネイティブ統合、MCP対応、HITL承認ゲート | LLM呼び出しが中核機能、RAGが標準搭載 | Zapier Agents(自律型)、Zapier Copilot、AI Actions | OpenAI/Anthropic/Gemini等の公式モジュール、Make AI Agents |
| セルフホスト | 可(無料、要インフラ管理) | 可(無料、要インフラ管理) | 不可(クラウド専用) | 不可(クラウド専用) |
| 料金モデル | セルフホスト無料/クラウドは実行(ワークフロー1回の実行)課金 | セルフホスト無料/クラウドはメンバー数・アプリ数等で段階課金 | タスク(1ステップ実行)課金 | クレジット課金(標準モジュール実行1回=1クレジットが基本) |
| 学習コストの目安 | 中〜高(ノードの概念・データ構造の理解が必要) | 中(AI特化のため機能は絞られている) | 低(非エンジニア向けに設計) | 低〜中 |

「AIの生成・判断が主目的ならDify、業務システム間の連携が主目的でAIはその一部ならn8n、非エンジニアがとにかく手軽に自動化したいならZapier/Make」という整理が実務上の目安になる。Zapier・Makeもそれぞれ自律型のAIエージェント機能(Zapier Agents、Make AI Agents)を備えるようになっており、「非エンジニアがGUIだけでエージェントを作る」ならZapier/Make、「LangChainベースの細かい制御・MCP連携・セルフホストまで踏み込みたい」ならn8n、という住み分けが実務上のポイントになる(Zapier・Makeの詳細は各ツールの個別ページ、3ツールの横断比較は[n8n・Make・Zapierの比較と使い分け](./automation-tools-comparison.md)を参照)。

## 実務での使い方

### 導入方法(セルフホスト版とクラウド版)

- **セルフホスト**: Dockerがあれば以下のコマンドで起動できる(無料・無制限の実行回数)。
  ```bash
  docker volume create n8n_data
  docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n
  ```
  起動後、ブラウザで `http://localhost:5678` にアクセスすると編集画面が開く。自社のVPS(サーバー)上で運用すればデータは完全に自社管理下に置ける。なお報道によれば、セルフホスト環境でもBusiness相当の機能(SSO等)を実行回数課金で使える有償プランが用意されており、無料のCommunity版と個別見積りのEnterprise版の中間の選択肢になっている。
- **n8n Cloud**: n8n.io からサインアップし、クレジットカード登録は不要な14日間の無料トライアルで試せる(常設の無料プランはない)。インフラ管理不要ですぐに使い始められる。

### Cloud版の料金プラン(2026年7月時点の目安。最新情報は n8n.io/pricing で必ず確認)

| プラン | 料金(年払い時の月額目安) | 実行回数の目安 | 主な特徴 |
|---|---|---|---|
| Starter | 約$20/月 | 2,500実行/月 | クラウド版の入門プラン |
| Pro | 約$50/月 | 10,000実行/月 | 実行回数が拡大 |
| Business | 約$800/月(従業員20名未満の企業は50%オフ申請可) | 40,000実行/月 | SSO、バージョン管理、複数環境対応 |
| Enterprise | 個別見積り | 要相談 | 大規模組織向け機能・サポート |

課金の単位は「実行(execution)」であり、ワークフロー内のノード数やステップ数にかかわらず、ワークフローを1回動かすごとに1実行としてカウントされる点がZapier(タスク単位)・Make(クレジット単位)と異なる。全プランで「アクティブワークフロー数の上限」は撤廃されている。なお、各プランには対話でワークフローを組み立てる「AI Workflow Builder」機能向けの月間AIクレジット枠(Starterで2,000〜2,300程度、Proでプラン規模に応じて5,000〜1万数千程度が目安)が付帯すると報じられており、これは自分のAI Agentノードが呼び出すOpenAI・Anthropic等のAPI利用料(各社に別途課金)とは別枠の扱いになる。

### 画面操作の基本手順

1. n8nの編集画面で「+」からトリガーノードを選ぶ(例: 「Gmail Trigger」で新着メールを起点にする)
2. 続けて「+」でノードを追加し、線でつないでいく。ノードをクリックすると右側にパラメータ設定パネルが開き、Gmail・Slackなど各サービスのAPI認証情報(Credential)をここで登録する
3. AIを使う場合は「AI Agent」ノード、または単体の「OpenAI」「Anthropic Chat Model」などのノードを追加し、モデル名・プロンプトを設定する
4. 画面右上の「Execute Workflow」でテスト実行し、各ノードの入出力を確認する
5. 問題なければ画面右上のトグルで「Active(有効化)」にし、常時稼働させる

### 実務ユースケース例:新着メールをAIで要約してSlackに通知

構成は「Gmail Trigger → OpenAI(または Anthropic/Gemini)ノードで要約 → Slackノードで投稿」という3ステップ。

1. **Gmail Triggerノード**: 「新規メール受信時」をトリガー条件に設定する(未読メールをポーリングする方式)
2. **AIノード(OpenAIなど)のプロンプト例(コピペ可)**
   ```
   以下のメール本文を、日本語で3行以内に要約してください。
   重要な依頼事項や期限がある場合は、要約の最後に「対応要:◯◯」の形で明記してください。

   メール本文:
   {{ $json.text }}
   ```
3. **Slackノード**: 投稿先チャンネルを指定し、メッセージ本文に `件名: {{ $json.subject }}\n要約: {{ $('OpenAI').item.json.text }}` のように、前段ノードの出力を変数として埋め込む

n8n公式のワークフローテンプレート集(n8n.io/workflows)には、「Gmail+Gemini+Slackで日次メール要約」「未読メールをGPT-4oで要約してSlack通知」といった同種のテンプレートが多数公開されており、ゼロから組まずにテンプレートをインポートして自社用に調整するほうが早い。

### AIエージェントに承認ゲートを挟む場合(HITL)

Slackへの投稿程度なら自動実行のままでよいが、「メール送信」「顧客データベースの更新」「決済処理」のようにやり直しが利かない操作をAI Agentノードのツールとして接続する場合は、そのツールの設定で人による承認を必須にできる。承認依頼は指定したSlackチャンネルやTelegram、n8nのChatノード上に「エージェントが使おうとしているツール名とパラメータ」付きで届き、人間が承認すればそのまま実行、却下すればエージェントに却下理由が伝わり別の対応を試みる、という流れになる。AIエージェントの「暴走」対策として、重要な処理を任せる前にまずこのHITL設定を検討するとよい。

## 注意点・よくある誤解

- **セルフホストは「無料」だが「タダ」ではない**: ソフトウェア自体は無料でも、サーバーの費用(VPSで月数ドル程度が目安)と、アップデート・バックアップ・セキュリティ対応といった運用の手間が発生する。技術的な保守体制がない場合はクラウド版のほうが総コストを抑えられることもある
- **ワークフローの肥大化に注意**: ノードや条件分岐が増えるほど全体像が把握しづらくなる「スパゲッティ化」が起きやすい。ノードに分かりやすい名前を付ける、処理単位で「Sub-workflow(他のワークフローから呼び出せる部品)」として分割する、といった工夫が必要
- **APIキーの管理はCredential機能に統一する**: OpenAIやSlackなどのAPIキーをノードの設定欄やコードノードに直接書き込むと、ワークフローを他人と共有・複製した際に漏洩するリスクがある。n8nの「Credential」機能で一元管理し、個々のノードからは参照だけさせる
- **課金単位の違いに注意**: n8nは「ワークフロー1回の実行」単位で課金されるため、Zapier(タスク=ステップ単位)やMake(クレジット単位)と単純比較すると見積りを誤りやすい。ステップ数が多い複雑なワークフローほどn8nの実行課金は有利になりやすい
- **「fair-codeだから完全に自由」というわけではない**: Sustainable Use Licenseの下でも、n8nをそのままホスティングして他社に転売するような使い方は許可されていない。社内利用・自社サービスの裏側で使う分には問題ないが、n8n自体を製品化する場合はライセンスを確認する
- **MCPノードは「便利だが公開範囲の管理が必須」**: MCP Server Triggerでワークフローを外部公開すると、認証設定を誤ると社内システムへの操作を外部のAIツールから呼び出せてしまう。認証・アクセス範囲は必ず絞り込んだ上で有効化する
- **HITLは「重要な処理だけ」に絞る**: すべてのツール呼び出しに承認を必須にすると、結局人間が毎回判断することになり自動化のメリットが薄れる。取り返しのつく処理は自動実行のままにし、送信・更新・決済など不可逆な操作にだけ承認ゲートを設定するのが実務上のバランスになる

## 最初の一歩

n8n.ioでクラウド版の無料トライアルを開始し(またはDockerでローカルにセルフホストし)、公式テンプレート集から「Gmail要約→Slack通知」系のテンプレートを1つインポートして、自分の受信メールで実行してみる。

## 関連トピック

- [Difyとは何か](./dify-basics.md)
- [Difyワークフローの基本](./dify-workflow-basics.md)
- [Makeの基本](./make-basics.md)
- [Zapierの基本](./zapier-basics.md)
- [n8n・Make・Zapierの比較と使い分け](./automation-tools-comparison.md)
- [ノーコードでのAIエージェント構築](./nocode-ai-agent-building.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)

## 更新履歴

### 2026-07-23: AI関連機能(LangChainネイティブ統合、MCP対応、Human-in-the-Loop)と会社の資金調達状況を最新化
- **内容**: 2026年の大型アップデート(通称「n8n 2.0」、LangChainネイティブ統合・AI関連ノード70種以上)、MCP Server Trigger/MCP Client Toolノードによるエージェント間連携、AI AgentノードのHuman-in-the-Loop(ツール承認ゲート)、SAPの戦略出資による評価額拡大などの会社動向を追記。Cloud料金プランは前回調査時点から大きな変更がないことを再確認しつつ、AI Workflow Builder向けAIクレジット枠とセルフホストBusinessプランの存在を追記。比較表・使い分け・注意点・関連トピックをこれらに合わせて更新
- **出典**: [Introducing n8n 2.0(n8n公式ブログ)](https://blog.n8n.io/introducing-n8n-2-0/)、[Human-in-the-loop automation(n8n公式ブログ)](https://blog.n8n.io/human-in-the-loop-automation/)、[Human-in-the-loop for AI tool calls(n8n公式ドキュメント)](https://docs.n8n.io/advanced-ai/human-in-the-loop-tools/)、[MCP Server Trigger(n8n公式ドキュメント)](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-langchain.mcptrigger/)、[MCP Client Tool(n8n公式ドキュメント)](https://docs.n8n.io/integrations/builtin/cluster-nodes/sub-nodes/n8n-nodes-langchain.toolmcp/)、[n8n raises $180m to get AI closer to value with orchestration(n8n公式ブログ)](https://blog.n8n.io/series-c/)、[SAP backs n8n at $5.2B valuation(Tech Funding News)](https://techfundingnews.com/sap-backs-n8n-at-5-2b-valuation-to-automate-complex-data-heavy-enterprise-workflows-with-ai/)、[Fair-code pioneer n8n raises $60M(TechCrunch)](https://techcrunch.com/2025/03/24/fair-code-pioneer-n8n-raises-60m-for-ai-powered-workflow-automation/)、[n8n Pricing 2026(ConnectSafely)](https://connectsafely.ai/articles/n8n-cloud-pricing-guide)、[n8n Pricing and Plans for 2026(Lindy)](https://www.lindy.ai/blog/n8n-pricing)、[Zapier vs Make vs n8n in 2026: Where AI Agents Actually Fit(Medium/Automation Labs)](https://medium.com/@automation.labs/zapier-vs-make-vs-n8n-in-2026-where-ai-agents-actually-fit-1edbbeff85f3)、[n8n Self-Hosted Pricing: True Cost Breakdown(OpenHosst)](https://openhosst.com/blog/n8n-self-hosted-pricing)
- **注記**: n8nのAI Workflow Builder向けAIクレジット枠、セルフホストBusinessプランの詳細、および会社評価額・資金調達の一部数値は第三者メディアの記載をもとにした2026年7月時点の目安(n8n.io・community.n8n.ioの一部公式ページは本セッションからアクセス制限のため直接確認できず、docs.n8n.io配下のノードドキュメントURLは検索結果に基づき実在を確認)。掲載・記事化前に n8n.io/pricing およびdocs.n8n.ioで最終確認を推奨

### 2026-07-06: 初版執筆
- **内容**: n8nの概要(ノードベースのワークフロー自動化、AI Agentノード、LangChain統合)、Sustainable Use License、セルフホスト/クラウドの違い、Cloud版料金プラン、Dify/Zapier/Makeとの比較表、Gmail→AI要約→Slack通知の実装例を整理
- **出典**: [n8n Pricing 2026 (ConnectSafely)](https://connectsafely.ai/articles/n8n-cloud-pricing-guide)、[GitHub: n8n-io/n8n](https://github.com/n8n-io/n8n)、[n8n Docs: Sustainable Use License](https://docs.n8n.io/sustainable-use-license/)、[n8n Docs: AI Agent Node](https://docs.n8n.io/integrations/builtin/cluster-nodes/root-nodes/n8n-nodes-langchain.agent)、[n8n Docs: Advanced AI](https://docs.n8n.io/advanced-ai/)、[n8n Workflow Template: Gmail要約をSlack/WhatsApp/Docsへ通知](https://n8n.io/workflows/15403-summarize-daily-gmail-emails-with-gemini-and-send-to-slack-whatsapp-and-docs/)、[Zapier Pricing 2026まとめ (firstaimovers)](https://www.firstaimovers.com/p/zapier-pricing-platform-comparison-guide-2026)、[Make.com Pricing 2026 (trackstack)](https://trackstack.tech/en/make-com-pricing-2026/)
- **注記**: n8n Cloud・Zapier・Makeの料金プラン名・金額は第三者メディアの記載をもとにした2026年7月時点の目安。掲載・記事化前に各公式サイト(n8n.io/pricing、zapier.com/pricing、make.com/pricing)で最終確認を推奨
