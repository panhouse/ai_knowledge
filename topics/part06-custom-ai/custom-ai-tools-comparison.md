---
title: GPTs・Gem・Copilot Agent・Claude Projectsの比較と使い分け
part: 6
chapter: 第2章 主要ツールでの作り方
tags: [GPTs, Gem, Copilot Studio, エージェントビルダー, Claude Projects, カスタムAI, ツール比較]
created: 2026-07-30
updated: 2026-09-15
---

# GPTs・Gem・Copilot Agent・Claude Projectsの比較と使い分け

## これは何か

「自分専用のAIを作りたいが、会社にはChatGPTもGeminiもCopilotもClaudeも入っている。どれで作ればいいのか」——これは、カスタムAI機能に手を付けようとした人が最初にぶつかる疑問である。ChatGPTの**GPTs**、Geminiの**Gem**、Microsoft 365 Copilotの**エージェントビルダー/Copilot Studio**、Claudeの**Projects**は、いずれも「指示+参照資料を1つのボットとして保存し、以降ワンクリックで呼び出す」という同じ発想の機能として並んで語られてきた。

しかし**2026年後半に入り、「4つとも対等な選択肢」という前提そのものが崩れている**。GPTsはOpenAIが新規作成を段階的に終了させる最中で、Gemも終了・後継機能への移行が(未確認情報ながら)報じられている。本ページは、この状況を踏まえて**2026年9月時点で実際に何が選べるか**を軸に4ツールを横並びで比較し、「自分の状況ならどれを選ぶべきか」の判断材料を1ページにまとめる。各ツール個別の詳しい作成手順・料金・終了スケジュールは、末尾の「関連トピック」にある各ツールの専用ページを参照してほしい。

## 仕組み・背景

4ツールはいずれも、次の3要素の組み合わせでできている。

1. **指示(システムプロンプト相当)**: 役割・トーン・回答ルールを固定で覚えさせる文章
2. **ナレッジ(参照ファイル)**: PDF・Excel等をアップロードし、会話の中でAIに参照させる
3. **公開範囲の設定**: 自分だけで使うか、チームに配るか、外部に公開するか

違いが出るのはここから先で、GPTsとCopilot Studioは「外部システムに接続して処理を実行する」機能(Actions/コネクタ)まで踏み込んでいるのに対し、GemとClaude Projectsは「指示+ナレッジで賢く答える」範囲にとどまる。この違いは今も変わらないが、2026年9月時点ではその前に「そもそも新しく作れるか」という、より根本的な違いが生じている。

| 概念 | ChatGPT | Gemini | Microsoft 365 Copilot | Claude |
|---|---|---|---|---|
| 呼び方 | GPTs(カスタムGPT) | Gem | エージェントビルダー(簡易版)/Copilot Studio(本格版) | Projects(プロジェクト) |
| 作成画面 | ChatGPT左サイドバー「GPTを探す」→GPT Builder(2026年9月時点、個人は新規作成不可) | gemini.google.com左メニュー「Gemを表示」→Gemマネージャー | 「Microsoft Copilot」アプリ(2026年8月に個人向け・M365向けアプリが統合、copilot.cloud.microsoftへ順次移行中)左ペイン「エージェント」、またはcopilotstudio.microsoft.com | claude.ai左サイドバー「Projects」 |
| 指示欄の呼称 | Instructions(指示) | カスタム指示 | 指示(自然言語で自動生成→手動調整) | Project instructions(カスタム指示) |

### GPTs・Gemの「終了」を前提に読む

- **GPTs**: OpenAIは2026年4月にGPTsの後継として「ワークスペースエージェント(workspace agents、Codex基盤)」を発表し、その後具体的な終了スケジュールを公開した。**個人(Free/Go/Plus/Pro)は2026年8月16日付けで新規GPTの作成・GPTストアへの新規公開ができなくなった**。**組織(Business/Enterprise/Edu/Teachers)も2026年9月25日ごろに新規作成が終了し、既存GPTs自体の完全停止(退役)は2026年12月11日ごろが予定されている**(Enterprise向けの公表スケジュール。ワークスペースにより前後する可能性がある)。既存GPTの利用・編集は退役日まで継続でき、OpenAIのヘルプセンターも公開の必要なく退役前に下書きを移行できるとしているが、「今からGPTsで何かを新しく作る」という選択肢は個人・組織ともにすでに、あるいはまもなく閉じる([OpenAI Help Center: Custom GPT retirement and migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq))
- **Gem**: 2026年8月上旬、Geminiアプリの一部ユーザー向けに「Gemは10月20日に終了し、後継の『Skills』(Gemini Spark内の機能)への移行を」という告知バナーが機能フラグの裏で見つかったと複数の海外メディアが報じている。2026年9月時点でもGoogleの公式発表はなく実施時期・有無は未確定だが、報道通りなら後継のSkillsはGoogle AI Pro/Ultraの有料契約必須・個人アカウント限定・一部地域(EEA・英国・スイス・ナイジェリア)対象外とされ、無料ユーザーや対象地域のユーザーは同等機能を失う可能性がある

両ツールとも、後継として挙がっているのが「Skills」という共通の名前である点は偶然ではない。Anthropicが2025年10月にClaudeへ導入した`SKILL.md`という「タスクの手順書をフォルダで持たせる」形式が、Google(Gemini Spark)・Microsoft(Copilot Studioの新設「Skills」)にも同種の仕組みとして広がりつつあり、「指示+ナレッジを1つのボットに固定する」旧来のGPTs/Gem型のカスタムAIから、「特定タスクの手順を必要な時だけ読み込ませる」Skills型の設計へ、業界全体が緩やかに移行している段階にある(詳しくは[AIエージェントのSkills(スキル)機能とは何か](../part11-ai-agents/claude-skills-and-agent-skills-basics.md)を参照)。ただしSkillsは「専用ボットを作って呼び出す」GPTs/Gem/Projectsとは役割が異なり、単純な代替品ではない点に注意する。

## 使いどころ・使い分け

判断の起点は、まず「そもそも新しく作れるか」、その上で「何を外に繋ぎたいか」「誰に公開したいか」の3つである。

| こういう場合は… | 向いているツール | 理由 |
|---|---|---|
| 今から新しく、不特定多数に公開するボットを作りたい | **実質的に新規の選択肢はない** | GPTsは個人が2026年8月16日、組織が2026年9月25日ごろから新規作成不可。GPTストアへの新規掲載もできない。他の3ツールは一般公開マーケットプレイス自体を持たない |
| すでに社内で稼働しているGPTを保守・改修したい | **既存のGPTsをそのまま維持**(ただし移行計画は必須) | 編集・利用は退役予定日(2026年12月11日ごろ)まで継続可能。退役前にワークスペースエージェント等への移行を計画する |
| CRM・ERP・チケット管理などの業務システムと繋いで、承認フローや自動処理までさせたい | **Copilot Studio** | Power Platformの1,400以上のコネクタとマルチステップワークフローに対応するのはCopilot Studioのみ |
| SharePoint・OneDriveの社内文書だけを検索・要約するボットを最短で作りたい | **エージェントビルダー**(2026年8月に「Microsoft Copilot」アプリへ統合) | M365 Copilotライセンスに含まれ追加費用なし。知識源を指定するだけで完結する軽量版 |
| Google Drive・スプレッドシートなどGoogle系ファイルと連携させたい | **Gem**(ただし終了リスクを踏まえて使う) | Google Driveのファイルを常に最新版で参照でき無料でも作成できるが、2026年10月20日終了・Skills移行という未確認報道がある。指示文はGemini外にも保管しておく |
| 長文資料を読み込ませて深く対話し、生成した文書やコードをその場で編集したい | **Claude Projects** | Artifacts(生成物の専用編集パネル)と大容量ナレッジ(自動RAG化で実質約200万トークン相当)が強み。終了予定もない |
| 予算をかけず今日から無料で試したい | **Claude Projects**(Free、上限5個)、次点で**Gem** | GPTsは新規作成自体が不可。Copilot系はM365 Copilotライセンス(組織契約)が前提。Gemも無料だが終了リスクがある分Projectsを優先 |
| 外部APIを自作して呼び出させたい(自社サービス連携など) | **組織ならCopilot Studioのカスタムコネクタ、個人ならClaude APIやMCP経由のTool Use** | GPTsのActionsは既存GPTでは使えるが新規GPTでは設定できない。今から新しく作るなら、GPTs以外の経路を最初から選んでおく必要がある |

### 機能・条件の比較表(2026年9月時点)

| 観点 | GPTs(ChatGPT) | Gem(Gemini) | エージェントビルダー/Copilot Studio(Microsoft) | Projects(Claude) |
|---|---|---|---|---|
| 新規作成の可否 | **不可**。個人(Free/Go/Plus/Pro)は2026年8月16日付けで新規GPT作成・GPTストア公開が停止済み。組織(Business/Enterprise/Edu/Teachers)も2026年9月25日ごろに新規作成終了予定 | 作成可(無料プランでも可)。ただし2026年10月20日終了・後継「Skills」への移行という未確認報道あり(Google公式発表はまだない) | 作成可。エージェントビルダーはM365 Copilot(Copilot Chat含む)ライセンスに含まれ追加費用なし。社外公開のみCopilot Studioのスタンドアロンライセンスが必要 | 作成可。Freeでも作成可(上限5プロジェクト)。Pro以上は実質無制限 |
| 既存のものの扱い・終了予定 | 編集・利用は退役日まで継続可能だが、完全停止(退役)が2026年12月11日ごろに予定(Enterprise向け公表スケジュール、ワークスペースにより前後) | (終了報道が事実なら)10月20日以降は利用できなくなる可能性。自動移行は未確認 | 終了予定なし | 終了予定なし |
| ナレッジファイルの上限 | 最大20ファイル・1ファイル512MBまで(文書は概ね200万トークンまで) | 最大10ファイル・1ファイル100MBまで | エージェントビルダー: OneDrive約50件・添付ファイル約20件が目安/Copilot Studio: サイト・フォルダ単位でほぼ無制限 | 1ファイル30MBまで、ファイル数に上限なし(合計200,000トークンを超えると自動でRAGモードに切替、実質約200万トークン相当) |
| 外部API・業務システム連携 | Actions(OpenAPIスキーマで外部API呼び出し)。既存GPTでは利用継続可だが新規GPTでは設定不可 | 非対応 | Power Platformコネクタ(1,400以上)、Dataverse、マルチステップワークフロー(Copilot Studio) | 非対応(Claude API側でTool Useを別途実装する必要あり) |
| 主な知識源 | アップロードファイル | アップロードファイル/Google Drive(常に最新版を参照) | SharePoint/OneDrive/Dataverse/公開Webサイト/Microsoft Graph横断検索 | アップロードファイル/Google Drive(読み取り専用、Privateプロジェクト限定)/GitHub |
| 公開・共有範囲 | 自分のみ/リンク共有/GPTストアで一般公開(いずれも既存GPTのみ。新規参入は不可) | 非公開/リンク共有/組織内共有(管理者が可否を制御) | Teams/SharePoint/Webサイト/Slack等マルチチャネルで社内〜社外顧客まで、社内エージェントストアへの公開も可 | Private、Team/Enterpriseなら組織内共有(メンバーごとに「Can use」「Can edit」を設定) |
| 外部の一般公開マーケットプレイス | あり(GPTストア。ただし新規掲載は停止) | なし | なし(自組織のエージェントストアが基本) | なし |
| 生成物のその場編集機能 | Canvas | Canvas | なし | Artifacts |
| 使えるモデルの例 | GPT-5.6ファミリー(Sol/Terra/Luna) | Gemini 3.6 Flash(無料)、Gemini 3.1 Pro・3.7 Flash(有料) | (エージェント自体は特定モデル固定ではなくMicrosoft側の基盤モデルで動作) | Opus 5・Sonnet 5・Haiku 4.5・最上位のFable 5.1(2026年9月1日にFable 5から更新) |
| 料金の考え方 | プラン料金に含まれる(追加課金なし。ただし新規作成自体が不可) | プラン料金に含まれる(追加課金なし) | 社内利用は追加費用なし。社外公開・大量のアクション実行時のみCopilotクレジットを従量課金 | プラン料金に含まれる(上位モデルの多用時のみ利用上限に注意) |

## 実務での使い方

### 4ツールで使い回せる指示文の型

指示欄(システムプロンプト相当)の書き方は、実はどのツールでもほぼ同じ型が通用する。以下のテンプレートをベースに、末尾だけツールの呼称に置き換えれば使い回せる(GPTsについては、既存GPTの指示文を書き直す場合に使える)。

```
## 私について
[この専用AIを使う想定ユーザー。例: "中小企業の経理担当者"]

## 会社・業務について
[前提となる会社・業務の背景。例: "従業員50名の製造業。経費精算は月末締め"]

## このAIの役割
[何をしてほしいか。例: "経費精算ルールに関する質問に、添付の社内規程を根拠に答える"]

## 回答のルール
- 添付のナレッジファイルに書かれていないことは、推測せず「規程に記載がありません」と答える
- 回答の最後に、根拠にした規程の項番を示す
```

| 欄の呼び方 | ChatGPT(GPTs) | Gemini(Gem) | Microsoft 365 Copilot | Claude(Projects) |
|---|---|---|---|---|
| 指示欄 | Instructions(指示) | カスタム指示 | 指示(自然言語での自動生成が起点) | Project instructions |
| ナレッジ添付欄 | ナレッジ | ナレッジ(端末アップロード/Google Drive) | 知識を追加(SharePoint/OneDrive/添付ファイル/公開Webサイト等) | Add content(+ボタン) |

### 作成画面への入り口(一覧・2026年9月時点)

| ツール | 入り口 |
|---|---|
| GPTs | ChatGPT(Web版)にログイン→左サイドバー「GPTを探す」。**個人アカウントは新規作成ボタンが表示されない(2026年8月16日以降)**。既存GPTの編集は引き続き可能 |
| Gem | gemini.google.com→左メニュー「Gemを表示」→「Gemマネージャー」→「+新しいGem」 |
| エージェントビルダー | 「Microsoft Copilot」アプリ(copilot.cloud.microsoft、2026年8月に個人向け・M365向けアプリが統合され順次移行中)左ペイン「エージェント」→「+新しいエージェント」 |
| Copilot Studio | copilotstudio.microsoft.com にサインイン→左メニュー「エージェント」→「+作成」 |
| Claude Projects | claude.ai→左サイドバー「Projects」→「+ New project」 |

具体的な入力項目・設定手順(ナレッジの上限値、公開範囲の切り替え方、Actionsやコネクタの設定など)は、各ツールの専用ページに画面遷移込みで記載している。まずどのツールを使うか本ページで決め、詳細は該当ページを見る、という使い方を想定している。

### コスト面の意思決定材料(2026年9月時点の料金目安)

- **GPTsは新規作成の目的でプランを契約する意味がすでに薄い**: Plus以上($20/月、日本国内は¥3,000/月)は既存GPTの編集・利用には使えるが、新規GPT作成の解禁にはつながらない
- **追加費用ゼロで始めたいなら**: Claude Projects(Freeプラン、上限5個)が最も安定した無料の選択肢。Gemも無料プランで作成できるが、終了リスクを踏まえて重要な指示文は外部にも保管しておく
- **すでに契約しているプラン起点で選ぶ**: 会社がM365 Copilotを導入済みなら「Microsoft Copilot」アプリ内のエージェントビルダーが最も追加コストが低い(Business $18〜21/ユーザー/月、Enterpriseは$30/ユーザー/月が別途必要)。Google Workspaceが主戦場ならGem、ただし終了報道を踏まえて長期依存は避ける
- **外部公開・大量自動化まで見据えるなら**: 新規のGPTストア掲載はできないため、Copilot Studioの社外公開・大量アクション実行(Copilotクレジットの従量課金、$200/25,000クレジットのパック購入または$0.01/クレジットのPAYG)が現実的な選択肢になる。事前の試算が必須
- **Claude Projectsを本格運用するなら**: Pro($20/月)、Max($100/月〜$200/月)、Team Standard(1シート$20〜25/月)、Team Premium(1シート$100〜125/月)の料金帯があり、上位プランほどFable 5.1など最上位モデルの利用上限が広い

## 注意点・よくある誤解

- **「GPTsで新しく作ればいい」という前提がすでに崩れている**: 個人アカウントは2026年8月16日、組織アカウントも2026年9月25日ごろから新規GPT作成・GPTストア公開ができない。研修資料や過去の解説記事に「GPTsで作る」という選択肢が並んでいても、2026年9月時点では実行できない可能性が高い。既存GPTを保守する場合も、完全停止(2026年12月11日ごろ予定)より十分前に移行計画を立てる
- **Gemも「無料で使える定番」と決めつけない**: 2026年10月20日にGemが終了しSkillsへ一本化されるという報道は2026年9月時点でも未確定(Google公式発表なし)だが、実施された場合、無料プランや一部地域のユーザーは同等機能を失う可能性がある。重要な業務で使っているGemは、指示文を別途ドキュメント保管しておくとよい
- **「指示+ナレッジ」の機能だけを見て選ぶと、後で外部連携で詰まる**: GemとClaude Projectsは外部API・業務システム連携に対応しないため、「将来的にCRMや基幹システムと繋ぎたい」という要件があるなら、Copilot Studio(コネクタ)を選んでおいた方が作り直しの手間がない(GPTsのActionsは既存GPTのみ利用可能で新規の選択肢にはならない)
- **「公開」の意味がツールごとに違う**: GPTsの「誰でも(GPTストアに公開)」は文字通り世界中の誰でも使える状態を指す(ただし新規掲載自体は停止)が、Gem・Claude Projects・Copilot系の「共有」「公開」はいずれも自組織内(または招待した相手)止まりで、外部一般公開の機能自体を持たない
- **ナレッジファイルは「完全に機密」ではない**: どのツールでも、アップロードした資料の内容は共有範囲を広げるほど閲覧可能になる。機密情報を含む資料は、共有範囲を最も狭い設定(自分のみ/Private)にするか、組織の権限管理(SharePoint権限、Workspace管理者設定など)と連動させて運用する
- **ツール名・機能は変化が速い分野で、今まさに再編の最中**: Copilot Studioは2026年7月の大規模リビルドに続き2026年8月にアプリ統合も進み、GPTs・Gemは終了・移行のスケジュールが具体化している。本ページの比較表は執筆時点のスナップショットであり、実際に導入する際は各ツールの専用ページ(下記「関連トピック」)の更新履歴で最新状態を確認する

## 最初の一歩

自分が「毎回同じ前提を説明してから使っている」業務を1つ選ぶ。**もしGPTsで作ろうとしていたなら、まず自分のアカウントで新規作成ボタンが表示されるか確認し**、表示されない(すでに多くの場合そうなっている)場合は、上記の使い分け表からGPTs以外のツールを選んで、公開範囲「自分のみ」でカスタムAIを1つ作ってみる。

## 関連トピック

- [カスタムAIの基礎(共通設計原則)](custom-ai-design-principles.md)
- [GPTsの作り方と公開設定](gpts-creation-basics.md)
- [Gem(Geminiのカスタムボット機能)の基本](gemini-gem-feature.md)
- [Microsoft Copilot Studioによるカスタムエージェント作成の基本](copilot-agent-builder-basics.md)
- [Claude(Anthropic)の「プロジェクト」機能の基本](claude-projects-basics.md)
- [GPTsのナレッジファイルとアクション連携](gpts-knowledge-and-actions.md)
- [AIエージェントのSkills(スキル)機能とは何か](../part11-ai-agents/claude-skills-and-agent-skills-basics.md)

## 更新履歴

### 2026-09-15: GPTs新規作成の終了・Gem終了報道・料金/モデルを全面的に最新化
- **内容**: GPTsが個人(2026年8月16日〜)・組織(2026年9月25日ごろ〜)ともに新規作成不可となり、完全停止(退役)が2026年12月11日ごろに予定されていることを反映し、「使いどころ・使い分け」「機能・条件の比較表」「コスト面の意思決定材料」「注意点」を全面的に書き換え(「新規に何が作れるか」を最初の判断軸に変更)。Gemが2026年10月20日に終了し後継「Skills」(Gemini Spark)へ移行するという未確認報道(Google公式発表はまだない)を反映。Microsoft側の「Microsoft Copilot」アプリへの統合(2026年8月、copilot.cloud.microsoft)、Copilot StudioのSkills対応・料金体系を最新化。Claude Projectsの現行モデル(Opus 5・Sonnet 5・Haiku 4.5・2026年9月1日にFable 5から更新されたFable 5.1)と料金帯を反映。ChatGPT/Gemini/Microsoft 365 Copilot各プランの料金を2026年9月時点の数値に更新。GPTs/Gem双方の後継候補が「Skills」という共通名称である背景(SKILL.md形式の業界収れん)を新設し、Part 11のSkills解説ページへ相互リンクを追加
- **出典**: [OpenAI Help Center: Custom GPT retirement and migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq)、[OpenAI: Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)、[TestingCatalog: Google may retire Gems in October, forcing migration to Skills](https://www.testingcatalog.com/google-may-retire-gems-in-october-forcing-migration-to-skills/)、[Android Authority: Google could retire a free Gemini feature in favor of a paid one](https://www.androidauthority.com/google-retire-gemini-gems-leak-3696240/)、[futurework.blog: Microsoft Copilot app – one app, new name, new icon, new URL!](https://futurework.blog/2026/08/14/microsoft-copilot-app-one-app-new-name-new-icon-new-url/)、[CloudZero: Microsoft Copilot Studio Pricing In 2026](https://www.cloudzero.com/blog/copilot-studio-pricing/)、[MacRumors: Anthropic Launches Claude Fable 5.1 With Lower Costs and Fewer False Positives](https://www.macrumors.com/2026/09/01/anthropic-claude-fable-5-1/)、[theaicareerlab.com: ChatGPT Plans Compared (Sept 2026)](https://theaicareerlab.com/blog/chatgpt-pricing-plans-explained)、同ディレクトリ内の4つの個別ページ(gpts-creation-basics.md/gemini-gem-feature.md/copilot-agent-builder-basics.md/claude-projects-basics.md、いずれも2026年8月19日〜9月13日更新)で裏取り済みの内容を横断編集

### 2026-07-30: 初版執筆
- **内容**: GPTs・Gem・エージェントビルダー/Copilot Studio・Claude Projectsの4ツールを横断比較。作成に必要なプラン・ナレッジ上限・外部API/業務システム連携の可否・公開範囲・料金体系の比較表、使い分けの判断表、4ツール共通で使い回せる指示文テンプレート、作成画面への入り口一覧を整理。各項目は同ディレクトリ内の4つの個別ページ(2026年7月19日〜28日更新)で裏取り済みの内容をもとに横断編集し、ChatGPT Goプランでのカスタム作成可否についてはOpenAI公式ヘルプセンターを根拠とする既存ページの記載(Plus以上が必要)を優先した(一部SEO記事はGoでも作成可能と記載しているが、一次情報での確認が取れないため採用しなかった)
- **出典**: [OpenAI Help Center: Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts)、[Google公式ヘルプ: Tips for creating custom Gems](https://support.google.com/gemini/answer/15235603?hl=en)、[Microsoft Learn: Choose between Agent Builder in Microsoft 365 Copilot and Copilot Studio](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/copilot-studio-experience)、[Microsoft Tech Community: Meet the new Copilot Studio, rebuilt for more complex multi-step work](https://techcommunity.microsoft.com/blog/copilot-studio-blog/meet-the-new-copilot-studio-rebuilt-for-more-complex-multi-step-work/4526488)、[Claude Help Center: What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)、[Claude Help Center: Retrieval augmented generation (RAG) for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)、[LumiChats: Claude Projects vs ChatGPT Projects vs Gemini Gems (2026)](https://lumichats.com/blog/claude-projects-vs-chatgpt-projects-vs-gemini-gems-2026)
