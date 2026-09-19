---
title: 海外の主要基盤モデル企業一覧(フロンティアAI企業)
part: 17
chapter: 第1章 基盤モデル・フロンティアAI系
tags: [基盤モデル, LLM, OpenAI, Anthropic, Google, Microsoft, Amazon, Meta, xAI]
created: 2026-09-19
updated: 2026-09-19
---

# 海外の主要基盤モデル企業一覧(フロンティアAI企業)

## このカテゴリについて

このページは、海外(日本国外)で独自の基盤モデル(LLM: 大規模言語モデルなど)を開発・
提供している主要企業を一覧する。ChatGPT・Claude・Geminiのような「製品としての使い方・
料金プラン・APIの詳細」は、各社の個別ページ(下記「関連トピック」参照)で深掘りしている
ため、このページでは重複させず、**企業としての立ち位置・資金調達・戦略・提携**に絞って
まとめる。資金調達額・評価額・提携関係は数週間〜数か月単位で変動するため、意思決定に
使う際は必ず各社の公式発表で最新状況を確認すること。より詳しい業界構造・提携動向の分析は
[生成AI業界の主要プレイヤーと動向](../part13-ai-trends/ai-industry-major-players-trends.md)
(Part 13)を参照。

## 企業一覧

### OpenAI

- **一言で**: ChatGPTと最新フラッグシップ「GPT-6 Astra」を開発する、非営利法人が支配権を持つ営利子会社(OpenAI Group PBC)体制のAI企業。
- **代表プロダクト・サービス**: ChatGPT、GPT-6 Astra(2026年9月3日投入)、コーディングエージェント「Codex」、動画生成「Sora」、自社設計・Broadcom製造の推論特化チップ「Jalapeño」。
- **特徴・強み**: 2026年3月末に総額1,220億ドルの資金調達を完了し評価額8,520億ドルに到達。ARR(年換算売上高)は2026年7月時点で約400億ドル(2025年末の倍)まで急拡大し、企業向け売上が四半期50%増で初めて法人向けが売上の過半を占める構成に転換した。上場は2027年目標との観測があったが、2026年9月13日にサム・アルトマンCEOがAI安全性対応を理由に「2026年中は上場しない」と明言する一方、同時期に評価額1.2兆〜1.5兆ドル規模の新規資金調達が投資家主導で協議されており、非公開のまま調達を続ける方針。SoftBankが主要出資者(累計出資額約646億ドル)で、日本法人はソフトバンクとの合弁「SB OAI Japan」を通じ法人向けAI「Crystal Intelligence」を展開。
- **料金の目安**: GPT-6 AstraのAPI価格は入力100万トークンあたり10ドル・出力50ドル(前世代GPT-5.6 Sol比で約2.5倍に上昇)。ChatGPTのプラン別料金・APIの詳細は[ChatGPTのモデル一覧と使い分け](../part03-ai-chat-tools/chatgpt-model-lineup.md)・[OpenAI APIの基本](../part09-api-development/openai-api-basics.md)を参照。
- **最終確認日**: 2026-09-19

### Anthropic

- **一言で**: 企業(エンタープライズ)向け利用に軸足を置く戦略を明確にしている、Claudeシリーズの開発元。
- **代表プロダクト・サービス**: Claude(Opus/Sonnet/Haiku、最新モデルは「Claude Fable 5.1」「Claude Mythos 5.1」)、開発者向けエージェント「Claude Code」。
- **特徴・強み**: 法人向けAPI市場でOpenAIを上回るシェアとの報道が続き、ARR(年換算売上高)は2026年4月300億ドル→5月470億ドル→7月末650億ドルと急拡大、第2四半期には四半期売上109億ドル・初の営業黒字(約5.6億ドル)を計上した。2026年9月時点でNasdaq上場に向けた手続きが進行中(当初9月末〜10月上旬目標だったが10月中旬以降・米中間選挙直前へ後ろ倒し)で、目標評価額は市場推計で最大2兆ドル規模、調達額130億ドル超との観測がある。増資に加え、特別目的会社(SPV)を介してGoogle製TPUをリースする「オフバランス」型のチップ調達契約を約60日間で総額710億ドル規模積み上げるなど、資金調達手法の多角化が進む。半導体・計算資源の調達先はAmazon・Google・Microsoft/Nvidia・Oracle Cloud Infrastructureと多岐にわたる。
- **料金の目安**: 詳細な最新価格・プランは[Claudeの基本](../part03-ai-chat-tools/claude-basics.md)・[Anthropic APIの基本](../part09-api-development/anthropic-api-basics.md)を参照。
- **最終確認日**: 2026-09-19

### Google(Alphabet / Google DeepMind)

- **一言で**: 自社LLM(Gemini)・自社クラウド(Google Cloud)・自社半導体(TPU)・配布チャネル(検索・Android・Workspace)を垂直統合する形でAI事業を展開するAlphabet傘下の企業群。
- **代表プロダクト・サービス**: Gemini(現行主力は2026年2月投入の「Gemini 3.1 Pro」、Flash系列は2026年9月2日投入の「Gemini 3.8 Flash」)、委任型エージェント「Gemini Spark」、動画生成「Veo」、自社設計半導体TPU。
- **特徴・強み**: 次期フラッグシップ「Gemini 3.5 Pro」は2026年5月の予告以降6〜8月と延期を繰り返し、9月時点でも正式版は未投入(一部エンタープライズ向けVertex AIプレビューのみ)。開発難航・人材流出を受け2026年8月にAI部門の指揮系統を刷新し、Demis HassabisはCEOから会長(Chair)へ退き、CTOのKoray KavukcuogluがCEOサンダー・ピチャイへ直轄報告するSVPに就任。27年在籍したJeff Deanら幹部研究者が退社し独立系AI企業「Discovery Loop」を設立(GoogleはDiscovery Loopに出資・クラウド提供で関与を継続)。共同創業者Sergey BrinもAI商用化の陣頭指揮に復帰している。
- **料金の目安**: 詳細な最新価格・プランは[Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)・[Google Gemini APIの基本](../part09-api-development/google-gemini-api-basics.md)を参照。
- **最終確認日**: 2026-09-19

### Microsoft

- **一言で**: OpenAI・Anthropic双方の大株主でありながら、両社と競合する自社開発モデルも展開する「二重の立場」を強めるクラウド・ソフトウェア大手。
- **代表プロダクト・サービス**: Copilot、Azure OpenAI Service、自社開発モデル「MAI」シリーズ(7種、中核はMAI-Thinking-1)。
- **特徴・強み**: 2025年10月の再編でOpenAI Group PBCの約27%株式を保有。2026年4月にOpenAIとの独占契約を解消し、OpenAIが他クラウドでもモデルを提供可能になった。MAI-Thinking-1は独立評価でClaude Sonnet 4.6と互角、SWE-Bench ProのコーディングスコアはOpus 4.6水準とされ、企業に対し単一のフロンティアラボに依存せず複数モデルを併用するよう促す姿勢を鮮明にしている。会計年度2026年第4四半期のAzure売上は前年比43%増(通期1,000億ドル超)、設備投資は前年比70%増の410億ドルに達し、通期の設備投資見通しは会計年度2027年には1,300億ドル規模へ倍増する見通し。2026年8月にはOpenAIと共同で北欧に次世代専用半導体アーキテクチャを用いたAIスーパーコンピューティング拠点を新設すると発表した。
- **料金の目安**: Copilot・Azure OpenAI Serviceの料金プランは製品ごとに個別。[Microsoft Copilotの基本](../part03-ai-chat-tools/microsoft-copilot-basics.md)・[Azure OpenAI Service・Amazon Bedrock経由でのLLM API利用の基本](../part09-api-development/enterprise-cloud-llm-api-basics.md)を参照。
- **最終確認日**: 2026-09-19

### Amazon(AWS)

- **一言で**: 「特定のモデルが市場を独占することはない」という前提に立ち、他社モデルへの計算資源提供と自社モデル・自社半導体の展開を両立させる「両建て」戦略を取るクラウド大手。
- **代表プロダクト・サービス**: 複数モデルを切り替えて使えるプラットフォーム「Bedrock」、自社モデル「Nova」シリーズ(Nova 2 Lite/Pro/Sonic)、自社設計半導体「Trainium」。
- **特徴・強み**: 2026年8月初旬の決算で2026年通期のAI関連設備投資見通しを約2,000億ドルからメモリ価格上昇等を理由に2,200億ドルへ上方修正し、AWSの受注残高(バックログ)は前年比2.5倍の4,960億ドルに達したと発表、2027年まで需要に供給が追いつかない状態が続くと説明している。Anthropicとは今後10年で1,000億ドル超をAWS技術(Trainium2/3/4、Graviton)に投じる契約を締結済み。OpenAIとの間でも、当初380億ドル規模だったクラウド契約をAmazonの50億ドル出資と合わせて今後8年で最大1,000億ドル規模へ拡張するなど、フロンティアラボ各社との取引を広げている。
- **料金の目安**: Bedrock・Novaの料金プランは[Azure OpenAI Service・Amazon Bedrock経由でのLLM API利用の基本](../part09-api-development/enterprise-cloud-llm-api-basics.md)を参照。
- **最終確認日**: 2026-09-19

### Meta

- **一言で**: 最先端モデルを非公開(クローズド)路線に転換する一方、中位モデルはオープンウェイトで公開する二層構造を取るSNS大手のAI部門。
- **代表プロダクト・サービス**: Meta AI、画像・動画・コーディング生成の「Muse」シリーズ(Muse Image/Video/Spark/Code)、インフラ事業「Meta Compute」。
- **特徴・強み**: 最先端モデルは2026年7月のホスト型Llama API終了以降、非公開の新シリーズ(社内コード名「Avocado」、開発は新設のTBD Lab)に置き換わりつつある一方、中位モデル「Muse Spark 1.2」(改変版Llama Community Licenseで重み公開)や29.6BパラメータのApache 2.0ライセンスモデル「Muse Glimmer」も投入しており、「フロンティア級は非公開・中位モデルはオープンウェイト」という二層戦略が明確になった。同時期にMeta Superintelligence Labsを訓練・研究・製品・インフラの4グループに再編し、FAIR(基礎研究)・製品AI・AIインフラ部門を中心に約600人のAI人員を削減する一方、Avocadoを開発するTBD Labは採用を継続。政策面ではNVIDIA・Microsoftらと「オープンウェイトモデルへの拙速な規制に反対する」公開書簡に名を連ねている。
- **料金の目安**: Meta AIの利用状況・料金は[Meta AIの基本](../part03-ai-chat-tools/meta-ai-basics.md)を参照。
- **最終確認日**: 2026-09-19

### xAI(SpaceXAI)

- **一言で**: 2026年2月にSpaceXと株式交換で統合し、Grokシリーズを開発するElon Musk系のAI企業。
- **代表プロダクト・サービス**: Grok(最新は「Grok 4.5」、開発中の次期モデル「Grok 5」)、AIコーディングエディタ「Cursor」(2026年8月に買収完了)。
- **特徴・強み**: 2026年2月にSpaceXと株式交換で統合(合併後評価額1.25兆ドル)、同年6月12日にSpaceXがNasdaqへ上場(IPO調達額750億ドル、評価額1.77兆ドル)。コーディング特化のAI企業Cursorについては2026年4月に買収の権利(株式交換)で合意し、上場後の6月16日に権利行使を発表、8月14日付けで約600億ドル・全株式交換による買収を正式に完了した。7月8日にはCursorと共同開発した新モデル「Grok 4.5」を投入(Elon Muskは「Opus級モデルをより速く、低コストに」と説明)。次期モデル「Grok 5」(6兆パラメータ規模とも報じられる)は複数回の延期を重ね、2026年9月時点でも公開時期は未定のまま。
- **料金の目安**: Grokの利用状況・料金は[Grokの基本](../part03-ai-chat-tools/grok-basics.md)を参照。
- **最終確認日**: 2026-09-19

## 関連トピック

- [生成AI業界の主要プレイヤーと動向(資金調達・提携・戦略)](../part13-ai-trends/ai-industry-major-players-trends.md)
- [ChatGPTのモデル一覧と使い分け](../part03-ai-chat-tools/chatgpt-model-lineup.md)
- [Claudeの基本](../part03-ai-chat-tools/claude-basics.md)
- [Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)
- [Microsoft Copilotの基本](../part03-ai-chat-tools/microsoft-copilot-basics.md)
- [Meta AIの基本](../part03-ai-chat-tools/meta-ai-basics.md)
- [Grokの基本](../part03-ai-chat-tools/grok-basics.md)
- [国産基盤モデル・研究開発系AI企業一覧](../part16-japan-ai-companies/foundation-model-companies-japan.md)

## 更新履歴

### 2026-09-19: 初版執筆
- **内容**: OpenAI・Anthropic・Google(Alphabet)・Microsoft・Amazon(AWS)・Meta・xAI(SpaceXAI)の7社について、企業としての立ち位置・資金調達・戦略・提携をまとめた。製品機能・料金の詳細は各社の個別ページ(Part3・Part9)へ内部リンクし、重複を避けた。数値・固有名詞はPart13「生成AI業界の主要プレイヤーと動向」で確認済みの出典に基づく
- **出典**: [OpenAI: GPT-6 Astra](https://openai.com/index/gpt-6-astra/)、[Benzinga: OpenAI Eyes Fresh Funding at $1.2 Trillion Valuation as Sam Altman Rules Out 2026 IPO](https://www.benzinga.com/markets/tech/26/09/61807691/openai-funding-valuation-sam-altman-rules-out-2026-ipo)、[SoftBank Group: Execution of Follow-on Investment (Second Tranche) in OpenAI](https://group.softbank/en/news/press/20260701)、[CNBC: Anthropic IPO launch shifts toward mid-October: Reuters](https://www.cnbc.com/2026/09/05/anthropic-ipo-launch-shifts-toward-mid-october-reuters.html)、[Yahoo Finance: Anthropic SPVs Stack $71 Billion in Chip-Lease Debt in 60 Days](https://finance.yahoo.com/technology/ai/articles/anthropic-spvs-stack-71-billion-000514097.html)、[Fortune: Demis Hassabis steps down from Google DeepMind CEO role amid a major AI leadership shake-up](https://fortune.com/2026/08/05/demis-hassabis-steps-down-google-deepmind-ai-shakeup/)、[The Register: With Gemini 3.8 Flash, Google reminds everyone it's still in the race](https://www.theregister.com/ai-and-ml/2026/09/02/with-gemini-38-flash-google-reminds-everyone-its-still-in-the-race/5294049)、[TechTimes: Microsoft Build 2026: MAI-Thinking-1 Is First In-House Reasoning Model](https://www.techtimes.com/articles/317631/20260602/microsoft-build-2026-mai-thinking-1-first-house-reasoning-model-trained-without-openai-data.htm)、[DataCenterKnowledge: Amazon Lifts 2026 AI Capex to $220B](https://www.datacenterknowledge.com/infrastructure/amazon-lifts-ai-infrastructure-spending-to-220b-as-demand-outpaces-capacity)、[GeekWire: Amazon invests $50B in OpenAI, deepens AWS partnership with expanded $100B cloud deal](https://www.geekwire.com/2026/amazon-invests-50b-in-openai-deepens-aws-partnership-with-expanded-100b-cloud-deal/)、[Yahoo Finance: Meta cutting 600 AI jobs even as it continues to hire more for its superintelligence lab](https://finance.yahoo.com/news/meta-cutting-600-ai-jobs-174547660.html)、[Meta: Upcoming changes to Llama API](https://llama.developer.meta.com/docs/llama-api-deprecation/)、[Bloomberg: SpaceX Completes $60 Billion Cursor Acquisition](https://www.bloomberg.com/news/articles/2026-08-14/spacex-completes-its-60-billion-cursor-acquisition/)、[Axios: Scoop: Musk's SpaceXAI releases new model, Grok 4.5](https://www.axios.com/2026/07/08/spacexai-grok-new-model)、[GeoToolbox: Grok 5: Release Date, Specs & What's Confirmed](https://geotoolbox.ai/blog/grok-5)(いずれも[生成AI業界の主要プレイヤーと動向](../part13-ai-trends/ai-industry-major-players-trends.md)で確認済み)
