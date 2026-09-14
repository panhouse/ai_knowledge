---
title: リアルタイム音声API(ボイスエージェント構築)の基本
part: 9
chapter: 第2章 API活用実践
tags: [Realtime API, Gemini Live API, ElevenLabs, ボイスエージェント, IVR, 音声AI]
created: 2026-07-25
updated: 2026-09-05
---

# リアルタイム音声API(ボイスエージェント構築)の基本

## これは何か

「電話の一次受付をAIに任せたい」「営業ロールプレイの相手をAIにさせたい」といった要望は、[ChatGPTの音声モード機能](../part03-ai-chat-tools/chatgpt-voice-mode-feature.md)のようなアプリを人が使うだけでは実現できない。自社の電話回線やアプリに、AIが人と自然に音声で会話する機能そのものを組み込む必要があるからだ。リアルタイム音声API(Realtime Voice API)は、この「自社サービスに音声対話するAIを組み込む」ための開発者向けAPIで、OpenAIの「Realtime API」、GoogleのGemini「Live API」などが代表格になる。マイクからの音声ストリームを送ると、AIが話の内容を理解し、遅延の小さい音声で応答を返してくる、という双方向のやり取りを1本のAPI接続(WebSocket/WebRTC)の上で実現する。

このページは「アプリの利用者としてAIと音声で話す」視点ではなく、「自社でボイスボット・IVR(自動音声応答)・音声エージェントを開発する」側の視点で、何ができるか・何が必要か・どう選ぶかを扱う。

## 仕組み・背景

### 「音声認識→LLM→音声合成」の3段構えから「1つのAPIで音声を直接扱う」方式へ

音声で対話するシステムを作る従来のやり方は、次の3つの処理を別々のサービスでつなぐ「カスケード方式」だった。

1. **音声認識(ASR/STT)**: 話者の声をテキストに変換する
2. **LLMによる応答生成**: テキストになった質問をLLMに渡し、回答テキストを生成する
3. **音声合成(TTS)**: 回答テキストを声に変換して読み上げる

この方式は各段階を個別に選定・チューニングできる柔軟さがある一方、3つのサービスを順番に呼ぶため合計の遅延(レイテンシ)が積み上がりやすく、テキストに変換する過程で声の抑揚・感情・間(ま)といった情報が失われ、返ってくる声も機械的になりがちだった。

**リアルタイム音声API**は、音声データを直接理解し、直接音声で応答を生成する「音声対音声(speech-to-speech)」のモデルを、WebSocketやWebRTCのストリーミング接続の上で提供する。テキストへの変換工程を経ないため応答までの遅延が小さく、話者が話している途中でAI側の発話を止めて割り込む「割り込み(interruption/barge-in)」にも標準対応している。ユーザーが話し始めたことをAI側が検知して自分の発話を止める処理(音声区間検出、VAD: Voice Activity Detection)や、話し終わりの判定(ターン検出)もAPI側が担う設計になっている。

なお、ElevenLabsの「ElevenAgents」(旧称Conversational AI)のように、自社製の音声認識(ASR)・音声合成(TTS)・独自の「ターン検出モデル」を、選択したLLM(OpenAI/Google/Anthropicなど)と組み合わせて1つの管理されたループとして提供する「ホスト型オーケストレーション型」の製品もある。厳密には音声対音声の単一モデルではないが、開発者から見れば1つのAPI/プラットフォームとして音声対話を実装できる点は共通しており、実務上は同じ土俵で比較検討されることが多い。

なお、Anthropicは2026年9月時点でも開発者向けの音声対音声リアルタイムAPIは提供していない(Claude/Claude Codeの「音声モード」はアプリ利用者向けの完成品機能であり、自社サービスへの組み込み用途には使えない)。自社開発でAnthropicのモデルを使いたい場合は、ElevenLabsのようなオーケストレーション型プラットフォームでLLMとしてClaudeを選ぶのが現実的な選択肢になる。

## 使いどころ・使い分け

| やりたいこと | 向いている手段 |
|---|---|
| 電話やアプリで人とAIが自然な会話のキャッチボールをする(コールセンターIVR、営業ロールプレイ練習、社内ヘルプデスク等) | リアルタイム音声API |
| 会議や商談の録音を後から要約・議事録化したい | 音声ファイルのアップロード+文字起こし(バッチ処理で十分。リアルタイム性は不要) |
| 定型的な一問一答(FAQボットのようなテキストで完結する用途) | 通常のテキストチャットAPI(音声にする必要がない分、実装もコストもシンプル) |
| 自社アプリの利用者に音声対話機能を"体験"させたいだけ(開発は不要) | [ChatGPTの音声モード機能](../part03-ai-chat-tools/chatgpt-voice-mode-feature.md)やGemini Liveアプリなど、完成品のアプリをそのまま使う |
| コールセンターの応答を録音してあとから感情分析・品質チェックしたい | 音声認識(バッチ)+分析用LLM(リアルタイム性は不要) |

判断基準はシンプルで、「その場でAIと人が声で会話のキャッチボールをする必要があるか」「開発者として自社サービスに組み込む必要があるか」の2点。どちらもYesならリアルタイム音声API、どちらかがNoならより単純な手段(バッチ処理のASR/TTS、完成品アプリ)で足りることが多い。

### 向く業務シーンの例

- **コールセンターIVRの一次対応**: 「どのご用件ですか」の聞き取りから、簡単な照会への即答、複雑な用件は有人オペレーターへの引き継ぎまでをAIが担う
- **営業・接客のロールプレイ練習ツール**: 新人研修で、AIを想定顧客役にして商談の受け答えを声で練習する
- **社内ヘルプデスクの一次受付**: 「経費精算のやり方」「PCが壊れた時の連絡先」など、社内問い合わせの一次対応を音声で行う
- **多言語窓口**: 訪日客・海外拠点向けの音声窓口を、対応言語の追加コストを抑えて用意する

### 向かない・過剰なケース

- テキストのチャットボットで十分な単純なQ&A(音声にすると開発・運用コストが跳ね上がるだけで体験の向上が小さい)
- 発話内容を一言一句正確に記録・確認する必要がある用途(契約条件の確認など。音声のみでのやり取りは聞き逃し・言い間違いのリスクがあり、テキストでの最終確認が必要になる)
- 呼量(コール数)が少なく、有人対応で十分まかなえる規模

## 実務での使い方

### 主要なリアルタイム音声APIの比較(2026年9月時点)

| 項目 | OpenAI Realtime API | Google Gemini Live API | ElevenLabs ElevenAgents |
|---|---|---|---|
| 方式 | 音声対音声のネイティブモデル(gpt-realtime系) | 音声対音声のネイティブモデル(Gemini Live、Native Audio) | ASR+選択式LLM+TTS+独自ターン検出モデルを組み合わせたホスト型オーケストレーション |
| 代表モデル/製品名 | gpt-realtime-2.1、gpt-realtime-2.1-mini(2026年7月リリース。GPT-5級の推論力を音声対音声に持ち込んだ「GPT-Realtime-2」系の改良版)。ほかに音声翻訳特化のGPT-Realtime-Translate、文字起こし特化のGPT-Realtime-Whisperがある | Gemini Live API(Gemini 2.5 Flash Native Audioが標準。より高品質な音声対話向けにGemini 3.1 Flash Liveも提供) | ElevenAgents(旧称Conversational AI) |
| 対応言語の目安 | 約50言語 | 90言語以上(Gemini 3.1 Flash Liveの公表値。トーン・感情・背景音まで拾う音響ニュアンス検出付き) | 32言語(Flash v2.5使用時。上位モデルで70言語以上に対応) |
| 接続方式 | WebSocket / WebRTC / SIP(ネイティブSIPコネクタがGA、Twilio等のSIPトランクと直結可能) | WebSocket(Live API)。音声に加えカメラ映像・画面共有のライブ映像入力にも対応 | WebSocket / SIPトランク(電話連携) |
| 割り込み(barge-in)対応 | 標準対応(VADによる自動検知、2.1系で無音・雑音判定と割り込み挙動を改善) | 標準対応(VAD設定で割り込み検知、生成中の応答は破棄) | 対応(「eager/normal/patient」などターンの割り込みやすさを設定可能) |
| レイテンシの目安 | プロンプトキャッシュ改善によりp95遅延を25%以上短縮(2.1系) | Gemini 3.1 Flash LiveでTTFT(応答開始までの時間)約960ms | Flash v2.5で音声生成75ms未満(TTS単体の値) |
| 料金体系 | 音声トークンの従量課金(gpt-realtime-2.1: 音声入力$32/出力$64/100万トークン。mini版: 音声入力$10/出力$20/100万トークン。別途Whisper文字起こしが$0.006/分) | トークン従量課金(Gemini 3.1 Flash Liveでテキスト$0.75/$4.50、音声$3.00/$12.00(いずれも100万トークンあたり、入力/出力)。目安として音声入力$0.005/分・音声出力$0.018/分程度) | 月額プラン(Free〜$990/月のBusiness)に分数がバンドル(Starter 75分〜Business 12,375分)+超過分の従量課金。LLM・電話連携費用は別建て |
| 電話(IVR)連携のしやすさ | ネイティブSIPコネクタ(GA)、Twilio Elastic SIP Trunking等の公式連携ガイドあり。有人転送(warm transfer)の実装例も整備 | Vertex AI版がGoogle I/O 2026にGAし、本番SLA・マルチリージョン対応が加わり企業導入が拡大中 | SIPトランクによる電話連携が強み(コールセンター用途を強く意識した設計) |
| 特徴 | 関数呼び出し(Function Calling)の精度向上、MCP(リモートMCPサーバー)対応、画像入力に対応し既存のOpenAIエコシステムと統合しやすい | 関数呼び出し・コード実行・Google検索をツールとして呼び出し可能。音声だけでなく映像もリアルタイムに扱える点が独自 | LLMをOpenAI/Google/Anthropic等から選べる柔軟性、電話業務向けの機能が充実 |

料金・対応言語・レイテンシの数値は各社が頻繁に更新するため、**PoCや発注前には必ず各社の公式料金ページ・リリースノートで最新値を確認すること**。

### PoC(概念実証)を始める最低限の構成

1. **APIキー・利用契約の取得**: OpenAI/Google/ElevenLabsいずれかの開発者アカウントを作成し、支払い方法を登録してAPIキーを発行する(通常の[OpenAI APIの基本](openai-api-basics.md)や[Google Gemini APIの基本](google-gemini-api-basics.md)と同じ従量課金の枠組み)
2. **音声の入出力経路の用意**: PoCの段階では、ブラウザのマイク入力(WebRTC)や、Twilioなどの電話連携サービス経由での音声ストリーム受け渡しが最短。既存の電話交換機(PBX)と連携する場合はSIPトランクでの接続を検討する(OpenAI Realtime APIはネイティブのSIPコネクタがGAしており、Twilio Elastic SIP TrunkingなどのSIPトランクを直接つなげられる)
3. **システムプロンプト(instructions)の設計**: 「どんな役割で」「何を話してよいか」「困った時はどう答えるか(有人転送の条件など)」をテキストの指示として渡す。基本はテキストのシステムプロンプトと同じ考え方
4. **必要な業務データへの接続**: 在庫確認・予約状況の照会など、社内データを参照させたい場合はFunction Calling(詳細は[Function Calling(Tool Calling)の基本](function-calling-basics.md))で社内APIを呼び出す関数を登録する
5. **エスカレーション経路の設計**: AIが対応できない・すべきでない場合に、有人オペレーターへどう引き継ぐか(会話履歴の引き継ぎ方も含め)を最初から設計に入れておく
6. **試験運用とログ確認**: 少人数・限定シナリオでまず動かし、誤認識・意図しない回答・料金の実績値を確認してから対象を広げる

### 料金の考え方

リアルタイム音声APIの多くは「分単位・トークン単位の従量課金」で、テキストのみのAPI利用よりも単価は高くなりやすい。PoCの段階では、想定する1コールあたりの平均通話時間(例: 3分)× 想定コール数で月額の概算を出し、閾値を決めて実運用に進むかどうかを判断するとよい。ElevenLabsのように月額プランに一定の通話分数がバンドルされ、超過分だけ従量課金になる製品もあれば、OpenAI・Googleのように純粋なトークン従量課金の製品もあり、想定する呼量によって有利な料金体系が変わる。

トークン従量課金の製品では、AIが話す時間(音声出力)の方が聞く時間(音声入力)より単価が高いため、AIの発話が長い設計(丁寧な説明を毎回返す等)ほど費用がかさみやすい。プロンプトキャッシュ(会話履歴やシステムプロンプトのキャッシュ利用)が効くと単価は下がるため、キャッシュが有効に働く設計(システムプロンプトを毎回変えない、等)にできているかもコスト試算に含めるとよい。

### 既存の業務ツールとの連携の考え方

- **電話網との接続**: 自社の電話番号でAIボイスボットを稼働させるには、Twilioなどの電話API事業者を介してリアルタイム音声APIに音声ストリームを橋渡しするのが一般的な構成
- **CRM・予約システムとの連携**: Function Callingで、通話中に顧客情報や予約状況を照会・更新する関数を呼び出す設計にすると、通話内容と業務システムが連動する
- **ノーコードでの構築**: フルスクラッチでの実装が難しい場合、DifyやVoiceflowなど音声対応をうたうノーコード/ローコードの会話設計ツールを経由する選択肢もある(ただし本格的な電話連携やレイテンシ要件がある場合は制約に注意)

## 注意点・よくある誤解

- **「ChatGPTの音声モード」とは別物**: [ChatGPTの音声モード機能](../part03-ai-chat-tools/chatgpt-voice-mode-feature.md)は、OpenAIが用意した完成品アプリを利用者が使う機能であり、契約・料金体系も別。自社のIVRやボイスボットに組み込みたい場合は、本ページで扱うAPI(Realtime API等)を自前で開発・運用する必要がある
- **レイテンシは環境次第で変動する**: カタログ値は理想条件での数値であることが多く、実際のネットワーク環境・会話の長さ・関数呼び出しの有無によって体感の遅延は変わる。PoCの段階で実際の通話環境に近い条件で計測すること
- **長時間通話でレイテンシが劣化する場合がある**: 会話履歴が長くなるにつれて応答が遅くなる事例が報告されており、定期的な会話コンテキストのリセット・要約などの設計上の工夫が必要になることがある
- **多言語対応の「対応言語数」は鵜呑みにしない**: カタログ上の対応言語数は資料によって幅があり、実際の発音の自然さ・方言対応レベルは言語によって差が大きい。想定する利用言語で必ず試聴・検証する
- **音声のみでの重要事項確認は避ける**: 契約条件・金額など聞き間違いが致命的になる情報は、音声のやり取りの後にテキストやSMS・メールで確認内容を送るなど、二重チェックの仕組みを設計に組み込む
- **通話内容の記録・利用規約の確認**: 音声データや文字起こしが学習・品質改善に使われるかどうかは契約プラン次第。個人情報や機密情報を扱う場合は、[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)の観点で契約条件(データ保持期間・オプトアウト設定)を確認する
- **費用は「分単位」で積み上がる**: テキストAPIの感覚で試算すると想定より高額になりやすい。PoCの段階で実際の通話時間・呼量から月額の概算を必ず出しておく

## 最初の一歩

OpenAIまたはGoogleの開発者アカウントでAPIキーを取得し、公式のクイックスタート(ブラウザからマイクで話しかけるサンプル)を1つ動かして、割り込み(話している途中でAIの発話が止まるか)とレイテンシの体感を確かめてみる。

## 関連トピック

- [OpenAI APIの基本](openai-api-basics.md)
- [Google Gemini APIの基本](google-gemini-api-basics.md)
- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [ChatGPTの音声(Advanced Voice Mode)機能](../part03-ai-chat-tools/chatgpt-voice-mode-feature.md)

## 更新履歴

### 2026-09-05: 主要3製品の最新モデル・料金・機能を更新
- **内容**: OpenAI Realtime APIをgpt-realtime-2.1/2.1-mini(ネイティブSIPコネクタGA、MCP対応、翻訳・書き起こし特化モデル追加)に、Google Gemini Live APIをGemini 3.1 Flash Live(90言語以上、映像入力対応、Vertex AIでGA)に更新。ElevenLabsは「ElevenAgents」への名称変更と月額プラン別のバンドル分数を反映。料金の考え方に音声出力単価・プロンプトキャッシュの影響を追記し、Anthropicが2026年9月時点でも開発者向けリアルタイム音声APIを提供していない旨を補足
- **出典**: [Introducing gpt-realtime and Realtime API updates for production voice agents | OpenAI](https://openai.com/index/introducing-gpt-realtime/)、[New Realtime models on the API: gpt-realtime-2.1 and gpt-realtime-2.1-mini | OpenAI Developer Community](https://community.openai.com/t/new-realtime-models-on-the-api-gpt-realtime-2-1-and-gpt-realtime-2-1-mini/1385896)、[OpenAI Realtime API Cuts Voice Agent Latency 25%, Adds Reasoning Mini Model | Tech Times](https://www.techtimes.com/articles/319860/20260707/openai-realtime-api-cuts-voice-agent-latency-25-adds-reasoning-mini-model.htm)、[Realtime API with SIP | OpenAI API](https://developers.openai.com/api/docs/guides/realtime-sip)、[Connect the OpenAI Realtime SIP Connector with Twilio Elastic SIP Trunking | Twilio](https://www.twilio.com/en-us/blog/developers/tutorials/product/openai-realtime-api-elastic-sip-trunking)、[OpenAI Realtime API Pricing in 2026: Real-World Data From 4,000 Measured Sessions | HackerNoon](https://hackernoon.com/openai-realtime-api-pricing-in-2026-real-world-data-from-4000-measured-sessions)、[Gemini 3.1 Flash Live: Google's latest AI audio model](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-live/)、[Gemini 3.1 Flash Live Preview — Pricing, Providers & Benchmarks | LLM Gateway](https://llmgateway.io/models/gemini-3.1-flash-live-preview)、[How to use Gemini Live API Native Audio in Vertex AI | Google Cloud Blog](https://cloud.google.com/blog/topics/developers-practitioners/how-to-use-gemini-live-api-native-audio-in-vertex-ai)、[Live API capabilities guide | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/live-api/capabilities)、[Tool use with Live API | Gemini API | Google AI for Developers](https://ai.google.dev/gemini-api/docs/live-api/tools)、[ElevenLabs price change — Conversational AI (Agents) price cut | UsagePricing](https://www.usagepricing.com/blueprint/activity/elevenlabs-2026-05-07-price-change)、[The Complete Guide to ElevenLabs Plans, Overages, and Usage-Based Pricing in 2026 | Flexprice](https://flexprice.io/blog/elevenlabs-pricing-breakdown)、[ElevenLabs Pricing 2026: Plans, Credits & API Costs | Layer3labs](https://www.layer3labs.io/guides/elevenlabs-pricing)、[ElevenLabs models compared: v3 vs Multilingual v2 vs Flash v2.5 (2026) | Voxrater](https://voxrater.com/insights/elevenlabs-models-compared/)、[Anthropic Adds Model Choice to Claude Voice Mode For All Users | SQ Magazine](https://sqmagazine.co.uk/anthropic-claude-voice-mode-models/)

### 2026-07-25: 初版執筆
- **内容**: 従来の「音声認識→LLM→音声合成」のカスケード方式と、音声対音声のネイティブモデルによるリアルタイム音声APIの違い、OpenAI Realtime API・Google Gemini Live API・ElevenLabs Conversational AIの横並び比較(対応言語・レイテンシ・割り込み対応・料金体系)、PoCを始める際の最低限の構成、電話網・CRM連携の考え方、注意点を整理
- **出典**: [Advancing voice intelligence with new models in the API | OpenAI](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)、[OpenAI Realtime API Pricing in 2026: Real-World Data From 4,000 Measured Sessions | HackerNoon](https://hackernoon.com/openai-realtime-api-pricing-in-2026-real-world-data-from-4000-measured-sessions)、[OpenAI Realtime API Cuts Voice Agent Latency 25%, Adds Reasoning Mini Model | Tech Times](https://www.techtimes.com/articles/319860/20260707/openai-realtime-api-cuts-voice-agent-latency-25-adds-reasoning-mini-model.htm)、[New Realtime models on the API: gpt-realtime-2.1 and gpt-realtime-2.1-mini | OpenAI Developer Community](https://community.openai.com/t/new-realtime-models-on-the-api-gpt-realtime-2-1-and-gpt-realtime-2-1-mini/1385896)、[Realtime and audio | OpenAI API](https://developers.openai.com/api/docs/guides/realtime)、[Gemini API Pricing: Full Breakdown of Costs | developer.puter.com](https://developer.puter.com/tutorials/gemini-api-pricing/)、[Gemini Live API Is Now in Production: Build Real-Time Voice and Vision Agents | byteiota](https://byteiota.com/gemini-live-api-production-vertex-ai/)、[[Live API] gemini-live-2.5-flash-native-audio | Google AI Developers Forum](https://discuss.ai.google.dev/t/live-api-gemini-live-2-5-flash-native-audio-returns-no-output-after-setupcomplete-gemini-2-0-flash-live-001-not-accessible/142985)、[ElevenLabs — We cut our pricing for Conversational AI](https://elevenlabs.io/blog/we-cut-our-pricing-for-conversational-ai)、[ElevenLabs Pricing & Plans for AI Calling: Full Guide for 2026 | CloudTalk](https://www.cloudtalk.io/blog/elevenlabs-pricing/)、[ElevenLabs - Unpacking ElevenAgent's Orchestration Engine](https://elevenlabs.io/blog/unpacking-elevenagents-orchestration-engine)、[ElevenAgents | ElevenLabs Documentation](https://elevenlabs.io/docs/eleven-agents/overview)
