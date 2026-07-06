---
title: ChatGPTのモデル一覧と使い分け
part: 2
chapter: 第1章 ChatGPTの概要
tags: [ChatGPT, モデル選択, GPT, 推論モデル, GPT-5]
created: 2026-07-05
updated: 2026-07-06
---

# ChatGPTのモデル一覧と使い分け

## これは何か

ChatGPTの画面左上にある「モデルピッカー」(モデル選択メニュー)には、速度・精度・コストのバランスが異なる複数のモデルが並ぶ。デフォルトのまま使い続けても多くの場面で困らないが、複雑な分析やコーディングでは推論に特化したモデルに切り替えるだけで回答の質が大きく変わる。逆に単純な作業に重いモデルを使うと、応答が遅くなるうえ利用回数の上限(レートリミット)を早く消費してしまう。自分のタスクに合ったモデルを選べるようになっておくと、同じ契約プランでもアウトプットの質と使える回数の両方が変わってくる。

## 仕組み・背景

2026年7月時点のChatGPTは、GPT-5.5系列のモデルを中心に、用途別に大きく3つの系統で構成されている。GPT-5系列は2025年8月の「GPT-5」登場以降、5.1→5.2→5.3→5.4→5.5と数か月おきに世代交代しており、モデル名やモード区分は今後も変わっていく前提で見る必要がある。

- **GPT-5.5 Instant**: 応答速度を優先した汎用モデル。全プラン(Freeを含む)のデフォルト。ほとんどの日常業務はこれで足りる
- **GPT-5.5 Thinking**: 回答を出す前にモデル内部で段階的に「考える」推論(reasoning)モデル。思考の深さをMedium/High/Extra Highの3段階で調整でき、深くするほど精度は上がるが待ち時間も増える
- **GPT-5.5 Pro**: 最も計算資源を投入する最上位モデル。Standard/Extendedの2段階があり、コンテキスト(一度に読み込める文章量)も272Kトークンと広い。ミスが許されない検討向けだが、Apps・Memory(過去のやり取りの記憶)・Canvas・画像生成など一部のChatGPT機能は実行中に使えない

このほかに、次の2種類も押さえておく必要がある。

- **軽量モデル(自動フォールバック)**: 利用回数の上限に達すると、手動では選べない軽量版(通称mini)に自動的に切り替わる仕組みがある。「急に回答が単純になった」と感じたら、これが原因のことが多い
- **レガシーモデル**: GPT-4o・GPT-4.1・o3など旧世代のモデルも、設定で明示的にオンにすれば移行期間中は選択肢に残る。ただし順次終了が決まっており、2026年2月にGPT-4o・GPT-4.1・GPT-4.1 mini・o4-miniが、2026年6月にGPT-4.5がすでに終了、o3も2026年8月26日に終了予定となっている

また「Instant」を選んでいても、複雑な質問だと自動的にThinkingへ引き上げる「Auto-switch to Thinking」という機能があり、モデルピッカーの「Configure」からオン・オフを切り替えられる。

なお「モデル」と「プラン」は別の話である点も最初に押さえておきたい。プラン(Free/Go/Plus/Pro/Business/Enterprise)は「いくら払っていくつ使えるか」という契約の話、モデルは「同じ会話の中でどの頭脳に答えを作らせるか」という話で、プランは「箱の大きさ」、モデルは「箱の中でどれを使うか」と考えると整理しやすい。

このほか、通常の「答えを返す」モデルとは毛色の異なる特殊モードとして、コーディングに特化した**Codex**(自律的にコードを読み書き・実行してPull Requestまで作成する専用エージェント。chatgpt.com/codex や対応IDEから利用)と、ブラウザ操作を伴う半自律タスクをこなす**エージェントモード**(入力欄のツールメニューから起動)がある。Deep Research(高度な調査レポート機能)のような専用機能も、モデル選択とは別枠でその機能自体を呼び出す形になる。

## 使いどころ・使い分け

### 業務シーン別の選び方

| 業務シーン | 向いているモデル | 理由 |
|---|---|---|
| メール・チャット文面の作成、要約、雑談的な壁打ち | GPT-5.5 Instant | 待ち時間がほぼなく、多くのメッセージを回せる。デフォルトのままでよい |
| 大量の問い合わせ下書きを次々にこなす | GPT-5.5 Instant(上限到達後は軽量版に自動切替) | 品質より処理件数のスピードが重要な場面 |
| 複雑な数値分析、契約書などの長文精読、多段階の論理展開が必要な企画書 | GPT-5.5 Thinking(Medium〜High) | 内部で考える時間を確保することで見落としが減る |
| プログラムのコード生成・デバッグ | GPT-5.5 Thinking(High以上) | コードは一発で正解を出しにくく、推論過程の深さが精度に直結する。自律的に大量のコーディングを任せたい場合はChatGPTの汎用モデルではなく、コーディング特化のCodex系エージェント製品の利用も検討する |
| 経営判断に関わる調査、法務・財務など誤りが許されない検討 | GPT-5.5 Pro | 最も精度が高いが、Apps・Memory・Canvas・画像生成が使えない点に注意 |
| 複数サイトを横断した情報収集、フォーム入力・予約などの代行 | エージェントモード | ブラウザ操作を伴う半自律タスクを任せられる(モデルピッカーではなく入力欄のツールメニューから起動) |
| 過去のGPTsやワークフローがGPT-4o等の旧モデル前提で作られている | レガシーモデル(移行期間中のみ) | 挙動が変わると困る場合の橋渡し。順次廃止されるため早めに新モデルへの移行確認を |

判断の目安はシンプルで、「**すぐ返事が欲しい・内容が軽い→Instant**」「**込み入っている・裏取りが必要・コードを書く→Thinking(High寄り)**」「**失敗が許されない重要な一発勝負→Pro**」の3段階で考えればよい。

### 比較表(速度・精度・コスト)

| モデル | 速度 | 精度・推論力 | 主なコスト面の制約 | 主な利用可能プラン |
|---|---|---|---|---|
| GPT-5.5 Instant | 最速 | 標準 | Free/Goは5時間ごとの回数制限あり。Plus/Goは3時間ごと160件程度で軽量版に自動切替 | Free/Go/Plus/Pro/Business/Enterprise全て |
| GPT-5.5 Thinking(Medium/High/Extra High) | 数秒〜数十秒の思考時間 | 高い(段階を上げるほど精度も待ち時間も増加) | Plus以上で利用可。Businessは週3,000件程度の目安 | Plus/Pro/Business/Enterprise |
| GPT-5.5 Pro(Standard/Extended) | 最も遅い(場合により数分) | 最高精度、コンテキスト272K | Proプラン中心。法人プランは管理者のワークスペース設定による | Pro/Business/Enterpriseの一部 |
| 軽量モデル(自動フォールバック) | 非常に高速 | Instantより簡易 | 手動選択不可。上限到達時に自動適用される裏側の仕組み | 全プラン共通 |
| レガシーモデル(o3・GPT-4.1等) | モデルにより異なる | 旧世代相当 | 設定でオプトインが必要。順次終了予定(o3は2026年8月26日終了予定) | Plus/Pro/Business/Enterprise(管理者許可制) |

## 実務での使い方

### モデルの切り替え手順(Web版)

1. チャット画面左上のモデル名(例:「ChatGPT 5.5」)をクリック
2. ドロップダウンから「Instant」「Thinking」「Pro」のいずれかを選ぶ(Proが表示されるのはProプラン以上の契約者、または管理者がProを許可した法人ワークスペース)
3. Thinking/Proを選んだ場合、同じメニューの「Configure」(歯車アイコン)から思考の深さ(Medium/High/Extra High、またはStandard/Extended)を指定できる
4. 「Configure」内の「Auto-switch to Thinking」のオン・オフで、Instant使用中に複雑な質問を自動的にThinkingへ引き上げるかどうかを設定できる

### モバイルアプリでの切り替え

チャット画面上部のモデル名をタップすると同様のメニューが開く。基本操作はWeb版と同じ。

### 旧モデルを使いたい場合

設定(Settings)→General→「Show additional models」をオンにすると、o3やGPT-4.1などのレガシーモデルがピッカーに表示される。ただし個別モデルには終了予定日が公表されており、恒久的な選択肢ではない点に注意する。

### プランによる違い(モデル選択の観点)

- **Free**: モデルピッカーなし。常にGPT-5.5 Instant(上限超過で軽量版へ自動切替)
- **Go**: Instant中心。Thinkingは回数を絞って利用可(入力欄の「+」から選択、5時間あたり10回程度が目安)
- **Plus**: Instant・Thinkingをフル活用可(Proは非対応)
- **Pro**: Instant・Thinking・Proすべて選択可。上限も大幅に緩い
- **Business/Enterprise**: Instantはほぼ無制限、Thinkingも週数千件規模まで利用可。Proの可否は管理者のワークスペース設定による

Codexやエージェントモードの利用可否・上限もプランによって段階的に異なる(Plusで基本機能、Proでヘビーユース向けに上限拡大)。プランごとの料金・機能・ガバナンスの全体像は[ChatGPTのプラン比較](chatgpt-plan-comparison.md)を参照。本ページはモデル選びに絞って解説する。

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

- **モデル名・効果レベルの区分は数か月おきに変わる**: GPT-5登場(2025年8月)以降、短いスパンで世代交代しており、Instant/Thinking/Proの名称や段階数も変化してきた。本ページの数値・名称は執筆時点の目安であり、実際の画面表示を都度確認する
- **「常に一番賢いモデルを使えばよい」は誤り**: Thinking/Proは待ち時間が長く、利用回数の上限も早く消費する。日常的なやり取りはInstantのままで十分なことが多い。まずInstantで試し、物足りなければ一段階ずつ上げるのが効率的
- **「モデル」と「プラン」を混同しない**: 「Plusに入っているのにThinkingが使えない」といった相談は、実際にはモデルピッカーでInstantのまま操作していたというケースが多い。契約プランとモデル選択は別の階層の話
- **Codex・エージェントモードは「モデル」というより「専用ツール」**: 同じGPT-5.5系列の技術を使っていても、通常のチャット用モデル選択とは別のUI・別の利用上限で動いている点に注意する
- **Proモデルは一部機能が使えない**: Apps・Memory・Canvas・画像生成などがPro実行中は利用できない場合がある。これらの機能が必要ならInstant/Thinkingに切り替える
- **利用上限に達すると自動的に別モデルへ切り替わる**: 「急に回答の質が落ちた」と感じたら、上限到達で軽量版に切り替わっている可能性がある。画面上部のモデル表示を確認する
- **レガシーモデルは「いつか消える」前提で使う**: 過去のGPTsやワークフローが旧モデルに依存している場合、公表されている終了予定日までに新モデルでの動作確認を済ませておく
- **無料プランはそもそも選択肢がない**: 精度が必要な業務利用を無料プランで行うのは選択肢の面で無理があるため、Plus以上への移行を検討する

## 最初の一歩

今使っているChatGPTの画面でモデルピッカーを開き、「Configure」から現在の思考レベル設定とAuto-switchのオン・オフを確認してみる。次に、いま抱えている複雑な分析タスクを一つ選び、Instantのままの回答とThinkingに切り替えた回答を見比べてみる。

## 関連トピック

- [ChatGPTのプラン比較](chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-06: 重複ページの統合
- **統合元**: chatgpt-model-comparison.md(本ページをベースに、「モデル」と「プラン」の混同への注意、Codex・エージェントモード・Deep Researchとの関係、シーン別の3段階の判断目安、Goプランでの Thinking 利用手順を統合)
- **出典**: [OpenAI公式ブログ: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)、[OpenAI Help Center: ChatGPT エージェント](https://help.openai.com/ja-jp/articles/11752874-chatgpt-agent)、[OpenAI: Codex](https://openai.com/codex/)、[TechRadar: ChatGPT just made it easier to pick the right model](https://www.techradar.com/ai-platforms-assistants/chatgpt/chatgpt-just-made-it-easier-to-pick-the-right-model-just-like-gemini-does-heres-when-to-use-instant-thinking-or-pro)

### 2026-07-05: 初版執筆
- **内容**: ChatGPTのモデルピッカー(Instant/Thinking/Pro)の構成、業務シーン別の使い分け、プランごとの利用可否・上限、モデル切り替えの画面操作手順、レガシーモデルの終了スケジュールを整理
- **出典**: [OpenAI Help Center: GPT-5.5 in ChatGPT](https://help.openai.com/en/articles/11909943-gpt-55-in-chatgpt)、[OpenAI Help Center: ChatGPT Business - Models & Limits](https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits)、[OpenAI Help Center: ChatGPT Enterprise and Edu - Models & Limits](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-and-edu-models-limits)、[OpenAI Help Center: Legacy Model Access for Enterprise and Edu Users](https://help.openai.com/en/articles/11954883-legacy-model-access-for-enterprise-and-edu-users)、[OpenAI Help Center: Retiring GPT-4o and other ChatGPT models](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)、[OpenAI公式ブログ: Retiring GPT-4o, GPT-4.1, GPT-4.1 mini, and OpenAI o4-mini in ChatGPT](https://openai.com/index/retiring-gpt-4o-and-older-models/)、[GIGAZINE: 'GPT-5.5 Instant' is now available](https://gigazine.net/gsc_news/en/20260507-openai-gpt-5-5-instant/)、[9to5Mac: PSA: OpenAI will soon remove several models from ChatGPT](https://9to5mac.com/2026/01/30/psa-openai-will-remove-several-models-from-chatgpt-next-month/)、[knightli.com: GPT-5.5 Instant vs Thinking vs Pro](https://knightli.com/en/2026/05/07/gpt-5-5-instant-thinking-pro-differences/)、[genai-ai.co.jp: 【2026年7月最新】ChatGPTのバージョン一覧](https://genai-ai.co.jp/ai-kanri/blog/cc-chatgpt-version-guide/)
- **注記**: OpenAI公式ヘルプセンター(help.openai.com)への直接アクセスができなかったため、検索エンジンのプレビュー経由での参照および複数の第三者情報のクロスチェックに基づく内容。モデル名・利用回数上限は特に変化が速いため、正確な最新値は契約中のプランの設定画面および[公式料金ページ](https://chatgpt.com/pricing)で要確認
