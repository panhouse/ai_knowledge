---
title: "Anthropic API(Claude API)の基本"
part: 9
chapter: 第1章 LLM APIの基礎
tags: [Anthropic API, Claude API, API開発, LLM API]
created: 2026-07-06
updated: 2026-07-06
---

# Anthropic API(Claude API)の基本

## これは何か

Claude.ai(またはClaude Desktop/モバイルアプリ)を契約していれば、DifyやGASなど他のツールからもClaudeを自由に呼び出せる、と誤解している人は多い。実際にはClaude.aiのサブスク(Free/Pro/Max)とAnthropic API(従量課金、通称「Claude API」)は完全に別契約であり、社内システムやノーコードツールにClaudeを組み込みたい場合はAPIを別途契約する必要がある。この関係は[OpenAI APIの基本](openai-api-basics.md)で説明したChatGPTとOpenAI APIの関係とまったく同じ構図である。

## 仕組み・背景

- **Claude.ai**: claude.ai上でチャット形式でClaudeと対話する、エンドユーザー向けの製品。Free/Pro/Maxなどの月額サブスクリプションで提供される。
- **Anthropic API(Claude API)**: 開発者向けのインターフェースで、自社の業務システム・チャットボット・要約や分類のバッチ処理など、Claudeを自社サービスに組み込むための仕組み。管理画面は「Claude Developer Platform」(旧称・通称ともに「Claude Console」)と呼ばれ、Claude.aiのサブスク契約とは別会計である。Claude Proに入っていてもAPI利用料は割引されないし、逆にClaude.aiを契約していなくてもAnthropicアカウントと支払い方法さえあればAPIのみ契約できる。

APIの中核は**Messages API**と呼ばれる単一のエンドポイント(`POST https://api.anthropic.com/v1/messages`)で、会話履歴を`messages`配列として渡すとClaudeの応答が返ってくる。OpenAI APIのChat Completions API/Responses APIに相当する存在だが、認証ヘッダーや必須パラメータの作法が異なる(後述の比較表を参照)。

料金は「トークン(文章を分割した単位)」ごとの従量課金で、入力(プロンプト)側より出力(生成結果)側の単価が高く設定されている(2026年7月時点の主要モデルでは、おおむね出力が入力の5倍)。モデルのグレードによっても単価は大きく変わり、高性能なモデルほど高額になる。

## 使いどころ・使い分け

| やりたいこと | 向いている契約 |
|---|---|
| 自分でチャット画面から質問・相談したい | Claude.ai(Free/Pro/Max) |
| 社内システムやスプレッドシートにClaudeの機能を組み込みたい | Anthropic API |
| Difyやn8nなどノーコードツールでAIアプリを作りたい | Anthropic API(ノーコードツール側にAPIキーを設定) |
| 大量のデータを一括で要約・分類したい(即時応答不要) | Anthropic APIのBatch API(通常の半額で処理できる) |
| 長い社内文書・マニュアルを毎回参照させたい | Anthropic APIのPrompt Caching(同じ前提文を使い回して割引) |
| じっくり考えさせてから答えさせたい複雑な推論タスク | Anthropic APIのExtended Thinking対応モデル |

## 実務での使い方

### APIキーの取得手順

1. platform.claude.com(旧console.anthropic.com。現在はここにリダイレクトされる)にアクセスし、メール・Google・SSOでログインまたはサインアップする(Claude.aiと同じAnthropicアカウントでよい)
2. 左サイドバーの「API Keys」、または直接 platform.claude.com/settings/keys にアクセス
3. 先に「Settings」→「Billing」でクレジットカードを登録しておく(未登録だとキーを発行しても呼び出しがエラーになる)
4. 「Create Key」をクリックし、名前(例: "Production"、"Dify連携用")と権限(フルアクセス/読み取り専用)を設定する
5. 生成されたキー(`sk-ant-`で始まる文字列)はその場でしか全文表示されないため、必ずコピーして安全な場所に保管する(紛失時は再表示できず、失効させて再発行が必要)
6. あわせて「Settings」→「Limits」等から想定外の高額請求を防ぐための利用上限を設定しておく

### 最小のコード例(Messages API)

```bash
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-4-6",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "この請求書PDFの合計金額を1文で要約して"}
    ]
  }'
```

OpenAI APIと違い、認証は`Authorization: Bearer`ではなく`x-api-key`ヘッダーで行い、APIのバージョンを`anthropic-version`ヘッダーで明示する必要がある(公式SDKを使えば自動で付与される)。

### 料金体系のイメージ(2026年7月時点、モデル名・価格は変更が頻繁なため必ず公式ページ platform.claude.com/docs/en/about-claude/pricing で最終確認すること)

- 現行ラインナップはおおむねOpus(最上位)/Sonnet(バランス型)/Haiku(軽量・高速)の3グレードで、Opus 4.8は入力$5・出力$25、Sonnet 4.6は入力$3・出力$15、Haiku 4.5は入力$1・出力$5(いずれも100万トークンあたり)という水準が目安
- 出力トークンは入力トークンのおよそ5倍の単価
- Prompt Caching(直前と同じ前提文の再利用)を使うとキャッシュ済み入力は通常の入力より大幅に割引される(目安9割引)
- Batch API(非同期処理)は同期呼び出しに比べて約50%安い
- Opus/Sonnet系の一部モデルは100万トークンの長いコンテキストウィンドウに追加料金なしで対応

### ノーコードツール・業務システムとの連携例

- **Dify**: モデルプロバイダーの設定画面で「Anthropic」を選び、APIキーを入力するだけで、Dify上に作ったチャットボットやワークフローからClaudeを呼び出せる
- **GAS(Google Apps Script)**: `UrlFetchApp`で`https://api.anthropic.com/v1/messages`にHTTPリクエストを送り、スプレッドシートの内容を要約・分類するといった社内自動化によく使われる。ヘッダーに`x-api-key`と`anthropic-version`を忘れずに付与する
- **n8n / Zapier / Make**: 「Anthropic」用の専用ノード・アクションが用意されており、他システムとの連携・自動実行のトリガーとして組み合わせて使われる

### 代表的な機能(名前と一言メモ)

- **Messages API**: 会話履歴をやり取りする中核のエンドポイント。OpenAIのChat Completions APIに相当
- **Tool Use(ツール呼び出し)**: モデルに外部の関数・API・DBクエリを呼び出させる仕組み。OpenAIの「Function Calling」に相当する機能で、呼び方(用語)が異なるだけで考え方は同じ。詳しくは[Function Calling(Tool Use)の基本](function-calling-basics.md)を参照
- **Extended Thinking(拡張思考)**: 回答前にモデル内部でより長く「考える」過程を明示的に確保するモード。複雑な推論・計算・多段階の判断が必要なタスクの精度を上げられる
- **Prompt Caching**: システムプロンプトや長いマニュアル・ドキュメントなど、繰り返し使う前提文をキャッシュし、2回目以降の呼び出しコストを大幅に下げる仕組み
- **Batch API**: 大量のリクエストをまとめて非同期送信し、通常より安く(約半額)処理する仕組み

### OpenAI APIとの違い(比較表)

| 項目 | Anthropic API(Claude) | OpenAI API |
|---|---|---|
| 管理画面 | Claude Developer Platform(platform.claude.com) | platform.openai.com |
| 認証ヘッダー | `x-api-key: <キー>` | `Authorization: Bearer <キー>` |
| APIバージョン指定 | `anthropic-version`ヘッダーが必須(SDK利用時は自動) | 明示的なバージョンヘッダーは基本不要 |
| 中核エンドポイント | `/v1/messages`(Messages API) | `/v1/chat/completions` または `/v1/responses` |
| システムプロンプトの渡し方 | `messages`とは別に独立した`system`パラメータ | `messages`配列内に`role: "system"`として含める |
| 外部関数呼び出し | Tool Use | Function Calling |
| 「じっくり考えさせる」機能 | Extended Thinking | 推論(reasoning)系モデルの内部推論 |
| キャッシュ割引 | Prompt Caching(自動または明示指定、目安9割引) | プロンプトキャッシュ(自動適用、割引率はモデル依存) |
| 非同期・低価格処理 | Batch API(約50%割引) | Batch API(約50%割引) |
| 料金体系 | 入出力トークン単価制、出力は入力の約5倍が目安 | 入出力トークン単価制、出力は入力の3〜6倍程度が目安 |

大枠の思想(トークン従量課金、Batch APIでの割引、Tool Use/Function Callingの考え方)はよく似ているが、ヘッダー名・エンドポイント名・パラメータの細部が異なるため、片方のAPI用に書いたコードはそのままではもう一方に流用できない点に注意。

## 注意点・よくある誤解

- **Claude.ai課金とAPI課金は別会計**: Claude Proの月額料金はAPI利用料の割引にはならない。混同して「なぜ別料金が発生するのか」と驚かないよう、契約前に整理しておく。
- **料金・モデル名は非常に頻繁に更新される**: 2026年に入ってからもモデルの世代・価格が複数回改定されている。記事や社内資料に価格を書く場合は、必ず公式サイトの最新情報を都度確認する。
- **`x-api-key`と`anthropic-version`の付け忘れ**: OpenAI API用のコードを流用すると`Authorization: Bearer`のまま送ってしまいがちだが、Anthropic APIでは認証エラーになる。ヘッダーの違いを意識する。
- **利用上限を設定せずに使うと高額請求のリスクがある**: 想定外の大量呼び出し(バグによる無限ループ等)に備えて、必ず利用上限(Limits)を設定しておく。

## 最初の一歩

自社でDifyやGASなどのノーコード連携を検討しているなら、まずplatform.claude.comでAPIキーを1つ発行し、利用上限を低めに設定した状態で上記のcurl例をそのまま実行してみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)
- [Function Calling(Tool Use)の基本](function-calling-basics.md)
- [Claudeの基本](../part03-ai-chat-tools/claude-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: Claude.aiとAnthropic APIの違い、Messages APIの呼び出し方、APIキー取得手順、料金体系(モデル別トークン単価)、Tool Use/Extended Thinking/Prompt Caching/Batch APIの概要、OpenAI APIとの比較表を整理
- **出典**: [Claude Platform Docs: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)、[Claude Platform Docs: API overview](https://platform.claude.com/docs/en/api/overview)、[Claude Platform Docs: Versioning](https://platform.claude.com/docs/en/api/versioning)、[Claude Platform Docs: Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)、[CloudZero: Anthropic Claude API Pricing In 2026](https://www.cloudzero.com/blog/claude-api-pricing/)
- **注記**: モデル別の具体的な料金は変更が頻繁なため、本文の数値は目安として扱い、最新の単価は必ず [Claude Platform公式Pricingページ](https://platform.claude.com/docs/en/about-claude/pricing) で確認すること
