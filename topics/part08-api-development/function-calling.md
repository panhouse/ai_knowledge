---
title: Function Calling(関数呼び出し)の使い方
part: 8
chapter: 第2章 API活用実践
tags: [API, Function Calling, Tool use, 外部連携]
created: 2026-07-05
updated: 2026-07-05
---

# Function Calling(関数呼び出し)の使い方

## これは何か

ChatGPTやClaudeに「今日の東京の天気は?」「A商品の在庫は何個残ってる?」と聞いても、モデルは学習データに基づいて言葉を生成しているだけなので、リアルタイムの天気や社内システムの在庫数は原理的に答えられない。この「モデル単体では届かない外の世界」につなぐための仕組みがFunction Calling(関数呼び出し)である。あらかじめ「こういう関数(天気取得・在庫検索・チケット起票など)が使える」とAPIに教えておくと、モデルが「この関数を、この引数で呼んでほしい」というリクエストをJSON形式で返してくれる。社内チャットボットやAIエージェント、Dify・Makeなどのノーコード自動化ツールの「ツール」機能は、内部的にほぼ全てこの仕組みの上に成り立っている。

## 仕組み・背景

Function Callingの最大のポイントは「**実際に関数を実行するのはモデルではなく、呼び出し側(開発者のプログラム)**」という役割分担にある。モデルはあくまで「何を呼ぶべきか」「どんな引数を渡すべきか」を判断してJSONを組み立てるだけで、外部のAPIを叩いたりDBを更新したりする処理そのものは行わない。流れは次の4ステップ。

1. **関数を登録する**: 開発者が「関数名」「何をする関数かの説明(description)」「必要な引数とその型(パラメータのスキーマ)」をAPIリクエストに含めて渡しておく
2. **モデルが判断する**: ユーザーの質問を見て、「この関数を呼べば答えられそうだ」と判断すると、通常の文章の代わりに「関数名+引数」をJSON形式で返す(このとき、モデルは"呼びたい"と提案するだけで、実行はしていない)
3. **開発者側のプログラムが実行する**: 受け取ったJSONをもとに、実際の天気APIや社内DBへの問い合わせを自分のプログラムで実行する
4. **結果をモデルに返す**: 実行結果を再びモデルに渡すと、モデルがそれを踏まえて自然な文章の回答を生成する

呼び方は提供元によって微妙に異なるが、指しているものはほぼ同じ概念である。

| 提供元 | 呼び方 | 関数定義を渡すパラメータ | 引数のスキーマ名 |
|---|---|---|---|
| OpenAI API | Function calling(Toolsの一種) | `tools`(各要素は`type: "function"`) | `parameters`(JSON Schema) |
| Claude API(Anthropic) | Tool use(ツール使用) | `tools` | `input_schema`(JSON Schema) |
| Gemini API(Google) | Function calling | `tools`(`functionDeclarations`の配列) | `parameters`(JSON Schema) |

いずれも「関数の説明」と「引数の型」をJSON Schema(データの形を定義する共通フォーマット)で書く点は共通している。

## 使いどころ・使い分け

| やりたいこと | 向いている方法 |
|---|---|
| リアルタイム情報(天気・株価・為替・最新ニュース)を答えさせたい | Function Calling(外部APIを呼ぶ関数を用意) |
| 社内DB・在庫システム・顧客情報を検索して答えさせたい | Function Calling(社内APIを呼ぶ関数を用意) |
| チャットの指示から実際にチケット起票・予定登録・メール送信などを実行させたい | Function Calling(書き込み系の関数を用意。実行前の確認ステップを挟むのが安全) |
| 社内マニュアルやFAQなど、静的な文書の中身を検索して答えさせたい | RAG(検索拡張生成。ナレッジベースへの埋め込み検索の方が向く) |
| 出力の形式(JSONのキー名や型)だけを固定したい(外部の関数は呼ばない) | Structured Outputs(構造化出力。Function Callingと似ているが「行動」ではなく「整形」が目的) |
| ノーコードでAIエージェント・自動化ワークフローを組みたい | Dify・Make・n8nなどの「ツール」機能(内部でFunction Callingを利用) |

判断基準はシンプルで、「モデルの知識だけで答えられない」かつ「外部に問い合わせる/外部で何かを実行する必要がある」場合にFunction Callingが候補になる。逆に、答えが手元の文書の中に書いてあるだけならRAG、出力の見た目を整えたいだけならStructured Outputsの方が適している。

## 実務での使い方

### 最小構成のJSON例(OpenAI API・Chat Completions形式)

天気を調べる関数を1つ登録し、モデルに呼び出させる例。

```json
{
  "model": "gpt-5.1",
  "messages": [
    { "role": "user", "content": "東京の今日の天気を教えて" }
  ],
  "tools": [
    {
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "description": "指定した地域の現在の天気を取得する",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "都市名(例: 東京, 大阪)"
            },
            "unit": {
              "type": "string",
              "enum": ["celsius", "fahrenheit"]
            }
          },
          "required": ["location"],
          "additionalProperties": false
        },
        "strict": true
      }
    }
  ],
  "tool_choice": "auto"
}
```

これに対してモデルは、文章の代わりに次のような「関数を呼びたい」というリクエストを返す(この時点ではまだ何も実行されていない)。

```json
{
  "tool_calls": [
    {
      "id": "call_abc123",
      "type": "function",
      "function": {
        "name": "get_current_weather",
        "arguments": "{\"location\": \"東京\", \"unit\": \"celsius\"}"
      }
    }
  ]
}
```

開発者側は`get_current_weather`関数を実際に実行し、その結果を`role: "tool"`のメッセージとして会話履歴に追加してモデルに送り返す。これを受けてモデルが「東京の今日の天気は晴れ、最高気温26度です」といった自然文の回答を生成する。

- `tool_choice`は`"auto"`(モデルに判断を任せる)、`"required"`(必ずどれかの関数を呼ばせる)、`"none"`(関数を呼ばせない)、または特定の関数名を指定して強制することもできる
- `strict: true`(Structured Outputsと同じ仕組み)を付けると、モデルが返す引数が指定したJSON Schemaに厳密に一致することが保証され、キーの誤字や型違いによるエラーを防げる
- 1回の応答で複数の関数呼び出しを同時に返す「並列関数呼び出し(parallel tool calls)」にも対応しており、「東京と大阪の天気を両方教えて」のような質問でも1往復で処理できる

### ツール横断の対応付け

同じ「関数を定義して呼ばせる」という考え方は、主要なAPI・ノーコードツールで名前を変えて登場する。

| 概念 | OpenAI API | Claude API | Gemini API | Dify | Make / n8n |
|---|---|---|---|---|---|
| 呼び方 | Function calling(Tools) | Tool use | Function calling | エージェントノードの「Function Calling」戦略 | 「ツール」(AI Agentに接続するシナリオ/ノード) |
| 定義する場所 | `tools`パラメータ | `tools`パラメータ | `tools.functionDeclarations` | エージェントノードの「ツール」設定画面(50以上の組み込みツールから選択、または自作) | シナリオ全体を1つの「ツール」として登録し、AI Agentモジュールに接続 |
| 実行結果の返し方 | `role: "tool"`メッセージ | `tool_result`ブロック | `functionResponse` | 画面上で自動的に処理される(ノーコード) | シナリオの出力が自動的にAI Agentへ返る |

Difyでは、エージェントノードの中で「Function Calling」または「ReAct」という2つの推論方式をプラグイン的に切り替えられるが、GPT-4系などFunction Calling対応モデルを使う場合はFunction Calling戦略の方が安定して動作しやすい。Make・n8nでは、開発者がJSON Schemaを手書きする代わりに、既存のシナリオ(Make)やノード(n8n)を「ツール化」してAIエージェントに接続する形でFunction Callingの仕組みを隠蔽している。

### 実装時の最小チェックリスト

1. 関数の`description`は「いつ使うべきか」まで具体的に書く(曖昧な説明はモデルの誤選択・呼び出し漏れの原因になる)
2. 引数の`required`と型を正確に定義し、可能なら`strict`モードを有効にする
3. 実行結果をそのままモデルに渡すのではなく、エラー時は「関数の実行に失敗しました」といった構造化されたメッセージとして返す
4. 書き込み系(DB更新・送信・起票など)の関数は、実行前に人間の承認ステップを挟むか、影響範囲を限定した専用APIを用意する

## 注意点・よくある誤解

- **モデルが直接システムを操作しているわけではない**: あくまで「この関数をこの引数で呼びたい」という提案を返しているだけで、実際にAPIを叩く・DBを書き換えるのは開発者が用意したプログラム側の責任である。この役割分担を理解していないと、「AIが誤操作した」という事故の原因を見誤る。
- **引数がハルシネーション(もっともらしい誤り)で埋められることがある**: 必須パラメータが会話から読み取れない場合、モデルが「東京」のような値を勝手に推測して埋めてしまうことがある。重要な処理では、実行前に値の妥当性をコード側で検証する。
- **登録する関数を増やしすぎると選択精度が落ちる**: 数十個規模の関数を一度に渡すと、モデルが似た関数を取り違えたり、そもそも呼ぶべき関数を選べなくなったりする。関数を機能ごとにグループ分けする、必要な関数だけを動的に絞り込んで渡す、といった工夫が必要になる。
- **関数定義そのものがトークン(課金対象)を消費する**: `tools`に渡す関数名・説明・スキーマも入力トークンとしてカウントされるため、関数の数や説明文の長さがそのままAPIコストに跳ね返る。
- **並列呼び出しは同時実行される前提で設計する**: 「在庫を1個減らす」のような処理を並列に呼ばれても矛盾が起きないよう、関数側を冪等(べきとう、同じ処理を繰り返しても結果が壊れない設計)にしておく。

## 最初の一歩

OpenAI APIのプレイグラウンド(platform.openai.com/playground)か手元のスクリプトで、`get_current_weather`のようなダミー関数を1つだけ定義し、「東京の天気は?」と質問してモデルが実際にJSON形式の関数呼び出しを返してくることを確認してみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)
- [Difyとは何か](../part09-nocode-lowcode/dify-basics.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: Function Callingの役割分担(モデルは提案するだけ・実行は開発者側)、OpenAI/Claude/Geminiでの呼び方とパラメータ名の対応、JSON例、Dify・Make/n8nとの対応付け、実装時の注意点を整理
- **出典**: [OpenAI Help Center: Function calling in the OpenAI API](https://help.openai.com/en/articles/8555517-function-calling-in-the-openai-api)、[OpenAI: Introducing Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/)、[Claude Platform Docs: Tool use with Claude](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)、[Claude Platform Docs: Define tools](https://platform.claude.com/docs/en/agents-and-tools/tool-use/define-tools)、[Google AI for Developers: Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)、[Dify Docs: エージェント](https://docs.dify.ai/ja-jp/guides/workflow/node/agent)、[Make Help Center: Step 1. Set up the AI agent](https://help.make.com/step-1-set-up-the-ai-agent)
