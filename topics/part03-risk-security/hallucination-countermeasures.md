---
title: ハルシネーション(AIの誤情報生成)への対策
part: 3
chapter: 第2章 ハルシネーション対策
tags: [ハルシネーション, リスク管理, ファクトチェック, RAG]
created: 2026-07-05
updated: 2026-07-05
---

# ハルシネーション(AIの誤情報生成)への対策

## これは何か

ハルシネーション(hallucination)とは、生成AIが事実に基づかない情報や、存在しない出典・数値・法令・URLなどを、あたかも真実であるかのように自信満々の文章で作り出してしまう現象のこと。厄介なのは「わかりません」と言わずに、もっともらしい嘘を流暢に出力する点で、忙しい業務の中でチェックを怠るとそのまま資料・顧客向け文書・意思決定に紛れ込んでしまう。ハルシネーションは技術的に完全にはゼロにできないため、「起きる前提」でどう防止・検知するかという運用スキルが必須になる。

## 仕組み・背景

生成AI(LLM = 大規模言語モデル)は、事実データベースを検索して答えているのではなく、学習した大量の文章から「次に来る確率が最も高い単語」を予測して文章を生成している。そのため、学習データにない情報や、頻度の低いマイナーな事実を聞かれると、統計的にもっともらしい単語列を「それらしく」埋めてしまう。

OpenAIが2025年9月に発表した論文「Why Language Models Hallucinate」は、この原因を突き詰めて説明している。要点は、モデルの訓練・評価の仕組み自体が「わからない」と正直に答えるより、自信満々に(誤りでも)断言する方が高スコアになるよう設計されてしまっている、という点にある。試験で「わからない」と書けば0点、適当に答えれば正解の可能性がある選択式テストと同じ構造で、モデルは「当てずっぽうで答える」方に最適化されてしまっている([OpenAI, 2025](https://openai.com/index/why-language-models-hallucinate/))。この論文は、評価方法自体を「不確実性を正直に示した方が得をする」ように変えない限り、ハルシネーションは構造的になくならないと結論づけている。

もう一つの背景要因が「知識のカットオフ」で、モデルの学習データには収集時点までの情報しか入っていない。最新の価格改定や法改正、社内の非公開情報を聞かれても、モデルは古い知識や一般論で「それらしく」補ってしまう。これを補うのが後述するWeb検索接続やRAG(検索拡張生成、Retrieval-Augmented Generation の略。回答の前に外部の正確な情報源を検索し、その内容を根拠にして回答を組み立てる仕組み)である。

## 使いどころ・使い分け

すべての生成AI利用に同じ警戒レベルを当てはめる必要はない。用途によってハルシネーションのリスクと必要な対策レベルは大きく変わる。

| リスク水準 | 具体例 | 対策の目安 |
|---|---|---|
| 高(必ず一次情報で裏取り) | 法令・契約条項の解釈、医療・薬事情報、統計数値・引用文献、顧客への公式回答、社外公開資料 | Web検索/RAGを必須にし、出典を明示させ、人間が一次情報に当たって検証してから使用 |
| 中(構造は使えるが要チェック) | 社内向け報告書のドラフト、競合分析、企画書のたたき台、メール文面 | 固有名詞・数値・日付だけ重点的にファクトチェック。全文を鵜呑みにしない |
| 低(そのまま使いやすい) | 文章の言い換え・要約(原文がある場合)、ブレインストーミング、壁打ち相手、構成案の叩き台 | 事実性より発想の広がりを重視する用途なので許容度が高い |

判断基準はシンプルで、「その情報が間違っていたら誰かが損をするか・誤解が広がるか」で考える。数値・固有名詞・日付・法令・引用は特に誤りが混入しやすく、かつ誤りに気づきにくいので要注意ゾーンとして扱う。

また、モデルの傾向として「推論(reasoning)を深く行うモデルほどハルシネーションが減る」とは限らない点も押さえておきたい。OpenAIの検証では、推論モデルのo3は人物に関する質問(PersonQAベンチマーク)で33%の頻度で誤答し、前世代のo1(16%)の倍以上だったと報告されている([OpenAI, 2025](https://openai.com/index/why-language-models-hallucinate/))。「賢そうなモデル=嘘をつかないモデル」ではない、という前提でツールを選ぶ必要がある。

参考までに、要約タスクにおける事実整合性を継続計測しているVectara社の「Hallucination Leaderboard」(2026年5月時点)では、GPT-5.4-nanoが3.1%、Gemini-2.5-flash-liteが3.3%、GPT-5.4-miniが5.5%、Gemini-2.5-proが7.0%、Claude-haiku-4.5が9.8%、Claude-opus-4.5が10.9%などとなっており、同じ「文書要約」というタスクでもモデルによって数倍の差がある([Vectara Hallucination Leaderboard](https://github.com/vectara/hallucination-leaderboard))。この数値は「要約時に原文にない内容を付け加える頻度」を測ったものであり、一般的な質問応答すべてに当てはまるわけではないが、モデル選定時の目安にはなる。数値は日々更新されるため、実際に使う直前に最新のリーダーボードを確認するとよい。

## 実務での使い方

### 1. プロンプトで「わからない」を許可する

最も効果が高く、かつ今日から使える対策は、プロンプトの中で「不確実なら断言せず、わからないと答えてよい」と明示すること。Anthropicの公式ガイドでも、これは基本かつ強力な手法として紹介されている([Anthropic, Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations))。

コピペで使えるプロンプト例:

```
あなたはM&Aアドバイザーとして、この買収検討レポートを分析してください。
<レポート>
{{レポート本文}}
</レポート>

財務予測・統合リスク・規制上のハードルに焦点を当てて分析してください。
レポートに記載がない、または判断材料が不十分な点については、
推測で埋めずに「この点については十分な情報がありません」と明記してください。
```

### 2. 出典・引用を強制する(裏取り可能にする)

「情報源を示せ」と指示するだけで、根拠のない発言を減らせる。さらに一歩進めて、生成後に「各主張に対応する引用元があるか自己チェックさせる」と精度が上がる。

```
以下の資料だけを情報源として、新製品「〇〇」に関するプレスリリース案を作成してください。
<資料>
{{製品資料・市場レポート}}
</資料>

作成後、本文中の主張ひとつひとつについて、資料内の該当箇所を直接引用して
裏付けを示してください。裏付けとなる引用が資料内に見つからない主張は、
本文から削除し、削除箇所を[ ]で示してください。
```

長文(2万トークン超)を扱う場合は、まず該当箇所を一字一句そのまま引用させてから要約・分析させると、本文に書かれていない内容を作文しにくくなる([Anthropic, Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations))。

### 3. 「Web検索」「RAG」など根拠を外部に持たせる機能を使う

チャット単体の知識に頼らず、外部の情報源を検索させて回答の根拠にする機能は、最新情報のズレによるハルシネーションを大きく減らせる。ツールごとの対応は以下の通り。

| 機能 | ChatGPT | Claude | Gemini |
|---|---|---|---|
| Web検索でグラウンディング(最新情報を検索して根拠にする) | チャット画面下部のツールから「検索」を有効化。既定でも必要に応じ自動的にWeb検索が働く | 画面左下のツールアイコンから「Web検索」をオン([Anthropic Help Center](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)) | 回答の下、三点メニューから「回答を再確認」を選ぶと、Google検索と照合し一致箇所を緑、未確認・古い箇所をオレンジで色分け表示([Google, Geminiアプリ ヘルプ](https://support.google.com/gemini/answer/14143489?hl=ja)) |
| 独自ファイル・社内文書に基づく回答(RAG) | カスタムGPTの「Knowledge(ナレッジ)」欄にファイルをアップロード、または「コネクタ」でクラウドストレージ・メール等と接続([OpenAI Help Center](https://help.openai.com/ja-jp/articles/8868588-retrieval-augmented-generation-rag-and-semantic-search-for-gpts)) | プロジェクト機能にファイルを追加してその範囲内で回答させる。API利用時は「Citations」機能で文書中の該当箇所を自動引用([Anthropic, Citations API](https://claude.com/blog/introducing-citations-api)) | Gemini for Google Workspaceでドライブ内文書を参照、開発者向けにはVertex AI Searchなどと連携 |
| API/開発者向けの検索接続 | Assistants/Responses APIの file search ツール | Web search tool、Citations API | Grounding with Google Search(有料枠は1,000件あたり35ドル程度)([Google Developers Blog](https://developers.googleblog.com/en/gemini-api-and-ai-studio-now-offer-grounding-with-google-search/)) |

判断基準は「その回答は最新情報が必要か」「回答の根拠が社内の特定文書に限定されるべきか」。前者ならWeb検索、後者ならRAG(ナレッジ/プロジェクト機能)を有効にする。両方とも使わずにチャット単体の「記憶」だけに頼るのは、価格・法令・統計など変化する情報を扱う場面では避けたい。

### 4. 出力後のセルフチェックをAI自身にやらせる

生成させた文章をそのまま使わず、もう一度AIに「この文章の中で、根拠が曖昧な記述・数値・固有名詞をリストアップして」と聞き直すと、一次チェックとして機能する。さらに重要な文書では、同じ質問を複数回投げて回答がぶれる箇所を洗い出す(ぶれる=不確実な部分である可能性が高い)という手法も有効([Anthropic, Reduce hallucinations](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations))。

```
先ほどの回答を見直し、根拠となる情報源が明示されていない断定的な記述
(数値・固有名詞・日付・法令名など)をすべてリストアップしてください。
それぞれについて、確信度合い(高・中・低)も付けてください。
```

## 注意点・よくある誤解

- **「賢いモデル・推論モデルだから嘘をつかない」は誤解**: 前述の通り、深く推論するモデルほど誤答が増えるケースが報告されている。モデルの世代が新しい・高性能=ハルシネーションが少ない、と単純に考えないこと。
- **Web検索を有効にしても万能ではない**: 検索結果自体が誤った情報や古い情報を含んでいれば、AIはそれをそのまま根拠として使ってしまう。GeminiのGoogle自身のヘルプでも「ソースが示されていてもGeminiの判断が誤っていることがある」と明記されている([Google, Geminiアプリ ヘルプ](https://support.google.com/gemini/answer/14143489?hl=ja))。検索連携は「精度を上げる補助」であって「事実確認の代替」ではない。
- **数値・固有名詞・URLは特に危険**: 存在しない論文・判例・URLを、実在するかのような体裁で生成する例が典型的なハルシネーション。重要な数値やリンクは必ずクリックして一次情報を確認する。
- **「出典を出させたから安心」も油断禁物**: 出典として提示された文献名・URLそのものが実在しない場合がある。出典が実在するか、内容が本当に一致しているかまで確認して初めて裏取りが完了する。
- **ハルシネーションはゼロにはできない**: OpenAIの論文が示す通り、現在のモデルの訓練・評価の仕組みが変わらない限り、原理的な発生源は残り続ける。「対策すれば絶対に起きない」ではなく、「重要度に応じて検知・裏取りの仕組みを組み込む」という運用でリスクを管理する。

## 最初の一歩

次に生成AIへ調べもの・分析を依頼するときは、プロンプトの末尾に「わからない場合は、推測で埋めずにわからないと答えてください」の一文を必ず添えてみる。それだけでも断定的な誤情報の混入をかなり減らせる。

## 関連トピック
- [生成AI利用における情報漏洩対策](./information-leakage-prevention.md)
- [AIが扱いやすいデータ形式](../part06-data-analysis/ai-friendly-data-formats.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: ハルシネーションの発生メカニズム、リスク水準別の使い分け、ChatGPT/Claude/Geminiの根拠付け機能の対応表、コピペで使えるプロンプト例(不確実性の許可・引用強制・セルフチェック)をまとめた初版を執筆
- **出典**: [Why language models hallucinate | OpenAI](https://openai.com/index/why-language-models-hallucinate/)
- **出典**: [Reduce hallucinations | Claude Platform Docs](https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-hallucinations)
- **出典**: [Introducing Citations on the Anthropic API](https://claude.com/blog/introducing-citations-api)
- **出典**: [Enable and use web search | Claude Help Center](https://support.claude.com/en/articles/10684626-enable-and-use-web-search)
- **出典**: [関連ソースを表示し、Geminiアプリの回答を再確認する | Google](https://support.google.com/gemini/answer/14143489?hl=ja)
- **出典**: [Grounding with Google Search | Gemini API](https://ai.google.dev/gemini-api/docs/google-search)
- **出典**: [Gemini API and Google AI Studio now offer Grounding with Google Search](https://developers.googleblog.com/en/gemini-api-and-ai-studio-now-offer-grounding-with-google-search/)
- **出典**: [GPT向けのRetrieval Augmented Generation（RAG）とセマンティック検索 | OpenAI Help Center](https://help.openai.com/ja-jp/articles/8868588-retrieval-augmented-generation-rag-and-semantic-search-for-gpts)
- **出典**: [Vectara Hallucination Leaderboard](https://github.com/vectara/hallucination-leaderboard)
