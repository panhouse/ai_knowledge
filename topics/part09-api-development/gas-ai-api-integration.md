---
title: "GAS(Google Apps Script)からのAI API連携"
part: 9
chapter: 第3章 業務ツール連携
tags: [GAS, Google Apps Script, UrlFetchApp, PropertiesService, スプレッドシート, Gemini API, カスタム関数, 業務自動化]
created: 2026-07-06
updated: 2026-07-06
---

# GAS(Google Apps Script)からのAI API連携

## これは何か

「スプレッドシートに入力した問い合わせ文をAIで自動分類したい」「Gmailに来たメールの返信文案をAIに下書きさせたい」――こうした要望のたびに有料のSaaSを契約したり、社内にサーバーを立ててIT部門に依頼したりする必要はない。GAS(Google Apps Script、Googleスプレッドシート・ドキュメント・Gmailなどに組み込まれたJavaScriptベースの無料スクリプト環境)からAI APIのエンドポイントへ直接リクエストを送れば、追加のサーバーコストや契約なしに、普段使っているGoogleのツールの中にAI機能を組み込める。ノーコードツールほど手軽ではないが、多少のコードを貼り付けられる人であれば、社内の「ちょっとしたAI自動化」はほぼこの方法でカバーできる。

## 仕組み・背景

GASはGoogleのクラウド上でスクリプトが実行される仕組みで、自分のPCやサーバーを起動しっぱなしにする必要がない(スプレッドシートを閉じていてもトリガーで動く)。AI連携の中核になるのは次の2つの標準機能。

- **UrlFetchApp**: GASから外部のHTTPS APIを呼び出すための標準機能。OpenAI・Google Gemini・AnthropicのClaudeはいずれも「HTTPSでJSON形式のリクエストを送り、JSON形式の応答を受け取る」という共通の形を取っているため、`UrlFetchApp.fetch(url, params)`を使えば、どのAI APIも基本的に同じコードパターンで呼び出せる。
- **PropertiesService**: APIキーのような機密情報を、スクリプト本文に直接書かずに保存しておくための仕組み。`PropertiesService.getScriptProperties()`で取得できる「スクリプト プロパティ」という保管庫にキーを入れておき、実行時に読み出す。

これに加えて、スプレッドシートのセルに`=AI_SUMMARIZE(A1)`のように書ける**カスタム関数**(`@customfunction`という注釈を付けて定義する関数)を作れる点がGAS連携の大きな強みで、AI呼び出しを「関数」として業務担当者の手元まで届けられる。ただしカスタム関数には後述する実行時間・権限面の制約がある。さらに時間主導型のトリガー(一定間隔で自動実行する仕組み)を設定すれば、夜間バッチのような定期実行も組める。

Google自身のGemini APIについては、Google Cloudの公式Codelab(「Automate Google Workspace tasks with the Gemini API」)がGASからの呼び出し方法を解説しており、この組み合わせが公式にドキュメント化されている点はOpenAI・Anthropicとの違いといえる。手軽に試すだけなら、この記事のOpenAI・Claudeと同じ「APIキー+UrlFetchApp」方式で十分だが、Geminiにはもう一段"native"な選択肢もある。GASのスクリプトエディタには**Vertex AI**という組み込みのAdvanced Service(GmailApp・DriveAppと同じ位置づけの、コードを書かずに有効化できる専用サービス)があり、左メニューの「サービス」の「+」→「Vertex AI API」を追加すると、UrlFetchAppを自分で書かなくても`VertexAI.Endpoints.generateContent(payload, model)`のような専用メソッドでGemini(例: Gemini 2.5 Flash)を呼び出せる。ただしこちらは個人のAPIキーではなく、課金を有効化したGoogle CloudプロジェクトとAgent Platform API(旧Vertex AI API)の有効化が前提になるため、セットアップはAI StudioのAPIキー方式より重い。**個人・小規模チームでまず試すならAPIキー+UrlFetchApp、社内で既にGoogle Cloudプロジェクトを運用しているならVertex AI Advanced Serviceの方がAPIキーの受け渡し・失効管理が要らず安全**、という使い分けになる。本記事では汎用性の高いAPIキー+UrlFetchApp方式を中心に解説する。

## 使いどころ・使い分け

| 状況 | GASからの直接連携 | 向いている代替 |
|---|---|---|
| 個人・小規模チームでスプレッドシート/Gmail/Docsの作業を自動化したい | ◎ 向いている(サーバー不要・無料枠で足りることが多い) | - |
| 社外向けサービスや、同時に多数のユーザーが使うシステムに組み込みたい | △ 不向き(後述の実行時間・クォータ制限があり本番運用には力不足) | 自社サーバー、[Dify](../part10-nocode-lowcode/dify-workflow-nodes.md)などのノーコードAIアプリ基盤 |
| 数万件規模のデータを一括で要約・分類したい | △ 不向き(6分の実行時間制限に収まらない) | [バッチ処理(Batch API)の基本](batch-api-basics.md) |
| リアルタイムに近い応答速度が必要なチャット機能 | △ 不向き(UrlFetchAppは同期呼び出しで待ち時間がそのままユーザーに返る) | Dify・専用チャットボット製品 |
| セルの値をトリガーに「都度AIで加工する」軽い処理(要約・分類・翻訳・キーワード抽出) | ◎ 得意分野そのもの | - |

判断基準はシンプルで、「自分やチームの手元の業務改善で完結するか」「実行時間・呼び出し頻度が個人利用の範囲に収まるか」で分ける。社内向けの軽い自動化ならGASが最短ルート、社外向け・大量処理・高可用性が必要になった時点で専用の基盤に切り替える、という使い分けになる。

## 実務での使い方

### 事前準備: APIキーの取得

- **OpenAI**: platform.openai.com で発行([OpenAI APIの基本](openai-api-basics.md)参照)
- **Gemini**: Google AI Studio(aistudio.google.com)の「Get API key」から発行、または既存のGoogle Cloudプロジェクトで有効化
- **Claude(Anthropic)**: console.anthropic.com(Claude Developer Platform)で発行

いずれも従量課金のため、契約前に利用上限(Usage limits等)を設定しておく。

### ステップ1: スクリプトエディタを開く

Googleスプレッドシートを開き、メニューの「拡張機能」→「Apps Script」をクリックすると、ブラウザで動くスクリプトエディタが立ち上がる。

### ステップ2: APIキーをスクリプト プロパティに登録する

スクリプト本文に直接キーを書き込むと、後で誰かに共有・閲覧された際にキーが漏洩する。必ずスクリプト プロパティという保管庫に入れる。

1. スクリプトエディタ左側メニューの歯車アイコン「プロジェクトの設定」をクリック
2. 画面を下にスクロールし、「スクリプト プロパティ」の項目を見つける
3. 「スクリプト プロパティを追加」をクリックし、プロパティ(名前)に`OPENAI_API_KEY`のような分かりやすい名前、値にAPIキー本体を入力
4. 「スクリプト プロパティを保存」をクリック

(エディタのバージョンによっては、この画面に「スクリプト プロパティ」欄が表示されない場合がある。その場合は下記コードの`setProperty()`の行だけを一時的にエディタに貼り付けて1回だけ実行し、キーを保存したらその行は削除する、という方法でも同じ結果になる。)

コード側からは次のように読み出す。

```javascript
// 保存: 通常は上記のUI画面から入力するが、コードから設定することもできる
PropertiesService.getScriptProperties().setProperty('OPENAI_API_KEY', 'sk-xxxxxxxx');

// 読み出し: 実際の利用時はこちらだけを使う
const apiKey = PropertiesService.getScriptProperties().getProperty('OPENAI_API_KEY');
```

### ステップ3: カスタム関数を書く(OpenAIの例)

セルに`=AI_SUMMARIZE(A1)`と書けば、A1セルの文章をAIが1文で要約してくれる関数の例。

```javascript
/**
 * 指定したテキストをAIで日本語1文に要約する
 * @param {string} text 要約したい文章が入ったセル
 * @return {string} 要約結果
 * @customfunction
 */
function AI_SUMMARIZE(text) {
  if (!text) return '';

  const apiKey = PropertiesService.getScriptProperties().getProperty('OPENAI_API_KEY');
  const url = 'https://api.openai.com/v1/chat/completions';

  const payload = {
    model: '(使用するモデル名。2026年7月時点ではGPT-5.4 mini/nanoのような軽量・低コストモデルが候補。必ず platform.openai.com/docs/models で最新のモデル名を確認する)',
    messages: [
      { role: 'system', content: '与えられた文章を日本語で1文に要約して。要約以外の説明は出力しない。' },
      { role: 'user', content: text }
    ]
  };

  const options = {
    method: 'post',
    contentType: 'application/json',
    headers: { Authorization: 'Bearer ' + apiKey },
    payload: JSON.stringify(payload),
    muteHttpExceptions: true // trueにしないとエラー時に例外で処理が落ちてしまう
  };

  const response = UrlFetchApp.fetch(url, options);
  const json = JSON.parse(response.getContentText());

  if (json.error) {
    return 'エラー: ' + json.error.message;
  }
  return json.choices[0].message.content;
}
```

### ステップ4: 権限を事前に承認しておく

カスタム関数はセルの中から自動的に呼ばれる性質上、実行中に「このアプリを承認しますか」という確認ダイアログを表示できない。そのため、`=AI_SUMMARIZE(A1)`をセルに入力する前に、スクリプトエディタ上部の関数選択ドロップダウンから`AI_SUMMARIZE`(または動作確認用の別関数)を選び、▶(実行)ボタンを一度手動で押して、UrlFetchAppを使うための権限(外部リクエストの許可)を承認しておく必要がある。この手順を省くと、セルには`#ERROR!`だけが表示され原因が分かりにくい。

### ステップ5: 実際にセルで使う

スプレッドシートに戻り、任意のセルに`=AI_SUMMARIZE(A1)`と入力すれば、A1の文章の要約がそのセルに表示される。分類なら「クレーム/質問/要望のいずれかだけを1語で返して」のようにプロンプトを変えるだけで応用できる。

### GeminiとClaudeを呼ぶ場合の違い

仕組みは共通だが、APIキーの渡し方や応答の取り出し方がプロバイダーごとに異なる。

| 項目 | OpenAI | Gemini | Claude(Anthropic) |
|---|---|---|---|
| エンドポイント | `https://api.openai.com/v1/chat/completions` | `https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent` | `https://api.anthropic.com/v1/messages` |
| APIキーの渡し方 | `Authorization: Bearer ...` ヘッダー | URLのクエリパラメータ `?key=...` | `x-api-key` ヘッダー |
| 追加で必要なヘッダー | なし | なし | `anthropic-version`(バージョン指定が必須) |
| 応答からテキストを取り出す場所 | `json.choices[0].message.content` | `json.candidates[0].content.parts[0].text` | `json.content[0].text` |

Geminiを呼ぶ場合のコード例(APIキーはURLに付ける点がOpenAI/Claudeと異なる)。

```javascript
function AI_SUMMARIZE_GEMINI(text) {
  if (!text) return '';
  const apiKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
  const model = '(使用するモデル名。例: Gemini Flash系の軽量モデル。ai.google.dev/gemini-api/docs/models で最新のモデル名を確認する)';
  const url = 'https://generativelanguage.googleapis.com/v1beta/models/' + model
    + ':generateContent?key=' + apiKey;

  const payload = {
    contents: [
      { parts: [ { text: '次の文章を日本語で1文に要約して:\n' + text } ] }
    ]
  };

  const options = {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };

  const response = UrlFetchApp.fetch(url, options);
  const json = JSON.parse(response.getContentText());
  return json.candidates[0].content.parts[0].text;
}
```

Claudeを呼ぶ場合は、`x-api-key`と`anthropic-version`の2つのヘッダーを付ける点と、`max_tokens`(出力上限トークン数)が必須パラメータである点がOpenAIと異なる。

```javascript
function callClaude(text) {
  const apiKey = PropertiesService.getScriptProperties().getProperty('ANTHROPIC_API_KEY');
  const url = 'https://api.anthropic.com/v1/messages';

  const payload = {
    model: '(使用するモデル名)',
    max_tokens: 300,
    messages: [
      { role: 'user', content: '次の文章を日本語で1文に要約して:\n' + text }
    ]
  };

  const options = {
    method: 'post',
    contentType: 'application/json',
    headers: {
      'x-api-key': apiKey,
      'anthropic-version': '2023-06-01'
    },
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };

  const response = UrlFetchApp.fetch(url, options);
  const json = JSON.parse(response.getContentText());
  return json.content[0].text;
}
```

### Gmail自動下書き・Docs要約への応用

セル関数と同じ「AI APIを呼ぶ関数」を、Gmail・Docsの操作と組み合わせれば応用範囲が広がる。

- **Gmail自動下書き**: `GmailApp.search()`で未対応の新着メールを検索し、本文をAI要約・返信文案生成の関数に渡し、`GmailApp.createDraft()`または`thread.createDraftReply()`で下書きを作成する(送信は必ず人が確認してから行う設計にする)。

```javascript
function draftAutoReplies() {
  const threads = GmailApp.search('is:unread label:inbox newer_than:1d');
  threads.forEach(function(thread) {
    const message = thread.getMessages().pop();
    const bodyText = message.getPlainBody();
    const draftText = callClaude('次のメールへの丁寧な返信文案を日本語で作成して:\n' + bodyText);
    thread.createDraftReply(draftText);
  });
}
```

- **Docs要約**: `DocumentApp.getActiveDocument().getBody().getText()`で本文テキストを取得し、AI要約関数に渡した結果を、文書の末尾や別のGoogleドキュメントに追記する。

これらは即時応答が不要なため、時間主導型のトリガーで「1時間おきに新着メールをチェック」のように定期実行させるのが実務的。トリガーの設定手順は次のとおり。

1. スクリプトエディタ左側メニューの時計アイコン(トリガー)をクリック
2. 右下の「トリガーを追加」をクリック
3. 「実行する関数を選択」で対象の関数(例: `draftAutoReplies`)を選ぶ
4. 「イベントのソースを選択」で「時間主導型」を選び、間隔(時間ベースのタイマー、例: 1時間おき)を指定
5. 「保存」をクリック

なお、GASには「Gmailに新着メールが来たら即実行する」という専用トリガーは存在しないため、実務上は時間主導型トリガーで定期的に新着を確認するパターンが標準になる。

## 注意点・よくある誤解

- **APIキーをスクリプト本文に直書きしない**: GASのプロジェクトは共同編集者に共有したり、コピーして配布したりできるため、コード中に`const apiKey = "sk-..."`のように書くと簡単に流出する。必ずPropertiesServiceに保存し、コードにはキーそのものを書かない。
- **カスタム関数は実行時間30秒、通常のスクリプトは6分で強制終了する**: セルの数式として呼ばれるカスタム関数は約30秒でタイムアウトし、それより長い処理(大量データの一括処理など)はトリガーやメニュー実行の通常の関数(こちらは1回の実行あたり最大6分。コンシューマ向け・Google Workspaceのアカウントいずれも同じ)に分けて設計する。6分を超える処理が必要な場合は、処理を分割して複数回のトリガー実行に分けるなどの工夫が必要。
- **カスタム関数は権限ダイアログを表示できない**: 事前に手動実行で承認しておかないと、セルに`#ERROR!`が出るだけで原因が分かりにくい。
- **セルの再計算が予期しない課金を生む**: カスタム関数はスプレッドシートを開き直したり、依存する他のセルを編集・並べ替えたりするたびに自動で再計算され、その都度AI APIが呼ばれて課金対象になる。数百行に一括でAI関数をコピーすると、シートを開くだけで数百回分のAPI呼び出しが走ることがある。対策としては、結果が確定したら「コピー→形式を選択して貼り付け→値のみ貼り付け」で数式を固定値に変換する、あるいはカスタム関数ではなく「ボタンを押した時だけ実行する」通常の関数+カスタムメニューの形にする方法がある。
- **UrlFetchAppには1日あたりの呼び出し回数の上限(クォータ)がある**: コンシューマ向けGoogleアカウントとGoogle Workspaceアカウントで上限が異なる。大量のセルに一斉適用する前に、想定呼び出し回数が上限に収まるか確認する。
- **本番の社外向けシステムには使わない**: GASは可用性やスケーラビリティを保証する仕組みではないため、多数のユーザーが同時にアクセスするサービスや、ミスがあった際の影響が大きい業務には不向き。その場合は自社サーバーや[Dify](../part10-nocode-lowcode/dify-workflow-nodes.md)などの専用基盤、大量データなら[バッチ処理(Batch API)の基本](batch-api-basics.md)を検討する。
- **モデル名・料金は変更が頻繁**: 本文のコード例では意図的に固定のモデル名を書かず「(使用するモデル名)」としている。実際に使うモデルは各社の公式ドキュメント(OpenAI: platform.openai.com、Gemini: ai.google.dev、Claude: platform.claude.com)で最新のものを確認する。

## 最初の一歩

OpenAI・Gemini・Claudeのいずれか1つでAPIキーを取得し、スプレッドシートの「拡張機能」→「Apps Script」からスクリプトプロパティにキーを登録した上で、テスト用のシートの1セルだけに`=AI_SUMMARIZE(A1)`を試してみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)
- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [バッチ処理(Batch API)の基本](batch-api-basics.md)
- [AIが扱いやすいデータ形式](../part07-data-analysis/ai-friendly-data-formats.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: GASからOpenAI/Gemini/Claude各APIをUrlFetchApp経由で呼び出す方法、PropertiesServiceによるAPIキーの安全な保存手順(画面の場所まで含む)、カスタム関数(`=AI_SUMMARIZE(A1)`)の実装例、GeminiのVertex AI Advanced Serviceという代替経路、Gmail自動下書き・Docs要約への応用、トリガー設定手順、実行時間制限・再計算による予期しない課金などの注意点を整理
- **出典**: [Google for Developers: Class UrlFetchApp](https://developers.google.com/apps-script/reference/url-fetch/url-fetch-app)、[UrlFetchApp: The Unofficial Documentation](https://justin.poehnelt.com/posts/definitive-guide-to-urlfetchapp/)、[Google for Developers: プロパティ サービス](https://developers.google.com/apps-script/guides/properties)、[Google for Developers: Quotas for Google Services](https://developers.google.com/apps-script/guides/services/quotas)、[Google for Developers: Authorization for Google Services](https://developers.google.com/apps-script/guides/services/authorization)、[Google for Developers: Installable Triggers](https://developers.google.com/apps-script/guides/triggers/installable)、[Google Codelabs: Automate Google Workspace tasks with the Gemini API](https://codelabs.developers.google.com/codelabs/gemini-workspace)、[Google for Developers: Vertex AI Service (Apps Script Advanced Services)](https://developers.google.com/apps-script/advanced/vertex-ai)、[Google for Developers: Quickstart: Generate text using Agent Platform](https://developers.google.com/apps-script/quickstart/vertex-ai)、[Google AI for Developers: Gemini API text generation](https://ai.google.dev/gemini-api/docs/text-generation)、[Claude Platform Docs: Messages API](https://docs.anthropic.com/en/api/messages)、[OpenAI: Introducing GPT-5.4 mini and nano](https://openai.com/index/introducing-gpt-5-4-mini-and-nano/)、[8bees.net: Google Apps Script 新エディターでのプロパティ設定場所](https://8bees.net/gas%E3%83%97%E3%83%AD%E3%83%91%E3%83%86%E3%82%A3%E8%A8%AD%E5%AE%9A%E5%A0%B4%E6%89%80)、[take-it-easy.site: スクリプトプロパティで機密情報と設定値を安全に管理する完全ガイド](https://blog.take-it-easy.site/gas/using-script-properties-in-gas/)、[AutoWorker: スプレッドシートでChatGPTライクの応答を返すカスタム関数を作成する方法](https://auto-worker.com/blog/?p=7167)、[LION AI: Google Apps Script（GAS）とは？できること・始め方・活用事例を徹底解説](https://www.lion-ai.co.jp/articles/google-apps-script-gas)
