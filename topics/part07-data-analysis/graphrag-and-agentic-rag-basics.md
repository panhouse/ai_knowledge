---
title: GraphRAG・Agentic RAGの基本(発展形RAGの選び方)
part: 7
chapter: 第4章 RAGの精度改善と基盤
tags: [RAG, GraphRAG, Agentic RAG, 知識グラフ, ナレッジグラフ, AIエージェント, マルチホップ検索]
created: 2026-07-06
updated: 2026-09-27
---

# GraphRAG・Agentic RAGの基本(発展形RAGの選び方)

## これは何か

[RAG(検索拡張生成)の基本](rag-basics.md)で説明した「質問のたびに関連資料を検索して1回で回答を組み立てる」という基本形のRAGには、構造上どうしても苦手な質問がある。「A社とB社は業務提携をしているか、そのきっかけは何か」のように**複数の文書をまたいで初めて答えが見えてくる質問**と、「今期の解約率が上がった原因を調べて」のように**1回の検索では材料が足りず、調べ直しや裏取りを繰り返す必要がある調査タスク**だ。GraphRAG(グラフRAG)とAgentic RAG(エージェント型RAG)は、この2つの壁を突破するために考えられた発展形のRAGアーキテクチャで、それぞれ別の弱点を補う。GraphRAGは資料を「関係性の地図(知識グラフ)」として整理しておくことで文書をまたいだ質問に強くなる方式、Agentic RAGはAIエージェント(自律的に判断して複数の手順をこなすAI)に検索そのものを任せ、「この結果で十分か」を自己判断させながら検索を繰り返す方式。いずれも[RAGの精度を上げる方法](rag-accuracy-improvement.md)で紹介したチャンキング・ハイブリッド検索・リランキングといった調整(基本形のRAGの中でのチューニング)とは次元が違う、**RAGの土台そのものを組み替える選択**であり、構築・運用のコストも技術力も一段上がる。本ページは、「うちの場合、基本形のRAGの改善で足りるのか、それともここまで踏み込むべきか」を判断できることを目標に、2つの発展形の仕組みと導入基準を整理する。

## 仕組み・背景

### GraphRAGとは

GraphRAGは、Microsoft Researchが2024年に提唱し、同年7月にOSS(オープンソースソフトウェア)として公開したアプローチ。通常のRAGが文書を「意味が近いかどうか」だけでベクトル化して保存するのに対し、GraphRAGはあらかじめ資料からエンティティ(人物・組織・製品などの固有の対象)と、そのエンティティ同士の関係性を抜き出し、ノード(エンティティ)とエッジ(関係)で構成される「知識グラフ」として整理しておく。さらに、関連の深いエンティティ群を「コミュニティ」としてグループ化し、そのコミュニティごとの要約もあらかじめ作っておく。質問が来たときは、この知識グラフとコミュニティ要約を検索対象に含めることで、個々の文書の断片だけでなく「AとBはどうつながっているか」まで辿って回答できるようになる。

具体的には、通常のベクトル検索型RAGは「A社の設立年」のような1つの文書内で答えが見つかる質問には強いが、「A社とB社の資本関係」「この規程改定が影響する部署をすべて挙げて」のように**複数の文書をまたいで関係を辿る質問(マルチホップクエリ)**には弱い。各チャンクを個別にベクトル化しているだけなので、チャンク同士のつながりという情報がそもそも保存されていないためだ。GraphRAGは関係性そのものを事前に構造化しておくことで、この種の質問に答えられるようにする。

ただし知識グラフの構築(インデックス化)には、資料からエンティティ・関係を抜き出す作業にLLM(大規模言語モデル)を何度も呼び出す必要があり、構築コストが通常のRAGより高くなりやすい。Microsoft自身の発表によれば、初期(2024年前半)は1データセットのインデックス化に約33,000ドルかかっていたが、その後「LazyGraphRAG」という改良版によって、事前の要約処理を省き必要になったタイミングで関係を辿る方式に切り替えることで、インデックスコストを10〜90%削減できるとMicrosoftは説明している。

ただし本家`microsoft/graphrag`の開発体制には2026年に入り大きな変化があった。GitHub公式リポジトリのトップには「本プロジェクトは大部分がメンテナンスモードに入り、新規PRの受け入れや新機能の実装は行わない。CVE(セキュリティ脆弱性)対応を中心としたバグ修正・依存関係の更新のみを継続する」という趣旨の告知が掲載されており、理由として「2024年7月の初版リリース以降、フロンティアモデル(最先端の大規模言語モデル)の能力が大きく変化し、Microsoftの研究ポートフォリオもそれに応じて多様化した」ことが挙げられている。もっともパッケージ自体はCVE対応・依存関係更新のリリースが継続しており(PyPI上の最新版は2026年9月時点でv3.2.0)、GraphRAGとLazyGraphRAGの技術自体は「Microsoft Discovery」という科学研究向けのエージェント基盤に組み込まれるなど、Microsoft社内での活用は続いている。つまり「OSSとしての新機能開発は本家では止まったが、技術・実装としては引き続き現役」という状態であり、今後の機能追加は後述するLightRAGやNeo4j、Difyのような周辺エコシステム側が主導していく可能性が高い。

加えて、同じ「グラフ+RAG」の発想を独自実装で追求したOSSの**LightRAG**(香港大学発、国際会議EMNLP 2025で採択された手法)のように、小型モデルでのエンティティ抽出やインクリメンタル更新(資料追加時にグラフ全体を作り直さずに済む仕組み)を売りに、Microsoft実装よりさらに低コストな抽出ロジックをうたう代替ライブラリも活発に更新が続いており(GitHub上でも2026年3月時点まで更新継続)、「GraphRAG=必ず高コスト、かつMicrosoft実装一択」という2024年時点のイメージは薄れつつある。とはいえ、コストと精度のバランスは実装ごとに大きく異なり、実装元が公表する削減率は自社に有利な条件での比較であることも多いため、導入時は自社データでの比較検証(PoC、概念実証)を挟むことが望ましい。

### Agentic RAGとは

Agentic RAGは、「検索(Retrieval)→生成(Generation)」を1回きりのパイプラインとして固定するのではなく、AIエージェントに検索の指揮を執らせる方式。エージェントは、検索結果を受け取った時点で「この情報で質問に答えられるか」を自己判断し、不十分だと判断すれば検索キーワードを変えて再検索したり、別の情報源(社内ナレッジベース・Web検索・データベースへの問い合わせなど複数のツール)に切り替えたり、複数の検索結果を比較して矛盾がないか確認したりを、あらかじめ決めた上限回数まで自律的に繰り返す。基本形のRAGが「決まった手順を1回実行するだけ」なのに対し、Agentic RAGは「検索する・確認する・やり直す」というループを回せる点が本質的な違いになる。

この方式が向いているのは、1回の検索では材料が揃わない調査・分析タスクだ。たとえば「今期の解約率が上がった原因を、契約データと問い合わせログの両方から調べて」という依頼には、契約データを検索した結果を見てから「問い合わせログの方も見る必要がある」と気づいて追加検索する、といった判断が要る。逆に、「有休は何日残っているか」のような一問一答には、そもそも繰り返し検索する必要がなく、Agentic RAGは過剰装備でしかない。むしろ検索を何度も繰り返す分、応答時間とトークン消費(≒料金)が基本形のRAGの数倍〜十数倍に増えるため、質問の種類を見誤ると「遅くて高いだけ」になりかねない。

なお、この考え方は業務システムの外でも既に一般ユーザー向けの機能として実装されている。ChatGPTやGeminiの「Deep Research」機能(複数のWebページを自律的に検索・巡回して調査レポートを作る機能)は、Agentic RAGの発想を検索エンジン向けに応用したものと言える。

さらに2025年後半以降は、企業向け検索基盤そのものにAgentic RAGの考え方が組み込まれ始めている。Microsoft Azure AI Searchの「エージェント検索(agentic retrieval)」は、複雑な質問をLLMが複数のサブクエリに自動分解し、並列で検索・リランキングした上で結果を統合する処理を標準機能として提供しており、社内文書(SharePoint・OneLake等)やWebを横断する企業向け知識層「Foundry IQ」ナレッジベースの中核機能へと発展している。Microsoftの検証によれば、Foundry IQのエージェント検索は複数データソースを力任せに全検索する方式と比べてRAG回答の品質スコアを平均36%改善し、小型モデルと組み合わせた場合はコストを抑えながら証拠の再現率(recall、必要な情報をどれだけ取りこぼさず拾えたか)を最大54%高められるという。Google CloudのAgent Search(旧Vertex AI Search)も2026年5月に、SQL検索・ベクトル検索など複数の取得手段をLLMが自律的に選択しながら複数のデータストアを横断して段階的に検索する「エージェント型検索」を追加した。なお提供元のVertex AIは、2026年4月のGoogle Cloud Next 2026で発表された「Gemini Enterprise Agent Platform」への統合が同年5月に完了しており、コンソール上でも「Vertex AI」の呼称は使われなくなっている(既存のAPIエンドポイント自体は変更なし)。つまり2024年時点は「LangGraphなどでエンジニアが自作する」しか選択肢がなかったが、2026年時点では「クラウドの検索基盤が標準機能として提供する」という選択肢が実用段階に入ってきている。

## 使いどころ・使い分け

通常のRAG・GraphRAG・Agentic RAGは、どれか1つを選ぶ二択ではなく、症状に応じて段階的に検討するのが基本。

| | 通常のRAG(基本形) | GraphRAG | Agentic RAG |
|---|---|---|---|
| 向いているクエリ | 1つの文書・チャンクの中に答えがある質問(社内規程の内容、FAQ、マニュアルの手順など) | 複数の文書・エンティティをまたいで関係を辿る質問(組織間の関係、影響範囲の洗い出し、コンプライアンス上の関連文書の特定など) | 1回の検索では材料が揃わない調査・分析タスク(原因分析、複数情報源をまたいだ裏取り、誤りの許容度が低い業務での多角的な確認) |
| 構築コスト | 低い(チャンク化・埋め込みのみ) | 高い(エンティティ・関係抽出にLLM呼び出しが多数走る。LazyGraphRAGやLightRAGなど軽量な実装で大幅に低減可能) | 中〜高い(検索ロジック自体をエージェントとして設計・実装する必要がある。ただしAzure AI Search等のマネージド機能を使えば軽減できる場合もある) |
| 運用コスト・レイテンシ | 低い(検索1回+生成1回) | 中程度(検索自体は速いが、資料更新時にグラフの再構築が必要) | 高い(検索を複数回繰り返す分、応答時間・トークン消費が数倍〜十数倍に増えやすい) |
| 必要な技術力 | 低い(既存ツールの機能で対応可能) | 高い(知識グラフの設計・運用にエンジニアリングが必須) | 高い(エージェントの判断ロジック・ツール構成の設計が必須。マネージド機能を使う場合は設定レベルまで下がる) |
| 代表的な実装 | ChatGPTプロジェクト、NotebookLM(2026年7月に「Gemini Notebook」へ改称)、Dify ナレッジベース | Microsoft GraphRAG(本家は2026年にメンテナンスモード入り)、LightRAG、Neo4j + LangChain | LangGraph、LlamaIndex、Azure AI Search(Foundry IQ/エージェント検索)、Dify Agentアプリ、Copilot Studio エージェント |

### 導入判断のチェックリスト

1. **まず基本形のRAGで試す**: 大半の業務は基本形のRAGで十分。回答の粒度がブレる、的外れな回答が混ざるといった症状は、まず[RAGの精度を上げる方法](rag-accuracy-improvement.md)のチャンキング・ハイブリッド検索・リランキングなどの調整で解決するかを確認する
2. **「関係性を辿れない」という症状が出たらGraphRAGを検討**: チャンキングやリランキングを調整しても、「複数の文書をまたいだ関係」を聞かれると答えられない、または関係のない文書がバラバラに返ってくるだけで統合的な回答にならない場合。組織図・契約関係・コンプライアンス上の関連規程など、エンティティ同士のつながりが業務上重要なドメインほど効果が出やすい
3. **「1回の検索では終わらない」という症状が出たらAgentic RAGを検討**: 利用者が毎回、AIの回答を見て「もう少し別の角度からも調べて」と何度も追加質問しているなら、その追加質問のパターンをエージェントに自動化させる価値がある。特に誤りの許容度が低い業務(法務・医療・財務など)で、複数の情報源を裏取りしてから答えさせたい場合に向く
4. **両方の症状が同時に出る場合は組み合わせを検討、ただし本当に必要か再検討する**: 「関係性を辿りながら、複数回にわたって調べ直す」必要がある高度な調査タスクでは、GraphRAGをAgentic RAGが呼び出す1つのツールとして組み込む構成もある。ただしこれは構築・運用コストが最も高い組み合わせになるため、その複雑さに見合う業務価値があるかを先に見積もる
5. **技術力・予算が明らかに足りない場合は導入を見送る**: いずれもエンジニアリングチームによる構築・保守が前提になる。ノーコードツールの標準機能で完結する範囲を優先し、発展形は「基本形の壁にぶつかってから」検討するのが無駄のない順番

## 実務での使い方

2026年9月時点でも、GraphRAGはDifyやNotebookLM(Gemini Notebook)のような一般的なノーコード・個人向けツールに「ワンクリックで有効化できる標準機能」としてはまだ搭載されておらず、エンジニアがシステムを組み立てる前提の選択肢という位置づけが続いている([RAGの基本](rag-basics.md)の発展形の節と同じ整理)。ただしDifyでは、ビルトインのナレッジベースにネイティブなGraphRAG機能を追加するコミュニティ発のプルリクエストが提出されており(2026年9月時点で未マージ)、ノーコード側の標準機能化に向けた動きも出始めている。一方Agentic RAGは、後述するAzure AI SearchやGoogle Cloud Agent Searchのようにクラウド検索基盤側が標準機能として提供する段階に入っており、二つの発展形で「自作が必須か、製品で済ませられるか」の温度差がさらに広がった。ビジネス側の担当者としては、下記の実装手段が「エンジニアに何を頼めばよいか」の共通言語として押さえておくと話がしやすい。

### GraphRAGの主な実装手段

- **Microsoft GraphRAG(OSSライブラリ)**: GitHub上で公開されているPythonライブラリ(`microsoft/graphrag`)。資料を投入すると、エンティティ抽出・関係マッピング・コミュニティ検出・コミュニティ要約までを自動化してくれるが、インデックス化の際にLLMを多数回呼び出すため、資料量が多いとコストと時間がかかる。後継の「LazyGraphRAG」は事前の要約処理を省く方式で、インデックスコストを10〜90%抑えられるとMicrosoftは説明している。ただし本家リポジトリは2026年に「大部分がメンテナンスモードに入り、新規PRや新機能は受け付けない」ことを公式にアナウンスしており(バグ修正・CVE対応・依存関係更新のみ継続)、パッケージ自体は2026年9月時点でもv3.2.0までリリースが続く一方、機能面の主導権は後述のLightRAGやNeo4j、Difyのような周辺実装に移りつつある
- **LightRAG(OSSライブラリ)**: 香港大学発のOSSで、国際会議EMNLP 2025で採択された手法。小型モデルでのエンティティ抽出とインクリメンタル更新(資料を追加してもグラフ全体を作り直さずに済む)を売りに、Microsoft GraphRAGよりインデックスコスト・トークン消費を大幅に抑えられるとする実装。GitHub上でも2026年3月時点まで継続的に更新されており、Microsoft本家がメンテナンスモードに入った後の「グラフRAGの主流実装」の有力候補として注目度が上がっている。精度面の優劣はデータ規模や質問の種類で変わるため、採用前にPoCでの比較を推奨
- **Neo4j + LangChain / 公式`neo4j-graphrag`パッケージ**: グラフデータベースのNeo4jに知識グラフを構築し、独立した統合パッケージ`langchain-neo4j`が提供する`GraphCypherQAChain`(自然言語の質問をグラフ検索用のクエリ言語Cypherに変換して検索する仕組み)や、Neo4j公式のPythonパッケージ`neo4j-graphrag`を使って検索する構成。エンジニアがグラフの設計から関与する分、業務ドメインに合わせたスキーマ(エンティティ・関係の種類の定義)を作り込める。Neo4jはMicrosoftが2025年にAutoGenとSemantic Kernelを統合して公開した新しいエージェント開発基盤「Microsoft Agent Framework」向けにも、GraphRAGをコンテキスト提供のツールとして組み込むための連携機能を提供している
- **Difyでの実現可能性**: ビルトインのナレッジベース機能そのものには、2026年9月時点でもまだGraphRAGは組み込まれていない。外部のグラフデータベース(Neo4jなど)や`microsoft/graphrag`をAPI化したものをHTTPリクエストノードやカスタムツールとしてワークフローから呼び出す構成が現実的な選択肢だが、グラフの構築・保守は別途エンジニアリングが必要で、Difyだけで完結する話ではない。なお、ビルトインのナレッジベースにネイティブなナレッジグラフ機能(取り込み時にチャンクごとにエンティティ・関係をLLMで抽出し、ハイブリッド検索の一部として横断検索できるようにする案)を追加するプルリクエストがコミュニティから提出されており、2026年9月時点ではまだマージされていないが、標準機能化に向けた開発は進行中

### Agentic RAGの主な実装手段

- **LangGraph(LangChain社)**: 「検索する→十分か判断する→不十分なら検索し直す」というループ(状態遷移)をコードで組み立てるためのフレームワーク。2026年時点でAgentic RAGの実装先として最も広く使われている選択肢の1つ
- **LlamaIndex**: Property Graph Index(ラベル付きプロパティグラフとして知識グラフを構築・検索する仕組み)や、契約書・請求書のような定型文書を軸にしたAgentic Document Workflowsに強みを持つフレームワーク。2026年には汎用のイベント駆動型エージェントフレームワーク「Workflows」が独立パッケージとして1.0に到達し、Agentic Document Workflowsもこの基盤の上で構築される形に整理された。「文書を読み込んで判断するナレッジワーカー型のエージェント」を作る用途で選ばれやすく、データコネクタの豊富さも特徴
- **Difyの「エージェント」ノード・Agentアプリ**: Difyのワークフロー(チャットフロー)に「エージェント」ノードを組み込むと、ReAct・Function Callingなどの推論戦略をプラグインとして選び、複数のツール(ナレッジ検索ノードをツール化したもの、外部API、Web検索プラグインなど)をLLMに自律的に選択・呼び出しさせられる。ノーコードでAgentic RAGに近い挙動を作れる範囲だが、「検索結果が不十分な場合は検索キーワードを変えて再度ツールを呼び出す」といった自己判断の基準をシステムプロンプトで明示する必要があり、単純なナレッジ検索ノードの設定よりチューニングの試行錯誤が増える
- **Azure AI Search「エージェント検索(agentic retrieval)」/ Foundry IQ / Google Cloud Agent Search**: マネージドの検索基盤自体がAgentic RAGを標準機能として提供し始めた例。Azure AI Searchは複雑な質問をLLMが複数のサブクエリに自動分解し、並列検索・リランキングした上で統合結果を返す「エージェント検索」を提供し、企業向け知識層「Foundry IQ」の中核機能になっている。Microsoftの検証では、複数データソースを力任せに全検索する方式と比べてRAG回答の品質スコアを平均36%改善し、小型モデルと組み合わせた場合はコストを抑えつつ証拠の再現率を最大54%高められるという結果が示されている。Google CloudのAgent Search(旧Vertex AI Search)も2026年5月に同種の「エージェント型検索」を追加し、複数のデータストアを横断した段階的な検索に対応した。自前でエージェントを組まなくても、対応クラウドの検索基盤を使うだけである程度のAgentic RAGが実現できる選択肢が実用段階に入ってきている
- **Copilot Studio・Deep Research系機能**: Microsoft Copilot Studioのエージェント機能や、ChatGPT・GeminiのDeep Research機能は、Agentic RAGの考え方をあらかじめ製品として実装したもの。自前で構築せず「既にエージェント的に検索してくれる機能」を使う選択肢として押さえておくとよい

### 導入前に確認すべきこと

エンジニアに依頼する前に、次を明確にしておくと会話がスムーズになる。

- 「関係性を辿れない」のか「1回の検索で終わらない」のか、実際に困っている質問の実例を5〜10個集めておく
- 想定する資料量・更新頻度(GraphRAGはグラフの再構築コストがかかるため、頻繁に更新される資料には向きにくい)
- 許容できる応答時間(Agentic RAGは数秒〜数十秒の追加レイテンシが発生し得る)
- 誰が知識グラフ・エージェントの設計とメンテナンスを担うか(いずれも作って終わりではなく、業務ドメインの変化に応じた継続的な調整が必要)

## 注意点・よくある誤解

- **「GraphRAGを入れれば精度が全部上がる」わけではない**: エンティティ・関係の抽出精度は使うLLMや資料の質に依存する。誤った関係性が知識グラフに入り込むと、それをもとにした回答も誤る(いわば「グラフのハルシネーション」)。業務ドメインに合わせたエンティティ・関係の設計(スキーマ)を人が確認する工程は省けない
- **知識グラフは自動更新されない**: 資料を追加・修正しても、再度エンティティ抽出とコミュニティ要約を作り直さない限り、古い関係性のまま検索され続ける。更新頻度が高い資料には運用負荷が重い
- **Agentic RAGは「賢くなる」のではなく「時間とコストをかけて確認を増やす」仕組み**: 検索を繰り返す分だけ応答が遅くなり、トークン消費(料金)も増える。単純な一問一答やFAQボットに導入すると、コストだけ増えて体感速度が悪化する
- **エージェントの検索ループには必ず上限を設定する**: 自己判断に任せきると、無関係な検索を繰り返してコストだけ積み上がる「暴走」が起きうる。最大検索回数・最大実行時間などの上限を必ず決めておく
- **GraphRAGは依然「標準機能」としては未成熟、Agentic RAGは製品化が先行**: DifyやNotebookLM(Gemini Notebook)などでGraphRAGをボタン一つで有効化できる段階にはまだない(Difyはネイティブ対応のプルリクエストが進行中だが2026年9月時点で未マージ)。加えて本家Microsoft GraphRAGが2026年にメンテナンスモードへ移行し新機能開発を止めたため、今後の機能拡張はLightRAGやNeo4jのような周辺実装が主導する可能性が高い。一方Agentic RAGは、Azure AI Searchの「エージェント検索/Foundry IQ」やGoogle Cloud Agent Searchのようにクラウド検索基盤側が標準機能として提供する段階に入っており、必ずしも自前でエージェントを組まなくても実現できる場面が増えた。ただしこれらは対応するクラウド・製品が限定されるため、「今使っている基盤がどこまで対応しているか」を必ず確認する
- **基本形のRAGの改善で解決する問題を、発展形で解決しようとしない**: 回答のブレ・抜け漏れ・的外れといった症状の多くは、[RAGの精度を上げる方法](rag-accuracy-improvement.md)で紹介したチャンキング・ハイブリッド検索・リランキングの調整で解決する。まずそちらを試してから発展形を検討する順番を守る

## 最初の一歩

今のRAGで「答えられなかった質問」を1つ思い出し、それが「複数の文書をまたいだ関係性を聞いている質問」なのか、「1回の検索では材料が足りず調べ直しが必要な質問」なのかを分類してみる。前者ならGraphRAG、後者ならAgentic RAGが候補になる、という整理を関係者(エンジニア)と共有することが検討の第一歩になる。

## 関連トピック

- [RAG(検索拡張生成)の基本](rag-basics.md)
- [RAGの精度を上げる方法](rag-accuracy-improvement.md)
- [ベクトルデータベースの基本(Embeddingとの関係)](vector-database-basics.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)

## 更新履歴

### 2026-09-27: GraphRAG本家のメンテナンスモード移行とAgentic RAGのマネージド化の進展を反映して最新化
- **内容**: Microsoft本家`microsoft/graphrag`がGitHub上で「大部分がメンテナンスモードに入り新規PR・新機能は受け付けない」ことを公式アナウンスした事実(理由・現状のリリース状況を含む)を反映し、「OSSとしては本家が停止、周辺実装(LightRAG・Neo4j・Dify)が主導」という2026年9月時点の構図に書き換えた。LightRAGがEMNLP 2025採択・2026年3月まで更新継続の活発なOSSであること、LangChainの`GraphCypherQAChain`が現在は独立パッケージ`langchain-neo4j`提供であること、DifyがビルトインナレッジベースへのネイティブGraphRAG対応PRを提出済み(未マージ)であることを追記。Agentic RAGの節はAzure AI Search「Foundry IQ」の効果指標(RAG回答品質+36%、証拠再現率+54%)を追記し、Google CloudのVertex AI→Gemini Enterprise Agent Platformへの名称統合が2026年5月に完了したこと、Agent Searchへの「エージェント型検索」追加(2026年5月)を反映。LlamaIndexの「Workflows 1.0」到達も追記
- **出典**: [GitHub: microsoft/graphrag](https://github.com/microsoft/graphrag)、[PyPI: graphrag](https://pypi.org/project/graphrag/)、[Microsoft Research Blog: LazyGraphRAG sets a new standard for GraphRAG quality and cost](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)、[GitHub: HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)、[LangChain Reference: GraphCypherQAChain (langchain-neo4j)](https://reference.langchain.com/python/langchain-neo4j/chains/graph_qa/cypher/GraphCypherQAChain)、[GitHub: langgenius/dify PR #41039 - feat(rag): add native knowledge graph (GraphRAG) for built-in knowledge base](https://github.com/langgenius/dify/pull/41039)、[Microsoft Tech Community: Foundry IQ: boost response relevance by 36% with agentic retrieval](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-iq-boost-response-relevance-by-36-with-agentic-retrieval/4470720)、[Microsoft Tech Community: Foundry IQ: Improve recall by up to 54% with knowledge bases](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-iq-improve-recall-by-up-to-54-with-knowledge-bases/4524852)、[Google Cloud Docs: Agent Search release notes](https://docs.cloud.google.com/generative-ai-app-builder/docs/release-notes)、[Google Cloud Docs: Gemini Enterprise Agent Platform name changes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes)、[LlamaIndex Blog: Announcing Workflows 1.0](https://www.llamaindex.ai/blog/announcing-workflows-1-0-a-lightweight-framework-for-agentic-systems)

### 2026-08-01: GraphRAGの代替実装とAgentic RAGのマネージド化を反映して最新化
- **内容**: GraphRAGの節にMicrosoft GraphRAGが2026年7月時点でも活発にリリースが続くOSSであることと、より低コストな代替実装LightRAG、Neo4j公式パッケージ`neo4j-graphrag`・Microsoft Agent Framework(AutoGenとSemantic Kernelの統合後継)との連携を追記。Agentic RAGの節にAzure AI Searchの「エージェント検索(agentic retrieval)」・Foundry IQナレッジベース、Google Cloud Agent Search(旧Vertex AI Search)といったクラウド検索基盤側のマネージド機能化、LlamaIndexのProperty Graph Index/Agentic Document Workflowsを追記。「GraphRAGは依然自作前提、Agentic RAGは製品化が先行」という2026年時点の温度差を比較表・注意点に反映
- **出典**: [PyPI: graphrag](https://pypi.org/project/graphrag/)、[GitHub: microsoft/graphrag](https://github.com/microsoft/graphrag)、[LightRAG公式サイト](https://lightrag.github.io/)、[Neo4j Labs: GraphRAG](https://neo4j.com/labs/genai-ecosystem/graphrag/)、[Microsoft Learn: Neo4j GraphRAG Context Provider for Agent Framework](https://learn.microsoft.com/en-us/agent-framework/integrations/neo4j-graphrag)、[Visual Studio Magazine: Microsoft Ships Production-Ready Agent Framework 1.0](https://visualstudiomagazine.com/articles/2026/04/06/microsoft-ships-production-ready-agent-framework-1-0-for-net-and-python.aspx)、[Microsoft Learn: Agentic retrieval overview - Azure AI Search](https://learn.microsoft.com/en-us/azure/search/agentic-retrieval-overview)、[Microsoft Tech Community: Foundry IQ: Unlock knowledge retrieval for agents](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/foundry-iq-unlocking-ubiquitous-knowledge-for-agents/4470812)、[Google Cloud Docs: Gemini Enterprise Agent Platform name changes](https://docs.cloud.google.com/gemini-enterprise-agent-platform/vertex-ai-name-changes)、[LlamaIndex Blog: Introducing the Property Graph Index](https://www.llamaindex.ai/blog/introducing-the-property-graph-index-a-powerful-new-way-to-build-knowledge-graphs-with-llms)

### 2026-07-06: 初版執筆
- **内容**: GraphRAG(知識グラフによる関係性検索)とAgentic RAG(AIエージェントによる自律的な検索の繰り返し)の仕組みと向き不向きを、通常のRAGとの3方向比較表・導入判断チェックリストとして整理。Microsoft GraphRAG(OSS)・LazyGraphRAGによるコスト削減の経緯、Neo4j+LangChainでの実装、LangGraph・DifyのエージェントノードによるAgentic RAG実装、Copilot Studio・Deep Research系機能との関係を実務目線で解説
- **出典**: [Microsoft Research: Project GraphRAG](https://www.microsoft.com/en-us/research/project/graphrag/)、[Microsoft Research Blog: GraphRAG: New tool for complex data discovery now on GitHub](https://www.microsoft.com/en-us/research/blog/graphrag-new-tool-for-complex-data-discovery-now-on-github/)、[Microsoft Research Blog: LazyGraphRAG sets a new standard for GraphRAG quality and cost](https://www.microsoft.com/en-us/research/blog/lazygraphrag-setting-a-new-standard-for-quality-and-cost/)、[GitHub: microsoft/graphrag](https://github.com/microsoft/graphrag)、[IBM: What is GraphRAG?](https://www.ibm.com/think/topics/graphrag)、[IBM: What is Agentic RAG?](https://www.ibm.com/think/topics/agentic-rag)、[Redis Blog: Agentic RAG: How enterprises are surmounting the limits of traditional RAG](https://redis.io/blog/agentic-rag-how-enterprises-are-surmounting-the-limits-of-traditional-rag/)、[ByteByteGo: EP220: RAG vs Graph RAG vs Agentic RAG](https://blog.bytebytego.com/p/ep220-rag-vs-graph-rag-vs-agentic)、[Neo4j Blog: GraphRAG and agentic architecture: Practical experimentation with Neo4j and NeoConverse](https://neo4j.com/blog/developer/graphrag-and-agentic-architecture-with-neoconverse/)、[LangChain Docs: Build a custom RAG agent with LangGraph](https://docs.langchain.com/oss/python/langgraph/agentic-rag)、[アルファテックブログ: Difyを使ってAgentic RAGと親子チャンク分割を試してみた](https://www.alpha.co.jp/blog/202505_01/)、[Taskhub: GraphRAGとは？仕組みや従来のRAGとの違い、実装手順をわかりやすく解説](https://taskhub.jp/useful/rag-graph/)、[Taskhub: Agentic RAGとは？従来のRAGとの違いや仕組み、代表的なデザインパターンを解説](https://taskhub.jp/useful/agentic-rag/)、[ソフトバンク クラウドテクノロジーブログ: GraphRAGとは何か〜AWS上で試した「つながり」を活かす検索・推論手法〜](https://www.softbank.jp/biz/blog/cloud-technology/articles/202512/graph-rag/)
- **注記**: 一部のDify公式ドキュメント(legacy-docs.dify.ai配下)は検索エンジンのスニペット経由で内容を確認した。Dify側のエージェントノードの画面文言・設定項目は、掲載前に公式サイトでの再確認を推奨
