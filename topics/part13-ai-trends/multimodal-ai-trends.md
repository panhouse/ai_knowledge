---
title: 生成AIのマルチモーダル化の動向(Omniモデル・統合マルチモーダルAI)
part: 13
chapter: 第1章 技術トレンド
tags: [マルチモーダルAI, Omniモデル, GPT-6 Astra, GPT-Live, Gemini Omni, Qwen3.8-Omni-Flash]
created: 2026-07-07
updated: 2026-09-21
---

# 生成AIのマルチモーダル化の動向(Omniモデル・統合マルチモーダルAI)

## これは何か

以前の生成AIは「文章はChatGPT」「画像生成はMidjourney」「音声はElevenLabs」のように、モダリティ(データの種類)ごとに別々のモデル・ツールを使い分け、人間がその間をつなぐ必要があった。これに対して2024年以降、テキスト・画像・音声・動画を1つのモデルが最初から一体で理解・生成する「ネイティブ・マルチモーダル(Native Multimodal)」なモデルが主流になり、各社がこれを「Omni(オムニ、あらゆるものを扱うという意味)」というブランド名で呼ぶようになった。2026年9月時点では「マルチモーダルに対応しているか」自体はもう差別化にならず、各社の実装方式の違い(特に音声を音声のまま直接処理するか、テキスト変換を挟む二段階構成か、そして「対話の窓口」と「裏側のモデル」が実は別物であるケースが増えていること)が実務上の使い勝手を左右する段階に入っている。この違いを理解していないと、「音声対応」という宣伝文句だけを見て導入し、会話の自然さや対応モダリティの組み合わせが期待と違っていた、という失敗が起きやすい。

## 仕組み・背景

### パイプライン型からネイティブ・マルチモーダルへ

従来の「マルチモーダル対応」の多くは、実態としては「画像認識専用モデルが画像をテキストの説明文に変換し、その説明文をLLMに読ませる」というように、モダリティごとに専門モデルをパイプライン(直列)でつなぐ方式だった。この方式は各モダリティの処理は得意でも、モダリティをまたいだ細かいニュアンス(声のトーンと表情の組み合わせなど)を統合的に理解するのは苦手という限界があった。

OpenAIが2024年5月に発表したGPT-4oは、テキスト・音声・画像を単一のモデルで直接処理する「ネイティブ・マルチモーダル」の設計を採用した主要モデルの一つとされる。画像はテキストと同じ「トークン」の列に変換されてモデルに入力され、Transformer(注意機構でどの情報に注目するかを重み付けする仕組み)がテキストと画像を同時に処理する。これにより音声入力から音声出力まで最短232ミリ秒という、人間同士の会話に近い速度での応答が可能になった。

### 2026年9月時点の状況:「対応の有無」から「作り方の違い」へ

主要フロンティアモデルはどれも「マルチモーダル対応」を謳うのが当たり前になった一方、各社のアプローチには明確な違いが出てきている。

1. **OpenAI: 最上位モデルは「テキスト+画像」に絞り、音声はGPT-Liveという別建て** — 2026年9月3日に発表された世代交代モデル「GPT-6 Astra」は、コンピュータ操作・長時間エージェント・コーディングに重点を置いた設計で、モデル自体が受け付ける入力はテキスト・画像までで、音声・動画のネイティブ処理には対応していない([モデル動向の詳細](ai-model-trends-basics.md)を参照)。一方、ChatGPTの音声体験は2026年7月8日に新しい音声システム「GPT-Live」へ置き換わっており、これは音声をテキストに変換せず音声のまま処理する別建ての仕組みで、聞きながら話す(相槌・割り込み)自然な会話ができる。つまり「最上位の推論モデル(Astra)」と「音声で話しかける入り口(GPT-Live)」は必ずしも同じモデルではなく、下位のGPT-5.6ファミリー(Luna/Terra/Sol)も中位〜廉価帯として併存している。カメラ映像・画面共有が必要な場合は引き続き旧来の「Advanced Voice Mode」を使う形になっており、開発者向けには別途Realtime API(gpt-realtime-2.1)が提供されている。
2. **Google: Gemini Omniによる「動画をまるごと編集」、ただしAPIエンドポイントは移行期** — 2026年5月のGoogle I/Oで発表された「Gemini Omni」は、画像・音声・動画・テキストを自由な組み合わせで入力し、動画を出力する「any-to-any(エニー・トゥ・エニー)」型モデル。Geminiアプリ・Google Flow・YouTube Shortsへの展開に続き、Google Workspaceの動画作成ツール「Google Vids」にも「Gemini Omni Flash」として統合され、自然言語の指示だけで動画のカット編集・音声合成に加え、本人そっくりの声・外見を再現する「パーソナルアバター」生成まで行えるようになった(EEA・英国・米テキサス州・イリノイ州では編集機能の一部に地域制限がある)。開発者向けには要注意の変更があり、既存の`gemini-omni-flash-preview`エンドポイントは2026年9月30日に廃止予定であるため、このAPIを直接呼び出している場合は後継エンドポイントへの移行を早めに確認する必要がある。テキストモデル本体は中位の「Gemini 3.8 Flash」(9月2日、セキュリティ強化版「3.8 Flash Cyber」も同時投入)まで更新が進む一方、最上位のGemini 3.5 Proは9月時点でも延期が続いている。
3. **Anthropic: 「理解」に強く、生成にはまだ踏み込まない路線が継続** — 2026年9月1日に投入された最上位モデル「Claude Fable 5.1」は、引き続きテキスト+画像の「理解」(図表・グラフ・PDF内の表の読み取りなど)に強みを置き、画像・音声・動画のネイティブ生成には対応していない。Claude(コード実行ツール等)が生成する画像・音声・動画ファイルには、AIによる生成であることを示す電子署名「C2PA Content Credentials」が付与される。Claudeアプリの音声モードは2026年7月23日にHaikuからOpus/Sonnetベースへ切り替わり18言語対応になったが、仕組みは「聞く→考える→話す」のターン制のままで、音声合成は外部プロバイダ(ElevenLabsを下請けとして利用)への発注という二段階構成である。GPT-LiveやGemini Liveのような「音声を音声のまま直接処理する」エンドツーエンド型とは、この点で設計思想が異なる。
4. **xAI: 単一Omniより「専用モデルの組み合わせ」** — xAIはGrok 4.6(2026年8月)をテキスト・推論の主力としつつ、音声はGrok Voice、画像・動画生成はGrok Imagineと、モダリティごとに専用モデルを使い分ける構成を続けている。Grok Voiceは文字起こし用の新版「grok-voice-transcribe-2.0」が利用可能になった(既定は引き続き旧版の1.0)。Grok Imagineは画像生成の旧モデル「grok-imagine-image-quality」の提供終了が2026年11月2日に予告され、以降のリクエストは低画質設定の「grok-imagine-image-2.0」に自動的に振り替わる予定で、単価も下がる見込み。1つのOmniモデルへの統合を進める他社とは異なるアプローチであり、次期フラッグシップとされるGrok 5(6兆パラメータ級と噂される)は9月時点でも正式な提供時期が未確定のままである。
5. **オープンウェイト: AlibabaがQwen3.8-Omni-Flashを投入し、コスト構造が一変** — Alibabaは2026年9月18日、次世代の軽量オムニモーダルモデル「Qwen3.8-Omni-Flash」を公開した。テキスト・画像・音声・動画(URL経由で最大2時間・2GBの動画、最大3時間の音声)をネイティブに入力できる1Mトークンの長文コンテキストを持ち、113言語・方言に対応、関数呼び出し(Function Calling)やWeb検索と組み合わせたエージェント的な用途を想定した設計になっている。出力はテキストのみ。価格は入力100万トークンあたり$0.15・出力$0.47(キャッシュ利用時は$0.016)で、前世代のQwen3.5-Omni-Plusに比べ音声入力の時間単価が98%、音声+動画の組み合わせでは93%安くなったとされる。ただし2026年9月時点ではウェイト(重み)は公開されておらず、QwenCloud・Alibaba Cloud Model Studio・Qwen Studio経由のAPI利用に限られるため、「重みをダウンロードして自社サーバーで動かせるOmniモデル」としては、引き続き前世代のQwen3.5-Omni(Plus/Flash/Light)が現状の選択肢になる。

## 使いどころ・使い分け

### 「対応モダリティの宣伝」を鵜呑みにしない

同じ「マルチモーダル対応」でも、モデルによって実際にできることは大きく異なる。導入前に、次の観点を具体的な組み合わせで確認する必要がある。

| 確認観点 | 例 |
|---|---|
| 入力として何を受け付けるか | テキスト+画像は多くのモデルが対応。動画そのもの(音声トラック込み)を直接理解できるか、静止画の連続としてしか扱えないかはモデルで差がある |
| 出力として何を生成できるか | テキストのみ出力か、音声・画像・動画も直接生成できるか(例: Claudeは2026年9月時点でも画像・文章の理解に強い一方、音声・動画のネイティブ生成には対応していない) |
| 音声応答が「ネイティブ」か「二段階(TTS)」か | GPT-LiveやGemini Liveは音声を音声のまま直接処理するため相槌・割り込みが自然。Claudeの音声モードのように「聞く→考える→話す」のターン制+外部TTSの構成は、会話としての自然さでは一歩劣るが、実装がシンプルで既存のテキストモデルの品質をそのまま音声に載せられる利点がある |
| リアルタイム性 | 会話のような低遅延応答が必要か、数分かけてレポートや動画を生成する非同期処理でよいか |
| 精度の深さ | 専門特化ツール(画像生成ならMidjourney、音声合成ならElevenLabs、動画編集ならRunway・HeyGen等)と比べたときの品質差をどこまで許容できるか |

### 統合モデル vs 専門特化ツールの使い分け

| 場面 | 向いている選択 | 理由 |
|---|---|---|
| 会議のホワイトボードを撮って議事録化したい、画面を見せながら音声で相談したい | 統合(Omni)モデル | 画像・音声・テキストを1つの文脈でまとめて扱えるため、やり取りが自然でシステム連携もシンプル |
| 広告用の高品質なビジュアルを作り込みたい | 画像生成特化ツール(Midjourneyなど) | 構図・画風の作り込みにおいて専門ツールの表現力・制御性が勝る場合が多い |
| 社内システムに「画像+テキスト+音声」を1回のAPIリクエストでまとめて渡し、複数のツールを組み合わせる手間を省きたい | 統合(Omni)モデルのAPI(Realtime API、Gemini Live API等) | 1つのモデル呼び出しで完結し、モダリティ間で情報を受け渡す実装の手間が減る |
| 簡単な社内動画(既存素材のカット編集・ナレーション差し替え)をノーコードで手早く作りたい | Gemini Omni(Google Vids等) | 自然言語の指示だけで動画編集ができ、専用ソフトの操作を覚える必要がない |
| 動画の最終的な編集・仕上げの精度、または本人そっくりのアバター・音声クローンを慎重に扱いたい | 動画生成・編集特化ツール(Runway、Kling等)+人手・法務による確認 | 生成AIは下地・叩き台作りには強いが、最終品質の細部調整や肖像・声の権利確認はまだ専門ツールや人手に分がある場面が多い |

## 実務での使い方

### 主要ツールでの対応付け(2026年9月時点)

| 提供元 | Omni・統合マルチモーダル機能 | 入り口 |
|---|---|---|
| OpenAI | 最上位モデル「GPT-6 Astra」(2026年9月GA)はテキスト+画像入力まで(音声・動画は非対応)。ChatGPTの音声体験「GPT-Live」(2026年7月8日〜、Astraとは別建て)、開発者向けRealtime API(gpt-realtime-2.1)、下位のGPT-5.6ファミリー(Luna/Terra/Sol)がネイティブマルチモーダルとして併存 | ChatGPTアプリの音声モード(有料プランはGPT-Liveがデフォルト)。カメラ映像・画面共有が必要な場合は引き続き旧Advanced Voice Modeを利用。開発者はRealtime APIで音声・画像入力を実装 |
| Google | Gemini Omni / Gemini Omni Flash、Gemini Live API | Geminiアプリの「Live」機能でカメラ映像+音声のリアルタイム対話、Google Vids・Google Flow・YouTube Shortsでの動画生成・編集。開発者向けの`gemini-omni-flash-preview`エンドポイントは2026年9月30日に廃止予定のため、後継エンドポイントへの移行を要確認 |
| Alibaba(API提供・ウェイト非公開) | Qwen3.8-Omni-Flash(2026年9月18日公開。1Mトークンコンテキスト、動画・音声・画像・テキストをネイティブ入力、出力はテキストのみ) | QwenCloud・Alibaba Cloud Model Studio・Qwen Studio経由のAPI利用。自社サーバーでの実行(セルフホスト)には非対応 |
| Alibaba(オープンウェイト) | Qwen3.5-Omni(Plus/Flash/Light、前世代) | Hugging FaceからモデルをダウンロードしてOllama等のローカル実行環境で利用([ローカルLLMの基本](../part08-specialized-ai-tools/local-llm-basics.md)を参照) |
| Anthropic | Claude Fable 5.1・Opus 5・Sonnet 5。画像・文章理解に対応(音声・動画のネイティブ生成は非対応、2026年9月時点)。音声モードは外部TTS(ElevenLabs)経由の二段階構成。生成した画像・音声・動画ファイルにはC2PA Content Credentialsが付与される | Claude.aiやAPIで画像をアップロードして読み取らせる用途が中心。Claudeアプリの音声モードはOpus/Sonnetベースで動作(2026年7月23日〜) |
| xAI | Grok 4.6(テキスト・推論)+ Grok Voice(文字起こし新版「grok-voice-transcribe-2.0」を選択可能、既定は旧版)+ Grok Imagine(画像生成の旧モデルは2026年11月2日に提供終了予定、「grok-imagine-image-2.0」へ移行)というモデル分割型 | grok.com・XアプリのGrok機能から個別に利用 |

### コピペで使える実例:画像+テキストでの現場報告の一次整理

現場の写真とメモ書きを組み合わせて、そのまま報告書の下書きにする指示例。

```
以下の写真と手書きメモから、現場報告の下書きを作成してください。

【写真】(ここに現場の写真を添付)
【手書きメモの内容】(ここにメモの内容、または写真自体を添付)

## 含めてほしい項目
- 状況の概要(写真から読み取れる事実のみ)
- 気づいた懸念点
- 次に取るべきアクション案

## 注意
- 写真やメモから読み取れない情報は「不明」とし、憶測で補わないこと
```

### 業務シナリオの例:カメラ+音声を使った一次対応の効率化

1. 修理・点検の現場でスマートフォンのカメラを対象物に向けながら、GPT-LiveやGemini Liveなどの音声モードで「型番と、目視できる損傷箇所を教えて」と話しかける
2. Omniモデルが映像と音声を同時に処理し、型番の読み取りと損傷箇所の説明を音声・テキストで返す(ネイティブ音声処理のため、相槌を打ちながらの対話も可能)
3. その場で得られた情報をもとに、応急対応が必要か・持ち帰って専門家に確認するかを判断する
4. やり取りの記録(画像・音声認識結果)を業務システムに残し、後で人がレビューする

### コストの目安(2026年9月時点)

リアルタイム音声を開発者APIで使う場合の単価は、通常のテキストチャットとは別体系になっていることが多い。本番導入前に想定利用量で試算しておく。

| API | 目安単価 |
|---|---|
| OpenAI Realtime API(gpt-realtime-2.1) | 音声入力 $32/100万トークン、音声出力 $64/100万トークン(mini版は$10/$20) |
| Google Gemini Live API(Gemini 3.1 Flash Live等) | 音声入力 約$3/100万トークン、音声出力 約$12/100万トークン |
| Qwen3.8-Omni-Flash(Alibaba、テキスト・画像・音声・動画入力/テキスト出力) | 入力$0.15/100万トークン、出力$0.47/100万トークン(キャッシュ利用時の入力は$0.016)。前世代Qwen3.5-Omni-Plus比で音声入力の時間単価が98%、音声+動画の組み合わせで93%安いとされる |

いずれもキャッシュ(直前の会話文脈の再利用)を効かせると実質単価は大きく下がるため、頻繁に同じコンテキストで呼び出す設計にするとコストを抑えやすい。

## 注意点・よくある誤解

- **「Omniモデル」と「対話の入り口」は別物になりつつある**: OpenAIのGPT-6 Astraのように、最上位の推論モデル自体はテキスト+画像までしか受け付けず、音声対応は別建てのGPT-Liveが担う、という「モデルと窓口の分離」が2026年9月以降に目立つようになった。「最上位モデル=すべてのモダリティに対応」と思い込まず、実際にどの入力・出力をどのモデル(またはモデルの組み合わせ)が処理しているかを確認する。
- **「対応モダリティ」の宣伝文句を鵜呑みにしない**: 入力として受け付けられるモダリティと、出力として生成できるモダリティは別物であり、モデルごとに組み合わせが異なる。導入前に必ず自社のユースケースに必要な入出力の組み合わせを具体的にテストすること。
- **Preview版のAPIエンドポイントは廃止予告に注意する**: Google の`gemini-omni-flash-preview`のように、プレビュー扱いのマルチモーダルAPIエンドポイントは数か月単位で廃止・後継への統合が行われる。本番システムに直接組み込んでいる場合は、各社の変更履歴(チェンジログ)を定期的に確認し、廃止予告が出た時点で移行作業を計画する。
- **「ネイティブ音声」か「TTSを挟む二段階」かを見分ける**: 同じ「音声で話せる」でも、GPT-LiveやGemini Liveのように音声を音声のまま処理する方式と、Claudeの音声モードのように音声認識→テキスト処理→外部TTSという二段階構成の方式では、割り込み・相槌の自然さやレイテンシに差が出る。カスタマーサポートのような自然な対話品質が重要な用途では、この違いを実機で確認してから選ぶ。
- **リアルタイム処理はコストが跳ねやすい**: 音声・動画をリアルタイムで処理する機能は、通常のテキストチャットに比べて課金の単位や単価が異なる(音声トークンは一般にテキストトークンより高単価、動画は処理するフレーム数に応じて課金されるなど)。前述の単価目安を参考に、本番導入前に想定利用量でのコスト試算を行う。
- **専門特化ツールの品質にはまだ及ばない場面がある**: 統合モデルは「1つのモデルで何でもできる」利便性が強みである一方、画像・動画・音声それぞれの最終的な仕上がり品質では、専門特化ツールに分がある場面がまだ多い。「下書き・叩き台は統合モデルで素早く」「最終仕上げは専門ツールや人手で」という役割分担が現実的。
- **誤認識が複数モダリティに連鎖するリスク**: 画像の誤認識が誤った音声応答やその後のアクションに連鎖するなど、モダリティをまたいだハルシネーションは気づきにくい。重要な判断に使う場合は、元の画像・音声を人が確認する工程を残す。
- **カメラ・マイク常時利用、そして「声・外見のクローン」にはプライバシー・肖像権配慮が必要**: ライブ映像・音声を継続的に送る機能は、意図せず映り込む第三者や周囲の会話まで送信してしまう可能性がある。加えて、Google Vidsのパーソナルアバターのように本人の声・外見を再現する機能は、なりすまし・ディープフェイクのリスクにも直結する。利用場所・利用範囲を限定し、本人の同意取得プロセスを社内ルールとして事前に整備する。

## 最初の一歩

ChatGPTの「GPT-Live」またはGeminiアプリの「Live」機能を使い、身近な業務(ホワイトボードの内容を映しながら要点をまとめてもらう、資料を見せながら説明を求めるなど)を1つ試して、テキストだけのやり取りや従来の音声モードとの違い(相槌・割り込みの自然さ)を体感してみる。

## 関連トピック

- [モデルの種類と選び方(マルチモーダル・パラメータ数・SLM・VLM)](../part02-llm-basics/model-types-and-selection-basics.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [ChatGPTの画像生成機能](../part03-ai-chat-tools/chatgpt-image-generation-feature.md)
- [ローカルLLMの基本(自社PC・サーバーで動かす生成AI)](../part08-specialized-ai-tools/local-llm-basics.md)

## 更新履歴

### 2026-09-21: GPT-6 Astra・Qwen3.8-Omni-Flashなど2026年9月時点の各社動向に最新化
- **内容**: OpenAIの最上位モデルが「GPT-5.6」から世代交代モデル「GPT-6 Astra」(2026年9月3日発表)に切り替わったことを反映し、Astra自体はテキスト+画像入力のみで音声・動画には非対応であること、ChatGPTの音声体験「GPT-Live」はAstraとは別建てのモデルであることを明記(「モデルと対話の窓口が分離する」という新しい注意点を追加)。Googleの節に、開発者向け`gemini-omni-flash-preview`エンドポイントが2026年9月30日に廃止予定であることを追記。AnthropicはClaude Fable 5.1(9月1日)への更新を反映し、生成ファイルにC2PA Content Credentialsが付与される点を追加。xAIはGrok 4.6への更新、Grok Voice文字起こし新版「grok-voice-transcribe-2.0」、Grok Imagine旧モデルの2026年11月2日提供終了予告を反映。オープンウェイト系の節を、Alibabaが2026年9月18日に公開した非公開ウェイトの新モデル「Qwen3.8-Omni-Flash」(1Mトークン、動画・音声ネイティブ入力、前世代比で音声コスト98%減)と、引き続きウェイトが公開されている前世代Qwen3.5-Omniの2本立てに整理。コスト目安表にQwen3.8-Omni-Flashの単価を追加し、注意点にAPIエンドポイントの廃止予告への対応を追加
- **出典**: [OpenAI公式X投稿: GPT-6 Astra rollout](https://x.com/OpenAI/status/2095595757072191802)、[llm-stats.com: GPT-6 Astra Benchmarks, Pricing & Context Window](https://llm-stats.com/models/gpt-6-astra)、[CNBC: OpenAI announces rollout of GPT-6 Astra model](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)、[Google AI for Developers: Release notes | Gemini API](https://ai.google.dev/gemini-api/docs/changelog)、[Google Workspace Blog: Gemini Omni Flash now available in Google Vids](https://workspace.google.com/blog/product-announcements/introducing-gemini-omni-flash-in-google-vids)、[MarkTechPost: Anthropic Releases Claude Fable 5.1 and Claude Mythos 5.1](https://www.marktechpost.com/2026/09/01/anthropic-releases-claude-fable-5-1-and-claude-mythos-5-1-52-6-on-terminal-bench-science-and-75-cheaper-cache-reads/)、[Claude Platform Docs: What's new in Claude Fable 5.1](https://platform.claude.com/docs/en/models/fable-5-1/whats-new-fable-5-1)、[x.ai: Release Notes](https://docs.x.ai/developers/release-notes)、[TechNode: Alibaba's Qwen releases Qwen3.8-Omni-Flash with 1M-token context](https://technode.com/2026/09/18/alibabas-qwen-releases-qwen3-8-omni-flash-with-1m-token-context/)、[MarkTechPost: Alibaba Qwen Releases Qwen3.8-Omni-Flash](https://www.marktechpost.com/2026/09/18/alibaba-qwen-releases-qwen3-8-omni-flash/)
- **注記**: GPT-6 Astra自体の音声・動画対応の有無は2026年9月時点の複数メディア報道に基づく。ChatGPTの音声体験(GPT-Live)は別モデルで提供されているため、「Astraが音声非対応」であることと「ChatGPTで音声が使えない」ことは同義ではない点に注意

### 2026-08-02: 2026年8月時点の各社動向に最新化
- **内容**: OpenAI GPT-5.6(Sol/Terra/Luna)とChatGPTの新音声体験「GPT-Live」、Google Gemini OmniのGoogle Vids統合(パーソナルアバター含む)とGemini 3.5/3.6 Flashの状況、Anthropic Claude Opus 5/Sonnet 5/Fable 5が依然として画像・音声・動画のネイティブ生成に非対応であること、xAIが単一Omniではなくモデル分割型(Grok 4.5+Grok Voice+Grok Imagine)を採る点、Qwen3.5-OmniがオープンウェイトOmniモデルとして最新である点を反映。「ネイティブ音声処理か外部TTSの二段階か」という新しい選定軸と、Realtime API・Gemini Live APIの具体的な単価を追加
- **出典**: [OpenAI: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)、[OpenAI: GPT-5.6](https://openai.com/index/gpt-5-6/)、[9to5Mac: OpenAI upgrading ChatGPT with all-new voice mode experience](https://9to5mac.com/2026/07/08/openai-upgrading-chatgpt-with-all-new-voice-mode-experience-watch-here/)、[apidog: GPT-Live vs Advanced Voice Mode](https://apidog.com/blog/gpt-live-vs-advanced-voice-mode/)、[HackerNoon: OpenAI Realtime API Pricing in 2026](https://hackernoon.com/openai-realtime-api-pricing-in-2026-real-world-data-from-4000-measured-sessions)、[Google Workspace Updates Blog: Generate higher quality AI video clips and edit any video with Gemini Omni in Vids](https://workspaceupdates.googleblog.com/2026/07/generate-higher-quality-ai-video-clips-and-edit-any-video-with-Gemini-Omni-in-Vids.html)、[HelenTech: Google Vids に Gemini Omni が追加](https://helentech.jp/news-google-vids-gemini-omni-personal-avatars-88796/)、[CometAPI: Gemini 3.5 Pro Release Date](https://www.cometapi.com/gemini-3-5-pro-release-date-rumored-specifications-all-we-know-in-2026-updated-july-2026/)、[MarkTechPost: Meet the New Claude Opus 5](https://www.marktechpost.com/2026/07/24/meet-the-new-claude-opus-5-frontier-class-agentic-coding-and-computer-use-at-unchanged-opus-pricing/)、[MLQ News: Anthropic Expands Claude Voice Mode to Opus and Sonnet Models](https://mlq.ai/news/anthropic-expands-claude-voice-mode-to-opus-and-sonnet-models/)、[TechCrunch: Anthropic updates Claude voice mode with more capable models](https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/)、[felloai: Can Claude Generate Images?](https://felloai.com/can-claude-generate-images/)、[cryptobriefing: Grok Imagine upgrades bring voice consistency, native 1080p video](https://cryptobriefing.com/grok-imagine-voice-consistency-text-to-video/)、[x.ai: Introducing Grok Voice Think Fast 2.0](https://x.ai/news/grok-voice-think-fast-2)、[GitHub: QwenLM/Qwen3-Omni](https://github.com/QwenLM/Qwen3-Omni)、[Constellation Research: Alibaba's Qwen launches new flagship LLM with Qwen 3.6-Plus](https://www.constellationr.com/insights/news/alibabas-qwen-launches-new-flagship-llm-qwen-36-plus)

### 2026-07-07: 初版執筆
- **内容**: ネイティブ・マルチモーダルモデルの仕組みとパイプライン型との違い、GPT-4oを起点とした経緯、2026年のGemini Omni・Qwen3.5-Omniなど「Omniモデル」の動向、統合モデルと専門特化ツールの使い分け基準、主要ツールの対応表、業務シナリオ例を整理
- **出典**: [Framia: GoogleがGemini Omni統合マルチモーダルAIモデルを発表](https://framia.converge.ai/page/ja-JP/news/gemini-omni-ai-video-seisei-model)、[Apiyi: Decoding Qwen3.5-Omni Native Multimodal Model](https://help.apiyi.com/en/qwen3-5-omni-multimodal-model-text-audio-video-realtime-en.html)、[Michael Brenndoerfer: GPT-4o: Unified Multimodal AI with Real-Time Speech, Vision, and Text](https://mbrenndoerfer.com/writing/gpt4o-unified-multimodal-ai-real-time-speech-vision-text)、[モンスターラボ: マルチモーダルAIとは？仕組み・代表モデル・活用事例](https://monstar-lab.com/dx/technology/about-multimodal-ai/)、[teamai: GPT-5 vs Claude 4 vs Gemini 3: 2026 AI Benchmark Showdown](https://teamai.com/blog/large-language-models-llms/the-2026-ai-frontier-model-war-2/)
