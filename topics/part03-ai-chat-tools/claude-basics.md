---
title: Claude(Anthropic)の基本
part: 3
chapter: 第5章 主要ツール各論
tags: [Claude, Anthropic, Claude Code, Cowork, モデルラインナップ]
created: 2026-07-05
updated: 2026-09-04
---

# Claude(Anthropic)の基本

## これは何か

Claudeは、AI企業Anthropic(アンソロピック)が開発する生成AIで、ChatGPT(OpenAI)、Gemini(Google)と並ぶ三大LLM(大規模言語モデル。文章生成AIの基盤技術)の一つ。「ChatGPTは知っているが、Claudeは何が違うのか分からない」という人が多いが、実はモデル名の付け方・プラン構成・強みの傾向がそれぞれ異なる。ここではClaudeのラインナップと、他ツールとの使い分けの目安を整理する。

## 仕組み・背景

Anthropicは2021年に元OpenAIの研究者らが設立したAI企業で、AIの安全性を重視した開発方針を掲げているのが特徴。Claudeは個人向けチャットサービスの**claude.ai**(Web・スマホアプリ・デスクトップアプリ)と、開発者・企業がシステムに組み込むための**Claude API**(開発者向けの従量課金サービス)の2系統で提供されており、この2つは契約・請求が別立てになっている(ChatGPTの「ChatGPT Plus」契約と「OpenAI API」の従量課金が別会計であるのと同じ構造)。

モデル名は「Opus(オーパス、大作)」「Sonnet(ソネット、定型詩)」「Haiku(俳句)」という文学・音楽の形式名をグレード(性能・価格帯)として使い、最上位には「Fable(寓話)」というシリーズ名が使われている。世代を表す数字(例: Sonnet 5、Opus 5)は数か月単位で更新されることが多く、名称・価格ともに変更頻度が高い。2026年6月30日には新シリーズの「Sonnet 5」が登場し、翌7月1日からFree・Proプランの既定モデルがSonnet 5に切り替わった。さらに7月24日には、Fable 5に迫る性能を約半額の価格で提供する中間グレード「Opus 5」が登場し、claude.aiのMaxプランの既定モデル・Proプランで選べる最上位モデルという位置づけになっている(旧世代のOpus 4.8はAPI経由では引き続き利用できるが、claude.aiの画面上ではOpus 5に置き換わった)。そして2026年9月1日には、最上位「Fable」シリーズの後継モデル「Fable 5.1」が登場した。コーディング・込み入った推論・長時間の自律的エージェント作業でFable 5からさらに性能が底上げされ、加えてプロンプトキャッシュ(繰り返し使う長いプロンプトを安く再利用する仕組み)の読み取り価格が1トークン単価あたり1/4(1M tokensあたり$1.00→$0.25)に下がったことで、実利用コストは典型的な使い方で約25%、エージェント的な使い方では最大45%程度下がっている。旧世代のFable 5もAPI経由では引き続き利用できる。なお最上位のFable 5.1と同等の能力を持つ「Mythos 5.1」というモデルも存在するが、これは米政府と連携する「Project Glasswing」プログラム経由でサイバー防衛担当者や重要インフラ事業者などごく一部にのみ提供される特別枠で、一般の業務利用者が触れる対象ではない。

## 使いどころ・使い分け

ChatGPT・Gemini・Claudeはいずれも汎用的なチャットAIで機能は重なる部分が多いが、傾向としては次のような違いがよく挙げられる(断定的な優劣ではなく「得意寄り」の目安)。

| 軸 | 傾向として強いツール |
|---|---|
| 長い資料の要約・大規模なコード生成、込み入った指示への追従 | Claude |
| コーディング・自律的なエージェント作業(ターミナルでの開発支援、フォルダ内のファイルを横断した事務作業など) | Claude(Claude Code、Claude Cowork)、ChatGPT(Codex系) |
| Google Workspace(Gmail・スプレッドシート・ドキュメント等)との連携 | Gemini |
| プラグイン・カスタムGPTの豊富さ、画像生成や音声など汎用性の幅広さ | ChatGPT |
| 手元の資料だけを根拠にした正確なリサーチ | Gemini(NotebookLM) |

いずれのツールも短期間で機能追加が続くため、「今どのツールが強いか」は流動的。業務で使い分ける場合は、まず今の作業に必要な機能(社内ツール連携か、長文処理か、コーディングか)から選び、複数ツールを併用するのが現実的。

## 実務での使い方

### 個人向けプラン(claude.ai、2026年8月時点の目安)

| プラン | 月額目安 | 主な違い |
|---|---|---|
| Free | $0 | 既定モデルはSonnet 5(2026年7月1日〜)。Projects・Artifacts・Memory(会話の記憶)は2026年前半にFreeプランへも開放され、Web検索・ファイルアップロードも利用できるが利用量の上限が低く、Cowork・Claude Codeは利用不可 |
| Pro | $20(年払いなら$17/月相当) | Free比で約5倍の利用量。最上位のFable 5、および中間グレードのOpus 5(Pro内での最上位モデル)にもアクセス可。2026年1月からClaude Cowork・Claude Codeも利用可能になった |
| Max 5x | $100 | Free比で約25倍(Pro比で約5倍)の利用量。既定モデルがOpus 5(2026年7月24日〜)。混雑時の優先アクセス |
| Max 20x | $200 | Free比で約100倍(Pro比で約20倍)の利用量。ヘビーユーザー向け。既定モデルはMax 5xと同じくOpus 5 |
| Team(Standard席) | 1人$25/月(年払いで$20/月相当) | 管理機能・一括請求・プロジェクトの組織内共有。Claude Code・Cowork・Microsoft 365やSlack等との連携も利用可 |
| Team(Premium席) | 1人$125/月(年払いで$100/月相当) | Standard席の約5倍の利用量。コーディングなど利用量が多いメンバー向け |
| Enterprise | 座席$20/月〜+使用量は別途API料金で請求 | SSO・監査ログ・カスタムのデータ管理など大企業向け機能。使用量が変動する組織向け。Compliance API(会話・セッション内容の監査用API)の対象がCowork・Claude Codeにも拡大した(2026年8月、ベータ) |

Team・Enterpriseの最低契約席数や条件は情報源により表記が揺れているため(2〜5席など)、契約前に必ず[Anthropic公式の料金ページ](https://claude.com/pricing)で最新の金額・条件を確認すること。料金・利用上限はAnthropicの発表頻度が高く、日本向けには2026年4月から消費税が別途請求される運用になっている。

### 個人向けプランで使えるモデル

Freeプランは既定でSonnet 5、Haiku 4.5が利用可能。Pro・Max・Team・Enterpriseでは、これに加えて中間グレードのOpus 5(2026年7月24日〜)、および最上位モデルの「Fable 5.1」(2026年9月1日、旧世代Fable 5の後継として登場)にアクセスできる。ただしFable系モデルはSonnet 5・Opus 5と同じ「使い放題」の位置づけではなく、Maxプランでは週次利用上限の一部を消費する形、Pro・Teamの標準席では別枠の利用クレジットを消費する形で提供される(上限の具体的な水準はプランや時期により変わるため、契約前に公式ヘルプセンターで確認する)。Maxプランでは既定モデルがOpus 5(旧世代のOpus 4.8はclaude.aiの画面上ではOpus 5に置き換わり、API経由でのみ引き続き提供)、Proプランでは選択できる最上位モデルという位置づけ。画面右上のモデル選択メニューから、プランで利用可能な範囲のモデルを都度選べる。

### 開発者向け:Claude APIのモデルラインナップ(2026年9月時点)

| モデル | モデルID | コンテキスト | 入力$/1M | 出力$/1M | 位置づけ |
|---|---|---|---|---|---|
| Claude Fable 5.1 | `claude-fable-5-1` | 1M | $10.00 | $50.00 | 最も高性能。2026年9月1日発表。最も難しい推論・長時間の自律的エージェント作業向け(最大出力128K)。プロンプトキャッシュの読み取り価格が$0.25/1M(旧Fable 5は$1.00/1M)に下がり、実質コストが2〜4割程度下がった |
| Claude Opus 5 | `claude-opus-5` | 1M | $5.00 | $25.00 | 2026年7月24日発表。Fable系に迫る性能を半額程度で提供する「日常使いの最上位モデル」。claude.aiのMaxの既定・Proの最上位モデル |
| Claude Sonnet 5 | `claude-sonnet-5` | 1M | $2.00(2026年8月10日に恒久価格として確定。当初予定していた9月1日からの$3.00への値上げは撤回) | $10.00(同上。当初予定は$15.00) | 速度と知能のバランス型。coding・エージェント作業でOpusに迫る品質。claude.aiのFree/Proの既定モデル |
| Claude Haiku 4.5 | `claude-haiku-4-5` | 200K | $1.00 | $5.00 | 最速・最安価。簡単なタスク・大量処理向け |

上記は現行世代の主要モデル。旧世代のFable 5・Opus 4.8・Opus 4.7・Opus 4.6・Sonnet 4.6も引き続きAPIから利用できるが、新規に組む場合は上表の現行モデルを使うのが基本。料金は変更・改定が非常に多いため、実装・見積もりの前には必ず[Anthropic公式のPricingページ](https://platform.claude.com/docs/en/about-claude/pricing)で最新の値を確認すること。プロンプトキャッシュ(繰り返し使う長いプロンプトを安く再利用する仕組み)やBatch API(即時性が不要な処理を50%引きで処理する仕組み)を使うと、実際のコストはさらに下げられる。

### Claude Code(開発者向けCLIツール)

Claude Codeは、ターミナル(コマンドライン画面)上で動くAnthropic製のAIコーディングエージェントで、コードベースの読み取り・ファイル編集・コマンド実行・Git操作などをAIに任せられる開発支援ツール。2026年1月からPro以上のプラン(Max/Team/Enterprise)や従量課金のAPIから利用できるようになった。ターミナルだけでなくIDE・デスクトップアプリからも操作できる。2026年8月には、サブエージェント(作業を分担する子エージェント)への処理委譲が既定で有効になったほか、GitLab対応の強化や、Team・Enterpriseプラン向けに「自社インフラ上でClaude Codeのクラウドセッションを動かせる」自己ホスト型環境(セルフホスト環境)がパブリックベータで追加された。詳細な使い方は別トピックで扱う。

### Claude Cowork(非エンジニア向けの汎用エージェント機能)

Claude Cowork(コワーク)は、Claude Codeと同じエージェント基盤を、ターミナル操作なしで一般業務に転用した機能。指定したフォルダへの読み書き権限をClaudeに与えることで、資料作成・調査・整理といった複数ステップの作業を「その場で説明する」のではなく実際に最後まで実行させられる。2026年1月にMax限定で提供開始後、数日でPro以上の全有料プランに開放された。デスクトップアプリが中心だったが、2026年7月からはクラウド上での実行(Web・モバイルからの操作、PCがオフラインでも作業継続)にも対応が広がり、Max→他プランの順に数週間かけて展開された。2026年8月には、ブラウザ拡張機能「Claude in Chrome」のサイドパネルもCoworkのセッションとして統合され、ブラウザで始めた作業をデスクトップ・Web・モバイルアプリ間で引き継げるようになっている(Max・Teamはこの統合が先行提供、Proは順次展開)。さらに同じく2026年8月、デスクトップアプリ内にログイン情報を持たないクリーンな「内蔵ブラウザ」が追加され、Coworkのタスクがサイドパネルでウェブページの閲覧・クリック・入力を自律的に行えるようになった。手元のブラウザに残っているログイン状態を使って自分の代わりに操作させたい場合は既存の拡張機能「Claude in Chrome」、ログイン不要な調査やまとめて任せたい定型作業には内蔵ブラウザ、という使い分けが目安(使用するブラウザはデスクトップアプリの「設定→Cowork→優先ブラウザ」で切り替え可能)。作業ステップ(開いたファイル・使ったツール・下した判断)を逐次確認・介入でき、定型作業は一定間隔で自動実行するスケジュール設定も可能。Freeプランでは利用できない。

### Artifacts機能(生成物のプレビュー・編集)

Artifactsは、Claudeが生成したコード・文書・簡単なWebアプリなどを、会話とは別のプレビュー画面に表示し、その場で編集・再生成できる機能。ChatGPTの「Canvas」、Geminiの「Canvas」に近い位置づけの機能で、2026年2月からHTML・React・SVG・Mermaid図・コード・文書といった主要な形式はFreeプランを含む全プランで無料利用できる。有料プランでは1つのArtifactあたり最大20MBの永続ストレージが使え、Artifact内からClaudeのAPIを直接呼び出せるため、単なる静的なプレビューではなく「Artifact自身がAIを内蔵した簡易アプリとして動く」使い方もできる。MCP(外部サービス連携の標準規格)経由でGoogle カレンダー・Gmail・Slackなどと直接連携させることも可能で、他ユーザーが作ったArtifactsを閲覧して自分用に流用できる「コミュニティカタログ」も用意されている。Team・Enterpriseプランでは、組織内でライブ状態のArtifactsを共有することもできる。

- 有効化: claude.aiの左下のアカウント名 → 「設定」→「アーティファクトを有効にする」をオン
- 使い方: 通常どおりプロンプトを入力するだけで、まとまった分量のコード・文書を生成する際に自動でArtifacts画面が開く

### Projects機能(ChatGPTのGPTs、GeminiのGemに相当)

Projectsは、特定の業務・案件専用に「カスタム指示」と「ナレッジ(参照資料)」をひとまとめにしたワークスペースを作れる機能。以前はPro以上のプラン限定だったが、2026年前半にFreeプランにも開放され、現在は全プランで利用できる(利用量の上限はプランに応じて異なる)。2026年7月からは、通常のチャットとCowork(後述のエージェント機能)が同じ画面に統合され、Projects・Artifactsも両方の入口から共通で使えるようになっている。

作成手順の目安:
1. claude.ai/projects を開き、「+ 新規プロジェクト」をクリック
2. プロジェクト名と説明を入力
3. 「カスタム指示」欄に、口調・出力形式・前提条件などを記入(例:「ですます調で書く」「専門用語には必ず一言説明を付ける」)
4. 「ナレッジ」欄に、会社概要・商品情報・過去の提案書などのファイルをアップロード
5. 以後、そのプロジェクト内で開始した会話はすべて、この指示とナレッジを踏まえて回答される

### Memory機能(会話をまたいだ記憶)

2026年3月、無料プランを含む全ユーザーにMemory(記憶)機能が展開された。ユーザーの名前・文章の好み・進行中のプロジェクトの文脈などを、会話をまたいで自動的に記憶し、次回以降の会話に反映する。記憶内容は「設定 → Capabilities(機能) → Memory」から一覧で確認・編集・削除できるため、機微な情報が誤って記憶された場合はここで削除する。なお、現在の「1件の要約メモに集約する」方式に加えて、記憶をトピックやプロジェクトごとに複数のファイルへ分けて管理する「Memory Files」という新方式のテストも報じられているが、2026年8月時点では一般提供されていない。

### 拡張思考(Extended Thinking)→ 適応的な推論(Adaptive Reasoning)

以前は「拡張思考」を明示的にオン/オフしたり、考える分量(トークン予算)を指定する必要があったが、2026年2月ごろのモデル世代(4.6系)以降は、Claudeが問題の難しさを内部で判断し、考える必要があるか・どこまで深く考えるかを自動的に決める「適応的な推論」に置き換わっている。ユーザー側での複雑な設定は基本的に不要になった。

### Web検索・Claude in Chrome(ブラウザ操作エージェント)

claude.aiにはWeb検索機能が組み込まれており、最新情報を検索して出典付きで回答に反映できる(設定でオン/オフ可能)。加えて、ブラウザ拡張機能「Claude in Chrome」が、ページの読み取り・クリック・フォーム入力・タブ間移動などをユーザーに代わって実行する、コンピュータ操作型のエージェント機能を提供している(2026年8月時点でChrome限定・有料プランのみのオープンベータ、Freeプランでは利用不可)。取引実行やCAPTCHA回避、医療系(HIPAA対象)組織での利用など、Anthropicが明示的に制限している操作もある。これらはCowork・Claude Codeのようなエージェント機能とあわせて、単なる会話にとどまらない「作業の実行」をClaudeに任せる方向性の一部。

## 注意点・よくある誤解

- **モデル名・料金の変更頻度が非常に高い**: 数か月単位で新モデルが出て旧モデルの価格が変わる。本ページの数値は目安であり、見積もり・契約の前には必ず公式サイトで確認する
- **claude.aiの契約とAPIの契約は別会計**: Pro/Maxなどのサブスクリプションに入っていても、開発者向けAPIの利用料は別途従量課金になる(逆にAPI利用者がclaude.aiを個人利用したい場合も別途契約が必要)
- **Sonnet 5の導入価格は恒久価格として確定した**: 発表当初は2026年8月31日までの期間限定価格(入力$2.00/出力$10.00)とされ、9月1日から入力$3.00/出力$15.00に値上げされる予定だったが、Anthropicは2026年8月10日にこの値上げを撤回し、$2.00/$10.00を恒久価格とすることを発表した。ただし今後の改定がないとは限らないため、長期のコスト試算をする際も都度公式サイトで確認する
- **「Claude」「Claude Code」「Claude Cowork」を混同しない**: 「Claude」はチャットサービス全般の名称、「Claude Code」は開発者向けCLIツール、「Claude Cowork」はターミナル操作なしで一般業務を任せるエージェント機能。それぞれ利用可能プランや操作方法が異なる
- **CoworkはFreeプランでは使えない**: エージェント的にファイルを読み書きする機能はPro以上の有料プラン限定。無料プランで試せるのはチャット・Projects・Artifacts・Memoryなど(2026年前半にProjects・Artifactsも無料プランへ開放された)
- **「Opus」「Fable」だけでも複数の世代・派生がある**: claude.aiの画面上ではOpus 4.8がOpus 5に置き換わっており、API上では旧世代のOpus 4.8も引き続き選べる。最上位の「Fable」も2026年9月にFable 5からFable 5.1へ更新されたが、旧Fable 5もAPI経由では引き続き利用できる。またFable 5.1と同等の性能を持つ「Mythos 5.1」は米政府連携プログラム「Project Glasswing」経由のごく一部の利用者向けで、一般業務では登場しない
- **Fable系モデルは「使い放題」ではない**: Pro/Max/Teamに契約すればFable 5.1が無制限に使えるわけではなく、Maxでは週次利用上限の一部、Pro・Teamの標準席では別枠のクレジットとして提供される。Sonnet 5・Opus 5と同じ感覚で使い倒すと上限に早く達することがあるため、消費ペースをアカウントの使用状況画面で確認しながら使うのが実務のコツ

## 最初の一歩

claude.aiに無料アカウントで登録し、Artifacts機能を有効にしたうえで、社内資料の要約や簡単な文面のたたき台作成を1つ試してみる。

## 関連トピック

- [Google Geminiの基本](./google-gemini-basics.md)
- [OpenAI APIの基本](../part09-api-development/openai-api-basics.md)
- [Function Calling(Tool Use)の基本](../part09-api-development/function-calling-basics.md)

## 更新履歴

### 2026-09-04: 最上位モデルの世代交代(Fable 5→Fable 5.1/Mythos 5.1)とCoworkの内蔵ブラウザ追加を反映して最新化
- **内容**: 2026年9月1日に発表された新モデル「Claude Fable 5.1」(`claude-fable-5-1`、$10/$50。旧Fable 5の後継で、コーディング・長時間の自律的エージェント作業の性能が向上し、プロンプトキャッシュの読み取り価格が$1.00→$0.25/1Mに下がったことで実質コストが典型利用で約25%・高度なエージェント利用で最大45%程度下がった)とその同等モデル「Claude Mythos 5.1」(Project Glasswing経由の限定提供)を追加し、旧世代のFable 5・Mythos 5もAPI経由では引き続き利用できることを明記。claude.aiの個人向けプランではFable系モデルがSonnet 5・Opus 5と異なり「使い放題」ではなく、Maxは週次利用上限の一部・Pro/Teamの標準席は別枠クレジットの消費という形で提供される点を新設の注意点として追記(Opus 5・Sonnet 5の位置づけ・価格に変更はないことを公式Pricingページで確認済み)。Claude Coworkにデスクトップアプリ内蔵の「内蔵ブラウザ」(ログイン情報を持たないクリーンなプロファイルでサイドパネル操作)が2026年8月に追加され、ログイン状態を引き継ぐ「Claude in Chrome」との使い分けを追記
- **出典**: [Anthropic公式: Pricing(Claude Platform Docs)](https://platform.claude.com/docs/en/about-claude/pricing)、[9to5Mac: Anthropic upgrades Claude with new Fable 5.1 model](https://9to5mac.com/2026/09/01/anthropic-upgrades-claude-with-new-fable-5-1-model-details-here/)、[VentureBeat: Anthropic's Claude Fable 5.1 and Mythos 5.1 arrive with a 75% cost reduction for Fable cache reads](https://venturebeat.com/technology/anthropics-claude-fable-5-1-and-mythos-5-1-arrive-with-a-75-cost-reduction-for-fable-cache-reads)、[MacRumors: Anthropic Launches Claude Fable 5.1 With Lower Costs and Fewer False Positives](https://www.macrumors.com/2026/09/01/anthropic-claude-fable-5-1/)、[Silicon Republic: Anthropic launches Claude Fable 5.1 and Mythos 5.1](https://www.siliconrepublic.com/machines/anthropic-launches-claude-fable-5-1-and-mythos-5-1)、[aiagentslibrary.com: Claude Cowork Built-In Browser vs Claude in Chrome](https://www.aiagentslibrary.com/blog/claude-cowork-browser-vs-claude-in-chrome/)、[digitalapplied.com: Claude Cowork Goes Web and Mobile](https://www.digitalapplied.com/blog/claude-cowork-web-mobile-expansion-guide-2026)

### 2026-08-15: Claude Opus 5の登場とSonnet 5価格恒久化、Cowork/Artifacts/Projectsの機能拡張を反映して最新化
- **内容**: 2026年7月24日発表の新モデル「Claude Opus 5」($5/$25、Fable 5に迫る性能を半額程度で提供)を追加し、claude.ai Maxの既定モデル・Proの最上位モデルになったこと、旧Opus 4.8はclaude.ai上ではOpus 5に置き換わったがAPI経由では引き続き利用可能であることを反映。Sonnet 5の導入価格($2/$10)が2026年8月10日に恒久価格として確定し、予定されていた9月1日からの値上げが撤回されたことを踏まえ、API料金表と注意点を修正(旧版は値上げが起きる前提の記述だった)。Artifacts・Projectsが2026年前半にFreeプランへ開放されたこと、Artifactsの永続ストレージ・API直接呼び出し・MCP連携・コミュニティカタログへの機能拡張、Claude Code/Coworkの自己ホスト型環境(セルフホスト環境)ベータ・Chrome連携・Compliance API拡大を追記。Fable 5と同等性能で政府連携プログラム経由のみ提供される「Mythos 5」の位置づけ、ブラウザ操作エージェント「Claude in Chrome」についても新設
- **出典**: [Anthropic: Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)、[techjournal.org: Claude Sonnet 5 Pricing Now Permanent](https://techjournal.org/claude-sonnet-5-pricing-now-permanent)、[explainx.ai: Claude Sonnet 5 Pricing Locked at $2/$10](https://explainx.ai/blog/anthropic-sonnet-5-permanent-pricing-august-2026)、[TechCrunch: Anthropic launches Claude Sonnet 5 as a cheaper way to run agents](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)、[Anthropic: Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)、[exodata.io: Claude Mythos 5 & Project Glasswing, Explained for Security Teams](https://exodata.io/claude-mythos-5-project-glasswing-security-teams/)、[Tom's Guide: Claude Artifacts are now free for all](https://tomsguide.com/ai/claude-artifacts-are-now-free-for-all-7-prompts-to-try-it-for-yourself)、[ppc.land: Claude artifacts expand to enable AI-powered app creation](https://ppc.land/claude-artifacts-expand-to-enable-ai-powered-app-creation/)、[X/Claude: Chat and Cowork are moving into one home](https://x.com/claudeai/status/2074525819414647044)、[Claude by Anthropic: Compliance API coverage extends to Claude Cowork and Claude Code](https://claude.com/blog/compliance-api-cowork-and-claude-code)、[Releasebot: Claude Code Updates - August 2026](https://releasebot.io/updates/anthropic/claude-code)、[9to5Mac: Claude's Chrome side panel is now a full Cowork session](https://9to5mac.com/2026/08/12/claude-cowork-chrome/)、[explainx.ai: Claude in Chrome: Features, Access & Safety](https://explainx.ai/blog/claude-in-chrome-browser-extension-guide-safety-2026)、[testingcatalog: Anthropic plans Claude memory update with new Memory Files](https://www.testingcatalog.com/anthropic-plans-claude-memory-update-with-new-memory-files/)

### 2026-07-19: プラン構成・モデルラインナップ・機能面を最新化
- **内容**: Sonnet 5がFree/Proの既定モデルになったこと(2026年7月1日〜)、Team Standard/Premium席の料金・内容、Claude Cowork(2026年1月提供開始、7月からクラウド対応拡大)の追加、Memory機能の全ユーザー展開(2026年3月〜)、拡張思考から適応的な推論への置き換え、claude.ai上のWeb検索・Computer Use相当機能を追記。既存のプラン表・API料金表は数値を再確認し、事実として維持
- **出典**: [Anthropic公式: Plans & Pricing](https://claude.com/pricing)、[Anthropic公式: Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)、[TechCrunch: Anthropic launches Claude Sonnet 5 as a cheaper way to run agents](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)、[EdTech Innovation Hub: Claude Sonnet 5 becomes Anthropic's default model](https://www.edtechinnovationhub.com/news/anthropic-makes-claude-sonnet-5-the-default-for-free-and-pro-users)、[Anthropic公式: Claude Cowork](https://www.anthropic.com/product/claude-cowork)、[Claude Help Center: Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)、[TechCrunch: Claude Cowork expands to mobile and web](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/)、[9to5Mac: Anthropic expanding Claude Cowork to mobile and web](https://9to5mac.com/2026/07/13/anthropic-expanding-claude-cowork-to-mobile-and-web-details-here/)、[Claude Help Center: What is the Team plan?](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)、[Claude Help Center: What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)

### 2026-07-05: 初版執筆
- **内容**: Claudeの位置づけ(ChatGPT・Geminiとの違い)、claude.aiの個人向け・法人向けプラン、Claude APIのモデルラインナップと料金、Claude Code・Artifacts・Projects機能の概要を整理
- **出典**: [Anthropic公式: Pricing(Claude Platform Docs)](https://platform.claude.com/docs/en/about-claude/pricing)、[Uravation: Claude料金比較｜Free/Pro/Max/Team/Enterprise【2026】](https://uravation.com/media/claude-pricing-plan-complete-guide-2026/)、[JAPAN AIラボ: Claudeの料金プランを徹底比較](https://japan-ai.co.jp/media/5975/)、[マネーフォワード クラウド: Claudeのプロジェクト機能とは](https://biz.moneyforward.com/ai/basic/4463/)、[Claude Help Center: How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)、[Claude Help Center: What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)、[Claude Code Docs: Claude Codeの概要](https://code.claude.com/docs/ja/overview)
