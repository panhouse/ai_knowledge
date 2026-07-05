---
title: Function Calling(Tool Use)の基本
part: 8
chapter: 第2章 API活用実践
tags: [Function Calling, Tool Use, API, MCP, ノーコード連携]
created: 2026-07-05
updated: 2026-07-05
---

# Function Calling(Tool Use)の基本

## これは何か

ChatGPTやClaudeに「今日の東京の天気は?」「このスプレッドシートの最新の売上を教えて」と聞くと、「リアルタイムの情報にはアクセスできません」「その情報は把握していません」と返ってくることがある。AIモデル自体は学習時点の知識しか持たず、外部のAPIや社内データベースに自力でアクセスすることはできないためだ。

**Function Calling**(OpenAI・Google Geminiでの呼称)/ **Tool Use**(Anthropic Claudeでの呼称)は、この壁を越えるための仕組みで、AIに「こういう機能(関数・API・DB検索など)が使えます」と教えておき、必要に応じてAIがその機能を呼び出す(正確には「呼び出したい」とリクエストする)ことを可能にする。天気API・社内システム・電卓・検索エンジンなどをAIに"手足"として持たせるイメージで、DifyやMakeのようなノーコードツールで「AIエージェント」を作るときの中核機能でもある。

## 仕組み・背景

まず押さえておくべき大原則: **AIモデル自身は外部システムに直接接続できない**。実際に関数を実行するのは、常に開発者側(あるいはノーコードツール側)のプログラムである。やり取りは以下のような往復(ラウンドトリップ)で進む。

1. 開発者が「使える関数一覧」をAIへのリクエストに含める(関数名・説明・受け取る引数の型を、JSON Schemaという形式で定義する)
2. ユーザーが「東京の天気は?」のように質問する
3. AIは自分の知識で答えられないと判断すると、文章の代わりに「`get_weather`という関数を `{"city": "東京"}` という引数で呼びたい」という構造化データを返す(この時点でAIは何も実行していない)
4. 開発者側のプログラムがそのリクエストを受け取り、実際に天気APIを呼び出す
5. 実行結果(例: 「東京、晴れ、28℃」)を開発者側がAIに送り返す
6. AIがその結果を踏まえて、ユーザー向けの自然な文章の最終回答を作る

この2〜6のやり取りは、必要なら複数回繰り返される(1回の回答のために複数の関数を呼ぶ、前の結果を見てさらに別の関数を呼ぶ、など)。この「AIが考える→ツールを呼ぶ→結果を見てまた考える」ループを自動的に回す仕組みが、いわゆる「AIエージェント」の基本動作でもある。

## 使いどころ・使い分け

| やりたいこと | Function Calling / Tool Useが必要か |
|---|---|
| 文章の要約・翻訳・下書き作成・アイデア出し | 不要(AIの知識と言語能力だけで完結) |
| 一般的な知識に基づく質疑応答・壁打ち相談 | 不要 |
| 天気・株価・為替・最新ニュースなどリアルタイム情報の取得 | 必要(外部APIから最新値を取ってくる) |
| 自社のCRM・スプレッドシート・DBの最新データを参照した回答 | 必要(社内システムへの問い合わせ) |
| 正確な計算(桁数の大きい四則演算、日付計算など) | 必要(AIは計算を"文章生成"として行うため間違えやすく、電卓関数を呼ばせた方が確実) |
| 「会議室を予約して」「チケットを起票して」等、何かを実行させたい | 必要(実行系のAPI・関数を呼ばせる) |
| 社内文書の内容をもとに質問に答えたい(検索拡張) | RAG(検索拡張生成)と組み合わせるのが一般的。検索処理自体を「関数」として呼ばせる実装も多い |

判断基準はシンプルで、「その回答に、AIの学習データにない・変化する・実行が必要な情報や操作が絡むか」で考えるとよい。絡むならFunction Calling/Tool Useの出番、絡まないなら素のチャットで十分。

## 実務での使い方

### ツール横断の対応付け

| 概念 | OpenAI API | Anthropic Claude API | Google Gemini API | Dify | n8n | Make |
|---|---|---|---|---|---|---|
| 呼び方 | Function Calling | Tool Use | Function Calling | 「ツール」/ Agent機能 | AI Agentノードの「Tool」 | 「AI Agents」のModule tools |
| 定義する場所 | リクエストの `tools` パラメータ(JSON Schema) | リクエストの `tools` パラメータ(`input_schema`) | `tools` の `function_declarations`(OpenAPIスキーマ形式) | 「ツール」→「カスタム」でOpenAPI/Swaggerスキーマを登録、またはAgentノードに追加 | AI AgentノードにHTTP Request等のノードをToolとして接続 | AI Agentのシナリオに「Module tool」としてアプリ(HTTP・Google Sheets等)を追加 |
| AIからの呼び出し結果 | `tool_calls`(関数名+引数) | `tool_use` コンテンツブロック(名前+`input`) | `functionCall`(名前+`args`) | 内部で自動処理 | 内部で自動処理 | 内部で自動処理 |
| 実行結果の返し方 | `role: "tool"` メッセージ | `tool_result` コンテンツブロック | `functionResponse` | 内部で自動処理 | 内部で自動処理 | 内部で自動処理 |

Dify・n8n・Makeのようなノーコードツールでは、上記の「往復」のプログラム部分(実行と結果の受け渡し)をツール側が自動でやってくれる。人間が設定するのは「どんな関数/APIが呼べるか」の定義だけ、というのが実務上のポイント。

### ノーコードツールでの設定の一般的な流れ

1. 呼び出したい外部サービス(天気API、社内システムのAPI、Google Sheets等)のAPIキー・認証情報を、ノーコードツールの認証設定画面に登録する
2. 「ツール」「Agentのツール」「Module tool」といった名称の設定画面で、呼び出すエンドポイント(URL)・パラメータ・戻り値の形式を定義する。多くのツールはOpenAPI(旧Swagger)形式のスキーマをインポートできる
3. AIエージェント本体(チャットボットやワークフロー)にそのツールを紐づけ、「こういう場合にこのツールを使ってください」という説明文(description)を付ける。この説明文の書き方でAIが正しくツールを選べるかが大きく変わる
4. テスト実行し、想定したツールが想定した引数で呼ばれるかを確認する

### コピペで使える関数定義の例(JSON Schema)

天気を取得する関数を定義する場合の例。OpenAI API(Responses API)・Dify・n8nのカスタムツール設定など、JSON Schemaで関数を記述する場面でベースとして流用できる。

```json
{
  "type": "function",
  "name": "get_weather",
  "description": "指定した都市の現在の天気と気温を取得する。ユーザーが天気・気温について尋ねたときに使う。",
  "parameters": {
    "type": "object",
    "properties": {
      "city": {
        "type": "string",
        "description": "天気を調べたい都市名(例: 東京、大阪)"
      },
      "unit": {
        "type": "string",
        "enum": ["celsius", "fahrenheit"],
        "description": "気温の単位。指定がなければcelsius(摂氏)を使う"
      }
    },
    "required": ["city"]
  }
}
```

Anthropic Claude API(Tool Use)では、この`parameters`が`input_schema`という名前になるだけで、中身の書き方(JSON Schemaで型・説明・必須項目を書く)はほぼ共通している。OpenAIの旧Chat Completions APIでは、この定義全体が`{"type": "function", "function": {...}}`のようにさらに1階層ネストされる点だけ違いがあるため、参考にするサンプルコードがどちらの形式かは確認するとよい。

### MCPとの関係(概要)

**MCP(Model Context Protocol、AIとツール・データソースをつなぐための共通規格)**は、このFunction Calling/Tool Useの考え方を一歩進めたものだ。従来はOpenAI用に作った関数定義はClaude用にそのまま使えない、というようにツールの定義がAIベンダーごとにバラバラだった。MCPは「AIとツールをつなぐ配線」を標準化し、一度MCPサーバーとして作ったツールを、対応する複数のAI・アプリから共通で呼び出せるようにする規格である。n8nのAI AgentノードもMCPサーバー・クライアントに公式対応するなど、ノーコードツール側の対応も進んでいる。MCPの詳細な仕組みや導入方法はPart 8第4章で別途扱う。

## 注意点・よくある誤解

- **「AIが関数を呼んだ」わけではない**: AIが返すのはあくまで「この関数をこの引数で呼びたい」という提案(構造化データ)であり、実際にAPIを叩いたりDBを更新したりするのは呼び出し側(開発者のプログラム、あるいはノーコードツールの実行エンジン)である。AIが外部システムに直接接続しているわけではない、という理解を誤解しないこと。
- **破壊的な操作は確認フローを挟む**: 「メールを送る」「レコードを削除する」「決済を実行する」のような取り消せない操作を関数として渡す場合、AIの判断だけで即実行させず、人間の承認ステップを挟む・実行前に確認メッセージを出すといった安全策を設計に入れる。権限管理を怠ると、AIの誤判断や悪意あるプロンプト(プロンプトインジェクション)によって意図しない操作が実行されるリスクがある。
- **ツールの説明文(description)の質が精度を左右する**: 関数名や説明があいまいだと、AIが誤ったツールを選んだり、必要なのに呼ばなかったりする。「いつ使うべきか」を説明文に具体的に書くことが実務上のコツ。
- **対応モデル・料金は一様ではない**: Function Calling/Tool Useは主要な最新モデルでは標準対応だが、軽量・旧世代モデルでは対応状況が異なる場合がある。またAnthropic APIでは、ツール定義自体もトークンとしてリクエストに含まれるため、ツールの数や説明文の長さが増えるほど入力トークン数(≒料金)が増える点は覚えておく。
- **並列呼び出し(parallel tool calls)に対応するモデルもある**: 1回のリクエストで複数のツールを同時に呼べるモデルもあれば、逐次的にしか呼べないモデルもある。ツールの実行順序に依存関係がある場合は、並列呼び出しの挙動を必ずテストする。

## 最初の一歩

Difyのアプリ設定画面で「ツール」タブを開き、天気APIのようなシンプルな無料APIを1つ「カスタムツール」として登録し、チャットボットに「今日の天気を聞かれたらこのツールを使って」と指示を与えて、実際にAIがツールを呼び出す様子を1回体験してみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)
- [Claude(Anthropic)の基本](../part07-other-llm-tools/claude-basics.md)
- [Difyの基本](../part09-nocode-lowcode/dify-basics.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: Function Calling(OpenAI/Gemini)とTool Use(Anthropic Claude)の基本的な仕組み・呼び出しの往復フロー、ツール横断の対応付け(OpenAI/Claude/Gemini/Dify/n8n/Make)、コピペ用のJSON Schema例、MCPとの関係、注意点(実行主体の誤解・権限管理)を整理
- **出典**: [Anthropic Claude Platform Docs: Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)、[OpenAI API: Function calling](https://developers.openai.com/api/docs/guides/function-calling)、[Google AI for Developers: Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)、[Model Context Protocol 公式サイト](https://modelcontextprotocol.io/specification/2025-11-25)、[Dify Docs: ツール](https://docs.dify.ai/ja-jp/guides/tools)、[Make Help Center: Module tools for AI agents](https://help.make.com/module-tools-for-ai-agents)
