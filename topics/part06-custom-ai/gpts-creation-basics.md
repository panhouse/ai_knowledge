---
title: GPTsの作り方と公開設定
part: 6
chapter: 第2章 主要ツールでの作り方
tags: [GPTs, ChatGPT, カスタムGPT, GPT Builder]
created: 2026-07-04
updated: 2026-09-18
---

# GPTsの作り方と公開設定

## これは何か

GPTs(カスタムGPT)は、特定の業務や役割に特化させたChatGPTを、プログラミングなしで作れる機能である。毎回同じ前提説明や参照資料をコピペしてから質問している人は、その手間をGPTsに1度設定してしまえば、以降はワンクリックで使い回せるようになる。

**2026年9月11日、OpenAIは全プランでGPTsを段階的に廃止し、後継の「Plugins(プラグイン)」へ移行すると発表した。**
個人プラン(Free/Go/Plus/Pro)では**すでに新規GPTの作成・公開ができなくなっており**、
既存のGPTは引き続き利用・編集できるものの、新しくGPTsを作りたい場合は本ページの手順ではなく
後述の「GPTs廃止とPluginsへの移行」を先に読むこと。既存のGPTを使い続けている、
または過去に作ったGPTを理解したい読者のために、以下では作成当時の仕組み・手順を維持しつつ、
廃止スケジュールと移行先を明記する。

## 仕組み・背景

GPTsの作成・編集には有料プラン(Plus/Pro/Business/Enterprise)が必要で、**FreeプランとGoプランでは作成できない**(他ユーザーが公開したGPTsの利用のみ可能)。「Go」はFreeより利用上限を引き上げた個人向けの安価プラン(2026年1月に日本を含む170カ国以上に展開)だが、GPTs作成のような高度機能はPlus以上でのみ解放される点に注意する。なお法人向けの「Team」プランは2025年8月に「Business」へ名称統合されており、現在は別プランとして存在しない。作成・編集はWebブラウザ版(chatgpt.com)限定で、モバイルアプリでは利用のみできる。

GPTを作る画面(GPT Builder)には2つのモードがある。

- **作成(Create)モード**: GPT Builderとの対話形式で目的やキャラクターを伝えると、Builderが自動でInstructions(指示文)や名前を組み立ててくれる。ただしこれはあくまで叩き台で、業務で使えるレベルにするにはConfigureモードでの手動調整がほぼ必須
- **構成(Configure)モード**: 名前・指示・ナレッジファイルなどの各項目を直接フォーム入力する詳細設定モード

## 使いどころ・使い分け

| 目的 | 使う機能 |
|---|---|
| 手早く試作したい | Createモードで対話しながら作成 |
| 社内資料を読ませて細かく調整したい | Configureモードで直接設定 |
| 社内限定で複数人に使わせたい | Business/Enterpriseワークスペースの共有機能 |
| 一般公開してGPTストアに掲載したい | 公開範囲を「誰でも」に設定し、ビルダープロフィールを公開設定にする |
| ひとりで長時間かかる作業(資料作成・調査など)をAIに丸ごと任せて完成品を受け取りたい | GPTsではなく「ChatGPT Work」(旧エージェントモードの後継、後述)を使う |
| 組織全体でSlack・Salesforce等の外部ツールと連携し、スケジュール実行や常時稼働のエージェントを組みたい | GPTsではなく「Workspace Agents」(Business/Enterprise/Edu/Teachers向け、後述)を検討する |

## 実務での使い方

### 作成手順(廃止前の仕様。既存GPTの理解・編集の参考として掲載)

**個人プラン(Free/Go/Plus/Pro)はすでに新規作成ができない。** 以下は廃止前の手順であり、
既に作成済みのGPTを編集する際の画面構成の参考として残している。新しく作りたい場合は
「GPTs廃止とPluginsへの移行」を参照する。

1. ChatGPT(Web版)にログインし、左サイドバーの「GPTを探す」をクリック
2. GPTストア画面右上の「＋作成する」をクリックするとGPT Builderが開く
3. Configureタブで以下の項目を設定する

| 項目 | 内容 |
|---|---|
| アイコン | 画像アップロードまたは画像生成AIで生成 |
| 名前 | 用途が一目で分かる短い名称(20文字以内が目安) |
| 説明 | GPTストア等の一覧に表示される概要文 |
| 指示(Instructions) | 振る舞い・応答スタイル・避けるべきことを定義するシステムプロンプト相当。全会話に適用される |
| 会話のきっかけ | ユーザーが最初に送る質問例(最大4つ) |
| ナレッジ | PDF・Excel等の参照ファイルをアップロード。**上限は最大20ファイル、1ファイルあたり512MBまで**(テキスト・文書系ファイルは1ファイルあたり約200万トークンが上限) |
| Capabilities | Web検索、画像生成、コードインタープリター&データ分析、**Canvas**(下書き・構造化された長文コンテンツをGPT利用者が編集できる機能)、**Apps**(旧称Connectors。Google Drive・Gmail・SharePointなどOpenAIが承認した外部サービスとの連携)のオン/オフ。Canvasは新規作成GPTではデフォルトON、既存GPTはOFFなので必要なら手動で有効化する |
| Actions | OpenAPIスキーマを使って独自の外部APIを呼び出させる機能。認証設定も含む。**AppsとActionsは同時には有効化できず、どちらか一方を選ぶ仕様**になっている(定型的な社外SaaS連携ならApps、自社独自APIを叩かせたいならActions、という使い分けが目安) |

2026年7月にGPT-5.6ファミリー(Sol/Terra/Luna)が投入されて以降、GPT Builderでもこの基盤モデルを選べる設定項目のロールアウトが進んでいる(Capabilitiesの組み合わせによって選べるモデルが変わり、表示されない場合は未展開のアカウント)。なお、Pro相当の深い推論(GPT-5.6 Sol等をPro modeで動かす場合)ではCanvas・Apps・画像生成が無効になる制約があるため、**Canvasを使わせたいGPTでは通常モードの実行モデルを選ぶ**。

### コピペで使える指示欄のテンプレート例

```
## 私について
[このGPTを使う想定ユーザー像。例: "中小企業の経理担当者"]

## 会社について
[前提となる会社・業務の背景。例: "従業員50名の製造業。経費精算は月末締め"]

## このGPTの役割
[何をしてほしいか。例: "経費精算ルールに関する質問に、添付の社内規程を根拠に答える"]

## 回答のルール
- 添付のナレッジファイルに書かれていないことは、推測せず「規程に記載がありません」と答える
- 回答の最後に、根拠にした規程の項番を示す
```

### 公開範囲の設定

編集画面右上の「保存」を押すと公開範囲を選べる。

| 選択肢 | 対象 |
|---|---|
| 自分のみ | 個人利用限定 |
| リンクを知っている人のみ | 特定のチーム・クライアントへの限定共有 |
| 誰でも(GPTストアに公開) | 一般公開。GPTストアに掲載できるのはこの設定のみ |

Business/Enterpriseのワークスペースでは、上記に加えて「共有」ボタンからワークスペース内のユーザー・グループを検索して個別共有したり、「リンクを持っているワークスペース全員」に社内限定公開したりできる。

GPTストアに一般公開する場合は、事前に設定の「ビルダープロフィール」で本名または独自ドメインのどちらかを公開設定にする必要がある(「自分のみ」「リンクを知っている人のみ」の場合は不要)。

なお、GPTストアの収益分配プログラム(利用状況に応じてビルダーに支払いが発生する仕組み)は、2026年8月時点でも米国拠点のビルダーを中心とした招待制の限定パイロットにとどまり、新規募集は行われていない。「公開すれば誰でも収益化できる」わけではない点に注意する。

### 他ツールでの類似機能

| 概念 | ChatGPT | Gemini | Microsoft 365 Copilot |
|---|---|---|---|
| カスタムAI作成機能 | GPTs(GPT Builder) | Gem | エージェントビルダー(より高度な構築はCopilot Studio) |

### GPTs廃止とPluginsへの移行(2026年9月時点)

**2026年9月11日、OpenAIはGPTsを全プランで段階的に廃止し、後継の「Plugins」へ移行すると正式発表した。**
以前は法人ワークスペース向けの終了時期が「報道ベース」の未確定情報だったが、現在は公式に確定日程が示されている。

| 項目 | 内容 |
|---|---|
| 新規GPTの作成・公開 | **個人プラン(Free/Go/Plus/Pro)はすでに不可**。Enterpriseワークスペースは2026年9月25日で終了予定 |
| 既存GPTの利用・編集 | 廃止日まで引き続き可能(プラン・権限による) |
| Enterpriseワークスペースの完全廃止 | 2026年12月11日に予定。以降GPTsは動作を停止しGPTストアからも削除される |
| 移行体験の提供開始目標 | 2026年9月17日(他プランも同じ日程を追う見込み) |
| 移行先 | **Plugins**(後述) |

移行先の**Plugins(プラグイン)**は、「Skills(再利用可能な指示・作業手順のセット。GPTsのInstructionsに相当)」と
「Apps(MCP=Model Context Protocol経由で外部サービスに接続する仕組み)」を組み合わせた、
ChatGPT・Codex共通の新しい機能パッケージの単位である。2026年7月9日に旧来の「アプリディレクトリ」が
「プラグインディレクトリ」に統合され、Pluginsが機能を探す際の中心的な入口になっている。
既存のGPTのInstructions・ナレッジ・Actionsは、移行フローを通じてPluginsのSkills・Appsに
置き換えていく想定だが、本稿執筆時点で自動変換ツールの詳細な移行手順は順次公開中である。

**GPTsの周辺には、性質の異なる2つの自動化・エージェント機能も2026年に追加されている**(混同しやすいので整理する)。

- **ChatGPT Work(2026年7月9日〜)**: 個人・チーム問わず使える新しい実行モード。旧来の「エージェントモード」の後継で、GPT-5.6/GPT-6 Astraを基盤に、依頼した作業をバックグラウンドで数分〜数時間かけて自律的に進め、スプレッドシートやスライド、レポート、簡易アプリといった「完成品」を返す。GPTsのような「固定の指示+ナレッジを毎回呼び出す軽量アシスタント」ではなく、都度のタスクをその場で自律的にこなす実行モードである点が異なる
- **Workspace Agents(2026年4月22日〜)**: Business/Enterprise/Edu/Teachers向けに発表された、Codexを基盤とするチーム向けエージェント機能。Slack・Salesforce・Google Drive・Microsoft製品などの外部ツールに接続し、スケジュール実行や複数ステップの業務を継続的にこなせる

「1つの決まった指示+ナレッジで動く軽量なアシスタント」を作りたい場合は、新規作成が止まっている今はPluginsのSkillsを確認するのが実務的な選択肢になる。ひとりで完結する重めの作業を丸ごと任せたいならChatGPT Work、組織全体で外部システム連携や常時稼働の自動化まで踏み込みたい場合はWorkspace Agentsの対象プランかどうかを確認する。

## 注意点・よくある誤解

- **GPTsは全プランで廃止に向かっている**: 2026年9月11日の公式発表により、個人プラン(Free/Go/Plus/Pro)は新規作成・公開がすでに不可、Enterpriseワークスペースも2026年9月25日で新規作成終了、2026年12月11日に完全廃止(動作停止・ストアから削除)予定。「作成ボタンが見当たらない」場合、プランの問題ではなく廃止によるものである可能性が高い。移行先はPlugins
- **既存GPTはすぐには消えない**: 廃止日(Enterpriseは2026年12月11日)までは利用・編集ができる。慌てて別ツールに移す前に、自組織・自分のワークスペースの管理画面のお知らせと移行フローの提供状況を確認する
- **「Team」プランはもう存在しない**: 2025年8月に「Business」へ名称統合されているため、古い記事や社内資料の「Teamプラン」表記は現在のBusinessを指す。
- **ナレッジファイルは完全な機密性を保証しない**: アップロードしたファイルの内容が、Actionsの設定次第で意図せず引用・開示される可能性があるため、機密情報を含むファイルの扱いは慎重に。
- **GPTストア公開にはビルダープロフィールの公開設定が必須**: これを忘れると「誰でも」を選んでも公開に進めないことがある。
- **GPTストアで公開しても自動的に稼げるわけではない**: 収益分配プログラムは招待制の限定パイロットにとどまり、一般公開はされていない。
- **AppsとActionsは併用できない**: 外部連携をどちらで実装するか、GPTを作る前に決めておく。
- **Pro相当の深い推論モデルを選ぶとCanvas・Apps・画像生成が無効になる**: Canvasを使わせたいGPTでは、実行モデルが通常モード(非Pro)になっているか確認する。
- **Pluginsへの移行は「まだ発表されたばかり」**: 移行体験の提供開始目標は2026年9月17日で、自動変換ツールの詳細手順は順次公開されている段階。個人・組織とも、実際に移行を進める前に自分のワークスペース(またはアカウント)に移行フローが届いているかを確認する。
- **チーム全体の自動化を考えているなら、GPTsだけで完結させようとしない**: 外部ツール連携やスケジュール実行が必要な用途は、Workspace Agents(対象プランの場合)の方が向いていることがある。個人で完結する重い作業の丸投げにはChatGPT Workが向いていることもある。

## 最初の一歩

すでにGPTsを作っているなら、まず自分(または自組織)のワークスペースに廃止・移行の案内が届いているかを確認する。まだ作っていないなら、新規にGPTsを作ろうとするのではなく、ChatGPTの「プラグイン」ディレクトリでPluginsの現状を一度眺めてみる。

## 関連トピック

- [GPTsのナレッジファイルとアクション連携](./gpts-knowledge-and-actions.md)
- [GPTs・Gem・Copilot Agent・Claude Projectsの比較と使い分け](./custom-ai-tools-comparison.md)
- [ChatGPTのプラン比較](../part03-ai-chat-tools/chatgpt-plan-comparison.md)

## 更新履歴

### 2026-09-18: GPTs廃止(Pluginsへの移行)の公式発表を反映
- **内容**: 2026年9月11日にOpenAIが公式発表した「GPTsを全プランで段階的に廃止しPluginsへ移行する」方針を反映。個人プラン(Free/Go/Plus/Pro)はすでに新規作成・公開が不可であること、Enterpriseワークスペースは2026年9月25日で新規作成終了・2026年12月11日に完全廃止予定であることを表にまとめて明記(以前の「報道ベースで未確認」という記述を、公式確定日程に更新)。移行先「Plugins」(Skills+Appsの組み合わせ、2026年7月9日にアプリディレクトリから統合)の概要を新設。作成手順・最初の一歩を、既存GPTの参考情報および新規作成不可を前提にした内容に更新
- **出典**: [OpenAI Help Center: Custom GPT retirement and migration FAQ](https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq)、[OpenAI Help Center: Plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex)

### 2026-08-05: ChatGPT Work・Apps/Actionsの仕様変更・GPTストア収益化の実態を反映して最新化
- **内容**: 2026年7月9日にローンチした新しい実行モード「ChatGPT Work」(旧エージェントモードの後継、GPT-5.6基盤)を追記し、GPTs・ChatGPT Work・Workspace Agentsの関係を整理し直した。GPT Builderの新設「Apps」(旧Connectors)とActionsが同時併用できない仕様、Pro相当の推論モデルではCanvas・Apps・画像生成が無効になる制約を追記。GPTストアの収益分配プログラムが招待制の限定パイロットにとどまる実態を明記。海外メディアが報じるBusiness/Enterprise/Edu/Teachers向けGPTsの提供終了時期(2026年8月26日ごろ)を、OpenAI公式ヘルプセンターでは終了日が未確認である旨を明記した上で注意喚起として追加
- **出典**: [OpenAI Help Center: Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts)、[OpenAI: Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)、[OpenAI Help Center: Apps in ChatGPT](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)、[VentureBeat: OpenAI unveils Workspace Agents, a successor to custom GPTs for enterprises](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more)、[FormWise: OpenAI Is Deprecating Custom GPTs. Here's the Migration Path.](https://formwise.ai/blog/openai-deprecating-custom-gpts-migration-path)、[digitalapplied.com: ChatGPT Work: OpenAI's Agent That Ships Finished Work](https://www.digitalapplied.com/blog/chatgpt-work-openai-agent-launch-2026)

### 2026-07-19: プラン要件を訂正し、Canvas・ナレッジ上限・Workspace Agentsの動きを追記
- **内容**: GPTs作成に必要なプランを「Plus/Pro/Business/Enterprise」に訂正(Goは利用のみ可・作成不可、Teamは2025年8月にBusinessへ名称統合済み)。GPT BuilderのCapabilitiesに新設された「Canvas」トグルとモデル互換性の注意、ナレッジファイルの上限(最大20件・1件512MB・約200万トークン)、一部ユーザー向けにロールアウト中のモデル選択項目を追記。2026年4月発表の「Workspace Agents」(Business/Enterprise/Edu/Teachers向けの新しいチーム自動化機能)とGPTsの関係を新設の節で整理し、関連トピックに「ChatGPTのプラン比較」を追加
- **出典**: [OpenAI Help Center: Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-and-editing-gpts)、[OpenAI Help Center: What is ChatGPT Go?](https://help.openai.com/en/articles/11989085-what-is-chatgpt-go)、[OpenAI Help Center: ChatGPT Business Rename FAQ](https://help.openai.com/en/articles/12111915-chatgpt-business-rename-faq)、[OpenAI Help Center: What is the canvas feature in ChatGPT and how do I use it?](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it)、[OpenAI: Introducing workspace agents in ChatGPT](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)、[VentureBeat: OpenAI unveils Workspace Agents, a successor to custom GPTs for enterprises](https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more)

### 2026-07-04: 初版執筆
- **内容**: GPTsの作成条件・GPT Builderの画面遷移・設定項目・公開範囲の設定、他ツールとの対応付けを整理
- **出典**: [OpenAI Help Center: Creating and editing GPTs](https://help.openai.com/ja-jp/articles/8554397-creating-and-editing-gpts)、[OpenAI Help Center: ワークスペース内でGPTを共有する方法](https://help.openai.com/ja-jp/articles/9083988-%E3%83%AF%E3%83%BC%E3%82%AF%E3%82%B9%E3%83%9A%E3%83%BC%E3%82%B9%E5%86%85%E3%81%A7gpt%E3%82%92%E5%85%B1%E6%9C%89%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95)、[Microsoft Learn: エージェントビルダー](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder)
- **注記**: プラン名・料金・UI文言は変更が頻繁なため、実際の画面文言は執筆時点と異なる可能性がある
