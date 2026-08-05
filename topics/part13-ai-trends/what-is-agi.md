---
title: "AGI(汎用人工知能)とは何か"
part: 13
chapter: 第3章 AGIと働き方の未来
tags: [AGI, ASI, 生成AI動向, AI戦略, ベンダー選定]
created: 2026-07-06
updated: 2026-07-29
---

# AGI(汎用人工知能)とは何か

## これは何か

「弊社は2027年にAGIを実現する」「このモデルはAGIに近づいた」——AIベンダーのブログやニュースで「AGI(Artificial General Intelligence、汎用人工知能)」という言葉を目にする機会が増えている。だが実はAGIには業界で合意された定義も、「達成した/していない」を判定する共通テストも存在しない。この状態のまま言葉だけを受け取ると、根拠の薄い期待や不安に振り回され、目の前のツールを「今日何に使えるか」という現実的な判断が疎かになる。AGIを、特定の企業の主張ではなく「評価の物差し」として理解しておくことが、AI戦略を語るうえでの土台になる。

大まかに言えば、AGIとは「人間が知的にこなせるほぼすべてのタスクで、人間と同等以上の能力を発揮するAI」を指す概念である。特定の1タスクのために作られた「特化型AI(Narrow AI)」(例: スパムメール判定だけを行うAI、将棋だけを指すAI)とは対極にあり、また現在のChatGPTやGeminiのような大規模言語モデル(LLM)とも区別される。今日のLLMは非常に幅広いタスクに対応できる汎用性を持つが、専門分野での高度な推論・長期記憶を要する計画・身体を伴う実世界操作などでは人間の熟練者に安定して届いていない。「幅は広いが、深さと安定性が人間に届いていない」のが現在地であり、AGIはその先にある「深さも幅も人間以上」という仮想的な到達点を指す言葉、と捉えると位置づけが掴みやすい。

## 仕組み・背景

AGIという言葉に単一の定義がないのは、測定の基準が「能力ベース」と「経済的インパクトベース」の少なくとも2系統に分かれていることが大きい。

**経済的インパクトベースの定義**の代表がOpenAIの創業時の憲章(Charter)で、AGIを「ほとんどの経済的価値のある仕事で人間を上回る、高度に自律的なシステム(highly autonomous systems that outperform humans at most economically valuable work)」と定義している(参照: [OpenAI Charter](https://openai.com/charter/))。この定義は「儲かる仕事を代替できるか」という基準であり、知能の中身よりも経済への影響を測る発想に近い。

**能力ベースの定義**の代表例が、Google DeepMindの研究チームが2023年に提唱し2024年に論文化した「Levels of AGI(AGIのレベル分け)」フレームワークで、自動運転のレベル分け(レベル0〜5)に倣い、AIの汎用性(どれだけ幅広いタスクに対応できるか)と性能(人間のどの水準に達しているか、未熟〜新人〜熟練者〜専門家〜超人的)の2軸でAIの進捗を段階的に評価しようとするものである。同チームは2026年3月にも「認知能力」の観点から進捗を測る改訂フレームワークを公開しており、"AGIが達成された瞬間"を一点で判定するのではなく、連続的な進捗として捉える発想が研究コミュニティでは主流になりつつある(参照: [DeepMind: Levels of AGI](https://arxiv.org/abs/2311.02462)、[DeepMind: Measuring Progress Toward AGI](https://arxiv.org/html/2605.28405))。

「AGIに到達したかどうか」を判定する基準も、時代とともに移り変わってきた。1950年に数学者アラン・チューリングが提案した**チューリングテスト**(会話のやり取りだけで相手が人間かAIか判別できなければ、そのAIは知的だと見なす基準)は長らく知能評価の代名詞だったが、現在のLLMは流暢な会話文を生成できてしまうため、「会話で人間と区別がつくか」はもはや知能の証明にならないというのが共通認識になっている。これに代わって近年注目されているのが、Google元エンジニアのFrançois Chollet氏が創設した**ARC-AGIベンチマーク**で、色付きマスの並びから変換ルールを見抜き、初見のパターンに適用させる抽象推論タスクを通じて、学習データの丸暗記では解けない「新しい状況への対応力」を測ろうとする設計になっている。

このベンチマークの推移は「飽和したらより難しい版に置き換わる」といういたちごっこの構図を示す好例でもある。2025年公開のARC-AGI-2は、2026年に入るとOpenAIのGPT-5.4 Proが約83%、GoogleのGemini 3「Deep Think」が約85%まで到達し、複数モデルを組み合わせた「メタシステム」に至っては95〜98%と、事実上飽和状態になった(参照: [IntuitionLabs: GPT-5.2 & ARC-AGI-2](https://intuitionlabs.ai/articles/gpt-5-2-arc-agi-2-benchmark))。ところが2026年3月25日、運営元のARC Prizeは形式を一新した**ARC-AGI-3**を公開する。色マスのパズルを解く一問一答形式から、説明もルールも与えられないゲーム風の環境を自力で探索し、目標そのものを発見しながら攻略していく「対話型・エージェント型」の推論力を問う内容に刷新されており、公開直後は人間の正答率100%に対し最先端モデルはすべて1%未満というスコアだった(参照: [ARC Prize: ARC-AGI-3](https://arcprize.org/arc-agi/3)、[dev.to: GPT-5, Claude, Gemini All Score Below 1%](https://dev.to/codepawl/gpt-5-claude-gemini-all-score-below-1-arc-agi-3-just-broke-every-frontier-model-5dbj))。2026年7月時点でもAnthropicのClaude Opus 5が約30%でトップ、OpenAIのGPT-5.6 Solが1桁%にとどまるなど、依然として大きな差が残っている(参照: [BenchLM: ARC-AGI-3 Leaderboard July 2026](https://benchlm.ai/benchmarks/arcAgi3))。「特定のベンチマークが飽和したら、より難しい版に置き換わり、差が再び開く」というこのパターンそのものが、「あるベンチマークで高得点=AGI到達」という早合点への強力な反証になっている。

一方、Anthropicは「AGI」という言葉自体をあまり使わない立場を取っている。共同創業者でCEOのDario Amodeiは自身のエッセイの中で「AGIという言葉は好きではない」と明言し、SF的な連想がつきまとう「AGI」の代わりに、「未解決の数理定理を証明できる」「優れた小説を書ける」「難しいコードベースをゼロから書ける」といった具体的な能力の列挙で「powerful AI(強力なAI)」を説明する方式を採っている(参照: [Dario Amodei: Machines of Loving Grace](https://darioamodei.com/essay/machines-of-loving-grace))。

定義が定まらない実害は、2025年まで存在したOpenAIとMicrosoftの提携契約にも表れていた。両社の契約には「OpenAIの取締役会がAGI達成を宣言した時点でMicrosoftのライセンスが打ち切られる」という、通称「AGI条項」が盛り込まれていたが、"AGI達成"を客観的に判定する基準がなく、取締役会の主観的判断に委ねられる不安定な条項になっていた。2026年4月、両社はこの条項自体を契約から削除する形で合意しており、「契約や規制の根拠として使うには、AGIという言葉は曖昧すぎる」という実務的な教訓を残した(参照: [Simon Willison: Tracking the history of the now-deceased OpenAI Microsoft AGI clause](https://simonwillison.net/2026/Apr/27/now-deceased-agi-clause/))。

2026年に入ってからは、企業トップ本人による"独自定義でのAGI宣言"がむしろ増えている。NVIDIAのJensen Huang CEOは2026年3月、Lex Fridman氏のポッドキャストで「我々はすでにAGIを達成したと思う」と発言したが、実際に示した定義は「10億ドル規模の事業を独力で立ち上げ運営できるAI」という同氏独自の実務基準であり、AI業界内では「都合の良い定義への置き換えではないか」という批判を招いた。Sam Altman氏はこの発言に部分的に同意した一方、Yann LeCun氏は明確に否定するなど、反応は割れている(参照: [Fortune: AGI definition debate](https://fortune.com/2026/03/30/agi-definition-jensen-huang-lex-fridman-deepmind-turing-text-cognitive-taxonomy/))。さらにAltman氏自身も、2026年7月25日のポッドキャストで「我々はもう特異点(シンギュラリティ)の中にいる」と発言して話題になった。ただし本人は、これを"ある日突然訪れる超知能"ではなく"指数関数的な進歩が積み重なる緩やかな変化(gentle singularity)"だと説明しており、2025年のエッセイで示した「本当の意味でのAGI」の到来時期は2035年前後という、自らの"達成宣言"よりずっと慎重な見立てのままである(参照: [Sam Altman: The Gentle Singularity](https://blog.samaltman.com/the-gentle-singularity)、[Fortune: Sam Altman thinks the singularity is already here](https://fortune.com/2026/07/27/sam-altman-ai-singularity-elon-musk-openai-hugging-face-breach/))。同じ人物・同じ会社の中でも文脈によって使う定義や強気度が変わる——この点こそが「AGI」という言葉の実務上の扱いにくさを象徴している。

## 使いどころ・使い分け

AGIは「導入するかどうかを選ぶ製品カテゴリ」ではなく、AIの実力を評価するための「物差し(概念)」である。実務での向き合い方は次のように整理できる。

| 観点 | 特化型AI(Narrow AI) | 現在の生成AI・LLM(2026年時点) | AGI(仮想的な到達点) |
|---|---|---|---|
| 対応できるタスクの幅 | 特定の1タスクのみ(例: スパム判定、需要予測) | 文章・コード・画像など非常に幅広いタスクに対応 | 人間が知的にこなせるほぼ全タスク |
| 性能の水準 | 対象タスクでは人間を上回ることも多い | タスクによって新人〜専門家レベルまで幅がある。ハルシネーションや長期計画の不安定さが残る | 全領域で人間の熟練者〜専門家水準以上、かつ安定 |
| 現時点での実在性 | すでに実用化・大量導入されている | すでに実用化されている(本サイトが扱う対象) | 実現時期・定義とも未確定の仮説的な概念 |
| ビジネス上の扱い方 | 個別業務への適用可否で判断する | [向く業務・向かない業務の切り分け](../part12-business-practice/ai-task-suitability.md)で判断する | ベンダーの主張を評価する「物差し」として使う。導入計画の前提にはしない |

判断基準として持っておきたいのは、「目の前のツールが今日できること」と「ベンダーが将来できると約束していること」を切り分けることである。AGIの実現時期は前者ではなく後者に属する話であり、業務のAI活用計画は前者(今日の実力)を基準に立てるのが原則になる。

## 実務での使い方

AGIという概念は、ビジネスパーソンにとって「何かを設定する」対象ではない。使い道は主に2つ、(1) ベンダーやメディアの「AGI」発言を読み解く物差しとして使う、(2) 社内のAI戦略議論で期待値を揃えるための共通言語として使う、である。

### ベンダーのAGI関連発言を読み解くチェックリスト

AIベンダーやその経営者が「AGI」に言及した記事を読むときは、次の3点を確認するとよい。

1. **どの定義で語っているか**: 「経済的価値のある仕事を代替できるか」(OpenAI型)なのか、「特定の認知タスクで人間の専門家水準に達したか」(DeepMind型)なのか、それとも定義を明示していないのか。定義を示さずに「AGIに到達した」と語る主張は、マーケティング的な誇張である可能性を疑う。2026年3月にNVIDIAのJensen Huang CEOが「AGIを達成した」と述べた際も、実際の中身は「10億ドル企業を運営できるAI」という同氏独自の基準だった。額面通りに受け取らず、定義の中身を確認する癖をつける
2. **誰の予測で、どの程度の確度か**: 経営者個人の見通しなのか、査読を経た研究チームの分析なのか。同じ2026年のダボス会議の場でも、AnthropicのDario Amodei氏は「1年以内にソフトウェア開発者の仕事のほとんどをAIが代替し、2年以内に複数分野でノーベル賞級の研究水準に達する」という強気の見通しを語った一方、Google DeepMindのDemis Hassabis氏は「(人間レベルのAGIには)5〜10年、この10年間で実現する確率は五分五分」と述べ、さらにMeta出身でAI研究の重鎮であるYann LeCun氏は「現在のLLMを訓練する延長線上に人間レベルの知能はない」と、そもそものアプローチに異を唱えている。同じ業界のトップ同士でも数年単位・アプローチ単位で意見が割れている、という事実そのものが重要な情報である(参照: [Fortune: AI luminaries at Davos clash over how close human-level intelligence really is](https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/))
3. **契約・投資判断の根拠にできる話か**: OpenAIとMicrosoftの提携契約から「AGI条項」自体が削除された経緯が示す通り、「AGI達成」を客観的に判定する基準は業界内にも存在しない。社内の投資判断や契約条件を、特定企業の「AGI宣言」に依存させないことが安全策になる

### 社内のAI戦略議論での使い方

経営層や事業部門から「AGIが来たらうちの会社はどうなるのか」と問われた際は、次のような整理で答えると建設的な議論になりやすい。

- 「AGI」を待つ・恐れるのではなく、[生成AIに向く業務・向かない業務の切り分け](../part12-business-practice/ai-task-suitability.md)で今使えるAIの適用範囲を広げていく方が、投資対効果が読みやすい
- ベンダーのロードマップ上の「AGI」「次世代モデルで実現」といった将来約束は、意思決定の前提ではなく参考情報として扱う
- 半年〜1年単位でLLMの実力そのものは着実に上がっているため、「AGIが来るかどうか」よりも「今のモデルで新しくできるようになったことは何か」を定点観測する方が実務的である

## 注意点・よくある誤解

- **「AGI」と「AIエージェント」は別の軸の話**: [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)で扱う「エージェンティックAI」は、目標を渡せば計画・実行まで自律的にこなす、現時点で実在する製品パターンを指す。一方でAGIは、その自律実行の"中身の知能"が人間並みかどうかという、まだ実現していない仮説的な能力水準の話である。「エージェント機能が搭載された=AGIに近づいた」という短絡は誤り
- **ベンチマークの高得点=AGI達成ではない。しかも「合格ライン」は動き続ける**: 「ARC-AGI」のように、AIの汎化能力(見たことのないパターンに対応する力)を測ろうとする専用ベンチマークも存在するが、特定ベンチマークでの高スコアは「そのテストが測る種類の推論に強い」ことを示すに過ぎない。実際、2025年公開のARC-AGI-2は2026年中に主要モデル・メタシステムでほぼ飽和したが、その直後の2026年3月に登場したより難しいARC-AGI-3では最先端モデルが軒並み1%未満まで叩き落とされた。「あるテストで満点近くを取った」というニュースだけを見て「AGIに近づいた」と判断するのは早計であり、より難しい後継ベンチマークが常に控えていることを前提に読む(参照: [ARC Prize: ARC-AGI-3](https://arcprize.org/arc-agi/3))
- **「AGIは実質死語」という見方と、経営者による強気の宣言が同時に存在する**: OpenAIのSam Altman氏自身が2025年に「AGIという言葉自体があまり有用ではなくなってきた」と発言した一方、2026年に入ってからは自社が「経済的価値のある仕事のほとんどで人間を上回る」という自社定義をすでに満たしたとの立場に近づき、同年7月25日には「我々はもう特異点(シンギュラリティ)の中にいる」とまで発言している(参照: [CNBC: Sam Altman now says AGI is 'not a super useful term'](https://www.cnbc.com/2025/08/11/sam-altman-says-agi-is-a-pointless-term-experts-agree.html)、[Fortune: Sam Altman thinks the singularity is already here](https://fortune.com/2026/07/27/sam-altman-ai-singularity-elon-musk-openai-hugging-face-breach/))。同一人物の中でも発言の強弱が文脈次第で変わる以上、「AGI」「シンギュラリティ」を含む発言は発言者ごと・場面ごとに前提が異なる可能性を常に疑ってよい
- **ASI(Artificial Superintelligence、人工超知能)はさらにその先の概念**: AGIが「人間と同等」を指すのに対し、ASIはあらゆる知的領域で人間の最も優れた専門家を大きく上回る水準を指す、AGIとは区別される仮想的な概念である。AGIが実現していない以上ASIの実現時期を論じるのはさらに投機性が高いが、一部の経営者はAGIよりASIの議論に軸足を移しつつある。2025年10月には非営利団体Future of Life Instituteが「広範な科学的合意と社会の同意が得られるまでASI開発を禁止すべき」とする「Statement on Superintelligence」を公開し、AI研究の重鎮であるYoshua Bengio氏・Geoffrey Hinton氏(ともにチューリング賞受賞者)やApple共同創業者のSteve Wozniak氏を含む700名超が署名するなど、経営者の発言にとどまらない政策論争にまで発展している(参照: [CyberScoop: Open letter calls for prohibition on superintelligent AI](https://cyberscoop.com/ai-superintelligence-ban-open-letter-future-of-life-harry-meghan-tech-leaders/))。この点も「まだ実現していない将来予測の話をしている」という前提を忘れずに読む必要がある
- **AGI論争に時間を使いすぎない**: 社内で「AGIが来たらどうする」という抽象論に時間を割くより、[生成AIに向く業務・向かない業務の切り分け](../part12-business-practice/ai-task-suitability.md)で今のツールの適用範囲を広げる方が、投資対効果の観点で優先度が高いことが多い

## 最初の一歩

次にニュースやベンダー資料で「AGI」という言葉を見かけたら、「どの定義(経済的インパクト/能力レベル)で使われているか」「発言者は誰で、どの程度の確度の予測か」の2点をその場で確認する癖をつける。それだけで、根拠のない期待や不安に振り回されず、目の前のツールの実力評価に意識を戻せる。

## 関連トピック

- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [生成AIに向く業務・向かない業務の切り分け](../part12-business-practice/ai-task-suitability.md)
- [LLMの得意・不得意](../part02-llm-basics/llm-strengths-and-limitations.md)

## 更新履歴

### 2026-07-29: ARC-AGI-3の登場と経営者の相次ぐAGI/シンギュラリティ発言を反映して最新化
- **内容**: ARC-AGIベンチマークがARC-AGI-2の事実上の飽和(GPT-5.4 Pro約83%、Gemini 3 Deep Think約85%、メタシステム95〜98%)を経て、2026年3月により難しい対話型・エージェント型のARC-AGI-3(公開直後は最先端モデルも1%未満、2026年7月時点でもClaude Opus 5が約30%でトップ)に置き換わった経緯を追加し、「ベンチマークが飽和したらより難しい版に置き換わる」といういたちごっこ構造を明記。NVIDIAのJensen Huang CEOによる2026年3月の「AGI達成」発言(独自定義に基づく点)、Sam Altman氏が2026年7月25日に「我々はもう特異点の中にいる」と発言した件とその慎重な補足(gentle singularity、本人の2035年前後というAGI到来時期の見立て)を追加。ASIに関して2025年10月のFuture of Life Institute「Statement on Superintelligence」(Bengio・Hinton・Wozniak氏ら700名超が署名)を追加し、ASI議論が経営者発言を超えて政策論争化している点を補強
- **出典**: [IntuitionLabs: GPT-5.2 & ARC-AGI-2 Benchmark Analysis](https://intuitionlabs.ai/articles/gpt-5-2-arc-agi-2-benchmark)、[ARC Prize: ARC-AGI-3](https://arcprize.org/arc-agi/3)、[dev.to: GPT-5, Claude, Gemini All Score Below 1% - ARC AGI 3](https://dev.to/codepawl/gpt-5-claude-gemini-all-score-below-1-arc-agi-3-just-broke-every-frontier-model-5dbj)、[BenchLM: ARC-AGI-3 Leaderboard July 2026](https://benchlm.ai/benchmarks/arcAgi3)、[Fortune: AGI definition debate (Jensen Huang)](https://fortune.com/2026/03/30/agi-definition-jensen-huang-lex-fridman-deepmind-turing-text-cognitive-taxonomy/)、[Sam Altman: The Gentle Singularity](https://blog.samaltman.com/the-gentle-singularity)、[Fortune: Sam Altman thinks the singularity is already here](https://fortune.com/2026/07/27/sam-altman-ai-singularity-elon-musk-openai-hugging-face-breach/)、[CyberScoop: Open letter calls for prohibition on superintelligent AI](https://cyberscoop.com/ai-superintelligence-ban-open-letter-future-of-life-harry-meghan-tech-leaders/)

### 2026-07-06: 初版執筆
- **内容**: AGIの定義が業界で統一されていない背景(経済的インパクトベース/能力ベースの2系統)、OpenAI・Google DeepMind・Anthropicそれぞれの立場の違い、2026年時点の主要人物間のタイムライン論争(ダボス会議でのAmodei・Hassabis・LeCunの対立)、OpenAI-Microsoft間の「AGI条項」削除の経緯、ASIとの違い、チューリングテストからARC-AGIベンチマークへの判定基準の変遷とARC-AGI-2の最新スコア、ベンダーのAGI関連発言を読み解く実務的なチェックリストを整理
- **出典**: [OpenAI Charter](https://openai.com/charter/)、[Simon Willison: Tracking the history of the now-deceased OpenAI Microsoft AGI clause](https://simonwillison.net/2026/Apr/27/now-deceased-agi-clause/)、[Dario Amodei: Machines of Loving Grace](https://darioamodei.com/essay/machines-of-loving-grace)、[Google DeepMind: Levels of AGI for Operationalizing Progress on the Path to AGI](https://arxiv.org/abs/2311.02462)、[Google DeepMind: Measuring Progress Toward AGI: A Cognitive Framework](https://arxiv.org/html/2605.28405)、[Fortune: AI luminaries at Davos clash over how close human-level intelligence really is](https://fortune.com/2026/01/23/deepmind-demis-hassabis-anthropic-dario-amodei-yann-lecun-ai-davos/)、[CNBC: Sam Altman now says AGI is 'not a super useful term' — and he's not alone](https://www.cnbc.com/2025/08/11/sam-altman-says-agi-is-a-pointless-term-experts-agree.html)、[ARC Prize: ARC-AGI-2](https://arcprize.org/arc-agi/2)、[AgentMarketCap: ARC-AGI-2 Leaderboard 2026](https://agentmarketcap.ai/blog/2026/04/06/arc-agi-2-leaderboard-2026-gemini-gpt5-claude-reasoning-benchmark)
