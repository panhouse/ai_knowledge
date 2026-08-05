---
title: トークンとは何か
part: 2
chapter: 第1章 LLMの仕組み
tags: [トークン, LLM基礎, コンテキストウィンドウ, 料金]
created: 2026-07-05
updated: 2026-08-05
---

# トークンとは何か

## これは何か

「トークン」とは、AI(大規模言語モデル、LLM = Large Language Model=大量の文章を学習した生成AIの頭脳部分)が文章を処理する際の最小単位のこと。ChatGPTやClaude、GeminiのAPI料金は「1トークンあたりいくら」で決まり、長文が読み込めるかどうかの上限(コンテキストウィンドウ=AIが一度に読み書きできる文章量の上限)もトークン数で決まる。トークンの仕組みを知らないと、「なぜこの長さの資料が読み込めないのか」「なぜ思ったより料金が高いのか」がブラックボックスのままになる。

## 仕組み・背景

AIは文章をそのまま理解しているわけではなく、まず文章を「トークン」という小さな単位に分割し、それぞれを数値に変換してから処理する。トークンは必ずしも「1文字=1トークン」でも「1単語=1トークン」でもなく、モデルごとに決められた変換ルール(トークナイザー)によって、頻出する文字のかたまりが1トークンとしてまとめられたり、逆に珍しい単語が複数トークンに分割されたりする。代表的な分割方式が**BPE(Byte Pair Encoding)**で、「学習データの中で頻繁に隣り合う文字列を繰り返し1つの単位にまとめていく」統計的な手法のため、よく出る単語ほど1トークンにまとまりやすく、まれな単語ほど細かく分割される。たとえば英語の "tokenization" は "token" + "ization" のように2〜3個のトークンに分かれることが多い。

英語ではOpenAIが公式ヘルプで「1トークン ≈ 4文字 ≈ 0.75単語(100トークン ≈ 英単語75語)」という目安を示している。一方、日本語は漢字・ひらがな・カタカナの組み合わせパターンが非常に多く、頻出パターンとして辞書に登録しきれないため文字単位に近い細かい分割になりやすく、同じ内容を表すのに英語より多くのトークンを消費する傾向がある。またトークナイザーの辞書はモデル提供元ごとに異なるため、同じ文章でもOpenAI・Anthropic・Googleでトークン数は微妙に異なる。

実務で押さえるべきポイントは3つ。

1. **料金はトークン単位で決まる**: API利用料は「入力トークン数」と「出力トークン数」それぞれに単価がかけられて計算される
2. **読み込める文章量(コンテキストウィンドウ)もトークン単位**: 「128Kトークン」「100万トークン」のように表記され、これを超える量の文章は一度に読み込めない
3. **言語によって同じ内容でもトークン数が変わる**: 日本語と英語では文字数とトークン数の関係が異なる(後述)。さらにモデルの世代が変わるとトークナイザー自体が変わり、同じ文章でもトークン数が増減することがある(例: Anthropicは2026年4月にClaude Opus 4.7で新しいトークナイザーを導入し、その後Claude Opus 4.8・Claude Opus 5・Claude Sonnet 5・Claude Fable 5にも同じ方式が採用された。Anthropic公式ドキュメントによれば、この新トークナイザーは同じテキストでもおよそ3割[30%]多くトークンを消費する〔増加率は内容によって変動〕。第三者の計測では、英語の文章は最大4割程度、日本語などのCJK言語は1.5〜3.5割程度増える傾向があると報告されている。ただし同じ現行世代でもClaude Sonnet 4.6・Claude Haiku 4.5は旧トークナイザーのままのため、モデルを切り替えただけでトークン数の見積もりがずれることがある)

## 使いどころ・使い分け

トークンを意識すべき場面とそうでない場面を分けて考えると実務がラクになる。

| 場面 | トークンを意識する必要性 | 理由 |
|---|---|---|
| 短いチャットでの質問・雑談・メール下書き | ほぼ不要 | 数百〜数千トークン程度で、上限に達することはまずない |
| 長文の要約・大量資料の読み込み(議事録・契約書・マニュアル全文など) | 必須 | コンテキストウィンドウを超えると読み込めない、または途中で切り捨てられる |
| 同じチャットで長時間・長期間やり取りを続ける | 必須 | 会話履歴も毎回まるごと読み込まれるため、雪だるま式にトークン消費が増える |
| API・バッチ処理で大量の文書を自動処理する業務 | 必須 | 処理件数×トークン数で料金が積み上がるため、事前の試算が欠かせない |
| 画像・PDF・音声を読み込ませる | 必須 | 画像1枚でも数百〜数千トークン相当として課金対象になる |

判断基準はシンプルで、「読み込ませたい文書の文字数 × 1.2」(日本語の場合の目安、詳細は後述)が、使いたいモデルのコンテキストウィンドウの何%になるかを見る。5割を超えたら要注意、8割に近づくなら文書を分割するか、より大きなコンテキストウィンドウのモデルに切り替える。

## 実務での使い方

### 主要モデルのコンテキストウィンドウと料金(2026年8月5日時点)

API利用時の料金とコンテキストウィンドウは次の通り。金額はいずれも「100万トークンあたり」の米ドル建て。

| 提供元 | モデル(位置づけ) | コンテキストウィンドウ | 入力価格 | 出力価格 |
|---|---|---|---|---|
| Anthropic | Claude Fable 5(最上位・Mythos級) | 100万トークン | $10 | $50 |
| Anthropic | Claude Opus 5(上位モデル、2026年7月24日リリースでOpus 4.8を置き換え) | 100万トークン | $5 | $25 |
| Anthropic | Claude Sonnet 5(標準モデル) | 100万トークン | $2(2026年8月31日まで。以降$3) | $10(同上。以降$15) |
| Anthropic | Claude Haiku 4.5(軽量・高速モデル) | 20万トークン | $1 | $5 |
| OpenAI | GPT-5.6 Sol(最上位) | 約105万トークン(出力上限12.8万トークン) | $5(27.2万トークン超過時は$10) | $30(同、$45) |
| OpenAI | GPT-5.6 Terra(バランス型・コスパ重視の標準用途) | 約105万トークン | $2 | $12 |
| OpenAI | GPT-5.6 Luna(低価格・高速、分類や大量処理向け) | 約105万トークン | $0.20 | $1.20 |
| Google | Gemini 3.1 Pro(現行最上位) | 100万トークン | $2(入力20万トークンまで)/$4(超過分) | $12/$18 |

補足:
- OpenAIはGPT-5.6シリーズ(最上位のSol、バランス型のTerra、低価格のLunaの3グレード)を2026年6月26日に一部パートナー企業向けの限定プレビューとして公開した後、2026年7月9日に一般提供へ切り替えた。さらに2026年7月30日、Terra・Lunaの2グレードのみ値下げを実施(Terra: 入力$2.5→$2/出力$15→$12、Luna: 入力$1→$0.20/出力$6→$1.20)。最上位のSolは据え置き。OpenAIは「GPT-5.6の開発過程で得た効率化(モデル自身に推論基盤コードを最適化させた成果を含む)を提供コストの引き下げに還元した」と説明している
- ChatGPTアプリの既定モデルもGPT-5.6ファミリーへの移行が進んでいる。無料・Plus等のプランでは主にバランス型のTerra相当の帯域が割り当てられ、上位のSolは有料プランの「推論」オプションやAPI経由で使う形になっている。既定モデルの割り当てはプラン変更のたびに変わりやすいため、正確な現状はChatGPTの設定画面で確認するのが安全
- Claude Sonnet 5・Claude Opus 4.7以降(Opus 4.8・Opus 5)・Claude Fable 5は新しいトークナイザーを採用しており、同じ日本語文書でも旧世代のトークナイザーのままのモデル(Claude Sonnet 4.6・Claude Haiku 4.5など)よりトークン数が多く出る傾向がある
- Googleの次世代モデル「Gemini 3.5 Pro」は2026年8月時点でも正式リリース前(2026年5月のGoogle I/Oで予告されたが、コーディング性能などの改善を理由に一般提供が繰り返し延期されている)のため本表には含めていない。同世代の軽量モデル「Gemini 3.5 Flash」(入力$1.50/出力$9)・「Gemini 3.5 Flash-Lite」(入力$0.30/出力$2.50)はすでに提供中で、Gemini 3.1 Proより安価な選択肢になっている。Gemini 3.5 Pro正式リリース後は本表を最新化する
- Anthropicは2026年8月時点で「Fast mode」(応答速度を優先する研究プレビュー機能)をClaude Opus 5・Opus 4.8向けに提供しており、通常の2倍の料金(入力$10/出力$50)で高速な応答が得られる。速度を優先したい業務でのみ検討する

### 日本語と英語のトークン換算の目安

日本語は英語に比べて「1文字あたりのトークン消費」が多くなりがちで、コスト・コンテキストウィンドウの見積もりを誤りやすいポイント。

| 言語 | 目安 |
|---|---|
| 日本語 | 1文字 ≈ 1〜1.3トークン(漢字・かなの混在比率やモデルにより変動) |
| 英語 | 1単語 ≈ 1.3トークン(4文字 ≈ 1トークン) |

古いトークナイザー(GPT-3世代)では「こんにちは」が6トークンに分割されていたが、GPT-4以降は改善され1トークンで処理できるようになるなど、モデルの世代が新しいほど日本語の扱いは効率化している。とはいえ、OpenAIのGPT-4o/GPT-5系が使う「o200k_base」トークナイザーでも、日本語・中国語・韓国語などCJK言語向けの語彙(トークンの辞書)は全体の3.6%程度しか割り当てられていないと報告されており、英語に比べれば依然として日本語の方がトークン消費は多めと見ておくのが安全。

**コピペで使える見積もり式**

```
必要トークン数(概算) = 読み込ませたい日本語の文字数 × 1.2
```

例: 4万字の議事録一式をAIに読み込ませたい場合
→ 40,000字 × 1.2 ≈ 48,000トークン
→ 指示文や過去の会話履歴も加わるので、実務では「文書本体はコンテキストウィンドウの6〜7割以内に収める」のが安全な目安。
→ 上記の見積もりなら大半のモデルで十分収まるが、GPT-5.6 Solのように27.2万トークンを超えると入出力とも料金が跳ね上がる「長文コンテキスト料金」の切り替わりラインを持つモデルもあるため、複数の資料を同時に読み込ませる際は注意する。

### 無料でトークン数を確認できるツール

長文を送る前に、実際のトークン数を事前に数えておくと事故が防げる。

- **OpenAI Tokenizer**([platform.openai.com/tokenizer](https://platform.openai.com/tokenizer)): アカウント登録不要。テキストを貼り付けるだけで、色分けされたトークンの区切りと合計トークン数が即座に表示される。GPT-4/GPT-5系のエンコーディングに対応
- **tiktoken**(Python): OpenAI公式のトークナイザーライブラリ。大量の文書を自動でまとめてカウントしたい場合はこちらをプログラムから呼び出す

```python
import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text_en = "This is a sample business report."
text_ja = "これは業務報告書のサンプルです。"

print(len(enc.encode(text_en)))  # 英語のトークン数
print(len(enc.encode(text_ja)))  # 日本語のトークン数(同程度の内容でも多くなりやすい)
```
- **Google AI Studio**: プロンプト入力欄のすぐ近くに「1,500 / 2,097,152」のような形式でリアルタイムのトークンカウンターが表示される。貼り付け前のプレビュー段階でも増分がわかるため、3社の中では最も親切
- **Anthropic(Claude)**: 公式の単体Web計測ツールはないが、APIに`count_tokens`エンドポイントがあり、送信前(=課金前)に正確なトークン数を取得できる。Anthropic Console(console.anthropic.com)のWorkbenchでプロンプトを入力すると使用トークン数が表示される。手元で概算したいだけなら、GPT系ツールでの計測値に1〜1.3倍程度の幅を見ておけば実務上は十分

### 長文を扱うときのトークン節約

- **貼る前に要約・抜粋する**: 契約書や議事録を丸ごと貼るのではなく、必要な章だけ抜粋する、または一度AIに要点だけ抽出させてから本題の質問に使う、という2段階の使い方でトークン消費を抑えられる。要約させる指示文の例:

```
以下の文章を、意味・数値・固有名詞を変えずに、
全体の40%程度の長さに要約してください。
見出しや目次、免責事項などの本文以外の要素は除外してください。
```

- **チャンク分割**: コンテキストウィンドウに収まらない長大な文書は、意味のまとまり(章・条項単位)で分割してから個別に要約させ、最後に要約同士を統合させると精度が落ちにくい。RAG(Retrieval-Augmented Generation、必要な部分だけを検索して都度読み込ませる仕組み)を使う場合も、検索対象のドキュメントを適切なチャンクサイズに分けておくことが前提になる

### ツール横断の対応付け

同じ「トークン数を確認する」という要求が、各ツールでどう見えるか。

| ツール | UI上での見え方 | 確認・対策方法 |
|---|---|---|
| ChatGPT(Plus/Pro/Business) | 明示的なトークン数表示はない。会話が長くなると古いやり取りが要約・省略され、上限が近いと警告が出ることがある | 送信前にOpenAI Tokenizerで下書きを計測しておく |
| Claude.ai(Pro/Max) | 常時表示のメーターはない。上限に接近すると画面に警告メッセージが表示される仕組み | タスクが変わったら新しいチャットを始める。長文はAPIのcount_tokensで事前確認 |
| Gemini(Google AI Studio / Gemini アプリ) | AI Studioは入力欄近くにリアルタイムのトークンカウンターを表示。Gemini アプリ(一般ユーザー向け)には表示なし | AI Studioで事前に文書を貼り付けて確認するのが最も手軽 |
| 各社API共通 | レスポンスの`usage`フィールドに実測の`input_tokens`/`output_tokens`が返る | ログを見れば1回の呼び出しごとの正確な消費量とコストが検証できる |

## 注意点・よくある誤解

- **「文字数=トークン数」ではない**: 日本語と英語で換算率が異なるだけでなく、同じ日本語でもモデルやトークナイザーの世代によってトークン数が変わる。見積もりは必ず実測かツールで確認する
- **異なるモデル間でトークン数は流用できない**: OpenAIのトークナイザーで数えた結果を、そのままClaudeやGeminiの料金計算に使うと誤差が出る。モデルごとにトークナイザーが異なるため、正確に知りたい場合はそのモデル・APIの公式カウント方法を使う
- **コンテキストウィンドウが大きい=何でも詰め込んでよい、ではない**: 上限ぎりぎりまで詰め込むと、料金が跳ね上がるだけでなく、関係のない情報が多いほど回答の精度が落ちる「コンテキスト腐敗(context rot)」と呼ばれる現象が知られている。必要な情報だけに絞り込む方が結果もコストも良くなることが多い
- **ChatGPTなどの「利用回数制限」とコンテキストウィンドウは別物**: プランの「〇時間ごとに何回まで」という制限は主に利用回数の話で、コンテキストウィンドウはモデル自体が一度に扱える文章量の仕様。両方を混同すると「なぜ回数は余っているのに長文が拒否されるのか」が理解できなくなる
- **画像・PDF・音声もトークンとして課金される**: テキストだけでなく、添付した画像や音声もトークンに変換されて計算に含まれる。画像1枚でも数百〜数千トークン相当になることがあるため、大量の画像を含む資料は事前に見積もりが必要
- **見えない「思考トークン」も課金対象になる**: Claudeの拡張思考(extended thinking)、GPT-5.6の推論(reasoning)モード、Geminiの思考モードなどは、回答の前にモデル内部で行う「思考過程」もトークンとして生成しており、画面に表示されなくても出力トークンとして課金される場合がある。想定より料金が高い場合はこの点を確認する
- **プロンプトキャッシュでコストを削減できる**: 同じ資料やシステムプロンプトを繰り返し使う場合、Anthropic・OpenAI・Googleとも「プロンプトキャッシュ」機能があり、2回目以降の読み込みが大幅に安くなる(Anthropicの場合、キャッシュ命中時は通常の入力価格の1割程度まで下がる)。同じ長文を何度も読み込ませる業務では必ず検討する
- **長い会話は分けた方が得**: 同じチャットで会話を続けるほど、毎回の応答で過去のやり取り全体を読み込み直すため、トークン消費が雪だるま式に増える。タスクが変わったタイミングで新しいチャットを始めるのが、コストと精度の両面で有利

## 最初の一歩

次に長めの資料をAIに読み込ませる前に、[OpenAI Tokenizer](https://platform.openai.com/tokenizer)かGoogle AI Studioの入力欄にその文書を貼り付けて、実際のトークン数を一度確認してみる。

## 関連トピック

- [LLMの仕組み:確率的単語予測と学習プロセス](llm-mechanism-basics.md)
- [AIの分類と生成AIの位置づけ](../part01-ai-basics/ai-classification-and-generative-ai.md)
- [ChatGPTのプラン比較](../part03-ai-chat-tools/chatgpt-plan-comparison.md)
- [OpenAI APIの基本](../part09-api-development/openai-api-basics.md)

## 更新履歴

### 2026-08-05: モデルラインナップと料金の節を最新化
- **内容**: Anthropic「Claude Opus 5」(2026年7月24日リリース、Opus 4.8と同料金)を反映。OpenAI「GPT-5.6 Terra/Luna」の値下げ(2026年7月30日、Terra $2.5→$2/$15→$12、Luna $1→$0.20/$6→$1.20)と長文コンテキスト料金の閾値(27.2万トークン)を追記し、料金表からGPT-5.5 Instantの単独行を整理。Anthropic公式ドキュメントの新トークナイザー増加率(約3割)を追記。Gemini 3.5 Proが2026年8月時点でも未リリースである点、および軽量モデルGemini 3.5 Flash/Flash-Liteの料金を補足。CJK言語向け語彙比率(o200k_baseで3.6%)の出典を追加
- **出典**: [Pricing - Claude Docs](https://platform.claude.com/docs/en/about-claude/pricing)、[Anthropic releases Claude Opus 5 - Axios](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5)、[Anthropic releases Claude Opus 5 - Fortune](https://fortune.com/2026/07/24/anthropic-debuts-claude-opus-5-with-feature-that-lets-users-toggle-between-cost-and-capability/)、[OpenAI Just Cut GPT-5.6 Luna's Price by 80 Percent - Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/openai-just-cut-gpt-5-013753910.html)、[OpenAI cuts prices for two of its GPT-5.6 AI models - CNBC](https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html)、[GPT-5.6 Sol API Pricing & Cost - Requesty](https://www.requesty.ai/models/openai/gpt-5.6-sol)、[Gemini 3.5 Pro: is it out yet? - eesel AI](https://www.eesel.ai/blog/gemini-3-5-pro)、[Gemini pricing in 2026 - CloudZero](https://www.cloudzero.com/blog/gemini-pricing/)、[Reverse-Engineering the OpenAI's GPT-5 Tokenizer - metehan.ai](https://metehan.ai/blog/reverse-engineering-the-gpt-5-tokenizer-aeo-geo/)

### 2026-07-21: モデルラインナップと料金・トークナイザーの節を最新化
- **内容**: 主要モデルのコンテキストウィンドウ・料金表を更新(Claude Fable 5・Claude Haiku 4.5を追加、GPT-5.6シリーズ[Sol/Terra/Luna]の一般提供開始とGPT-5.5 Instantが引き続きChatGPT既定モデルである点を反映)。Anthropicの新トークナイザーがOpus 4.7以降・Sonnet 5・Fable 5に採用される一方、Sonnet 4.6・Haiku 4.5は旧トークナイザーのままである点を明記し、増加率を英語最大4割・CJK言語1.5〜3.5割程度に精緻化
- **出典**: [Claude Sonnet 5's New Tokenizer: 41% More Tokens per Prompt - Synthorai](https://synthorai.io/blog/claude-sonnet-5-tokenizer/)、[Claude Token Counter, now with model comparisons - Simon Willison](https://simonwillison.net/2026/apr/20/claude-token-counts/)、[Claude Fable 5 and Claude Mythos 5 - Anthropic](https://www.anthropic.com/news/claude-fable-5-mythos-5)、[GPT-5.6: Frontier intelligence that scales with your ambition - OpenAI](https://openai.com/index/gpt-5-6/)、[GPT-5.6 in ChatGPT - OpenAI Help Center](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna)、[CJK Token Myth Busted — Measured Data - Mason AI Lab](https://masonailab.com/en/insights/token-efficiency/)、[Gemini 3.5 Pro delays due to coding performance - 9to5Google](https://9to5google.com/2026/07/16/gemini-3-5-pro-delays/)

### 2026-07-06: 重複ページの統合
- **内容**: 重複していた token-basics.md / tokens-and-tokenization.md / tokens-in-llm.md、および llm-tokenization-and-prediction.md のトークン固有の記述を本ページに統合。BPEの仕組みと英語の公式目安(1トークン≈4文字≈0.75単語)、tiktokenのコード例、モデル間でトークン数を流用できない点、長文のチャンク分割・要約指示文の実例、思考トークンの課金、コンテキスト腐敗(context rot)の用語を追加
- **出典**: [OpenAI Help Center: What are tokens and how to count them?](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them)、[Claude Platform Docs: Token counting](https://platform.claude.com/docs/en/build-with-claude/token-counting)、[Claude Platform Docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)、[みうのAIテックブログ: 日本語は1文字3トークン？](https://miu-ai-techblog.com/tokenizer_and_bpe/)

### 2026-07-05: 初版執筆
- **内容**: トークンの基本概念、コンテキストウィンドウとの関係、日本語と英語のトークン換算目安、Anthropic・OpenAI・Googleの最新モデルのコンテキストウィンドウと料金比較、無料のトークン計測ツールの使い方をまとめた
- **出典**: [Claude Platform Docs - Pricing](https://platform.claude.com/docs/en/about-claude/pricing)
- **出典**: [OpenAI API Pricing (developers.openai.com)](https://developers.openai.com/api/docs/pricing)
- **出典**: [GPT-5.5 Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.5)
- **出典**: [Introducing GPT-5.5 | OpenAI](https://openai.com/index/introducing-gpt-5-5/)
- **出典**: [Previewing GPT-5.6 Sol: a next-generation model | OpenAI](https://openai.com/index/previewing-gpt-5-6-sol/)
- **出典**: [Gemini 3.1 Pro Preview API Pricing 2026 - pricepertoken](https://pricepertoken.com/pricing-page/model/google-gemini-3.1-pro-preview)
- **出典**: [Gemini 3.1 Pro API Pricing (Updated July 2026) - TokenCost](https://tokencost.app/models/gemini-3-1-pro)
- **出典**: [Gemini 3.1 Pro Pricing in 2026 - Verdent Guides](https://www.verdent.ai/guides/gemini-3-1-pro-pricing)
- **出典**: [tiktokenで文字数・トークンの比率を出してみる - Zenn](https://zenn.dev/kun432/scraps/5de099a56197d9)
- **出典**: [トークンとは何ですか？また、どのように数えますか？ - OpenAI Help Center](https://help.openai.com/ja-jp/articles/4936856-what-are-tokens-and-how-to-count-them)
- **出典**: [OpenAI 言語モデルで日本語を扱う際のトークン数推定指標 - Zenn](https://zenn.dev/microsoft/articles/dcf32f3516f013)
- **出典**: [Google AI StudioのToken countとは？ - AI-Rise](https://ai-rise.net/column/google-ai-studio-token-count/)
- **出典**: [How do usage and length limits work? - Claude Help Center](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work)
- **出典**: [ChatGPT Pricing Guide: Free, Go, Plus, Pro (July 2026) - felloai](https://felloai.com/chatgpt-pricing-guide-free-go-plus-pro-alternatives-october-2025/)
