---
title: 中国発の基盤モデル企業一覧
part: 17
chapter: 第1章 基盤モデル・フロンティアAI系
tags: [基盤モデル, LLM, DeepSeek, Alibaba, Qwen, Moonshot AI, Zhipu AI, 中国]
created: 2026-09-20
updated: 2026-09-20
---

# 中国発の基盤モデル企業一覧

## このカテゴリについて

米国・欧州企業とは別に、中国発で独自の基盤モデル(LLM)を開発する主要企業を一覧する。
オープンウェイト(重みを無償公開する)モデルを軸に低コスト・高性能を打ち出す点と、
香港証券取引所への上場(IPO)を軸にした資金調達が急速に進んでいる点が共通の特徴。
企業としての立ち位置・資金調達・戦略に絞ってまとめ、モデルの技術的な仕組みそのものは
[モデルの種類と選び方](../part02-llm-basics/model-types-and-selection-basics.md)を参照。
米中間の技術規制・地政学リスクは
[生成AIの規制・ガバナンス動向](../part04-risk-security/ai-regulation-and-governance-trends.md)
と[日本における生成AI動向](../part13-ai-trends/japan-generative-ai-landscape.md)も合わせて参照。

## 企業一覧

### DeepSeek

- **一言で**: 2025年初頭に低コスト・高性能モデルで世界的に注目を集めた、杭州拠点のヘッジファンド系AI企業。
- **代表プロダクト・サービス**: 低コスト高性能モデル「DeepSeek-V4」シリーズ(最新は「V4 Flash」)。
- **特徴・強み**: 創業以来、外部からの資金調達を行わず親会社(ヘッジファンドHigh-Flyer)の資金で運営してきたが、2026年5月に初の外部調達となるシリーズAで70億ドルを調達し評価額520億ドルに到達。その後も評価額の急上昇が続き、2026年6月に500億ドル、7月に710億ドル(前月比約42%増)、8月には評価額約740億ドルで追加の80億ドル調達ラウンドを再開したと報じられている。中国本土での新規株式公開(IPO)に向けた準備も進めており、会計士・証券会社との協議を開始、2026年末〜2027年初頭の申請を目指すとされる。
- **料金の目安**: API料金は[DeepSeek公式サイト](https://www.deepseek.com/)を参照(低価格帯を強みとする)。
- **最終確認日**: 2026-09-20

### Alibaba(Qwenチーム)

- **一言で**: ECサイト大手Alibaba傘下で、オープンウェイトモデル「Qwen」シリーズを展開し累計ダウンロード数で世界最大級のシェアを持つ基盤モデル開発チーム。
- **代表プロダクト・サービス**: 最新フラッグシップ「Qwen3.8-Max」(総パラメータ2.4兆・活性化950億)、軽量版「Qwen3.8-Flash」「Qwen3.8-27B」。
- **特徴・強み**: 2026年8月に投入したQwen3.8-Maxはこの規模で初めてオープンウェイト公開されたモデルで、性能はOpenAI・Anthropicのモデルと競合水準とされる。Qwenシリーズの累計公開モデル数は460超、派生モデルは30万件超に達し、累計ダウンロード数は2026年8月時点で30億件を突破しMeta・Googleの公開モデルを上回った。一方で事業モデルにも変化があり、大規模商用利用者(年間5,000万ドル超の収益を生むケース)に対しては次期オープンウェイトモデルで収益分配(レベニューシェア)契約を求める方針を発表しており、「無償公開」から「大口利用者には対価を求める」段階的なマネタイズへ転換しつつある。
- **料金の目安**: セルフホストは無償(オープンウェイト)、Alibaba Cloud経由のAPI利用は従量課金。詳細は[Alibaba Cloud公式サイト](https://www.alibabacloud.com/)を参照。
- **最終確認日**: 2026-09-20

### Moonshot AI(Kimi)

- **一言で**: 2026年7月投入の「Kimi K3」が主要コーディングベンチマークでOpenAI・Anthropic製モデルを上回ったことで評価額が急騰した、北京拠点のAIスタートアップ。
- **代表プロダクト・サービス**: 対話AI「Kimi」、オープンウェイトの大規模モデル「Kimi K3」(2.8兆パラメータ)。
- **特徴・強み**: 評価額は2025年末の43億ドルから、2026年2月に100億ドル、5月のシリーズDで200億ドル超、Kimi K3投入後の7月には350億ドルへ急上昇。ARR(年換算売上高)はKimi K3投入からわずか2か月で2億ドルから3億ドルへ拡大した。香港証券取引所へのIPOに向けて非公開で申請を行い、調達目標額は約30億ドル、直前の資金調達ラウンドでの想定評価額は最大500億ドル規模と報じられている。
- **料金の目安**: API料金は[Moonshot AI公式サイト](https://www.moonshot.ai/)を参照。
- **最終確認日**: 2026-09-20

### Zhipu AI(Z.ai)

- **一言で**: 清華大学発、2026年1月に世界初の「基盤モデル企業単体」として香港証券取引所に上場した中国のAI企業。
- **代表プロダクト・サービス**: 大規模言語モデル「GLM」シリーズ、対話サービス「Z.ai」。
- **特徴・強み**: 2026年1月8日、香港証券取引所に上場し評価額約66億ドル・調達額約5.58億ドルを記録(基盤モデル企業単体としては世界初のIPOとされる)。上場後は株価が急騰し、2026年6月末〜7月初旬には時価総額が一時1,250億〜1,370億ドル超に達したのち調整が入り、9月11日終値時点では約470億ドルとなっている。2026年7月には香港市場で約40億ドル規模の追加株式売出しも実施した。
- **料金の目安**: API料金は[Zhipu AI公式サイト](https://www.zhipuai.cn/)を参照。
- **最終確認日**: 2026-09-20

## 関連トピック

- [海外の主要基盤モデル企業一覧(フロンティアAI企業)](foundation-model-companies-overseas.md)
- [欧州発の新興基盤モデル企業一覧](emerging-foundation-model-companies-europe-overseas.md)
- [生成AI業界の主要プレイヤーと動向(資金調達・提携・戦略)](../part13-ai-trends/ai-industry-major-players-trends.md)
- [モデルの種類と選び方(マルチモーダル・パラメータ数・SLM・VLM)](../part02-llm-basics/model-types-and-selection-basics.md)
- [オープンソースAIモデルのライセンス比較(商用利用時の論点)](../part08-specialized-ai-tools/open-source-model-license-comparison.md)

## 更新履歴

### 2026-09-20: 初版執筆
- **内容**: DeepSeek・Alibaba(Qwen)・Moonshot AI(Kimi)・Zhipu AI(Z.ai)の4社について、企業としての立ち位置・資金調達・IPO動向をまとめた。オープンウェイト戦略を軸にした急成長と、香港市場への相次ぐ上場・資金調達の動きを中心に整理した
- **出典**: [Bloomberg: DeepSeek's $8 Billion Fundraising Reopens, Valuation Nears $74 Billion](https://www.bloomberg.com/news/articles/2026-08-06/deepseek-resumes-8-billion-round-with-monolith-in-the-running)、[KuCoin: DeepSeek Eyes 2026 IPO Filing After $7B Funding Round](https://www.kucoin.com/news/flash/deepseek-eyes-2026-ipo-filing-after-7b-funding-round)、[Fortune: Alibaba AI models hit 3 billion downloads, passing Meta, Google](https://fortune.com/2026/08/15/alibaba-qwen-open-ai-models-3-billion-downloads-meta-google/)、[TechNode: Alibaba's Qwen to open-source Qwen3.8-Flash-Next](https://technode.com/2026/08/26/alibabas-qwen-to-open-source-qwen3-8-flash-next-previewing-qwen4-architecture/)、[thenextweb.com: Alibaba wants to charge the biggest users of its 'open' AI model](https://thenextweb.com/news/alibaba-charge-big-users-open-source-qwen)、[Bloomberg: China's Moonshot AI passes funding goal to hit $35 billion value](https://www.bloomberg.com/news/articles/2026-07-29/china-s-moonshot-ai-passes-funding-goal-to-hit-35-billion-value)、[SCMP: Kimi K3 developer Moonshot AI expedites fundraising ahead of planned IPO](https://www.scmp.com/tech/tech-trends/article/3361415/kimi-k3-developer-moonshot-ai-expedites-fundraising-ahead-planned-ipo-source-says)、[Turing Post: Zhipu AI (Z.ai): Founders, GLM Models, and Hong Kong IPO](https://www.turingpost.com/p/zhipu)
