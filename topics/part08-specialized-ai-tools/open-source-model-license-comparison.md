---
title: "オープンソースAIモデルのライセンス比較(商用利用時の論点)"
part: 8
chapter: 第4章 ローカル・オープンモデル
tags: [オープンソース, オープンウェイト, ライセンス, Llama, Gemma, Mistral, Apache 2.0, MIT, 法務]
created: 2026-07-25
updated: 2026-09-07
---

# オープンソースAIモデルのライセンス比較(商用利用時の論点)

## これは何か

Llama・Gemma・Mistral・Qwen・DeepSeek・GLM・Kimiなど、重みが公開され自社で動かせる「オープンウェイトモデル」は増えているが、そのライセンス条件はモデルごとにまったく異なり、「無料で公開されている=何をしても自由」ではない。自社サービスに組み込む・ファインチューニングして再配布する・生成物を販売するといった商用利用の場面では、再配布の条件、利用者数・収益の閾値、商標・命名規則、生成物の責任範囲などをモデルごとに確認しないと、契約違反や訴訟リスクを抱えたまま事業を進めてしまうことになる。しかもライセンス条件は同じモデルファミリーの中でも版が変わるたびに変化する(2026年4月にGoogleがGemmaの独自ライセンスをApache 2.0へ全面切り替えしたのが好例)。本ページは、モデル別の早見表([ローカルLLMの基本](./local-llm-basics.md)に既出)を繰り返すのではなく、**商用利用を検討する法務・調達担当者が実際に確認すべき論点**を横断的に整理する。

## 仕組み・背景

### 「オープンウェイト」と「オープンソース」は別物

- **オープンウェイト(open weight)**: 学習済みモデルの「重み」(パラメータの数値データ)だけが公開されている状態。ダウンロードして推論(実行)やファインチューニング(追加学習によるカスタマイズ)はできるが、学習に使ったデータセットや学習用コードは非公開のことが多く、モデルを"再現"することはできない
- **オープンソース(open source)**: 従来のソフトウェアの意味での「オープンソース」。重みに加えて、学習コード・十分な学習データの情報まで公開され、第三者がゼロから再構築・監査できる状態を指す

業界団体OSI(Open Source Initiative、オープンソースの定義を策定する非営利団体)は2024年に「Open Source AI Definition(オープンソースAIの定義、OSAID)」を公表し、**重みの公開だけではオープンソースと呼べない**という立場を明確にしている。この定義に照らすと、Llama・Qwen・GLM・Kimi等「オープンソース」を名乗ることが多いモデルの大半は、実際には学習データ・学習コードが非公開の「オープンウェイト」に分類される。マーケティング上の呼称と、法務・調達で確認すべき実態(ライセンス条文)は切り分けて考える必要がある。OSIはOSAID 1.0を「対話の出発点」と位置づけ、2026年を通じて課題(特に学習データの扱い)を洗い出す作業部会を運用しており、2026年第4四半期(Q4)を目処に改訂版(1.1〜2.0)を公表する計画を進めている。今後「オープンソースAI」の線引きがさらに厳密になる可能性がある(2026年9月時点で未公表)。

### ライセンスの系統(2026年9月時点)

主要なオープンウェイトモデルのライセンスは、おおむね次の系統に分類できる。ライセンス名だけを見ると同じ「Apache 2.0」「MIT」でも、**閾値条項が別立てで追加されているかどうか**で自由度が大きく変わる点に注意する。

1. **標準的なOSSライセンスをそのまま適用(完全な自由)**: Apache 2.0、MIT。ソフトウェア業界で広く使われてきた実績のあるライセンスをそのままモデルの重みに適用しており、商用利用・改変・再配布に関する制限が最も少ない。閾値条項も別立ての行為規範もない
2. **標準ライセンス+利用者数・収益に応じた追加条項(修正型)**: 見た目はMIT/Apache的だが、一定規模を超えると「モデル名の表示義務」や「別途契約」が発生する条項が追加されている設計(Kimi K2系、Mistral Medium系)。閾値未満なら実質的に標準ライセンスと変わらない
3. **独自のコミュニティライセンス(利用者数などの閾値条項付き)**: Llama Community License、Qwen Community License/Tongyi Qianwen Licenseなど。無料利用の枠を大きく取りつつ、一定規模を超える事業者には別途契約を求める「フリーミアム型」の設計
4. **独自ライセンス(累計収益閾値+セキュリティレビュー型)**: GLM-5.3のライセンスのように、直近12か月の累計収益が一定額(例: 100億ドル)を超える一部の超大手事業者のみ、提供元のセキュリティレビュー合格を商用利用の条件とする設計
5. **非商用限定ライセンス**: 研究・非商用目的に限定し、商用利用そのものを認めないタイプ(SB Intuitionsの一部モデル等)

なお、Google Gemmaは2026年4月の「Gemma 4」でこの構図が大きく変わった好例である。Gemma 1〜3は独自の「Gemma利用規約」+「禁止行為ポリシー」(下記参照)という上記でいう旧来の別枠の系統だったが、Gemma 4ではGoogleがこの独自ライセンスを廃止し、閾値条項も禁止行為ポリシーもない**素のApache 2.0**に全面移行した。ライセンスは「その時点のスナップショット」であり、同じモデルファミリーでも版が変われば系統ごと変わり得る、という点を示す事例である。

## 使いどころ・使い分け

### 主要ライセンスの横並び比較(2026年9月時点)

| 系統 | 代表モデル(2026年9月時点) | 商用利用 | 再配布・派生モデルの条件 | 利用者数・収益の閾値条項 | 商標・命名の制約 |
|---|---|---|---|---|---|
| Apache 2.0(標準OSS) | Gemma 4、Mistral Large 3/Small 4/Ministral 3、Qwen3系(35B以下中心。例外的にQwen3.5-397B-A17Bも)、gpt-oss(20B/120B)、GLM-5.3-Flash | 可(制限なし) | 著作権表示・変更点の明示のみ。特許の明示的な利用許諾(特許訴訟を起こされた場合に自身の特許ライセンスが失効する条項)あり | なし | なし(モデル名の変更も自由)。ただしgpt-ossはライセンスとは別に「gpt-oss usage policy」という行為規範が付随する(後述) |
| MIT(標準OSS) | DeepSeek(V3・V4 Pro/Flash等)、GLM-5.2 | 可(制限なし) | 著作権表示の保持のみ。Apache 2.0と異なり特許に関する明示的な取り決めがない | なし | なし |
| 修正MIT(表示義務が生じる型) | Kimi K2.6・K2.7 Code(Moonshot AI) | 可(規模を問わず利用自体は制限されない) | 基本はMIT型で自由。ただし閾値を超えると製品UI上に「Kimi K2.6」等の名称表示義務が発生する | 月間アクティブユーザー1億人超、または月間収益2,000万ドル超で表示義務(利用停止ではない) | 上記の表示義務の範囲に限定 |
| 修正MIT(収益閾値で利用不可になる型) | Mistral Medium 3.5 | 条件付きで可 | 閾値未満は概ねMIT型で自由 | 月間収益2,000万ドル超の企業は、社内利用も含め商用ライセンス契約がなければ利用不可 | 記載なし |
| 独自コミュニティライセンス(MAU閾値型) | Llama Community License(Llama 4 Scout/Maverick)、Qwen Community License 1.0/Tongyi Qianwen License(Qwen3-235B-A22B等の大型モデル) | 条件付きで可 | ライセンス全文の同梱義務、著作権表示・変更点の明示義務。Llama系は派生モデルの名称冒頭に「Llama」を含める義務・"Built with Llama"の表示義務があり、いずれもモデル出力を使って競合の非Llama/非Qwen系モデルを学習・蒸留・合成データ生成させることを禁じる条項がある | Llamaは前月の月間アクティブユーザー(MAU)が7億人超、Qwen大型モデルは月間アクティブユーザーが1億人超で提供元との別途契約が必要 | 「Llama」「Qwen」の使用は上記義務の範囲に限定。商標権は提供元に帰属し、生じた信用(グッドウィル)も提供元のものになる |
| 独自ライセンス(累計収益閾値+セキュリティレビュー型) | GLM-5.3(Zhipu AI/Z.ai) | 条件付きで可(通常の企業・個人利用は無制限) | 直近12か月の累計収益が100億ドルを超えてMaaS(Model as a Service)事業を営む事業者のみ、商用利用前にZ.aiのセキュリティレビュー合格が必要。それ以外は事実上MIT相当の自由度 | 直近12か月の累計収益100億ドル超(該当するのは一部の超大手クラウド・プラットフォーム事業者のみ) | 記載なし |
| 非商用限定ライセンス | Sarashina Model NonCommercial License(SB Intuitionsの音声合成モデル等一部) | 不可(研究・非商用利用のみ) | 非商用の範囲内でのみ改変・再配布可 | なし(そもそも商用利用不可) | 記載なし |

**判断基準の目安**

- **社内向けPoC(概念実証)・小規模な検証段階**: どのライセンスでも実質的な支障は出にくい。ただしAPI提供や外部公開を見据えるなら、この段階からライセンス条文を確認しておく
- **自社サービスに組み込んで外部提供する(SaaS化・API提供)**: Apache 2.0 / MITのモデル(Gemma 4、Mistral Large 3/Small 4、Qwen3の小型モデル、gpt-oss、DeepSeek V4、GLM-5.2/5.3-Flash等)を優先候補にする。ただし急成長が見込める事業では「修正MIT」型の閾値も無視できない。Kimi K2系はMAU1億人・月間収益2,000万ドルを超えると表示義務、Mistral Medium 3.5は月間収益2,000万ドルを超えると利用そのものに契約が必要になる
- **将来的にMAU数億人・年商数百億円規模へ育つ可能性がある大規模事業**: Llama系(7億MAU)、Qwen大型モデル(1億MAU)、Mistral Medium 3.5(月次収益2,000万ドル)は特に閾値を事業計画側と早めにすり合わせる。超大手クラウド事業者としてMaaS提供する場合はGLM-5.3のセキュリティレビュー要件も確認する
- **ファインチューニングした派生モデルを他社に再配布・販売する**: Llama系・Qwen大型モデルは名称・表示義務があるため、自社ブランドのモデルとして展開したい場合はブランディング上の制約になる。この制約を避けたい場合はApache 2.0 / MIT系のベースモデル(Mistral、Qwen小型、DeepSeek、GLM、gpt-oss等)を選ぶ
- **モデルの出力を使って別モデルを学習させる(合成データ生成・蒸留)**: LlamaやQwenの大型モデルのライセンスには、出力を使って競合の非Llama/非Qwen系モデルを学習・蒸留することを禁じる条項がある。合成データ生成のパイプラインにこれらのモデルを組み込む場合は、ライセンス条文で明示的に確認する
- **生成物(アウトプット)の権利関係を明確にしたい業務(コンテンツ制作・生成物の販売等)**: オープンウェイトモデルのライセンスは、そもそも生成物の著作権・利用権について明記していないことが多い(後述)。契約書や利用規約でのカバーが難しい場合は、生成物の権利関係を契約で明示する法人向けAPI(ChatGPT Enterprise、Claude for Enterprise等)の利用を優先する選択肢もある

## 実務での使い方

### 商用利用前に法務・調達がチェックすべき論点

1. **再配布(redistribution)の条件**: モデルそのもの、またはファインチューニング後の重みを社外(顧客・パートナー)に渡す場合、ライセンス全文の同梱義務、著作権表示の保持義務、変更点の明示義務があるかを確認する。Apache 2.0 / MITは形式的な条件のみだが、Llama系・Qwen大型モデルは前述の名称・表示義務が加わる
2. **派生モデル(derivative model)の扱い**: 「ファインチューニングしたら別物として自由に扱える」と誤解されがちだが、多くのライセンスは派生モデルにも元のライセンス条件を引き継がせる(フローダウン)設計になっている。特にLlama系は派生モデルの名称にも「Llama」を含めることを義務付けており、ファインチューニング後も元のライセンスから逃れられない。日本語ファインチューニングモデルの多くもこの点を継承している(例: ELYZAのLlama-3-ELYZA-JP-8Bは、ベースのLlama 3 Community LicenseとAcceptable Use Policyをそのまま引き継ぐ)
3. **利用者数・収益規模の閾値条項**: Llama(7億MAU超)、Qwen大型モデル(1億MAU超)、Kimi K2系(1億MAU超または月間収益2,000万ドル超)、Mistral Medium 3.5(月間収益2,000万ドル超)、GLM-5.3(直近12か月の累計収益100億ドル超)のように、規模条項の有無・内容はモデルごとにまったく異なる。自社サービスが将来その規模に到達する可能性がある場合は、契約担当者があらかじめ提供元への確認ルートを把握しておく
4. **生成物(アウトプット)の著作権・責任範囲**: OpenAI・Anthropic・Google等の法人向けAPI利用規約は生成物の権利を利用者に帰属させる条項を置いていることが多いが、オープンウェイトモデルのライセンス(Apache 2.0・MIT・Llama Community License等)は生成物の権利関係に触れていないのが実情である。生成物の著作権・第三者権利侵害リスクへの対応は、モデルのライセンスではなく自社の利用規約・契約書側で手当てする必要がある(著作権全般の論点は[生成AIの著作権リスク](../part04-risk-security/copyright-risks-in-generative-ai.md)を参照)
5. **保証・責任の所在(indemnification / liability)**: Apache 2.0・MITはいずれも「無保証(AS IS)・責任制限」を明記しており、モデルの出力が誤っていた場合や第三者の権利を侵害した場合の補償を提供元に求めることはできない。むしろライセンス条文上は利用者側が提供元へ補償(リバース・インデムニティ)する形になっていることが多く、法人向けAPIのような手厚い補償条項は期待できない
6. **商標・命名規則の制約**: 「Llama」「Qwen」「Gemma」等のモデル名・ロゴは商標として保護されており、ライセンスが認める範囲(前述の命名義務等)を超えて自社製品名やロゴに使うことはできない。マーケティング資料・プレスリリースでの表記も、各社の「ブランドガイドライン」を確認してから作成する
7. **ライセンス本体とは別の行為規範・利用ポリシーの有無**: Apache 2.0・MITというライセンス名だけを見て安心せず、提供元が別立てで「利用ポリシー(usage policy)」を運用していないか確認する。例えばOpenAIのgpt-oss(Apache 2.0)には別立ての「gpt-oss usage policy」が付随する。Gemma 4のようにライセンスと同時に行為規範自体が撤廃された例もあるため、「今どのバージョンにどの規範が付いているか」は都度最新のライセンスページで確認する

### 国内(日本)のオープンモデルの状況

日本国内の主要プレイヤーも、モデルの版によってライセンス系統が揺れている。「日本語対応」という理由だけで採用を決めず、以下のように個別に確認する。

| 提供元 | モデル例 | ライセンスの状況(2026年9月時点) |
|---|---|---|
| Preferred Networks(PFN) | PLaMo-13B・PLaMo-Embedding-1B(旧世代) / PLaMo 2・PLaMo 3(新世代) | 旧世代はApache 2.0で研究・商用とも自由。新世代(PLaMo 2以降)は独自の「PLaMo Community License」に切り替わっており、旧世代と同列に扱えない。採用前に版ごとのライセンス文面を個別確認する |
| SB Intuitions(ソフトバンク子会社) | Sarashina2.2の小型モデル・Vision系 / Sarashina2.2-TTS等の一部モデル | 小型言語モデル・Visionモデルの一部はMITで商用利用可能だが、音声合成(TTS)モデル等は「Sarashina Model NonCommercial License」で研究・非商用限定。同じSarashinaブランド内でもモデルごとにライセンスが異なる |
| ELYZA(KDDI傘下) | Llama-3-ELYZA-JP-8B / 70B | 8BはLlama 3 Community License + Acceptable Use Policyをそのまま継承(ベースのLlamaライセンスの制約をすべて引き継ぐ)。70Bは重みを公開せず、安全なAPI・協業プロジェクトを通じて企業向けに個別提供する形式で、一般公開の重みは存在しない |
| rinna | 日本語CLIP・音声認識(ASR)モデル等 | Apache 2.0 / MITいずれの例もあり、モデルごとに個別確認が必要。近年の音声系モデルはMITの例が多い |
| Sakana AI | 進化的アルゴリズムによる派生・合成モデル群 | ベースにLlama系・Qwen系等の既存オープンウェイトモデルを組み合わせて生成する手法のため、ベースモデルのライセンス(Llama Community License等)を派生モデル側にも引き継ぐ点に注意する |

日本の政府調達(デジタル庁の生成AI活用基盤「Gennai」等)でも、KDDI/ELYZAのLlama-3.1-ELYZA-JP-70BやPFNのPLaMo 2.0 Prime等、国内モデルの採用が進んでいるが、いずれも上記のとおりベースモデル由来のライセンス制約(閾値条項・命名義務等)を引き継ぐ設計になっている。国内モデルだから制約がない、と誤解しないこと。

### 確認の進め方(調達フロー)

1. Hugging Face上のモデルカードに記載されたライセンス名を確認する(例: `Apache-2.0`、`llama4`、`glm-5.3`)
2. ライセンス名が独自ライセンス(コミュニティライセンス等)の場合は、モデル配布元(Meta・Alibaba・Zhipu AI/Z.ai・Moonshot AI等)の公式サイトでライセンス全文を確認し、閾値条項・再配布条件を洗い出す
3. 自社の利用形態(社内利用のみ/外部提供/再配布/派生モデルの販売)を上表の「使いどころ・使い分け」に照らし、リスクの大小を判断する
4. 判断に迷う場合(利用者数・収益が閾値に近い、派生モデルを他社に販売する等)は、契約前に法務担当者・場合によっては弁護士へのライセンス条文レビューを依頼する

## 注意点・よくある誤解

- **「無料でダウンロードできる=商用利用も無条件で自由」ではない**: 前述のとおりLlama・Qwen大型モデルには利用者数の閾値条項があり、Kimi K2系・Mistral Medium 3.5には収益連動の条項がある。「Apache 2.0やMITのモデルだけが無条件で自由」という点を混同しないこと
- **同じ「Apache 2.0」「MIT」でも、別立ての利用ポリシーが付いていることがある**: gpt-oss(Apache 2.0)にはOpenAIの「gpt-oss usage policy」が付随する。ライセンス名だけで判断せず、提供元の配布ページに別の規約が掲載されていないか必ず確認する
- **ライセンスはモデルの版が変わるたびに変化しうる**: Gemmaは1〜3世代で独自の利用規約+禁止行為ポリシーだったが、Gemma 4(2026年4月)でGoogleが素のApache 2.0へ全面移行し、閾値条項・禁止行為ポリシーとも撤廃した。逆にGLMはGLM-5.2のMITからGLM-5.3で収益閾値付きの独自ライセンスへと制約が増えた例もある。「以前調べた時はこうだった」を過信せず、採用の都度、配布元の最新ライセンスページを再確認する
- **「オープンソース」という呼称を鵜呑みにしない**: 提供元が「オープンソース」と称していても、OSIの定義に照らせば学習データ・学習コードが非公開の「オープンウェイト」にすぎないケースが大半である。法務レビューでは呼称ではなくライセンス条文の実態を確認する
- **ファインチューニングすれば元のライセンスから解放される、というのは誤解**: 多くのライセンスは派生モデルにも元の条件を引き継がせる。「自社で追加学習したから完全に自社のものになった」と判断するのは危険で、特にLlama系は派生モデルの命名義務まで引き継ぐ。日本語ファインチューニングモデル(ELYZA等)も同様にベースのライセンス制約を引き継いでいる
- **国内モデル・独自開発モデルだから制約がない、というのも誤解**: Sakana AIの合成モデル群やELYZAのLlamaベースモデルのように、国内提供元の「独自モデル」も内部でLlama等の既存オープンウェイトモデルを利用している場合、そのベースモデルのライセンス制約(閾値条項・命名義務等)を引き継ぐ
- **生成物の権利・責任はモデルのライセンスではカバーされない**: 「モデルが無保証だから生成物の著作権侵害リスクも自己責任」という点を利用者側(社内の現場担当者)が理解していないことが多い。社内の生成AI利用ガイドラインで、生成物の著作権チェック・第三者権利侵害の一次確認フローを別途整備する必要がある
- **モデル別の詳細な早見表は[ローカルLLMの基本](./local-llm-basics.md)を参照**: 本ページは論点の整理を目的としており、Llama・Gemma・Mistral・Qwen・DeepSeek・GLM・Kimi等の個別モデルのライセンス名・特徴の一覧は重複させていない。最新のモデル別ライセンス状況は同ページの表を確認すること

## 最初の一歩

自社で採用中(または採用検討中)のオープンウェイトモデルを1つ選び、Hugging Face上のモデルカードに記載されたライセンス名をもとに配布元の公式ライセンス全文を開き、「再配布条件」「利用者数・収益の閾値」の2点だけをまず確認してみる。

## 関連トピック

- [ローカルLLMの基本(自社PC・サーバーで動かす生成AI)](./local-llm-basics.md)
- [Hugging Faceの基本(AIモデル・データセットのハブ)](./huggingface-basics.md)
- [量子化(モデル軽量化)の基本](./quantization-basics.md)
- [生成AIの著作権リスク](../part04-risk-security/copyright-risks-in-generative-ai.md)

## 更新履歴

### 2026-09-07: 主要モデルのライセンス系統を全面的に最新化
- **内容**: 比較表を刷新し、Gemma 4(2026年4月)が独自ライセンス+禁止行為ポリシーからApache 2.0へ全面移行した経緯を追加。Qwen3系がApache 2.0中心(大型モデルの一部はQwen Community License/Tongyi Qianwen Licenseに残存)である点、DeepSeek V4がMIT継続である点、Mistral Large 3/Small 4がApache 2.0・Mistral Medium 3.5が収益閾値付きの修正MIT型である点を整理。新たにGLM(Zhipu AI/Z.ai。GLM-5.2はMIT、GLM-5.3は累計収益100億ドル超でセキュリティレビューを要する独自ライセンス)とKimi(Moonshot AI。K2系はMAU・収益閾値超で表示義務が生じる修正MIT型、K3は独自ライセンス)を比較表に追加。国内モデル(PFNのPLaMo、SB IntuitionsのSarashina、ELYZA、rinna、Sakana AI)のライセンス状況を新設の小表にまとめ、日本語モデルだから制約がないという誤解に注意喚起を追加。ライセンス本体とは別に付随する利用ポリシー(gpt-oss usage policy等)の存在にも言及
- **出典**: [Llama 4 Community License Agreement - Meta](https://www.llama.com/llama4/license/)、[Google Releases Gemma 4 Open Models Under Apache 2.0 License - Winbuzzer](https://winbuzzer.com/2026/04/03/google-releases-gemma-4-open-models-under-apache-20-license-xcxwbn/)、[Gemma 4's Real Breakthrough Isn't the Benchmarks - Medium](https://medium.com/@AdithyaGiridharan/gemma-4s-real-breakthrough-isn-t-the-benchmarks-google-just-handed-enterprises-something-worth-7d658e41427c)、[Mistral Versions - license terms per release - mungomash.com](https://mungomash.com/ai/mistral/versions/)、[Mistral AI Models 2026 Complete Guide - Serenities AI](https://serenitiesai.com/articles/mistral-ai-models-2026-complete-guide)、[Qwen Versions - license terms per release - mungomash.com](https://mungomash.com/ai/qwen/versions/)、[DeepSeek V4 Open Source: MIT License Explained (2026) - Framia](https://framia.converge.ai/page/en-US/news/deepseek-v4-open-source-mit-license)、[Z.ai's GLM-5.3 goes open weight, but its new license aims at hyperscalers - The New Stack](https://thenewstack.io/zai-glm-weights-license/)、[What "Open Weights" Lets You Do: The 2026 Model License Map - Vetted Consumer](https://vettedconsumer.com/what-open-weights-lets-you-do-the-2026-model-license-map-read-from-the-actual-texts/)、[OpenAI open-weight models (gpt-oss) - OpenAI Help Center](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss)、[pfnet/plamo-3-nict-8b-base - Hugging Face](https://huggingface.co/pfnet/plamo-3-nict-8b-base)、[sbintuitions/sarashina2.2-3b-instruct-v0.1 - Hugging Face](https://huggingface.co/sbintuitions/sarashina2.2-3b-instruct-v0.1)、[elyza/Llama-3-ELYZA-JP-8B - Hugging Face](https://huggingface.co/elyza/Llama-3-ELYZA-JP-8B)、[Local LLM Development by Japanese Companies - codenote.net](https://codenote.net/en/posts/japanese-local-llm-development-case-studies/)、[Open Source AI Deep Dive - Open Source Initiative](https://opensource.org/deepdive)

### 2026-07-25: 初版執筆
- **内容**: 「オープンウェイト」と「オープンソース」の定義の違い(OSIのOpen Source AI Definitionに基づく整理)、Apache 2.0/MIT/Llama Community License/Tongyi Qianwen License/Gemma利用規約の横並び比較表、商用利用時に法務・調達が確認すべき論点(再配布条件・派生モデルの扱い・利用者数閾値・生成物の著作権と責任範囲・商標命名規則)を整理。モデル別の詳細な早見表は既存の[ローカルLLMの基本](./local-llm-basics.md)に譲り、本ページでは重複させない方針を明記
- **出典**: [LLAMA 4 COMMUNITY LICENSE AGREEMENT - Meta](https://www.llama.com/llama4/license/)、[Meta Llama 3 and the 700M MAU Limit - WCR.LEGAL](https://wcr.legal/llama-3-license-700m-mau-limit/)、[You're Probably Breaking the Llama Community License](https://notes.victor.earth/youre-probably-breaking-the-llama-community-license/)、[Gemma Terms of Use - Google AI for Developers](https://ai.google.dev/gemma/terms)、[Gemma Prohibited Use Policy - Google AI for Developers](https://ai.google.dev/gemma/prohibited_use_policy)、[Google Gemma: The Hidden Risks of an "Almost Open" License - WCR.LEGAL](https://wcr.legal/google-gemma-license-risks/)、['Open' AI model licenses often carry concerning restrictions - TechCrunch](https://techcrunch.com/2025/03/14/open-ai-model-licenses-often-carry-concerning-restrictions/)、[What Is Open Source AI? A Practical 2026 Guide to OSAID - Moesif Blog](https://www.moesif.com/blog/technical/api-development/Open-Source-AI/)、[Open Weights vs Open Source: The Real Difference (2026) - GEO Toolbox](https://geotoolbox.ai/blog/open-weights-vs-open-source)、[Mistral Releases Apache 2.0 Open Source Leanstral 1.5 - Open Source For You](https://www.opensourceforu.com/2026/07/mistral-releases-apache-2-0-open-source-leanstral-1-5/)、[Mistral Versions - license terms per release - mungomash.com](https://mungomash.com/ai/mistral/versions/)、[Tongyi Qianwen LICENSE AGREEMENT - GitHub](https://github.com/QwenLM/Qwen/blob/main/Tongyi%20Qianwen%20LICENSE%20AGREEMENT)、[Open-Weight License Landscape 2026 - Presenc AI](https://presenc.ai/research/open-weight-license-landscape-2026)、[Open Source AI Versus Proprietary AI Models: Key Differences in Contract Terms and IP Risks - Hunton](https://www.hunton.com/insights/publications/open-source-ai-versus-proprietary-ai-models-key-differences-in-contract-terms-and-ip-risks-part-2)、[How AI Models Are Licensed: A Brief Guide for Founders and Product Managers - WCR.LEGAL](https://wcr.legal/ai-model-licensing-guide-for-founders/)、[OpenAI open-weight models (gpt-oss) - OpenAI Help Center](https://help.openai.com/en/articles/11870455-openai-open-weight-models-gpt-oss)、[Open Source AI Licenses [2026]: Apache 2.0 to RAIL Guide - QubitTool](https://qubittool.com/blog/open-source-ai-license-compliance-guide)
