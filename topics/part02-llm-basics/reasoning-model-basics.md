---
title: "推論モデル(Reasoning Model)とは何か"
part: 2
chapter: 第2章 モデルの種類と選び方
tags: [推論モデル, Reasoning Model, Chain-of-Thought, モデル選び, Thinking]
created: 2026-07-06
updated: 2026-07-27
---

# 推論モデル(Reasoning Model)とは何か

## これは何か

数学の応用問題、複数条件が絡む企画書の検討、バグの原因究明のような「多段階で考える必要がある」質問をAIに投げると、瞬時に答えを返すモデルはしばしば早合点し、途中の論理を飛ばして間違った結論を出す。**推論モデル(Reasoning Model、「Thinkingモデル」「思考モデル」とも呼ばれる)**とは、最終的な答えを出す前にモデル内部で段階的な「考える過程」を長く生成してから答えを組み立てるように訓練・調整されたモデルのことだ。これに対して、考える過程をほとんど挟まずに即答するモデルを「即答モデル」「高速モデル」(ChatGPTの「Instant」、Geminiの「Fast」など)と呼ぶ。同じAIサービスの中に「即答モデル」と「推論モデル」の両方が用意され、タスクに応じて使い分けるのが2026年7月時点の標準的な構成であり、この2階建て構造を知らないと、複雑な作業に不向きな即答モデルをデフォルトのまま使い続けて精度を損ねたり、逆に単純な作業に重い推論モデルを使って待ち時間とコストを無駄にしたりする。

## 仕組み・背景

推論モデルの「考える過程」は、[Chain-of-Thought(CoT)プロンプティング](../part05-prompt-engineering/chain-of-thought-prompting.md)でユーザーが「ステップバイステップで考えて」と指示していた挙動を、モデル自身が内部処理として自動的に行うように学習させたものだ。ユーザーが手順を書かなくても、モデルが質問を受け取った時点で「論点を洗い出す→検証する→矛盾がないか見直す」といった思考の連鎖を大量のトークンとして生成し、そのうえで最終回答を組み立てる。この思考過程は、画面に「Thinking」として要約表示される場合もあれば、コストだけ発生して中身は見えない場合もある。

この方向性を最初に製品化したのはOpenAIで、2024年9月に発表した「o1」が、内部で長い思考過程を生成してから答える専用モデルとして登場し、数学・コーディングのベンチマークで従来モデルを大きく上回った。これ以降、「即答モデル」と「推論モデル」を並べて提供する形が業界標準になり、2026年7月時点の主要ベンダーの構成は次のようになっている(名称・仕様は数か月おきに変わるため、あくまで執筆時点の目安)。

| ベンダー | 即答(Fast)系 | 推論(Thinking)系 | 特徴 |
|---|---|---|---|
| OpenAI(ChatGPT) | GPT-5.5 Instant(利用上限到達時はGPT-5.5 Instant Miniに自動切替) | GPT-5.6 Sol(2026年7月9日に一般提供開始)。モデルピッカーではThinking(Medium/High/Extra High)・Pro(Standard/Extended)として選択。API側は思考の深さを`reasoning.effort`(none/low/medium/high/xhigh/max)の6段階、さらに複数のサブエージェントに検討を分担させる「ultra」モードまで指定できる | 下位モデルのTerra・Lunaは通常のモデルピッカーには出ず、コーディング特化の「Codex」やAPI経由でのみ利用可。詳細は[ChatGPTのモデル一覧と使い分け](../part03-ai-chat-tools/chatgpt-model-lineup.md) |
| Anthropic(Claude) | 思考オフの通常応答 | Claude Sonnet 5(2026年6月30日公開)・Opus 4.8の「適応的思考(adaptive thinking)」。effort(思考の力加減)をlow/medium/high(既定)/xhigh/maxから選ぶ | 旧来の「オン・オフの二択+思考トークン数(budget_tokens)を手動指定」する拡張思考は新モデルでは廃止され、effortダイヤルに一本化された |
| Google(Gemini) | Gemini 3.6 Flash(2026年7月21日公開)、さらに軽量なGemini 3.5 Flash-Lite | Gemini 3 Thinking、Gemini 3.1 Proの「思考レベル(標準/拡張)」、最上位の「Gemini 3 Deep Think」(2026年2月に精度を大幅強化) | 次期フラグシップ「Gemini 3.5 Pro」は2026年5月のI/Oで予告されたが、7月時点でもパートナー向けテストにとどまり一般提供時期は未定 |
| DeepSeek | DeepSeek-V4-Flashの非thinkingモード | DeepSeek-V4-Flash/V4-Proの「thinkingモード」(「DeepThink」ボタンで切替)。旧R1の役割はV4に統合され、V4-Proは複雑な推論・長文コンテキスト(最大約100万トークン)向け | オープンウェイト(モデルの重みを公開)で無料利用・自社ホスティングも可能な点が特徴。旧名称の`deepseek-chat`/`deepseek-reasoner`は2026年7月24日で廃止され、`deepseek-v4-flash`の非thinking/thinkingモード指定に一本化。後継「R2」は2026年7月時点でも未リリース |

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
| ChatGPT | 画面左上のモデル名をクリック→「Instant」「Thinking」「Pro」から選択。「Configure」から思考の深さ(Medium/High/Extra High)を調整。APIでは`reasoning.effort`(none/low/medium/high/xhigh/max)で細かく指定可能 | 2026年7月時点の実体モデルはInstantがGPT-5.5、Thinking/ProがGPT-5.6 Sol。詳細な手順・プラン別の利用可否は[ChatGPTのモデル一覧と使い分け](../part03-ai-chat-tools/chatgpt-model-lineup.md)を参照 |
| Claude(claude.ai) | チャット画面のモデルセレクターでOpus・Sonnet等の対応モデルを選択→入力欄左下の「Search and tools」からeffort(low/medium/high(既定)/xhigh/max)を選択 | Claude Sonnet 5・Opus 4.8では「適応的思考」が既定で有効になっており、旧来のオン・オフの手動切り替え自体が不要になりつつある |
| Gemini | 画面上部のモデル選択(Fast/Thinking/Pro)をタップ→Fast(実体はGemini 3.6 Flash)・Proを選んだ場合はさらに「思考レベル(標準/拡張)」を選べる。Proの上位に「Deep Think」あり | フラグシップ「Gemini 3.5 Pro」は2026年7月時点でもパートナー限定テスト中のため、一般ユーザー向けのProは引き続きGemini 3.1 Pro系統。「思考モード」自体を選んだ場合は思考レベルの選択肢は出ず、常にThinkingとして動作 |
| DeepSeek(チャット画面) | 入力欄左下の「DeepThink」ボタンをオン(青色点灯)にするとV4のthinkingモードが応答 | オフの状態はV4-Flashの非thinkingモードが応答。旧名称`deepseek-reasoner`は2026年7月24日で廃止済み。思考過程はトグルで開いて確認できる |

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

推論モデルの「考える過程」は、画面に表示されない場合でも裏側でトークンを生成しており、そのトークン分の料金がかかるのが一般的な仕組み。たとえばOpenAIのGPT-5.6 Sol系のAPI価格は1Mトークンあたり入力5ドル・出力30ドル程度で、見える回答が短くても裏側の思考トークンがその何倍にも積み上がり、実質的な課金対象トークン数が膨らむことがある。effortを上げるほど、あるいはOpenAIが新設した複数のサブエージェントに検討を分担させる「ultra」モードを使うほど、この思考トークンの量とコストはさらに跳ね上がる。AnthropicのClaudeも同様に、思考トークンは出力トークンと同じ単価で課金される。「表示されている回答は短いのに、なぜか利用料が高い」と感じたら、この思考トークンの分量が原因であることが多い。判断の目安は「間違えたときの損失が、推論モデルに切り替えた際の追加コストの5倍以上あるか」で、この目安を上回るタスクほど推論モデルへの切り替えが割に合う。

## 注意点・よくある誤解

- **「推論モデルだからハルシネーション(もっともらしい誤情報の生成)が起きない」は誤解、ただし話は単純ではない**: 人物に関する事実確認(PersonQAのようなベンチマーク)ではOpenAIのo3が約33%、前世代のo1が約16%というデータがあり、推論モデルの方がハルシネーション率が高くなる傾向が報告される一方、2026年の複数のベンチマークでは、複雑な多段階推論タスクに限ると思考を深くすることでハルシネーション率がむしろ大きく下がる(例: GPT-5.5 Proが8.3%→4.2%、Claude Opus 4.7が9.4%→5.1%に半減という報告)という逆方向の結果も出ている。つまり「思考を深くすれば必ず正確になる」わけでも「推論モデルは必ずハルシネーションが増える」わけでもなく、タスクの性質(単発の事実想起か、多段階の論理検証か)によって効果の向きが変わる、という理解が実態に近い。むしろ「考えたから正しいはず」という思い込みの方が危険で、重要な事実確認は推論モデルの回答でも省略しない。
- **「自信を持って長く説明している=正しい」ではない**: ある調査では、AIモデルは間違っている回答のときの方が正しい回答のときより自信度が高くなる傾向が報告されている。回答の長さ・断定的な口調は精度の保証にならない。
- **モデル名・思考レベルの区分は数か月おきに変わる**: 本ページで挙げた名称(GPT-5.6 Sol、Claude Sonnet 5・Opus 4.8、Gemini 3 Thinking・Deep Think、DeepSeek V4等)は執筆時点の目安であり、実際の画面表示・最新モデル名は都度確認する。
- **推論モデルは「待ち時間・コストとのトレードオフ」であることを忘れない**: 数十秒〜数分の待ち時間、数倍のコストを払っても、単純な質問では精度がほぼ変わらないことが多い。OpenAIの「ultra」モードのように複数のサブエージェントで検討を分担させる仕組みは、さらに強力な分だけコストも増える「レバー」であって無料のアップグレードではない。まず即答モデルで試し、物足りなければ推論モデルに上げる順番が無駄を減らす。
- **推論過程の表示(Thinking欄)は「要約」であり、モデルの思考をすべて正確に記述しているとは限らない**点も留保しておく。表示された思考過程を鵜呑みにせず、最終的な結論・根拠は別途確認する。

## 最初の一歩

普段使っているAIツールのモデル選択画面を開き、即答系(Instant/Fast)と推論系(Thinking)がどう表示されているか確認する。次に、最近「精度が足りない」と感じた質問を1つ選び、推論モデルに切り替えて同じ質問をもう一度投げ、回答の違いを見比べてみる。

## 関連トピック

- [LLMの得意・不得意と挙動の特性](llm-strengths-and-limitations.md)
- [Chain-of-Thought(CoT)プロンプティング](../part05-prompt-engineering/chain-of-thought-prompting.md)
- [ChatGPTのモデル一覧と使い分け](../part03-ai-chat-tools/chatgpt-model-lineup.md)

## 更新履歴

### 2026-07-27: 主要ベンダーの推論モデル世代交代(GPT-5.6 Sol/Claude Sonnet 5・Opus 4.8/Gemini 3.6 Flash・Deep Think/DeepSeek V4)を反映して最新化
- **内容**: OpenAIのGPT-5.6(Sol/Terra/Luna、一般提供は2026年7月9日)への交代とreasoning effortがnone〜maxの6段階+複数エージェントに分担させる「ultra」モードへ拡張されたこと、Anthropicの適応的思考が既定化されたClaude Sonnet 5(2026年6月30日公開)・Opus 4.8、GoogleのGemini 3.6 Flash登場とフラグシップ「Gemini 3.5 Pro」がパートナー限定テストにとどまり一般提供が遅延している現況・Gemini 3 Deep Thinkの位置づけ、DeepSeekがR1相当のthinkingモードをV4(V4-Flash/V4-Pro)に統合し`deepseek-chat`/`deepseek-reasoner`という旧名称が2026年7月24日で廃止されたことを反映し、仕組み・背景/実務での使い方/コスト面の意思決定材料の各節を更新。ハルシネーションの注意点も、タスクの性質(事実想起か多段階の論理検証か)によって推論の深さがプラスにもマイナスにも効くという2026年の複数ベンチマークの知見を踏まえて書き直した
- **出典**: [OpenAI: GPT-5.6](https://openai.com/index/gpt-5-6/)、[OpenAI Help Center: A preview of GPT-5.6 (Sol, Terra, and Luna)](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna)、[Artificial Analysis: GPT-5.6 has landed](https://artificialanalysis.ai/articles/gpt-5-6-has-landed)、[eesel AI: GPT-5.6 pricing](https://www.eesel.ai/blog/gpt-5-6-pricing)、[Developers Digest: Claude Sonnet 5 Developer Guide](https://www.developersdigest.tech/blog/claude-sonnet-5-developer-guide-2026)、[codersera: Claude Sonnet 5 vs Claude Opus 4.8](https://codersera.com/blog/claude-sonnet-5-vs-opus-4-8-2026/)、[TechCrunch: Google releases three new Gemini models — but no 3.5 Pro](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)、[9to5Google: Gemini 3 Deep Think gets 'major upgrade'](https://9to5google.com/2026/02/12/gemini-3-deep-think-upgrade/)、[DeepSeek: DeepSeek V4 GA — Legacy Aliases Retire July 24](https://deepseek.ai/blog/deepseek-v4-ga-surge-pricing-migration)、[DeepSeek API Docs: DeepSeek V4 Preview Release](https://api-docs.deepseek.com/news/news260424/)、[decodethefuture: DeepSeek R2 Release Date: Status & Rumors](https://decodethefuture.org/en/deepseek-r2-explained/)、[digitalapplied: AI Model Hallucination Rate Benchmarks 2026](https://www.digitalapplied.com/blog/ai-model-hallucination-rate-benchmarks-2026-study)

### 2026-07-06: 初版執筆
- **内容**: 推論モデル(Reasoning Model)を「答えを出す前に内部で段階的な思考過程を生成するモデル」として即答モデルと対比して定義し、OpenAI o1(2024年9月)を起点とする経緯、2026年7月時点のOpenAI/Anthropic/Google/DeepSeekの即答・推論モデル対応表、タスク別の使い分け表、主要ツールでの切り替え場所、思考トークンの課金の仕組み、推論モデルでもハルシネーションが減らない(むしろ増える場合がある)という注意点をまとめた
- **出典**: [Claude Platform Docs: Extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)、[Claude Help Center: Change the model, effort, and thinking settings](https://support.claude.com/en/articles/8664678-change-the-model-effort-and-thinking-settings)、[Anthropic: Claude Opus 4.6](https://www.anthropic.com/news/claude-opus-4-6)、[MarkTechPost: Claude Sonnet 5 vs Sonnet 4.6 vs Opus 4.8](https://www.marktechpost.com/2026/06/30/anthropic-claude-sonnet-5-vs-sonnet-4-6-vs-opus-4-8-agentic-coding-benchmarks-api-pricing-and-cost-performance-tradeoffs-compared/)、[4aiworld: Gemini 3 Explained: Fast, Thinking, Pro](https://4aiworld.com/gemini-3-fast-thinking-pro-models/)、[9to5Google: Gemini app rolling out 'Extended' thinking level](https://9to5google.com/2026/05/17/gemini-app-thinking-level/)、[BentoML: The Complete Guide to DeepSeek Models: V3, R1, V4 and Beyond](https://www.bentoml.com/blog/the-complete-guide-to-deepseek-models-from-v3-to-r1-and-beyond)、[The AI Rankings: DeepSeek in 2026](https://theairankings.com/deepseek/)、[ai-souken.com: DeepSeek-R1とは？使い方や料金、安全性について徹底解説](https://www.ai-souken.com/article/what-is-deepseek-r1)、[Humai: Reasoning Models Hallucinate More, Not Less — ICLR 2026 Paper](https://www.humai.blog/reasoning-made-ai-smarter-it-also-tripled-the-hallucinations/)、[Developers Digest: Extended Thinking in Claude](https://www.developersdigest.tech/blog/extended-thinking-claude-production-guide)、[Value Add VC: OpenAI API Pricing 2026](https://valueaddvc.com/blog/openai-api-pricing-2026-gpt-4o-o3-and-gpt-5-cost-breakdown-for-developers)
