---
title: Function Calling(Tool Use)の基本
part: 8
chapter: 第2章 API活用実践
tags: [Function Calling, Tool Use, JSON Schema, AIエージェント, API連携]
created: 2026-07-05
updated: 2026-07-05
---

# Function Calling(Tool Use)の基本

## これは何か

Function Calling(OpenAIの呼び方。Anthropicは「Tool Use」、Google Geminiは「Function calling」と呼ぶ)とは、開発者があらかじめ「こういう関数(ツール)が使えます」とAPIに登録しておくと、モデルが会話の途中で「この関数を、この引数で呼びたい」という構造化データを返してくれる仕組みのこと。天気を調べる、社内DBから注文状況を検索する、Slackにメッセージを送る、といった「AIが実際に何かを実行する」機能=AIエージェントの土台になっている。

重要な誤解ポイントとして、**モデル自身は関数を実行しない**。モデルがやるのは「この関数をこの引数で呼んでほしい」という指示(JSON形式)を返すところまでで、実際に関数(APIコールやDB検索)を実行し、その結果をモデルに送り返すのは常に開発者側のコードの役目である。

## 仕組み・背景

典型的な一往復は次の4ステップで進む。

1. **開発者がツールを定義する**: 関数の名前・説明文・引数の形式(JSON Schema)をAPIリクエストの`tools`パラメータに含めて送る
2. **モデルが呼び出しを決める**: ユーザーの発言を読み、ツールの説明文と照らして「これは関数を呼ぶべき場面だ」と判断すると、通常のテキストの代わりに「関数名+引数」という構造化データを返す(このときモデルの応答はテキスト生成ではなく停止し、呼び出し要求だけが返る)
3. **開発者側のコードが実行する**: 受け取った関数名・引数をもとに、実際のAPI・DB・社内システムを呼び出す。ここは完全に自分たちのコードの責任範囲であり、モデルは一切関与しない
4. **実行結果をモデルに返す**: 関数の戻り値(JSONなど)を会話履歴に追加してモデルに再送すると、モデルはその結果を踏まえて最終的な回答文を生成する

この「呼び出し要求→実行→結果を戻す→回答生成」のループは1回で終わるとは限らず、複数のツールを順番に(あるいは並列に)呼びながら最終回答にたどり着く「エージェント的ループ」に発展させることもできる。RAG(社内文書などを検索して回答に使う仕組み)の検索処理や、ChatGPTの「Actions」、DifyのToolノードなども、突き詰めれば同じFunction Callingの仕組みの上に作られている。

## 使いどころ・使い分け

| 状況 | 適した手段 |
|---|---|
| モデルの学習データにない最新情報・社内固有データが必要(在庫、注文状況、社内規程など) | Function Calling(必要なときだけ関数を呼んで最新データを取得) |
| AIに実際の操作をさせたい(メール送信、Slack投稿、チケット起票、DB更新など) | Function Calling |
| 出力を必ず決まったJSON形式に収めたい(項目の型・必須/任意まで保証したい) | Function Calling、または後述のStructured Outputs/JSONモード |
| 文章の要約・翻訳・下書き作成など、外部データも実行も不要な作業 | 素のプロンプトで十分(関数呼び出しは不要) |
| エンジニアがいない/コードを書きたくない | Dify・GPTsのActionsなど、ノーコードでFunction Calling相当を設定できるツール([Difyとは何か](../part09-nocode-lowcode/dify-basics.md)、[GPTsの作り方と公開設定](../part05-gpts-customization/gpts-creation-basics.md)) |
| すでにコードでAPIを直接叩いている(スクラッチ開発) | OpenAI API・Anthropic API・Gemini APIの`tools`パラメータを直接実装 |

## 実務での使い方

### 最小のツール定義例(OpenAI Chat Completions形式)

「注文番号から配送状況を調べる」関数を例にすると、次のようなJSONを`tools`パラメータに渡す。

```json
{
  "type": "function",
  "function": {
    "name": "get_order_status",
    "description": "注文番号を指定して、現在の配送ステータスを取得する",
    "parameters": {
      "type": "object",
      "properties": {
        "order_id": {
          "type": "string",
          "description": "注文番号(例: ORD-20260705-001)"
        }
      },
      "required": ["order_id"]
    }
  }
}
```

ユーザーが「注文ORD-20260705-001はどうなってる?」と聞くと、モデルは文章の代わりに`{"name": "get_order_status", "arguments": {"order_id": "ORD-20260705-001"}}`のような呼び出し要求を返す。開発者側はこれを受けて自社の受注システムを検索し、結果(例: 「発送済み、明日到着予定」)をモデルに返せば、モデルがそれを自然文の回答に整形してくれる。

### Anthropic Claude(Tool Use)の場合

Anthropicは`tools`パラメータの中で`name`・`description`・`input_schema`(JSON Schema)を指定する点がOpenAIと似ているが、キー名が`parameters`ではなく`input_schema`である点が異なる。モデルが関数を呼びたいときはテキストの代わりに`tool_use`という種類のブロックを返し、開発者はその結果を`tool_result`として会話に追加して返す。スキーマを厳密に守らせたい場合は、ツール定義に`strict: true`を追加する「Strict Tool Use」機能がある。

```json
{
  "name": "get_order_status",
  "description": "注文番号を指定して、現在の配送ステータスを取得する",
  "input_schema": {
    "type": "object",
    "properties": {
      "order_id": { "type": "string", "description": "注文番号" }
    },
    "required": ["order_id"]
  }
}
```

### 呼び方の対応表(2026年7月時点)

| 項目 | OpenAI | Anthropic Claude | Google Gemini |
|---|---|---|---|
| 機能名 | Function calling | Tool use | Function calling |
| リクエストのパラメータ名 | `tools`(`type: "function"`) | `tools` | `tools`(`function_declarations`) |
| 引数スキーマのキー名 | `parameters` | `input_schema` | `parameters`(OpenAPIスキーマのサブセット) |
| モデルからの呼び出し表現 | `tool_calls` | `tool_use`ブロック | 関数呼び出しを表す構造化レスポンス |
| 出力を厳密にスキーマ通りにする機能 | `strict: true`(Structured Outputs) | `strict: true`(Strict Tool Use) | スキーマ準拠のための各種設定 |

出力形式の細部(スキーマのキー名など)はベンダーごとに異なるが、「関数の説明とJSON Schemaを登録する→モデルが呼び出しを決める→開発者が実行して結果を返す」という基本構造は共通している。

### ノーコードで試したい場合

- **GPTs Actions**: マイGPTの設定画面から、OpenAPIスキーマ形式で外部APIを登録すると、コードを書かずにFunction Calling相当の仕組みを使える([GPTsの作り方と公開設定](../part05-gpts-customization/gpts-creation-basics.md)参照)
- **Dify**: ワークフロー機能で「ツール」ノードを組み込むと、内部的にはLLMのFunction Callingを使って外部APIやHTTPリクエストを呼び出せる([Difyとは何か](../part09-nocode-lowcode/dify-basics.md)参照)

## 注意点・よくある誤解

- **モデルは引数を「それらしく」でっち上げることがある**: 必須パラメータが会話中で明示されていない場合、モデルが推測で値を埋めて呼び出してしまうことがある(例: 都市名を聞かれていないのに「東京」と決め打ちする)。実行前に引数のバリデーション(型チェック・許容値チェック)を必ず挟む
- **破壊的な操作は人間の確認を挟む**: 「メール送信」「注文キャンセル」「本番DBの更新」のような取り消しにくい操作をモデルの判断だけで即実行させるのは危険。金額や対象を確認する承認ステップ(human-in-the-loop)を挟むのが基本
- **Function CallingとJSONモード/Structured Outputsは別物**: Structured Outputs(旧JSONモード)は「モデルの最終回答をJSON形式に固定する」機能であり、外部関数を呼ぶわけではない。「外部データの取得・実際の操作」が要るならFunction Calling、「出力の形式だけ固定したい」ならStructured Outputsで十分、と使い分ける
- **ツール定義もトークン消費の対象**: `tools`に渡した関数名・説明文・スキーマも入力トークンとしてカウントされ、料金と精度(長すぎる説明文は逆にモデルを混乱させる)の両方に影響する。ツールの数が増えるほど、似た名前・説明の関数をモデルが取り違えるリスクも上がる
- **呼ぶべきときに呼ばない/呼ばなくていいときに呼ぶ**: ツールの説明文(description)が曖昧だと、モデルが不要な場面で関数を呼んだり、逆に呼ぶべき場面で呼ばなかったりする。説明文は「いつ使うべきか」を具体的に書くと改善する

## 最初の一歩

OpenAIまたはAnthropicの開発者向けプレイグラウンド(platform.openai.com のPlayground、または console.anthropic.com)で、上記の`get_order_status`のようなダミー関数を1つ登録し、「注文ORD-001の状況を教えて」と入力して、モデルがどんな引数で呼び出しを返してくるかを実際に確認してみる。

## 関連トピック

- [OpenAI APIの基本](./openai-api-basics.md)
- [GPTsの作り方と公開設定](../part05-gpts-customization/gpts-creation-basics.md)
- [Difyとは何か](../part09-nocode-lowcode/dify-basics.md)
- [トークンとは何か](../part01-ai-llm-basics/token-basics.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: Function Calling(Tool Use)の基本メカニズム(モデルは実行せず呼び出し要求のみ返す点)、OpenAI/Anthropic/Geminiの呼称・スキーマの違い、最小のツール定義例、使いどころの判断基準、引数の誤生成や破壊的操作のリスクなど実務上の注意点を整理
- **出典**: [OpenAI API Docs: Function calling](https://developers.openai.com/api/docs/guides/function-calling)、[OpenAI Cookbook: How to call functions with chat models](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb)、[Anthropic Claude Docs: Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)、[Google AI for Developers: Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)
