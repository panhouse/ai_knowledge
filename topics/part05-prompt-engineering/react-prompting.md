---
title: "ReAct(Reasoning and Acting)プロンプティング"
part: 5
chapter: 第4章 エージェント的手法
tags: [プロンプトエンジニアリング, ReAct, 応用手法, AIエージェント, Tool Use]
created: 2026-07-06
updated: 2026-07-06
---

# ReAct(Reasoning and Acting)プロンプティング

## これは何か

「競合3社の最新料金を調べて比較表を作って」のような、AIに検索やツール呼び出しを挟んだ複数ステップの調査を頼むと、[Chain-of-Thought(CoT)](chain-of-thought-prompting.md)だけで考えさせた場合、1回検索した結果を鵜呑みにしたまま話を進めてしまい、その検索結果が的外れ・古い・不十分であっても気づかずに誤った前提で回答を組み立ててしまうことがある。ReAct(Reasoning and Acting、「推論と行動」)プロンプティングとは、AIに「考える(Thought)→外部の行動を起こす(Action。検索やツール呼び出し)→その結果を確認する(Observation)」の3ステップを1サイクルとして繰り返させ、行動の結果を都度確認しながら次の一手を考え直させる手法である。人間が調べものをするときに「検索する→出てきた結果を見る→次に何を調べるべきか考える」を繰り返すのと同じ発想だと考えるとわかりやすい。

## 仕組み・背景

ReActは2022年10月にGoogle ResearchとPrinceton大学の研究チーム(Yao, Shunyuらが第一著者)が発表した論文"ReAct: Synergizing Reasoning and Acting in Language Models"(arXiv:2210.03629、2023年のICLRに採択)で提案された手法だ。それまでのCoTは、モデルが頭の中だけで推論を進める手法であるため、途中の事実認識に誤り(ハルシネーション)があっても外部で検証する手段がなく、そのまま誤った結論に突き進んでしまう弱点があった。一方、推論を伴わずツールを呼ぶだけの手法は、なぜその行動を取ったのかをモデルが言語化しないため、人間が後から検証しにくく、エラーの原因も追いにくいという弱点があった。ReActはこの2つを交互に繰り返させることで、それぞれの弱点を補い合わせる。

具体的には、モデルの出力を次のような「Thought → Action → Observation」の繰り返しとして構成する。

```
Thought: (次に何を確認すべきか、その理由)
Action: 検索[調べる対象]  ※実際にはツール呼び出しとして実行される
Observation: (検索・ツール実行の結果)
Thought: (結果を踏まえて次に何をすべきか)
Action: 検索[別の対象]
Observation: (結果)
...
Thought: 十分な情報が得られた
Action: Finish[最終的な回答]
```

論文では、複数ステップのWikipedia検索を要する質問応答(HotpotQA)や事実検証(Fever)のベンチマークで、`Search[エンティティ名]`(該当項目の要約を取得)・`Lookup[キーワード]`(長い記事から該当箇所を探す)・`Finish[回答]`(十分な情報が集まったら終了)という3種類の行動を人間が書いた1〜2個のお手本(few-shot)例だけをプロンプトに含める形で検証している。結果として、ReActはCoT単体で起きがちなハルシネーションや、一度の誤りが後の推論全体に伝播してしまう「エラーの伝播」を、外部のWikipedia APIとやり取りしながら訂正することで抑え、人間にとって読みやすい(解釈可能な)思考の軌跡を生成できたと報告されている。さらに、仮想環境内で複数手順の意思決定を行うALFWorld・WebShopというベンチマークでは、模倣学習や強化学習によるベースライン手法に対して、ReActは1〜2個のお手本だけで、成功率をそれぞれ絶対値で34ポイント・10ポイント上回ったとされている。

## 使いどころ・使い分け

CoT・ToT・ReActはいずれも「モデルにいきなり結論を出させない」という共通の発想を持つが、何を繰り返させるかが異なる。

| 手法 | 繰り返す対象 | 外部の行動を伴うか | 向いている問題 |
|---|---|---|---|
| [CoT](chain-of-thought-prompting.md) | 頭の中の推論ステップ(1本道) | 伴わない | モデルが既に知っている情報で解ける計算・論理・条件判定 |
| [ToT](tree-of-thought-prompting.md) | 複数の推論の枝(分岐・比較・バックトラック) | 伴わない | 唯一の正解がなく、複数のアプローチを比較検討したい問題 |
| ReAct | 推論と外部行動のサイクル(Thought→Action→Observation) | 伴う(検索・ツール呼び出し・操作) | モデルが知らない最新情報の取得や、実際の検索・操作が必要な複数ステップの調査・実行タスク |

ReActが効くのは「モデルの知識だけでは答えられず、外部の情報取得や操作を挟む必要があり、かつその結果を確認しながら次の手を変える必要がある」タスクに限られる。次のような判断軸で使い分けるとよい。

- **モデルの知識だけで完結する単純な質問・計算**: ReActは不要。CoTで十分、あるいはCoTすら不要
- **複数の妥当な進め方があり、比較検討そのものが成果物になる**: ReActよりToTが向く
- **最新情報の検索や社内システムの照会を挟みながら、複数ステップで調査・作業を進めたい**: ReActが向く(競合価格調査、複数資料をまたぐ根拠確認、トラブルシューティングの原因調査など)
- **すでにWeb検索・ツール機能を有効にしたAI(ChatGPTのAgent、Claude Code、Gemini CLIなど)を使っている**: 多くの場合、モデル側が内部で既にReAct的なループを自動で回しているため、ユーザーがThought/Action/Observation形式を明示的に書く必要性は下がる(次章で詳述)

## 実務での使い方

### コピペで使える実例: 明示的にThought→Action→Observationを書かせるテンプレート

ChatGPT・Claude・GeminiいずれでもWeb検索やツール機能をオンにした状態で、次のテンプレートをそのまま貼ると、AIが検索結果を1つ確認するごとに「次に何を調べるべきか」を言語化しながら進めるようになる。調査過程を人間が検証しやすくなるほか、AIが1回の検索結果だけで結論を急ぐことを防げる。

```
以下のテーマについて調査し、最終的な回答をまとめてください。
回答を出す前に、次のサイクルを、十分な情報が揃うまで繰り返してください。
(Web検索・ブラウジング機能が使える場合は、必ず実際に検索してから
Observationを書いてください。想像や既存知識だけでObservationを
作らないでください。)

Thought: (次に何を確認すべきか、その理由)
Action: (検索するキーワード、または確認する対象)
Observation: (実際に検索・確認して得られた情報を要約したもの)

十分な情報が得られたら、最後に次の形式で終えてください。

Thought: 十分な情報が得られた
Answer: (最終的な回答。根拠にした情報の出典も簡潔に添える)

※サイクルは最大5回までとし、5回を超えても情報が不十分な場合は、
その時点でわかっている範囲を明示したうえで回答してください。

【調査したいテーマ】
[ここに調べたいことを書く]
例)当社が扱う業務用コピー機と競合するA社・B社・C社の最新モデルについて、
   本体価格・月額保守費用・主要スペックを調べ、比較表にまとめたい
```

### コピペで使える実例: ツール一覧を渡して行動を選ばせるパターン(社内利用を想定)

社内システムの照会やファイル検索など、決まったツールの中からAIに選んで使わせたい場合は、使える行動をあらかじめ列挙しておくと、行動の逸脱(存在しない操作を「実行したふり」をすること)を防ぎやすい。

```
あなたは社内問い合わせ対応のアシスタントです。次の行動だけを使って調査し、
Thought→Action→Observationのサイクルで進めてください。

【使える行動】
- 社内Wiki検索[キーワード]
- FAQ検索[キーワード]
- 過去問い合わせ履歴検索[キーワード]
- Finish[最終回答]

上記以外の行動は使わないでください。情報が見つからない場合は、
Observationに「該当情報なし」と記録し、次のThoughtで別の検索語を試すか、
それでも見つからなければFinishで「情報が見つからなかった」ことを含めて回答してください。

【問い合わせ内容】
[ここに問い合わせ文を貼る]
```

### 「もう内部で動いている」こととの関係: エージェント機能・Tool Useとの対応付け

2026年7月時点では、ChatGPT・Claude・Geminiのエージェント系機能は、ユーザーがThought/Action/Observationと明示的に書かなくても、内部でこれと同種のループを自動で回している。手動でこの形式を書く価値があるのは、「推論過程を人間の目で検証したい」「エージェント機能を持たない軽量モデルやシンプルなチャット画面でも段階的に調べさせたい」場合に限られる。

| ツール・機能 | 明示的にThought/Action/Observation形式で書かせる方法 | 内部で自動的にReAct的ループが動く機能 |
|---|---|---|
| ChatGPT | 上のテンプレートを、Web検索や「エージェントで実行」をオンにした状態で貼る | ChatGPT Agent、Deep Research |
| Claude(Claude.ai / API) | 同テンプレートを、拡張思考+Web検索/ツール使用をオンにした状態で貼る | Claude Codeなどのエージェント。Claude 4系では、ツール呼び出しの間に推論を挟む「インターリーブ思考(interleaved thinking)」機能があり、Opus 4.6/Sonnet 4.6のadaptive thinkingでは自動的に有効になる(他モデルはベータヘッダーで有効化) |
| Gemini(gemini.google.com / Gemini CLI) | 同テンプレートを、Google検索グラウンディングをオンにした状態で貼る | Gemini CLIは、組み込みツールとMCPサーバー連携を使ったThink→Act→Observeのループを内部で回し、複数ステップの作業を実行する |
| 開発者向け(API・LangChain等) | プロンプトでThought/Action/Observation形式を明示し、Action行をアプリ側のコードでパースして実行結果をObservationとして返す(LangChainの`create_react_agent`が代表例) | 各社のネイティブな[Function Calling(Tool Calling)](../part09-api-development/function-calling-basics.md) APIを使った「エージェントループ」。現在はテキストをパースするReAct形式より、モデルが構造化データ(JSON)で呼び出し要求を返すFunction Calling形式(LangChainの`create_tool_calling_agent`など)の方が信頼性が高く、実務では推奨されることが多い |

つまり、ReActは「モデルに推論とツール利用を交互にやらせる」という**発想・パターン**の名前であり、[Function Calling(Tool Calling)](../part09-api-development/function-calling-basics.md)は「その行動(Action)を実際にどう実行するか」という**技術的な実装手段**、[AIエージェント](../part12-ai-trends/ai-agent-basics.md)は「そのループを自律的に何ステップも繰り返すシステム全体」を指す言葉、という三層の関係で理解すると整理しやすい。

## 注意点・よくある誤解

- **ツールがなければ「調べたふり」になる**: Web検索やツール機能がオフの状態でThought/Action/Observation形式を書かせても、Observationはモデルの想像に過ぎない。ハルシネーションのリスクは減らず、むしろ「調べたような体裁」で回答の信頼度が実際より高く見えてしまう危険がある。テンプレートを使う前に、必ず検索・ツール機能が実際に有効になっているか確認する
- **ループが収束しないことがある**: 何度Action→Observationを繰り返しても十分な情報に辿り着けず、同じような検索を繰り返し続けることがある。プロンプトに「最大◯サイクルまで」という上限を明示し、それを超えたらその時点でわかっている範囲で回答させる、という抜け道を用意しておく
- **サイクル数に比例してコスト・待ち時間が増える**: 1サイクルごとにモデルへの推論呼び出しが発生するため、サイクルが増えるほどAPI利用料・応答時間が線形に増える。重要な調査・込み入ったタスクに絞って使い、簡単な質問には使わない
- **モデルが行動やObservationを捏造することがある**: 存在しないツール名を呼び出したように書いたり、実際には確認していない結果をObservationとして書いてしまうことがある。特に行動を自由なテキストで書かせている場合に起きやすいため、可能であれば[Function Calling](../part09-api-development/function-calling-basics.md)のような構造化された呼び出し形式と組み合わせ、実行できる行動をあらかじめ限定しておくと安全性が上がる
- **CoT・ToTとの混同**: CoTは頭の中だけの推論、ToTは複数案の比較検討であり、いずれも外部の行動を伴わない。外部情報も何もいらない単純な質問にReAct形式を強制しても、手間が増えるだけで効果はない

## 最初の一歩

次に複数ステップの調査(競合比較、複数の資料・システムをまたいだ根拠確認など)をAIに頼むときは、ChatGPTやClaudeでWeb検索・ツール機能を必ずオンにしたうえで上のコピペ用テンプレートを試し、AIが実際に検索→結果確認→次の検索を繰り返す様子を1回観察してみるとよい。

## 関連トピック

- [Chain-of-Thought(CoT)プロンプティング](./chain-of-thought-prompting.md) — 外部の行動を伴わない、頭の中だけの推論はこちら
- [Tree of Thought(ToT)プロンプティング](./tree-of-thought-prompting.md) — 複数案を比較検討したい場合はこちら
- [AIエージェントとは何か](../part12-ai-trends/ai-agent-basics.md) — ReAct的なループを自律的に繰り返すシステム全体の呼び方
- [Function Calling(Tool Calling)の基本](../part09-api-development/function-calling-basics.md) — ReActの「Action」を実際に実行する技術的な仕組み

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: ReActプロンプティングの定義(困りごとの起点)、Thought→Action→Observationループの仕組みと原論文(Yao et al., 2022)の評価結果(HotpotQA/Fever/ALFWorld/WebShop)、CoT・ToTとの違いを整理した比較表、Web検索・ツール機能をオンにして使う前提のコピペ用テンプレート2種、ChatGPT/Claude/Gemini/LangChainでの対応付け(Claude 4系のinterleaved thinking、Gemini CLIのThink→Act→Observeループを含む)、ツール未接続時の「調べたふり」リスクやループ非収束・コスト増などの注意点を執筆
- **出典**: [ReAct: Synergizing Reasoning and Acting in Language Models (arXiv:2210.03629)](https://arxiv.org/abs/2210.03629)
- **出典**: [ReAct Prompting - Prompt Engineering Guide](https://www.promptingguide.ai/techniques/react)
- **出典**: [ReAct: Synergizing Reasoning and Acting in Language Models - 公式プロジェクトページ](https://react-lm.github.io/)
- **出典**: [Building with extended thinking(interleaved thinking) - Claude Docs](https://docs.claude.com/en/docs/build-with-claude/extended-thinking)
- **出典**: [Understanding LangChain Agents: create_react_agent vs create_tool_calling_agent - Medium](https://medium.com/@anil.goyal0057/understanding-langchain-agents-create-react-agent-vs-create-tool-calling-agent-e977a9dfe31e)
- **出典**: [What Is the ReAct Loop? How AI Agents Reason, Act, and Iterate Toward a Goal - MindStudio](https://www.mindstudio.ai/blog/what-is-react-loop-ai-agents-reason-act-iterate)
- **出典**: [Agentic Loops: From ReAct to Loop Engineering (2026 Guide) - Data Science Dojo](https://datasciencedojo.com/blog/agentic-loops-explained-from-react-to-loop-engineering-2026-guide/)
