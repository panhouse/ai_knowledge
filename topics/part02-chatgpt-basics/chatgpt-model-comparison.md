---
title: ChatGPTのモデル比較と使い分け
part: 2
chapter: 第1章 ChatGPTの概要
tags: [ChatGPT, モデル比較, GPT, 推論モデル]
created: 2026-07-05
updated: 2026-07-05
---

# ChatGPTのモデル比較と使い分け

## これは何か

ChatGPTの入力欄付近には「モデルピッカー」と呼ばれるモデル選択メニューがあり、応答の速さと推論の深さ(どれだけじっくり考えるか)のバランスを選べる。何となくデフォルトのまま使っていると、複雑な分析や込み入った作業まで一番軽い設定で処理されてしまい、期待した精度が出ないことがある。逆に単純な質問にまで重い設定を使うと応答が遅くなるだけでなく、上位設定に課された利用回数の上限を早く消費してしまう。今ChatGPTで何が選べて、どう使い分けるべきかを整理する。

## 仕組み・背景

- 2025年8月のGPT-5世代導入時、ChatGPTは一時的にモデルピッカーを廃止して自動選択のみにした後、Auto・Fast(Instant)・Thinking・Proという名前付きの選択式ピッカーを復活させた。
- その後モデル自体もGPT-5.3 Instant→GPT-5.4 Thinking/Pro→GPT-5.5という順で世代交代し、2026年5月にGPT-5.5 Instantが全ユーザーのデフォルトモデルになった。
- 2026年6月10日、OpenAIはピッカーの名称をさらに整理し、「モデル名」ではなく「速さ×思考の深さ」を表す設定に統一した。**執筆時点(2026年7月)でChatGPT上に表示される選択肢は、すべてGPT-5.5系列をベースにした以下の6段階になっている。**

| 表示名 | ベースモデル | 位置づけ |
|---|---|---|
| Instant | GPT-5.5 Instant | 素早い応答。全プランで利用可能なデフォルト |
| Medium | GPT-5.5 Thinking(旧称 Thinking Standard) | 標準的な推論 |
| High | GPT-5.5 Thinking(旧称 Thinking Extended) | 踏み込んだ推論 |
| Extra High | GPT-5.5 Thinking(旧称 Thinking Heavy) | 最も重い推論(旧・軽量版のThinking Lightは廃止済み) |
| Pro Standard | GPT-5.5 Pro | Pro契約者向けの最上位、標準推論 |
| Pro Extended | GPT-5.5 Pro | Pro契約者向けの最上位、拡張推論 |

- Plus以上はInstant・Medium・Highの3つを選べる。Extra High・Pro Standard・Pro ExtendedはPro契約者専用。
- 「Instant」を選んでいても、質問が複雑だとChatGPTが自動的にMedium相当まで推論を強めることがある(Auto-switch機能、初期状態はオン)。ただし自動で格上げされるのはInstant→Medium相当までで、High以上・Proへは自動的には上がらない。
- 無料版(Free)はGPT-5.5 Instantを一定回数まで使え、5時間あたりの上限に達すると軽量な「miniモデル」に自動的に切り替わる(プラン別の詳細は[ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)を参照)。
- 旧世代モデルの整理も進んでいる。2026年2月13日にGPT-4o・GPT-4.1・GPT-4.1 mini・OpenAI o4-mini(旧世代の推論特化モデル)がChatGPTから退役し、2026年6月26日にはGPT-4.5も退役した。これにより現在ChatGPT上で選べるのはGPT-5.5系列のみとなっている。
- なお次世代のGPT-5.6(Sol・Terra・Lunaの3モデル構成)は2026年7月時点で発表済みだが、政府関連機関向けの限定プレビュー(API・Codex経由、約20組織限定)にとどまっており、一般のChatGPT利用者はまだ選択できない。数週間以内に一般提供が始まる見込みとアナウンスされているが、正式な提供開始時期・仕様は本ページ執筆時点では未確定。

## 使いどころ・使い分け

| 業務シーン | おすすめの設定 | 理由 |
|---|---|---|
| メール返信の下書き、議事録の要約、簡単な質問応答 | Instant | 応答が速く、日常業務の大半をカバーできる。利用回数の上限も消費しにくい |
| 複数の条件を踏まえた比較検討、文章の校正・構成整理 | Medium | Instantでは浅くなりがちな検討に、ひと呼吸おいた推論を挟んで精度を上げる |
| 込み入ったロジックの整理、資料構成の設計、やや複雑なコード修正 | High | より深い思考ステップが必要な作業向け |
| 複雑な数式を伴う分析、複数資料を横断した調査、大規模なコード設計(Pro限定) | Extra High | 最も重い推論。時間はかかるが精度を最優先したい場面 |
| 長時間かかる調査レポート作成、失敗が許されない重要な意思決定支援、大規模なコード変更(Pro限定) | Pro Standard / Pro Extended | GPT-5.5 Proの最高精度をじっくり時間をかけて引き出す |

判断に迷ったら、基本はInstant+Auto-switchオンのままにしておき、「明らかに込み入っている」「Instantの回答が浅いと感じた」ときだけMedium・Highへ手動で切り替える、という運用が無難。Extra High・Proは利用回数の上限が別立てで管理されるため、日常使いには向かない。

## 実務での使い方

### モデルピッカーの場所

- **Web版**: メッセージ入力欄付近に表示されているモデル名(例: 「Instant」)をクリックすると一覧が開く
- **iOS/Androidアプリ**: 会話画面の上部にモデル名が表示され、タップすると一覧が開く
- 一覧からInstant/Medium/High(Plus以上)、またはExtra High/Pro Standard/Pro Extended(Pro)を選択する

### 自動切り替え(Auto-switch)のオン・オフ

1. モデルピッカーを開く
2. 「Configure」を選択
3. 「Auto-switch to Thinking」の項目でオン・オフを切り替える(オンだと複雑な質問でInstantが自動的にMedium相当まで格上げされる)

### プロンプト例(用途別)

- 「この契約書の第3条を3行で要約して」→ **Instant**で十分
- 「以下の3案について、当社の状況(予算◯◯円・納期◯月)を踏まえてメリット・デメリットを比較し、根拠つきで1案に絞って提案して」→ **Medium**または**High**を明示的に指定
- 「添付の売上データから異常値を検出し、原因の仮説を3つ以上、優先順位付きで提示して」→ **High**または**Extra High**

### 他ツールとの対応(参考)

同じ「速さ重視/精度重視の切り替え」という考え方は他の主要ツールにもある。呼び方が違うだけなので、乗り換え時や併用時の対応付けとして覚えておくと迷わない。

| 概念 | ChatGPT | Gemini | Copilot | Claude |
|---|---|---|---|---|
| 速さ優先モード | Instant | Fast相当のモデル選択 | 「すぐに回答」 | 通常応答(拡張思考オフ) |
| 精度・推論優先モード | Medium/High/Extra High/Pro | Thinking相当のモデル選択 | 「Think Deeper」相当の機能 | 拡張思考(Extended Thinking)オン |

### 料金・上限との関係

Instant/Medium/High/Extra High/Pro Standard/Pro Extendedのどれが選べるか、また何回使えるかはプランによって大きく異なる(Free/Go/Plus/Pro/Business/Enterprise)。プランごとの料金・上限の詳細は[ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)を参照。法人プラン(Business/Enterprise)では、ワークスペース管理者が利用できるモデル・設定を制限している場合もある。

## 注意点・よくある誤解

- **「モデル名」ではなく「効果レベル」表示になった**: 以前の記事にある「GPT-5 Thinkingを選ぶ」「GPT-5.4 Proを使う」といった説明は、今の画面ではそのままでは通用しない。現在はInstant/Medium/High/Extra High/Pro Standard/Pro Extendedという効果レベルで選ぶ。
- **重い設定を常用すると非効率**: High以上は応答時間が伸び、Pro向け設定は利用回数の上限も別立てで管理される。常にExtra High・Proを使うと待ち時間や上限消費でかえって非効率になる。
- **Auto-switchはInstant→Medium相当までしか自動で上がらない**: High・Extra High・Proが必要な精度が求められる作業では、自動任せにせず手動で指定する必要がある。
- **無料版で急に精度が落ちたと感じたら上限超過の可能性**: 5時間あたりの利用上限に達し、軽量なminiモデルにフォールバックしていることが多い。
- **呼称・仕様は非常に頻繁に変わる**: 2025年8月から2026年6月までの間だけでも、モデルピッカーの構成・名称が複数回変更されている。本ページの名称は執筆時点のものであり、実際の画面表示と食い違う場合は都度読み替える。
- **次世代モデル(GPT-5.6)の情報を鵜呑みにしない**: 2026年7月時点では限定プレビュー段階で、一般のChatGPTでは使えない。「もうすぐ使える」という記事を見ても、実際に画面に表示されるまでは自社の利用計画に組み込まない。

## 最初の一歩

次に少し込み入った依頼をするときに、モデルピッカーを開いて試しに「Medium」または「High」を選び、普段の「Instant」との回答の違いを比べてみる。

## 関連トピック

- [ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: ChatGPT上で選べるモデル/効果レベル(Instant/Medium/High/Extra High/Pro Standard/Pro Extended)の違いと業務シーン別の使い分け、Auto-switch機能、モデルピッカーの操作手順、旧モデルの退役状況、次世代GPT-5.6の状況を整理
- **出典**: [OpenAI Help Center: GPT-5.5 in ChatGPT](https://help.openai.com/en/articles/11909943-gpt-55-in-chatgpt)、[TechRadar: ChatGPT just made it easier to pick the right model](https://www.techradar.com/ai-platforms-assistants/chatgpt/chatgpt-just-made-it-easier-to-pick-the-right-model-just-like-gemini-does-heres-when-to-use-instant-thinking-or-pro)、[The Decoder: OpenAI overhauls ChatGPT's model selection](https://the-decoder.com/openai-overhauls-chatgpts-model-selection/)、[TechCrunch: OpenAI releases GPT-5.5 Instant, a new default model for ChatGPT](https://techcrunch.com/2026/05/05/openai-releases-gpt-5-5-instant-a-new-default-model-for-chatgpt/)、[TechCrunch: ChatGPT's model picker is back, and it's complicated](https://techcrunch.com/2025/08/12/chatgpts-model-picker-is-back-and-its-complicated/)、[OpenAI: Retiring GPT-4o, GPT-4.1, GPT-4.1 mini, and OpenAI o4-mini in ChatGPT](https://openai.com/index/retiring-gpt-4o-and-older-models/)、[OpenAI Help Center: Retiring GPT-4o and other ChatGPT models](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)、[cryptobriefing: OpenAI updates ChatGPT model picker for pro users with six new response tiers](https://cryptobriefing.com/openai-chatgpt-model-picker-update/)、[VentureBeat: OpenAI unveils GPT-5.6 Sol, Terra and Luna models](https://venturebeat.com/technology/openai-unveils-gpt-5-6-sol-terra-and-luna-models-but-only-accessible-to-limited-preview-partners-for-now-per-us-gov)、[OpenAI: Previewing GPT-5.6 Sol: a next-generation model](https://openai.com/index/previewing-gpt-5-6-sol/)
- **注記**: OpenAI公式サイト・ヘルプページへの直接アクセスができなかったため、内容はWeb検索結果の複数ソースのクロスチェックに基づく。日付が執筆時点(2026年7月5日)と整合しない情報(一部モデルの退役予定日など)は不確実なため本文には含めていない。正確な最新の画面表示は[ChatGPT公式ヘルプセンター](https://help.openai.com/)で要確認
