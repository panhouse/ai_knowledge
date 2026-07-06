---
title: AIエージェントとは何か
part: 11
chapter: 第1章 AI市場の動向
tags: [AIエージェント, エージェンティックAI, 自律実行]
created: 2026-07-05
updated: 2026-07-05
---

# AIエージェントとは何か

## これは何か

ChatGPTやGeminiに質問を投げると、1回の回答で対話が完結する。これに対して「AIエージェント」は、人間が「ゴール(達成したい目標)」だけを渡せば、そこに至るまでの手順を自分で計画し、Web検索・ファイル操作・社内システムの呼び出しといった外部ツールを自ら使い分けながら、複数ステップの作業を最後までやり切ろうとするAIシステムを指す。「毎回指示しないと動かない」チャットボットと、「目標を渡せば後は任せられる」エージェントの違いを理解していないと、業務にAIを組み込む際の期待値も、権限設計もずれてしまう。

この自律的に計画・実行するAIの振る舞い方そのものを指す用語が「エージェンティックAI(Agentic AI)」であり、それを具体的なサービス・機能として実装したものが「AIエージェント」と呼ばれる。

## 仕組み・背景

AIエージェントの内部では、次のような「エージェントループ」が回っている。

1. ユーザーからゴールを受け取る
2. ゴールを達成するための手順を計画する
3. 必要なツール(Web検索、ファイル読み書き、ブラウザ操作、社内APIなど)を選んで呼び出す
4. ツールの実行結果を確認し、計画を見直す(失敗していれば別の手段を試す)
5. ゴールを達成した、あるいは人間の確認が必要と判断したら停止する

この「ツールをどう呼び出すか」を大規模言語モデル(LLM)自身に判断させる仕組みが「Function Calling(ツール呼び出し)」であり、さらに「そのツールがどこにあり、どう呼べばよいか」を各サービス間で共通化する規格として、Anthropicが2024年11月に公開した MCP(Model Context Protocol、モデル・コンテキスト・プロトコル)が事実上の業界標準として広がっている。2026年7月時点ではOpenAI・Google・Microsoft・AWSなど主要プラットフォームがMCPに対応しており、AIエージェントが社内システムやSaaSに接続する際の「共通の差込口」のような役割を果たしている(参照: [Anthropic「Introducing the Model Context Protocol」](https://www.anthropic.com/news/model-context-protocol))。

また、ブラウザやPC画面をマウス・キーボード操作で直接動かす能力を指して「Computer Use(コンピュータ操作)」と呼ぶ。API連携が用意されていないWebサイトや業務システムでも、人間と同じように画面を操作して代行できる点が特徴で、Anthropic・OpenAI・Googleがそれぞれ自社モデルにこの機能を組み込んでいる。

**従来のチャットボット/生成AIとAIエージェントの違い**

| 観点 | 従来のチャットボット・生成AI | AIエージェント |
|---|---|---|
| 依頼の単位 | 1回のプロンプトに対して1回の回答で完結 | 「ゴール」を渡すと、複数ステップの計画・実行を自動で繰り返す |
| 人間の関わり方 | 人間がステップごとに指示を出す(人間が「操作」する) | 次に何をすべきかをAI自身が判断する(人間は「委任」する) |
| 外部ツール・API利用 | 基本はテキスト生成のみ。検索や実行は補助的 | Web検索・ブラウザ操作・ファイル操作・社内システム呼び出しなどを自ら実行 |
| 状態の保持 | その会話の文脈のみを保持 | タスクの進行状況・中間結果・計画を保持し、失敗すれば計画を修正する |
| 出力の形 | テキスト(要約・文章・コード案など) | テキストに加え、実際の操作結果(送信済みメール、更新済みファイル、実行済みコードなど) |
| 典型的な依頼例 | 「この文章を要約して」 | 「競合3社の価格を調べて比較表を作り、Slackに投稿しておいて」 |
| 失敗した時の影響範囲 | 誤った回答をコピペしなければ影響は限定的 | 実行済みの操作(送信・削除・購入など)は取り消せない場合がある |

## 使いどころ・使い分け

**代表的なAIエージェントの分類(2026年7月時点)**

| 分類 | 主な役割 | 代表的なサービス・機能 |
|---|---|---|
| コーディングエージェント | 要件から実装・テスト・デバッグまでを自律的に実行 | Anthropic Claude Code、GitHub Copilot(CLI・Agent Mode)、Devin(Cognition)、Cursor |
| ブラウザ操作エージェント | Webサイトを実際に操作(検索・入力・購入など)して情報収集や作業を代行 | OpenAI ChatGPT Agent(旧Operator)、Google Gemini Spark(旧Project Mariner系機能を統合) |
| 業務自動化エージェント | 業務システム(CRM・ITSM・HRなど)に組み込まれ、定型業務を代行・オーケストレーション | Salesforce Agentforce、ServiceNow AI Agent Orchestrator、Microsoft Copilot Studio上のエージェント |
| 汎用アシスタントエージェント | 特定領域に限らず、調査・資料作成・タスク遂行を横断的に代行 | ChatGPT Agent、Google Gemini Spark、Microsoft 365 Copilot(Word/Excel/PowerPoint連携) |

**導入が向く業務の特徴**

- 手順がルール化できる、あるいは判断基準を言語化できる
- 利用先のシステムがAPIやMCPサーバーなど「ツール」として接続できる
- 誤りが起きても後戻り・修正が可能(取り消せる、影響範囲が小さい)
- 反復頻度が高く、承認フローを一度設計すれば繰り返し使い回せる

**導入がまだ向かない・要注意な業務の特徴**

- 対外送信・決済・削除など、取り消せないアクションを伴う
- 社内規程や法令解釈のように、都度の裁量判断・例外処理が必要
- 利用先システムがAPI化されておらず画面操作(GUI)しか手段がなく、かつ操作ミスの影響が大きい
- 権限管理・ログ・承認フローといったガバナンスが未整備

Gartnerは、自律型AIエージェントの導入パイロットのうち88%が本番運用まで進めず、生き残った11%は171%のROIを生んでいると分析しており、コスト超過・不明確な事業価値・不十分なリスク管理を理由に、2027年末までにエージェンティックAIプロジェクトの40%超が中止になると予測している。「向く業務」から小さく始め、ガバナンスを整えてから対象を広げるのが現実的な進め方になる(出典は更新履歴を参照)。

## 実務での使い方

### 主要ツールでの対応付け(2026年7月時点)

| 提供元 | 主なエージェント機能 | 呼び方・入り口 |
|---|---|---|
| OpenAI | ChatGPT Agent(2025年8月にOperatorを統合した後継)、開発者向けOpenAI Agents SDK | ChatGPTの入力欄でツールを選び「エージェントで実行」を指定。開発者はAgents SDK(Python/JavaScript)で組み込む |
| Anthropic | Claude Code(コーディングエージェント)、Claude Agent SDK、Computer Use(画面操作) | ターミナルで`claude`コマンドを実行。開発者はAgent SDK(Python/TypeScript)でカスタムエージェントを構築 |
| Google | Gemini Spark(24時間稼働の個人向けエージェント。旧Project Mariner系のブラウザ操作機能を統合) | Geminiアプリで「Spark」を選択(2026年7月時点はAI Ultraプランでベータ提供)。企業向けはGemini Enterprise(旧Vertex AI Agentspace) |
| Microsoft | Copilot Agents / Copilot Studio、Word・Excel・PowerPoint内の自律実行機能 | 各Office製品のCopilotボタンから、または「Copilot Studio」でエージェントを新規作成 |
| Salesforce | Agentforce | 「Agentforce Studio」でエージェントを設定し、CRM業務(リード対応・問い合わせ対応など)に組み込む |
| ServiceNow | AI Agent Orchestrator / AI Agent Studio | Now Platform内の「AI Agent Studio」で、既存エージェントの利用またはカスタムエージェントの作成を行う |

### コピペで使える実例: エージェントへの権限ポリシー

社内でAIエージェントを試す際は、最初に「どこまで人間の承認なしで実行させるか」を明文化しておくと、誤操作のリスクを大きく減らせる。エージェントへの指示(システムプロンプトやカスタム指示欄)に、次のようなテンプレートをそのまま貼り付けて使える。

```
## 承認不要で実行してよい操作
- Web検索、社内Wiki・ドキュメントの検索・要約
- メール文面・資料構成案などのドラフト作成(送信はしない)
- 既存データの集計・グラフ化・レポート作成

## 必ず事前確認を取る操作(承認必須)
- 社外へのメール送信・SNS投稿・チャット送信
- ファイルの削除・上書き・既存データの更新
- 決済・契約・予約など金銭や契約が発生する操作
- 個人情報・機密情報を含むデータの外部への出力

## 想定外の状況に遭遇したら
- 作業を中断し、判断に迷った点を報告してから次の指示を待つ
```

### 料金面で見ておくべきポイント

エージェントは1回のゴール達成のために何ステップも「計画→実行→確認」を繰り返すため、同じ依頼でも単発のチャットより消費トークン量が数倍〜数十倍になりやすい。Anthropicは2026年6月15日から、Claude Agent SDKやClaude Code GitHub Actions経由の利用を、対話的なClaude Code利用とは別建てのトークン課金で計測するようになっており、エージェント経由の作業は事前にステップ数や予算の上限を決めておかないとコストが読みにくくなる点に注意したい。

## 注意点・よくある誤解

- **「エージェント=文章がうまいチャットボット」ではない**: 依頼の単位が「1回の質問」から「ゴールの委任」に変わる点が本質的な違いであり、それに応じて権限設計・承認フローも作り直す必要がある。
- **過大な権限付与のリスク**: あるエージェントに「ファイルの読み取り・書き込み・削除」の全権限を与えたところ、タスク実行中に重要な設定ファイルを誤って削除し、復旧に2日を要した事例が報告されている。ファイル削除や本番環境への書き込みなど、影響が大きい操作は最小権限(必要な範囲だけ)に絞るのが基本。
- **プロンプトインジェクションのリスク**: ブラウザ操作エージェントやメール・Webページを読み込むエージェントは、閲覧先のページや受信メールに埋め込まれた悪意ある指示文に誘導され、意図しない操作を実行してしまう「プロンプトインジェクション」のリスクがある。外部コンテンツを読ませる用途では、実行前チェックや権限の絞り込みが特に重要。
- **ガバナンス整備が追いついていない**: Gartnerの調査では、自律型AIエージェントに対して成熟したガバナンス体制を持つ組織は21%にとどまるとされ、これが導入失敗の主因の一つとされている。
- **ハルシネーションは自律実行でも消えない**: 誤った前提のまま計画を立てて実行に進むと、その誤りが「実行結果」として現実の操作(送信・更新・購入など)に反映されてしまう。生成された情報を鵜呑みにせず、要所で人間が確認する設計が必要。

## 最初の一歩

まずは自社で既に使っているツール(ChatGPT・Claude・Gemini・Copilotなど)のエージェント機能を、影響範囲の小さい業務(社内向けの調査・資料のドラフト作成など)で試してみる。試す前に、上記のテンプレートを参考に「承認不要な操作」と「承認必須な操作」の境界を1行でも書き出しておくことが、事故を防ぐ最初の一歩になる。

## 関連トピック

- (関連ページは今後追加予定)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: AIエージェントの定義、従来のチャットボットとの違い(比較表)、エージェントループとMCP・Computer Useの仕組み、代表的な分類と2026年7月時点の主要サービス、導入の判断基準、権限ポリシーのテンプレート、企業導入におけるリスク(過大な権限付与・プロンプトインジェクション・ガバナンス未整備)を整理
- **出典**: [OpenAI: Introducing ChatGPT agent](https://openai.com/index/introducing-chatgpt-agent/)、[OpenAI: The next evolution of the Agents SDK](https://openai.com/index/the-next-evolution-of-the-agents-sdk/)、[Anthropic: Claude Agent SDK overview](https://code.claude.com/docs/en/agent-sdk/overview)、[Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)、[Google DeepMind: Project Mariner](https://deepmind.google/models/project-mariner/)、[Gemini: Gemini Spark overview](https://gemini.google/overview/agent/spark/)、[9to5Google: Gemini Spark rolls out to Google AI Ultra in the US](https://9to5google.com/2026/05/29/gemini-spark-ultra-us/)、[Microsoft: Microsoft Build 2026 – Empowering developers to adopt agentic AI](https://www.microsoft.com/insidetrack/blog/microsoft-build-2026-empowering-our-developers-to-adopt-agentic-ai-at-microsoft/)、[Salesforce: Agentforce Operations announcement](https://www.salesforce.com/news/stories/agentforce-operations-announcement/)、[ServiceNow: AI Agent Orchestrator press release](https://www.servicenow.com/company/media/press-room/ai-agents-studio.html)、[Gartner: Over 40% of agentic AI projects will be canceled by end of 2027](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)、[Gartner: Applying uniform governance across AI agents will lead to enterprise AI agent failure](https://www.gartner.com/en/newsroom/press-releases/2026-05-26-gartner-says-applying-uniform-governance-across-ai-agents-will-lead-to-enterprise-ai-agent-failure)
