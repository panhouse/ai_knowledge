---
title: "Reranking(再ランク付け)の基本"
part: 7
chapter: 第4章 RAGの精度改善と基盤
tags: [RAG, Reranking, リランキング, クロスエンコーダー, Cohere Rerank, Rerank v4, Jina Reranker v3, 検索精度改善, ハイブリッド検索]
created: 2026-07-06
updated: 2026-08-02
---

# Reranking(再ランク付け)の基本

## これは何か

Reranking(リランキング、再ランク付け)とは、ベクトル検索やキーワード検索でいったん集めた候補文書の集合を、専用のモデルで「質問との関連度」に基づいてもう一度採点し、並べ替え直す処理のこと。社内RAG(検索拡張生成。資料を検索してAIに読ませてから回答させる仕組み)チャットボットで「検索結果の上位に、関連性の低いチャンク(資料を分割した断片)が紛れ込む」「文書量が増えるほど的外れな回答が増える」といった悩みが出た場合、原因の多くはここにある。[RAGの精度を上げる方法](rag-accuracy-improvement.md)では5つの改善レバーの1つとして簡潔に触れているが、本ページはリランキングという技術そのものを単独で深掘りし、なぜ必要なのか、どのモデル・サービスを選ぶべきか、コストとレイテンシ(応答までの待ち時間)のトレードオフをどう判断するかを整理する。

## 仕組み・背景

### なぜベクトル検索だけでは不十分なのか

[Embedding(埋め込み)とは何か](embedding-basics.md)や[ベクトルデータベースの基本](vector-database-basics.md)で説明した通り、通常のベクトル検索は「質問文」と「文書」をそれぞれ独立に数値の配列(ベクトル)に変換し、その近さ(コサイン類似度など)で候補を絞り込む。この方式は「bi-encoder(バイエンコーダー)方式」と呼ばれ、文書側のベクトルを事前に計算・保存しておけるため、数百万件規模の文書からでもミリ秒単位で候補を返せるという speed(速さ)の利点がある。

しかし bi-encoder には構造上の弱点がある。質問と文書を「別々に」1本のベクトルへ圧縮してから比べるため、質問の中のどの単語が文書のどの部分に対応するかという細かい相互作用を見ずに近さを判定してしまう。その結果、「表現は似ているが実は聞かれていることとズレている」候補が上位に紛れ込みやすい。たとえるなら、2つのレポートをそれぞれ一言で要約してから、その要約文だけを見比べて「似ているかどうか」を判断するようなもので、要約段階で失われる細部の食い違いに気づけない。

### 2段階方式(retrieve-then-rerank)という解決策

そこで実務では、検索を2段階に分ける設計が標準になっている。

1. **1段目(Retrieve、検索)**: ベクトル検索やキーワード検索、あるいは両方を組み合わせたハイブリッド検索で、まず候補を広めに集める(例: 上位20〜100件)。速さ優先で、多少ノイズが混じっても構わない
2. **2段目(Rerank、再ランク付け)**: 1段目で絞った候補だけを対象に、質問文と文書を1組にして同時にモデルへ入力し、関連度スコアを直接計算し直す「cross-encoder(クロスエンコーダー)方式」のモデルにかける。質問と文書のすべての単語同士の関係を見た上で採点するため、bi-encoderより精度が高い

cross-encoder は精度が高い代わりに、候補1件ごとに質問との組み合わせを毎回計算し直す必要があり、計算コストが bi-encoder よりはるかに高い。数百万件全体にこの方式を使うと実用的な速度が出ないため、「1段目の bi-encoder で候補を絞り込み、2段目の cross-encoder(リランキングモデル)で上位だけを精密採点する」という役割分担が定着している。実務者が押さえるべきはアルゴリズムの詳細ではなく、「広く速く集める段階」と「狭く正確に選び直す段階」を分けている、という設計思想そのものである。

### リランキングが効くとされる場面

海外のベンチマーク検証では、リランキングを追加することで検索結果の上位に正解が来ているかを測る指標(nDCGやMRRなど)が15〜40%程度改善したとする報告が複数ある。特に効果が出やすいのは、[RAGの精度を上げる方法](rag-accuracy-improvement.md)でも触れた「文書量が多いナレッジで、上位の検索結果に関連度の低いチャンクが混ざる」症状のケースである。

## 使いどころ・使い分け

### 導入すべきかどうかの判断基準

すべてのRAGにリランキングが必要なわけではない。以下の基準で「試す価値があるか」を見極める。

| 状況 | リランキング導入の要否 |
|---|---|
| 文書数が少ない(数十件程度)、表記が統一されている | 効果が薄いことが多い。まずチャンキング・資料整形を優先 |
| 文書数が多い(数百〜数万件)、部署・製品・年度をまたいで似た内容の文書が存在する | 効果が出やすい。導入を検討する価値が高い |
| ハイブリッド検索(ベクトル+キーワード)をすでに導入している | 1段目の精度がある程度出ている状態でさらに底上げできるため相性が良い |
| 社内向けの検索・チャットボットで、数百ミリ秒〜1秒程度の応答遅延が許容できる | 導入しやすい |
| リアルタイム性が非常に重要な用途(音声対話でのミリ秒単位の応答など) | レイテンシ増加が許容できるか事前に検証が必要 |
| 機密情報を外部APIに送れない | クラウドAPI型ではなく、自社サーバーで動かすOSSのリランキングモデルを検討する |

### bi-encoder(ベクトル検索)と cross-encoder(リランキング)の役割の違い

| 観点 | bi-encoder(1段目・ベクトル検索) | cross-encoder(2段目・リランキング) |
|---|---|---|
| 処理方式 | 質問と文書を別々にベクトル化してから比較 | 質問と文書を1組にして同時に入力し、関連度を直接計算 |
| 速度 | 非常に速い(事前計算済みのベクトルを比較するだけ) | 遅い(候補ごとに毎回計算し直す) |
| 精度 | 表記ゆれには強いが、細かい文脈のズレを見落としやすい | 質問と文書の細部の対応関係まで見るため精度が高い |
| 適用範囲 | 数百万件規模の全文書が対象になれる | 1段目で絞った上位数十件程度が対象の限界 |
| 役割 | 広く速く候補を集める | 狭く正確に並べ替え直す |

## 実務での使い方

### 主要なリランキングモデル・サービスの比較(2026年8月時点)

料金・性能は変更されやすいため、導入前に必ず各社公式サイトで最終確認すること。特にCohereは2026年7月1日にRerank v3.5を非推奨化し、8月1日以降 `rerank-v3.5` 宛のリクエストは自動的に後継の `rerank-v4.0-fast` に転送される(返却スコアの分布が変わるため、スコア閾値をハードコードしている場合は再調整が必要)。

| モデル・サービス | 提供元 | 提供形態 | 料金の目安 | 多言語対応 | 特徴 |
|---|---|---|---|---|---|
| **Rerank v4.0 Fast / v4.0 Pro** | Cohere | API | Fast: $2.00 / 1,000検索、Pro: $2.50 / 1,000検索(1検索=クエリ1件+文書最大100件) | 100以上の言語(日本語含む) | 2025年12月にRerank 4世代へ刷新(旧v3.5は2026年8月に自動でFastへ移行済み)。リランキング専業サービスの代表格で、DifyなどノーコードツールでもRerankモデルプロバイダーとして標準サポートされる |
| **Reranker v3 / v3.5(旧v2 base-multilingual)** | Jina AI | API | 入出力ともに$0.02 / 100万トークン、新規APIキーに1,000万トークンの無料枠 | 多言語対応 | v3は0.6BパラメータでBEIRベンチマークがSOTA級。候補文書をまとめて1つの文脈窓に入れて相互作用を見る「listwise(リストワイズ)」方式を採用し、精度と速度を両立。後継のv3.5も公開済み |
| **rerank-2.5 / rerank-2.5-lite** | Voyage AI(MongoDB傘下) | API | rerank-2.5: $0.05 / 100万トークン、rerank-2.5-lite: $0.02 / 100万トークン、新規アカウントは2億トークンまで無料 | 対応 | liteモデルは同等精度で高速。MongoDB Atlasとの連携に強み |
| **BGE reranker v2-m3 / v2-gemma**| BAAI(オープンソース) | OSS(自社サーバーで運用) | 無料(サーバー費用は別途) | 100以上の言語 | Embeddingモデルの[BGE-M3](embedding-basics.md)と対になる標準リランカー。より高精度を求める場合はLLMベースの`bge-reranker-v2-gemma`系も選べる(その分推論コストは上がる)。データを外部に送れない場合の有力な選択肢 |
| **japanese-reranker シリーズ(hotchpotch)** | 個人開発者(hotchpotch、Hugging Face公開) | OSS(自社サーバーで運用) | 無料(サーバー費用は別途) | 日本語特化 | tiny/xsmall/small/baseなど複数サイズを用意し、ModernBERTベースの[ruri-v3](https://huggingface.co/collections/hotchpotch/query-crafter-japanese)を土台に再学習。小型モデルはCPUやApple Siliconでも実用速度で動作し、日本語RAGでのコスト・精度バランスに優れる |
| **Dify内蔵のRerankモデル連携** | Dify(ノーコードプラットフォーム) | 上記モデルをプロバイダー登録して利用 | 登録したモデルの料金に準じる | 登録したモデルに準じる | リランキングモデル自体は提供しておらず、Cohere・Jina AIなどをモデルプロバイダーとして登録して呼び出す仕組み |

選び方の目安。

- **「まず試したい・実績重視」→ Cohere Rerank**(対応ツールが多く導入事例が豊富。新規導入なら最初からv4.0系を選ぶ)
- **「コストを抑えたい・API従量課金の単価を下げたい」→ Jina Reranker や Voyage rerank-2.5-lite**(無料枠が大きく、トークン単価も低い)
- **「データを外部に送れない・自社サーバー内で完結させたい」→ BGE reranker や hotchpotchの日本語リランカー**(OSSなので自社インフラで運用できる)
- **「日本語の資料が中心で、精度とコストのバランスを取りたい」→ hotchpotchの日本語リランカー**(小型モデルでも実用的な速度と精度が報告されている)

### Difyでリランキングを設定する(画面の場所)

1. Difyの管理画面で「設定」→「モデルプロバイダー」を開き、Cohere や Jina AI などリランキングモデルを提供するプロバイダーのAPIキーを登録する
2. 「ナレッジ」→対象のナレッジベースを開き、「設定」タブの「検索設定」を開く
3. 「検索方法」を「ハイブリッド検索」に切り替える(ベクトル検索のみの設定ではRerankモデルの項目自体が意味を持たない)。Difyのハイブリッド検索には並べ替え方式が2種類あり、「重み設定(weight_rerank)」はベクトル検索とキーワード検索のスコアを重み付けで合成するだけで追加のモデル呼び出しは発生しない無料の方式、「Rerankモデル(rerank_model)」は本ページで扱う外部のcross-encoderモデルを呼び出す方式で、精度は高いがAPI費用とレイテンシが乗る
4. 精度を優先する場合は「Rerankモデル」をオンにし、手順1で登録したモデル(例: Cohere rerank-v4.0-fast)を選択する
5. Top-K(リランキング後に採用する上位件数。Rerankモデル選択時はモデルの最大入力件数に応じて自動調整される)とスコア閾値(この値を下回る候補は採用しない)を設定する。Top-Kを絞りすぎると必要な情報まで落ちる、緩すぎるとノイズが残るため、後述の検索テストで調整する
6. 画面右側の「検索テスト」タブで実際の質問文を入力し、Rerankモデルのオン・オフ(または重み設定との切り替え)を試して、狙った文書が上位に出るようになったかを見比べる

### コピペで使える実例:Cohere Rerank APIの最小呼び出しイメージ

開発者向けの疑似コード(実際のSDK呼び出しは公式ドキュメントを参照)。

```python
# 1段目のベクトル検索で候補を広めに集める(例: 上位30件)
candidates = vector_db.query(vector=query_vector, top_k=30)

# 2段目でリランキングモデルにかけ、質問との関連度で並べ替え直す
reranked = cohere_client.rerank(
    model="rerank-v4.0-fast",  # 旧rerank-v3.5は2026年8月以降このモデルへ自動転送される
    query="有休の繰り越しってできますか?",
    documents=[c.text for c in candidates],
    top_n=5,  # 最終的にAIへ渡す件数
)
```

### 料金試算の考え方

Cohere は「1検索(クエリ1件+文書最大100件)あたり」の従量課金、Jina AI・Voyage AI は「処理したトークン数」に応じた従量課金と、課金の単位が異なる。想定する1日あたりの質問数、1回の検索で何件の候補をリランキングにかけるか(Top-Kの設定値)を掛け合わせて概算しておくと、無料枠を超えた際のコスト急増を防げる。

### Difyのハイブリッド検索まわりの動き

DifyのGitHub上では、既存の「重み設定(weight_rerank)」「Rerankモデル(rerank_model)」に加えて、BM25とベクトル検索のランキング順位だけで統合するRRF(Reciprocal Rank Fusion、スコアの正規化が不要でElasticsearchやLangChainでも広く使われる方式)を3つ目の並べ替え戦略として追加する提案が議論されている。2026年8月時点では未実装の機能要望であり、実際にDifyへ導入する際は自社の環境のバージョンで利用できる方式を公式ドキュメントで確認すること。

## 注意点・よくある誤解

- **モデルの世代交代でスコアの水準が変わることがある**: Cohereは2026年7月にRerank v3.5を非推奨化し、2026年8月1日以降は`rerank-v3.5`宛のリクエストが自動で後継の`rerank-v4.0-fast`に転送される仕様になった。新旧モデルでは返却される関連度スコアの分布が異なるため、「スコアが0.5以上の候補だけ採用する」といった閾値をハードコードしている場合は、モデル移行のタイミングで挙動が変わっていないか必ず確認・再調整する
- **「有効にすれば必ず精度が上がる」わけではない**: 文書数が少なく表記が統一されている場合は効果が薄い。まず[RAGの精度を上げる方法](rag-accuracy-improvement.md)の診断テーブルで症状を確認し、当てはまる場合に導入する
- **レイテンシ(応答までの待ち時間)が増える**: 検索のたびに追加のモデル呼び出しが発生するため、候補件数(Top-K)が多いほど数百ミリ秒〜1秒程度、応答が遅くなることがある。社内向けチャットボットでは許容範囲でも、リアルタイム性が重要な用途では事前に体感速度を検証する
- **コストは候補件数(Top-K)と質問数に比例して積み上がる**: 1段目で集める候補を無闇に増やすと、2段目のリランキングにかかる料金も比例して増える。1段目の候補件数は「精度に必要な最小限」に絞るのが基本
- **他のレバーを飛ばして真っ先に導入しない**: チャンクサイズの調整や資料のノイズ除去といった無料・低コストの改善を先に試し、それでも解決しない場合にリランキングを検討するのが費用対効果の観点で妥当な順序
- **日本語データの場合、英語中心に学習されたモデルでは精度が伸びにくいことがある**: 日本語の資料が中心なら、多言語対応をうたうモデルでも実際に検索テストで日本語での精度を確認し、必要に応じて日本語特化のOSSモデル(hotchpotchの日本語リランカーなど)も比較対象に入れる

## 最初の一歩

今使っているRAGツール(Difyなど)で、検索テスト画面から実際によく聞かれる質問を入力し、Rerankモデルをオンにした場合とオフにした場合とで、上位に出てくる文書がどう変わるかを見比べてみる。

## 関連トピック

- [RAG(検索拡張生成)の基本](rag-basics.md)
- [RAGの精度を上げる方法](rag-accuracy-improvement.md)
- [Embedding(埋め込み)とは何か](embedding-basics.md)
- [ベクトルデータベースの基本(Embeddingとの関係)](vector-database-basics.md)
- [DifyでのRAG実装](../part10-nocode-lowcode/dify-rag-implementation.md)

## 更新履歴

### 2026-08-02: モデル・料金・Difyの検索方式まわりを最新化
- **内容**: Cohereが2026年7月にRerank v3.5を非推奨化し、8月1日以降は`rerank-v4.0-fast`へ自動転送される点を反映してモデル比較表・コピペ実例を`rerank-v4.0-fast`/`rerank-v4.0-pro`(料金: Fast $2.00/1,000検索、Pro $2.50/1,000検索)に更新。Jina AIの新型`reranker v3`(0.6B、listwise方式、BEIRでSOTA級)と後継の`v3.5`の存在を追記。BGE rerankerの高精度版(`v2-gemma`系)、hotchpotchの日本語リランカーがModernBERT/ruri-v3ベースである点を追記。Difyのハイブリッド検索が「重み設定(weight_rerank)」と「Rerankモデル(rerank_model)」の2方式であること、RRF(Reciprocal Rank Fusion)が3つ目の方式として議論中(未実装)であることを追記。スコア閾値の再調整に関する注意点を追加
- **出典**: [Cohere Rerank 3.5 (Deprecated) — Oracle Cloud Infrastructure Docs](https://docs.oracle.com/en-us/iaas/Content/generative-ai/cohere-rerank-3-5.htm)、[cohere-rerank-3.5 | Pinecone Docs](https://docs.pinecone.io/models/cohere-rerank-3.5)、[Rerank 4: Cohere's Most Powerful Reranker Yet | Cohere](https://cohere.com/blog/rerank-4)、[Rerank v3.5 - API Pricing & Providers | OpenRouter](https://openrouter.ai/cohere/rerank-v3.5)、[Rerank 4 Pro - API Pricing & Providers | OpenRouter](https://openrouter.ai/cohere/rerank-4-pro)、[Rerank 4 Fast pricing & specs — Cohere | CloudPrice](https://cloudprice.net/models/cohere-rerank-4-fast)、[Cohere AI pricing in 2026: A complete guide to real costs | eesel AI](https://www.eesel.ai/blog/cohere-ai-pricing)、[Jina Reranker v3: 0.6B Listwise Reranker for SOTA Multilingual Retrieval | Jina AI](https://jina.ai/news/jina-reranker-v3-0-6b-listwise-reranker-for-sota-multilingual-retrieval/)、[jinaai/jina-reranker-v3 | Hugging Face](https://huggingface.co/jinaai/jina-reranker-v3)、[jina-reranker-v3.5: An Efficient Listwise Reranker with Hybrid Attention and Self-Distillation (arXiv)](https://arxiv.org/html/2607.18152)、[rerank-2.5 - API Pricing & Providers | OpenRouter](https://openrouter.ai/voyageai/rerank-2.5)、[Rerank 2.5 Lite pricing — Voyage AI | Future AGI](https://futureagi.com/llm-cost-calculator/voyage-ai/rerank-2-5-lite/)、[BAAI/bge-reranker-v2-gemma | Hugging Face](https://huggingface.co/BAAI/bge-reranker-v2-gemma)、[hotchpotch/query-crafter-japanese collection | Hugging Face](https://huggingface.co/collections/hotchpotch/query-crafter-japanese)、[hotchpotch/japanese-reranker-xsmall-v2 | Hugging Face](https://huggingface.co/hotchpotch/japanese-reranker-xsmall-v2)、[[Feature] Add RRF as a rerank strategy for hybrid search · langgenius/dify Discussion #34643](https://github.com/langgenius/dify/discussions/34643)、[知識検索 - Dify Docs](https://docs.dify.ai/ja/cloud/use-dify/nodes/knowledge-retrieval)
- **注記**: Cohereの正式ドキュメント(docs.cohere.com、cohere.com/pricing)は今回のリサーチ環境からは直接アクセスできず、Oracle Cloud・Pinecone・OpenRouter・CloudPriceなど複数の第三者ドキュメント・料金アグリゲータの記載を突き合わせて裏取りした。掲載・記事化前に可能であればcohere.com公式で最終確認を推奨

### 2026-07-06: 初版執筆
- **内容**: リランキングの定義と2段階検索(retrieve-then-rerank)の設計思想、bi-encoder(ベクトル検索)とcross-encoder(リランキング)の違いと速度・精度のトレードオフ、導入すべきかどうかの判断基準、Cohere Rerank/Jina Reranker/Voyage AI/BGE reranker/hotchpotchの日本語リランカーの比較表、Difyでの設定手順(モデルプロバイダー登録→検索設定→Rerankモデル有効化)、料金試算の考え方、レイテンシ・コストに関する注意点を整理
- **出典**: [Cohere Rerank (公式)](https://cohere.com/rerank)、[Cohere Pricing (公式)](https://cohere.com/pricing)、[Rerank v3.5 - API Pricing & Providers | OpenRouter](https://openrouter.ai/cohere/rerank-v3.5)、[Jina AI Reranker API (公式)](https://jina.ai/reranker/)、[jinaai/jina-reranker-v2-base-multilingual | Hugging Face](https://huggingface.co/jinaai/jina-reranker-v2-base-multilingual)、[Voyage AI Docs: Pricing](https://docs.voyageai.com/docs/pricing)、[hotchpotch/japanese-reranker-base-v2 | Hugging Face](https://huggingface.co/hotchpotch/japanese-reranker-base-v2)、[renue: Cohere/Voyage/Jina/BGE/日本語OSSでRAG精度を15〜40%改善するRerankerガイド2026](https://renue.co.jp/posts/reranker-cross-encoder-cohere-voyage-jina-japanese-rag-guide-2026)、[Bi-Encoders vs Cross-Encoders — ZeroEntropy Blog](https://zeroentropy.dev/articles/biencoder-vs-crossencoder/)、[Towards Data Science: Advanced RAG Retrieval: Cross-Encoders & Reranking](https://towardsdatascience.com/advanced-rag-retrieval-cross-encoders-reranking/)、[Dify Docs (レガシー): Rerank](https://legacy-docs.dify.ai/ja-jp/learn-more/extended-reading/retrieval-augment/rerank)、[Qiita(pyon_kiti_jp): DifyのRerank設定について](https://qiita.com/pyon_kiti_jp/items/599040741ff988461077)
- **注記**: Cohere/Jina/Voyageの料金・無料枠、hotchpotch系モデルの性能評価は第三者メディア・検索エンジンのスニペット経由での確認を含む2026年7月時点の目安。掲載・記事化前に各公式サイト(cohere.com、jina.ai、voyageai.com)で最終確認を推奨
