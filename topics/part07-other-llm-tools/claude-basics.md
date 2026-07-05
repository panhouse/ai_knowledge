---
title: Claude(Anthropic)の基本
part: 7
chapter: 第2章 その他のLLM
tags: [Claude, Anthropic, LLM比較]
created: 2026-07-05
updated: 2026-07-05
---

# Claude(Anthropic)の基本

## これは何か

Claudeは、AI開発企業Anthropic社が提供する生成AI(チャットサービス「claude.ai」+開発者向けAPI)。ChatGPTやGeminiと同じ「汎用チャット型AI」のカテゴリだが、**長文書類の読み込み・要約と、コーディング(プログラム作成)の精度**で評価が高く、「文章の質」と「正確さ」を重視する業務でChatGPT/Geminiと並ぶ有力な選択肢になる。この記事ではモデルの世代・料金プラン・主要機能を整理し、他のLLMとの使い分けの判断材料を示す。

## 仕組み・背景

2026年7月時点で、Claudeの主力モデルは以下の4系統。2026年6月にラインナップが刷新され、無料版・Proプランの既定モデルも入れ替わった。

| モデル | 位置づけ | コンテキスト長(一度に読み込める文章量の上限) | 拡張思考モード |
|---|---|---|---|
| Claude Fable 5 | 最上位モデル。長時間動く自律エージェント向けの「次世代の知能」と位置づけ(2026年6月9日提供開始) | 100万トークン(日本語で概算数十万字規模) | 常時オン(Adaptive Thinking) |
| Claude Opus 4.8 | 複雑な自律コーディング・法人向け高度タスク向け | 100万トークン | 対応(Adaptive Thinking) |
| Claude Sonnet 5 | 速度と知能のバランス型。無料版・Proプランの既定モデル(2026年6月30日提供開始、Sonnet 4.6の後継) | 100万トークン | 対応(Adaptive Thinking) |
| Claude Haiku 4.5 | 最速・低コストモデル。近フロンティア級の知能を持つ | 20万トークン | 対応(手動トグルの拡張思考) |

このほか「Claude Mythos 5」という、防御的サイバーセキュリティ用途に限定した招待制モデル(Project Glasswing経由)も存在するが、一般利用者向けではない。

**拡張思考モード(Extended Thinking)**は、Claudeが即答する前に「考える時間」を取り、複雑な問題を段階的に分解してから回答する仕組み。長らくチャット画面の「Thinking」トグルで手動オン/オフする形だったが、Fable 5・Opus 4.8・Sonnet 5では**Adaptive Thinking(適応的思考)**に進化し、質問の複雑さをモデル自身が判断して思考の深さを自動調整するようになった(エージェント的なタスクで、ツール呼び出しの間に考える「Interleaved Thinking」も自動的に有効になる)。Haiku 4.5は従来型の手動トグル方式を維持している。

## 使いどころ・使い分け

ChatGPT・Gemini・Claudeはいずれも汎用チャット型AIだが、得意分野と料金帯には明確な違いがある。

| 項目 | ChatGPT | Gemini | Claude |
|---|---|---|---|
| 得意分野 | 汎用性・エージェントモード(ブラウザ操作等)、画像/音声/動画生成 | Google製品(Gmail・ドキュメント・スプレッドシート)との統合、資料に基づく調査(NotebookLM) | 長文コンテキストでの資料読解・要約、文章の質、コーディング(Claude Code) |
| 料金帯(個人) | 無料/$8前後(Go)/$20(Plus)/$100〜$200(Pro) | 無料/月額千円未満〜(AI Plus)/数千円程度(AI Pro)/1万円台〜(AI Ultra) | 無料/$20(Pro)/$100〜$200(Max) |
| 料金帯(法人) | Business 1人$20〜25/月、Enterprise要問い合わせ | Google Workspace with Gemini(Business Starter以上に統合) | Team 1席$20〜125/月、Enterprise要問い合わせ(20席以上なら自己サーブ契約も可) |
| 向いている業務 | 汎用チャット、画像/動画生成、ブラウジング系エージェントタスク | Google Workspace文書の作成・要約、社内資料のリサーチ | 長文ドキュメントのレビュー・要約、自律コーディングエージェント、正確さ重視の文章作成・編集 |

判断の目安:
- **契約書・議事録・技術資料など長文を丸ごと読ませて要約・レビューさせたい** → Claude(長文コンテキストと文章精度に強み)
- **社内でGoogle Workspaceを使っており、メール・ドキュメントと連携させたい** → Gemini
- **画像/音声/動画生成や、ブラウザ操作を伴う半自律タスクまで幅広くこなしたい** → ChatGPT
- **社内エンジニアがプログラムのコーディング・リファクタリング・デバッグを自律的に進めさせたい** → Claude(Claude Code)

## 実務での使い方

### 個人向けプラン(2026年7月時点)

| プラン | 料金 | 特徴 |
|---|---|---|
| Free | $0 | Web/iOS/Android/デスクトップでチャット可能。Web検索・メモリ・コード実行・MCPコネクタも利用できるが、1日あたりの利用回数に上限あり。既定モデルはSonnet 5 |
| Pro | $20/月(年払いなら$17/月=年$204) | Free比おおよそ5倍の利用量、優先アクセス、Claude Codeの利用、Opus 4.8へのアクセスを含む |
| Max(5x) | $100/月 | Proの5倍の利用量 |
| Max(20x) | $200/月 | Proの20倍の利用量、新機能・新モデルへの優先アクセス |

### 法人向けプラン

| プラン | 料金 | 特徴 |
|---|---|---|
| Team Standard | 1席$25/月(年払いなら1席$20/月)、最少5席〜最大150席 | SSO・ドメインキャプチャ・JITプロビジョニング、一括請求・管理コンソール、既定でチャット内容をモデル学習に利用しない、Claude Codeを各席で利用可能 |
| Team Premium | 1席$125/月(年払いなら1席$100/月) | Team Standardの5倍の利用量 |
| Enterprise | 個別見積もり(2026年2月からは20席以上なら自己サーブ・クレジットカード契約も可能) | Team相当の機能に加え、SCIM連携・役割ベースアクセス制御(RBAC)・監査ログなど最も強固なデータ管理機能 |

いずれのプランも「席料」は基本利用分のみで、Claude Code・Cowork(共同作業機能)などの追加利用分は別途API相当のレートで課金される場合があるため、大規模導入時は利用量の見積もりが必要。

### 主要機能の使い方

- **Artifacts(アーティファクト)**: コード・HTML・図表(Mermaid)・Reactコンポーネント・整形済みMarkdownなど「まとまった生成物」を作らせると、チャットの右側にプレビュー用のサイドパネルが自動で開く機能。無料版でも利用可能。2026年4月には、データソースに接続したまま開くたびに最新状態へ更新される「Live Artifacts」が追加され、KPIダッシュボードや進行管理表などの用途で使える。ChatGPTの「Canvas」に近い位置づけ
- **Projects(プロジェクト)**: 左サイドバーの「Projects」→「新しいプロジェクトを作成」から、特定の業務・クライアント向けの作業スペースを作れる機能。「プロジェクトの知識」欄に社内資料・過去のやり取りをアップロードしておくと、そのプロジェクト内の会話で自動的に参照される。「カスタム指示」欄には、そのプロジェクトでの前提(役割・トーン・出力形式など)を書いておく。ChatGPTのGPTsの「指示」欄、Geminiの「Gemのカスタム指示」欄に相当
- **Claude Code**: ターミナル(コマンドライン)上で動く自律型のコーディングエージェント。コードの検索・編集・テスト実行・GitHubへのコミットまでを自律的に進める。Pro以上の個人プラン、およびTeam/Enterpriseの全席で利用可能。2026年6月には、コーディング作業の内容を1つのWebページにまとめて共有URLで公開する「Claude Code Artifacts」もベータ提供された
- **拡張思考/Adaptive Thinkingの切り替え**: claude.aiのチャット画面では、送信ボタン付近のモデル名の横に「Thinking」の表示がある。Haiku 4.5などではここで手動オン/オフできるが、Fable 5・Opus 4.8・Sonnet 5では自動判断(Adaptive Thinking)になっており、手動での無効化ができない場合がある

## 注意点・よくある誤解

- **モデルの「コンテキスト長」と、チャットで実際に扱える会話の長さは別物**: モデル自体は100万トークン規模の文章を扱えても、チャット画面での長い会話の継続可否はプランや実装上の制約を受ける。本当に長い資料を正確に扱いたい場合は、その場に貼るのではなくProjectsの「プロジェクトの知識」に登録する方が実務的
- **モデル名・料金は変更頻度が非常に高い**: 2026年に入ってからもモデル世代交代(Sonnet 4.6→Sonnet 5等)や料金改定が続いている。本ページの数値は目安であり、契約前に必ず[Claude公式の料金ページ](https://claude.com/pricing)で最新情報を確認すること
- **法人利用にはTeam以上への移行を検討**: 個人向けのFree/Pro/Maxには、SSOやデータ非学習のデフォルト保証・監査ログといった管理者向け機能がない。会社の機密情報を扱うならTeam以上を検討する
- **Claude Codeは「プラン契約すれば無制限に使える」わけではない**: 席料と利用量は別枠になっており、大量に使うと追加コストが発生する場合がある。導入前に想定利用量を見積もる

## 最初の一歩

claude.aiで無料アカウントを作成し、契約書や議事録など長めの資料を1つ貼り付けて要約させてみる。物足りなければ、同じ資料をChatGPTやGeminiにも読ませて出力を比べてみると、自社業務にどちらが向いているかの手がかりになる。

## 関連トピック

- [Google Geminiの基本](google-gemini-basics.md)
- [ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: Claudeの2026年7月時点のモデルラインナップ(Fable 5/Opus 4.8/Sonnet 5/Haiku 4.5)、個人向け(Free/Pro/Max)・法人向け(Team/Enterprise)プランの料金・機能差、Artifacts・Projects・Claude Code・拡張思考(Adaptive Thinking)の使い方、ChatGPT/Geminiとの使い分けを整理
- **出典**: [Anthropic公式ドキュメント: Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)、[Claude Help Center: What is the Max plan?](https://support.claude.com/en/articles/11049741-what-is-the-max-plan)、[Claude Help Center: What is the Team plan?](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)、[Claude Help Center: What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)、[Claude Help Center: What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)、[Claude Help Center: Change the model, effort, and thinking settings](https://support.claude.com/en/articles/10574485-using-extended-thinking)、[Anthropic公式ドキュメント: Adaptive thinking](https://platform.claude.com/docs/en/build-with-claude/adaptive-thinking)、[VentureBeat: Claude Code Artifacts update](https://venturebeat.com/data/anthropics-claude-code-artifacts-update-brings-live-shared-dashboards-and-interactive-workspaces-to-enterprises)
- **注記**: claude.com/pricingへの直接アクセスができなかったため、料金の一部は公式ヘルプ記事および複数の第三者情報のクロスチェックに基づく目安。正確な最新値は契約前に公式サイトで要確認
