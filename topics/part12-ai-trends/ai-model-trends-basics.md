---
title: "生成AIの最新モデル動向(2026年:主要モデルの進化とベンチマークの見方)"
part: 12
chapter: 第1章 技術トレンド
tags: [モデル動向, ベンチマーク, GPT-5, Claude, Gemini, モデル選定]
created: 2026-07-07
updated: 2026-07-23
---

# 生成AIの最新モデル動向(2026年:主要モデルの進化とベンチマークの見方)

## これは何か

「また新しいモデルが出たらしいが、乗り換えるべきか」「ベンチマークで1位と謳っているが、それは業務で本当に賢いということなのか」——生成AIの主要モデルは数か月おきに更新され、そのたびに「過去最高スコア」を掲げた発表が続く。しかし発表の頻度自体が速すぎて、どの更新が実務に影響するレベルの進化で、どれが数字上のマイナーチェンジに過ぎないのかを見極めないまま「とりあえず最新モデルに乗り換える」を繰り返すと、移行コストばかりがかさむ。本ページは、2026年7月23日時点の主要モデルの動向を整理した上で、ベンチマークという「モデルの成績表」の読み方と、新モデル登場時に乗り換えるかどうかを判断する実務的な基準を示す。

**大前提として、モデル名・リリース時期・ベンチマークの数字は数週間単位で更新される。** 本ページは2026年7月23日時点のスナップショットであり、記事の材料に使う際は必ず各社公式発表で最新状況を確認すること。

## 仕組み・背景

### なぜこれほど頻繁に新モデルが出るのか

OpenAI・Anthropic・Googleなど主要ラボ(AI研究開発企業)は、(1)数週間〜数か月ごとの「ナンバリングの小刻みな更新」と、(2)半年〜1年に一度の「世代交代」を組み合わせて発表するのが基本パターンになっている。さらに、最上位モデルは一般提供の前に「限定パートナー向けプレビュー」として先出しされることも増えている(例: OpenAIのGPT-5.6は2026年6月26日にまず信頼できる一部組織限定のプレビューとして提供され、7月9日に一般提供に切り替わった)。

**2026年に入ってからの新しい変数として、各国政府による輸出規制・提供制限がモデルの入手可能性そのものに影響するようになった点も見逃せない。** 2026年6月、米政権は国家安全保障を理由にAnthropicへ、最上位モデルのClaude Fable 5・Mythos 5を非米国籍ユーザー全員に対して即時停止するよう指示し、Anthropicは予告なく世界中の全顧客への提供を止めた。同時期、ホワイトハウスはOpenAIに対してもGPT-5.6の提供範囲を政府承認済みパートナーに限定するよう要請している。Anthropicへの規制は7月1日に解除され、Fable 5/Mythos 5は世界展開を再開したが、こうした「性能や価格ではなく地政学的な理由で、契約中のモデルが突然使えなくなる」リスクは、今後もモデル選定の考慮事項に加える必要がある([Al Jazeera](https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says)、[CNN](https://edition.cnn.com/2026/06/25/tech/openai-limit-release-white-house))。

### 主要ラボの現在地(2026年7月23日時点)

| ラボ | 現在の主力モデル | 補足 |
|---|---|---|
| OpenAI | **GPT-5.6ファミリー**(Luna/Terra/Sol の3段階。2026年6月26日に限定プレビュー→7月9日に一般提供) | Sol が最上位・最高価格帯。3ティア構成で「コスト重視の業務」と「難しい業務」を使い分けやすくしたのが特徴 |
| Anthropic | **Claude Opus 4.8**(5月28日)、**Claude Sonnet 5**(6月30日、無料・Proプランの既定モデル)、**Claude Fable 5 / Mythos 5**(最上位。輸出規制で一時停止後、7月1日に世界展開再開) | 次世代Opus(社内呼称「Honeycomb」、Opus 5とも噂される)が7月9日に開発ツールCursorのモデル一覧に一時的に表示され話題になったが、7月23日時点で正式発表はない |
| Google | **Gemini 3.1 Pro**が現行の一般提供モデル。次期主力の**Gemini 3.5 Pro**は5月のGoogle I/Oで予告されたが、6月→7月→7月17日と延期が続き、7月23日時点でも一般提供に至っていない(Vertex AIでの企業向け限定プレビューのみ) | Bloombergの報道では、ハルシネーション率など内部の品質基準を満たせず、ベースモデルを作り直しているとされる |
| xAI | **Grok 4.5**(7月8日に一般公開。50万トークンの文脈window、MoE構成) | SpaceX・Tesla向けの非公開ベータを経て一般公開。イーロン・マスク氏は「Opus級の性能をより高速・低コストで」と位置付ける |
| Meta | オープンウェイト(モデルの重みを公開し自社サーバーで動かせる方式)の Llama 4 Scout/Maverick は提供継続。最上位のLlama 4 Behemothは未公開のまま。一方でMeta Superintelligence Labsは非公開の新モデル「Muse Spark」を投入 | 「Llama=オープンウェイトの旗手」という位置付けから、非公開モデルとの併存路線に転換しつつある |
| Moonshot AI(中国) | **Kimi K3**(7月16日にAPI提供開始、7月27日に重み公開予定。2.8兆パラメータで過去最大級のオープンウェイトモデル) | 独立系ベンチマークでClaude Fable 5・GPT-5.6 Solに次ぐ上位に位置し、コーディング系の一部評価では上位モデルを上回るとの報告もある |
| DeepSeek(中国) | **DeepSeek V4 Pro/Flash**(4月24日プレビュー→7月中旬に正式提供、ピーク時間帯課金を新規導入) | 低価格路線を継続。北京時間の業務時間帯(9-12時・14-18時)は基本料金の約2倍になる時間帯別価格を採用した点が実務上のポイント |

この一覧からわかる実務上のポイントは、「モデル名の枝番更新は数週間〜数か月ごとに動くのが常態であり、その都度乗り換えを検討する必要はない」ということと、「発表(アナウンス)と一般提供(GA)の間には数週間〜数か月のタイムラグがあり得る」ということである(Gemini 3.5 Proのように、発表から2か月以上遅延することもある)。乗り換えを検討すべきかどうかは、後述の「使いどころ・使い分け」で扱う判断軸で考える。

### ベンチマークとは何か、なぜ複数ある必要があるのか

「ベンチマーク」とは、モデルの能力を定量的に比較するための共通テストである。1つのベンチマークだけでは能力の全体像を測れないため、知識・推論・コーディング・エージェント的な実行力など、測る対象ごとに異なるベンチマークが使われる。

**主要ベンチマークの一覧(2026年7月時点でよく引用されるもの)**

| ベンチマーク | 何を測るか | 過信すると危険な理由 |
|---|---|---|
| MMLU / MMLU-Pro | 57科目(のちに拡張)にわたる知識・選択式の推論力 | 上位モデルが軒並み高得点に達し「飽和」(スコアの差が能力差を反映しなくなる状態)しており、上位モデル間の差はほぼ誤差の範囲に入っている |
| GPQA Diamond | 生物・物理・化学の博士(PhD)課程レベルの専門問題 | 高スコア化が進み、上位モデル同士の差が数ポイントしかない領域に入ってきている。「専門家超え」の見出しだけでなく、どの版・条件でのスコアかを確認する必要がある |
| SWE-bench Verified / SWE-bench Pro | 実際のGitHub issueをどれだけ自力で修正できるか(実務に近いコーディング能力) | **この1年で「信頼できるコーディング指標」の座が二度覆っている。** OpenAIは2026年2月、Verifiedで失敗した問題の約6割がテスト自体の欠陥だったとして同指標の採用を取りやめ、後継のSWE-bench Proへの移行を推奨した。ところが同じOpenAIが2026年7月8日、今度はPro自身を独自監査した結果を公表し、公開されている731タスクのうち約3割が「テストが厳格すぎて正しい実装まで不合格にする」などの欠陥を抱えていたとして推奨を撤回した。Proの公開データセットでの上位モデルのスコアは8か月で23.3%から80.3%まで上昇していたが、これは純粋な能力向上では説明がつかない伸び方であり、汚染(データ漏洩)や採点基準の抜け穴を突いた最適化を疑うべき事例として扱われている |
| ARC-AGI-2 / ARC-AGI-3 | 見たことのないパターンから規則を発見する抽象推論力(新規状況への適応力) | 汚染(データ漏洩)への耐性を意識して設計されているが、スコアの絶対値だけでなく「どれだけの計算コストをかけて解いたか」(1問あたりの推論コスト)を無視すると実用性の判断を誤る。ARC-AGI-3ではトップモデルでも1%未満にとどまり、人間には簡単でもAIには依然として難しい領域があることを示している |
| METR タイムホライゾン(時間水平線) | 人間なら何分〜何時間かかる作業を、AIエージェントがどこまで自律的にやり切れるか(実行の持続力) | 2026年1月の指標改定(Time Horizon 1.1)でタスク数を170→228件に拡充した結果、「達成できるタスクの長さが倍増する速度」の推定値自体が7か月から約3か月(2024年以降のトレンド)へ上方修正された。**測定手法の改定でヘッドライン数値そのものが動く**という好例であり、測定対象もソフトウェア関連タスクに偏っているため、あらゆる業務に一般化はできない |
| Humanity's Last Exam(HLE) | 100以上の分野にわたる、インターネット上に解答が存在しない超高難度の問題 | 採点する評価団体によってスコアが10〜20ポイント単位でぶれることがあり、「公式スコア」がどの評価基準によるものかを確認しないと単純比較できない |
| Chatbot Arena(LMArena) | 人間による2モデルのブラインド比較投票に基づく好感度ランキング | 「回答が長い」「フォーマットが整っている」「愛想がよい」回答が人間投票で有利になりやすいバイアスが指摘されており、実務上の正確性そのものを測っているわけではない。運営が主要ラボから収益を得るビジネスモデルに変わったことで中立性への懸念も指摘されている。加えて、2026年7月だけでもFable 5(7/1)・Grok 4.5(7/8)・GPT-5.6(7/9)・Kimi K3(7/16)と主要モデルが立て続けに投入されており、投票数が十分に蓄積するまでランキングが数週間単位で入れ替わり続けている状態にある |
| Artificial Analysis Intelligence Index | 複数のベンチマークを合成した総合指数 | 指数の版によって順位が変わる。7月時点のある版ではClaude Opus 4.8が首位(61.4)だったが、Fable 5・Kimi K3を反映した更新版ではClaude Fable 5が首位(59.9%)、GPT-5.6 Sol(58.9%)、Kimi K3(57.1%)の順に変わっている。「合成指数だから絶対」ではなく、どのテストをどう重み付けしたかという設計・版次第でランキングが動く点は個別ベンチマークと同じである |

## 使いどころ・使い分け

### ベンチマークの使い分け

| 知りたいこと | 参考にすべきベンチマーク |
|---|---|
| 知識・雑学的な受け答えの広さ | MMLU-Pro、GPQA Diamond |
| コーディング支援・自動化に使えるか | SWE-bench Pro(ただし前述の欠陥報告を踏まえ単独の絶対値は過信しない)、Codeforces系(競技プログラミング) |
| 複数ステップの作業をエージェントとして任せられるか | METRタイムホライゾン、Terminal-Bench等のエージェント系ベンチマーク |
| 人間らしい自然な受け答えの好感度 | Chatbot Arena(ただし正確性の指標ではない点に注意) |
| 未知の状況への応用力・新規性への強さ | ARC-AGI-2/3 |
| 総合的な「今どのモデルが強いか」の目安 | Artificial Analysis Intelligence Index(ただし版によって順位が変わる点に注意) |

いずれか1つの数字だけで判断せず、自社の用途に近いベンチマークを2〜3種類組み合わせて見る、あるいは合成指標を参考にするのが実務的である。ただし合成指標もどのテストをどう重み付けしたかという設計次第でランキングが変わるため、「絶対的な正解」ではなく「複数ある物差しの一つ」として扱う。

### 新モデルが出たら乗り換えるべきか:判断チェックリスト

新しいモデル(または枝番更新)が発表されるたびに次の5点を確認すると、乗り換えの要否を落ち着いて判断できる。

1. **ベンチマークの伸びが自社の用途に関係するか**: コーディング用途なのにMMLUの数ポイント差だけを理由に乗り換えるのは効果が薄い。用途に対応するベンチマーク(上表参照)で明確な差があるかを見る
2. **移行コスト(プロンプトの作り直し)が発生するか**: モデルが変わると、同じプロンプトでも出力形式や口調が変化することがある。JSON出力の形式・システムプロンプトの効き方・ツール呼び出しの挙動などを、本番投入前に「過去の失敗事例」を集めた回帰テスト用データセット(数十件程度でよい)で必ず確認する
3. **料金体系が変わっていないか**: 新モデルは旧モデルより高額な場合も安価な場合もある。1トークンあたりの単価だけでなく、思考過程(reasoning)にかかるトークン量や、DeepSeekのような時間帯別課金の有無も合わせて確認する
4. **旧モデルの提供終了(廃止)時期が迫っていないか**: 各社は旧モデルを一定期間後にAPIから廃止することが多い。乗り換えが「したいから」ではなく「せざるを得ない」タイミングかどうかも判断材料になる
5. **提供地域・利用条件が自社の契約と地政学リスクに左右されないか**: 2026年6月のClaude Fable 5/Mythos 5一時停止のように、政府の輸出規制で予告なく利用不可になった事例がある。特に最上位・最新モデルを本番の中核業務に組み込む場合は、廃止予告なしに使えなくなるリスクをどこまで許容できるか(=旧モデルや代替ベンダーへの切替手段を確保しているか)も検討に含める

上記5点のうち、**「1. 用途に関係するベンチマークで明確な差がある」「4. 廃止が迫っている」「5. 地政学リスクで利用不可になった」のいずれかに該当しない限り、慌てて乗り換える必要はない**、というのが実務的な目安になる。逆に、エージェント的な複数ステップ作業を任せる用途では、METRタイムホライゾンのような「作業をやり切る力」の伸びが大きい場合は優先的に検証する価値がある。

## 実務での使い方

### 主要モデルの価格帯(2026年7月時点、API料金・100万トークンあたり)

| モデル | 入力 | 出力 | 文脈window |
|---|---|---|---|
| GPT-5.6 Luna(廉価版) | $1 | $6 | – |
| GPT-5.6 Terra(中間) | $2.50 | $15 | – |
| GPT-5.6 Sol(最上位) | $5 | $30 | – |
| Claude Sonnet 5 | $2(〜8月末の導入価格。以降$3) | $10(以降$15) | 100万トークン |
| Claude Fable 5 | $10 | $50 | 100万トークン |
| Grok 4.5 | $2(キャッシュ利用時$0.50) | $6 | 50万トークン |
| Kimi K3(Moonshot AI) | $3 | $15 | 100万トークン |
| DeepSeek V4 Pro | $0.435(通常時。ピーク時間帯は約2倍) | $0.87(同上) | 100万トークン |
| DeepSeek V4 Flash | $0.14 | $0.28 | 100万トークン |

**業務での含意**: 最上位モデル(Fable 5・Sol)と廉価モデル(DeepSeek V4 Flash等)の間には価格で1桁〜2桁の差がある。すべての依頼を最上位モデルに投げるのではなく、「下書き・大量処理は廉価モデル、最終チェック・複雑な推論は上位モデル」という階層運用(モデルルーティング)が費用対効果を大きく左右する。GPT-5.6が3ティア構成を採ったのも、この使い分けを前提にした価格設計だと理解しておくとよい。

### 情報収集の仕組み化

- **一次情報を定点観測する**: OpenAI(openai.com/news)、Anthropic(anthropic.com/news)、Google(blog.google、cloud.google.com/blog)の公式発表を、新モデルのリリースノートとして確認する習慣をつける
- **リーダーボード横断サイトを併用する**: Artificial Analysis、LMArena(旧LMSYS Chatbot Arena)など、複数モデルのベンチマークを横並びで見られるサイトを併用すると、各社の自己申告スコアだけに頼らずに済む
- **自社専用の「回帰テストセット」を持つ**: 自社の代表的な依頼(問い合わせ回答、コード修正、資料要約など)を20〜50件程度集めておき、新モデル登場のたびに同じ入力を通して出力の質を比較する。promptfoo・DeepEval・Ragasなど、この比較を自動化するオープンソースのテストツールも普及している

### コピペで使える実例: 新モデル導入の検証手順テンプレート

社内で「新モデルに乗り換えるか」を検討する際、次のチェックリストをそのまま議事録・稟議のたたき台に使える。

```
## 新モデル導入検討シート

- 対象モデル: (例: GPT-5.6 Sol / Claude Sonnet 5 / Gemini 3.5 Pro)
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
| API利用時(開発者向け) | リクエストに含めるモデルID(例: `gpt-5.6-sol`、`claude-sonnet-5`、`claude-fable-5`)を各社ドキュメントで確認。モデルIDは頻繁に増減するため、廃止予定(deprecation)のお知らせをAPIダッシュボードで定期確認する |

## 注意点・よくある誤解

- **ベンチマークの1位=業務での最適解ではない**: ベンチマークは特定のタスク設計における成績であり、実際の業務データ・社内文書・独自の判断基準への適合度までは測れない。「ベンチマーク1位のモデルに入れ替えたら業務の精度が上がるはず」という前提は誤りで、自社データでの検証が必須
- **ベンチマークの汚染(contamination)・欠陥は珍しくない**: SWE-bench VerifiedもProも、それぞれ問題が発覚して評価対象から外れた経緯がある。「発表直後に急にスコアが跳ね上がったベンチマーク」や「短期間でスコアが不自然に伸びているベンチマーク」は汚染・過学習・採点抜け穴の悪用を疑う視点を持つ
- **ベンチマークの飽和に注意する**: MMLUのように上位モデルが軒並み高得点に達したベンチマークでは、数ポイントの差はほぼ誤差の範囲であり、優劣の根拠にならない。飽和したベンチマークでの「僅差の1位」を過度に強調する発表には注意する
- **評価団体・条件・版によってスコアが変わる**: 同じベンチマークでも、公式発表(ベンダー自己申告)と第三者評価団体(Artificial Analysis等)でスコアが異なることがある。合成指標(Intelligence Index等)も版が更新されると順位が入れ替わるため、見出しの数字だけでなく、どの条件・どの時点の版で測定されたかを確認する
- **発表(アナウンス)と一般提供(GA)は別物**: Gemini 3.5 ProのようにI/Oでの予告から一般提供まで数か月遅れる例や、Claude Opus 5(Honeycomb)のように開発ツールに一時的に露出しただけで正式発表に至っていない例がある。「発表された」ニュースだけを見て「もう使える」と誤解しないこと
- **地政学リスクは新しい不確実性要因である**: 2026年6月のClaude Fable 5/Mythos 5一時停止のように、性能や価格ではなく政府の輸出規制で予告なくモデルが使えなくなる事例が実際に起きている。最上位・最新モデルを本番の基幹業務に組み込む際は、代替モデルへの切替手段を用意しておく
- **「エージェントとして使える」はベンチマークだけでは判断できない**: METRのタイムホライゾンのような指標はソフトウェア関連タスクに偏っており、営業・法務・カスタマーサポートのような業務にそのまま当てはまるとは限らない。エージェント運用を検討する際は、[AIエージェントとは何か](ai-agent-basics.md)で扱った「向く業務・向かない業務」の判断軸と併用する
- **本ページは「生モノ」である**: モデル名・スコア・リリース時期は数週間〜数か月で古くなる。読む時点・記事化する時点で、必ず各社公式発表とベンチマーク元サイトの最新情報を確認すること。本リポジトリの運用ルール上も、本ページは14日以上経過したら増強・最新化の対象になる

## 最初の一歩

自社で使っている主要ツール(ChatGPT・Claude・Gemini等)について、「今どのモデル名を使っているか」を1つ確認し、そのモデルの提供終了(廃止)予定が公式ドキュメントに出ていないかを見てみる。次に新モデルの発表を目にしたときは、本ページの「乗り換え判断チェックリスト」の5項目に当てはめて即断せず検討する習慣をつけることが、最初の一歩になる。

## 関連トピック

- [AIエージェントとは何か](ai-agent-basics.md)
- [生成AI業界の主要プレイヤーと動向(資金調達・提携・戦略)](ai-industry-major-players-trends.md)
- [LLMのモデルの種類と選び方](../part02-llm-basics/model-types-and-selection-basics.md)
- [推論モデル(Reasoning Model)の基本](../part02-llm-basics/reasoning-model-basics.md)

## 更新履歴

### 2026-07-23: 主要モデルの系譜・価格・ベンチマーク動向を全面的に最新化
- **内容**: GPT-5.6ファミリー(Luna/Terra/Sol)の一般提供開始、Claude Sonnet 5・Fable 5/Mythos 5(輸出規制の一時停止と解除)・未発表のOpus 5(Honeycomb)の状況、Gemini 3.5 Proの度重なる延期、Grok 4.5の一般公開、Kimi K3(2.8兆パラメータのオープンウェイトモデル)、DeepSeek V4正式提供とピーク時間帯課金を反映して主要ラボの系譜表を刷新。SWE-bench Proの約3割欠陥発覚によるOpenAIの推奨撤回、METR Time Horizon 1.1による指標改定、LMArena/Artificial Analysis Intelligence Indexの版・時期によるランキング変動を追記。政府の輸出規制がモデルの入手可能性に影響する新しいリスクとして「乗り換え判断チェックリスト」に追加し、主要モデルの料金表を新設
- **出典**: [OpenAI: GPT-5.6](https://openai.com/index/gpt-5-6/)、[CNBC: OpenAI to publicly release GPT-5.6](https://www.cnbc.com/2026/07/08/openai-expanding-gpt-5point6-ai-model-release-ending-government-limits.html)、[MarkTechPost: OpenAI Releases GPT-5.6](https://www.marktechpost.com/2026/07/09/openai-releases-gpt-5-6-a-three-tier-model-family-with-programmatic-tool-calling/)、[OpenAI: Separating signal from noise in coding evaluations](https://openai.com/index/separating-signal-from-noise-coding-evaluations/)、[Anthropic: Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)、[TechCrunch: Anthropic launches Claude Sonnet 5](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/)、[Claude Platform Docs: Introducing Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)、[Al Jazeera: US lifts restrictions on Anthropic's Fable and Mythos](https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says)、[CNN: White House asks OpenAI to limit its next model release](https://edition.cnn.com/2026/06/25/tech/openai-limit-release-white-house)、[explainx.ai: Claude Opus 5 Release Date Rumors](https://explainx.ai/blog/claude-opus-5-release-speculation-july-2026)、[HackerNoon: Google Delays Gemini 3.5 Pro to July 17](https://hackernoon.com/google-delays-gemini-35-pro-to-july-17-the-strategic-play-behind-the-scrapped-base-model)、[TechCrunch: SpaceXAI releases Grok 4.5](https://techcrunch.com/2026/07/08/spacexai-releases-grok-4-5-which-elon-describes-as-an-opus-class-model/)、[Tom's Hardware: Moonshot releases 2.8 trillion parameter Kimi K3](https://www.tomshardware.com/tech-industry/artificial-intelligence/moonshot-releases-2-8-trillion-parameter-kimi-k3)、[TechNode: DeepSeek to launch V4 in mid-July with new peak-time API pricing](https://technode.com/2026/06/30/deepseek-to-launch-v4-in-mid-july-with-new-peak-time-api-pricing/)、[CloudZero: DeepSeek pricing 2026](https://www.cloudzero.com/blog/deepseek-pricing/)、[VentureBeat: Meta launches new proprietary AI model Muse Spark](https://venturebeat.com/technology/goodbye-llama-meta-launches-new-proprietary-ai-model-muse-spark-first-since)、[METR: Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/)、[LessWrong: METR Time Horizons — Now 10x/Year](https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year)

### 2026-07-07: 初版執筆
- **内容**: OpenAI・Anthropic・Google・xAI・Meta・DeepSeekの直近1年のモデル系譜と更新頻度の整理表、主要ベンチマーク(MMLU/MMLU-Pro、GPQA Diamond、SWE-bench Verified/Pro、ARC-AGI-2/3、METRタイムホライゾン、HLE、Chatbot Arena)の「何を測るか・過信すると危険な理由」表、新モデル登場時の乗り換え判断チェックリスト(4項目)、回帰テストの実務手順、主要ツールでのモデル確認場所を整理
- **出典**: [OpenAI: Why we no longer evaluate SWE-bench Verified](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/)、[blockchain.news: OpenAI Abandons SWE-bench Verified After Finding 59% of Failed Tests Were Flawed](https://blockchain.news/news/openai-abandons-swe-bench-verified-contamination-flawed-tests)、[TechCrunch: OpenAI's GPT-5 is here](https://techcrunch.com/2025/08/07/openais-gpt-5-is-here/)、[TechCrunch: Google launches Gemini 3 with new coding app and record benchmark scores](https://techcrunch.com/2025/11/18/google-launches-gemini-3-with-new-coding-app-and-record-benchmark-scores/)、[Google Cloud Blog: Gemini 3 is available for enterprise](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-is-available-for-enterprise)、[Anthropic: Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)、[Anthropic: Redeploying Claude Fable 5](https://www.anthropic.com/news/redeploying-fable-5)、[MacRumors: Anthropic's Claude Fable 5 Available Again After U.S. Lifts Export Controls](https://www.macrumors.com/2026/07/01/anthropic-fable-5-relaunch/)、[felloai: Best AI Models in July 2026](https://felloai.com/best-ai-models/)、[wavespeed.ai: June 2026 AI Launch Wave](https://wavespeed.ai/blog/posts/june-2026-ai-launch-wave/)、[labs.adaline.ai: ARC-AGI In 2026 — Why Frontier Models Still Don't Generalize](https://labs.adaline.ai/p/what-is-the-arc-agi-benchmark-and)、[LessWrong: METR Time Horizons — Now 10x/Year](https://www.lesswrong.com/posts/EYb2K9acKfyG2bome/metr-time-horizons-now-10x-year)、[METR: Time Horizon 1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/)、[FourWeekMBA: Lmsys Chatbot Arena Hits $100M](https://fourweekmba.com/ai-arena-ai-leaderboard-100m-business-model/)、[Artificial Analysis: Intelligence Benchmarking Methodology](https://artificialanalysis.ai/methodology/intelligence-benchmarking)
