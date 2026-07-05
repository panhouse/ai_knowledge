---
title: AIエージェント(Agentic AI)の基礎
part: 11
chapter: 第1章 AI市場の動向
tags: [AIエージェント, Agentic AI, 生成AI, 業界動向, 自動化]
created: 2026-07-05
updated: 2026-07-05
---

# AIエージェント(Agentic AI)の基礎

## これは何か

「AIエージェント」とは、生成AI(主に大規模言語モデル=LLM)が、人間に一つひとつ指示されなくても、目標達成に向けて自分で計画を立て、Webブラウズ・コード実行・API呼び出し・PC操作などの「行動」を複数ステップにわたって実行し、結果を見ながら次の行動を調整し続けるシステムを指す業界用語である。2025〜2026年にかけて「Agentic AI」とほぼ同義で使われるようになった。

普通のチャットボット(ChatGPTやClaudeとの一問一答のやり取り)が「1回の呼びかけに1回答える」だけなのに対し、AIエージェントは「頼まれた仕事を、途中経過を都度確認されなくても最後までやり切ろうとする」点が本質的な違いである。この違いを理解していないと、「AIエージェント」という言葉が指すものが、単にツールを1回呼び出すだけの機能なのか、何十ステップも自律実行する製品なのか噛み合わず、導入検討や社内説明で混乱が生じる。

## 仕組み・背景

AIエージェントは何か一つの新技術ではなく、既存の要素技術の組み合わせでできている。

- **LLM(推論エンジン)**: 何をすべきか計画し、状況を判断する「頭脳」部分。
- **Tool Use / Function Calling(関数呼び出し)**: LLMが外部のツール・API・検索・コード実行環境を呼び出す仕組み。エージェントの「手足」にあたる。この仕組み自体の詳細は[Function Callingの基本](../part08-api-development/function-calling-basics.md)を参照。
- **ループ構造(計画→実行→観察→再計画)**: 1回で終わらず、実行結果を見て次の一手を考え直すサイクルを、目標達成もしくは規定回数に達するまで繰り返す。
- **実行環境**: コードを動かすサンドボックス、Webブラウザを操作する仮想デスクトップ、PC画面を認識してクリック・入力を行う「Computer Use(コンピュータ操作)」機能など。

重要なのは、「AIエージェント」は白黒二択の概念ではなく、**自律性の程度による連続的なスペクトラム**だという点である。

1. **手動チャット**: 人間が毎回質問し、AIが1回答えるだけ(検索や外部操作はしない)
2. **単発のツール呼び出し**: 「この関数を1回呼んで結果を返す」程度(例: 天気APIを1回叩いて回答に組み込む)
3. **複数ステップの自律エージェント**: 目的を伝えると、複数のツールを組み合わせて数ステップ〜数十ステップを自律的にこなす(例: 「競合3社のサイトを調べて表にまとめて」と頼むとブラウジングと集計を繰り返す)
4. **完全自律の「デジタル従業員」**: 継続的にタスクキューを持ち、長時間・複数タスクを人間の逐次承認なしにこなし続ける(例: MetaがAI企業「Manus」を約20億ドルで買収した際に「デジタル従業員」と評された事例。[TechCrunch, 2025年12月](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/))

現在、業務で実用に耐えるのは主に2〜3の段階であり、4は一部の先進事例にとどまる。

## 使いどころ・使い分け

| 状況 | 適した形態 | 理由 |
|---|---|---|
| 1問1答で完結する質問・文章生成 | 通常のチャット | エージェントの自律実行は不要、速くて確実 |
| 定型的な1アクションの自動化(1件のデータ取得・1本のメール下書きなど) | 単発のツール呼び出し(Function Calling) | オーバーヘッドが少なく、動作が予測しやすい |
| 反復的な多段階のWeb調査・データ収集・資料の下書き作成 | 複数ステップの自律エージェント | 人が都度指示するより速く、ミスがあっても被害が限定的 |
| コーディング(実装・テスト・PR作成までの一連の流れ) | コーディングエージェント | 反復修正・テスト実行との相性が良く、成果物の検証がしやすい |
| 発注・送金・契約締結・顧客への一斉送信など、後戻りできない/影響範囲が広い操作 | 自律実行させない、または必ず人間承認を挟む | 誤りが起きた際の被害が金銭的・信頼的に大きく、取り返しがつかない |
| 長時間・多工程で、進捗の妥当性を人間が逐次判断すべき業務 | チェックポイント付きの半自律運用 | ノーチェックで走らせると、初期の誤りが後工程まで増幅されやすい |
| 専門的な文脈判断・倫理的配慮・社内政治的な配慮が必要な業務 | 人間が主導し、AIは調査・下書きの補助に留める | 現状のエージェントは「もっともらしい行動」はできても、暗黙の前提や組織事情までは読み切れない |

## 実務での使い方

2026年7月時点で、business向けに実際に使えるAIエージェント関連製品を整理すると次のようになる(製品名・提供形態は変化が速いため、導入前に必ず最新情報を確認すること)。

| ベンダー | 主な製品・機能 | 何ができるか | 利用形態・料金の目安 |
|---|---|---|---|
| OpenAI | ChatGPT agent(旧Operatorの機能を統合) | サンドボックス化された仮想PC上でWeb操作・フォーム入力・表計算編集・多段階リサーチを自律実行。重要操作の前には確認を挟む「watch mode」あり | ChatGPT有料プラン(Plus/Pro/Business等)で利用可 |
| OpenAI | Codex(GPT-5-Codex) | リポジトリ全体を読み、複数ファイルにまたがる実装・テスト実行・PR作成までを自律で行うコーディングエージェント。CLI・VS Code拡張・クラウド・Slack連携で利用可能 | ChatGPT全プラン(Free〜Enterprise)に含まれ、トークン量に応じた従量制クレジットを消費 |
| Anthropic | Claude Code | ターミナル・IDE・デスクトップアプリ・ブラウザから、コードベースの読解・編集・テスト実行・コミットまでを自律で行うコーディングエージェント | Claude Pro/Max/Teamなどのプランで利用可 |
| Anthropic | Claude in Chrome(Computer Use機能を活用) | ブラウザの拡張機能としてWebページの閲覧・クリック・フォーム入力・複数タブ操作を自律で実行。定型ブラウザ作業を定期実行するスケジュール機能もあり | ベータ版、Pro/Max/Team/Enterpriseの全有料プランで利用可(Proはモデルが限定) |
| Google | Gemini agent(旧Project Mariner) | GoogleはWebブラウジング自律エージェント「Project Mariner」を2026年5月に終了し、その技術をGeminiアプリの「Gemini agent」機能とChromeの「Auto Browse」、検索の「AIモード」に統合 | Gemini/Google検索の該当機能内で提供 |
| Microsoft | Copilot Studio(Computer-using agent、Agent 365) | ノーコードでWeb・デスクトップアプリを操作する「Computer-using agent」がGA(一般提供)化。Microsoft 365のメール・Teams・ファイル等と連携したエージェントを構築でき、Agent 365でエージェントの権限・稼働状況を一元管理 | Microsoft 365 Copilot/Copilot Studioの契約に含む |
| Dify(ノーコード) | Agentノード / Agentアシスタント | Function CallingまたはReAct戦略を選び、ツール呼び出しの最大反復回数などを設定するだけで、ノーコードで自律型エージェントを構築できる | [Difyとは何か](../part09-nocode-lowcode/dify-basics.md)を参照。SaaS版は無料枠あり、セルフホストも可能 |

**プロンプト例(業務での自律エージェント活用)**

```
目的: 競合3社(A社・B社・C社)の最新の料金プランを調べて、
比較表(プラン名・月額・主要機能・無料枠の有無)にまとめてほしい。

制約:
- 各社の公式サイトの情報を優先し、情報源のURLを併記すること
- 金額や機能に不明点があれば「不明」と明記し、推測で埋めないこと
- 最後に、3社の違いを3行で要約すること
```

このように「目的」「参照すべき情報源の優先順位」「不確実な場合の振る舞い」を明示すると、エージェントの自律実行の精度が上がる。

## 注意点・よくある誤解

- **「AIエージェント」は製品カテゴリ、Function Calling(Tool Use)は仕組み**: 「AIエージェントを使う」というときの実体は、多くの場合LLMがFunction Calling(ツール呼び出し)を繰り返す仕組みの上に構築されている。両者は階層が違う概念であり、混同すると社内での技術説明が噛み合わなくなる。詳細は[Function Callingの基本](../part08-api-development/function-calling-basics.md)を参照。
- **AGI(汎用人工知能)とは別の話**: 「AIエージェントが自律的に動く」ことと、「人間と同等以上の汎用知能を持つAGI」はまったく別の議論である。現在のAIエージェントは、与えられた道具の範囲内でタスクをこなしているに過ぎず、汎用的な自己判断能力を持つわけではない。AGIは実現時期も定義も専門家の間で意見が分かれる、より思弁的なテーマとして切り分けて考える。
- **自律性が高いほど、ミスの被害規模も跳ね上がる**: 人間が確認しながら操作する場合、誤りは1件ずつ止められる。しかし発注や送金の権限を持つエージェントが暴走すると、短時間で数億円規模の誤発注が発生しうるとの指摘がある([ITmedia, 2026年2月](https://www.itmedia.co.jp/enterprise/articles/2602/27/news041.html))。「速く多くこなせる」という利点は、そのまま「速く多く間違えるリスク」と表裏一体である。
- **権限は必要最小限に絞り、証跡(監査ログ)を残す**: 送金・発注・顧客への一斉送信などの高リスク操作は、エージェントに直接権限を持たせず、人間の承認ステップ(human-in-the-loop)を必須にする。誰が・いつ・どの権限でエージェントを動かしたかのログを残す運用も必須になりつつある([PwC Japan](https://www.pwc.com/jp/ja/knowledge/column/awareness-cyber-security/ai-agent-identity.html))。
- **エージェント同士の連鎖リスクにも注意**: 複数のAIエージェントが連携する「A2A(Agent to Agent)」構成では、一つのエージェントの誤りや思い込み(ハルシネーション)が他のエージェントに伝播し、被害が拡大するおそれがある([三菱総合研究所, 2026年4月](https://www.mri.co.jp/knowledge/opinion/2026/202604_3.html))。
- **事故が起きたときの責任の所在がまだ不明確**: AIエージェントによる損害の法的責任は判例の蓄積が乏しく、日本企業が導入をためらう一因になっている([日本経済新聞](https://www.nikkei.com/article/DGXZQOUA0489H0U6A300C2000000/))。契約・社内規程レベルで、AIエージェントの行為に対する責任分担をあらかじめ決めておくことが望ましい。
- **「自律的=高精度」ではない**: ステップ数が増えるほど、途中の1ステップの誤りが後工程に伝播しやすい。重要な成果物は必ず人間が最終レビューする前提で運用する。

## 最初の一歩

まずは低リスクな作業で「エージェントらしさ」を体感するのがよい。たとえばChatGPTの有料プランでAgent機能を使い、「〇〇について競合3社を調べて比較表にして」のような、失敗しても実害の小さい調査タスクを1つ任せてみる。あるいはコーディングに関わる人なら、Claude Codeや同種のコーディングエージェントに、テストコードのある小さな修正タスクを1つ渡し、人間の確認を挟みながら成果物を検証するとよい。

## 関連トピック

- [AIの分類と生成AIの位置づけ](../part01-ai-llm-basics/ai-classification-and-generative-ai.md)
- [Function Callingの基本](../part08-api-development/function-calling-basics.md)
- [Difyとは何か](../part09-nocode-lowcode/dify-basics.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: AIエージェントの定義とチャットボットとの違い、自律性のスペクトラム(手動チャット→単発ツール呼び出し→複数ステップ自律エージェント→完全自律のデジタル従業員)、主要ベンダー(OpenAI/Anthropic/Google/Microsoft/Dify)の2026年7月時点の製品比較、利用が向く場面と高リスクな場面の判断基準、Function Calling・AGIとの概念的な切り分け、権限管理・監査ログ・誤発注リスクなどの注意点を整理
- **出典**: [OpenAI「Introducing ChatGPT agent」](https://openai.com/index/introducing-chatgpt-agent/)、[OpenAI Codex公式](https://openai.com/codex/)、[Codex Pricing](https://developers.openai.com/codex/pricing)、[Anthropic Claude Code製品ページ](https://www.anthropic.com/product/claude-code)、[Claude for Chrome](https://claude.com/claude-for-chrome)、[Android Headlines: Project Mariner終了報道](https://www.androidheadlines.com/2026/05/google-shuts-down-project-mariner-ai-agent.html)、[Microsoft Copilot Blog: Copilot Studio 2026年5月アップデート](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/)、[Dify公式ドキュメント: エージェント](https://docs.dify.ai/ja-jp/guides/application-orchestrate/agent)、[TechCrunch: Meta acquires Manus](https://techcrunch.com/2025/12/29/meta-just-bought-manus-an-ai-startup-everyone-has-been-talking-about/)、[ITmedia: AIエージェントの誤発注リスク](https://www.itmedia.co.jp/enterprise/articles/2602/27/news041.html)、[PwC Japan: AIエージェント時代のアイデンティティ](https://www.pwc.com/jp/ja/knowledge/column/awareness-cyber-security/ai-agent-identity.html)、[三菱総合研究所: A2A経済がもたらす新たなリスク](https://www.mri.co.jp/knowledge/opinion/2026/202604_3.html)、[日本経済新聞: AIエージェントの損害、責任は誰がとる？](https://www.nikkei.com/article/DGXZQOUA0489H0U6A300C2000000/)
