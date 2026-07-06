---
title: "Claude(Anthropic)の「プロジェクト」機能の基本"
part: 6
chapter: 第2章 主要ツールでの作り方
tags: [Claude, Projects, カスタムAI, Anthropic]
created: 2026-07-06
updated: 2026-07-06
---

# Claude(Anthropic)の「プロジェクト」機能の基本

## これは何か

Claude.aiで毎回「うちの会社は◯◯業で、こういう規程があって……」と前提を説明し直してから質問している人は多い。**Projects(プロジェクト)**は、この前提説明(カスタム指示)と参照資料(ナレッジ)、会話履歴を1つの箱にまとめて、以降はその箱の中で始めた会話すべてに自動で適用できるようにする機能である。ChatGPTのGPTs・GeminiのGemと同じ「自分専用AIを作る」機能群の1つで、プログラミング不要という点も共通している。

## 仕組み・背景

Projectsは「カスタム指示(project instructions)」「ナレッジ(参照ファイル)」「会話履歴」の3点を1つのワークスペースにまとめる仕組みで、プロジェクト内で新しい会話を始めるたびに、指示とナレッジが自動的に読み込まれる。

- **カスタム指示**: そのプロジェクト内のすべての会話に適用される、役割・トーン・回答ルールなどの指示文。GPTsの「Instructions」、Gemの「カスタム指示」に相当する
- **プロジェクトナレッジ**: PDF・Word・スプレッドシート・コードなどをアップロードしておくと、会話の中でClaudeが参照する。1ファイルあたり30MBが上限
- **コンテキストウィンドウとRAGモードへの自動切り替え**: プロジェクトが一度に読み込める分量は200,000トークン(日本語で数百ページ相当)が基本上限だが、有料プラン(Pro/Max/Team/Enterprise)では、アップロードしたナレッジがこの上限に近づくと、Claudeが自動的に**RAG(検索拡張生成、必要な部分だけを都度検索して参照する仕組み)モード**に切り替わり、実質的な容量を最大10倍程度まで拡張できる。この際、画面に「必要な情報を都度検索します」といった案内が表示されることがある。ただし、RAGモードに入ると「アップロードした全文を毎回読んでいる」わけではなくなる点は、後述の注意点で扱う

なお、プロジェクト名・説明欄はあくまで自分たちの整理用のラベルであり、Claude自身がそれを読んで挙動を変えるわけではない(実際の振る舞いを決めるのはカスタム指示とナレッジ)。

## 使いどころ・使い分け

| 目的 | 使う機能 |
|---|---|
| 特定の業務・クライアント案件専用の相談相手を作りたい | Projectsでカスタム指示+ナレッジを設定 |
| 過去の会話を積み重ねながら1つのテーマを深掘りしたい | Projects内で会話を継続(会話履歴が同じ文脈で参照される) |
| コードを書きながら生成物(文章・表・簡易アプリ等)をその場で確認・編集したい | Projects内でArtifacts(生成物を専用パネルに表示する機能)を併用 |
| 社内の複数人に同じ設定のAIを使わせたい | Team/Enterpriseプランでプロジェクトを「Public」共有 |
| 外部に一般公開してストアに掲載したい | 非対応(ChatGPTのGPTストアのような公開マーケットプレイスはなく、共有範囲は自組織内に限られる) |

ChatGPTのGPTs・GeminiのGemとの主な違いは次の通り。

| 観点 | Claude Projects | ChatGPTのGPTs | GeminiのGem |
|---|---|---|---|
| 外部API連携(Actions) | 非対応(Claude API側でTool Useを組む必要がある) | 対応(Actions) | 非対応 |
| 一般公開・マーケットプレイス | なし(組織内共有のみ) | あり(GPTストア) | なし |
| 無料プランでの利用 | 2026年に無料化(上限5個までが目安) | 作成不可(利用のみ) | 一部機能に制限あり |
| ナレッジの参照方式 | 容量超過時に自動でRAGモードへ切り替え | ファイル検索(内部的に同様の仕組み) | Saved infoやドライブ連携 |
| 生成物の編集体験 | Artifacts(コード・文書をその場で編集) | Canvas | Canvas |

「外部システムと連携させたい・不特定多数に公開したい」ならGPTs、「Google系サービス(スプレッドシート等)との連携を重視したい」ならGem、「長文の資料を読み込ませて深く対話し、生成物をその場で編集したい」ならClaude Projects、という住み分けで検討するとよい。

## 実務での使い方

### 作成手順(2026年7月時点の目安)

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
| Public(組織内) | 同じTeam/Enterpriseワークスペースの全メンバー | 「Can use」(閲覧・利用のみ)または「Can edit」(指示・ナレッジの編集も可)を招待時に選択 |

共有プロジェクトであっても、メンバー各自が行った個々の会話の中身自体は既定で他メンバーに見えない(共有されるのはカスタム指示とナレッジ、明示的に共有した会話のみ)。

### Google Drive・GitHubとの連携

プロジェクトの「Add content」からGoogle Drive連携(読み取り専用。ファイルの検索・要約・横断分析はできるが、編集・作成・移動はできない)やGitHubリポジトリの参照を追加できる。ただしGoogle Drive連携は、2026年7月時点では**Privateなプロジェクトでのみ利用可能で、共有(Public)プロジェクトでは無効**になる点に注意する。

## 注意点・よくある誤解

- **「アップロードした資料は毎回全文読まれる」とは限らない**: プロジェクトナレッジが容量上限に近づくとRAGモードに自動移行し、質問に関連しそうな部分だけを検索して参照する挙動に変わる。全文を毎回精読しているわけではないため、「資料に書いてあるのに答えに反映されない」場合は、この切り替えが起きていないか疑う
- **無料プラン(Free)でもProjectsが使えるようになったが上限がある**: 2026年にFreeプランでも解放されたが、作成できるプロジェクト数には上限(目安5個)がある。頻繁に新しいプロジェクトを作る運用には向かないため、業務単位・案件単位でプロジェクトを使い回す設計にする
- **GPTsのような外部一般公開・マーケットプレイスはない**: 社外の不特定多数に使わせたい場合はProjectsでは実現できない。その用途はChatGPTのGPTsを検討する
- **Google Drive連携は共有プロジェクトでは使えない**: チームで使うプロジェクトにドライブ連携をそのまま持ち込もうとすると設定できず戸惑うことがある。共有プロジェクトではファイルを都度アップロードする運用に切り替える
- **機密情報の取り扱いはプランで扱いが異なる**: Free/Pro/Max(個人向けプラン)は既定でモデルの学習に利用され得る設定になっており、学習に使われたくない場合は「設定→プライバシー→Help improve Claude」をオフにする必要がある。Team/Enterprise(商用契約)は契約上、顧客のコンテンツをモデルの学習に使わないことが原則になっている。機密性の高い資料を扱うプロジェクトは、契約形態を確認してから作る

## 最初の一歩

自分が繰り返し同じ前提を説明してからClaudeに相談している業務を1つ選び、その前提をカスタム指示に、関連資料をナレッジに登録したプロジェクトを1つ(Privateで)作ってみる。

## 関連トピック

- [GPTsの作り方と公開設定](gpts-creation-basics.md)
- [Gem(Geminiのカスタムボット機能)の基本](gemini-gem-feature.md)
- [Claude(Anthropic)の基本](../part03-ai-chat-tools/claude-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: Claude Projectsの仕組み(カスタム指示・ナレッジ・会話履歴の統合、容量上限とRAGモードへの自動切り替え)、GPTs・Gemとの比較表、作成手順、カスタム指示の記入例、Team/Enterpriseでの共有設定、Google Drive/GitHub連携の制約、データ学習ポリシーの違いを整理
- **出典**: [Claude Help Center: What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects)、[Claude Help Center: How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)、[Claude Help Center: Manage project visibility and sharing](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing)、[Anthropic: Collaborate with Claude on Projects](https://www.anthropic.com/news/projects)、[Claude Help Center: Use Google Workspace connectors](https://support.claude.com/en/articles/10166901-use-google-workspace-connectors)、[Tom's Guide: Claude just made two of its best features free](https://www.tomsguide.com/ai/claude-just-made-two-of-its-best-features-free-heres-how-to-use-projects-and-artifacts)
