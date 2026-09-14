---
title: 音声・音楽生成AIの基本(Suno・Udio・ElevenLabsなどの選び方)
part: 8
chapter: 第3章 画像・動画・音声の生成AI
tags: [Suno, Udio, ElevenLabs, Lyria, 音楽生成AI, 音声合成, 音声クローン, TTS]
created: 2026-07-06
updated: 2026-09-05
---

# 音声・音楽生成AIの基本(Suno・Udio・ElevenLabsなどの選び方)

## これは何か

「動画のBGMが欲しい」「研修動画にナレーションを付けたい」というとき、
作曲家やナレーターを毎回手配するのはコストも時間もかかる。
音声・音楽生成AIは、テキストや簡単な指示だけで**楽曲**や**人間の声のような音声**を
数十秒〜数分で作り出すツール群で、この「素材調達」の手間を大きく減らせる。

このジャンルは大きく2系統に分かれる。

- **音楽生成AI**: 歌詞やジャンルを指定するとボーカル入りの楽曲をゼロから作曲する
  (代表: Suno、Udio。2026年にはGoogleの「Lyria」、ElevenLabsの「Music」など、
  学習データのライセンス取得を明確に打ち出す新規参入も増えている)
- **音声合成・音声クローンAI**: テキストを自然な音声に変換したり、
  特定の人の声を学習して同じ声で新しい台詞を話させたりする
  (代表: ElevenLabs)

ElevenLabsのように音声合成を主軸としながら音楽生成機能(ElevenLabs Music)も持つなど、
1社が両方を提供する「総合型」ツールも登場している。「何を入力し、何を出力するか」で
系統を選ぶ発想は変わらないが、選定にあたっては機能だけでなく**学習データの権利処理
(無許諾で学習させたモデルか、レーベル等とライセンス契約済みのモデルか)**も
重要な判断材料になってきている(詳細は後述)。

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
  読み上げさせられる。2026年にはこれとは別に音楽生成モデル「ElevenLabs Music」も
  投入し、Merlin・Kobaltなど音楽業界団体とのライセンス契約に基づく学習データのみを
  使うことを明言している
- **Google Lyria**: Gemini本体・Google AI Studio・動画編集ツール「Flow」「Vids」に
  統合された音楽生成モデル。歌詞・ジャンルを指定してボーカル入り/インストの楽曲を
  最長3分まで生成できる。既存のGeminiサブスクリプション(AI Plus / Pro / Ultra)の
  範囲内で使え、Googleの生成AI利用規約に基づく補償(indemnification)付きで
  商用利用が認められている点が特徴

2024年6月、Suno・UdioはRIAA(全米レコード協会)を通じてユニバーサル・ソニー・
ワーナーの主要レーベルから「著作権のある音源を無許可でAI学習に使用した」として
提訴された。2026年9月時点、この訴訟群は「レーベルとライセンス契約を結んで和解する動き」と
「訴訟が新たに拡大・激化する動き」が同時並行で進んでおり、状況はむしろ複雑化している。

- **Udio**: ユニバーサル(2025年10月)、ワーナー(2025年11月)に続き、インディーズ
  レーベル連合Merlin(2025年12月)、音楽出版のKobalt(2026年1月)ともライセンス契約で
  和解した。この和解に伴い**Udioは2025年10月29日付けで楽曲・動画・ステムのダウンロード
  機能を全プランで停止**しており(既存ユーザー向けに2025年11月3〜5日の48時間だけ
  猶予ダウンロード期間が設けられた)、2026年9月時点でも復旧していない。UMGとの合意に
  基づき、参加アーティストの楽曲だけを使い生成物を外部へ書き出せない「会員制プラットフォーム」
  への全面移行が予告されているが、2026年8月時点で正式ローンチは発表されておらず時期は
  未確定のまま延期が続いている
  [出典](https://www.musicbusinessworldwide.com/sony-music-files-new-lawsuit-against-ai-platform-udio-asserting-over-30000-sound-recordings-a-judge-barred-it-from-adding-to-its-original-case/)
- **ソニー vs Udio**: ソニーは和解を拒否し係争を継続。2024年6月提訴の原告訴訟
  (対象333曲)にディスカバリー(証拠開示)で判明した3万曲超を追加しようとしたが
  2026年6月29日に裁判所が却下したため、2026年7月20日、新たに30,117曲の音源を
  対象とする**別訴訟**をSDNY(ニューヨーク南部地区連邦地裁)に提起した。請求額は
  当初訴訟の約5,000万ドルから最大45億ドルまで拡大している
  [出典](https://variety.com/2026/music/news/sony-music-new-lawsuit-udio-ai-music-generator-1236817746/)
- **Suno**: ワーナーとは2025年10月にライセンス契約で和解したが、ソニー・ユニバーサルとは
  マサチューセッツ連邦地裁(ボストン)で係争が継続中。対象楽曲は2026年5月時点で
  560曲から61,026曲に拡大されており、事実証拠開示(fact discovery)は2026年9月30日に
  締め切られる予定で、双方はその後「著作権のある音源での無許諾学習が公正利用
  (フェアユース)にあたるか」を争点とするサマリージャッジメント(略式判決)の
  申立てに動くとみられる。2026年9月時点でこの争点についての判決はまだ出ていない
  [出典](https://www.techtimes.com/articles/320139/20260710/ai-music-training-hits-two-courts-july-suno-faces-verdicts-munich-boston.htm)
- **GEMA vs Suno(ドイツ)**: 2026年7月31日、ミュンヘン地方裁判所がドイツの著作権管理
  団体GEMAの訴えを認め、Sunoに敗訴判決を下した(生成AI音楽をめぐる欧州初の司法判断)。
  対象の6曲について、(1)米国内での学習用複製、(2)ドイツ国内でのモデルへの記憶
  (メモライゼーション)、(3)モデル提供による公衆への提供、(4)生成物による複製・
  公衆への提供、の4類型を差し止め、情報開示と損害賠償責任も認めた。違反1件につき
  最大25万ユーロの制裁金が科される。Sunoの「フェアユースにあたる」という主張は
  米国著作権法の枠組みで判断された上で退けられており、控訴が見込まれる
  (2026年9月時点で判決は未確定)
  [出典](https://www.twobirds.com/en/insights/2026/germany/munich-district-court-rules-on-ai-generated-music-gema-v-suno)

さらに2026年6月、米国音楽家組合(AFM)がユニバーサル・ワーナー(および傘下の
Atlantic Recording、Warner Records)を提訴した。レーベル側はSuno・Udioとの和解で
対価を得た一方、実際に演奏した個々のミュージシャンには契約上の「新規用途(new use)」
条項に基づく補償・クレジットが支払われていないという主張で、2026年7月には被告に
Atlantic・Warner Recordsを追加した修正訴状(amended complaint)が提出されている
[出典](https://www.musicbusinessworldwide.com/us-musicians-union-files-amended-lawsuit-against-universal-and-warner-over-suno-and-udio-ai-deals/)。
2026年9月時点でも判決は出ておらず、「レーベルが学習データをライセンスした」ことと
「関係者全員が納得・補償されている」ことはイコールではない状況が続いている。

こうした未確定な法的リスクを踏まえ、ElevenLabs MusicやGoogle Lyriaのように
「ライセンス取得済みの学習データのみを使用し、生成物の商用利用を保証する」ことを
前面に打ち出すツールも増えている。無許諾学習データ由来の訴訟リスクを避けたい
企業ユースでは、こうした「ライセンス明示型」のツールを選ぶという選択肢も
現実的になってきた。ただし係争そのものが決着していない以上、どのツールを選んでも
リスクがゼロになるわけではない点には注意したい(詳細は下記「注意点」)。

## 使いどころ・使い分け

まず「楽曲を作りたいのか、声を作りたいのか」「著作権リスクをどこまで許容するか」で
系統を選ぶ。

| 目的 | 向いているツール系統 | 具体例 |
|---|---|---|
| BGM・ジングル・テーマソングを作りたい | 音楽生成AI(Suno / Udio / Google Lyria) | YouTube動画のBGM、店舗のオリジナルテーマ曲、CMのジングル |
| 著作権リスクを抑えて商用利用したい | ライセンス取得済み学習データを明示するツール(ElevenLabs Music、Google Lyria) | 企業公式チャンネル、広告など「係争中モデル」を避けたい用途 |
| 原稿を音声化したい(ナレーション) | 音声合成AI(ElevenLabs等) | 研修動画・eラーニングのナレーション、記事の音声読み上げ |
| 特定の人物の声で話させたい | 音声クローンAI(ElevenLabs等) | 社長メッセージの多言語版、キャラクターボイスの量産 |
| 動画を多言語に吹き替えたい | 音声合成AI+翻訳(Dubbing機能) | 海外展開する製品紹介動画のローカライズ |

音楽生成AI同士(Suno vs Udio)の使い分けの目安(2026年9月時点)。

| 観点 | Suno | Udio |
|---|---|---|
| ボーカル・歌詞の再現力 | 高い。日本語歌詞も比較的自然([出典](https://n1-inc.co.jp/suno-ai-nihongo/)) | やや硬い場面があるが音質面で評価される([出典](https://www.matrixflow.net/case-study/137/)) |
| 生成後の編集機能 | ステム分割(ボーカル/楽器を最大12パートに分離)、ボーカル・伴奏の後付け | Voice Control(声質の微調整)、Style Blending、Inpaint(部分的な再生成)など編集の自由度は高いが、後述の通り現状は書き出し不可 |
| 最新モデル・状況 | 主力モデルはv5.5。2026年8月に「責任ある構築」方針と透かし(ウォーターマーク)技術を発表し、9月3日付で新しいダウンロード上限とToSを施行。音楽業界と協業する次世代モデル(v6)も予告されているが、2026年9月時点でリリース時期は未確定([出典](https://www.musicbusinessworldwide.com/wheres-v6/)) | UMGとの和解に伴う会員制プラットフォームへの移行が続くが正式ローンチは未発表。2025年10月末以降、**全プランでダウンロード機能が停止中** |
| ダウンロード上限(2026年9月3日〜) | Free: 生涯7曲まで(個人利用のみ) / Pro: 月20曲 / Premier: 月60曲(Suno Studio内は無制限) | 停止中(全プラン、復旧時期未定) |
| 無料プランの商用利用 | 不可(有料プランのみ) | 不可(有料プランでも現状ダウンロード自体が不可) |
| 向いている使い方 | 生成した曲を実際にダウンロードして動画等に組み込みたい | プラットフォーム内での試作・アイデア出しに限定するなら |

業務で「BGMをダウンロードして動画に組み込む」実務ニーズには、**現状Sunoの方が
唯一現実的な選択肢**になっている。Udioは2025年10月末からダウンロード機能自体が
全プランで停止しており、2026年9月時点でも復旧の見通しは示されていない。Udioを使う
理由があるとすれば、プラットフォーム内で聴きながら試作・ブレインストーミングする
用途に限られる。

「AIっぽさ」が完全には抜けないため、**企業のメインCMソングのような看板コンテンツ**には
人間の作曲家への発注、**社内動画・SNS用のBGM・叩き台**にはAI生成、という
二段構えが現実的な落としどころになる。

音声合成AIについては、汎用チャットAI(ChatGPT・Geminiなど)の読み上げ機能との違いも
押さえておきたい。汎用チャットAIの音声出力は「会話用の合成音声」で選択肢が少なく
声質のカスタマイズもできないのに対し、ElevenLabsは声のトーン・抑揚・多言語対応・
クローン作成まで踏み込める「素材制作用」のツールという位置づけになる。なお2026年9月、
GoogleはGeminiアプリ・AI Studio・Flow Music・Vidsに音楽生成モデル「Lyria 3.5」を
統合した。Google AI Plus/Pro/Ultraなど既存のGeminiサブスクリプションの範囲内で
1日10〜50曲を生成でき、商用利用もGoogleの補償(indemnification)付きで認められる。
すでに組織としてGeminiを契約していれば、追加のツール契約を増やさずに楽曲生成を
試せる選択肢として現実的になった
([出典](https://blog.google/innovation-and-ai/products/gemini-app/lyria-3/))。

## 実務での使い方

### Sunoの始め方と料金(2026年9月時点)

1. [suno.com](https://suno.com) にアクセスし、Googleアカウント等でサインアップ
2. 画面上部の「Create」から歌詞・ジャンル・雰囲気をテキストで指定して生成
3. 生成された楽曲はダウンロード、ステム分割、ボーカル/伴奏の差し替えが可能
   (ただしダウンロード数には下表の上限がある)

| プラン | 料金(月払い/年払い) | クレジット | ダウンロード上限(2026年9月3日〜) | 主な機能 | 商用利用 |
|---|---|---|---|---|---|
| Free | 無料 | 1日50クレジット | 生涯7曲まで(個人利用のみ) | 個人利用のみ | 不可 |
| Pro | $10/月(年払い$8/月) | 2,500/月 | 月20曲 | v5.5等の上位モデル、ステム分割(最大12パート)、30分までの音源アップロード、優先生成キュー | 可(出力の権利は利用者に帰属) |
| Premier | $30/月(年払い$24/月) | 10,000/月 | 月60曲(Suno Studioは無制限) | Suno Studio(DAW的な編集画面)、Proの全機能 | 可 |

[出典](https://suno.com/pricing) /
[出典](https://help.suno.com/en/articles/13614785)

2026年8月、Sunoは「責任ある構築」方針と透かし技術の導入を発表し、9月3日付けで
上記のダウンロード上限と新しい利用規約(ToS)を施行した。**この上限は9月3日より前に
生成した楽曲にも遡って適用される**(再生・共有は全プランで従来どおり可能だが、
ダウンロードは上限にカウントされる)。音楽業界と協業して開発する次世代モデルの
投入も予告されているが、2026年9月時点でリリース時期は未確定
[出典](https://roo.beehiiv.com/p/suno-new-models-september-2026)。

### Udioの始め方と料金(2026年9月時点)

1. [udio.com](https://www.udio.com) にアクセスしてサインアップ
2. プロンプト欄に曲の雰囲気・ジャンルを、Lyrics欄に歌詞を入力して生成
3. 生成後はVoice Control・Style Blending・Inpaintで部分修正が可能
   (※ダウンロード・外部書き出しは下記の通り全プランで停止中)

| プラン | 料金(月額/年払い) | クレジット | 同時生成数 | ダウンロード | 商用利用 |
|---|---|---|---|---|---|
| Free | 無料 | 月100(1日10) | 4曲まで並列 | 不可 | 不可 |
| Standard | $10/月(年払い$96/年) | 2,400/月 | 6曲まで並列 | 停止中(2025年10月末〜) | 停止中 |
| Pro | $30/月(年払い$288/年) | 6,000/月 | 高負荷・並列生成向け | 停止中(2025年10月末〜) | 停止中 |

[出典](https://www.eesel.ai/blog/udio-pricing) /
[出典](https://www.digitalmusicnews.com/2025/10/31/udio-downloads-disabled-umg-deal/)

UMGとの和解に伴い**2025年10月29日付けで全プランのダウンロード機能が停止**され、
11月3〜5日の48時間だけ猶予期間が設けられたのち、2026年9月時点でも復旧していない。
参加アーティストの楽曲のみを扱う新しい会員制プラットフォームへの移行が予告されているが、
2026年8月時点で正式ローンチは発表されておらず時期は未定。したがって現状のUdioは
「プラットフォーム内で聴く・試作する」ことはできても、**成果物を実務で使うことは
できない**点を理解した上で契約を検討すること。

いずれもクレジットは基本的に翌月へ持ち越されない(購入した追加クレジットのみ失効しない)ため、
月内の使い切りを前提に容量を選ぶこと。

### ElevenLabsの始め方と料金(2026年9月時点)

ElevenLabsは単純なTTS(読み上げ)ツールから、ナレーション・動画・音楽・
カスタマーサポート用音声エージェントまでを1つのタイムラインで扱う
「音声・動画の総合制作基盤」へと役割を広げている。2026年時点では
制作画面「Studio 3.0」、会話AI機能「ElevenLabs Agents」、90以上の言語に対応する
「Dubbing v2」(2026年6月にAPI経由でも利用可能化)などが主要機能として追加されている。
さらに2026年4月には音楽生成アプリ「ElevenMusic」、5月には新モデル「Music v2」を投入し、
Merlin・Kobaltなど音楽業界団体とのライセンス契約に基づく学習データのみを使用し
「生成した楽曲はすべて商用利用がクリアされている」とうたう点が、Suno・Udioとの
大きな違いになっている
([出典](https://elevenlabs.io/blog/introducing-music-v2))。

1. [elevenlabs.io](https://elevenlabs.io) でサインアップし、日本語UIも選択可能
2. 「Text to Speech」でテキストを入力し、声(Voice Library)を選んで生成。
   自分の声を使いたい場合は「Voices → Add Voice → Instant/Professional Voice Clone」から
   音声サンプルをアップロードして学習させる
3. 動画の多言語吹き替えは「Dubbing」機能にファイルをアップロードして言語を選択するだけで、
   翻訳・音声合成・リップシンクの調整まで一括処理される(Dubbing v2で地域方言の
   識別精度や背景音・BGMとの共存処理が向上)
4. 楽曲を作りたい場合は「Music」からジャンル・雰囲気・歌詞を指定して生成。
   セクション単位のInpaint(部分再生成)や曲中でのジャンル転換にも対応する

| プラン | 料金(月額、年払いは実質2か月分無料) | クレジット | 音声クローン | 主な用途 |
|---|---|---|---|---|
| Free | $0 | 10,000 | 不可 | 機能を試す(商用利用不可) |
| Starter | $6(年払い実質$5) | 30,000 | Instant Voice Cloning(即席クローン)が利用可能 | 個人・小規模の商用利用、Music/Voiceの商用ライセンスが付く最初のプラン |
| Creator | $22(年払い実質$18.33) | 121,000 | Professional Voice Cloning(高精度クローン)が利用可能 | ナレーション制作、ポッドキャスト |
| Pro | $99(年払い実質$82.50) | 600,000 | 上記全て+API利用枠拡大 | 動画制作会社、代理業務 |
| Scale / Business | $299 / $990 | 180万 / 600万 | チーム共有、複数シート | 制作チーム・エンタープライズ |

[出典](https://elevenlabs.io/pricing) /
[出典](https://flexprice.io/blog/elevenlabs-pricing-breakdown)

音楽生成(Music)は1分あたり約900クレジットを消費するため、Starter($6/月・30,000
クレジット)でも月30分程度の楽曲生成が可能な計算になる。ただし「アーティスト名・
楽曲名を含めたプロンプトの禁止」「武器・たばこ・医薬品・アダルト・宗教/政治関連への
利用禁止」などUse Policy上の制約があるため、生成前に確認しておくこと。

Instant Voice Cloning(即席クローン)は1〜2分程度のクリアな録音があれば作成できるが
長文では音質が揺れやすく、Professional Voice Cloning(専門クローン)は学習データが多く必要な分、
長尺のナレーションでも安定した声を再現できる。社内研修動画のナレーターを
毎回固定したい場合はProfessional Voice Cloningの利用が向く。

### Google Lyriaの始め方(2026年9月時点)

1. Geminiアプリ(gemini.google.com またはモバイルアプリ)を開き、プロンプト欄に
   「〇〇な雰囲気で3分間のインスト曲を作って」のように依頼するか、Google AI Studio・
   Flow Music・Vidsから楽曲生成機能を呼び出す
2. ジャンル・雰囲気をテキストで指定するか、選択式のスタイルから選んでボーカル入り/
   インストゥルメンタルを生成(最長3分)
3. 利用にはGoogle AI Plus(1日10曲まで)・Pro(1日20曲まで)・Ultra(1日50曲まで)の
   いずれかのGeminiサブスクリプションが必要(Google AI Studioでの単発テストのみ無料)。
   商用利用はGoogleの生成AI利用規約・補償の対象になる
   [出典](https://findskill.ai/blog/google-lyria-3-pro-ai-music-gemini/)

すでに社内でGoogle Workspace・Gemini関連のサブスクリプションを契約している場合、
追加のツール導入なしに楽曲生成を試せる点が実務上のメリットになる。

### コピペで使えるプロンプト例

**Suno/Udio/Lyriaでの社内向けBGM生成プロンプト例**

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

| 機能 | Suno | Udio | ElevenLabs | Google Lyria |
|---|---|---|---|---|
| 主目的 | 楽曲生成(ボーカル入り) | 楽曲生成(ボーカル入り) | 音声合成・音声クローン・吹き替え+楽曲生成(Music) | 楽曲生成(ボーカル入り/インスト) |
| 声を学習させる機能 | Personas(自分の生成曲から声質を継承) | Voice Control(声質の微調整) | Instant/Professional Voice Cloning | なし |
| 多言語対応 | 主要言語+日本語対応 | 主要言語+日本語対応 | 訳・吹き替えまで含むDubbing v2(90言語以上) | 主要言語対応 |
| 学習データの権利処理 | 一部レーベルと和解、ソニー等とは係争中 | 一部レーベルと和解、ソニーとは係争中 | 音楽業界団体とライセンス契約済みと明言 | Google独自(詳細な学習データ内訳は非公開) |
| 生成物のダウンロード | 可(プランごとに上限あり) | 現状不可(全プラン停止中) | 可 | 可(Geminiサブスク経由) |
| 無料プランの商用利用 | 不可 | 不可 | 不可(Starter以上で可) | 不可(有料サブスクのみ) |

## 注意点・よくある誤解

- **無料プランで作った曲・音声は商用利用できない**。後から有料プランに切り替えても、
  無料期間中に生成した分の商用利用は認められないため、business用途は最初から
  有料プランで生成すること
  [出典](https://aipicks.jp/mag/suno-guide-2026)
- **「ダウンロードできる=商用利用できる」とは限らない**。2026年9月3日以降、Sunoは
  Free/Pro/Premierいずれのプランにもダウンロード数の上限を設けており、Freeプランで
  ダウンロードした楽曲は上限内でも個人利用限定で商用利用不可。一方Udioは2025年10月末
  以降、**有料プランに入っていてもダウンロード自体が全面停止**しており、社外に
  持ち出せる成果物は現状存在しない。「有料契約=すぐ使える」と思い込まず、
  契約前にダウンロード可否を必ず確認すること
  [出典](https://help.suno.com/en/articles/13614785) /
  [出典](https://www.digitalmusicnews.com/2025/10/31/udio-downloads-disabled-umg-deal/)
- **学習データの著作権問題は2026年9月時点でも未確定、むしろ訴訟は拡大している**。
  Udioはユニバーサル・ワーナー・Merlin・Kobaltと和解しライセンス済みモデルへの
  移行を進めているが、ソニーとは和解しておらず、2026年7月には対象30,117曲・
  請求額最大45億ドルの新訴訟を起こされている。Sunoはワーナーとのみ和解し、
  ソニー・ユニバーサルとの訴訟(対象約61,000曲)は2026年9月30日に証拠開示が
  締め切られフェアユースを争うサマリージャッジメントの段階に入る見込み。さらに
  ドイツではGEMAがSunoに勝訴し(2026年7月31日、ミュンヘン地裁)、生成AI音楽の
  学習・出力を差し止める欧州初の判断が出た。米国音楽家組合(AFM)もレーベル側を
  「和解金を得たのに演奏者本人には補償していない」として提訴しており、
  レーベルとの和解だけでは著作権・補償の論点がすべて解消したとは言えない状況が
  続いている。企業として広く配信するコンテンツに使う場合は、この動向を継続的に
  確認し、ElevenLabs MusicやGoogle Lyriaのような「ライセンス明示型」のツールへの
  切り替えも選択肢に入れつつ、社内ガイドラインの著作権リスク管理と合わせて判断すること
  (関連: [生成AIの著作権リスクと実務での注意点](../part04-risk-security/copyright-risks-in-generative-ai.md))
  [出典](https://variety.com/2026/music/news/sony-music-new-lawsuit-udio-ai-music-generator-1236817746/)
  /
  [出典](https://www.twobirds.com/en/insights/2026/germany/munich-district-court-rules-on-ai-generated-music-gema-v-suno)
  /
  [出典](https://www.musicbusinessworldwide.com/us-musicians-union-files-amended-lawsuit-against-universal-and-warner-over-suno-and-udio-ai-deals/)
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
(ただし無料プランの出力は商用利用不可、かつSunoは2026年9月3日以降ダウンロード数に
上限があるため、実際に社内配布・公開する場合は有料プランへの切り替えが必要な点に注意)。

## 関連トピック

- [生成AIの著作権リスクと実務での注意点](../part04-risk-security/copyright-risks-in-generative-ai.md)
- [GitHub Copilotの基本(コーディング支援AI)](github-copilot-basics.md)

## 更新履歴

### 2026-09-05: Udioのダウンロード停止長期化・Suno新ダウンロード上限・GEMA勝訴・Sony新訴訟・Lyria/ElevenLabs Musicの新規参入を反映
- **内容**: 「仕組み・背景」の著作権訴訟タイムラインを全面更新。Udioが2025年10月末から
  全プランでダウンロード機能を停止したまま2026年9月時点でも復旧していないこと、
  ソニーがUdioに対し対象30,117曲・請求額最大45億ドルの新訴訟(2026年7月20日)を
  起こしたこと、ドイツGEMAがSunoに勝訴した欧州初の判決(2026年7月31日、ミュンヘン地裁)、
  米国音楽家組合(AFM)の修正訴状(2026年7月)を追記。Sunoのダウンロード上限・新ToS
  (2026年9月3日施行)を「実務での使い方」「注意点」に反映。GoogleのLyria 3.5
  (Gemini/AI Studio/Flow/Vidsに統合、2026年9月4日)とElevenLabs Music v2
  (ライセンス済みデータのみで学習、2026年5月)を新規ツールとして追加し、
  「使いどころ・使い分け」「ツール横断の対応付け」を再構成した
- **出典**: [Sony Music Files New Lawsuit(MBW)](https://www.musicbusinessworldwide.com/sony-music-files-new-lawsuit-against-ai-platform-udio-asserting-over-30000-sound-recordings-a-judge-barred-it-from-adding-to-its-original-case/) / [Sony sues Udio again(Variety)](https://variety.com/2026/music/news/sony-music-new-lawsuit-udio-ai-music-generator-1236817746/) / [Munich Court Rules GEMA v Suno(Bird & Bird)](https://www.twobirds.com/en/insights/2026/germany/munich-district-court-rules-on-ai-generated-music-gema-v-suno) / [AFM amended lawsuit(MBW)](https://www.musicbusinessworldwide.com/us-musicians-union-files-amended-lawsuit-against-universal-and-warner-over-suno-and-udio-ai-deals/) / [Udio downloads disabled(Digital Music News)](https://www.digitalmusicnews.com/2025/10/31/udio-downloads-disabled-umg-deal/) / [Suno download limits FAQ](https://help.suno.com/en/articles/13614785) / [Where's V6?(MBW)](https://www.musicbusinessworldwide.com/wheres-v6/) / [ElevenLabs Music v2](https://elevenlabs.io/blog/introducing-music-v2) / [Lyria 3 in Gemini app(Google Blog)](https://blog.google/innovation-and-ai/products/gemini-app/lyria-3/) / [Lyria 3.5 pricing/access(FindSkill)](https://findskill.ai/blog/google-lyria-3-pro-ai-music-gemini/)

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
