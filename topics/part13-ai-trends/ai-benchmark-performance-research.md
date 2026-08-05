---
title: "生成AIは人間をどこまで超えたか:主要ベンチマークで見る到達点と限界(2026年時点)"
part: 13
chapter: 第1章 技術トレンド
tags: [ベンチマーク, MMLU, ARC-AGI, FrontierMath, HLE, IMO, SWE-bench, モデル動向]
created: 2026-07-11
updated: 2026-08-03
---

# 生成AIは人間をどこまで超えたか:主要ベンチマークで見る到達点と限界(2026年時点)

## これは何か

「生成AIが人間の専門家を超えた」という見出しは2024年以降ほぼ毎月のように登場するが、
分野によって「圧倒的に超えている」「わずかに超えた」「まだ大きく劣る」がまったく違う。
記事や社内説明でこの手の見出しを引用する際、根拠となるベンチマーク(能力を測る共通テスト)の
性質を知らずに数字だけを転記すると、誇張や誤りをそのまま広めることになりかねない。
本ページは、知識・数学・コーディング・資格試験・科学的発見・自律エージェント能力といった
主要な指標で生成AIがどこまで到達し、どこでまだ人間に及ばないのかを整理し、
これらの数字を記事や社内資料で引用する際に確認すべき注意点をまとめる。

**本ページは2026年8月時点のスナップショットであり、スコアは数か月単位で更新される。**
[生成AIの最新モデル動向](ai-model-trends-basics.md)が「新モデルに乗り換えるべきか」という
実務判断のためのページであるのに対し、本ページは「AIの能力向上そのものをどう理解し、
どう引用するか」に焦点を当てる。

## 仕組み・背景

### 「人間を超えた」を測る6つの物差し

| カテゴリ | 代表的な指標 | 何を測るか |
|---|---|---|
| 学術ベンチマーク | MMLU-Pro、GPQA Diamond、ARC-AGI、FrontierMath、HLE | 知識・専門知識・抽象推論・研究レベル数学 |
| 競技・大会 | IMO(国際数学オリンピック)、Codeforces、ICPC | 数学・競技プログラミングの人間トップ層との比較 |
| 資格・専門家試験 | 司法試験、LSAT、USMLE(医師国家試験) | 実在の資格試験での合格ライン・偏差値相当 |
| 科学的発見 | AlphaFold、AlphaEvolve、GNoME | 実際の未解決問題を解いた・新発見をしたか |
| コーディング実務 | SWE-bench Verified/Pro、Terminal-Bench 2.1 | 実際のGitHub issueやターミナル操作をどれだけ自力で片付けられるか |
| 自律エージェント性能 | METR Time Horizon | 人間の助けなしにどれだけ長い作業をやり切れるか(タイムホライゾン) |

2026年に入って新たに実務上の定番になったのが「コーディング実務」の**Terminal-Bench**と
「自律エージェント性能」の**METR Time Horizon**。前者はSWE-bench同様のコード修正ではなく、
ターミナル操作を伴う一連のエンジニア作業(ビルド・調査・デバッグ等)を評価し、
後者は「50%の成功率で自律的にやり切れる作業時間の長さ」を継続測定する指標で、
単発の正答率では見えない「どれだけ長く任せて放置できるか」を示す。

### 到達点(2026年8月時点)

| ベンチマーク | 人間基準 | AIの到達点 | 到達した時期 |
|---|---|---|---|
| MMLU(57科目の知識) | 専門家89.8% | Gemini Ultraが90.04%で初めて超えた(2023/12)。以後は上位モデルが軒並み88〜90%台に達し完全に飽和 | 2023年 |
| GPQA Diamond(博士レベル科学) | PhD専門家65〜70% | OpenAI o1が77.3%で初超え(2024/09)。2026年8月時点ではGemini 3.1 Pro Preview・GPT-5.6 Solがともに94%前後、Claude Opus 5・Claude Fable 5も93%台で、上位モデル間の差は1〜2ポイントまで縮小(実質飽和) | 2024〜2026年 |
| FrontierMath(研究者レベル数学) | ―(公開当初は最先端AIでも2%未満) | Epoch AIが2026年6月に「v2(Tier4)」へ全面切り替え(旧版は監査で問題の42%に誤りが判明したため)。新版でGPT-5.6 Solがトップ(Tier4で約83%、総合スコア0.890)、Claude Fable 5が僅差で続く | 2024〜2026年で急伸、指標自体は2026年6月に刷新 |
| ARC-AGI-2(未知パターンへの抽象推論) | 人間平均66% | GPT-5.6 Solが92.5%、Claude Opus 5が90.4%、GPT-5.5が85%(2026年7月時点)。人間平均は上回ったが、これは「上位人間層」ではなく「平均的な受験者」基準である点に注意 | 人間平均を超過(2026年) |
| ARC-AGI-3(対話型・より難化) | 人間ほぼ100% | 最高でもClaude Opus 5の30.2%(2026年3月時点のOpus 4.6は0.5%程度だったため急伸)。GPT-5.6 Solは7.8%にとどまり、モデル間の差も非常に大きい | 大きく未到達だが急速に縮まりつつある |
| Humanity's Last Exam(超高難度・全分野) | 専門家目安90%程度 | Claude Fable 5が53.3%で最高値、GPT-5.6 Solが47.2%、Claude Opus 4.8が45.7%(2026年7月時点) | 未到達 |
| SWE-bench(実務コーディング) | ― | Verifiedは2026年もOpenAIが評価対象から除外したまま(汚染により無効化)。汚染耐性の高いSWE-bench Proでは、ベンダー発表値でClaude Mythos 5が80.3%・Claude Fable 5が80%・Claude Opus 5が79.2%だが、Scale AIが運営する標準化された公開セットではGPT-5.4(xHigh)が59.1%(2026年6月時点)と大きく異なる | 指標自体が2026年に切り替わり、評価環境差も拡大 |
| Terminal-Bench 2.1(ターミナル操作を伴う実務コーディング) | ― | GPT-5.6 Sol(xhigh)が89.5%、Claude Opus 5(max)が89.1%(2026年7月時点)。ICLR 2026掲載の研究発端で、2026年にエージェント評価の標準的な参照先として定着 | 2026年に定番指標化 |
| IMO(国際数学オリンピック) | 金メダル35/42点、満点42点(2026年は666人中満点7人のみ) | 2025年はGoogle DeepMindのGemini Deep ThinkがIMO公式に金メダル相当と認定。2026年大会(7月10〜21日、上海)では、HuaweiのAIモデル「Celia」とXiaohongshu(小紅書)の「dots-note 3.0」がIMO運営自身の採点で満点42/42を取得。これはAIが公式採点で満点を取った初の事例 | 2025年に金メダル相当、2026年に満点達成 |
| METR Time Horizon(自律作業時間) | ― | 2019〜2025年平均で7か月ごとに倍増していたが、2024〜2025年は4か月ごとの倍増に加速。Claude Opus 4.6の「50%成功率で完遂できる作業時間」は約12時間(2026年1月にタスク体系をTH1.1へ刷新後の値) | 加速中 |

この表からわかる通り、「知識を問う」「決まったパターンを当てはめる」領域(MMLU、GPQA、数学オリンピック)では
すでに人間の専門家を超えているか、僅差まで迫っている一方、「見たことのないパターンに対話的に適応する」
領域(ARC-AGI-2/3)では依然として大きな差が残る。ARC-AGI-2は2026年に人間平均を上回ったが、
より難化したARC-AGI-3ではトップモデルでも30%程度にとどまる。ARC Prizeの創設者François Cholletは
「高スコアモデルでも、人間には非常に簡単なタスクで失敗し続ける」と指摘しており、
単一の「AI IQ」のような総合順位では捉えきれない凹凸がある。

## 使いどころ・使い分け

### この種の数字を引用してよい場面・避けるべき場面

| 場面 | 判断 | 理由 |
|---|---|---|
| 記事で「AIの進歩の速さ」を示す事例として引用 | ◯ | 「2024年に2%未満だった指標が2年で90%近くまで伸びた」という**変化の速度**は再現性のある事実 |
| 「このベンチマークで1位だから業務にも最適」と結論づける | ✕ | ベンチマークは特定タスクの成績であり、自社データでの検証なしに実務適性は判断できない([生成AIの最新モデル動向](ai-model-trends-basics.md)の乗り換え判断チェックリスト参照) |
| 「AIはもう医師・弁護士に取って代わる」の根拠として単独引用 | ✕ | 資格試験のスコアは知識問題の再現力であり、臨床判断・対人交渉・責任所在などの実務要素を測っていない |
| ベンダー自身の発表スコアをそのまま「客観的な世界記録」として記載 | △ | 自己申告スコアは独立評価機関(Artificial Analysis、Epoch AI、ARC Prizeなど)の値と乖離することがあるため、可能な限り併記する |
| 「同じベンチマーク名」だからと異なる情報源のスコアを単純比較する | ✕ | SWE-bench Proのように、評価環境(エージェントの足回り=スキャフォールディング)次第で同一モデルでも10〜20ポイント動く指標がある。情報源(ベンダー発表か、標準化された第三者測定か)を必ず揃える |

### 「人間超え」の粒度を区別する

- **飽和した指標**(MMLU、GPQA Diamond等): 上位モデル同士の差が誤差レベルまで縮まっており、「1位」を強調する意味が薄い
- **急伸中の指標**(FrontierMath、ARC-AGI-3): 半年〜1年単位でスコアが大きく動くため、記事化する際は測定時期を必ず明記する
- **依然として大きな差が残る指標**(ARC-AGI-3): 「AIは万能」という論調へのカウンターとして使える
- **採点主体が公式か自己申告かを区別する**: 2026年のIMOでは、Huawei・Xiaohongshuの満点はIMO運営自身が公式採点した一方、同時期に「別の投資家が独自に実施しClaude系エージェントに採点させた」非公式テストでも複数モデルが満点相当と報告された。同じ「IMOで満点」でも採点の権威づけが全く違うため、記事化する際は必ず区別する

## 実務での使い方

### 記事・資料への引用テンプレート

コピペしてベンチマーク数字を記事や資料に落とし込む際は、以下の4点を必ずセットで書く。

```
[ベンチマーク名]で[モデル名]が[スコア]を記録(測定:[年月]、出典:[評価機関名])
※人間基準:[基準値]/[出典]
※自己申告か独立評価かの別:[ベンダー発表 / 第三者評価(Artificial Analysis等) / 公式採点(IMO運営等)]
```

### 最新スコアの一次情報源(定点観測先)

| 情報源 | 特徴 |
|---|---|
| [Artificial Analysis](https://artificialanalysis.ai/) | 複数モデルのベンチマークを独立測定し横並びで公開。合成指標「Intelligence Index」(2026年8月時点、Claude Opus 5が167モデル中トップ)や「Agentic Index」も提供 |
| [Epoch AI](https://epoch.ai/) | FrontierMathなど研究レベルベンチマークの独立運営元。汚染対策(非公開問題)に積極的で、2026年6月にv2へ刷新済み |
| [ARC Prize](https://arcprize.org/) | ARC-AGIシリーズの公式運営。人間ベースラインとの比較や「まだ解けないタスク」の分析を公開 |
| [METR](https://metr.org/) | AIエージェントが自律的にやり切れる作業時間の長さ(タイムホライゾン)を測定。2026年1月にTH1.1へ改訂 |
| [IMO公式サイト](https://www.imo-official.org/) | 国際数学オリンピックの公式結果・採点情報。AIの成績が「公式採点」か「ベンダー・第三者の自己申告」かを確認する一次情報源 |

### 数字を記事化する際のチェック手順

1. スコアの発表元が**ベンダー自身か第三者評価機関・公式運営か**を確認する
2. **測定時期**を明記する(数か月で数値が大きく動くため)
3. 「人間基準」がどう定義されているか(平均受験者か、専門家平均か、トップ層か)を確認する
4. データ汚染(ベンチマークの正解が学習データに混入)の指摘がないか、該当ベンチマークの運営元発表を確認する
5. 同じベンチマーク名でも評価環境(スキャフォールディング)の違いで数値が動くケースがないか確認する(SWE-bench Proが典型例)

## 注意点・よくある誤解

- **自己申告スコアの偏り**: SWE-bench Verifiedの例のように、ベンダー自身が公表するスコアは独立評価より高く出る傾向がある。2026年、OpenAIはSWE-bench Verifiedの失敗ケースの約6割がテスト自体の欠陥であり、かつ主要フロンティアモデルに学習データ汚染があったことを認め、以後は汚染に強いSWE-bench Proへの移行を推奨した。SWE-bench Proでも、ベンダー発表値(70〜80%台)とScale AIの標準化された公開セットでの測定値(50〜60%台)には大きな開きがある
- **「同じベンチマークで満点」でも採点の権威づけは別物**: 2026年のIMOでHuawei・Xiaohongshuが獲得した満点42/42はIMO運営自身が公式採点したものだが、同時期に複数のモデルが「満点相当」と報告された別の非公式テストは、投資家が独自に用意しClaude系エージェントに採点させたものだった。「AIがIMOで満点」という見出しだけを見て、採点主体を確認しないまま引用しないこと
- **「専門家超え」の再評価**: GPT-4の司法試験スコアは当初「上位90パーセンタイル」と発表されたが、MIT研究者らの再評価により、実際は7月受験者全体で約68位、弁護士との比較では約48位相当と大幅に下方修正された。ベンダーの一次発表を鵜呑みにせず、独立検証の有無を確認する
- **科学的発見の成果にも訂正例がある**: DeepMindのGNoME(新結晶構造探索AI)が発見したとされた安定材料の一部は、2025年後半に「既知構造との重複」を理由とした撤回要求が学術誌に提出されている。「AIが新発見をした」という成果発表も、事後の検証で見直されることがある
- **飽和したベンチマークでの僅差比較は無意味に近い**: MMLUやGPQA Diamondのように上位モデルが軒並み90%台に達した指標では、1〜2ポイントの差を「業界トップ」の根拠にするのは誤解を招く
- **ARC-AGIの急伸と急落は今も続く**: OpenAI o3はARC-AGI-1で87.5%(人間基準を超過)に達したが、より難化したARC-AGI-2では当初3%未満まで急落した(2026年は上位モデルが人間平均を超えるまで急伸)。さらに難化したARC-AGI-3ではトップでも30%程度と、シリーズが更新されるたびに「人間超え」の位置づけがリセットされる。「1つのベンチマークで人間を超えた」ことは、次の版・他のベンチマークでも同様に人間を超えたことを意味しない
- **「◯◯ベンチで1位」の情報源アグリゲーターは玉石混淆**: BenchLM.aiやllm-stats.comのような非公式の集計サイトは速報性は高いが、算出方法の記載が薄いことがある。数字を確定情報として引用する際は、可能な限り運営元(Artificial Analysis、Epoch AI、ARC Prize、METR、IMO公式)の一次情報に当たる

## 最初の一歩

記事や資料で「AIが人間を超えた」という数字を引用する前に、まず発表元が
ベンダー自身か独立評価機関・公式運営(Artificial Analysis、Epoch AI、ARC Prize、IMO公式など)かを1つ確認する習慣をつける。

## 関連トピック

- [生成AIの最新モデル動向(2026年:主要モデルの進化とベンチマークの見方)](ai-model-trends-basics.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [生成AI業界の主要プレイヤーと動向(資金調達・提携・戦略)](ai-industry-major-players-trends.md)
- [AIプロジェクトの進め方と評価指標の基礎](../part01-ai-basics/ai-project-and-evaluation-basics.md)

## 更新履歴

### 2026-08-03: 主要ベンチマークのスコアを2026年8月時点に最新化
- **内容**: Claude Opus 5・Claude Fable 5/Mythos 5・GPT-5.6(Sol/Terra/Luna)・Gemini 3.1 Pro Previewなど新世代モデルのスコアに全面更新。GPQA Diamondが実質飽和(上位モデルが93〜95%で団子状態)したこと、FrontierMathがv2(Tier4)へ刷新されたこと、ARC-AGI-2が人間平均を超えた一方でARC-AGI-3は依然30%程度にとどまること、SWE-bench Proでベンダー発表値と標準化測定値に大きな開きがあることを反映。2026年7月のIMO本大会でHuawei・Xiaohongshuのモデルが公式採点で満点42/42を達成した事例(非公式な満点報告との違いを含む)を追加。新たに定番化したTerminal-Bench 2.1・METR Time Horizon・Artificial Analysis Intelligence Indexを指標一覧に追加
- **出典**: [BenchLM.ai: ARC-AGI-2 Leaderboard (July 2026)](https://benchlm.ai/benchmarks/arcAgi2)、[BenchLM.ai: ARC-AGI-3 Leaderboard (July 2026)](https://benchlm.ai/benchmarks/arcagi3)、[ARC Prize: ARC-AGI-3 Human Leaderboard](https://arcprize.org/arc-agi/3/leaderboard)、[Artificial Analysis: GPQA Diamond Benchmark Leaderboard](https://artificialanalysis.ai/evaluations/gpqa-diamond)、[Epoch AI: FrontierMath Tier 4 (v2)](https://epoch.ai/benchmarks/frontiermath-tier-4-v2)、[BenchLM.ai: Humanity's Last Exam Leaderboard](https://pricepertoken.com/leaderboards/benchmark/hle)、[OpenAI: Why we no longer evaluate SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)、[morphllm.com: SWE-bench Pro Leaderboard (2026)](https://www.morphllm.com/swe-bench-pro)、[digitalapplied.com: SWE-bench in 2026: Benchmarks vs Scaffolding Reality](https://www.digitalapplied.com/blog/swe-bench-verified-june-2026-benchmark-vs-scaffolding-analysis)、[Snorkel AI: Terminal-Bench 2.1](https://snorkel.ai/leaderboard/terminal-bench-2-1/)、[METR: Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/)、[techxplore.com: AI catches up with humans to score 100% at top math contest](https://techxplore.com/news/2026-07-ai-humans-score-math-contest.html)、[digitalapplied.com: Four AIs Scored a Perfect 42/42 on IMO 2026. So What?](https://www.digitalapplied.com/blog/imo-2026-perfect-scores-ai-benchmark-saturation)、[Malay Mail: Huawei, Xiaohongshu AI storm Olympiad, join maths elite with perfect 100pc score](https://www.malaymail.com/amp/news/tech-gadgets/2026/07/23/huawei-xiaohongshu-ai-storm-olympiad-join-maths-elite-with-perfect-100pc-score/228720)、[IMO official: IMO 2026 Concludes in Shanghai](https://www.imo-official.org/news/imo-2026-concludes-in-shanghai/)、[TechCrunch: OpenAI launches its new family of models with GPT-5.6](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)、[Axios: Anthropic releases new model, Opus 5](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5)、[BenchLM.ai: Artificial Analysis Intelligence Index Leaderboard (August 2026)](https://benchlm.ai/benchmarks/artificialanalysis)

### 2026-07-11: 初版執筆(教材ページとして再構成)
- **内容**: 社内に残っていた未整形のベンチマーク調査メモ(2026-07-06時点の3本のDeep Researchレポートのマージ)を、教材ページの型(これは何か/使いどころ/実務での使い方/注意点)に沿って再構成。HLE・ARC-AGI-2/3・FrontierMath・SWE-bench・IMOの最新スコアを2026年7月時点で再検証し、独立評価機関の情報源一覧と、記事化する際の引用チェック手順を追加
- **出典**: [pricepertoken.com: Humanity's Last Exam Leaderboard 2026](https://pricepertoken.com/leaderboards/benchmark/hle)、[BenchLM.ai: ARC-AGI-2 Benchmark 2026](https://benchlm.ai/benchmarks/arcAgi2)、[ARC Prize: ARC-AGI-3 Human Leaderboard](https://arcprize.org/arc-agi/3/leaderboard)、[Epoch AI: FrontierMath Tier 4 (v2)](https://epoch.ai/benchmarks/frontiermath-tier-4-v2)、[the-decoder.com: Claude Fable 5 outpaces GPT-5.5 by 13 points on FrontierMath's toughest problems](https://the-decoder.com/claude-fable-5-outpaces-gpt-5-5-by-13-points-on-frontiermaths-toughest-problems/)、[OpenAI: Why we no longer evaluate SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)、[blockchain.news: OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)、[Google DeepMind: Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the IMO](https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)、[Polymarket: AI wins IMO gold medal in 2026?](https://polymarket.com/event/ai-wins-imo-gold-medal-in-2026)、[Scientific American: Mathematicians Question AI Performance at International Math Olympiad](https://www.scientificamerican.com/article/mathematicians-question-ai-performance-at-international-math-olympiad/)
