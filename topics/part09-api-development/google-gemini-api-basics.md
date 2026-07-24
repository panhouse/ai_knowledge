---
title: Google Gemini APIの基本
part: 9
chapter: 第1章 LLM APIの基礎
tags: [Gemini API, Google AI Studio, Vertex AI, Gemini Enterprise Agent Platform, APIキー, LLM API]
created: 2026-07-06
updated: 2026-07-20
---

# Google Gemini APIの基本

## これは何か

Gemini.app(gemini.google.com)やGoogle AI Pro/Ultraに課金していれば、DifyやGASなど他のツールからもGeminiを自由に呼び出せる、と誤解している人は多い。実際にはGemini.appのサブスク(Free/Google AI Pro/Ultra)とGemini API(従量課金)は完全に別契約であり、社内システムやノーコードツールにGeminiを組み込みたい場合はAPIを別途利用する必要がある。この関係は[OpenAI APIの基本](openai-api-basics.md)・[Anthropic API(Claude API)の基本](anthropic-api-basics.md)で説明したChatGPT/Claude.aiとの構図と同じだが、Geminiには「無料で試せる開発者用サンドボックス」であるGoogle AI Studioと、企業向けに管轄が分かれるGemini Enterprise Agent Platform(旧Vertex AI)経由という2つの入口がある点が特徴的である。

## 仕組み・背景

- **Gemini.app**: gemini.google.com上でチャット形式でGeminiと対話する、エンドユーザー向けの製品。Free/Google AI Pro/Ultraなどの月額サブスクリプションで提供される。詳細は[Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)を参照。
- **Gemini API(Google AI Studio経由)**: 開発者向けのインターフェースで、個人開発者・スタートアップ・プロトタイピング向けの「最速で試せる」入口。aistudio.google.com上でAPIキーを発行し、`generativelanguage.googleapis.com`のエンドポイントにHTTPリクエストを送ってGeminiを呼び出す。Gemini.appのサブスク契約とは別会計で、Google AI Pro/Ultraに入っていてもAPI利用料は割引されない。逆にGemini.appを契約していなくてもGoogleアカウントさえあればAPIのみ無料枠で試せる。
- **Gemini API(Gemini Enterprise Agent Platform経由)**: 同じGeminiモデルを、Google Cloudのプロジェクト・IAM(権限管理)・データ居住地(リージョン)制御・SLA(サービス品質保証)付きで呼び出す企業向けの入口。従来「Vertex AI」と呼ばれていたが、2026年4月23日のGoogle Cloud Next 26でAgentspace等を統合し「Gemini Enterprise Agent Platform」への改称・再編が発表され、同年5月末までに移行が完了した。Model Garden・AutoML・Model Registry・Endpoints・Pipelinesといった旧Vertex AIの機能群は、この「エージェント基盤」の中の一部として位置づけ直されている。呼称は変わったが、Gemini APIそのものの呼び出し方(エンドポイント・SDK)は後方互換で維持されているため、既存コードの書き換えは不要である。社内のガバナンス要件(データを学習に使わせない、リージョンを固定する等)が絡む本番導入ではこちらが選ばれることが多い。

料金は「トークン(文章を分割した単位)」ごとの従量課金で、入力(プロンプト)側より出力(生成結果)側の単価が高く設定されている。モデルのグレード(後述のPro/Flash/Flash-Lite)によっても単価は大きく変わる。加えて、Gemini 3世代以降のモデルは回答前に内部で「思考(Thinking)」する推論型モデルであり、この思考過程もトークンとして生成され、ユーザーには見えない部分も含めて出力トークン料金で課金される点に注意が必要である(詳細は後述)。

## 使いどころ・使い分け

| やりたいこと | 向いている入口 |
|---|---|
| 自分でチャット画面から質問・相談したい | Gemini.app(Free/Google AI Pro/Ultra) |
| 個人開発・プロトタイプで手早くAPIを試したい | Gemini API(Google AI Studio、無料枠あり) |
| 社内システムやスプレッドシートにGeminiの機能を組み込みたい | Gemini API(Google AI Studio、小〜中規模ならこれで十分) |
| データ居住地・IAM・SLAなど企業のガバナンス要件を満たしたい | Gemini API(Gemini Enterprise Agent Platform、旧Vertex AI経由) |
| Difyやn8nなどノーコードツールでAIアプリを作りたい | Gemini API(ノーコードツール側にAPIキーを設定) |
| 大量のデータを一括で要約・分類したい(即時応答不要) | Gemini APIのBatch API(通常の約50%引で処理できる) |
| 100万トークン級の長大な資料・複数ドキュメントをまるごと読ませたい | Gemini 3.5 Flash/Gemini 3.1 Proなど長いコンテキストウィンドウに対応したモデル |
| 最新のWeb情報を踏まえて回答させたい | Grounding with Google Search機能を有効化した呼び出し(2026年以降は検索クエリ単位の課金に変更) |

## 実務での使い方

### APIキーの取得手順(Google AI Studio)

1. aistudio.google.com にアクセスし、Gemini.appと同じGoogleアカウントでログインする
2. 左サイドバーの「Get API key」、または直接 aistudio.google.com/app/apikey にアクセス
3. 「Create API key」をクリックし、キーを紐づけるGoogle Cloudプロジェクトを選択する(無料枠だけで試す場合は課金設定なしでも発行できる)
4. 生成されたキーをコピーして安全な場所に保管する(平文で共有しない)
5. 本番利用に進む場合は、Google Cloud側で「Billing」を有効化し、想定外の高額請求を防ぐための予算アラート・クォータ設定をしておく。2026年4月1日以降、新規のGoogle Cloudアカウントはあらかじめ前払い(プリペイド)の請求設定を済ませないとGemini APIの有料利用に進めない仕様に変更されているため、初めて課金設定をする場合はこの点を確認しておく

### 最小のコード例(Generative Language API)

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash:generateContent" \
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

2026年7月時点の主力ラインナップはおおむね3グレードに分かれる(モデル名は頻繁に更新されるため、必ず ai.google.dev/gemini-api/docs/models で最新のモデルIDを確認すること)。

| グレード | 位置づけ | 向いている用途 |
|---|---|---|
| Pro(Gemini 3.1 Pro、プレビュー) | 現行の最上位。複雑な推論・高精度な多段階タスクに強い | 難しい分析・コード生成・専門的な質問応答 |
| Flash(Gemini 3.5 Flash、GA) | バランス型。2026年5月のGoogle I/Oで刷新され、コーディング・エージェント系ベンチマークでは旧Proを上回る場面もある | チャットボット、要約、一般的な業務アプリのバックエンド、エージェント・コーディング用途 |
| Flash-Lite(Gemini 3.1 Flash-Lite) | 最軽量・最安・低レイテンシ | 高頻度・大量呼び出しの分類・タグ付けなどコスト重視の処理 |

2026年7月20日時点、次世代の「Gemini 3.5 Pro」(2百万トークン級のコンテキストウィンドウや「Deep Think」モードが噂される)はGoogle I/O 2026で予告されたものの、リリースが複数回延期されており、限定プレビュー以外では正式提供されていない。社内資料に反映する際は「Gemini 3.5 Proは執筆時点で未GA、仕様・価格は未確定」と明記し、憶測で断定しないこと。また旧世代のGemini 3 Pro/Gemini 3 Flash、およびさらに旧いGemini 2.5系(Pro/Flash/Flash-Lite)は新規開発には非推奨で、Gemini 2.5系はGemini Enterprise Agent Platform上で2026年10月16日以降(Gemini 3系のGA状況次第でさらに延びる可能性あり)順次廃止が予告されている。既存システムで旧モデルIDを指定している場合は、早めにGemini 3.1 Pro/Gemini 3.5 Flashへの切り替えを検討する。

迷ったら「まずFlashで動かし、精度が足りない部分だけPro、コストが問題になった部分だけFlash-Liteに切り替える」という段階的な選び方が実務的である。

### 料金体系のイメージ(2026年7月時点、モデル名・価格は変更が非常に頻繁なため必ず公式ページ ai.google.dev/gemini-api/docs/pricing で最終確認すること)

- **Gemini 3.5 Flash**: 入力100万トークンあたり約1.5ドル、出力約9ドル。キャッシュ済み入力は約0.15ドル
- **Gemini 3.1 Pro(プレビュー)**: 20万トークンまでは入力約2ドル/出力約12ドル、20万トークンを超える長いプロンプトは入力約4ドル/出力約18ドルに単価が上がる2段階制
- **Gemini 3.1 Flash-Lite**: 入力約0.25ドル/出力約1.5ドルと最安クラス
- **思考(Thinking)トークンも出力課金の対象**: Gemini 3世代の推論モデルは、回答を組み立てる前に内部で「思考」を行い、そのトークンも(ユーザーに見えない場合でも)出力トークン料金で課金される。単純なタスクでは数%程度だが、複雑な数学・コーディングタスクでは思考トークンが総コストの3割前後を占めることもあり、想定より請求額が大きくなる典型的な原因になっている
- **Context Caching(直前と同じ長い前提文の再利用)**: キャッシュ済み入力は通常の入力より大幅に割引される(目安9割引程度。例: Gemini 3.1 Proの入力単価2ドル→キャッシュ利用時0.2ドル)。ただしキャッシュを保持するストレージ自体にも別途課金があり(目安はFlash系で100万トークン・1時間あたり1ドル、Pro系で4.5ドル程度)、短時間しか再利用しないキャッシュはかえって割高になる場合がある
- **Batch API(非同期処理)**: 同期呼び出しに比べて約50%安い(例: Gemini 3.5 Flashは同期の入力1.5ドル/出力9ドルがバッチでは0.75ドル/4.5ドルに)
- **Grounding with Google Search(組み込みWeb検索)**: 2026年以降、Gemini 3系では「検索クエリ数」単位の課金に変更されており、無料クォータを超えると1,000クエリあたり目安14ドル程度。旧Gemini 2.5系は「グラウンディングを使ったプロンプト数」単位(1,000プロンプトあたり目安35ドル程度)で課金方式そのものが異なるため、切り替え時は見積もりの前提を作り直す必要がある
- **無料枠あり(ただし2026年4月に大幅縮小)**: Google AI Studio自体の利用(ブラウザでの試用)は常に無料。API経由でもFlash/Flash-Liteモデルには無料枠(リクエスト数・トークン数の上限付き)が用意されている。一方で2026年4月1日以降、Pro系モデル(Gemini 3.1 Proなど)は無料枠の対象から完全に外れ有料専用になったほか、毎月の利用上限(スペンドキャップ)が必須設定になり、上限に達すると自動的にAPI呼び出しが一時停止する仕組みが導入された
- 無料枠で送った入力・出力はGoogleのモデル改善に利用される場合があり、人手によるレビューが行われることもある。有料枠(課金アカウント経由)ではデータの取り扱い契約が異なり、原則としてモデル学習には使われない。データを学習に使われたくない場合は有料枠、またはGemini Enterprise Agent Platform(旧Vertex AI)経由の利用を検討する

### レート制限(呼び出し回数の上限)の考え方

Gemini APIのレート制限は、RPM(1分あたりのリクエスト数)・TPM(1分あたりのトークン数)・RPD(1日あたりのリクエスト数)の組み合わせで管理され、プロジェクト(APIキー単位ではない)ごとに、これまでの課金アカウントでの累計利用額に応じて自動的に「利用ティア」が上がっていく仕組みになっている。目安として、無料ティアはFlash系で毎分15リクエスト・1日1,500リクエスト程度、初回課金後のTier 1は毎分150〜300リクエスト程度・月間スペンド上限250ドル、累計利用額が一定額(目安100ドル)を超え数日経過するとTier 2に上がり毎分1,000リクエスト超・月間スペンド上限2,000ドル程度まで拡大する。具体的な数値はモデル・時期によって変動するため、Google AI StudioのプロジェクトごとのRate limitsページで自分のプロジェクトの現在値を確認することが最も確実である。

### ノーコードツール・業務システムとの連携例

- **Dify**: モデルプロバイダーの設定画面で「Google Gemini」を選び、Google AI StudioのAPIキーを入力するだけで、Dify上に作ったチャットボットやワークフローからGeminiを呼び出せる
- **GAS(Google Apps Script)**: `UrlFetchApp`で`generativelanguage.googleapis.com`にHTTPリクエストを送る形で、スプレッドシートの内容を要約・分類するといった社内自動化によく使われる。同じGoogleエコシステムのため、GASとの組み合わせは特に相性が良い
- **n8n / Zapier / Make**: 「Google Gemini」用の専用ノード・アクションが用意されており、他システムとの連携・自動実行のトリガーとして組み合わせて使われる

### 代表的な機能(名前と一言メモ)

- **Function Calling(ツール呼び出し)**: モデルに外部の関数・API・DBクエリを呼び出させる仕組み。OpenAIの「Function Calling」、Anthropicの「Tool Use」に相当する
- **Structured Outputs(構造化出力・JSON mode)**: 開発者が指定したJSON Schemaに厳密に一致する形式で出力させる機能。データ抽出・分類・エージェントのツール入力生成などに使う
- **Grounding with Google Search**: モデルの回答に最新のGoogle検索結果を組み込む、組み込みのWeb検索ツール。他社APIでは別途Web検索ツールを自前で用意する必要があるのに対し、Geminiは公式機能として提供している点が特徴。前述の通り2026年に課金方式が「検索クエリ単位」に変更されている
- **Context Caching**: 長いシステムプロンプトやマニュアルなど繰り返し使う前提文をキャッシュし、2回目以降の呼び出しコストを大幅に下げる仕組み(OpenAI/Anthropicのプロンプトキャッシュに相当)
- **Batch API**: 大量のリクエストをまとめて非同期送信し、通常より安く(約半額)処理する仕組み
- **Thinking(思考モード)**: Gemini 3世代以降で導入された推論機能。回答前に内部で段階的に考え、複雑な問題の精度を上げる一方、思考トークン分も出力課金の対象になる。API側で思考の「深さ」を調整できるモデルもある
- **長いコンテキストウィンドウ**: Gemini 3.5 Flash/Gemini 3.1 Proなど主力モデルは標準で100万トークン級の入力に対応しており、複数の長文資料をまるごと読ませる用途で強みを持つ(2百万トークンへの拡張は次世代のGemini 3.5 Proで噂されているが2026年7月時点で未確定)

### OpenAI API・Anthropic APIとの比較表

| 項目 | OpenAI API | Anthropic API(Claude) | Google Gemini API(AI Studio) |
|---|---|---|---|
| 管理画面 | platform.openai.com | platform.claude.com | aistudio.google.com |
| 認証方法 | `Authorization: Bearer <キー>` | `x-api-key: <キー>` | `x-goog-api-key: <キー>`(またはURLクエリ`?key=`) |
| 中核エンドポイント | `/v1/chat/completions` または `/v1/responses` | `/v1/messages` | `/v1beta/models/{model}:generateContent` |
| モデルの呼び分け軸 | GPT系のグレード | Opus(最上位)/Sonnet(バランス)/Haiku(軽量) | Pro(最上位、Gemini 3.1 Pro)/Flash(バランス、Gemini 3.5 Flash)/Flash-Lite(軽量、Gemini 3.1 Flash-Lite) |
| 無料枠 | 基本的になし(要クレジット購入) | 基本的になし | AI Studioの利用自体は常に無料、APIもFlash/Flash-Liteに無料枠あり(2026年4月以降Proは有料専用、月間スペンドキャップも必須化) |
| 外部関数呼び出し | Function Calling | Tool Use | Function Calling |
| JSON/構造化出力 | Structured Outputs | ツール指定によるJSON強制等 | Structured Outputs(response_schema) |
| 組み込みWeb検索 | 別途ツール構成が必要 | 別途ツール構成が必要 | Grounding with Google Search(組み込み機能、2026年以降クエリ単位課金) |
| キャッシュ割引 | プロンプトキャッシュ(自動適用) | Prompt Caching(目安9割引) | Context Caching(目安9割引、別途ストレージ課金あり) |
| 非同期・低価格処理 | Batch API(約50%割引) | Batch API(約50%割引) | Batch API(約50%割引) |
| 長文コンテキストの目安 | モデルにより拡張 | 一部モデルで100万トークン | 主力モデルで標準100万トークン級 |
| 推論(思考)過程の課金 | モデルにより推論トークンを出力課金 | モデルにより拡張思考(Extended Thinking)を出力課金 | Thinking機能を出力トークンとして課金 |
| 企業向け入口 | Azure OpenAI Service等 | Amazon Bedrock/Google Cloud経由の提供等 | Gemini Enterprise Agent Platform(旧Vertex AI)、IAM/データ居住地/SLA対応 |

大枠の思想(トークン従量課金、Batch APIでの割引、Function Calling/Tool Useの考え方、推論トークンの出力課金化)は3社ともよく似た方向に収斂しつつあるが、認証ヘッダー・エンドポイント名・パラメータの細部が異なるため、1社用に書いたコードはそのまま他社に流用できない点に注意。

## 注意点・よくある誤解

- **Gemini.app課金とAPI課金は別会計**: Google AI Pro/Ultraの月額料金はAPI利用料の割引にはならない。混同して「なぜ別料金が発生するのか」と驚かないよう、契約前に整理しておく。
- **思考(Thinking)トークンが請求額を押し上げる**: Gemini 3世代の推論型モデルは、見えている回答文が短くても、背後で大量の思考トークンを消費していることがある。想定より請求額が大きい場合は、まずこの「見えない出力トークン」を疑う。
- **無料枠のデータはモデル改善に使われる可能性がある**: 個人情報や機密情報を含むデータを無料枠で送ると、Googleの学習データとして利用され得る。社内の機密文書を扱う場合は有料枠、またはデータを学習に使わないGemini Enterprise Agent Platform(旧Vertex AI)経由の利用を検討する。
- **2026年4月以降、Proモデルは無料枠の対象外・月間スペンドキャップが必須**: 以前は無料枠でPro系モデルも一定回数まで試せたが、現在はFlash/Flash-Liteのみが無料枠の対象で、Pro系は有料契約が必須になっている。加えて新規のGoogle Cloudアカウントは前払い請求設定が必要になり、月間の利用上限(スペンドキャップ)設定も必須化された。
- **モデル名・世代の入れ替わりが非常に速い**: 2026年7月時点の現行GAはGemini 3.5 Flash、プレビュー中の現行最上位はGemini 3.1 Proで、旧世代のGemini 3 Pro/Flash・Gemini 2.5系は非推奨〜段階的廃止(Gemini 2.5系はGemini Enterprise Agent Platform上で2026年10月16日以降廃止予定、時期は変動しうる)に向かっている。噂の「Gemini 3.5 Pro」は複数回延期されており、2026年7月20日時点で正式なGA日程・価格は未確定。記事や社内資料に具体的なモデル名・価格を書く場合は、必ず公式サイトの最新情報を都度確認する。
- **URLクエリでのAPIキー渡しはログに残るリスクがある**: `?key=`方式は手軽だが、アクセスログやブラウザ履歴にキーが残る可能性がある。本番環境では`x-goog-api-key`ヘッダーでの送信、またはサーバー側でのキー管理を徹底する。
- **「Vertex AI」と「Gemini Enterprise Agent Platform」の名称混乱**: 2026年4月のリブランド発表・5月末の移行完了以降も、社内資料や過去の検索結果には「Vertex AI」表記が残っていることが多い。API呼び出し自体は後方互換のため、名称よりも「IAM・データ居住地・SLAが必要ならこちらの入口」という判断軸で捉えておくとよい。

## 最初の一歩

自社でDifyやGASなどのノーコード連携を検討しているなら、まずaistudio.google.comでAPIキーを1つ発行し、無料枠のGemini 3.1 Flash-LiteモデルにcurlまたはPostmanで1回リクエストを送ってみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)
- [Anthropic API(Claude API)の基本](anthropic-api-basics.md)
- [Function Calling(Tool Use)の基本](function-calling-basics.md)
- [Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)

## 更新履歴

### 2026-07-20: モデルラインナップ・料金・無料枠・Vertex AI改称を全面最新化
- **内容**: 現行モデルをGemini 3.5 Flash(GA)/Gemini 3.1 Pro(プレビュー)/Gemini 3.1 Flash-Liteに更新し、噂される次世代「Gemini 3.5 Pro」の延期状況と旧世代(Gemini 3 Pro/Flash・Gemini 2.5系)の非推奨・段階的廃止(Gemini Enterprise Agent Platform上で2026年10月16日以降廃止予定)を追記。料金表を2026年7月時点の実額(Flash: 入力1.5ドル/出力9ドル、Pro: 2ドル/12ドル〜4ドル/18ドル、Flash-Lite: 0.25ドル/1.5ドル)に更新し、Gemini 3世代で新たに課金対象となった「思考(Thinking)トークン」、Context Cachingのストレージ課金、Grounding with Google Searchの課金方式変更(プロンプト単位→検索クエリ単位)を新規追記。2026年4月の無料枠縮小(Pro有料化・月間スペンドキャップ必須化・新規アカウントの前払い請求必須化)を反映。「Vertex AI」から「Gemini Enterprise Agent Platform」への改称完了(2026年4月23日発表・5月末移行完了、Agentspace統合)を反映し、レート制限(利用ティア)の節を新設した
- **出典**: [Google Cloud: Gemini Enterprise Agent Platform(旧Vertex AI)](https://cloud.google.com/products/gemini-enterprise-agent-platform)、[Google Cloud: Agent Platform Pricing](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing)、[Google Blog: Gemini 3.5 frontier intelligence with action](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)、[Google Blog: Gemini 3.1 Pro](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-pro/)、[MarkTechPost: Google Introduces Gemini 3.5 Flash at I/O 2026](https://www.marktechpost.com/2026/05/20/google-introduces-gemini-3-5-flash-at-i-o-2026-a-faster-and-cheaper-model-for-ai-agents-and-coding/)、[gcpstudyhub: Google Is Retiring Gemini 2.5 on Agent Platform](https://gcpstudyhub.com/blog/google-is-retiring-gemini-2-5-on-agent-platform-what-you-need-to-know-and-do-before-october-2026)、[gcpstudyhub: Vertex AI Is Now Gemini Enterprise Agent Platform](https://gcpstudyhub.com/blog/vertex-ai-replaced-by-gemini-enterprise-agent-platform)、[BenchLM.ai: Gemini API Pricing (July 2026)](https://benchlm.ai/blog/posts/gemini-api-pricing)
- **注記**: 「Gemini 3.5 Pro」の仕様・価格・GA時期は2026年7月20日時点で未確定情報(複数メディアが延期を報道)であり、公式発表前提の内容ではない。モデル名・料金は改定が非常に頻繁なため、本文の数値は目安として扱い、最新の単価・モデルIDは必ず [Gemini API公式Pricingページ](https://ai.google.dev/gemini-api/docs/pricing) と [Modelsページ](https://ai.google.dev/gemini-api/docs/models) で確認すること

### 2026-07-06: 初版執筆
- **内容**: Gemini.appとGemini APIの違い(Google AI Studio経由・Vertex AI経由)、APIキー取得手順、モデル指定の考え方(Pro/Flash/Flash-Lite)、料金体系(無料枠・従量課金)、Function Calling/Structured Outputs/Grounding with Google Search/Context Caching/Batch APIの概要、OpenAI API・Anthropic APIとの3社比較表を整理
- **出典**: [Google AI for Developers: Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing)、[Google AI for Developers: Using Gemini API keys](https://ai.google.dev/gemini-api/docs/api-key)、[Google AI for Developers: Rate limits](https://ai.google.dev/gemini-api/docs/rate-limits)、[Google AI for Developers: Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)、[Google AI for Developers: Structured outputs](https://ai.google.dev/gemini-api/docs/structured-output)、[Google Cloud: Gemini Enterprise Agent Platform(旧Vertex AI)](https://cloud.google.com/products/gemini-enterprise-agent-platform)
- **注記**: モデル名・料金は改定が非常に頻繁なため、本文の数値は目安として扱い、最新の単価・モデルIDは必ず [Gemini API公式Pricingページ](https://ai.google.dev/gemini-api/docs/pricing) と [Modelsページ](https://ai.google.dev/gemini-api/docs/models) で確認すること
