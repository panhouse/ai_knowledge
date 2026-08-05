---
title: "RAGの評価方法(RAGAS・LLM-as-a-Judgeなど)"
part: 7
chapter: 第4章 RAGの精度改善と基盤
tags: [RAG, 評価, RAGAS, LLM-as-a-judge, ゴールデンセット, Context Precision, Faithfulness, LangSmith]
created: 2026-07-07
updated: 2026-08-03
---

# RAGの評価方法(RAGAS・LLM-as-a-Judgeなど)

## これは何か

RAGを導入すると必ずぶつかるのが「思ったより回答の質が安定しない。でも、何をどう直せば良くなるのか判断する物差しがない」という悩みだ。[RAGの精度を上げる方法](rag-accuracy-improvement.md)では、チャンキングやハイブリッド検索といった「直す打ち手」を整理したが、そもそも「今どれくらい合っているのか」「昨日の設定変更は良くなったのか悪くなったのか」を測る仕組みがなければ、打ち手を打つたびに勘と印象で判断することになる。本ページは、その「測り方」そのもの、つまりRAGの評価手法(手動のゴールデンセットによるチェックから、RAGASのような自動評価ライブラリ、LLM-as-a-judgeによる採点まで)を整理する。「打ち手」ではなく「物差し」の話に絞っているため、改善のレバー自体は前述の[RAGの精度を上げる方法](rag-accuracy-improvement.md)、RAGの基本構造は[RAG(検索拡張生成)の基本](rag-basics.md)を先に読んでおくと理解しやすい。

## 仕組み・背景

### なぜRAGの評価は難しいのか

RAGの評価が普通のアンケートやテストの採点より厄介なのは、「検索」と「生成」という性質の違う2つの工程が直列につながっており、どちらで間違えたのかを切り分けないと直しようがないからだ。

- **検索の失敗**: そもそも正解が書かれた資料(チャンク)が検索結果に出てこない。この場合、AIがどれだけ賢くても正しく答えようがない
- **生成の失敗**: 正解が書かれた資料は検索結果に出ているのに、AIがそれを無視した、読み間違えた、あるいは資料にない内容を勝手に付け足した(ハルシネーション)

さらに、RAGの回答は自由文であり、選択式テストのように「合っている/間違っている」を機械的に◯×判定できない。同じ内容でも言い回しが違うだけで不正解と誤判定してしまうため、単純な文字列一致では評価できない。この2つの理由(工程が2段階/回答が自由文)が、RAGの評価を「なんとなく良さそう」で済ませがちにしている原因になっている。

### 評価の4つの観点

RAGの評価ライブラリの事実上の標準になっているRAGAS(Retrieval Augmented Generation Assessment、RAGパイプラインを正解データなしでも評価できるように設計されたオープンソースの評価フレームワーク)は、検索と生成を切り分けて次の4つの指標で評価する考え方を広めた。他のツール(TruLens、Microsoft Foundryなど)も呼び方は違うが、ほぼ同じ4観点で整理されている。

| 観点 | 何を測るか | 主にどこの失敗を検出するか | 別名(他ツールでの呼び方) |
|---|---|---|---|
| **Context Precision(文脈の精度)** | 検索結果として渡したチャンクのうち、実際に質問と関係あるものがどれだけの割合を占めるか | 無関係なチャンクを多く拾いすぎていないか | Retrieval Relevance(LangSmith)、Retrieval(Microsoft Foundry) |
| **Context Recall(文脈の再現率)** | 正解に必要な情報が、検索結果の中にちゃんと含まれているか | 肝心のチャンクを検索で取りこぼしていないか(検索の失敗) | Context Relevance(TruLens「RAGトライアド」の1つ)、Contextual Recall(DeepEval) |
| **Faithfulness(忠実性)** | 生成された回答の内容が、検索結果(渡したチャンク)の記述だけで裏付けられるか | 資料にない内容を勝手に付け足すハルシネーション | Groundedness(グラウンデッド性。TruLens・Microsoft Foundry系でよく使われる呼称) |
| **Answer Relevancy(回答の的確さ)** | 生成された回答が、ユーザーの質問に正面から答えているか(脱線・的外れになっていないか) | 資料は正しく読めているが、質問の意図とズレた回答をしている | Answer Relevance(TruLens)、Relevance(Microsoft Foundry) |

なお「Microsoft Foundry」は旧称「Azure AI Foundry」(さらにその前は「Azure AI Studio」)が2025年11月に改称されたもの。呼称は変わったが評価指標(Groundedness・Relevance・Retrieval等)の中身は同じ考え方を引き継いでいる。

このほか、あらかじめ用意した「模範解答」と生成結果を比較する **Answer Correctness(回答の正確性)** という指標もある。これは正解データ(ゴールデンセット)がある場合にのみ使える指標で、上記4つが「正解データなしでも計算できる」ことを売りにしているのとは性質が異なる。

### 測り方の2系統:手動評価と自動評価

これらの指標を実際に数値化する方法は大きく2つある。

1. **手動評価(ゴールデンセット・スポットチェック)**: 業務担当者が実際の質問と正解をセットにした一覧(ゴールデンセット)を作り、目視で◯×を付けていく方法
2. **自動評価**: 上記4指標などをプログラムで自動計算する方法。さらに2つの実装方式に分かれる
   - **RAGAS・TruLens・DeepEvalなどの評価ライブラリ**: 指標ごとに専用の計算ロジック(内部的にはLLMへの複数回の問い合わせを組み合わせている)を用意しており、Pythonコードから呼び出して数値を得る
   - **LLM-as-a-judge(LLMに採点させる方式)**: 「この回答は資料に忠実か、質問に的確に答えているか」を評価用のプロンプトに書き、別のAIモデルに1回のプロンプトでまとめて採点させる方式。ライブラリを使わずプロンプトだけで組めるのが特徴で、評価の型自体は[点数法(ルーブリック採点)プロンプティング](../part05-prompt-engineering/rubric-scoring-prompting.md)と同じ考え方をRAG評価に応用したものと言える

RAGASの内部でも一部の指標はLLM-as-a-judge的な仕組みで計算されているため、両者は完全に別物というより「LLMに採点させる」という共通の土台の上に、RAGAS等は指標ごとに個別のロジックを積んでいる、という関係に近い。

## 使いどころ・使い分け

| 方法 | 向いているケース | 向かないケース・限界 |
|---|---|---|
| **手動評価(スポットチェック)** | 導入初期、質問数が少ない(数十件程度)、まず現状把握したいだけ | 質問数・設定変更の頻度が増えると目視チェックが追いつかない |
| **RAGAS等の評価ライブラリ** | 検索・生成の失敗を指標別に切り分けて継続的に測りたい、CI/CD(コードを変更するたびに自動テストする仕組み)に組み込みたい、エンジニアがいる | 環境構築とコード実装が必要で、非エンジニアだけでは導入しにくい。評価用LLMの呼び出し回数が多く地味にコストがかかる |
| **LLM-as-a-judge(自作プロンプト)** | ライブラリを入れずに素早く始めたい、1回のプロンプトで複数観点をまとめて採点したい、評価理由も自然言語で欲しい | 採点者となるAIモデル・プロンプト・温度設定(出力のランダム性の度合い)によって点数がぶれることがある。同じ入力でも実行のたびに評価が変わりうる |
| **LangSmith・Langfuse・Arize Phoenixなどの観測プラットフォーム** | 本番トラフィックを継続的に監視し、問題のある回答を自動でサンプリングして評価にかけたい、どのチャンクが検索されどこで崩れたかまで追跡したい | LangSmithは有償(小規模なら無料枠内、トラフィック量に応じて課金が増える)、Arize Phoenixは自前ホストの手間がかかるなど、いずれも別途導入コストがあり、小規模な検証だけなら過剰装備になりやすい |

使い分けの基本方針は「いきなり自動評価基盤を作らない」こと。RAGの評価は「ゴールデンセットで手動チェック→問題箇所をLLM-as-a-judgeプロンプトで補助的に自動採点→件数や変更頻度が増えたらRAGAS等のライブラリやLangSmithのような専用基盤に本格導入」という順で育てるのが実務では現実的。最初から精緻な自動評価基盤を作ろうとして頓挫するより、少数のゴールデンセットで手を動かし始める方が早く効果が出る。

## 実務での使い方

### 1. まずゴールデンセット(想定質問と正解の一覧)を作る

エンジニアでなくても今日から始められる最初のステップ。スプレッドシートに以下の列を用意し、実際に聞かれそうな質問を20〜30件程度書き出す。

| 列名 | 内容例 |
|---|---|
| 質問 | 「年次有給休暇は入社何ヶ月目から使えますか?」 |
| 想定正解 | 「入社6ヶ月後、出勤率8割以上で10日付与」 |
| 正解の根拠箇所 | 「就業規則第◯条」 |
| 検索◯× | 正解の根拠チャンクが検索結果に出たか |
| 生成◯× | 出てきたチャンクをもとに正しい回答が生成されたか |
| 備考 | ズレていた場合の具体的な内容 |

「検索◯×」と「生成◯×」を分けて記録するのが最大のポイント。両方まとめて「合っている/間違っている」だけを見ると、検索側の問題(チャンキング・ハイブリッド検索・リランキングで対処)と生成側の問題(プロンプトの指示で対処)のどちらを直すべきか分からなくなる。

### 2. LLM-as-a-judgeで採点を半自動化する(コピペ実例)

ゴールデンセットの件数が増えて目視が大変になってきたら、以下のようなプロンプトを評価用のAI(ChatGPT・Claude・Gemini・API経由のいずれでも可)に投げ、採点を補助させる。生成に使ったAIと評価に使うAIはできれば別モデルにする(同じモデルだと自分の回答を甘く採点しやすい「自己評価バイアス」がかかる)。

```
あなたはRAG(検索拡張生成)システムの回答品質を採点する評価者です。
以下の [質問]・[検索結果として渡された参考資料]・[AIの回答] を読み、
4つの観点についてそれぞれ1〜5点で採点し、理由を1行で述べてください。
資料に書かれていないことを勝手に加えている場合はFaithfulnessを1〜2点にしてください。

[質問]
{ここに質問文を挿入}

[検索結果として渡された参考資料]
{ここに検索でヒットしたチャンクを挿入}

[AIの回答]
{ここに実際の生成結果を挿入}

出力形式:
- Context Precision(参考資料は質問に関係あるか): 点数 / 理由
- Faithfulness(回答は参考資料の内容だけで裏付けられるか): 点数 / 理由
- Answer Relevancy(回答は質問に正面から答えているか): 点数 / 理由
- 総合判定(合格/要修正): どちらか一言
```

このプロンプトをゴールデンセットの各行に対して実行し、「要修正」が付いた行だけ人間が目視で確認すれば、全件を最初から目視するより負担を大きく減らせる。ただし採点結果は実行のたびに多少ぶれるため、同じ入力を2〜3回実行して結果が割れる項目は人間の判断を優先する。

### 3. 継続運用が必要になったらRAGAS等のライブラリ・専用基盤を検討する

エンジニアがいる、または変更のたびに評価をやり直す運用が定着してきた段階では、次のような選択肢がある。いずれも設定・コードで触れる自由度と引き換えに、導入にエンジニアリングの工数がかかる。

| ツール | 位置づけ | 特徴 |
|---|---|---|
| **RAGAS**(`pip install ragas`。最新版0.4系。OSS、Apache 2.0) | Context Precision・Context Recall・Faithfulness・Answer Relevancyなど、指標ごとに専用ロジックを持つPythonライブラリ | 正解データなしでも計算できる指標を中心に設計されており、検索と生成を分けて数値化しやすい。指標を計算するたびにLLMへの問い合わせが複数回走るため、実行コストと時間がかかる点は考慮する。開発元の組織名がexplodinggradientsからVibrantLabsに変わっている(GitHub上のリポジトリ名・パッケージ名・インストールコマンドは変更なし) |
| **TruLens**(OSS。Snowflakeが開発を継続) | 「RAGトライアド」と呼ばれるContext Relevance・Groundedness・Answer Relevanceの3指標を中心にした評価・観測ツール | 本番運用の継続監視(オブザーバビリティ)寄りの位置づけ。Snowflakeの生成AI基盤(Cortex)との連携やMLflowとの統合が強化されている |
| **DeepEval**(Confident AI社。OSS) | RAG・エージェント・マルチターン対話など50種類以上の評価指標を持つ汎用LLM評価フレームワーク。pytest(Pythonのテストツール)と親和性が高い | CI/CDに評価を組み込み、コード変更のたびに自動テストとして走らせたい場合に向く。定型指標(Faithfulness・Answer Relevancy等)に加え、独自の採点基準を自然文で書けるG-Eval(ルーブリック採点をコード化したカスタム指標)を組み合わせるのが定石 |
| **Arize Phoenix**(OSS) | OpenTelemetry(分散システムの標準的な観測データ規格)ベースのトレーシング(処理の流れの記録)と評価をセットにした観測プラットフォーム | RAGASやDeepEvalが「採点」中心なのに対し、Phoenixは「どのチャンクが検索され、AIがどう処理し、どこで崩れたか」を可視化するデバッグ・原因調査寄りの位置づけ。ローカルやKubernetes上に自前でホストできる |
| **LangSmith**(LangChain社。有償/無料枠あり) | 本番トラフィックのログ収集(トレーシング)と評価をセットで提供するプラットフォーム | 正確性(Correctness)・関連性(Relevance)・忠実性(Groundedness)・検索関連性(Retrieval Relevance)といった評価者をあらかじめ用意。人間が採点結果を訂正すると、その訂正が few-shot 事例として評価プロンプトに自動的に反映されていく「自己改善」の仕組み(Align Evals)を持つのが特徴 |
| **Microsoft Foundry**(旧Azure AI Foundry。Microsoft) | Retrieval・Groundedness・Relevanceなど「組み込み評価者(Built-in Evaluators)」を用意 | Azure上でRAGを構築している場合、評価まで同じプラットフォーム内で完結できる。2025年11月にAzure AI Foundryから改称された |

一方、Dify(ノーコードでAIアプリを組み立てられるプラットフォーム)のようなノーコードツールは、ナレッジベースの「検索テスト」タブで個別の質問に対する検索結果を1件ずつ目視確認する機能はあるが、RAGASのような複数指標をまとめて自動採点する仕組みは標準搭載していない(2026年8月時点)。ノーコードでRAGを構築している場合、自動評価まで求めるなら「検索テストでのスポットチェック+本ページのLLM-as-a-judgeプロンプトを手動で回す」までが現実的な範囲で、指標の自動集計まで求めるならLangSmithのような外部の評価基盤と連携するか、エンジニアが別途RAGAS等を組む判断になる。

## 注意点・よくある誤解

- **LLM-as-a-judgeは「一発で正確」ではない**: 採点モデル・プロンプトの書き方・実行のたびのランダム性によって点数がぶれることがある。重要な意思決定(リリース可否の判断など)には、同じ入力を複数回採点して結果の安定性を確認するか、最終的に人間の目視確認を挟む
- **生成に使ったAIと評価に使うAIを同じにしない**: 同一モデル(または同じモデルファミリー)に自分の回答を採点させると、甘い評価になりやすい(自己評価バイアス・ファミリーバイアス)。可能であれば別ベンダーのモデルで採点する。また、回答が長く流暢なだけで高得点を付けてしまう「長さバイアス」もあるため、点数と一緒に理由も出力させて目視で妥当性を確認する
- **「検索◯×」と「生成◯×」を分けずに記録すると原因が分からなくなる**: まとめて◯×だけ付けると、チャンキング側を直すべきかプロンプト側を直すべきか判断できず、改善が的外れになる
- **正解データなし指標(Faithfulness等)と正解データあり指標(Answer Correctness)を混同しない**: 前者は「資料に忠実か」、後者は「模範解答と合っているか」を測っており、性質が異なる。ゴールデンセットに正解を用意した場合は両方を使い分けると原因の切り分けがより正確になる
- **評価の仕組みを作って満足しない**: ゴールデンセットは一度作って終わりではなく、実際に「回答が違った」と報告のあった質問を追加し続けることで、評価の精度が実態に近づいていく
- **自動評価はコストと時間がかかる**: RAGASやLLM-as-a-judgeは指標を計算するたびにAIモデルへの問い合わせが複数回発生するため、大量の質問セットを毎回フル評価すると地味に料金・待ち時間がかさむ。まずは変更のあった箇所に関連する質問だけに絞って評価するなど、範囲を絞る工夫が有効

## 最初の一歩

今使っているRAGツールで実際によく聞かれる質問を5〜10個選び、上記のスプレッドシートの列(質問・想定正解・根拠箇所・検索◯×・生成◯×)を埋めてみる。◯×が付けられた時点で、次に設定を変更したときに同じ質問セットで見比べられる「物差し」が手に入る。

## 関連トピック

- [RAG(検索拡張生成)の基本](rag-basics.md)
- [RAGの精度を上げる方法](rag-accuracy-improvement.md)
- [点数法(ルーブリック採点)プロンプティング](../part05-prompt-engineering/rubric-scoring-prompting.md)
- [DifyでのRAG実装(ナレッジベースの作成とワークフロー連携)](../part10-nocode-lowcode/dify-rag-implementation.md)

## 更新履歴

### 2026-08-03: ツール動向の節を最新化
- **内容**: RAGASの開発元組織がexplodinggradientsからVibrantLabsに変わったこと(パッケージ名・インストールコマンドは変更なし、最新版0.4.3)、TruLensがSnowflakeの下で開発継続中でMLflow連携が強化されていること、DeepEvalの運営元Confident AI社とG-Eval(カスタム採点指標)の位置づけ、観測プラットフォームとしてArize Phoenix(OpenTelemetryベースのトレーシング重視ツール)を新規に追加、LangSmithの「自己改善する評価者(Align Evals、人間の訂正をfew-shot事例として自動反映)」、Azure AI Foundryが2025年11月にMicrosoft Foundryへ改称された点を反映、LLM-as-a-judgeの注意点にファミリーバイアス・長さバイアスを追記
- **出典**: [GitHub: vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas)、[PyPI: ragas 0.4.3](https://pypi.org/project/ragas/)、[TruLens公式サイト](https://www.trulens.org/)、[TruLens Release History](https://www.trulens.org/contributing/release_history/)、[Snowflake Blog: TruLens ❤️ Snowflake OSS](https://www.snowflake.com/en/blog/trulens-open-source-ai/)、[Confident AI: DeepEval](https://www.confident-ai.com/frameworks/deepeval)、[DeepEval Docs: Introduction to LLM Evaluation Metrics](https://deepeval.com/docs/metrics-introduction)、[Arize AI: What is Arize Phoenix?](https://arize.com/docs/phoenix)、[LangChain Docs: How to improve your evaluator with few-shot examples](https://docs.langchain.com/langsmith/create-few-shot-evaluators)、[LangChain Docs: Run evals with openevals package](https://docs.langchain.com/langsmith/openevals)、[Microsoft Learn: Foundry Gets New Name (Directions on Microsoft)](https://www.directionsonmicrosoft.com/reports/foundry-gets-new-name-anthropic-models/)、[Microsoft Learn: RAG Evaluators - Microsoft Foundry](https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/rag-evaluators)、[FutureAGI Blog: LLM-as-Judge Best Practices in 2026](https://futureagi.com/blog/llm-as-judge-best-practices-2026)

### 2026-07-07: 初版執筆
- **内容**: RAGの評価が「検索の失敗」と「生成の失敗」という2段階の問題であり自由文回答のため単純な◯×判定ができないという難しさの整理、Context Precision/Context Recall/Faithfulness/Answer Relevancyの4観点とTruLens・Azure AI Foundryなど他ツールでの呼称対応表、手動評価(ゴールデンセット)と自動評価(RAGAS等のライブラリ/LLM-as-a-judge)の使い分け、ゴールデンセットのテンプレート列構成、LLM-as-a-judgeにそのまま投げられる採点プロンプト例、RAGAS/TruLens/DeepEval/LangSmith/Azure AI Foundryの主要評価ツール比較表、Difyなどノーコードツールでは自動採点の仕組みが標準搭載されていない点、自己評価バイアス・評価のブレなどの注意点を整理
- **出典**: [Ragas公式サイト](https://www.ragas.io/)、[Ragas PyPI](https://pypi.org/project/ragas/)、[Ragas Docs: Context Precision](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/)、[HIBARI Tech Blog: RAGの評価方法の実装&比較〜失敗談を添えて〜【RAGAS】【LLM-as-a-judge】](https://hibari-ai.com/techblog/rag_evaluation_article)、[SIOS Tech Lab: 【RAG評価手法】評価できないものは改善できない!?体系的に評価指標をご紹介!](https://tech-lab.sios.jp/archives/43719)、[Superlinked Blog: Evaluating Retrieval Augmented Generation using RAGAS](https://superlinked.com/blog/evaluating-retrieval-augmented-generation-ragas)、[Atlan: RAGAS, TruLens, DeepEval: LLM Evaluation Frameworks (2026)](https://atlan.com/know/llm-evaluation-frameworks-compared/)、[Braintrust: Best RAG Evaluation Tools in 2026, Compared](https://www.braintrust.dev/articles/best-rag-evaluation-tools)、[DeepEval Blog: DeepEval vs Trulens](https://deepeval.com/blog/deepeval-vs-trulens)、[LangChain: LangSmith Evaluation](https://www.langchain.com/langsmith/evaluation)、[Lubu Labs: LLM as Judge in LangSmith](https://www.lubulabs.com/ai-blog/langsmith-llm-as-judge)、[Microsoft Learn: Retrieval-Augmented Generation (RAG) Evaluators for Generative AI - Microsoft Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/evaluation-evaluators/rag-evaluators?view=foundry-classic)、[Dify公式ドキュメント: ナレッジベース](https://docs.dify.ai/ja-jp/guides/knowledge-base)
- **注記**: ragas.io・docs.ragas.io・hibari-ai.com・tech-lab.sios.jp・langfuse.com・ibm.com等の一次情報に直接アクセスできず(403)、検索エンジンのスニペット経由で内容を確認した。RAGASのGitHub運営組織がexplodinggradients/ragasからvibrantlabsai/ragasに変わっている兆候が検索結果に見られたが、正式な経緯を裏取りできなかったため本文には反映していない。ライブラリのインストールコマンド・バージョン依存の細部は導入前に公式ドキュメントでの再確認を推奨
