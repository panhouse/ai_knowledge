---
title: "生成AIは人間をどこまで超えたか:主要ベンチマークで見る到達点と限界(2026年時点)"
part: 13
chapter: 第1章 技術トレンド
tags: [ベンチマーク, MMLU, ARC-AGI, FrontierMath, HLE, IMO, モデル動向]
created: 2026-07-11
updated: 2026-07-11
---

# 生成AIは人間をどこまで超えたか:主要ベンチマークで見る到達点と限界(2026年時点)

## これは何か

「生成AIが人間の専門家を超えた」という見出しは2024年以降ほぼ毎月のように登場するが、
分野によって「圧倒的に超えている」「わずかに超えた」「まだ大きく劣る」がまったく違う。
記事や社内説明でこの手の見出しを引用する際、根拠となるベンチマーク(能力を測る共通テスト)の
性質を知らずに数字だけを転記すると、誇張や誤りをそのまま広めることになりかねない。
本ページは、知識・数学・コーディング・資格試験・科学的発見・IQといった主要な指標で
生成AIがどこまで到達し、どこでまだ人間に及ばないのかを整理し、
これらの数字を記事や社内資料で引用する際に確認すべき注意点をまとめる。

**本ページは2026年7月時点のスナップショットであり、スコアは数か月単位で更新される。**
[生成AIの最新モデル動向](ai-model-trends-basics.md)が「新モデルに乗り換えるべきか」という
実務判断のためのページであるのに対し、本ページは「AIの能力向上そのものをどう理解し、
どう引用するか」に焦点を当てる。

## 仕組み・背景

### 「人間を超えた」を測る5つの物差し

| カテゴリ | 代表的な指標 | 何を測るか |
|---|---|---|
| 学術ベンチマーク | MMLU-Pro、GPQA Diamond、ARC-AGI、FrontierMath、HLE | 知識・専門知識・抽象推論・研究レベル数学 |
| 競技・大会 | IMO(国際数学オリンピック)、Codeforces、ICPC | 数学・競技プログラミングの人間トップ層との比較 |
| 資格・専門家試験 | 司法試験、LSAT、USMLE(医師国家試験) | 実在の資格試験での合格ライン・偏差値相当 |
| 科学的発見 | AlphaFold、AlphaEvolve、GNoME | 実際の未解決問題を解いた・新発見をしたか |
| コーディング実務 | SWE-bench Verified/Pro | 実際のGitHub issueをどれだけ自力で直せるか |

### 到達点(2026年7月時点)

| ベンチマーク | 人間基準 | AIの到達点 | 到達した時期 |
|---|---|---|---|
| MMLU(57科目の知識) | 専門家89.8% | Gemini Ultraが90.04%で初めて超えた(2023/12、その後飽和) | 2023年 |
| GPQA Diamond(博士レベル科学) | PhD専門家65〜70% | OpenAI o1が77.3%で初超え(2024/09)、2026年はGemini 3.1 Pro Previewが94.1%、Claude Sonnet 5が96.2% | 2024〜2026年 |
| FrontierMath Tier1-3(研究者レベル数学) | ―(公開当初は最先端AIでも2%未満) | Claude Fable 5が88%、GPT-5.5が75%(Epoch AI測定、2026年7月時点) | 2024〜2026年で急伸 |
| ARC-AGI-2(未知パターンへの抽象推論) | 人間95%以上 | GPT-5.5が85%(2026年7月時点の最高値) | まだ人間基準未到達 |
| ARC-AGI-3(対話型・より難化) | 人間ほぼ100% | 最高でもOpus 4.6が0.5%程度(2026年7月時点) | 大きく未到達 |
| Humanity's Last Exam(超高難度・全分野) | 専門家目安90%程度 | Claude Fable 5が53.3%(2026年7月時点の最高値) | 未到達 |
| SWE-bench(実務コーディング) | ― | Verifiedでは上位90%超えも報告されたが、2026年2月にOpenAIが「汚染により無効」と発表。汚染耐性の高いSWE-bench Proでは上位でも23〜58%程度に低下 | 指標自体が2026年に切り替わった |
| IMO(国際数学オリンピック) | 金メダル35/42点 | 2025年にGoogle DeepMindのGemini Deep ThinkがIMO公式に金メダル相当と認定。2026年大会は7月10〜21日に上海で開催中(本ページ執筆時点で結果未確定) | 2025年に公式認定達成 |

この表からわかる通り、「知識を問う」「決まったパターンを当てはめる」領域(MMLU、GPQA、数学オリンピック)では
すでに人間の専門家を超えているか、僅差まで迫っている一方、「見たことのないパターンに対話的に適応する」
領域(ARC-AGI-2/3)では依然として大きな差が残る。ARC Prizeの創設者François Cholletは
「o3のような高スコアモデルでも、人間には非常に簡単なタスクで失敗し続ける」と指摘しており、
単一の「AI IQ」のような総合順位では捉えきれない凹凸がある。

## 使いどころ・使い分け

### この種の数字を引用してよい場面・避けるべき場面

| 場面 | 判断 | 理由 |
|---|---|---|
| 記事で「AIの進歩の速さ」を示す事例として引用 | ◯ | 「2024年に2%未満だった指標が2年で90%近くまで伸びた」という**変化の速度**は再現性のある事実 |
| 「このベンチマークで1位だから業務にも最適」と結論づける | ✕ | ベンチマークは特定タスクの成績であり、自社データでの検証なしに実務適性は判断できない([生成AIの最新モデル動向](ai-model-trends-basics.md)の乗り換え判断チェックリスト参照) |
| 「AIはもう医師・弁護士に取って代わる」の根拠として単独引用 | ✕ | 資格試験のスコアは知識問題の再現力であり、臨床判断・対人交渉・責任所在などの実務要素を測っていない |
| ベンダー自身の発表スコアをそのまま「客観的な世界記録」として記載 | △ | 自己申告スコアは独立評価機関(Artificial Analysis、Epoch AI、ARC Prizeなど)の値と乖離することがあるため、可能な限り併記する |

### 「人間超え」の粒度を区別する

- **飽和した指標**(MMLU等): 上位モデル同士の差が誤差レベルまで縮まっており、「1位」を強調する意味が薄い
- **急伸中の指標**(FrontierMath、GPQA Diamond): 半年〜1年単位でスコアが大きく動くため、記事化する際は測定時期を必ず明記する
- **依然として大きな差が残る指標**(ARC-AGI-2/3): 「AIは万能」という論調へのカウンターとして使える

## 実務での使い方

### 記事・資料への引用テンプレート

コピペしてベンチマーク数字を記事や資料に落とし込む際は、以下の4点を必ずセットで書く。

```
[ベンチマーク名]で[モデル名]が[スコア]を記録(測定:[年月]、出典:[評価機関名])
※人間基準:[基準値]/[出典]
※自己申告か独立評価かの別:[ベンダー発表 / 第三者評価(Artificial Analysis等)]
```

### 最新スコアの一次情報源(定点観測先)

| 情報源 | 特徴 |
|---|---|
| [Artificial Analysis](https://artificialanalysis.ai/) | 複数モデルのベンチマークを独立測定し横並びで公開。合成指標「Intelligence Index」も提供 |
| [Epoch AI](https://epoch.ai/) | FrontierMathなど研究レベルベンチマークの独立運営元。汚染対策(非公開問題)に積極的 |
| [ARC Prize](https://arcprize.org/) | ARC-AGIシリーズの公式運営。人間ベースラインとの比較や「まだ解けないタスク」の分析を公開 |
| [METR](https://metr.org/) | AIエージェントが自律的にやり切れる作業時間の長さ(タイムホライゾン)を測定 |

### 数字を記事化する際のチェック手順

1. スコアの発表元が**ベンダー自身か第三者評価機関か**を確認する
2. **測定時期**を明記する(数か月で数値が大きく動くため)
3. 「人間基準」がどう定義されているか(専門家平均か、トップ層か)を確認する
4. データ汚染(ベンチマークの正解が学習データに混入)の指摘がないか、該当ベンチマークの運営元発表を確認する

## 注意点・よくある誤解

- **自己申告スコアの偏り**: SWE-bench Verifiedの例のように、ベンダー自身が公表するスコアは独立評価より高く出る傾向がある。2026年2月、OpenAIはSWE-bench Verifiedの失敗ケースの約6割がテスト自体の欠陥であり、かつ主要フロンティアモデルに学習データ汚染があったことを認め、以後は汚染に強いSWE-bench Proへの移行を推奨した。Verifiedで70〜80%だったスコアがProでは23〜58%まで下がるケースが報告されている
- **「専門家超え」の再評価**: GPT-4の司法試験スコアは当初「上位90パーセンタイル」と発表されたが、MIT研究者らの再評価により、実際は7月受験者全体で約68位、弁護士との比較では約48位相当と大幅に下方修正された。ベンダーの一次発表を鵜呑みにせず、独立検証の有無を確認する
- **科学的発見の成果にも訂正例がある**: DeepMindのGNoME(新結晶構造探索AI)が発見したとされた安定材料の一部は、2025年後半に「既知構造との重複」を理由とした撤回要求が学術誌に提出されている。「AIが新発見をした」という成果発表も、事後の検証で見直されることがある
- **IQスコアをLLMに当てはめる妥当性には議論がある**: TrackingAIなどが公開するLLMの「IQ相当値」は、公開テストへの学習データ混入リスクやサンプル数の少なさ(基準集団がわずか数十名など)から、方法論的な限界が指摘されている。運営団体自身も「広範な知能の決定的な指標ではない」と留保している
- **飽和したベンチマークでの僅差比較は無意味に近い**: MMLUのように上位モデルが軒並み88%を超えた指標では、数ポイントの差を「業界トップ」の根拠にするのは誤解を招く
- **ARC-AGIの急伸と急落**: OpenAI o3はARC-AGI-1で87.5%(人間基準を超過)に達したが、より難化したARC-AGI-2では3%未満まで急落した。「1つのベンチマークで人間を超えた」ことは、他のベンチマークでも同様に人間を超えたことを意味しない

## 最初の一歩

記事や資料で「AIが人間を超えた」という数字を引用する前に、まず発表元が
ベンダー自身か独立評価機関(Artificial Analysis、Epoch AI、ARC Prizeなど)かを1つ確認する習慣をつける。

## 関連トピック

- [生成AIの最新モデル動向(2026年:主要モデルの進化とベンチマークの見方)](ai-model-trends-basics.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [生成AI業界の主要プレイヤーと動向(資金調達・提携・戦略)](ai-industry-major-players-trends.md)
- [AIプロジェクトの進め方と評価指標の基礎](../part01-ai-basics/ai-project-and-evaluation-basics.md)

## 更新履歴

### 2026-07-11: 初版執筆(教材ページとして再構成)
- **内容**: 社内に残っていた未整形のベンチマーク調査メモ(2026-07-06時点の3本のDeep Researchレポートのマージ)を、教材ページの型(これは何か/使いどころ/実務での使い方/注意点)に沿って再構成。HLE・ARC-AGI-2/3・FrontierMath・SWE-bench・IMOの最新スコアを2026年7月時点で再検証し、独立評価機関の情報源一覧と、記事化する際の引用チェック手順を追加
- **出典**: [pricepertoken.com: Humanity's Last Exam Leaderboard 2026](https://pricepertoken.com/leaderboards/benchmark/hle)、[BenchLM.ai: ARC-AGI-2 Benchmark 2026](https://benchlm.ai/benchmarks/arcAgi2)、[ARC Prize: ARC-AGI-3 Human Leaderboard](https://arcprize.org/arc-agi/3/leaderboard)、[Epoch AI: FrontierMath Tier 4 (v2)](https://epoch.ai/benchmarks/frontiermath-tier-4-v2)、[the-decoder.com: Claude Fable 5 outpaces GPT-5.5 by 13 points on FrontierMath's toughest problems](https://the-decoder.com/claude-fable-5-outpaces-gpt-5-5-by-13-points-on-frontiermaths-toughest-problems/)、[OpenAI: Why we no longer evaluate SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)、[blockchain.news: OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)、[Google DeepMind: Advanced version of Gemini with Deep Think officially achieves gold-medal standard at the IMO](https://deepmind.google/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/)、[Polymarket: AI wins IMO gold medal in 2026?](https://polymarket.com/event/ai-wins-imo-gold-medal-in-2026)、[Scientific American: Mathematicians Question AI Performance at International Math Olympiad](https://www.scientificamerican.com/article/mathematicians-question-ai-performance-at-international-math-olympiad/)
