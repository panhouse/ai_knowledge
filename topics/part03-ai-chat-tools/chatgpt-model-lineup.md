---
title: ChatGPTのモデル一覧と使い分け
part: 3
chapter: 第1章 プラン・モデルの選び方
tags: [ChatGPT, モデル選択, GPT, 推論モデル, GPT-5.6]
created: 2026-07-05
updated: 2026-07-23
---

# ChatGPTのモデル一覧と使い分け

## これは何か

ChatGPTの画面左上にある「モデルピッカー」(モデル選択メニュー)には、速度・精度・コストのバランスが異なる複数のモデルが並ぶ。デフォルトのまま使い続けても多くの場面で困らないが、複雑な分析やコーディングでは推論に特化したモデルに切り替えるだけで回答の質が大きく変わる。逆に単純な作業に重いモデルを使うと、応答が遅くなるうえ利用回数の上限(レートリミット)を早く消費してしまう。自分のタスクに合ったモデルを選べるようになっておくと、同じ契約プランでもアウトプットの質と使える回数の両方が変わってくる。

## 仕組み・背景

2026年7月23日時点のChatGPTは、日常応答を担う「GPT-5.5 Instant」と、複雑な推論を担う「GPT-5.6」世代(Sol・Terra・Luna)を組み合わせた構成になっている。2025年8月の「GPT-5」登場以降、5.1→5.2→5.3→5.4→5.5→5.6と数か月おきに世代交代しており、モデル名や区分は今後も変わっていく前提で見る必要がある。

モデルピッカーの選択肢自体の骨格(Instant/Thinking/Pro)は変わっていないが、2026年7月9日にGPT-5.6が一般提供開始されたことで、Thinking・Proを選んだときに裏側で動く「頭脳」がGPT-5.5からGPT-5.6 Solに置き換わった。

- **Instant**: GPT-5.5 Instant。応答速度を優先した汎用モデル。全プラン(Freeを含む)のデフォルトで、ほとんどの日常業務はこれで足りる
- **Thinking(Medium/High/Extra High)**: GPT-5.6 Sol。回答を出す前にモデル内部で段階的に「考える」推論(reasoning)モデルで、思考の深さをMedium/High/Extra Highの3段階で調整できる。深くするほど精度は上がるが待ち時間も増える
- **Pro(Standard/Extended)**: GPT-5.6 Sol Pro。最も計算資源を投入する最上位モデル。API仕様ではコンテキスト(一度に読み込める文章量)が約105万(1.05M)トークンまで拡大しており、以前のGPT-5.5世代(約27万トークン)から大幅に広がった(ChatGPTアプリで実際にどこまで使えるかは別途変わる可能性があるため、重要な長文作業の前に公式ヘルプで要確認)。ミスが許されない検討向けだが、Apps・Memory(過去のやり取りの記憶)・Canvas・画像生成など一部のChatGPT機能は実行中に使えない

GPT-5.6にはSolの下に、5.5相当の性能をより低コストで出す**Terra**、最速・最安の**Luna**という下位モデルもあるが、通常のChatGPT会話画面(モデルピッカー)では選べない。TerraとLunaは、後述のCodex(コーディング専用エージェント)や開発者向けAPIから利用する位置づけになっている。

このほかに、次の2種類も押さえておく必要がある。

- **軽量モデル(自動フォールバック)**: 利用回数の上限に達すると、手動では選べない軽量版に自動的に切り替わる仕組みがある。2026年7月6日に「GPT-5.5 Instant Mini」が導入され、それまでの「GPT-5.3 Instant Mini」を置き換えた。モデルピッカーには表示されず、APIやCodexにも影響しない裏側の仕組みなので、「急に回答が単純になった」と感じたら、これが原因のことが多い
- **レガシーモデル**: 旧世代のモデルも、設定で明示的にオンにすれば移行期間中は選択肢に残るが、順次終了が決まっている。2026年2月にGPT-4o・GPT-4.1・GPT-4.1 mini・o4-miniが、3月にGPT-5.1系列(Instant/Thinking/Pro)が、6月上旬にGPT-5.2とGPT-5.3-Codexが、6月26日にGPT-4.5が、そして本ページ執筆時点の7月23日にGPT-5.4がGPT-5.6導入に伴い終了する。o3も2026年8月26日に終了予定であり、この記事執筆時点で「Show additional models」から選べるレガシーモデルはo3のみとなっている

また「Instant」を選んでいても、複雑な質問だと自動的にThinkingへ引き上げる仕組みがあり、ChatGPTでは「Auto」(会話画面では「Latest」とも表示)としてこれをデフォルトの挙動にしている。モデルピッカーの「Configure」からこの自動切り替えのオン・オフを切り替えられる。**自動的にThinkingへ引き上げられた分は、Thinkingの週間利用上限を消費しない**点も実務上のポイントで、上限を消費するのは自分でThinkingを手動選択したときだけである。

なお「モデル」と「プラン」は別の話である点も最初に押さえておきたい。プラン(Free/Go/Plus/Pro/Business/Enterprise)は「いくら払っていくつ使えるか」という契約の話、モデルは「同じ会話の中でどの頭脳に答えを作らせるか」という話で、プランは「箱の大きさ」、モデルは「箱の中でどれを使うか」と考えると整理しやすい。

このほか、通常の「答えを返す」モデルとは毛色の異なる特殊モードとして、次の3つがある。

- **Codex**: コーディングに特化し、自律的にコードを読み書き・実行してPull Requestまで作成する専用エージェント
- **エージェントモード(ChatGPT agent)**: ブラウザ操作を伴う半自律タスクをこなす機能。2025年に別サービスだったOperatorが統合され、正式名称は「ChatGPT agent」だが、入力欄のツールメニュー上では引き続き「エージェントモード」として選べる
- **ChatGPT Work**: 2026年7月9日に新設された、業務成果物(表計算・スライド・文書・簡易Webページなど)を仕上げるところまで担うビジネス向けエージェント。GPT-5.6とCodexの技術基盤の上に構築されている

2026年7月9日にはデスクトップアプリも刷新され、「Chat」「Work」「Codex」の3モードに再編されている。Deep Research(高度な調査レポート機能)のような専用機能も、モデル選択とは別枠でその機能自体を呼び出す形になる点は変わらない。

## 使いどころ・使い分け

### 業務シーン別の選び方

| 業務シーン | 向いているモデル | 理由 |
|---|---|---|
| メール・チャット文面の作成、要約、雑談的な壁打ち | GPT-5.5 Instant | 待ち時間がほぼなく、多くのメッセージを回せる。デフォルトのままでよい |
| 大量の問い合わせ下書きを次々にこなす | GPT-5.5 Instant(上限到達後はGPT-5.5 Instant Miniに自動切替) | 品質より処理件数のスピードが重要な場面 |
| 複雑な数値分析、契約書などの長文精読、多段階の論理展開が必要な企画書 | Thinking(Medium〜High、実体はGPT-5.6 Sol) | 内部で考える時間を確保することで見落としが減る |
| プログラムのコード生成・デバッグ | Thinking(High以上、実体はGPT-5.6 Sol)/Codex | コードは一発で正解を出しにくく、推論過程の深さが精度に直結する。自律的に大量のコーディングを任せたい場合はChatGPTの汎用モデルではなく、コーディング特化のCodexの利用も検討する |
| 経営判断に関わる調査、法務・財務など誤りが許されない検討 | Pro(実体はGPT-5.6 Sol Pro) | 最も精度が高いが、Apps・Memory・Canvas・画像生成が使えない点に注意 |
| 複数サイトを横断した情報収集、フォーム入力・予約などの代行 | エージェントモード(ChatGPT agent) | ブラウザ操作を伴う半自律タスクを任せられる(モデルピッカーではなく入力欄のツールメニューから起動) |
| 資料・簡易Webページなど「完成品」まで一気に仕上げたい業務タスク | ChatGPT Work | ゴールを渡すと表計算・スライド・文書・簡易サイトなどの成果物として返してくれる新しいビジネス向けエージェント(2026年7月導入) |
| 過去のGPTsやワークフローが旧モデル前提で作られている | レガシーモデル(移行期間中のo3のみ) | 挙動が変わると困る場合の橋渡し。o3も2026年8月26日に終了予定のため早めに新モデルへの移行確認を |

判断の目安はシンプルで、「**すぐ返事が欲しい・内容が軽い→Instant**」「**込み入っている・裏取りが必要・コードを書く→Thinking(High寄り)**」「**失敗が許されない重要な一発勝負→Pro**」の3段階で考えればよい。迷ったら「Auto」に任せてもよいが、社内ルールで思考の深さを固定したい場合は手動選択に切り替える。

### 比較表(速度・精度・コスト)

| モデル | 速度 | 精度・推論力 | 主なコスト面の制約 | 主な利用可能プラン |
|---|---|---|---|---|
| Instant(GPT-5.5 Instant) | 最速 | 標準 | Free/Goは数時間ごとの回数制限あり。上限到達でGPT-5.5 Instant Miniに自動切替 | Free/Go/Plus/Pro/Business/Enterprise全て |
| Thinking Medium/High/Extra High(実体はGPT-5.6 Sol) | 数秒〜数十秒の思考時間 | 高い(段階を上げるほど精度も待ち時間も増加) | Plus以上で利用可。5時間あたりの上限はプランと段階で変動(Plusは目安十数〜100件程度)。Businessは週3,000件程度の目安 | Plus/Pro/Business/Enterprise |
| Pro Standard/Extended(実体はGPT-5.6 Sol Pro) | 最も遅い(場合により数分) | 最高精度、API仕様でコンテキスト約1.05Mトークン | Pro/Business/Enterpriseの一部。Businessは月十数件程度が目安 | Pro/Business/Enterpriseの一部 |
| Terra・Luna(GPT-5.6の下位モデル) | Lunaが最速・最安 | Terraは5.5相当をより低コストで、Lunaは簡易タスク向け | 通常のモデルピッカーでは選択不可。Codex・APIから利用 | Codex/API(プランにより異なる) |
| GPT-5.5 Instant Mini(自動フォールバック) | 非常に高速 | Instantより簡易 | 手動選択不可。上限到達時に自動適用される裏側の仕組み | 全プラン共通 |
| レガシーモデル(o3) | やや遅い(推論モデル) | 旧世代相当 | 設定でオプトインが必要。2026年8月26日に終了予定 | Plus/Pro/Business/Enterprise(管理者許可制) |

## 実務での使い方

### モデルの切り替え手順(Web版)

1. チャット画面左上のモデル名(例:「Auto」または「ChatGPT」)をクリック
2. ドロップダウンから「Auto」「Instant」「Thinking」「Pro」のいずれかを選ぶ(Proが表示されるのはProプラン以上の契約者、または管理者がProを許可した法人ワークスペース)
3. Thinking/Proを選んだ場合、同じメニューの「Configure」(歯車アイコン)から思考の深さ(Medium/High/Extra High、またはStandard/Extended)を指定できる
4. 「Configure」内の「Auto-switch to Thinking」のオン・オフで、Instant使用中に複雑な質問を自動的にThinkingへ引き上げるかどうかを設定できる。自動切り替え分はThinkingの週間上限を消費しない

### モバイルアプリでの切り替え

チャット画面上部のモデル名をタップすると同様のメニューが開く。基本操作はWeb版と同じ。

### 旧モデルを使いたい場合

設定(Settings)→General→「Show additional models」をオンにすると、o3などのレガシーモデルがピッカーに表示される。ただし個別モデルには終了予定日が公表されており、恒久的な選択肢ではない点に注意する(2026年7月23日時点で選べるレガシーモデルはo3のみ)。

### プランによる違い(モデル選択の観点)

- **Free**: モデルピッカーなし。常にGPT-5.5 Instant(上限超過でGPT-5.5 Instant Miniへ自動切替)
- **Go(月額8ドル程度)**: Instant中心。GPT-5.6世代のThinking(Sol/Terra/Luna)には非対応で、GPT-5.5世代のモデルにとどまる。Thinkingは回数を絞って利用可(入力欄の「+」から選択)
- **Plus(月額20ドル)**: Instant・Thinking(GPT-5.6 Sol/Terra/Luna)をフル活用可(Proは非対応)
- **Pro(月額100ドル/200ドル)**: 2026年4月に100ドルの中間プランが新設され、200ドルプランとの違いは主に利用量上限(100ドルはPlusの5倍、200ドルは20倍が目安)。モデルの利用可否自体はInstant・Thinking・Proともに両プランで同じ
- **Business/Enterprise**: Instantはほぼ無制限、Thinkingも週数千件規模まで利用可。Proの可否は管理者のワークスペース設定による

Codex・エージェントモード・ChatGPT Workの利用可否・上限もプランによって段階的に異なる(Plusで基本機能、Pro/Businessでヘビーユース向けに上限拡大)。プランごとの料金・機能・ガバナンスの全体像は[ChatGPTのプラン比較](chatgpt-plan-comparison.md)を参照。本ページはモデル選びに絞って解説する。

### コピペで使える例(モデルの実力を引き出すプロンプトの一言)

Thinking/Proに切り替えるだけでなく、プロンプト内でも「じっくり検討してほしい」旨を明示すると、思考ステップを増やす方向に働きやすい。

```
このプロンプトは複数の前提条件を比較検討する必要があります。
結論を急がず、以下の手順で考えてください。
1. 論点を洗い出す
2. それぞれの論点についてメリット・デメリットを整理する
3. 最後に総合的な結論と根拠を述べる
```

## 注意点・よくある誤解

- **モデル名・区分は数か月おきに変わる**: GPT-5登場(2025年8月)以降、5.1〜5.6まで短いスパンで世代交代しており、Instant/Thinking/Proの名称や段階数自体は維持されつつも、裏側で動く実体モデル(GPT-5.5→GPT-5.6 Sol等)が入れ替わっている。本ページの数値・名称は執筆時点の目安であり、実際の画面表示を都度確認する
- **「常に一番賢いモデルを使えばよい」は誤り**: Thinking/Proは待ち時間が長く、利用回数の上限も早く消費する。日常的なやり取りはInstantのままで十分なことが多い。まずInstantまたはAutoで試し、物足りなければ一段階ずつ上げるのが効率的
- **「モデル」と「プラン」を混同しない**: 「Plusに入っているのにThinkingが使えない」といった相談は、実際にはモデルピッカーでInstantのまま操作していたというケースが多い。契約プランとモデル選択は別の階層の話
- **Goプランは最新の推論モデルには対応しない**: GoはGPT-5.5世代までで、GPT-5.6 Sol/Terra/Lunaは使えない。込み入った分析やコーディングに使うならPlus以上が前提になる
- **Codex・エージェントモード・ChatGPT Workは「モデル」というより「専用ツール」**: 同じGPT-5.6系列の技術を使っていても、通常のチャット用モデル選択とは別のUI・別の利用上限で動いている点に注意する。特にChatGPT Workは2026年7月に新設されたばかりで、Codex(コーディング専用)・エージェントモード(ブラウザ操作)との役割の違いを混同しやすい
- **Proモデルは一部機能が使えない**: Apps・Memory・Canvas・画像生成などがPro実行中は利用できない場合がある。これらの機能が必要ならInstant/Thinkingに切り替える
- **利用上限に達すると自動的に別モデルへ切り替わる**: 「急に回答の質が落ちた」と感じたら、上限到達でGPT-5.5 Instant Miniなどの軽量版に切り替わっている可能性がある。画面上部のモデル表示を確認する
- **レガシーモデルは「いつか消える」前提で使う**: 過去のGPTsやワークフローが旧モデルに依存している場合、公表されている終了予定日までに新モデルでの動作確認を済ませておく。2026年に入ってからだけでもGPT-4o系(2月)、GPT-5.1系(3月)、GPT-5.2・GPT-5.3-Codex(6月)、GPT-4.5(6月)、GPT-5.4(7月)と、ほぼ毎月のように何らかのモデルが終了している
- **無料プランはそもそも選択肢がない**: 精度が必要な業務利用を無料プランで行うのは選択肢の面で無理があるため、Plus以上への移行を検討する

## 最初の一歩

今使っているChatGPTの画面でモデルピッカーを開き、「Auto」になっているか、手動でモデルを固定しているかを確認してみる。次に、いま抱えている複雑な分析タスクを一つ選び、Instant(またはAuto)のままの回答とThinkingに切り替えた回答を見比べてみる。

## 関連トピック

- [ChatGPTのプラン比較](chatgpt-plan-comparison.md)
- [ChatGPTのエージェント機能(ChatGPT Agent)とスケジュールタスク(Tasks)](chatgpt-agent-mode-feature.md)

## 更新履歴

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
