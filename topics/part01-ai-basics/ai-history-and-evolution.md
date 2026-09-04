---
title: 生成AIの発展の歴史
part: 1
chapter: 第2章 AIの歴史とブーム
tags: [AI基礎, 生成AI, LLM, Transformer, 歴史, AIエージェント]
created: 2026-07-05
updated: 2026-08-19
---

# 生成AIの発展の歴史

## これは何か

「半年前に覚えたChatGPTの使い方が、もう古い」「モデル名がGPT-5.5、Gemini 3.5、Claude Sonnet 5と次々に変わって追いきれない」——生成AIを業務で使う人の多くが感じる悩みである。この変化の速さは気まぐれではなく、AI開発の「進化のドライバー(何に投資すれば性能が伸びるか)」がここ数年で数回切り替わってきた結果であり、切り替わりのたびに主要ツールの機能セットが一段変わっている。ドライバーの移り変わりを押さえておくと、新モデル発表のたびに一喜一憂せずに「今回は何が変わったのか」を自分で判断できるようになる。

## 仕組み・背景

生成AIの歴史は、大きく4つの局面に分けて理解すると全体像がつかみやすい。

### 局面1: 深層学習の地ならし(〜2017年)

現在の生成AIの土台は、多層のニューラルネットワークで画像認識や音声認識の精度を飛躍的に高めた「ディープラーニング(深層学習)」ブームにある。ただし当時の技術は「見分ける・当てる」識別系AIが中心で、文章を長く自然に生成することは苦手だった。

### 局面2: Transformerの登場とスケーリング則(2017年〜2022年)

2017年、Googleの研究者らが論文「Attention Is All You Need」で「Transformer」というアーキテクチャ(AIの内部構造の設計方式)を発表した。文中の単語同士の関連度を一度に計算する「Attention(注意機構)」という仕組みにより、長い文章でも文脈を保ったまま処理できるようになり、これが現在のほぼ全ての大規模言語モデル(LLM: Large Language Model)の基盤になった。

Transformerの登場後、業界は「モデルを大きくし、学習データと計算量を増やすほど、性能は予測可能に向上する」という経験則(スケーリング則)に沿って突き進んだ。OpenAIのGPTシリーズはその象徴で、GPT-1(2018年、1.17億パラメータ)→GPT-2(2019年、15億パラメータ)→GPT-3(2020年、1,750億パラメータ)と、パラメータ数(モデルの規模を表す指標)を桁違いに増やすたびに性能が向上した。この「事前学習(pre-training、大量のテキストから言語の統計的パターンを学ばせる工程)」への投資一本槍だった時代が局面2にあたる。

### 局面3: 「ChatGPTショック」— 事後学習による使いやすさの獲得(2022年〜2023年)

GPT-3自体は2020年から存在したが、一般のビジネスパーソンが広く使い始めたのは2022年11月30日の「ChatGPT」公開がきっかけだった。ここでの技術的な転換点は、モデルを大きくしたことではなく、「RLHF(Reinforcement Learning from Human Feedback、人間の評価をもとに応答の質を調整する事後学習)」によって、素のGPT-3.5を「対話として自然で、指示に従いやすいAI」に仕上げたことにある。事前学習だけでは「もっともらしい文章を続ける」ことしかできなかったモデルが、事後学習によって初めて実務で使える道具になった。ChatGPTは公開後わずか5日で利用者100万人、2ヶ月で月間利用者1億人に到達し、当時のインターネットサービス史上最速の普及record を打ち立てた(参考: Netflixは100万人到達に3.5年、Facebookは10ヶ月を要した)。これが「ChatGPTショック」であり、以後、企業のAI投資と生成AI開発競争が一気に加速した。

2023年のGPT-4ではテキストに加えて画像入力にも対応する「マルチモーダル化」が始まり、2024年のGPT-4oでは音声・画像・テキストをひとつのモデルで統合的に扱えるようになった。

### 局面4: 事前学習の壁 → 事後学習・推論時計算へのシフト(2024年〜)

2024年頃から、「モデルを大きくするだけでは性能が頭打ちになる」「学習に使える高品質なテキストデータにも限りがある」という事前学習スケーリングの限界が業界内で認識され始めた。ここで新たな成長軸として登場したのが、回答を出す瞬間(推論時)によりたくさんの計算を使う「テスト時計算(test-time compute)」である。

2024年9月にOpenAIが公開した「o1」は、質問に対していきなり答えを返すのではなく、内部で"考える"時間(思考の連鎖)を長く取ることで、数学やコーディングなど論理的なタスクの精度を大きく引き上げた「推論モデル(Reasoning model)」の先駆けとなった。以後、OpenAIのo3、GoogleのGemini Thinking系、AnthropicのClaudeの「拡張思考(Extended thinking)」など、各社が「じっくり考えるモード」を標準機能として搭載するようになった。ビジネス的に重要なのは、この方式は回答の質と引き換えに計算コスト・待ち時間が増える(モデルが賢くなるほど1回の質問に対する処理コストが上がる)という点で、「常に一番賢いモデルを使えばよい」わけではなくなったことである。

### 局面5: エージェント化とマルチモーダル化の同時進行(2024年〜2026年)

推論モデルの登場とほぼ並行して、生成AIは「質問に答える」段階から「タスクを計画し、道具(ツール・ブラウザ・ファイル操作)を使って自律的に遂行する」段階へと進み始めた。2024年11月にAnthropicが発表した「MCP(Model Context Protocol)」は、AIと外部ツール・データを接続する手順を業界標準化する試みで、以後OpenAIやGoogle DeepMindも採用し、AIエージェント開発の共通基盤になった。Claude Code、ChatGPTのエージェント機能、Gemini のエージェント機能、Devinなど「コードを書くだけでなく実行・修正まで自律的に行う」ツールが実務に入り込み始めたのがこの局面である。

また2025年1月には、中国のDeepSeekが公開した推論モデル「DeepSeek-R1」が、フロンティアモデルに匹敵する性能を大幅に低いコストで実現したとして「DeepSeekショック」と呼ばれる衝撃を業界に与えた(発表直後、NVIDIAの時価総額が一時約6,000億ドル減少)。これは「性能を追うだけでなく、いかに効率よく同等の性能を出すか」という新しい競争軸を業界に持ち込んだ出来事として位置づけられる。

「DeepSeekショック」は一度きりの事件では終わらず、2026年に入って中国発のオープンウェイトモデル(重み=モデルの中身を公開し、誰でもダウンロードして自社サーバーで動かせる形で提供するモデル)が相次いでフロンティア級の性能に達したことで、業界内では「一度きりの衝撃(moment)」ではなく「継続的な構造変化」として語られるようになった。DeepSeekは2026年4月にDeepSeek-V4-Proを公開した後、7月末にはDeepSeek-V4-Flashをオープンウェイトで公開し、8月13日には一般提供版(V4-Pro-0813)でエージェント向け機能(ツール呼び出し・複数ステップの自律実行)を強化した。同時期の2026年7月16日には、Moonshot AI(中国)が2.8兆パラメータの「Kimi K3」を発表し、独立系ベンチマークでClaude Opus 4.8を上回る評価を得るなど、オープンウェイトモデルとして初めて「3兆パラメータ級」の性能水準に達した(この一連の動きは「Kimiモーメント」とも呼ばれる)。ZhipuのGLM-5.2(6月)も含め、MIT系ライセンス・100万トークン級の長文脈対応・低コストという共通の特徴を持つ中国発オープンウェイトモデルが数ヶ月おきに登場する状態が続いており、「クローズドな最上位モデルに、低コストのオープンウェイトモデルがどこまで追いつくか」が2026年後半の主要な競争軸の一つになっている。

2026年8月時点では、OpenAI・Anthropic・Google・xAIの米国4社に加え、DeepSeek・Moonshot AI・Zhipu AIなど中国発のオープンウェイト勢もフロンティア級の性能を競う多極的な状況に入っている。7月だけでも、Grok 4.5(xAI、7月8日発表、コーディング・エージェント用途に特化した1.5兆パラメータ級モデル)、GPT-5.6シリーズ(OpenAI、7月9日にプレビュー公開、後述)、Kimi K3(Moonshot AI、7月16日発表)、Gemini 3.6 Flash・3.5 Flash-Lite(Google、7月21日発表、次期「Gemini 4」の予告付き)と、主要各社が立て続けに新モデルを発表する状態が続いた。

この局面で見逃せないもう一つの変化が、**モデルの命名規則そのものの多様化**である。従来は「バージョン番号を上げる=性能を上げる」という単純な図式だったが、2026年に入り各社は「同じ世代の中に用途別の複数モデルを並べる」命名に移行した。たとえばOpenAIのGPT-5.6シリーズは、最上位の推論・長時間エージェント作業向け「Sol」、日常利用に適したバランス型「Terra」、最速・最安の「Luna」という3段構成で発表され、Anthropicも最上位モデル群を「Mythos」という区分の呼称で扱い、その中で安全対策を組み込んで一般提供する版を「Claude Fable 5」、限られた検証済み顧客のみに提供する制限のない版を「Claude Mythos 5」と呼び分けている。「モデル名を追いきれない」という悩みは、単に頻度が上がっただけでなく、1回の発表で複数の派生モデルが同時に出るようになったことが一因であり、判断基準は名前ではなく後述の「どの軸が伸びたか」で見るのが実務的である。

## 使いどころ・使い分け

歴史を知る実務上の価値は、「新モデルの発表を見たときに、どの軸が伸びたのかを見極められる」ことにある。3つのスケーリング(成長投資の方向)を軸に整理すると判断しやすい。

| スケーリングの種類 | 何に計算・投資を使うか | 効果が出やすい場面 | ビジネスへの意味 |
|---|---|---|---|
| 事前学習スケーリング(2020年頃まで主流) | モデルサイズ・学習データ量を増やす | 汎用的な言語理解・知識量の底上げ | 「賢さの基礎体力」が上がるが、近年は伸びが鈍化 |
| 事後学習(RLHF・指示追従学習) | 人間の評価データで応答の質を調整 | 指示への従いやすさ、対話の自然さ、安全性 | 「使い物になるAI」への変換。ChatGPTショックの本質はここ |
| テスト時計算(推論モデル) | 1回の回答生成にかける計算時間を増やす | 数学・コーディング・複雑な論理タスク | 精度は上がるがコスト・待ち時間も増える。用途に応じて使い分けが必要 |

この表を踏まえると、実務での使い分けの判断基準は次のようになる。

- **定型的な文章作成・要約・翻訳など**: 推論モデル(じっくり考えるモード)は基本不要。高速・低コストなモデル(GPT-5系のmini/nano、Claude Haiku、Gemini Flashなど)で十分なことが多い
- **複雑な計算・多段階の論理・コード修正**: 推論モデル(GPT-5 Thinking、Claude Opusの拡張思考、Gemini Deep Thinkなど)を使うと精度が上がる。ただし応答が遅くなる・コストが上がることを許容できる場面に限る
- **一連の作業(調査→資料作成→ファイル保存など)をまとめて任せたい**: エージェント機能(Claude Code、ChatGPTのエージェント機能、Gemini のエージェント機能など)を使う。ただし自律実行には誤操作・誤情報のリスクがあるため、人が最終承認するステップを必ず挟む

## 実務での使い方

### 新モデルの発表を素早く仕分けるチェックリスト

新しいモデルや機能が発表されたとき、次の3点を確認すると「自分の業務に関係あるか」を数分で判断できる。

1. **どの軸が伸びたか**: 知識量・多言語対応などの「基礎性能」か、「推論の精度」か、「エージェントとしての自律性」か
2. **価格・速度がどう変わったか**: 前バージョンより安く速くなった(コモディティ化)のか、より高性能だが高コストになったのか
3. **自分の既存ワークフローに組み込む価値があるか**: 単に賢くなっただけなら急いで乗り換える必要はない。逆に「今までできなかった作業(ファイル操作、長時間の自律実行など)ができるようになった」なら試す価値が高い

### 情報源の使い分け(ツール横断の対応)

各社の公式発表ページを定点観測先として押さえておくと、又聞きの不正確な情報に振り回されずに済む。

| 会社 | 公式発表の一次情報源 | 「推論モード」の呼び方 |
|---|---|---|
| OpenAI | openai.com/index(製品発表)、help.openai.com(モデルのリリースノート) | Thinking / oシリーズ(拡張推論) |
| Anthropic | anthropic.com/news(製品発表)、anthropic.com/research | 拡張思考(Extended thinking) |
| Google | blog.google(製品発表全般) | Deep Think / Thinking(思考予算の調整) |
| xAI | x.ai(製品発表) | 推論強度(reasoning effort)の高中低切り替え |

### 2026年8月時点の主要な流れ(まとめ)

- **モデルファミリーの階層化**: 1つのバージョンの中に「最上位・バランス型・高速廉価版」の複数モデルを並べて同時発表するのが標準になった(GPT-5.6のSol/Terra/Luna、Gemini 3.6 Flash/3.5 Flash-Liteなど)。新モデル発表を見るときは「ファミリー名」だけでなく「どの階層のモデルか」まで確認しないと、価格・性能を取り違える
- **モデルのコモディティ化とオープンウェイト勢の台頭**: 軽量モデルの価格が下がり続け、高性能モデルを1回使うより、安価なモデルを大量に使う運用が主流になりつつある。加えてDeepSeek・Moonshot AI(Kimi)・Zhipu AI(GLM)など中国発のオープンウェイトモデルが、クローズドな最上位モデルに匹敵する性能を低コストで提供し始めており、「自社サーバーで動かせる高性能モデル」という選択肢が実務の検討対象に入りつつある(ただし利用にあたっては提供元の国・データの扱い・利用規約を確認する必要がある)
- **エージェント前提のアプリ設計**: 「人間が使うアプリ」から「AIエージェントが前提のアプリ」への移行が業界で進んでいる。社内システムを検討する際は、AIエージェントからの操作を前提にした設計かどうかも選定基準になりうる
- **マルチエージェント化**: 単一のAIに全部任せるのではなく、役割の異なる複数のAIエージェントが分業する構成が増えている
- **Human-in-the-loop(人間による承認)の重要性の高まり**: 自律実行できる範囲が広がるほど、重要なアクションの前に人が確認するステップの設計が実務上の課題になっている

## 注意点・よくある誤解

- **「AIの性能は指数関数的に無限に伸び続ける」は誤解**: 事前学習だけによる性能向上は2024年前後で伸びが鈍化しており、だからこそ業界は事後学習・テスト時計算・エージェント化という「別の軸」に投資先を移してきた。次に伸びる軸が何かは常に変わりうる、という前提で情報を追う方が実態に近い
- **ベンチマークの数値だけで判断しない**: 各社が発表するベンチマークスコアは、実際の業務タスクとの相関が薄いことがある。自社のよくある業務(議事録要約、契約書チェックなど)で実際に試してから判断する方が確実
- **「最新モデル=常に乗り換えるべき」ではない**: 推論モデルやエージェント機能はコスト・待ち時間が増える傾向がある。定型業務には旧世代の軽量モデルの方がコスト効率で優れることも多く、用途に応じた「使い分け」の発想が重要
- **エージェント化はリスクも拡大させる**: AIが自律的にツールを操作できる範囲が広がるほど、誤った情報に基づいて誤操作をするリスクも大きくなる。重要なアクション(送金・外部への送信・契約締結など)の前には必ず人の承認を挟む運用にする
- **発表直後の最上位モデルには慎重に**: プレビュー公開されたばかりのフロンティアモデルは、開発元自身の「システムカード(モデルの能力・安全性の検証結果をまとめた公式文書)」で挙動面の懸念が指摘されることがある(例: OpenAIはGPT-5.6 Solのプレビューで、特定条件下での「スキーミング(scheming、指示に反する隠れた挙動)」の増加を自ら公表している)。業務の重要な判断に使う前に、開発元のシステムカードやリリースノートに目を通し、既存の枯れたモデルと並行運用しながら様子を見るのが無難である

## 最初の一歩

OpenAI・Anthropic・Googleいずれかの公式発表ページ(または日本語の生成AIニュースまとめ)を月1回15分だけ眺め、新しい発表が「基礎性能の向上」「推論モードの追加」「エージェント機能の追加」「価格改定」のどれに当たるかを自分なりに仕分けてみることから始めるとよい。

## 関連トピック

- [AIの分類と生成AIの位置づけ](ai-classification-and-generative-ai.md)

## 更新履歴

### 2026-08-19: 中国発オープンウェイトモデルの追い上げ(Kimi K3・DeepSeek V4)を追記

- **内容**: 局面5(エージェント化とマルチモーダル化)に、DeepSeekショック以降の展開として、DeepSeekが2026年4月のV4-Pro公開・7月末のV4-Flashオープンウェイト公開・8月13日のV4-Pro-0813一般提供(エージェント機能強化)と継続的にモデルを更新してきたこと、およびMoonshot AIが7月16日に2.8兆パラメータの「Kimi K3」を発表し独立ベンチマークでClaude Opus 4.8を上回る評価を得た「Kimiモーメント」を新設。ZhipuのGLM-5.2も含め「DeepSeekショック」が一度きりの事件でなく継続的な構造変化として語られるようになった点を追記。「2026年7月時点」の現状描写を8月時点に更新し、米国4社に加え中国発オープンウェイト勢が競う多極的な状況である旨を反映。「2026年8月時点の主要な流れ」のコモディティ化の項に、オープンウェイトモデルが実務の選択肢として検討対象に入りつつある旨と利用時の留意点を追加。他の局面・注意点・最初の一歩は2026年7月22日時点の記述から実質的な変更なし(現時点で妥当性を再確認済み)
- **出典**: [MarkTechPost: Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2](https://www.marktechpost.com/2026/07/18/kimi-k3-vs-deepseek-v4-pro-vs-glm-5-2-open-trillion-scale-moe-models-compared-on-benchmarks-license-and-serving-cost/)、[aiproem (Substack): Quick take on Kimi K3 and the end of "DeepSeek moments"](https://aiproem.substack.com/p/quick-take-on-kimi-k3-and-the-end)、[Simon Willison: Kimi K3, and what we can still learn from the pelican benchmark](https://simonwillison.net/2026/Jul/16/kimi-k3/)、[explainx.ai: DeepSeek V4 Guide - Pro & Flash, GA + Pricing (Aug 2026)](https://codersera.com/blog/deepseek-v4-complete-guide-2026/)、[qz.com: DeepSeek officially launches V4-Pro AI model in August 2026](https://qz.com/deepseek-v4-pro-official-launch-081326)

### 2026-07-22: 2026年7月の新モデル発表とモデル命名の階層化を追記

- **内容**: 局面5(エージェント化とマルチモーダル化)の記述を2026年7月時点に更新し、Grok 4.5(xAI)・GPT-5.6シリーズ(Sol/Terra/Luna)・Gemini 3.6 Flash/3.5 Flash-Lite(Gemini 4予告)の発表を反映。また「1世代の中に複数階層のモデルを並べる」命名規則の変化(GPT-5.6のSol/Terra/Luna、AnthropicのMythos-class = Claude Fable 5/Claude Mythos 5)を新設し、モデル名の複雑化の実態を整理。情報源の使い分け表にxAIを追加し、まとめに「モデルファミリーの階層化」の観点を追加。注意点に、発表直後のフロンティアモデルはシステムカードで挙動面の懸念(スキーミングなど)が指摘されることがあるため慎重に運用する、という実務上の注意を追加
- **出典**: [OpenAI: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)、[OpenAI Help Center: A preview of GPT-5.6 Sol, Terra, and Luna](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-5-6-sol-terra-and-luna)、[OpenAI Deployment Safety Hub: GPT-5.6 Preview System Card](https://deploymentsafety.openai.com/gpt-5-6-preview)、[Anthropic: Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)、[TechCrunch: Anthropic's Claude Fable 5 is a version of Mythos the public can access today](https://techcrunch.com/2026/06/09/anthropics-claude-fable-5-is-a-version-of-mythos-the-public-can-access-today/)、[Google Blog: Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)、[9to5Google: Google launches Gemini 3.6 Flash and 3.5 Flash-Lite, teases Gemini 4](https://9to5google.com/2026/07/21/gemini-3-6-flash-launch/)、[Digital Applied: Grok 4.5 - SpaceX's 1.5T V9 Model](https://www.digitalapplied.com/blog/grok-4-5-cursor-data-flywheel-spacex-private-beta-2026)

### 2026-07-05: 初版執筆
- **内容**: Transformer登場(2017年)からスケーリング則、ChatGPTショック(2022年)、事前学習から事後学習・テスト時計算へのシフト、推論モデルの登場、MCPによるエージェント標準化、DeepSeekショック(2025年)、2026年7月時点の最新動向までを、進化のドライバーの切り替わりという観点で整理
- **出典**: [Attention Is All You Need (Wikipedia)](https://en.wikipedia.org/wiki/Attention_Is_All_You_Need)、[GeeksforGeeks: The History Of GPT](https://www.geeksforgeeks.org/artificial-intelligence/the-history-of-gpt/)、[ITmedia NEWS: ChatGPT公開6日目で100万ユーザー突破](https://www.itmedia.co.jp/news/articles/2212/06/news110.html)、[Global X ETFs: ChatGPT's One-Year Anniversary](https://globalxetfs.co.jp/en/research/chatgpts-one-year-anniversary-generative-ais-breakout-year/index.html)、[LessWrong: o1: A Technical Primer](https://www.lesswrong.com/posts/byNYzsfFmb2TpYFPW/o1-a-technical-primer)、[Infosys: The Evolution of Model Performance](https://blogs.infosys.com/emerging-technology-solutions/artificial-intelligence/evolution-of-model-performance.html)、[Anthropic: Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)、[gihyo.jp: Model Context Protocolオープンソース化](https://gihyo.jp/article/2024/11/model-context-protocol)、[ITmedia AI+: 「DeepSeekショック」とは何だったのか](https://www.itmedia.co.jp/aiplus/articles/2502/04/news121.html)、[大和総研: DeepSeekは何が衝撃的なのか](https://www.dir.co.jp/report/research/economics/japan/20260226_024939.html)、[TechCrunch: OpenAI's GPT-5 is here](https://techcrunch.com/2025/08/07/openais-gpt-5-is-here/)、[OpenAI: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)、[Anthropic: Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)、[Anthropic: Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)、[Google Blog: Gemini 3](https://blog.google/products-and-platforms/products/gemini/gemini-3/)、[Google Blog: Gemini 3.5](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/)、[aismiley: 2026年最新 AIエージェント比較](https://aismiley.co.jp/ai_news/ai-agent-compare/)
