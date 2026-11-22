---
title: Gemini Task(旧Gemini Spark)の基本
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [Gemini, Google, Gemini Task, Gemini Spark, AIエージェント, Antigravity, スケジュールタスク]
created: 2026-08-07
updated: 2026-11-22
---

# Gemini Task(旧Gemini Spark)の基本

## これは何か

Gemini Task(タスク)は、Geminiアプリに組み込まれた**自律実行エージェント**である。「今週のメールと予定を確認して、対応が必要なことを一覧にして」のように目標を渡すと、Gmail・Googleカレンダー・ドキュメント・スプレッドシートなどを実際に読み書きし、Webの閲覧・予約・買い物のようなブラウザ操作まで進めて、終わったら知らせてくれる。

2026年5月のGoogle I/Oで「**Gemini Spark**」として発表され、有料会員向けのベータとして提供されてきたが、2026年10月に**「Task」へ改称されて通常のチャット画面に統合**された。入力欄の近くにある「Chat/Task」の切り替えで呼び出す形になり、Sparkで作ったタスクやスケジュールはそのまま引き継がれている。さらに2026年11月時点のGoogle公式ヘルプでは、**日本・米国など6か国ではGoogle AIの有料プランなしでも使える**と案内されている([Gemini Apps ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en))。ネット上の記事で「Gemini Spark」と書かれているものは、いまの「Task」のことだと読み替えてよい。

ChatGPTの「ChatGPT Work」、Claudeの「[Claude Cowork](../part11-ai-agents/claude-cowork-basics.md)」と同じ「委任型エージェント」のGoogle版で、Googleのサービスに置いてある情報をそのまま扱える点が最大の強み。

## 仕組み・背景

### 名前の変遷: Project Mariner → Gemini Spark → Task

- **Project Mariner**: Google DeepMindのブラウザ操作エージェントの研究プロジェクト。機能はSparkに統合された
- **Gemini Spark(2026年5月〜)**: Google I/O 2026で発表。Geminiアプリの専用画面から使う「パーソナルAIエージェント」として、有料会員向けのベータで提供
- **Task(2026年10月〜)**: Googleは公式ヘルプで「分かりやすくするためにTaskに改称した」と説明している。Sparkの入口はナビゲーションから消え、通常チャットの入力欄の「Chat/Task」切り替えに統合された。設定画面の名前も「Gemini Spark Settings」から「Task settings」に変わった([9to5Google](https://9to5google.com/2026/10/12/gemini-spark-task-redesign/))

なお、Googleには以前から To-Do アプリ「Google ToDo リスト(Google Tasks)」もあり、Task(エージェント)とは別物である。TaskからGoogle ToDo リストを操作することはできる。

### 動き方

- **クラウドで作業を続ける**: タスクを始めたあとは端末を閉じても作業が続く。モバイルではリモート(クラウド上)のブラウザだけを使う。手元のパソコンのChromeを使う作業(デスクトップ限定)は、端末とChromeを起動したままにしておく必要がある
- **基盤**: Googleのエージェント基盤「Antigravity」の上に構築され、発表時点ではタスクごとに使い捨ての仮想マシン(VM)を割り当てる設計と説明されていた([Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud))
- **同時実行は最大15件**: 実行中のタスクが15件あると、スケジュールも起動しない
- **利用量は計算量ベース**: 上位のGoogle AIプランほど上限が大きく、上限に近づくとGeminiが通知する

### 承認が必要な操作

Taskは次の操作の前に**必ず利用者の確認を求める**設計になっている(2026年11月時点の公式ヘルプ)。

- メッセージの送信、データの削除、機微な情報の共有
- 購入、金融取引、Webフォームの入力・送信
- 「Googleでログイン」やGoogleパスワードマネージャーを使ったサイトへのサインイン

さらに、健康・金融・政府発行IDに関する情報を共有する前には、利用者が「常に許可」を選んでいても一時停止する。作業中はいつでも停止・ブラウザ操作の引き取り(テイクオーバー)・個別操作の拒否ができる。

### Google Workspaceとの連携

Gmail(検索・下書き)、カレンダー(予定の管理)、ドキュメント・スプレッドシート・スライドの編集、Keep・Google ToDo リストの管理ができる。使うには、Geminiアプリの設定でこれらのGoogleサービスとの接続を有効にしておく必要がある。

## 使いどころ・使い分け

### 向く仕事・向かない仕事

| 向く | 向かない |
|---|---|
| Gmail・カレンダー・Driveにある情報を横断して調べる・まとめる | 会社のGoogle Workspaceアカウントでの業務(仕事用・学校用アカウントは非対応) |
| ニュースレターの要約・整理、To-Doリスト作り、メルマガの配信停止 | 送信・決済などを承認なしで完了させたい業務 |
| 航空券・ホテルの価格を見張り、予算内になったら知らせる | 機微な情報を扱う作業を、無人のスケジュールで回すこと |
| 出典付きの調査をまとめ、PDF・文書・表・スライドに仕上げる | Outlook・Slack・Notionなど非Google系ツール中心の業務 |

### Chat と Task の使い分け

| | Chat(通常のチャット) | Task |
|---|---|---|
| 向く依頼 | 質問・相談・文章作成など、その場で答えが返るもの | 複数の手順を踏み、Googleサービスやブラウザを操作して仕上げるもの |
| 実行時間 | 数秒〜数十秒 | 数分〜それ以上(端末を閉じても続く) |
| スケジュール | チャットのスケジュール(定期的な要約など) | Taskのスケジュール(日時指定またはイベントをきっかけに実行) |
| 承認 | 基本的に不要 | 送信・削除・購入などの前に確認が入る |

チャットのスケジュールとTaskのスケジュールは別物として管理される。どちらもWeb版では「Scheduled」ページで一覧・一時停止・再開ができる。

### 他の委任型エージェントとの違い(2026年11月時点)

| | Gemini Task | [Claude Cowork](../part11-ai-agents/claude-cowork-basics.md) | ChatGPT Work |
|---|---|---|---|
| 提供元 | Google | Anthropic | OpenAI |
| 主な入口 | Geminiアプリ入力欄の「Task」切り替え | Claudeの通常チャット(2026年9月に統合) | ChatGPTのモード切り替え「Work」 |
| 強み | Gmail・カレンダー・Drive・Docsなど Googleサービスとの連携 | 手元のファイル・フォルダを扱う文書作成、Microsoft 365連携 | 汎用的なブラウザ操作・調査、多数のアプリ連携 |
| 会社のアカウント | 非対応(個人のGoogleアカウントのみ) | Team・Enterpriseで一般提供 | Business・Enterpriseで利用可 |

ツール横断の詳しい対応表(スケジュールタスクとの違い、常時稼働型エージェント、料金・プランの詳細)は[主要AIチャットツールのエージェント機能・スケジュールタスク比較](ai-chat-tools-agent-tasks-comparison.md)にまとめてある。本ページはTask単体の使い方に絞る。

## 実務での使い方

### 使える条件(2026年11月時点の公式ヘルプ)

| 条件 | 内容 |
|---|---|
| 年齢 | 18歳以上 |
| アカウント | 個人のGoogleアカウント(仕事用・学校用のアカウントは「現時点では」非対応) |
| 地域・プラン | 日本・米国・オーストラリア・カナダ・インド・韓国では**Google AIの有料プランなしで利用可**。それ以外のGemini提供地域ではGoogle AI ProまたはUltraが必要(EEA〈欧州経済領域〉・ナイジェリア・スイス・英国は対象外) |
| 利用できるアプリ | Geminiのモバイルアプリ、Mac用アプリ、Web版(gemini.google.com) |
| その他 | Geminiのアクティビティ(履歴)がオンになっていること |

無料で使える場合も、利用量の上限は有料プランより小さい(上位プランほど上限が大きい)。

### 始め方

1. Geminiアプリ(またはgemini.google.com)を開き、個人のGoogleアカウントでログインする
2. Gmail・カレンダーなどを使わせたい場合は、設定でGoogleサービスとの接続を有効にしておく
3. 入力欄の近くにある「**Chat/Task**」の切り替えで「**Task**」を選ぶ
4. 目標を自然文で書いて送信する。進行中・完了・要対応のタスクはサイドバーのチャット履歴に並び、「Ready(完了)/Needs attention(要対応)/In progress(進行中)」で絞り込める
5. 定期実行したい場合はタスクの中でスケジュールを設定する。Web版では「Scheduled」ページで一覧・一時停止・再開ができる

### コピペで使える依頼文の例

**① 週次のタスク整理(読み取り中心)**

```
今週1週間分のメールとカレンダーの予定を確認して、来週の月曜9時までに
対応が必要なことを一覧にし、スプレッドシートにまとめてください。
各行に「依頼者・内容・期限・元メールの件名」を入れてください。
返信や予定の変更など、取り消しにくい操作はしないでください。
```

**② 価格の見張り(スケジュール向き)**

```
12月20日〜22日の東京→福岡の往復航空券の価格を毎朝確認し、
往復3万円以下の便が見つかったら便名・価格・予約ページのURLを知らせてください。
予約や支払いは行わず、知らせるだけにしてください。
```

**③ 調査レポートの作成**

```
国内の中小企業向け勤怠管理SaaSを5つ調べ、料金(月額・1人あたり)・
無料トライアルの有無・主な機能を比較表にしたGoogleドキュメントを作ってください。
各数値には出典URLを付け、公式サイトで確認できなかった項目は「未確認」と書いてください。
```

「取り消しにくい操作はしない」「知らせるだけ」と、**やってよいことの範囲を毎回依頼文に書く**のがコツ。承認の確認が入る設計ではあるが、範囲を最初に絞っておくと確認の回数も減り、意図しない操作も防げる。

## 注意点・よくある誤解

- **「Gemini Spark」の記事は「Task」のことと読み替える**: 2026年10月の改称前の記事や比較表では「Spark」と書かれている。機能・タスク・スケジュールは引き継がれている
- **「無料で使える」≠「会社のアカウントで使える」**: 日本では有料プランなしでも使えるようになったが、**仕事用・学校用のGoogleアカウントでは2026年11月時点で使えない**。会社のGoogle Workspaceのデータを扱わせたい場合は、個人アカウントに業務データを持ち込まないこと(情報漏洩・社内規程違反のリスク)
- **スケジュールは端末の状態に左右される**: 公式ヘルプでは、Taskモードがオフの間や端末の電源が切れている間はスケジュールが実行されないとしている。また、オフライン中に実行されたスケジュールでは、意図しない操作を止められない可能性があると注意している。機微な作業をスケジュールに入れないこと
- **ログイン情報や支払い情報をタスクのチャットに書かない**: 必要な場面ではブラウザ操作を自分で引き取り(テイクオーバー)、Webページ上で直接入力する
- **間接プロンプトインジェクションのリスク**: 閲覧したWebページや受信メールに隠れた悪意ある指示に誘導される可能性がある。機密情報へのアクセスと外部送信の手段が同時にそろう使い方は特に注意する([プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md))
- **名前・提供条件は数か月単位で変わる**: Project Mariner→Spark→Taskと1年足らずで2度名前が変わり、提供条件も有料限定から一部の国での無料提供へ広がった。導入判断の前に[公式ヘルプ](https://support.google.com/gemini/answer/17094507?hl=en)で最新の条件を確認する

## 最初の一歩

個人のGoogleアカウントでGeminiを開き、入力欄の「Task」を選んで、上の①のような送信や変更を含まない読み取り中心の依頼を1件試してみる。

## 関連トピック

- [主要AIチャットツールのエージェント機能・スケジュールタスク比較](ai-chat-tools-agent-tasks-comparison.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [Claude Coworkの基本](../part11-ai-agents/claude-cowork-basics.md)
- [ChatGPTのエージェント機能(ChatGPT Work・dots)とスケジュールタスク](chatgpt-agent-mode-feature.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)

## 更新履歴

### 2026-11-22: 「Task」への改称と無料提供の拡大を反映して全面改訂
- **内容**: 2026年10月にGemini Sparkが「Task」に改称され、通常チャットの「Chat/Task」切り替えに統合されたことを反映してページを全面改訂。公式ヘルプにもとづき、利用条件(18歳以上・個人アカウントのみ・日本など6か国は有料プランなしで利用可・対応アプリ)、同時実行15件の上限、確認が必要な操作、スケジュールの管理場所と端末オフ時の挙動、テイクオーバーを整理。Chat/Taskの使い分け表と依頼文の例を追加し、陳腐化した料金表(Ultra・Proの月額と提供開始経緯)と他社エージェントの搭載モデル名を削除
- **出典**: [Manage your tasks & workflows in Gemini Apps(Gemini Apps ヘルプ)](https://support.google.com/gemini/answer/17094507?hl=en)、[9to5Google: Gemini 'Task' redesign integrates Spark into the main chat app(2026年10月12日)](https://9to5google.com/2026/10/12/gemini-spark-task-redesign/)、[Chrome Unboxed: Google is quietly ditching the 'Spark' brand(2026年10月1日)](https://chromeunboxed.com/google-is-quietly-ditching-the-spark-brand-to-merge-tasks-directly-into-gemini/)、[Claude by Anthropic: Claude Cowork and chat are now one Claude](https://claude.com/blog/cowork-is-now-claude)

### 2026-08-07: 初版執筆
- **内容**: Gemini SparkをGoogle版の委任型エージェントとして新規執筆。Antigravity基盤・セッション専用VM・送信・決済前の承認要求、Google Workspace/Enterprise連携、Claude Cowork・ChatGPT Workとの比較表、2026年8月時点の対応プラン、法人Workspaceアカウントが非対応である点の注意を整理
- **出典**: [Gemini Spark(公式)](https://gemini.google/overview/agent/spark/) /
  [Innovations from Google I/O 26 on Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud) /
  [Gemini Spark、Proプランで利用可能に(Impress Watch)](https://www.watch.impress.co.jp/docs/news/2128877.html) /
  [Google、AIエージェント「Gemini Spark」をAI Proへ拡大(マイナビニュース)](https://news.mynavi.jp/techplus/article/20260730-4756674/) /
  [GIGAZINE: Gemini Spark、日本語対応](https://gigazine.net/gsc_news/en/20260716-gemini-spark-japanese/)
