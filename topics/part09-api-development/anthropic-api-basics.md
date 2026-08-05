---
title: "Anthropic API(Claude API)の基本"
part: 9
chapter: 第1章 LLM APIの基礎
tags: [Anthropic API, Claude API, API開発, LLM API]
created: 2026-07-06
updated: 2026-08-05
---

# Anthropic API(Claude API)の基本

## これは何か

Claude.ai(またはClaude Desktop/モバイルアプリ)を契約していれば、DifyやGASなど他のツールからもClaudeを自由に呼び出せる、と誤解している人は多い。実際にはClaude.aiのサブスク(Free/Pro/Max)とAnthropic API(従量課金、通称「Claude API」)は完全に別契約であり、社内システムやノーコードツールにClaudeを組み込みたい場合はAPIを別途契約する必要がある。この関係は[OpenAI APIの基本](openai-api-basics.md)で説明したChatGPTとOpenAI APIの関係とまったく同じ構図である。

## 仕組み・背景

- **Claude.ai**: claude.ai上でチャット形式でClaudeと対話する、エンドユーザー向けの製品。Free/Pro/Maxなどの月額サブスクリプションで提供される。
- **Anthropic API(Claude API)**: 開発者向けのインターフェースで、自社の業務システム・チャットボット・要約や分類のバッチ処理など、Claudeを自社サービスに組み込むための仕組み。管理画面は「Claude Developer Platform」(platform.claude.com。プロンプトのテスト画面などは今も「Claude Console」と呼ばれる)で、Claude.aiのサブスク契約とは別会計である。Claude Proに入っていてもAPI利用料は割引されないし、逆にClaude.aiを契約していなくてもAnthropicアカウントと支払い方法さえあればAPIのみ契約できる。

APIの中核は**Messages API**と呼ばれる単一のエンドポイント(`POST https://api.anthropic.com/v1/messages`)で、会話履歴を`messages`配列として渡すとClaudeの応答が返ってくる。OpenAI APIのChat Completions API/Responses APIに相当する存在だが、認証ヘッダーや必須パラメータの作法が異なる(後述の比較表を参照)。

**モデルのグレードは2026年8月時点で4段階**になっている。上から「Claude Fable 5」(最上位・最も高性能で最も高額。長時間の自律的なエージェントタスク向け)、「Claude Opus 5」(複雑なエージェント型コーディング・エンタープライズ業務向けの主力モデル。2026年7月下旬にClaude Opus 4.8の後継として登場し、料金はOpus 4.8と同水準のまま性能が向上)、「Claude Sonnet 5」(速度と性能のバランスが良く、多くの本番用途で推奨される中核モデル)、「Claude Haiku 4.5」(軽量・高速・低コスト)という並びで、料金も入力・出力トークンあたりの単価で明確に分かれている(いずれも出力単価は入力単価のおよそ5倍)。一つ前の世代である「Claude Opus 4.8」「Opus 4.7」「Opus 4.6」も引き続き利用可能(料金はOpus 5と同じ$5/$25)だが、新規に始めるなら基本的にOpus 5を選べばよい。なお「Claude Mythos 5」という限定提供モデルもあるが、これはサイバーセキュリティ防御用途の招待制プログラム(Project Glasswing)向けで、一般の業務利用では基本的に対象外。

料金は「トークン(文章を分割した単位)」ごとの従量課金で、入力(プロンプト)側より出力(生成結果)側の単価が高く設定されている。モデルのグレードによっても単価は大きく変わり、高性能なモデルほど高額になる。

## 使いどころ・使い分け

| やりたいこと | 向いている契約・モデル |
|---|---|
| 自分でチャット画面から質問・相談したい | Claude.ai(Free/Pro/Max) |
| 社内システムやスプレッドシートにClaudeの機能を組み込みたい | Anthropic API |
| Difyやn8nなどノーコードツールでAIアプリを作りたい | Anthropic API(ノーコードツール側にAPIキーを設定) |
| 定型的な要約・分類・チャットボットを大量に高速・低コストでさばきたい | Anthropic APIのClaude Haiku 4.5 |
| 多くの業務システムでバランス重視の主力モデルを使いたい | Anthropic APIのClaude Sonnet 5 |
| 難易度の高いエージェント型コーディング・複雑な業務判断を任せたい | Anthropic APIのClaude Opus 5 |
| 長時間の自律実行・非常に難しい推論タスクを最高性能で任せたい(コストは度外視) | Anthropic APIのClaude Fable 5 |
| 大量のデータを一括で要約・分類したい(即時応答不要) | Anthropic APIのBatch API(通常の半額で処理できる) |
| 長い社内文書・マニュアルを毎回参照させたい | Anthropic APIのPrompt Caching(同じ前提文を使い回して割引) |
| じっくり考えさせてから答えさせたい複雑な推論タスク | Anthropic APIのAdaptive Thinking対応モデル |

## 実務での使い方

### APIキーの取得手順

1. platform.claude.com(旧console.anthropic.com。現在はここにリダイレクトされる)にアクセスし、メール・Google・SSOでログインまたはサインアップする(Claude.aiと同じAnthropicアカウントでよい)
2. 左サイドバーの「API Keys」、または直接 platform.claude.com/settings/keys にアクセス
3. 先に「Settings」→「Billing」でクレジットカードを登録しておく(未登録だとキーを発行しても呼び出しがエラーになる)
4. 「Create Key」をクリックし、名前(例: "Production"、"Dify連携用")と権限(フルアクセス/読み取り専用)、必要なら有効期限を設定する
5. 生成されたキー(`sk-ant-`で始まる文字列)はその場でしか全文表示されないため、必ずコピーして安全な場所に保管する(紛失時は再表示できず、失効させて再発行が必要)
6. あわせて「Settings」→「Limits」等から想定外の高額請求を防ぐための利用上限(月間の支出上限・レート制限)を設定しておく

### 最小のコード例(Messages API)

```bash
curl https://api.anthropic.com/v1/messages \
  -H "content-type: application/json" \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-5",
    "max_tokens": 1024,
    "messages": [
      {"role": "user", "content": "この請求書PDFの合計金額を1文で要約して"}
    ]
  }'
```

日常的な要約・分類・チャットボット用途なら`claude-sonnet-5`、コーディングや複雑な判断を伴うタスクなら`claude-opus-5`のように、用途に応じてモデルIDだけ差し替えればよい。OpenAI APIと違い、認証は`Authorization: Bearer`ではなく`x-api-key`ヘッダーで行い、APIのバージョンを`anthropic-version`ヘッダーで明示する必要がある(公式SDKを使えば自動で付与される)。

### 料金体系のイメージ(2026年8月時点、モデル名・価格は変更が頻繁なため必ず公式ページ platform.claude.com/docs/ja/about-claude/pricing で最終確認すること)

- 現行ラインナップは上からFable 5(最上位)/Opus 5(高性能・エージェント型コーディング向け主力)/Sonnet 5(バランス型・主力)/Haiku 4.5(軽量・高速)の4グレードで、100万トークンあたりの入力/出力単価はFable 5が$10/$50、Opus 5が$5/$25、Sonnet 5が$3/$15(**2026年8月31日まで導入価格の$2/$10が適用中**)、Haiku 4.5が$1/$5という水準
- Opus 5は2026年7月下旬にOpus 4.8の後継として登場したモデルで、価格はOpus 4.8と同じ$5/$25のまま性能が向上している。旧世代のOpus 4.8・4.7・4.6も同じ$5/$25で引き続き利用できるが、レート制限はOpus 5だけ独立した専用枠になっている(下記「レート制限」参照)
- どのモデルも出力トークンは入力トークンのおよそ5倍の単価
- Prompt Caching(直前と同じ前提文の再利用)を使うとキャッシュ済み入力は通常の入力より大幅に割引される(キャッシュ読み取りは通常の1割の価格、つまり9割引。ただしキャッシュへの書き込み自体は通常より割高で、5分間有効なキャッシュは1.25倍、1時間有効なキャッシュは2倍の料金がかかる)
- Batch API(非同期処理)は同期呼び出しに比べて入力・出力とも50%安い
- Fable 5・Opus 5・Opus 4.8/4.7/4.6・Sonnet 5・Sonnet 4.6は、100万トークンの長いコンテキストウィンドウを追加料金なしの標準料金で利用できる
- Opus 4.7以降(Opus 5・Fable 5・Sonnet 5含む)は新しいトークナイザーを採用しており、同じ文章でも旧世代モデル(Sonnet 4.6以前)よりトークン数が目安3割ほど多くカウントされる点に注意(単価だけでなくトークン数の違いも実コストに影響する)

### レート制限(利用しすぎを防ぐ仕組み)

APIキーには「1分あたり何リクエストまで」「1分あたり何トークンまで」といったレート制限と、「1か月あたりいくらまで」という支出上限が組織単位で設定されている。2026年8月時点では利用実績に応じて自動的にStart(月間支出上限$500)→Build(同$1,000)→Scale(同$200,000)の3段階に昇格する仕組みで、各段階でモデルごとのRPM(1分あたりリクエスト数)・ITPM(1分あたり入力トークン数)・OTPM(1分あたり出力トークン数)の上限が決まっている(例: Startティアの主要モデルは1,000RPM・200万ITPM・40万OTPM程度)。旧世代のOpus 4.8/4.7/4.6は合算で1つの上限を共有するが、**Claude Opus 5だけは独立したレート制限枠**を持つため、Opus 5に切り替えても旧Opusモデルの枠を消費しない(その代わりOpus 5用に別途枠を確保しておく必要がある)。上限を超えると`429`エラーが返り、レスポンスの`retry-after`ヘッダーで待機秒数が分かる。なお、Prompt Cachingでキャッシュから読み込んだ入力トークンはITPMの上限にカウントされない(モデルにより例外あり)ため、キャッシュを活用するほど実質的なスループットを高められる。上限の確認・引き上げ申請はConsoleの「Settings」→「Limits」から行う。

### ノーコードツール・業務システムとの連携例

- **Dify**: モデルプロバイダーの設定画面で「Anthropic」を選び、APIキーを入力するだけで、Dify上に作ったチャットボットやワークフローからClaudeを呼び出せる
- **GAS(Google Apps Script)**: `UrlFetchApp`で`https://api.anthropic.com/v1/messages`にHTTPリクエストを送り、スプレッドシートの内容を要約・分類するといった社内自動化によく使われる。ヘッダーに`x-api-key`と`anthropic-version`を忘れずに付与する
- **n8n / Zapier / Make**: 「Anthropic」用の専用ノード・アクションが用意されており、他システムとの連携・自動実行のトリガーとして組み合わせて使われる

### 代表的な機能(名前と一言メモ)

- **Messages API**: 会話履歴をやり取りする中核のエンドポイント。OpenAIのChat Completions APIに相当
- **Tool Use(ツール呼び出し)**: モデルに外部の関数・API・DBクエリを呼び出させる仕組み。OpenAIの「Function Calling」に相当する機能で、呼び方(用語)が異なるだけで考え方は同じ。詳しくは[Function Calling(Tool Use)の基本](function-calling-basics.md)を参照
- **Adaptive Thinking(適応的思考)**: 回答前にモデル内部でより長く「考える」過程を、モデル自身が必要な分だけ自動で確保する仕組み。以前は`budget_tokens`という数値で思考量を人手で指定する「Extended Thinking」が主流だったが、現行モデルでは基本的にモデル任せのAdaptive Thinkingが推奨されている。複雑な推論・計算・多段階の判断が必要なタスクの精度を上げられる
- **Prompt Caching**: システムプロンプトや長いマニュアル・ドキュメントなど、繰り返し使う前提文をキャッシュし、2回目以降の呼び出しコストを大幅に下げる仕組み
- **Batch API**: 大量のリクエストをまとめて非同期送信し、通常より安く(約半額)処理する仕組み
- **Web検索・Webページ取得ツール**: モデルが自分でWeb検索や指定URLの取得を行い、最新情報を踏まえて回答できるようにするサーバー側ツール。検索1,000回あたり$10の従量課金(URL取得は追加料金なし)
- **Claude Managed Agents**: エージェントの実行ループとサンドボックス環境(ファイル操作・コマンド実行など)をAnthropic側がホストしてくれる仕組み。自前でエージェントのループやサーバーを構築しなくても、長時間動く自律型エージェントを構築できる比較的新しい機能。課金はトークン(通常のモデル料金)に加えて、セッションが実際に稼働(`running`)している時間に対して1セッション時間あたり$0.08の従量課金が乗る(待機中の`idle`時間は課金対象外)

### OpenAI APIとの違い(比較表)

| 項目 | Anthropic API(Claude) | OpenAI API |
|---|---|---|
| 管理画面 | Claude Developer Platform(platform.claude.com) | platform.openai.com |
| 認証ヘッダー | `x-api-key: <キー>` | `Authorization: Bearer <キー>` |
| APIバージョン指定 | `anthropic-version`ヘッダーが必須(SDK利用時は自動) | 明示的なバージョンヘッダーは基本不要 |
| 中核エンドポイント | `/v1/messages`(Messages API) | `/v1/chat/completions` または `/v1/responses` |
| システムプロンプトの渡し方 | `messages`とは別に独立した`system`パラメータ | `messages`配列内に`role: "system"`として含める |
| 外部関数呼び出し | Tool Use | Function Calling |
| 「じっくり考えさせる」機能 | Adaptive Thinking(旧Extended Thinking) | 推論(reasoning)系モデルの内部推論 |
| キャッシュ割引 | Prompt Caching(自動または明示指定、キャッシュ読み取りは9割引) | プロンプトキャッシュ(自動適用、割引率はモデル依存) |
| 非同期・低価格処理 | Batch API(約50%割引) | Batch API(約50%割引) |
| 料金体系 | 入出力トークン単価制、出力は入力の約5倍が目安 | 入出力トークン単価制、出力は入力の3〜6倍程度が目安 |

大枠の思想(トークン従量課金、Batch APIでの割引、Tool Use/Function Callingの考え方)はよく似ているが、ヘッダー名・エンドポイント名・パラメータの細部が異なるため、片方のAPI用に書いたコードはそのままではもう一方に流用できない点に注意。

## 注意点・よくある誤解

- **Claude.ai課金とAPI課金は別会計**: Claude Proの月額料金はAPI利用料の割引にはならない。混同して「なぜ別料金が発生するのか」と驚かないよう、契約前に整理しておく。
- **料金・モデル名は非常に頻繁に更新される**: 2026年に入ってからも数か月おきにモデルの世代・価格が改定されている(直近ではClaude Opus 5が2026年7月下旬にOpus 4.8の後継として登場)。記事や社内資料に価格を書く場合は、必ず公式サイトの最新情報を都度確認する。
- **「Opus」を指定するコードは自動的に最新版を使うわけではない**: `claude-opus-4-8`のようにモデルIDを直書きしているコードは、Opus 5が出ても古いモデルを呼び続ける。新規案件は`claude-opus-5`を、既存コードは移行を検討する。
- **モデル世代でトークンの数え方が変わる**: Opus 4.7以降(Opus 5・Fable 5・Sonnet 5含む)は新しいトークナイザーの影響で、同じ日本語・英語の文章でも旧世代モデルよりトークン数が多く算出される。単価表だけを見て「安くなった/高くなった」と単純比較しないこと。
- **`x-api-key`と`anthropic-version`の付け忘れ**: OpenAI API用のコードを流用すると`Authorization: Bearer`のまま送ってしまいがちだが、Anthropic APIでは認証エラーになる。ヘッダーの違いを意識する。
- **利用上限を設定せずに使うと高額請求のリスクがある**: 想定外の大量呼び出し(バグによる無限ループ等)に備えて、必ず利用上限(Limits、月間支出上限とレート制限の両方)を設定しておく。

## 最初の一歩

自社でDifyやGASなどのノーコード連携を検討しているなら、まずplatform.claude.comでAPIキーを1つ発行し、利用上限を低めに設定した状態で上記のcurl例をそのまま実行してみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)
- [Function Calling(Tool Use)の基本](function-calling-basics.md)
- [Claudeの基本](../part03-ai-chat-tools/claude-basics.md)

## 更新履歴

### 2026-08-05: Claude Opus 5の登場を反映
- **内容**: 2026年7月下旬に登場した「Claude Opus 5」(Opus 4.8の後継、料金はOpus 4.8と同じ$5/$25)をラインナップに追加し、コーディング・複雑な判断向けの推奨モデルをOpus 4.8からOpus 5に更新。コード例のモデルIDをclaude-opus-5に変更(用途別の使い分けも追記)。旧世代Opus(4.8/4.7/4.6)は合算のレート制限枠を共有する一方、Claude Opus 5は独立したレート制限枠を持つ点を追記。Claude Managed Agentsのセッション稼働時間課金($0.08/セッション時間)を追記
- **出典**: [Claude Platform Docs: Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)、[Claude Platform Docs: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)、[Claude Platform Docs: Rate limits](https://platform.claude.com/docs/en/api/rate-limits)、[Technology.org: Anthropic Debuts Claude Opus 5 at Half the Price](https://www.technology.org/2026/07/27/anthropic-claude-opus-5-launch-half-price/)

### 2026-07-20: モデルラインナップ・料金・レート制限を最新化
- **内容**: モデルグレードをFable 5/Opus 4.8/Sonnet 5(新登場)/Haiku 4.5の4段階に更新し、コード例のモデルIDをclaude-sonnet-5に変更。料金表・Prompt Cachingの割引率(キャッシュ書き込み1.25倍/2倍・読み取り0.1倍)・長コンテキストの無料枠・新トークナイザーによるトークン数増加を追記。レート制限(Start/Build/Scaleの3段階の支出上限・RPM/ITPM/OTPM)の節を新設。Extended ThinkingをAdaptive Thinkingに用語更新し、Web検索ツール・Claude Managed Agentsを代表機能に追加
- **出典**: [Claude Platform Docs: 料金(日本語)](https://platform.claude.com/docs/ja/about-claude/pricing)、[Claude Platform Docs: Models overview](https://platform.claude.com/docs/en/about-claude/models/overview)、[Claude Platform Docs: Rate limits](https://platform.claude.com/docs/en/api/rate-limits)

### 2026-07-06: 初版執筆
- **内容**: Claude.aiとAnthropic APIの違い、Messages APIの呼び出し方、APIキー取得手順、料金体系(モデル別トークン単価)、Tool Use/Extended Thinking/Prompt Caching/Batch APIの概要、OpenAI APIとの比較表を整理
- **出典**: [Claude Platform Docs: Pricing](https://platform.claude.com/docs/en/about-claude/pricing)、[Claude Platform Docs: API overview](https://platform.claude.com/docs/en/api/overview)、[Claude Platform Docs: Versioning](https://platform.claude.com/docs/en/api/versioning)、[Claude Platform Docs: Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)、[CloudZero: Anthropic Claude API Pricing In 2026](https://www.cloudzero.com/blog/claude-api-pricing/)
- **注記**: モデル別の具体的な料金は変更が頻繁なため、本文の数値は目安として扱い、最新の単価は必ず [Claude Platform公式Pricingページ](https://platform.claude.com/docs/en/about-claude/pricing) で確認すること
