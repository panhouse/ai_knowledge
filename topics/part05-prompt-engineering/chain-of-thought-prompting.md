---
title: Chain-of-Thought(CoT)プロンプティング
part: 5
chapter: 第3章 思考を引き出す手法
tags: [プロンプトエンジニアリング, CoT, 推論モデル, Zero-shot, 適応的思考]
created: 2026-07-05
updated: 2026-07-24
---

# Chain-of-Thought(CoT)プロンプティング

## これは何か

割引計算・条件が複数絡む判定・多段階の論理を要する質問をAIに投げると、根拠を示さずにいきなり結論だけを返し、しかもその結論が間違っていることがある。Chain-of-Thought(CoT、「思考の連鎖」)プロンプティングとは、AIに答えを一足飛びに出させるのではなく、人間が暗算せず紙に途中式を書くように「途中の考え方」を言葉にしながら段階的に結論へ進ませる指示テクニックのことだ。単に「ステップバイステップで考えて」と一言添えるだけで、計算・論理パズル・複雑な条件判定の正答率が大きく上がることが知られている。

2025年以降、主要なAIモデルには、これを毎回指示しなくても自動でやってくれる「推論モデル(reasoning model)」「Thinkingモード」が標準搭載され、2026年に入るとさらに一歩進んで「思考するかどうか・どこまで深く考えるか」をモデル自身がリクエストごとに判断する仕組みへ移行しつつある。たとえば2026年7月公開のClaude Sonnet 5は、ユーザーが何も設定しなくても「適応的思考(adaptive thinking)」が既定で有効になる。そのため今は「CoTを自分で書くべき場面」と「モデルの内蔵Thinkingに任せるべき場面」の見極めに加え、「思考の深さそのものをどう調整するか」まで実務上のポイントになっている。

## 仕組み・背景

大規模言語モデルは、質問を読んでから答えの最初の1トークン(単語の断片)を生成するまでに使える「計算量」が限られている。難しい問題ほど、いきなり結論を書かせると計算のステップを省略してしまい、間違いが起きやすい。CoTプロンプティングは、モデルに答えを出す前に途中の推論過程をテキストとして書き出させることで、実質的に「考える時間(計算ステップ)」を増やし、各ステップを言語化することで論理の飛躍や計算ミスを減らす手法だ。2022年にGoogleの研究チームが提案した"Chain-of-Thought Prompting"論文と、続く"Large Language Models are Zero-Shot Reasoners"論文(通称Kojima論文)で、「Let's think step by step(ステップバイステップで考えましょう)」という一文を付けるだけで算数問題の正答率が十数%から70〜80%まで跳ね上がることが示され、プロンプトエンジニアリングの基本技として広まった。

2024年後半以降のOpenAI o1/o3系とその後継のGPT-5系、Anthropic Claude 3.7以降の「拡張思考(extended thinking)」、GoogleのGemini 2.5/3系「Thinking」モデルは、このCoTのプロセスをモデルの内部処理として自動化した「推論モデル」にあたる。ユーザーが「ステップバイステップで」と書かなくても、モデルが内部で見えない思考トークンを生成しながら段階的に答えを組み立て、その過程の要約を「Thinking」欄として画面に表示する。

2026年に入ると、この仕組みはさらに一段抽象化された。OpenAIのGPT-5.5、AnthropicのClaude Opus 4.7/4.8・Claude Sonnet 5は、いずれも「思考する/しない」を都度モデルが自動判断し(簡単な質問には思考なしで即答し、難しい問題にだけ思考トークンを割く)、その深さを「reasoning effort」「effort」という1段のダイヤル(low/medium/high/xhighなど)で指定する設計にそろいつつある。Claude Sonnet 5ではこの「適応的思考」が既定で有効になり、従来の「オン/オフ+思考トークン数の予算(budget_tokens)を手動指定する」方式(拡張思考)は同モデルでは廃止され、`budget_tokens`を指定するとエラーになる。つまりCoTは「ユーザーが書く呪文」→「モデルに内蔵されたThinking機能」→「effortという1つのパラメータ・モードで深さを調整するもの」へと進化してきている、という理解が2026年時点では実態に近い。

## 使いどころ・使い分け

CoTが効くかどうかは、タスクの性質で決まる。人間が暗算やその場の思いつきで答えず、紙に書いて考えるようなタスクではCoTが効き、単純な検索・分類・整形ではほぼ効果がない。なお、課題が「答えの正しさ」ではなく「出力フォーマット・トーンのブレ」なら、CoTではなく例示で型を教える[Zero-shot・Few-shotプロンプティング](zero-shot-and-few-shot-prompting.md)の出番である。

| タスクの性質 | CoTの効果 | 具体例 |
|---|---|---|
| 複数ステップの計算・論理 | 効果大 | 割引・税込み計算、旅費精算の妥当性判定、KPIの逆算 |
| 条件が絡み合う判断 | 効果大 | 契約書の複数条項を突き合わせたリスク判定、稟議の承認可否判断 |
| 多段階の文章構成 | 効果中 | 複雑な提案書の骨子作り、複数観点を統合する要約 |
| 単純な事実検索・言い換え | 効果小〜なし | 「この単語の意味は?」「この文を丁寧語にして」 |
| 定型フォーマット変換 | 効果小〜なし | CSVをMarkdown表にする、指定フォーマットへの整形 |
| 単純な二値・多値分類 | 効果小〜なし | 「このメールはスパムか」「感情はポジ・ネガ・中立か」 |

もう一段、実務で重要な使い分けが「自分でCoTを書くべきか、モデルの内蔵Thinkingに任せるべきか」だ。

| モデルの種類 | 具体例 | 明示的なCoT指示 | 理由 |
|---|---|---|---|
| 非推論(高速)モデル | ChatGPTの「Instant」、Claudeの思考オフ(旧モデルの拡張思考オフ)、Geminiの「Fast」 | 有効・推奨 | 内部で自動推論をしないため、指示しないと考えずに即答してしまう |
| 推論(Thinking)モデル | ChatGPTの「Thinking」「Pro」、Claudeの拡張思考/適応的思考が有効な状態、Geminiの「Thinking」「Pro」 | 基本不要、むしろ最小限に | 既に内部で多段階推論をしているため、重ねて細かく指示すると回答が冗長・遅くなるだけで精度は上がりにくい |

OpenAIのGPT-5.5向けプロンプティングガイドも、推論モデルに対しては「ステップバイステップで考えて」と手順を逐一書くより、明確なゴール・制約条件・期待する出力フォーマット(「JSON形式で」「見出しは3つまで」など)を渡すほうが結果が安定すると明言しており、思考の深さ自体は`reasoning.effort`(none/low/medium/high/xhigh、既定はmedium)というパラメータ、あるいはChatGPTの「Instant/Thinking/Pro」モード選択で調整するのが基本という考え方に変わった。Anthropicも同様に、Claude Sonnet 5・Claude Opus 4.7/4.8では思考の深さを`effort`パラメータ(low/medium/high(既定)/xhigh/max)で制御する設計に移行しており、プロンプト側での細かいCoT指示は「まず高レベルの指示から始め、Claudeの誘導がうまくいかない場合だけ補足する」補助的な位置づけになっている。つまり2026年時点では「推論モデル=常にCoT不要」というより、「モデルの設定(Thinkingのオン/オフ・effortレベル)がまず主役で、プロンプト内の明示的なCoT指示はそれを補う二次的な手段」という理解が実務的に近い。

## 実務での使い方

### コピペで使える実例(1): Zero-shot CoT

非推論モデルや、推論モードを持たない旧来型モデルに対して、一言添えるだけで精度を底上げできる最も手軽な型。

```
以下の問題に答えてください。
いきなり結論を出さず、途中の計算・判断根拠をステップに分けて示してから、
最後に「結論:」に続けて答えだけを一行でまとめてください。

[ここに問題文を貼る]
例)当社は現在、月額10万円のツールAと、月額7万円のツールBを併用している。
   ツールBを解約してツールAの上位プラン(月額14万円)に一本化する場合、
   年間のコストはいくら増減するか。
```

### コピペで使える実例(2): Few-shot CoT(お手本付き)

業務特有の判断基準がある場合は、途中の考え方まで含めた「お手本」を1〜2個見せてから、同じ形式で答えさせると再現性が上がる。経費精算の可否判定、問い合わせの一次切り分けなどに応用しやすい。

```
あなたは経費精算の一次チェック担当です。以下のお手本と同じ考え方の手順で、
最後の申請についても判定してください。

---
【お手本1】
申請内容: 深夜23時までの残業後にタクシーで帰宅した交通費 3,200円
考え方:
 1. 就業規則を確認: 22時以降の残業でタクシー利用は原則承認対象
 2. 深夜残業の事実: 23時退社なので該当する
 3. 金額の妥当性: 自宅までの一般的なタクシー料金として不自然な高額ではない
判定: 承認

【お手本2】
申請内容: 定時(18時)退社後、私用の途中に立ち寄った書店での書籍代 1,800円
考え方:
 1. 業務との関連性を確認: 職務に直接関係する書籍か不明
 2. 定時退社であり残業要件に該当しない
 3. 経費規程の対象品目(業務用書籍は要事前申請)に該当するか確認: 事前申請なし
判定: 却下

---
【判定対象】
申請内容: [ここに実際の申請内容を貼る]
考え方:
```

### コピペで使える実例(3): 構造化CoT(思考と結論を分離)

思考過程をそのまま最終回答に混ぜたくない場合(顧客向け文面など)は、タグで区切って「思考」と「回答」を分離すると、後工程で思考部分だけを非表示にできる。

```
次のクレームメールへの返信文を作成してください。
まず<thinking>タグの中で、相手の感情・要求事項・自社の落ち度の有無を整理し、
そのうえで<answer>タグの中に、顧客にそのまま送れる返信文だけを書いてください。

[ここにクレームメール本文を貼る]
```

### ツール横断の対応付け

| ツール | 明示的CoTプロンプトの効き方 | 内蔵Thinking(推論)モード | オンにする場所(2026年7月時点) |
|---|---|---|---|
| ChatGPT | 「Instant」モードでは有効。「Thinking」「Pro」モードでは基本不要 | GPT-5.5系「Thinking」(推論強度: Medium/High/Extra High)、「Pro」(Standard/Extended) | 入力欄上部のモデルピッカーで Instant / Thinking / Pro を選択。Extra HighやPro Extendedなど上位の推論強度はPro/Business/Enterprise/Eduプランで解放 |
| Claude(Claude.ai) | 思考オフの通常応答では有効。思考オンでは基本不要、まず高レベル指示から | Claude Sonnet 5(2026年7月公開、無料/Proプランの既定モデル)やOpus 4.7/4.8では「適応的思考」が既定で有効。旧世代モデルは「拡張思考(Extended thinking)」を手動トグルで有効化 | 送信ボタン横のモデル名をクリックし、モデルとThinking関連の設定を確認する。新モデルは思考の有無・深さをモデル自身が判断するため、手動でThinkingをオンにする操作自体が不要になりつつある |
| Gemini(gemini.google.com) | 「Fast」では有効 | 「Thinking」、上位の「Pro」は常時Thinking。Thinkingレベル(Standard/Extended)も選択可 | 入力欄のモデルピッカーで Fast / Thinking / Pro を選択。Fast選択時もThinkingレベルを選べる |

### 料金・速度のトレードオフ

推論モデルの「見えない思考」も、多くのAPIでは出力トークンと同じ単価で課金される。Anthropicの適応的思考(旧・拡張思考)も、OpenAIの推論トークンも同様に出力扱いで、複雑な問題では最終的な回答文の数倍の思考トークンを消費することがあり、体感コストと待ち時間(数秒〜数十秒)が跳ね上がる。2026年時点では、この「どこまで考えさせるか」を細かく制御する手段として、OpenAIの`reasoning.effort`(none/low/medium/high/xhigh)、Anthropicの`effort`(low/medium/high/xhigh/max)というパラメータが用意されており、ChatGPTの「Instant/Thinking(Medium・High・Extra High)/Pro」やClaudeのモデル・モード選択は、内部的にはこのeffortレベルを切り替えるUIだと理解しておくとよい。したがって、

- 単純作業・大量処理: 非推論モデル(Instant/Fast)、または推論モデルでもeffortを低め(low/medium)に設定し、コストと速度を優先
- 一発勝負の重要判断(契約リスク判定、経営数値の検算など): 推論モデル(Thinking/Pro)でeffortを高め(high以上)に設定し、精度を優先

という使い分けが、コスト管理の観点からも合理的だ。

## 注意点・よくある誤解

- **「Thinking」欄の文章を鵜呑みにしない**: 推論モデルが表示する思考過程は「実際の内部計算をそのまま人間可読にしたもの」ではなく要約・言い換えであることが多い。もっともらしい理由付けをしながら結論だけ誤っているケースもあるため、重要な数値は思考過程ではなく最終結論を検算する
- **推論モデルへのCoT指示は「二重がけ」になりやすい**: Thinkingオンのモデルに「ステップバイステップで考えて」と重ねて書いても精度はほぼ上がらず、回答が無駄に長くなり速度・コストだけ悪化することが多い。まずは指示なしで試し、精度が不足する場合だけ高レベルの補足を足す
- **「思考の深さ」は言い回しよりモード・パラメータで揃えるほうが安定する**: 2026年のOpenAI・Anthropic公式ガイドはいずれも、思考の深さをプロンプトの言葉で誘導するより、ChatGPTの「Thinking」内のレベル選択やAPIの`reasoning.effort`/`effort`パラメータで直接指定するほうが再現性が高いとしている。プロンプト内の「もっとよく考えて」的な指示は、あくまで補助的な微調整として使う
- **「ステップバイステップで考えて」の一文だけでは思考が浅くなることがある**: 何をどの順で考えるべきかが自明でないタスクでは、Zero-shot CoTの一言だけでは効果が乏しい場合がある。「1. 基本の割引率を特定→2. 加算条件の確認→3. 上限チェック→4. 結論」のように、考える手順そのものを番号付きでプロンプトに示すと、複数条件が絡む業務ロジックの見落としがさらに減って安定する
- **Few-shotのお手本が偏っていると、その偏りごと答えが引きずられる**: 経費精算の判定例のように業務ルールを教える場合、お手本自体が古い規程や個人の癖を反映していないか確認する
- **単純タスクにまでThinkingを使うと逆に非効率**: 定型的な言い換えや簡単な分類にThinkingモードを使うと、待ち時間とコストが増えるだけで品質はほとんど変わらない
- **CoTは「魔法の呪文」ではない**: モデルが元々知らない事実(社内規程の詳細など)は、CoTを付けても正しく推論できない。必要な情報はプロンプトや参照資料として与える必要がある

## 最初の一歩

次に複数ステップの計算や判断をAIに頼むとき、まず非推論モード(ChatGPTのInstant、Claudeの思考オフなど)に「ステップバイステップで考えてから結論だけ書いて」を付けて試し、同じ質問を推論モード(ChatGPTのThinking、Claudeの思考オンなど)にも投げて、回答の精度・速度・コスト感を見比べてみるとよい。余裕があれば、推論モードの中でも「High」「Extra High」のようにeffort(思考の強さ)を変えて同じ質問を試し、精度がどこまで伸びてコストがどう増えるかも体感しておくと、実務でのモデル選びの勘所がつかめる。

## 関連トピック
- [プロンプトの基本構成要素](./prompt-basic-structure.md)
- [Zero-shot・Few-shotプロンプティング](./zero-shot-and-few-shot-prompting.md) — 出力の形式・トーンを揃えたい場合はこちら

## 更新履歴

### 2026-07-24: 推論モデルの進化(effortダイヤル・適応的思考)を反映して最新化
- **内容**: Claude Sonnet 5(2026年7月公開)で「適応的思考」が既定化され旧来の拡張思考(budget_tokens指定)が廃止されたこと、OpenAI GPT-5.5の`reasoning.effort`とAnthropicの`effort`パラメータが「CoTを書く」から「思考の深さをダイヤルで指定する」への移行を体現していることを反映し、仕組み・背景/使いどころ・使い分け/ツール横断の対応付け/料金トレードオフ/注意点/最初の一歩の各節を更新
- **出典**: [Extended thinking - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
- **出典**: [Steering thinking (adaptive thinking, effort levels) - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/thinking-steering-and-cost)
- **出典**: [Claude Sonnet 5の新機能(適応的思考が既定で有効) - Claude Platform Docs](https://platform.claude.com/docs/ja/about-claude/models/whats-new-sonnet-5)
- **出典**: [Reasoning best practices - OpenAI API](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
- **出典**: [GPT-5.5 in ChatGPT - OpenAI Help Center](https://help.openai.com/en/articles/11909943)
- **出典**: [推論モデルに「think step by step」は、もういらない - Qiita](https://qiita.com/akira_papa_AI/items/8bd363fa218de466c581)
- **出典**: [Gemini App Gets New Thinking Levels - Beebom](https://gadgets.beebom.com/news/google-gemini-app-thinking-levels-app-integrations-roll-out)

### 2026-07-06: 重複ページの統合
- **内容**: Zero-shot/Few-shot/CoTを扱う重複6ページを本ページ(CoT)とZero-shot・Few-shotページの2本に統合。考える手順を番号付きで示すと安定するコツと、Few-shotページへの使い分け導線を追記した。統合元: prompting-techniques-basics.md / zero-few-shot-and-cot-prompting.md / zero-shot-few-shot-cot-prompting.md / zero-shot-few-shot-cot.md
- **出典**: [Chain of thought - Claude Docs (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought)

### 2026-07-05: 初版執筆
- **内容**: CoTプロンプティングの定義・仕組み・使い分け(手動CoT vs 推論モデルの内蔵Thinking)・Zero-shot/Few-shot/構造化の実例プロンプト・ChatGPT/Claude/Geminiの対応付けと料金トレードオフを執筆
- **出典**: [Chain of thought - Claude Docs (Anthropic)](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/chain-of-thought)
- **出典**: [Let Claude think (chain of thought prompting) - Anthropic](https://docs.anthropic.com/en/docs/let-claude-think)
- **出典**: [Extended thinking - Claude Platform Docs](https://platform.claude.com/docs/en/build-with-claude/extended-thinking)
- **出典**: [GPT-5 prompting guide - OpenAI Cookbook](https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide)
- **出典**: [Reasoning best practices - OpenAI API](https://developers.openai.com/api/docs/guides/reasoning-best-practices)
- **出典**: [GPT-5.5 in ChatGPT - OpenAI Help Center](https://help.openai.com/en/articles/11909943-gpt-5-in-chatgpt)
- **出典**: [Change the model, effort, and thinking settings - Claude Help Center](https://support.claude.com/en/articles/10574485-using-extended-thinking)
- **出典**: [Gemini thinking - Gemini API Docs (Google)](https://ai.google.dev/gemini-api/docs/thinking)
- **出典**: [Gemini app rolling out 'Extended' thinking level - 9to5Google](https://9to5google.com/2026/05/17/gemini-app-thinking-level/)
- **出典**: [Fast, Thinking, and Pro: A Guide to Google's Gemini Models - Devoteam](https://www.devoteam.com/expert-view/gemini-model-fast-vs-thinking-vs-pro/)
- **出典**: [Large Language Models are Zero-Shot Reasoners (Kojima et al., 2022)](https://machelreid.github.io/resources/kojima2022zeroshotcot.pdf)
