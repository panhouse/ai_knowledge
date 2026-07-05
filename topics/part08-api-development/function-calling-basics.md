---
title: Function Calling(Tool Use)の基本
part: 8
chapter: 第2章 API活用実践
tags: [Function Calling, Tool Use, API, AIエージェント]
created: 2026-07-05
updated: 2026-07-05
---

# Function Calling(Tool Use)の基本

## これは何か

ChatGPTに「今日の在庫数を教えて」と聞いても、AIは自社の在庫システムを知らないので答えられない。Function Calling(Tool Use、ツール呼び出しとも呼ばれる)は、この壁を越えるための仕組みで、AIモデルに「社内システムのこの機能(関数・API)を、この条件で呼び出したい」と自分で判断させ、実行結果を受け取ってから回答を組み立てさせる機能である。生成AIチャットと社内システムを繋ぐ「配線」にあたり、社内チャットボットや自動化、いわゆるAIエージェントの土台となる技術である。

## 仕組み・背景

Function Callingは2023年半ばにOpenAIが「function calling」として発表し、その後OpenAIも含め業界全体で「tool use(ツール呼び出し)」という呼び方に収斂した。名称は違っても中身はほぼ同じ考え方で、次の4ステップで動く。

1. **ツールの登録**: 開発者が「関数名」「何をする関数か」「必要な引数(パラメータ)」をJSON形式でAIに事前に伝える(例:「`get_stock`という関数があり、`product_id`を渡すと在庫数を返す」)
2. **AIの判断**: ユーザーの質問に対し、AIは自分の知識だけで答えられるか、外部の関数を呼ぶ必要があるかを判断する。呼ぶ必要があると判断すると、AIは実際にはコードを実行せず、「`get_stock`を`product_id=123`で呼びたい」という指示(JSON)だけを返す
3. **実行は人間側のシステムが行う**: AIモデル自身はDBにもAPIにもアクセスできない。実際に関数を実行し、在庫システムに問い合わせるのは開発者が用意したプログラム側の役目である。これがFunction Callingの最も誤解されやすい点で、AIが「勝手に社内システムを操作する」わけではなく、あくまで「この処理をお願いします」という依頼書を作るだけである
4. **結果を戻して回答を生成**: 実行結果(例:「在庫は42個」)をAIに返すと、AIはその情報をもとに自然な文章で回答を生成する

この「AIは指示するだけ、実行は自分のプログラム」という分業構造があるからこそ、社内システムの安全性を保ちながらAIに外部データへのアクセスを許可できる。1回の会話で複数のツールを同時に呼び出す「並列ツール呼び出し(parallel tool calling)」に対応するモデルも増えており、「在庫を確認しつつ配送日数も調べる」といった複合的な依頼を1往復で処理できるようになってきている。

## 使いどころ・使い分け

| やりたいこと | 向いている手段 |
|---|---|
| 社内の最新データ(在庫・顧客情報・売上等)をAIに参照・更新させたい | Function Calling(Tool Use) |
| 社内文書やマニュアルの内容を検索して答えさせたい(更新頻度が低い知識) | RAG(検索拡張生成、文書の検索が主目的) |
| AIに出力形式(JSON)だけを固定させたい(外部処理は不要) | Structured Outputs(構造化出力) |
| 「調べる→判断する→実行する」を複数ステップ自律的に繰り返させたい | Function Callingを土台にしたAIエージェント |
| 単純に文章を生成・要約させたいだけ | 通常のプロンプト(Function Calling不要) |

判断のコツは「AIの学習データにない、今この瞬間の情報や、システム側の操作が必要か」で考えるとよい。天気・在庫・予約状況のようにリアルタイム性が求められる情報や、実際に「登録する」「送信する」といった副作用を伴う処理はFunction Calling向き。逆に社内規程やFAQのように「探して引用する」だけで完結する場合はRAGの方が適している(両者は排他ではなく、1つのチャットボットの中で「検索はRAG、予約実行はFunction Calling」のように併用されることも多い)。

## 実務での使い方

### 関数定義のイメージ(概念レベル、実装コードではない)

エンジニアがAIに渡す「ツールの説明書」は、おおむね次のようなJSON構造になる(在庫確認システムと連携する例)。

```json
{
  "name": "get_stock",
  "description": "商品IDを指定して現在の在庫数を取得する",
  "parameters": {
    "type": "object",
    "properties": {
      "product_id": { "type": "string", "description": "商品コード" }
    },
    "required": ["product_id"]
  }
}
```

ビジネスパーソンが自分でこのJSONを書く場面は少ないが、エンジニアに要件を伝える際は「どんな情報を」「どんな条件で」取得・更新したいのかを言語化しておくと、この定義に落とし込みやすくなる。

### 主要プロバイダでの呼び名・設定の対応

| 概念 | OpenAI API | Anthropic Claude API | Google Gemini API |
|---|---|---|---|
| 機能名 | Function calling(2023年に`tools`パラメータへ改称、現在は「tool calling」とほぼ同義で併用) | Tool use | Function calling |
| ツールの登録場所 | リクエストの`tools`配列 | リクエストの`tools`配列(`tool_use`ブロックで応答) | リクエストの`tools`(`FunctionDeclaration`) |
| 呼び出し方の制御 | `tool_choice`(`auto`/`required`/`none`/関数名指定) | `tool_choice`(`auto`/`any`/`tool`) | `tool_config.function_calling_config.mode`(`AUTO`/`ANY`/`NONE`) |
| 開発者が使う主なAPI | Responses API(旧Assistants APIは2026年8月26日に廃止予定) | Messages API | Gemini API |

いずれのプロバイダも「AUTO(AIに判断を任せる)」「強制的に必ずどれかのツールを呼ばせる」「ツールを使わせない」の3パターンを制御できる点は共通しており、例えば「まず自由に会話させ、必要な情報が揃った段階で強制的にツールを呼ばせて構造化データを取り出す」という使い分けが定番のパターンになっている。

### ノーコード・業務システムでの活用イメージ

- **社内チャットボット×在庫確認**: 「A商品の在庫ある?」という質問に対し、AIが在庫システムのAPIをFunction Callingで呼び出し、リアルタイムの数字で回答する
- **Dify・n8nなどのワークフローツール**: 多くのノーコードAIツールは「ツール」「アクション」という名前でFunction Calling相当の機能を提供しており、GUI上でAPIのエンドポイントとパラメータを設定するだけで、コードを書かずに同様の連携が作れる
- **社内Slack/Teamsボット**: 「明日の14時に会議室を予約して」という自然文から、カレンダーAPIを呼び出して実際に登録まで行う、という一連の自動化の起点になる

### 料金面の考え方

Function Calling自体に追加の専用料金が発生するわけではなく、通常のAPI利用と同じトークン課金(入力・出力それぞれの従量課金)の枠内で扱われる。ただしツールの説明文(関数定義)もプロンプトの一部としてトークン消費されるため、ツール数が多い・説明が長いほど入力トークンが増えてコストに影響する点は意識しておきたい。

## 注意点・よくある誤解

- **AIが直接システムを操作しているわけではない**: AIが返すのは「この関数をこの引数で呼びたい」という指示(JSON)だけで、実際にDBを書き換えたりAPIを叩いたりするのは開発者が用意したプログラム側の責任である。「AIが暴走して勝手に注文を確定する」といった事態は、実行側のプログラムに承認フローやガードレールを入れることで防ぐ設計になっている
- **AIが存在しない関数名や誤った引数を生成することがある**: いわゆるハルシネーション(もっともらしい誤り)はFunction Callingでも起こりうる。実行前に引数のバリデーション(値の検証)を挟む、重要な処理(送金・削除等)は人間の承認を挟むといった設計上の防御が必須
- **ツールを増やしすぎると精度が落ちる**: 似たような機能のツールを大量に登録すると、AIがどれを呼ぶべきか迷いやすくなる。1つのボットに詰め込みすぎず、用途ごとに絞り込むのがコツ
- **RAGとの混同**: 「AIに社内情報を答えさせる」という目的は同じでも、RAGは文書検索、Function Callingはシステム連携・処理実行という役割の違いがある。両方が必要なケースも多い
- **プロバイダ間でAPI仕様が異なる**: OpenAI・Anthropic・Googleはいずれも似た概念だがパラメータ名や制御方法(`tool_choice`の値など)が異なるため、プロバイダを乗り換える際はコードの書き換えが必要になる

## 最初の一歩

自社で「AIチャットボットに在庫確認や予約状況の照会をさせたい」といったニーズがあれば、まずは既存のノーコードツール(Dify等)の「ツール」「アクション」設定画面を開き、社内APIを1つだけ試しに登録して、Function Callingの動きを実際に触って確認してみる。

## 関連トピック

- [OpenAI APIの基本](../part08-api-development/openai-api-basics.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: Function Calling(Tool Use)の仕組み(4ステップの処理フロー)、RAG・Structured Outputsとの使い分け、主要プロバイダ(OpenAI/Anthropic/Google)での呼び名・パラメータ対応表、関数定義の概念的なJSON例、ノーコードツールでの活用イメージ、実行責任の所在に関する注意点を整理
- **出典**: [OpenAI Function calling ガイド](https://developers.openai.com/api/docs/guides/function-calling)、[OpenAI Using tools ガイド](https://developers.openai.com/api/docs/guides/tools)、[Claude Platform Docs: Tool use overview](https://platform.claude.com/docs/en/agents-and-tools/tool-use/overview)、[Claude Platform Docs: How tool use works](https://platform.claude.com/docs/en/agents-and-tools/tool-use/how-tool-use-works)、[Google AI for Developers: Function calling with the Gemini API](https://ai.google.dev/gemini-api/docs/function-calling)、[NTTPC 技業LOG: Function CallingでLLMを「業務アシスタント」に](https://www.nttpc.co.jp/technology/function-calling.html)
