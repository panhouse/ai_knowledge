---
title: 半導体・電機業界における生成AI活用事例
part: 14
chapter: "第1章 製造業"
tags: [半導体, 電機業界, 生成AI活用事例, EDA, チップ設計, 歩留まり改善, サプライチェーン, 情報漏洩対策]
created: 2026-07-17
updated: 2026-08-12
---

# 半導体・電機業界における生成AI活用事例

## これは何か

半導体・電機業界は、数百億トランジスタ規模の回路設計、ナノメートル単位の欠陥を見抜く
検査、装置1台の停止が数千万円規模の損失に直結するファブ(製造工場)運用、
そして世界的な部材調達の綱引きという、他の製造業にはない固有の課題を抱える。
本ページは、そのうち**チップ設計支援(EDA〈電子設計自動化〉AIツール)、
ウェハ欠陥検出・歩留まり分析、ファブの予知保全、データシート・技術文書生成、
サプライチェーン・部材枯渇予測、設計データの機密保護**という、半導体・電機業界
ならではの生成AI活用事例を整理する事例カタログである。

なお、外観検査全般や設備の異常検知の基本的な考え方、需要予測にもとづく生産計画の
仕組みは[製造業における生成AI活用事例](manufacturing-ai-use-cases.md)で
業種横断的に扱っており、本ページでは重複を避けて詳しく触れない。本ページは
「半導体・電機業界に固有の粒度(回路設計データ・ウェハ単位の欠陥・
部材の枯渇リスク)」に絞って掘り下げる。

## 業務工程別の活用マップ

| 領域 | 課題 | AI・生成AIの役割 | 代表事例(本ページ内) |
|---|---|---|---|
| チップ設計(EDA) | 回路設計・検証・レイアウト最適化の工程が複雑化し、設計者の経験と工数に依存 | 自然言語やLLM(大規模言語モデル)でRTL(回路の動作記述)やスクリプトを生成し、AIエージェントが設計フローを自律的に最適化 | Synopsys.ai Copilot(AgentEngineer™)、Cadence Cerebrus AI Studio / ChipStack AI Super Agent、Rapidus「Raads」 |
| ウェハ欠陥検出・歩留まり分析 | 先端プロセスでは0.1マイクロメートル未満の微小欠陥が歩留まりを左右するが、ルールベース検査では見逃しが多い | AI画像認識(ディープラーニング)で欠陥を分類し、少ない実欠陥データを合成データで補いながら検査精度を高める。計算リソグラフィ工程では生成AIが処理を追加高速化 | NVIDIA cuLitho(計算リソグラフィ)、ソニー×三菱電機「Advanced Vision Solutions」(AIビジョンセンサー) |
| ファブの予知保全 | 製造装置の突発停止はライン全体を止め、1時間あたり数千万円規模の損失につながる | センサーデータ(振動・温度・電流・プラズマ状態等)をAIが解析し、異常の予兆を早期検知 | TSMCのAIドリフト検知による非計画停止ゼロ化(報道ベース) |
| データシート・技術文書生成 | 電子部品のデータシート・アプリケーションノートは種類が膨大で、必要な情報を探す・まとめるだけでも時間がかかる | LLMがデータシートからパラメータを抽出・要約し、ドライバコードやFAQ形式の技術文書の下書きを生成 | D2S-FLOW(データシート→SPICEモデル抽出)、ChatEDA、Cyanobyte |
| サプライチェーン・部材枯渇予測 | AIデータセンター向け需要の急増でHBM(広帯域メモリ)等の特定部材に需要が集中し、想定外の枯渇・納期遅延が起きる | 需要・リードタイム・価格のシナリオをAIが予測し、調達判断の前倒しを支援 | Supplyframe Commodity IQ、Resilincのサプライチェーンリスク分析 |
| 設計データの機密保護 | チップの回路図・歩留まりデータ・テスト手順は企業の中核的な営業秘密であり、汎用生成AIへの入力は情報漏洩に直結する | 社内限定のEDA AIツール・オンプレミス/専用テナント環境での利用に限定するガバナンス設計 | Samsung半導体エンジニアによるChatGPTへのソースコード入力事故(2023年) |

**読み方のコツ**: 「チップ設計」「データシート生成」はLLMによる**コード・文章生成**が主役、
「ウェハ欠陥検出」「予知保全」は**画像認識・異常検知の機械学習**が主役、
「サプライチェーン予測」は**時系列予測+シナリオ生成**という組み合わせで、
それぞれ技術的な中身が異なる。「生成AI」という言葉でひとくくりにせず、
どの技術がどの工程を担っているかを区別して評価するとよい。

## 代表事例の詳細

### 1. チップ設計支援: Synopsys.ai Copilot(AgentEngineer™) / Cadence Cerebrus AI Studio・ChipStack AI Super Agent / Rapidus「Raads」

- **企業**: シノプシス(Synopsys)、ケイデンス(Cadence)、ラピダス(Rapidus、日本の
  次世代半導体製造企業)
- **課題**: 先端半導体の回路設計・検証・レイアウト最適化は工程が複雑化する一方、
  熟練設計者の確保が追いつかず、設計期間の長期化がボトルネックになっている
- **導入したAI・仕組み**:
  - **Synopsys.ai Copilot**は、社内外のLLMとRAG(検索拡張生成)を組み合わせた
    「Knowledge Assistant」(社内文書の質問応答、最大70%の回答時間短縮)、
    設計ワークフロー用スクリプトを生成する「Workflow Assistant」、自然言語から
    RTLコードを生成する「Code Advisor」、検証用テストベンチを生成する
    「Formal Advisor」で構成され、導入企業で2〜5倍の設計生産性向上が報告されている。
    さらに2026年3月の「Synopsys Converge 2026」では、複数のEDAエージェントを
    協調動作させる新技術「AgentEngineer™」を発表し、自然言語・形式仕様からの
    RTL生成→Lintチェック→ユニットテストベンチ生成→検証収束までを自律的に
    反復する「業界初のL4オーケストレーション型マルチエージェント設計・検証
    ワークフロー」を実証した(従来数百人月かかる大規模SoCの検証工程の
    自動化がねらい)
  - **Cadence Cerebrus AI Studio**は、複数ブロック・複数ユーザーでのSoC
    (システムオンチップ)設計を自律的なAIエージェントが統合的に最適化する
    「agentic AI」型のプラットフォームで、SoCの市場投入までの期間を5〜10倍
    高速化するとされる。Samsung Semiconductor India Researchでは、SoCサブシステムで
    PPA(性能・消費電力・面積)が8〜11%改善したと報告されている。2026年2月には
    前工程(フロントエンド)の設計・検証に特化した「ChipStack AI Super Agent」を
    発表し、テストベンチ作成・テスト計画立案・リグレッション実行・デバッグ修正
    までを自動化する。Cerebrus・Verisium(検証プラットフォーム)・JedAI(データ
    基盤)を統合し、生産性を最大10倍に高めるとされ、NVIDIA・Qualcomm・Altera・
    Tenstorrentなどが早期導入企業として名を連ねる
  - **Rapidus「Raads(Rapidus AI-Agentic Design Solution)」**は、日本が推進する
    2nm(ナノメートル)ロジック半導体の量産に向け、2025年12月に発表された。
    LLMベースのEDAツール「Raads Generator」が半導体の仕様入力からRapidusの
    2nmプロセスに最適化したRTL設計データを出力する。既存EDAツールと併用する
    ことで設計期間を50%、設計コストを30%削減できるとされ、2026年から順次
    ツール群を提供開始する(品質保証・設計支援を行う「Raads Navigator/
    Indicator」、レイアウト設計の「Raads Manager」、PPA最適化の
    「Raads Optimizer」を予定)。Rapidusが掲げる短TAT(製造リードタイム)戦略
    「RUMS(Rapid and Unified Manufacturing Service)」の中核を担う位置づけである
- **自社への応用ヒント**: 各社とも「AIが設計を全自動で完結させる」のではなく、
  自然言語での指示からコード・スクリプトのたたき台を生成し、AIエージェントが
  最適化の反復作業を肩代わりする形で導入されている。設計そのものより先に、
  「ドキュメント検索」「スクリプト生成」のような周辺業務から着手すると
  投資対効果を検証しやすい。ChipStack AI Super AgentのようにNVIDIA Nemotron
  等のクラウドホスト型LLM・OpenAI GPT系モデルを選択できるツールもあるため、
  導入時は「オンプレミス/専用テナントで完結するか」「外部クラウドAPIに
  設計データが渡るか」をベンダーに必ず確認すること(後述の情報漏洩リスク参照)

### 2. ウェハ欠陥検出・歩留まり分析: AI画像認識による外観検査の高度化

- **業界動向**: 先端ノードでは0.1マイクロメートル未満の微粒子がダイ(チップ1個分の
  領域)を丸ごと不良にしうる一方、検出漏れによる歩留まり損失は業界全体で
  年間500億ドルを超えるとされる。従来のルールベースAOI(自動光学検査)の
  分類精度が約70%程度なのに対し、ディープラーニングを使うAI画像認識では
  約95%まで精度を高められるとの報告がある
- **課題と対処**: 半導体の欠陥は絶対数が少なく、AI検査モデルの学習に十分な量・
  多様性のあるデータを揃えにくい([製造業における生成AI活用事例](manufacturing-ai-use-cases.md)の
  日本精工の事例と同じ構造の課題)。この分野でもデータ拡張(オーグメンテーション)や
  合成データ生成でデータ不足を補う取り組みが進んでいる
- **効果**: 先端ノードのダイ単価では、歩留まりが1%改善するだけで検査システムへの
  投資額を生産1か月分で回収できるとされ、投資対効果が測りやすい領域として
  各ファブでAI検査の導入が進む
- **前工程(リソグラフィ)への生成AI応用**: 検査だけでなく、ウェハに回路パターンを
  焼き付ける露光工程の手前で行う「計算リソグラフィ」(マスクパターンを事前に
  最適化する計算処理で、半導体製造で最も計算負荷が高い工程の一つ)にも生成AIが
  応用されている。NVIDIAの「cuLitho」はGPUでこの処理を高速化する基盤で、
  TSMCとSynopsysが量産導入しており、cuLitho自体で従来のCPU処理比40〜60倍、
  さらに生成AIアルゴリズムを組み合わせることで追加で2倍の高速化が得られると
  報告されている
- **国内の新事例**: ソニーセミコンダクタソリューションズと三菱電機は
  2026年7月22日、FA(ファクトリーオートメーション)向けのAI搭載
  ビジョンセンサー・ソリューションを開発する合弁会社「Advanced Vision
  Solutions株式会社」(出資比率: 三菱電機60%・ソニーセミコンダクタソリューションズ
  40%)の設立に合意し、2026年10月に事業を開始する予定である。ソニー側の
  イメージセンサー・エッジAI(センサー内で推論処理まで行う仕組み)技術と、
  三菱電機のFA分野の制御技術・顧客基盤を組み合わせ、半導体・電子機器を含む
  製造現場の外観検査・異常検知・自律制御の高度化を狙う
- **自社への応用ヒント**: 「検査精度を上げる」ことだけでなく、「新種の欠陥
  パターンにルールベース検査が追従できていないか」を点検すると、AI画像認識への
  切り替え候補が見つけやすい。cuLithoやAdvanced Vision Solutionsのような
  組み合わせは、装置ベンダー・EDAベンダー・センサーメーカーが提供する
  専用ソリューションが前提であり、自社で汎用LLMから同等の効果を再現しようとする
  のは非効率である点に注意する

### 3. ファブの予知保全: 製造装置の異常予兆検知

- **課題**: 半導体ファブでは製造装置の突発停止がライン全体の稼働に影響し、
  停止1時間あたり100万ドル以上の損失が生じることもある
- **導入したAI・仕組み**: 振動・温度・電流・プラズマ状態などのセンサーデータを
  AIがリアルタイム解析し、異常の予兆を事前に検出することで、計画外停止を
  30〜50%、保全コストを25〜30%、不要な部品交換を15〜30%削減できるとされる。
  TSMCではAIによる早期のドリフト(装置特性の微小なずれ)検知により、
  対象設備の非計画停止を18か月かけてゼロ化したと報じられている
- **自社への応用ヒント**: この分野の主役は生成AI(LLM)ではなく従来型の異常検知
  モデルである。生成AIを組み合わせる場合は、[製造業における生成AI活用事例](manufacturing-ai-use-cases.md)の
  ダイキン工業×日立製作所の事例のように、異常検知そのものではなく
  「異常発生後の原因診断・過去事例検索」を生成AIが支援する形が現実的である

### 4. データシート・技術文書生成: LLMによる部品情報の抽出・文書化支援

- **課題**: 電子部品のデータシート・アプリケーションノートは製品ごとに書式も
  分量もばらばらで、必要なパラメータ(電圧・電流・ピン配置・タイミング条件等)を
  探し出すだけでも設計者の時間を消費する
- **導入されているAI・仕組み**:
  - 研究段階の取り組みとして「D2S-FLOW」は、LLMを使ってデータシートから
    パラメータを自動抽出し、回路シミュレーション用のSPICEモデルを生成する
    パイプラインを提案している
  - 「ChatEDA」はGPT-4等のLLMを使い、自然言語での対話からEDAツール向けの
    タスク計画・スクリプト生成・実行までを行う会話型インターフェースを実現する
    研究プロジェクトである
  - 「Cyanobyte」プロジェクトはAIでデータシートを読み取り、そこからマイコン用の
    ドライバコードを生成する取り組みを行っている
  - 実務でより手軽に使えるのは、汎用LLM+RAG(社内のデータシートPDF群を
    検索対象にする)によるドキュメントQ&Aで、「このICの推奨動作温度範囲は?」
    「このピンの最大定格電流は?」といった質問に、根拠となるデータシートの
    該当箇所を示しながら回答させる使い方である
- **自社への応用ヒント**: 「データシートを丸ごとAIに読ませて質問に答えさせる」
  RAG型の使い方は、既存の汎用チャットAIでも比較的低コストで試せる。
  ただし未公開の自社設計データを外部のデータシート検索的なAIサービスに
  投入してよいかは、後述する情報漏洩リスクの観点で必ず確認すること

### 5. サプライチェーン・部材枯渇予測: AIによる需給シナリオ予測

- **背景**: 2020年代前半の世界的な半導体不足以降、この業界では「特定部材の
  枯渇をどれだけ早く察知し、代替調達や設計変更に動けるか」が経営課題として
  定着した。2025〜2026年もAIデータセンター向け需要の急拡大により、
  HBM(広帯域メモリ)やCoWoS(先端パッケージング技術)といった特定工程に
  需給がひっ迫している。2026年8月5日付のDIGITIMESの報道では、SK Hynix・
  Micron・Samsungのメモリ大手3社の2027年分のDRAM/HBM生産枠が既に完売
  (フルアロケーション)状態にあり、生産枠の約7割がAI・HBM向けに割り当てられ、
  自動車・PC・スマートフォン向けなど他業界の調達が後回しにされる構造が
  続くと報じられている。DDR5等の一般向けDRAM価格も2026年内は高止まりする
  見通しが続いている。日本国内では、Micronが広島工場に1.5兆円を投じて
  HBM4量産用クリーンルームを新設中(2026年7月4日起工、2030年に月産4万枚
  規模を目指す)、ソニーとTSMCも熊本で次世代イメージセンサー合弁に1兆円を
  投資するなど、需給ひっ迫を見越した生産能力の分散・国内誘致が進んでいる
- **導入されているAI・仕組み**: Supplyframeの「Commodity IQ」は、電子部品の
  需要・リードタイム・価格の予測をダッシュボード化し、調達担当者が
  「どの部材がいつ枯渇リスクを迎えるか」を早期に把握できるようにする
  サプライチェーンインテリジェンスサービスである。Resilincも同様に、
  AI半導体需要の急増が既存のサプライチェーンに与えるリスクを分析した
  レポートを継続的に発信している
- **自社への応用ヒント**: この種のAIは「枯渇するかどうか」を断定的に当てる
  ものではなく、複数シナリオの確率的な予測を早期に示すことに価値がある。
  電子機器メーカー側は、主要部材についてこうした外部の需給予測サービスの
  アラートを定期的に確認し、設計段階で代替部品(セカンドソース)を
  用意しておく判断材料として使うのが現実的な活用法である。特に車載・産機用途で
  メモリ・アナログICを使う企業は、「AI向け需要に生産枠を奪われていないか」を
  四半期単位で確認する優先度が上がっている

### 6. 設計データの機密保護: Samsung半導体エンジニアによるChatGPT入力事故(2023年)

- **何が起きたか**: 2023年3月末から4月にかけて、Samsung Electronicsの
  半導体部門のエンジニアが、社外秘の情報をChatGPTに入力する事故が3件相次いだ。
  (1)半導体製造装置の測定用データベースのソースコードをバグ修正・最適化目的で
  入力、(2)歩留まり・欠陥測定に関する装置のソースコードを別のエンジニアが
  最適化目的で入力、(3)社内会議の音声を文字起こしし、未発表の半導体プロセス
  技術に関する議事録作成をChatGPTに依頼、という3つの経路である。
  Samsungはこの事故を受けて社内でのChatGPT等の利用を禁止した
- **半導体業界に固有のリスクである理由**: チップの回路設計(RTL・ネットリスト)、
  歩留まり・欠陥データ、テスト手順は、他業種の「顧客リスト」以上に
  企業の競争力そのものを左右する営業秘密であり、いったん外部の汎用AIサービスに
  入力されると回収が事実上不可能になる。しかも設計・検証エンジニアは
  日常的にコードやログを大量に扱うため、「デバッグを手伝ってほしい」という
  自然な業務動機で機密データを入力してしまいやすい
- **自社への応用ヒント**: 上記1で紹介したSynopsys.aiやCadence Cerebrusのような
  EDA AIツールは、汎用チャットAIとは異なりオンプレミスや専用テナント環境での
  提供を前提に設計されている。設計データを扱わせる場合は、汎用の無料AIツールと
  企業契約のEDAベンダー提供AI・社内専用環境を明確に切り分け、
  「どのAIになら回路データを入力してよいか」を設計者に周知することが欠かせない。
  ただし2026年時点のEDAベンダー製ツールの中には、Cadence ChipStack AI
  Super Agentのように「NVIDIA Nemotron等のクラウドホスト型モデル」と
  「OpenAI GPT系のクラウドAPI」の両方を選択可能にしているものもあり、
  「EDAベンダー提供のAIだから安全」と一律に判断せず、契約時に
  「どのモデルがどこで推論されるか」「入力データがベンダー・第三者のモデル
  学習に再利用されないか」を個別に確認する必要がある。
  情報漏洩の経路全般については[生成AIの情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)を参照

## 実務での使い方

### データシート下書き生成プロンプト(汎用LLM向け)

自社製品の仕様一覧から、データシートの技術説明パートの下書きを作らせる例。
社外秘の実測データや未発表スペックは入力せず、公開予定の仕様のみを使うこと。

```
あなたは電子部品メーカーの技術文書担当です。以下の製品仕様から、
データシートの「概要(General Description)」と「主な特長(Key Features)」
のセクションを英語と日本語の両方で作成してください。

## 製品仕様
- 製品名: (例: 3.3V降圧DC-DCコンバータIC XYZ-100)
- 主要パラメータ: (例: 入力電圧4.5V〜18V、出力電流最大3A、
  スイッチング周波数500kHz、変換効率最大95%)
- パッケージ: (例: 8ピンSOP)
- 想定用途: (例: 産業機器・車載インフォテインメント機器の電源回路)

## 条件
- 数値は必ず入力した仕様の範囲内に収め、断定できない性能は「代表値」と明記する
- 競合製品との比較や誇張表現は行わない
- 最後に「詳細は最新版データシート・アプリケーションノートを参照してください」
  という注記を入れる
```

### 部品データシートQ&A(社内RAG向け)プロンプト例

社内のデータシートPDF群を検索対象にしたRAGシステムに投げる質問の型。

```
以下のデータシート抜粋のみを根拠として回答してください。
抜粋に記載がない場合は「データシートに記載なし」と答え、憶測で補わないこと。

質問: このICの動作保証温度範囲と、その範囲を超えた場合に
      保証されなくなる項目を教えてください。
```

### ツール横断の対応付け

| 用途 | 主に使われるツール・基盤 | 備考 |
|---|---|---|
| チップ設計・RTL生成・検証スクリプト生成 | Synopsys.ai Copilot(AgentEngineer™)、Cadence Cerebrus AI Studio / ChipStack AI Super Agent、Rapidus Raads | いずれもEDAベンダー・製造企業提供の専用環境が前提。ただしChipStack AI Super Agentのようにクラウドホスト型LLM(NVIDIA Nemotron・OpenAI GPT等)を選べるものもあり、モデルの推論先は個別確認が必要。汎用チャットAIに設計データを入力するのは情報漏洩リスクが高く非推奨 |
| ウェハ欠陥検出・外観検査・計算リソグラフィ | ファブ・検査装置ベンダー提供のAI画像認識システム、NVIDIA cuLitho、ソニー×三菱電機Advanced Vision Solutions(2026年10月事業開始予定) | 生成AIではなく画像分類の機械学習が主体。合成データ生成や計算リソグラフィの追加高速化に生成AIが補助的に使われる |
| データシート・技術文書の下書き | ChatGPT、Gemini、Copilot等の汎用チャットAI+社内RAG | 未公開の実測データ・仕様は入力せず、公開予定の一般仕様のみを扱う |
| サプライチェーン・部材枯渇予測 | Supplyframe Commodity IQ、Resilinc等の専業インテリジェンスサービス | 汎用チャットAIによる自由記述の需給予測は根拠が不透明になりやすく、専業データベースに基づくサービスが実務では使われる |

## 注意点・よくある誤解

- **チップ設計データを汎用生成AIに入力しない**: Samsungの事故が示す通り、
  ソースコード・歩留まりデータ・会議の議事録といった一見「デバッグの相談」
  程度に見える入力でも、営業秘密の外部流出につながる。EDAベンダー提供の
  専用AI環境か、社内で完結するオンプレミス環境かを必ず確認する
- **「生成AI」と「AI」を混同しない**: ウェハ欠陥検出やファブの予知保全は
  従来型の機械学習(画像分類・異常検知)が主役であり、生成AI(LLM)は
  データ拡張やドキュメント検索など周辺業務を補完する形で使われることが多い
- **AIエージェント型EDAツールはまだ導入初期段階**: Synopsys AgentEngineer™・
  Cadence Cerebrus AI Studio/ChipStack AI Super Agent・Rapidus Raadsのような
  「AIエージェントが設計フローを自律的に最適化する」ツールは2025年末〜2026年に
  相次いで発表・提供開始されたばかり(ChipStackは2026年2月に早期アクセス提供
  開始)であり、効果の数値(生産性2〜10倍等)はベンダー・先行導入企業の発表値
  である点を踏まえ、自社導入時は自社データでの検証を前提にする
- **「EDAベンダー提供だから安全」と即断しない**: 汎用チャットAIより情報漏洩
  リスクは低いが、ツールによってはクラウドホスト型の外部LLMを推論に使う
  選択肢があるため、契約前に「モデルの推論先」「入力データの学習利用の有無」を
  必ず確認する(上記6を参照)
- **サプライチェーン予測は「当てる」ものではなく「早く気づく」ためのもの**:
  需給予測AIの数値をそのまま経営判断の確定値として扱うと外れたときの
  ダメージが大きい。複数シナリオのうちどれに備えるかという意思決定支援の
  材料として使うのが実務的である
- **欠陥データ・不良データの偏りは生成AIで完全には解消できない**: 合成データ生成は
  学習データの量・多様性を補う手段であり、実データによる検証を省略してよい
  わけではない([製造業における生成AI活用事例](manufacturing-ai-use-cases.md)の
  日本精工の事例と同じ留意点)

## 最初の一歩

自社で「設計者・エンジニアが日常的にどのAIツールに何を入力しているか」を
一度棚卸しし、回路データ・歩留まりデータ・未発表の仕様が汎用の無料AIツールに
入力されていないかを確認することから始めるとよい。

## 関連トピック

- [製造業における生成AI活用事例](manufacturing-ai-use-cases.md)
- [生成AIの情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)
- [RAG(検索拡張生成)の基本](../part07-data-analysis/rag-basics.md)

## 更新履歴

### 2026-08-12: EDAエージェント型ツールの進化とサプライチェーン・国内新事例を反映して最新化
- **内容**: (1)チップ設計支援に、Synopsysが2026年3月のConverge 2026で発表した
  マルチエージェント技術「AgentEngineer™」(業界初のL4オーケストレーション型
  設計・検証ワークフロー)と、Cadenceが2026年2月に発表した前工程特化の
  「ChipStack AI Super Agent」(NVIDIA・Qualcomm・Altera・Tenstorrent等が早期導入)
  を追加。(2)ウェハ欠陥検出の節に、NVIDIA cuLithoによる計算リソグラフィへの
  生成AI応用(追加2倍の高速化)と、国内新事例としてソニーセミコンダクタ
  ソリューションズ×三菱電機の合弁会社「Advanced Vision Solutions」
  (2026年10月事業開始予定、AIビジョンセンサー)を追加。(3)サプライチェーンの節を
  2026年8月時点のDRAM/HBM需給(2027年生産枠が完売、AI・HBM向けが約7割)と
  Micron広島工場・ソニー×TSMC熊本合弁などの生産分散動向で最新化。
  (4)設計データの機密保護の節に、EDAベンダー提供ツールでもクラウドホスト型の
  外部LLMを選択できる場合がある点(ChipStack AI Super AgentのNVIDIA Nemotron/
  OpenAI GPT選択機能)を踏まえた確認ポイントを追加し、注意点・ツール対応表にも
  同趣旨を反映した
- **出典**:
  [New Synopsys.ai Copilots Deliver 2–5× Faster Chip Design Productivity(Edge AI and Vision Alliance)](https://www.edge-ai-vision.com/2026/05/new-synopsys-ai-copilots-deliver-2-5x-faster-chip-design-productivity/)、
  [Synopsys Outlines Vision for Engineering the Future(Synopsys公式)](https://news.synopsys.com/2026-03-11-Synopsys-Outlines-Vision-for-Engineering-the-Future)、
  [Synopsys Reveals Agentic AI To Speed Next-Gen Chip And System Designs(Forbes)](https://www.forbes.com/sites/marcochiappetta/2026/03/11/synopsys-reveals-agentic-ai-to-speed-next-gen-chip-and-system-designs/)、
  [Cadence Unleashes ChipStack AI Super Agent, Pioneering a New Frontier in Chip Design and Verification(Cadence公式)](https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2026/cadence-unleashes-chipstack-ai-super-agent-pioneering-a-new.html)、
  [Cadence launches ChipStack AI Super Agent for chip verification(Engineering.com)](https://www.engineering.com/cadence-launches-chipstack-ai-super-agent-for-chip-verification/)、
  [TSMC and Synopsys use Nvidia cuLitho in chip production, explore generative AI for computational lithography(DataCenterDynamics)](https://www.datacenterdynamics.com/en/news/tsmc-and-synopsys-use-nvidia-culitho-in-chip-production-explore-generative-ai-for-computational-lithography/)、
  [TSMC and Synopsys Bring Breakthrough NVIDIA Computational Lithography Platform to Production(NVIDIA Newsroom)](https://nvidianews.nvidia.com/news/tsmc-synopsys-nvidia-culitho)、
  [三菱電機とソニー、AIビジョンセンサーで新会社設立へ:「Advanced Vision Solutions」(EE Times Japan)](https://eetimes.itmedia.co.jp/ee/articles/2607/23/news079.html)、
  [三菱電機とソニーがAIビジョンセンサの合弁会社を設立へ 製造現場の省人化を支援(TECH+)](https://news.mynavi.jp/techplus/article/20260722-4729323/)、
  [DRAM価格高騰2026──なぜここまで上がったか・いつ解消するか・今どうすべきかを完全解説(semi-connect)](https://semi-connect.net/dram-price-surge-2026-cause-forecast/)、
  [メモリ価格動向・価格推移【2026年8月更新】(RAMExperts)](https://ramexperts.online/kb/dram-price-trend/)、
  [マイクロン、AI需要で広島工場増強へ起工式 1.5兆円投資(EE Times Japan)](https://eetimes.itmedia.co.jp/ee/articles/2607/06/news047.html)、
  [ソニーGとTSMC、熊本工場に1兆円投資 次世代画像センサー29年量産(日本経済新聞)](https://www.nikkei.com/article/DGXZQOUC055VT0V00C26A8000000/)

### 2026-07-17: 初版執筆
- **内容**: Part14(業種別 生成AI活用事例)第1章 製造業に、半導体・電機業界に
  固有の生成AI活用事例として、チップ設計支援(EDA AIツール)、ウェハ欠陥検出・
  歩留まり分析、ファブの予知保全、データシート・技術文書生成、
  サプライチェーン・部材枯渇予測、設計データの機密保護の6領域を整理した。
  製造業ページ(外観検査・予知保全の一般論)との重複範囲を明記し、相互リンクした
- **出典**:
  [Introducing Generative AI for Chip Design(Synopsys公式ブログ)](https://www.synopsys.com/blogs/chip-design/copilot-generative-ai-chip-design.html)、
  [AI Copilots Boost Chip Design Productivity by 2–5×(Synopsys公式ブログ)](https://www.synopsys.com/blogs/chip-design/synopsys-ai-copilots-chip-design.html)、
  [Transforming Chip Design with Agentic AI: Introducing Cadence Cerebrus AI Studio(ELE Times)](https://www.eletimes.ai/transforming-chip-design-with-agentic-ai-introducing-cadence-cerebrus-ai-studio)、
  [Samsung Semiconductor India Research Leverages Cadence Cerebrus AI Studio(Cadence公式)](https://www.cadence.com/en_US/home/resources/videos/designed-with-cadence/samsung-semiconductor-india-research-leverages-cadence-cerebrus.html)、
  [Rapidus unveils new AI design tools for advanced semiconductor manufacturing(Rapidus Corporation公式)](https://www.rapidus.inc/en/news_topics/information/rapidus-unveils-new-ai-design-tools-for-advanced-semiconductor-manufacturing/)、
  [ラピダス、生成AIで半導体設計支援 26年度にツール提供(日経クロステック)](https://xtech.nikkei.com/atcl/nxt/column/18/03415/122300008/)、
  [日本の半導体復権への「ラストピース」はAIだった:Rapidus「Raads」(XenoSpectrum)](https://xenospectrum.com/rapidus-raads-ai-design-tool-2nm-semiconductor-2026/)、
  [Wafer Defect Detection: 2026 Guide, AI & Inspection(Averroes.ai)](https://averroes.ai/blog/wafer-defect-detection-guide)、
  [半導体業界のAI活用事例(AI革命株式会社メディア)](https://ai-revolution.co.jp/media/ai-in-semiconductor/)、
  [D2S-FLOW: Automated Parameter Extraction from Datasheets for SPICE Model Generation Using Large Language Models(arXiv)](https://arxiv.org/pdf/2502.16540)、
  [A Survey of Research in Large Language Models for Electronic Design Automation(arXiv、ChatEDA記載)](https://arxiv.org/pdf/2501.09655)、
  [Using AI to scan datasheets and help generate driver code in Cyanobyte(Medium)](https://fleker.medium.com/using-ai-to-scan-datasheets-and-help-generate-driver-code-in-cyanobyte-ce6bb55a91e9)、
  [What is the Long-term Outlook for AI Component Demand?(Supplyframe)](https://intelligence.supplyframe.com/long-term-outlook-ai-component-demand/)、
  [AI Chip Supply Chain Risk 2026(Resilinc)](https://resilinc.ai/learning-center/white-papers-reports/resilinc-special-report-supply-chain-risk-to-consider-in-the-ai-driven-chip-shortage/)、
  [Global semiconductor market faces shortages as AI demand strains supply chains(DIGITIMES)](https://www.digitimes.com/news/a20260506PD233/semiconductor-industry-ai-demand-2026.html)、
  [Samsung Bans ChatGPT Among Employees After Sensitive Code Leak(Forbes)](https://www.forbes.com/sites/siladityaray/2023/05/02/samsung-bans-chatgpt-and-other-chatbots-for-employees-after-sensitive-code-leak/)、
  [Incident 768: ChatGPT Reportedly Implicated in Samsung Data Leak(AI Incident Database)](https://incidentdatabase.ai/cite/768/)、
  [1秒間に96億回データ転送 ルネサス、AIメモリー向け半導体(日本経済新聞)](https://www.nikkei.com/article/DGKKZO92787540V21C25A1BZ0000/)
