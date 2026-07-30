---
title: "主要LLM APIの横断比較(OpenAI・Anthropic・Google)"
part: 9
chapter: 第1章 LLM APIの基礎
tags: [OpenAI API, Anthropic API, Gemini API, API比較, 認証, 料金, モデル選定]
created: 2026-07-30
updated: 2026-07-30
---

# 主要LLM APIの横断比較(OpenAI・Anthropic・Google)

## これは何か

OpenAI・Anthropic(Claude)・Google(Gemini)のAPIは、いずれも「トークン従量課金でチャット系エンドポイントを叩く」という基本思想は同じだが、認証ヘッダー・エンドポイント名・モデルの呼び分け方・料金の刻み方が三社三様で、片方用に書いたコードや見積もりはそのまま流用できない。各社個別の「◯◯ APIの基本」([OpenAI](openai-api-basics.md)・[Anthropic](anthropic-api-basics.md)・[Google Gemini](google-gemini-api-basics.md))を読んでも、いざ「うちはどれを使うべきか」「複数ベンダーを併用するときの見積もりはどう揃えるか」を考えるときに、三社を並べた一枚の判断材料が欲しくなる。本ページはその横断比較に特化し、個々のAPIの仕組み自体は各社ページに委ねる。

## 仕組み・背景

3社とも「エンドユーザー向けチャットサブスク」と「開発者向けAPI(従量課金)」が別契約である点は共通(詳細は各社ページ)。API自体の構造も収斂しつつある。

- **単一のチャット系エンドポイント**にmessages/contentsの配列を渡し、応答を受け取る
- **入力より出力のほうがトークン単価が高い**(目安3〜6倍)
- **プロンプトキャッシュ**(直前と同じ前提文の再利用)で入力コストを9割前後削減できる
- **Batch API**(非同期処理)で通常の約50%引き
- **外部関数呼び出し**(OpenAI: Function Calling / Anthropic: Tool Use / Google: Function Calling)
- 最新の推論(思考)系モデルは、回答の前に内部で「考える」過程もトークンとして消費し、多くの場合これも出力課金の対象になる

一方で、認証方式・バージョン管理・モデルの命名規則・料金の刻み方は各社バラバラで、この「バラバラな部分」が横断比較の主眼になる。

## 使いどころ・使い分け

| 判断軸 | 向いている選択 |
|---|---|
| すでに社内でOpenAIのエコシステム(ChatGPT Enterprise、Azure OpenAI等)を使っている | OpenAI API(運用ノウハウ・請求経路を一本化しやすい) |
| コーディング支援・エージェント的な長時間タスクの精度を最優先したい | Anthropic API(Claude Opus 5 / Claude Fable 5 が強い領域) |
| Googleのエコシステム(GAS、スプレッドシート、Google Cloud)と密接に連携したい、または低コストで大量処理したい | Google Gemini API(GASとの親和性、無料枠、Flash-Liteの安さ) |
| 100万トークン級の長い資料をまるごと読ませたい | 3社とも主力モデルが100万トークン級に対応(後述の比較表を参照。ただしGeminiは20万トークン超で単価が上がる2段階制のモデルもある) |
| 組み込みのWeb検索機能をそのまま使いたい | Google Gemini API(Grounding with Google Search)が最も手軽。OpenAI・Anthropicも同等機能はあるが別途ツール構成が必要 |
| 特定ベンダーへのロックインを避けたい・障害時に切り替えたい | 3社ともMessages/Chat系の考え方は似ているため、抽象化レイヤー(LangChain、Vercel AI SDK等)やDify・n8nなどのノーコード基盤を挟んでおくと切り替えコストを下げられる |
| 予算上限を厳密に管理したい | 3社とも月間支出上限・レート制限の設定機能を持つが、Google Cloudアカウントは前払い請求設定が必須化されている点に注意(後述) |

**使わない方がよい場面**: 単発のちょっとした質問・文章生成なら、わざわざAPIキーを発行せずChatGPT/Claude.ai/Gemini.appのチャット画面で十分。API契約が必要になるのは「システムに組み込む」「大量処理する」「アプリ化する」段階から。

## 実務での使い方

### 横断比較表(2026年7月30日時点)

| 項目 | OpenAI API | Anthropic API(Claude) | Google Gemini API |
|---|---|---|---|
| 管理画面 | platform.openai.com | platform.claude.com | aistudio.google.com(企業向けはGemini Enterprise Agent Platform、旧Vertex AI) |
| 認証ヘッダー | `Authorization: Bearer <キー>` | `x-api-key: <キー>` | `x-goog-api-key: <キー>`(または非推奨のURLクエリ`?key=`) |
| APIバージョン指定 | 明示的なバージョンヘッダー不要 | `anthropic-version`ヘッダーが必須(SDK利用時は自動付与) | 不要(エンドポイントパスに`v1beta`等が組み込み) |
| 中核エンドポイント | `/v1/chat/completions` または `/v1/responses` | `/v1/messages` | `/v1beta/models/{model}:generateContent` |
| モデル階層(現行ラインナップ) | Sol(最上位)/ Terra(バランス)/ Luna(高速・低コスト) | Fable 5(最上位)/ Opus 5(高性能)/ Sonnet 5(バランス・主力)/ Haiku 4.5(軽量) | Pro(最上位、プレビュー)/ Flash(バランス)/ Flash-Lite(軽量) |
| 代表的なモデルID(API指定文字列) | `gpt-5.6-sol` / `gpt-5.6-terra` / `gpt-5.6-luna`(裸の`gpt-5.6`はSolへのエイリアス) | `claude-fable-5` / `claude-opus-5` / `claude-sonnet-5` / `claude-haiku-4-5` | `gemini-3.1-pro-preview` / `gemini-3.6-flash` / `gemini-3.5-flash-lite` |
| 料金(100万トークンあたり、入力/出力、目安) | Sol $5.00/$30.00、Terra $2.50/$15.00、Luna $1.00/$6.00 | Fable 5 $10/$50、Opus 5 $5/$25、Sonnet 5 $2/$10(2026年8月31日まで導入価格、以降$3/$15)、Haiku 4.5 $1/$5 | Pro(20万トークンまで)$2/$12(超過分は$4/$18)、Flash $1.50/$7.50、Flash-Lite $0.30/$2.50 |
| コンテキストウィンドウ(主力モデル) | 100万トークン(全ティア共通)、最大出力128,000トークン | 100万トークン(Fable 5・Opus 5・Sonnet 5)、Haiku 4.5は20万トークン。最大出力128,000トークン(Haiku 4.5は64,000) | 100万トークン(Flash・Flash-Lite・Pro系) |
| プロンプトキャッシュ | 自動適用、キャッシュ読み取りは通常の約1割の価格 | Prompt Caching(自動または明示指定)、読み取りは約1割の価格。書き込みは5分キャッシュで1.25倍、1時間キャッシュで2倍 | Context Caching、読み取りは約1割の価格。ただし別途ストレージ課金あり(目安: Flash系100万トークン・1時間あたり$1程度) |
| Batch API割引 | 約50%引き | 約50%引き | 約50%引き |
| 組み込みWeb検索 | 別途ツール構成が必要 | 別途ツール構成が必要(検索1,000回あたり$10) | Grounding with Google Search(組み込み、検索クエリ単位課金) |
| モデル命名の考え方 | 日付なしのエイリアス(`gpt-5.6-sol`等)。旧o-series(o1/o3/o4-mini)は順次廃止、Assistants APIも廃止予定 | 基本は日付なしエイリアス(`claude-opus-5`等)。より古いモデルは日付付きスナップショットID(例: `claude-haiku-4-5-20251001`)も残る | バージョン番号そのものがモデルID(`gemini-3.6-flash`)。プレビュー版には`-preview`サフィックスが付く |
| 無料枠 | 基本的になし | 基本的になし | AI Studio自体の利用は常に無料、Flash/Flash-Liteは無料枠あり(Pro系は2026年4月以降有料専用) |

**料金・モデル名の変更頻度に関する注記**: この表の数値・モデルIDは2026年7月30日時点のWeb検索による裏取りに基づく。3社ともモデル世代交代が数か月単位で起きており(直近ではAnthropicが2026年7月24日にClaude Opus 5を、Googleが2026年7月21日にGemini 3.6 FlashとGemini 3.5 Flash-Liteをリリース)、本文の数値をそのまま社内資料や記事に転記せず、必ず各社の公式Pricingページで最終確認すること。

### 認証まわりの最小コード例(横並び)

同じ「1文で自己紹介させる」リクエストを3社で書くと、ヘッダー名とボディ構造の違いが分かりやすい。

**OpenAI API(curl)**

```bash
curl https://api.openai.com/v1/responses \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-terra",
    "input": "あなたは何ができるAIか、1文で自己紹介して"
  }'
```

**Anthropic API(curl)**

```bash
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{
    "model": "claude-sonnet-5",
    "max_tokens": 200,
    "messages": [
      {"role": "user", "content": "あなたは何ができるAIか、1文で自己紹介して"}
    ]
  }'
```

**Google Gemini API(curl)**

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.6-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {"parts": [{"text": "あなたは何ができるAIか、1文で自己紹介して"}]}
    ]
  }'
```

違いをまとめると:

| 違いのポイント | OpenAI | Anthropic | Google |
|---|---|---|---|
| 認証ヘッダー名 | `Authorization: Bearer` | `x-api-key` | `x-goog-api-key` |
| APIバージョン明示 | 不要 | `anthropic-version`が必須 | 不要 |
| システムプロンプトの渡し方 | `input`/`messages`内に`role: "system"` | `messages`とは別の独立した`system`パラメータ | 別パラメータ`system_instruction`(任意) |
| 会話履歴の呼び名 | `input`(Responses API)または`messages`(Chat Completions) | `messages` | `contents` |

### 決め方のフローチャート(意思決定材料)

1. **すでに使っているノーコード基盤・SaaSが対応しているか確認する** — Dify・n8n・Zapier・Makeなどは3社ともコネクタを用意していることが多いため、まずは既存ツールの対応状況で決めてよい
2. **コーディング・複雑な業務判断が中心なら Anthropic(Claude Opus 5 / Sonnet 5)を優先候補にする**
3. **大量・高頻度・低コストの定型処理(分類・要約・タグ付け)なら Luna / Haiku 4.5 / Flash-Lite のような軽量ティアを比較する**(いずれも100万トークンあたり$1前後〜)
4. **Googleエコシステム(GAS、スプレッドシート、Google Workspace)との連携が主目的なら Gemini API を優先する**
5. **最終的にはPoC(概念実証)で同一プロンプト・同一データセットを3社に投げ、精度・速度・コストを実測してから本番採用を決める**(ベンチマークの数字は鵜呑みにせず、自社データでの再現性を確認する)

## 注意点・よくある誤解

- **料金表は「今日時点」でしか正しくない**: 3社とも数か月おきにモデル世代・価格体系が変わる。本ページの数値も執筆時点のスナップショットであり、記事や見積もりに転記する前に必ず各社公式ページを再確認する。
- **トークンの数え方はモデルごとに異なる**: 同じ日本語・英語の文章でも、モデルが採用するトークナイザーによってトークン数が変わる(例: Anthropicは新世代モデルで旧世代比おおよそ3割増)。単価だけを比較して「安い/高い」と早合点しない。
- **「見えない出力トークン」の存在**: Gemini・Claude・GPTの推論(思考)系モデルは、回答文の裏で「思考トークン」を消費しており、これも出力課金の対象になることが多い。想定より請求額が大きい場合、まずこの見えないトークンを疑う。
- **キャッシュ割引は「頻繁に同じ前提文を使う」場合にのみ効く**: 毎回内容が変わるプロンプトにキャッシュを設定しても効果はなく、むしろキャッシュ書き込み分の割高な料金だけがかかる。長いシステムプロンプト・マニュアルを繰り返し参照させる用途に限って設定する。
- **APIキーの管理と利用上限設定は必須**: 3社ともキーの紛失・漏洩や、バグによる無限ループでの高額請求リスクがある。発行直後に月間支出上限・レート制限を必ず設定する。
- **地域・データ取り扱いポリシーの違い**: 企業導入でデータ保護要件が厳しい場合、Anthropic APIならBedrock/Google Cloud経由、Google GeminiならGemini Enterprise Agent Platform(旧Vertex AI)経由など、標準の開発者向けAPIとは別の「企業向け入口」を検討する必要がある。
- **1社用に書いたコードはそのまま流用できない**: 認証ヘッダー名・エンドポイント・パラメータ名が異なるため、片方のAPI用SDKコードをコピーして単純に置き換えるだけでは動かない。抽象化レイヤーを挟むか、切り替え時は各社の公式クイックスタートで書き直すのが安全。

## 最初の一歩

同じ1問(例:「この文章を3行で要約して」)を、OpenAI・Anthropic・Googleの3社それぞれの無料または低コストなモデル(Luna・Haiku 4.5・Flash-Lite)にcurlで投げ比べてみる。認証ヘッダーの違いとレスポンス構造の違いを実際に手を動かして体感するのが、横断比較を頭に入れる一番の近道。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)
- [Anthropic API(Claude API)の基本](anthropic-api-basics.md)
- [Google Gemini APIの基本](google-gemini-api-basics.md)
- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [バッチ処理(Batch API)の基本](batch-api-basics.md)

## 更新履歴

### 2026-07-30: 初版執筆
- **内容**: OpenAI・Anthropic・Google Gemini APIを認証方式・料金・コンテキストウィンドウ・キャッシュ・モデル命名の観点で横断比較する表と、認証まわりの最小コード例、選び方のフローチャートを新規執筆。2026年7月24日リリースのClaude Opus 5、同7月21日リリースのGemini 3.6 Flash/Gemini 3.5 Flash-Liteなど直近の変更を反映
- **出典**: [OpenAI: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)、[OpenAI: GPT-5.6 announcement](https://openai.com/index/gpt-5-6/)、[Axios: Anthropic releases new model, Opus 5](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5)、[TechCrunch: Anthropic launches Opus 5](https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/)、[Google Blog: Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)、[9to5Google: Google launches Gemini 3.6 Flash and 3.5 Flash-Lite](https://9to5google.com/2026/07/21/gemini-3-6-flash-launch/)、[BenchLM.ai: OpenAI API Pricing (July 2026)](https://benchlm.ai/openai/api-pricing)、[BenchLM.ai: Anthropic API Pricing (July 2026)](https://benchlm.ai/anthropic/api-pricing)、[BenchLM.ai: Gemini API Pricing (July 2026)](https://benchlm.ai/google/api-pricing)、[Claude Platform Docs: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
