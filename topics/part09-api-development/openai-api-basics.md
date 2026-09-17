---
title: OpenAI APIの基本
part: 9
chapter: 第1章 LLM APIの基礎
tags: [OpenAI API, 従量課金, APIキー, トークン, GPT-6 Astra, GPT-5.6, Responses API]
created: 2026-07-04
updated: 2026-09-17
---

# OpenAI APIの基本

## これは何か

ChatGPT Plusに課金していれば、DifyやGASなど他のツールからもOpenAIのAIモデルを自由に呼び出せる、と誤解している人は多い。実際にはChatGPT(サブスク)とOpenAI API(従量課金)は完全に別の契約であり、社内システムやノーコードツールにAIを組み込みたい場合はAPIを別途契約する必要がある。

## 仕組み・背景

- **ChatGPT**: chat.openai.com上でチャット形式でAIと対話する、エンドユーザー向けの製品。Free/Go/Plus/Proなどの月額サブスクリプションで提供される。
- **OpenAI API**: 開発者向けのインターフェースで、自社の業務システム・チャットボット・要約や分類のバッチ処理など、AIを自社サービスに組み込むための仕組み。ChatGPTのサブスク契約とは別会計で、ChatGPT Plusに入っていてもAPI利用料は1円も割引されない。逆にChatGPTを契約していなくても、OpenAIアカウントと支払い方法さえあればAPIのみ契約できる。

APIの料金は「トークン(文章を分割した単位)」ごとの従量課金で、入力(プロンプト)側と出力(生成結果)側で単価が異なり、通常は出力トークンの方が3〜6倍程度高く設定されている。モデルのグレードによっても単価は大きく変わり、高性能なモデルほど高額になる。

### モデルラインナップの現在地(2026年9月時点)

OpenAIのモデル体系は数ヶ月おきに更新されており、2026年7月9日に「**GPT-5.6**」(Sol・Terra・Lunaの3ティア)が広く利用可能になった直後の2026年9月3日には、次世代フラッグシップ「**GPT-6 Astra**」がAPI・ChatGPT・Azure OpenAI Service・AWS Bedrockに同時展開された。API上のモデルIDは`gpt-6-astra`で、コンテキストウィンドウは100万トークン。OpenAIが自社の安全基準(Preparedness Framework)で「Critical」レベルのサイバーセキュリティ能力に達したと初めて位置づけたモデルでもあり、コンピュータ操作・ブラウジング・ソフトウェア開発などで最上位の性能を謳う。GPT-5.6系(Sol/Terra/Luna)はAstra登場後も引き続き提供されており、コストや用途に応じてAstraと使い分ける形になっている。

| モデル/ティア名 | 位置づけ | 目安の用途 |
|---|---|---|
| **GPT-6 Astra** | 最新・最上位フラッグシップ | コンピュータ操作、高度なソフトウェア開発、複雑なエージェントタスク |
| **Sol** | GPT-5.6の最上位ティア | 複雑な推論、高度なコーディング、精度最優先の業務 |
| **Terra** | バランス型 | 日常的な業務利用の主力(コストと性能のバランス) |
| **Luna** | 高速・低コスト | 大量処理、リアルタイム応答、コスト最優先の用途 |

Solには通常モードに加えて、料金2倍・応答速度が最大2.5倍になる「**Sol Fast**」モードがあり、Astraにも同様に料金2倍で高速化する「Fast」モードが用意されている。リアルタイム性が必要かつ精度も譲れない用途(有人対応の補助など)で選択肢になる。

また、これまで「推論モデル」として別系統だったo1・o3・o4-miniなどのo-series(考えてから答えるモデル)は、GPT-5世代への統合が進んでおり、GPT-5.6では「reasoning effort(推論の強さ)」を`none`・`low`・`medium`・`high`・`xhigh`・`max`の6段階で指定することで、1つのモデル(例: Terra)を軽い応答から深い推論まで使い分けられるようになっている。この設定は品質だけでなくコストのダイヤルでもあり、段階を上げるほど出力トークン(単価が最も高い部分)が増えて課金額も膨らむ点に注意する。

旧o-seriesや旧世代モデルのIDは順次非推奨・廃止が進んでおり、**ChatGPT上の提供終了**と**APIでの提供終了**で時期が異なる点を混同しないこと。o4-miniはChatGPT上では2026年2月13日に終了済みだが、API経由では2026年10月23日まで利用可能(移行先は`gpt-5.4-mini`系が案内されている)。o3はChatGPT上で2026年8月26日に終了予定(API側の古いスナップショットは2026年12月11日に廃止予定)。セキュリティ特化版の`gpt-5.4-cyber`も2026年10月1日までに`gpt-5.6-cyber`への移行が求められている。新規開発では現行の`gpt-6-astra`または`gpt-5.6-*`系のモデル名を使うのが安全。

## 使いどころ・使い分け

| やりたいこと | 向いている契約・モデル |
|---|---|
| 自分でチャット画面から質問・相談したい | ChatGPT(Free/Plus/Pro等) |
| 社内システムやスプレッドシートにAI機能を組み込みたい | OpenAI API |
| Difyやn8nなどノーコードツールでAIアプリを作りたい | OpenAI API(ノーコードツール側にAPIキーを設定) |
| 大量のデータを一括で要約・分類したい(即時応答不要) | OpenAI APIのBatch API(通常の半額で処理できる) |
| コンピュータ操作・複雑なエージェントタスクなど最上位の性能が必要 | GPT-6 Astra |
| 契約書レビューや複雑な分析など、精度を最優先したい(コストはAstraより抑えたい) | GPT-5.6 Sol |
| 社内チャットボットなど日常業務全般 | GPT-5.6 Terra(バランス型) |
| FAQ自動応答・大量メール分類など高頻度・低コスト処理 | GPT-5.6 Luna(高速・低コスト、2026年7月末の値下げで最安クラスに) |
| リアルタイム音声対応など、速度と精度の両方が必要 | GPT-6 Astra FastまたはGPT-5.6 Sol Fast(いずれも料金2倍で高速化) |

## 実務での使い方

### APIキーの取得手順

1. platform.openai.com にログイン(ChatGPTと同じOpenAIアカウントでよい)
2. 左サイドバーの「API keys」、または直接 platform.openai.com/api-keys にアクセス
3. 「Create new secret key」をクリックし、名前・権限・紐づけるプロジェクトを設定
4. 生成されたキーはその場でしか全文表示されないため、必ずコピーして安全な場所に保管する(紛失した場合は再表示できず、新規発行が必要)
5. あわせて支払い方法の登録と、想定外の高額請求を防ぐための利用上限(Usage limits)の設定をしておく

### 料金体系のイメージ(2026年9月時点、モデル名・価格は変更が頻繁なため必ず公式ページ platform.openai.com/docs/pricing で最終確認すること)

主要モデルの1Mトークンあたり価格(標準・キャッシュ入力込み):

| モデル | 入力 | キャッシュ入力 | 出力 |
|---|---|---|---|
| GPT-6 Astra(最新・最上位) | $10.00 | $1.00 | $50.00 |
| GPT-5.6 Sol(最上位ティア) | $4.00(プロモ価格、旧$5.00) | $0.40 | $20.00(プロモ価格、旧$30.00) |
| GPT-5.6 Terra(バランス) | $2.00 | $0.20 | $12.00 |
| GPT-5.6 Luna(高速・低コスト) | $0.20 | $0.02 | $1.20 |

- GPT-5.6 Solの上記価格は**2026年11月21日まで**のプロモーション価格で、それ以降は通常価格に戻る可能性がある(要・公式ページ確認)
- Astraは新モデルのため現時点では最上位の価格帯だが、長文コンテキスト利用時はさらに単価が上がる長文コンテキスト料金体系が別途設定されている
- 軽量・高速なモデルほど安価、最上位の高性能モデルは入力・出力ともに桁が上がる、という基本構造は変わらない
- **キャッシュされた入力**(直前と同じ内容の再利用)は通常の入力より大幅に割引される(目安として90%引き)。一方でキャッシュの「書き込み」自体には通常入力の1.25倍程度の料金がかかる設計になっている点に注意
- **Batch API**(24時間以内の非同期処理)は同期呼び出しに比べて一律約50%安い。キャッシュ割引とBatch割引は併用可能で、条件が揃えば通常価格から大幅に圧縮できる
- **利用量に応じたレート制限(Usage tier)**: 支払い実績の累計額に応じてTier 1〜5の区分があり、Tierが上がるほど1分あたりのリクエスト数(RPM)・トークン数(TPM)の上限が緩和される。急にトラフィックが増える見込みがある場合は、事前に課金実績を積んでTierを上げておくか、上限緩和の申請をしておく

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
- **料金・モデル名は非常に頻繁に更新される**: 2025年後半から2026年前半にかけてだけでもGPT-5→5.1→5.2→5.4→5.5→5.6と短期間でモデル世代が何度も切り替わっており、2026年7月にはモデルの命名方式自体(サイズ表記→Sol/Terra/Lunaのティア名)が変わり、さらに2026年9月3日には次世代フラッグシップGPT-6 Astraが登場した。価格競争が激しく、プロモーション価格(Sol)のように期限付きの値下げもあるため、記事や社内資料に価格・モデル名を書く場合は、必ず公式サイトの最新情報を都度確認する。
- **「ChatGPT上での廃止」と「APIでの廃止」は別スケジュール**: 同じモデルでも、ChatGPT向けの提供終了とAPI向けの提供終了で時期がずれることが多い(例: o4-miniはChatGPT上では2026年2月に終了済みだが、APIでは2026年10月23日まで有効)。Assistants API(2026年8月26日にAPIから完全に削除予定、以後は`/v1/assistants`等へのアクセスがすべてエラーになる)を前提に組んだ社内システムは、放置すると突然使えなくなるリスクがある。新規開発では現行のGPT-5.6系モデル名・Responses APIを使い、既存システムは廃止スケジュールを定期的に確認する。
- **利用上限を設定せずに使うと高額請求のリスクがある**: 想定外の大量呼び出し(バグによる無限ループ等)に備えて、必ずUsage limitsを設定しておく。

## 最初の一歩

自社でDifyやGASなどのノーコード連携を検討しているなら、まずplatform.openai.comでAPIキーを1つ発行し、利用上限を低めに設定した状態でテスト的に呼び出してみる。

## 関連トピック

- [Function Calling(Tool Use)の基本](function-calling-basics.md)

## 更新履歴

### 2026-09-17: GPT-6 Astraの登場を反映して最新化
- **内容**: 2026年9月3日にAPI・ChatGPT・Azure OpenAI Service・AWS Bedrockへ同時展開された次世代フラッグシップ「GPT-6 Astra」(モデルID`gpt-6-astra`、コンテキスト100万トークン、Preparedness FrameworkでCriticalレベルのサイバーセキュリティ能力と初めて位置づけられたモデル)を追記。料金表にAstra($10/$1キャッシュ/$50)を追加し、GPT-5.6 Solが2026年11月21日まで適用のプロモーション価格($4/$0.40/$20、旧$5/$30)に切り替わっている点を反映。`gpt-5.4-cyber`が2026年10月1日までに`gpt-5.6-cyber`へ移行期限を迎える点も追記
- **出典**: [OpenAI: GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/)、[OpenAI Deployment Safety Hub: GPT-6 Astra System Card](https://deploymentsafety.openai.com/gpt-6-astra)、[CNBC: OpenAI announces rollout of GPT-6 Astra model](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)、[9to5Mac: OpenAI releasing major upgrade to ChatGPT and Codex with GPT-6 Astra](https://9to5mac.com/2026/09/04/openai-releasing-major-upgrade-to-chatgpt-and-codex-with-gpt-6-astra-details-here/)、[OpenAI API Pricing (公式): developers.openai.com/api/docs/pricing](https://developers.openai.com/api/docs/pricing)

### 2026-08-03: 料金体系とモデル廃止スケジュールを最新化
- **内容**: 2026年7月30日のGPT-5.6 Terra・Luna大幅値下げ(Lunaは約80%安、Terraは約20%安、Solは据え置き)を反映して料金表を更新。reasoning effortの段階を`none`〜`max`の6段階に具体化し、Sol Fastモード(2倍料金・最大2.5倍速)を追記。o4-mini・Assistants APIの廃止時期を「ChatGPT向け」と「API向け」で明確に区別して整理し、利用量に応じたレート制限(Usage tier)の存在を追記。次世代モデル(コード名Astra)の動向にも軽く言及
- **出典**: [Yahoo Finance: OpenAI cuts GPT-5.6 Luna and Terra prices by up to 80%](https://finance.yahoo.com/technology/ai/articles/openai-cuts-gpt-5-6-173045044.html)、[VentureBeat: AI price wars, OpenAI cuts GPT-5.6 Luna prices by 80%](https://venturebeat.com/technology/ai-price-wars-openai-cuts-gpt-5-6-luna-prices-by-80-as-model-competition-shifts-toward-cost)、[CNBC: OpenAI cuts prices for two of its GPT-5.6 AI models](https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html)、[Axios: OpenAI discounts GPT-5.6 Luna and Terra](https://www.axios.com/2026/07/30/openai-cuts-prices-gpt-terra-luna5)、[TheRouter.ai: OpenAI's biggest deprecation wave yet](https://therouter.ai/news/openai-legacy-model-deprecation-wave-july-october-2026/)、[OpenAI Developer Community: Assistants API beta deprecation, August 26, 2026 sunset](https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666)、[OpenAI: Retiring GPT-4o, GPT-4.1, GPT-4.1 mini, and OpenAI o4-mini in ChatGPT](https://openai.com/index/retiring-gpt-4o-and-older-models/)、[The News: OpenAI is preparing to launch a new Astra model series](https://www.thenews.com.pk/latest/1410885-openai-is-preparing-to-launch-a-new-astra-model-series-what-to-know)

### 2026-07-19: モデルラインナップと料金体系を最新化
- **内容**: 2026年7月9日に広く提供開始されたGPT-5.6(Sol/Terra/Luna)への刷新を反映し、モデル体系・料金表・o-series統合の動向、Responses API/Chat Completions API/Assistants API廃止スケジュール、Batch API・キャッシュ割引の最新値を追記
- **出典**: [OpenAI: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)、[OpenAI Developer Community: Introducing GPT-5.6 series](https://community.openai.com/t/introducing-gpt-5-6-series-sol-terra-and-luna-coming-july-9-10am-pt/1384931)、[OpenAI Help Center: A preview of GPT-5.6 Sol, Terra and Luna](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna)、[MarkTechPost: OpenAI Releases GPT-5.6](https://www.marktechpost.com/2026/07/09/openai-releases-gpt-5-6-a-three-tier-model-family-with-programmatic-tool-calling/)、[VentureBeat: OpenAI unveils GPT-5.6](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)、[TheRouter.ai: OpenAI legacy model deprecation wave](https://therouter.ai/news/openai-legacy-model-deprecation-wave-july-october-2026/)

### 2026-07-04: 初版執筆
- **内容**: ChatGPTとOpenAI APIの違い、料金体系の基本、APIキー取得手順、ノーコードツールとの連携例、Batch API/Function Calling/Structured Outputsの概要を整理
- **出典**: [OpenAI Developer Community](https://community.openai.com/t/openai-pay-as-you-go-vs-chatgpt-subscription/160812)、[OpenAI Developer Community: APIキー発行手順](https://community.openai.com/t/how-to-generate-openai-api-key/401363)、[SIOS Tech Lab](https://tech-lab.sios.jp/archives/46026)
- **注記**: モデル別の具体的な料金は変更が頻繁なため本文では意図的に固定額を明記していない。最新の単価は必ず [OpenAI公式Pricingページ](https://openai.com/api/pricing/) で確認すること
