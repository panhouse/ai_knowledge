---
title: "推論モデル(Reasoning Model)とは何か"
part: 2
chapter: 第2章 モデルの種類と選び方
tags: [推論モデル, Reasoning Model, Chain-of-Thought, モデル選び, Thinking]
created: 2026-07-06
updated: 2026-07-06
---

# 推論モデル(Reasoning Model)とは何か

## これは何か

数学の応用問題、複数条件が絡む企画書の検討、バグの原因究明のような「多段階で考える必要がある」質問をAIに投げると、瞬時に答えを返すモデルはしばしば早合点し、途中の論理を飛ばして間違った結論を出す。**推論モデル(Reasoning Model、「Thinkingモデル」「思考モデル」とも呼ばれる)**とは、最終的な答えを出す前にモデル内部で段階的な「考える過程」を長く生成してから答えを組み立てるように訓練・調整されたモデルのことだ。これに対して、考える過程をほとんど挟まずに即答するモデルを「即答モデル」「高速モデル」(ChatGPTの「Instant」、Geminiの「Fast」など)と呼ぶ。同じAIサービスの中に「即答モデル」と「推論モデル」の両方が用意され、タスクに応じて使い分けるのが2026年7月時点の標準的な構成であり、この2階建て構造を知らないと、複雑な作業に不向きな即答モデルをデフォルトのまま使い続けて精度を損ねたり、逆に単純な作業に重い推論モデルを使って待ち時間とコストを無駄にしたりする。

## 仕組み・背景

推論モデルの「考える過程」は、[Chain-of-Thought(CoT)プロンプティング](../part05-prompt-engineering/chain-of-thought-prompting.md)でユーザーが「ステップバイステップで考えて」と指示していた挙動を、モデル自身が内部処理として自動的に行うように学習させたものだ。ユーザーが手順を書かなくても、モデルが質問を受け取った時点で「論点を洗い出す→検証する→矛盾がないか見直す」といった思考の連鎖を大量のトークンとして生成し、そのうえで最終回答を組み立てる。この思考過程は、画面に「Thinking」として要約表示される場合もあれば、コストだけ発生して中身は見えない場合もある。

この方向性を最初に製品化したのはOpenAIで、2024年9月に発表した「o1」が、内部で長い思考過程を生成してから答える専用モデルとして登場し、数学・コーディングのベンチマークで従来モデルを大きく上回った。これ以降、「即答モデル」と「推論モデル」を並べて提供する形が業界標準になり、2026年7月時点の主要ベンダーの構成は次のようになっている(名称・仕様は数か月おきに変わるため、あくまで執筆時点の目安)。

| ベンダー | 即答(Fast)系 | 推論(Thinking)系 | 特徴 |
|---|---|---|---|
| OpenAI(ChatGPT) | GPT-5.5 Instant | GPT-5.5 Thinking(Medium/High/Extra High) | モデルピッカーで切り替え。詳細は[ChatGPTのモデル一覧と使い分け](../part03-ai-chat-tools/chatgpt-model-lineup.md) |
| Anthropic(Claude) | 素の応答(思考オフ) | Claude Sonnet 5・Opus 4.8の「拡張思考(extended thinking)」。effort(思考の力加減)をlow/medium/high/xhigh/maxから選ぶ「適応的思考(adaptive thinking)」に移行中 | オン・オフの二択から、思考の深さを段階調整する方式に変わってきている |
| Google(Gemini) | Gemini 3 Flash(Fast) | Gemini 3 Thinking、Gemini 3.1 Proの「思考レベル(標準/拡張)」、最上位の「Deep Think」 | モデル選択画面で「Fast/Thinking/Pro」を切り替え |
| DeepSeek | DeepSeek-V4(V3系の後継、通常チャット) | DeepSeek-R1(「DeepThink」ボタンで起動する専用推論モデル) | オープンウェイト(モデルの重みを公開)で無料利用・自社ホスティングも可能な点が特徴。R1の後継「R2」は2026年6月時点で未リリース |

なお推論モデルは「必ず正解に近づく魔法」ではなく、「答えを出す前に検討する時間(計算量)を増やす」仕組みにすぎない。単純な質問に使っても、途中の思考が長くなるだけで結論はほぼ変わらないことが多い。

## 使いどころ・使い分け

判断の軸は「唯一の正解に向けて多段階の論理・計算・検証が必要か」「間違えたときの実害はどれくらいか」の2つ。この2軸で実害が大きく、多段階の検討が必要なタスクほど推論モデル側に倒す。

| タスクの性質 | 向いているモデル | 理由 |
|---|---|---|
| 雑談・アイデア出し・メール下書き・要約 | 即答モデル | 待ち時間がほぼなく、コストも安い。多段階の検討が不要 |
| 数学の応用問題・数値計算を含む分析 | 推論モデル | 途中の計算過程を明示的に検証しながら進むため誤りが減る |
| プログラムの設計判断・複雑なバグの原因究明 | 推論モデル(高い思考レベル) | 一発で正解を出しにくく、仮説→検証の反復が効く |
| 複数条件が絡む企画書・契約書の論点整理 | 推論モデル | 見落としがちな条件の矛盾・抜け漏れを拾いやすい |
| 定型文書の作成・トーン調整・言い換え | 即答モデル | 「正解の一意性」が低く、推論の深さが結果に効きにくい |
| リアルタイム性が必要な対話(接客チャット等) | 即答モデル | 推論モデルは数秒〜数分待たされるため、対話のテンポを壊す |

判断に迷ったら、まず即答モデルで試し、回答に見落とし・計算ミス・論理の飛躍を感じたら推論モデルに切り替える、という順番が実務的には無駄が少ない。多くのツールには「複雑な質問を自動で推論モデルに引き上げる」機能(例: ChatGPTの「Auto-switch to Thinking」)もあるため、まずはそれを有効にしておくのも手。

## 実務での使い方

### 主要ツールでの切り替え場所

| ツール | 切り替え場所 | 補足 |
|---|---|---|
| ChatGPT | 画面左上のモデル名をクリック→「Instant」「Thinking」「Pro」から選択。「Configure」から思考の深さ(Medium/High/Extra High)を調整 | 詳細な手順・プラン別の利用可否は[ChatGPTのモデル一覧と使い分け](../part03-ai-chat-tools/chatgpt-model-lineup.md)を参照 |
| Claude(claude.ai) | チャット画面のモデルセレクターでOpus・Sonnet等の対応モデルを選択→入力欄左下の「Search and tools」から拡張思考をオン、またはeffort(low/medium/high/xhigh/max)を選択 | 会話の途中でオン・オフを切り替えると新しいチャットに切り替わることがあるため、使う予定なら会話の最初から有効にする |
| Gemini | 画面上部のモデル選択(Fast/Thinking/Pro)をタップ→Fast・Proを選んだ場合はさらに「思考レベル(標準/拡張)」を選べる。Proの上位に「Deep Think」あり | 「思考モード」自体を選んだ場合は思考レベルの選択肢は出ず、常にThinkingとして動作 |
| DeepSeek(チャット画面) | 入力欄左下の「DeepThink」ボタンをオン(青色点灯)にするとR1が応答 | オフの状態は通常チャット用のV4が応答。思考過程はトグルで開いて確認できる |

### コピペで使える例(推論モデルに切り替えたうえで、さらに検討を促す一言)

推論モデルを選んでいても、検討してほしい観点を具体的に書くと精度がさらに上がりやすい。

```
この件は複数の前提条件と制約があるため、結論を急がず次の手順で検討してください。
1. 前提条件・制約条件をすべて洗い出す
2. 条件同士に矛盾がないか確認する
3. 複数の解決案を出し、それぞれのメリット・デメリットを比較する
4. 最後に推奨案とその根拠、リスクが残る点を明示する
```

### コスト面の意思決定材料

推論モデルの「考える過程」は、画面に表示されない場合でも裏側でトークンを生成しており、そのトークン分の料金がかかるのが一般的な仕組み。たとえばOpenAIのo3系モデルでは、見える回答が500トークンでも裏側で数千トークンの思考が生成され、実質的な課金対象トークン数が数倍に膨らむことがある。AnthropicのClaudeも同様に、思考トークンは出力トークンと同じ単価で課金される。「表示されている回答は短いのに、なぜか利用料が高い」と感じたら、この思考トークンの分量が原因であることが多い。判断の目安は「間違えたときの損失が、推論モデルに切り替えた際の追加コストの5倍以上あるか」で、この目安を上回るタスクほど推論モデルへの切り替えが割に合う。

## 注意点・よくある誤解

- **「推論モデルだからハルシネーション(もっともらしい誤情報の生成)が起きない」は誤解**: 2026年の複数の検証では、推論モデルは即答モデルよりハルシネーションの発生率が高くなる傾向すら報告されている(例: OpenAIのPersonQAベンチマークでo3が約33%、前世代のo1が約16%というデータ)。長く考えるほど、参照した情報から少しずつ内容がずれていき、それらしい誤った詳細を作文してしまう「考えすぎ」の弊害があるとされる。むしろ「考えたから正しいはず」という思い込みの方が危険で、重要な事実確認は推論モデルの回答でも省略しない。
- **「自信を持って長く説明している=正しい」ではない**: ある調査では、AIモデルは間違っている回答のときの方が正しい回答のときより自信度が高くなる傾向が報告されている。回答の長さ・断定的な口調は精度の保証にならない。
- **モデル名・思考レベルの区分は数か月おきに変わる**: 本ページで挙げた名称(GPT-5.5 Thinking、Claude Opus 4.8、Gemini 3 Thinking、DeepSeek R1等)は執筆時点の目安であり、実際の画面表示・最新モデル名は都度確認する。
- **推論モデルは「待ち時間・コストとのトレードオフ」であることを忘れない**: 数十秒〜数分の待ち時間、数倍のコストを払っても、単純な質問では精度がほぼ変わらないことが多い。まず即答モデルで試し、物足りなければ推論モデルに上げる順番が無駄を減らす。
- **推論過程の表示(Thinking欄)は「要約」であり、モデルの思考をすべて正確に記述しているとは限らない**点も留保しておく。表示された思考過程を鵜呑みにせず、最終的な結論・根拠は別途確認する。

## 最初の一歩

普段使っているAIツールのモデル選択画面を開き、即答系(Instant/Fast)と推論系(Thinking)がどう表示されているか確認する。次に、最近「精度が足りない」と感じた質問を1つ選び、推論モデルに切り替えて同じ質問をもう一度投げ、回答の違いを見比べてみる。

## 関連トピック

- [LLMの得意・不得意と挙動の特性](llm-strengths-and-limitations.md)
- [Chain-of-Thought(CoT)プロンプティング](../part05-prompt-engineering/chain-of-thought-prompting.md)
- [ChatGPTのモデル一覧と使い分け](../part03-ai-chat-tools/chatgpt-model-lineup.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: 推論モデル(Reasoning Model)を「答えを出す前に内部で段階的な思考過程を生成するモデル」として即答モデルと対比して定義し、OpenAI o1(2024年9月)を起点とする経緯、2026年7月時点のOpenAI/Anthropic/Google/DeepSeekの即答・推論モデル対応表、タスク別の使い分け表、主要ツールでの切り替え場所、思考トークンの課金の仕組み、推論モデルでもハルシネーションが減らない(むしろ増える場合がある)という注意点をまとめた
- **出典**: [Claude Platform Docs: Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)、[Claude Help Center: Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)、[Anthropic: Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)、[MarkTechPost: Claude Sonnet 5 vs Sonnet 4.6 vs Opus 4.8](https://www.marktechpost.com/2026/06/30/anthropic-claude-sonnet-5-vs-sonnet-4-6-vs-opus-4-8-agentic-coding-benchmarks-api-pricing-and-cost-performance-tradeoffs-compared/)、[4aiworld: Gemini 3 Explained: Fast, Thinking, Pro](https://4aiworld.com/gemini-3-fast-thinking-pro-models/)、[9to5Google: Gemini app rolling out 'Extended' thinking level](https://9to5google.com/2026/05/17/gemini-app-thinking-level/)、[BentoML: The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)、[The AI Rankings: DeepSeek in 2026](https://theairankings.com/deepseek/)、[ai-souken.com: DeepSeek-R1とは？使い方や料金、安全性について徹底解説](https://www.ai-souken.com/article/what-is-deepseek-r1)、[Humai: Reasoning Models Hallucinate More, Not Less — ICLR 2026 Paper](https://www.humai.blog/reasoning-made-ai-smarter-it-also-tripled-the-hallucinations/)、[Developers Digest: Extended Thinking in Claude](https://www.developersdigest.tech/blog/extended-thinking-claude-production-guide)、[Value Add VC: OpenAI API Pricing 2026](https://valueaddvc.com/blog/openai-api-pricing-2026-gpt-4o-o3-and-gpt-5-cost-breakdown-for-developers)
