---
title: "業務システム・SaaSとのAI API連携の基本(kintone・Slack・Excel/Power Automate等)"
part: 9
chapter: 第3章 業務ツール連携
tags: [kintone, Slack, Power Automate, AI Builder, Salesforce, API連携, Webhook, 業務システム連携]
created: 2026-07-06
updated: 2026-07-06
---

# 業務システム・SaaSとのAI API連携の基本(kintone・Slack・Excel/Power Automate等)

## これは何か

「kintoneに溜まった問い合わせをAIで自動分類したい」「Slackに来た質問にAIが即答してくれたら助かる」「Excelの表をAIに毎朝チェックしてもらいたい」——こうした要望に対して、新しいAIアプリをゼロから作る必要はない。すでに業務で使っているkintone・Slack・Microsoft Power Automate(Excel含む)・Salesforceといった業務システム・SaaS(クラウド上で提供されるソフトウェア)側から、直接または簡易なコードでAI API(ChatGPT・Claude・Geminiなどを呼び出すためのプログラム的な接続口)を呼び出せば、使い慣れた画面・データはそのままに、判断・要約・分類といったAIの処理だけを1ステップ追加できる。本ページは、[GAS(Google Apps Script)からのAI API連携](gas-ai-api-integration.md)がGoogle Workspace専用の連携方法を扱うのに対し、日本企業で広く使われる業務システム・SaaS側の標準機能から連携する場合の実務パターンと、そのための経路の選び方を整理する。

## 仕組み・背景

業務システム・SaaSとAI APIをつなぐ経路は、大きく3パターンに整理できる。どれも「業務システム側の何らかのイベント(レコード保存・メッセージ受信・行の追加など)をきっかけに、AI APIへリクエストを送り、結果を業務システムに書き戻す」という骨格は共通で、違いは「その橋渡しをどこで・誰が書くか」にある。

| パターン | 橋渡しの場所 | 必要なスキル | 代表例 |
|---|---|---|---|
| 1. 業務システム標準の機能+簡易コード | 業務システム自身のカスタマイズ機能・Webhook | JavaScriptなど簡易なコードが書ける人 | kintoneのJavaScriptカスタマイズ、SlackのIncoming Webhook/Bot |
| 2. 自動化ツール内蔵のAIコネクタ | Microsoft Power Automate等のRPA/自動化プラットフォーム | ローコード(GUI操作が中心) | Power AutomateのAI Builder・HTTPアクション |
| 3. ノーコード連携ツールを中継させる | 業務システムの外側に立つ中継ツール | ローコード(GUI操作が中心) | [n8n](../part10-nocode-lowcode/n8n-basics.md)・[Make](../part10-nocode-lowcode/make-basics.md)・[Zapier](../part10-nocode-lowcode/zapier-basics.md)・[Dify](../part10-nocode-lowcode/dify-api-integration.md) |

パターン1は「業務システムそのものにAI呼び出しのコードを埋め込む」方式で、追加のツール契約なしにAI APIの利用料だけで済むのが強みだが、業務システムのカスタマイズ機能の制約(後述のkintoneのプロキシ機能や、Slack Incoming Webhookの一方通行など)をそのまま受ける。パターン2は、すでにMicrosoft 365・Power Platformを契約している企業であれば、ライセンスの範囲内(ただし多くはプレミアムコネクタが必要)でGUI中心に組める。パターン3は、複数のSaaSをまたぐ複雑な自動化や、業務システム側に十分なカスタマイズ機能がない場合に強く、[n8nの基本](../part10-nocode-lowcode/n8n-basics.md)や[Makeの基本](../part10-nocode-lowcode/make-basics.md)、[Zapierの基本](../part10-nocode-lowcode/zapier-basics.md)で解説した各ツールの「Webhookトリガー→AIモジュール→書き戻し」という組み方がそのまま当てはまる。本ページではパターン3の各ツールの詳細には立ち入らず、パターン1・2を中心に、業務システム側から見た連携の実務を扱う。

## 使いどころ・使い分け

### 3つの経路の判断基準

| 観点 | 1. 業務システム標準+簡易コード | 2. 自動化ツール内蔵AIコネクタ | 3. ノーコード連携ツール中継 |
|---|---|---|---|
| 必要なスキル | JavaScript/HTTP APIの基礎が書ける人が1人いれば足りる | ほぼGUI操作。JSON設定の理解があると安心 | ほぼGUI操作 |
| 追加コスト | 既存の業務システム契約内で完結(AI API利用料のみ) | プレミアムコネクタ・AI Builder/Copilotクレジットなどの追加ライセンスが必要になることが多い | ノーコードツールの月額利用料が別途発生 |
| リアルタイム性 | 高い(業務システムのイベントに直結させやすい) | 中(フローの起動トリガーの粒度に依存) | 中〜低(ツール側のポーリング間隔に依存する場合がある) |
| 複数SaaSを横断する自動化のしやすさ | 低い(基本は1システム内で完結) | 中(Power Platform内の他コネクタと組み合わせ可) | 高い(1,000以上のアプリをまたいで組める) |
| 向いている組織 | 社内に簡易コードを書ける担当者がいる | すでにMicrosoft 365/Power Platformを契約している | 複数SaaSをまたぐ自動化を非エンジニアだけで完結させたい |

判断基準を整理すると次のようになる。

- **社内にJavaScript/簡易コードを書ける人がいるか** → いれば経路1が最も安く・速く・システムをまたがないので管理しやすい
- **すでにn8n/Make/Zapier/Difyなどのノーコードツールを契約しているか** → あれば経路3に相乗りするのが最短(新しい契約が不要)
- **Power Platform(Microsoft 365 Copilot等)を契約中か** → 経路2(Power Automateのプレミアムコネクタ前提)が組みやすい
- **リアルタイム性が必要か**(問い合わせ受信直後に即答する必要がある等) → 経路1(Webhookに直結)が有利。バッチ的な処理でよければ経路2・3でも十分
- **データ主権・セキュリティ要件が厳しいか** → 経由するシステムが増えるほど確認すべき経路が増える。経路1(業務システム→AI APIの直結)が最も経由が少なく、監査もしやすい

### 主要な業務システム別の標準的な連携先

| 業務システム | 標準の連携経路 | 補足 |
|---|---|---|
| kintone | JavaScriptカスタマイズ+`kintone.proxy()` | 既製プラグイン(例:「Smart at AI for kintone Powered by GPT」等)を使う選択肢もある |
| Slack | Incoming Webhook(投稿専用)/ Events API・Bot Token(双方向) | 双方向にはサーバーが必要。手軽さ重視なら投稿専用から始める |
| Microsoft Power Automate(Excel含む) | AI Builderのプロンプトビルダー、またはHTTPアクション | いずれもプレミアムライセンスが前提になることが多い |
| Salesforce | Agentforce(Agent Builder)、Einstein、Flow+外部サービス連携 | まず公式のAI機能で要件が満たせないか確認するのが基本 |

## 実務での使い方

### kintone: JavaScriptカスタマイズ+`kintone.proxy()`でAI APIを呼ぶ

kintoneのJavaScriptカスタマイズはブラウザ上で動くコードのため、そのまま`fetch()`でOpenAIやClaudeのAPIを呼ぼうとすると、ブラウザのCORS(Cross-Origin Resource Sharing、異なるドメイン間の通信を制限する仕組み)によってブロックされる。これを回避するために用意されているのが`kintone.proxy()`で、kintone側のプロキシサーバー(中継サーバー)を経由してリクエストを送ることで、CORSの制約を受けずに任意の外部APIを呼び出せる。

1. kintoneの対象アプリを開き、「アプリの設定」→「JavaScript / CSSでカスタマイズ」をクリックする
2. 「アップロードして追加」から、以下のようなカスタマイズファイルを登録する
3. 「保存」→「アプリを更新」で反映する

レコード保存時に問い合わせ内容をAIで分類し、結果を別フィールドに書き込む例(コピペ可、`(使用するモデル名)`は各社ドキュメントで最新のものに置き換える)。

```javascript
(function() {
  'use strict';

  kintone.events.on('app.record.detail.process.proceed', function(event) {
    const record = event.record;
    const inquiryText = record.問い合わせ内容.value;

    const url = 'https://api.anthropic.com/v1/messages';
    const headers = {
      'x-api-key': 'sk-ant-xxxxxxxx', // 本番運用ではプラグイン化して設定画面から保存する
      'anthropic-version': '2023-06-01',
      'Content-Type': 'application/json'
    };
    const body = {
      model: '(使用するモデル名)',
      max_tokens: 50,
      messages: [
        { role: 'user', content: '次の問い合わせ内容を「見積依頼」「クレーム」「その他」のいずれか1語で分類して:\n' + inquiryText }
      ]
    };

    return kintone.proxy(url, 'POST', headers, body).then(function(response) {
      const json = JSON.parse(response[0]);
      record.AI分類結果.value = json.content[0].text;
      return event;
    });
  });
})();
```

`kintone.proxy()`は「クロスドメイン制約を回避できる」だけで、APIキー自体の安全性を保証するものではない。この点は後述の注意点で扱う。

### Slack: Incoming WebhookとAI APIを組み合わせた最小実装例

SlackとAIの連携は「Slackへ投稿するだけ(一方向)」か「Slackでのやり取りに反応する(双方向)」かで難易度が大きく変わる。

- **Incoming Webhook(一方向・投稿専用)**: 事前に発行した1本のURLにJSONをPOSTするだけでSlackの指定チャンネルに投稿できる。サーバー不要で最も手軽
- **Events API + Bot Token(双方向)**: ユーザーの発言やメンションを検知して返信するには、Slackからのイベント通知を受け取る常時稼働のサーバー(またはSocket Mode)が必要になり、構築難易度が上がる

まずはIncoming Webhookで「AIが生成した内容をSlackに自動投稿する」構成から始めるのが実務的な第一歩になる。

**手順1: Incoming Webhook URLを発行する(画面の場所)**

1. api.slack.com/apps を開き、「Create New App」→「From scratch」でアプリを新規作成する
2. 左メニューの「Incoming Webhooks」を開き、右上のトグルをONにする
3. 画面下部の「Add New Webhook to Workspace」をクリックし、投稿先チャンネルを選んで「許可する」
4. 発行された`https://hooks.slack.com/services/...`のURLをコピーする(この文字列自体がパスワード同様の機密情報)

**手順2: AIの生成結果をSlackに投稿する(GAS例、コピペ可)**

AI API自体の呼び出し方法(APIキーの安全な保存や`UrlFetchApp`の使い方)は[GAS(Google Apps Script)からのAI API連携](gas-ai-api-integration.md)で解説した内容と共通のため、ここではSlackへの投稿部分に絞って示す。

```javascript
function notifySlackWithAiSummary(inquiryText) {
  // 1. AI APIで要約を生成(callClaude等の実装はGAS連携ページを参照)
  const summary = callClaude('次の問い合わせを1文で要約して:\n' + inquiryText);

  // 2. Slack Incoming Webhookへ投稿する
  const webhookUrl = PropertiesService.getScriptProperties().getProperty('SLACK_WEBHOOK_URL');
  const payload = {
    text: '*新規問い合わせの要約*\n' + summary
  };
  const options = {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify(payload),
    muteHttpExceptions: true
  };
  UrlFetchApp.fetch(webhookUrl, options);
}
```

`SLACK_WEBHOOK_URL`はAPIキーと同様、スクリプト プロパティに保存してコード中に直書きしない。ユーザーからの発言を受けて双方向にやり取りしたい場合は、常時稼働サーバーを自分で構築する代わりに、[n8nの基本](../part10-nocode-lowcode/n8n-basics.md)のSlackトリガーノードなど、ノーコード連携ツール側にサーバーの役割を任せる方法もある。

### Microsoft Power Automate(Excel含む): AI Builder/HTTPコネクタ経由の連携

Power Automateには、大きく2つのAI連携ルートがある。

- **AI Builderのプロンプトビルダー**: GUIでプロンプトを書くだけでAIの呼び出しを組み込める、最もローコードなルート。旧「テキストを生成」アクションは非推奨となり、現在は新しい「プロンプトビルダー」アクションへの移行が案内されている。課金はAI Builderクレジット(その後Copilot Studioクレジットの二段構え、いわゆる「デュアルモードライセンス」)で行われ、2026年11月1日にシードクレジットの利用期限が切れる予定のため、既存フローがある場合は移行の要否を確認する必要がある
- **HTTPアクション+任意のAI API**: OpenAI・Azure OpenAI・ClaudeなどのAPIエンドポイントを、HTTPアクションから直接POSTする方法。プロンプトの自由度が高く、モデルの選択肢も広い

いずれの方法も、HTTPアクションやAI Builder系アクションは「プレミアムコネクタ」に分類され、利用にはPower Automateのプレミアムライセンス(Per userまたはPer flowプラン)が別途必要になる点は共通の前提になる。

**HTTPアクションの設定例(コピペ可、値は自社のAPIキー・モデル名に置き換える)**

| 項目 | 設定値の例 |
|---|---|
| 方法 | POST |
| URI | `https://api.openai.com/v1/chat/completions` |
| ヘッダー | `Authorization: Bearer {APIキー}` / `Content-Type: application/json` |
| 本文(Body) | `{"model": "(使用するモデル名)", "messages": [{"role": "user", "content": "@{triggerBody()?['本文']}を要約して"}]}` |

HTTPアクションの直後に「JSONの解析(Parse JSON)」アクションを追加し、レスポンスのスキーマを取得しておくと、以降のアクションで「AIの回答」を動的な値として選べるようになる。Excelとの組み合わせでは、「Excel Online (Business)」コネクタの「表内に存在する行を一覧表示」で対象データを取得し、行ごとにHTTPアクションでAIを呼び、「行の更新」で結果を書き戻す、という「表を1行ずつAIで処理する」定期実行フローが典型的な構成になる。

### Salesforceなど主要CRM: 公式AI機能を優先する考え方

Salesforceは、Agentforce(自律的に判断して業務を遂行するAIエージェントを、ローコードの「Agent Builder」で作る仕組み)とEinstein(予測・分類・生成AIの基盤機能群)という2つのAI機能を統合している。独自にAPI連携を組む前に、まず次の公式ルートで要件が満たせないかを確認するのが基本的な考え方になる。

- **Agent Builder / Prompt Builder**: ローコードでAIエージェントやプロンプトを組み立てる公式機能
- **Flow + 外部サービス連携(Named Credentials)/ Apexコールアウト**: Salesforce標準の自動化機能から外部のAI APIを呼び出す、業務システム側にコードを書く経路(本ページの経路1に相当)
- **MuleSoft連携**: 複数システムを横断する複雑な連携が必要な場合の統合基盤

他の主要CRM・SaaSでも考え方は同様で、「まずベンダー公式のAI機能で足りるかを確認し、足りない部分だけを経路1〜3で補う」という優先順位が実務上の目安になる。公式機能はアクセス権限・監査ログ・データガバナンスが製品に統合されているため、自前でAPI連携を組むより運用上の安全性が高いことが多い。

## 注意点・よくある誤解

- **ブラウザ側のカスタマイズコードにAPIキーを直書きしない**: kintoneの`kintone.proxy()`はCORSを回避する仕組みであり、APIキー自体を隠す仕組みではない。リクエスト内容はブラウザ上のJavaScriptが組み立てるため、ブラウザの開発者ツールで通信内容を確認できる人にはキーが見える。本番運用では、プラグイン化して設定情報を保存する仕組みを使うか、自社サーバー(簡易なプロキシ)を経由させ、APIキーをブラウザ側に一切渡さない構成にする
- **Slack Incoming Webhookは投稿専用の一方通行**: ユーザーの発言に反応してAIが返信するような双方向のやり取りには、Events API・Bot Tokenと常時稼働のサーバー(またはSocket Mode)が必要で、構築難易度が一段上がる。まず投稿専用の一方向連携から試し、双方向が必要になった段階でノーコード連携ツールや専用のBot構築サービスを検討する
- **Power Automateのプレミアムコネクタには別ライセンスが必要**: HTTPアクションやAI Builder系アクションは「プレミアムコネクタ」扱いのため、Microsoft 365に付属する範囲のPower Automateだけでは動かず、Premium(Per userまたはPer flow)ライセンスの追加購入が前提になることが多い。導入前にライセンス費用を確認する
- **AI Builderの旧アクションと課金体系は移行期にある**: 旧「テキストを生成」アクションは非推奨で、新しい「プロンプトビルダー」アクションへの移行が案内されている。AI Builderクレジットのシード分は2026年11月1日で利用期限を迎える予定のため、既存フローがある場合は早めに移行計画を確認する
- **CRM等の大規模SaaSでは自前連携より公式AI機能を先に検討する**: Salesforceに限らず、業務システムベンダーが提供する公式のAIエージェント機能・生成AI機能は権限管理や監査ログが統合されており、独自にAPI連携を組むより運用上の安全性が高い場合が多い。要件が公式機能で満たせるかを先に確認してから、足りない部分だけ経路1〜3で補う
- **機密データの外部送信リスク**: 業務システムに保存された顧客情報・人事情報などをAI APIに渡す前に、社内の情報取り扱いルールやAI事業者のデータ保持ポリシーを確認する。特に経路3(ノーコード連携ツール中継)は、データが業務システム→中継ツール→AI APIという複数の第三者サービスを経由するため、経由先すべてを把握しておく

## 最初の一歩

自社で使っている業務システムを1つ選び、最小のテストを試す。kintoneなら検証用アプリで`kintone.proxy()`から1件のレコードをAIに分類させてみる、SlackならIncoming Webhook URLを1本発行してAIが生成した要約を投稿してみる、Power AutomateならHTTPアクション1つだけの単発フローを組んでAI APIのレスポンスを確認してみる、のいずれかで十分。

## 関連トピック

- [GAS(Google Apps Script)からのAI API連携](gas-ai-api-integration.md)
- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [n8nの基本](../part10-nocode-lowcode/n8n-basics.md)
- [Makeの基本](../part10-nocode-lowcode/make-basics.md)
- [Zapierの基本](../part10-nocode-lowcode/zapier-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: 業務システム・SaaSからAI APIへ連携する3つの経路(業務システム標準機能+簡易コード/自動化ツール内蔵AIコネクタ/ノーコード連携ツール中継)の整理と使い分け基準、kintoneの`kintone.proxy()`によるJavaScriptカスタマイズ実装例、SlackのIncoming Webhook(投稿専用)とEvents API(双方向)の違いおよびGASを使った最小実装例、Power AutomateのHTTPアクション設定例とAI Builderのプロンプトビルダーへの移行動向、Salesforce(Agentforce/Einstein)における公式AI機能優先の考え方、APIキー管理やライセンス面の注意点を整理
- **出典**: [cybozu developer network: 外部のAPIを実行する(kintone.proxy)](https://cybozu.dev/ja/kintone/docs/js-api/proxy/kintone-proxy/)、[cybozu developer network: kintoneとChatGPTを使ってAIチャットボット型FAQを構築しよう](https://cybozu.dev/ja/kintone/tips/development/3rd-party-services/generative-ai/create-faq-chatbot-using-kintone-chatgpt/)、[株式会社メディアフュージョン: カスタマイズ kintone 初心者向け CORSの仕組みとkintone proxy](https://www.mediafusion.co.jp/dx-blog/tt20250204/)、[コムデックAIラボ: kintoneとOpenAIのChatGPTを連携できるプラグイン・サービス5選](https://www.comdec.jp/comdeclab/kintone-ai-10/)、[Slack Help Center: Incoming webhooks for Slack](https://slack.com/help/articles/115005265063-Incoming-webhooks-for-Slack)、[Slack Developer Docs: The Events API](https://docs.slack.dev/apis/events-api/)、[Microsoft Learn: Power Automateでテキスト生成モデルを使用する(非推奨)](https://learn.microsoft.com/ja-jp/ai-builder/azure-openai-model-pauto)、[Microsoft Learn: AI Builderクレジットの期間終了](https://learn.microsoft.com/ja-jp/ai-builder/endofaibcredits)、[Microsoft Learn: Copilotクレジット制ライセンス(デュアルモード)](https://learn.microsoft.com/ja-jp/ai-builder/dual-mode-licensing)、[Qiita: すぐに始めるChatGPT API まずはPower Automateで呼び出してみる](https://qiita.com/Satoshi_Yoshino/items/b4fc4a74265069fdf109)、[Salesforce Developers: Agentforce and Generative AI](https://developer.salesforce.com/docs/einstein/genai/overview)、[Salesforce: Agentforce - The AI Agent Platform](https://www.salesforce.com/agentforce/)
- **注記**: kintoneプラグイン名・Power AutomateのAI Builderライセンス移行スケジュール(2026年11月1日)は本文執筆時点の情報。掲載・記事化前に各公式サイト(cybozu.dev、learn.microsoft.com、salesforce.com)で最終確認を推奨
