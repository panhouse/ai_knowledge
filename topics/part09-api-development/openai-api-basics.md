---
title: OpenAI APIの基本
part: 9
chapter: 第1章 LLM APIの基礎
tags: [OpenAI API, 従量課金, APIキー, トークン, GPT-5.6, Responses API]
created: 2026-07-04
updated: 2026-07-19
---

# OpenAI APIの基本

## これは何か

ChatGPT Plusに課金していれば、DifyやGASなど他のツールからもOpenAIのAIモデルを自由に呼び出せる、と誤解している人は多い。実際にはChatGPT(サブスク)とOpenAI API(従量課金)は完全に別の契約であり、社内システムやノーコードツールにAIを組み込みたい場合はAPIを別途契約する必要がある。

## 仕組み・背景

- **ChatGPT**: chat.openai.com上でチャット形式でAIと対話する、エンドユーザー向けの製品。Free/Go/Plus/Proなどの月額サブスクリプションで提供される。
- **OpenAI API**: 開発者向けのインターフェースで、自社の業務システム・チャットボット・要約や分類のバッチ処理など、AIを自社サービスに組み込むための仕組み。ChatGPTのサブスク契約とは別会計で、ChatGPT Plusに入っていてもAPI利用料は1円も割引されない。逆にChatGPTを契約していなくても、OpenAIアカウントと支払い方法さえあればAPIのみ契約できる。

APIの料金は「トークン(文章を分割した単位)」ごとの従量課金で、入力(プロンプト)側と出力(生成結果)側で単価が異なり、通常は出力トークンの方が3〜6倍程度高く設定されている。モデルのグレードによっても単価は大きく変わり、高性能なモデルほど高額になる。

### モデルラインナップの現在地(2026年7月時点)

OpenAIのモデル体系は数ヶ月おきに更新されており、2026年7月9日に最新世代「**GPT-5.6**」が広く利用可能になった。従来の「無印/mini/nano」というサイズ表記に代わり、今回から**Sol・Terra・Luna**という3つの「能力ティア」の名前が使われている点が大きな変化。

| ティア名 | 位置づけ | 目安の用途 |
|---|---|---|
| **Sol** | 最上位・最高性能 | 複雑な推論、高度なコーディング、精度最優先の業務 |
| **Terra** | バランス型 | 日常的な業務利用の主力(コストと性能のバランス) |
| **Luna** | 高速・低コスト | 大量処理、リアルタイム応答、コスト最優先の用途 |

また、これまで「推論モデル」として別系統だったo1・o3・o4-miniなどのo-series(考えてから答えるモデル)は、GPT-5世代への統合が進んでおり、GPT-5.6では「reasoning effort(推論の強さ)」を`none`〜`max`の段階で指定することで、1つのモデル(例: Terra)を軽い応答から深い推論まで使い分けられるようになっている。旧o-seriesのモデルIDは順次非推奨・廃止(o4-miniは2026年10月23日、o3はChatGPT上で2026年8月26日に廃止予定など)となっているため、新規開発では`gpt-5.6-*`系のモデル名を使うのが安全。

## 使いどころ・使い分け

| やりたいこと | 向いている契約・モデル |
|---|---|
| 自分でチャット画面から質問・相談したい | ChatGPT(Free/Plus/Pro等) |
| 社内システムやスプレッドシートにAI機能を組み込みたい | OpenAI API |
| Difyやn8nなどノーコードツールでAIアプリを作りたい | OpenAI API(ノーコードツール側にAPIキーを設定) |
| 大量のデータを一括で要約・分類したい(即時応答不要) | OpenAI APIのBatch API(通常の半額で処理できる) |
| 契約書レビューや複雑な分析など、精度を最優先したい | GPT-5.6 Sol(最上位ティア) |
| 社内チャットボットなど日常業務全般 | GPT-5.6 Terra(バランス型) |
| FAQ自動応答・大量メール分類など高頻度・低コスト処理 | GPT-5.6 Luna(高速・低コスト) |

## 実務での使い方

### APIキーの取得手順

1. platform.openai.com にログイン(ChatGPTと同じOpenAIアカウントでよい)
2. 左サイドバーの「API keys」、または直接 platform.openai.com/api-keys にアクセス
3. 「Create new secret key」をクリックし、名前・権限・紐づけるプロジェクトを設定
4. 生成されたキーはその場でしか全文表示されないため、必ずコピーして安全な場所に保管する(紛失した場合は再表示できず、新規発行が必要)
5. あわせて支払い方法の登録と、想定外の高額請求を防ぐための利用上限(Usage limits)の設定をしておく

### 料金体系のイメージ(2026年7月時点、モデル名・価格は変更が頻繁なため必ず公式ページ platform.openai.com/docs/pricing で最終確認すること)

最新世代GPT-5.6のティア別価格(1Mトークンあたり、目安):

| モデル | 入力 | 出力 |
|---|---|---|
| GPT-5.6 Sol(最上位) | $5.00 | $30.00 |
| GPT-5.6 Terra(バランス) | $2.50 | $15.00 |
| GPT-5.6 Luna(高速・低コスト) | $1.00 | $6.00 |

- 軽量・高速なモデルほど安価、最上位の高性能モデルは入力・出力ともに桁が上がる、という基本構造は変わらない
- **キャッシュされた入力**(直前と同じ内容の再利用)は通常の入力より大幅に割引される(目安として90%引き程度)。一方でキャッシュの「書き込み」自体には通常入力の1.25倍程度の料金がかかる設計になっている点に注意
- **Batch API**(24時間以内の非同期処理)は同期呼び出しに比べて一律約50%安い。キャッシュ割引とBatch割引は併用可能で、条件が揃えば通常価格から大幅に圧縮できる

### ノーコードツール・業務システムとの連携例

- **Dify**: モデルプロバイダーの設定画面にOpenAIのAPIキーを入力するだけで、Dify上に作ったチャットボットやワークフローからOpenAIのモデルを呼び出せる
- **GAS(Google Apps Script)**: `UrlFetchApp`でAPIにHTTPリクエストを送り、スプレッドシートの内容を要約・分類するといった社内自動化によく使われる
- **Zapier / Make / n8n**: 他システムとの連携・自動実行のトリガーとして、AIアプリと組み合わせて使われる

### 代表的な機能(名前と一言メモ)

- **Responses API**: 会話の状態管理やツール呼び出しをまとめて扱える、現在OpenAIが新規開発に推奨しているAPIの窓口。旧来の「Chat Completions API」も引き続きサポートされているため、既存システムをすぐに移行する必要はない
- **Batch API**: 大量のリクエストをまとめて非同期送信し、通常より安く処理する仕組み
- **Function Calling(ツール呼び出し)**: モデルに外部の関数・API・DBクエリを呼び出させる仕組み。モデルが「この関数をこの引数で呼びたい」という指示を返し、開発者側で実行結果をモデルに戻す。GPT-5.6では「Programmatic Tool Calling」として、モデルがツール呼び出しをコードのように連鎖・制御できる拡張版が追加されている
- **Structured Outputs**: 開発者が指定したJSON Schemaに厳密に一致する形式で出力させる機能

## 注意点・よくある誤解

- **ChatGPT課金とAPI課金は別会計**: ChatGPT Plusの月額料金はAPI利用料の割引にはならない。混同して「なぜ別料金が発生するのか」と驚かないよう、契約前に整理しておく。
- **料金・モデル名は非常に頻繁に更新される**: 2025年後半から2026年前半にかけてだけでもGPT-5→5.1→5.2→5.4→5.5→5.6と短期間でモデル世代が何度も切り替わっており、2026年7月にはモデルの命名方式自体(サイズ表記→Sol/Terra/Lunaのティア名)が変わった。記事や社内資料に価格・モデル名を書く場合は、必ず公式サイトの最新情報を都度確認する。
- **古いモデルIDは順次廃止される**: o1・o3・o4-miniなどのo-seriesや、Assistants API(2026年8月26日に廃止予定)を前提に組んだ社内システムは、放置すると突然使えなくなるリスクがある。新規開発では現行のGPT-5系モデル名・Responses APIを使い、既存システムは廃止スケジュールを定期的に確認する。
- **利用上限を設定せずに使うと高額請求のリスクがある**: 想定外の大量呼び出し(バグによる無限ループ等)に備えて、必ずUsage limitsを設定しておく。

## 最初の一歩

自社でDifyやGASなどのノーコード連携を検討しているなら、まずplatform.openai.comでAPIキーを1つ発行し、利用上限を低めに設定した状態でテスト的に呼び出してみる。

## 関連トピック

- [Function Calling(Tool Use)の基本](function-calling-basics.md)

## 更新履歴

### 2026-07-19: モデルラインナップと料金体系を最新化
- **内容**: 2026年7月9日に広く提供開始されたGPT-5.6(Sol/Terra/Luna)への刷新を反映し、モデル体系・料金表・o-series統合の動向、Responses API/Chat Completions API/Assistants API廃止スケジュール、Batch API・キャッシュ割引の最新値を追記
- **出典**: [OpenAI: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)、[OpenAI Developer Community: Introducing GPT-5.6 series](https://community.openai.com/t/introducing-gpt-5-6-series-sol-terra-and-luna-coming-july-9-10am-pt/1384931)、[OpenAI Help Center: A preview of GPT-5.6 Sol, Terra and Luna](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna)、[MarkTechPost: OpenAI Releases GPT-5.6](https://www.marktechpost.com/2026/07/09/openai-releases-gpt-5-6-a-three-tier-model-family-with-programmatic-tool-calling/)、[VentureBeat: OpenAI unveils GPT-5.6](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)、[TheRouter.ai: OpenAI legacy model deprecation wave](https://therouter.ai/news/openai-legacy-model-deprecation-wave-july-october-2026/)

### 2026-07-04: 初版執筆
- **内容**: ChatGPTとOpenAI APIの違い、料金体系の基本、APIキー取得手順、ノーコードツールとの連携例、Batch API/Function Calling/Structured Outputsの概要を整理
- **出典**: [OpenAI Developer Community](https://community.openai.com/t/openai-pay-as-you-go-vs-chatgpt-subscription/160812)、[OpenAI Developer Community: APIキー発行手順](https://community.openai.com/t/how-to-generate-openai-api-key/401363)、[SIOS Tech Lab](https://tech-lab.sios.jp/archives/46026)
- **注記**: モデル別の具体的な料金は変更が頻繁なため本文では意図的に固定額を明記していない。最新の単価は必ず [OpenAI公式Pricingページ](https://openai.com/api/pricing/) で確認すること
