---
title: Function Calling(Tool Calling)の基本
part: 8
chapter: 第2章 API活用実践
tags: [API, Function Calling, Tool Calling, 開発連携]
created: 2026-07-05
updated: 2026-07-05
---

# Function Calling(Tool Calling)の基本

## これは何か

ChatGPTやClaudeに「今日の東京の天気は?」と聞いても、モデルは天気予報サービスに繋がっていないため、学習データにある古い知識か、もっともらしい憶測でしか答えられない。Function Calling(Tool Calling、ツール呼び出し)は、この「LLMは自分の頭の中にある知識しか話せない」という制約を破り、社内DB検索・天気予報API・在庫システムなど外部の仕組みをLLMに「使わせる」ための土台となる仕組みである。

具体的には、開発者側が「こういう関数(ツール)が使えます」という一覧(名前・説明・必要な引数)をAPIリクエストに含めておくと、LLMは質問に答えるのに外部の情報や処理が必要だと判断した場合、テキストで答える代わりに「この関数をこの引数で呼んでほしい」というJSON形式の要求を返す。この要求に基づいて実際に関数(APIやDB検索など)を実行するのはあくまでアプリ側であり、LLM自身は何も実行しない。実行結果をLLMに渡すと、それを踏まえた最終回答を生成する。

## 仕組み・背景

Function Callingの処理は、開発者が組む「1往復半」のやり取りとして理解すると分かりやすい。

1. **ツール一覧を渡す**: リクエストの中に「関数名・説明・引数の型(JSON Schemaという形式で指定)」の一覧を含める
2. **LLMが呼び出し要求を返す**: LLMはユーザーの質問を読み、テキストで直接答えるべきか、ツールを使うべきかを判断する。ツールが必要と判断すると、テキストではなく「関数名+引数(JSON)」という構造化データを返す(この時点ではまだテキスト回答は生成されていない)
3. **アプリ側が実際に実行する**: 開発者が書いたコードが、その関数名と引数を受け取り、実際にAPIを呼んだりDBを検索したりする。ここでLLMは何もしていない
4. **実行結果をLLMに返す**: 実行結果を「この関数の結果はこうでした」という形でLLMに送り返す
5. **LLMが最終回答を生成する**: 結果を踏まえて、人間向けの自然文で最終回答を作る

具体例(「東京の天気は?」):

```
ユーザー: 「東京の天気は?」
   ↓
LLM: 「get_weather(city="Tokyo") を呼んでほしい」という要求を返す(テキスト回答ではない)
   ↓
アプリ: 実際に気象庁APIや天気予報サービスのAPIを呼び、「東京: 晴れ、28℃」という結果を得る
   ↓
アプリ: この結果をLLMに「function_callの結果はこうでした」と送り返す
   ↓
LLM: 「東京は現在晴れで、気温は28℃です」という最終回答を生成する
```

この一連の流れがあるため、Function Callingは「AIエージェント」と呼ばれる仕組みの中核技術になっている。エージェントは、この呼び出し→実行→回答のループを複数回・複数のツールにわたって自律的に繰り返すことで、単純な一問一答を超えた複雑なタスク(調査してから予約する、複数のシステムを横断して集計する、など)をこなす。

## 使いどころ・使い分け

| 状況 | 向いている手段 |
|---|---|
| LLMが学習データに持っていない社内情報・リアルタイム情報が必要 | Function Calling(社内DB検索・天気API・在庫システムなどを関数として渡す) |
| 大量の社内文書・マニュアルの中から関連箇所を探して回答させたい | RAG(Retrieval-Augmented Generation、検索拡張生成) |
| 「今のCPUの空き状況を確認して」「この注文をキャンセルして」のような**処理の実行**が必要 | Function Calling |
| 複数のツールを行き来しながら自律的にタスクを進めるエージェントを作りたい | Function Calling(+ ReAct等の推論戦略)がベース技術 |

**Function CallingとRAGの違い**: どちらも「LLMの外にある情報を使う」点は同じだが、RAGは基本的に「文書を検索して関連箇所をテキストとしてプロンプトに埀め込む」一方通行の情報取得であり、LLMが能動的に「いつ・何を」検索するかを都度JSONで指示することは前提としない(検索は毎回自動的に行われることが多い)。Function Callingは「LLMが状況に応じて、どの関数を・どの引数で呼ぶか」を自分で判断する点が異なり、検索だけでなく「実行」(メール送信、注文処理など)も対象にできる。実務では、RAGの検索処理自体を1つの「検索ツール」としてFunction Calling経由でLLMに呼ばせる、という組み合わせ方もよく使われる。

**Function CallingとMCP(Model Context Protocol)の関係**: MCPはAnthropicが2024年11月に提唱した、LLMとツール・データソースをつなぐための「共通規格」である。Function Calling自体は各APIごとに「ツールの一覧をリクエストに埋め込む」という仕組みだが、ツールが増えるほど、ツールごとに接続コードを個別に書く必要が出てくる。MCPは、この「ツールを提供する側(MCPサーバー)」と「LLMを使う側(MCPクライアント)」の間の通信方法を標準化し、一度MCPサーバーを立てれば複数のAIツール・複数のLLMから同じツール群を再利用できるようにするものである。関係を一言で言えば、**Function CallingはLLMが「何をすべきか」を判断する仕組み、MCPはその判断に使う「ツールをどう安全・標準的に提供するか」の配線の規格**であり、両者は競合ではなく組み合わせて使うものである。MCPの詳細は別トピックで扱う。

**ノーコードツールでの位置づけ**: DifyのようなノーコードAIアプリ構築ツールでも、同じ概念が「ツール」として提供されている。Difyの「エージェント」ノードでは、推論戦略として標準で「Function Calling」と「ReAct」(思考と行動を交互に繰り返す方式)が用意されており、どちらを選んでも「ツールリスト」に呼び出し可能なツール(社内APIをOpenAPI形式で登録したカスタムツール、Web検索、DALL-Eなど)を追加していく操作感は共通している。Function Callingはツール利用が主目的で速度・正確性を重視する場合、ReActは複雑な推論を伴う自律的な判断が必要な場合に向く、という使い分けがDifyの公式ドキュメントでも案内されている。

## 実務での使い方

### 共通の考え方

どのAPIでも、渡す情報の骨格は共通している。

- **name**: 関数の名前(英語のスネークケースが基本、例: `get_weather`)
- **description**: この関数が何をするか、いつ使うべきかの説明文。ここの書き込みが薄いとLLMが誤って呼んだり呼ぶべき時に呼ばなかったりするため、**最も精度を左右する部分**
- **parameters / input_schema**: 引数の型定義。JSON Schema(または準拠形式)で「どんな引数が必要か」を指定する

### OpenAI API(Responses API)での書き方

```python
from openai import OpenAI
client = OpenAI()

tools = [
    {
        "type": "function",
        "name": "get_weather",
        "description": "指定した都市の現在の天気と気温を取得する。都市名から実際の気象データを取得したい場合に使う。",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {"type": "string", "description": "都市名。例: Tokyo"}
            },
            "required": ["city"],
            "additionalProperties": False
        },
        "strict": True
    }
]

response = client.responses.create(
    model="gpt-5.1",  # モデル名は例。最新のモデル名は都度公式ドキュメントで確認
    input="東京の天気は?",
    tools=tools,
)
```

LLMがツールを使うべきと判断すると、`response.output` に `type: "function_call"` の要素が入り、`name`(関数名)と `arguments`(JSON文字列の引数)が入っている。アプリ側で実際に `get_weather(city="Tokyo")` を実行し、結果を次のリクエストで返す。

```python
response_2 = client.responses.create(
    model="gpt-5.1",
    previous_response_id=response.id,
    input=[
        {
            "type": "function_call_output",
            "call_id": "call_xxx",  # 直前のfunction_callのidと対応させる
            "output": "東京: 晴れ、28℃"
        }
    ]
)
```

`tool_choice` パラメータで、LLMの振る舞いを制御できる。

- `"auto"`(デフォルト): 使うかどうかLLM自身が判断
- `"required"`: 必ず何らかのツールを呼ばせる
- `"none"`: ツールを使わせない
- `{"type": "function", "name": "get_weather"}`: 特定の関数を強制的に呼ばせる

なお、旧世代のChat Completions APIでは `tools=[{"type": "function", "function": {"name": ..., "parameters": ...}}]` のように `function` オブジェクトで一段ネストする形式だった。OpenAIは機能をResponses APIに一本化する方針で、Assistants APIは2026年8月26日で終了予定のため、新規開発はResponses APIで書くのが基本になる。

### Anthropic Claude APIでの書き方

Claudeでは `input_schema` という名前を使い、実行結果は `tool_result` というブロックで返す。

```json
{
  "model": "claude-opus-4-8",
  "max_tokens": 1024,
  "tools": [
    {
      "name": "get_weather",
      "description": "指定した都市の現在の天気と気温を取得する。都市名から実際の気象データを取得したい場合に使う。",
      "input_schema": {
        "type": "object",
        "properties": {
          "city": {"type": "string", "description": "都市名。例: Tokyo"}
        },
        "required": ["city"]
      }
    }
  ],
  "messages": [
    {"role": "user", "content": "東京の天気は?"}
  ]
}
```

Claudeがツールを使うと判断すると、応答の `content` 配列に `type: "tool_use"` のブロック(`id`、`name`、`input`)が入る。アプリ側は関数を実行し、次のユーザーメッセージとして `tool_result` ブロックを送り返す。

```json
{
  "role": "user",
  "content": [
    {
      "type": "tool_result",
      "tool_use_id": "toolu_01A...",
      "content": "東京: 晴れ、28℃"
    }
  ]
}
```

`tool_choice` は4種類。

- `{"type": "auto"}`(デフォルト): 使うかどうかClaude自身が判断
- `{"type": "any"}`: 何らかのツールを必ず使わせる(どれを使うかは強制しない)
- `{"type": "tool", "name": "get_weather"}`: 特定のツールを強制
- `{"type": "none"}`: ツールを使わせない

また `strict: true` をツール定義に付けると、引数がスキーマに厳密に一致することを保証できる(2026年に追加された機能)。

### Google Gemini APIでの書き方

Geminiは関数の定義を `function_declarations` としてまとめ、`tools` に渡す。REST APIではキャメルケース(`functionDeclarations`)、Python SDK(`google-genai`)ではスネークケースで表記される。

```python
from google import genai
from google.genai import types

client = genai.Client()

get_weather = {
    "name": "get_weather",
    "description": "指定した都市の現在の天気と気温を取得する。都市名から実際の気象データを取得したい場合に使う。",
    "parameters": {
        "type": "object",
        "properties": {
            "city": {"type": "string", "description": "都市名。例: Tokyo"}
        },
        "required": ["city"]
    }
}

response = client.models.generate_content(
    model="gemini-3-flash",  # モデル名は例。最新のモデル名は都度公式ドキュメントで確認
    contents="東京の天気は?",
    config=types.GenerateContentConfig(
        tools=[types.Tool(function_declarations=[get_weather])],
        tool_config=types.ToolConfig(
            function_calling_config=types.FunctionCallingConfig(mode="AUTO")
        )
    )
)

call = response.candidates[0].content.parts[0].function_call
# call.name == "get_weather", call.args == {"city": "Tokyo"}
```

実行結果は `function_response` として、会話履歴に追加して送り返す。

```python
response_2 = client.models.generate_content(
    model="gemini-3-flash",
    contents=[
        "東京の天気は?",
        types.Content(role="model", parts=[types.Part(function_call=call)]),
        types.Content(role="user", parts=[types.Part(
            function_response=types.FunctionResponse(
                name="get_weather",
                response={"result": "東京: 晴れ、28℃"}
            )
        )]),
    ]
)
```

`function_calling_config.mode` で振る舞いを制御する。

- `"AUTO"`(デフォルト): 使うかどうかモデル自身が判断
- `"ANY"`: 必ず関数を呼ばせる(`allowed_function_names` で呼べる関数を絞り込むことも可能)
- `"NONE"`: 関数呼び出しを禁止

なお、GeminiのSDKには「モデルが関数呼び出しを返したら、SDK側が自動的に実際のPython関数を呼んで結果をモデルに戻す」自動関数実行(Automatic Function Calling)という便利機能もあり、`Chat` オブジェクト経由で使うと1〜5の往復を意識せず1回の呼び出しで済ませられる。

### ツール横断の対応付け(まとめ)

| 概念 | OpenAI (Responses API) | Anthropic Claude | Google Gemini |
|---|---|---|---|
| ツール一覧を渡すパラメータ | `tools`(`type: "function"`) | `tools` | `tools`(`function_declarations`) |
| 引数のスキーマ | `parameters`(JSON Schema) | `input_schema`(JSON Schema) | `parameters`(OpenAPI準拠スキーマ) |
| モデルからの呼び出し要求 | `function_call`(`arguments`はJSON文字列) | `tool_use`(`input`はオブジェクト) | `function_call`(`args`はオブジェクト) |
| 実行結果の返送 | `function_call_output` | `tool_result` | `function_response` |
| 呼び出し制御パラメータ | `tool_choice`: `auto` / `required` / `none` / 特定関数指定 | `tool_choice`: `auto` / `any` / `tool` / `none` | `function_calling_config.mode`: `AUTO` / `ANY` / `NONE` |
| 厳密なスキーマ準拠 | `strict: true` | `strict: true`(ツール定義に付与) | (スキーマ自体をシンプルに保つのが基本) |

### ノーコードツール(Dify)での対応

- Difyの「エージェント」ノードで推論戦略に「Function Calling」または「ReAct」を選択し、「ツールリスト」に呼び出し可能なツール(組み込みツール、または自社APIをOpenAPI形式で登録したカスタムツール)を追加する
- 裏側では上記のOpenAI/Claude/Gemini等のFunction Calling APIをDifyが呼び出しており、開発者はJSON Schemaを自分で書かずに画面上のフォームでツールを定義できる

## 注意点・よくある誤解

- **LLMは関数を「実行」しない**: LLMが返すのは「この関数をこの引数で呼びたい」という要求(JSON)だけであり、実際にAPIを叩いたりDBを更新したりするのはアプリ側のコードである。この境界を誤解すると、「LLMに直接社内システムを操作させている」という誤った(そして危険な)前提でセキュリティ設計をしてしまう。
- **description(説明文)の質がすべてを左右する**: 関数名や引数名だけでは、LLMは「いつ使うべきか」「使ってはいけない場合」を正しく判断できない。Anthropicの公式ガイドも「ツールの説明は3〜4文以上を目安に、何をするか・いつ使うべきか・使うべきでない場合・引数の意味・注意点まで書く」ことを推奨している。
- **危険な操作は必ず人の確認を挟む**: 注文のキャンセル・決済・メール送信など取り消しにくい操作を関数化する場合は、LLMの呼び出し要求を無条件に実行せず、確認ステップやアクセス制御を挟むこと。
- **ツールが多すぎると選択精度が落ちる**: 似たようなツールを大量に並べると、LLMがどれを使うべきか迷い、誤ったツールを呼びやすくなる。関連する操作は1つのツールに`action`パラメータで束ねるなど、ツールの数を絞る工夫が有効(Anthropicもこれをベストプラクティスとして案内している)。
- **API・SDKのバージョンによって呼び方が変わる**: 特にOpenAIは旧Chat Completions API(`function`オブジェクトでネスト)と新Responses API(フラットな構造)で細部が異なり、Assistants APIは2026年8月に終了予定。学習・実装時は必ず現在推奨されているAPIのドキュメントで確認する。

## 最初の一歩

OpenAI・Claude・Geminiいずれかの公式クイックスタートに載っている「天気を取得する」ようなサンプルの関数を1つだけ用意し、実際にAPIへリクエストを送って「function_call/tool_use」の応答が返ってくることを確認してみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: Function Calling(Tool Calling)の仕組み、業務での重要性、OpenAI/Claude/Geminiでの呼び方の対応付け、RAG・MCPとの関係、Difyでの位置づけを整理
- **出典**: [OpenAI API: Function calling](https://developers.openai.com/api/docs/guides/function-calling)、[Claude Platform Docs: Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/implement-tool-use)、[Google Gemini API: Function calling](https://ai.google.dev/gemini-api/docs/function-calling)、[google-gemini/cookbook: Function_calling.ipynb](https://github.com/google-gemini/cookbook/blob/main/quickstarts/Function_calling.ipynb)、[Dify Docs: エージェント](https://docs.dify.ai/ja/use-dify/nodes/agent)、[Neon Blog: What's MCP all about? Comparing MCP with LLM function calling](https://neon.com/blog/mcp-vs-llm-function-calling)
