---
title: "コンテキストウィンドウの基本(なぜ大切か・モデル別の違い)"
part: 2
chapter: 第1章 LLMの仕組み
tags: [コンテキストウィンドウ, トークン, LLM, 長文処理, Lost in the Middle]
created: 2026-07-06
updated: 2026-08-09
---

# コンテキストウィンドウの基本(なぜ大切か・モデル別の違い)

## これは何か

コンテキストウィンドウ(context window)とは、AI(LLM = 大規模言語モデル)が1回の応答を作るときに「同時に読み込める文章量の上限」のこと。指示文(プロンプト)だけでなく、それまでの会話履歴、添付した資料、そして生成中の回答そのものまで、すべてがこの1つの枠の中に積み上がっていく。単位は[トークン](what-are-tokens.md)(AIが文章を処理する最小単位)で、「32万トークン」「100万トークン」のように表記される。

この枠を意識せずに長い会話を続けたり、大量の資料をそのまま貼り付けたりすると、「さっき伝えた指示をAIが無視する」「途中から話が噛み合わなくなる」「長文の途中に書いた重要な条件を読み落とす」といった不具合が起きる。コンテキストウィンドウは、AIに何をどこまで一度に任せられるかを決める、業務利用の土台になる仕組みである。

## 仕組み・背景

### 何が枠の中に入るのか

コンテキストウィンドウには、次のものがすべて含まれ、合計トークン数で1つの上限を共有する(Anthropicの公式ドキュメントが挙げる例)。

- システムプロンプト(AIへの役割・ルール設定)
- それまでの会話履歴(ユーザーの発言・AIの応答すべて)
- 添付した文書・画像・ツールの実行結果
- ツールの定義そのもの(Function Callingを使う場合)
- **これから生成する回答自体**(内部で考える「思考(thinking)」トークンも含む)

つまり「入力用の枠」と「出力用の枠」が別々にあるのではなく、1つの枠を入力と出力で分け合っている。長い資料を貼るほど、AIが長い回答を返すほど、この枠は早く埋まっていく。

### 枠が埋まるとどうなるか

API(開発者がプログラムから直接AIを呼び出す方式)では、入力だけで上限を超えると「プロンプトが長すぎる」というエラーになり、生成の途中で上限に達すると回答が強制的に途中で打ち切られる。一方、ChatGPT・Claude.ai・Geminiアプリのような一般ユーザー向けのチャット画面では、上限に近づくと**古い発言から順に自動で会話履歴が捨てられる(先入れ先出し)**か、要約されて圧縮される仕組みを取っていることが多い。これが「さっき伝えた指示を、会話が長くなるとAIが忘れる」ように見える主な原因で、実際には忘れているのではなく、そもそも枠の外に押し出されて見えなくなっている。

[RAG(検索拡張生成)の基本](../part07-data-analysis/rag-basics.md)で扱っているチャンク化(資料を小さな断片に分割する処理)も、根本的にはこのコンテキストウィンドウの制約に対処するための工夫である。1万ページの社内マニュアルを毎回丸ごと読み込ませることはできないため、質問に関連する部分だけを検索して、その断片だけをコンテキストウィンドウに詰め込む、という設計になっている。

### 枠の中に収まっていても精度が落ちる(Lost in the Middle / コンテキスト腐敗)

見落とされがちなのが、「上限に収まっているから大丈夫」とは限らない点。長い文章・長い会話の**真ん中あたりに埋もれた情報は、AIが見落としやすい**ことが複数の研究で確認されており、"Lost in the Middle"(真ん中で迷子になる)と呼ばれる。文章の最初と最後に近い情報ほど正しく参照され、中盤の情報ほど参照ミスが増えるU字型の傾向で、2023年に複数モデルで確認された後、2026年時点でも構造的な弱点として残っている(Transformer[LLMの内部構造の方式]という仕組み自体に起因するとされ、モデルの世代が新しくなっても完全には解消されていない)。Anthropicは公式ドキュメントでこれを**「コンテキスト腐敗(context rot)」**と呼び、「コンテキストウィンドウが大きいほど良い、ではない。トークン数が増えるほど精度・記憶の正確さは低下する」と明言している。むしろコンテキストウィンドウが100万トークン級に大きくなるほど、「技術的には収まるが実際には読み落とされる」範囲が広がるという指摘もある。

データベース企業Chromaが2025年7月に公開した検証(GPT-4.1・Claude 4・Gemini 2.5・Qwen3など18モデルを対象)は、この現象をさらに具体的に裏付けた。「20万トークンの窓でも、5万トークン程度の入力からすでに精度低下が始まる」「100万トークンの窓があっても、実際に100万トークン全体にわたって一貫して推論できるわけではない」「答えと紛らわしい情報が周囲に多いほど劣化が速い」、そして意外なことに「整然と構造化された入力の方が、あえてシャッフルした入力より精度が落ちやすい」という結果まで報告されている。この検証チームが導く2026年時点の実務上の結論は、「関連しそうな箇所を5万〜20万トークン程度にまで検索で絞り込んでから、その範囲内で長文推論させる」というハイブリッド構成であり、これは次項「使いどころ・使い分け」で述べるRAGと長文一括投入の使い分けの根拠にもなっている。

料金への影響は[トークンとは何か](what-are-tokens.md)で詳しく扱っているが、要点だけ言えば「コンテキストウィンドウを大きく使うほどトークン消費が増え、料金も上がる」。さらに長い会話を続けるほど、次の発言のたびに過去の会話履歴をまるごと読み込み直すため、雪だるま式にコストが積み上がっていく。

## 使いどころ・使い分け

コンテキストウィンドウの大きさだけで「良い・悪い」を判断せず、やりたいことに応じて手段を選ぶ。

| したいこと | 向いている手段 | 理由 |
|---|---|---|
| 数ページの資料を読んで質問したい | そのままチャットに貼る・添付する | 資料が小さければコンテキストウィンドウの制約もLost in the Middleの影響も出にくい |
| 数十〜数千ページの資料から、必要な箇所だけ正確に探して答えさせたい | [RAG](../part07-data-analysis/rag-basics.md)(ファイルアップロード機能・ナレッジベース・[NotebookLM](../part08-specialized-ai-tools/notebooklm-basics.md)など) | 関連部分だけを検索して渡すため、巨大な資料を丸ごと1つのコンテキストウィンドウに詰め込まずに済み、Lost in the Middleの影響も抑えられる |
| 資料全体の「大まかな流れ・論調」をつかみたい(細部の一言一句より要約重視) | 大きいコンテキストウィンドウのモデルにそのまま丸ごと読み込ませる | 要約や全体像の把握はLost in the Middleの影響を受けにくく、検索の手間もかからない |
| 同じチャットで長時間・長期間、対話や作業を続けたい | 定期的に新しいチャットを始める、または要約して引き継ぐ | 会話履歴が肥大化するほどコストと精度劣化(コンテキスト腐敗)のリスクが上がる |
| 巨大な資料の中の「特定の1つの数字・条件」を一字一句正確に確認したい | 該当箇所をピンポイントで抜粋・検索してから質問する | 大きいコンテキストウィンドウに丸ごと入れるより、狙った箇所を直接渡す方が読み落としのリスクが低い |

判断基準はシンプルに、「その資料の全体像をつかみたいのか」「その資料の中の特定の一点を正確に取り出したいのか」で分ける。後者ほど、コンテキストウィンドウの大きさに頼らず検索・抜粋で的を絞る方が安全。

## 実務での使い方

### 主要モデルのコンテキストウィンドウ比較(2026年8月時点)

いずれもAPI利用時の入力コンテキストウィンドウの上限(以下は目安。実際の利用可能量はプラン・利用経路によって変わる点は次項参照)。

| 提供元 | モデル | コンテキストウィンドウ(入力) | 出力上限 |
|---|---|---|---|
| OpenAI | GPT-5.6 Sol / Terra / Luna(2026年7月9日に一般提供開始) | 約105万トークン(入力92.2万+出力12.8万の合計) | 12.8万トークン |
| Anthropic | Claude Fable 5(最上位モデル) | 100万トークン | 12.8万トークン |
| Anthropic | Claude Opus 5(2026年7月24日リリース。Opus 4.8の後継で価格は据え置き) | 100万トークン | 12.8万トークン |
| Anthropic | Claude Sonnet 5 | 100万トークン | 12.8万トークン |
| Anthropic | Claude Haiku 4.5(軽量・高速モデル) | 20万トークン | - |
| Google | Gemini 3.1 Pro(現行Pro)/ Gemini 3 Flash / 3.1 Flash-Lite | 100万トークン | 6.4万トークン |
| xAI | Grok 4.20(現行モデルで最大の窓) | 200万トークン | - |
| xAI | Grok 4.3 | 100万トークン | - |
| xAI | Grok 4.5(2026年7月8日、コーディング・エージェント特化の最新フラッグシップ) | 50万トークン(あえて縮小) | - |
| Meta | Llama 4 Scout(オープンウェイト) | 理論値1,000万トークン | - |

補足:
- Anthropicは2026年7月24日にClaude Opus 5を投入し、Opus 4.8の実質的な後継とした(価格は$5/$25per百万トークンで4.8から据え置き)。Claude Maxでは既定モデル、Claude Proでは最上位モデルという位置づけで、Opus 4.8自体は本稿時点でまだ提供終了になっていない
- Google Gemini 3.5 Pro(次世代Pro、2Mトークン級と噂される)は、2026年5月のGoogle I/Oで発表されたものの2026年8月9日時点でまだ一般提供されていない。Googleは7月21日時点で「パートナー企業とテスト中」と説明しており、当初目標の6月からリリースが大きくずれ込んでいる。正式仕様は未確定のため、契約前に必ず公式発表を確認すること
- xAIのGrok 4.1 Fast(200万トークン級の旧世代)は2026年8月15日に提供終了予定。現行ラインナップはGrok 4.20(200万)・Grok 4.3(100万)・Grok 4.5(50万、コーディング・エージェント用途で速度とコストを優先し窓をあえて縮小)の3系統に分かれ、「新しい・上位のモデルほど窓が大きい」とは限らない点に注意
- Meta Llama 4 Scoutの1,000万トークンは公表上の理論値であり、独立した検証では実際に情報を正確に取り出せる範囲(実効的な精度)はそれより大幅に狭いと報告されている。「上限が大きい=常に信頼できる」と早合点しないこと。なお「Meta が2026年4月に600Bパラメータ・500万トークン窓の『Llama 5』を発表した」とするブログ記事が一部で出回っているが、Meta公式ブログ・Hugging Faceのmeta-llama公式アカウントのいずれにも該当する発表・モデルカードが見当たらず、本稿執筆時点(2026年8月9日)では真偽を確認できていない。裏取りできない数値としてこのページには採用しない
- xAIのGrok系・MetaのLlama系はAPIや自社ホスティングでの利用が主で、一般的な業務利用ではOpenAI・Anthropic・Googleの3社が中心になる

### 「モデルの上限」と「実際に使える上限」は別物

上の表はAPIで使う場合の最大値であり、**ChatGPT・Claude.ai・Geminiアプリなど一般ユーザー向けの画面では、契約プランによってこれより小さい上限に制限されていることが多い**。たとえば、

- OpenAIのChatGPTは2026年8月6日、無料版・Go版の既定モデルをGPT-5.5 InstantからGPT-5.6 Lunaに切り替えた(コンテキストウィンドウ12.8万トークン、テキストチャットは無制限)。Plus/Proユーザー向けにはGPT-5.6 Solが提供され、回答にかける思考の深さをスライダーで選べるようになっている。ChatGPT Businessプランのヘルプページでは、Luna/Terraで12.8万トークン、Sol(旗艦モデル)で27.2万トークンという上限が明記されている
- Anthropicの有料Claude.aiプランでは、Claude Sonnet 5は全プランで100万トークンが使える。新しいClaude Opus 5(Opus 4.8の後継)はClaude Proでは既定20万トークンに制限されており、アカウント設定で「使用クレジット」をオン(実際に課金しなくてもオンにするだけでよい)にすると100万トークンまで拡張できる。最上位のClaude Fable 5はMax/Team/Enterpriseプランで利用可能で、既定で100万トークン
- Googleの一般ユーザー向けGeminiアプリでは、無料版が約3.2万トークン、Google AI Plus(月額)が12.8万トークン、Google AI Pro/Ultra(上位プラン)がGemini 3.1 Proで100万トークンという段階になっている

同じモデル名でも「どの画面・どの契約プランから使っているか」でコンテキストウィンドウが変わるため、長文が読み込めない場合はまずこの点を確認する。

### コンテキストウィンドウの限界に達しているかどうかの見分け方

次のような症状が出たら、コンテキストウィンドウの限界に近づいているサインと考える。

- チャットの序盤で伝えたルール・キャラクター設定・禁止事項を、AIが途中から守らなくなる
- 「さっき言ったのに」と感じる指示の繰り返しが増える
- 長文資料を読み込ませた後、本来含まれているはずの記述について「そのような記述はありません」と誤って答える
- 画面に「これ以上のメッセージは要約されます」「コンテキストが上限に近づいています」といった警告が表示される
- 長い資料や画像を添付した直後に、明確な「入力が長すぎます」というエラーが返る

### すぐに使える対処法

- **タスクが変わったら新しいチャットを始める**: 同じチャットを延々と続けず、話題が変わった時点で新規スレッドに切り替える。コストと精度の両面で有利
- **資料を丸ごと貼らず、RAG的な機能を使う**: 大量の資料を扱う場合は、[NotebookLM](../part08-specialized-ai-tools/notebooklm-basics.md)やChatGPTのプロジェクト機能など、資料を検索して必要な部分だけを参照する仕組みを使う。詳しい判断基準は[RAG(検索拡張生成)の基本](../part07-data-analysis/rag-basics.md)を参照
- **重要な指示は冒頭と末尾の両方に書く**: 長い会話・長いプロンプトでは、文章の最初と最後に近い情報ほど正しく参照されやすい。特に守ってほしいルールは、指示文の冒頭だけでなく末尾でも再掲する
- **本当に読み込んでいるか、要点を聞いて確認する**: 長文を読み込ませた直後に「読み込んだ資料の第◯章の要点を3行で教えて」のように具体的な箇所を尋ね、狙った内容が正しく参照されているかを一度確認する
- **不要な定型文はあらかじめ削る**: 目次・免責事項・ヘッダー/フッターの繰り返しなど、本文と関係のない部分はコンテキストウィンドウを無駄に消費するノイズになる。貼る前に削っておく

コピペで使える確認プロンプトの例(長文を読み込ませた直後に使う):

```
今読み込んだ資料の内容だけを根拠に、以下に答えてください。
一般知識で補完せず、資料に書かれていないことは「記載なし」と答えてください。

1. 資料全体を200字で要約してください
2. 資料の中盤(全体の30〜70%の位置)に書かれている内容を1つ具体的に引用してください
3. 上記の引用が資料のどの章・見出しに該当するか教えてください
```

2番目の質問で的確な引用が返ってこない場合、Lost in the Middleの影響が出ている可能性が高い。その資料は丸ごと読み込ませるより、RAG的な検索の仕組みを使う方が安全と判断できる。

## 注意点・よくある誤解

- **「コンテキストウィンドウが大きいモデル=常に高精度」ではない**: 前述の「コンテキスト腐敗」のとおり、詰め込む情報量が増えるほど関連性の低い情報が混ざり、回答の精度が落ちることがある。大きい枠は「収められる量が増える」だけで、「収めた分だけ正確に使いこなせる」ことは保証しない
- **枠に収まっている=正しく参照される、ではない**: Lost in the Middleにより、特に長文の中盤に埋もれた情報は読み落とされやすい。重要な条件・数値ほど、文章の冒頭付近に置くか、該当箇所を別途抜粋して渡す方が安全
- **「アプリで使える上限」と「モデルの最大上限」を混同しない**: 同じモデルでも、APIと一般ユーザー向けアプリ、さらに契約プランによって実際に使える上限は異なる。長文が拒否された場合、モデルの限界ではなく契約プラン側の制限であることも多い
- **長い会話は「忘れられている」のではなく「押し出されている」ことが多い**: 一般ユーザー向けチャット画面の多くは、上限に近づくと古い発言を自動で削除・要約する。これは不具合ではなく仕組み上の挙動であり、重要な情報は会話の途中で一度メモとして書き出しておくと安全
- **画像・音声・添付ファイルもコンテキストウィンドウを消費する**: テキストだけでなく、画像1枚・音声ファイルもトークンに変換されて枠を消費する。大量の画像を含む資料は、テキストだけの場合より早く上限に近づく
- **「整った資料だから安心」とは限らない**: Chromaの検証(2025年7月)では、見出し・箇条書きが整然と構造化された入力の方が、あえてシャッフルした入力より精度が落ちやすいという結果が出ている。読みやすく整形すること自体は、Lost in the Middle対策として万能ではない

## 最初の一歩

いま長く続けているチャットを1つ選び、そのチャットの序盤で伝えた指示やルールをAIが正しく守れているか、あらためて質問して確認してみる。守れていなければ、その指示を新しいチャットの冒頭で再掲するところから始める。

## 関連トピック

- [トークンとは何か](what-are-tokens.md)
- [LLMの仕組み:確率的単語予測と学習プロセス](llm-mechanism-basics.md)
- [LLMの得意・不得意と挙動の特性](llm-strengths-and-limitations.md)
- [RAG(検索拡張生成)の基本](../part07-data-analysis/rag-basics.md)
- [NotebookLMの基本](../part08-specialized-ai-tools/notebooklm-basics.md)

## 更新履歴

### 2026-08-09: 主要モデルのコンテキストウィンドウ比較とLost in the Middle研究を最新化
- **内容**: モデル別比較表を2026年8月時点に更新。AnthropicはClaude Opus 5(2026年7月24日リリース、Opus 4.8後継、価格据え置きの$5/$25)を追加し、Claude ProプランでのOpus系列の実際の上限(既定20万トークン→使用クレジット有効化で100万トークンに拡張)を反映。OpenAIはChatGPT無料/Go版の既定モデルが2026年8月6日にGPT-5.6 Lunaへ切り替わったこと、Plus/Pro向けにGPT-5.6 Solの思考深度スライダーが導入されたことを追記。xAIはGrok 4.1 Fastの提供終了予定(2026年8月15日)とGrok 4.20(200万)/Grok 4.3(100万)/Grok 4.5(50万、コーディング・エージェント特化であえて窓を縮小)の現行3系統を整理。Googleは次世代Gemini 3.5 Proが2026年8月9日時点でも一般提供されておらず「パートナー企業とテスト中」の段階であることを更新。一部サイトで流通する「Meta Llama 5(600Bパラメータ・500万トークン窓、2026年4月発表)」の情報は、Meta公式・Hugging Face公式アカウントで裏付けが取れなかったため採用せず、その旨を明記。あわせて、Chroma Research社の検証(2025年7月、GPT-4.1・Claude 4・Gemini 2.5・Qwen3など18モデル対象)を引用し、Lost in the Middle/コンテキスト腐敗の節に「意味的に紛らわしい情報が多いほど劣化が速い」「整然と構造化された入力の方がシャッフルより精度が落ちやすい」「実務は関連箇所を5万〜20万トークンに絞ってから長文推論するハイブリッド構成が基本」という知見を追加
- **出典**: [OpenAI: GPT-5.6](https://openai.com/index/gpt-5-6/)、[OpenAI Help Center: ChatGPT Business - Models & Limits](https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits)、[digitalapplied: ChatGPT Goes GPT-5.6 — Free Tier Gets Unlimited Luna](https://www.digitalapplied.com/blog/chatgpt-gpt-5-6-luna-free-default-unlimited-chats)、[Anthropic: Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)、[Claude Platform Docs: What's new in Claude Opus 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-opus-5)、[Wade Tregaskis: Claude Opus 5 is limited to a 0.2M token context window by default](https://wadetregaskis.com/claude-opus-5-is-limited-to-a-0-2m-token-context-window-by-default/)、[techjacksolutions: Grok 4.5](https://techjacksolutions.com/ai-tools/grok/what-is-grok-4-5/)、[datanorth.ai: xAI releases Grok 4.5](https://datanorth.ai/news/xai-releases-grok-4-5-coding-focused-model)、[docs.x.ai: Grok 4.3](https://docs.x.ai/developers/models/grok-4.3)、[TechTimes: Gemini 3.5 Pro targets July 17 after full rebuild, every spec remains unconfirmed](https://www.techtimes.com/articles/320308/20260713/gemini-35-pro-targets-july-17-after-full-rebuild-every-spec-remains-unconfirmed.htm)、[Hugging Face: meta-llama organization](https://huggingface.co/meta-llama)、[Chroma: Context Rot: How Increasing Input Tokens Impacts LLM Performance](https://www.trychroma.com/research/context-rot)、[GitHub: chroma-core/context-rot](https://github.com/chroma-core/context-rot)

### 2026-07-22: 主要モデルのコンテキストウィンドウ比較を最新化
- **内容**: 主要モデルのコンテキストウィンドウ比較表を更新。OpenAIはGPT-5.6(Sol/Terra/Luna、2026年7月9日GA、API上は約105万トークン)を追加しつつ、ChatGPT画面の既定モデルは引き続きGPT-5.5 Instantであることを明記。AnthropicはClaude Fable 5(最上位、100万トークン)とHaiku 4.5(20万トークン)を追加し、Claude.aiプランごとの実際の上限(Sonnet 5は全プランで100万、Opus 4.8は既定50万でクレジット有効化により100万に拡張、Fable 5はMax/Team/Enterpriseで既定100万)を更新。Googleは2026年7月21日にGAしたGemini 3.6 Flash(100万トークン)を追加し、未リリースのGemini 3.5 Pro(200万トークン級と噂されるが7月22日時点で正式発表なし)を補足として言及。xAIはGrok 4 Fastが非推奨化(2026年5月15日)・提供終了予定(2026年8月15日)であることを反映し、現行のGrok 4.20(200万トークン)とGrok 4.3(100万トークン)の2系統に更新
- **出典**: [Claude Platform Docs: What's new in Claude Sonnet 5](https://platform.claude.com/docs/en/about-claude/models/whats-new-sonnet-5)、[Claude Help Center: How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)、[Anthropic: Introducing Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8)、[Anthropic: Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)、[Anthropic: System Card: Claude Haiku 4.5](https://www.anthropic.com/claude-haiku-4-5-system-card)、[OpenAI Help Center: ChatGPT Business - Models & Limits](https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits)、[OpenAI Help Center: GPT-5.6 in ChatGPT](https://help.openai.com/articles/11909943)、[CNBC: OpenAI to publicly release GPT-5.6](https://www.cnbc.com/2026/07/08/openai-expanding-gpt-5point6-ai-model-release-ending-government-limits.html)、[9to5Google: Google launches Gemini 3.6 Flash and 3.5 Flash-Lite, teases Gemini 4](https://9to5google.com/2026/07/21/gemini-3-6-flash-launch/)、[TechTimes: Gemini 3.5 Pro targets July 17 after full rebuild, every spec remains unconfirmed](https://www.techtimes.com/articles/320308/20260713/gemini-35-pro-targets-july-17-after-full-rebuild-every-spec-remains-unconfirmed.htm)、[Oracle Cloud Docs: xAI Grok 4 Fast (Deprecated)](https://docs.oracle.com/en-us/iaas/Content/generative-ai/xai-grok-4-fast.htm)、[llm-stats: Grok 4.3 benchmarks, pricing & context window](https://llm-stats.com/models/grok-4.3)、[Apiyi: Grok 4.20 Beta解説(2Mトークンコンテキスト)](https://help.apiyi.com/en/grok-4-20-beta-xai-flagship-hallucination-multimodal-agent-guide-en.html)

### 2026-07-06: 初版執筆
- **内容**: コンテキストウィンドウの定義(システムプロンプト・会話履歴・添付資料・出力すべてが1つの枠を共有する)、チャット画面での「先入れ先出し」による履歴の押し出し挙動、RAG・チャンク化との関係、Lost in the Middle/コンテキスト腐敗(context rot)という精度劣化現象、OpenAI・Anthropic・Google・xAI・Metaの主要モデルのコンテキストウィンドウ比較表、モデル上限とアプリ・プラン上限の違い、限界を見分けるサインと具体的な対処法・確認用プロンプト例を整理
- **出典**: [Claude Platform Docs: Context windows](https://platform.claude.com/docs/en/build-with-claude/context-windows)、[Anthropic: Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)、[Lost in the Middle: An Emergent Property from Information Retrieval Demands in LLMs (arXiv)](https://arxiv.org/pdf/2510.10276)、[GPT-5.5 Model | OpenAI API](https://developers.openai.com/api/docs/models/gpt-5.5)、[GPT-5.5's Million-Token Context Window: Practical Strategies for Codex CLI (codex.danielvaughan.com)](https://codex.danielvaughan.com/2026/04/25/gpt-5-5-million-token-context-window-codex-cli-long-context-workflows/)、[OpenAI Help Center: ChatGPT Business - Models & Limits](https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits)、[Claude Help Center: How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)、[MarkTechPost: Google AI Releases Gemini 3.1 Pro with 1 Million Token Context](https://www.marktechpost.com/2026/02/19/google-ai-releases-gemini-3-1-pro-with-1-million-token-context-and-77-1-percent-arc-agi-2-reasoning-for-ai-agents/)、[Google AI for Developers: Long context](https://ai.google.dev/gemini-api/docs/long-context)、[Writingmate: Grok 4 Fast's 2M Context Window](https://writingmate.ai/blog/grok-4-fast-2m-context-window-pricing-vs-chatgpt-2026)、[digitalapplied: AI Context Window Comparison 2026: 1M to 10M Tokens](https://www.digitalapplied.com/blog/ai-context-window-comparison-2026-1m-to-10m-tokens)
- **注記**: 一部の一次情報ページ(support.claude.com、support.google.com、deepmind.google等)は本セッションから直接アクセスできず、検索エンジンのスニペットおよび複数の第三者記事の突き合わせに基づく記述を含む。ChatGPT・Claude.ai・Geminiアプリの契約プラン別コンテキストウィンドウは変更が頻繁なため目安とし、契約・運用前には必ず各社公式ヘルプページで最新値を確認すること
