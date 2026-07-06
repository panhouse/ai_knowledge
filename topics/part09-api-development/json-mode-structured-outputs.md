---
title: "JSONモード・Structured Outputsの基本"
part: 9
chapter: 第2章 API活用実践
tags: [API, JSONモード, Structured Outputs, データ抽出, JSON Schema]
created: 2026-07-06
updated: 2026-07-06
---

# JSONモード・Structured Outputsの基本

## これは何か

LLM(大規模言語モデル)に「この問い合わせメールから会社名と希望金額を抜き出して」と頼むと、返ってくるのは「承知しました。会社名は◯◯株式会社、ご希望金額は120万円です。」のような自然文であることが多い。これをそのままスプレッドシートやDBに流し込みたい場合、開発者は「会社名は」の後ろの文字列を正規表現で抜き出す…といった処理を書くはめになる。しかしこの方法は、モデルが言い回しを変えたり前置きの一文を付けたり、項目の順番を変えたりするだけで簡単に崩れる、非常に脆いやり方である。

JSONモード(JSON mode)とStructured Outputs(構造化出力)は、この問題をAPI側の機能で解決する仕組みで、「モデルの最終回答そのものを、事前に決めたJSON形式に強制的に従わせる」機能である。プログラムがそのまま`json.loads()`のような処理でパースできる出力を、モデルに毎回確実に返させることができる。

両者には重要な違いがある。**JSONモード**は「文法的に正しいJSON(カッコの対応や引用符の付け方が正しい)であること」しか保証しない古い世代の機能で、キー名や型がこちらの想定と違っても、崩れた構造のまま返ってくることがある。**Structured Outputs**は、開発者が渡したJSON Schema(JSON形式のデータが「どんな構造であるべきか」を定義する機械可読な規格)に、キー名・型・必須項目・入れ子構造まで完全に一致させることを保証する新しい世代の機能で、2024〜2026年にかけてOpenAI・Google・Anthropicの主要APIすべてに実装された。

## 仕組み・背景

### JSONモード(旧世代・ゆるい保証)

OpenAIが最初に提供した`response_format: {"type": "json_object"}`が代表例。モデルに「有効なJSONで返して」と指示し、出力の途中でJSONとして文法的に破綻しないよう軽く制約をかける仕組みで、プロンプト側でどんなキー・構造にすべきかを説明はできるが、**その説明に従うかどうかはモデルの精度に依存する**。キーを1つ忘れる、型を文字列と数値で揺らす、といった崩れが起こり得る。

### Structured Outputs(新世代・厳密な保証)

OpenAIが2024年8月に導入した`response_format`の`json_schema`オプション(`strict: true`)を皮切りに、Google Gemini(`response_schema`/`response_mime_type`。2025年からはより表現力の高い`response_json_schema`もプレビュー提供)、Anthropic Claude(2025年11月にベータ公開、2026年にかけて`output_config.format`として提供)が追随し、現在は3社とも「JSON Schemaで定義した構造に完全一致させる」機能を持つ。

技術的には、渡されたJSON Schemaを「文法(grammar)」に変換し、モデルが次の1トークンを生成するたびに「その文法に違反するトークンは選べないようにする」制約付きデコーディング(constrained decoding)という方式で実現されている。単に「JSONで返して」とお願いしているだけの旧世代のJSONモードとは異なり、**構造的に外れた出力そのものが生成できなくなる**ため、キー名の欠落・型の不一致・余計なキーの混入が原理的に起きない(ただし後述のとおり、値の内容が正しいかは別問題)。

### Function Callingとの違い(重要な区別)

[Function Calling(Tool Calling)の基本](function-calling-basics.md)と混同されやすいが、両者は目的が異なる。

- **Function Calling**は、モデルに「外部のツール・関数を呼びたい」という意思表示をさせる仕組み。呼び出し先の関数を実際に実行するのは開発者側のコードであり、モデルの最終回答はその実行結果を踏まえた自然文になることが多い。
- **JSONモード/Structured Outputs**は、外部のツール実行を一切伴わない。モデルが「利用者に見せる最終回答」そのものを、機械が読める形式に整形させるための機能である。ツールを何も持たないシンプルな1回のAPI呼び出しでも使える。

ただし実務上は重なる部分もある。契約書からの項目抽出のように「決まった形式でデータを取り出したい」だけの用途であれば、ツールを1つも定義せずJSONモード/Structured Outputsだけで済むことが多い。逆に、抜き出したデータをその場で別システムに書き込みたい(＝抜き出しと同時に外部処理を実行したい)場合はFunction Callingの方が自然である。またOpenAIのstrictモードやAnthropicのstrict tool useのように、**Function Callingの引数(arguments)自体にもJSON Schemaの厳密一致を適用する仕組み**があり、「ツールを呼びつつ、その引数の型も完全に保証する」という組み合わせも可能になっている。

### データ形式としてのJSON

[AIが扱いやすいデータ形式](../part07-data-analysis/ai-friendly-data-formats.md)で触れたとおり、JSONは「API連携やDBとの受け渡しなど、機械的処理をさせたいとき」に向く形式である。本ページで扱うJSONモード/Structured Outputsは、その「AIの出力を機械処理しやすいJSONにする」という要求を、プロンプトでの工夫ではなくAPIの機能として確実に実現する手段だと位置づけられる。

## 使いどころ・使い分け

| したいこと | 向いている手段 |
|---|---|
| 自由な文章で説明・要約・提案をさせたい(人がそのまま読む) | 通常のプロンプト(制約不要) |
| 文章から会社名・金額・日付などの項目を抜き出し、DBやスプレッドシートに登録したい | Structured Outputs(JSON Schemaで厳密に定義) |
| 問い合わせ内容を「バグ報告/機能要望/その他」のように定型カテゴリへ分類したい | Structured Outputs(`enum`で選択肢を固定) |
| 抜き出したデータを使って、その場で別のシステム操作(メール送信・DB更新など)まで実行させたい | Function Calling(実行系のツールとして登録) |
| とりあえず崩れにくいJSON文字列が返ればよく、キー構造の厳密さは求めない、または古いモデルしか使えない | JSON mode(レガシー。新規開発では基本的にStructured Outputsを優先) |
| 1回のやり取りで、モデルの「考え方」も含めて人に説明したい(思考過程を自然文で見せたい) | 通常のプロンプト。JSON化すると読みにくくなるため不向き |

判断基準はシンプルに「その回答を人がそのまま読むのか、プログラムが読み込んで次の処理に渡すのか」。後者であればJSONモード/Structured Outputsの出番になり、新規に組むなら基本的に厳密保証のあるStructured Outputsを選ぶ。

## 実務での使い方

### OpenAIのStructured Outputs(コピペ用の最小例)

以下はOpenAI APIで「数学の解き方をステップごとのJSONで返させる」最小例(2026年7月時点のドキュメントに基づく)。`response_format.type`を`json_schema`にし、`strict: true`を付けるのが要点。

```bash
curl https://api.openai.com/v1/chat/completions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "(使用するモデル名。2026年7月時点ではgpt-5.5など)",
    "messages": [
      { "role": "system", "content": "You are a helpful math tutor." },
      { "role": "user", "content": "8x + 7 = -23 を解いて" }
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "math_reasoning",
        "strict": true,
        "schema": {
          "type": "object",
          "properties": {
            "steps": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "explanation": { "type": "string" },
                  "output": { "type": "string" }
                },
                "required": ["explanation", "output"],
                "additionalProperties": false
              }
            },
            "final_answer": { "type": "string" }
          },
          "required": ["steps", "final_answer"],
          "additionalProperties": false
        }
      }
    }
  }'
```

Python SDKでは、Pydanticモデルを渡すだけでスキーマを自動生成してくれる`client.chat.completions.parse(response_format=YourPydanticModel)`(または新しいResponses APIの`client.responses.parse()`)というヘルパーが用意されており、生のJSON Schemaを手書きしなくても済む。

旧世代のJSONモードを使う場合は`"response_format": {"type": "json_object"}`だけを指定する(スキーマは渡せない。プロンプト側で構造を説明する必要があり、崩れる可能性も残る)。

### 各社での呼び方・パラメータの対応表

| 項目 | OpenAI | Anthropic(Claude) | Google(Gemini) |
|---|---|---|---|
| 旧世代:JSONモード(構文だけ保証) | `response_format: {"type": "json_object"}` | 対応する専用パラメータはなし(厳密なツール定義でJSON文字列を返させる代替策が使われてきた) | `generationConfig.response_mime_type: "application/json"`(スキーマ省略時) |
| 新世代:Structured Outputs(スキーマに完全一致) | `response_format: {"type": "json_schema", "json_schema": {"name", "schema", "strict": true}}` | `output_config.format: {"type": "json_schema", "schema": {...}}`(2025年11月にベータ公開。旧ベータ名`output_format`からの移行期) | `generationConfig`の`response_mime_type: "application/json"` + `response_schema`(OpenAPI 3.0のサブセット)。より表現力の高い`response_json_schema`(JSON Schema準拠、プレビュー)も選択可 |
| SDKの簡易ヘルパー | `client.chat.completions.parse()` / `client.responses.parse()`(Pydanticモデルを渡すだけ) | `client.messages.parse(output_format=YourModel)` | `response_schema`にPydanticモデルやTypedDictを直接渡せる |
| 追加キーを許さない設定 | `additionalProperties: false`(strictモードでは実質必須) | `additionalProperties: false` | スキーマに定義したプロパティ以外は基本的に生成されない仕様 |
| 出力の取得場所 | `choices[0].message.content`(JSON文字列。要`json.loads`) | `content[0].text`(JSON文字列) | `response.text`または`response.parsed`(SDKがパース済みオブジェクトを返す場合あり) |

いずれのプロバイダーも、モデルが安全上の理由で回答を拒否した場合(OpenAIの`refusal`フィールド、Claudeの`stop_reason: "refusal"`)や、出力が途中で`max_tokens`に達して切れた場合は、スキーマへの一致が保証されない点は共通している。

### 業務での活用例

- **問い合わせメールの構造化**: 「会社名・氏名・希望プラン・緊急度」をJSON Schemaで定義し、受信メールの本文から一発でCRMに登録できる形に変換する
- **アンケート自由記述のタグ付け**: 自由記述の回答を、事前に決めた`enum`のカテゴリ(「価格」「機能」「サポート」等)に分類し、集計しやすい形で出力させる
- **レポートの定型フォーマット化**: 週次レポートの「達成事項・課題・次週の予定」を毎回同じJSON構造で出力させ、社内ダッシュボードに自動反映する
- **複数モデルの回答比較**: 複数のLLMに同じ評価項目のJSONを出力させ、スプレッドシート上で横並びに比較する

## 注意点・よくある誤解

- **Function Callingと同じものではない**: 前述のとおり、Function Callingは「外部ツールを呼ぶ意思表示」、JSONモード/Structured Outputsは「最終回答自体の整形」であり、担っている役割が異なる。ただし引数のスキーマ厳密一致(strict tool use)のように、両者の技術基盤(JSON Schemaへの制約付きデコーディング)は共通している。
- **スキーマが複雑すぎると精度が落ちる・遅くなる**: 深い入れ子構造や大量のプロパティを持つ巨大なスキーマを渡すと、モデルの出力品質が下がったり、初回リクエストでスキーマを内部の「文法」にコンパイルする分レイテンシが増えたりする(コンパイル結果は一定時間キャッシュされるプロバイダーもある)。1回の抽出で欲張らず、必要なら複数回のAPI呼び出しに分割する。
- **厳密モードで使えるJSON Schemaのキーワードには制限がある**: 各社とも、`strict`/厳密モードでは`additionalProperties`は`false`固定、再帰的なスキーマや外部URLの`$ref`、数値の`minimum`/`maximum`/`multipleOf`、文字列の`minLength`/`maxLength`/`pattern`といった一部のキーワードが使えない、またはOpenAIのように「実質すべてのプロパティを`required`に含める」といった独自の制約があるので、事前に各社の最新リファレンスで対応キーワードを確認する。
- **構造が正しいことと、内容が正しいことは別問題**: スキーマに完全一致していても、値そのものが誤って抽出されている(ハルシネーション)可能性は残る。特に金額・日付・固有名詞などは、受け取り側のプログラムで型チェックだけでなく妥当性の検証(存在するIDか、金額が現実的な範囲か等)を必ず行う。「スキーマ一致=検証不要」という誤解は避ける。
- **モデル・提供プラットフォームによって対応状況が異なる**: 古いモデルバージョンやセルフホスト・一部クラウド経由の提供形態では、Structured Outputs自体が使えず旧世代のJSONモードしか選べない場合がある。導入前に使用予定のモデル・API経路(直接API/Azure/Bedrock/Vertex AI等)の対応表を確認する。
- **旧世代JSONモードだけで運用するリスク**: スキーマを渡せない分、プロンプト側で構造を細かく指示しても、キーの欠落・型の揺れ・(まれに)出力が終わらず同じ文字を繰り返すような崩れが起こり得る。新規に構築するなら、対応モデルがあるかぎりStructured Outputsを優先する。

## 最初の一歩

すでに「文章から項目を抜き出す」プロンプトを運用しているなら、その出力形式をJSON Schemaとして書き出し、OpenAI・Claude・Geminiいずれかの`response_format`/`output_config.format`/`response_schema`に渡してみる。これまで正規表現でパースしていた処理を`json.loads()`一発に置き換えられるかを確認するのが最短の検証になる。

## 関連トピック

- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [AIが扱いやすいデータ形式](../part07-data-analysis/ai-friendly-data-formats.md)
- [OpenAI APIの基本](openai-api-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: JSONモード(構文のみ保証)とStructured Outputs(スキーマ完全一致)の違い、制約付きデコーディングの仕組み、Function Callingとの役割の区別、OpenAI/Anthropic/Geminiのパラメータ対応表、OpenAIのコピペ用最小例(`response_format.json_schema.strict`)、各社のスキーマ制限・注意点を整理
- **出典**: [OpenAI: Structured model outputs](https://developers.openai.com/api/docs/guides/structured-outputs), [OpenAI: Introducing Structured Outputs in the API](https://openai.com/index/introducing-structured-outputs-in-the-api/), [Anthropic: Structured outputs (Claude Platform Docs)](https://platform.claude.com/docs/en/build-with-claude/structured-outputs), [Google AI for Developers: Structured output (Gemini API)](https://ai.google.dev/gemini-api/docs/structured-output), [Google Blog: Gemini API structured outputs (JSON Schema support)](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-api-structured-outputs/), [Firebase AI Logic: Generate structured output](https://firebase.google.com/docs/ai-logic/generate-structured-output)
