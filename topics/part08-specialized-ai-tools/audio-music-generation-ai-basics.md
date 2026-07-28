---
title: 音声・音楽生成AIの基本(Suno・Udio・ElevenLabsなどの選び方)
part: 8
chapter: 第3章 画像・動画・音声の生成AI
tags: [Suno, Udio, ElevenLabs, 音楽生成AI, 音声合成, 音声クローン, TTS]
created: 2026-07-06
updated: 2026-07-27
---

# 音声・音楽生成AIの基本(Suno・Udio・ElevenLabsなどの選び方)

## これは何か

「動画のBGMが欲しい」「研修動画にナレーションを付けたい」というとき、
作曲家やナレーターを毎回手配するのはコストも時間もかかる。
音声・音楽生成AIは、テキストや簡単な指示だけで**楽曲**や**人間の声のような音声**を
数十秒〜数分で作り出すツール群で、この「素材調達」の手間を大きく減らせる。

このジャンルは大きく2系統に分かれる。

- **音楽生成AI**: 歌詞やジャンルを指定するとボーカル入りの楽曲をゼロから作曲する
  (代表: Suno、Udio)
- **音声合成・音声クローンAI**: テキストを自然な音声に変換したり、
  特定の人の声を学習して同じ声で新しい台詞を話させたりする
  (代表: ElevenLabs)

両者は「何を入力し、何を出力するか」がまったく異なるため、
用途に応じて使い分ける必要がある。

## 仕組み・背景

いずれも拡散モデル(diffusion model、ノイズから徐々に目的の出力を生成する仕組み)や
Transformer系の生成モデルを音声波形・音声トークンに応用したもので、
画像生成AIと同様に「大量の音声データで学習し、テキストなどの条件を与えて
それらしい音声を生成する」という原理は共通している。

- **Suno / Udio**: 歌詞テキストとジャンル・雰囲気の指示(プロンプト)を入力すると、
  イントロ・Aメロ・サビ・アウトロといった構成を持つ完成度の高い楽曲を
  ボーカル込みで一括生成する。人間の作曲家のように「メロディ」「歌詞」「演奏」を
  個別に作るのではなく、曲全体を1つの生成タスクとして出力する点が特徴
- **ElevenLabs**: 入力テキストを読み上げる音声合成(TTS: Text-to-Speech)が中核機能。
  さらに「音声クローン」機能では、数十秒〜数分の音声サンプルから
  その人の声質・話し方の特徴を学習し、以後は任意のテキストをその声で
  読み上げさせられる

2024年6月、Suno・UdioはRIAA(全米レコード協会)を通じてユニバーサル・ソニー・
ワーナーの主要レーベルから「著作権のある音源を無許可でAI学習に使用した」として
提訴された。この訴訟は2026年7月時点で「和解して手を組む陣営」と「訴訟を継続する陣営」に
分かれている。

- **Udio**: ユニバーサル(2025年10月)、ワーナー(2025年11月)に続き、インディーズ
  レーベル連合Merlin(2025年12月)、音楽出版のKobalt(2026年1月)ともライセンス契約で
  和解した。ソニーのみ訴訟を継続中。和解の一環として、UMGとUdioは参加アーティストの
  楽曲だけを使った新しい会員制プラットフォームを2026年前半までに構築し、
  既存のUdioは移行期間を経て段階的にこちらへ置き換わる予定になっている。
  新プラットフォームでは生成した楽曲を**ダウンロード・外部プラットフォームへの
  書き出しができない**「囲い込み型」の設計が特徴で、既存ユーザーは移行完了までの間は
  従来のプラン・ダウンロード機能を引き続き使える
  [出典](https://www.billboard.com/pro/umg-udio-ai-deal-faq-artist-payments-user-downloads-lawsuit/)
- **Suno**: ワーナーとは2025年10月にライセンス契約で和解したが、ソニー・ユニバーサルとは
  和解しておらず訴訟が継続中。2026年5月には対象楽曲数が560曲から61,026曲に拡大され、
  「著作権のある音源での学習が公正利用(フェアユース)にあたるか」を争点とする
  サマリージャッジメント(略式判決)審理がマサチューセッツ連邦地裁で2026年7月に
  予定されている。本稿執筆時点(2026年7月27日)ではまだ判決は出ていないが、
  AI音楽生成の学習データの適法性を占う判例になる可能性が高い
  [出典](https://www.techtimes.com/articles/320139/20260710/ai-music-training-hits-two-courts-july-suno-faces-verdicts-munich-boston.htm)

さらに2026年6月には、米国音楽家組合(AFM)がユニバーサル・ワーナー両社を提訴した。
レーベル側はSuno・Udioとの和解で対価を得た一方、実際に演奏した個々のミュージシャンには
契約上の「新規用途」条項に基づく補償・クレジットが支払われていないという主張で、
「レーベルが学習データをライセンスした」ことと「関係者全員が納得・補償されている」ことは
イコールではない点を浮き彫りにしている
[出典](https://www.musicbusinessworldwide.com/musicians-union-sues-umg-and-warner-music-alleging-member-recordings-were-licensed-to-suno-and-udio-without-compensation-or-credit/)。
この経緯は「AI生成音楽の学習データの合法性」がまだ完全には確定していないことを示しており、
業務利用の際は下記「注意点」で扱う商用利用条件の確認が欠かせない。

## 使いどころ・使い分け

まず「楽曲を作りたいのか、声を作りたいのか」で系統を選ぶ。

| 目的 | 向いているツール系統 | 具体例 |
|---|---|---|
| BGM・ジングル・テーマソングを作りたい | 音楽生成AI(Suno / Udio) | YouTube動画のBGM、店舗のオリジナルテーマ曲、CMのジングル |
| 原稿を音声化したい(ナレーション) | 音声合成AI(ElevenLabs等) | 研修動画・eラーニングのナレーション、記事の音声読み上げ |
| 特定の人物の声で話させたい | 音声クローンAI(ElevenLabs等) | 社長メッセージの多言語版、キャラクターボイスの量産 |
| 動画を多言語に吹き替えたい | 音声合成AI+翻訳(Dubbing機能) | 海外展開する製品紹介動画のローカライズ |

音楽生成AI同士(Suno vs Udio)の使い分けの目安。

| 観点 | Suno | Udio |
|---|---|---|
| ボーカル・歌詞の再現力 | 高い。日本語歌詞も比較的自然([出典](https://n1-inc.co.jp/suno-ai-nihongo/)) | やや硬い場面があるが音質面で評価される([出典](https://www.matrixflow.net/case-study/137/)) |
| 生成後の編集機能 | ステム分割(ボーカル/楽器を最大12パートに分離)、ボーカル・伴奏の後付け | Voice Control(声質の微調整)、Style Blending、Inpaint(部分的な再生成)など編集の自由度が高い([出典](https://www.eesel.ai/blog/udio-pricing)) |
| 最新モデル・機能 | v5.5(2026年3月)で「Voices」「Custom models」「My Taste」などパーソナライズ機能を追加。2026年7月にはLyrics(歌詞)入力画面を刷新し、曲の長さを指定する「Duration」スライダーも追加された([出典](https://suno.com/blog/v5-5)) | UMGとの和解に伴い、生成物のダウンロード・外部書き出しができない会員制プラットフォームへの移行を2026年中に予定(詳細は前節参照) |
| 無料プランの商用利用 | 不可(有料プランのみ) | 不可(有料プランのみ) |
| 向いている使い方 | とにかく手早く「使える1曲」を仕上げたい | 生成後に細部を追い込みたい、ブレンドで独自性を出したい |

業務で使う場合は、Udioが今後「生成した曲を社外に持ち出せない」設計へ移行する可能性がある点に
留意し、**BGMをダウンロードして動画に組み込む用途**には当面Sunoの方が運用しやすい。

「AIっぽさ」が完全には抜けないため、**企業のメインCMソングのような看板コンテンツ**には
人間の作曲家への発注、**社内動画・SNS用のBGM・叩き台**にはAI生成、という
二段構えが現実的な落としどころになる。

音声合成AIについては、汎用チャットAI(ChatGPT・Geminiなど)の読み上げ機能との違いも
押さえておきたい。汎用チャットAIの音声出力は「会話用の合成音声」で選択肢が少なく
声質のカスタマイズもできないのに対し、ElevenLabsは声のトーン・抑揚・多言語対応・
クローン作成まで踏み込める「素材制作用」のツールという位置づけになる。

## 実務での使い方

### Sunoの始め方と料金(2026年7月時点)

1. [suno.com](https://suno.com) にアクセスし、Googleアカウント等でサインアップ
2. 画面上部の「Create」から歌詞・ジャンル・雰囲気をテキストで指定して生成
3. 生成された楽曲はダウンロード、ステム分割、ボーカル/伴奏の差し替えが可能

| プラン | 料金(月払い/年払い) | クレジット | 生成可能数の目安 | 主な機能 | 商用利用 |
|---|---|---|---|---|---|
| Free | 無料 | 1日50クレジット | 1日あたり短い曲10曲程度 | 個人利用のみ | 不可 |
| Pro | $10/月(年払い$8/月) | 2,500/月 | 月500曲程度 | v5.5等の上位モデル、ステム分割(最大12パート)、30分までの音源アップロード、優先生成キュー | 可(出力の権利は利用者に帰属) |
| Premier | $30/月(年払い$24/月) | 10,000/月 | 月2,000曲程度 | Suno Studio(DAW的な編集画面)、Proの全機能 | 可 |

[出典](https://suno.com/pricing)

### Udioの始め方と料金(2026年7月時点)

1. [udio.com](https://www.udio.com) にアクセスしてサインアップ
2. プロンプト欄に曲の雰囲気・ジャンルを、Lyrics欄に歌詞を入力して生成
3. 生成後はVoice Control・Style Blending・Inpaintで部分修正が可能

| プラン | 料金(月額) | クレジット | 同時生成数 | 商用利用 |
|---|---|---|---|---|
| Free | 無料 | 月100(1日10) | 4曲まで並列 | 不可 |
| Standard | $10/月 | 2,400/月 | 6曲まで並列 | 可 |
| Pro | $30/月 | 6,000/月 | 高負荷・並列生成向け | 可 |

[出典](https://www.eesel.ai/blog/udio-pricing)

いずれもクレジットは基本的に翌月へ持ち越されない(購入した追加クレジットのみ失効しない)ため、
月内の使い切りを前提に容量を選ぶこと。

### ElevenLabsの始め方と料金(2026年7月時点)

ElevenLabsは単純なTTS(読み上げ)ツールから、ナレーション・動画・音楽・
カスタマーサポート用音声エージェントまでを1つのタイムラインで扱う
「音声・動画の総合制作基盤」へと役割を広げている。2026年時点では
制作画面「Studio 3.0」、会話AI機能「ElevenLabs Agents」、90以上の言語に対応する
「Dubbing v2」、静止画をリップシンク動画に変換する「Lipsync Video Synthesis」
などが主要機能として追加されている
([出典](https://blog.mean.ceo/elevenlabs-news-july-2026/))。

1. [elevenlabs.io](https://elevenlabs.io) でサインアップし、日本語UIも選択可能
2. 「Text to Speech」でテキストを入力し、声(Voice Library)を選んで生成。
   自分の声を使いたい場合は「Voices → Add Voice → Instant/Professional Voice Clone」から
   音声サンプルをアップロードして学習させる
3. 動画の多言語吹き替えは「Dubbing」機能にファイルをアップロードして言語を選択するだけで、
   翻訳・音声合成・リップシンクの調整まで一括処理される(Dubbing v2で対応言語が拡大)

| プラン | 料金(月額、年払いは実質2か月分無料) | クレジット | 音声クローン | 主な用途 |
|---|---|---|---|---|
| Free | $0 | 10,000 | 不可 | 機能を試す |
| Starter | $6(年払い実質$5) | 30,000 | Instant Voice Cloning(即席クローン)が利用可能 | 個人・小規模の商用利用 |
| Creator | $22(年払い実質$18.33) | 121,000 | Professional Voice Cloning(高精度クローン)が利用可能 | ナレーション制作、ポッドキャスト |
| Pro | $99(年払い実質$82.50) | 600,000 | 上記全て+API利用枠拡大 | 動画制作会社、代理業務 |
| Scale / Business | $299 / $990 | 180万 / 600万 | チーム共有、複数シート | 制作チーム・エンタープライズ |

[出典](https://bigvu.tv/blog/elevenlabs-pricing-2026-plan-worth/) /
[出典](https://flexprice.io/blog/elevenlabs-pricing-breakdown)

Instant Voice Cloning(即席クローン)は1〜2分程度のクリアな録音があれば作成できるが
長文では音質が揺れやすく、Professional Voice Cloning(専門クローン)は学習データが多く必要な分、
長尺のナレーションでも安定した声を再現できる。社内研修動画のナレーターを
毎回固定したい場合はProfessional Voice Cloningの利用が向く。

### コピペで使えるプロンプト例

**Suno/Udioでの社内向けBGM生成プロンプト例**

```
[Genre: Corporate, Uplifting]
[Mood: 前向きで落ち着いた、朝礼で流せる雰囲気]
[Tempo: 100 BPM前後]
[Instruments: ピアノ, アコースティックギター, 軽いパーカッション]
ボーカルなし、2分程度のインストゥルメンタル、
展示会ブースのBGMとして使うので同じフレーズが自然にループできる構成にしてください
```

**ElevenLabsでの研修動画ナレーション原稿の整え方**

```
【原稿ルール】
- 漢字の読みが一意でない語は、ふりがなまたはローマ字読みを( )で併記する
  例: 「相殺(そうさい)」「弊社(へいしゃ)」
- 1文は60文字以内に区切る(長文は不自然な息継ぎになりやすいため)
- 強調したい語の前に半角スペースを1つ入れて短いポーズを作る
```

### ツール横断の対応付け

| 機能 | Suno | Udio | ElevenLabs |
|---|---|---|---|
| 主目的 | 楽曲生成(ボーカル入り) | 楽曲生成(ボーカル入り) | 音声合成・音声クローン・吹き替え |
| 声を学習させる機能 | Personas(自分の生成曲から声質を継承) | Voice Control(声質の微調整) | Instant/Professional Voice Cloning |
| 多言語対応 | 主要言語+日本語対応 | 主要言語+日本語対応 | 訳・吹き替えまで含むDubbing機能(多言語) |
| 無料プランの商用利用 | 不可 | 不可 | 不可(Starter以上で可) |

## 注意点・よくある誤解

- **無料プランで作った曲・音声は商用利用できない**。後から有料プランに切り替えても、
  無料期間中に生成した分の商用利用は認められないため、business用途は最初から
  有料プランで生成すること
  [出典](https://aipicks.jp/mag/suno-guide-2026)
- **学習データの著作権問題は2026年7月時点でも未確定**。Udioはユニバーサル・ワーナー・
  Merlin・Kobaltと和解しライセンス済みモデルへの移行を進めているが、ソニーとの訴訟は
  継続中。Sunoはワーナーとのみ和解し、ソニー・ユニバーサルとの訴訟(対象曲は約61,000曲に
  拡大)は「学習が公正利用にあたるか」を争う段階に入っており、2026年7月に
  サマリージャッジメント審理が予定されている。さらに2026年6月には米国音楽家組合が
  レーベル側(ユニバーサル・ワーナー)を「和解金を得たのに演奏者本人には補償していない」
  として提訴しており、レーベルとの和解だけでは著作権・補償の論点が
  すべて解消したとは言えない状況が続いている。企業として広く配信するコンテンツに使う場合は、
  この動向を継続的に確認し、社内ガイドラインの著作権リスク管理と合わせて判断すること
  (関連: [生成AIの著作権リスクと実務での注意点](../part04-risk-security/copyright-risks-in-generative-ai.md))
  [出典](https://www.techtimes.com/articles/320139/20260710/ai-music-training-hits-two-courts-july-suno-faces-verdicts-munich-boston.htm)
  /
  [出典](https://www.musicbusinessworldwide.com/musicians-union-sues-umg-and-warner-music-alleging-member-recordings-were-licensed-to-suno-and-udio-without-compensation-or-credit/)
- **音声クローンは「なりすまし」に悪用されるリスクが実際に起きている**。
  経営層の声をSNSやインタビュー動画から学習させ、
  「極秘案件で今すぐ対応が必要」といった切迫した電話・Web会議で
  不正送金を指示する詐欺が国内でも報告されている。
  対策として「電話のみの指示では送金しない」「本人しか答えられない質問で確認する」
  「公式な連絡先へ折り返し確認する」を社内ルール化しておくこと
  [出典](https://www.psi.co.jp/topics/2026/nl_20260225_1.html)
- **他人の声を無断でクローンすることは規約違反**。ElevenLabsのProfessional Voice
  Cloningは「本人が自分の声を登録・検証する」ことを前提とした設計になっており、
  他人の声を本人の同意なくクローンする行為は利用規約(Prohibited Use Policy)で
  明確に禁止されている。社内でナレーターの声をクローンして使う場合も、
  本人からの明示的な同意(用途を特定した上での同意)を取得し、記録を残すこと
  [出典](https://elevenlabs.io/use-policy)
- **日本語の発音は完璧ではない**。特にSuno/Udioの歌詞は漢字の読み間違いが起きやすく、
  ひらがな・ローマ字表記に調整すると改善するケースが多い。ElevenLabsのナレーションも
  固有名詞や専門用語で読みが揺れることがあるため、読みを指定した原稿に整えてから
  生成する運用にすると安定する
  [出典](https://n1-inc.co.jp/suno-ai-nihongo/)
- **「AIっぽさ」は完全には消えない**。ボーカルの発声や伴奏のミックスに独特の質感が
  残ることがあるため、企業の看板コンテンツ(メインCM等)への採用は試作・叩き台段階での
  利用にとどめ、最終仕上げは人間のクリエイターと組み合わせる判断も検討する

## 最初の一歩

ElevenLabsまたはSunoの無料プランに登録し、社内資料の一節を音声化する、
または展示会用BGMを1曲試作してみることから始めるとよい
(ただし無料プランの出力は商用利用不可のため、実際に社内配布・公開する場合は
有料プランへの切り替えが必要な点に注意)。

## 関連トピック

- [生成AIの著作権リスクと実務での注意点](../part04-risk-security/copyright-risks-in-generative-ai.md)
- [GitHub Copilotの基本(コーディング支援AI)](github-copilot-basics.md)

## 更新履歴

### 2026-07-27: 著作権訴訟の進展とSuno/ElevenLabsの新機能を反映
- **内容**: 「仕組み・背景」「使いどころ・使い分け」「注意点」を最新化。UdioがUMG・ワーナー・
  Merlin・Kobaltと和解し生成物のダウンロード不可な会員制プラットフォームへ移行予定であること、
  SunoはUMG・ソニーと訴訟継続中(対象曲が約61,000曲に拡大、2026年7月にフェアユースを
  争うサマリージャッジメント審理)であること、米国音楽家組合(AFM)がレーベル側を
  提訴した経緯を追記。あわせてSuno v5.5(Voices/Custom models/My Taste)や
  ElevenLabsのStudio 3.0・Agents・Dubbing v2・Lipsync Video Synthesisなど
  2026年前半の新機能を反映した
- **出典**: [Suno faces verdicts in Munich and Boston(TechTimes)](https://www.techtimes.com/articles/320139/20260710/ai-music-training-hits-two-courts-july-suno-faces-verdicts-munich-boston.htm) / [UMG-Udio Deal FAQ(Billboard)](https://www.billboard.com/pro/umg-udio-ai-deal-faq-artist-payments-user-downloads-lawsuit/) / [Musicians union sues UMG and Warner(MBW)](https://www.musicbusinessworldwide.com/musicians-union-sues-umg-and-warner-music-alleging-member-recordings-were-licensed-to-suno-and-udio-without-compensation-or-credit/) / [Suno v5.5 blog](https://suno.com/blog/v5-5) / [ElevenLabs News July 2026](https://blog.mean.ceo/elevenlabs-news-july-2026/)

### 2026-07-06: 初版執筆
- **内容**: 音楽生成AI(Suno・Udio)と音声合成・音声クローンAI(ElevenLabs)の違い、
  各ツールの2026年7月時点の料金プラン・機能比較表、社内研修ナレーション・広告BGM・
  多言語吹き替えといった業務での使いどころ、著作権(RIAA訴訟の現況)・
  音声なりすまし詐欺の注意点をまとめた
- **出典**: [Suno Pricing](https://suno.com/pricing) / [Udio Pricing解説(eesel AI)](https://www.eesel.ai/blog/udio-pricing) / [ElevenLabs Pricing解説(BIGVU)](https://bigvu.tv/blog/elevenlabs-pricing-2026-plan-worth/) / [Suno review 2026(eesel AI, RIAA訴訟の経緯)](https://www.eesel.ai/blog/suno-review) / [ElevenLabs Prohibited Use Policy](https://elevenlabs.io/use-policy) / [ディープフェイク音声詐欺の事例(PSI CyberSecurity Insight)](https://www.psi.co.jp/topics/2026/nl_20260225_1.html) / [Suno AIの日本語対応](https://n1-inc.co.jp/suno-ai-nihongo/)
