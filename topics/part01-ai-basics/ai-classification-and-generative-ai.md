---
title: AIの分類と生成AIの位置づけ
part: 1
chapter: 第1章 人工知能とは
tags: [AI基礎, 生成AI, 機械学習, ディープラーニング, エージェントAI]
created: 2026-07-04
updated: 2026-07-21
---

# AIの分類と生成AIの位置づけ

## これは何か

「AI」「機械学習」「生成AI」という言葉は、しばしば同じ意味であるかのように使われるが、実際には範囲の異なる入れ子構造になっている。この関係を理解していないと、「AIを導入する」と言われたときに、それが需要予測のような裏方の仕組みなのか、ChatGPTのような文章を作るツールなのかが噛み合わず、ツール選定や社内説明で無駄な手戻りが発生する。

## 仕組み・背景

AIの分類は、大きく次の入れ子構造で整理できる。

**AI ⊃ 機械学習 ⊃ ディープラーニング(深層学習) ⊃ 生成AI**

- **AI(人工知能)**: 人間の知的活動をコンピュータで模倣する技術・システムの総称。最も広い概念。
- **機械学習**: AIの一種で、人間がルールを逐一プログラムするのではなく、データからパターンやルールをAI自身に学習させるアプローチ。
- **ディープラーニング**: 機械学習の一種で、人間の脳の神経回路を模した「ニューラルネットワーク」を多層に重ねる手法。画像認識や自然言語処理の精度を飛躍的に高めた。
- **生成AI**: ディープラーニングを用いて、学習データにはない新しいコンテンツ(文章・画像・音声・動画・コードなど)を作り出すAI。ChatGPTやClaude、Geminiなどが該当する。

この階層とは別に、「何をするAIか」という機能面での分類軸もある。

- **ルールベースAI**: 人間があらかじめ決めた条件・ルールに従って判断する。判断根拠が明確で予測可能だが、想定外の状況への対応力は乏しい。
- **機械学習AI(識別・予測系)**: データから自動でパターンを見つけ、分類・予測・判別を行う。顔認証、需要予測、スパム判定、与信スコアリングなどが代表例。判断精度は高いが、「なぜその結果になったか」が見えにくい(ブラックボックス性)という弱点がある。
- **生成AI**: 分類・予測ではなく、新しいアウトプットそのものを作り出す。識別系AIが「既存データを判断するAI」だとすれば、生成AIは「新しいデータを作るAI」であり、両者は目的が根本的に異なる。

実務では両者が組み合わさることも多い。たとえば社内チャットボットは、ユーザーの質問意図を機械学習(識別系)で把握し、回答文そのものは生成AIで作る、という役割分担になっている。2026年時点でも「ルールベース+機械学習+生成AI(LLM)を組み合わせ、ルールで担保する透明性と機械学習・生成AIの柔軟性をどうバランスさせるか」が実務での基本的な設計思想であり、3者は対立する選択肢ではなく併用が前提になっている。

さらに2025年後半以降は、生成AI(LLM)を土台にしつつ「目標(ゴール)だけを渡せば、手順の計画・外部ツールの呼び出し・結果確認までを自律的にループさせる」**エージェントAI(エージェンティックAI)**という発展形が実務に広がっている。生成AIが「1回の指示に対して1回の出力を返す」のに対し、エージェントAIは「ゴール達成まで複数ステップを自分で回し続ける」点が異なり、両者は同じ生成AI(LLM)の技術を使いながら「振る舞い方」で区別される。詳細は[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)を参照。

## 使いどころ・使い分け

| 目的 | 向いているAIの種類 | 具体例 |
|---|---|---|
| 判断基準が明確な定型処理を自動化したい | ルールベースAI | 経費精算の申請ルールチェック、在庫の自動発注 |
| 過去データから未来の数値や分類を予測したい | 機械学習(識別・予測系) | 需要予測、解約予兆検知、不正取引検知 |
| 判断根拠の説明責任が重い(監査・規制対応) | ルールベース or 説明可能な機械学習 | 与信審査、医療診断支援 |
| ゼロから文章・画像・コードなどを作りたい | 生成AI | 提案書のドラフト作成、バナー画像制作、コード雛形の生成 |
| 複数ステップの作業をゴールだけ渡して任せたい | エージェントAI(生成AIの発展形) | 複数サイトを横断した情報収集、フォーム入力の代行、コーディングの自律実行 |

「AIを使う」という会話が噛み合わないときは、まずこの表のどの列の話をしているのかを揃えると議論が早い。特に、生成AIはブラックボックス性が高く出力の正確性を保証できないため、法的・財務的に重い最終判断を生成AIだけに委ねるのは避け、ルールベースや人によるチェックと組み合わせるのが基本方針になる。

## 実務での使い方

生成AIはさらに、作り出すコンテンツの種類(モダリティ)で分類すると理解しやすい。自社でツールを選ぶ際の見取り図として使える。

| モダリティ | 代表的なサービス例(2026年7月時点) |
|---|---|
| テキスト生成 | ChatGPT(OpenAI、GPT-5.5系列)、Claude(Anthropic、Sonnet 5/Opus 4.8/Fable 5)、Gemini(Google、Flash/Pro) |
| 画像生成 | Midjourney(V7)、Adobe Firefly、Google Gemini(Nano Banana Pro/2/2 Lite)、ChatGPT(GPT Image、旧DALL-E 3から2026年5月に切り替え) |
| 動画生成 | Google Veo 3.1、Runway(Gen-4.5)、Kling AI(Kling 3.0)、Luma Dream Machine(Ray3) |
| 音声・音楽生成 | ElevenLabs(音声合成・音声クローン)、Suno / Udio(ボーカル入り楽曲の作曲) |
| コード生成 | GitHub Copilot、Cursor など |

各モダリティの詳しい比較・選び方は[画像生成AIの基本](../part08-specialized-ai-tools/image-generation-ai-basics.md)、[動画生成AIの基本](../part08-specialized-ai-tools/video-generation-ai-basics.md)、[音声・音楽生成AIの基本](../part08-specialized-ai-tools/audio-music-generation-ai-basics.md)を参照。なお動画生成AIの代表格だったOpenAI Soraは、2026年4月26日にアプリ提供が終了し、API自体も2026年9月24日に提供終了予定と発表されている。「有名だから」で代表例を固定せず、新規導入時は現行サービスかどうかを都度確認する必要がある好例と言える。

2026年時点では、これらのモダリティを1つのモデルで横断的に扱う「マルチモーダルAI」がさらに進み、ChatGPTやGemini、Claudeは標準でテキスト・画像・音声を統合的に扱えるようになっている。ツールを比較検討する際は、「テキストだけで十分か」「画像や音声も含めて1つのツールに集約したいか」を軸に選ぶとよい。

## 注意点・よくある誤解

- **「AI=生成AI」ではない**: 社内で以前から使われている需要予測システムやレコメンドエンジンも広義のAIであり、ChatGPTのような生成AIとは別物。導入検討の際にこれらを混同すると、既存システムとの役割分担を誤る。
- **生成AIは万能の判断者ではない**: 生成AIは「作る」ことに強いが、「正しいかどうかを判定する」ことは本質的な得意分野ではない。誤った情報をもっともらしく生成する(ハルシネーション)リスクは常にあるため、重要な判断は人が最終確認する運用が前提になる。
- **説明可能性のトレードオフを意識する**: ルールベースAIは判断根拠が明確な分、柔軟性に欠ける。生成AI・機械学習は柔軟だが説明が難しい。規制業種(金融・医療・人事評価など)では、この特性差が採用可否に直結する。
- **「生成AI」と「エージェントAI」を混同しない**: 生成AIは「1回の指示に1回の出力」で完結するのに対し、エージェントAIは同じ生成AI(LLM)を使いながら複数ステップの作業を自律的に回し続ける。エージェントAIは出力の質だけでなく、外部システムを実際に操作する分の運用リスク(誤操作・権限管理)も増える点に注意する
- **モダリティ別の代表ツールは半年〜1年でも入れ替わる**: OpenAI Soraのように2026年に入って提供終了が決まったサービスもあれば、Google「Nano Banana」シリーズのように同一ブランド内でモデルが数か月おきに更新されるケースもある。社内資料・研修教材に固有のツール名・モデル名を書いたら、半年に一度は現行かどうかを見直す運用にする

## 最初の一歩

自社や自分の業務で「AIを使っている(使いたい)」場面を1つ思い浮かべ、それが「判断・予測」なのか「新規コンテンツの作成」なのかを仕分けてみる。後者であれば、まずはChatGPTかGeminiで試してみるのが手軽な第一歩になる。

## 関連トピック

- [機械学習の基礎(教師あり学習・教師なし学習・強化学習)](machine-learning-basics.md)
- [ディープラーニング(深層学習)の基礎](deep-learning-basics.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [画像生成AIの基本](../part08-specialized-ai-tools/image-generation-ai-basics.md)
- [動画生成AIの基本](../part08-specialized-ai-tools/video-generation-ai-basics.md)
- [音声・音楽生成AIの基本](../part08-specialized-ai-tools/audio-music-generation-ai-basics.md)

## 更新履歴

### 2026-07-21: モダリティ別の代表サービス例を現行世代に更新し、エージェントAIとの関係を追加
- **内容**: テキスト・画像・動画・音声生成の代表サービス例をGPT-5.5系列/Claude Sonnet 5・Opus 4.8・Fable 5/Gemini Flash・Pro、Nano Banana Pro/2/2 Lite、Google Veo 3.1・Runway Gen-4.5・Kling 3.0、ElevenLabs・Suno/Udioなど2026年7月時点の世代に更新。OpenAI Soraのアプリ提供終了(2026年4月26日)・API提供終了予定(2026年9月24日)を「代表例も入れ替わる」実例として明記。生成AIの発展形である「エージェントAI(エージェンティックAI)」との違いを仕組み・使いどころ・注意点の各節に追加し、関連トピックを実在ページへのリンクに差し替え。ルールベース/機械学習/生成AIの3分類の枠組み自体は2026年7月時点でも通用することをWeb検索で再確認した
- **出典**: [JAPAN AI ラボ: ルールベース型AIとは？仕組み・機械学習との違い・活用事例まで解説](https://japan-ai.co.jp/media/7009/)、[OvalEdge: Agentic AI vs Generative AI: Key Differences, Use Cases & How to Choose in 2026](https://www.ovaledge.com/blog/agentic-ai-vs-generative-ai)、[OpenAI Help Center: What to know about the Sora discontinuation](https://help.openai.com/en/articles/20001152-what-to-know-about-the-sora-discontinuation)、[Anthropic: Building Effective AI Agents](https://www.anthropic.com/research/building-effective-agents)(本リポジトリの[画像生成AIの基本](../part08-specialized-ai-tools/image-generation-ai-basics.md)・[動画生成AIの基本](../part08-specialized-ai-tools/video-generation-ai-basics.md)・[音声・音楽生成AIの基本](../part08-specialized-ai-tools/audio-music-generation-ai-basics.md)・[Claude(Anthropic)の基本](../part03-ai-chat-tools/claude-basics.md)・[Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)で既に裏取り済みのモデル名・料金情報も参照)

### 2026-07-04: 初版執筆
- **内容**: AIの分類階層(AI/機械学習/ディープラーニング/生成AI)、ルールベースAIと機械学習AIの違い、識別系AIと生成系AIの違い、モダリティ別の代表サービスを整理
- **出典**: [マネーフォワード クラウド](https://biz.moneyforward.com/ai/basic/649/)、[Microsoft AI 101](https://www.microsoft.com/en-us/ai/ai-101/generative-ai-vs-other-types-of-ai)、[Hakky Handbook](https://book.st-hakky.com/data-science/difference-between-rule-based-and-ml)、[クラウドコンタクトセンター](https://www.cloud-contactcenter.jp/blog/explanation-of-what-generative-ai-is.html)、[aismiley](https://aismiley.co.jp/ai_news/generative-ai-compare/)
