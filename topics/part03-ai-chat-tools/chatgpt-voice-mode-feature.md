---
title: "ChatGPTの音声(Advanced Voice Mode)機能"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [ChatGPT, 音声, Advanced Voice Mode, GPT-Live, 音声会話, 同時通訳, 語学学習, マルチモーダル]
created: 2026-07-06
updated: 2026-07-27
---

# ChatGPTの音声(Advanced Voice Mode)機能

## これは何か

移動中や作業中は、画面を見て文字を打つこと自体が面倒でChatGPTを開かない、という機会損失が起きがちである。ChatGPTの音声会話機能は、テキストを一切打たずに話しかけるだけで自然な会話ができる機能で、感情や間の取り方まで再現された音声で、電話で人と話すような感覚でやり取りできる点が最大の特徴になる。2026年7月8日、この音声会話のエンジンが「Advanced Voice Mode(高度な音声モード)」から、聞きながら同時に話せる新モデル「GPT-Live」へと刷新された。語学練習の相手、運転中・家事中の壁打ち相手、外国語での同時通訳など、「画面に文字を打てない/打ちたくない」場面での活用を想定した機能である。

## 仕組み・背景

### 「音声認識+読み上げ」→「音声を理解するモデル」→「聞きながら話すモデル」

初期のChatGPTの音声会話は、①音声をテキストに変換(音声認識)→②テキストでChatGPTが応答を生成→③その文章を読み上げる(音声合成)、という3段階の処理を裏で直列に行っていた。この方式では、話し方の抑揚・間・感情といった「声に乗る情報」がテキスト変換の時点で失われてしまい、返ってくる声も機械的になりやすかった。

2024年に登場した「Advanced Voice Mode(高度な音声モード)」は、GPT-4o以降のモデルが音声データを直接理解し、直接音声で応答を生成するネイティブなマルチモーダル方式に切り替わった。テキストに変換する工程を経ないため応答までの遅延が短縮され、話者の感情を汲み取った抑揚のある返答や、笑い声・ため息といった自然な相槌も表現できるようになった。

2026年7月8日には、さらに一段進んだ新モデル「GPT-Live-1」(軽量版「GPT-Live-1 mini」)が投入され、ChatGPTの音声会話の既定エンジンになった。従来のAdvanced Voice Modeは「相手が話し終えるのを待ってから応答を生成する」半二重(half-duplex)方式だったのに対し、GPT-Liveは**聞きながら話す**全二重(full-duplex)方式を採用している。ユーザーが話している途中でも内容を処理し続けるため、話の腰を折らずに「うんうん」「なるほど」といった相槌を挟んだり、ユーザーが話している最中に割り込まれても自然に聞き直したりできる。「もっとゆっくり話して」と頼めばその場で話速を落とすなど、対話の細かい調整にもリアルタイムに応じる。ウェブ検索や込み入った計算・推論が必要な質問が来ると、GPT-Liveは裏側でテキスト推論用のモデルに処理を委ね、その回答を音声の会話に自然に組み込んで返す仕組みになっている。

もう一つの目玉が**リアルタイム翻訳(同時通訳)**である。「これから私が話す内容を全部スペイン語に同時通訳して」のように指示すると、話し終わるのを待たずに訳出が始まるため、対面での通訳や、海外配信の同時通訳のような使い方ができる。

一方で、2026年7月時点ではGPT-Liveはまだ**カメラ映像・画面共有に対応していない**。資料を見せながら質問したり、カメラを向けて「これは何?」と尋ねたりする使い方をしたい場合は、音声セッション開始時に旧来の「Advanced Voice Mode(レガシー)」を選択する必要がある(OpenAIは対応を予定しているが時期は未定)。

## 使いどころ・使い分け

| 場面 | 音声モード(GPT-Live) | 通常のテキストチャット |
|---|---|---|
| 移動中・運転中・家事をしながらの相談 | 向く(画面操作なしで完結) | 不向き(操作に手が取られる) |
| 語学の発音練習・ロールプレイ会話 | 向く(発音矯正・アクセント切り替えに対応) | 不向き(声に出す練習にならない) |
| 商談・海外との会話でのリアルタイム通訳 | 向く(全二重で話しながら訳出できる) | 不向き(発話ごとに文章を打ち直す必要がある) |
| 込み入った資料の作成・長文の推敲 | 不向き(出力を目で確認・編集する作業に弱い) | 向く(Canvasなど編集機能と相性が良い) |
| 咄嗟のブレインストーミング・壁打ち | 向く(テンポよく会話できる) | 向く場合もある(整理しながら書きたい人向け) |
| 込み入った数式・コードの確認 | 不向き(音声では細部が伝わりにくい) | 向く |
| 資料を見せながら・カメラを向けての質問 | 不向き(GPT-Liveは非対応。旧Advanced Voice Modeへの切り替えが必要) | 向く(画像添付で代替可能) |
| ながら作業での情報収集(ニュース確認等) | 向く(裏でウェブ検索して回答を音声に統合) | 不向き |

判断の目安は「その場で画面に文字を打てるか」「出力を目で見て編集する必要があるか」「カメラ・画面共有が要るか」の3点。前2つがNoで、かつカメラ・画面共有が不要なら音声モード(GPT-Live)が有利。カメラ・画面共有を使いたい場合のみ、旧Advanced Voice Modeを選ぶ。

## 実務での使い方

### 起動方法(2026年7月時点)

- **スマートフォン(iOS/Android)**: ChatGPTアプリでチャット画面を開き、入力欄右下の波形アイコンをタップすると音声セッションが始まる。既定エンジンは新しい「GPT-Live」で、2026年7月23日以降はMac用デスクトップアプリにも展開され、手前に開いているウィンドウの内容を参照しながら話せるようになった
- **パソコン(Web版・Windows/Mac用デスクトップアプリ)**: チャット入力欄にあるヘッドフォン(またはマイク)のアイコンをクリックすると音声セッションが始まる
- カメラ・画面共有を使いたい場合は、音声セッション開始時のメニューから「Advanced Voice Mode(レガシー)」を選ぶ。GPT-Live自体はまだカメラ・画面共有に非対応
- 初回利用時に声の種類(Arbor、Breeze、Cove、Ember、Juniper、Maple、Sol、Spruce、Valeなど9種類前後)を選択する画面が出るので、好みの声を選んでおく。後から設定でいつでも変更できる
- 回答の深さは「インテリジェンス」設定で即時・中・高から選べる。雑談は即時、込み入った相談は中〜高にすると裏側の推論モデルにより多く処理を回してくれる

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

商談・海外とのやり取りでリアルタイム通訳に使う場合:

```
これから私と相手が交互に話します。私が日本語で話した内容は英語に、
相手が英語で話した内容は日本語に、話し終わるのを待たずに同時通訳してください。
固有名詞や数字は正確に訳し、意訳しすぎないでください。
```

### 主要ツールでの対応付け(2026年7月時点)

| ツール | 機能名 | 特徴 |
|---|---|---|
| ChatGPT | GPT-Live(既定。旧Advanced Voice Modeはカメラ・画面共有用にレガシーとして選択可能) | 聞きながら話す全二重会話・リアルタイム同時通訳・裏側のウェブ検索や推論モデルへの委譲に対応。カメラ・画面共有は現時点でGPT-Live自体は非対応 |
| Google Gemini | Gemini Live | 「メールを読み上げて、返信案も口頭で考えて」のようにGoogleサービス(メール・カレンダー等)と連携した音声操作が得意 |
| Microsoft Copilot | Copilot Voice(「Hey Copilot」ウェイクワード対応) | Windows上で「Hey Copilot」と話しかけて起動できる音声チャット。会話の割り込みにも対応 |
| Claude(Anthropic) | ネイティブな音声会話機能は2026年7月時点で未提供 | モバイルアプリの音声入力は「音声→テキスト変換」止まりで、GPT-Liveのような音声対音声・全二重のやり取りはできない |

### 料金・利用制限の目安(2026年7月時点)

| プラン | 使えるモデル | 音声モードの利用制限の目安 |
|---|---|---|
| Free | GPT-Live-1 mini(軽量版) | 直近24時間のローリングウィンドウで利用量が限られ、上限に達するとアプリ内で通知される(具体的な分数は非公開・変更されやすい) |
| Go($8/月) | GPT-Live-1(フル版) | Freeよりまとまった時間を利用可能 |
| Plus($20/月) | GPT-Live-1(フル版) | 1日数時間程度まで利用可能な目安 |
| Pro($200/月) | GPT-Live-1(フル版)。カメラ・画面共有が必要な場合は旧Advanced Voice Modeも選択可 | 不正利用防止のガードレールの範囲内でほぼ無制限 |
| Team・Business・Enterprise | 組織のプラン・管理者設定に準じる | 組織のプラン・管理者設定に準じる |

利用可能時間・上限は変更されやすいため、実際に使う前にアプリ内の表示や公式ヘルプページ([Voice Mode FAQ](https://help.openai.com/en/articles/8400625-voice-mode-faq))で最新の値を確認すること。

## 注意点・よくある誤解

- **周囲に会話が聞こえる環境では使いにくい**: オフィスなど声を出しづらい環境では使えない場面が多い。イヤホンを使う、あるいは静かな場所に移動するといった運用上の工夫が要る
- **込み入った内容の確認には不向き**: 契約条件の細部確認や数値の羅列など、聞き逃し・言い間違いのリスクがある内容は、音声だけでやり取りせず、最終的にテキストで出力させて目で確認する
- **無料プランは利用時間が短い**: 業務で日常的に使うならGo以上への加入が事実上前提になる。無料プランはより軽量な「GPT-Live-1 mini」になる点にも注意
- **カメラ・画面共有は既定エンジンでは使えない**: 2026年7月時点のGPT-Liveは音声のみに対応で、資料を見せながら質問する用途には非対応。この用途では音声セッション開始時に旧来の「Advanced Voice Mode(レガシー)」を明示的に選ぶ必要がある
- **同時通訳は完璧ではない**: リアルタイム翻訳は便利だが、固有名詞・専門用語・数字の訳し間違いが起こりうる。契約交渉など訳語の正確性が重要な場面では、後でテキストログを見返して確認する運用にする
- **会話内容も学習データとして扱われうる**: テキストチャットと同様に、音声での会話内容もモデル改善への利用のオプトアウト設定が適用される。機密情報を話す前に[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)の設定を確認しておく
- **「音声モード=文字起こし機能」ではない**: 会議の録音を後から要約させたい場合は、音声モードではなく、録音ファイルをアップロードして要約させる使い方が適している。音声モードはあくまでリアルタイムの対話用機能

## 最初の一歩

スマートフォンのChatGPTアプリで波形アイコンをタップし、直近で誰かに相談したかった軽い悩みや、明日の予定の整理を1つ、声に出して話しかけてみる。途中でわざと割り込んで話してみると、GPT-Liveが聞きながら話す全二重の感覚がつかみやすい。

## 関連トピック

- [ChatGPTのエージェント機能(ChatGPT Agent)とスケジュールタスク(Tasks)](chatgpt-agent-mode-feature.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-07-27: 新モデル「GPT-Live」への刷新を反映
- **内容**: 2026年7月8日にOpenAIが音声会話の既定エンジンを「Advanced Voice Mode」から全二重(聞きながら話せる)方式の「GPT-Live-1/GPT-Live-1 mini」に刷新した内容を反映。リアルタイム同時通訳の使い方、裏側での検索・推論モデルへの委譲、カメラ・画面共有が現時点でGPT-Live自体には非対応で旧Advanced Voice Modeの選択が必要な点、Goプラン($8/月)を含む料金・利用制限表、使いどころ表・コピペ例・注意点を更新
- **出典**: [OpenAI releases new voice models for more natural live conversations | TechCrunch](https://techcrunch.com/2026/07/08/openai-releases-new-voice-models-for-more-natural-live-conversations/)、[ChatGPT's new voice mode will slow down if you tell it to | Engadget](https://www.engadget.com/2210651/chatgpt-new-voice-mode-will-slow-down-if-you-tell-it-to/)、[OpenAI's next-generation ChatGPT Voice will make Advanced Voice Mode look outdated | Neowin](https://www.neowin.net/news/openais-next-generation-chatgpt-voice-will-make-advanced-voice-mode-look-outdated/)、[GPT Live Voice Mode: Real-Time Translation and Natural Conversation Explained | MindStudio](https://www.mindstudio.ai/blog/gpt-live-voice-mode-real-time-translation-explained)、[I used ChatGPT's new voice mode to translate the World Cup in real time | Tom's Guide](https://www.tomsguide.com/ai/i-used-chatgpts-new-voice-mode-to-translate-the-world-cup-in-real-time-heres-what-happened)、[ChatGPT already listens and speaks. Soon it may see as well | Yahoo Tech](https://tech.yahoo.com/computing/articles/chatgpt-already-speaks-soon-may-185644092.html)、[ChatGPT音声モードが進化、聞きながら話せるように――同時通訳も可能「GPT-Live-1」公開 | CNET Japan(Yahoo!ニュース)](https://news.yahoo.co.jp/articles/49614b7e9d20a5aefb7be5f31f20937d78e5d80a)、[GPT-Liveとは？OpenAIの全二重リアルタイム音声モデル | AI革命株式会社メディア](https://ai-revolution.co.jp/media/what-is-gpt-live/)、[ChatGPT Pricing Guide: Free, Go, Plus, Pro (July 2026) | FelloAI](https://felloai.com/chatgpt-pricing-guide-free-go-plus-pro-alternatives-october-2025/)

### 2026-07-06: 初版執筆
- **内容**: ChatGPTのAdvanced Voice Modeの仕組み(音声ネイティブモデルによる低遅延・感情表現)、起動方法、使いどころの判断基準、コピペ用プロンプト例、Gemini Live/Copilot Voice/Claudeとのツール横断比較、プラン別利用制限の目安、注意点を整理
- **出典**: [Voice Mode FAQ | OpenAI Help Center](https://help.openai.com/en/articles/8400625-voice-mode-faq)、[ChatGPT Voice Mode: Complete Guide (2026) | ToolChase](https://toolchase.com/blog/chatgpt-voice-mode-guide/)、[How to Use ChatGPT Advanced Voice Mode | All About AI](https://www.allaboutai.com/ai-how-to/use-chatgpt-advanced-voice-mode/)、[OpenAI finally brings humanlike ChatGPT Advanced Voice Mode | VentureBeat](https://venturebeat.com/ai/openai-finally-brings-humanlike-chatgpt-advanced-voice-mode-to-u-s-plus-team-users)、[ChatGPTの音声会話機能「高度な音声モード」とは | chatsense](https://chatsense.jp/blog/chatgpt-advanced-vice-mode)、[ChatGPTの音声機能とは | DX/AI研究所](https://ai-kenkyujo.com/news/chatgpt-onsei-kinou/)、[Using Copilot Voice with Microsoft Copilot | Microsoft Support](https://support.microsoft.com/en-us/microsoft-copilot/using-copilot-voice-with-microsoft-copilot)、[Claude vs Gemini 2026 | tech-insider.org](https://tech-insider.org/claude-vs-gemini-2026-2/)
