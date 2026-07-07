---
title: "ChatGPTの音声(Advanced Voice Mode)機能"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [ChatGPT, 音声, Advanced Voice Mode, 音声会話, 語学学習, マルチモーダル]
created: 2026-07-06
updated: 2026-07-06
---

# ChatGPTの音声(Advanced Voice Mode)機能

## これは何か

移動中や作業中は、画面を見て文字を打つこと自体が面倒でChatGPTを開かない、という機会損失が起きがちである。「音声モード(Advanced Voice Mode、高度な音声モード)」は、テキストを一切打たずに話しかけるだけでChatGPTと自然な会話ができる機能で、感情や間の取り方まで再現された音声で、電話で人と話すような感覚でやり取りできる点が最大の特徴になる。語学練習の相手、運転中・家事中の壁打ち相手、資料を見せながらの質問など、「画面に文字を打てない/打ちたくない」場面での活用を想定した機能である。

## 仕組み・背景

### 「音声認識+読み上げ」から「音声そのものを理解するモデル」へ

初期のChatGPTの音声会話は、①音声をテキストに変換(音声認識)→②テキストでChatGPTが応答を生成→③その文章を読み上げる(音声合成)、という3段階の処理を裏で直列に行っていた。この方式では、話し方の抑揚・間・感情といった「声に乗る情報」がテキスト変換の時点で失われてしまい、返ってくる声も機械的になりやすかった。

2024年に登場した「Advanced Voice Mode」は、GPT-4o以降のモデルが音声データを直接理解し、直接音声で応答を生成するネイティブなマルチモーダル方式に切り替わっている。テキストに変換する工程を経ないため、応答までの遅延が2〜3秒程度まで短縮され、話者の感情(急いでいる、困っている等)を汲み取った抑揚のある返答や、笑い声・ため息といった自然な相槌も表現できるようになった。会話の途中で話者が割り込んで話しても、ChatGPT側が発話を止めて聞き直す「割り込み(interrupt)」にも対応している。

音声だけでなく、スマートフォンのカメラや画面共有を組み合わせることもできる。カメラを向けながら「これは何?」と尋ねたり、資料を画面共有しながら「この表の3行目を説明して」と頼んだりする使い方が可能で、音声・映像・テキストを横断した会話が成立する。

## 使いどころ・使い分け

| 場面 | 音声モード | 通常のテキストチャット |
|---|---|---|
| 移動中・運転中・家事をしながらの相談 | 向く(画面操作なしで完結) | 不向き(操作に手が取られる) |
| 語学の発音練習・ロールプレイ会話 | 向く(発音矯正・アクセント切り替えに対応) | 不向き(声に出す練習にならない) |
| 込み入った資料の作成・長文の推敲 | 不向き(出力を目で確認・編集する作業に弱い) | 向く(Canvasなど編集機能と相性が良い) |
| 咄嗟のブレインストーミング・壁打ち | 向く(テンポよく会話できる) | 向く場合もある(整理しながら書きたい人向け) |
| 込み入った数式・コードの確認 | 不向き(音声では細部が伝わりにくい) | 向く |
| ながら作業での情報収集(ニュース確認等) | 向く | 不向き |

判断の目安は「その場で画面に文字を打てるか」「出力を目で見て編集する必要があるか」の2点。前者がNoで後者も不要なら音声モードが有利。

## 実務での使い方

### 起動方法(2026年7月時点)

- **スマートフォン(iOS/Android)**: ChatGPTアプリでチャット画面を開き、入力欄右下の波形アイコンをタップすると音声モードの画面に切り替わる
- **パソコン(Web版・Windows/Mac用デスクトップアプリ)**: チャット入力欄にあるヘッドフォン(またはマイク)のアイコンをクリックすると音声セッションが始まる
- 初回利用時に声の種類(Arbor、Breeze、Cove、Ember、Juniper、Maple、Sol、Spruce、Valeなど9種類前後)を選択する画面が出るので、好みの声を選んでおく。後から設定でいつでも変更できる

### コピペで使える活用例

語学練習の相手をさせる場合:

```
これから英語で雑談をします。私が話した英文に文法の間違いがあれば、
会話の流れを止めずにさりげなく正しい言い方を織り交ぜて返してください。
明らかな間違いだけを指摘し、細かい言い回しの好みまでは直さないでください。
```

移動中の情報整理・壁打ちに使う場合:

```
今日の商談で話す予定の3つの論点を、私が口頭で説明するので、
聞きながら抜け漏れや弱そうな部分があれば質問して指摘してください。
```

### 主要ツールでの対応付け(2026年7月時点)

| ツール | 機能名 | 特徴 |
|---|---|---|
| ChatGPT | Advanced Voice Mode(高度な音声モード) | ネイティブ音声モデルによる低遅延・感情表現豊かな会話。カメラ・画面共有と併用可能 |
| Google Gemini | Gemini Live | 「メールを読み上げて、返信案も口頭で考えて」のようにGoogleサービス(メール・カレンダー等)と連携した音声操作が得意 |
| Microsoft Copilot | Copilot Voice(「Hey Copilot」ウェイクワード対応) | Windows上で「Hey Copilot」と話しかけて起動できる音声チャット。会話の割り込みにも対応 |
| Claude(Anthropic) | ネイティブな音声会話機能は2026年7月時点で未提供 | モバイルアプリの音声入力は「音声→テキスト変換」止まりで、Advanced Voice Modeのような音声対音声のやり取りはできない |

### 料金・利用制限の目安(2026年7月時点)

| プラン | 音声モードの利用制限の目安 |
|---|---|
| Free | 1日あたり短時間(15分前後)のプレビュー利用 |
| Plus($20/月) | 1日数時間程度まで利用可能 |
| Pro($200/月) | 不正利用防止のガードレールの範囲内でほぼ無制限 |
| Team・Business・Enterprise | 組織のプラン・管理者設定に準じる |

利用可能時間・上限は変更されやすいため、実際に使う前にアプリ内の表示や公式ヘルプページで最新の値を確認すること。

## 注意点・よくある誤解

- **周囲に会話が聞こえる環境では使いにくい**: オフィスなど声を出しづらい環境では使えない場面が多い。イヤホンを使う、あるいは静かな場所に移動するといった運用上の工夫が要る
- **込み入った内容の確認には不向き**: 契約条件の細部確認や数値の羅列など、聞き逃し・言い間違いのリスクがある内容は、音声だけでやり取りせず、最終的にテキストで出力させて目で確認する
- **無料プランは利用時間が短い**: 業務で日常的に使うならPlus以上への加入が事実上前提になる
- **会話内容も学習データとして扱われうる**: テキストチャットと同様に、音声での会話内容もモデル改善への利用のオプトアウト設定が適用される。機密情報を話す前に[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)の設定を確認しておく
- **「音声モード=文字起こし機能」ではない**: 会議の録音を後から要約させたい場合は、音声モードではなく、録音ファイルをアップロードして要約させる使い方が適している。音声モードはあくまでリアルタイムの対話用機能

## 最初の一歩

スマートフォンのChatGPTアプリで波形アイコンをタップし、直近で誰かに相談したかった軽い悩みや、明日の予定の整理を1つ、声に出して話しかけてみる。

## 関連トピック

- [ChatGPTのエージェント機能(ChatGPT Agent)とスケジュールタスク(Tasks)](chatgpt-agent-mode-feature.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: ChatGPTのAdvanced Voice Modeの仕組み(音声ネイティブモデルによる低遅延・感情表現)、起動方法、使いどころの判断基準、コピペ用プロンプト例、Gemini Live/Copilot Voice/Claudeとのツール横断比較、プラン別利用制限の目安、注意点を整理
- **出典**: [Voice Mode FAQ | OpenAI Help Center](https://help.openai.com/en/articles/8400625-voice-mode-faq)、[ChatGPT Voice Mode: Complete Guide (2026) | ToolChase](https://toolchase.com/blog/chatgpt-voice-mode-guide/)、[How to Use ChatGPT Advanced Voice Mode | All About AI](https://www.allaboutai.com/ai-how-to/use-chatgpt-advanced-voice-mode/)、[OpenAI finally brings humanlike ChatGPT Advanced Voice Mode | VentureBeat](https://venturebeat.com/ai/openai-finally-brings-humanlike-chatgpt-advanced-voice-mode-to-u-s-plus-team-users)、[ChatGPTの音声会話機能「高度な音声モード」とは | chatsense](https://chatsense.jp/blog/chatgpt-advanced-vice-mode)、[ChatGPTの音声機能とは | DX/AI研究所](https://ai-kenkyujo.com/news/chatgpt-onsei-kinou/)、[Using Copilot Voice with Microsoft Copilot | Microsoft Support](https://support.microsoft.com/en-us/microsoft-copilot/using-copilot-voice-with-microsoft-copilot)、[Claude vs Gemini 2026 | tech-insider.org](https://tech-insider.org/claude-vs-gemini-2026-2/)
