---
title: "Embedding(埋め込み)とは何か"
part: 7
chapter: 第3章 RAGの基礎
tags: [Embedding, 埋め込み, ベクトル, セマンティック検索, RAG]
created: 2026-07-06
updated: 2026-07-31
---

# Embedding(埋め込み)とは何か

## これは何か

Embedding(埋め込み、またはEmbeddingベクトル)とは、文章・画像・音声といった情報を「意味」を表す数値の並び(ベクトル)に変換したものを指す。この変換のおかげで、コンピューターは文字面が違っても意味が近い情報同士を「近い」と判定できるようになる。たとえば「有休の繰越」と「年次有給休暇の持ち越し」は単語としては1つも一致しないが、Embeddingに変換すると数値的に近い場所に配置される。これができないと、コンピューターは単語が一致するかどうかでしか検索・比較ができず、表記ゆれや言い換えに弱い「キーワード検索」しかできない。[RAG(検索拡張生成)の基本](./rag-basics.md)や[ベクトルデータベースの基本](./vector-database-basics.md)で触れている「埋め込み」は、まさにこの仕組みのことであり、本ページはその土台となる「Embeddingとは何か」を単独で解説する。

## 仕組み・背景

### 地図の上に意味を配置する、というイメージ

Embeddingを理解する一番簡単な方法は「意味の地図」を思い浮かべることだ。地図上では、距離が近い都市ほど地理的に近い。Embeddingの世界では、意味が近い文章ほど「地図」上の距離が近くなるように数値が割り振られる。実際には2次元の地図ではなく、数百〜数千個の数値の並び(次元)からなる空間だが、考え方は同じで「似た意味のものは近くに、違う意味のものは遠くに配置される」という点だけ押さえておけばよい。

具体例で見てみる。「猫」「子猫」「犬」「自動車」という4つの言葉をEmbeddingに変換すると、イメージとしてはこうなる。

| 言葉 | 「地図」上の位置(イメージ) |
|---|---|
| 猫 | (0.82, 0.41, …) |
| 子猫 | (0.79, 0.44, …) |
| 犬 | (0.65, 0.38, …) |
| 自動車 | (0.02, -0.71, …) |

「猫」と「子猫」は数値が近く(意味が近い動物同士)、「犬」もペット・動物という意味でそこそこ近い。「自動車」だけ大きく離れた場所にある。実際のEmbeddingはこのような数値が1,000個前後並ぶ配列(ベクトル)で、人間が数値を1つずつ見て理解するものではないが、「近い数値=近い意味」という関係だけがコンピューターにとって重要になる。この近さは主に「コサイン類似度(2つのベクトルの向きがどれだけ近いか)」という指標で計算される。

### Embeddingはどこから来るのか

Embeddingは、あらかじめ大量の文章で学習された「Embeddingモデル」に文章を入力すると出力される。実務での使い方は非常に単純で、OpenAIやGoogleなどが提供するAPI(ソフトウェア同士が情報をやり取りする窓口)に文章を送ると、その文章を表す数値の配列が返ってくる、というだけである。裏側でどのような計算が行われているかを理解する必要はなく、「文章を送ると、意味を表す数値の並びが返ってくる箱」として捉えておけば実務では十分。

### 「異なるEmbeddingモデル同士は混ぜられない」という重要な制約

ここが最も実務で誤解されやすく、かつ重要な点である。Embeddingモデルが違えば、同じ文章を入力しても返ってくる数値の並びは全く異なる。地図の例で言えば、Aモデルの地図とBモデルの地図は、そもそも描き方(縮尺・向き・基準点)が違う別々の地図であり、Aモデルで作った「猫」の位置とBモデルで作った「子猫」の位置を比べても、地理的に近いかどうかは何の意味も持たない。

そのため、次のようなミスは検索結果を破綻させる。

- 過去にモデルAで変換して保存したデータに対して、モデルBで変換した質問文を使って検索する
- 同じデータベースの中に、モデルAとモデルBで変換したベクトルを混在させて保存する

どちらも「別の地図の上で距離を測る」ような行為になり、検索結果は意味的に無関係なものばかりが返ってくる。Embeddingモデルを変更する際は、保存済みのデータをすべて新しいモデルで再変換(再インデックス化)する必要がある。

なお、この制約には例外的な動きも出てきている。Voyage AIの「voyage-4」ファミリー(voyage-4-large/voyage-4/voyage-4-lite/voyage-4-nano)は、同一シリーズ内であれば異なるサイズのモデル同士でもベクトルを比較できる「共有Embedding空間」を採用しており、大きいモデルで登録したデータを小さいモデルで検索する、といった使い方が再インデックスなしで可能になっている。ただしこれは同一ベンダー・同一シリーズ内に限った話であり、「異なる提供元・異なるシリーズのモデルは混ぜられない」という基本原則自体は変わらない。

## 使いどころ・使い分け

Embeddingが役に立つのは、「意味で探したい・意味で比べたい」場面である。逆に、完全一致や特定のコードの検索にはキーワード検索の方が向く。

| 業務シーン | Embeddingが向く理由 |
|---|---|
| **社内FAQ・マニュアルの検索(セマンティック検索)** | 「有休の繰越」でも「年次有給休暇の持ち越し」でもヒットさせられる。表記ゆれ・言い換えに強い |
| **問い合わせ・レビューの重複/類似検出** | 似た内容のサポートチケットやクレームを、文言が違っても自動でグルーピングできる |
| **顧客フィードバックのテーマ分類(クラスタリング)** | 大量の自由記述レビューを、Embedding同士の近さでグループ化し「価格への不満」「配送の遅延」などのテーマを自動で浮かび上がらせる |
| **レコメンデーション(おすすめ)** | 「このユーザーが読んだ記事に近い記事」「似た商品」をEmbeddingの近さで探す |
| **RAG(社内資料に基づく回答生成)** | 質問文と資料を同じ空間に配置し、意味が近い資料を検索してAIに読ませる。詳細は[RAGの基本](./rag-basics.md)参照 |

一方、次のような場合はEmbeddingよりキーワード検索や完全一致検索が適する。

- 商品コード・契約番号・法令の条文番号など、表記が1文字でも違えば別物として扱いたい場合
- 「意味」ではなく「その単語が本文に含まれているか」自体が重要な場合(例: 監査での網羅的なキーワード抽出)

実務では、両者を組み合わせる「ハイブリッド検索」も広く使われる。詳細は[RAGの精度を上げる方法](./rag-accuracy-improvement.md)を参照。

## 実務での使い方

### コードを書かずにEmbeddingの効果を体感する

- **NotebookLM・ChatGPTのファイルアップロード**: 裏側で資料をEmbeddingに変換し、質問文と意味が近い部分を検索している。利用者はEmbeddingという言葉を意識する必要はない
- **Dify(ノーコードでRAGアプリを作る場合)**: 「ナレッジ」→「ナレッジベースを作成」→設定画面の中に「Embeddingモデル」という項目があり、OpenAI・Cohereなど複数のモデルから選べる。ここで初めて「Embeddingモデルを選ぶ」という操作に触れることになる。手順の詳細は[DifyでのRAG実装](../part10-nocode-lowcode/dify-rag-implementation.md)を参照

### 開発者向け:APIでEmbeddingを取得する最小イメージ

コピペで使える疑似コード(実際のSDK呼び出しは各社ドキュメントを参照)。

```python
# 文章をEmbedding(数値の配列)に変換する
response = embedding_model.embed("有給休暇は前年度の未消化分を翌年度に限り繰り越せる")
print(response.vector)  # 例: [0.0123, -0.0456, 0.0789, ...] のような1536個の数値

# 2つの文章の意味の近さを比較する
vector_a = embedding_model.embed("有休の繰り越しってできますか?")
vector_b = embedding_model.embed("年次有給休暇の持ち越しについて教えてください")
similarity = cosine_similarity(vector_a, vector_b)  # 1.0に近いほど意味が近い
```

### 主要なEmbeddingモデルの比較(2026年7月時点)

料金・仕様は変更されやすいため、導入前に必ず各社公式サイトで最終確認すること。

| モデル・サービス | 提供元 | 次元数 | 多言語対応 | 料金の目安(入力1Mトークンあたり) | 特徴 |
|---|---|---|---|---|---|
| **text-embedding-3-small** | OpenAI | 1,536(次元数を指定して短縮可) | 対応 | $0.02(バッチ利用は$0.01) | コストが最も安く、多くのRAG実装で既定の選択肢になっている |
| **text-embedding-3-large** | OpenAI | 3,072(短縮可) | 対応 | $0.13(バッチ利用は$0.065) | smallより精度が高い代わりに料金・保存容量も増える。MTEBベンチマーク(意味検索など複数タスクの精度を横断比較する代表的な指標)で64.6点程度 |
| **gemini-embedding-001** | Google | 3,072が既定(1,536/768に短縮可、精度劣化が小さい設計) | 100以上の言語に対応、多言語ベンチマークで上位 | $0.15(バッチ利用は$0.075) | 多言語の検索精度に強みがあり、日本語を含む非英語データのRAGで選ばれやすい。MTEB英語版で68点台とトップクラスの評価も報告されている |
| **embed-v4.0** | Cohere | 1,536 | 対応(多言語) | テキスト$0.12、画像$0.47 | テキストと画像を同じ空間に埋め込めるマルチモーダル対応、最大12.8万トークンの長文入力に対応(OpenAIの8,191トークンやVoyageの3.2万トークンより大幅に長く、長文を分割せずに扱いやすい) |
| **voyage-4ファミリー(voyage-4-large/voyage-4/voyage-4-lite/voyage-4-nano)** | Voyage AI(MongoDB傘下) | 2048/1024/512/256から選択(全モデル共通) | 対応 | voyage-4-lite $0.02、voyage-4 $0.06、voyage-4-large $0.12(いずれもバッチ利用で33%引き) | シリーズ内でベクトル空間を共有しており、サイズ違いのモデルを組み合わせても再インデックス不要。新規アカウントはシリーズ全体で最初の2億トークンが無料。2026年6月には長文のチャンク分割の悩みを軽減する新モデル「voyage-context-4」も登場 |
| **BGE-M3** | BAAI(オープンソース、MIT license) | 1,024 | 100以上の言語に対応 | 無料(自社サーバーで動かす場合はサーバー費用が発生) | 密ベクトル・疎ベクトル・トークン単位のベクトルを同時に出力でき、ハイブリッド検索を1モデルで実現。データを外部に送れない場合の有力な選択肢 |
| **Qwen3-Embedding(0.6B/4B/8B)** | Alibaba(オープンソース、Apache 2.0) | 1,024〜4,096(モデルサイズにより異なる) | 対応(多言語MTEBで上位、8Bモデルは70点台) | 無料(自社サーバーで動かす場合はサーバー費用が発生) | 2026年時点でオープンソース勢の中でも多言語精度が高い部類。ただし日本語単体の精度(JMTEBなど)では、後述の日本語特化モデルに劣る場合がある |
| **Sarashina3 embedding / PLaMo-Embedding-1B** | SB Intuitions / Preferred Networks(いずれも国産・オープンソース) | 1,536(Matryoshka表現学習で1024/512/256/128に短縮可)/ 1B相当 | 日本語特化 | 無料(自社サーバーで動かす場合はサーバー費用が発生。Sarashinaは商用利用に別途ライセンス契約が必要) | 日本語データでの検索精度を重視する場合や、国内で開発・提供されたモデルを使いたい場合の選択肢。PLaMo-Embedding-1BはApache 2.0で商用利用の制約がない |

選び方の目安。

- **「まず試したい・コストを抑えたい」→ OpenAI text-embedding-3-small**(実績が多く安価)
- **「日本語など英語以外のデータが中心」→ Google gemini-embedding-001**(多言語の検索精度で高評価)
- **「画像も一緒に検索したい」→ Cohere embed-v4.0**(テキストと画像を同じ空間で扱える)
- **「データを外部API に送れない・自社サーバー内で完結させたい」→ BGE-M3・Qwen3-Embeddingなどオープンソースモデル**(自社サーバーで運用する分、構築・保守の手間は増える)
- **「日本語データの精度を特に重視したい、かつ自社サーバーで完結させたい」→ PLaMo-Embedding-1B(商用利用可)やSarashina3 embedding**(国産の日本語特化モデル。Sarashinaは商用利用時にライセンス条件を要確認)
- **「Difyなどノーコードツールを使うだけ」→ ツールの既定設定のままでよい**(既定モデルで十分なことが多く、自分で比較検討する必要は薄い)

## 注意点・よくある誤解

- **Embeddingモデルを乗り換えると、保存済みデータの再変換(再インデックス化)が必要になる**: 前述の通り、モデルが違えば「地図」自体が違うため、過去に保存したEmbeddingはそのままでは新しい質問文と比較できない。全データを新モデルで変換し直す作業には時間とAPI利用料がかかるため、Embeddingモデルは後から気軽に変更できるものではないと認識しておく
- **次元数が大きい=常に高精度、ではない**: 次元数が大きいほど表現力は上がりやすいが、保存容量と検索コストも増える。多くのモデルは次元数を短縮して使う機能(Matryoshka表現学習などと呼ばれる技術)を持っており、精度をほとんど落とさずコストを抑えられる場合がある
- **チャンク(分割した文章の単位)が大きすぎても小さすぎても精度が落ちる**: 1つのEmbeddingは、渡した文章全体の意味を1つの数値配列に圧縮するため、長すぎる文章を渡すと複数の話題が混ざって意味がぼやける。RAGにおけるチャンクサイズの調整は[RAGの精度を上げる方法](./rag-accuracy-improvement.md)で扱う。この悩みを軽減する目的で、文書全体の文脈を保ったままチャンクを埋め込む「Voyage AIのvoyage-context-4」のようなモデルも登場しているが、2026年7月時点ではまだ発展途上の技術であり、チャンク設計を不要にするものではない
- **Embeddingにも入力できる文章量の上限がある**: モデルによって上限トークン数が異なり、上限を超えると入力が切り捨てられる、またはエラーになる。長文を扱う場合は事前に分割しておく必要がある
- **完全一致検索が必要な場面でEmbeddingだけに頼らない**: 型番・契約番号などは意味的に近い別物(例: 型番が1文字違うだけの別商品)を「近い」と誤判定するリスクがあるため、キーワード検索と組み合わせるほうが安全

## 最初の一歩

OpenAIやGoogleのEmbedding APIを試す前に、まずはDifyの「ナレッジベースを作成」画面を開き、「Embeddingモデル」の設定項目がどこにあるかを確認してみる。すでにRAGやNotebookLMを使っている場合は、意味は同じだが言い回しが違う2つの質問文(例:「有休の繰越」と「年次有給休暇の持ち越し」)で検索し、両方で同じ資料がヒットすることを確認すると、Embeddingが実際に何をしているかが体感できる。

## 関連トピック

- [RAG(検索拡張生成)の基本](./rag-basics.md)
- [ベクトルデータベースの基本(Embeddingとの関係)](./vector-database-basics.md)
- [RAGの精度を上げる方法](./rag-accuracy-improvement.md)
- [DifyでのRAG実装](../part10-nocode-lowcode/dify-rag-implementation.md)

## 更新履歴

### 2026-07-31: 主要モデル比較表とVoyage AIの制約解説を最新化
- **内容**: Voyage AIの料金をvoyage-4/voyage-4-lite/voyage-4-largeで細分化し、シリーズ内でベクトル空間を共有する仕様(サイズ違いモデルの組み合わせが再インデックス不要)を追記。長文チャンク分割の課題を軽減する新モデルvoyage-context-4に言及。比較表にオープンソースのQwen3-Embedding(多言語MTEB上位)と、国産の日本語特化モデルSarashina3 embedding・PLaMo-Embedding-1B(いずれもMatryoshka表現学習による次元短縮に対応)を追加し、「選び方の目安」にも反映。OpenAI・Google・Cohereの料金・仕様は変更なしを確認
- **出典**: [Voyage AI Blog: The Voyage 4 model family](https://blog.voyageai.com/2026/01/15/voyage-4/)、[Voyage AI Docs: Pricing](https://docs.voyageai.com/docs/pricing)、[Voyage AI Blog: voyage-context-4](https://blog.voyageai.com/2026/06/29/voyage-context-4/)、[Qwen: Qwen3 Embedding](https://qwenlm.github.io/blog/qwen3-embedding/)、[GitHub: QwenLM/Qwen3-Embedding](https://github.com/QwenLM/Qwen3-Embedding)、[SB Intuitions TECH BLOG: Sarashina3 embedding](https://www.sbintuitions.co.jp/blog/entry/2026/07/02/101054)、[Preferred Networks Tech Blog: PLaMo-Embedding-1Bの開発](https://tech.preferred.jp/ja/blog/plamo-embedding-1b/)、[Hugging Face: pfnet/plamo-embedding-1b README](https://huggingface.co/pfnet/plamo-embedding-1b/blob/main/README_ja.md)、[Awesome Agents: Embedding Model Leaderboard MTEB Rankings April 2026](https://awesomeagents.ai/leaderboards/embedding-model-leaderboard-mteb-april-2026/)

### 2026-07-06: 初版執筆
- **内容**: Embeddingの定義(文章を意味を表す数値の配列に変換する仕組み)、地図のアナロジーによる説明、Embeddingモデル間の非互換性という実務上の重要な注意点、業務シーン別の使いどころ、OpenAI/Google/Cohere/Voyage AI/BGE-M3の比較表、Difyでの遭遇箇所、チャンクサイズ・次元数に関する注意点を整理
- **出典**: [OpenAI: New embedding models and API updates](https://openai.com/index/new-embedding-models-and-api-updates/)、[OpenAI API Docs: text-embedding-3-large](https://developers.openai.com/api/docs/models/text-embedding-3-large)、[Google Developers Blog: Gemini Embedding now generally available in the Gemini API](https://developers.googleblog.com/gemini-embedding-available-gemini-api/)、[Google AI for Developers: Embeddings | Gemini API](https://ai.google.dev/gemini-api/docs/embeddings)、[Cohere Pricing (公式)](https://cohere.com/pricing)、[Oracle Cloud Docs: Cohere Embed 4](https://docs.oracle.com/en-us/iaas/Content/generative-ai/cohere-embed-4.htm)、[Voyage AI Docs: Pricing](https://docs.voyageai.com/docs/pricing)、[Voyage AI Blog: The Voyage 4 model family](https://blog.voyageai.com/2026/01/15/voyage-4/)、[BentoML: The Best Open-Source Embedding Models in 2026](https://www.bentoml.com/blog/a-guide-to-open-source-embedding-models)、[Dify Docs: ナレッジベース](https://docs.dify.ai/ja-jp/guides/knowledge-base)
- **注記**: 各社の料金・次元数・仕様は第三者メディアも含めた2026年7月時点の目安。掲載・記事化前に各公式サイト(openai.com、ai.google.dev、cohere.com、voyageai.com)で最終確認を推奨
