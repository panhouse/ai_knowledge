---
title: Claude(Anthropic)の基本
part: 3
chapter: 第5章 主要ツール各論
tags: [Claude, Anthropic, Claude Code, Cowork, モデルラインナップ]
created: 2026-07-05
updated: 2026-07-19
---

# Claude(Anthropic)の基本

## これは何か

Claudeは、AI企業Anthropic(アンソロピック)が開発する生成AIで、ChatGPT(OpenAI)、Gemini(Google)と並ぶ三大LLM(大規模言語モデル。文章生成AIの基盤技術)の一つ。「ChatGPTは知っているが、Claudeは何が違うのか分からない」という人が多いが、実はモデル名の付け方・プラン構成・強みの傾向がそれぞれ異なる。ここではClaudeのラインナップと、他ツールとの使い分けの目安を整理する。

## 仕組み・背景

Anthropicは2021年に元OpenAIの研究者らが設立したAI企業で、AIの安全性を重視した開発方針を掲げているのが特徴。Claudeは個人向けチャットサービスの**claude.ai**(Web・スマホアプリ・デスクトップアプリ)と、開発者・企業がシステムに組み込むための**Claude API**(開発者向けの従量課金サービス)の2系統で提供されており、この2つは契約・請求が別立てになっている(ChatGPTの「ChatGPT Plus」契約と「OpenAI API」の従量課金が別会計であるのと同じ構造)。

モデル名は「Opus(オーパス、大作)」「Sonnet(ソネット、定型詩)」「Haiku(俳句)」という文学・音楽の形式名をグレード(性能・価格帯)として使い、最上位には「Fable(寓話)」というシリーズ名が使われている。世代を表す数字(例: Sonnet 5、Opus 4.8)は数か月単位で更新されることが多く、名称・価格ともに変更頻度が高い。2026年6月30日には新シリーズの「Sonnet 5」が登場し、翌7月1日からFree・Proプランの既定モデルがSonnet 5に切り替わった。

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

### 個人向けプラン(claude.ai、2026年7月時点の目安)

| プラン | 月額目安 | 主な違い |
|---|---|---|
| Free | $0 | 2026年7月1日から既定モデルがSonnet 5に。Projects・Artifacts・Memory(会話の記憶)などの主要機能も試せるが利用量の上限が低く、Cowork・Claude Codeは利用不可 |
| Pro | $20(年払いなら$17/月相当) | Free比で約5倍の利用量。Opus 4.8・Fable 5にもアクセス可。2026年1月からClaude Cowork・Claude Codeも利用可能になった |
| Max 5x | $100 | Free比で約25倍(Pro比で約5倍)の利用量。混雑時の優先アクセス |
| Max 20x | $200 | Free比で約100倍(Pro比で約20倍)の利用量。ヘビーユーザー向け |
| Team(Standard席) | 1人$25/月(年払いで$20/月相当) | 管理機能・一括請求・プロジェクトの組織内共有。Claude Code・Cowork・Microsoft 365やSlack等との連携も利用可 |
| Team(Premium席) | 1人$125/月(年払いで$100/月相当) | Standard席の約5倍の利用量。コーディングなど利用量が多いメンバー向け |
| Enterprise | 座席$20/月〜+使用量は別途API料金で請求 | SSO・監査ログ・カスタムのデータ管理など大企業向け機能。使用量が変動する組織向け |

Team・Enterpriseの最低契約席数や条件は情報源により表記が揺れているため(2〜5席など)、契約前に必ず[Anthropic公式の料金ページ](https://claude.com/pricing)で最新の金額・条件を確認すること。料金・利用上限はAnthropicの発表頻度が高く、日本向けには2026年4月から消費税が別途請求される運用になっている。

### 個人向けプランで使えるモデル

Freeプランは既定でSonnet 5(旧Sonnet 4.6相当の後継)、Haiku 4.5が利用可能。Pro・Max・Team・Enterpriseでは、これに加えて最上位モデルのFable 5、および高性能なOpus 4.8にもアクセスできる。画面右上のモデル選択メニューから、プランで利用可能な範囲のモデルを都度選べる。

### 開発者向け:Claude APIのモデルラインナップ(2026年7月時点)

| モデル | モデルID | コンテキスト | 入力$/1M | 出力$/1M | 位置づけ |
|---|---|---|---|---|---|
| Claude Fable 5 | `claude-fable-5` | 1M | $10.00 | $50.00 | 最も高性能。最も難しい推論・長時間の自律的エージェント作業向け(最大出力128K) |
| Claude Opus 4.8 | `claude-opus-4-8` | 1M | $5.00 | $25.00 | 最も高性能なOpus系統。長時間の自律作業やナレッジワークに強い |
| Claude Sonnet 5 | `claude-sonnet-5` | 1M | $3.00(2026年8月31日まで導入価格$2.00) | $15.00(導入価格$10.00) | 速度と知能のバランス型。coding・エージェント作業でOpusに迫る品質。claude.aiのFree/Proの既定モデル |
| Claude Haiku 4.5 | `claude-haiku-4-5` | 200K | $1.00 | $5.00 | 最速・最安価。簡単なタスク・大量処理向け |

上記は現行世代の主要モデル。旧世代のOpus 4.7・Opus 4.6・Sonnet 4.6も引き続きAPIから利用できるが、新規に組む場合は上表の現行モデルを使うのが基本。料金は変更・改定が非常に多いため、実装・見積もりの前には必ず[Anthropic公式のPricingページ](https://platform.claude.com/docs/en/about-claude/pricing)で最新の値を確認すること。プロンプトキャッシュ(繰り返し使う長いプロンプトを安く再利用する仕組み)やBatch API(即時性が不要な処理を50%引きで処理する仕組み)を使うと、実際のコストはさらに下げられる。

### Claude Code(開発者向けCLIツール)

Claude Codeは、ターミナル(コマンドライン画面)上で動くAnthropic製のAIコーディングエージェントで、コードベースの読み取り・ファイル編集・コマンド実行・Git操作などをAIに任せられる開発支援ツール。2026年1月からPro以上のプラン(Max/Team/Enterprise)や従量課金のAPIから利用できるようになった。ターミナルだけでなくIDE・デスクトップアプリからも操作できる。詳細な使い方は別トピックで扱う。

### Claude Cowork(非エンジニア向けの汎用エージェント機能)

Claude Cowork(コワーク)は、Claude Codeと同じエージェント基盤を、ターミナル操作なしで一般業務に転用した機能。指定したフォルダへの読み書き権限をClaudeに与えることで、資料作成・調査・整理といった複数ステップの作業を「その場で説明する」のではなく実際に最後まで実行させられる。2026年1月にMax限定で提供開始後、数日でPro以上の全有料プランに開放された。デスクトップアプリが中心だが、2026年7月からはクラウド上での実行(Web・モバイルからの操作、PCがオフラインでも作業継続)にも対応が広がっている。作業ステップ(開いたファイル・使ったツール・下した判断)を逐次確認・介入でき、定型作業は一定間隔で自動実行するスケジュール設定も可能。Freeプランでは利用できない。

### Artifacts機能(生成物のプレビュー・編集)

Artifactsは、Claudeが生成したコード・文書・簡単なWebアプリなどを、会話とは別のプレビュー画面に表示し、その場で編集・再生成できる機能。ChatGPTの「Canvas」、Geminiの「Canvas」に近い位置づけの機能で、無料プランでも利用できる。

- 有効化: claude.aiの左下のアカウント名 → 「設定」→「アーティファクトを有効にする」をオン
- 使い方: 通常どおりプロンプトを入力するだけで、まとまった分量のコード・文書を生成する際に自動でArtifacts画面が開く

### Projects機能(ChatGPTのGPTs、GeminiのGemに相当)

Projectsは、特定の業務・案件専用に「カスタム指示」と「ナレッジ(参照資料)」をひとまとめにしたワークスペースを作れる機能。Pro以上のプランで利用できる。

作成手順の目安:
1. claude.ai/projects を開き、「+ 新規プロジェクト」をクリック
2. プロジェクト名と説明を入力
3. 「カスタム指示」欄に、口調・出力形式・前提条件などを記入(例:「ですます調で書く」「専門用語には必ず一言説明を付ける」)
4. 「ナレッジ」欄に、会社概要・商品情報・過去の提案書などのファイルをアップロード
5. 以後、そのプロジェクト内で開始した会話はすべて、この指示とナレッジを踏まえて回答される

### Memory機能(会話をまたいだ記憶)

2026年3月、無料プランを含む全ユーザーにMemory(記憶)機能が展開された。ユーザーの名前・文章の好み・進行中のプロジェクトの文脈などを、会話をまたいで自動的に記憶し、次回以降の会話に反映する。記憶内容は「設定 → Capabilities(機能) → Memory」から一覧で確認・編集・削除できるため、機微な情報が誤って記憶された場合はここで削除する。

### 拡張思考(Extended Thinking)→ 適応的な推論(Adaptive Reasoning)

以前は「拡張思考」を明示的にオン/オフしたり、考える分量(トークン予算)を指定する必要があったが、2026年2月ごろのモデル世代(4.6系)以降は、Claudeが問題の難しさを内部で判断し、考える必要があるか・どこまで深く考えるかを自動的に決める「適応的な推論」に置き換わっている。ユーザー側での複雑な設定は基本的に不要になった。

### Web検索・Computer Use(コンピュータ操作)

claude.aiにはWeb検索機能が組み込まれており、最新情報を検索して出典付きで回答に反映できる(設定でオン/オフ可能)。加えて、ファイル整理・メール送信・スケジュール管理など、ユーザーのデバイス上での操作を自動化する「Computer Use(コンピュータ操作)」に相当する機能も提供されている。これらはCowork・Claude Codeのようなエージェント機能とあわせて、単なる会話にとどまらない「作業の実行」をClaudeに任せる方向性の一部。

## 注意点・よくある誤解

- **モデル名・料金の変更頻度が非常に高い**: 数か月単位で新モデルが出て旧モデルの価格が変わる。本ページの数値は目安であり、見積もり・契約の前には必ず公式サイトで確認する
- **claude.aiの契約とAPIの契約は別会計**: Pro/Maxなどのサブスクリプションに入っていても、開発者向けAPIの利用料は別途従量課金になる(逆にAPI利用者がclaude.aiを個人利用したい場合も別途契約が必要)
- **Sonnet 5には期間限定の導入価格がある**: 2026年8月31日までは入力$2.00/出力$10.00の導入価格だが、それ以降は入力$3.00/出力$15.00の通常価格に切り替わる。長期のコスト試算をする際はこの切り替わりを踏まえること
- **「Claude」「Claude Code」「Claude Cowork」を混同しない**: 「Claude」はチャットサービス全般の名称、「Claude Code」は開発者向けCLIツール、「Claude Cowork」はターミナル操作なしで一般業務を任せるエージェント機能。それぞれ利用可能プランや操作方法が異なる
- **CoworkはFreeプランでは使えない**: エージェント的にファイルを読み書きする機能はPro以上の有料プラン限定。無料プランで試せるのはチャット・Artifacts・Memoryなど

## 最初の一歩

claude.aiに無料アカウントで登録し、Artifacts機能を有効にしたうえで、社内資料の要約や簡単な文面のたたき台作成を1つ試してみる。

## 関連トピック

- [Google Geminiの基本](./google-gemini-basics.md)
- [OpenAI APIの基本](../part09-api-development/openai-api-basics.md)
- [Function Calling(Tool Use)の基本](../part09-api-development/function-calling-basics.md)

## 更新履歴

### 2026-07-19: プラン構成・モデルラインナップ・機能面を最新化
- **内容**: Sonnet 5がFree/Proの既定モデルになったこと(2026年7月1日〜)、Team Standard/Premium席の料金・内容、Claude Cowork(2026年1月提供開始、7月からクラウド対応拡大)の追加、Memory機能の全ユーザー展開(2026年3月〜)、拡張思考から適応的な推論への置き換え、claude.ai上のWeb検索・Computer Use相当機能を追記。既存のプラン表・API料金表は数値を再確認し、事実として維持
- **出典**: [Anthropic公式: Plans & Pricing](https://claude.com/pricing)、[Anthropic公式: Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)、[TechCrunch: Anthropic launches Claude Sonnet 5 as a cheaper way to run agents](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)、[EdTech Innovation Hub: Claude Sonnet 5 becomes Anthropic's default model](https://www.edtechinnovationhub.com/news/anthropic-makes-claude-sonnet-5-the-default-for-free-and-pro-users)、[Anthropic公式: Claude Cowork](https://www.anthropic.com/product/claude-cowork)、[Claude Help Center: Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)、[TechCrunch: Claude Cowork expands to mobile and web](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/)、[9to5Mac: Anthropic expanding Claude Cowork to mobile and web](https://9to5mac.com/2026/07/13/anthropic-expanding-claude-cowork-to-mobile-and-web-details-here/)、[Claude Help Center: What is the Team plan?](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)、[Claude Help Center: What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)

### 2026-07-05: 初版執筆
- **内容**: Claudeの位置づけ(ChatGPT・Geminiとの違い)、claude.aiの個人向け・法人向けプラン、Claude APIのモデルラインナップと料金、Claude Code・Artifacts・Projects機能の概要を整理
- **出典**: [Anthropic公式: Pricing(Claude Platform Docs)](https://platform.claude.com/docs/en/about-claude/pricing)、[Uravation: Claude料金比較｜Free/Pro/Max/Team/Enterprise【2026】](https://uravation.com/media/claude-pricing-plan-complete-guide-2026/)、[JAPAN AIラボ: Claudeの料金プランを徹底比較](https://japan-ai.co.jp/media/5975/)、[マネーフォワード クラウド: Claudeのプロジェクト機能とは](https://biz.moneyforward.com/ai/basic/4463/)、[Claude Help Center: How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)、[Claude Help Center: What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)、[Claude Code Docs: Claude Codeの概要](https://code.claude.com/docs/ja/overview)
