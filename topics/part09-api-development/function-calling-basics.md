---
title: Function Calling(Tool Calling)の基本
part: 9
chapter: 第2章 API活用実践
tags: [API, Function Calling, Tool Use, AIエージェント, Responses API]
created: 2026-07-05
updated: 2026-08-20
---

# Function Calling(Tool Calling)の基本

## これは何か

生成AIのモデル自身は、社内データベースを検索したり、最新の在庫状況を調べたり、メールを送信したりすることができない。モデルは「文章を生成する」ことしかできない箱であり、外の世界とは直接つながっていないからだ。Function Calling(Tool Calling、日本語では「関数呼び出し」「ツール呼び出し」とも呼ばれる)は、この壁を越えるための仕組みで、開発者があらかじめ「使えるツール(関数)」をモデルに教えておき、モデルが必要に応じて「この関数をこの引数で呼びたい」という構造化されたリクエストを返す。実際にその関数を実行するのは開発者側のプログラムであり、実行結果をモデルに戻すことで、モデルは最新のデータや実際のアクション結果を踏まえた回答ができる。

「AIチャットボットが注文状況を答えてくれる」「AIエージェントが実際にタスクをこなす」といった、生成AIが単なる会話を超えて何かを「実行する」アプリケーションは、ほぼ例外なくこの仕組みの上に成り立っている。

## 仕組み・背景

Function Callingの処理は、次の5ステップで進む。

1. **ツールの定義**: 開発者が「どんな関数が使えるか」を、名前・説明・引数の形式(JSON Schema)としてモデルに渡す準備をする。JSON Schemaとは、JSON形式のデータが「どんな構造であるべきか」を定義するための規格で、「引数`city`は文字列で必須」のようなルールを機械可読な形で書ける。
2. **モデルへの提示**: ユーザーの質問と一緒に、この「使えるツール一覧」をAPIリクエストに含めてモデルに送る。
3. **モデルの判断・出力**: モデルはユーザーの依頼内容を見て、ツールを使うべきだと判断すれば、実際にコードを実行するのではなく「この関数をこの引数で呼んでほしい」という構造化データ(JSON)を出力する。ツールが不要だと判断すれば、普通に文章で回答する。
4. **開発者側での実行**: アプリケーション側のコードが、モデルから来たリクエストを受け取り、実際にAPIを叩く・DBを検索する・メールを送るなどの処理を行う。ここは完全にモデルの外(自社のプログラム)で行われる処理であり、モデルはこの中身を知らない。
5. **結果をモデルに返却**: 実行結果をモデルに送り返すと、モデルはそれを踏まえて自然な文章で最終回答を作る。

重要なのは、**モデルは「関数を呼びたい」という意思表示をするだけで、関数を実際に実行する力は持たない**という点である。実行と安全確認の責任は常に開発者側のコードにある。

なお、2025〜2026年にかけて各社は以下のような機能拡張を進めている(詳細は本文末の出典を参照)。

- **並列ツール呼び出し(parallel tool calls)**: 1回のやり取りで複数のツールを同時に呼び出せる機能。OpenAIのAPIでは`parallel_tool_calls`パラメータで制御でき、処理に依存関係がある場合(Aの結果がないとBを呼べない、など)はあえて無効化することが推奨されている。Anthropicも既定で複数の`tool_use`ブロックを1ターンで返しうる(逆に1つに限定したい場合は`tool_choice`に`disable_parallel_tool_use: true`を指定する)。どちらも実行順序自体はAPIが決めるわけではなく、「並行実行して良いか(副作用のない読み取り専用の処理か)」の判断は開発者側のコードの責任になる。
- **スキーマの厳密一致(strict mode)**: OpenAIの「Structured Outputs」(ツール定義に`"strict": true`を付ける)やAnthropicの「strict tool use」(ツール定義に`strict: true`)など、モデルの出力トークン自体を指定したJSON Schemaに一致するものだけに制約する「grammar-constrained sampling」という技術が各社で整備され、`"2"`のような文字列型と数値型の取り違えや必須項目の欠落が起きにくくなっている。OpenAIは2025年半ばにstrict modeと並列ツール呼び出しの併用にも対応し、GPT-5以降のモデルは両立できる。
- **大量のツールを扱う仕組み**: Anthropicの「Tool Search Tool」(`tool_search_tool_regex_20251119`/`tool_search_tool_bm25_20251119`)のように、数百〜数千個のツールをモデルのコンテキストに全部読み込ませず、使う可能性があるツールに`defer_loading: true`を付けて必要な時だけ検索・呼び出す機能も登場している(公表されているベンチマークでは、トークン消費を約85%削減しつつMCPツールの選択精度も上がる結果が出ている)。
- **「組み込みツール」と「カスタム関数」は別物**: OpenAIのResponses APIやAnthropicのMessages APIには、Web検索・コード実行・ファイル検索・リモートMCPサーバー呼び出しなどモデル提供側が用意する「組み込みツール(built-in tools)」がある。これらはスキーマ定義や実行コードを書かずに`tools`に名前を指定するだけで使え、実行自体もOpenAI/Anthropic側のサーバーで完結する。一方、本ページで扱う「関数呼び出し(custom function calling)」は、社内APIやDBなど自社が持つ機能をツール化するもので、スキーマ定義も実際の実行も開発者側の責任になる。両者は同じ`tools`パラメータの中に混在させて1回のリクエストで使い分けられる。
- **OpenAIのAPI体系の刷新と旧APIの廃止**: OpenAIは2025年に「Responses API」を新設し、Function Calling・Web検索・コード実行・リモートMCPサーバー呼び出しなどを1つのAPIリクエストの中でエージェント的にループさせられるようにした。旧来の「Assistants API」(`/v1/assistants`・`/v1/threads`等)は**2026年8月26日に廃止**され、それ以降は呼び出すとエラーになる(移行猶予・縮退モードはない)。本ページ執筆時点(2026年8月20日)であと数日に迫っており、まだ移行できていない場合は最優先でResponses APIへの移行作業を進める必要がある。新規に実装するなら基本はResponses APIを使う(詳細は次項)。
- **Gemini 3系の thought signature**: Gemini 3以降のモデルでFunction Callingを使う場合、モデルが返す`functionCall`パートには`thoughtSignature`(内部の思考過程を表す暗号化データ)が付与される。マルチターンの会話でこれを次のリクエストに含め忘れると、`400`エラー(thought signature is required)になる。連続してツールを呼ぶ場合は呼び出しごとにsignatureが付くため、すべて送り返す必要がある。公式SDK(Google Gen AI SDK)を使えば自動的に処理されるが、raw HTTPで直接APIを叩く場合は明示的に扱う必要がある。
- **大規模エージェント向けの発展形(Anthropic)**: 2025年11月に追加された「Programmatic Tool Calling」は、モデルがツールを1回ずつ呼ぶのではなく、複数のツール呼び出しを組み合わせるコードそのものを書いて管理された実行環境の中で走らせる仕組みで、公表事例ではツール数が多い業務エージェントの入力トークンを4割弱削減できたとされる。2026年4月には、安価なモデル(Haiku/Sonnet)がタスクを回しながら、行き詰まった時だけ高性能モデル(Opus)に相談する「Advisor Strategy」も登場した。いずれも本ページの基本形(呼び出し要求→開発者が実行→結果を返す)を土台にした、コスト最適化のための上級者向け拡張という位置づけ。

## 使いどころ・使い分け

すべてのAI活用にFunction Callingが必要なわけではない。他の手段との使い分けの目安は次のとおり。

| やりたいこと | 向いている手段 |
|---|---|
| 一般知識をもとに文章を書く・要約する・翻訳する | 通常のプロンプト(Function Calling不要) |
| 社内文書やマニュアルの内容をもとに回答させたい | RAG(検索拡張生成。文書を検索してプロンプトに埋め込む方式) |
| 「今日の在庫数」「このお客様の注文状況」など、都度変わるリアルタイムのデータを調べて答えさせたい | Function Calling(社内APIやDBへの問い合わせ関数を用意) |
| AIに実際の操作(メール送信、チケット起票、予約変更など)を実行させたい | Function Calling(実行系のAPIをツールとして登録) |
| 文章から特定の項目(会社名・金額・日付など)を決まった形式で抜き出したい | Function CallingまたはStructured Outputs/JSONモード(どちらも「決まった形式で出力させる」目的では近いが、外部処理を伴わない単純な抽出ならJSONモードで十分なことも多い) |
| 複数ステップの調査・判断を自律的に繰り返させたい(AIエージェント) | Function Calling(+ループ処理)が土台となる仕組み |

判断基準はシンプルで、「モデルの学習データだけで答えられるか」「回答のために外部の最新情報や実際の操作が必要か」で分ける。後者であればFunction Callingの出番になる。

## 実務での使い方

### 最小構成のイメージ(概念コード)

以下は「都市名を渡すと天気を返す関数」を例にした、ツール定義から結果返却までの一連の流れの概念的なイメージ。OpenAIの現行の推奨インターフェースである**Responses API**に近い形で書いているが、実際のパラメータ名は使用するAPI・SDKのバージョンで異なるため、必ず各社の最新リファレンスで確認すること。

```jsonc
// 1. 開発者がツール(関数)のスキーマを定義してリクエストに含める
// (Responses APIでは "function" のネストがなく、name/description/parametersが
//  ツール定義に直接フラットに並ぶ点に注意。strict: true を付けるとスキーマに
//  完全一致した引数だけを返すようになる)
{
  "model": "(使用するモデル名)",
  "input": "東京の天気を教えて",
  "tools": [
    {
      "type": "function",
      "name": "get_weather",
      "description": "指定した都市の現在の天気を取得する",
      "strict": true,
      "parameters": {
        "type": "object",
        "properties": {
          "city": { "type": "string", "description": "都市名(例: 東京)" },
          "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
        },
        "required": ["city", "unit"],
        "additionalProperties": false
      }
    }
  ]
}

// 2. モデルは自分で天気APIを呼ぶのではなく、
//    「この関数をこの引数で呼んでほしい」という要求だけを返す
//    (output配列に type: "function_call" の要素として現れる)
{
  "output": [
    {
      "type": "function_call",
      "call_id": "call_abc123",
      "name": "get_weather",
      "arguments": "{\"city\": \"東京\", \"unit\": \"celsius\"}"
    }
  ]
}

// 3. 開発者側のコードが実際に天気APIを呼び出し、結果を得る
// (例: get_weather("東京", "celsius") -> {"temp": 29, "condition": "晴れ"})

// 4. 実行結果を「この関数呼び出しへの回答」として、直前のinputに続けて送り返す
{
  "type": "function_call_output",
  "call_id": "call_abc123",
  "output": "{\"temp\": 29, \"condition\": \"晴れ\"}"
}

// 5. モデルはこの結果を踏まえて、最終的な自然文の回答を生成する
// -> 「東京は現在晴れ、気温29度です。」
```

**旧来のChat Completions API**(`/v1/chat/completions`)では、ツール定義は`{"type": "function", "function": {"name": ..., "parameters": ...}}`のように`function`キーの中にネストする形式で、モデルからの呼び出し要求はレスポンスの`tool_calls`配列(`function.name`/`function.arguments`)、結果は`role: "tool"`のメッセージ(`tool_call_id`で紐付け)として返す。Chat Completionsは自社APIだけを呼ぶ単純な用途なら引き続き使えるが、OpenAIの組み込みツール(Web検索・コード実行・リモートMCPサーバーなど)と組み合わせて1リクエストの中でエージェント的にループさせたい場合はResponses APIが前提になる。**Assistants API**(`/v1/assistants`・`/v1/threads`)は**2026年8月26日で廃止**され、それ以降はエラーになるため、まだ使っている場合は直ちにResponses APIへの移行を進める必要がある。

AnthropicのClaudeやGoogleのGeminiでもキー名が違うだけで考え方はまったく同じ(ツールのスキーマを渡す → モデルが呼び出し要求を返す → 開発者が実行 → 結果を返す)。

### 各社での呼び方・実装の違い

| 項目 | OpenAI(Responses API) | Anthropic(Claude) | Google(Gemini) |
|---|---|---|---|
| 機能の呼称 | Function calling(APIパラメータは`tools`) | Tool use | Function calling(呼称はOpenAIと同じ) |
| ツール定義のキー | `tools`配列の要素に`type: "function"`と`name`/`description`/`parameters`をフラットに指定(旧Chat Completionsは`function`キーの中にネスト) | `tools`の中に`name`/`description`/`input_schema` | `tools`の中の`function_declarations`に`name`/`description`/`parameters` |
| モデルからの呼び出し要求 | `output`配列の`type: "function_call"`要素(`call_id`/`name`/`arguments`。argumentsはJSON文字列なのでパースが必要) | `stop_reason: "tool_use"`と`tool_use`コンテンツブロック(`name`と`input`。inputは解析済みオブジェクト) | `functionCall`(`name`と`args`)。Gemini 3系は`thoughtSignature`も併せて返る |
| 実行結果の返し方 | 次のリクエストの`input`に`type: "function_call_output"`(`call_id`と`output`)を追加 | `tool_result`コンテンツブロック(`tool_use_id`を紐付け)。複数の結果は1つの`user`メッセージにまとめる | `functionResponse`(`name`と`response`) |
| 厳密スキーマ一致の機能 | Structured Outputs(ツール定義に`strict: true`) | strict tool use(ツール定義に`strict: true`、ベータヘッダー不要) | 対応するSchema制約(サポート属性は限定的) |
| 並列ツール呼び出し | `parallel_tool_calls`パラメータで制御(既定は有効) | 既定で有効(結果は1メッセージにまとめて返す) | 対応(依存関係がなければ複数の`functionCall`が同時に返る) |
| 備考 | 旧`functions`/`function_call`トップレベルパラメータは非推奨・廃止済み。Assistants APIは2026-08-26に廃止(移行猶予なし) | 「Tool Search Tool」(`tool_search_tool_regex_20251119`/`_bm25_20251119`)で大量ツールを検索方式で扱う機能や、「Programmatic Tool Calling」「Advisor Strategy」など大規模エージェント向けの拡張を追加 | Gemini 3系はマルチターンの`functionCall`に`thoughtSignature`を含め忘れると400エラーになる。公式SDK利用時は自動処理される |

いずれのプロバイダーも同時に複数のツール呼び出しを1ターンで返す「並列ツール呼び出し」に対応しているが、処理の順序に依存関係がある場合(前の結果がないと次の関数を呼べない場合など)は、並列実行をオフにする設定を使う必要がある。

### 業務での活用例

- **社内システム連携チャットボット**: 「在庫確認」「注文状況照会」「休暇残日数の確認」などの関数を用意し、チャットボットが必要に応じて社内DB・基幹システムのAPIを呼び出して回答する
- **AIエージェントによる実行タスク**: 「カレンダーに予定を登録する」「チケット管理システムに起票する」「特定のフォーマットでメールを下書きする」といった関数をツールとして登録し、AIに実際の作業を代行させる
- **構造化データ抽出**: 契約書や問い合わせメールから「会社名・金額・希望納期」などをツール呼び出しの引数という形で抜き出させ、そのままシステムに登録する(この用途は次章で扱うJSONモード/Structured Outputsとも重なる)
- **計算・コード実行の委譲**: 計算やコード実行など、LLMが不得意な処理を専用の関数・実行環境に委譲する

### ノーコード・ローコードツールでの位置づけ

コードを書かなくても、主要ツールでは「ツール」「アクション」という名前でこの仕組みが提供されている。

| ツール | 対応する機能・設定場所 |
|---|---|
| ChatGPTのカスタムGPT | 「GPTを編集」→「設定」→「Actions」タブでOpenAPIスキーマを登録すると、Function Callingの仕組みで外部APIを呼び出す |
| Dify | ワークフロー/エージェントの「ツール」欄で、OpenAPIスキーマからカスタムツールを登録するか、既存のツールプラグインを追加する |
| GAS(Google Apps Script) | `UrlFetchApp`でモデルのAPIを呼び、返ってきた`tool_calls`/`tool_use`をコード側で判定して、社内API・スプレッドシート操作の関数を実行する分岐処理を自分で書く |
| Zapier / Make / n8n | AIアプリのステップに「アクション」を渡すことで、Function Calling相当の判断をZapier/Make側の分岐ロジックが担う場合がある |

### MCP(Model Context Protocol)との関係

MCPはFunction Callingを置き換えるものではなく、その「配線」を標準化する共通規格である。Function Callingだけで運用すると、ツールを使うモデル・アプリの組み合わせごとに個別にスキーマを定義し、実行コードを書く必要がある(ツールが10個、連携先が3つあれば30通りの実装が発生しうる)。MCPは「MCPサーバー」としてツールを1回実装しておけば、Claude・ChatGPT・その他のMCP対応クライアントから同じ形式で呼び出せるようにする、いわば「電源の規格(Function Calling)」に対する「プラグの形(MCP)」のような位置づけ。AnthropicのAPIにも「MCPコネクタ」があり、リモートのMCPサーバーに接続してツールを呼び出せる(内部的にはTool Useの仕組みの上で動いている)。

## 注意点・よくある誤解

- **モデルは引数を「それらしく」補完することがある**: 必須の情報がユーザーの発言に含まれていなくても、モデルが場所や日付などの値を勝手に推測して埋めてしまう場合がある。特に軽量・高速なモデルほどこの傾向が出やすい。関数を実行する前に、引数の値が本当に妥当か(空文字でないか、存在するIDか等)を必ずコード側で検証する。
- **引数をそのまま実行に使うのは危険**: モデルが生成した引数をSQLクエリやシェルコマンドに無検証で渡すと、インジェクションなどのセキュリティリスクにつながる。必ずバリデーション・サニタイズを行う。
- **間違ったツールを呼ぶ・不要な時に呼んでしまうこともある**: ツールの`description`(説明文)が曖昧だと、モデルが意図と異なるツールを選んでしまうことがある。ツールの説明は「いつ使うべきか」「いつ使うべきでないか」まで具体的に書くと精度が上がる。
- **実行前の安全確認(Human-in-the-loop)を軽視しない**: メール送信・決済・データ削除など取り返しのつかない操作をツール化する場合、モデルの呼び出し要求をそのまま無条件に実行するのは危険。金額や対象が一定の条件を超える場合は人間の承認を挟む、実行ログを残す、権限を最小限にするなど、セキュリティ面の設計が必須になる(この観点はセキュリティ関連のトピックで別途扱う)。
- **JSONモード/Structured Outputsとの混同**: 「決まった形式でデータを出力させたい」だけであれば、外部実行を伴わないJSONモードやStructured Outputsの方がシンプルな場合がある。外部システムへの問い合わせ・操作が必要かどうかで使い分ける。
- **料金への影響**: ツールの定義(スキーマ)自体も入力トークンとしてAPI利用料に加算される。ツールの数が多い・説明文が長いほどコストが上がる点は見落とされがちなので、必要なツールだけを都度渡すなど設計上の工夫をする。
- **OpenAIの実装は「どのAPIか」で形が変わる**: Chat Completions(ツール定義が`function`キーの中にネスト)とResponses API(フラットな構造)ではJSONの形が異なるため、他社ブログやサンプルコードをコピペする際は年式とAPIの種類を必ず確認する。新規実装ならResponses APIが基本。Assistants APIは**2026年8月26日で廃止**され、以降は`/v1/assistants`系のエンドポイントを呼ぶとエラーになる点に注意(移行猶予やAPIの縮退運用はない)。
- **「組み込みツール」を使うだけならFunction Callingの実装は不要**: Web検索・コード実行・ファイル検索など、モデル提供側の組み込みツールを使うだけなら、スキーマ定義や実行コードを自分で書く必要はなく、`tools`にツール名を指定するだけで動く。関数のスキーマ設計や実行結果の受け渡しに手間がかかるのは、あくまで自社のAPI・DBをツール化する「カスタム関数」の場合であり、両者を混同しないこと。なお自社APIだけを呼ぶ単純な用途では、組み込みツールを使わないChat Completions APIの方がトークン単価だけで済み割安なケースもある。
- **Gemini 3系のthought signature忘れによる400エラー**: raw HTTPやSDKの薄いラッパー経由で直接Gemini APIを叩いている場合、マルチターンの会話で前回の`functionCall`パートに付いていた`thoughtSignature`を次のリクエストに含め忘れると、「thought signature is required」という400エラーになる。公式のGoogle Gen AI SDKを使っていれば通常は自動処理されるが、独自にリクエストを組み立てている場合は要注意。

## 最初の一歩

すでにOpenAI・Anthropic・GeminiいずれかのAPIキーを持っているなら、天気や社内FAQなど1つだけの簡単な関数(例: 都市名から固定の天気データを返すダミー関数)を`tools`として定義し、実際にモデルが「呼び出し要求」を返してくる様子を一度手元で確認してみる。コードを書かずに試すなら、OpenAI PlaygroundやAnthropic Console(platform.claude.com)の画面上でツールを定義して挙動を観察するのが最短。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)

## 更新履歴

### 2026-08-20: 組み込みツールとの違い・Assistants API廃止の直前対応・Anthropicの大規模エージェント向け拡張を追加して最新化
- **内容**: OpenAI/Anthropicの「組み込みツール(Web検索・コード実行・リモートMCPサーバー等)」と本ページの「カスタム関数呼び出し」が別物であること、両者は同じ`tools`に混在させられることを仕組み・注意点に追記。OpenAI Assistants APIの廃止日(2026年8月26日)が執筆時点で目前に迫っており、移行猶予なくエラーになる旨を強調する形に書き直し。Anthropicの並列ツール呼び出し(`disable_parallel_tool_use`)・strict tool useの技術名(grammar-constrained sampling)を正確化。Anthropicが2025年11月以降に追加した「Programmatic Tool Calling」(ツール呼び出しをコードとしてまとめて実行)と2026年4月の「Advisor Strategy」(安価なモデルが高性能モデルに相談する仕組み)を、大規模エージェント向けの発展形として追加
- **出典**: [OpenAI Developer Community: Assistants API beta deprecation — August 26, 2026 sunset](https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666)、[OpenAI: Function calling](https://developers.openai.com/api/docs/guides/function-calling)、[OpenAI: Using tools](https://developers.openai.com/api/docs/guides/tools)、[Anthropic: Strict tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/strict-tool-use)、[Anthropic: Parallel tool use](https://platform.claude.com/docs/en/agents-and-tools/tool-use/parallel-tool-use)、[Anthropic: Tool search tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/tool-search-tool)、[Anthropic: Programmatic tool calling](https://platform.claude.com/docs/en/agents-and-tools/tool-use/programmatic-tool-calling)、[The Agent Report: Anthropic's Advanced Tool Use Platform (2026-06)](https://the-agent-report.com/2026/06/anthropic-advanced-tool-use-platform-june-2026/)

### 2026-07-22: OpenAI Responses APIとGemini 3のthought signatureを反映して最新化
- **内容**: OpenAIの標準インターフェースがResponses API(ツール定義がフラットな構造、`output`配列の`function_call`要素、`function_call_output`での結果返却)に移行した点を反映して概念コード例と各社比較表を全面改訂。Chat Completions(ネスト構造)は互換のため残っている旨と、Assistants APIが2026年8月26日に廃止予定である旨を追記。Anthropicの並列ツール呼び出しの既定値・Tool Search Toolの正式名称(`tool_search_tool_regex_20251119`/`_bm25_20251119`)を明確化。Gemini 3系で必須になった`thoughtSignature`(マルチターンで送り返さないと400エラー)を仕組み・比較表・注意点に追加
- **出典**: [OpenAI: Function calling](https://developers.openai.com/api/docs/guides/function-calling)、[OpenAI: Migrate to the Responses API](https://developers.openai.com/api/docs/guides/migrate-to-responses)、[OpenAI: New tools and features in the Responses API](https://openai.com/index/new-tools-and-features-in-the-responses-api/)、[Google AI for Developers: Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)、[Google AI for Developers: Thought signatures](https://ai.google.dev/gemini-api/docs/generate-content/thought-signatures)

### 2026-07-06: 重複ページの統合
- **内容**: 同一トピックの重複ページ `function-calling.md` を本ページに統合。ノーコード・ローコードツールでの位置づけ(カスタムGPTのActions/Dify/GAS/Zapier等)、MCPとの関係、引数のインジェクション対策、Playground/Consoleでの試し方を取り込んだ
- **出典**: [OpenAI Help Center: Function Calling in the OpenAI API](https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api)、[Model Context Protocol 公式仕様(Tools)](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)、[Descope: What Is the Model Context Protocol (MCP) and How It Works](https://www.descope.com/learn/post/mcp)

### 2026-07-05: 初版執筆
- **内容**: Function Calling(Tool Calling)の基本的な仕組み(5ステップ)、OpenAI/Anthropic/Geminiでの呼称・実装の違い、最小構成の概念コード例、業務活用例、引数のハルシネーションや実行前の安全確認などの注意点を整理
- **出典**: [OpenAI: Function calling](https://developers.openai.com/api/docs/guides/function-calling), [OpenAI Developer Community: Parallel Function Calling](https://community.openai.com/t/parallel-function-calling/626868), [Anthropic: Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview), [Anthropic: Introducing advanced tool use on the Claude Developer Platform](https://www.anthropic.com/engineering/advanced-tool-use), [Google AI for Developers: Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)
