---
title: MCP(Model Context Protocol)の基本
part: 9
chapter: 第4章 MCP・エージェント連携
tags: [MCP, Model Context Protocol, AIエージェント, ツール連携, コネクタ]
created: 2026-07-06
updated: 2026-08-14
---

# MCP(Model Context Protocol)の基本

## これは何か

AIチャットに「Slackの未読を要約して」「Google Driveのこの資料を読んで」と頼んでも、そのままでは何もできない。ChatGPT・Claude・Geminiなど、AIの種類ごと・接続先(Slack、Notion、社内DB…)ごとに、バラバラな方法で「つなぎ込み」のコードを書く必要があったからだ。MCP(Model Context Protocol、モデルコンテキストプロトコル)は、この「AIと外部のツール・データを接続する方法」を統一するために2024年11月にAnthropicが公開したオープンな規格。2026年8月時点では、ChatGPT・Gemini・Microsoft Copilotを含む主要なAIツールがすべて対応を完了しており、主要SDK(TypeScript/Python/Go/C#等)の月間ダウンロード数は合計で5億回近くに達するなど、事実上の業界標準になっている。よく「AIにとってのUSB-C(どの機器にも挿さる共通端子)」と例えられる。

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

なお、2025年12月9日にAnthropicはMCPをLinux Foundation傘下の新組織「Agentic AI Foundation(AAIF)」に寄贈し、OpenAI・Block(共同創設)、Google・Microsoft・AWS・Cloudflare・Bloomberg(支援)が参加する、特定企業に依存しないガバナンス体制に移行した。これによりMCPは「Anthropicの規格」から「業界共通のオープンスタンダード」としての位置づけがより明確になっている。2026年8月13〜14日には韓国・ソウルで開催された「MCP Dev Summit Seoul」に合わせ、金融機関やアジア太平洋地域の主要企業を含む57団体(Gold会員3・Silver会員33・Associate会員21)の新規加盟が発表され、AAIFの加盟組織は合計247団体に拡大した。9月には日本・中国で「AGNTCon + MCPCon」の開催も予定されており、MCPは単なる技術仕様から、業界横断のエンタープライズ基盤としての性格を強めている。

### 仕様の大型改定(2026-07-28版、5月にリリース候補→7月28日に正式版)

MCPの仕様は数か月おきに改定されており、2026年5月21日に凍結されたリリース候補(RC)を10週間の検証期間を経て、2026年7月28日に正式リリースされた版は「プロトコル発足以来、最大級の改定」と位置づけられている。ビジネス面で押さえておきたい変更点は次の通り。

- **プロトコルの「ステートレス化」**: それまでMCPサーバーは会話の状態(セッション)を保持し続ける前提だったため、大規模に運用しようとすると専用の仕組みが必要だった。今回の改定でプロトコルの中核部分がステートレス(状態を持たない)になり、初期化のハンドシェイクも廃止。一般的なWebサーバーと同じ仕組みで手軽にスケール(サーバーレス・エッジ環境への配置も含め)できるようになった。エンジニアにとっては「MCPサーバーを増やす・落ちても復旧しやすくする」といった運用の手間が減る変更である
- **Multi Round-Trip Requests(MRTR)・ヘッダーベースのルーティング**: 常時接続を張らなくても、サーバーがクライアントに途中で追加の確認を求めるようなやり取りができる仕組み(MRTR)が新設された。またメソッド名・ツール名がHTTPヘッダー(`Mcp-Method`・`Mcp-Name`)に載るようになり、社内でMCP通信を中継・監視する「ゲートウェイ」がJSON本文を解析せずにルーティングできるようになった。いずれも大規模運用のインフラを組みやすくする変更である
- **Extensions(拡張)の仕組みが正式化**: 「MCP Apps」(SlackやFigmaなどの画面をチャット内にそのまま表示できる仕組み)、「Tasks」(時間のかかる処理を後から確認できる仕組み)に加え、認証を一元化する「Enterprise Managed Authorization(EMA)」(後述)が、本体仕様から切り離した「拡張機能」として正式に位置づけられた。本体を安定させたまま、個別機能だけを速いペースで進化させる狙いがある
- **認証まわりの強化**: MCPサーバーが正式にOAuth 2.1の「リソースサーバー」と位置づけられ、クライアントが正しい認可サーバーを自動発見できるようRFC 9728(OAuth 2.0 Protected Resource Metadata)への対応が必須化。クライアント側もRFC 8707(Resource Indicators)によって「このトークンはどのMCPサーバー宛てか」を明示することが求められ、悪意あるサーバーが他サーバー宛てのトークンを騙し取る攻撃を防ぐ設計になった。RFC 9207(発行者検証)への対応も追加され、動的クライアント登録(DCR)から新方式「Client ID Metadata Documents(CIMD)」への移行も進む(後述の「注意点」も参照)
- **非推奨(廃止)ルールの明文化**: 機能を「有効→非推奨→廃止」の3段階で管理し、各段階の間に最低12か月の移行期間を設けることが明文化された。ビジネス側から見ると「ある日突然使っていた機能が消える」リスクが下がる変更である
- **普及状況**: 正式版の公開時点で、Tier 1 SDK(TypeScript・Python・Go・C#、ベータ版のRust)の月間ダウンロード数は合計で5億回近くに達し、TypeScript・Python SDKは単体でも累計10億ダウンロードを超えたと公表されている

### Enterprise Managed Authorization(EMA): 認証の一元管理

2026-07-28版で正式な拡張機能に昇格したのが「Enterprise Managed Authorization(EMA)」。組織が使っているID基盤(Microsoft Entra ID、Oktaなど)を「唯一の判断者」とし、管理者がグループ・役割・条件付きアクセスなどのポリシーを一度設定しておけば、利用者は最初のログイン時点で許可されたMCPサーバーに自動接続できる(アプリごとに個別のOAuth同意を求められない「ゼロタッチ」の仕組み)。Anthropic・Microsoft・Oktaなどが対応を進めており、Microsoftはこの仕組みを使って、Microsoft 365管理センターの「Copilot」→「コネクタ」タブからFederated Copilot Connectors(MCPベースの外部データ連携)を一元的に管理・展開できるようにしている。

### MCPとA2A(Agent2Agent)の関係

MCPとよく並べて語られるのが、Googleが2025年4月に公開したA2A(Agent2Agent Protocol、エージェント間プロトコル)である。役割はきれいに分かれている。

- **MCP**: AI(エージェント)が**ツール・データ**につながるための規格(縦の接続)
- **A2A**: AI**エージェント同士**がつながるための規格(横の接続。例: 自社の受発注エージェントと取引先の在庫管理エージェントを直接やり取りさせる)

A2Aは2025年6月にGoogleからLinux Foundationへ寄贈され、2026年4月時点でMicrosoft・AWS・Salesforce・SAPなど150社を超える組織が支持を表明している。両者は競合ではなく、実務では「社内外のツールにはMCPでつなぎ、複数のエージェント同士の分業にはA2Aを使う」という組み合わせが前提になっている。詳細は[A2A(Agent2Agent)プロトコルの基本](a2a-protocol-basics.md)を参照。

## 使いどころ・使い分け

| 状況 | 向いている選択 |
|---|---|
| 1回だけChatGPTに質問して終わる、資料をその都度手動でアップロードして要約させる | MCP不要。通常のチャット操作で十分 |
| 社内チャットボットを、複数のAIアプリ(Claude・ChatGPT・自社IDEなど)から同じ社内システムにつなぎたい | MCP向き。サーバーを1つ整備すれば複数クライアントから使い回せる |
| Slack・Google Drive・GitHubなど、すでに世の中にMCPサーバーが用意されている定番SaaSと連携したい | MCP向き。既製のMCPサーバー(コネクタ)を有効化するだけで済むことが多い |
| 自社独自のDB・基幹システムなど、まだMCPサーバーが存在しない接続先と連携したい | MCPサーバーを自社で開発する必要がある(エンジニアの工数が発生) |
| 1つのAIアプリの中だけで完結する、単発の関数呼び出し(天気を調べる等)を実装したい | Function Callingで直接実装する方がシンプルな場合が多い |
| 自社のAIエージェントと、取引先・他部門のAIエージェントを対等に連携させたい(受発注の自動やり取り等) | MCPではなくA2A向き。[A2A(Agent2Agent)プロトコルの基本](a2a-protocol-basics.md)を参照 |

判断基準は「複数のAIアプリ・複数の利用者にまたがって、同じ外部接続を繰り返し使い回すか」。使い回す予定がない一回限りの用途では、MCPサーバーを新規に作るコストに見合わないことが多い。また「つなぐ相手がツール・データなのかAIエージェントなのか」もMCPとA2Aを分ける判断軸になる。

## 実務での使い方

### 主なMCPサーバー・クライアントの例(2026年8月時点)

- **クライアント(MCP対応のAIアプリ)**:
  - **Claude Desktop / Claude Code**: Anthropic製。コネクタ(Connectors)という呼び方でMCPサーバーを追加する
  - **ChatGPT**: 2025年9月にMCP対応(当初は「コネクタ」と呼称)。2025年12月17日付けで呼び方が「コネクタ」から「アプリ(Apps)」に変更され、開発者はOpenAIの「Apps SDK」(MCPをベースに、チャット内に表示するUIまで含めて開発できる仕組み)で作成する。2026年2月22日には、SlackやFigmaの画面をチャット内に表示する拡張仕様「MCP Apps」への完全準拠も公式に案内された
  - **Google Gemini / Gemini Enterprise**: 2026年6月30日、Google CloudがGemini Enterprise Agent Platform向けの完全マネージド型リモートMCPサーバーを一般提供(GA)開始。Claude CodeなどGemini以外のAIエージェントからもGoogle Cloud上のリソースに接続できるようになった
  - **Microsoft Copilot**: Microsoft 365管理センターの「Copilot」→「コネクタ」タブから「Federated Copilot Connectors」としてMCPベースの外部データ連携を管理者が一元的に展開・管理できる。2026年半ばには前述のEnterprise Managed Authorization(EMA)にも対応し、利用者ごとのOAuth同意なしに許可済みMCPサーバーへ自動接続できるようになった
  - 各種AI対応IDE(Cursor、VS Code等)、OpenAIのAgents SDKなど
- **サーバー(接続先の例)**: Slack、Google Drive/Google Workspace、GitHub(公式サーバーがGo言語で提供されリポジトリ・Issue・PR・CI/CD操作に対応)、Notion、Git、Postgres、Puppeteer(ブラウザ操作)など。Anthropicが公開する参照実装リポジトリ(`modelcontextprotocol/servers`)には、ファイル操作・Web取得・時刻変換など汎用的なサーバーの例が揃っている
- **公式MCPレジストリ**: 2025年9月に公開された公式レジストリ(`registry.modelcontextprotocol.io`)には、直近の公式集計(2026年5月時点)で約9,650件のサーバー(最新版のみの件数)、バージョン違いを含めると約29,000件が登録されている。GitHub上で「mcp-server」トピックが付いたリポジトリも同時期に1万5,000件を超えており、エコシステムの裾野は2025年初頭の1,200件規模から1年強で7倍以上に拡大した。2026年8月時点でもこの水準からさらに拡大しているとみられるが、集計方法によって「5,800件台」から「1万件超」まで幅があるため、正確な件数は都度公式レジストリで確認するのが確実
- Claudeの「Connectors Directory(コネクタ ディレクトリ)」の掲載件数は集計方法によって数百件規模で幅があり(2026年6月時点で300〜400件台、8月時点で400件台という集計もある)、週単位で増減するため正確な件数は都度公式ページで確認するのが確実。2026年1月からは、Figma・Slackなど外部サービスのUIプレビューやインタラクティブ要素をチャット内に直接表示できる拡張仕様「MCP Apps」への対応が始まっており、2026-07-28版の仕様改定で正式な拡張機能(Extension)として位置づけが確定した

### 非エンジニアがClaudeで既存コネクタを有効にする手順(画面操作のみ、コード不要)

1. claude.ai にログインし、画面左下のアカウントアイコン → 「設定」→ 「コネクタ」を開く
2. 「コネクタを参照」をクリックすると、Slack・Google Drive・Notionなど接続できるアプリの一覧が表示される。名前検索・カテゴリ絞り込みができる
3. 使いたいアプリを選ぶと、そのアプリ自体のログイン画面に遷移するので、普段使っているアカウントでログインし、Claudeからのアクセスを許可する
4. 設定が終わると、チャット画面の「+」メニューからいつでもそのコネクタを呼び出せる。プロンプト中でアプリ名(例:「Google Driveの◯◯という資料を見て」)を伝えるだけでも、Claudeが自動的にコネクタを使って応答する

自社独自のサーバー(社内APIなど)や、ディレクトリに載っていないリモートMCPサーバーを使いたい場合は、同じ「コネクタ」画面の「カスタムコネクタを追加」からMCPサーバーのURLを入力して接続する(こちらは事前にエンジニアがMCPサーバー自体を用意している必要がある)。

Claude Code(開発者向けCLIツール)からMCPサーバーに接続する設定は、コマンドラインでの登録が必要になるため開発者向けの作業になる。

**呼び方の対応(ツール横断)**: 同じ「MCP経由の外部連携」でも、ツールによって画面上の呼び方が異なる。Claude=「コネクタ(Connectors)」/ ChatGPT=「アプリ(Apps)」(2025年12月に「コネクタ」から改称)/ Microsoft Copilot=「Federated Copilot Connectors」(M365管理センターで管理者が設定)/ Gemini Enterprise=「リモートMCPサーバー」。画面上でこれらの言葉を見かけたら、いずれもMCPによる外部接続機能だと読み替えるとよい。

### 料金・コストの考え方

MCP自体の利用に追加のライセンス料はかからないオープン規格だが、実際にはつなぐ先のサービス(Slack・GitHub等)の契約プランや、AIアプリ側のプラン(コネクタ機能が使えるのは有料プラン以上、というケースが多い)によって使える範囲が変わる。また、AIエージェントがMCP経由で何度もツールを呼び出す使い方をすると、その分APIのトークン消費・利用量が増える点も踏まえておく。

## 注意点・よくある誤解

- **MCP対応=安全とは限らない**: MCPサーバーに与える権限(読み取りだけか、書き込み・削除までできるか)は接続先ごとに異なる。特に社外で公開されている非公式のMCPサーバーを安易に信頼して認証情報を渡すと、データ漏えいや意図しない操作のリスクがある。信頼できる提供元(公式・大手ベンダー)のサーバーを優先し、権限は必要最小限に絞る
- **プロンプトインジェクションの新しい入口になる**: MCPの最大のセキュリティ課題は、[プロンプトインジェクション](../part04-risk-security/prompt-injection-basics.md)(AIに対して悪意ある指示を紛れ込ませ、意図しない動作をさせる攻撃)の攻撃面がMCP経由で大きく広がる点にある。代表的な手口は次の3つ。
  - **ツールポイズニング(tool poisoning)**: 一見普通のMCPサーバーが、ツールの説明文(description)の中に人間には見えにくい悪意ある指示を埋め込んでおき、AIがそれを「正規の指示」として実行してしまう
  - **ラグプル攻撃(rug pull)**: 導入時には安全なツール説明だったのに、利用者が承認した後でサーバー側がこっそり説明文を書き換え、危険な指示に差し替える
  - **confused deputy(混乱した代理人)問題**: 高い権限を持つAIエージェントが、外部から読み込んだ文書(例: GitHubのIssueやチケットの本文)に仕込まれた指示に従わされ、本来アクセスすべきでない社外の第三者に対して権限を「代理行使」させられてしまう(例: 公開Issueの内容がきっかけで非公開リポジトリの情報が外部に送信される)
  - 対策としては、MCPサーバーの提供元を信頼できる相手に限定する、ツールに渡す権限をタスクに必要な最小限にする、重要な操作(送信・削除・決済など)の前に人間の承認を挟む、可能であればツールの説明文やレスポンス内容を事前にレビュー・監視する、といった多層防御が推奨されている
- **「MCP対応=OAuthで守られている」とは限らない**: MCPの仕様では、インターネット経由でアクセスできるリモートMCPサーバーはOAuth 2.1(PKCEという追加の検証手順を含む認証の仕組み)への対応が事実上の必須要件とされ、2026-07-28版ではさらに「MCPサーバーはOAuth 2.1のリソースサーバーである」ことが明文化され、クライアント・サーバー双方に細かい実装要件(RFC 9728・RFC 8707・RFC 9207への対応)が課された。ところが2026年前半の実態調査では、公開されているMCPサーバーのうちOAuth 2.1を実装しているのはわずか8.5%にとどまり、約25%は認証そのものが存在せず、約53%は漏えいすると無期限に悪用され得る長期間有効なAPIキー・固定トークンをそのまま使っていたと報告されている。仕様が厳格化された分、実装との乖離はむしろ広がりやすい局面にあり、「MCPサーバーだから安全」という思い込みは禁物。特に自社でMCPサーバーを立てる・非公式のリモートMCPサーバーに接続する際は、認証方式(OAuth対応か、鍵はどう管理されているか、EMAのような組織的な認可基盤に対応しているか)を必ず確認する
- **「MCPを入れれば何でもできる」ではない**: MCPは接続の規格にすぎず、実際に何ができるかは接続先のMCPサーバーが何のToolsやResourcesを公開しているかに依存する。欲しい連携のMCPサーバーがまだ存在しなければ、自社で開発するかカスタムコードで対応するしかない
- **Function Callingと同じものだと誤解しやすい**: 前述のとおり、MCPは「接続の標準化」、Function Callingは「モデルがツールを呼び出す仕組み」で役割が異なる。両者は排他的ではなく、MCPサーバーの内部でFunction Calling相当の仕組みが動いていると理解するとよい
- **A2Aと混同しやすい**: MCPは「AIとツール・データの接続」、A2Aは「AIエージェント同士の接続」で役割が異なる(詳細は前述の「MCPとA2Aの関係」を参照)。複数のAIエージェントを連携させる話が出た時点で、それがツール接続の話なのかエージェント間連携の話なのかを切り分けるとよい
- **進化が非常に速い分野**: 2024年11月の登場から2年弱でOpenAI・Google・Microsoftなど主要ベンダーが相次いで対応を完了し、2025年12月にはガバナンスもAgentic AI Foundationへ移管された。2026年7月28日には「発足以来最大級」とされる仕様改定(プロトコルのステートレス化、Extensions framework、認証強化、非推奨ポリシーの明文化)が正式公開され、2026年8月には運営母体のAgentic AI Foundationも57団体増の247団体体制に拡大している。仕様・対応状況・利用可能なコネクタの一覧は数か月単位で更新されているため、導入判断の前には必ず公式情報で最新状況を確認する

## 最初の一歩

すでにClaudeの有料プランを使っているなら、「設定→コネクタ→コネクタを参照」から、普段使っているSlackかGoogle Driveのコネクタを1つ有効化し、「(接続したアプリ名)の最近の内容を教えて」と聞いてみることで、MCP経由の連携がどんな感覚かを体験できる。

## 関連トピック

- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [A2A(Agent2Agent)プロトコルの基本](a2a-protocol-basics.md)
- [OpenAI APIの基本](openai-api-basics.md)
- [Claude(Anthropic)の基本](../part03-ai-chat-tools/claude-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)

## 更新履歴

### 2026-08-14: 2026-07-28仕様の正式版確定・Enterprise Managed Authorization・AAIF加盟拡大を反映して最新化
- **内容**: 前回時点では「リリース候補(RC)」段階として紹介していた2026-07-28版の仕様が2026年7月28日に正式リリース(GA)されたことを明記し、Multi Round-Trip Requests(MRTR)・ヘッダーベースのルーティング・キャッシュ可能なリスト応答・RFC 9728/RFC 8707/RFC 9207への対応・動的クライアント登録(DCR)からClient ID Metadata Documents(CIMD)への移行方針など、認証まわりを中心にした技術的な変更点を追記。新たに正式な拡張機能(Extension)となった「Enterprise Managed Authorization(EMA)」(組織のID基盤を使った認可の一元管理・ゼロタッチ接続)を新設の小見出しで解説し、Microsoft Copilotの管理画面での対応状況を追記。ChatGPTが2026年2月22日にMCP Apps仕様へ完全準拠したこと、MCPの月間SDKダウンロード数が5億回近くに達したことを反映。運営母体のAgentic AI Foundation(AAIF)が2026年8月13〜14日に57団体(Gold3・Silver33・Associate21)の新規加盟を発表し加盟組織が合計247団体に拡大したことを追記し、「注意点」のOAuth実装率の記述は仕様厳格化との乖離が広がりやすい旨を補足
- **出典**: [Model Context Protocol Blog: The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/), [Claude by Anthropic: MCP 2026-07-28 spec: stateless core, coming to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude), [Model Context Protocol Blog: Enterprise-Managed Authorization: Zero-touch OAuth for MCP](https://blog.modelcontextprotocol.io/posts/enterprise-managed-auth/), [The Register: Model Context Protocol prepares to break with its stateful past](https://www.theregister.com/devops/2026/07/23/model_context_protocol_prepares_to_break_with_its_stateful_past/5276722/), [WorkOS: The biggest MCP spec update ships July 28: What changes for AI agent authentication](https://workos.com/blog/mcp-2026-spec-agent-authentication), [OpenAI Developer Community: Future of ChatGPT Apps SDK with MCP Apps Standardization?](https://community.openai.com/t/future-of-chatgpt-apps-sdk-with-mcp-apps-standardization/1372743), [AIwire/HPCwire: Agentic AI Foundation Welcomes 57 New Members, Gaining Major Financial Services Players and APAC Leaders](https://www.hpcwire.com/aiwire/2026/08/13/agentic-ai-foundation-welcomes-57-new-members-gaining-major-financial-services-players-and-apac-leaders/), [Agentic AI Foundation: MCP Is Now Enterprise Infrastructure - MCP Dev Summit North America 2026](https://aaif.io/blog/mcp-is-now-enterprise-infrastructure-everything-that-happened-at-mcp-dev-summit-north-america-2026/)

### 2026-07-23: 2026-07-28仕様改定・A2Aとの関係・認証セキュリティの実態を追記して最新化
- **内容**: 「発足以来最大級」とされる2026年7月28日版の仕様改定(プロトコルのステートレス化、Extensions frameworkによるMCP Apps/Tasksの正式な拡張機能化、認証強化、非推奨ポリシーの明文化)を追記。GoogleのA2A(Agent2Agent)プロトコルとの役割の違い・組み合わせ方を新設の小見出しと使い分け表・関連トピックリンクで整理。ChatGPTが2025年12月に「コネクタ」から「アプリ(Apps)」に呼称変更したこと、Gemini EnterpriseのリモートMCPサーバーが2026年6月30日にGA、Microsoft CopilotのFederated Copilot Connectorsなど各社の最新対応状況、MCP公式レジストリ・Claude Connectors Directoryの最新件数を更新。「注意点」に、リモートMCPサーバーはOAuth 2.1が事実上必須とされているにもかかわらず実装率はわずか8.5%、無認証が約25%、長期間有効な鍵の使い回しが約53%という2026年の実態調査結果を追加し、認証面の過信に警鐘を追加
- **出典**: [Model Context Protocol Blog: The 2026-07-28 MCP Specification Release Candidate](https://blog.modelcontextprotocol.io/posts/2026-07-28-release-candidate/), [Model Context Protocol Blog: The 2026 MCP Roadmap](https://blog.modelcontextprotocol.io/posts/2026-mcp-roadmap/), [Microsoft Tech Community: Only 8.5% of MCP Servers Use OAuth](https://techcommunity.microsoft.com/blog/appsonazureblog/only-8-5-of-mcp-servers-use-oauth-%E2%80%94-heres-how-to-host-one-securely-on-app-servic/4530349), [Practical DevSecOps: MCP Security Statistics 2026](https://www.practical-devsecops.com/mcp-security-statistics-2026-report/), [OpenAI Help Center: Developer mode and MCP apps in ChatGPT](https://help.openai.com/en/articles/12584461-developer-mode-and-mcp-apps-in-chatgpt), [OpenAI: Introducing apps in ChatGPT and the new Apps SDK](https://openai.com/index/introducing-apps-in-chatgpt/), [ITBrief: Google launches remote MCP server for Gemini Enterprise](https://itbrief.com.au/story/google-launches-remote-mcp-server-for-gemini-enterprise), [Smartsheet: Smartsheet Adds ChatGPT, Microsoft Copilot and Google Cloud Gemini Enterprise Connections for its MCP Server](https://www.smartsheet.com/content-center/news/smartsheet-adds-chatgpt-microsoft-copilot-and-google-cloud-gemini-enterprise), [The New Stack: Google Donates the Agent2Agent Protocol to the Linux Foundation](https://thenewstack.io/google-donates-the-agent2agent-protocol-to-the-linux-foundation/), [Google Open Source Blog: A year of open collaboration - Celebrating the anniversary of A2A](https://opensource.googleblog.com/2026/04/a-year-of-open-collaboration-celebrating-the-anniversary-of-a2a.html)

### 2026-07-06: Function Callingとの比較表・ガバナンス動向・セキュリティ節を追加
- **内容**: Function CallingとMCPの違いを表形式で整理し、2025年12月にAnthropicがMCPをLinux Foundation傘下の「Agentic AI Foundation(AAIF)」に寄贈しOpenAI・Google・Microsoft等が参加する中立ガバナンスに移行したこと、公式MCPレジストリの登録件数(2026年5月時点で約9,600サーバー)、ChatGPT・Geminiの公式MCP対応状況、MCP Apps拡張を追記。「注意点」にツールポイズニング・ラグプル攻撃・confused deputy問題などプロンプトインジェクション関連のMCP固有リスクと対策を追加し、関連トピックにプロンプトインジェクションページへのリンクを追加
- **出典**: [Linux Foundation: Announces the Formation of the Agentic AI Foundation (AAIF)](https://www.linuxfoundation.org/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation), [Anthropic: Donating the Model Context Protocol and establishing the Agentic AI Foundation](https://www.anthropic.com/news/donating-the-model-context-protocol-and-establishing-of-the-agentic-ai-foundation), [TechCrunch: OpenAI, Anthropic, and Block join new Linux Foundation effort](https://techcrunch.com/2025/12/09/openai-anthropic-and-block-join-new-linux-foundation-effort-to-standardize-the-ai-agent-era/), [OpenAI: OpenAI co-founds the Agentic AI Foundation](https://openai.com/index/agentic-ai-foundation/), [WorkOS: Everything your team needs to know about MCP in 2026](https://workos.com/blog/everything-your-team-needs-to-know-about-mcp-in-2026), [Checkmarx Zero: 11 Emerging AI Security Risks with MCP](https://checkmarx.com/zero-post/11-emerging-ai-security-risks-with-mcp-model-context-protocol/), [Aptible: Prompt injection in MCP - how tool poisoning works](https://www.aptible.com/mcp-security/mcp-prompt-injection), [Invariant Labs: MCP Security Notification - Tool Poisoning Attacks](https://invariantlabs.ai/blog/mcp-security-notification-tool-poisoning-attacks), [OWASP: MCP Tool Poisoning](https://owasp.org/www-community/attacks/MCP_Tool_Poisoning), [Simon Willison: Model Context Protocol has prompt injection security problems](https://simonwillison.net/2025/Apr/9/mcp-prompt-injection/)

### 2026-07-06: 初版執筆
- **内容**: MCP(Model Context Protocol)の定義、ホスト・クライアント・サーバーの三者構成、Function Callingとの役割の違い(接続の標準化 vs 呼び出しの仕組み)、使いどころの判断基準、ClaudeでのMCPコネクタの有効化手順(画面操作)、主なMCPサーバー・クライアントの例、セキュリティ面の注意点を整理
- **出典**: [Model Context Protocol公式: What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.io/docs/getting-started/intro), [Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol), [OpenAI Developers: MCP and Connectors](https://developers.openai.com/api/docs/guides/tools-connectors-mcp), [Claude Help Center: Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities), [Google Cloud: What is Model Context Protocol (MCP)? A guide](https://cloud.google.com/discover/what-is-model-context-protocol), [GitHub: modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
