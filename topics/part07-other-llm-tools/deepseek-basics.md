---
title: "DeepSeekの基本"
part: 7
chapter: "第2章 その他のLLM"
tags: [DeepSeek, 中国AI, オープンウェイト, 推論モデル, データプライバシー]
created: 2026-07-06
updated: 2026-07-06
---

# DeepSeekの基本

## これは何か

DeepSeek(ディープシーク)は、中国のAI企業DeepSeek(杭州、クオンツファンドHigh-Flyer系列)が開発する生成AIで、無料のチャットアプリ・API・そして「オープンウェイト」(AIモデルの重みファイル=パラメータそのものを公開し、誰でも自社サーバーで動かせる状態にすること)のモデル群で知られる。2025年1月に主力モデルを低コストで開発したと発表し、米国のAI関連株が急落するほどの衝撃を与えたことで世界的に知られるようになった。日本のビジネスパーソンにとっての論点は、「ChatGPT・Claude・Geminiより圧倒的に低コストで使え、しかも自社インフラに持ち込んで動かせる」という魅力と、「中国企業が提供するサービスにデータを送ってよいのか」というデータの扱いへの懸念が同時に存在する点にある。

## 仕組み・背景

DeepSeekが注目された最大の理由は「オープンウェイト戦略」と「低コスト開発の主張」の2つ。

- **オープンウェイト戦略**: モデルの重みをHugging Face等で公開し、多くのモデルをMITライセンス(改変・商用利用・再配布をほぼ自由に許可するオープンソースライセンス)で提供している。企業はAPIを使うだけでなく、重みをダウンロードして自社サーバーやプライベートクラウドの上で動かす「self-hosting(自社ホスティング)」ができる。これはChatGPT・Claude・Geminiの主力モデルが非公開(クローズド)であるのとは対照的な戦略。
- **低コスト開発の主張とその信頼性**: 2025年1月公開時、DeepSeekは主力モデル(V3系)の事前学習にかかったGPU代を「約560万ドル」と公表し、「OpenAIやGoogleの数十分の一のコストで同水準のモデルを作れた」という受け止め方が広がった。ただしこの数字は事前学習用GPUの稼働コストのみを指し、研究開発人件費・試行錯誤にかかった追加の学習・データ整備・インフラ投資などを含んでいない。調査会社SemiAnalysisなどは、ハードウェア投資まで含めた実質コストは十数億ドル規模との推計を示しており、「破格の低コストで最先端に追いついた」という報道は割り引いて理解する必要がある。

現行のモデルラインナップ(2026年7月時点)は次のとおり。

| モデル | 位置づけ | パラメータ規模 | ライセンス |
|---|---|---|---|
| DeepSeek-V4-Pro | 最上位モデル。複雑な推論・コーディングに強い | 総1.6T(活性化49B)、コンテキスト1M | MIT(オープンウェイト) |
| DeepSeek-V4-Flash | 軽量・低コスト版。日常的な処理向け | 総284B(活性化13B)、コンテキスト1M | MIT(オープンウェイト) |
| DeepSeek-R1(旧世代) | 推論特化モデルとして2025年に話題化。現在はV4に統合 | - | MIT(オープンウェイト) |

かつて「推論モデル」として話題を集めたR1系は、V4では独立した別モデルではなく「思考モード」(Non-Think/Think High/Think Maxの3段階)としてV4-Pro・V4-Flashに統合されている。次世代モデル「R2」は2026年7月時点で公式発表がなく、噂の域を出ていない。

## 使いどころ・使い分け

| 状況 | 判断の目安 |
|---|---|
| コストを最優先したい大量処理(要約・分類・下書き生成など) | DeepSeek V4-Flash(API)が有力な選択肢。ChatGPT・Claudeの数十分の一の価格帯 |
| 自社インフラに閉じた環境でLLMを動かしたい(クラウド外部にデータを出せない業種・規制対応) | オープンウェイトを自社GPU上でself-hostする用途に向く(後述のとおり相応のGPU投資が必要) |
| 契約書・顧客情報・未公開の経営情報など機密性の高いデータを扱う業務 | DeepSeek公式のチャット・APIはデータが中国側サーバーに送られるため不向き。ChatGPT Enterprise・Claude Team/Enterprise・Gemini for Workspace等、データ保護契約のある法人向けプランを使う |
| 最先端の自律的エージェント作業・マルチモーダル処理(画像・音声・自動操作) | ChatGPT・Claude・Geminiが機能の広さで先行することが多い |
| コーディング・推論系ベンチマークでの生の性能 | DeepSeek V4-ProはSWE-bench等でGPT-5系・Claude Opus系に匹敵する結果を示す報告があり、性能だけを見れば十分競合力がある |

判断の目安: 「性能とコストだけを比較するなら候補に入るが、機密データを扱うなら公式サービスは避け、扱うとしても自社ホスティングに限定する」というのがビジネス利用の実務的な線引きになる。

### コスト・性能のクロスツール比較(2026年7月時点の目安)

| 軸 | DeepSeek | ChatGPT(OpenAI) | Claude(Anthropic) | Gemini(Google) |
|---|---|---|---|---|
| 標準モデルの入力料金(1Mトークンあたり目安) | V4-Flashで$0.14前後 | GPT-5系で$2〜3程度 | Sonnet系で$3程度 | Gemini系で$1〜数ドル程度 |
| オープンウェイトでの自社ホスティング | 可(MITライセンス) | 不可(クローズド) | 不可(クローズド) | 一部軽量モデルのみGemmaとして別途公開 |
| 法人向けデータ保護契約(学習に使わない等) | 公式サービスには同種の契約なし | ChatGPT Enterpriseで提供 | Team/Enterpriseで提供 | Gemini for Workspaceで提供 |
| データの保存先 | 中国国内のサーバー | 各社の契約条件による(主に米国等) | 各社の契約条件による(主に米国等) | 各社の契約条件による(主に米国等) |

料金・性能は数か月単位で変動するため、実際の見積もりの際は各社公式のPricingページで最新値を確認すること。

## 実務での使い方

### 個人・検証目的で試す場合

- **チャットアプリ**: [chat.deepseek.com](https://chat.deepseek.com)(Web版)、およびiOS/Android向けアプリから無料で利用できる。ただしモバイルアプリは国・地域によって配信状況が変わることがある(後述の「注意点」参照)
- 使い方はChatGPT等と同様で、テキストを入力するだけ。「DeepThink」のようなボタンで思考モード(推論を深く行うモード)をオン・オフできる

### 開発者向け:API

- [platform.deepseek.com](https://platform.deepseek.com)でアカウント登録し、APIキーを発行する
- OpenAI互換のエンドポイント形式で呼び出せるため、既存のOpenAI SDKのコードをベースURLとモデル名だけ変えて動かせる
- 主なモデルID: `deepseek-v4-pro`(高性能)、`deepseek-v4-flash`(軽量・低コスト)。旧モデル名`deepseek-chat`/`deepseek-reasoner`は2026年7月24日に廃止予定で、それまでは自動的にV4-Flashの非思考モード/思考モードにルーティングされる
- 料金目安(1Mトークンあたり、キャッシュ未ヒット時): V4-Flashが入力$0.14/出力$0.28、V4-Proが入力$0.4〜$1.7程度/出力$0.9〜$3.5程度(提供元・キャッシュ条件により変動)。同じプロンプトを繰り返し使う場合のキャッシュヒット時はさらに大幅に安くなる
- 契約前には必ず[DeepSeek公式のPricingページ](https://api-docs.deepseek.com/quick_start/pricing)で最新の金額を確認すること

### 自社ホスティング(オープンウェイトの活用)

- V4-Pro・V4-Flashの重みはHugging Face(`deepseek-ai`名義)で公開されており、MITライセンスの範囲で商用利用・改変・再配布ができる
- vLLM等の推論エンジンを使って自社・クラウドのGPU上に展開する運用が一般的だが、必要なGPUメモリの規模は大きく(V4-Flashで約158GB、V4-Proで約862GB相当のモデルサイズ)、個人や中小企業が手軽に導入できる規模ではない。実質的には、ある程度のインフラ投資ができる企業がデータを外部に出さずに使うための選択肢と捉えるのが実務的
- 自社ホスティングであれば、モデルへの入力データは自社の管理下から外部(中国側サーバー等)へ送られないため、後述するデータプライバシーの懸念は基本的に回避できる

## 注意点・よくある誤解

- **公式チャット・APIを使うと、データは中国国内のサーバーに送信される**: 日本の個人情報保護委員会は2025年2月、DeepSeekに関する情報提供を公表し、データが中国の法制度の適用対象になりうる点に注意を呼びかけた。また日本のデジタル庁も2025年2月、各省庁に対して業務利用を控えるよう事務連絡を出している。あくまで「公務員・政府機関向けの注意喚起」であり、日本国内での全面的な使用禁止措置ではない点には留意が必要だが、機密情報の取り扱いには相応の慎重さが求められる
- **他国では利用制限の動きがある**: 韓国の個人情報保護委員会(PIPC)は、DeepSeekがユーザーの同意なくTikTok運営会社ByteDance系列の中国クラウド事業者(北京火山引擎/Beijing Volcano Engine)にプロンプト等のデータを送信していたと発表し、韓国国内のアプリストアからDeepSeekアプリが一時配信停止となった。イタリアの個人データ保護当局(Garante)も同様の懸念からサービス提供を制限した経緯があり、オーストラリア・台湾・米国の一部州機関などでも政府端末での利用制限が報じられている。ただしこれらは「政府機関・公的部門での利用制限」が中心で、民間企業・個人による利用そのものを禁止する国は限定的であり、対応は国・時期によって分かれる
- **規制状況は流動的**: 上記はいずれも執筆時点(2026年7月)のスナップショットであり、各国の規制・企業の内部方針は短期間で変わりうる。実際に業務利用を検討する際は、必ず自社の情報システム部門・法務部門に最新の可否を確認すること
- **「低コスト学習」の宣伝を額面通りに受け取らない**: 「560万ドルで学習できた」という数字はGPU稼働費のみを指し、研究開発人件費やインフラ投資を含んでいない。第三者機関の推計では実質投資額は十数億ドル規模とされ、「破格の安さで最先端モデルに追いついた」という論調は誇張を含む可能性がある
- **「オープンウェイトだから安全」と「公式サービスだから安全」を混同しない**: 自社GPU上でモデルの重みを動かす自社ホスティングであればデータは外部に出ないが、chat.deepseek.comや公式APIをそのまま使う場合はデータが中国側サーバーに送られる。この2つは同じ「DeepSeek」でもリスクの構造が全く異なる
- **機密情報・個人情報は入力しない**: 検証・お試し目的で公式チャット・APIを使う場合も、契約書・顧客情報・未公開の経営情報などは入力しない運用にするのが無難

## 最初の一歩

業務での本格採用ではなく技術検証・コスト比較の目的であれば、まずchat.deepseek.comで機密性のない一般的な質問(コード生成のお試し、文章の下書きなど)を1つ試し、回答品質とコスト感を体感してみる。ただし社内で使う前には、情報システム部門・法務部門に利用可否を確認すること。

## 関連トピック

- [Google Geminiの基本](./google-gemini-basics.md)
- [Claude(Anthropic)の基本](./claude-basics.md)
- [Microsoft Copilotの基本](./microsoft-copilot-basics.md)
- [生成AI利用における情報漏洩対策](../part03-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: DeepSeekの位置づけ(オープンウェイト戦略・低コスト開発の主張とその信頼性)、V4-Pro/V4-Flashの現行ラインナップとR1からの統合経緯、チャットアプリ・API・自社ホスティングの実務的な使い方、日本のデジタル庁・個人情報保護委員会の注意喚起と他国の利用制限動向、ChatGPT/Claude/Geminiとのコスト・データ保護面の比較を整理
- **出典**: [DeepSeek API Docs: Models & Pricing](https://api-docs.deepseek.com/quick_start/pricing)、[DeepSeek API Docs: Thinking Mode](https://api-docs.deepseek.com/guides/thinking_mode)、[DeepSeek API Docs: V4 Preview Release](https://api-docs.deepseek.com/news/news260424)、[CNBC: China's DeepSeek releases preview of long-awaited V4 model as AI race intensifies](https://www.cnbc.com/2026/04/24/deepseek-v4-llm-preview-open-source-ai-competition-china.html)、[デジタル庁: DeepSeek等の生成AIの業務利用に関する注意喚起(事務連絡、令和7年2月6日)](https://www.digital.go.jp/assets/contents/node/basic_page/field_ref_resources/d2a5bbd2-ae8f-450c-adaa-33979181d26a/e7bfeba7/20250206_councils_social-promotion-executive_outline_01.pdf)、[個人情報保護委員会: DeepSeekに関する情報提供](https://www.ppc.go.jp/news/careful_information/250203_alert_deepseek/)、[日本経済新聞: DeepSeekの利用に注意 政府が各省庁に喚起](https://www.nikkei.com/article/DGXZQOUA069NC0W5A200C2000000/)、[South China Morning Post: South Korea says DeepSeek sent data to ByteDance owned servers in China without consent](https://www.scmp.com/news/asia/east-asia/article/3307788/south-korea-says-deepseek-sent-data-bytedance-owned-servers-china-without-consent)、[Techstrong.ai: Early Critic of DeepSeek Says Model Cost Was $1.6 Billion, Not $5.6 Million](https://techstrong.ai/agentic-ai/early-critic-of-deepseek-says-model-cost-was-1-6-billion-not-5-6-million/)、[CNBC: DeepSeek's AI claims have shaken the world — but not everyone's convinced](https://www.cnbc.com/2025/01/30/chinas-deepseek-has-some-big-ai-claims-not-all-experts-are-convinced-.html)
