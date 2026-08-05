---
title: "DifyのAPI連携(作ったアプリを外部システムから呼び出す)"
part: 10
chapter: 第2章 Difyワークフロー
tags: [Dify, API連携, Webhook, 外部システム連携, GAS, チャットボット埋め込み]
created: 2026-07-06
updated: 2026-08-02
---

# DifyのAPI連携(作ったアプリを外部システムから呼び出す)

## これは何か

Dify上でチャットボット・エージェント・ワークフローを作って「公開する」を押すと、そのアプリには自動的にAPIエンドポイント(外部プログラムがアクセスするための接続先URL)とAPIキー(呼び出し元を認証するための鍵となる文字列)が発行される。これにより、Difyの画面を開かなくても、自社サイトのチャットウィジェット・Slack・GAS(Google Apps Script)・Make・n8nなどの自動化ツール・社内システムなど、Dify以外のあらゆる場所からそのアプリを部品として呼び出せるようになる。「Dify内で完結する業務」から「Difyで作った処理を他システムに組み込む」への橋渡しをするのがAPI連携である。

2025年後半以降のDify(v1.10系)では、外部システムがDifyのAPIを「呼びに行く」従来の方式に加えて、外部システムからのHTTPリクエストを受け取ってワークフローを起動する「Webhookトリガー」がワークフローのノードとして標準搭載された。呼び出す/呼ばれるの両方向を押さえておくと、他システムとの連携パターンの選択肢が広がる。

## 仕組み・背景

### APIキー発行の画面

APIキーはアプリ単位で発行する。Difyの「スタジオ」でアプリを開くと、画面左側のメニュー(または右上の「公開する」ボタン付近のタブ、UIバージョンにより位置が異なる)に「APIアクセス(API Access)」という項目があり、これを開くと「APIキー」セクションがある。「新しいシークレットキーを作成」をクリックすると発行できる。発行されたキーは`app-`から始まる文字列で、以後すべてのAPIリクエストのAuthorizationヘッダーに`Bearer {APIキー}`の形式で付与する。APIキーはアプリ単位の紐付けであり、あるアプリ用に発行したキーは別のアプリでは使えない点に注意する。

同じ「APIアクセス」画面には、エンドポイント一覧・パラメータ説明・言語別サンプルコードを含むAPIリファレンスが表示されるので、実装時はそこを一次情報として参照する。

### エンドポイントの種類(アプリタイプで変わる)

Difyはアプリのタイプによって呼び出すエンドポイントが異なる。

| アプリタイプ | 主なエンドポイント | 特徴 |
|---|---|---|
| チャットボット・エージェント・チャットフロー | `POST /v1/chat-messages` | 会話の継続を前提とし、`conversation_id`(会話ID)を使ってやり取りの文脈を維持する |
| テキスト生成アプリ(要約・翻訳など単発処理) | `POST /v1/completion-messages` | 会話の概念がなく、1回の入力に対して1回の出力を返す |
| ワークフロー | `POST /v1/workflows/run` | [Difyワークフローの基本](./dify-workflow-basics.md)で触れた通り、`conversation_id`を持たず毎回独立した処理として実行される。時間のかかる処理では`workflow_run_id`を使って`GET /v1/workflows/run/<workflow_run_id>`をポーリングする |

### リクエスト・レスポンスの基本構造

いずれのエンドポイントもJSON形式でやり取りする。チャットメッセージ送信(`/v1/chat-messages`)の主なリクエスト項目は次の通り。

| パラメータ | 内容 |
|---|---|
| `query` | ユーザーの発言・質問文(必須) |
| `inputs` | アプリ側で定義した変数をキー/値で渡す(既定は空オブジェクト`{}`) |
| `response_mode` | `blocking`(処理完了後に結果を一括で返す同期モード)または`streaming`(SSE=Server-Sent Eventsで逐次配信するモード、公式は基本こちらを推奨) |
| `conversation_id` | 会話を継続する場合に前回のレスポンスで受け取ったIDを指定。新規会話なら空にする |
| `user`(必須) | アプリ内でエンドユーザーを識別するための任意の文字列(例: 社員IDやメールアドレスのハッシュ値) |

`blocking`モードのレスポンスにはJSONで`answer`(回答文)や`conversation_id`などが返る。ワークフロー実行(`/v1/workflows/run`)では`outputs`にワークフローの終了ノードで定義した出力が入る。

### 公式SDK(クライアントライブラリ)

curlで直接叩く以外に、開発元langgeniusが公式に配布しているSDKもある。認証ヘッダーの組み立てやストリーミング(SSE)受信の実装を自分で書かずに済むため、アプリ開発に組み込む場合はSDKの利用を検討するとよい。

| 言語 | パッケージ | 導入コマンド |
|---|---|---|
| Node.js | `dify-client` | `npm install dify-client` |
| Python | `dify-client`(PyPI)/ `dify_client` | `pip install dify-client` |
| Go・Ruby | コミュニティ/公式リポジトリで別途配布 | 各リポジトリのREADME参照 |

いずれもDify本体または`langgenius`名義のGitHubリポジトリで管理されている。バージョンによって対応APIの網羅度が異なるため、導入前にREADMEで対応エンドポイントを確認する。

### Webhookトリガー(外部システム→Difyを起動する)

「APIで呼び出す」の逆方向として、ワークフローのキャンバスに「Webhookトリガー」ノードを置くと、ノードごとに固有のHTTP URLが発行される。外部システムがそのURLにリクエストを送るとワークフローが起動し、リクエストのクエリパラメータ・ヘッダー・ボディの内容がそのままワークフロー内の変数として使える。スプレッドシートの拡張機能・外部SaaSのWebhook通知・社内システムのイベント発火など、「Dify側から定期的に見に行く」のではなく「何かが起きた瞬間にDifyを動かしたい」場合に、HTTPリクエストノードを使う回りくどい構成をとらずに済む。

## 使いどころ・使い分け

### Dify画面内で完結させる vs API連携する

| やりたいこと | 適した方法 |
|---|---|
| 社内の限られたメンバーだけが使う、Difyにログインしての利用で十分 | Difyの「スタジオ」画面をそのまま使う(API不要) |
| 自社サイトに手軽にチャット窓を付けたいだけで、見た目のカスタマイズは最小限でよい | 「公開する」→「サイトに埋め込む」から発行される`iframe`タグまたは`script`タグを貼るだけの埋め込み機能(コード連携不要)。DifyのChrome拡張機能も同様の手軽さで使える |
| 自社サイトのデザインに完全に合わせたUIにしたい、ログイン中のユーザー情報と連動させたい | API連携(`chat-messages`をバックエンド経由で呼び出し、フロントは自社実装) |
| SlackやTeamsなどのチャットツールから呼び出したい | API連携(Slackの Bot・ワークフロー機能からDifyのAPIをHTTPで叩く) |
| GASでスプレッドシートやGmailと組み合わせ、定期実行・トリガー実行したい | API連携(後述のGAS連携例を参照) |
| 外部SaaS側のイベント(フォーム送信・レコード追加など)が起きた瞬間にDifyを動かしたい | Webhookトリガー(Difyがリクエストを受け取る側になる、上記参照) |
| 社内の別システム(基幹システム・CRM等)からバッチ的に呼び出したい | API連携(`workflows/run`が本命) |

### DifyのAPI連携 と n8n/Make/Zapier/Difyワークフロー内連携との違い

似た言葉が並ぶため混同しやすいが、「誰が主導権を持つか」で整理すると分かりやすい。

- **DifyのAPI連携(本ページの内容)**: 外部システム側が主導権を持ち、必要なタイミングでDifyのアプリを「関数」のように呼び出す。呼び出し元は自社サイト・Slack・GAS・社内システムなど何でもよい
- **Difyワークフロー内の「HTTPリクエスト」ノード**([Difyワークフローの主要ノードと組み立て方](./dify-workflow-nodes.md)参照): Dify側が主導権を持ち、ワークフローの処理の途中で外部のAPIを呼びに行く。方向が逆(Difyから外へ)である点に注意
- **Webhookトリガー(本ページの仕組み・背景を参照)**: 外部システムがDifyに向けてリクエストを送り、Difyのワークフローを起動する。「呼び出す」ではなく「呼ばれる」側になる点がAPI連携と対称的
- **n8n経由の連携**([n8nの基本](./n8n-basics.md)参照): n8nのHTTP RequestノードからDifyのAPIを呼ぶ、あるいは逆にDifyのHTTPリクエストノード・Webhookトリガーからn8nのWebhookを呼ぶ、双方向の組み合わせが可能。多数のSaaSをまたぐ複雑な条件分岐や、Difyの標準ツールにない連携が必要な場合はn8nを間に挟む構成が有効
- **Make経由の連携**([Makeの基本](./make-basics.md)参照): MakeにはDify専用の公式アプリ(モジュール)があり、「ワークフローを実行する」「任意のAPIコールを行う」といったモジュールをシナリオの中にドラッグ&ドロップで組み込める。汎用のHTTPモジュールで自前実装するより設定が速い
- **Zapier経由の連携**: DifyにZapier専用の公式アプリは(2026年8月時点で)なく、ZapierのWebhook(汎用HTTP)アクションからDifyのAPIを呼ぶか、DifyのMCP(Model Context Protocol、AIがツールを呼び出すための標準規格。詳細は[MCP(Model Context Protocol)の基本](../part09-api-development/mcp-basics.md)参照)対応プラグイン経由でZapier MCPのツール群をDifyのエージェントから利用する構成になる

## 実務での使い方

### 手順1: APIキーを発行する(画面操作)

1. Difyの「スタジオ」で対象のアプリを開く
2. アプリが未公開の場合は、まず画面右上の「公開する」をクリックして最新版を公開する
3. 画面左のメニュー(またはアプリ画面上部)にある「APIアクセス」を開く
4. 「APIキー」セクションの「新しいシークレットキーを作成」をクリックして発行する。発行直後にだけ全文が表示されるため、その場でパスワード管理ツール等に控える
5. 同じ画面にAPIリファレンス(エンドポイント一覧・パラメータ説明・言語別のサンプルコード)も表示されるので、実装時に参照する

### 手順2: チャットメッセージを送信する(curl例、コピペ可)

```bash
curl -X POST 'https://api.dify.ai/v1/chat-messages' \
  --header 'Authorization: Bearer app-xxxxxxxxxxxxxxxx' \
  --header 'Content-Type: application/json' \
  --data-raw '{
    "inputs": {},
    "query": "有給休暇の繰越は何日までできますか?",
    "response_mode": "blocking",
    "conversation_id": "",
    "user": "user-001"
  }'
```

レスポンス例(`blocking`モード、抜粋):

```json
{
  "answer": "就業規則第◯条により、繰越可能な有給休暇は最大10日までです。",
  "conversation_id": "b5f7...",
  "message_id": "a1c2..."
}
```

2回目以降の発言では、レスポンスに含まれた`conversation_id`を次のリクエストにそのまま渡すことで、会話の文脈を保った状態でやり取りを続けられる。ワークフローを呼ぶ場合は`https://api.dify.ai/v1/workflows/run`に対して`inputs`(ワークフローの開始ノードで定義した入力変数)と`response_mode`、`user`を送る点は共通だが、`query`や`conversation_id`は使わない(自己ホスト版を使っている場合はホスト名を`https://api.dify.ai`から自社のドメインに読み替える)。

### 手順3: GASと組み合わせて定期実行する

[GAS(Google Apps Script)からのAI API連携](../part09-api-development/gas-ai-api-integration.md)で解説した`UrlFetchApp`(GASから外部APIを呼ぶ標準機能)と`PropertiesService`(APIキーを安全に保管する仕組み)は、OpenAIやGeminiだけでなくDifyのAPIにもそのまま応用できる。例えば「スプレッドシートに並んだ問い合わせ文を、Difyで作った分類・回答生成ワークフローに1行ずつ渡し、結果を隣の列に書き戻す」処理は次のように書ける。

```javascript
function callDifyWorkflow(inquiryText) {
  const apiKey = PropertiesService.getScriptProperties().getProperty('DIFY_API_KEY');
  const url = 'https://api.dify.ai/v1/workflows/run';

  const payload = {
    inputs: { inquiry_text: inquiryText },
    response_mode: 'blocking',
    user: 'gas-batch-user'
  };

  const options = {
    method: 'post',
    contentType: 'application/json',
    headers: { Authorization: 'Bearer ' + apiKey },
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };

  const response = UrlFetchApp.fetch(url, options);
  const json = JSON.parse(response.getContentText());
  return json.data.outputs.reply_text; // ワークフローの終了ノードで定義した出力変数名に合わせる
}
```

これに時間主導型トリガー(GASの「トリガー」画面から「時間主導型」を選択して設定)を組み合わせれば、「1時間おきにスプレッドシートの未処理行をDifyのワークフローに渡し、回答案を自動生成する」といった定期バッチ処理が、追加のサーバーなしで組める。GAS側の`OPENAI_API_KEY`と同じ要領で、スクリプトプロパティに`DIFY_API_KEY`を登録してから使う。

### 手順4: Make・n8nから呼び出す(自動化ツール経由)

- **Make**: シナリオ編集画面で「モジュールを追加」→「Dify」を検索すると公式アプリが見つかる。「Execute a workflow」(ワークフローを実行)モジュールを使えば、APIキーの接続設定(Connection)を1回作るだけで、以降はGUI上でアプリ選択・`inputs`のマッピングができ、curlやコードを書かずに済む。より自由度が必要な場合は同アプリの「Make an API call」(汎用APIコール)モジュールで任意のエンドポイントを叩ける
- **n8n**: 標準の「HTTP Request」ノードを使い、Method=POST・URL=`https://api.dify.ai/v1/chat-messages`(または`workflows/run`)・HeaderにAuthorizationを設定すればよい。[n8nの基本](./n8n-basics.md)で解説した認証情報(Credentials)の仕組みにAPIキーを登録しておくと、複数のワークフローで使い回せる

### 主要な使い方の対応付け

| やりたいこと | 使うエンドポイント/機能 |
|---|---|
| 自社サイトにチャット窓を手軽に埋め込みたい | 「公開する」→「サイトに埋め込む」の`iframe`/`script`タグ(APIキー不要) |
| 自社サイトに完全カスタムのチャットUIを作りたい | `POST /v1/chat-messages`をバックエンド経由で呼ぶ |
| Slackから質問できるようにしたい | Slack Bot側からDifyの`chat-messages`をHTTPで呼び出す(またはDify Marketplaceの既製Slack連携プラグインを利用) |
| GASで定期バッチ処理したい | `POST /v1/workflows/run`を`UrlFetchApp`から呼ぶ(上記コード例) |
| Make・n8nからノーコードで呼び出したい | Makeの公式Difyアプリ、またはn8nのHTTP Requestノード |
| 外部SaaS側のイベントでDifyを起動したい | ワークフローの「Webhookトリガー」ノードで発行されるURLに向けて外部システムからPOSTする |
| 実行に時間がかかる重いワークフローを呼びたい | `workflows/run`実行後、レスポンスの`workflow_run_id`で`GET /v1/workflows/run/<workflow_run_id>`をポーリング |

## 注意点・よくある誤解

- **APIキーの漏洩リスク**: APIキーはアプリ全体への実行権限を持つため、フロントエンドのJavaScriptに直接書き込むと誰でも閲覧・盗用できてしまう。必ずバックエンド(サーバー側やGASのようなサーバーレス実行環境)で保持し、フロントエンドからは自社の別APIを経由して呼び出す構成にする。GAS連携では[GAS(Google Apps Script)からのAI API連携](../part09-api-development/gas-ai-api-integration.md)で解説した`PropertiesService`(スクリプトプロパティ)への保存が有効
- **キーが流出した場合はAPIアクセス画面から即座に無効化する**: 「APIキー」一覧から該当のキーを削除し、新しいキーを発行して呼び出し元をすべて更新する。定期的なキーのローテーション(発行し直し)も検討する
- **料金プランはメッセージクレジット制**: Dify Cloudの料金は2026年8月時点でSandbox(無料)/Professional(月59ドル、年払いなら590ドル)/Team(月159ドル、年払いなら1,590ドル)/Enterprise(個別見積り)の4段階。課金の基本単位は「メッセージクレジット」(チャットの1回答・エージェントの1ステップ・ワークフロー内のモデル呼び出し1回などを1クレジットとしてカウントする消費枠)で、Sandboxは登録時に200クレジットのみ・Professionalは月5,000クレジット・Teamは月10,000クレジットが上限になる。クレジットを使い切ると追加購入または上位プランへの移行が必要になるため、GASでの一括処理などクレジット消費が急に増える用途では事前に想定回数を見積もっておく
- **APIの純粋なレート制限(呼び出し回数/月)はSandboxのみ**: Sandboxプランは月5,000回のAPI呼び出し上限があるが、Professional以上ではこのAPI呼び出し自体の回数上限は撤廃される(クレジット消費の上限が実質的な歯止めになる)。自己ホスト(OSS)版では、こうしたプラットフォーム側の制限自体が存在しない
- **ナレッジベース検索には別枠のレート制限がある**: RAG(ナレッジベースを検索して回答に活用する仕組み)を伴うアプリをAPI経由で呼ぶ場合、ワークスペース単位で「1分あたりの検索・登録操作数」の上限が別途あり、Sandboxは10回/分、Professionalは100回/分、Teamは1,000回/分が目安(2026年8月時点)。上限を超えると一時的にナレッジベース関連の操作が制限される
- **429エラー(レート制限超過)への備え**: 短時間に大量のリクエストを送ると一時的にリクエストが拒否されることがある。GASなどでループ処理をする場合は、1件ごとに数百ミリ秒程度の間隔を空ける、エラー時にリトライする、といった作りにしておくと安定する
- **`user`パラメータは適当な固定値にしない**: エンドユーザーを識別するための項目のため、全リクエストで同じ値を使うと会話やレート制御の単位が意図せず混ざることがある。実際の利用者やバッチの処理単位ごとに区別できる値を設定する
- **ワークフローAPIには会話の概念がない**: `workflows/run`は呼び出しごとに独立した処理で、`chat-messages`のような`conversation_id`による文脈維持はできない。対話を継続させたい場合はチャットフロー+`chat-messages`を選ぶ

## 最初の一歩

Difyで作成済みの(または簡単な要約・分類用に新規作成した)アプリを1つ選び、「公開する」→「APIアクセス」からAPIキーを発行して、上記のcurl例のクエリ文だけ自分の質問に書き換えてターミナルから実行し、レスポンスのJSONが返ってくることを確認してみる。

## 関連トピック

- [Difyワークフローの基本](./dify-workflow-basics.md)
- [Difyワークフローの主要ノードと組み立て方](./dify-workflow-nodes.md)
- [GAS(Google Apps Script)からのAI API連携](../part09-api-development/gas-ai-api-integration.md)
- [MCP(Model Context Protocol)の基本](../part09-api-development/mcp-basics.md)
- [n8nの基本](./n8n-basics.md)
- [Makeの基本](./make-basics.md)

## 更新履歴

### 2026-08-02: 料金体系・SDK・Webhookトリガー・自動化ツール連携の節を最新化
- **内容**: 料金プランを「メッセージクレジット」制の最新体系(Sandbox/Professional 月59ドル/Team 月159ドル/Enterprise)に更新し、Professional以上ではAPI呼び出し回数のレート制限自体が撤廃されクレジット消費が実質的な上限になる点、ナレッジベース検索の別枠レート制限(Sandbox 10回/分・Professional 100回/分・Team 1,000回/分)を反映。ワークフローノードとして標準搭載された「Webhookトリガー」(外部システムからDifyを起動する仕組み)、公式SDK(Node.js/Python)、MakeのDify公式アプリとn8nのHTTP Requestノードによる連携手順、ZapierはDify公式アプリがなくWebhook/MCP経由になる点を追記。APIキー発行画面の位置に関する記述を実態に合わせて修正
- **出典**: [Dify Pricing Teardown 2026 (DEV Community)](https://dev.to/beton/dify-pricing-teardown-2026-42g5)、[Dify Pricing 2026 (comparedge.com)](https://comparedge.com/tools/dify-ai/pricing)、[Dify Pricing 2026 (CheckThat.ai)](https://checkthat.ai/brands/dify/pricing)、[Dify Cloud Pricing: Plans, Free Tier, and When to Self-Host](https://www.architjn.com/blog/dify-cloud-pricing-plans-free-tier-when-to-self-host)、[Dify Docs: Knowledge Request Rate Limit](https://docs.dify.ai/en/use-dify/knowledge/knowledge-request-rate-limit)、[Dify Docs: Webhook Trigger](https://docs.dify.ai/en/cloud/use-dify/nodes/trigger/webhook-trigger)、[Dify Blog: Introducing Trigger](https://dify.ai/blog/introducing-trigger)、[Dify Blog: Which Trigger Should I Use?](https://dify.ai/blog/which-trigger-should-i-use-a-beginner-s-guide-to-starting-dify-workflows)、[Make: Dify Integration](https://www.make.com/en/integrations/dify)、[Dify Blog: MCP Plugin Hands-On Guide (Zapier連携)](https://dify.ai/blog/dify-mcp-plugin-hands-on-guide-integrating-zapier-for-effortless-agent-tool-calls)、[GitHub: langgenius/dify-python-sdk](https://github.com/langgenius/dify-python-sdk)、[npm: dify-client (langgenius/dify nodejs-client)](https://github.com/langgenius/dify/tree/main/sdks/nodejs-client)
- **注記**: Dify公式サイト(dify.ai/pricing)はスクレイピング防止の設定によりツールから直接取得できなかったため、複数の独立した第三者ソース(dev.to・comparedge.com・CheckThat.ai・architjn.com)の記載が一致することを確認した上で採用している。掲載・記事化前に公式ページで金額・上限値の最終確認を推奨

### 2026-07-06: 初版執筆
- **内容**: Difyの各アプリタイプ(チャットボット/テキスト生成/ワークフロー)で自動発行されるAPIエンドポイント・APIキーの仕組み、APIキー発行の画面操作手順、`chat-messages`/`completion-messages`/`workflows/run`の使い分けとリクエスト/レスポンスの基本構造、curlによる呼び出し例、GAS連携ページと組み合わせた定期バッチ処理の実装例、埋め込みウィジェット・n8n経由連携との違い、APIキー管理とレート制限の注意点を整理
- **出典**: [Dify Docs: Send Chat Message](https://docs.dify.ai/api-reference/chat/send-chat-message)、[Dify Docs: API(Developing with APIs)](https://docs.dify.ai/en/use-dify/publish/developing-with-apis)、[Dify Docs(日本語): API統合](https://docs.dify.ai/ja-jp/guides/application-publishing/developing-with-apis)、[Dify Docs(日本語): Webサイトへの埋め込み](https://docs.dify.ai/ja-jp/guides/application-publishing/embedding-in-websites)、[Dify Docs: Knowledge Request Rate Limit](https://docs.dify.ai/en/use-dify/knowledge/knowledge-request-rate-limit)、[Dify Docs: Workflow & Chatflow](https://docs.dify.ai/en/self-host/use-dify/build/workflow-chatflow)、[HelloCraftAI: Dify APIキーの取得方法と設定手順をわかりやすく解説](https://hellocraftai.com/blog/dify-api%E3%82%AD%E3%83%BC%E3%81%AE%E5%8F%96%E5%BE%97%E6%96%B9%E6%B3%95%E3%81%A8%E8%A8%AD%E5%AE%9A%E6%89%8B%E9%A0%86%E3%82%92%E3%82%8F%E3%81%8B%E3%82%8A%E3%82%84%E3%81%99%E3%81%8F%E8%A7%A3%E8%AA%AC/)、[SIOS Tech Lab: Dify入門ガイド：Web公開・API活用する3つの方法](https://tech-lab.sios.jp/archives/45994)
- **注記**: APIキー発行画面のタブ名(「アクセスAPI」/「APIアクセス」)はDifyのバージョン・UI改訂によって表記が変わることがある。掲載・記事化前に実際の画面で最終確認を推奨
