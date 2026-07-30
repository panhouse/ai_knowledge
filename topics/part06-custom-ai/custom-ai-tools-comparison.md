---
title: GPTs・Gem・Copilot Agent・Claude Projectsの比較と使い分け
part: 6
chapter: 第2章 主要ツールでの作り方
tags: [GPTs, Gem, Copilot Studio, エージェントビルダー, Claude Projects, カスタムAI, ツール比較]
created: 2026-07-30
updated: 2026-07-30
---

# GPTs・Gem・Copilot Agent・Claude Projectsの比較と使い分け

## これは何か

「自分専用のAIを作りたいが、会社にはChatGPTもGeminiもCopilotもClaudeも入っている。どれで作ればいいのか」——これは、カスタムAI機能に手を付けようとした人が最初にぶつかる疑問である。ChatGPTの**GPTs**、Geminiの**Gem**、Microsoft 365 Copilotの**エージェントビルダー/Copilot Studio**、Claudeの**Projects**は、いずれも「指示+参照資料を1つのボットとして保存し、以降ワンクリックで呼び出す」という同じ発想の機能だが、外部システム連携・公開範囲・必要プランには無視できない差がある。本ページは4ツールを横並びで比較し、「自分の状況ならどれを選ぶべきか」の判断材料を1ページにまとめる。各ツール個別の詳しい作成手順・料金は、末尾の「関連トピック」にある各ツールの専用ページを参照してほしい。

## 仕組み・背景

4ツールはいずれも、次の3要素の組み合わせでできている。

1. **指示(システムプロンプト相当)**: 役割・トーン・回答ルールを固定で覚えさせる文章
2. **ナレッジ(参照ファイル)**: PDF・Excel等をアップロードし、会話の中でAIに参照させる
3. **公開範囲の設定**: 自分だけで使うか、チームに配るか、外部に公開するか

違いが出るのはここから先で、GPTsとCopilot Studioは「外部システムに接続して処理を実行する」機能(Actions/コネクタ)まで踏み込んでいるのに対し、GemとClaude Projectsは「指示+ナレッジで賢く答える」範囲にとどまる。この違いが、後述する使い分けの一番の分かれ目になる。

| 概念 | ChatGPT | Gemini | Microsoft 365 Copilot | Claude |
|---|---|---|---|---|
| 呼び方 | GPTs(カスタムGPT) | Gem | エージェントビルダー(簡易版)/Copilot Studio(本格版) | Projects(プロジェクト) |
| 作成画面 | ChatGPT左サイドバー「GPTを探す」→GPT Builder | gemini.google.com左メニュー「Gemを表示」→Gemマネージャー | Copilotアプリ左ペイン「エージェント」、またはcopilotstudio.microsoft.com | claude.ai左サイドバー「Projects」 |
| 指示欄の呼称 | Instructions(指示) | カスタム指示 | 指示(自然言語で自動生成→手動調整) | Project instructions(カスタム指示) |

## 使いどころ・使い分け

判断の起点は「何を外に繋ぎたいか」「誰に公開したいか」の2つである。

| こういう場合は… | 向いているツール | 理由 |
|---|---|---|
| 不特定多数にストア形式で一般公開したい | **GPTs** | 4ツールの中でGPTストアを持つのはChatGPTだけ |
| CRM・ERP・チケット管理などの業務システムと繋いで、承認フローや自動処理までさせたい | **Copilot Studio** | Power Platformの1,400以上のコネクタとマルチステップワークフローに対応するのはCopilot Studioのみ |
| SharePoint・OneDriveの社内文書だけを検索・要約するボットを最短で作りたい | **エージェントビルダー** | M365 Copilotライセンスに含まれ追加費用なし。知識源を指定するだけで完結する軽量版 |
| Google Drive・スプレッドシートなどGoogle系ファイルと連携させたい | **Gem** | Google Driveのファイルを常に最新版で参照でき、無料プランでも作成できる |
| 長文資料を読み込ませて深く対話し、生成した文書やコードをその場で編集したい | **Claude Projects** | Artifacts(生成物の専用編集パネル)と大容量ナレッジ(自動RAG化で実質約200万トークン相当)が強み |
| 予算をかけず今日から無料で試したい | **Gem** または **Claude Projects** | いずれも無料プランで作成可(GPTsはPlus以上、Copilot系はM365 Copilotライセンスが前提) |
| 外部APIを自作して呼び出させたい(自社サービス連携など) | **GPTs**(Actions) | OpenAPIスキーマを登録するだけで外部API連携ができる、個人でも手が届く仕組み |

### 機能・条件の比較表(2026年7月時点)

| 観点 | GPTs(ChatGPT) | Gem(Gemini) | エージェントビルダー/Copilot Studio(Microsoft) | Projects(Claude) |
|---|---|---|---|---|
| 作成に必要なプラン | Plus/Pro/Business/Enterprise。**Free・Goは利用のみで作成不可** | 無料プランでも作成可(動作モデルの性能・利用枠は有料プランほど高い) | M365 Copilot(Copilot Chat含む)ライセンスがあれば追加費用なしで作成可。社外公開のみCopilot Studioのスタンドアロンライセンスが必要 | Freeでも作成可(上限5プロジェクト)。Pro以上は実質無制限 |
| ナレッジファイルの上限 | 最大20ファイル・1ファイル512MBまで(文書は概ね200万トークンまで) | 最大10ファイル・1ファイル100MBまで | エージェントビルダー: OneDrive約50件・アップロード約20件が目安/Copilot Studio: サイト・フォルダ単位でほぼ無制限 | 1ファイル30MBまで、ファイル数に上限なし(合計200,000トークンを超えると自動でRAGモードに切替、実質約200万トークン相当) |
| 外部API・業務システム連携 | Actions(OpenAPIスキーマで外部API呼び出し) | 非対応 | Power Platformコネクタ(1,400以上)、Dataverse、マルチステップワークフロー(Copilot Studio) | 非対応(Claude API側でTool Useを別途実装する必要あり) |
| 主な知識源 | アップロードファイル | アップロードファイル/Google Drive(常に最新版を参照) | SharePoint/OneDrive/Dataverse/公開Webサイト/Microsoft Graph横断検索 | アップロードファイル/Google Drive(読み取り専用、Privateプロジェクト限定)/GitHub |
| 公開・共有範囲 | 自分のみ/リンク共有/GPTストアで一般公開 | 非公開/リンク共有/組織内共有(管理者が可否を制御) | Teams/SharePoint/Webサイト/Slack等マルチチャネルで社内〜社外顧客まで、社内エージェントストアへの公開も可 | Private、Team/Enterpriseなら組織内共有(メンバーごとに「Can use」「Can edit」を設定) |
| 外部の一般公開マーケットプレイス | あり(GPTストア) | なし | なし(自組織のエージェントストアが基本) | なし |
| 生成物のその場編集機能 | Canvas | Canvas | なし | Artifacts |
| 料金の考え方 | プラン料金に含まれる(追加課金なし) | プラン料金に含まれる(追加課金なし) | 社内利用は追加費用なし。社外公開・大量のアクション実行時のみCopilotクレジットを従量課金 | プラン料金に含まれる(上位モデルの多用時のみ利用上限に注意) |

## 実務での使い方

### 4ツールで使い回せる指示文の型

指示欄(システムプロンプト相当)の書き方は、実はどのツールでもほぼ同じ型が通用する。以下のテンプレートをベースに、末尾だけツールの呼称に置き換えれば使い回せる。

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
| ナレッジ添付欄 | ナレッジ | ナレッジ(端末アップロード/Google Drive) | 知識を追加(SharePoint/OneDrive/アップロード/公開Webサイト等) | Add content(+ボタン) |

### 作成画面への入り口(一覧)

| ツール | 入り口 |
|---|---|
| GPTs | ChatGPT(Web版)にログイン→左サイドバー「GPTを探す」→右上「＋作成する」 |
| Gem | gemini.google.com→左メニュー「Gemを表示」→「Gemマネージャー」→「+新しいGem」 |
| エージェントビルダー | Microsoft 365 Copilotアプリ(copilot.cloud.microsoft)左ペイン「エージェント」→「+新しいエージェント」 |
| Copilot Studio | copilotstudio.microsoft.com にサインイン→左メニュー「エージェント」→「+作成」 |
| Claude Projects | claude.ai→左サイドバー「Projects」→「+ New project」 |

具体的な入力項目・設定手順(ナレッジの上限値、公開範囲の切り替え方、Actionsやコネクタの設定など)は、各ツールの専用ページに画面遷移込みで記載している。まずどのツールを使うか本ページで決め、詳細は該当ページを見る、という使い方を想定している。

### コスト面の意思決定材料

- **追加費用ゼロで始めたいなら**: Gem(無料プラン)またはClaude Projects(Freeプラン、上限5個)。GPTsはPlus以上($20/月相当)、Copilot系はM365 Copilotライセンス(組織契約)が前提になる
- **すでに契約しているプラン起点で選ぶ**: 会社がM365 Copilotを導入済みならエージェントビルダーが最も追加コストが低い。Google Workspaceが主戦場ならGemが自然な選択
- **外部公開・大量自動化まで見据えるなら**: GPTsのGPTストア掲載は追加費用なしだが不特定多数への一般公開が前提になる。Copilot Studioの社外公開・大量アクション実行はCopilotクレジットの従量課金が発生するため、事前の試算が必須

## 注意点・よくある誤解

- **「指示+ナレッジ」の機能だけを見て選ぶと、後で外部連携で詰まる**: GemとClaude Projectsは外部API・業務システム連携に対応しないため、「将来的にCRMや基幹システムと繋ぎたい」という要件があるなら、最初からGPTs(Actions)かCopilot Studio(コネクタ)を選んでおいた方が作り直しの手間がない
- **無料で使えるからといって、無料プランに機能差がないわけではない**: GemもClaude Projectsも無料プランで作成自体はできるが、動作するモデルの性能・利用回数枠・(Claudeの場合は)作成できるプロジェクト数(上限5個)には有料プランとの差がある
- **「公開」の意味がツールごとに違う**: GPTsの「誰でも(GPTストアに公開)」は文字通り世界中の誰でも使える状態を指すが、Gem・Claude Projects・Copilot系の「共有」「公開」はいずれも自組織内(または招待した相手)止まりで、外部一般公開の機能自体を持たない。「社内で共有したいだけなのに、誤って世界に公開してしまう/その逆」を避けるため、公開範囲の選択肢は毎回確認する
- **ナレッジファイルは「完全に機密」ではない**: どのツールでも、アップロードした資料の内容は共有範囲を広げるほど閲覧可能になる。機密情報を含む資料は、共有範囲を最も狭い設定(自分のみ/Private)にするか、組織の権限管理(SharePoint権限、Workspace管理者設定など)と連動させて運用する
- **ツール名・機能は変化が速い分野**: Copilot Studioは2026年7月に大幅なリビルドを経ており、GPTsもチーム向け機能がWorkspace Agentsへ拡張されるなど、各ツールの機能範囲は数か月単位で更新される。本ページの比較表は執筆時点のスナップショットであり、実際に導入する際は各ツールの専用ページ(下記「関連トピック」)の更新履歴で最新状態を確認する

## 最初の一歩

自分が「毎回同じ前提を説明してから使っている」業務を1つ選び、上記の使い分け表で自分の状況(無料で試したいか、外部連携が要るか、社内システムと繋ぎたいか)に合うツールを1つ選んで、まずは公開範囲「自分のみ」でカスタムAIを1つ作ってみる。

## 関連トピック

- [カスタムAIの基礎(共通設計原則)](custom-ai-design-principles.md)
- [GPTsの作り方と公開設定](gpts-creation-basics.md)
- [Gem(Geminiのカスタムボット機能)の基本](gemini-gem-feature.md)
- [Microsoft Copilot Studioによるカスタムエージェント作成の基本](copilot-agent-builder-basics.md)
- [Claude(Anthropic)の「プロジェクト」機能の基本](claude-projects-basics.md)
- [GPTsのナレッジファイルとアクション連携](gpts-knowledge-and-actions.md)

## 更新履歴

### 2026-07-30: 初版執筆
- **内容**: GPTs・Gem・エージェントビルダー/Copilot Studio・Claude Projectsの4ツールを横断比較。作成に必要なプラン・ナレッジ上限・外部API/業務システム連携の可否・公開範囲・料金体系の比較表、使い分けの判断表、4ツール共通で使い回せる指示文テンプレート、作成画面への入り口一覧を整理。各項目は同ディレクトリ内の4つの個別ページ(2026年7月19日〜28日更新)で裏取り済みの内容をもとに横断編集し、ChatGPT Goプランでのカスタム作成可否についてはOpenAI公式ヘルプセンターを根拠とする既存ページの記載(Plus以上が必要)を優先した(一部SEO記事はGoでも作成可能と記載しているが、一次情報での確認が取れないため採用しなかった)
- **出典**: [OpenAI Help Center: Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts)、[Google公式ヘルプ: Tips for creating custom Gems](https://support.google.com/gemini/answer/15235603?hl=en)、[Microsoft Learn: Choose between Agent Builder in Microsoft 365 Copilot and Copilot Studio](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/copilot-studio-experience)、[Microsoft Tech Community: Meet the new Copilot Studio, rebuilt for more complex multi-step work](https://techcommunity.microsoft.com/blog/copilot-studio-blog/meet-the-new-copilot-studio-rebuilt-for-more-complex-multi-step-work/4526488)、[Claude Help Center: What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)、[Claude Help Center: Retrieval augmented generation (RAG) for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects)、[LumiChats: Claude Projects vs ChatGPT Projects vs Gemini Gems (2026)](https://lumichats.com/blog/claude-projects-vs-chatgpt-projects-vs-gemini-gems-2026)
