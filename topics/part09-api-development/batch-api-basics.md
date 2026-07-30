---
title: "バッチ処理(Batch API)の基本"
part: 9
chapter: 第2章 API活用実践
tags: [Batch API, API, コスト削減, 非同期処理, JSONL, RAG]
created: 2026-07-06
updated: 2026-07-29
---

# バッチ処理(Batch API)の基本

## これは何か

「サポートチケット3万件をAIで一括分類したい」「社内文書アーカイブを全部要約したい」といった大量処理を、通常のAPI(1件ずつ呼び出す方式)でやろうとすると、レート制限(一定時間あたりのリクエスト数上限)に引っかかったり、料金が想定以上にかさんだりする。Batch API(バッチAPI)は、大量のリクエストを1つのファイルにまとめて送信し、「即答は不要なので、24時間以内など決まった猶予の中でまとめて処理してほしい」という形で依頼する仕組みで、通常の半額程度の料金で処理できる。OpenAI・Anthropic・Googleなど主要な生成AIプロバイダーが同様のサービスを提供している。

## 仕組み・背景

通常のAPI呼び出し(同期呼び出し)は「リクエストを送ったらその場で結果が返ってくる」方式で、チャットボットのようにユーザーを待たせられない用途に向く。一方Batch APIは次のような流れで動く。

1. **リクエストをJSONL形式のファイルにまとめる**: JSONL(JSON Lines)とは、1行に1件のJSON(構造化データ)を並べたテキスト形式。「1万件の問い合わせメールを分類してほしい」なら、1万行のファイルを作り、各行に「どの問い合わせを」「どんなプロンプトで」処理するかを書く。
2. **ファイルをアップロードし、バッチ処理を開始する**: APIにファイルを送ると、処理を待つキューに入る。
3. **非同期で処理される**: 各社とも「24時間以内」を目安の処理枠(SLA、サービス品質保証の意味)としており、実際には数十分〜数時間で終わることが多い。混雑状況によっては24時間ぎりぎりになったり、期限内に終わらなかったリクエストは「期限切れ」扱いになり課金されない。
4. **結果ファイルを取得する**: 処理が終わると、やはりJSONL形式の結果ファイルが用意される。各行は元のリクエストにつけた識別子(`custom_id`)で紐づいており、**結果の並び順は入力順と一致しない**ため、必ずこの識別子で突き合わせる。

料金が安くなる理由は、プロバイダー側からすると「今すぐ処理する必要がない仕事」をまとめて計算資源が空いている時間帯に流し込めるため。ユーザー側は即時性を諦める代わりに、その効率化分の還元を受け取る形になる。

## 使いどころ・使い分け

判断基準はシンプルで、「その場でユーザーに返す必要があるか」「多少時間がかかっても構わないか」で分ける。

| 比較軸 | 通常のAPI(同期呼び出し) | Batch API |
|---|---|---|
| 応答速度 | 数秒〜数十秒でその場で返る | 目安24時間以内(実際は数十分〜数時間のことが多い) |
| 料金 | 定価 | 約50%割引(OpenAI・Anthropic・Googleともに) |
| 向いている用途 | チャットボット、リアルタイム検索連携、ユーザー操作への即時応答 | 大量データの一括処理、締切に余裕がある夜間バッチ処理 |
| レート制限への影響 | 大量に同時実行するとすぐ上限に達しやすい | バッチ専用の別枠で処理されるため、通常のレート制限を圧迫しにくい |

**向いている業務シーンの例**

- サポートチケットの一括分類: 「深夜のうちに、その日届いた数千件の問い合わせを『クレーム/質問/要望』に自動仕分けしておく」
- ドキュメントアーカイブの一括要約: 社内に蓄積された議事録・レポートを一括で3行要約に変換する
- RAG(検索拡張生成。文書を検索してAIに読ませてから回答させる方式)構築時の埋め込みベクトル生成: ナレッジベースにする文書が数万件ある場合、埋め込み(文章を検索用の数値ベクトルに変換する処理)をバッチでまとめて作る方がコストを大きく抑えられる
- コンテンツの一括モデレーション・タグ付け: 過去に投稿された大量のユーザー投稿にまとめて不適切表現チェックやカテゴリタグを付ける

**向いていないケース**

- チャットボットやカスタマーサポートの自動応答など、ユーザーが画面の前で回答を待っている用途
- 在庫確認・注文状況照会など、Function Calling([Function Calling(Tool Calling)の基本](function-calling-basics.md)参照)で都度リアルタイムに答える必要がある処理
- 数件〜数十件程度の少量処理(バッチ化の準備コストの方が高くつく)

## 実務での使い方

### OpenAI Batch API の使い方(概念フロー)

1. リクエストをまとめたJSONLファイルを用意する。1行が1件のリクエストで、`custom_id`(結果を突き合わせるための自分で決める識別子)・`method`・呼び出したいエンドポイント(`/v1/chat/completions`や`/v1/embeddings`など)・実際のリクエスト本体(`body`)を書く。

```jsonc
// batch_requests.jsonl の1行のイメージ(実際は改行なしの1行のJSON)
{
  "custom_id": "ticket-00001",
  "method": "POST",
  "url": "/v1/chat/completions",
  "body": {
    "model": "(使用するモデル名)",
    "messages": [
      { "role": "system", "content": "問い合わせ内容を『クレーム/質問/要望』のいずれかに分類し、ラベルのみ出力して" },
      { "role": "user", "content": "(問い合わせ本文がここに入る)" }
    ]
  }
}
```

2. このファイルをFiles APIでアップロードし、バッチ作成のエンドポイントに「どのファイルを」「どのエンドポイント宛てに」「完了期限(現状は24時間)」を指定して送信する。
3. バッチのステータス(処理中/完了など)をポーリング(一定間隔で確認)するか、Web管理画面(platform.openai.com)で進捗を確認する。
4. 完了したら結果ファイルをダウンロードし、`custom_id`をキーに元データと突き合わせて業務システムに反映する。

2026年7月時点でOpenAIのBatch APIが対応する主なエンドポイントは`/v1/chat/completions`(チャット形式の生成)・`/v1/responses`・`/v1/completions`・`/v1/embeddings`(埋め込み生成)・`/v1/moderations`・`/v1/images/generations`・`/v1/images/edits`・`/v1/videos`など、画像・動画生成系にも対応範囲が広がっている。1つのバッチファイルには最大5万件のリクエスト、ファイルサイズは最大200MBまでという制限があり、`/v1/embeddings`は1バッチあたり最大5万件の埋め込み入力までという別枠の上限も持つ(件数・容量の上限は変更されることがあるため、必ず公式ドキュメントで確認する)。料金はどのモデルでも一律で通常価格の約50%になる。結果ファイルはOpenAI側で自動的には削除されず、明示的に削除するか、アップロード時に`expires_after`(14〜30日で設定可)を指定しない限り残り続ける点はAnthropic・Googleの「一定日数で自動的にダウンロード不可になる」方式と異なる。

### Anthropic Message Batches API の使い方(概念フロー)

Anthropicも考え方は同じだが、ファイルアップロード方式ではなく、リクエスト本体をAPI呼び出しの中に直接まとめて送る点がOpenAIと異なる。

```jsonc
// Message Batches API へのリクエストボディのイメージ
{
  "requests": [
    {
      "custom_id": "doc-summary-001",
      "params": {
        "model": "(使用するモデル名)",
        "max_tokens": 500,
        "messages": [
          { "role": "user", "content": "次の議事録を3行で要約して: (本文)" }
        ]
      }
    }
  ]
}
```

1件のバッチは最大10万リクエストまたは256MBのいずれか早い方が上限。処理は`processing_status`が`in_progress`→`ended`に変わるのをポーリングで確認し、`ended`になったら`results_url`からJSONL形式の結果を取得する。結果は成功(`succeeded`)・エラー(`errored`)・キャンセル(`canceled`)・期限切れ(`expired`)の4種類のいずれかで返り、エラー・キャンセル・期限切れの分は課金されない。料金はどのモデルでも入力・出力ともに標準価格の50%で、プロンプトキャッシュ(直前と同じ内容の再利用を割引く仕組み)の割引とも併用できる。全アクティブモデルがBatch APIに対応しており、画像入力(Vision)・Tool Use(Web検索やコード実行などのサーバー側ツールを含む)・拡張思考(Extended Thinking)もそのまま使える。バッチは処理に数分〜1時間以上かかることがあるため、プロンプトキャッシュを使う場合は通常の5分キャッシュではなく1時間キャッシュ(TTL指定)にしておくとキャッシュヒット率が上がる。処理結果は作成から29日間ダウンロード可能で、それを過ぎるとバッチ自体は参照できても結果ファイルは取得できなくなる。

### Google Gemini Batch API(Batch Mode)の使い方(概念フロー)

GoogleのGemini APIにも同様の仕組みがあり、「Batch Mode」または「Batch API」と呼ばれる。標準の同期呼び出しに対して50%割引・目安24時間以内の処理という設計はOpenAI・Anthropicと共通だが、リクエストの渡し方に2種類の方法がある。

1. **インラインリクエスト**: 少量(リクエスト全体で20MB未満が目安)であれば、バッチ作成リクエストの中に`GenerateContentRequest`(生成リクエストの塊)のリストを直接埋め込んで送信できる。
2. **JSONLファイルのアップロード**: 大量データの場合は、1行1リクエストのJSONLファイルをFile API経由でアップロードして参照させる(ファイルサイズは最大2GBまで)。
3. バッチジョブを作成すると非同期でキューに入り、ステータス(`PENDING`→`RUNNING`→`SUCCEEDED`など)をポーリングで確認する。
4. 完了したら結果を取得する。インライン送信の場合は結果も直接返り、ファイル送信の場合は結果ファイルをダウンロードする。

2026年6月時点で、Gemini Batch APIはテキスト生成(`generateContent`)に加えて埋め込みモデル(`gemini-embedding-001`など)のバッチ処理にも対応し、さらにOpenAI SDKと同じ書き方(APIキーとベースURLをGoogle側に向けるだけ)でバッチを作成・状態確認・結果取得できる「OpenAI互換レイヤー」も追加された(ただしOpenAI互換レイヤーでのファイルのアップロード・ダウンロードは非対応で、通常のGemini APIの方式を使う必要がある)。Batch API用のレート制限は通常の同期呼び出しとは別枠で、より高いスループットが確保されている。

### 比較表: OpenAI vs Anthropic vs Google Gemini のBatch API

| 項目 | OpenAI Batch API | Anthropic Message Batches API | Google Gemini Batch API(Batch Mode) |
|---|---|---|---|
| 割引率 | 約50%(全モデル一律) | 50%(全モデル一律、入力・出力とも) | 約50%(標準の同期呼び出し比) |
| 完了までの目安 | 24時間以内(実際は1〜6時間程度で終わることが多い) | 24時間以内(実際は1時間以内で終わることが多い) | 24時間以内(実際はより短時間で終わることが多い) |
| リクエストの渡し方 | JSONLファイルをFiles APIでアップロード | APIリクエストの`requests`配列に直接まとめて送信 | インライン埋め込み(20MB未満目安)、またはJSONLファイルのアップロード |
| 1バッチの上限 | 最大5万リクエスト、ファイルサイズ200MBまで | 最大10万リクエスト、256MBまで | ファイルサイズ最大2GBまで |
| 対応エンドポイント・モデル | `/v1/chat/completions`、`/v1/responses`、`/v1/completions`、`/v1/embeddings`、`/v1/moderations`、画像・動画生成系など | Messages API相当のほぼ全機能(画像入力・Tool Use・システムプロンプト・マルチターン・拡張思考など、全アクティブモデル対応) | テキスト生成(`generateContent`)、埋め込み(`gemini-embedding-001`など)、OpenAI SDK互換の`/v1/chat/completions`形式 |
| 結果ファイルの保存期間 | 自動削除なし(手動削除、または`expires_after`で14〜30日を設定可能) | 作成から29日間ダウンロード可能 | 個別に確認(公式ドキュメント参照。ジョブ自体は一定期間後にクリーンアップされる) |
| 結果の識別方法 | `custom_id`で突き合わせ(順序は保証されない) | `custom_id`で突き合わせ(順序は保証されない) | リクエストの並び順、またはインライン応答内の対応関係で突き合わせ |

3社とも「半額・24時間以内・JSON系フォーマットでの一括投入・専用のレート制限枠」という基本構造は共通しているため、複数プロバイダーを併用する場合も考え方を使い回しやすい。ただし結果ファイルの保存期間や対応エンドポイントの細部は異なるため、乗り換えや併用時は必ず各社の最新ドキュメントで確認する。

### ノーコード・軽量な使い方

自分でコードを書かなくても、DifyやGASでバッチ的な処理を組める場合がある。

- **GAS(Google Apps Script)**: スプレッドシートに溜まった問い合わせを一度に読み込み、夜間トリガーで`UrlFetchApp`からバッチ作成・結果取得のAPIを順に呼ぶ処理を書けば、擬似的な夜間一括処理が組める
- **Dify**: ワークフローの中でBatch API自体を直接扱う機能は標準では薄いため、大量データの一括処理はまず社内のスクリプト(GASやPythonなど)でBatch APIを呼び、結果をDifyのナレッジベースやDBに取り込む形が現実的

## 注意点・よくある誤解

- **「即時性がいらない」の見極めを誤らない**: バッチ処理中はリクエストの内容を後から修正できない。分類ルールやプロンプトに誤りがあると、数万件分の結果が丸ごとやり直しになるため、本番投入前に少量サンプルを通常のAPIでテストしてから流す。
- **結果の順序は保証されない**: 入力と同じ順で結果が返ってくるとは限らないため、必ず`custom_id`で元データと突き合わせる設計にする。
- **期限内に終わらないリクエストがある**: 混雑状況によっては24時間以内に処理しきれず「期限切れ」になるリクエストが一定数出ることがある。バッチ全体が失敗するわけではなく、その分だけ課金されず終了扱いになるので、期限切れ分は次のバッチで再投入するなどのリトライ設計をしておく。
- **エラー行の扱い**: フォーマット不備や無効なリクエストは結果ファイル上でエラーとして返ってくる。バッチ全体を止めずに一部だけ失敗する設計になっているため、結果を受け取った後にエラー行だけ抽出して個別対応する処理を組み込んでおくとよい。
- **ストリーミングやリアルタイム系オプションは使えない**: バッチはまとめて結果を返す方式のため、`stream`(逐次出力)などリアルタイム用のオプションは指定できない。
- **結果ファイルの保存期間はプロバイダーごとに違う**: OpenAIは明示的に削除するか`expires_after`を設定しない限り結果ファイルが残り続けるのに対し、Anthropicは作成から29日で結果がダウンロードできなくなる。「後でまとめて取得すればいい」と放置すると、Anthropic側では取りこぼす恐れがあるため、バッチ完了後はなるべく早く結果を回収してシステム側に保存しておく。
- **Batch用のレート制限は通常のAPIと別枠**: 3社とも「バッチ専用の投入待ちキュー上限」を別に持つため、通常のAPIのレート制限には直接影響しない一方、バッチ自体にも独自の上限(同時実行数・投入待ちリクエスト数など)があるので、大量のバッチを同時に投げすぎると待ち行列が詰まることがある。
- **料金・上限は変更が多い分野**: バッチの割引率・上限件数・対応エンドポイントは各社とも改定が入りやすいため、本番運用前に必ず公式ドキュメントの最新情報を確認する。

## 最初の一歩

社内に「急ぎではないが数百件以上まとめて処理したいテキストデータ」(問い合わせの分類、議事録の要約など)がないか棚卸しし、まずは10件程度の小さなJSONLファイルを作ってBatch APIに投げてみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)
- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [RAG(検索拡張生成)の基本](../part07-data-analysis/rag-basics.md)

## 更新履歴

### 2026-07-29: Google Gemini Batch APIの節を新設し、3社比較表・料金/上限を最新化
- **内容**: OpenAI Batch APIの対応エンドポイントを画像・動画生成系まで拡張して更新、結果ファイルの保存期間の違い(OpenAIは自動削除なし・Anthropicは29日・Gemini)を整理。Anthropic Message Batches APIは100,000件/256MB・50%割引・29日保存・全アクティブモデル対応・1時間キャッシュ推奨を再確認。Google Gemini Batch API(Batch Mode)を新規に1セクション追加し、インライン送信(20MB未満)とJSONLファイルアップロード(最大2GB)の2方式、埋め込みモデル対応、2026年6月に追加されたOpenAI SDK互換レイヤーを解説。比較表をOpenAI/Anthropic/Google Geminiの3社比較に拡張し、注意点にBatch専用レート制限・結果保存期間の違いを追記
- **出典**: [Anthropic: Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)、[OpenAI Developer Community: Batch API is now available](https://community.openai.com/t/batch-api-is-now-available/718416)、[OpenAI Help Center: Batch API FAQ](https://help.openai.com/en/articles/9197833-batch-api-faq)、[Google Developers Blog: Batch Mode in the Gemini API](https://developers.googleblog.com/scale-your-ai-workloads-batch-mode-gemini-api/)、[Google Developers Blog: Gemini Batch API now supports Embeddings and OpenAI Compatibility](https://developers.googleblog.com/en/gemini-batch-api-now-supports-embeddings-and-openai-compatibility/)、[Google AI for Developers: Batch API](https://ai.google.dev/gemini-api/docs/batch-api)

### 2026-07-06: 初版執筆
- **内容**: Batch APIの基本的な仕組み(JSONLでの一括送信・24時間以内の非同期処理・約50%の割引)、OpenAI Batch APIとAnthropic Message Batches APIの使い方と比較表、業務での使いどころ(サポートチケット分類・文書要約・RAG向け埋め込み生成・モデレーション)、注意点を整理
- **出典**: [OpenAI: Batch API](https://developers.openai.com/api/docs/guides/batch)、[OpenAI Developer Community: Batch API file size limit](https://community.openai.com/t/openai-file-size-limit-and-batch-api-result-files/897738)、[Anthropic: Batch processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing)、[Google Developers Blog: Batch Mode in the Gemini API](https://developers.googleblog.com/scale-your-ai-workloads-batch-mode-gemini-api/)
