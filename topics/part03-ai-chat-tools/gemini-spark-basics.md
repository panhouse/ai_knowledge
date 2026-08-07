---
title: Gemini Spark(Google)の基本
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [Gemini, Google, Gemini Spark, AIエージェント, Antigravity, Google AI Ultra]
created: 2026-08-07
updated: 2026-08-07
---

# Gemini Spark(Google)の基本

## これは何か

Gemini Spark は、Google が2026年5月のGoogle I/Oで発表した**Gemini appに常駐する自律実行エージェント**である。
「今週の競合情報を調べてスプレッドシートにまとめて」のように目標を渡すと、Gmail・Googleカレンダー・
ドキュメント・スプレッドシートなどを実際に読み書きしながら、**スマホの電源を切っても・PCを閉じても
クラウド上で作業を続け**、完了したら通知する。

ChatGPTの「ChatGPT Work」、Claudeの「[Claude Cowork](../part11-ai-agents/claude-cowork-basics.md)」と
同じ「委任型エージェント」のGoogle版だが、Sparkは**24時間365日クラウドの専用VM(仮想マシン)で稼働し続ける**
ことを前面に押し出している点が特徴で、Google はこれを「パーソナルAIエージェント」と位置づけている
([Gemini公式](https://gemini.google/overview/agent/spark/))。

## 仕組み・背景

### Antigravity基盤とGemini 3.5

Sparkは Google のエージェント基盤「**Antigravity**」の上に構築され、モデルには高速・低コストな
**Gemini 3.5 Flash**が使われている。1つのタスクごとに**セッション専用の使い捨てVM**が新規に割り当てられ、
セッション間でデータが混ざらない設計になっている。すべての通信は「Agent Gateway」経由で行われ、
認証情報がエージェント自身に平文で渡らないよう暗号化される([Google Cloud Blog](https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud))。

### 承認が必要な操作

Sparkは「見えないところで勝手に何でもやる」わけではなく、**メール送信や決済など取り消しにくい操作の前には
明示的な承認を求める**仕組みが組み込まれている。進行中は要所で通知が届き、ユーザーはいつでも介入できる。

### Google Workspaceとの統合、企業向けの連携

個人向けはGmail・カレンダー・Drive・ドキュメント・スプレッドシート・スライド・YouTube・Googleマップと標準連携する。
企業向けの「Gemini Enterprise」版では、Microsoft SharePoint・OneDrive・ServiceNowなど社外のSaaSにも
コネクタ経由で接続でき、たとえば「新機能のリクエストを検知したらAntigravityと連携してコード変更を提案し、
Jiraチケットを作成し、スケジュールを再計算する」といった**開発フローへの組み込み例**も示されている
(Sparkが高レベルの判断・調整を行い、Antigravityがコード生成などの実装を担う構図)。

## 使いどころ・使い分け

### 向く仕事・向かない仕事

| 向く | 向かない |
|---|---|
| Gmail・カレンダー・Driveにある情報を横断して調べる・まとめる | 会社のGoogle Workspaceアカウントでの利用(個人アカウント限定) |
| 定型化された週次・月次のレポート作成 | 送信・決済などを承認なしで完了させたい業務 |
| 長時間かかる調査を裏で走らせ、完了後に確認する使い方 | リアルタイムの対話が必要な業務 |

### 他の委任型エージェントとの違い

| | Gemini Spark | [Claude Cowork](../part11-ai-agents/claude-cowork-basics.md) | ChatGPT Work |
|---|---|---|---|
| 提供元 | Google | Anthropic | OpenAI |
| 基盤 | Antigravity + Gemini 3.5 Flash | Claude | GPT-5.6系 |
| 実行場所 | Google Cloud専用VM(常時稼働) | 手元PC中心(Web/モバイルはベータ) | クラウド(仮想ブラウザ) |
| 得意分野 | Google Workspace連携、Web情報の収集の速さ | ローカルファイルを扱う文書作成、慎重な推論 | 汎用的なブラウザ操作・調査 |
| 主な入口 | Gemini app内の「Spark」 | Claude Desktop/Web/モバイル | ChatGPTの「Work」タブ |

ツール横断の詳しい対応表(スケジュールタスクとの違い、料金・プランの詳細、日本からの利用可否など)は
[主要AIチャットツールのエージェント機能・スケジュールタスク比較](ai-chat-tools-agent-tasks-comparison.md)に
まとめてあるため、本ページでは Spark 単体の使い方とレビューの実務に絞って書く。

## 実務での使い方

### 使えるプラン・利用開始方法(2026年8月時点)

Sparkは個人のGoogle AIサブスクリプションに含まれる機能で、法人のGoogle Workspaceアカウントでは使えない。

| プラン | 月額(日本) | Spark利用可否 |
|---|---|---|
| Google AI Ultra | 14,500円〜 | 可(2026年7月16日に日本語対応・利用可能に) |
| Google AI Pro | 2,900円 | 可(2026年7月29日、日本のPro契約者にも「数週間以内」に順次展開すると発表) |
| Free | 無料 | 不可 |

利用開始は、Gemini app(スマホ・Web)を開き「Spark」を選択して目標を自然文で伝えるだけ。
専用の設定画面は不要だが、**Gmail・カレンダーなど使わせたいサービスへの接続許可**は初回に確認される。

### コピペで使える依頼文の例

```
今週1週間分のメールとカレンダーの予定を確認して、来週の月曜9時までに
対応が必要なタスクを一覧にしてスプレッドシートにまとめてください。
返信や予定の変更など取り消しにくい操作をする前には、必ず私に確認してください。
```

「取り消しにくい操作の前には確認してください」は、承認の粒度を明示するために毎回入れるとよい。

## 注意点・よくある誤解

- **「日本語対応した」≠「会社のアカウントで使える」**: 2026年7月に日本語対応・利用可能になったのは
  個人のGoogle AI Ultra/Pro契約者のみ。会社のGoogle Workspaceアカウントでは2026年8月時点でまだ使えない
- **エージェントモードはチャットよりコストが跳ねやすい**: 検索→確認→実行を何ステップも繰り返すため、
  同じ質問をチャットで聞くより消費量が大きい
- **間接プロンプトインジェクションのリスク**: 閲覧したWebページや受信メールに悪意ある指示が
  埋め込まれていると、それに従ってしまう可能性がある。機密情報へのアクセスと外部送信手段が同時に
  揃う使い方は特に注意する([プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md))
- **この分野は数か月で変わる**: Project MarinerがSparkに統合されたように、名称・対応プラン・料金は
  今後も変わりうる。導入判断時は必ず公式ページで最新情報を確認する

## 最初の一歩

Google AI ProまたはUltraを契約している場合、Gemini appで「Spark」を開き、
送信や決済を含まない軽い調査(「今週の未読メールを要約して」など)を1件試してみる。

## 関連トピック

- [主要AIチャットツールのエージェント機能・スケジュールタスク比較](ai-chat-tools-agent-tasks-comparison.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [Claude Coworkの基本](../part11-ai-agents/claude-cowork-basics.md)
- [ChatGPTのエージェント機能(旧ChatGPT Agent→ChatGPT Work)とスケジュールタスク(Tasks)](chatgpt-agent-mode-feature.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)

## 更新履歴

### 2026-08-07: 初版執筆
- **内容**: Gemini SparkをGoogle版の委任型エージェントとして新規執筆。Antigravity基盤+Gemini 3.5 Flash・
  セッション専用VM・Agent Gateway経由の認証情報保護といった技術的な仕組み、送信・決済前の承認要求、
  Google Workspace/Enterprise連携の実例、Claude Cowork・ChatGPT Workとの比較表、
  2026年8月時点の対応プラン(Ultra 14,500円〜/Pro 2,900円、日本での提供開始経緯)、
  法人Workspaceアカウントが非対応である点の注意を整理
- **出典**: [Gemini Spark(公式)](https://gemini.google/overview/agent/spark/) /
  [Innovations from Google I/O 26 on Google Cloud](https://cloud.google.com/blog/products/ai-machine-learning/innovations-from-google-io-26-on-google-cloud) /
  [Gemini Spark、Proプランで利用可能に(Impress Watch)](https://www.watch.impress.co.jp/docs/news/2128877.html) /
  [Google、AIエージェント「Gemini Spark」をAI Proへ拡大(マイナビニュース)](https://news.mynavi.jp/techplus/article/20260730-4756674/) /
  [GIGAZINE: Gemini Spark、日本語対応](https://gigazine.net/gsc_news/en/20260716-gemini-spark-japanese/)
