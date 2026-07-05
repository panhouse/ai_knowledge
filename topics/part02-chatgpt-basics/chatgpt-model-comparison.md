---
title: ChatGPTのモデル比較
part: 2
chapter: 第1章 ChatGPTの概要
tags: [ChatGPT, モデル選択, GPT-5]
created: 2026-07-05
updated: 2026-07-05
---

# ChatGPTのモデル比較

## これは何か

ChatGPTの画面には「Instant」「Thinking」「Pro」といった、契約プランとは別の「モデル選択メニュー」がある。プラン(Free/Go/Plus/Pro/Business/Enterprise)が「いくら払っていくつ使えるか」という契約の話であるのに対し、モデルは「同じ会話の中で、どの頭脳を使って答えを作らせるか」という話。ここを理解していないと、簡単な質問にわざわざ時間のかかる高精度モデルを使って待たされたり、逆に複雑な分析を軽量モデルにやらせて浅い答えしか返ってこなかったりする。

なお料金プランそのものの違いは[ChatGPTのプラン比較](chatgpt-plan-comparison.md)で扱っているので、本ページはプラン内で選べる「モデル・モード」の使い分けに絞って解説する。

## 仕組み・背景

OpenAIは2025年半ばに、それまで乱立していたGPT系(GPT-4o、GPT-4.1など)とo系推論モデル(o3、o4-miniなど)を「GPT-5」に統合した。さらに2026年に入ってからも改良版(GPT-5.1〜GPT-5.4)を経て、2026年4月23日には最新版「GPT-5.5」が発表されている。GPT-5.5はコーディング・デバッグ、Web上の調査、データ分析、資料作成、ソフトウェア操作といった実務タスクをより広くこなせるように改良された世代とされる。

2026年7月時点でのモデル選択メニューは、内部的な世代名(GPT-5.5など)を前面に出さず、**「どれだけ深く考えさせるか」という体感で選ばせる作り**になっている。具体的には次の3系統に整理されている。

- **Instant(インスタント)**: GPT-5.5 Instant。即答型。日常的な質問や短い作業に向く、標準の初期設定
- **Thinking(シンキング)**: GPT-5.5 Thinking。回答前に内部で段階的に考える「推論」に時間をかけるモデル。考える深さを Medium(標準)/High(深い)/Extra High(最大、Pro以上限定)の3段階から選べる
- **Pro**: GPT-5.5 Pro。最も精度と安定性を重視した上位モデル。Standard/Extendedの2段階があり、Pro・Business・Enterprise向け

さらに「Instant」使用時に、質問が複雑だとChatGPTが自動的にMedium相当の推論へ切り替える**自動エスカレーション**の設定もある(オン/オフは後述のConfigureから変更可能)。

このほか、コーディングに特化した**Codex**というエージェント(自律的にコードを読み書き・実行してPull Requestまで作成する専用モード。chatgpt.com/codex や対応IDEから利用)や、ブラウザ操作を伴う半自律タスクをこなす**エージェントモード**(入力欄のツールメニューから起動)など、通常の「答えを返す」モデルとは毛色の異なる特殊モードも用意されている。

## 使いどころ・使い分け

| モデル・モード | 実体 | 得意なこと | 向いているタスク例 |
|---|---|---|---|
| Instant | GPT-5.5 Instant | 速い・自然な受け答え | メール・チャット文面の下書き、要約、簡単な質問、雑談的な壁打ち |
| Thinking - Medium | GPT-5.5 Thinking(標準推論) | ある程度筋道立てた検討 | 企画書のたたき台、複数条件を踏まえた比較検討 |
| Thinking - High | GPT-5.5 Thinking(高推論) | 込み入った多段階の思考 | 複雑なデータ分析、コードの設計・デバッグ、契約書など長文の精査 |
| Thinking - Extra High(Pro以上) | GPT-5.5 Thinking(最大推論) | 非常に難しい問題への粘り強い検討 | 込み入った戦略立案、専門性の高い調査・検証 |
| Pro Standard / Extended(Pro・Business・Enterprise) | GPT-5.5 Pro | 最高水準の精度・安定性、長時間タスクへの耐性 | 重要な意思決定の裏取り、ミスが許されない資料の最終チェック |
| Codex(chatgpt.com/codex 等) | GPT-5.3 Codex等コーディング特化モデル | コードの自動修正・実行・PR作成 | 開発者向けの本格的なコーディング作業 |
| エージェントモード | GPT-5.5ベースの自律エージェント | ブラウザ操作を伴う半自律タスク | 複数サイトを横断した情報収集、フォーム入力、予約などの代行 |
| レガシーモデル(Configureで有効化した場合のみ) | GPT-4oなど旧世代(移行期間限定) | 過去のプロンプト資産との互換性 | 旧モデル前提で作り込んだ業務フローの一時的な継続利用のみ |

判断の目安はシンプルで、「**すぐ返事が欲しい・内容が軽い→Instant**」「**込み入っている・裏取りが必要・コードを書く→Thinking(High寄り)**」「**失敗が許されない重要な一発勝負→Pro**」の3段階で考えればよい。Deep Research(高度な調査レポート機能)のような専用機能を使う場合は、モデル選択とは別枠でその機能自体を呼び出す形になる。

## 実務での使い方

### モデルの切り替え手順(2026年7月時点、画面は変更されうるため目安)

1. ChatGPT(chatgpt.com またはアプリ)でチャット画面を開く
2. 画面上部、入力欄の近くにある**モデル選択メニュー**(現在選択中のモデル名が表示されているボタン)をクリックする
3. 「Instant」「Thinking」「Pro」のタブから選び、Thinking/Proを選んだ場合はさらに推論の深さ(Medium/High/Extra High、またはStandard/Extended)を選ぶ
4. メニュー内の「Configure」から、Instantの自動エスカレーションのオン/オフや、契約プランで許可されていれば旧モデル(レガシーモデル)の表示切り替えができる

### 業務シーン別のおすすめ

| 業務シーン | おすすめモデル |
|---|---|
| 取引先へのメール文面を整える | Instant |
| 会議メモを要約する | Instant(内容が専門的で込み入っていればMedium) |
| 複数案を比較して企画書の骨子を作る | Thinking - Medium〜High |
| 業務用マクロ・簡単なスクリプトを書く | Thinking - High、または開発者ならCodex |
| 契約書や決算資料など、間違いが許されない文書の精査 | Thinking - High、重要度が高ければPro |
| 複数サイトの情報収集や比較表作成を自動化したい | エージェントモード |

### プランによる利用可能モデルの違い(概要)

モデル選択の幅は契約プランによって決まる。詳しい料金・機能の違いは[ChatGPTのプラン比較](chatgpt-plan-comparison.md)を参照してほしいが、モデル選びに直結する点だけ挙げると次の通り。

- **Free**: Instantのみ。しかも5時間あたりの利用回数が厳しく制限され、超過すると自動的に軽量な応答に切り替わる
- **Go**: Instantに加え、入力欄の「+」から「Thinking」を選べば5時間に10回程度までThinkingを試せる
- **Plus**: Instant・Medium・Highを自由に選択可能。業務利用ならこれで大半のタスクをカバーできる
- **Pro / Business / Enterprise**: 上記に加えExtra High、Pro Standard/Extendedまで選択可能。レガシーモデルの利用可否や利用上限もこの層で緩和される

Codexやエージェントモードの利用可否・上限もプランによって段階的に異なる(Plusで基本機能、Proでヘビーユース向けに上限拡大)。

## 注意点・よくある誤解

- **「一番賢いモデル=常に正解」ではない**: Pro系やThinkingの高推論設定は応答が遅く、利用回数の消費も大きい。単純な質問にまで使うと、待ち時間が増えるだけで成果物の質はほとんど変わらないことが多い。まずInstantで試し、物足りなければ一段階ずつ上げるのが効率的。
- **「モデル」と「プラン」を混同しない**: 「Plusに入っているのにThinkingが使えない」といった相談は、実際にはモデル選択メニューでInstantのまま操作していたというケースが多い。プランは「箱の大きさ」、モデルは「箱の中でどれを使うか」と考えると整理しやすい。
- **モデル名・ラインアップは非常に頻繁に変わる**: GPT-5→5.1→5.2…5.5と数か月おきに世代交代しており、旧世代は発表から一定期間(目安90日程度)でレガシー化・提供終了となる。本ページの名称・世代は執筆時点のものであり、実際の画面のメニュー名・選択肢は必ずアプリ内のモデル選択メニューで確認すること。
- **レガシーモデルは期間限定**: 「Configure」で表示できる旧モデルは移行措置であり、いずれ完全に使えなくなる。旧モデル前提のプロンプト・業務フローがある場合は早めにThinking/Pro系への移行を検討する。
- **Codex・エージェントモードは「モデル」というより「専用ツール」**: 同じGPT-5.5系列の技術を使っていても、通常のチャット用モデル選択とは別のUI・別の利用上限で動いている点に注意する。

## 最初の一歩

普段使っているチャット画面でモデル選択メニューを開き、今どのモデル(Instant/Thinking/Proのどれか)が選ばれているかを確認したうえで、直近の複雑な依頼を一つThinking(Medium以上)に切り替えて試してみる。

## 関連トピック

- [ChatGPTのプラン比較](chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: ChatGPTのモデル選択メニュー(Instant/Thinking/Pro)の仕組み、業務シーン別の使い分け、プランによる利用可能モデルの違い、Codex・エージェントモードとの関係を整理
- **出典**: [OpenAI公式ブログ: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/), [OpenAI Help Center: GPT-5.5 in ChatGPT](https://help.openai.com/en/articles/11909943-gpt-5-in-chatgpt), [OpenAI Help Center: Legacy Model Access for Enterprise and Edu Users](https://help.openai.com/en/articles/11954883-legacy-model-access-for-enterprise-and-edu-users), [OpenAI Help Center: ChatGPT Business - Models & Limits](https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits), [TechRadar: ChatGPT just made it easier to pick the right model](https://www.techradar.com/ai-platforms-assistants/chatgpt/chatgpt-just-made-it-easier-to-pick-the-right-model-just-like-gemini-does-heres-when-to-use-instant-thinking-or-pro), [OpenAI Help Center: ChatGPT エージェント](https://help.openai.com/ja-jp/articles/11752874-chatgpt-agent), [OpenAI: Codex](https://openai.com/codex/)
- **注記**: OpenAI公式ヘルプページへの直接アクセスができなかったため、一部の画面上の文言・利用回数上限は複数の第三者情報のクロスチェックに基づく目安。モデル名・選択肢の構成は数か月単位で変わるため、正確な最新情報は必ずChatGPT内の「モデル選択メニュー」と[公式料金ページ](https://chatgpt.com/pricing)で確認すること
