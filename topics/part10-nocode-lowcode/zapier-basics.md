---
title: "Zapierの基本"
part: 10
chapter: 第3章 自動化・連携ツール
tags: [Zapier, 自動化, ノーコード, AIエージェント]
created: 2026-07-06
updated: 2026-07-06
---

# Zapierの基本

## これは何か

「問い合わせフォームの回答をいちいちスプレッドシートに転記している」「新規リードが来たらSlackで通知したいが、エンジニアの手を借りずに自分たちで自動化を組みたい」——こうした部門レベルの業務自動化を、プログラミング知識なしで実現する最も老舗かつ利用者数の多いツールがZapier(ザピアー)である。2011年創業のクラウド専業サービスで、Gmail・Slack・Google スプレッドシート・Salesforceなど9,000以上のアプリ同士を「Zap(ザップ)」という単位でつなぎ、トリガー(処理の起点)とアクション(実際の処理)を選ぶだけでノーコードの自動化フローを作れる。すでに社内の非AI自動化でZapierを使っている企業は多いが、近年はAIエージェント機能「Zapier Agents」や自然言語でZapを組み立てる「Zapier Copilot」を追加し、単なる連携ツールから「AIも扱えるオーケストレーション基盤」へと進化している。

## 仕組み・背景

Zapierの基本単位は「Zap」で、1つのトリガー(例: フォーム送信、新着メール受信、スプレッドシートの行追加)と、それに続く1つ以上のアクション(例: Slackに投稿、AIに分類させる、CRMにレコードを追加)を組み合わせて作る。[n8n](./n8n-basics.md)の「ノード」や[Make](./make-basics.md)の「モジュール」と考え方は同じだが、Zapierは画面をできるだけシンプルに保ち、非エンジニアが迷わず設定できることを最優先に設計されている。

### AI関連の仕組み

2023年以降、Zapierは段階的にAI機能を追加してきた。2026年7月時点で中心となるのは次の3つである。

- **Zapier Copilot**: 「Slackにメッセージを送るステップを追加して」のように自然言語で指示すると、AIがZapの構成(トリガー・アクション・フィールドのマッピング)を自動生成する機能。Zap・Tables(表形式データベース)・Interfaces(簡易な業務アプリ作成機能)・Chatbots・Agentsなど、Zapierの全プロダクトを横断してAIが編集を支援する。変更ごとに「チェックポイント」が作られ、1クリックで元に戻せる。
- **Zapier Agents(旧称: Zapier Central)**: 自律的に判断してタスクを遂行する「AIチームメイト」を作る機能。指示文で「何をトリガーに、どのアプリを使って、何をすべきか」を記述するだけでエージェントが組める。PII(個人情報)・プロンプトインジェクション・有害な言い回しなどを検知して出力をブロック・エスカレーションする「AI Guardrails」、任意のLLMを指定できる「Bring Your Own Model」、過去の対話・処理結果を保持する「Memory」といった機能を備え、9,000以上のアプリに対して行動できる。
- **AI Actions**: ChatGPTなど外部のAIアシスタントからZapierのアクションを自然言語で呼び出せるようにする機能。Zap側だけでなく、他社のAIチャット製品からZapierの連携先を操作したい場合に使う。

これらは2025年から2026年にかけて有料プランに標準搭載されるようになり、Zaps(ワークフロー)・Agents・Copilot・Tables・Interfaces・Forms・Canvas(ワークフロー図)・Chatbotsという7〜8種の製品群が「1つのプラットフォーム」としてまとめて提供される形に整理されている。

## 使いどころ・使い分け

| やりたいこと | 向いているツール |
|---|---|
| プログラミング知識がないメンバーが最短で自動化を始めたい、対応アプリ数を重視したい | Zapier(9,000以上のアプリ連携数は業界最多クラス) |
| 複数のSaaS・DB・社内システムをつなぎ、AIをその中の1ステップとして使いたい | Zapier・[Make](./make-basics.md)・[n8n](./n8n-basics.md) |
| AIチャットボット・社内RAG検索アプリなど「AI利用そのもの」が主目的 | [Dify](./dify-basics.md)(RAG・プロンプト管理・チャットUIが標準装備) |
| セキュリティ・データ主権を重視し自社サーバーで運用したい | n8n(セルフホスト無料。Zapier・Makeはクラウド専用) |
| 複雑な条件分岐やコードによる細かいデータ加工が必要 | n8n(Codeノードで直接JavaScript/Pythonを実行できる) |
| 自律的に判断して複数アプリを横断操作するAIエージェントを、非エンジニアがGUIだけで作りたい | Zapier(Zapier Agents)。次点でMake AI Agents |

比較表([n8nの基本](./n8n-basics.md)・[Makeの基本](./make-basics.md)の比較表と対応。2026年7月時点の目安。料金・仕様は変更されやすいため各公式サイトで最終確認すること)

| 項目 | Zapier | n8n | Make | Dify |
|---|---|---|---|---|
| 主な用途 | 汎用ワークフロー自動化(連携アプリ数が最多クラス) | 汎用ワークフロー自動化(AIは機能の1つ) | 汎用ワークフロー自動化 | AIチャットボット/RAGアプリ構築 |
| AI機能 | Zapier Agents(自律型AIエージェント)、Zapier Copilot(自然言語でのZap自動生成)、AI Actions | AI Agentノード、主要LLM全対応、LangChain統合 | OpenAI/Anthropic/Gemini等の公式モジュール、Make AI Agents | LLM呼び出しが中核機能、RAGが標準搭載 |
| セルフホスト | 不可(クラウド専用) | 可(無料、要インフラ管理) | 不可(クラウド専用) | 可(無料、要インフラ管理) |
| 料金モデル | タスク(1アクションステップの実行)課金 | セルフホスト無料/クラウドは実行(ワークフロー1回の実行)課金 | クレジット課金(標準モジュール実行1回=1クレジットが基本) | セルフホスト無料/クラウドはメンバー数・アプリ数等で段階課金 |
| 学習コストの目安 | 低(非エンジニア向けに設計、対応アプリ数が多く迷いにくい) | 中〜高(ノードの概念・データ構造の理解が必要) | 低〜中 | 中(AI特化のため機能は絞られている) |

「AIの生成・判断が主目的ならDify、業務システム間の連携が主目的でAIはその一部ならZapier/Make/n8n」という大枠は3ツール共通だが、その中でも「対応アプリ数の広さ・ブランド認知度・とにかく迷わず使い始められること」を最優先するならZapier、「画面の分かりやすさと価格の手頃さ」ならMake、「柔軟性・セルフホスト可否・複雑なロジック」ならn8nという住み分けが実務上の目安になる。ZapierとMakeは近い競合関係にあり、一般にZapierの方が連携アプリ数・ブランド認知度で先行し、Makeはより複雑な分岐・データ加工を視覚的に組みやすい代わりに画面の情報量がやや多い。

## 実務での使い方

### Zap作成の基本手順(画面の場所)

1. zapier.comでサインアップ後、左メニューの「Zaps」→右上の「Create Zap(Zapを作成)」をクリックする
2. 「Trigger(トリガー)」の検索窓にアプリ名(例: 「Google Forms」「Gmail」)を入力し、起点となるイベントを選ぶ
3. 「+」でアクションを追加し、同様にアプリ名で検索する。AIを使う場合は「AI by Zapier」アクション、またはOpenAI・Anthropic・Google Geminiなど各社の公式連携アクションを選ぶ
4. 各ステップをクリックすると右側に設定パネルが開き、対象サービスのアカウント接続とフィールドのマッピングを行う
5. 画面上部の「Test step(テスト実行)」で各ステップの入出力を確認する
6. 問題なければ画面右上の「Publish(公開)」でZapを有効化し、常時稼働させる

AIエージェントを作る場合は左メニューの「Agents」から「Create agent」を選び、テンプレートを使うか、指示文(何をトリガーに、どのアプリを使って、何をすべきか)を自然言語で入力する。作成中はZapier Copilotが右側に開き、アクションの追加やエラー調査を対話形式で支援してくれる。

### 料金プラン(2026年7月時点の目安。最新情報は zapier.com/pricing で必ず確認)

課金の単位は「タスク」で、Zapが実際にアプリへ書き込み・読み込みなどのアクションを実行するたびに1タスクとしてカウントされる(トリガーの検知自体は通常タスクに含まれない)。ステップ数の多いZapほどタスク消費が早い点が、n8n(ワークフロー1回の実行単位)・Make(クレジット単位)との課金モデルの違いになる。

| プラン | 料金(年払い時の月額目安) | タスク数/月の目安 | 主な特徴 |
|---|---|---|---|
| Free | 無料 | 100タスク | Zapは1トリガー+1アクションの2ステップのみ。Tables・Interfacesなど基本機能は利用可 |
| Professional | 約$19.99/月〜(750タスクの場合。スライダーで最大200万タスクまで段階的に上がる) | 750タスク〜 | マルチステップZap、条件分岐(Paths)、Webhook、AIフィールドなどが利用可能 |
| Team | 約$69/月(年払い、25ユーザーまで) | 2,000タスク〜(超過分は自動でPay-as-you-goに切替、目安として通常単価の約1.25倍) | 複数ユーザー・ロール管理、Zap共有 |
| Enterprise | 個別見積り | 年間タスク管理など要相談 | SSO、高度なガバナンス、専任サポート |

### 実務ユースケース例:フォーム回答をAIで分類してSlackに通知

構成は「Google Forms(トリガー)→ AI by Zapier(または OpenAI/Anthropic)アクションで分類 → Slackアクションで投稿」という3ステップ。

1. **Google Formsトリガー**: 「New Form Response(新しい回答)」をトリガーイベントに設定する
2. **AIアクションのプロンプト例(コピペ可)**
   ```
   以下の問い合わせ内容を読み、次の3カテゴリのいずれか1語だけで分類してください。
   カテゴリ: 「見積依頼」「クレーム」「その他」

   問い合わせ内容:
   {{フォームの回答本文}}
   ```
3. **Slackアクション(Send Channel Message)**: 投稿先チャンネルを指定し、メッセージ本文に「フォーム回答: {{回答本文}} / 分類結果: {{前段AIアクションの出力}}」のように前段ステップの出力を変数として埋め込む

同じ構成で、後段のアクションをGoogle スプレッドシートへの記録やCRMへのレコード追加に差し替えれば、他業務にもそのまま応用できる。

## 注意点・よくある誤解

- **タスク課金は「ステップ数」に直結する**: マルチステップZapほど1回の起動で消費するタスク数が増えるため、AIによる分類・要約などをZapに組み込むほど、n8n(実行単位)・Make(クレジット単位)と比べて見積りが割高になりやすい。大量処理を想定するなら、ステップ数とタスク単価を必ず事前計算する
- **Freeプランは2ステップ限定**: 「トリガー+アクション1つ」しか組めないため、フォーム回答→AI分類→Slack通知のような3ステップ以上のZapを試すには、最初からProfessional以上の有料プランが必要になる
- **超過分は自動でPay-as-you-goに切り替わる**: 月間タスク上限に達すると、明示的に止めない限り上位プランへの誘導や超過課金(通常単価の約1.25倍が目安)が自動的に発生する。想定外の課金を避けるため、通知設定や上限の見直しを定期的に行う
- **即時性・複雑なロジックには限界がある**: トリガーがポーリング型(定期的な巡回検知)の場合、反映まで数分のラグが出ることがある。即時性が必要ならWebhookトリガーを使う。また複雑な繰り返し処理やコードによる細かいデータ加工は、n8nのCodeノードのような自由度には及ばない
- **データがZapierという第三者SaaSを経由する**: 業務データがZapierのクラウド上を経由するため、社内のデータ主権・セキュリティ規定によっては利用可否の確認が必要になる。厳格な自社管理が必要な場合はn8nのセルフホストが選択肢になる
- **AI機能の課金はZapier側のタスク消費+モデル利用分**: AI by Zapierや各社LLM連携アクションを使う場合、Zapierのタスク課金に加えて、利用するモデル・トークン量に応じた消費が発生する場合がある。想定コストは事前に小さく試して確認する

## 最初の一歩

zapier.comで無料アカウントを作成し、「Google Forms(またはGmail)→ AI by Zapierで分類・要約 → Slack通知」という3ステップのZapを1つ作り(2ステップ超のためProfessionalの無料トライアルを使う)、「Test step」で実際に動かしてみる。

## 関連トピック

- [n8nの基本](./n8n-basics.md)
- [Makeの基本](./make-basics.md)
- [Difyとは何か](./dify-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: Zapierの概要(Zapという基本単位、9,000以上のアプリ連携)、AI関連機能(Zapier Copilot、Zapier Agents〈旧Zapier Central〉、AI Actions)、n8n/Make/Difyとの比較表、Zap作成の画面操作手順、料金プラン(タスク課金モデル)、フォーム回答のAI分類→Slack通知の実装例を整理
- **出典**: [Zapier Pricing 公式](https://zapier.com/pricing)、[Zapier Pricing 2026 (No Code MBA)](https://www.nocode.mba/articles/zapier-pricing-2026)、[Zapier Pricing Breakdown 2026 (Activepieces)](https://www.activepieces.com/blog/zapier-pricing)、[Build an agent in Zapier Agents (Zapier Help)](https://help.zapier.com/hc/en-us/articles/24393442652557-Build-an-agent-in-Zapier-Agents)、[Build AI teammates with Zapier Agents (Zapier公式)](https://zapier.com/agents)、[Zapier AI Agents 2026 Complete Guide (Sacesta)](https://www.sacesta.com/our-work/blog/zapier-ai-agents-complete-guide-2026)、[Zapier Agents: Combine AI agents with automation (Zapier公式ブログ)](https://zapier.com/blog/zapier-agents-guide/)、[Generate Zap outlines using natural language and AI (Zapier Help)](https://help.zapier.com/hc/en-us/articles/15705185924621-Generate-Zap-outlines-using-natural-language-and-the-power-of-AI-Beta)、[What is Zapier Copilot? (Zapier Help)](https://help.zapier.com/hc/en-us/articles/38215656607757-What-is-Zapier-Copilot)、[Zapier Copilot: Build systems even faster with AI (Zapier公式ブログ)](https://zapier.com/blog/zapier-copilot-guide/)、[Zapier Adds Copilot Assistant and Enterprise-Grade Governance (SD Times)](https://sdtimes.com/zapier-adds-copilot-assistant-and-enterprise-grade-governance-to-ai-orchestration-platform/)
- **注記**: 料金プラン名・タスク数・金額は第三者メディアの記載をもとにした2026年7月時点の目安。掲載・記事化前に zapier.com/pricing で最終確認を推奨
