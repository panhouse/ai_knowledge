---
title: "オープンソースAIモデルのライセンス比較(商用利用時の論点)"
part: 8
chapter: 第4章 ローカル・オープンモデル
tags: [オープンソース, オープンウェイト, ライセンス, Llama, Gemma, Mistral, Apache 2.0, MIT, 法務]
created: 2026-07-25
updated: 2026-07-25
---

# オープンソースAIモデルのライセンス比較(商用利用時の論点)

## これは何か

Llama・Gemma・Mistral・Qwen・DeepSeekなど、重みが公開され自社で動かせる「オープンウェイトモデル」は増えているが、そのライセンス条件はモデルごとにまったく異なり、「無料で公開されている=何をしても自由」ではない。自社サービスに組み込む・ファインチューニングして再配布する・生成物を販売するといった商用利用の場面では、再配布の条件、利用者数の閾値、商標・命名規則、生成物の責任範囲などをモデルごとに確認しないと、契約違反や訴訟リスクを抱えたまま事業を進めてしまうことになる。本ページは、モデル別の早見表([ローカルLLMの基本](./local-llm-basics.md)に既出)を繰り返すのではなく、**商用利用を検討する法務・調達担当者が実際に確認すべき論点**を横断的に整理する。

## 仕組み・背景

### 「オープンウェイト」と「オープンソース」は別物

- **オープンウェイト(open weight)**: 学習済みモデルの「重み」(パラメータの数値データ)だけが公開されている状態。ダウンロードして推論(実行)やファインチューニング(追加学習によるカスタマイズ)はできるが、学習に使ったデータセットや学習用コードは非公開のことが多く、モデルを"再現"することはできない
- **オープンソース(open source)**: 従来のソフトウェアの意味での「オープンソース」。重みに加えて、学習コード・十分な学習データの情報まで公開され、第三者がゼロから再構築・監査できる状態を指す

業界団体OSI(Open Source Initiative、オープンソースの定義を策定する非営利団体)は2024年に「Open Source AI Definition(オープンソースAIの定義)」を公表し、**重みの公開だけではオープンソースと呼べない**という立場を明確にしている。この定義に照らすと、Llama・Gemma・DeepSeek・Qwenなど「オープンソース」を名乗ることが多いモデルの大半は、実際には学習データ・学習コードが非公開の「オープンウェイト」に分類される。マーケティング上の呼称と、法務・調達で確認すべき実態(ライセンス条文)は切り分けて考える必要がある。OSIは2026年内にこの定義の改訂(1.1〜2.0)を予定しており、今後「オープンソースAI」の線引きがさらに厳密になる可能性がある。

### ライセンスの3系統

主要なオープンウェイトモデルのライセンスは、おおむね次の3系統に分類できる。

1. **標準的なOSS(オープンソースソフトウェア)ライセンスをそのまま適用**: Apache 2.0、MIT。ソフトウェア業界で広く使われてきた実績のあるライセンスをそのままモデルの重みに適用しており、商用利用・改変・再配布に関する制限が最も少ない
2. **独自のコミュニティライセンス(利用者数などの閾値条項付き)**: Llama Community License、Tongyi Qianwen License(Qwen)など。無料利用の枠を大きく取りつつ、一定規模を超える事業者には別途契約を求める「フリーミアム型」の設計
3. **利用規約(Terms of Use)+行為規範(Acceptable Use Policy)の組み合わせ**: Gemma Terms of Use、Gemma Prohibited Use Policyなど。ライセンス自体はApache 2.0に近い体裁でも、別建ての行為規範・停止条項(Googleが違反と判断した場合に利用を差し止められる条項)が付随し、実質的な自由度は下がる

## 使いどころ・使い分け

### 主要ライセンスの横並び比較

| ライセンス | 採用モデルの例 | 商用利用 | 再配布・派生モデルの条件 | 利用者数などの閾値条項 | 商標・命名の制約 |
|---|---|---|---|---|---|
| Apache 2.0 | Gemma(4以降)、Mistral(Large 3/Small 4等の主力モデル)、Qwen(小型モデル中心)、gpt-oss | 可(制限なし) | 著作権表示・変更点の明示のみ。特許の明示的な利用許諾(特許訴訟を起こされた場合に自身の特許ライセンスが失効する条項)あり | なし | なし(モデル名の変更も自由) |
| MIT | DeepSeek(V3・R1・V4系)、GLM、Kimi | 可(制限なし) | 著作権表示の保持のみ。Apache 2.0と異なり特許に関する明示的な取り決めがない | なし | なし |
| Llama Community License(独自) | Llama 3系・Llama 4系 | 条件付きで可 | 派生モデルの名称冒頭に「Llama」を含める義務、製品・サービスに"Built with Llama"の表示義務、ライセンス全文の同梱義務 | 前月の月間アクティブユーザー(MAU)が7億人を超える場合は別途Metaとの契約が必要 | 「Llama」の使用はこの命名義務の範囲に限定。商標権はMetaに帰属し、生じた信用(グッドウィル)もMetaのものになる |
| Tongyi Qianwen License(独自、Qwen大型モデル向け) | Qwen(大型モデルの一部) | 条件付きで可 | 重みの再ライセンス禁止、再配布時の条件あり | 月間アクティブユーザーが1億人を超える場合はAlibaba Cloudへのライセンス申請が必要 | モデル名に関する制約あり(要契約確認) |
| Gemma利用規約+禁止行為ポリシー | Gemma(3以前の一部) | 条件付きで可 | ライセンス条文自体はApache 2.0に近いが、別立ての「禁止行為ポリシー」への継続的な遵守義務が全ての再配布先に引き継がれる(フローダウン義務) | 明示的な数値閾値はないが、Googleが違反と判断すれば一方的に利用停止できる条項がある | Googleの商標は不使用が前提 |

**判断基準の目安**

- **社内向けPoC(概念実証)・小規模な検証段階**: どのライセンスでも実質的な支障は出にくい。ただしAPI提供や外部公開を見据えるなら、この段階からライセンス条文を確認しておく
- **自社サービスに組み込んで外部提供する(SaaS化・API提供)**: Apache 2.0 / MITのモデル(Mistral主力モデル、gpt-oss、DeepSeek、GLM、Kimi等)を優先候補にする。Llama系・Qwen大型モデルを使う場合は、自社サービスの想定MAUが閾値(Llamaは7億人、Qwen大型モデルは1億人)を超える見込みがないかを事業計画側と必ずすり合わせる
- **ファインチューニングした派生モデルを他社に再配布・販売する**: Llama系は「Llama」を名称冒頭に含める義務があるため、自社ブランドのモデルとして展開したい場合はブランディング上の制約になる。この制約を避けたい場合はApache 2.0 / MIT系のベースモデルを選ぶ
- **生成物(アウトプット)の権利関係を明確にしたい業務(コンテンツ制作・生成物の販売等)**: オープンウェイトモデルのライセンスは、そもそも生成物の著作権・利用権について明記していないことが多い(後述)。契約書や利用規約でのカバーが難しい場合は、生成物の権利関係を契約で明示する法人向けAPI(ChatGPT Enterprise、Claude for Enterprise等)の利用を優先する選択肢もある
- **社会的影響が大きい用途(医療診断支援、与信判断、採用選考等)**: Gemmaのように禁止行為ポリシーが付くライセンスでは、対象業務がポリシーの禁止事項に抵触しないか事前に確認する。禁止行為ポリシーは提供元の判断で改定されることがあるため、社内の利用規程に転記して終わりにせず、定期的に原文を確認する運用にする

## 実務での使い方

### 商用利用前に法務・調達がチェックすべき論点

1. **再配布(redistribution)の条件**: モデルそのもの、またはファインチューニング後の重みを社外(顧客・パートナー)に渡す場合、ライセンス全文の同梱義務、著作権表示の保持義務、変更点の明示義務があるかを確認する。Apache 2.0 / MITは形式的な条件のみだが、Llama系は前述の名称・表示義務が加わる
2. **派生モデル(derivative model)の扱い**: 「ファインチューニングしたら別物として自由に扱える」と誤解されがちだが、多くのライセンスは派生モデルにも元のライセンス条件を引き継がせる(フローダウン)設計になっている。特にLlama系は派生モデルの名称にも「Llama」を含めることを義務付けており、ファインチューニング後も元のライセンスから逃れられない
3. **利用者数・収益規模の閾値条項**: Llama(7億MAU超)、Qwen大型モデル(1億MAU超)のように、一定規模を超えると無償ライセンスの対象外になり、提供元との個別契約が必要になる条項がある。自社サービスが将来その規模に到達する可能性がある場合は、契約担当者があらかじめ提供元への確認ルートを把握しておく
4. **生成物(アウトプット)の著作権・責任範囲**: OpenAI・Anthropic・Google等の法人向けAPI利用規約は生成物の権利を利用者に帰属させる条項を置いていることが多いが、オープンウェイトモデルのライセンス(Apache 2.0・MIT・Llama Community License等)は生成物の権利関係に触れていないのが実情である。生成物の著作権・第三者権利侵害リスクへの対応は、モデルのライセンスではなく自社の利用規約・契約書側で手当てする必要がある(著作権全般の論点は[生成AIの著作権リスク](../part04-risk-security/copyright-risks-in-generative-ai.md)を参照)
5. **保証・責任の所在(indemnification / liability)**: Apache 2.0・MITはいずれも「無保証(AS IS)・責任制限」を明記しており、モデルの出力が誤っていた場合や第三者の権利を侵害した場合の補償を提供元に求めることはできない。むしろライセンス条文上は利用者側が提供元へ補償(リバース・インデムニティ)する形になっていることが多く、法人向けAPIのような手厚い補償条項は期待できない
6. **商標・命名規則の制約**: 「Llama」「Gemma」等のモデル名・ロゴは商標として保護されており、ライセンスが認める範囲(前述の命名義務等)を超えて自社製品名やロゴに使うことはできない。マーケティング資料・プレスリリースでの表記も、各社の「ブランドガイドライン」を確認してから作成する

### 確認の進め方(調達フロー)

1. Hugging Face上のモデルカードに記載されたライセンス名を確認する(例: `Apache-2.0`、`llama4`、`gemma`)
2. ライセンス名が独自ライセンス(コミュニティライセンス等)の場合は、モデル配布元(Meta・Alibaba等)の公式サイトでライセンス全文を確認し、閾値条項・再配布条件を洗い出す
3. 自社の利用形態(社内利用のみ/外部提供/再配布/派生モデルの販売)を上表の「使いどころ・使い分け」に照らし、リスクの大小を判断する
4. 判断に迷う場合(利用者数が閾値に近い、派生モデルを他社に販売する等)は、契約前に法務担当者・場合によっては弁護士へのライセンス条文レビューを依頼する

## 注意点・よくある誤解

- **「無料でダウンロードできる=商用利用も無条件で自由」ではない**: 前述のとおりLlama・Qwen大型モデルには利用者数の閾値条項があり、Gemmaには禁止行為ポリシーがある。「Apache 2.0やMITのモデルだけが無条件で自由」という点を混同しないこと
- **「オープンソース」という呼称を鵜呑みにしない**: 提供元が「オープンソース」と称していても、OSIの定義に照らせば学習データ・学習コードが非公開の「オープンウェイト」にすぎないケースが大半である。法務レビューでは呼称ではなくライセンス条文の実態を確認する
- **ファインチューニングすれば元のライセンスから解放される、というのは誤解**: 多くのライセンスは派生モデルにも元の条件を引き継がせる。「自社で追加学習したから完全に自社のものになった」と判断するのは危険で、特にLlama系は派生モデルの命名義務まで引き継ぐ
- **利用規約・禁止行為ポリシーは提供元の判断で改定されることがある**: Gemmaの禁止行為ポリシーのように、ライセンス本体とは別に運用される規約は、事前通知なく更新される場合がある。ライセンス条文を一度確認して終わりにせず、事業への影響が大きいモデルほど定期的に原文を再確認する運用にする
- **生成物の権利・責任はモデルのライセンスではカバーされない**: 「モデルが無保証だから生成物の著作権侵害リスクも自己責任」という点を利用者側(社内の現場担当者)が理解していないことが多い。社内の生成AI利用ガイドラインで、生成物の著作権チェック・第三者権利侵害の一次確認フローを別途整備する必要がある
- **モデル別の詳細な早見表は[ローカルLLMの基本](./local-llm-basics.md)を参照**: 本ページは論点の整理を目的としており、Llama・Gemma・Mistral・Qwen・DeepSeek等の個別モデルのライセンス名・特徴の一覧は重複させていない。最新のモデル別ライセンス状況は同ページの表を確認すること

## 最初の一歩

自社で採用中(または採用検討中)のオープンウェイトモデルを1つ選び、Hugging Face上のモデルカードに記載されたライセンス名をもとに配布元の公式ライセンス全文を開き、「再配布条件」「利用者数の閾値」の2点だけをまず確認してみる。

## 関連トピック

- [ローカルLLMの基本(自社PC・サーバーで動かす生成AI)](./local-llm-basics.md)
- [Hugging Faceの基本(AIモデル・データセットのハブ)](./huggingface-basics.md)
- [量子化(モデル軽量化)の基本](./quantization-basics.md)
- [生成AIの著作権リスク](../part04-risk-security/copyright-risks-in-generative-ai.md)

## 更新履歴

### 2026-07-25: 初版執筆
- **内容**: 「オープンウェイト」と「オープンソース」の定義の違い(OSIのOpen Source AI Definitionに基づく整理)、Apache 2.0/MIT/Llama Community License/Tongyi Qianwen License/Gemma利用規約の横並び比較表、商用利用時に法務・調達が確認すべき論点(再配布条件・派生モデルの扱い・利用者数閾値・生成物の著作権と責任範囲・商標命名規則)を整理。モデル別の詳細な早見表は既存の[ローカルLLMの基本](./local-llm-basics.md)に譲り、本ページでは重複させない方針を明記
- **出典**: [LLAMA 4 COMMUNITY LICENSE AGREEMENT - Meta](https://www.llama.com/llama4/license/)、[Meta Llama 3 and the 700M MAU Limit - WCR.LEGAL](https://wcr.legal/llama-3-license-700m-mau-limit/)、[You're Probably Breaking the Llama Community License](https://notes.victor.earth/youre-probably-breaking-the-llama-community-license/)、[Gemma Terms of Use - Google AI for Developers](https://ai.google.dev/gemma/terms)、[Gemma Prohibited Use Policy - Google AI for Developers](https://ai.google.dev/gemma/prohibited_use_policy)、[Google Gemma: The Hidden Risks of an "Almost Open" License - WCR.LEGAL](https://wcr.legal/google-gemma-license-risks/)、['Open' AI model licenses often carry concerning restrictions - TechCrunch](https://techcrunch.com/2025/03/14/open-ai-model-licenses-often-carry-concerning-restrictions/)、[What Is Open Source AI? A Practical 2026 Guide to OSAID - Moesif Blog](https://www.moesif.com/blog/technical/api-development/Open-Source-AI/)、[Open Weights vs Open Source: The Real Difference (2026) - GEO Toolbox](https://geotoolbox.ai/blog/open-weights-vs-open-source)、[Mistral Releases Apache 2.0 Open Source Leanstral 1.5 - Open Source For You](https://www.opensourceforu.com/2026/07/mistral-releases-apache-2-0-open-source-leanstral-1-5/)、[Mistral Versions - license terms per release - mungomash.com](https://mungomash.com/ai/mistral/versions/)、[Tongyi Qianwen LICENSE AGREEMENT - GitHub](https://github.com/QwenLM/Qwen/blob/main/Tongyi%20Qianwen%20LICENSE%20AGREEMENT)、[Open-Weight License Landscape 2026 - Presenc AI](https://presenc.ai/research/open-weight-license-landscape-2026)、[Open Source AI Versus Proprietary AI Models: Key Differences in Contract Terms and IP Risks - Hunton](https://www.hunton.com/insights/publications/open-source-ai-versus-proprietary-ai-models-key-differences-in-contract-terms-and-ip-risks-part-2)、[How AI Models Are Licensed: A Brief Guide for Founders and Product Managers - WCR.LEGAL](https://wcr.legal/ai-model-licensing-guide-for-founders/)、[OpenAI open-weight models (gpt-oss) - OpenAI Help Center](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss)、[Open Source AI Licenses [2026]: Apache 2.0 to RAIL Guide - QubitTool](https://qubittool.com/blog/open-source-ai-license-compliance-guide)
