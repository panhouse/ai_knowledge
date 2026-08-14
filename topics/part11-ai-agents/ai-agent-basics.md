---
title: AIエージェントとは何か
part: 11
chapter: 第1章 エージェントの基礎
tags: [AIエージェント, エージェンティックAI, 自律実行]
created: 2026-07-05
updated: 2026-08-14
---

# AIエージェントとは何か

## これは何か

ChatGPTやGeminiに質問を投げると、1回の回答で対話が完結する。これに対して「AIエージェント」は、人間が「ゴール(達成したい目標)」だけを渡せば、そこに至るまでの手順を自分で計画し、Web検索・ファイル操作・社内システムの呼び出しといった外部ツールを自ら使い分けながら、複数ステップの作業を最後までやり切ろうとするAIシステムを指す。「毎回指示しないと動かない」チャットボットと、「目標を渡せば後は任せられる」エージェントの違いを理解していないと、業務にAIを組み込む際の期待値も、権限設計もずれてしまう。

この自律的に計画・実行するAIの振る舞い方そのものを指す用語が「エージェンティックAI(Agentic AI)」であり、それを具体的なサービス・機能として実装したものが「AIエージェント」と呼ばれる。Anthropicはこの違いを「**ワークフロー**(人があらかじめ決めた手順どおりにAIとツールを呼び出す仕組み)」と「**エージェント**(LLMが自分でツールの呼び出し方を都度決めるループ)」という対比で整理しており、「エージェント=LLMがループの中で自律的にツールを使うこと」というシンプルな定義が業界でも定着しつつある(参照: [Anthropic「Building Effective AI Agents」](https://www.anthropic.com/research/building-effective-agents))。

## 仕組み・背景

AIエージェントの内部では、次のような「エージェントループ」が回っている。

1. ユーザーからゴールを受け取る
2. ゴールを達成するための手順を計画する
3. 必要なツール(Web検索、ファイル読み書き、ブラウザ操作、社内APIなど)を選んで呼び出す
4. ツールの実行結果を確認し、計画を見直す(失敗していれば別の手段を試す)
5. ゴールを達成した、あるいは人間の確認が必要と判断したら停止する

この「ツールをどう呼び出すか」を大規模言語モデル(LLM)自身に判断させる仕組みが「Function Calling(ツール呼び出し)」であり、さらに「そのツールがどこにあり、どう呼べばよいか」を各サービス間で共通化する規格として、Anthropicが2024年11月に公開した MCP(Model Context Protocol、モデル・コンテキスト・プロトコル)が事実上の業界標準として広がっている。2026年7月28日には仕様が刷新され、常時接続のセッション管理を前提とした従来方式から、1回ごとのリクエストをどのサーバーが受けても処理できる「ステートレス(状態を持たない)」な作り直しが行われたほか、ツール実行の途中でユーザーに追加確認を挟める仕組みや認可まわりの強化が加わった。TypeScript・Python向けSDKだけで累計10億ダウンロードを超えるなど採用が急速に進んでおり、OpenAI・Google・Microsoft・AWSなど主要プラットフォームがMCPに対応することで、AIエージェントが社内システムやSaaSに接続する際の「共通の差込口」のような役割を果たしている(参照: [Anthropic「Introducing the Model Context Protocol」](https://www.anthropic.com/news/model-context-protocol)、[Model Context Protocol Blog「The 2026-07-28 Specification」](https://blog.modelcontextprotocol.io/posts/2026-07-28/))。

また、ブラウザやPC画面をマウス・キーボード操作で直接動かす能力を指して「Computer Use(コンピュータ操作)」と呼ぶ。API連携が用意されていないWebサイトや業務システムでも、人間と同じように画面を操作して代行できる点が特徴で、Anthropic・OpenAI・Googleがそれぞれ自社モデルにこの機能を組み込んでいる。

**従来のチャットボット/生成AIとAIエージェントの違い**

| 観点 | 従来のチャットボット・生成AI | AIエージェント |
|---|---|---|
| 依頼の単位 | 1回のプロンプトに対して1回の回答で完結 | 「ゴール」を渡すと、複数ステップの計画・実行を自動で繰り返す |
| 人間の関わり方 | 人間がステップごとに指示を出す(人間が「操作」する) | 次に何をすべきかをAI自身が判断する(人間は「委任」する) |
| 外部ツール・API利用 | 基本はテキスト生成のみ。検索や実行は補助的 | Web検索・ブラウザ操作・ファイル操作・社内システム呼び出しなどを自ら実行 |
| 状態の保持 | その会話の文脈のみを保持 | タスクの進行状況・中間結果・計画を保持し、失敗すれば計画を修正する |
| 出力の形 | テキスト(要約・文章・コード案など) | テキストに加え、実際の操作結果(送信済みメール、更新済みファイル、実行済みコードなど) |
| 典型的な依頼例 | 「この文章を要約して」 | 「競合3社の価格を調べて比較表を作り、Slackに投稿しておいて」 |
| 失敗した時の影響範囲 | 誤った回答をコピペしなければ影響は限定的 | 実行済みの操作(送信・削除・購入など)は取り消せない場合がある |

## 使いどころ・使い分け

**代表的なAIエージェントの分類(2026年8月時点)**

| 分類 | 主な役割 | 代表的なサービス・機能 |
|---|---|---|
| コーディングエージェント | 要件から実装・テスト・デバッグまでを自律的に実行 | Anthropic Claude Code、GitHub Copilot(CLI・Agent Mode)、Devin(Cognition)、Cursor、Meta Muse Code(2026年8月5日にベータ投入。自社モデルMuse Spark 1.2を搭載し、大規模リポジトリ向けに複数のサブエージェントを並列実行するターミナル型ツール) |
| ブラウザ操作エージェント | Webサイトを実際に操作(検索・入力・購入など)して情報収集や作業を代行 | OpenAI ChatGPT(ブラウザ操作機能を内蔵。単体アプリだった「ChatGPT Atlas」は2026年8月9日に終了し機能はChatGPT本体に統合済み)、Google Gemini Spark(旧Project Mariner系機能を統合)、Perplexity Comet(エージェント機能を内蔵したChromiumベースのブラウザ) |
| 業務自動化エージェント | 業務システム(CRM・ITSM・HRなど)に組み込まれ、定型業務を代行・オーケストレーション | Salesforce Agentforce、ServiceNow AI Agent Orchestrator、Microsoft Copilot Studio上のエージェント、Microsoft「Autopilots」(Teams・Outlook・SharePoint等に横断で常駐する固有IDを持つ自律エージェント。第1弾は「Scout」) |
| 汎用アシスタントエージェント | 特定領域に限らず、調査・資料作成・タスク遂行を横断的に代行 | OpenAI ChatGPT Work(2026年7月投入。GPT-5.6を搭載し、資料・表計算・簡易Webアプリ作成などの業務を数時間単位で任せられる)、Anthropic Claude Cowork(非エンジニア向けにファイル操作・連携アプリ操作を行うデスクトップ/Web/モバイル版エージェント)、Google Gemini Spark、Microsoft 365 Copilot(Word/Excel/PowerPoint連携)、Manus(サンドボックス化された仮想マシン上でブラウザ・ターミナル・ファイルを操作する汎用自律エージェント) |

エージェント化すべきかどうかは、「ステップ数(工程が3段階以上に分かれるか)」「外部実行の必要性(実際にツールやシステムを操作する必要があるか)」「間違った場合の被害の大きさ(取り消せるか)」の3軸で考えるとよい。

**導入が向く業務の特徴**

- 手順がルール化できる、あるいは判断基準を言語化できる
- 利用先のシステムがAPIやMCPサーバーなど「ツール」として接続できる
- 誤りが起きても後戻り・修正が可能(取り消せる、影響範囲が小さい)
- 反復頻度が高く、承認フローを一度設計すれば繰り返し使い回せる

**導入がまだ向かない・要注意な業務の特徴**

- 対外送信・決済・削除など、取り消せないアクションを伴う
- 社内規程や法令解釈のように、都度の裁量判断・例外処理が必要
- 利用先システムがAPI化されておらず画面操作(GUI)しか手段がなく、かつ操作ミスの影響が大きい
- 権限管理・ログ・承認フローといったガバナンスが未整備

Gartnerは、自律型AIエージェントの導入パイロットのうち88%が本番運用まで進めず、生き残った11%は171%のROIを生んでいると分析しており、コスト超過・不明確な事業価値・不十分なリスク管理を理由に、2027年末までにエージェンティックAIプロジェクトの40%超が中止になると予測している。一方で、業務アプリケーションへのエージェント組み込み自体は急速に進んでおり、Gartnerは2026年末までにエンタープライズアプリケーションの40%がタスク特化型AIエージェントを内蔵するようになる(2025年時点では5%未満)とも予測している。つまり「エージェント機能が付いたツールは急増するが、そのすべてが投資に見合う成果を出すわけではない」のが実態であり、「向く業務」から小さく始め、ガバナンスを整えてから対象を広げるのが現実的な進め方になる(出典は更新履歴を参照)。

## 実務での使い方

### 主要ツールでの対応付け(2026年8月時点)

| 提供元 | 主なエージェント機能 | 呼び方・入り口 |
|---|---|---|
| OpenAI | ChatGPT Work(2026年7月9日発表。GPT-5.6搭載で、文書・表計算・プレゼン資料・簡易Webアプリ作成などを数時間単位で任せられる後継エージェント)、開発者向けOpenAI Agents SDK。ブラウザ単体アプリ「ChatGPT Atlas」は2026年8月9日に終了し、ブラウザ操作はChatGPT本体に統合済み | ChatGPTの入力欄でモードを「Chat」から「Work」に切り替えて依頼。開発者はAgents SDK(Python/JavaScript)で組み込む |
| Anthropic | Claude Code(コーディングエージェント)、Claude Cowork(非エンジニア向け。ファイル操作やSlack・Google Driveなど連携アプリの操作をデスクトップ/Web/モバイルで代行)、Claude Agent SDK、Computer Use(画面操作) | ターミナルで`claude`コマンドを実行、またはClaudeデスクトップアプリで「Cowork」を選択。開発者はAgent SDK(Python/TypeScript)でカスタムエージェントを構築 |
| Google | Gemini Spark(24時間稼働の個人向けエージェント。旧Project Mariner系のブラウザ操作機能を統合) | Geminiアプリで「Spark」を選択。企業向けはGemini Enterprise内で機能フラグとして順次公開中で、SharePoint・OneDrive・ServiceNowなどの既存コネクタ経由で業務システムに接続する |
| Microsoft | Copilot Agents / Copilot Studio、Word・Excel・PowerPoint内の自律実行機能、Work IQ API(2026年6月に一般提供開始。Copilotの文脈・実行機能をアプリ間で呼び出せる基盤API)、常駐型の「Autopilots」(第1弾「Scout」がTeams・Outlook・SharePoint等を横断) | 各Office製品のCopilotボタンから、または「Copilot Studio」でエージェントを新規作成。開発者はWork IQ APIをCopilotクレジット従量課金で呼び出す |
| Meta | Muse Code(2026年8月5日にベータ投入したターミナル型コーディングエージェント。自社モデルMuse Spark 1.2を搭載) | ターミナルから専用コマンドでインストールして実行。入力100万トークンあたり1.25ドル・出力100万トークンあたり4.25ドルの従量課金に加え、プロンプトを学習データに提供する代わりに割安になる「contributor」プランがある |
| Salesforce | Agentforce | 「Agentforce Studio」でエージェントを設定し、CRM業務(リード対応・問い合わせ対応など)に組み込む |
| ServiceNow | AI Agent Orchestrator / AI Agent Studio | Now Platform内の「AI Agent Studio」で、既存エージェントの利用またはカスタムエージェントの作成を行う |

### コピペで使える実例: エージェントへの権限ポリシー

社内でAIエージェントを試す際は、最初に「どこまで人間の承認なしで実行させるか」を明文化しておくと、誤操作のリスクを大きく減らせる。エージェントへの指示(システムプロンプトやカスタム指示欄)に、次のようなテンプレートをそのまま貼り付けて使える。

```
## 承認不要で実行してよい操作
- Web検索、社内Wiki・ドキュメントの検索・要約
- メール文面・資料構成案などのドラフト作成(送信はしない)
- 既存データの集計・グラフ化・レポート作成

## 必ず事前確認を取る操作(承認必須)
- 社外へのメール送信・SNS投稿・チャット送信
- ファイルの削除・上書き・既存データの更新
- 決済・契約・予約など金銭や契約が発生する操作
- 個人情報・機密情報を含むデータの外部への出力

## 想定外の状況に遭遇したら
- 作業を中断し、判断に迷った点を報告してから次の指示を待つ
```

### 業務シナリオの例: 競合調査レポートの自動作成

1. 「主要な競合5社の直近の価格改定と新機能をWebで調べ、比較表と3行サマリー付きのレポートをスプレッドシートにまとめて」とエージェントに依頼する
2. エージェントが各社サイト・プレスリリースを自律的に巡回し、情報を収集する
3. 途中、有料資料のダウンロードやアカウント登録が必要な場面では、エージェントが処理を一時停止し、人間に許可を求める(多くの製品は「重要な行動の前には確認を取る」設計になっている)
4. 収集結果を基に比較表・要約をまとめたファイルを作成し、人間が最終レビューをして社内共有する

この一連の流れはチャットボットに1問ずつ聞いて回るより圧倒的に速いが、最終レビューの工程は省略しないことが重要である。

### ログイン情報(パスワード)をどう扱うか

ブラウザ操作エージェントに社内システムやSaaSへのログインを代行させる場合、最大の懸念は「パスワードそのものをAIに渡してよいか」という点である。この課題に対し、パスワード管理ツール側でエージェントに認証情報を直接見せずにログインだけを代行させる仕組みが登場している。たとえば1Passwordは2026年7月16日、Claudeのブラウザ機能向けに「1Password for Claude」を発表した。パスワードやワンタイムパスコードはAI本体・その文脈(コンテキスト)・Anthropic側のシステムのいずれにも渡らず、1Password側が安全なチャネル経由でログイン画面に直接入力する仕組みで、実行のたびに生体認証で承認する。同様の「エージェントにはログイン結果だけを渡し、認証情報そのものは渡さない」という設計思想は、他のパスワード管理ツールでも今後標準的になっていくと見られる。エージェントに社内システムを操作させる際は、パスワードを直接プロンプトや設定に書き込むのではなく、こうした仲介の仕組みを使えないか確認したい。

### 料金面で見ておくべきポイント

エージェントは1回のゴール達成のために何ステップも「計画→実行→確認」を繰り返すため、同じ依頼でも単発のチャットより消費トークン量が数倍〜数十倍になりやすい。Anthropicは2026年6月15日から、Claude Agent SDKやClaude Code GitHub Actions経由の利用を、対話的なClaude Code利用とは別建てのトークン課金で計測するようになっており、エージェント経由の作業は事前にステップ数や予算の上限を決めておかないとコストが読みにくくなる点に注意したい。

## 注意点・よくある誤解

- **「エージェント=文章がうまいチャットボット」ではない**: 依頼の単位が「1回の質問」から「ゴールの委任」に変わる点が本質的な違いであり、それに応じて権限設計・承認フローも作り直す必要がある。
- **過大な権限付与のリスク**: 開発者コミュニティで実際に起きた例として、学習プラットフォームDataTalks.Clubの運営者がインフラ移行作業をコーディングエージェント「Claude Code」に任せたところ、設定ファイルの不整合をきっかけに`terraform destroy`(インフラ一括削除)コマンドが実行され、本番のデータベースやサーバーごと2.5年分のデータが一時消失する事故が報告されている(24時間後にバックアップから復旧)。ファイル削除や本番環境への書き込みなど、取り消しが難しい操作は事前承認を必須にし、権限は業務に必要な最小限(最小権限)に絞るのが基本。
- **プロンプトインジェクションのリスク**: ブラウザ操作エージェントやメール・Webページを読み込むエージェントは、閲覧先のページや受信メールに埋め込まれた悪意ある指示文に誘導され、意図しない操作を実行してしまう「プロンプトインジェクション」のリスクがある。外部コンテンツを読ませる用途では、実行前チェックや権限の絞り込みが特に重要。
- **セキュリティインシデントはすでに「よくあること」になっている**: Cloud Security Alliance(CSA)とToken Securityが2026年4月に公表した調査では、社内でAIエージェントを運用する組織の65%が、この1年間にAIエージェントに起因するセキュリティインシデントを少なくとも1件経験しており、その内訳は機密データの漏えい(61%)、業務停止(43%)、意図しない操作の実行(41%)が上位を占める。「まだ起きていないリスク」ではなく「すでに多くの組織で起きている前提」で権限設計・監視体制を組むべき段階に来ている。
- **ガバナンス整備が追いついていない**: Gartnerの調査では、自律型AIエージェントに対して成熟したガバナンス体制を持つ組織は21%にとどまるとされ、これが導入失敗の主因の一つとされている。FINRA(米国金融取引業規制機構)の2026年報告書も、エージェントの「自律性(人間の検証なしに行動する)」「スコープクリープ(想定より広い権限で動いてしまう)」「監査可能性の低さ(多段階の推論過程を後から追いにくい)」を主要リスクとして挙げており、重要な行動の前に人間の承認を必須にする「human-in-the-loop」、権限を業務に必要な最小限に絞る「スコープ設計」、行動ログを残す「監査証跡」の3点をセットで検討したい。
- **「エージェント」は誇張されやすいマーケティング用語でもある**: Gartnerは、実質的な自律性を持たないRPA(定型作業の自動化)やチャットボットを「エージェント」と呼び替えて売る現象を「agent washing」と名付けており、「エージェント」を名乗る製品のうち本当に自律的といえるものはごく一部にとどまると指摘している。製品検討時は、実際に何ステップまで人手なしで完結できるのか、どの操作の前に人間の確認が入るのか(=次の一手を誰が決めるのか)を必ず確認すること。
- **製品の統廃合が早いことを前提に選定する**: OperatorはChatGPT Agentに、Project MarinerはGemini(Spark/ブラウザ自動操作機能)に、それぞれ1年前後で統合・終了している。単体ブラウザアプリとして投入された「ChatGPT Atlas」も予告どおり2026年8月9日に終了し、機能はChatGPT本体に統合された。後継の「ChatGPT Work」も発表からすぐに看板機能が入れ替わっており、さらにMetaが2026年8月にMuse Codeでコーディングエージェント市場へ新規参入するなど、プレイヤーの顔ぶれ自体が数か月単位で変わり続けている。特定製品への過度な作り込みは避け、標準的なインターフェース(ブラウザ操作・ファイル操作・API連携・MCP)を軸に業務フローを設計する方が安全。
- **ハルシネーションは自律実行でも消えない**: 誤った前提のまま計画を立てて実行に進むと、その誤りが「実行結果」として現実の操作(送信・更新・購入など)に反映されてしまう。生成された情報を鵜呑みにせず、要所で人間が確認する設計が必要。

## 最初の一歩

まずは自社で既に使っているツール(ChatGPT・Claude・Gemini・Copilotなど)のエージェント機能を、影響範囲の小さい業務(社内向けの調査・資料のドラフト作成など)で試してみる。試す前に、上記のテンプレートを参考に「承認不要な操作」と「承認必須な操作」の境界を1行でも書き出しておくことが、事故を防ぐ最初の一歩になる。

## 関連トピック

- [Function Calling(関数呼び出し)の基本](../part09-api-development/function-calling-basics.md)
- [情報漏えい対策](../part04-risk-security/information-leakage-prevention.md)
- [生成AIに向く業務・向かない業務の切り分け](../part12-business-practice/ai-task-suitability.md)
- [Difyとは何か](../part10-nocode-lowcode/dify-basics.md)

## 更新履歴

### 2026-08-14: MCP仕様更新・新規参入プレイヤーを反映して最新化
- **内容**: MCP(Model Context Protocol)の2026年7月28日付仕様改定(セッション管理を廃したステートレス化、実行途中の追加確認、SDK累計10億ダウンロード超の採用実績)を仕組み・背景に追加。MetaがコーディングエージェントMuse Code(自社モデルMuse Spark 1.2搭載)でこの市場に新規参入したことを分類表・ツール対応表・注意点に反映。予告どおり2026年8月9日に完了した「ChatGPT Atlas」終了の記述を現在完了形に更新
- **出典**: [Model Context Protocol Blog: The 2026-07-28 Specification](https://blog.modelcontextprotocol.io/posts/2026-07-28/)、[CNBC: Meta debuts Muse Code to take on Anthropic and OpenAI](https://www.cnbc.com/2026/08/05/meta-debuts-muse-code-to-take-on-anthropic-and-openai-.html)、[OpenAI Help Center: Evolving Atlas into ChatGPT for browser-based agentic work](https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work)

### 2026-07-22: 主要プレイヤーの新製品と、セキュリティインシデントの実態を反映して最新化
- **内容**: OpenAIの新エージェント「ChatGPT Work」(GPT-5.6搭載)投入と「ChatGPT Atlas」終了(2026年8月9日)、AnthropicのCoworkのWeb/モバイル展開、MicrosoftのWork IQ API一般提供と常駐型「Autopilots」、Googleのエンタープライズ向けコネクタ強化を分類表・ツール対応表に反映。エージェント導入率に関するGartnerの最新予測(2026年末までにエンタープライズアプリの40%がエージェント搭載)、CSA/Token Securityによるセキュリティインシデント実態調査(65%の組織が経験済み)、Claude Codeによる実際のインフラ削除事故、1Passwordの認証情報保護連携を追加し、注意点・実務での使い方を増強
- **出典**: [Bloomberg: OpenAI Unveils ChatGPT Work Agent to Field Tasks for Hours](https://www.bloomberg.com/news/articles/2026-07-09/openai-unveils-chatgpt-work-agent-to-field-tasks-for-hours)、[OpenAI Help Center: Evolving Atlas into ChatGPT for browser-based agentic work](https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work)、[TechCrunch: The coding agent wars are spilling into the rest of the office (Claude Cowork)](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/)、[1Password: 1Password for Claude](https://1password.com/blog/1password-for-claude)、[Microsoft 365 Blog: Announcing the new Work IQ APIs](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/announcing-the-new-work-iq-apis/)、[TestingCatalog: Google plans to upgrade Gemini Enterprise connectors](https://www.testingcatalog.com/google-plans-to-upgrade-gemini-enterprise-connectors/)、[Gartner: Gartner Predicts 40% of Enterprise Apps Will Feature Task-Specific AI Agents by 2026](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)、[Cloud Security Alliance: Autonomous but Not Controlled: AI Agent Incidents Now Common in Enterprises](https://cloudsecurityalliance.org/artifacts/autonomous-but-not-controlled-ai-agent-incidents-now-common-in-enterprises)、[Tom's Hardware: Claude Code deletes developers' production setup, including its database and snapshots](https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-code-deletes-developers-production-setup-including-its-database-and-snapshots-2-5-years-of-records-were-nuked-in-an-instant)

### 2026-07-06: 重複ページの統合
- **内容**: 同一テーマの重複ページ `ai-agents-basics.md`・`ai-agents-overview.md` を本ページに統合。ワークフローとエージェントの対比(Anthropicの定義)、エージェント化の3つの判断軸、Manus・Perplexity Cometの追加、競合調査の業務シナリオ例、FINRAの指摘するリスク3点、agent washingへの注意、製品統廃合を前提とした選定方針、関連トピックへのリンクを取り込んだ
- **出典**: [Anthropic: Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents)、[Gartner: Gartner Warns of Agent Washing Risks](https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-warns-of-agent-washing-risks-in-supply-chain-planning-technology-market)、[Android Headlines: Google shuts down Project Mariner](https://www.androidheadlines.com/2026/05/google-shuts-down-project-mariner-ai-agent.html)、[No Hacks: The Agentic Browser Landscape in 2026](https://nohacks.co/blog/agentic-browser-landscape-2026)、[Wikipedia: Manus (AI agent)](https://en.wikipedia.org/wiki/Manus_(AI_agent))

### 2026-07-05: 初版執筆
- **内容**: AIエージェントの定義、従来のチャットボットとの違い(比較表)、エージェントループとMCP・Computer Useの仕組み、代表的な分類と2026年7月時点の主要サービス、導入の判断基準、権限ポリシーのテンプレート、企業導入におけるリスク(過大な権限付与・プロンプトインジェクション・ガバナンス未整備)を整理
- **出典**: [OpenAI: Introducing ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/)、[OpenAI: The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)、[Anthropic: Claude Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)、[Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)、[Google DeepMind: Project Mariner](https://deepmind.google/models/project-mariner/)、[Gemini: Gemini Spark overview](https://gemini.google/overview/agent/spark/)、[9to5Google: Gemini Spark rolls out to Google AI Ultra in the US](https://9to5google.com/2026/05/29/gemini-spark-ultra-us/)、[Microsoft: Microsoft Build 2026 – Empowering developers to adopt agentic AI](https://www.microsoft.com/insidetrack/blog/microsoft-build-2026-empowering-our-developers-to-adopt-agentic-ai-at-microsoft/)、[Salesforce: Agentforce Operations announcement](https://www.salesforce.com/news/stories/agentforce-operations-announcement/)、[ServiceNow: AI Agent Orchestrator press release](https://www.servicenow.com/company/media/press-room/ai-agents-studio.html)、[Gartner: Over 40% of agentic AI projects will be canceled by end of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)、[Gartner: Applying uniform governance across AI agents will lead to enterprise AI agent failure](https://www.gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure)
