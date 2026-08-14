---
title: スポーツ業界における生成AI活用事例
part: 14
chapter: "第12章 その他・未分類"
tags: [スポーツ, 生成AI活用事例, ファンエンゲージメント, ダイナミックプライシング, 審判支援, ハイライト自動生成, トラッキングデータ]
created: 2026-07-15
updated: 2026-08-11
---

# スポーツ業界における生成AI活用事例

## これは何か

スポーツ業界は、選手の動きを捉えるトラッキングデータ(位置・速度・回転数などをセンサーや
カメラで計測したデータ)と、試合映像・実況・チケット販売という「データ量が多く、
かつリアルタイム性が求められる」業務が揃っており、AI活用が急速に進んでいる業種である。
本ページは、[メディア・広告・エンタメにおける生成AI活用事例](media-entertainment-ai-use-cases.md)
が広告制作・出版報道・ゲーム/映像コンテンツ制作・放送局の多言語化という
**メディア業界一般**の事例を扱うのに対し、**スポーツの「チーム・リーグ運営」そのもの**に
入り込んだAI活用──パフォーマンス分析、ファン向けのスポーツ専用体験、
チケットのダイナミックプライシング(需要に応じた価格自動変動)、審判判定支援──を
実名事例で整理する事例カタログである。放送局の字幕生成や広告代理店のクリエイティブ制作は
前者のページに譲り、ここでは重複を避けている。

## 業務領域別の活用マップ

| 業務領域 | 課題 | AI・生成AIの役割 | 代表事例(本ページ内) |
|---|---|---|---|
| パフォーマンス分析・トラッキング | 選手の動き・投球や打球の質を人手で解析するには限界があり、リアルタイムの戦術判断に間に合わない | トラッキングカメラ・センサーのデータをAIが解析し、プレー分類・守備貢献度・勝率予測・実況コメントなどを自動算出 | MLB「Statcast」「Scout Insights」(Google Cloud)、NPB「NPB+」(ホークアイ×ソニー×コナミ)、NBA「Inside the Game powered by AWS」の「Play Finder」、Wimbledon「Likelihood to Win」(IBM watsonx) |
| 実況・ハイライト自動生成 | 1シーズンで数百〜数千試合が行われ、全試合のハイライト切り出しや多言語実況を人手で追うのは非現実的 | 生成AIが試合映像を解析してハイライト動画を自動生成し、多言語の音声実況やテキスト解説も自動生成 | WSC Sports(NBA・NHL・LaLiga・DAZN等650超団体が採用)、東北楽天ゴールデンイーグルス「AI解説者」 |
| ファンエンゲージメント(対話AI・パーソナライズ) | 大会期間中はファンからの質問・関心が集中し、24時間の個別対応を人手で回すのは困難 | 対話型AIが試合データや過去の実績を踏まえて質問に回答し、AIアバターが会場案内や常設の問い合わせ対応を担当 | Wimbledon「Match Chat」(IBM watsonx Orchestrate)、Jリーグ「JリーグキングAIアバタープロジェクト powered by Nikon」/アビスパ福岡公式サイト(Niiva Talk) |
| チケットのダイナミックプライシング | 固定価格制では人気カードは即完売する一方、平日開催や不人気カードは空席が目立ち、収益機会を取りこぼす | AIが対戦カード・日程・天候・過去の販売実績・残席数などを分析し、席種ごとの価格をリアルタイムで自動調整 | NPB(2026年シーズンも12球団中8球団前後が導入、福岡ソフトバンクホークス・中日ドラゴンズ等)、Jリーグ(川崎フロンターレ、京都サンガF.C.)、Bリーグ(アルバルク東京) |
| 審判判定支援 | 際どいプレーの判定は人間の目だけでは誤審や判定の遅延が生じやすく、公平性への疑義も招く | トラッキング技術とAIが判定案・自動判定を生成し、最終権限は引き続き人間の審判が持つ形で判定を補助 | MLBの「ABSチャレンジシステム」(ロボット審判)、サッカーの半自動オフサイド技術(SAOT、FIFAワールドカップ2026で精度向上) |

**読み方のコツ**: 上の表は「観客・ファンに向けた体験を作る活用」(トラッキング分析、
ハイライト、ファンエンゲージメント)と「収益・公平性という経営の根幹に関わる活用」
(ダイナミックプライシング、審判判定支援)の2系統に分かれる。後者はAIの判断ミスが
そのまま炎上や信頼低下に直結するため、同じ「AI活用」でも求められる説明責任の重さが違う
点を意識して読むとよい。

## 使いどころ・使い分け

| 観点 | 大規模リーグ・国際大会向き | 中小規模チーム・国内リーグ向き |
|---|---|---|
| 基盤の作り方 | AWS・Google Cloud・IBM watsonxなど大手クラウドと複数年契約を結び、自前のAI基盤を構築(NBA×AWS、MLB×Google Cloud、Wimbledon×IBM) | WSC Sports、Nikon「Niiva」のような特化ベンダーのSaaS(Software as a Service、契約するだけで使える形態のクラウドサービス)を利用、あるいはNPB+のようにリーグ・ゲーム会社・機器メーカーが共同開発する座組みを組む |
| 目的 | 放送価値・グローバルなファン体験の向上、独自データの蓄積による差別化 | 限られた人員でのファン対応・コンテンツ量産、まずは低コストで試す |
| 向かない場面 | 予算・データ規模が小さいチームが大規模自前基盤を目指すと投資回収が難しい | 大会本番の判定に関わる領域(審判支援)を検証なしに小規模導入するのはリスクが大きい |

- **「見せる情報」と「決める情報」を区別する**: ハイライト生成や実況コメントのように
  多少の粒度の粗さが許容される用途は積極導入して構わないが、価格決定や審判判定のように
  収益・公平性に直結する用途は、人がAIの根拠を検証できる仕組み(チャレンジ制度、
  異議申立ての手順)とセットで導入する
- **ベータ運用から始める**: 楽天イーグルスの「AI解説者」やMLBのロボット審判のように、
  多くの事例はまず一部の試合・大会でベータ版として試し、反応を見てから本格導入する
  進め方を取っている。いきなり全面導入するのではなく、この段階的な進め方を参考にできる

## 実務での使い方

### 1. パフォーマンス分析・トラッキング(海外野球): MLB「Statcast」「Scout Insights」

- **主体**: MLB(米大リーグ機構)、Google Cloud
- **課題**: 投球・打球のわずかな違い(回転数・角度・速度)を人手で正確に評価するのは
  難しく、選手評価や戦術判断のスピードにも限界があった
- **導入したAI・仕組み**: 全30球場にHawk-Eye(複数台のカメラで対象物の3次元的な動きを
  追跡する画像解析システム)を設置し、投手ごとの投球フォームを学習したニューラルネットワーク
  (人間の神経回路を模した機械学習モデル)が全投球を自動で球種分類する。基盤には
  Google Cloudを使い、ボール・選手・姿勢のデータを予測モデルに変換して、
  投手の「勝ち球」ランキングなどの指標をファン向け・球団向けの双方に提供している。
  さらに2026年3月23日、開幕にあわせて公式アプリ「Gameday」に新機能
  「Scout Insights」を追加した。Gemini 2.5 FlashとGemmaのモデルを用い、
  BigQuery・AlloyDB上に蓄積した膨大な過去データの中から「サプライザル(surprisal、
  統計的な意外性)」の高い洞察を選び出し、実況の合間に自動生成コメントとして表示する。
  試合中にその場でAI推論を行うと表示に遅れが出るため、当日のラインアップから
  起こり得る場面をあらかじめ予測してコメントを事前生成しておき、実際の場面が来た瞬間に
  最適な1件を呼び出す設計とすることで、表示までの遅延を約2秒に抑えている。
  Google CloudのエンジニアがMLBのエンジニアリングチームに直接常駐する体制も、
  6シーズンにわたるパートナーシップで初めて取られた
- **自社への応用ヒント**: 「センサーで大量データを集める」だけでなく、
  そのデータを「誰が読んでも意味の分かる指標(球種のランク付けなど)」に翻訳する工程まで
  AIに任せている点が学びどころ。加えてScout Insightsのように、リアルタイム性が
  求められる用途でAI推論の遅延がネックになる場合は「起こり得るパターンを先読みして
  事前生成し、本番では呼び出すだけにする」設計が有効で、チャットボットや接客AIなど
  他分野の応答速度改善にも応用できる考え方である

### 2. パフォーマンス分析・トラッキング(国内野球): NPB「NPB+」×ホークアイ

- **主体**: 株式会社NPBエンタープライズ、株式会社コナミデジタルエンタテインメント、
  ソニー株式会社
- **課題**: 国内プロ野球も投球・打球のトラッキングデータ自体は取得できるようになって
  いたが、それをファン向けにリアルタイムでわかりやすく届ける公式の仕組みが長らくなかった
- **導入したAI・仕組み**: ソニーグループのHawk-Eye Innovationsが提供するトラッキング
  システムが、NPB12球団すべての一軍本拠地球場に導入済みとなり、投球のスピード・回転数、
  打球速度・角度、スイングスピードなどを計測できる体制が整った。この計測データを
  もとに、NPBエンタープライズ・コナミ・ソニーの3社が共同でNPB公認アプリ
  「NPB+(プラス)」を開発し、2025年10月にポストシーズン期間中の限定テスト配信を
  実施した後、機能追加を経て2026年2月26日に正式サービスを開始した。ホークアイの
  データに基づく一球速報や、プレーを3DCGで再現する機能を備え、2026年3月開催の
  「2026 World Baseball Classic」にあわせて侍ジャパンの試合を追う「侍ジャパンモード」
  も追加された
- **自社への応用ヒント**: MLBのStatcastのような海外の先行事例を、国内では
  リーグ運営会社・ゲーム会社・機器メーカーが共同開発するコンソーシアム型の座組みで
  実現している点が参考になる。自社単独で分析基盤を一から作る余力がない場合も、
  計測機器のメーカーやシステムベンダーと共同でアプリ・サービスを開発する座組みを
  検討する価値がある

### 3. パフォーマンス分析・トラッキング(海外バスケ): NBA「Inside the Game powered by AWS」

- **主体**: NBA(北米プロバスケットボールリーグ)、AWS(Amazon Web Services)
- **課題**: 選手やボールの動きを表す膨大なトラッキングデータはあっても、
  それを放送・コーチング・ファン向けの「意味のある洞察」に変換する仕組みが不足していた
- **導入したAI・仕組み**: NBAとAWSは複数年契約を結び、AWSをNBA・WNBA・G Leagueなどの
  公式クラウド・AI提供元とした。2025-26シーズンから提供が始まった「Inside the Game」では、
  Amazon BedrockとAmazon SageMakerを使い、選手1人あたり29点のトラッキングデータポイントから
  動きを解析する。目玉機能「Play Finder」は、過去の試合から似たプレーを瞬時に検索・分類する
  AI技術で、放送実況者がリアルタイムで過去の類似プレーの文脈を紹介できるようにする。
  「Defensive Box Score(守備貢献度の数値化)」「Shot Difficulty(シュートの難易度評価)」
  「Gravity(選手がディフェンダーを引き付ける度合い)」といった新指標もあわせて提供され、
  NBA各球団のフロントオフィスやコーチ陣もこれらのAIモデルに直接アクセスできる。
  この2025-26シーズンは2026年6月にニューヨーク・ニックスが1973年以来となる優勝を
  果たして幕を閉じ、シーズンを通じてPlay Finderや新指標が放送・公式アプリで活用された。
  AWSとNBAは2026-27シーズンに向けても契約を継続し、機能拡張を進めている
- **自社への応用ヒント**: ファン向けの新指標公開と、球団のコーチ・フロント向けの
  意思決定支援を同じAI基盤の上で両立させている点が参考になる。データ活用の企画では
  「社外に見せる価値」と「社内の意思決定に使う価値」を最初から分けて設計すると、
  同じ投資から両方のリターンを得やすい

### 4. ファンエンゲージメント・パフォーマンス分析(テニス): Wimbledon×IBM「watsonx」

- **主体**: 全英オープンテニス選手権(Wimbledon)、IBM
- **課題**: 大会期間中は世界中から大量のアクセスが集中し、試合の流れを瞬時に説明し
  ファンの疑問に答える体験を、限られたスタッフだけで提供するのは困難だった
- **導入したAI・仕組み**: 2026年大会からIBMのAI基盤「watsonx」を活用した新機能を
  公式アプリ・サイトに導入し、実際に2026年6月末〜7月の The Championships 2026で
  稼働した。「Key Moments」は試合の流れを左右した局面をAIが特定し、
  なぜ重要だったかを解説する。「Match Chat」は「watsonx Orchestrate」(複数のAIエージェントを
  連携させる基盤)上に構築され、Wimbledon編集スタイルとテニス特有の言い回しを学習した
  AIエージェント群が、写真・映像付きで会話形式の質問に回答する(2025年時点の技術論文では
  Wimbledon・全米オープン向けの前身版で約100万ユーザーが利用し、平均応答時間6.25秒と
  報告されている)。「Likelihood to Win」は現在・過去の統計と試合の勢いを踏まえて
  各選手の勝率をリアルタイムで算出する。IBMによれば、前年(2025年)大会には世界で
  約7億3,000万人が大会に接触し、デジタルチャネルでの表示回数(インプレッション)は
  180億回に達したとされ、2026年の新機能群はこの規模のファンを見据えて投入されている
- **自社への応用ヒント**: 「AIエージェント群を自社の編集スタイル・専門用語に合わせて
  チューニングする」という発想が、汎用チャットボットとの違いを生んでいる。
  自社に対話AIを導入する際も、汎用の受け答えで満足せず、自社特有の言葉遣い・
  過去データに合わせた調整にどこまで投資するかが体験の質を左右する

### 5. 実況・ハイライト自動生成: WSC Sportsのプラットフォーム(NBA・LaLiga・DAZN等)

- **主体**: WSC Sports(イスラエル発のスポーツテック企業)
- **課題**: 1シーズンで数百試合が行われるリーグでは、試合ごとのハイライト切り出しや
  多言語での実況コメント作成を人手だけでこなすのは現実的でない
- **導入したAI・仕組み**: WSC Sportsのプラットフォームは、放送映像をリアルタイムで解析し
  重要な場面を自動検出してハイライト動画を生成する。NBA・NHL・LaLiga(スペインサッカー
  1部リーグ)・DAZN・PGA Tour・ESPN・YouTube TVなど650を超える団体が採用し、
  2025年上半期だけで提携先全体で800万本超のクリップを追加人員なしで生成
  (前年同期比52%増)、あるプレーオフでは1大会で6万7,000本超のハイライトを生成した
  実績がある。NBAでは2024年以降、生成AIによる多言語音声実況の自動生成にも
  同社の技術が使われている。2026年に入ってからは事業範囲をさらに広げており、
  2026年7月にはTikTokと提携してクリエイターが権利者公認のショート動画を作成できる
  仕組みを始めたほか、スポンサーシップ活用を手がけるPartnerbrite社を買収し、
  「ハイライトを量産する」だけでなく「協賛収益化までカバーする」方向へ守備範囲を
  広げつつある
- **自社への応用ヒント**: 「動画1本ずつを人手で編集する」発想から、
  「素材を大量に生成し、視聴者ごとに最適な形で届ける」発想への転換が鍵。
  自社のコンテンツ配信でも、まず全量を自動処理できる仕組みを作ってから、
  ターゲットごとの出し分けを組み合わせる順序が参考になる。加えて、
  自動生成の仕組みが定着した後は「生成した素材をどう収益化に繋げるか」まで
  視野を広げる段階が来ることも見据えておくとよい

### 6. 実況コメント生成(国内野球): 東北楽天ゴールデンイーグルス「AI解説者」

- **主体**: 楽天グループ、東北楽天ゴールデンイーグルス
- **課題**: 動画配信での実況・解説は視聴者の関心を引く一方、全試合・全場面で
  選手データを踏まえた深掘り解説を人手だけで用意するのは負荷が高い
- **導入したAI・仕組み**: 動画配信サービスの「Rakuten パ・リーグ Special」向けに、
  試合映像や選手の成績データを解析してコメントを自動生成する「AI解説者」を開発し、
  2026年6月に東京ドームでの「楽天スーパーナイター」でデモンストレーションを実施。
  配信ページのライブチャット欄に導入し、実況アナウンサーや解説者からの問いかけに対して
  選手の成績データを用いながら深掘りする形で応答する。2026年8月時点でも、
  当該シーズン中のベータ提供に向けた開発・検証が続いている段階で、本格運用は
  来シーズン(2027年)以降を見込んでいる
- **自社への応用ヒント**: いきなり全国放送で本格投入するのではなく、
  自社イベントでのデモから始めてベータ版へ、という段階的な展開が特徴。
  新しい生成AI機能を社内外に出す際は、限定的な場での実証→ベータ公開→本格運用という
  順を追うことで、失敗時の影響範囲を抑えながら改善できる

### 7. ファンエンゲージメント(国内サッカー): Jリーグ「Niiva Talk」AIアバター

- **主体**: 公益社団法人日本プロサッカーリーグ(Jリーグ)、サガン鳥栖ほかJクラブ、
  株式会社ニコン
- **課題**: カップ戦決勝のような大規模イベントや、クラブ公式サイトへの日常的な
  問い合わせでは、来場者・訪問者からの会場アクセス・イベント内容・選手情報などの
  質問が集中し、スタッフだけでは対応しきれない
- **導入したAI・仕組み**: 2025年のJリーグYBCルヴァンカップ決勝の特設サイト内で、
  ニコンのAIアバターソリューション「Niiva Talk」を使った
  「JリーグキングAIアバタープロジェクト powered by Nikon」を公開。試合情報・出場選手・
  スタジアムアクセス・イベント内容などをAIアバターがリアルタイムで案内した。
  同じ「Niiva Talk」は大会特設サイトに限らずクラブの常設チャネルとしても展開されており、
  アビスパ福岡(J1)は2025年8月にニコンとDXパートナー契約を締結し、公式サイトの
  トップページに常時稼働のAIアバターを設置。ユニフォーム姿のアバターが音声での
  質問に答える窓口として運用している
- **自社への応用ヒント**: 「大会当日だけ・特設サイトだけ」という範囲を絞った試験導入
  (JリーグYBCルヴァンカップ決勝)と、「常設・年間を通じた問い合わせ窓口」としての本格
  導入(アビスパ福岡)の両方のパターンが揃ってきた点が参考になる。年間を通じた常設の
  対話AI導入にいきなり踏み切るのではなく、まず単発の大型イベントで限定的に試し、
  手応えを見てから常設チャネルへ広げるという段階的な入り方は他業種でも応用しやすい

### 8. チケットのダイナミックプライシング: NPB・Jリーグ・Bリーグの導入状況

- **主体**: プロ野球12球団(2025年に続き2026年シーズンも8球団前後が導入を継続、
  福岡ソフトバンクホークス・中日ドラゴンズ等)、Jリーグ(川崎フロンターレ、
  京都サンガF.C.等)、Bリーグ(アルバルク東京等)
- **課題**: 固定価格制では人気カード・好条件の試合はすぐに完売する一方、
  平日開催や下位対戦カードでは空席が目立ち、収益機会を取りこぼしていた
- **導入したAI・仕組み**: ダイナミックプライシング(需要と供給に応じてチケット価格が
  リアルタイムで変動する仕組み)をAIが支える形で、対戦カードの人気度・日程・天候・
  過去の類似試合の販売実績・現在の販売ペース・席種ごとの残席数などを総合的に分析し、
  価格を自動調整する。プロ野球では2025年シーズン時点で12球団中8球団が導入しており、
  千葉ロッテマリーンズ・東京ヤクルトスワローズなどは平日ナイターの外野席でも
  5,000円、大型連休期間は外野席が1万円近くに達する例もある。福岡ソフトバンクホークスは
  ダイナミックプライシングとチケットのリセール(再販売)システムを組み合わせて運用している。
  2026年シーズンからは中日ドラゴンズも主催試合の一部で「ダイナミックプライシングデー」を
  新設するなど、対象球団・対象試合は緩やかに拡大が続いている。Jリーグでは
  川崎フロンターレ・京都サンガF.C.などが、Bリーグではアルバルク東京などが
  同様の仕組みを導入している
- **自社への応用ヒント**: 価格変動の判断根拠(何のデータをどう反映しているか)を
  ファンに開示するかどうかが炎上リスクを左右する。読売ジャイアンツ・阪神タイガースの
  ようにあえてダイナミックプライシングを導入しない方針を明言している球団もあり、
  「収益最大化」と「ファンの納得感・裾野の広さ」のどちらを優先するかは業界内でも
  判断が割れていることを踏まえ、自社の顧客層に合わせて採否を検討する必要がある

### 9. 審判判定支援: MLB「ABSチャレンジシステム」とサッカーの半自動オフサイド技術(SAOT)

- **主体**: MLB(ロボット審判)、FIFA・UEFA・イングランドサッカー協会(SAOT)
- **課題**: ストライク・ボールやオフサイドのような際どい判定は、人間の目だけでは
  誤審や判定の遅延が生じやすく、大会の公平性への疑義にもつながっていた
- **導入したAI・仕組み**: MLBは球場に設置したカメラでボールの軌道を追跡し、
  投球がストライクゾーンを通過したかどうかを3Dアニメーションで示す
  「ABSチャレンジシステム」(いわゆる「ロボット審判」)を2026年シーズンから正式導入した。
  各チームには1試合あたり2回の「チャレンジ」(判定への異議申立て、成功すれば
  権利を維持)が与えられ、最終的な判定を10〜15秒程度で表示する仕組みで、
  あくまで人間の主審の判定に対する補助・再確認の位置づけになっている。
  2026年シーズンは開幕からトレード期限(8月3日)までに全球団合計で7,100回を
  超えるチャレンジが行われ、成功率は53%前後で推移しており、捕手のチャレンジ成功率が
  投手・打者よりも高い傾向が続いている。サッカーでは、UEFAチャンピオンズリーグ
  (2022-23シーズン)、FIFAワールドカップ2022、イングランドFAカップ(2025年2月)などで
  導入されてきた「半自動オフサイド技術(SAOT)」が、2026年6〜7月に北中米3カ国
  (アメリカ・カナダ・メキシコ)で開催されたFIFAワールドカップ2026でさらに
  精度を高めて全16会場に導入された。オフサイドの許容誤差はこれまでの50cmから
  10cmへ引き下げられ、副審のイヤホンにAIがオフサイドの可能性を直接音声で通知する
  仕組みも加わり、映像確認にかかっていた時間が大幅に短縮されたと報じられている。
  SAOTはボールと選手の追跡データからAIがキックの瞬間とオフサイドラインを自動算出し、
  VAR(ビデオアシスタントレフェリー)の判定作業を高速化・標準化するが、
  最終的な判定の言い渡しは引き続き人間の審判が行う
- **自社への応用ヒント**: どちらの事例も「AIが判定を下す」のではなく
  「AIが判定材料を高速に整理し、人間が最終判断・言い渡しを行う」設計になっている点が
  共通している。ワールドカップ2026のように精度基準(許容誤差)を段階的に引き下げて
  改善を続けている点も参考になる。業務でAI判定を導入する際も、AIの出力をそのまま
  採用するのではなく、人間が異議を申し立てたり再確認したりできる余地を残す設計と、
  精度基準を継続的に見直す運用の両方が、公平性への信頼を保つ鍵になる

## 注意点・よくある誤解

- **AI判定はあくまで「支援」であり「代替」ではない**: MLBのロボット審判もサッカーのSAOTも、
  最終的な判定権限は人間の審判に残る設計になっている。「AIが自動で判定を下す」と
  誤解されがちだが、実態は「AIが根拠を高速に提示し、人間またはチャレンジ制度が
  最終確認する」仕組みである点を正しく理解しておく必要がある
- **ダイナミックプライシングは「収益最大化」と「ファン離れ」のトレードオフを伴う**:
  価格高騰への反発でライト層のファンが離れるリスクがあり、実際に導入を見送る球団もある。
  AIによる価格最適化を導入する際は、短期の収益指標だけでなく、
  長期的なファン基盤の維持という観点もセットで議論する必要がある
- **ファンデータのプライバシーへの配慮が必要**: パーソナライズされたファンエンゲージメントは、
  観戦履歴・購入傾向・ウェアラブル由来の生体データなど機微な情報を扱うことが多い。
  選手側のデータについても、要配慮情報の扱いや同意取得のルールを事前に整備しておく必要がある
- **華やかな事例の多くはまずベータ・限定公開から始まっている**: 楽天の「AI解説者」や
  Wimbledonの新機能のように、多くはいきなり全面展開せず、特定の試合・大会に限定して
  検証してから本格導入する進め方を取っている。導入効果を評価する際は
  「ベータ版の反応」と「本格運用後の実績」を区別して見る必要がある

## 最初の一歩

自チーム・自社イベントで今すでに集めているデータ(観戦履歴、チケット販売実績、
試合映像など)のうち、まず「ファンに見せても問題のない情報」を1つ選び、
WSC Sportsのハイライト自動生成や楽天の「AI解説者」のように、
小規模なベータ運用として試せないかを検討することから始めるとよい。

## 関連トピック

- [メディア・広告・エンタメにおける生成AI活用事例](media-entertainment-ai-use-cases.md)
- [宿泊・観光業における生成AI活用事例](hospitality-tourism-ai-use-cases.md)

## 更新履歴

### 2026-08-11: 主要事例を2026年8月時点の最新情報に更新
- **内容**: MLBのStatcastに新機能「Scout Insights」(Gemini 2.5 Flash/Gemma、
  BigQuery・AlloyDB活用、2026年3月開始)を追記し、国内トラッキング事例として
  NPB「NPB+」(ホークアイ×ソニー×コナミ、2026年2月正式開始)を新規事例として追加した。
  NBA「Inside the Game」を2025-26シーズン終了(ニックス優勝)を踏まえて更新し、
  WimbledonのMatch Chatに前年大会の規模データ(7億3,000万人・180億インプレッション)を
  追記。WSC Sportsの提携団体数を650超に更新し、TikTok提携・Partnerbrite買収による
  事業拡大を追記した。Jリーグ「Niiva Talk」にアビスパ福岡の常設導入事例を追加、
  NPBダイナミックプライシングに中日ドラゴンズの2026年参入を追記。MLBのABSチャレンジ
  システムを2026年シーズン中盤の実績値(7,100件超・成功率53%)に更新し、
  FIFAワールドカップ2026における半自動オフサイド技術(SAOT)の精度向上
  (許容誤差50cm→10cm、審判への音声通知)を新規に追加した
- **出典**:
  [How MLB is bringing AI-powered color commentary to fans with Scout Insights(Google Cloud Blog)](https://cloud.google.com/transform/mlb-scout-insights-ai-powered-color-commentary-gameday-app)、
  [MLB, Google Cloud Debut AI-Powered, Real-Time Game Analysis With 'Scout Insights' in MLB Gameday(Sports Video Group)](https://www.sportsvideo.org/2026/03/23/mlb-google-cloud-debut-ai-powered-real-time-game-analysis-with-scout-insights-in-mlb-gameday/)、
  [ホークアイのデータをリアルタイムで可視化するプロ野球速報アプリ「NPB+」テスト配信開始(PRONEWS)](https://jp.pronews.com/news/202510141918681463.html)、
  [NPB公認プロ野球速報アプリ「NPB＋（プラス）」を10日から期間限定テスト配信！2026年シーズンに合わせて本格稼働を目指す(ベースボールチャンネル)](https://www.baseballchannel.jp/npb/234467/)、
  [「侍ジャパンモード」新搭載！野球速報アプリ「NPB+」、ホークアイのデータで野球選手の"凄さ"を実感しよう！(ソニー広報note)](https://note.com/sonycorporation/n/nf02e1facecc4)、
  [2026 NBA Finals: Biggest takeaways from Knicks-Spurs Game 5(ESPN)](https://www.espn.com/nba/story/_/id/48940704/2026-nba-finals-biggest-takeaways-highlights-san-antonio-spurs-new-york-knicks-championship)、
  [NBA, Amazon Launch "Inside the Game" Defense, Shooting Stats Package(Sportico)](https://www.sportico.com/leagues/basketball/2025/nba-amazon-web-services-inside-the-game-stats-ai-1234872489/)、
  [Wimbledon Goes High-Tech With Fan-Focused Digital Experience(Forbes)](https://www.forbes.com/sites/timnewcomb/2026/06/29/wimbledon-goes-high-tech-with-fan-focused-digital-experience/)、
  [Wimbledon adds IBM AI tools for live match coverage(artificialintelligence-news.com)](https://www.artificialintelligence-news.com/news/wimbledon-ibm-ai-tools-live-match-coverage/)、
  [TikTok and WSC Sports Partner to Give Rights Holders a New Way to Reach Fans Through Content Creators(WSC Sports)](https://wsc-sports.com/blog/news/tiktok-and-wsc-sports-partner-to-give-rights-holders-a-new-way-to-reach-fans-through-content-creators/)、
  [WSC Sports Acquires Partnerbrite to Unify Content Creation and Sponsorship Activation(WSC Sports)](https://wsc-sports.com/blog/news/wsc-sports-acquires-partnerbrite-to-unify-content-creation-and-sponsorship-activation/)、
  [ニコンと共同で公式サイトに「AIアバター」を導入(アビスパ福岡公式サイト)](https://www.avispa.co.jp/news/post-80230)、
  [中日ドラゴンズ、2026年シーズンのチケット販売概要を発表(フォーメーション)](https://baseball.fromation.co.jp/archives/158475)、
  [2026 MLB ABS challenge system tracker: Team, player rankings(ESPN)](https://www.espn.com/mlb/story/_/id/48305211/2026-mlb-abs-challenge-system-tracker-team-player-rankings)、
  [MLB Teams' ABS Challenge Success Rate Stats Revealed After Opening Month of 2026 Season(Bleacher Report)](https://bleacherreport.com/articles/25422872-mlb-teams-abs-challenge-success-rate-stats-revealed-after-opening-month-2026-season)、
  [World Cup 2026's AI Offside System Now Pipes Calls Straight Into The Referee's Ear(Tech Times)](https://www.techtimes.com/articles/317958/20260607/world-cup-2026s-ai-offside-system-now-pipes-calls-straight-referees-ear.htm)、
  [FIFA's New AI Offside Technology for World Cup 2026(Open Magazine)](https://openthemagazine.com/sports/fifas-new-ai-offside-tech-promises-faster-calls-at-world-cup-2026)

### 2026-07-15: 初版執筆
- **内容**: Part14(業種別 生成AI活用事例)のその他・未分類の章として、スポーツ業界の
  パフォーマンス分析・トラッキング(MLB Statcast、NBA Inside the Game powered by AWS、
  Wimbledon×IBM watsonx)、実況・ハイライト自動生成(WSC Sports、楽天イーグルスAI解説者)、
  ファンエンゲージメント(Wimbledon Match Chat、JリーグNiiva Talk)、
  チケットのダイナミックプライシング(NPB・Jリーグ・Bリーグ)、
  審判判定支援(MLBロボット審判、サッカーの半自動オフサイド技術)の実在事例を整理した
- **出典**:
  [AI at Bat: How MLB is surfacing stats faster with AI(Google Cloud Blog)](https://cloud.google.com/transform/mlb-statcast-ai-fan-experience-team-analytics)、
  [NBA and AWS announce new multi-year partnership to power the next era of basketball innovation(NBA.com)](https://www.nba.com/news/nba-aws-partnership)、
  [NBA, Amazon Launch "Inside the Game" Defense, Shooting Stats Package(Sportico)](https://www.sportico.com/leagues/basketball/2025/nba-amazon-web-services-inside-the-game-stats-ai-1234872489/)、
  [Wimbledon and IBM Introduce New AI-Powered Fan Experiences and Modernized Digital Platforms for The Championships 2026(IBM Newsroom)](https://newsroom.ibm.com/2026-06-22-wimbledon-and-ibm-introduce-new-ai-powered-fan-experiences-and-modernized-digital-platforms-for-the-championships-2026)、
  [750 million fans and 2.7 million data points: How IBM's AI powers Wimbledon from hidden 'Court 19'(Fortune)](https://fortune.com/2026/07/09/wimbledon-ibm-ai-digital-transformation-sports/)、
  [Why More Teams Are Switching to AI-Powered Sports Analytics(WSC Sports)](https://wsc-sports.com/blog/industry-insights/why-more-teams-are-switching-to-ai-powered-sports-analytics/)、
  [NBA Using GenAI Technology from WSC Sports to Automate Multilingual Content(WSC Sports)](https://wsc-sports.com/blog/customer-spotlight/nba-launches-genai-technology-with-wsc-sports-to-automate-multilingual-content/)、
  [楽天、プロ野球をデータで深掘りする「AI解説者」を披露(AI Watch)](https://ai.watch.impress.co.jp/docs/news/2119086.html)、
  [楽天がプロ野球「AI解説者」今季ベータ提供へ、選手なりきり体験なども(ケータイ Watch)](https://k-tai.watch.impress.co.jp/docs/news/2119107.html)、
  [２０２５ＪリーグYBCルヴァンカップ決勝の特設Webサイトにおいて「ＪリーグキングAIアバタープロジェクト powered by Nikon」を公開(Jリーグ公式)](https://www.jleague.jp/sp/news/article/32187/)、
  [ダイナミックプライシングで野球チケットはいくら高くなった？(チケットラボ)](https://lab.ticketme.co.jp/pricing/dynamic-pricing/dynamic-pricing-baseball/)、
  [プロ野球「ダイナミックプライシング」価格変動に憤り 空席散見でも「満員御礼」に(ニフティニュース)](https://news.nifty.com/article/sports/athletic/12378-4116358/)、
  [勝ち続けるためのデータ活用。福岡ソフトバンクホークスの強さの仕組み(ソフトバンクニュース)](https://www.softbank.jp/sbnews/entry/20260402_02)、
  [ダイナミックプライシング（価格変動制）について(川崎フロンターレ公式)](https://www.frontale.co.jp/tickets/dynamic_pricing.html)、
  [2025-26ダイナミックプライシングについて(アルバルク東京公式)](https://www.alvark-tokyo.jp/news/detail/id=18154)、
  [ロボット審判導入は必然？ MLBは１年で３万超の誤審撲滅、欧州サッカーも2030年までに(REAL SPORTS)](https://real-sports.jp/page/articles/346535691586372833/)、
  [MLB、「ロボット審判」を来季から正式導入 ボール・ストライクの一部を自動判定(Full-Count)](https://full-count.jp/2025/09/24/post1832864/)、
  [How does semi-automated offside technology work in football?(The FA)](https://www.thefa.com/news/2025/feb/27/emirates-fa-cup-semi-automated-offside-explainer-20252702)、
  [Semi-automated offside technology(FIFA Inside)](https://inside.fifa.com/innovation/innovating-the-game/semi-automated-offside-technology)
