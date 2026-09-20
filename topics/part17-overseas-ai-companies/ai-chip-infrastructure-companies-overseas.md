---
title: 海外のAI半導体・インフラ企業一覧
part: 17
chapter: 第2章 AI半導体・インフラ系
tags: [AI半導体, GPU, NVIDIA, AMD, Broadcom, Groq, Cerebras]
created: 2026-09-20
updated: 2026-09-20
---

# 海外のAI半導体・インフラ企業一覧

## このカテゴリについて

生成AIの学習・推論を支える計算基盤(GPU・AIアクセラレータ・カスタムASIC)を開発・
供給する海外企業を一覧する。ベンダー選定・調達リスク(特定チップへの依存)を検討する際の
基礎知識として使う。国内の同分野企業は
[AI半導体・アクセラレータ開発企業一覧(国内)](../part16-japan-ai-companies/ai-chip-accelerator-companies-japan.md)
を参照。クラウド経由でのモデル利用(Bedrock・Azure OpenAI Service等)は
[Azure OpenAI Service・Amazon Bedrock経由でのLLM API利用の基本](../part09-api-development/enterprise-cloud-llm-api-basics.md)
で扱っており、本ページは半導体・ハードウェアそのものの供給企業に絞る。

## 企業一覧

### NVIDIA

- **一言で**: AI向けGPU(データセンター向けアクセラレータ)で圧倒的シェアを持つ、生成AIブームの最大の受益者とされる半導体大手。
- **代表プロダクト・サービス**: Blackwell(B200/B300)シリーズ、次世代「Vera Rubin」プラットフォーム、AI開発フレームワーク「CUDA」。
- **特徴・強み**: 2026年に入りデータセンターAIアクセラレータの売上ベースシェアは75〜85%程度(2024年のピーク約87%からは低下したが依然として最大手)。2026年2月1日締め第4四半期(2026会計年度通期)のデータセンター売上は約1,937億ドル、直近四半期(2026年4月26日締め)は752億ドルで前年比92%増と急拡大が続く。AMD・Broadcom系カスタムASIC・自社チップ開発を進めるハイパースケーラー各社との競争が強まっているが、CUDAエコシステムを軸にした優位は当面続くと見られている。
- **料金の目安**: GPU自体は直接販売のほか、AWS・Azure・Google Cloud等のクラウド経由でのレンタル利用が一般的(非公開・案件ごと)。
- **最終確認日**: 2026-09-20

### AMD

- **一言で**: NVIDIAに次ぐデータセンターGPUベンダーとして、Instinctシリーズでシェア拡大を狙う半導体大手。
- **代表プロダクト・サービス**: AI向けGPU「Instinct MI400シリーズ」(フロンティアAI・AIファクトリー向け「MI455X」、ソブリンAI・HPC向け「MI430X」、オンプレミス企業向け「MI440X」)、ラックスケール基盤「Helios」。
- **特徴・強み**: 2026年のAdvancing AIイベントでMI400シリーズを正式発表。MI455XはTSMC N2プロセスの演算チップレット12基と3nmチップレット3基で構成され3,200億トランジスタを集積、HBM4メモリを288GB→432GBへ50%増量し帯域19.6TB/sを実現。72GPU構成のHeliosラックで2.9エクサFLOPSを謳う。データセンター(GPU)売上は四半期58億ドル規模まで拡大したが、NVIDIAとのシェア差は依然大きい。次世代「Instinct MI500」は2027年投入予定。
- **料金の目安**: クラウド経由(Oracle Cloud、Microsoft Azure等)でのレンタル利用が中心(非公開・案件ごと)。
- **最終確認日**: 2026-09-20

### Broadcom

- **一言で**: 自社ブランドのGPUは持たず、Google・OpenAI・Anthropic・Metaなど大手AI企業向けにカスタムAIチップ(ASIC)を共同設計・供給する「黒子」的存在の半導体大手。
- **代表プロダクト・サービス**: GoogleのTPU(2014年以来7世代を共同設計)、OpenAIと共同開発した推論特化チップ「Jalapeño」(2026年6月発表、2026年内の初期展開を計画)、Metaのカスタムアクセラレータ「MTIA」向け設計協力。
- **特徴・強み**: 2026年度第1四半期(2026年2月締め)のAI半導体売上は84億ドルで前年比106%増、第2四半期は107億ドルに拡大するとの見通しを提示。AI関連の受注残高(バックログ)は730億ドル規模とされ、CEOのHock Tan氏は「2027年にAIチップ関連売上が単年で1,000億ドルを超える見通しが立っている」と説明。2026年4月にはGoogleとTPUの将来世代設計・供給に関する2031年までの長期契約を締結したことをSEC提出書類(8-K)で開示。Anthropicとは2026年に1ギガワット、2027年に3ギガワットのTPU供給拡大で合意している。
- **料金の目安**: 個別カスタム設計のため非公開(契約はハイパースケーラー・AI企業との相対契約)。
- **最終確認日**: 2026-09-20

### Groq

- **一言で**: 推論(インファレンス)特化の独自チップ「LPU」を開発してきたスタートアップ。2025年末にNVIDIAへ技術ライセンス供与し、2026年はクラウド事業者(ニュークラウド)へ軸足を移している。
- **代表プロダクト・サービス**: 推論特化半導体「LPU」(Language Processing Unit)、トークン従量課金のクラウド推論サービス「GroqCloud」。
- **特徴・強み**: 2025年9月のシリーズEで69億ドル評価・7.5億ドルを調達したが、同年12月24日にNVIDIAがLPU関連技術を約200億ドルでライセンス取得すると発表し、創業者Jonathan Ross氏らがNVIDIAに移籍。この再編を経て2026年8月には35億ドル評価で3.5億ドルを追加調達し、NVIDIA製GPUを用いたニュークラウド(推論クラウド)事業へ転換した。次世代4nm LPUはSamsung Foundryとの提携で開発中。
- **料金の目安**: GroqCloudはトークン数に応じた従量課金制(モデル・レートにより変動)。
- **最終確認日**: 2026-09-20

### Cerebras Systems

- **一言で**: 「ウェハースケールエンジン(WSE)」と呼ぶ皿サイズの巨大チップでAI学習・推論を高速化する半導体スタートアップ。2026年5月にNasdaq上場(ティッカー: CBRS)を果たした。
- **代表プロダクト・サービス**: ウェハースケールエンジン(4兆個超のトランジスタを1枚のシリコンに集積)を搭載する「CS-3」システム、次世代「CS-6」(スタック型DRAM搭載予定)。
- **特徴・強み**: 2026年4月17日にSECへS-1(上場目論見書)を提出、5月13日に想定レンジを上回る価格でIPO価格決定、上場初日に株価が68%急伸し評価額は約488億ドルに達した(調達額は最大48億ドル規模で2026年時点最大級のIPOの一つ)。OpenAIとは2026年初頭に計算能力提供で200億ドル規模の複数年契約を締結。メモリ帯域は21PB/sとうたい、NVIDIAの新型Rubin GPUの約1,000倍と主張している。
- **料金の目安**: クラウド推論サービス(Cerebras Inference)はトークン従量課金、オンプレミス機器は個別見積もり。
- **最終確認日**: 2026-09-20

## 関連トピック

- [AI半導体・アクセラレータ開発企業一覧(国内)](../part16-japan-ai-companies/ai-chip-accelerator-companies-japan.md)
- [海外の主要基盤モデル企業一覧(フロンティアAI企業)](foundation-model-companies-overseas.md)
- [Azure OpenAI Service・Amazon Bedrock経由でのLLM API利用の基本](../part09-api-development/enterprise-cloud-llm-api-basics.md)
- [生成AIの電力消費・データセンター投資とエネルギー動向(2026年時点)](../part13-ai-trends/ai-energy-and-datacenter-trends.md)

## 更新履歴

### 2026-09-20: 初版執筆
- **内容**: NVIDIA・AMD・Broadcom・Groq・Cerebras Systemsの5社について、AI半導体・インフラ企業としての立ち位置・最新動向をまとめた
- **出典**: [siliconanalysts.com: NVIDIA AI GPU Market Share 2026](https://siliconanalysts.com/analysis/nvidia-ai-accelerator-market-share-2024-2026)、[AMD Newsroom: AAI 2026 MI400 Instinct Update](https://newsroom.amd.com/news/aai-2026-mi400-instinct-update/)、[Tom's Hardware: The custom AI ASIC state of play (May 2026)](https://www.tomshardware.com/tech-industry/semiconductors/custom-ai-asics-examined-from-broadcom-to-mtia)、[StockTitan: Broadcom secures long-term AI chip deal with Google (8-K)](https://www.stocktitan.net/sec-filings/AVGO/8-k-broadcom-inc-reports-material-event-35aab0650b17.html)、[TechCrunch: Groq raises $350M to fuel its pivot from AI chips to neocloud](https://techcrunch.com/2026/08/17/groq-raises-350m-to-fuel-its-pivot-from-ai-chips-to-neocloud/)、[IntuitionLabs: Nvidia's $20B Groq Acquisition](https://intuitionlabs.ai/articles/nvidia-groq-ai-inference-deal)、[CNBC: Cerebras IPO mints two billionaires](https://www.cnbc.com/2026/05/14/cerebras-ipo-mints-two-billionaires-sets-stage-for-potential-ai-wave.html)、[Futurum Group: Cerebras S-1 Teardown](https://futurumgroup.com/insights/cerebras-s-1-teardown-is-the-23b-wafer-scale-ipo-the-end-of-gpu-homogeneity/)
