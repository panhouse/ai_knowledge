---
title: "Azure OpenAI Service・Amazon Bedrock経由でのLLM API利用の基本(直接契約との違い)"
part: 9
chapter: 第1章 LLM APIの基礎
tags: [Azure OpenAI Service, Amazon Bedrock, Vertex AI, Gemini Enterprise Agent Platform, エンタープライズ調達, データレジデンシー, IAM, LLM API]
created: 2026-08-31
updated: 2026-08-31
---

# Azure OpenAI Service・Amazon Bedrock経由でのLLM API利用の基本(直接契約との違い)

## これは何か

[OpenAI APIの基本](openai-api-basics.md)や[Anthropic API(Claude API)の基本](anthropic-api-basics.md)で説明したのは、OpenAIやAnthropicと直接クレジットカードを登録して契約する「直接契約」の入口だった。しかし実際の企業導入では、情報システム部門やセキュリティ審査から「新しいベンダーとの契約は増やせない」「データは自社のクラウド契約(Azure/AWS/Google Cloud)の管理下から出せない」という理由で直接契約を止められ、代わりに**すでに契約しているクラウド事業者経由で同じモデルを呼び出す**よう指示されることが多い。これがAzure OpenAI Service(Microsoft経由でGPTモデルを呼ぶ)、Amazon Bedrock(AWS経由でClaudeなど複数社のモデルを呼ぶ)、Google Vertex AI(Gemini Enterprise Agent Platform。Google Cloud経由でGemini・Claudeなどを呼ぶ)という3つの「クラウド経由の入口」であり、モデルの中身(GPTやClaude)は直接契約と同じでも、認証方式・契約主体・請求経路・モデルの提供タイミングが異なる。本ページはこの「同じモデルを2通りの入口から呼べる」という構図と、実務でどちらを選ぶべきかを整理する。

## 仕組み・背景

- **モデルの中身は直接契約と同じ**: Azure OpenAI Serviceで動くGPT-5.6シリーズ(Sol/Terra/Luna)はOpenAIが開発したモデルそのものであり、Amazon Bedrock・Vertex AIで動くClaude Opus 5・Claude Sonnet 5もAnthropicが開発したモデルそのものである。モデルの回答品質や基本的な使い方(プロンプトの書き方)が変わるわけではない。
- **提供の仕組みが違う**: OpenAIとMicrosoftは資本・提携関係にあり、Azure上でOpenAIのモデルをMicrosoftが「Foundry Models」の一つとして卸売り的に提供している。一方Anthropicは「フロンティアAIモデルとしてAWS・Google Cloud・Microsoft Azureの3大クラウドすべてで使える唯一の存在」を標榜し、Amazon BedrockとGoogle CloudのVertex AI(2026年に「Gemini Enterprise Agent Platform」へ改称・Model Gardenに統合)の両方に自社モデルを提供するマルチクラウド戦略を取っている。GoogleのGeminiは自社モデルなので、Vertex AI(Gemini Enterprise Agent Platform)経由がGoogleにとっての企業向け入口になる。
- **契約主体と請求が変わる**: 直接契約では支払い先がOpenAI・Anthropic・Googleそのものになるのに対し、クラウド経由では既存のAzure請求書・AWSアカウント・Google Cloudの請求先にそのまま乗る。エンタープライズ契約(EA/ELA)の値引き・支出管理の対象にできる点が、情シス・調達部門にとっての最大の利点になる。
- **認証・呼び出し方が変わる**: 直接契約のAPIキー(`sk-...`や`x-api-key`)に対し、Azure OpenAI ServiceはAzureリソース単位のAPIキーまたはMicrosoft Entra ID(旧Azure AD)によるトークン認証+「デプロイ名」の指定、Amazon BedrockはAWSのIAM(アクセス権限管理)ロール+SigV4署名+リージョン別のモデルID、Vertex AIはGoogle CloudのプロジェクトID・リージョン・サービスアカウントという、まったく別の認証の作法になる(詳細は後述の比較表)。
- **モデルの提供タイミングにズレが生じうる**: OpenAIは自社の直接APIに新モデルを最初に投入し、Azure OpenAI Serviceへの反映は数週間〜数か月遅れることが多い(大型モデルほど遅れが大きい傾向)。一方Anthropicは「Claude Fable 5をAPI・Amazon Bedrock・Google Cloud・Microsoft Foundryで同時提供」のように主要モデルを複数入口でほぼ同時にリリースする方針を取っており、Claude Opus 5もAWS向け発表は直接API発表と同日(2026年7月24日)だった。ただし同時リリースでも、利用できるリージョン(データセンターの所在地域)は当初は限定的で、順次拡大していく点は共通する。

## 使いどころ・使い分け

| 項目 | Azure OpenAI Service | Amazon Bedrock | Google Vertex AI(Gemini Enterprise Agent Platform) | 直接契約(各社API) |
|---|---|---|---|---|
| 主に呼べるモデル | OpenAIのGPTシリーズ(GPT-5.6 Sol/Terra/Luna等) | Anthropic Claude、Amazon Nova、Meta Llama、Mistral等マルチベンダー | Google Gemini(Gemini 3.6 Flash/3.1 Pro等)、Anthropic Claude、Mistral等 | 各社1社分のみ |
| 請求経路 | 既存のAzure請求書・EA契約 | 既存のAWSアカウント・請求 | 既存のGoogle Cloud請求・契約 | ベンダーへの新規個別契約 |
| 主な認証方式 | APIキーまたはMicrosoft Entra ID | AWS IAM(ロール・ポリシー)+ SigV4署名 | Google Cloud IAM(サービスアカウント) | ベンダー発行のAPIキー |
| データ居住地(リージョン)の選択 | Azureの多数のリージョンから選択可能 | Bedrockが対応する各リージョンから選択(Claude Opus 5は主要リージョンで順次拡大中) | Google Cloudの各リージョンから選択可能 | 一部ベンダーはデフォルトが米国、エンタープライズ契約でのみ他地域対応 |
| 新モデルの反映速度 | OpenAI直接APIより数週間〜数か月遅れが常態化 | Anthropicは主要モデルをBedrockとほぼ同時公開の方針(ただし当初は一部リージョン限定) | 同上(Anthropic側の方針に準拠)。Google自身のGeminiは自社発表と足並みを揃えやすい | 各社とも自社APIが最速 |
| 料金 | 基本トークン単価はOpenAI直接APIと同水準だが、サポートプラン・PTU(予約枠)・ネットワーク関連費用が上乗せされ実質15〜40%程度高くなることがある | Claude はAnthropic直接APIと同じ単価(ゼロデータ保持ZDRが標準で有効になる点が特徴) | Anthropicモデルはグローバルエンドポイント基準で約10%のリージョン割増あり。Geminiは基本的に直接APIと同水準 | 基準となる単価 |
| 向いている企業 | すでにMicrosoft 365・Azure ADを中心に統制している企業、Azure EAで一括請求したい企業 | すでにAWSを基盤に使っている企業、複数ベンダーのモデルを1つのIAM基盤で統一管理したい企業 | すでにGoogle Workspace/Google Cloudを基盤に使っている企業、Geminiと他社モデルを併用したい企業 | クラウド契約がない・調達フローが軽い個人開発者やスタートアップ、最新モデルをいち早く試したい開発者 |

**判断基準(フローチャート的に)**

1. **すでに全社でAzure/AWS/Google Cloudのどれかとエンタープライズ契約を結んでいるか** → 結んでいるなら、まずそのクラウドの入口(Azure OpenAI Service / Amazon Bedrock / Vertex AI)を第一候補にする。追加のベンダー契約・追加の請求書を増やさずに済み、社内のセキュリティ審査も通りやすい。
2. **データ居住地・業界規制(金融のAPRA、医療のHIPAA等)への対応が必須か** → 必須ならクラウド経由を選ぶ。Azure OpenAI ServiceはHIPAA(Microsoftとの契約に基づく医療データ保護)・SOC 2 Type II・FedRAMP High・ISO 27001などの認証をAzure契約の枠組みでそのまま利用でき、リージョンを固定してデータの越境を防げる。Amazon BedrockもClaudeについてゼロデータ保持(ZDR)がデフォルト有効で、FedRAMP High・DoD IL4/5相当の認可を取得済み。直接契約はデータレジデンシーの選択肢が限られる(OpenAIはEU居住地対応がEnterpriseプラン限定など)。
3. **最新モデルをリリース当日から使いたいか** → 最優先ならOpenAIは直接API、AnthropicはAWS/Google Cloudへのほぼ同時公開があるためBedrock/Vertex AIでもさほど遅れない。Azure OpenAI Serviceだけは「数週間〜数か月の遅れ」を前提に計画する。
4. **複数ベンダーのモデルを1つの管理画面・IAM基盤で切り替えたいか** → Amazon Bedrock(Claude・Nova・Llama・Mistral等)やVertex AI(Gemini・Claude・Mistral等)はマルチベンダーのモデルを同一の認証・課金基盤で扱える。単一ベンダーのみでよいならAzure OpenAI Serviceで十分。
5. **既存のノーコード連携(Dify・n8n等)や社内システムの実装コストを抑えたいか** → 直接契約のAPIキー方式が最も設定項目が少なく、多くのノーコードツールも直接契約用のコネクタを標準搭載している。クラウド経由はIAMロールやAzure Entra IDの設定が1段階増える。

**使わない方がよい場面**: 個人の検証・小規模なプロトタイプで、そもそも自社のAzure/AWS/Google Cloud契約がない場合は、わざわざクラウドリソースを新規に作るより直接契約のAPIキーを使う方が圧倒的に早い。

## 実務での使い方

### Azure OpenAI Serviceの設定手順(画面の場所まで)

1. Azureポータル(portal.azure.com)にサインインし、上部の「リソースの作成」→検索欄に「Azure OpenAI」と入力し、表示された「Azure OpenAI」(Microsoft Foundry Models配下)を選択して「作成」をクリックする
2. 作成画面で「サブスクリプション」「リソースグループ」(新規作成可)、モデルが利用可能な「リージョン」、一意な「名前」を入力し、価格レベルは「Standard S0」を選択して「確認および作成」→「作成」を実行する(通常1分程度でデプロイ完了)
3. デプロイ完了後、リソースのページを開き「Foundryポータルに移動」(または直接 ai.azure.com にアクセスしてリソースを選択)する
4. 左メニューの「デプロイ」→「モデルをデプロイ」→「基本モデルをデプロイ」から使いたいモデル(例: gpt-5.6-terra)を選び、任意の「デプロイ名」(例: "prod-terra")を付けてデプロイする。**このデプロイ名がAPI呼び出し時のモデル指定になる点が直接契約と最大に異なる部分**で、OpenAI直接APIのようにモデルID文字列をそのまま渡すのではなく、自分で決めたデプロイ名を渡す
5. リソースの「キーとエンドポイント」画面(左メニュー)からAPIキーとエンドポイントURLを取得する。本番環境では管理が煩雑なAPIキーの代わりに、Microsoft Entra IDでアプリにマネージドIDを割り当て、「Cognitive Services OpenAI User」ロールを付与するキーレス認証が推奨されている
6. なお2026年時点でAzure OpenAI Serviceは引き続き「Limited Access」サービスに分類されているが、通常利用(コンテンツフィルターの変更やAbuse Monitoringの解除を伴わない利用)であればAzureの全顧客が申請フォームなしで利用でき、フィルター緩和など特殊な設定を行いたい場合のみ別途申請が必要になる

### 呼び出しコード例の比較(認証まわりの違い)

**Azure OpenAI Service(Python、APIキー認証)**

```python
from openai import AzureOpenAI

client = AzureOpenAI(
    azure_endpoint="https://<リソース名>.openai.azure.com/",
    api_key="<Azureで取得したキー>",
    api_version="2026-06-01",
)
response = client.chat.completions.create(
    model="prod-terra",  # モデルIDではなく「デプロイ名」を指定する
    messages=[{"role": "user", "content": "この請求書PDFの合計金額を1文で要約して"}],
)
```

**Amazon Bedrock(Python、boto3。事前にIAM認証情報を設定済みの前提)**

```python
import boto3, json

client = boto3.client("bedrock-runtime", region_name="us-east-1")
response = client.converse(
    modelId="global.anthropic.claude-sonnet-5",  # リージョン別・グローバル別のモデルID
    messages=[{"role": "user", "content": [{"text": "この請求書PDFの合計金額を1文で要約して"}]}],
)
```

**Google Vertex AI / Gemini Enterprise Agent Platform(Python、Claudeモデルを呼ぶ例)**

```python
from anthropic import AnthropicVertex

client = AnthropicVertex(project_id="<GCPプロジェクトID>", region="us-east5")
response = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "この請求書PDFの合計金額を1文で要約して"}],
)
```

Bedrockでは呼び出し前にAWSコンソールの「Amazon Bedrock」→左メニュー「Model access」からモデルへのアクセスを有効化しておく必要がある(2026年時点で多くのサーバーレスモデルは自動的にリージョン内で利用可能になったが、一部モデルやMarketplace経由のモデルは依然手動有効化が必要)。加えてIAMポリシーで`bedrock:InvokeModel`等の権限を許可しておく、という「モデルアクセスの有効化」と「IAM権限」の**二重のゲート**がある点がAzure・直接契約にはない特徴で、片方だけ設定を忘れると`AccessDeniedException`になる。

### ツール横断の対応付け

| 概念 | Azure OpenAI Service | Amazon Bedrock | Vertex AI(Gemini Enterprise Agent Platform) | 直接契約 |
|---|---|---|---|---|
| 管理画面 | Azure Portal / ai.azure.com(Foundryポータル) | AWSマネジメントコンソール(Bedrock) | Google Cloud Console(Vertex AI / Agent Platform) | platform.openai.com等 |
| モデルの指定単位 | 自分で名付けた「デプロイ名」 | リージョン付き・グローバル付きの「モデルID」 | 「モデルID」(publisher経由) | 「モデルID」 |
| 認証 | APIキー または Entra IDトークン | IAMロール+SigV4署名 | サービスアカウント(GCP認証) | APIキー |
| アクセス許可の単位 | Azureリソース+デプロイ | IAMポリシー+Bedrockの「Model access」設定(二重ゲート) | GCPプロジェクトのIAMロール | アカウント単位のAPIキー権限 |
| データ保持のデフォルト | Azure契約に準拠(リージョン選択・Zero Data Retention契約可) | Claudeはゼロデータ保持(ZDR)がデフォルト有効 | Google Cloudの契約に準拠 | ベンダーごとに既定のログ保持期間あり |
| 請求先 | Azureの請求書・EA契約 | AWSアカウントの請求 | Google Cloudの請求 | ベンダーへの個別支払い |

### 料金の考え方(2026年8月時点、必ず各社公式ページで最終確認)

- Azure OpenAI Service: GPT-5.6シリーズのグローバル配置は直接APIとほぼ同一のトークン単価だが、サポートプラン・PTU(予約スループット、月額目安2,448ドル/ユニットから)・データ egress・Private Link・Log Analyticsなどの周辺コストが積み上がり、実質的な総コストは直接APIより15〜40%程度高くなるケースが報告されている
- Amazon Bedrock: ClaudeモデルはAnthropic直接APIと「ドル建てで完全に同一」の単価設定(例: Claude Sonnet 5は2026年8月31日まで導入価格の$2/$10、以降$3/$15で両者共通)。Prompt Cachingの割引率も同一
- Vertex AI: Claudeモデルはグローバルエンドポイント基準の料金に対し、リージョン指定エンドポイントは約10%の割増が発生する。Gemini自体は基本的にGoogle AI Studio経由の直接APIと同水準
- いずれのクラウド経由でも、モデルの基本トークン単価そのものは直接契約とほぼ変わらないため、「クラウド経由だから高い/安い」と一律に語れない。周辺コスト(サポート・予約枠・リージョン割増)まで含めた総コストで比較すること

## 注意点・よくある誤解

- **「Azureを契約していれば自動でAzure OpenAI Serviceが使える」わけではない**: Azureサブスクリプションとは別に、Azure OpenAI Serviceのリソースを作成し、モデルごとにデプロイする作業が必要。しかもモデルによっては特定リージョンでの提供やクォータ申請が必要な場合がある。
- **モデルIDとデプロイ名を混同しない**: Azure OpenAI Serviceの呼び出しでは、直接APIのようにモデルID(例: `gpt-5.6-terra`)をそのまま渡すのではなく、自分でデプロイ時に付けた「デプロイ名」を渡す。他社の直接API用サンプルコードをそのまま流用すると、この違いでエラーになりやすい。
- **Bedrockは「モデルアクセスの有効化」と「IAM権限」の両方が必要**: どちらか一方だけ設定してもう一方を忘れると`AccessDeniedException`になる。特に新しいモデル(Claude Opus 5等)を使い始めるときは、まずコンソールの「Model access」画面で有効化されているか確認する。
- **新モデルの反映タイミングは経路によって大きく異なる**: 特にAzure OpenAI Serviceは大型モデルほど直接APIから数週間〜数か月遅れる傾向が続いている。「最新モデルをすぐ試したいが社内はAzure経由縛り」という場合、検証だけ直接APIの個人アカウントで先行させ、本番はAzure反映後に切り替える運用がよく取られる。
- **リージョンが限定される・データが越境することがある**: 「クラウド経由だから安全」と過信せず、実際にどのリージョンにデータが保存・処理されるかは各社のリージョン対応状況を個別に確認する。Anthropicの新モデルは当初一部リージョンのみでの提供から始まり、順次拡大していく点にも注意。
- **料金は「同じ」とは限らない**: BedrockのClaudeは直接APIと同額だが、Azure OpenAI Serviceは周辺コストで実質的に割高になりがちで、Vertex AIのClaudeはリージョン指定で約10%の割増がある。単純な「クラウド経由は高い/安い」という思い込みではなく、モデル・提供元ごとに個別に確認する。
- **クラウド経由でも「Anthropic API直接の新機能」がすぐ使えるとは限らない**: Claude Managed AgentsのようなAnthropic側で先行提供される機能は、Bedrock/Vertex AIへの展開が後追いになることがある。機能単位での提供状況も併せて確認する。

## 最初の一歩

すでに自社がAzure・AWS・Google Cloudのいずれかとエンタープライズ契約を結んでいるなら、まずそのクラウドの管理コンソールで「Azure OpenAI」「Amazon Bedrock」「Vertex AI」のいずれかを検索し、自分のアカウントで既にアクセス可能になっているか(Bedrockなら「Model access」画面)を確認するところから始めるとよい。

## 関連トピック

- [主要LLM APIの横断比較(OpenAI・Anthropic・Google)](llm-api-cross-tool-comparison.md)
- [OpenAI APIの基本](openai-api-basics.md)
- [Anthropic API(Claude API)の基本](anthropic-api-basics.md)
- [Google Gemini APIの基本](google-gemini-api-basics.md)
- [プロンプト・RAG・ファインチューニングの使い分け](../part02-llm-basics/finetuning-vs-rag-vs-prompting.md)

## 更新履歴

### 2026-08-31: 初版執筆
- **内容**: Azure OpenAI Service・Amazon Bedrock・Google Vertex AI(Gemini Enterprise Agent Platform)経由でのLLM API利用と、OpenAI/Anthropic/Google直接契約との違いを整理。企業がクラウド経由を選ぶ理由(既存クラウド契約への一本化、データレジデンシー・SOC2/ISO/FedRAMP対応、IAM統合)、認証方式(Azureキー/Entra ID+デプロイ名、Bedrock IAM+モデルID、Vertex AIプロジェクト/リージョン)の違い、Azure OpenAI Serviceのリソース作成〜モデルデプロイの画面手順、料金の同一性・非同一性(Bedrock ClaudeはAnthropic直接APIと同額、Azureは周辺コストで15〜40%程度割高になりうる、Vertex AIのClaudeはリージョン指定で約10%割増)、新モデル反映タイミングの違い(Azureは数週間〜数か月遅れが常態化、AnthropicはBedrock/Vertex AIとほぼ同時公開の方針)を新規執筆
- **出典**: [Microsoft Learn: Endpoints for Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/endpoints)、[Microsoft Learn: Create and deploy an Azure OpenAI resource](https://learn.microsoft.com/en-us/azure/foundry-classic/openai/how-to/create-resource)、[Microsoft Learn: Limited access to Azure OpenAI in Microsoft Foundry Models](https://learn.microsoft.com/en-us/azure/foundry/responsible-ai/openai/limited-access)、[Azure Blog: GPT-5.6 now available in Microsoft Foundry](https://azure.microsoft.com/en-us/blog/gpt-5-6-now-available-in-microsoft-foundry/)、[CloudZero: Azure OpenAI pricing in 2026](https://www.cloudzero.com/blog/azure-openai-pricing/)、[AWS: Claude Opus 5 is now available on AWS](https://aws.amazon.com/about-aws/whats-new/2026/07/claude-opus-5-aws/)、[AWS Blog: Introducing Claude Opus 5 on AWS](https://aws.amazon.com/blogs/machine-learning/introducing-claude-opus-5-on-aws-anthropics-most-capable-opus-model/)、[AWS Security Blog: Simplified model access in Amazon Bedrock](https://aws.amazon.com/blogs/security/simplified-amazon-bedrock-model-access/)、[Anthropic: Claude in Amazon Bedrock approved for FedRAMP High and DoD IL4/5](https://www.anthropic.com/news/claude-in-amazon-bedrock-fedramp-high)、[Claude Platform Docs: Claude on Google Cloud (Vertex AI)](https://platform.claude.com/docs/en/build-with-claude/claude-on-vertex-ai)、[Google Cloud: Try Claude on Agent Platform's Model Garden](https://cloud.google.com/products/model-garden/claude)、[Hikari's Notebook: Comparing Anthropic API and AWS Bedrock Pricing](https://www.hikari-dev.com/en/blog/2026/03/30/anthropic-api-vs-bedrock-price/)、[EPC Group: Azure OpenAI vs OpenAI API: Enterprise Comparison 2026](https://www.epcgroup.net/blog/azure-openai-vs-openai-api-enterprise-comparison-2026)、[Reintech: OpenAI API vs Azure OpenAI vs AWS Bedrock: Enterprise LLM Comparison 2026](https://reintech.io/blog/openai-api-vs-azure-openai-vs-aws-bedrock-enterprise-llm-comparison-2026)
- **注記**: モデル世代・料金・提供リージョンは変更が非常に頻繁なため、本文の数値は目安として扱い、導入時は必ずMicrosoft Learn(learn.microsoft.com)・AWS公式ドキュメント(docs.aws.amazon.com)・Google Cloud公式ドキュメント(docs.cloud.google.com)・Anthropic公式ページ(platform.claude.com)で最新状況を確認すること
