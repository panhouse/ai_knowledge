---
title: GPTsの作り方と公開設定
part: 6
chapter: 第2章 主要ツールでの作り方
tags: [GPTs, ChatGPT, カスタムGPT, GPT Builder]
created: 2026-07-04
updated: 2026-08-05
---

# GPTsの作り方と公開設定

## これは何か

GPTs(カスタムGPT)は、特定の業務や役割に特化させたChatGPTを、プログラミングなしで作れる機能である。毎回同じ前提説明や参照資料をコピペしてから質問している人は、その手間をGPTsに1度設定してしまえば、以降はワンクリックで使い回せるようになる。

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

### 作成手順(2026年8月時点の目安)

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

### GPTs・ChatGPT Work・Workspace Agentsの関係(2026年8月時点)

GPTsの周辺には、性質の異なる2つの「自動化・エージェント機能」が2026年に追加されている。混同しやすいので整理する。

- **ChatGPT Work(2026年7月9日〜)**: 個人・チーム問わず使える新しい実行モード。旧来の「エージェントモード」の後継で、GPT-5.6を基盤に、依頼した作業をバックグラウンドで数分〜数時間かけて自律的に進め、スプレッドシートやスライド、レポート、簡易アプリといった「完成品」を返す。GPTsのような「固定の指示+ナレッジを毎回呼び出す軽量アシスタント」ではなく、都度のタスクをその場で自律的にこなす実行モードである点が異なる
- **Workspace Agents(2026年4月22日〜)**: Business/Enterprise/Edu/Teachers向けに発表された、Codexを基盤とするチーム向けエージェント機能。OpenAI自身が「GPTsの進化形(evolution of GPTs)」と位置付けており、Slack・Salesforce・Google Drive・Microsoft製品などの外部ツールに接続し、スケジュール実行や複数ステップの業務を継続的にこなせる。発表時点では研究プレビュー(research preview)扱いで開始された

OpenAIの公式ヘルプセンターは「GPTs will remain available while teams test workspace agents(チームがWorkspace Agentsを試している間もGPTsは引き続き利用可能)」「Soon, we'll make it easy to convert GPTs into workspace agents(近くGPTsをWorkspace Agentsへ変換しやすくする)」としており、GPTsの即時廃止を公式に明言してはいない。一方で海外メディアの複数の報道は、Business/Enterprise/Edu/Teachersのワークスペースにおけるカスタムアクション(またはGPTs自体)の提供終了時期を2026年8月26日ごろと伝えている。本稿執筆時点(2026年8月5日)ではOpenAI公式ヘルプセンターにこの具体的な終了日を明記した記載は確認できていないため、**法人ワークスペースの管理者は「報道されている」段階の情報として扱い、自組織のワークスペース管理画面のお知らせや移行ツールの提供状況を直接確認すること**を推奨する。

個人プラン(Free/Go/Plus/Pro)のGPTs作成・利用自体には現時点で影響がなく、「1つの決まったプロンプト+ナレッジで動く軽量なアシスタント」を作りたいだけならGPTsで十分。ひとりで完結する重めの作業を丸ごと任せたいならChatGPT Work、組織全体で外部システム連携や常時稼働の自動化まで踏み込みたい場合はWorkspace Agentsの対象プランかどうかを確認する。

## 注意点・よくある誤解

- **FreeプランとGoプランでは作れない**: 「GPTsを作りたいのに作成ボタンが出ない」という場合は、まずプランを確認する(Go契約者は「利用」はできても「作成」はできない)。
- **「Team」プランはもう存在しない**: 2025年8月に「Business」へ名称統合されているため、古い記事や社内資料の「Teamプラン」表記は現在のBusinessを指す。
- **ナレッジファイルは完全な機密性を保証しない**: アップロードしたファイルの内容が、Actionsの設定次第で意図せず引用・開示される可能性があるため、機密情報を含むファイルの扱いは慎重に。
- **GPTストア公開にはビルダープロフィールの公開設定が必須**: これを忘れると「誰でも」を選んでも公開に進めないことがある。
- **GPTストアで公開しても自動的に稼げるわけではない**: 収益分配プログラムは招待制の限定パイロットにとどまり、一般公開はされていない。
- **AppsとActionsは併用できない**: 外部連携をどちらで実装するか、GPTを作る前に決めておく。
- **Pro相当の深い推論モデルを選ぶとCanvas・Apps・画像生成が無効になる**: Canvasを使わせたいGPTでは、実行モデルが通常モード(非Pro)になっているか確認する。
- **法人ワークスペース(Business/Enterprise/Edu/Teachers)は「GPTsがいつまで使えるか」を自組織で要確認**: 2026年8月26日ごろに提供終了との報道があるが、本稿執筆時点でOpenAI公式が明記した終了日は確認できていない。ワークスペース管理者は自組織の管理画面のお知らせを直接確認すること。
- **チーム全体の自動化を考えているなら、GPTsだけで完結させようとしない**: 外部ツール連携やスケジュール実行が必要な用途は、Workspace Agents(対象プランの場合)の方が向いていることがある。個人で完結する重い作業の丸投げにはChatGPT Workが向いていることもある。

## 最初の一歩

自分が毎回同じ前提を説明してからChatGPTに質問している業務を1つ思い出し、その前提を「指示」欄に書き込んだGPTを1つ作ってみる(自分のみ公開で十分)。

## 関連トピック

- [GPTsのナレッジファイルとアクション連携](./gpts-knowledge-and-actions.md)
- [GPTs・Gem・Copilot Agent・Claude Projectsの比較と使い分け](./custom-ai-tools-comparison.md)
- [ChatGPTのプラン比較](../part03-ai-chat-tools/chatgpt-plan-comparison.md)

## 更新履歴

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
