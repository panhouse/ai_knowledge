---
title: Function Calling(Tool Use)の基本
part: 8
chapter: 第2章 API活用実践
tags: [Function Calling, Tool Use, API連携, AIエージェント]
created: 2026-07-05
updated: 2026-07-05
---

# Function Calling(Tool Use)の基本

## これは何か

LLM(大規模言語モデル)は学習データの範囲でしか「知らない」ため、単体では「今日の天気」「社内システムの在庫数」といった最新情報を取得できず、「会議室を予約する」「メールを送る」といった外部システムの操作もできない。Function Calling(OpenAIの呼び方)/Tool Use(Anthropicの呼び方)は、この壁を越えるための仕組みで、LLMに「今の質問に答えるにはこの関数(ツール)をこの引数で呼び出すべきだ」と判断させる。ただし実際にその関数を実行するのはLLMではなく、開発者が用意したアプリケーション側のプログラムである。この「モデルが考え、アプリが手を動かす」という役割分担が最大のポイントで、AIエージェントや社内システム連携を組む際の土台になる。

## 仕組み・背景

やり取りの流れは次の4ステップ。

1. 開発者が「使える関数(ツール)の一覧」を、名前・説明・引数の型をJSON Schemaという形式でモデルに渡す
2. モデルはユーザーの発言を見て、ツールを使うべきか、使うならどの関数にどんな引数を渡すべきかを判断する
3. モデルは関数を実際には実行せず、「この関数をこの引数で呼びたい」という構造化されたリクエスト(JSON)だけを返す
4. アプリ側のプログラムがそのリクエストを受け取って実際に処理(API呼び出し・DB検索・予約実行など)を行い、結果をもう一度モデルに渡す。モデルはその結果を踏まえて自然な文章で最終回答を生成する

ツールの定義は、たとえば「指定した都市の天気を取得する関数」であれば次のようなJSON(OpenAI形式に近いイメージ)になる。

```json
{
  "name": "get_weather",
  "description": "指定した都市の現在の天気を取得する",
  "parameters": {
    "type": "object",
    "properties": {
      "location": { "type": "string", "description": "都市名(例: 東京)" },
      "unit": { "type": "string", "enum": ["celsius", "fahrenheit"] }
    },
    "required": ["location"]
  }
}
```

- **名前(name)**: 関数の識別子。モデルはこの名前でどの関数を呼ぶかを指定する
- **説明(description)**: 「いつ・何のために使う関数か」をモデルに伝える文章。ここが曖昧だと誤った場面で呼ばれたり、逆に必要な場面で呼ばれなかったりする
- **引数の定義(parameters / properties)**: 引数の型・必須かどうか・許される値(enum)などをJSON Schemaで指定する

OpenAIとAnthropicでは呼び方・JSONの細部の名称が異なる(意味はほぼ同じ)。

| 項目 | OpenAI(Function Calling) | Anthropic(Tool Use) |
|---|---|---|
| 引数スキーマのキー名 | `parameters` | `input_schema` |
| モデルの返答の種類 | `tool_calls`(`function.arguments`はJSON文字列) | `tool_use`ブロック(`input`は解析済みオブジェクト) |
| 実行結果を返す形式 | `role: "tool"` のメッセージ | `tool_result` コンテンツブロック |
| 厳密なスキーマ一致を強制する機能 | Structured Outputs(`strict: true`) | Strict tool use(`strict: true`) |

## 使いどころ・使い分け

| やりたいこと | Function Calling / Tool Useが向いている | 向いていない・不要 |
|---|---|---|
| 最新の天気・株価・在庫数など、都度変わる情報を取得したい | ○(APIやDBを叩く関数を呼ばせる) | - |
| 社内システム(顧客DB・ナレッジベース)を検索して回答に反映したい | ○ | 検索結果を貼るだけで十分ならRAG(検索拡張生成)の方がシンプルな場合もある |
| 会議室予約・メール送信・チケット発行など「実行」を伴う操作をさせたい | ○(実行系はFunction Calling/Tool Useでないと原理的にできない) | - |
| 出力をJSON等の決まった形式に整えたいだけ(外部関数は呼ばない) | △ | Structured Outputs / JSONモードの方が単純で確実 |
| 学習データの範囲内で答えられる一般知識の質問 | 不要 | 素のプロンプトで十分 |

判断の軸は「情報を取得するだけか、それとも何かを実行する必要があるか」。取得だけならRAGや検索ツールでも代替できるが、予約・送信・登録のような「実行」を含む業務フローはFunction Calling/Tool Use(またはそれを土台にしたAIエージェント)でなければ実現できない。

## 実務での使い方

### API(OpenAI/Anthropic)での基本形

- **OpenAI**: リクエストの `tools` パラメータに `{"type": "function", "function": {"name": ..., "description": ..., "parameters": {...}}}` の形で関数を並べて渡す。モデルが呼びたいと判断すると、レスポンスの `tool_calls` に関数名と引数(JSON文字列)が入って返ってくるので、自分のコードでその関数を実行し、結果を `role: "tool"` のメッセージとして会話履歴に追加してもう一度モデルを呼ぶ
- **Anthropic**: `tools` パラメータに `{"name": ..., "description": ..., "input_schema": {...}}` の形で渡す。モデルは `stop_reason: "tool_use"` とともに `tool_use` ブロックを返すので、実行結果を `tool_result` コンテンツブロックとして返す

### ノーコード・ローコードツールでの位置づけ

| ツール | 対応する機能・設定場所 |
|---|---|
| ChatGPTのカスタムGPT | 「GPTを編集」→「設定」→「Actions」タブでOpenAPIスキーマを登録すると、Function Callingの仕組みで外部APIを呼び出す |
| Dify | ワークフロー/エージェントの「ツール」欄で、OpenAPIスキーマからカスタムツールを登録するか、既存のツールプラグインを追加する |
| GAS(Google Apps Script) | `UrlFetchApp`でモデルのAPIを呼び、返ってきた`tool_calls`/`tool_use`をコード側で判定して、社内API・スプレッドシート操作の関数を実行する分岐処理を自分で書く |
| Zapier / Make / n8n | AIアプリのステップに「アクション」を渡すことで、Function Calling相当の判断をZapier/Make側の分岐ロジックが担う場合がある |

### 典型的な業務ユースケース

- 天気・ニュース・株価など外部APIから最新情報を取得して回答に反映する
- 社内のFAQ・マニュアル・顧客DBを検索する関数を呼び、検索結果を根拠に回答させる
- 会議室予約・在庫確認・チケット発行など、社内システムのAPIを実行してタスクを完了させる
- 計算やコード実行など、LLMが不得意な処理を専用の関数・実行環境に委譲する

### MCP(Model Context Protocol)との関係

MCPはFunction Calling/Tool Useを置き換えるものではなく、その「配線」を標準化する共通規格である。Function Calling/Tool Useだけで運用すると、ツールを使うモデル・アプリの組み合わせごとに個別にスキーマを定義し、実行コードを書く必要がある(ツールが10個、連携先が3つあれば30通りの実装が発生しうる)。MCPは「MCPサーバー」としてツールを1回実装しておけば、Claude・ChatGPT・その他のMCP対応クライアントから同じ形式で呼び出せるようにする、いわば「電源の規格(Function Calling)」に対する「プラグの形(MCP)」のような位置づけ。AnthropicのAPIにも「MCPコネクタ」があり、リモートのMCPサーバーに接続してツールを呼び出せる(内部的にはTool Useの仕組みの上で動いている)。

## 注意点・よくある誤解

- **「設定すればAIが直接何でもできる」わけではない**: 実行するのは常にアプリ側のコード。権限管理・認証・実行結果の妥当性チェックはすべて開発者側の責任として残る
- **引数をそのまま実行に使うのは危険**: モデルが生成した引数をSQLクエリやシェルコマンドに無検証で渡すと、インジェクションなどのセキュリティリスクにつながる。必ずバリデーション・サニタイズを行う
- **description・引数名が曖昧だと誤作動する**: 説明が不十分だと、不要な場面でツールを呼んだり、必須パラメータが無くても値を勝手に推測(ハルシネーション気味に補完)したりする。用途・引数の意味は具体的に書く
- **ツール定義自体もトークン課金の対象**: `tools`に渡す名前・説明・スキーマは毎回の入力トークンとして課金される。ツール数が多いほどコストが増えるため、常時渡すツールは必要最小限に絞る
- **並列呼び出し・複数ターンの制御が必要**: 1回の応答で複数のツールを同時に呼ぶ「並列ツール呼び出し」に対応する設計にしておかないと、複数の質問を一度にされた際に取りこぼしが起きる

## 最初の一歩

OpenAI PlaygroundかAnthropic Console(platform.claude.com)で、`get_weather`のようなシンプルなツールを1つ定義し、実際にモデルがどのようなJSONで「この関数を呼びたい」と返してくるかを見てみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: Function Calling(OpenAI)/Tool Use(Anthropic)の基本的な仕組み、JSON Schemaによる関数定義、典型的な業務ユースケース、ノーコードツールでの位置づけ、MCPとの関係を整理
- **出典**: [OpenAI Function calling ガイド](https://developers.openai.com/api/docs/guides/function-calling)、[OpenAI Help Center: Function Calling in the OpenAI API](https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api)、[Anthropic: Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)、[Anthropic: Introducing advanced tool use](https://www.anthropic.com/engineering/advanced-tool-use)、[Model Context Protocol 公式仕様(Tools)](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)、[Descope: What Is the Model Context Protocol (MCP) and How It Works](https://www.descope.com/learn/post/mcp)
