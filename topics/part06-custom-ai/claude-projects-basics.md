---
title: "Claude(Anthropic)の「プロジェクト」機能の基本"
part: 6
chapter: 第2章 主要ツールでの作り方
tags: [Claude, Projects, カスタムAI, Anthropic, Fable 5, Opus 5]
created: 2026-07-06
updated: 2026-08-19
---

# Claude(Anthropic)の「プロジェクト」機能の基本

## これは何か

Claude.aiで毎回「うちの会社は◯◯業で、こういう規程があって……」と前提を説明し直してから質問している人は多い。**Projects(プロジェクト)**は、この前提説明(カスタム指示)と参照資料(ナレッジ)、会話履歴を1つの箱にまとめて、以降はその箱の中で始めた会話すべてに自動で適用できるようにする機能である。ChatGPTのGPTs・GeminiのGemと同じ「自分専用AIを作る」機能群の1つで、プログラミング不要という点も共通している。

## 仕組み・背景

Projectsは「カスタム指示(project instructions)」「ナレッジ(参照ファイル)」「会話履歴」の3点を1つのワークスペースにまとめる仕組みで、プロジェクト内で新しい会話を始めるたびに、指示とナレッジが自動的に読み込まれる。

- **カスタム指示**: そのプロジェクト内のすべての会話に適用される、役割・トーン・回答ルールなどの指示文。GPTsの「Instructions」、Gemの「カスタム指示」に相当する
- **プロジェクトナレッジ**: PDF・Word・スプレッドシート・コードなどをアップロードしておくと、会話の中でClaudeが参照する。1ファイルあたり30MBが上限で、アップロード数自体には上限がない(ただし後述のコンテキスト容量には収まる必要がある)
- **コンテキストウィンドウとRAGモードへの自動切り替え**: プロジェクトが一度に読み込める分量は200,000トークン(日本語で数百ページ相当)が基本上限だが、有料プラン(Pro/Max/Team/Enterprise)では、アップロードしたナレッジがこの上限に近づくと、Claudeが自動的に**RAG(検索拡張生成、必要な部分だけを都度検索して参照する仕組み)モード**に切り替わり、実質的な容量を最大10倍(約200万トークン相当)まで拡張できる。全文を読み込む場合と応答品質は変わらないとされているが、「アップロードした全文を毎回読んでいる」わけではなくなる点は、後述の注意点で扱う
- **利用できるモデル**: プロジェクト内の会話でも、画面上部のモデル選択から通常のClaude.aiと同じモデルを選べる。2026年7月24日に**Opus 5**が登場し、Opus 4.8の後継としてMaxプランの既定モデル・Proプランで選べる最上位モデルの座を引き継いだ(Opus 4.8も選択肢としては残る)。このほかSonnet 5・Haiku 4.5・最上位モデルのFable 5が選べる。Fable 5は2026年7月20日以降、Max/Team Premiumプランには利用上限の50%相当で標準搭載される一方、Pro/Team Standardプランでは一度きりの利用クレジット経由でのアクセスに限られる(詳細は「実務での使い方」)
- **Cowork(タスクを丸ごと任せるエージェント機能)との統合**: 2026年7月以降、Web版・デスクトップ版ではChatとCoworkのホーム画面・サイドバーが統合され、Projectsとartifactsは両モードで共通して扱われるようになった。プロジェクト内でカスタム指示・ナレッジを詰めた上で、実際の作業だけをCoworkに任せる、という使い分けがしやすくなっている(Coworkの詳細は[Claude Cowork(エージェント型タスク実行)の基本](../part11-ai-agents/claude-cowork-basics.md)を参照)

なお、プロジェクト名・説明欄はあくまで自分たちの整理用のラベルであり、Claude自身がそれを読んで挙動を変えるわけではない(実際の振る舞いを決めるのはカスタム指示とナレッジ)。

## 使いどころ・使い分け

| 目的 | 使う機能 |
|---|---|
| 特定の業務・クライアント案件専用の相談相手を作りたい | Projectsでカスタム指示+ナレッジを設定 |
| 過去の会話を積み重ねながら1つのテーマを深掘りしたい | Projects内で会話を継続(会話履歴が同じ文脈で参照される) |
| コードを書きながら生成物(文章・表・簡易アプリ等)をその場で確認・編集したい | Projects内でArtifacts(生成物を専用パネルに表示する機能)を併用 |
| 社内の複数人に同じ設定のAIを使わせたい | Team/Enterpriseプランでプロジェクトを組織内共有 |
| 外部に一般公開してストアに掲載したい | 非対応(ChatGPTのGPTストアのような公開マーケットプレイスはなく、共有範囲は自組織内に限られる) |

ChatGPTのGPTs・GeminiのGemとの主な違いは次の通り。

| 観点 | Claude Projects | ChatGPTのGPTs | GeminiのGem |
|---|---|---|---|
| 外部API連携(Actions) | 非対応(Claude API側でTool Useを組む必要がある) | 対応(Actions) | 非対応 |
| 一般公開・マーケットプレイス | なし(組織内共有のみ) | あり(GPTストア) | なし |
| 無料プランでの利用 | 無料化済み(作成できるプロジェクト数は上限5個) | 作成不可(利用のみ) | 一部機能に制限あり |
| ナレッジの参照方式 | 容量超過時に自動でRAGモードへ切り替え | ファイル検索(内部的に同様の仕組み) | Saved infoやドライブ連携 |
| 生成物の編集体験 | Artifacts(コード・文書をその場で編集) | Canvas | Canvas |

「外部システムと連携させたい・不特定多数に公開したい」ならGPTs、「Google系サービス(スプレッドシート等)との連携を重視したい」ならGem、「長文の資料を読み込ませて深く対話し、生成物をその場で編集したい」ならClaude Projects、という住み分けで検討するとよい。

## 実務での使い方

### 作成手順(2026年8月時点の目安)

1. claude.aiにログインし、左サイドバーの「Projects」をクリック
2. 「+ New project」(新規プロジェクト作成)をクリック
3. プロジェクト名と説明(任意、自分たちの整理用)を入力
4. 「Set project instructions」からカスタム指示を記入し、保存する
5. プロジェクト画面の「Add content」(+ボタン)から、参照させたいファイルをアップロードする
6. プロジェクト内で「New chat」を開始すると、以降その会話にカスタム指示とナレッジが自動適用される

### コピペで使えるカスタム指示の記入例

```
## 私について
[このプロジェクトを使う想定ユーザー。例: "中小企業の人事担当者"]

## このプロジェクトの目的
[何のためのプロジェクトか。例: "就業規則・給与規程に関する社内問い合わせに答える"]

## 期待するアウトプット
- 添付のナレッジ(規程集)に書かれている内容を根拠に回答する
- ナレッジに記載がない場合は、推測せず「規程に記載がありません」と答える
- 回答の最後に、根拠にした規程の項番を示す
```

### Team/Enterpriseでの共有

プロジェクト作成時に公開範囲を選べる。

| 選択肢 | 対象 | 権限 |
|---|---|---|
| Private | 自分のみ | 自分が編集・利用 |
| 組織内共有(旧称Public) | 同じTeam/Enterpriseワークスペースの全メンバーまたは指定メンバー | メンバーごとに「Can use」(閲覧・利用のみ)または「Can edit」(指示・ナレッジの編集・メンバー管理も可)を招待時に選択 |

共有プロジェクトであっても、メンバー各自が行った個々の会話の中身自体は既定で他メンバーに見えない(共有されるのはカスタム指示とナレッジ、明示的に共有した会話のみ)。

### プラン別の料金とプロジェクト・モデルの使える範囲(2026年8月時点)

| プラン | 料金の目安 | Projects作成数 | Fable 5へのアクセス |
|---|---|---|---|
| Free | 無料 | 上限5個 | 基本的に対象外(有料プランへのアップグレードが必要) |
| Pro | 月額$20(年払いなら実質$17) | 実質無制限 | 利用クレジット経由(初回$100分付与、消化後はAPI料金相当で従量課金) |
| Max 5x / Max 20x | 月額$100 / $200 | 実質無制限 | 利用上限の一部としてFable 5を含む(2026年7月20日以降、通常モデル比50%相当の上限で標準搭載) |
| Team Standard | 1シートあたり月額$25(年払い$20、最低5シート) | 実質無制限 | 利用クレジット経由(Proと同様) |
| Team Premium | 1シートあたり月額$125(年払い$100) | 実質無制限 | Max同様、標準搭載(上限50%相当) |
| Enterprise | 個別見積もり | 実質無制限 | 契約内容による(営業担当に確認) |

Fable 5(Claudeの最上位モデル)は2026年7月20日から料金プランへの組み込みが整理され、Max・Team Premiumでは「他モデルの半分の利用上限」で常時使えるようになった一方、Pro・Team Standardでは都度クレジットを消費する形が続く。プロジェクト内でどのモデルを使うかは会話ごとにモデル選択メニューから切り替えられるため、「重い分析・自律的な作業はFable 5、コーディングや複雑な推論はOpus 5、日常的なやり取りはSonnet 5」のように使い分けるとよい。

### Google Drive・GitHubとの連携

プロジェクトの「Add content」からGoogle Drive連携(読み取り専用。ファイルの検索・要約・横断分析はできるが、編集・作成・移動はできない。Google DocsをAdd contentで追加すると、ドライブ上の更新がプロジェクトナレッジにも自動反映される)やGitHubリポジトリの参照を追加できる。ただしGoogle Drive連携は、2026年7月時点でも**Privateなプロジェクトでのみ利用可能で、組織内共有プロジェクトでは無効**になる点に変わりはない。

## 注意点・よくある誤解

- **「アップロードした資料は毎回全文読まれる」とは限らない**: プロジェクトナレッジが容量上限(200,000トークン)に近づくとRAGモードに自動移行し、質問に関連しそうな部分だけを検索して参照する挙動に変わる。全文を毎回精読しているわけではないため、「資料に書いてあるのに答えに反映されない」場合は、この切り替えが起きていないか疑う
- **無料プラン(Free)でもProjectsが使えるが上限がある**: Freeプランでも解放されているが、作成できるプロジェクト数には上限(5個)がある。頻繁に新しいプロジェクトを作る運用には向かないため、業務単位・案件単位でプロジェクトを使い回す設計にする
- **Fable 5は「使い放題」ではない**: Max・Team Premiumでも他モデルの半分の利用上限という制約付きで、Pro・Team Standardでは追加クレジットが尽きるとAPI従量課金相当の料金がかかる。ヘビーに使う想定なら、プロジェクトのモデル選択を都度確認し、日常タスクはSonnet 5やHaiku 4.5に切り替えるコスト意識を持つ
- **GPTsのような外部一般公開・マーケットプレイスはない**: 社外の不特定多数に使わせたい場合はProjectsでは実現できない。その用途はChatGPTのGPTsを検討する
- **Google Drive連携は共有プロジェクトでは使えない**: チームで使うプロジェクトにドライブ連携をそのまま持ち込もうとすると設定できず戸惑うことがある。共有プロジェクトではファイルを都度アップロードする運用に切り替える
- **機密情報の取り扱いはプランで扱いが異なる**: Free/Pro/Max(個人向けプラン)は既定でモデルの学習に利用され得る設定になっており、学習に使われたくない場合は「設定→プライバシー→Help improve Claude」をオフにする必要がある。Team/Enterprise(商用契約)は契約上、顧客のコンテンツをモデルの学習に使わないことが原則になっている。機密性の高い資料を扱うプロジェクトは、契約形態を確認してから作る

## 最初の一歩

自分が繰り返し同じ前提を説明してからClaudeに相談している業務を1つ選び、その前提をカスタム指示に、関連資料をナレッジに登録したプロジェクトを1つ(Privateで)作ってみる。

## 関連トピック

- [GPTsの作り方と公開設定](gpts-creation-basics.md)
- [Gem(Geminiのカスタムボット機能)の基本](gemini-gem-feature.md)
- [Claude(Anthropic)の基本](../part03-ai-chat-tools/claude-basics.md)
- [Claude Cowork(エージェント型タスク実行)の基本](../part11-ai-agents/claude-cowork-basics.md)

## 更新履歴

### 2026-08-19: Opus 5の登場とCowork統合を反映して最新化
- **内容**: 2026年7月24日に登場したOpus 5がOpus 4.8を継いでMaxプランの既定モデル・Proプランの最上位選択モデルになったことを「利用できるモデル」節とモデルの使い分けの記述に反映。Web/デスクトップ版でChatとCoworkのホーム画面・サイドバーが統合され、Projects/artifactsが両モードで共通化された点を新設し、Coworkの基本ページへの相互リンクを追加。料金プラン表・Fable 5のアクセス条件・ファイル容量(30MB/ファイル)・RAGモードへの自動切り替え・Free版のプロジェクト数上限(5個)・Google Drive連携の制約は2026年8月時点でも変更がないことを裏取りの上で確認し、日付表記のみ更新
- **出典**: [Axios: Anthropic releases new model, Opus 5](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5)、[X (@mikeyk): Chat and Cowork now share one home tab](https://x.com/mikeyk/status/2074531605537046953)、[TechCrunch: Claude Cowork expands to mobile and web](https://techcrunch.com/2026/07/07/the-coding-agent-wars-are-spilling-into-the-rest-of-the-office-claude-cowork/)、[VentureBeat: Anthropic brings Claude Cowork to mobile and web](https://venturebeat.com/technology/anthropic-brings-claude-cowork-to-mobile-and-web-as-usage-data-shows-most-users-arent-coding)、[Tech Times: Claude Fable 5 Billing Splits Today](https://www.techtimes.com/articles/320999/20260720/claude-fable-5-billing-splits-today-max-gets-it-free-pro-pays-per-token.htm)

### 2026-07-22: プラン・料金体系とFable 5関連の記述を最新化
- **内容**: プラン別の料金表(Free/Pro/Max 5x・20x/Team Standard・Premium/Enterprise)を新設し、2026年7月20日付でFable 5がMax・Team Premiumに標準搭載(他モデル比50%の利用上限)、Pro・Team Standardはクレジット経由アクセスになった変更を反映。プロジェクト内のモデル選択、RAGモードの実質容量(約200万トークン相当)、Google Drive連携・共有権限(「Can use」「Can edit」)の表記を裏取りの上で更新
- **出典**: [Claude Help Center: What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)、[Claude Help Center: Retrieval augmented generation (RAG) for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)、[Claude Help Center: Manage project visibility and sharing](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing)、[Claude Help Center: Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)、[Tygart Media: Claude Team Pricing 2026](https://tygartmedia.com/claude-team-pricing-2026-standard-premium-seats/)、[Tygart Media: Claude Pricing Tiers Compared](https://tygartmedia.com/claude-pricing-tiers-compared-free-pro-max-team-enterprise/)、[Claude Help Center: Claude Fable 5 on your plan](https://support.claude.com/en/articles/15424964-claude-fable-5-on-your-plan)、[Tech Times: Claude Fable 5 Ends Subscription Limbo](https://www.techtimes.com/articles/320905/20260718/claude-fable-5-ends-subscription-limbo-permanent-max-credits-only-pro.htm)

### 2026-07-06: 初版執筆
- **内容**: Claude Projectsの仕組み(カスタム指示・ナレッジ・会話履歴の統合、容量上限とRAGモードへの自動切り替え)、GPTs・Gemとの比較表、作成手順、カスタム指示の記入例、Team/Enterpriseでの共有設定、Google Drive/GitHub連携の制約、データ学習ポリシーの違いを整理
- **出典**: [Claude Help Center: What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)、[Claude Help Center: How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)、[Claude Help Center: Manage project visibility and sharing](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing)、[Anthropic: Collaborate with Claude on Projects](https://www.anthropic.com/news/projects)、[Claude Help Center: Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)、[Tom's Guide: Claude just made two of its best features free](https://www.tomsguide.com/ai/claude-just-made-two-of-its-best-features-free-heres-how-to-use-projects-and-artifacts)
