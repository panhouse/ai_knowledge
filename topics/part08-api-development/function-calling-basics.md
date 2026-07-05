---
title: Function Calling(関数呼び出し)の基本
part: 8
chapter: 第2章 API活用実践
tags: [Function Calling, API, OpenAI API, ツール利用]
created: 2026-07-05
updated: 2026-07-05
---

# Function Calling(関数呼び出し)の基本

## これは何か

生成AIに「今日の東京の天気は?」「この注文番号の配送状況は?」のように、自社システムや外部サービスが持つ最新情報・個別データを答えさせたいことがある。しかしAIモデル自身は学習時点の知識しか持たず、社内DBや外部APIの中身をリアルタイムには知らない。Function Calling(関数呼び出し)は、AIに「この質問に答えるにはどの関数(あらかじめ用意した処理)を、どんな引数で呼べばよいか」を判断・出力させる仕組みで、AIと外部システムを安全に橋渡しする土台になる。実際に関数を実行するのはAIではなく開発者側のプログラムであり、AIは「呼び出し指示(JSON形式のデータ)」を作るところまでを担う。

## 仕組み・背景

流れは次の4ステップで理解すると分かりやすい。

1. **ツール定義を渡す**: 開発者が「どんな関数が使えるか」を、名前・説明・引数の形式をJSON Schema(データの構造を定義するJSON=データをやり取りするための軽量なテキスト形式、のルール)で書いてAPIに渡す。例:「`get_weather`という関数があり、引数として`city`(都市名)を取る」。
2. **AIが呼び出しを判断**: ユーザーの質問を見て、AIが「この質問に答えるには`get_weather`を`city: "東京"`で呼ぶべきだ」と判断し、通常の文章の代わりにその指示をJSON形式で返す。AI自身は関数を実行しない。
3. **開発者側が実際に実行**: アプリ側のプログラムがそのJSONを受け取り、実際に天気APIを呼び出して結果(気温・降水確率など)を取得する。
4. **結果をAIに戻して最終回答を作らせる**: 実行結果を再びAIに渡すと、AIがそれを踏まえて自然な文章の回答を生成する。

つまりFunction Callingは「AIに外部の力を使わせる」というより、「AIに“何をすべきか”を構造化データで指示させ、実行は人間が書いたプログラムに委ねる」仕組みである。この構造化された出力を強制する関連機能として、OpenAIには「Structured Outputs」(出力の形式をJSON Schema通りに厳密に固定する機能)があり、Function Callingの引数出力の正確性を高めるためによく併用される。

## 使いどころ・使い分け

Function Callingが向くのは「AIに“判断”と“行動の呼び出し”をさせたい」場面で、社内文書を検索させて根拠付きで答えさせたいだけならRAG(検索拡張生成=文書を検索してAIに読ませてから回答させる仕組み)の方が適している。両者は併用されることも多い(検索も1つの「関数」としてFunction Callingで呼び出すケースがある)。

| 観点 | Function Calling | RAG(検索拡張生成) |
|---|---|---|
| 主な用途 | 外部システムの操作・最新データの取得・計算処理の実行 | 社内文書・マニュアルなど蓄積された情報からの回答 |
| データの性質 | リアルタイム・可変(在庫数、天気、予約状況など) | 比較的静的なドキュメント群 |
| AIの役割 | 「何をすべきか」を判断し引数を組み立てる | 検索結果を要約・引用して回答文を作る |
| 実行されるもの | あらかじめ定義した関数・API | ベクトル検索などによる文書検索 |
| 向かない例 | 大量の非構造テキストからの知識検索 | リアルタイムの数値取得や外部操作 |

具体的にFunction Callingが向くケース:
- 「見積もりを計算して」「カレンダーに予定を入れて」のように外部システムを操作させたいとき
- 天気・為替・在庫数・配送状況など、都度変わる情報をAPI経由で取らせたいとき
- ユーザーの自然な日本語の質問を、社内APIが要求する厳密なパラメータ形式に変換させたいとき

向かないケース:
- 単に長い文書を要約・検索させたいだけ(RAGで十分)
- 実行結果の正確性を100%保証したい高リスク処理(送金など)を、人の確認なしに自動実行させる設計(誤判定のリスクがあるため、必ず人の承認ステップを挟むべき)

## 実務での使い方

### 最小構成のJSON Schema例

天気を調べる`get_weather`という関数をAIに使わせたい場合、次のようなツール定義をAPIに渡す(OpenAI APIの`tools`パラメータの書式に準拠した例)。

```json
{
  "type": "function",
  "function": {
    "name": "get_weather",
    "description": "指定した都市の現在の天気を取得する",
    "parameters": {
      "type": "object",
      "properties": {
        "city": {
          "type": "string",
          "description": "天気を調べたい都市名(例: 東京)"
        }
      },
      "required": ["city"]
    }
  }
}
```

ユーザーが「東京の天気を教えて」と入力すると、AIは文章の代わりに次のような呼び出し指示を返す。

```json
{
  "name": "get_weather",
  "arguments": { "city": "東京" }
}
```

これを受け取ったアプリ側が実際の天気APIを呼び出し、結果(例: `{"temp": 29, "condition": "晴れ"}`)をAIに返すと、AIが「東京は現在29度で晴れです」といった最終回答を生成する。

### ツール横断の対応付け

同じ考え方でも、API・ツールごとに呼び名やパラメータ名が異なる。開発者に依頼する際は下表の用語で会話すると齟齬が減る。

| ツール・API | 呼び名 | APIでの主な指定箇所 | 備考 |
|---|---|---|---|
| OpenAI API | Function calling(ガイド名は「Function calling」のまま) | `tools`パラメータに関数定義を配列で渡す | `strict: true`でStructured Outputsを併用すると引数の型が厳密に守られる |
| Anthropic Claude API | Tool use(ツール利用) | `tools`パラメータ | Web検索・コード実行などAnthropic提供の「サーバーツール」と、自作の「クライアントツール」を区別して扱う |
| Google Gemini API | Function calling | `tools`内に関数定義(OpenAPIスキーマ形式)を渡す | Gemini 3系ではストリーミングでの引数出力(`streamFunctionCallArguments`)にも対応 |
| OpenAI GPTs(ノーコード) | Actions(アクション) | GPT編集画面の「Actions」セクションにOpenAPIスキーマを貼り付け | 裏側の仕組みはFunction Callingそのもの。GPTがユーザーの質問からどのAPIを呼ぶか・どんなJSONを送るかを自動判断する |
| Dify | ツール(Tools)/ Agentノードの「Function Calling」戦略 | ワークフローの「Agent」ノードでツールを追加し、モデルの推論戦略として「Function Calling」を選択 | GPT-4やClaudeなどネイティブに関数呼び出しに対応したモデルでの利用を想定 |

料金面では、Function Calling自体に追加料金が発生するわけではなく、ツール定義や呼び出し結果もすべて入力・出力トークンとしてAPI利用料に加算される点に注意する。ツール定義の`description`を書き込みすぎると、それだけでトークン消費が増えるため、必要十分な説明文に留めるのがコスト最適化のコツになる。

## 注意点・よくある誤解

- **AIが直接コードを実行しているわけではない**という誤解が多い。AIは「呼び出したい関数名と引数」を提案するだけで、実行の可否・実際の処理はすべて開発者側のプログラム(またはノーコードツールの内部処理)が担う。この境界を理解していないと、セキュリティ設計を誤る。
- **外部関数実行のリスク**: 送金・削除・外部送信のような不可逆・高リスクな操作を関数として公開する場合、AIの判断ミスや悪意あるプロンプト(プロンプトインジェクション)によって意図しない呼び出しが行われる可能性がある。重要な操作は必ず人の承認ステップ(確認画面など)を挟む、権限を最小限にする、といった対策が必須。
- **関数の説明文(description)の質が精度を左右する**: 関数名やパラメータの説明が曖昧だと、AIが誤った関数を選んだり、引数を取り違えたりする。「いつ使うべきか」を具体的に書くほど呼び出し精度が上がる。
- **並列呼び出しとStructured Outputsの併用に制限がある場合がある**: OpenAI APIでは、Structured Outputs(`strict: true`)を使う場合、複数関数を同時に呼び出す並列呼び出し(`parallel_tool_calls`)を無効にする必要があるなど、機能同士の相性に制約があるため、公式ドキュメントで最新の制約を確認してから設計するとよい。
- **ノーコードでも仕組みは同じ**: GPTsのActionsやDifyのAgentノードを使う場合も、裏側ではFunction Callingと同じ仕組みが動いている。エンジニアに依頼せず自分で試す場合も、「関数の説明文をどう書くか」がAPIを直接使う場合と同様に精度を左右する。

## 最初の一歩

自分のGPTs(GPT Editor)の「Actions」セクション、またはDifyの「Agent」ノードで、シンプルな1つの関数(例: 天気取得やスプレッドシート検索)を試しに定義し、説明文を変えながら呼び出し精度がどう変わるかを観察してみる。

## 関連トピック
- [OpenAI APIの基本](./openai-api-basics.md)
- [GPTsの作り方と公開設定](../part05-gpts-customization/gpts-creation-basics.md)
- [Difyとは何か](../part09-nocode-lowcode/dify-basics.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: Function Callingの仕組み(4ステップの流れ)、RAGとの使い分け、JSON Schemaによる最小定義例、OpenAI/Claude/Gemini/GPTs/Difyでの用語対応表、セキュリティ上の注意点を執筆
- **出典**: [Function calling | OpenAI API](https://developers.openai.com/api/docs/guides/function-calling)
- **出典**: [Using tools | OpenAI API](https://developers.openai.com/api/docs/guides/tools)
- **出典**: [Structured model outputs | OpenAI API](https://developers.openai.com/api/docs/guides/structured-outputs)
- **出典**: [Tool use with Claude - Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)
- **出典**: [Function calling with the Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/function-calling)
- **出典**: [GPT Actions | OpenAI](https://developers.openai.com/api/docs/actions/introduction)
- **出典**: [Configuring actions in GPTs | OpenAI Help Center](https://help.openai.com/en/articles/9442513-configuring-actions-in-gpts)
- **出典**: [Agent - Dify Docs](https://docs.dify.ai/en/use-dify/nodes/agent)
