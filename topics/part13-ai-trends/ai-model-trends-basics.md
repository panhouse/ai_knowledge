---
title: "生成AIの最新モデル動向(2026年:主要モデルの進化とベンチマークの見方)"
part: 13
chapter: 第1章 技術トレンド
tags: [モデル動向, ベンチマーク, GPT-5, Claude, Gemini, モデル選定]
created: 2026-07-07
updated: 2026-09-04
---

# 生成AIの最新モデル動向(2026年:主要モデルの進化とベンチマークの見方)

## これは何か

「また新しいモデルが出たらしいが、乗り換えるべきか」「ベンチマークで1位と謳っているが、それは業務で本当に賢いということなのか」——生成AIの主要モデルは数か月おきに更新され、そのたびに「過去最高スコア」を掲げた発表が続く。しかし発表の頻度自体が速すぎて、どの更新が実務に影響するレベルの進化で、どれが数字上のマイナーチェンジに過ぎないのかを見極めないまま「とりあえず最新モデルに乗り換える」を繰り返すと、移行コストばかりがかさむ。本ページは、2026年9月4日時点の主要モデルの動向を整理した上で、ベンチマークという「モデルの成績表」の読み方と、新モデル登場時に乗り換えるかどうかを判断する実務的な基準を示す。

**大前提として、モデル名・リリース時期・ベンチマークの数字は数週間単位で更新される。** 実際、この3週間だけでもAnthropicが「Claude Fable 5.1」(9月1日)を、OpenAIが世代交代モデル「GPT-6 Astra」(9月3日)を相次いで発表するなど、更新の波はむしろ加速している。本ページは2026年9月4日時点のスナップショットであり、記事の材料に使う際は必ず各社公式発表で最新状況を確認すること。

## 仕組み・背景

### なぜこれほど頻繁に新モデルが出るのか

OpenAI・Anthropic・Googleなど主要ラボ(AI研究開発企業)は、(1)数週間〜数か月ごとの「ナンバリングの小刻みな更新」と、(2)半年〜1年に一度の「世代交代」を組み合わせて発表するのが基本パターンになっている。さらに、最上位モデルは一般提供の前に「限定パートナー向けプレビュー」として先出しされることも増えている(例: OpenAIのGPT-5.6は2026年6月26日にまず信頼できる一部組織限定のプレビューとして提供され、7月9日に一般提供に切り替わった)。2026年8月以降も、xAIのGrok 4.6(8月12日)、MetaのMuse Spark 1.2(8月5日)・オープンウェイトの小型モデルMuse Glimmer(8月10日)、GoogleのGemini 3.7 Flash(8月13日、3.6 Flashからわずか23日後)、DeepSeekのV4 Pro改訂版「0813」(8月12〜13日)と枝番更新が続き、9月には**Anthropicが「Claude Fable 5.1」(9月1日)、OpenAIが世代番号そのものを繰り上げた「GPT-6 Astra」(9月3日)を2日違いで投入する**という、2026年で最も動きの速い週を迎えた。**「世代交代」の頻度自体も上がっている**点は2026年後半の新しい傾向として押さえておきたい(GPT-5→GPT-5.6→GPT-6は約1年、Claude Fable 5→5.1は2か月弱の間隔)。

**2026年に入ってからの新しい変数として、各国政府による輸出規制・提供制限がモデルの入手可能性そのものに影響するようになった点も見逃せない。** 2026年6月、米政権は国家安全保障を理由にAnthropicへ、最上位モデルのClaude Fable 5・Mythos 5を非米国籍ユーザー全員に対して即時停止するよう指示し、Anthropicは予告なく世界中の全顧客への提供を止めた。同時期、ホワイトハウスはOpenAIに対してもGPT-5.6の提供範囲を政府承認済みパートナーに限定するよう要請している。Anthropicへの規制は7月1日に解除され、Fable 5/Mythos 5は世界展開を再開したが、こうした「性能や価格ではなく地政学的な理由で、契約中のモデルが突然使えなくなる」リスクは、今後もモデル選定の考慮事項に加える必要がある([Al Jazeera](https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says)、[CNN](https://edition.cnn.com/2026/06/25/tech/openai-limit-release-white-house))。

**もう1つの新しい変数として、ラボ自身が定める「安全性の閾値」を理由にした段階的公開が始まった。** OpenAIは2026年9月3日公開の「GPT-6 Astra」について、自社のPreparedness Framework(危険な能力を段階評価する安全基準)上で「Critical(重大)」レベルのサイバー能力に達した初のモデルだと発表し、一般提供前に数週間の追加安全対策を挟んだ上で、まずサイバーセキュリティ関連の認可プログラム参加企業・エンタープライズ顧客に限定して提供を開始した([OpenAI公式X投稿](https://x.com/OpenAI/status/2095595757072191802)、[Bloomberg](https://www.bloomberg.com/news/articles/2026-09-03/openai-rolls-out-gpt-6-astra-model-with-added-cyber-guardrails))。地政学的な輸出規制と並んで、「ベンチマーク上は最強でも、安全性審査を理由に自社が使えるようになるまで数週間〜数か月かかる」という新しいタイムラグ要因が生まれた点は覚えておきたい。

### 主要ラボの現在地(2026年9月4日時点)

| ラボ | 現在の主力モデル | 補足 |
|---|---|---|
| OpenAI | **GPT-6 Astra**(9月3日発表。世代番号を繰り上げた最新の最上位モデル。コンピュータ操作・長時間エージェント・コーディングに重点)、下位には引き続き**GPT-5.6ファミリー**(Luna/Terra/Sol)が併存 | Astraは自社のPreparedness Framework上で初めて「Critical」水準のサイバー能力と判定され、一般提供は段階的(まず認可企業・Enterprise、順次Plus/Pro/Business/APIへ拡大)。価格は$10/$50(高速モードは$20/$100)、文脈windowは約105万トークン。ARC-AGI-3で最大99.9%(標準的な採点条件では62.7%)、FrontierMath Tier 4で97.6%、ExploitBenchで100%などを発表しているが、条件依存の高さが独立系レビューで指摘されている(後述) |
| Anthropic | **Claude Fable 5.1**(9月1日発表。既存のFable 5の後継で、公開済みの全ベンチマークでOpus 5・Fable 5を上回る)、**Claude Opus 5**(7月24日発表、Claude Max/Proの主力)、**Claude Sonnet 5**(6月30日発表、$2/$10入出力を恒久化)、**Claude Mythos 5.1**(サイバー・生命科学分野の認可組織限定) | Fable 5.1は入出力価格($10/$50)を据え置きつつ、キャッシュ読み込み単価を$0.25(従来比75%減)に引き下げ、実運用では2〜4割程度のコスト削減になるとされる。1Mトークンの文脈window、最大出力12.8万トークン |
| Google | **Gemini 3.1 Pro**が現行の一般提供モデル。次期主力の**Gemini 3.5 Pro**は5月のGoogle I/Oで予告されたが、6月→7月17日→8月上旬と延期を重ね、9月4日時点でも一般提供に至っていない(Vertex AIでの企業向け限定プレビューのみ) | 最上位モデルが遅延する一方、中位モデルの刷新は継続中。8月13日には前モデルからわずか23日で「Gemini 3.7 Flash」を投入(導入価格$0.75/$3.75、1M文脈window維持) |
| xAI | **Grok 4.6**(8月12日に一般公開。50万トークンの文脈window、長時間稼働するエージェント・コーディング・視覚タスクに重点) | Grok 4.5(7月8日公開)の後継で、9月4日時点でも最上位モデルの地位を維持。6兆パラメータ級とされる次世代「Grok 5」は開発中であることは公表されているものの、Q1→Q2と延期を重ね、正式な提供時期は依然未確定 |
| Meta | オープンウェイト(モデルの重みを公開し自社サーバーで動かせる方式)のLlama 4 Scout/Maverickは提供継続。Meta Superintelligence Labsはコーディング特化の非公開モデル「Muse Spark 1.2」(8月5日)に加え、単一の民生GPUでも動く300億パラメータの軽量オープンモデル「Muse Glimmer」(Apache 2.0ライセンス、8月10日)を投入 | Muse Glimmerは常時稼働のローカルエージェント用途を想定した小型モデルで、クラウド課金なしで使える点が特徴。Muse Spark 1.2は引き続き、プロンプト等の学習提供と引き換えに大幅割引となる「contributor」料金プランを提供 |
| Moonshot AI(中国) | **Kimi K3**(7月16日にAPI提供開始、7月27日に重み公開。2.8兆パラメータで過去最大級のオープンウェイトモデル) | Modified MIT ライセンスで公開。Artificial Analysis Intelligence Indexでは9月時点でも独自モデルを除くオープンウェイトモデルの中で最上位クラス(総合順位でも上位数社の独自モデルに次ぐ水準)を維持している |
| DeepSeek(中国) | **DeepSeek V4 Pro/Flash**(7月中旬に正式提供→8月12〜13日に改訂版「V4 Pro 0813」が正式版に、7月31日には「V4-Flash-0731」もGA)。次世代「V5」は9月4日時点で公式発表なし(SNS上の未確認の噂のみ) | 総合スコア(Artificial Analysis Intelligence Index)自体は伸び悩んだとの評価がある一方、エージェント型コーディングやサイバーセキュリティ関連の評価スコアはプレビュー版から大きく上昇。低価格路線・時間帯別課金の枠組みは維持され、8月21日には実験的な画像対応版「V4-Flash-Vision-Exp」も追加された |

この一覧からわかる実務上のポイントは、「モデル名の枝番更新は数週間〜数か月ごとに動くのが常態であり、その都度乗り換えを検討する必要はない」ということと、「発表(アナウンス)と一般提供(GA)の間には数週間〜数か月のタイムラグがあり得る」ということである(Gemini 3.5 Proのように、発表から3か月以上経っても一般提供に至らない例や、GPT-6 Astraのように安全性審査を理由に自社が実際に使えるまで段階的に待たされる例もある)。乗り換えを検討すべきかどうかは、後述の「使いどころ・使い分け」で扱う判断軸で考える。

### ベンチマークとは何か、なぜ複数ある必要があるのか

「ベンチマーク」とは、モデルの能力を定量的に比較するための共通テストである。1つのベンチマークだけでは能力の全体像を測れないため、知識・推論・コーディング・エージェント的な実行力・実務適性など、測る対象ごとに異なるベンチマークが使われる。

**2026年に入ってからの大きな変化として、「知識・選択式の教科書的なベンチマーク」から「実務・経済価値に近いタスクを測るベンチマーク」への重心移動が進んでいる。** MMLU・HumanEvalのような黎明期の定番は上位モデルがほぼ満点近くに達して見出しに使われなくなり、代わりにGDPval(実在する44職種の経済的価値のある業務を再現)やFrontier-Bench(Anthropicが専門的な納品物の質を評価)のような「実務代替性」に着目したベンチマークが主要ラボの発表で前面に出てきている。

**主要ベンチマークの一覧(2026年9月時点でよく引用されるもの)**

| ベンチマーク | 何を測るか | 過信すると危険な理由 |
|---|---|---|
| GDPval / GDPval-AA | 米国GDP寄与度上位9業界・44職種(ソフトウェア開発者、弁護士、看護師等)を代表する実在業務タスクをどれだけこなせるか(実務代替性) | OpenAI主導で設計された比較的新しい指標であり、対象職種・タスクの選定自体に偏りがあり得る。Artificial Analysisが独自に採点する「GDPval-AA」はElo(相対評価)方式のため、単体のスコアだけでなく他モデルとの相対関係で見る必要がある |
| Frontier-Bench | 専門的な知識労働の「納品物としての質」を評価する、Anthropicが公開した評価軸 | 自社モデルの強みを示しやすい設計になっていないか(評価団体自身が主要ラボである場合の利益相反)を意識する必要がある。第三者による再現・検証が進むまでは、単独のラボの発表数値を鵜呑みにしない |
| MMLU / MMLU-Pro | 57科目(のちに拡張)にわたる知識・選択式の推論力 | 上位モデルが軒並み高得点に達し「飽和」(スコアの差が能力差を反映しなくなる状態)しており、2026年時点では主要ラボの発表資料でも見出しに使われなくなってきている |
| GPQA Diamond | 生物・物理・化学の博士(PhD)課程レベルの専門問題 | トップ層(90%台)では飽和しつつあるが、60〜90%のレンジではモデル間の実力差を反映しやすく、実務の調達判断ではまだ参考になる。ただし「専門家超え」の見出しだけでなく、どの版・条件でのスコアかを確認する必要がある |
| SWE-bench Verified / SWE-bench Pro | 実際のGitHub issueをどれだけ自力で修正できるか(実務に近いコーディング能力) | **この1年で「信頼できるコーディング指標」の座が二度覆っている。** OpenAIは2026年2月、Verifiedで失敗した問題の約6割がテスト自体の欠陥だったとして同指標の採用を取りやめ、後継のSWE-bench Proへの移行を推奨した。ところが同じOpenAIが2026年7月8日、今度はPro自身を独自監査した結果を公表し、公開されている731タスクのうち約3割が「テストが厳格すぎて正しい実装まで不合格にする」などの欠陥を抱えていたとして推奨を撤回した。Proの公開データセットでの上位モデルのスコアは8か月で23.3%から80.3%まで上昇していたが、これは純粋な能力向上では説明がつかない伸び方であり、汚染(データ漏洩)や採点基準の抜け穴を突いた最適化を疑うべき事例として扱われている |
| ARC-AGI-2 / ARC-AGI-3 | 見たことのないパターンから規則を発見する抽象推論力(新規状況への適応力) | 汚染(データ漏洩)への耐性を意識して設計されているが、スコアの絶対値だけでなく「どれだけの計算コストをかけて解いたか」(1問あたりの推論コスト)を無視すると実用性の判断を誤る。**「測定条件で数字が激変する」典型例が2026年9月に起きた**: OpenAIはGPT-6 AstraがARC-AGI-3を「飽和」させたとして99.9%を発表したが、これはOpenAI独自の「Provider Adapterハーネス」(モデル間で内部状態を引き継がせる特別な仕組み、約$19Kのコスト)での数字であり、ARC Prize側の標準的な採点条件では62.7%(約$26Kのコスト)にとどまる。半年前は7.8%だった同モデル系列がここまで伸びたこと自体は事実だが、「どのハーネス・条件でのスコアか」を確認せずに見出しの数字だけを比較すると実力を過大評価する |
| METR タイムホライゾン(時間水平線) | 人間なら何分〜何時間かかる作業を、AIエージェントがどこまで自律的にやり切れるか(実行の持続力) | 2026年1月の指標改定(Time Horizon 1.1)でタスク数を170→228件に拡充した結果、「達成できるタスクの長さが倍増する速度」の推定値自体が7か月から約3か月(2024年以降のトレンド)へ上方修正された。**測定手法の改定でヘッドライン数値そのものが動く**という好例であり、測定対象もソフトウェア関連タスクに偏っているため、あらゆる業務に一般化はできない |
| Humanity's Last Exam(HLE) | 100以上の分野にわたる、インターネット上に解答が存在しない超高難度の問題 | 採点する評価団体によってスコアが10〜20ポイント単位でぶれることがあり、「公式スコア」がどの評価基準によるものかを確認しないと単純比較できない |
| Chatbot Arena(LMArena) | 人間による2モデルのブラインド比較投票に基づく好感度ランキング | 「回答が長い」「フォーマットが整っている」「愛想がよい」回答が人間投票で有利になりやすいバイアスが指摘されており、実務上の正確性そのものを測っているわけではない。研究者からは「Leaderboard Illusion(リーダーボードの幻影)」として、大手ラボがスコアを選択的にしか公表しない・ランキング用に特別チューニングした版だけを提出するといった問題も指摘されている。運営が主要ラボから収益を得るビジネスモデルに変わったことで中立性への懸念も指摘されており、総合ランキングよりコーディング・数学など分野別ランキングの方が参考にしやすいとされる |
| Artificial Analysis Intelligence Index | 複数のベンチマークを合成した総合指数(v4.0はGDPval-AA・Terminal-Bench・GPQA Diamond・SciCodeなど10種のベンチマークを合成) | 9月2日時点の版ではClaude Fable 5.1が首位(65.7%)、僅差でClaude Opus 5(63.1%)が続く。Kimi K3はオープンウェイトモデルとして最上位クラス(独自モデルを除けば単独首位級)に入る。GPT-6 Astraは発表直後で本指数への反映・独立検証がまだ進んでおらず、個別ベンチマーク(Terminal-Bench・DeepSWE等)ではFable 5.1・Opus 5と一進一退の結果が報告されている。指数の版が更新されるたびに、どのテストをどう重み付けしたかという設計次第でランキングが動く点は個別ベンチマークと同じである |

## 使いどころ・使い分け

### ベンチマークの使い分け

| 知りたいこと | 参考にすべきベンチマーク |
|---|---|
| 実務に近い経済価値の高い業務をこなせるか | GDPval / GDPval-AA、Frontier-Bench(ただし主要ラボ発の指標である点を割り引いて見る) |
| 知識・雑学的な受け答えの広さ | GPQA Diamond(MMLU系はすでに飽和しており参考価値が下がっている) |
| コーディング支援・自動化に使えるか | SWE-bench Pro(ただし前述の欠陥報告を踏まえ単独の絶対値は過信しない)、Codeforces系(競技プログラミング) |
| 複数ステップの作業をエージェントとして任せられるか | METRタイムホライゾン、Terminal-Bench等のエージェント系ベンチマーク |
| 人間らしい自然な受け答えの好感度 | Chatbot Arena(ただし正確性の指標ではなく、Leaderboard Illusion問題がある点に注意) |
| 未知の状況への応用力・新規性への強さ | ARC-AGI-2/3 |
| 総合的な「今どのモデルが強いか」の目安 | Artificial Analysis Intelligence Index(ただし版によって順位が変わる点に注意) |

いずれか1つの数字だけで判断せず、自社の用途に近いベンチマークを2〜3種類組み合わせて見る、あるいは合成指標を参考にするのが実務的である。ただし合成指標もどのテストをどう重み付けしたかという設計次第でランキングが変わるため、「絶対的な正解」ではなく「複数ある物差しの一つ」として扱う。

### 新モデルが出たら乗り換えるべきか:判断チェックリスト

新しいモデル(または枝番更新)が発表されるたびに次の6点を確認すると、乗り換えの要否を落ち着いて判断できる。

1. **ベンチマークの伸びが自社の用途に関係するか**: コーディング用途なのにMMLUの数ポイント差だけを理由に乗り換えるのは効果が薄い。用途に対応するベンチマーク(上表参照)で明確な差があるかを見る
2. **移行コスト(プロンプトの作り直し)が発生するか**: モデルが変わると、同じプロンプトでも出力形式や口調が変化することがある。JSON出力の形式・システムプロンプトの効き方・ツール呼び出しの挙動などを、本番投入前に「過去の失敗事例」を集めた回帰テスト用データセット(数十件程度でよい)で必ず確認する
3. **料金体系が変わっていないか**: 新モデルは旧モデルより高額な場合も安価な場合もある。1トークンあたりの単価だけでなく、思考過程(reasoning)にかかるトークン量や、DeepSeekのような時間帯別課金の有無も合わせて確認する(逆に、当初は値上げが予告されていても、Claude Sonnet 5のように撤回されるケースもある)
4. **旧モデルの提供終了(廃止)時期が迫っていないか**: 各社は旧モデルを一定期間後にAPIから廃止することが多い(例: Claude Opus 4.1は2026年8月に提供終了)。乗り換えが「したいから」ではなく「せざるを得ない」タイミングかどうかも判断材料になる
5. **提供地域・利用条件が自社の契約と地政学リスクに左右されないか**: 2026年6月のClaude Fable 5/Mythos 5一時停止のように、政府の輸出規制で予告なく利用不可になった事例がある。特に最上位・最新モデルを本番の中核業務に組み込む場合は、廃止予告なしに使えなくなるリスクをどこまで許容できるか(=旧モデルや代替ベンダーへの切替手段を確保しているか)も検討に含める
6. **自社の契約プランで実際に使えるモデルか**: GPT-6 Astraのように、ラボ自身の安全性審査(Preparedness Framework等)を理由に一般提供が数週間〜数か月にわたって段階的に行われるケースが出てきた。「発表された最上位モデル」と「自社の契約(無料/Plus/Enterprise等)で今日使えるモデル」は別物であることを前提に、稟議のタイミングをずらす

上記6点のうち、**「1. 用途に関係するベンチマークで明確な差がある」「4. 廃止が迫っている」「5. 地政学リスクで利用不可になった」のいずれかに該当しない限り、慌てて乗り換える必要はない**、というのが実務的な目安になる。逆に、エージェント的な複数ステップ作業を任せる用途では、METRタイムホライゾンのような「作業をやり切る力」の伸びが大きい場合は優先的に検証する価値がある。

## 実務での使い方

### 主要モデルの価格帯(2026年9月4日時点、API料金・100万トークンあたり)

| モデル | 入力 | 出力 | 文脈window |
|---|---|---|---|
| GPT-6 Astra(最上位・9月3日発表) | $10(高速モードは$20) | $50(高速モードは$100) | 約105万トークン |
| GPT-5.6 Sol | $5 | $30 | – |
| GPT-5.6 Terra(中間) | $2.50 | $15 | – |
| GPT-5.6 Luna(廉価版) | $1 | $6 | – |
| Claude Fable 5.1(最上位・9月1日発表) | $10(キャッシュ読み込みは$0.25、従来比75%減) | $50 | 100万トークン |
| Claude Opus 5 | $5(高速モードは$10) | $25(高速モードは$50) | 100万トークン |
| Claude Sonnet 5 | $2(恒久価格。予定されていた$3への値上げは撤回) | $10 | 100万トークン |
| Gemini 3.7 Flash | $0.75(2026年内の導入価格。2027年以降$1.50) | $3.75(2027年以降$7.50) | 約105万トークン |
| Grok 4.6 | $2(キャッシュ利用時割引あり) | $6 | 50万トークン |
| Kimi K3(Moonshot AI) | $3 | $15 | 100万トークン |
| Muse Glimmer(Meta、オープンウェイト) | 無料(自社サーバー・ローカルGPUで実行) | – | – |
| Muse Spark 1.2(Meta、通常プラン) | $1.25 | 非公開(プロンプト等の学習提供に同意する「contributor」プランは$0.10/$0.20) | 100万トークン |
| DeepSeek V4 Pro | $0.435(通常時。ピーク時間帯は約2倍) | $0.87(同上) | 100万トークン |
| DeepSeek V4 Flash | $0.14 | $0.28 | 100万トークン |

**業務での含意**: 最上位モデル(Astra・Fable 5.1)と廉価モデル(DeepSeek V4 Flash等)の間には価格で1桁〜2桁の差がある。すべての依頼を最上位モデルに投げるのではなく、「下書き・大量処理は廉価モデル、最終チェック・複雑な推論は上位モデル」という階層運用(モデルルーティング)が費用対効果を大きく左右する。GPT-5.6が3ティア構成を採ったのも、この使い分けを前提にした価格設計であり、GPT-6 Astra登場後もGPT-5.6ファミリーは併存して中位〜廉価帯を担っている。また、Metaの「contributor」プランのように自社のプロンプト・生成内容を学習データとして提供する代わりに大幅割引を受けられる料金プランや、Muse Glimmerのように無料でローカル実行できるオープンウェイトモデルも選択肢として広がっており、機密情報の取り扱いポリシーと合わせて確認すべきポイントである。

### 情報収集の仕組み化

- **一次情報を定点観測する**: OpenAI(openai.com/news)、Anthropic(anthropic.com/news)、Google(blog.google、cloud.google.com/blog)の公式発表を、新モデルのリリースノートとして確認する習慣をつける
- **リーダーボード横断サイトを併用する**: Artificial Analysis、LMArena(旧LMSYS Chatbot Arena)など、複数モデルのベンチマークを横並びで見られるサイトを併用すると、各社の自己申告スコアだけに頼らずに済む
- **自社専用の「回帰テストセット」を持つ**: 自社の代表的な依頼(問い合わせ回答、コード修正、資料要約など)を20〜50件程度集めておき、新モデル登場のたびに同じ入力を通して出力の質を比較する。promptfoo・DeepEval・Ragasなど、この比較を自動化するオープンソースのテストツールも普及している

### コピペで使える実例: 新モデル導入の検証手順テンプレート

社内で「新モデルに乗り換えるか」を検討する際、次のチェックリストをそのまま議事録・稟議のたたき台に使える。

```
## 新モデル導入検討シート

- 対象モデル: (例: GPT-5.6 Sol / Claude Opus 5 / Gemini 3.5 Pro)
- 現行モデルからの主な変更点: (例: コーディング系ベンチマークが◯pt向上)
- 自社用途との関連度: (高/中/低。関連するベンチマーク名を記載)
- 移行コスト: プロンプト修正の要否(要/不要)、想定工数
- 料金への影響: 現行比で(上昇/同等/下落)、想定コスト増減(時間帯別課金の有無も確認)
- 廃止予定: 現行モデルのAPI提供終了予定日(不明な場合は要確認)
- 提供地域・規制リスク: 輸出規制等で利用不可になる可能性(高/中/低)
- 判定: (今回は見送り / 小規模検証へ進む / 全面移行を検討)
```

### 主要ツールでの「使っているモデル」の確認場所

| ツール | モデル名の確認・切り替え場所 |
|---|---|
| ChatGPT | 画面上部のモデル選択メニュー、または「設定→General」でデフォルトモデルを確認 |
| Claude.ai | 画面左上のモデル名表示、または新規チャット作成時のモデル選択プルダウン |
| Gemini | 画面上部のモデル選択(Pro/Flash等)、法人向けはGoogle Cloudコンソールの「Vertex AI→Model Garden」 |
| API利用時(開発者向け) | リクエストに含めるモデルID(例: `gpt-6-astra`、`gpt-5.6-sol`、`claude-fable-5-1`、`claude-opus-5`)を各社ドキュメントで確認。モデルIDは頻繁に増減するため、廃止予定(deprecation)のお知らせをAPIダッシュボードで定期確認する |

## 注意点・よくある誤解

- **ベンチマークの1位=業務での最適解ではない**: ベンチマークは特定のタスク設計における成績であり、実際の業務データ・社内文書・独自の判断基準への適合度までは測れない。「ベンチマーク1位のモデルに入れ替えたら業務の精度が上がるはず」という前提は誤りで、自社データでの検証が必須
- **主要ラボ自身が設計したベンチマークには利益相反リスクがある**: GDPvalはOpenAI主導、Frontier-BenchはAnthropicが公開した指標であり、自社モデルの強みを反映しやすい設計になっていないかを意識する必要がある。第三者(Artificial Analysis等)による再現・独立採点の結果と合わせて見るのが実務的である
- **ベンチマークの汚染(contamination)・欠陥は珍しくない**: SWE-bench VerifiedもProも、それぞれ問題が発覚して評価対象から外れた経緯がある。「発表直後に急にスコアが跳ね上がったベンチマーク」や「短期間でスコアが不自然に伸びているベンチマーク」は汚染・過学習・採点抜け穴の悪用を疑う視点を持つ
- **ベンチマークの飽和に注意する**: MMLUやHumanEvalのように上位モデルが軒並み高得点に達したベンチマークは、2026年時点ではすでに見出しに使われなくなっている。数ポイントの差はほぼ誤差の範囲であり、優劣の根拠にならない。飽和したベンチマークでの「僅差の1位」を過度に強調する発表には注意する
- **評価団体・条件・版によってスコアが変わる**: 同じベンチマークでも、公式発表(ベンダー自己申告)と第三者評価団体(Artificial Analysis等)でスコアが異なることがある。合成指標(Intelligence Index等)も版が更新されると順位が入れ替わるため、見出しの数字だけでなく、どの条件・どの時点の版で測定されたかを確認する
- **発表(アナウンス)と一般提供(GA)は別物**: Gemini 3.5 ProのようにI/Oでの予告から3か月以上経っても一般提供に至らない例がある。「発表された」ニュースだけを見て「もう使える」と誤解しないこと
- **地政学リスクは新しい不確実性要因である**: 2026年6月のClaude Fable 5/Mythos 5一時停止のように、性能や価格ではなく政府の輸出規制で予告なくモデルが使えなくなる事例が実際に起きている。最上位・最新モデルを本番の基幹業務に組み込む際は、代替モデルへの切替手段を用意しておく
- **「ベンチマークを飽和させた」という発表は測定条件をセットで確認する**: 2026年9月のGPT-6 Astraは「ARC-AGI-3を飽和(99.9%)」と発表されたが、これはOpenAI独自のハーネス(モデルの内部状態を引き継ぐ仕組み、1問あたり数万円規模のコスト)での数字であり、ARC Prize側の標準的な採点条件では62.7%にとどまった。「〇〇ベンチマークで過去最高」という見出しを見たら、自己申告か第三者評価か、どのハーネス・ツール利用条件でのスコアかを必ず確認する
- **安全性審査による段階公開は、ベンチマーク1位=即日使えるとは限らないことを意味する**: GPT-6 Astraは自社のPreparedness Framework上で「Critical」水準のサイバー能力と判定され、一般提供前に安全対策の期間を挟み、その後も認可企業→Enterprise→Plus/Pro/Businessの順で段階的に展開された。発表日と「自社の契約プランで実際に使える日」は別物であると理解しておく
- **「エージェントとして使える」はベンチマークだけでは判断できない**: METRのタイムホライゾンのような指標はソフトウェア関連タスクに偏っており、営業・法務・カスタマーサポートのような業務にそのまま当てはまるとは限らない。エージェント運用を検討する際は、[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)で扱った「向く業務・向かない業務」の判断軸と併用する
- **本ページは「生モノ」である**: モデル名・スコア・リリース時期は数週間〜数か月で古くなる。読む時点・記事化する時点で、必ず各社公式発表とベンチマーク元サイトの最新情報を確認すること。本リポジトリの運用ルール上も、本ページは7日以上経過したら増強・最新化の対象になる

## 最初の一歩

自社で使っている主要ツール(ChatGPT・Claude・Gemini等)について、「今どのモデル名を使っているか」を1つ確認し、そのモデルの提供終了(廃止)予定が公式ドキュメントに出ていないかを見てみる。次に新モデルの発表を目にしたときは、本ページの「乗り換え判断チェックリスト」の6項目に当てはめて即断せず検討する習慣をつけることが、最初の一歩になる。

## 関連トピック

- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [生成AI業界の主要プレイヤーと動向(資金調達・提携・戦略)](ai-industry-major-players-trends.md)
- [LLMのモデルの種類と選び方](../part02-llm-basics/model-types-and-selection-basics.md)
- [推論モデル(Reasoning Model)の基本](../part02-llm-basics/reasoning-model-basics.md)

## 更新履歴

### 2026-09-04: GPT-6 Astra・Claude Fable 5.1という2大世代交代モデルの投入を反映して最新化
- **内容**: OpenAIが世代番号を繰り上げた最上位モデル「GPT-6 Astra」を9月3日に発表(自社Preparedness Framework上で初の「Critical」水準サイバー能力と判定され、認可企業・Enterprise優先の段階公開、$10/$50・約105万トークン文脈window、ARC-AGI-3で99.9%〈標準採点では62.7%〉・FrontierMath Tier 4で97.6%等)、Anthropicが「Claude Fable 5.1」を9月1日に発表(公開済み全ベンチマークでOpus 5・旧Fable 5を上回り、キャッシュ読み込み単価を75%減の$0.25に)したことを反映し、主要ラボの系譜表・価格表を全面更新。あわせてGoogleのGemini 3.7 Flash(8月13日)、MetaのオープンウェイトMuse Glimmer(8月10日)、DeepSeekのV4-Flash-0731・V4-Flash-Vision-Exp(8月下旬)を追記。ARC-AGI-3の「99.9% vs 62.7%」がハーネス(採点条件)依存で変わる典型例であることをベンチマーク表・注意点に追加し、Artificial Analysis Intelligence Indexの9月時点の首位(Claude Fable 5.1)を反映。安全性審査による段階公開という新しい可用性リスクを、乗り換え判断チェックリストと注意点に追加
- **出典**: [OpenAI公式X投稿: GPT-6 Astra rollout](https://x.com/OpenAI/status/2095595757072191802)、[Bloomberg: OpenAI Rolls Out GPT-6 Astra Model With Added Cyber Guardrails](https://www.bloomberg.com/news/articles/2026-09-03/openai-rolls-out-gpt-6-astra-model-with-added-cyber-guardrails)、[Axios: OpenAI releases new model GPT-6 Astra, says it may represent AGI](https://www.axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman)、[MarkTechPost: OpenAI Releases GPT-6 Astra — A 1.05M-Context Computer-Use Model Gated Behind a 'Critical' Cyber Threshold](https://www.marktechpost.com/2026/09/03/openai-releases-gpt-6-astra-a-1-05m-context-computer-use-model-gated-behind-a-critical-cyber-threshold/)、[ARC Prize: OpenAI's GPT-6 Astra on ARC-AGI-3](https://arcprize.org/blog/astra)、[officechai: GPT-6 Astra "Major Breakthrough" On ARC-AGI-3 With Score Of 62%](https://officechai.com/ai/gpt-6-astra-major-breakthrough-on-arc-agi-3-with-score-of-62/)、[Artificial Analysis: GPT-6 Astra model page](https://artificialanalysis.ai/models/gpt-6-astra)、[MarkTechPost: Anthropic Releases Claude Fable 5.1 and Claude Mythos 5.1](https://www.marktechpost.com/2026/09/01/anthropic-releases-claude-fable-5-1-and-claude-mythos-5-1-52-6-on-terminal-bench-science-and-75-cheaper-cache-reads/)、[MacRumors: Anthropic Launches Claude Fable 5.1 With Lower Costs and Fewer False Positives](https://www.macrumors.com/2026/09/01/anthropic-claude-fable-5-1/)、[DataCamp: Claude Fable 5.1 — Features, Benchmarks, and Pricing](https://www.datacamp.com/blog/claude-fable-5-1)、[BenchLM.ai: Artificial Analysis Intelligence Index Leaderboard (September 2026)](https://benchlm.ai/benchmarks/artificialanalysis)、[9to5Google: Gemini 3.7 Flash launches three weeks after last model](https://9to5google.com/2026/08/13/gemini-3-7-flash-launch/)、[Google Blog: Gemini 3.7 Flash — our most intelligent workhorse model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-3-7-flash/)、[The AI Rankings: Gemini 3.5 Pro Release Date — Three Delays and Still Unreleased](https://theairankings.com/google/gemini-3-5-pro/)、[Forbes: Meta Turns Muse Glimmer Into A Local AI Model That Undercuts The Cloud](https://www.forbes.com/sites/jonmarkman/2026/08/11/meta-unveils-muse-glimmer-a-30b-parameter-ai-model-that-runs-locally/)、[Meta AI Research: Introducing Muse Glimmer](https://research.meta.ai/blog/introducing-muse-glimmer-open-agentic-model)、[Yotta Labs: DeepSeek V4 — Release Date, Specs, and How to Access It](https://www.yottalabs.ai/post/deepseek-v4-release-date-specs-how-to-access-2026)

### 2026-08-14: Claude Opus 5・Grok 4.6・DeepSeek V4 Pro 0813等の投入とベンチマーク重心の変化を反映して最新化
- **内容**: Anthropicが噂されていた「Honeycomb」ではなく正式名称「Claude Opus 5」を7月24日に発表(Fable 5に迫る性能を半額程度で提供、Claude Max/Proの既定・最上位モデルに)、Claude Sonnet 5の$2/$10価格を8月10日に恒久化(予定していた値上げを撤回)、Grok 4.5の後継Grok 4.6の一般公開(8月12日)、Meta Muse Spark 1.2・Muse Codeの投入(8月5日、contributor料金プラン新設)、DeepSeek V4 Proの改訂版「0813」がプレビューを終えて正式版に(8月12〜13日)、Gemini 3.5 Proがさらに延期し続けている状況を反映して主要ラボの系譜表・価格表を更新。GDPval/GDPval-AA・Frontier-Benchという「実務代替性」を測る新しい主要ベンチマークを追加し、MMLU等の旧来指標が見出しから外れつつある潮流を明記。Artificial Analysis Intelligence Index(v4.0)の8月時点の順位(Claude Opus 5が首位)を反映し、Chatbot Arenaの「Leaderboard Illusion」問題を注意点に追加
- **出典**: [Anthropic: Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)、[Axios: Anthropic releases new model, Opus 5](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5)、[CloudZero: Claude Opus 5 pricing](https://www.cloudzero.com/blog/claude-opus-5-pricing/)、[techjournal.org: Claude Sonnet 5 Pricing Now Permanent](https://techjournal.org/claude-sonnet-5-pricing-now-permanent)、[TechCrunch: Google releases three new Gemini models — but no 3.5 Pro](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)、[Google: Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)、[llm-stats.com: Grok 4.6 — xAI's Agent-Focused Frontier Model](https://llm-stats.com/blog/research/grok-4.6-launch)、[Meta AI Research: Introducing Muse Code and Muse Spark 1.2](https://research.meta.ai/blog/introducing-muse-code-and-muse-spark-1-2)、[eesel AI: Meta Muse Spark 1.2 — what changed, what it costs](https://www.eesel.ai/blog/meta-muse-spark-12)、[Unite.AI: DeepSeek Ships V4 Pro as Its Flagship Model Leaves Preview](https://www.unite.ai/deepseek-ships-v4-pro-as-its-flagship-model-leaves-preview/)、[South China Morning Post: DeepSeek's updated V4 Pro AI model struggles on benchmarks, shines in cybersecurity](https://www.scmp.com/tech/big-tech/article/3363895/deepseeks-updated-v4-pro-ai-model-struggles-benchmarks-shines-cybersecurity)、[Northflank: Kimi K3 — benchmarks, pricing, hardware requirements](https://northflank.com/blog/what-is-kimi-k3-self-hosting)、[BenchLM.ai: Artificial Analysis Intelligence Index Leaderboard (August 2026)](https://benchlm.ai/benchmarks/artificialanalysis)、[codersera: Claude Opus 5 Benchmarks Explained — Frontier-Bench, ARC-AGI-3 and SWE-bench](https://codersera.com/blog/claude-opus-5-benchmarks-explained-2026/)、[AiCE-Lab: The Complete Guide to LLM Benchmarks (2026)](https://www.aice-lab.org/posts/llm-benchmarks-complete-guide-2026/)

### 2026-07-23: 主要モデルの系譜・価格・ベンチマーク動向を全面的に最新化
- **内容**: GPT-5.6ファミリー(Luna/Terra/Sol)の一般提供開始、Claude Sonnet 5・Fable 5/Mythos 5(輸出規制の一時停止と解除)・未発表のOpus 5(Honeycomb)の状況、Gemini 3.5 Proの度重なる延期、Grok 4.5の一般公開、Kimi K3(2.8兆パラメータのオープンウェイトモデル)、DeepSeek V4正式提供とピーク時間帯課金を反映して主要ラボの系譜表を刷新。SWE-bench Proの約3割欠陥発覚によるOpenAIの推奨撤回、METR Time Horizon 1.1による指標改定、LMArena/Artificial Analysis Intelligence Indexの版・時期によるランキング変動を追記。政府の輸出規制がモデルの入手可能性に影響する新しいリスクとして「乗り換え判断チェックリスト」に追加し、主要モデルの料金表を新設
- **出典**: [OpenAI: GPT-5.6](https://openai.com/index/gpt-5-6/)、[CNBC: OpenAI to publicly release GPT-5.6](https://www.cnbc.com/2026/07/08/openai-expanding-gpt-5point6-ai-model-release-ending-government-limits.html)、[MarkTechPost: OpenAI Releases GPT-5.6](https://www.marktechpost.com/2026/07/09/openai-releases-gpt-5-6-a-three-tier-model-family-with-programmatic-tool-calling/)、[OpenAI: Separating signal from noise in coding evaluations](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)、[Anthropic: Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)、[TechCrunch: Anthropic launches Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)、[Claude Platform Docs: Introducing Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)、[Al Jazeera: US lifts restrictions on Anthropic's Fable and Mythos](https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says)、[CNN: White House asks OpenAI to limit its next model release](https://edition.cnn.com/2026/06/25/tech/openai-limit-release-white-house)、[explainx.ai: Claude Opus 5 Release Date Rumors](https://explainx.ai/blog/claude-opus-5-release-speculation-july-2026)、[HackerNoon: Google Delays Gemini 3.5 Pro to July 17](https://hackernoon.com/google-delays-gemini-35-pro-to-july-17-the-strategic-play-behind-the-scrapped-base-model)、[TechCrunch: SpaceXAI releases Grok 4.5](https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/)、[Tom's Hardware: Moonshot releases 2.8 trillion parameter Kimi K3](https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3)、[TechNode: DeepSeek to launch V4 in mid-July with new peak-time API pricing](https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/)、[CloudZero: DeepSeek pricing 2026](https://www.cloudzero.com/blog/deepseek-pricing/)、[VentureBeat: Meta launches new proprietary AI model Muse Spark](https://venturebeat.com/technology/goodbye-llama-meta-launches-new-proprietary-ai-model-muse-spark-first-since)、[METR: Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/)、[LessWrong: METR Time Horizons — Now 10x/Year](https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year)

### 2026-07-07: 初版執筆
- **内容**: OpenAI・Anthropic・Google・xAI・Meta・DeepSeekの直近1年のモデル系譜と更新頻度の整理表、主要ベンチマーク(MMLU/MMLU-Pro、GPQA Diamond、SWE-bench Verified/Pro、ARC-AGI-2/3、METRタイムホライゾン、HLE、Chatbot Arena)の「何を測るか・過信すると危険な理由」表、新モデル登場時の乗り換え判断チェックリスト(4項目)、回帰テストの実務手順、主要ツールでのモデル確認場所を整理
- **出典**: [OpenAI: Why we no longer evaluate SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)、[blockchain.news: OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)、[TechCrunch: OpenAI's GPT-5 is here](https://techcrunch.com/2025/08/07/openais-gpt-5-is-here/)、[TechCrunch: Google launches Gemini 3 with new coding app and record benchmark scores](https://techcrunch.com/2025/11/18/google-launches-gemini-3-with-new-coding-app-and-record-benchmark-scores/)、[Google Cloud Blog: Gemini 3 is available for enterprise](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-is-available-for-enterprise)、[Anthropic: Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)、[Anthropic: Redeploying Claude Fable 5](https://www.anthropic.com/news/redeploying-fable-5)、[MacRumors: Anthropic's Claude Fable 5 Available Again After U.S. Lifts Export Controls](https://www.macrumors.com/2026/07/01/anthropic-fable-5-relaunch/)、[felloai: Best AI Models in July 2026](https://felloai.com/best-ai-models/)、[wavespeed.ai: June 2026 AI Launch Wave](https://wavespeed.ai/blog/posts/june-2026-ai-launch-wave/)、[labs.adaline.ai: ARC-AGI In 2026 — Why Frontier Models Still Don't Generalize](https://labs.adaline.ai/p/what-is-the-arc-agi-benchmark-and)、[LessWrong: METR Time Horizons — Now 10x/Year](https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year)、[METR: Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/)、[FourWeekMBA: Lmsys Chatbot Arena Hits $100M](https://fourweekmba.com/ai-arena-ai-leaderboard-100m-business-model/)、[Artificial Analysis: Intelligence Benchmarking Methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
