---
title: 医療・ヘルスケアにおける生成AI活用事例
part: 13
chapter: "第4章 医療・ヘルスケア"
tags: [医療, ヘルスケア, 生成AI活用事例, アンビエントAIスクライブ, 画像診断支援, 医薬品開発]
created: 2026-07-06
updated: 2026-07-23
---

# 医療・ヘルスケアにおける生成AI活用事例

## これは何か

医療・ヘルスケア業界は「深刻な人手不足」「膨大な文書作成業務」「専門知識の更新速度」
という慢性課題を抱える一方、誤情報や見落としが患者の生命に直結するため、
生成AI・AIの導入には他業種以上に厳格な精度検証と規制対応が求められる領域である。
本ページは、実在する医療機関・企業の導入事例を「問診・診療記録作成支援」
「医療文献調査・エビデンス検索」「患者向け説明・問い合わせ対応」「画像診断支援」
「医薬品開発・治験」という業務領域別に整理し、自院・自社に応用する際に
何を参考にし、何に注意すべきかを示す事例カタログである。

## 業務領域別の活用マップ

| 業務領域 | 課題 | AI・生成AIの役割 | 代表事例(本ページ内) |
|---|---|---|---|
| 問診・診療記録作成支援 | 診療後の記録業務(いわゆる「カルテ残業」)による医師・看護師の燃え尽きと人手不足 | 診察室の会話を音声認識し、生成AIがカルテ・診療記録・退院時サマリーの下書きを自動生成する「アンビエントAIスクライブ」 | Microsoft Dragon Copilot(旧DAX Copilot)/ Ubie生成AI・medimo(兵庫医科大学病院)/ OPTiM AIホスピタル(慢性期病院) |
| 医療文献調査・エビデンス検索 | 医学論文・ガイドラインの更新量が多く、最新のエビデンスを人手で追い切れない | RAG(検索拡張生成、社内外の文書を検索してから回答を生成する仕組み)で論文・ガイドラインを検索し、出典付きで要約回答する | OpenEvidence / Mayo Clinic × Google Cloud |
| 患者向け説明・問い合わせ対応 | 診察時間の制約による説明不足、患者の不安・疑問への対応不足 | AIアバターやチャットボットが問診・症状の聞き取りや、疾患・治療の説明を行う | 大阪国際がんセンター「対話型疾患説明生成AI」 |
| 画像診断支援 | 放射線科医・内視鏡医などの読影医不足、疲労による所見の見落とし | 異常検知は従来型の認識系AI(画像分類・検出モデル、国内はPMDA承認のSaMDとして実装)が担い、生成AIは所見文章の作成・要約を担う分業が進む | Aidoc「First Read」/ Cognita「Cognita CXR」/ Google「MedGemma」/ AIメディカルサービス「gastroAI model-G3」 |
| 医薬品開発・治験 | 新薬開発に要する期間(平均10年以上)とコスト(数百億円規模)の膨大さ | 生成AIが候補化合物の分子構造を生成し、標的探索・治験成功率予測までを高速化 | Insilico Medicine |

**読み方のコツ**: 「問診・記録作成」「患者対応」は自然言語の生成・要約が主役のため
生成AI(LLM)がそのまま活躍しやすい領域である。一方「画像診断支援」は
**異常検知そのものは従来型の認識系AI(画像分類・物体検出モデル)が専門**であり、
生成AIは検出結果を人間が読める所見文に変換する役割を担うことが多い
(「生成AIが画像を見て病気を見つける」という理解は正確ではない点に注意)。

## 代表事例の詳細

### 1. 問診・診療記録作成支援(海外): Microsoft Dragon Copilot(旧Nuance DAX Copilot)

- **企業・製品**: Microsoft社。2022年に音声認識大手Nuance Communicationsを買収し、
  アンビエント音声認識サービス「DAX(Dragon Ambient eXperience)」を展開。
  2025年3月に音声入力の「Dragon Medical One」と統合し「Dragon Copilot」に名称変更
- **課題**: 医師が診察後にカルテ記載・要約作成に費やす時間(「カルテ残業」)が
  燃え尽き症候群(バーンアウト)の主要因の一つになっている
- **導入したAI・仕組み**: 診察室での医師と患者の会話をマイクで収集し、
  アンビエントAI(周囲の音声を常時聞き取るAI)が発話内容から構造化された
  診療記録の下書きを自動生成する。2026年3月のHIMSS(米国最大級の医療IT展示会)では
  「エージェント型」の臨床アシスタントへ進化したことを発表し、「Work IQ」という
  基盤機能により電子カルテ(EHR)の患者データと、メール・Teamsチャット・PDFなど
  周辺の業務データを横断して回答できるようになった。対象職種も医師に加え
  看護師・放射線科医にまで拡大し、9か国でサービスを提供している
- **効果**: UCLA Healthが14専門領域238人の外来医師を対象に実施した
  ランダム化比較試験(NEJM AI, 2025年)では、DAX Copilot利用群は
  バーンアウト指標(Mini-Z)が2.8ポイント改善し、業務負荷指標が39.9ポイント低下した。
  一方でカルテ記載にかかる時間そのものの短縮効果は1.7%減と統計的に有意ではなく、
  「時間短縮」より「精神的負荷の軽減」で効果が出た点が特徴的である。
  2026年3月時点で1日あたり10万人以上の臨床医が日常的に利用していると発表されている
- **自社への応用ヒント**: アンビエントAIスクライブの効果測定を「作業時間」だけで
  評価すると過小評価になりかねない。バーンアウト・満足度といった
  定性的な指標も含めて効果を測ることが、この種のツールの価値を正しく捉える鍵になる。
  また、Microsoftは地方の中小病院向けに60%割引の提供イニシアチブを2026年に開始しており、
  「都市部の大病院向け高額ツール」という先入観は薄れつつある

### 2. 問診・診療記録作成支援(国内): Ubie生成AI/medimo(兵庫医科大学病院)

- **企業**: Ubie株式会社(問診AI大手)、株式会社medimo(医学部生が創業した診療支援ツール開発企業)
- **課題**: インフォームドコンセント(治療・手術前の説明と同意)や日々の診療記録の
  文字化・カルテ記載に医師・看護師の時間が割かれている
- **導入したAI・仕組み**: 「ユビー生成AI」は音声要約機能により診療記録・IC記録の
  作成を支援する機能で、2026年1〜2月時点で大学病院10施設以上を含む全国100病院に導入。
  「medimo」は音声認識と生成AIを組み合わせ、医師と患者の会話からわずか数秒で
  カルテ下書きを自動生成するツールで、2025年6月に兵庫医科大学病院が
  大学病院として全国初の正式導入をした
- **効果**: Ubie生成AIについては、南部徳洲会病院がIC記録作成など月間約4,000件の
  業務に音声要約機能を活用し、月約200時間の業務時間を創出したと報告されている。
  2026年に発表された琉球大学病院の事例では、活用範囲を「カルテ作成」以外にも広げ、
  CRC(治験コーディネーター)によるレジストリ登録業務の処理速度を1時間あたり1.85件から
  4.31件へと2.33倍に高速化したほか、緊急転院時にFAXで届く情報をもとにした
  入院初期記録の作成時間を約2時間から最短5分へ短縮したと報告されている
- **自社への応用ヒント**: 海外のDAXと同様、日本でも「音声→生成AIによる下書き→
  医師が確認・修正」という三段構えのワークフローが共通している。
  生成AIに記録を「完成させる」ことを期待せず、最終確認は必ず医師・看護師が行う
  前提で設計されている点が、医療分野でのAI活用の型として参考になる。
  琉球大学病院の事例が示すように、プロンプトを現場ごとにカスタマイズできる生成AIは
  「カルテ記載」という狭い用途にとどまらず、治験事務や緊急時対応など
  周辺業務にも横展開しやすいことが強みである

### 2'. 診療記録作成支援(国内・慢性期病院ほか): OPTiM AIホスピタル

- **企業**: 株式会社オプティム
- **課題**: 大学病院など急性期の大規模病院だけでなく、慢性期病院(長期療養を担う病院)
  でも看護サマリー・診療情報提供書・退院時サマリーなどの文書作成負担は重く、
  医師・看護師が本来の診療・ケア業務に割く時間を圧迫している
- **導入したAI・仕組み**: 国内初とうたうオンプレミス(自院サーバー内で完結させる構成)と
  クラウドのハイブリッド型生成AIサービス「OPTiM AIホスピタル」を2025年1月に提供開始。
  退院時看護サマリー・診療情報提供書・医師の意見書・SOAP形式のカルテなどの
  下書きを自動生成する機能に加え、電子カルテと連携する「カルテAIアシスタント」
  「カルテAIサマリー」機能を持つ。2025年10月には慢性期病院として初めて
  医療法人大誠会内田病院に導入された
- **効果**: 社会医療法人祐愛会織田病院では2024年4〜10月の導入により、
  退院時看護サマリー作成にかかる時間を54.2%削減。福岡県済生会二日市病院では
  2025年5月の本稼働後、入院12日以上の患者の退院時看護サマリーの84%をAI活用で作成し、
  関連業務コストを36%削減したと報告されている
- **自社への応用ヒント**: 生成AI活用は大学病院など先進的な大規模施設だけの
  取り組みではない。オンプレミス構成による個人情報保護と、既存の電子カルテベンダー
  (電子カルテ「Chart Man・Go!」「MI・RA・Is」「PrimeKarte」等)との連携実績が
  蓄積されつつあり、中小規模・慢性期病院がベンダー選定をする際の目安になる

### 3. 医療文献調査・エビデンス検索支援(海外): OpenEvidence

- **企業**: OpenEvidence社(米国、2025年から急成長)
- **課題**: 日々更新される医学論文・診療ガイドラインを臨床の合間に人手で
  追い切れず、エビデンスに基づいた判断(EBM)の負担が大きい
- **導入したAI・仕組み**: 医療従事者向けに特化したRAG型の生成AI検索サービス。
  医学専門モデルと最新の医学論文データベースを組み合わせ、
  毎日文献を更新しながら、必ず出典を引用し、根拠不十分な場合は
  回答を保留する設計になっている
- **効果**: 2026年1月時点で米国の医師の約4割が利用し、2025年12月には
  月間1,800万件の臨床相談に利用されたと報告されている。同月にシリーズDで
  2.5億ドルを調達し、企業価値は前回(2025年10月時点60億ドル)から倍増して
  120億ドルに到達。無料の医療AI検索ツールを75万人以上の臨床医が定常的に利用し、
  年換算売上高は3億ドル規模に達したとも報じられている。個人利用にとどまらず、
  電子カルテ(EHR)と統合したエンタープライズ版の病院導入も2026年に相次いでおり、
  Sutter Health(2026年2月)、Mount Sinai(同3月、傘下7病院)、Cedars-Sinai
  (同5月、医師・看護師・薬剤師・セラピストを含む病院全体)が採用を発表している。
  Cedars-Sinaiの事例では、患者の電子カルテ情報(既往歴・併存疾患・薬剤・
  アレルギー等)を踏まえた個別化された文献検索ができる点が特徴とされる
- **自社への応用ヒント**: 「出典を必ず示す」「根拠が薄い場合は答えない」という
  設計方針は、誤情報が命に関わる医療分野での生成AI活用における
  ハルシネーション対策の実例として、他業種のRAGシステム設計にも応用できる。
  医師個人が現場で使い始め、後から病院全体の公式導入に広がるという
  「ボトムアップ型」の普及の仕方も、医療AI導入の典型パターンとして参考になる

### 3'. 医療文献調査・データ活用基盤(海外): Mayo Clinic × Google Cloud

- **企業**: Mayo Clinic(米国大手医療機関)、Google Cloud、Atropos Health
- **課題**: 院内に蓄積された膨大な医療知識・データを、必要なときに
  医療従事者が迅速に検索・参照できる仕組みが不足していた
- **導入したAI・仕組み**: Google Cloudの生成AI検索基盤(Gen App Builder、
  企業向けエンタープライズサーチ機能)を用いた医療情報検索ワークフローを構築。
  併せて、40年分・556万人の患者からの6.44億件の臨床所見を匿名化した
  データプラットフォームを整備し、150以上の組織がAIモデルの開発・検証に参加できる
  基盤とした。Atropos Health社との協業では、医師の質問に応じて
  「Prognostograms」と呼ばれる根拠レポートを自動生成する仕組みも提供している
- **自社への応用ヒント**: 生成AIの検索精度は結局「参照できるデータの質と量」に
  規定される。Mayo Clinicの事例は、生成AI導入の前段としてデータプラットフォーム
  そのものへの投資が不可欠であることを示す好例である

### 4. 患者向け説明・問い合わせ対応(国内): 大阪国際がんセンター「対話型疾患説明生成AI」

- **企業・機関**: 大阪国際がんセンター、医薬基盤・健康・栄養研究所、日本IBM
  (「AI創薬プラットフォーム事業」の共同研究)
- **課題**: 診察時間内では患者の疑問・不安に十分に答えきれず、
  特に乳がんの初診患者は治療方針や副作用への不安を抱えたまま受診することが多い
- **導入したAI・仕組み**: 2024年8月から乳腺・内分泌外科の外来初診患者向けに
  「対話型疾患説明生成AI」の実運用を開始。医師の姿をしたAIアバターと
  生成AIチャットボットを組み合わせ、受診前にPC・タブレット・スマートフォンから
  疾患や治療の流れについて対話形式で説明を受けられる。各学会の診療ガイドラインを
  学習させることで医学的に正しい応答を生成する設計とした。合わせて、
  副作用で文字入力が難しい患者でも音声で日々の体調を記録できる
  「看護音声入力生成AI」も導入している
- **効果**: 来院前に疾患理解を進めることで、実際の診察時間の短縮や
  患者の不安軽減につなげることを目的としている
- **自社への応用ヒント**: 患者向けチャットボットを「何でも答えるFAQ」として
  設計するのではなく、学会ガイドラインなど検証済みの一次情報を土台にした
  RAG構成にすることで、医学的な正確性を確保しながら患者理解を助ける説明を
  自動生成できる。同様の仕組みは「心臓疾患に関する相談に24時間365日対応する」
  ニューハート・ワタナベ国際病院の「AIニューハート」(2025年10月リリース)など、
  国内の専門病院にも広がりつつある

### 5. 画像診断支援: Aidoc「First Read」・Cognita・Google「MedGemma」・国内の内視鏡AI

- **企業**: Aidoc社(イスラエル発、画像診断AI大手。世界約2,000施設に導入)、
  Cognita社(スタンフォード発、放射線科大手Radiology Partnersが2025年末に買収)、
  Google DeepMind、株式会社AIメディカルサービス(国内)
- **課題**: 放射線科医・内視鏡医の不足と読影業務の増加により、画像診断のスループットと
  正確性の両立が難しくなっている
- **導入したAI・仕組み**: 「所見の下書きを生成AIが書く」領域でFDA(米食品医薬品局)の
  ブレークスループ・デバイス指定(画期的な医療機器を優先審査する制度で、
  指定自体は正式な販売承認ではない)を取得する動きが2026年に相次いだ。
  Aidocの「First Read」は胸部X線画像を解析し、命に関わる4つの重要所見について
  読影レポートの下書き文章を生成するAIで2026年6月に指定を取得。
  Cognitaの「Cognita CXR」は胸部X線の読影を支援する生成AI(視覚言語モデル)として
  2026年3月に同種の指定を取得した業界初の事例とされる。
  異常の検出自体は従来型の画像分類・検出モデルが担い、生成AIは検出結果を
  読影レポートの文章に変換する役割を担う。最終的な確認・修正・署名は
  放射線科医が行う設計になっている。Google DeepMindの医療特化モデルは
  2026年1月に「MedGemma 1.5」へ更新され、胸部X線に加えて3D CT・MRI、
  病理の全体スライド画像、検査値の構造化抽出なども扱えるようになったが、
  依然として開発者向けの基盤モデルであり、病院がそのまま導入できる
  完成品としては提供されていない。国内では画像診断支援AIはPMDA
  (医薬品医療機器総合機構)の承認を受けたプログラム医療機器(SaMD)として
  実運用されており、株式会社AIメディカルサービスの内視鏡画像診断支援ソフト
  「gastroAI model-G3」が2026年5月に製造販売承認を取得し、同年夏から
  順次販売開始予定である(胃内視鏡動画から早期胃がん・腺腫の疑い領域を
  最大3か所まで検出しリアルタイムに映像へ重畳表示する)
- **効果**: Aidocは1,600以上の病院・150以上の米国医療システムに導入されている。
  Rad AI社は2026年6月、米Yale New Haven Health System(16以上の外来画像センター・
  5病院キャンパス、年間70万件超の検査を持つ医療システム)との提携を拡大し、
  同システム全体の読影レポート生成基盤として展開することを発表した。
  「所見の下書き生成」という領域での生成AI活用が2025〜2026年に急速に広がっている
- **自社への応用ヒント**: 「画像診断AI」と一括りにせず、
  (1)異常を検出する認識系AI(従来型の機械学習・ディープラーニング、国内では
  gastroAI model-G3のようにPMDA承認済みSaMDとして実装される)と、
  (2)検出結果を人間が読める文章にする生成AI、を役割分担で捉えることが重要。
  「ブレークスループ・デバイス指定」は開発を後押しする制度であって
  販売承認そのものではない点も、導入検討時に見誤りやすいポイントである

### 6. 医薬品開発・治験: Insilico Medicine

- **企業**: Insilico Medicine(香港発、生成AI創薬のグローバル臨床段階バイオテック企業)
- **課題**: 新薬開発は従来、候補化合物の探索から臨床試験入りまでに
  6年以上・4億ドル以上のコストがかかるとされ、成功率の低さが課題だった
- **導入したAI・仕組み**: 標的探索プラットフォーム「PandaOmics」、
  AI駆動型の低分子化合物生成プラットフォーム「Chemistry42」、
  治験結果予測プラットフォーム「inClinico」を組み合わせ、
  生成AIが疾患に有効な可能性のある新規の分子構造を大量に生成・評価する
- **効果**: 特発性肺線維症(IPF)治療薬候補「レントセルチブ(Rentosertib、旧称
  ISM001-055/INS018_055)」は、標的探索から治験候補選定までを生成AIが担った
  初の医薬品候補の一つとされ、2025年に第2相(IIa相)の結果をNature Medicine誌に
  発表した後、2026年7月に第3相(最終段階の大規模臨床試験)を開始したと発表された。
  従来手法では6年・4億ドル以上を要する工程を、同社は3分の1の期間・10分の1の
  コストで達成したと報告している。同社は炎症性腸疾患(IBD)治療薬候補
  「ガルタドスタット」の第2相治験や、NLRP3阻害薬「ISM8969」の
  米FDA・中国当局への治験許可(IND)取得など、パイプライン全体を拡大している
- **自社への応用ヒント**: 医薬品開発における生成AIの価値は「候補の質」ではなく
  「候補を大量に、高速に生成・絞り込みできること」にある。
  探索フェーズを高速化しても、臨床試験自体の期間・コストは変わらないため、
  投資判断では「開発初期のリードタイム短縮」という限定的な効果として
  評価するのが実態に近い。レントセルチブが第3相まで進んだことは、
  生成AI創薬が「話題性」の段階を超え、実際に規制当局の審査プロセスを
  通過し得ることを示す材料として参考になる

## 注意点・よくある誤解

- **誤情報が命に関わる**: 医療分野のハルシネーション(もっともらしい誤情報)は
  他業種と異なり患者の生命・健康に直結する。OpenEvidenceの「根拠不十分なら
  回答を保留する」設計や、各事例に共通する「AIは下書き、最終確認は必ず医師・
  看護師」という運用は、精度要件が特に厳しい医療分野での標準的な安全策である
- **医師法・薬機法上の規制**: 日本では診断・治療の最終判断は医師法第17条により
  医師が行う医療行為とされ、AIはあくまで支援にとどまる。画像診断支援など
  「診断」に関わるプログラムは薬機法上の医療機器プログラム(SaMD)として
  PMDA(医薬品医療機器総合機構)の承認・認証が必要であり、汎用の生成AI
  (ChatGPT等)をそのまま疾病の診断・治療目的で販売・提供することはできない。
  内視鏡AI「gastroAI model-G3」(2026年5月承認)のように、国内では画像診断支援AIは
  実際にSaMDとして個別に承認を取得したうえで販売されている。
  厚生労働省・経済産業省のガイドラインでもこの区別が明記されている
- **診療報酬による導入インセンティブ**: 2026年度診療報酬改定では「AI・ICT活用の
  推進」が基本方針に明記され、退院時サマリーや診療情報提供書の作成に生成AIを
  活用した場合、医師事務作業補助者の配置基準上、補助者1人を最大1.2〜1.3人分として
  カウントできる仕組みが導入された。文書作成支援ツールの導入は、単なる
  「効率化」ではなく診療報酬上のメリットにも直結するようになっており、
  導入検討時には自院が該当する加算要件を確認する価値がある
- **個人情報・医療データの取り扱い**: 患者の会話・カルテ情報を生成AIに
  入力する際は、個人情報保護法に加えて次世代医療基盤法(医療分野の研究開発に
  資するための匿名加工医療情報に関する法律)の枠組みを踏まえる必要がある。
  実務では「閉域接続」「入力データを学習に使わない設定」を必須条件とし、
  まずは議事録要約など患者情報を含まない領域から導入し、
  段階的に診療記録作成・臨床支援へと広げるアプローチが取られることが多い
- **「生成AI」と「認識系AI」を混同しない**: 画像診断支援の項目で見たように、
  異常検知そのものは従来型の画像分類・検出モデルが担うことが多く、
  生成AI(LLM)は所見文章の生成・要約という補完的な役割にとどまる場合が多い。
  「生成AIが病気を見つけてくれる」という理解は誤解を招きやすい
- **効果測定は「時間」だけでなく「負荷」も見る**: UCLA HealthのDAX Copilot試験が
  示すように、アンビエントAIスクライブは記録時間そのものの短縮効果が
  必ずしも大きくない場合でも、燃え尽き症候群の軽減という別の価値を生むことがある。
  導入効果をタスク時間だけで測ると過小評価になりうる

## 最初の一歩

自院・自社の医療関連業務で「文書作成・記録に最も時間がかかっている工程」を1つ選び、
その工程が患者の個人情報を直接扱わない範囲(議事録要約・院内マニュアル検索など)
から生成AI活用を試せないか検討することから始めるとよい。

## 関連トピック

- [RAG(検索拡張生成)の基本](../part07-data-analysis/rag-basics.md)
- [ハルシネーションとその対策](../part04-risk-security/hallucination-and-countermeasures.md)
- [AIの分類と生成AIの位置づけ](../part01-ai-basics/ai-classification-and-generative-ai.md)
- [製造業における生成AI活用事例](manufacturing-ai-use-cases.md)
- [製薬業界における生成AI活用事例](pharmaceutical-industry-ai-use-cases.md)

## 更新履歴

### 2026-07-23: 2026年前半の最新動向を反映して全事例を更新・国内新事例を追加
- **内容**: Microsoft Dragon Copilotのエージェント型アシスタントへの進化(HIMSS 2026)、
  Ubie生成AIの琉球大学病院での治験事務・緊急時記録への横展開、国内の慢性期病院向け
  オンプレミス生成AI「OPTiM AIホスピタル」(織田病院・済生会二日市病院・内田病院)を
  新事例として追加、OpenEvidenceの評価額120億ドル到達とSutter Health・Mount Sinai・
  Cedars-SinaiへのEHR統合型エンタープライズ導入拡大、画像診断支援にCognita CXR・
  Rad AI(Yale New Haven Health提携拡大)・国内SaMD承認事例「gastroAI model-G3」
  (AIメディカルサービス)を追加してMed-GeminiをMedGemma 1.5に更新、
  Insilico Medicineのレントセルチブが第3相治験入りしたことを反映。
  注意点に2026年度診療報酬改定によるAI活用インセンティブ(医師事務作業補助者の
  配置基準優遇)を追加した
- **出典**:
  [Unify. Simplify. Scale: Microsoft Dragon Copilot meets the moment at HIMSS 2026(Microsoft公式)](https://www.microsoft.com/en-us/microsoft-cloud/blog/healthcare/2026/03/05/unify-simplify-scale-microsoft-dragon-copilot-meets-the-moment-at-himss-2026/)、
  [Microsoft Upgrades Dragon Copilot to an Agentic Clinical Assistant at HIMSS 2026(HIT Consultant)](https://hitconsultant.net/2026/03/05/microsoft-dragon-copilot-himss-2026-agentic-clinical-ai-nurses-radiologists/)、
  [Microsoft's Dragon Copilot Healthcare AI Assistant Gets Rural Push(Winbuzzer)](https://winbuzzer.com/2026/03/06/microsoft-dragon-copilot-rural-hospitals-himss-2026-xcxwbn/)、
  [OpenEvidence hits $12B valuation, with new round led by Thrive, DST(TechCrunch)](https://techcrunch.com/2026/01/21/openevidence-hits-12b-valuation-with-new-round-led-by-thrive-dst/)、
  [Cedars-Sinai Deploys OpenEvidence Enterprise Platform to Drive Precision Clinical Decision Support(HIT Consultant)](https://hitconsultant.net/2026/05/20/cedars-sinai-deploys-openevidence-enterprise-clinical-ai/)、
  [琉球大学病院「ユビー生成AI」活用で臨床研究業務を2.33倍に効率化、緊急転院時の入院初期記録作成も2時間から5分に短縮(Ubie株式会社)](https://prtimes.jp/main/html/rd/p/000000214.000048083.html)、
  [琉球大学病院が生成AI導入で臨床研究業務を2.33倍に効率化(IoTNEWS)](https://iotnews.jp/medical-healthcare/273644/)、
  [「ユビー生成AI」，大学病院10施設以上を含む全国100病院へ導入(Innervision)](https://www.innervision.co.jp/sp/products/release/20260319)、
  [オンプレミスLLM搭載サービス「OPTiM AI ホスピタル」によって退院時看護サマリー作成にかかる時間を54.2%削減(OPTiM)](https://www.optim.co.jp/media/cat-case/aih_251006-01)、
  [慢性期病院初、病院向け生成AI搭載サービス「OPTiM AI ホスピタル」を医療法人大誠会内田病院で導入(OPTiM)](https://www.optim.co.jp/newsdetail/20251023-pressrelease-01)、
  [病院向けオンプレミス生成AI搭載サービス「OPTiM AI ホスピタル」、福岡県済生会二日市病院に導入(OPTiM)](https://www.optim.co.jp/newsdetail/20250515-pressrelease-01)、
  [FDA gives generative AI in radiology two breakthrough designation nods(STAT)](https://www.statnews.com/2026/06/25/radiology-generative-ai-cognita-aidoc-fda-breakthrough-designation/)、
  [Mosaic Clinical Technologies Announces FDA Breakthrough Device Designation for Cognita's Generative AI Model for Radiology(BusinessWire)](https://www.businesswire.com/news/home/20260304633206/en/Mosaic-Clinical-Technologies-Announces-FDA-Breakthrough-Device-Designation-for-Cognitas-Generative-AI-Model-for-Radiology)、
  [Yale New Haven Health Modernizes Legacy Radiology Infrastructure With Rad AI(PR Newswire)](https://www.prnewswire.com/news-releases/yale-new-haven-health-modernizes-legacy-radiology-infrastructure-with-rad-ai-302795825.html)、
  [Next generation medical image interpretation with MedGemma 1.5 and medical speech to text with MedASR(Google Research)](https://research.google/blog/next-generation-medical-image-interpretation-with-medgemma-15-and-medical-speech-to-text-with-medasr/)、
  [AIメディカルサービス、内視鏡画像診断支援ソフトウェアgastroAI model-G3の製造販売承認を取得(Innervision)](https://www.innervision.co.jp/sp/products/release/20260623)、
  [Insilico Initiates Phase III Clinical Trial for Rentosertib(Insilico Medicine公式)](https://insilico.com/news/xmjsn4l091-insilico-initiates-phase-iii-clinical-tr)、
  [Insilico Medicine Launches Phase III Trial for AI-Developed Drug(Bio-IT World)](https://www.bio-itworld.com/news/2026/07/08/insilico-medicine-launches-phase-iii-trial-for-ai-developed-drug)、
  [令和8年度診療報酬改定 医師事務作業補助体制加算×生成AIで1人が最大1.3人換算に(enishia)](https://enishia-inc.co.jp/2026/02/24/2026_015/)

### 2026-07-06: 初版執筆
- **内容**: Part13(業種別 生成AI活用事例)の医療・ヘルスケアの章として、
  問診・診療記録作成支援(アンビエントAIスクライブ)・医療文献調査・エビデンス検索・
  患者向け説明・問い合わせ対応・画像診断支援・医薬品開発・治験の5業務領域について、
  実在機関・企業の導入事例(Microsoft Dragon Copilot/DAX Copilot・Ubie生成AI・
  medimo(兵庫医科大学病院)・OpenEvidence・Mayo Clinic×Google Cloud・
  大阪国際がんセンター・Aidoc・Google DeepMind Med-Gemini・Insilico Medicine)を
  具体的な効果とともに整理し、医師法・薬機法・次世代医療基盤法など
  医療特有の規制・精度要件への注意点も付記した
- **出典**:
  [Nuance DAX Copilot Review 2026(Vero)](https://www.veroscribe.com/blog/nuance-dax-review-2026)、
  [Microsoft Dragon Copilot(Microsoft公式)](https://www.microsoft.com/en-us/health-solutions/clinical-workflow/dragon-copilot)、
  [Ambient AI Scribes in Clinical Practice: A Randomized Trial(NEJM AI)](https://ai.nejm.org/doi/abs/10.1056/AIoa2501000)、
  [UCLA study finds AI scribes may reduce documentation time and improve physician well-being(UCLA Health)](https://www.uclahealth.org/news/release/ucla-study-finds-ai-scribes-may-reduce-documentation-time)、
  [「ユビー生成AI」、大学病院10施設以上を含む全国100病院へ導入(Ubie株式会社)](https://prtimes.jp/main/html/rd/p/000000198.000048083.html)、
  [兵庫医科大学病院、音声認識と生成AIを活用した診療支援ツール「medimo」を大学病院として初正式導入(medimo)](https://prtimes.jp/main/html/rd/p/000000012.000124331.html)、
  [病状説明をAIが自動要約し電子カルテに記録～大学病院で全国初の導入～(兵庫医科大学)](https://www.hyo-med.ac.jp/news/3273/)、
  [医療AIの覇権確定か：OpenEvidenceが評価額120億ドルに到達(XenoSpectrum)](https://xenospectrum.com/openevidence-raises-250m-12b-valuation-medical-ai/)、
  [米国医師40%が選ぶOpenEvidence、医療AI検索の新常識](https://axconstdx.com/2025/12/02/%E7%B1%B3%E5%9B%BD%E5%8C%BB%E5%B8%AB40%E3%81%8C%E9%81%B8%E3%81%B6openevidence%E3%80%81%E5%8C%BB%E7%99%82ai%E6%A4%9C%E7%B4%A2%E3%81%AE%E6%96%B0%E5%B8%B8%E8%AD%98/)、
  [Google-CloudとMayo-ClinicがAI提携(AI総合研究所)](https://www.ai-souken.com/case/473)、
  [米国を代表する医療機関、メイヨークリニックのAI導入(Forbes JAPAN)](https://forbesjapan.com/articles/detail/62632)、
  [乳がん患者の質問に答える「生成AI対話システム」運用開始、大阪国際がんセンター(ASCII.jp)](https://ascii.jp/elem/000/004/219/4219342/)、
  [「AI創薬プラットフォーム事業」の共同研究において、患者に寄り添う医療のための問診生成AIおよび看護音声入力生成AIの実運用を開始(大阪国際がんセンター)](https://oici.jp/center/news/4291/)、
  [Aidoc Receives FDA Breakthrough Device Designation for AI That Drafts Radiology Reports(PR Newswire)](https://www.prnewswire.com/news-releases/aidoc-receives-fda-breakthrough-device-designation-for-ai-that-drafts-radiology-reports-302809910.html)、
  [Advancing Multimodal Medical Capabilities of Gemini(arXiv, Google DeepMind)](https://arxiv.org/pdf/2405.03162)、
  [MedGemma(Google DeepMind公式)](https://deepmind.google/models/gemma/medgemma/)、
  [生成AIで発見・設計された初の医薬品が第II相臨床試験段階に(Insilico Medicine)](https://prtimes.jp/main/html/rd/p/000000016.000075178.html)、
  [より迅速な治療: Insilico Medicine が生成AIで創薬を加速(NVIDIA Blog)](https://blogs.nvidia.co.jp/blog/insilico-medicine-uses-generative-ai-to-accelerate-drug-discovery/)、
  [医療デジタルデータのAI研究開発等への利活用に係るガイドライン(厚生労働省)](https://www.mhlw.go.jp/content/001310044.pdf)、
  [改正次世代医療基盤法について(内閣府健康・医療戦略推進事務局)](https://www8.cao.go.jp/iryou/kouhou/pdf/kaisei_jisedaiiryou_rikatsuyou.pdf)
