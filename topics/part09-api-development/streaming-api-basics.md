---
title: ストリーミング応答(Streaming)の基本
part: 9
chapter: 第2章 API活用実践
tags: [API, Streaming, SSE, レイテンシ, UX, Function Calling, Batch API]
created: 2026-08-19
updated: 2026-08-19
---

# ストリーミング応答(Streaming)の基本

## これは何か

ChatGPTやClaude.appでメッセージを送ると、回答がひとかたまりで表示されるのではなく、文章が1文字ずつ・数語ずつ画面に流れ込んでくる。この「生成されている途中の文章をリアルタイムに表示する」仕組みがストリーミング(Streaming)で、API経由でチャットボットや業務アプリを自作する際にも、通常のAPI呼び出しに1つのパラメータを追加するだけで同じ体験を実現できる。ストリーミングを使わないと、モデルが数百〜数千字の回答を作り終えるまで画面が固まったように見え、特に長文生成や複雑な指示の場合はユーザーが「壊れているのでは」と感じて離脱する原因になる。

## 仕組み・背景

### 通常のAPI呼び出し(非ストリーミング)との違い

通常のAPI呼び出しは、リクエストを送ってから、モデルが回答をすべて生成し終えるまでサーバー側で待ち、完成した回答をまとめて1回で返す。これを非ストリーミング(または同期)呼び出しと呼ぶ。一方ストリーミングは、モデルが生成したトークン(文章を分割した単位)を、生成されるそばから少しずつクライアントに送り返す方式。

重要な誤解を先に解いておくと、**ストリーミングはモデルの生成速度そのものを速くするわけではない**。回答をすべて生成し終えるまでの合計時間(トータルのレイテンシ)は理屈上ほぼ変わらない。変わるのは「最初の一文字がユーザーの画面に表示されるまでの時間(Time To First Token、TTFT)」で、これが劇的に短くなることで**体感速度**が上がる。バッチ処理([バッチ処理(Batch API)の基本](batch-api-basics.md)参照)が「即時性を捨てて安さを取る」仕組みだとすれば、ストリーミングは「合計時間は変えずに体感の待ち時間を減らす」仕組みと整理すると位置づけがわかりやすい。

### 技術的な土台: SSE(Server-Sent Events)

主要な生成AI APIのストリーミングは、いずれもSSE(Server-Sent Events)という技術の上に成り立っている。SSEは、サーバーからブラウザ・クライアントへ一方向にテキストデータを逐次送り続けるためのシンプルな仕組みで、レスポンスのヘッダーが`Content-Type: text/event-stream`になり、本文が`data: {...}`という行の連続として送られてくる。1行のJSONが送られてくるたびにクライアント側のプログラムがそれを解釈し、断片を画面に追記していく。接続は生成が終わるまで開いたままになり、最後に「完了」を示す合図(プロバイダーごとに形式は異なる)が送られて終了する。

各社ともAPIリクエストに1つのパラメータを足すだけでこの方式に切り替わる。

- **OpenAI**: リクエストに`"stream": true`を指定する。Chat Completions APIでは、各チャンクが`choices[0].delta.content`という形で断片テキストを含む(完成形の`message`ではなく差分の`delta`である点に注意)。新しい**Responses API**では、`response.created`(開始)・`response.output_text.delta`(テキスト断片)・`response.completed`(完了)・`response.failed`(失敗)のように、用途ごとに名前が付いた「セマンティックイベント」形式になっており、見たいイベント種別だけを拾えるよう設計されている。
- **Anthropic(Claude API)**: `client.messages.stream(...)`というSDKのヘルパーを使うのが基本(内部的には`stream: true`を指定したリクエスト)。イベントは`message_start`(開始)→`content_block_start`(テキストやツール呼び出しのブロック開始)→`content_block_delta`(断片、`text_delta`/`thinking_delta`など)→`content_block_stop`(ブロック終了)→`message_delta`(`stop_reason`や使用トークン数などメッセージ全体の更新)→`message_stop`(完了)という流れで届く。
- **Google Gemini API**: `generateContent`の代わりに`streamGenerateContent`エンドポイントを呼ぶ(URLに`?alt=sse`を付けるとSSE形式になる)。SDKでは`generateContentStream`(Python/JavaScriptとも同名の関数)を使い、断片テキストを非同期の反復処理(イテレータ)で順に受け取る。

各社で呼び出し方・イベント名は異なるが、「パラメータ1つで有効化」「断片(delta)が連続で届く」「最後に完了の合図がある」という骨格は共通している。

## 使いどころ・使い分け

| 判断軸 | ストリーミングが向く | ストリーミングが向かない(非ストリーミングでよい) |
|---|---|---|
| ユーザーが画面の前で待っているか | チャットUI、AIアシスタント機能など、人がリアルタイムに読む用途 | バックグラウンドで動く処理、人が結果を見ないバッチ処理 |
| 回答をそのまま使えるか、後処理が必要か | 生成した文章をそのまま表示するだけでよい | 出力をJSONとしてパースする・バリデーションする・DBに登録するなど、完成形が必要な処理 |
| 出力形式 | 自由文(chatの回答、要約文など) | JSONモード/Structured Outputs、Function Callingの引数生成など「完成して初めて意味を持つ」形式 |
| 処理方式 | 1件ずつのリアルタイム呼び出し | Batch API(バッチAPI)を使う大量処理(**Batch APIはそもそもストリーミング非対応**) |
| 実行環境 | 素直にHTTPコネクションを保持できる環境(自社サーバー、ブラウザ) | GAS(Google Apps Script)の`UrlFetchApp`など、そもそもストリーミング受信の仕組みを持たない環境 |

判断基準はシンプルで、「ユーザーが生成過程をリアルタイムに見る意味があるか」「後続処理のために完成した出力全体が必要か」で分ける。**チャットボットの画面出力にはほぼ常にストリーミングを使うべきで、逆にJSON抽出・Function Calling・バッチ処理のような「機械が完成品を読む」用途では非ストリーミングの方がシンプルで事故が少ない。**

### JSON mode / Structured Outputs・Function Callingとの相性

ストリーミングとJSONモード(決まった形式で出力させる機能。[JSONモード・Structured Outputsの基本](json-mode-structured-outputs.md)参照)やFunction Calling([Function Calling(Tool Calling)の基本](function-calling-basics.md)参照)は技術的には併用できるが、実務では相性がよくない。

- JSON出力を途中まで受け取っても、閉じ括弧が来るまでは構文的に不完全なJSONであり、そのままではパースできない。生成が終わるまで断片を貯め込んでから一括でパースするなら、最初から非ストリーミングで待った方がコードがシンプルになる。
- Function Callingでモデルが返す「呼び出したい関数名・引数」も、引数(JSON文字列)がストリーミング中は断片で届くため、呼び出しが完了するまで結局は全断片を結合してからでないと関数を実行できない。ツールを都度リアルタイムに実行させたい高度なエージェント実装でない限り、Function Calling中心のバックエンド処理は非ストリーミングの方が実装・デバッグが楽になる。

つまり「人間がその場で読む文章」はストリーミング向き、「プログラムが完成形を読む構造化データ」は非ストリーミング向き、という切り分けが実務上わかりやすい。

## 実務での使い方

### 最小構成のコード例

**Anthropic(Claude API、Python SDK)**

```python
with client.messages.stream(
    model="(使用するモデル名)",
    max_tokens=1024,
    messages=[{"role": "user", "content": "生成AIの活用事例を3つ教えて"}],
) as stream:
    for text in stream.text_stream:
        print(text, end="", flush=True)   # 断片が届くたびに逐次出力

    final_message = stream.get_final_message()  # 完成した全文・使用トークン数はここで取得
```

**OpenAI(Chat Completions API、概念イメージ)**

```jsonc
// リクエスト: stream: true を付けるだけ
{
  "model": "(使用するモデル名)",
  "messages": [{ "role": "user", "content": "生成AIの活用事例を3つ教えて" }],
  "stream": true
}

// レスポンス: SSEで断片(delta)が連続して届く
// data: {"choices":[{"delta":{"content":"生成"},"finish_reason":null}]}
// data: {"choices":[{"delta":{"content":"AI"},"finish_reason":null}]}
// ...
// data: {"choices":[{"delta":{},"finish_reason":"stop"}]}
// data: [DONE]
```

**Google Gemini API(curlでのSSE確認例)**

```bash
curl "https://generativelanguage.googleapis.com/v1beta/models/(使用するモデル名):streamGenerateContent?alt=sse" \
  -H "x-goog-api-key: $GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  --no-buffer \
  -d '{"contents":[{"parts":[{"text":"生成AIの活用事例を3つ教えて"}]}]}'
```

`--no-buffer`はcurl側の受信バッファリングを無効にするオプションで、これを付けないとcurl自身が断片を貯め込んでしまい、ストリーミングの動きを目視で確認できない。

### 各社の対応付け

| 項目 | OpenAI | Anthropic(Claude) | Google Gemini |
|---|---|---|---|
| 有効化パラメータ | `stream: true`(Chat Completions / Responses API共通) | `stream: true`(SDKでは`client.messages.stream(...)`ヘルパー推奨) | `streamGenerateContent`エンドポイントを呼ぶ(SSE化は`?alt=sse`) |
| SDKの推奨呼び出し | Responses APIの`stream=True`(セマンティックイベント) | `messages.stream()` → `.text_stream`で断片、`.get_final_message()`で完成形 | `generate_content_stream()`(Python)/`generateContentStream()`(JS) |
| 主なイベント/断片の場所 | Chat Completions: `choices[0].delta.content`。Responses API: `response.output_text.delta`等のイベント名 | `content_block_delta`イベントの`delta.text`(テキスト)/`delta.thinking`(思考過程) | 各チャンクの`candidates[0].content.parts[0].text` |
| 完了の合図 | Chat Completions: `data: [DONE]`。Responses API: `response.completed`イベント | `message_stop`イベント(直前の`message_delta`に`stop_reason`・使用トークン数) | ストリームのクローズ(明示的な完了イベント名は用途により異なる) |
| 使用トークン数の取得タイミング | ストリーム終盤のイベント(または完了後に別途取得) | `message_delta`イベントの`usage`フィールド(ストリーム終盤) | レスポンス終盤の`usageMetadata` |

### ノーコードツールでの位置づけ

- **Dify**: チャットボット形式のアプリはAPI(`/chat-messages`エンドポイント)の`response_mode`パラメータで`"streaming"`(SSEで逐次応答)か`"blocking"`(完成形をまとめて返す)を選べる。画面上でDifyのチャットUIを使う場合は自動的にストリーミング表示になるため、開発者が個別に設定する場面は主に自作フロントエンドからDify APIを呼ぶ場合に限られる。
- **GAS(Google Apps Script)**: [GAS(Google Apps Script)からのAI API連携](gas-ai-api-integration.md)で使う`UrlFetchApp`は、レスポンスを最後まで受け取ってから返す仕組みのため、**そもそもストリーミング受信に対応していない**。スプレッドシート連携や夜間バッチのようにGASでAI APIを呼ぶ場合は、ストリーミングを使わず通常の呼び出しで完成した回答をまとめて受け取る設計にする(チャット的なリアルタイム表示をどうしても作りたい場合は、GASではなく別途Webアプリ側で実装する必要がある)。

### 自社バックエンドを介して配信する場合の注意(プロキシ・バッファリング)

自社のサーバー(Node.js/Pythonなど)がLLM APIとストリーミングでやり取りし、それをさらに自社のフロントエンドにストリーミング配信する構成はよくあるが、間に挟まる**リバースプロキシやロードバランサーがレスポンスをバッファリング(一旦貯め込んでからまとめて転送)してしまい、ストリーミングの恩恵が消える**という落とし穴がある。典型的にはnginxが該当し、対策として`proxy_buffering off;`の指定や、バックエンド側のレスポンスヘッダーに`X-Accel-Buffering: no`を付ける必要がある。あわせて、接続を長時間開いたままにするため`proxy_read_timeout`のようなタイムアウト設定を延ばしておかないと、生成が長引いた際に接続が途中で切られることもある。「APIはストリーミング対応にしたのに画面はカクカクとしか表示されない」という症状が出たら、まずこのプロキシ層のバッファリング設定を疑うとよい。

## 注意点・よくある誤解

- **「速くなる」わけではない**: 繰り返しになるが、ストリーミングは体感速度(TTFT)を改善する仕組みであり、生成完了までの合計時間や料金を変えるものではない。同じ入力・出力トークン数であれば、ストリーミングの有無で課金額は基本的に変わらない。
- **途中で切断されたら、その分の課金がどうなるかはプロバイダー依存**: 通信エラーなどでストリームが途中で切れた場合、そこまで生成された分の出力トークンが課金対象になるかどうかはプロバイダーやケースによって扱いが異なりうる。重要な処理では、切断時の再試行設計(最初からやり直す/どこまで課金されたかログで確認する)をあらかじめ決めておく。
- **途中経過は「未完成」であることを忘れない**: ストリーミング中の断片をそのまま外部システムに渡す・保存すると、不完全な文章やJSONの断片を扱うことになる。画面表示以外の用途(ログ保存、後続処理へのバケツリレーなど)には、完成後の全文(`get_final_message()`などで取得できる最終形)を使う。
- **エラーはストリームの途中でも起こりうる**: レート制限超過や接続断は、生成が始まった後でも発生する。ある程度の文章が画面に表示された状態で急に途切れる体験は非ストリーミングよりもむしろユーザーを混乱させやすいため、アプリ側で「回答が途中で終わりました。もう一度お試しください」のようなフォールバック表示を用意しておく。
- **Batch APIとは併用できない**: [バッチ処理(Batch API)の基本](batch-api-basics.md)で扱うBatch APIは、非同期でまとめて処理する方式のためストリーミングオプションを指定できない。「安く大量に処理したい」場合はBatch、「リアルタイムに見せたい」場合はストリーミングと、目的によって完全に別の道具として使い分ける。
- **長い出力ではタイムアウト対策としても有効**: HTTPクライアントやサーバーには「一定時間データが来ないと接続を切る」タイムアウトが設定されていることが多く、生成に数分かかるような長文・大量トークンの出力を非ストリーミングで待つと、回答が完成する前にクライアント側のタイムアウトに引っかかって失敗することがある。ストリーミングにすると断片が継続的に届き続けるため接続が生きていると判定され、こうしたタイムアウトを回避しやすくなる。長文要約やレポート生成など出力が長くなりがちな用途では、UXのためだけでなく安定性のためにもストリーミングを選ぶ価値がある。

## 最初の一歩

すでにOpenAI・Anthropic・Geminiいずれかのモデルにcurlやコードで通常のAPI呼び出しをしたことがあるなら、そのリクエストに`stream: true`(またはGeminiの場合は`streamGenerateContent`エンドポイントへの切り替え)を1つ加えるだけで、SSEの断片が連続して返ってくる様子を実際に確認してみる。

## 関連トピック

- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [バッチ処理(Batch API)の基本](batch-api-basics.md)
- [JSONモード・Structured Outputsの基本](json-mode-structured-outputs.md)
- [リアルタイム音声API(ボイスエージェント構築)の基本](realtime-voice-api-basics.md)
- [主要LLM APIの横断比較(OpenAI・Anthropic・Google)](llm-api-cross-tool-comparison.md)
- [GAS(Google Apps Script)からのAI API連携](gas-ai-api-integration.md)

## 更新履歴

### 2026-08-19: 初版執筆
- **内容**: ストリーミング応答(SSEベースの逐次出力)の仕組みと、非ストリーミング(同期呼び出し)との違い(TTFT改善であり合計時間や料金は変わらない点)を整理。OpenAI(Chat Completions/Responses API)・Anthropic(Claude API)・Google Gemini APIそれぞれのパラメータ名・SDK呼び出し方・イベント種別の対応表とコード例を作成。JSONモード/Structured Outputs・Function Callingとの相性、Batch APIとの併用不可、GASのUrlFetchAppが非対応であること、nginx等のプロキシバッファリング(`X-Accel-Buffering`)の落とし穴を注意点として追記
- **出典**: [OpenAI: Streaming API responses](https://developers.openai.com/api/docs/guides/streaming-responses)、[OpenAI: Chat Completions streaming events](https://developers.openai.com/api/reference/resources/chat/subresources/completions/streaming-events)、[OpenAI Cookbook: How to stream completions](https://cookbook.openai.com/examples/how_to_stream_completions)、[Anthropic: Streaming Messages](https://platform.claude.com/docs/en/build-with-claude/streaming)、[Google AI for Developers: Streaming interactions](https://ai.google.dev/gemini-api/docs/streaming)、[nginx: ngx_http_proxy_module (X-Accel-Buffering)](https://nginx.org/en/docs/http/ngx_http_proxy_module.html)、[oneuptime: How to Configure Server-Sent Events Through Nginx](https://oneuptime.com/blog/post/2025-12-16-server-sent-events-nginx/view)
