---
title: OpenAI APIの基本
part: 8
chapter: 第1章 OpenAI API基礎
tags: [OpenAI API, 従量課金, APIキー, トークン]
created: 2026-07-04
updated: 2026-07-04
---

# OpenAI APIの基本

## これは何か

ChatGPT Plusに課金していれば、DifyやGASなど他のツールからもOpenAIのAIモデルを自由に呼び出せる、と誤解している人は多い。実際にはChatGPT(サブスク)とOpenAI API(従量課金)は完全に別の契約であり、社内システムやノーコードツールにAIを組み込みたい場合はAPIを別途契約する必要がある。

## 仕組み・背景

- **ChatGPT**: chat.openai.com上でチャット形式でAIと対話する、エンドユーザー向けの製品。Free/Go/Plus/Proなどの月額サブスクリプションで提供される。
- **OpenAI API**: 開発者向けのインターフェースで、自社の業務システム・チャットボット・要約や分類のバッチ処理など、AIを自社サービスに組み込むための仕組み。ChatGPTのサブスク契約とは別会計で、ChatGPT Plusに入っていてもAPI利用料は1円も割引されない。逆にChatGPTを契約していなくても、OpenAIアカウントと支払い方法さえあればAPIのみ契約できる。

APIの料金は「トークン(文章を分割した単位)」ごとの従量課金で、入力(プロンプト)側と出力(生成結果)側で単価が異なり、通常は出力トークンの方が3〜6倍程度高く設定されている。モデルのグレードによっても単価は大きく変わり、高性能なモデルほど高額になる。

## 使いどころ・使い分け

| やりたいこと | 向いている契約 |
|---|---||
| 自分でチャット画面から質問・相談したい | ChatGPT(Free/Plus/Pro等) |
| 社内システムやスプレッドシートにAI機能を組み込みたい | OpenAI API |
| Difyやn8nなどノーコードツールでAIアプリを作りたい | OpenAI API(ノーコードツール側にAPIキーを設定) |
| 大量のデータを一括で要約・分類したい(即時応答不要) | OpenAI APIのBatch API(通常の半額程度で処理できる) |

## 実務での使い方

### APIキーの取得手順

1. platform.openai.com にログイン(ChatGPTと同じOpenAIアカウントでよい)
2. 左サイドバーの「API keys」、または直接 platform.openai.com/api-keys にアクセス
3. 「Create new secret key」をクリックし、名前・権限・紐づけるプロジェクトを設定
4. 生成されたキーはその場でしか全文表示されないため、必ずコピーして安全な場所に保管する(紛失した場合は再表示できず、新規発行が必要)
5. あわせて支払い方法の登録と、想定外の高額請求を防ぐための利用上限(Usage limits)の設定をしておく

### 料金体系のイメージ(2026年7月時点、モデル名・価格は変更が頻繁なため必ず公式ページ platform.openai.com/docs/pricing で最終確認すること)

- 軽量・高速なモデルほど安価(1トークンあたり1円未満のオーダー)、最上位の高性能モデルは入力・出力ともに桁が上がる
- キャッシュされた入力(直前と同じ内容の再利用)は通常の入力より大幅に割引される
- Batch API(24時間以内の非同期処理)は同期呼び出しに比べて約50%安い

### ノーコードツール・業務システムとの連携例

- **Dify**: モデルプロバイダーの設定画面にOpenAIのAPIキーを入力するだけで、Dify上に作ったチャットボットやワークフローからOpenAIのモデルを呼び出せる
- **GAS(Google Apps Script)**: `UrlFetchApp`でAPIにHTTPリクエストを送り、スプレッドシートの内容を要約・分類するといった社内自動化によく使われる
- **Zapier / Make / n8n**: 他システムとの連携・自動実行のトリガーとして、AIアプリと組み合わせて使われる

### 代表的な機能(名前と一言メモ)

- **Batch API**: 大量のリクエストをまとめて非同期送信し、通常より安く処理する仕組み
- **Function Calling(ツール呼び出し)**: モデルに外部の関数・API・DBクエリを呼び出させる仕組み。モデルが「この関数をこの引数で呼びたい」という指示を返し、開発者側で実行結果をモデルに戻す
- **Structured Outputs**: 開発者が指定したJSON Schemaに厳密に一致する形式で出力させる機能

## 注意点・よくある誤解

- **ChatGPT課金とAPI課金は別会計**: ChatGPT Plusの月額料金はAPI利用料の割引にはならない。混同して「なぜ別料金が発生するのか」と驚かないよう、契約前に整理しておく。
- **料金・モデル名は非常に頻繁に更新される**: 2026年に入ってからも短期間でモデルの世代・価格が複数回改定されている。記事や社内資料に価格を書く場合は、必ず公式サイトの最新情報を都度確認する。
- **利用上限を設定せずに使うと高額請求のリスクがある**: 想定外の大量呼び出し(バグによる無限ループ等)に備えて、必ずUsage limitsを設定しておく。

## 最初の一歩

自社でDifyやGASなどのノーコード連携を検討しているなら、まずplatform.openai.comでAPIキーを1つ発行し、利用上限を低めに設定した状態でテスト的に呼び出してみる。

## 関連トピック

- [Function Calling(Tool Use)の基本](function-calling-basics.md)

## 更新履歴

### 2026-07-04: 初版執筆
- **内容**: ChatGPTとOpenAI APIの違い、料金体系の基本、APIキー取得手順、ノーコードツールとの連携例、Batch API/Function Calling/Structured Outputsの概要を整理
- **出典**: [OpenAI Developer Community](https://community.openai.com/t/openai-pay-as-you-go-vs-chatgpt-subscription/160812)、[OpenAI Developer Community: APIキー発行手順](https://community.openai.com/t/how-to-generate-openai-api-key/401363)、[SIOS Tech Lab](https://tech-lab.sios.jp/archives/46026)
- **注記**: モデル別の具体的な料金は変更が頻繁なため本文では意図的に固定額を明記していない。最新の単価は必ず [OpenAI公式Pricingページ](https://openai.com/api/pricing/) で確認すること
