---
title: Google Gemini APIの基本
part: 9
chapter: 第1章 LLM APIの基礎
tags: [Gemini API, Google AI Studio, Vertex AI, APIキー, LLM API]
created: 2026-07-06
updated: 2026-07-06
---

# Google Gemini APIの基本

## これは何か

Gemini.app(gemini.google.com)やGoogle AI Pro/Ultraに課金していれば、DifyやGASなど他のツールからもGeminiを自由に呼び出せる、と誤解している人は多い。実際にはGemini.appのサブスク(Free/Google AI Pro/Ultra)とGemini API(従量課金)は完全に別契約であり、社内システムやノーコードツールにGeminiを組み込みたい場合はAPIを別途利用する必要がある。この関係は[OpenAI APIの基本](openai-api-basics.md)・[Anthropic API(Claude API)の基本](anthropic-api-basics.md)で説明したChatGPT/Claude.aiとの構図と同じだが、Geminiには「無料で試せる開発者用サンドボックス」であるGoogle AI Studioと、企業向けに管轄が分かれるVertex AI経由という2つの入口がある点が特徴的である。

## 仕組み・背景

- **Gemini.app**: gemini.google.com上でチャット形式でGeminiと対話する、エンドユーザー向けの製品。Free/Google AI Pro/Ultraなどの月額サブスクリプションで提供される。詳細は[Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)を参照。
- **Gemini API(Google AI Studio経由)**: 開発者向けのインターフェースで、個人開発者・スタートアップ・プロトタイピング向けの「最速で試せる」入口。aistudio.google.com上でAPIキーを発行し、`generativelanguage.googleapis.com`のエンドポイントにHTTPリクエストを送ってGeminiを呼び出す。Gemini.appのサブスク契約とは別会計で、Google AI Pro/Ultraに入っていてもAPI利用料は割引されない。逆にGemini.appを契約していなくてもGoogleアカウントさえあればAPIのみ無料枠で試せる。
- **Gemini API(Vertex AI経由)**: 同じGeminiモデルを、Google Cloudのプロジェクト・IAM(権限管理)・データ居住地(リージョン)制御・SLA(サービス品質保証)付きで呼び出す企業向けの入口。2026年4月のGoogle Cloud Next 26で、Vertex AIの生成AI・エージェント関連機能は「Gemini Enterprise Agent Platform」という名称に整理・拡張されると発表されたが、Gemini APIそのものの呼び出し方(エンドポイント・SDK)は後方互換で維持されている。社内のガバナンス要件(データを学習に使わせない、リージョンを固定する等)が絡む本番導入ではこちらが選ばれることが多い。

料金は「トークン(文章を分割した単位)」ごとの従量課金で、入力(プロンプト)側より出力(生成結果)側の単価が高く設定されている。モデルのグレード(後述のPro/Flash/Flash-Lite)によっても単価は大きく変わる。

## 使いどころ・使い分け

| やりたいこと | 向いている入口 |
|---|---|
| 自分でチャット画面から質問・相談したい | Gemini.app(Free/Google AI Pro/Ultra) |
| 個人開発・プロトタイプで手早くAPIを試したい | Gemini API(Google AI Studio、無料枠あり) |
| 社内システムやスプレッドシートにGeminiの機能を組み込みたい | Gemini API(Google AI Studio、小〜中規模ならこれで十分) |
| データ居住地・IAM・SLAなど企業のガバナンス要件を満たしたい | Gemini API(Vertex AI / Gemini Enterprise Agent Platform経由) |
| Difyやn8nなどノーコードツールでAIアプリを作りたい | Gemini API(ノーコードツール側にAPIキーを設定) |
| 大量のデータを一括で要約・分類したい(即時応答不要) | Gemini APIのBatch API(通常の約50%引で処理できる) |
| 100万トークン級の長大な資料・複数ドキュメントをまるごと読ませたい | Gemini 3 Pro/Flashなど長いコンテキストウィンドウに対応したモデル |
| 最新のWeb情報を踏まえて回答させたい | Grounding with Google Search機能を有効化した呼び出し |

## 実務での使い方

### APIキーの取得手順(Google AI Studio)

1. aistudio.google.com にアクセスし、Gemini.appと同じGoogleアカウントでログインする
2. 左サイドバーの「Get API key」、または直接 aistudio.google.com/app/apikey にアクセス
3. 「Create API key」をクリックし、キーを紐づけるGoogle Cloudプロジェクトを選択する(課金設定がなくても発行でき、無料枠だけで試すこともできる)
4. 生成されたキーをコピーして安全な場所に保管する(平文で共有しない)
5. 本番利用に進む場合は、Google Cloud側で「Billing」を有効化し、想定外の高額請求を防ぐための予算アラート・クォータ設定をしておく

### 最小のコード例(Generative Language API)

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash:generateContent" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {"parts": [{"text": "この請求書PDFの合計金額を1文で要約して"}]}
    ]
  }'
```

OpenAI API(`Authorization: Bearer`)やAnthropic API(`x-api-key`ヘッダー)と異なり、Gemini APIは`x-goog-api-key`ヘッダー、またはURLクエリパラメータ`?key=`でキーを渡す方式に対応している。クエリパラメータ方式はアクセスログやブラウザ履歴にキーが残るリスクがあるため、本番環境ではヘッダー渡しを使うのが安全である。

### モデル指定の考え方(Pro / Flash / Flash-Lite)

2026年7月時点の主力ラインナップはおおむね3グレードに分かれる(モデル名は`gemini-3-pro`のような世代表記で頻繁に更新されるため、必ず ai.google.dev/gemini-api/docs/models で最新のモデルIDを確認すること)。

| グレード | 位置づけ | 向いている用途 |
|---|---|---|
| Pro(例: Gemini 3 Pro) | 最上位。複雑な推論・高精度な多段階タスクに強い | 難しい分析・コード生成・専門的な質問応答 |
| Flash(例: Gemini 3 Flash/3.5 Flash) | バランス型。速度とコストと性能の妥協点 | チャットボット、要約、一般的な業務アプリのバックエンド |
| Flash-Lite(例: Gemini 3.1 Flash-Lite) | 最軽量・最安・低レイテンシ | 高頻度・大量呼び出しの分類・タグ付けなどコスト重視の処理 |

迷ったら「まずFlashで動かし、精度が足りない部分だけPro、コストが問題になった部分だけFlash-Liteに切り替える」という段階的な選び方が実務的である。

### 料金体系のイメージ(2026年7月時点、モデル名・価格は変更が非常に頻繁なため必ず公式ページ ai.google.dev/gemini-api/docs/pricing で最終確認すること)

- Flash-Liteが最安(入力・出力ともに100万トークンあたり1〜2ドル台のオーダー)、Flashはその数倍、Proはさらに数倍という価格差が目安
- 出力トークンは入力トークンより高く設定されており、モデルによって3〜8倍程度の差がある
- Context Caching(直前と同じ長い前提文の再利用)を使うとキャッシュ済み入力は通常の入力より大幅に割引される(目安9割引程度)
- Batch API(非同期処理)は同期呼び出しに比べて約50%安い
- **無料枠あり**: Google AI Studio自体の利用(ブラウザでの試用)は常に無料。API経由でもFlash/Flash-Liteモデルには無料枠(リクエスト数・トークン数の上限付き)が用意されている。2026年4月以降、Proモデルは無料枠の対象から外れ有料専用になった
- 無料枠で送った入力・出力はGoogleのモデル改善に利用される場合がある。データを学習に使われたくない場合は有料枠、またはVertex AI経由(Vertex AI/Gemini Enterprise Agent Platform)を使う

### ノーコードツール・業務システムとの連携例

- **Dify**: モデルプロバイダーの設定画面で「Google Gemini」を選び、Google AI StudioのAPIキーを入力するだけで、Dify上に作ったチャットボットやワークフローからGeminiを呼び出せる
- **GAS(Google Apps Script)**: `UrlFetchApp`で`generativelanguage.googleapis.com`にHTTPリクエストを送る形で、スプレッドシートの内容を要約・分類するといった社内自動化によく使われる。同じGoogleエコシステムのため、GASとの組み合わせは特に相性が良い
- **n8n / Zapier / Make**: 「Google Gemini」用の専用ノード・アクションが用意されており、他システムとの連携・自動実行のトリガーとして組み合わせて使われる

### 代表的な機能(名前と一言メモ)

- **Function Calling(ツール呼び出し)**: モデルに外部の関数・API・DBクエリを呼び出させる仕組み。OpenAIの「Function Calling」、Anthropicの「Tool Use」に相当する
- **Structured Outputs(構造化出力・JSON mode)**: 開発者が指定したJSON Schemaに厳密に一致する形式で出力させる機能。データ抽出・分類・エージェントのツール入力生成などに使う
- **Grounding with Google Search**: モデルの回答に最新のGoogle検索結果を組み込む、組み込みのWeb検索ツール。他社APIでは別途Web検索ツールを自前で用意する必要があるのに対し、Geminiは公式機能として提供している点が特徴
- **Context Caching**: 長いシステムプロンプトやマニュアルなど繰り返し使う前提文をキャッシュし、2回目以降の呼び出しコストを大幅に下げる仕組み(OpenAI/Anthropicのプロンプトキャッシュに相当)
- **Batch API**: 大量のリクエストをまとめて非同期送信し、通常より安く(約半額)処理する仕組み
- **長いコンテキストウィンドウ**: Pro/Flash系モデルは標準で100万トークン級の入力に対応しており、複数の長文資料をまるごと読ませる用途で強みを持つ

### OpenAI API・Anthropic APIとの比較表

| 項目 | OpenAI API | Anthropic API(Claude) | Google Gemini API(AI Studio) |
|---|---|---|---|
| 管理画面 | platform.openai.com | platform.claude.com | aistudio.google.com |
| 認証方法 | `Authorization: Bearer <キー>` | `x-api-key: <キー>` | `x-goog-api-key: <キー>`(またはURLクエリ`?key=`) |
| 中核エンドポイント | `/v1/chat/completions` または `/v1/responses` | `/v1/messages` | `/v1beta/models/{model}:generateContent` |
| モデルの呼び分け軸 | GPT系のグレード | Opus(最上位)/Sonnet(バランス)/Haiku(軽量) | Pro(最上位)/Flash(バランス)/Flash-Lite(軽量) |
| 無料枠 | 基本的になし(要クレジット購入) | 基本的になし | AI Studioの利用自体は常に無料、APIもFlash/Flash-Liteに無料枠あり(2026年4月以降Proは有料専用) |
| 外部関数呼び出し | Function Calling | Tool Use | Function Calling |
| JSON/構造化出力 | Structured Outputs | ツール指定によるJSON強制等 | Structured Outputs(response_schema) |
| 組み込みWeb検索 | 別途ツール構成が必要 | 別途ツール構成が必要 | Grounding with Google Search(組み込み機能) |
| キャッシュ割引 | プロンプトキャッシュ(自動適用) | Prompt Caching(目安9割引) | Context Caching(目安9割引) |
| 非同期・低価格処理 | Batch API(約50%割引) | Batch API(約50%割引) | Batch API(約50%割引) |
| 長文コンテキストの目安 | モデルにより拡張 | 一部モデルで100万トークン | 主力モデルで標準100万トークン級 |
| 企業向け入口 | Azure OpenAI Service等 | Amazon Bedrock/Google Vertex AI経由の提供等 | Vertex AI(Gemini Enterprise Agent Platform)、IAM/データ居住地/SLA対応 |

大枠の思想(トークン従量課金、Batch APIでの割引、Function Calling/Tool Useの考え方)は3社ともよく似ているが、認証ヘッダー・エンドポイント名・パラメータの細部が異なるため、1社用に書いたコードはそのまま他社に流用できない点に注意。

## 注意点・よくある誤解

- **Gemini.app課金とAPI課金は別会計**: Google AI Pro/Ultraの月額料金はAPI利用料の割引にはならない。混同して「なぜ別料金が発生するのか」と驚かないよう、契約前に整理しておく。
- **無料枠のデータはモデル改善に使われる可能性がある**: 個人情報や機密情報を含むデータを無料枠で送ると、Googleの学習データとして利用され得る。社内の機密文書を扱う場合は有料枠、またはデータを学習に使わないVertex AI経由の利用を検討する。
- **2026年4月以降、Proモデルは無料枠の対象外**: 以前は無料枠でPro系モデルも一定回数まで試せたが、現在はFlash/Flash-Liteのみが無料枠の対象で、Pro系は有料契約が必須になっている。
- **モデル名・世代の入れ替わりが非常に速い**: Gemini 3、3.1、3.5のように短期間で新世代が投入され、旧世代の料金・提供状況も変わる。記事や社内資料に具体的なモデル名・価格を書く場合は、必ず公式サイトの最新情報を都度確認する。
- **URLクエリでのAPIキー渡しはログに残るリスクがある**: `?key=`方式は手軽だが、アクセスログやブラウザ履歴にキーが残る可能性がある。本番環境では`x-goog-api-key`ヘッダーでの送信、またはサーバー側でのキー管理を徹底する。
- **「Vertex AI」と「Gemini Enterprise Agent Platform」の名称混乱**: 2026年4月のリブランド発表以降、企業向け入口の呼称が過渡期にあり、資料によって表記が揺れる。API呼び出し自体は後方互換のため、名称よりも「IAM・データ居住地・SLAが必要ならこちらの入口」という判断軸で捉えておくとよい。

## 最初の一歩

自社でDifyやGASなどのノーコード連携を検討しているなら、まずaistudio.google.comでAPIキーを1つ発行し、無料枠のFlash-LiteモデルにcurlまたはPostmanで1回リクエストを送ってみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)
- [Anthropic API(Claude API)の基本](anthropic-api-basics.md)
- [Function Calling(Tool Use)の基本](function-calling-basics.md)
- [Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: Gemini.appとGemini APIの違い(Google AI Studio経由・Vertex AI経由)、APIキー取得手順、モデル指定の考え方(Pro/Flash/Flash-Lite)、料金体系(無料枠・従量課金)、Function Calling/Structured Outputs/Grounding with Google Search/Context Caching/Batch APIの概要、OpenAI API・Anthropic APIとの3社比較表を整理
- **出典**: [Google AI for Developers: Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing)、[Google AI for Developers: Using Gemini API keys](https://ai.google.dev/gemini-api/docs/api-key)、[Google AI for Developers: Rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)、[Google AI for Developers: Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)、[Google AI for Developers: Structured outputs](https://ai.google.dev/gemini-api/docs/structured-output)、[Google Cloud: Gemini Enterprise Agent Platform(旧Vertex AI)](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- **注記**: モデル名・料金は改定が非常に頻繁なため、本文の数値は目安として扱い、最新の単価・モデルIDは必ず [Gemini API公式Pricingページ](https://ai.google.dev/gemini-api/docs/pricing) と [Modelsページ](https://ai.google.dev/gemini-api/docs/models) で確認すること
