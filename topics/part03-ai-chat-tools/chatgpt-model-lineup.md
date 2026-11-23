---
title: ChatGPTのモデル一覧と使い分け
part: 3
chapter: 第1章 プラン・モデルの選び方
tags: [ChatGPT, モデル選択, GPT, 推論モデル, GPT-6, GPT-6 Sol, GPT-6.2, GPT-5.6 Luna]
created: 2026-07-05
updated: 2026-11-23
---

# ChatGPTのモデル一覧と使い分け

## これは何か

ChatGPTの画面には、速度・精度・コストのバランスが異なる複数のモデル(またはモデルの「考える深さ」を調整するスライダー)が用意されている。デフォルトのまま使い続けても多くの場面で困らないが、複雑な分析やコーディングでは推論(reasoning、回答前にモデル内部で段階的に考えること)に力を入れたレベルに切り替えるだけで回答の質が大きく変わる。逆に単純な作業に重い設定を使うと、応答が遅くなるうえ利用回数の上限(レートリミット)を早く消費してしまう。自分のタスクに合ったレベルを選べるようになっておくと、同じ契約プランでもアウトプットの質と使える回数の両方が変わってくる。

## 仕組み・背景

### 2026年11月時点の全体像: 「チャット」と「Work・Codex」でモデルが違う

2026年9月3日に次世代フラッグシップ「GPT-6 Astra」が発表されて以降、ChatGPTのモデルはGPT-6世代へ移行した。11月時点でいちばん押さえておきたいのは、**同じChatGPTでも、通常のチャット画面と、成果物づくりのエージェント「ChatGPT Work」・コーディングエージェント「Codex」とでは、選べるモデルが別々に管理されている**という点である(利用上限も別枠)。

| 画面 | 中心になるモデル(2026年11月時点) | 選び方 |
|---|---|---|
| 通常のチャット(有料プラン) | **GPT-6 Sol**(Instant〜Extra High)、最上位の「Pro」は**GPT-6 Pro**(GPT-6 Astraが土台) | 推論の深さを決めるスライダーで選ぶ |
| 通常のチャット(Free/Go) | **GPT-5.6 Luna** | モデルは選べない。「Think」ボタンで1回だけ深く考えさせる |
| ChatGPT Work・Codex | **GPT-6.2 Astra/GPT-6.2 Sol**(2026年11月17日提供開始)ほか | Work・Codexそれぞれのモデル選択メニューで選ぶ |

2026年11月17日に公開されたGPT-6.2 Astra・SolはPlus・Pro・Enterprise・EduのWorkとCodexで使えるようになったが、**通常のチャットの選択肢は変わっていない**(OpenAIヘルプセンターの記載)。「最新のGPT-6.2をチャットで使いたい」と探しても見つからないのはこのためである。

### チャット画面の「推論スライダー」

有料プランのチャット画面では、モデルピッカー内のスライダーで「Instant/Medium/High/Extra High/Pro」の段階を選ぶ。左ほど速く、右ほど回答前に内部で考える時間(推論、reasoning)が長くなり、精度が上がる代わりに待ち時間と利用枠の消費が増える。

| 段階 | 中身(2026年11月時点) | 向く仕事 |
|---|---|---|
| Instant | GPT-6 Sol(すぐ返答) | メール文面、要約、軽い壁打ち |
| Medium/High | GPT-6 Solが標準〜長めに考える | 分析、長文の精読、企画の論理展開 |
| Extra High | GPT-6 Solで最も深く考える | コードのデバッグ、多段階の検討 |
| Pro | GPT-6 Pro(GPT-6 Astraが土台)。GPT-5.6 Sol Proも選べる | 誤りが許されない調査・判断 |

どの段階まで使えるかはプランで決まる(下記「プランによる違い」)。以前から「Latest(最新)」を選んでいた人は同じ段階のままGPT-6に移され、GPT-5.6 Solを明示的に選んでいた人はGPT-5.6のまま残る。GPT-6への移行で、選べる旧モデルが廃止されたわけではない。

### Work・Codexで選べるモデル

- **GPT-6.2 Astra**: 負荷の高い専門業務向けの上位モデル。API名は`gpt-6.2-astra`、API価格は100万トークンあたり入力8ドル・出力40ドル(キャッシュ入力0.40ドル)
- **GPT-6.2 Sol**: 日常業務向けの主力モデル。API名は`gpt-6.2-sol`、入力2ドル・出力10ドル(キャッシュ入力0.10ドル)
- **GPT-6.1 Sol・GPT-6.1 Terra、GPT-5.6 Sol・Terra・Luna**: Work・Codexでは前の世代も選べる(Terraはチャットでは選べない)。Enterprise・Eduでは管理者の有効化が必要なものがある

Proプランでは、応答を高速化する「Ultrafast」もWork・Codexで使える(Pro 200ドルはSolから、Pro 500ドルは両モデルで)。

### 「モデル」と「プラン」は別の話

プラン(Free/Go/Plus/Pro/Business/Enterprise)は「いくら払っていくつ使えるか」という契約の話、モデルやスライダーの位置は「同じ会話の中でどれだけ考えさせるか」という話である。プランは「箱の大きさ」、スライダーは「箱の中でどれだけ力を入れるか」と考えると整理しやすい。

Deep Research(高度な調査レポート機能)のような専用機能は、モデル選択とは別に、その機能自体を呼び出す。なお旧称の「エージェントモード(ChatGPT Agent)」は2026年7月9日に「ChatGPT Work」へ一本化されており、ブラウザ操作を伴う代行作業もWorkで扱う([ChatGPTのエージェント機能](chatgpt-agent-mode-feature.md)参照)。

## 使いどころ・使い分け

### 業務シーン別の選び方

| 業務シーン | 向いている設定 | 理由 |
|---|---|---|
| メール・チャット文面の作成、要約、雑談的な壁打ち | チャットのInstant(Free/GoはGPT-5.6 Lunaのまま) | 待ち時間がほぼなく、多くのメッセージを回せる |
| 大量の問い合わせ下書きを次々にこなす | Free/GoならGPT-5.6 Luna(テキストチャットは事実上無制限) | 品質より件数が重要な場面。無料・低価格プランでも数をこなせる |
| 複雑な数値分析、契約書などの長文精読、多段階の論理展開が必要な企画書 | チャットのMedium〜High | 内部で考える時間を確保することで見落としが減る |
| コード生成・デバッグ | チャットのExtra High(Pro以上)/CodexでGPT-6.2 Sol・Astra | 推論の深さが精度に直結する。まとまった実装を任せるならCodex |
| 経営判断に関わる調査、法務・財務など誤りが許されない検討 | チャットのPro(GPT-6 Pro。Pro・Business・Enterprise) | 最も精度が高いが遅く、利用枠も少ない |
| 表計算・スライド・文書など「完成品」まで一気に仕上げたい | ChatGPT WorkでGPT-6.2 Sol(重い案件はGPT-6.2 Astra) | Workは成果物づくりのエージェント。最新のGPT-6.2はWorkとCodexでのみ選べる |
| 複数サイトを横断した情報収集、フォーム入力・予約などの代行 | ChatGPT Work | 旧エージェントモードはWorkに統合済み。Chat・Work・Codexの切り替えでWorkを選ぶ |

判断の目安は「**軽い・急ぎ→Instant**」「**込み入っている・裏取りが必要→Medium〜High**」「**コード・難問→Extra High/Codex**」「**失敗が許されない一発勝負→Pro**」「**成果物まで任せたい→Work**」の5つで考えればよい。迷ったらスライダーは初期位置のままでよい。

### 比較表(2026年11月時点)

| 設定・モデル | どこで使うか | 特徴 | 利用できるプラン |
|---|---|---|---|
| GPT-6 Sol(Instant〜Extra High) | チャット | 有料プランのチャットの主力。スライダーで考える深さを調整 | Plus(Instant〜High)、Pro・Business・Enterprise(Extra Highまで) |
| GPT-6 Pro(GPT-6 Astraが土台) | チャットの「Pro」段階 | 最高精度。遅く、週単位の利用枠がある | Pro・Business・Enterprise |
| GPT-5.6 Luna | Free/Goのチャット | 速くて軽い。テキストチャットは事実上無制限 | Free・Go |
| GPT-6.2 Astra | Work・Codex | 負荷の高い専門業務向け。API価格は入力$8/出力$40 | Plus・Pro・Enterprise・Edu |
| GPT-6.2 Sol | Work・Codex | 日常業務の主力。API価格は入力$2/出力$10 | Plus・Pro・Enterprise・Edu |

## 実務での使い方

### スライダーの切り替え手順(Web版・有料プラン)

1. チャット画面上部のモデルピッカーを開く
2. スライダーで「Instant/Medium/High/Extra High/Pro」のいずれかを選ぶ(契約プランで使えない段階は選べない)
3. 選んだ段階は以降のメッセージに適用される。重い段階で済ませたら、日常のやり取りはInstantに戻しておくと利用枠を節約できる

Business・Enterpriseでは、管理者がメンバーの使えるモデルを制限している場合がある。Businessでは設定→一般にある「Higher intelligence」の項目もあわせて確認する。

### Free/Goプランでの操作

モデルピッカーは表示されず、GPT-5.6 Lunaが使われる。難しい質問だけ深く考えさせたいときは、入力欄の「**Think**」ボタンをオンにしてから送信する(そのメッセージだけ処理時間が長くなる)。

### ChatGPT Work・Codexでのモデル選択

WorkとCodexには、チャットとは別のモデル選択メニューがある。GPT-6.2 Astra・Solを使いたい場合はこちらで選ぶ。利用上限もチャットとは別に数えられるため、「チャットの上限に達したからWorkも使えない」とはならない。

### プランによる違い(モデル選択の観点、2026年11月時点)

- **Free/Go**: GPT-5.6 Lunaが既定で、テキストチャットは事実上無制限(乱用防止の制限はある)。Medium以上の段階とProは使えない。「Think」ボタンで個別メッセージだけ深く考えさせられる
- **Plus**: チャットはInstant・Medium・Highまで(Extra HighとProは対象外)。WorkとCodexではGPT-6.2 Astra・Solを選べる
- **Pro(100ドル/200ドル)**: チャットでExtra HighとPro(GPT-6 Pro)まで使える。ただしGPT-6 Proは無制限ではなく、Pro 100ドルではGPT-6 ProとGPT-5.6 Sol Proで週単位の枠を共有、Pro 200ドルでは週の上限に達するとGPT-5.6 ThinkingのMediumに切り替わる
- **Business**: Extra High・Proまで使えるが、使えるモデルは管理者が制御できる。Business Standard・PremiumではGPT-6 ProとGPT-5.6 Sol Proが同じ利用枠を共有する
- **Enterprise・Edu**: Extra High・Proまで使えるが、ワークスペースのモデル利用権限に従う。新しい管理画面が届くまで旧来のモデルピッカーが表示される利用者もいる

プランごとの料金・機能・ガバナンスの全体像は[ChatGPTのプラン比較](chatgpt-plan-comparison.md)を参照。本ページはモデル選びに絞って解説する。

### コピペで使える例(モデルの実力を引き出すプロンプトの一言)

スライダーをMedium以上に上げるだけでなく、プロンプト内でも「じっくり検討してほしい」旨を明示すると、思考ステップを増やす方向に働きやすい。

```
このプロンプトは複数の前提条件を比較検討する必要があります。
結論を急がず、以下の手順で考えてください。
1. 論点を洗い出す
2. それぞれの論点についてメリット・デメリットを整理する
3. 最後に総合的な結論と根拠を述べる
```

### 社内マニュアルに書くときのひな形

モデル名は数か月で変わるため、社内マニュアルには「用途→画面→設定」の順で書き、モデル名は括弧で添える程度にとどめると書き直しが少なくて済む。

```
## ChatGPTの使い分け(2026年11月時点)
- 日常のメール・要約: チャット/スライダー「Instant」
- 分析・契約書の精読: チャット/スライダー「High」(GPT-6 Sol)
- 資料・表の作成を任せる: ChatGPT Work(GPT-6.2 Sol)
- 重要な判断の最終確認: チャット/スライダー「Pro」(Proプラン以上のみ)
※ 画面の表示が変わった場合は情報システム部門に連絡すること
```

## 注意点・よくある誤解

- **モデル名・区分は数か月おきに変わる**: 2026年だけでもGPT-5.6(7月)、GPT-6 Astra(9月)、GPT-6.1 Sol、GPT-6.2 Astra・Sol(11月)と世代交代が続いている。本ページの名称は執筆時点の目安であり、実際の画面表示と公式ヘルプを都度確認する
- **「最新のGPT-6.2」はチャットでは選べない**: 2026年11月時点でGPT-6.2 Astra・SolはWorkとCodex向けで、通常のチャットはGPT-6 Sol/GPT-6 Proのまま。記事で「GPT-6.2が使えるようになった」と読んでも、チャット画面に表示されないのは不具合ではない
- **チャットとWork・Codexは利用上限が別**: 同じプランでも、チャットとWork・Codexの利用枠は別々に数えられる。OpenAIのサポートに依頼しても上限はリセットされない
- **「常に一番賢い設定を使えばよい」は誤り**: 右に寄せるほど待ち時間が長く、利用枠も早く減る。まずInstantで試し、物足りなければ一段階ずつ上げるのが効率的
- **Proプランでも最上位モデルは無制限ではない**: GPT-6 Proには週単位の上限があり、上限に達すると下位の設定に切り替わる。重要案件の検証用に枠を残しておく
- **「モデル」と「プラン」を混同しない**: 「Plusに入っているのに込み入った質問がうまく処理されない」という相談は、スライダーをInstantのまま使っているケースが多い。またPlusではExtra HighとProは選べない
- **無料・Goプランは日常の文章作成なら十分**: GPT-5.6 Lunaのテキストチャットは事実上無制限で、回数を気にせず使える。ただし深い推論やWork・Codexの最新モデルが必要な業務はPlus以上が前提になる
- **旧モデルに依存したGPTs・ワークフローは早めに動作確認する**: GPT-6への移行自体は旧モデルを廃止しなかったが、OpenAIは2026年に入ってからもGPT-4o系・GPT-5.1系・o3などを順次終了してきた。業務で使うGPTsは、終了予定日が公表される前に現行モデルで動作確認しておく

## 最初の一歩

今使っているChatGPTの画面でモデルピッカーを開き、スライダーがどの位置になっているか、自分のプランでどの段階まで選べるかを確認してみる。次に、いま抱えている複雑な分析タスクを一つ選び、Instantのままの回答とスライダーをHigh寄りに動かした回答を見比べてみる。

## 関連トピック

- [ChatGPTのプラン比較](chatgpt-plan-comparison.md)
- [ChatGPTのエージェント機能(ChatGPT Work・dots)とスケジュールタスク](chatgpt-agent-mode-feature.md)

## 更新履歴

### 2026-11-23: GPT-6世代の構成(チャットはGPT-6 Sol、Work・CodexはGPT-6.2)に合わせて全面改訂
- **内容**: 通常のチャットとChatGPT Work・Codexでモデルが別管理になっている構成を軸にページを全面改訂。チャットのスライダー(Instant〜Extra HighはGPT-6 Sol、ProはGPT-6 Astra土台のGPT-6 Pro)、プラン別に使える段階(PlusはHighまで等)とGPT-6 Proの週上限、2026年11月17日提供開始のGPT-6.2 Astra・Sol(Work・Codex向け、API価格)、Work・Codexで選べる旧世代モデル、Ultrafastを反映。ロールアウト中だった9月時点の記述(Astraへの移行状況、GPT-5.6 Sol中心の比較表、Business上限の件数目安など)を削除し、社内マニュアル用のひな形を追加
- **出典**: [OpenAI Help Center: GPT-6 and other models in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt)、[OpenAI: Introducing GPT-6.2 Astra and Sol](https://openai.com/index/introducing-gpt-6-2-astra-sol/)、[9to5Mac: OpenAI upgrades ChatGPT and Codex with new GPT-6.2 Astra and Sol models(2026年11月17日)](https://9to5mac.com/2026/11/17/openai-upgrades-chatgpt-and-codex-with-new-gpt-6-2-astra-and-sol-models/)、[OpenAI: GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/)

### 2026-09-04: 次世代フラッグシップ「GPT-6 Astra」の発表・ロールアウト開始を反映して最新化
- **内容**: 2026年9月3日に発表された次世代フラッグシップ「GPT-6 Astra」(および上位版「GPT-6 Pro」)の登場を反映。Daybreakプログラム経由の一部組織への先行提供を皮切りに、Plus/Pro/Business/Enterpriseへ数日かけて順次展開中でFree/Goは対象外であること、コンピュータ操作・コーディング・サイバーセキュリティ・科学分野でGPT-5.6 Solを上回るとされる点、サイバーセキュリティ評価が「Critical」域に達しDaybreak管理下に置かれている点、API価格(入力$10/出力$50・100万トークンあたり)とコンテキスト約1.05Mトークンを追記。ロールアウトがまだ進行中でアカウントにより表示が異なりうる旨の注記を各所に追加した。あわせて、2026年8月26日にo3が予定通り終了し、本ページ執筆時点でオプトイン可能な旧世代(レガシー)モデルが事実上なくなったことを反映し、業務シーン別の使い分け表・比較表・プラン別の違いを更新した
- **出典**: [OpenAI: GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/)、[OpenAI Help Center: GPT-5.6 and GPT-6 Pro in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)、[9to5Google: OpenAI launches GPT-6 Astra, 'the world's most intelligent and aligned model' that you can't use just yet](https://9to5google.com/2026/09/03/openai-gpt-6-astra-launch/)、[9to5Mac: OpenAI releasing major upgrade to ChatGPT and Codex with GPT-6 Astra, details here](https://9to5mac.com/2026/09/03/openai-releasing-major-upgrade-to-chatgpt-and-codex-with-gpt-6-astra-details-here/)、[Axios: OpenAI releases new model GPT-6 Astra, says it may represent AGI](https://www.axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman)、[CNBC: OpenAI announces rollout of GPT-6 Astra model](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)、[Bloomberg: OpenAI Launches GPT-6 Astra With Enhanced Cybersecurity Safeguards](https://www.bloomberg.com/news/articles/2026-09-03/openai-rolls-out-gpt-6-astra-model-with-added-cyber-guardrails)、[MarkTechPost: OpenAI Releases GPT-6 Astra: A 1.05M-Context Computer-Use Model Gated Behind a 'Critical' Cyber Threshold](https://www.marktechpost.com/2026/09/03/openai-releases-gpt-6-astra-a-1-05m-context-computer-use-model-gated-behind-a-critical-cyber-threshold/)
- **注記**: OpenAI公式サイト・ヘルプセンターへの直接アクセスができなかったため、検索エンジンのプレビュー経由での参照および複数の第三者情報のクロスチェックに基づく内容。GPT-6 Astraの発表は本ページ執筆日の前日(9月3日)であり、ChatGPT画面への反映は「数日かけて」進行中の段階のため、スライダーの各段階(Instant/Medium/High/Extra High/Pro)が最終的にどこまでAstra系に置き換わるか、Business/Enterpriseの詳細な利用上限などは今後変わる可能性が高い。正確な最新値は契約中のプランの設定画面および[公式料金ページ](https://chatgpt.com/pricing)で要確認

### 2026-08-14: モデル選択の仕組みがスライダー型に変わったことを反映して最新化
- **内容**: 2026年8月6日のアップデートにより、Plus以上ではInstant/Thinkingという別モデル切り替えから、GPT-5.6 Sol1本を軸に「Instant/Medium/High/Extra High/Pro」の推論エフォートをスライダーで指定する方式へ変わったことを反映。Free/GoではGPT-5.6 Lunaが既定モデルとなりテキストチャットが事実上無制限化されたこと、Thinkボタンの追加、Business/EnterpriseはSol/Terra/Lunaを個別設定できる構成であること、API向けのUltrafast(最大14倍速)とセキュリティ特化のGPT-5.6-Cyber(Daybreakプログラム限定)の登場を追記し、業務シーン別の使い分け表・比較表・操作手順・プラン別の違いを全面的に書き換えた
- **出典**: [OpenAI: Improving GPT-5.6 Sol in ChatGPT—and expanding access to GPT-5.6 Luna for free users](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/)、[OpenAI Help Center: GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt)、[9to5Mac: OpenAI updating ChatGPT with a smarter GPT-5.6 Sol and unlimited free chats](https://9to5mac.com/2026/08/06/openai-updating-chatgpt-with-a-smarter-gpt-5-6-sol-and-unlimited-free-chats/)、[TechCrunch: ChatGPT brings unlimited text chats to free users](https://techcrunch.com/2026/08/06/openai-brings-unlimited-chatgpt-text-chats-to-free-users/)、[the-decoder: OpenAI improves GPT-5.6 Sol in ChatGPT and restricts free users to its weakest model](https://the-decoder.com/openai-improves-gpt-5-6-sol-in-chatgpt-and-restricts-free-users-to-its-weakest-model/)、[MacRumors: Free ChatGPT Users Get Unlimited Text Chats and GPT-5.6 Luna](https://www.macrumors.com/2026/08/06/chatgpt-free-unlimited-text-chats/)、[OpenAI: Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed](https://openai.com/index/previewing-ultrafast/)、[TechCrunch: OpenAI introduces 'Ultrafast,' a new mode that makes GPT-5.6 Sol work at 14x the speed](https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/)、[SecurityWeek: OpenAI Unveils New Cybersecurity Model GPT-5.6-Cyber](https://www.securityweek.com/openai-unveils-new-cybersecurity-model-gpt-5-6-cyber/)、[OpenAI: Expanding Daybreak as the Cyber Defense Window Narrows](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/)
- **注記**: OpenAI公式ヘルプセンター・公式ブログへの直接アクセスができなかったため、検索エンジンのプレビュー経由での参照および複数の第三者情報のクロスチェックに基づく内容。特にスライダー統合後の利用回数上限の消費ルール、Business/Enterprise向けの詳細な選択肢はソースにより記述の粒度が異なり、正確な最新値は契約中のプランの設定画面および[公式料金ページ](https://chatgpt.com/pricing)で要確認

### 2026-07-23: GPT-5.6世代へのモデル交代とレガシーモデル終了スケジュールを最新化
- **内容**: 2026年7月9日のGPT-5.6(Sol/Terra/Luna)一般提供開始により、ThinkingとProの実体モデルがGPT-5.5からGPT-5.6 Sol・Sol Proに交代したことを反映。GPT-5.5 Instant Miniへのフォールバック交代(7月6日)、Autoルーターの自動切り替えがThinking週間上限を消費しない仕様、GPT-5.1〜GPT-5.4の順次終了(3月・6月・7月23日)、新設のビジネス向けエージェント「ChatGPT Work」、Proプランの100ドル/200ドルの2階層化を追記
- **出典**: [OpenAI: GPT-5.6: Frontier intelligence that scales with your ambition](https://openai.com/index/gpt-5-6/)、[OpenAI Help Center: GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna)、[OpenAI Help Center: Retiring GPT-4o and other ChatGPT models](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)、[9to5Mac: OpenAI unveils ChatGPT Work agent, GPT-5.6 models now available](https://9to5mac.com/2026/07/09/openai-announcing-the-next-chapter-for-chatgpt-today-watch-here/)、[the-decoder: OpenAI staffer maps out which of GPT-5.6 Sol's five reasoning levels fits which task complexity](https://the-decoder.com/openai-staffer-maps-out-which-of-gpt-5-6-sols-five-reasoning-levels-fits-which-task-complexity/)、[reconn-ai: July 6, 2026 — GPT-5.5 Instant Mini in ChatGPT](https://reconn-ai.com/chatgpt-july-6-2026-gpt-5-5-instant-mini-in-chatgpt)、[ghacks: OpenAI Upgrades GPT-5.5 Instant and Confirms Retirement of o3 and GPT-4.5 Models](https://www.ghacks.net/2026/06/03/openai-upgrades-gpt-5-5-instant-and-confirms-retirement-of-o3-and-gpt-4-5-models/)、[thenextweb: OpenAI's new $100 ChatGPT Pro plan targets Claude Max](https://thenextweb.com/news/openais-new-100-chatgpt-pro-plan-targets-claude-max-with-five-times-the-codex-access)、[note: 【2026年7月版】ChatGPT WorkとはーCodex統合とSitesで何が変わるか](https://note.com/kazu_t/n/nb664dad5f627)、[uravation: ChatGPT Workとは｜できること・料金・使い方【2026年7月】](https://uravation.com/media/chatgpt-work-guide-2026/)
- **注記**: OpenAI公式ヘルプセンター・公式ブログへの直接アクセスができなかったため、検索エンジンのプレビュー経由での参照および複数の第三者情報のクロスチェックに基づく内容。モデル名・利用回数上限・コンテキストサイズは特に変化が速いため、正確な最新値は契約中のプランの設定画面および[公式料金ページ](https://chatgpt.com/pricing)で要確認

### 2026-07-06: 重複ページの統合
- **統合元**: chatgpt-model-comparison.md(本ページをベースに、「モデル」と「プラン」の混同への注意、Codex・エージェントモード・Deep Researchとの関係、シーン別の3段階の判断目安、Goプランでの Thinking 利用手順を統合)
- **出典**: [OpenAI公式ブログ: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)、[OpenAI Help Center: ChatGPT エージェント](https://help.openai.com/ja-jp/articles/11752874-chatgpt-agent)、[OpenAI: Codex](https://openai.com/codex/)、[TechRadar: ChatGPT just made it easier to pick the right model](https://www.techradar.com/ai-platforms-assistants/chatgpt/chatgpt-just-made-it-easier-to-pick-the-right-model-just-like-gemini-does-heres-when-to-use-instant-thinking-or-pro)

### 2026-07-05: 初版執筆
- **内容**: ChatGPTのモデルピッカー(Instant/Thinking/Pro)の構成、業務シーン別の使い分け、プランごとの利用可否・上限、モデル切り替えの画面操作手順、レガシーモデルの終了スケジュールを整理
- **出典**: [OpenAI Help Center: GPT-5.5 in ChatGPT](https://help.openai.com/en/articles/11909943-gpt-55-in-chatgpt)、[OpenAI Help Center: ChatGPT Business - Models & Limits](https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits)、[OpenAI Help Center: ChatGPT Enterprise and Edu - Models & Limits](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-and-edu-models-limits)、[OpenAI Help Center: Legacy Model Access for Enterprise and Edu Users](https://help.openai.com/en/articles/11954883-legacy-model-access-for-enterprise-and-edu-users)、[OpenAI Help Center: Retiring GPT-4o and other ChatGPT models](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)、[OpenAI公式ブログ: Retiring GPT-4o, GPT-4.1, GPT-4.1 mini, and OpenAI o4-mini in ChatGPT](https://openai.com/index/retiring-gpt-4o-and-older-models/)、[GIGAZINE: 'GPT-5.5 Instant' is now available](https://gigazine.net/gsc_news/en/20260507-openai-gpt-5-5-instant/)、[9to5Mac: PSA: OpenAI will soon remove several models from ChatGPT](https://9to5mac.com/2026/01/30/psa-openai-will-remove-several-models-from-chatgpt-next-month/)、[knightli.com: GPT-5.5 Instant vs Thinking vs Pro](https://knightli.com/en/2026/05/07/gpt-5-5-instant-thinking-pro-differences/)、[genai-ai.co.jp: 【2026年7月最新】ChatGPTのバージョン一覧](https://genai-ai.co.jp/ai-kanri/blog/cc-chatgpt-version-guide/)
- **注記**: OpenAI公式ヘルプセンター(help.openai.com)への直接アクセスができなかったため、検索エンジンのプレビュー経由での参照および複数の第三者情報のクロスチェックに基づく内容。モデル名・利用回数上限は特に変化が速いため、正確な最新値は契約中のプランの設定画面および[公式料金ページ](https://chatgpt.com/pricing)で要確認
