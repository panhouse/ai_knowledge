---
title: ベクトルデータベースの基本(Embeddingとの関係)
part: 7
chapter: 第4章 RAGの精度改善と基盤
tags: [ベクトルデータベース, Embedding, RAG, 類似検索, インフラ, ハイブリッド検索]
created: 2026-07-06
updated: 2026-08-22
---

# ベクトルデータベースの基本(Embeddingとの関係)

## これは何か

ベクトルデータベースとは、文章や画像を数値の配列(ベクトル、Embedding=埋め込み)に変換したものを大量に保存し、「意味が近いものを高速に探し出す」ことに特化したデータベースのこと。[RAG(検索拡張生成)の基本](./rag-basics.md)で説明した「チャンク化→埋め込み→検索→生成」という流れのうち、埋め込みを「どこに保存し」「どう検索するか」を担うインフラ部分がベクトルデータベースにあたる。自分でRAGチャットボットや社内検索システムを構築しようとした瞬間に、Pinecone・Weaviate・Qdrant・Chroma・Milvus・pgvectorといった聞き慣れない製品名の選択を迫られることになるが、それぞれの立ち位置と選び方を知らないと、PoC(概念実証)止まりで終わったり、本番移行時に想定外のコストが発生したりする。逆に言えば、ChatGPTやNotebookLM、Difyのようなツールを「機能」として使うだけであれば、ベクトルデータベースの存在を意識する必要はない。なお2026年時点では、専用のベクトルデータベースを新設せずとも、PostgreSQL(pgvector拡張)やElasticsearch/OpenSearchといった「既に使っているデータベース・検索基盤にベクトル検索を追加する」という選択肢も実務での主流の一つになっている。

## 仕組み・背景

### 通常のキーワード検索との違い

従来の全文検索(キーワード検索)は、「単語が一致するかどうか」で探す。「有休 繰越」と検索すれば「有休」「繰越」という単語を含む文書がヒットするが、「年次有給休暇の持ち越し」という表記ゆれには対応できない。一方ベクトルデータベースは、文章の「意味」を表す数値の並び(ベクトル)同士の距離や角度を比較して、意味的に近いものを探す。表記が違っても意味が近ければヒットする点が最大の違いで、この計算には主に「コサイン類似度(2つのベクトルの向きがどれだけ近いか)」や「ユークリッド距離(2点間の直線距離)」といった指標が使われる。数式を理解する必要はなく、「向きや位置が近いベクトル=意味が近い文章、と機械的に判定している」とだけ押さえておけばよい。

### 近似最近傍探索(ANN)で大量データでも高速に検索できる理由

理屈の上では、質問のベクトルと保存済みの全ベクトルとの距離を1件ずつ計算すれば「完全に正確な」検索結果が得られる(これを総当たり検索と呼ぶ)。しかし数百万〜数億件のベクトルを毎回全件計算していては実用的な速度が出ない。そこでベクトルデータベースは、ANN(Approximate Nearest Neighbor、近似最近傍探索)というアルゴリズムを使い、「99%以上の精度で正解に近い結果を、劇的に速く」返す設計になっている。代表的な方式に、ベクトル同士をグラフ状につないでたどる「HNSW(階層的な近傍グラフ)」や、似たベクトルをあらかじめクラスタ(集団)に分けておいてから探す「IVFFlat」がある。実務者が押さえるべきはアルゴリズムの詳細ではなく、「多少の取りこぼし(完全一致ではなく近似)と引き換えに、大量データでもミリ秒単位の検索速度を実現している」という設計思想そのものである。

近年はこれに加えて「量子化(Quantization)」によるコスト最適化も一般的になっている。ベクトルの数値精度を落として保存する(例: 32bitの浮動小数点数を16bitの「halfvec」や1bitまで圧縮する方式)ことで、検索精度をほぼ落とさずに保存容量とメモリ使用量を大きく減らす技術で、pgvectorのhalfvecやMilvusの「RaBitQ」(1bit量子化で最大32倍のインデックス圧縮)、Weaviateの「Binary Quantization」などが代表例。コストを左右する要素として押さえておきたい。

### メタデータフィルタリングとハイブリッド検索の標準化

多くのベクトルデータベースは、ベクトルと一緒に「部署名」「作成日」「アクセス権限」といった付随情報(メタデータ)も保存でき、「営業部の資料に絞って類似検索する」といった条件付き検索(フィルタリング)ができる。検索精度と権限管理の両面で重要な機能であり、[RAGの精度を上げる方法](./rag-accuracy-improvement.md)で扱う「メタデータフィルタリング」はこの仕組みを前提にしている。

もう一つ、2026年時点で押さえておきたいのが「ハイブリッド検索」の標準化である。以前は一部の製品の差別化要因だったが、現在はQdrant・Weaviate・Milvus・Elasticsearch・OpenSearch・pgvector(拡張機能を組み合わせる形)など、主要な選択肢のほぼ全てが「ベクトル検索(意味の近さ)」と「BM25などのキーワード検索(単語の一致度)」を組み合わせ、RRF(Reciprocal Rank Fusion、複数の検索結果の順位を統合する手法)で1つのランキングにまとめる仕組みを標準搭載するようになった。RRFの調整パラメータ(k値)は「60」がElasticsearch・OpenSearch・Qdrantの実装で共通のデフォルトとして定着しており、独自にチューニングする必要は薄い。表記ゆれに強いベクトル検索と、固有名詞・型番・法令番号のような「完全一致がむしろ重要」な検索に強いキーワード検索を両取りできるため、製品選定時は「ハイブリッド検索に対応しているか」ではなく「精度・レイテンシ・運用のしやすさ」で比較するのが実務的になっている。さらに精度を追い込む場合は、ハイブリッド検索で得た候補をCross-Encoder(質問と候補文をペアで読んで関連度を再採点するモデル)で並べ直す「リランキング」を後段に加える構成が定番になってきており、レイテンシ・コストの予算が許す範囲で検討する価値がある。

## 使いどころ・使い分け

主要な選択肢を「マネージド(運用を任せられる)/セルフホスト(自社で構築・運用)」「小規模PoC向け/本番運用向け」の軸で整理する(2026年8月時点。料金・仕様は変更されやすいため導入前に必ず公式サイトで最終確認すること)。

| 製品 | ホスティング形態 | 向いている規模・用途 | 特徴 |
|---|---|---|---|
| **Pinecone** | フルマネージドのみ(セルフホスト不可) | 小規模PoCから大規模本番まで | 運用の手間が最も少ない。Standardプランは月額$50の最低利用料に加え、保存$0.33/GB/月・書き込み$4/100万ユニット・読み込み$16/100万ユニットの従量課金。無料のStarterプランはインデックス5個(各100ネームスペースまで)・2GB・書き込み200万ユニット/月・読み込み100万ユニット/月。AIエージェント経由で読み書きが急増すると、明細に事後的に計上される「capacity fee」と呼ばれる追加費用が発生することがあると報告されており、想定より費用が跳ねやすい点に注意 |
| **Weaviate** | マネージド(Weaviate Cloud)/セルフホスト(OSS)両対応 | 中〜大規模、テキスト・画像を自動でベクトル化させたい場合 | データの自動ベクトル化(vectorizer)とハイブリッド検索(BM25+ベクトル)を標準搭載。ただしハイブリッド検索自体は他製品でも標準化が進んでおり差別化要因としては相対的に薄れつつある。クラウドの共有プラン(Flex)は月額$45から、「保存した次元数」に応じた従量課金(目安1億次元あたり約$9.5)が加わる。目安として1000万ベクトル規模では月$200〜400程度、量子化(Binary Quantization)を使うとこれを大きく圧縮できるとされる |
| **Qdrant** | マネージド(Qdrant Cloud)/セルフホスト(OSS)両対応 | 中〜大規模の本番運用、フィルタ付き検索・レイテンシ重視の場合 | Rust製で高速(平均レイテンシはOSS勢の中でも短い部類とされる)。フィルタ条件を先に適用してから検索する設計のためメタデータフィルタリングと相性が良い。ノード課金(確保したvCPU・メモリの稼働時間に対する課金)でクエリ数自体には追加費用がかからないため、大規模でも比較的コスト予測がしやすい。永続無料枠(0.5vCPU・1GBメモリ・4GBディスク)あり、有料のStandardプランは月$30程度から。目安として1000万ベクトル規模ではWeaviateより安価な月$65〜180程度で収まる例が多いと報告されている |
| **Milvus / Zilliz Cloud** | セルフホスト(OSS)/マネージド(Zilliz Cloud) | 数億〜数十億件級の大規模データ、オープンソースで最大規模を扱いたい場合 | オープンソースのベクトルDBとして最も広く採用されている(GitHub star数はベクトルDBの中で最多クラス)。1bit量子化(RaBitQ)による大幅なインデックス圧縮や、全文検索(BM25)を高速化する機能も搭載。Zilliz Cloudは2026年1月からAWS・Azure・GCP共通で保存$0.04/GB/月・コンピュート$0.096/CU時間に価格を標準化しており、目安として100万ベクトル(1536次元)規模で月$80〜150程度。NVIDIA・Salesforceなど大手の採用事例も多いが、小規模用途にはやや大掛かり |
| **Chroma** | セルフホスト(OSS、Apache 2.0)/マネージド(Chroma Cloud)両対応 | 個人のPoC・プロトタイピング・社内検証 | pip/npmで数行のコードから始められる手軽さが最大の強み。LangChainなどのチュートリアルで既定の選択肢としてよく使われる。Chroma Cloudは無料枠(埋め込み100万件まで+$5分の無料クレジット)があり、以降は書き込み$2.50/GiB・保存$0.33/GiB/月・クエリ$0.0075/TiB・下り転送$0.09/GiBの従量課金 |
| **pgvector** | セルフホスト/マネージド(Supabase・Neon等のPostgreSQLサービスに付属) | 既にPostgreSQLを使っている業務システムにRAGを追加したい場合(目安1000万件規模まで) | 独立したベクトルDBを新たに構築せず、使い慣れたPostgreSQLの拡張機能として追加するだけで済む。「halfvec」による量子化(容量を約半分に圧縮)、フィルタ付き検索の高速化(iterative scan)、HNSWインデックスの並列構築、非ゼロ成分だけを保存する「sparsevec」(BM25やSPLADEのような疎ベクトルの表現に有効)といった機能が揃い、成熟した選択肢になっている。BM25+ベクトルのハイブリッド検索も実運用レベルに達しており、OpenAI・Supabase・Neonなどが本番採用している。どのバージョンが使えるかはSupabase・Neon・AWS RDSなど利用するホスティング先の対応状況に左右される |
| **Elasticsearch / OpenSearch** | マネージド/セルフホスト両対応 | 既に全文検索基盤(Elasticsearch/OpenSearch)を運用しており、そこにベクトル検索を追加したい場合 | 元々はキーワード検索エンジンだが、両者ともベクトル検索とRRFによるハイブリッド検索を標準搭載するに至った。ベクトル検索単体の性能比較では検証条件によって優劣の報告が分かれており(Elastic社の検証ではElasticsearchが優位、第三者機関の検証ではOpenSearchが総合で上回るとの報告もある)、既存基盤の拡張として使う場合に有力な選択肢 |
| **Dify内蔵ベクトルDB** | ナレッジベース機能内で自動管理 | Difyでノーコードのチャットボット・RAGアプリを作る場合 | Difyをローカル構築するとデフォルトでWeaviateが同梱される。裏側でWeaviate・Qdrant・Milvus・pgvectorなど複数のベクトルDBに対応しており、利用者はどれが動いているか意識せず使える |

判断の目安は次の通り。

- **「まず試したい・個人検証」→ Chroma**(セットアップが最も速く、埋め込み100万件までは無料)
- **「運用の手間をかけたくない・本番でも自社インフラを持ちたくない」→ Pinecone**(フルマネージドでセルフホストの選択肢自体がない。ただしAIエージェント用途はコストの読みにくさに注意)
- **「本番運用でテキスト・画像の自動ベクトル化まで任せたい」→ Weaviate**(vectorizer機能とハイブリッド検索を標準搭載)
- **「本番運用でフィルタ検索・レイテンシ・コスト予測のしやすさを重視」→ Qdrant**(価格性能比が良いとされる)
- **「オープンソースで数億件超の超大規模データを扱いたい」→ Milvus/Zilliz Cloud**(大規模実績が豊富)
- **「既にPostgreSQLで基幹システムを運用している」→ pgvector**(1000万件規模までは新しいDBを増やさずに済むことが多い)
- **「既にElasticsearch/OpenSearchで全文検索基盤を運用している」→ その拡張機能でベクトル検索を追加**(新規インフラを増やさずに済む)
- **「ノーコードでRAGアプリを作りたいだけ」→ Difyなどのツール内蔵機能**(ベクトルDBの存在自体を意識しなくてよい)

## 実務での使い方

### 「意識しなくてよい」ケースと「自分で構築が必要」なケース

まず区別すべきは、自分がベクトルデータベースを直接触る必要があるかどうかである。

- **意識不要**: ChatGPTのファイルアップロード・プロジェクト機能、NotebookLM、Microsoft Copilot、Notion AIなど、多くの一般向けAIツールは裏側で自動的にベクトルデータベース相当の仕組みを動かしている。利用者はファイルをアップロードするだけでよく、ベクトルDBの選定・運用は不要
- **ある程度意識する**: Difyのようなノーコードプラットフォームでは、内部で使われているベクトルDB(既定はWeaviate)を設定画面から他の製品に切り替えることもできるが、通常は既定のままで問題ない
- **自分で構築・運用が必要**: 独自のRAGシステムをAPI経由でゼロから開発する場合、社内の複数システムから同じベクトルDBを共有参照したい場合、特定のデータ主権要件(データを自社サーバー外に出せない、など)がある場合は、Pinecone・Weaviate・Qdrant・pgvectorなどを自分で選定・契約・構築する必要がある

### 最小構成のイメージ(自分で構築する場合)

自作RAGシステムの最小構成は、おおむね次の3ステップで動く。

1. **Embeddingモデルでベクトル化**: OpenAIの`text-embedding-3-small`(1M トークンあたり$0.02、1536次元)、Googleの`gemini-embedding-001`(2026年3月には画像・音声・動画・PDFまで扱えるマルチモーダル版「Gemini Embedding 2」もプレビュー公開)、Cohereの`embed-v4`などのAPIにテキストを渡し、ベクトル(例: 1536次元の数値配列)を得る。なおAnthropicは自社製のEmbeddingモデルを持たず、Claudeと組み合わせる場合はVoyage AI(2025年にMongoDBが約2.2億ドルで買収、2026年1月にMoE構成の「Voyage 4」ファミリーを投入)を推奨パートナーとして案内している
2. **ベクトルデータベースに保存**: 得られたベクトルと、元のテキスト・メタデータ(ファイル名・作成日など)をセットでベクトルDBに登録(upsertと呼ばれる)する
3. **検索・回答生成**: ユーザーの質問を同じEmbeddingモデルでベクトル化し、ベクトルDBに「近いものを上位N件返して」と問い合わせ、得られたテキストをLLMへのプロンプトに含めて回答を生成する

コピペで使える最小イメージ(Pythonの疑似コード、実際のSDK呼び出しは各社ドキュメントを参照)。

```python
# 1. 資料をベクトル化して保存(事前準備)
vector = embedding_model.embed("有給休暇は前年度の未消化分を翌年度に限り繰り越せる")
vector_db.upsert(id="rule_012", vector=vector, metadata={"category": "就業規則"})

# 2. 質問時にベクトル化して検索
query_vector = embedding_model.embed("有休の繰り越しってできますか?")
results = vector_db.query(vector=query_vector, top_k=5, filter={"category": "就業規則"})
```

### 料金モデルの考え方

ベクトルデータベースの料金は製品によって課金単位が異なるため、比較する際は「何に対して課金されるか」を揃えて考える必要がある。

| 課金の軸 | 内容 | 該当する製品の例 |
|---|---|---|
| **書き込み量・読み込み量(クエリ数)** | データの登録(write)と検索(read)それぞれに単価が付く | Pinecone(書き込み$4/100万ユニット・読み込み$16/100万ユニット)、Chroma Cloud(書き込み$2.50/GiB・クエリ$0.0075/TiB) |
| **保存データ量(GB)・保存次元数** | 保存しているベクトルの総量や次元数に応じて課金 | 各社共通で発生する基本コスト(Pinecone $0.33/GB/月、Chroma Cloud $0.33/GiB/月、Zilliz Cloud $0.04/GB/月)。Weaviate Cloudは「保存した次元数」ベース(目安1億次元あたり約$9.5)の課金体系 |
| **クラスタの稼働時間・スペック(ノード課金)** | CPU・メモリを確保した時間に応じて課金し、クエリ数自体には追加費用がかからない | Qdrant Cloud(月$30程度〜)、Weaviate Cloud(Flexプラン以降、月$45程度〜)、Zilliz Cloud(コンピュート$0.096/CU時間) |
| **セルフホストの場合のインフラ費** | ベクトルDB自体は無料でも、動かすサーバー(VPS等)の費用が発生 | Weaviate・Qdrant・Milvus・Chroma・pgvectorのOSS版(目安として月額$30程度のVPSでも数千万件規模を扱えるとの報告あり) |

いずれの製品も個人検証レベルであれば無料枠(Pineconeは2GB・書き込み200万ユニット/月、Qdrant Cloudは0.5vCPU・1GBメモリ、Chroma Cloudは埋め込み100万件+$5分のクレジット)で足りることが多いが、本番の利用者数・データ量が増えると、無料枠の上限を超えた分から従量課金が発生し、想定より早くコストが跳ね上がることがある。目安として1000万ベクトル規模まで育った場合、Qdrantは月$65〜180程度、Weaviateは月$200〜400程度、Zilliz Cloudの100万ベクトル(1536次元)規模では月$80〜150程度といった報告があり、同じ「大規模」でも製品によって桁が変わりうる。特にAIエージェントが自律的に大量の読み書きを行うような使い方では、通常のユーザー利用より読み書き回数が急増しやすく、Pineconeのように使用量に応じた不透明な追加費用(capacity fee)が事後的に発生する製品もあるため、契約前に「どの操作に単価が付くか」を確認し、想定データ量・想定クエリ数(エージェント経由のアクセスも含めて)で概算しておくことが重要。

## 注意点・よくある誤解

- **Embeddingモデルを変更すると、既存データの再ベクトル化が必要になる**: OpenAIの旧モデルから新モデルに切り替える、Embeddingモデルを他社製品に乗り換えるといった場合、過去に保存したベクトルはそのままでは使えない。新しい質問文と古い保存済みベクトルとでは「意味の近さ」を計算する基準がそもそも異なるため、保存済みの全チャンクを新しいモデルで計算し直し(再インデックス化)、ベクトルDBに登録し直す必要がある。データ量が多いほどこの作業には時間とAPI利用料がかかるため、Embeddingモデルの選定は後から気軽に変えられるものではないと認識しておく。加えて、Embeddingを提供する会社自体が買収・事業方針転換するリスクもある(例: ChatGPTやClaudeと違って自社製Embeddingモデルを持たないAnthropicが推奨してきたVoyage AIは、2025年にMongoDBに買収されている)。特定のスタートアップ製Embedding APIに一本足で依存する場合は、この種の事業継続リスクも織り込んでおく
- **次元数の設計を後から変えるのは難しい**: ベクトルの次元数(数値配列の長さ、例: 1536次元)はEmbeddingモデルによって決まっており、同じインデックス(検索用のデータ構造)内で異なる次元数のベクトルを混在させることはできない。次元数が大きいほど表現力は上がるが、保存容量と検索コストも増えるため、精度と コストのバランスで選ぶ
- **メタデータ設計を後回しにすると検索の絞り込みができなくなる**: 「どの部署の資料か」「いつ更新されたか」「公開範囲は誰か」といった情報をメタデータとして最初から設計しておかないと、後から「特定の部署だけ検索対象にする」といった絞り込みができず、関係のない情報が混ざったり、権限のない資料が検索結果に出てしまったりするリスクがある
- **無料枠での検証と本番運用は別物と考える**: 無料プランやセルフホストの検証環境でうまく動いても、本番でユーザー数・データ量・同時アクセス数が増えると、クラスタのスペック不足や従量課金の急増に直面しやすい。本番移行前に想定データ量・想定クエリ数でコスト試算をしておく
- **セルフホストは「ソフトウェアが無料」なだけで「運用がタダ」ではない**: Weaviate・Qdrant・Milvus・Chroma・pgvectorはいずれもOSS(オープンソースソフトウェア)として無料で使えるが、サーバー費用・バックアップ・アップデート対応・障害対応といった運用の手間は別途発生する。技術的な保守体制がない場合はマネージドサービスの方が総コストを抑えられることもある
- **AIエージェント経由の利用はコストが読みにくい**: チャットボットのように「人間が1問1答で使う」前提の料金試算は、AIエージェントが自律的に何度も検索・書き込みを繰り返す使い方には当てはまらない。読み書き回数が短時間で跳ね上がり、Pineconeの「capacity fee」のように事後的に明細へ計上される従量費用が発生する製品もあるため、エージェント経由の利用を想定する場合は保守的にコストを見積もっておく
- **「ハイブリッド検索対応」はもはや選定の決め手にならない**: 数年前はWeaviateなど一部製品の差別化要因だったが、2026年時点ではQdrant・Milvus・Elasticsearch・OpenSearch・pgvector(拡張機能経由)など主要な選択肢のほとんどがBM25+ベクトルのハイブリッド検索とRRFによる統合に対応した。「対応しているか」ではなく、自社のデータ・クエリ傾向における精度とレイテンシで比較する

## 最初の一歩

自分でRAGを構築する予定がなければ、まずはChatGPTのプロジェクト機能やNotebookLMでファイルを読み込ませ、裏側でベクトル検索が動いていることを体感してみる。自分で構築を検討している場合は、Chroma(またはDifyの内蔵ナレッジベース)を使って手元の資料数件を登録し、意味の近い文章が検索でヒットする様子を無料で試してみるとよい。

## 関連トピック

- [RAG(検索拡張生成)の基本](./rag-basics.md)
- [RAGの精度を上げる方法](./rag-accuracy-improvement.md)
- [DifyでのRAG実装](../part10-nocode-lowcode/dify-rag-implementation.md)

## 更新履歴

### 2026-08-22: 主要製品の料金を再確認し、ハイブリッド検索のRRF既定値・リランキング、Embeddingモデルの新版とVoyage AI(MongoDB傘下化)の事業継続リスクを追記
- **内容**: Pinecone(書き込み$4/100万ユニット・読み込み$16/100万ユニット・保存$0.33/GB/月、Starterのインデックス上限とネームスペース数)、Weaviate Cloud(Flexプラン月$45〜、次元数ベース課金の単価、1000万ベクトル規模の目安コスト)、Qdrant Cloud(Standardプラン月$30〜、1000万ベクトル規模の目安コスト)、Zilliz Cloud(2026年1月からの保存・コンピュート料金の標準化、100万ベクトル規模の目安コスト)、Chroma Cloud(書き込み・クエリ・下り転送の課金単価)、pgvector(疎ベクトルを保存する`sparsevec`)の情報を最新化。「仕組み・背景」にRRFの既定値(k=60)とCross-Encoderによるリランキングを追記し、ハイブリッド検索が2026年8月時点でも標準機能であることを再確認。「実務での使い方」にGoogleのマルチモーダル版「Gemini Embedding 2」、CohereのEmbed v4、AnthropicがClaudeとの組み合わせで推奨するVoyage AI(2025年にMongoDBが買収、2026年1月に「Voyage 4」ファミリーを投入)を追加し、「注意点」にEmbedding提供元の事業継続リスクの視点を追記
- **出典**: [Withorb: Pinecone pricing explained](https://www.withorb.com/blog/pinecone-pricing)、[Tiger Data: A Guide to Pinecone Pricing](https://www.tigerdata.com/blog/a-guide-to-pinecone-pricing)、[LeanOps: Weaviate Cloud Pricing 2026](https://leanopstech.com/blog/weaviate-cloud-pricing-2026/)、[Ranksquire: Weaviate Cloud Pricing 2026](https://ranksquire.com/2026/04/22/weaviate-cloud-pricing-2026/)、[Ranksquire: Qdrant Cloud Pricing 2026](https://ranksquire.com/2026/04/19/qdrant-cloud-pricing-2026/)、[Zilliz Blog: New in Zilliz Cloud (2026 pricing update)](https://zilliz.com/blog/zilliz-cloud-oct-2025-update)、[LeanOps: Milvus & Zilliz Cloud Pricing 2026](https://leanopstech.com/blog/milvus-zilliz-cloud-pricing-2026/)、[Chroma Docs: Pricing](https://docs.trychroma.com/cloud/pricing)、[DBA Dataverse: pgvector Release Notes & Updates 2026](https://dbadataverse.com/tech/postgresql/2026/05/pgvector-release-notes-updates-2026)、[AI Workflow Lab: Hybrid RAG - BM25 + RRF Guide 2026](https://aiworkflowlab.dev/article/how-to-build-hybrid-search-rag-bm25-rrf-fusion-cross-encoder-reranking)、[Digital Applied: Hybrid Search - BM25, Vector & Reranking Reference 2026](https://www.digitalapplied.com/blog/hybrid-search-bm25-vector-reranking-reference-2026)、[Seeking Alpha: Google unveils new multimodal Gemini Embedding 2 model](https://seekingalpha.com/news/4562806-google-unveils-new-multimodal-gemini-embedding-2-model)、[TokenMix: Claude Embedding Models 2026 - Anthropic Has None](https://tokenmix.ai/blog/claude-embedding-models)、[Respan: Anthropic vs Voyage AI (MongoDB)](https://www.respan.ai/market-map/compare/anthropic-vs-voyage-ai)
- **注記**: 各社の料金プラン・単価・目安コストは第三者メディアによる2026年時点の試算を含み、公式発表そのものではない。掲載・記事化前に各公式サイト(pinecone.io/pricing、weaviate.io/pricing、qdrant.tech/pricing、zilliz.com/pricing、trychroma.com)で最終確認を推奨

### 2026-07-24: 主要製品の料金・機能を最新化し、Milvus/Zilliz・Elasticsearch/OpenSearchを追加、ハイブリッド検索の標準化を反映
- **内容**: Pinecone(無料枠の詳細、AIエージェント利用時の「capacity fee」)、Weaviate(次元数ベース課金・量子化)、Qdrant(ノード課金・自己ホストの目安コスト)、Chroma(埋め込み100万件までの無料枠拡大)、pgvector(halfvec量子化・iterative scan・並列HNSW構築・BM25拡張によるハイブリッド検索の実運用化)の情報を更新。比較表にMilvus/Zilliz Cloud(オープンソース最大規模向け)とElasticsearch/OpenSearch(既存の検索基盤へのベクトル検索追加)を新規に追加。ハイブリッド検索(BM25+ベクトル、RRFによる統合)が主要製品でほぼ標準機能化した点を「仕組み・背景」「注意点」に反映し、AIエージェント経由利用時のコスト変動リスクを新規に追記
- **出典**: [Pinecone Docs: Quotas and limits](https://docs.pinecone.io/reference/quotas-and-limits)、[Pinecone: Opening up our free plan](https://www.pinecone.io/blog/updated-free-plan/)、[LeanOps: Vector DB Bills Exposed](https://leanopstech.com/blog/vector-database-cost-comparison-2026/)、[LeanOps: Weaviate Cloud Pricing 2026](https://leanopstech.com/blog/weaviate-cloud-pricing-2026/)、[DigitalApplied: Vector Databases for AI Agents 2026](https://www.digitalapplied.com/blog/vector-databases-for-ai-agents-pinecone-qdrant-2026)、[Chroma Docs: Pricing](https://docs.trychroma.com/cloud/pricing)、[Instaclustr: pgvector 2026 guide](https://www.instaclustr.com/education/vector-database/pgvector-key-features-tutorial-and-pros-and-cons-2026-guide/)、[Tiger Data: Yes, You Can Do Hybrid Search in Postgres](https://www.tigerdata.com/blog/hybrid-search-postgres-you-probably-should)、[Elastic Search Labs: OpenSearch vs. Elasticsearch filtered vector search](https://www.elastic.co/search-labs/blog/opensearch-vs-elasticsearch-filtered-vector-search)、[PRNewswire: Zilliz recognized as a Stars Company](https://www.prnewswire.com/news-releases/zilliz-is-recognized-as-a-stars-company-in-marketsandmarkets-latest-360quadrant-for-the-vector-database-market-302750027.html)、[MarkTechPost: Best Vector Databases in 2026](https://www.marktechpost.com/2026/05/10/best-vector-databases-in-2026-pricing-scale-limits-and-architecture-tradeoffs-across-nine-leading-systems/)
- **注記**: 一部の料金・性能比較値は第三者メディアによる2026年時点の試算・検証であり、公式発表そのものではない。掲載・記事化前に各公式サイト(pinecone.io/pricing、weaviate.io/pricing、qdrant.tech/pricing、trychroma.com、zilliz.com/pricing)で最終確認を推奨

### 2026-07-06: 初版執筆
- **内容**: ベクトルデータベースの定義とキーワード検索との違い、コサイン類似度・近似最近傍探索(ANN、HNSW/IVFFlat)の仕組み、Pinecone/Weaviate/Qdrant/Chroma/pgvector/Dify内蔵DBの比較表と使い分け、自分で構築が必要なケースと意識不要なケースの区別、料金モデルの考え方、Embeddingモデル変更時の再ベクトル化・次元数・メタデータ設計に関する注意点を整理
- **出典**: [Pinecone Pricing (公式)](https://www.pinecone.io/pricing/)、[Pinecone Docs: Understanding cost](https://docs.pinecone.io/guides/manage-cost/understanding-cost)、[Weaviate: A Simpler, More Transparent Pricing Model for Weaviate Cloud](https://weaviate.io/blog/weaviate-cloud-pricing-update)、[Weaviate Pricing (公式)](https://weaviate.io/pricing)、[Qdrant Pricing (公式)](https://qdrant.tech/pricing/)、[Chroma Products: ChromaDB](https://www.trychroma.com/products/chromadb)、[PostgreSQL: pgvector 0.8.0 Released!](https://www.postgresql.org/about/news/pgvector-080-released-2952/)、[Instaclustr: pgvector Key features, tutorial, and pros and cons](https://www.instaclustr.com/education/vector-database/pgvector-key-features-tutorial-and-pros-and-cons-2026-guide/)、[ideaman's Notes: Difyが対応しているベクトルデータベース](https://notes.ideamans.com/posts/2024/dify-vector-stores.html)、[Dify Docs: アプリ内でのナレッジベース統合](https://docs.dify.ai/ja-jp/guides/knowledge-base/integrate-knowledge-within-application)
- **注記**: 各社の料金プラン名・金額・無料枠は第三者メディアも含めた2026年7月時点の目安。掲載・記事化前に各公式サイト(pinecone.io/pricing、weaviate.io/pricing、qdrant.tech/pricing、trychroma.com)で最終確認を推奨
