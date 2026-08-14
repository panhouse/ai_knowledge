---
title: "生成AIの規制・ガバナンス動向(企業が押さえるべきポイント)"
part: 4
chapter: 第4章 法務・ガバナンス
tags: [EU AI Act, AI事業者ガイドライン, AI推進法, ガバナンス, 法規制, リスク管理]
created: 2026-07-06
updated: 2026-08-14
---

# 生成AIの規制・ガバナンス動向(企業が押さえるべきポイント)

## これは何か

生成AIを業務で使う会社は、「自社が法律違反にならないか」「取引先・海外拠点がある場合に他国の規制に巻き込まれないか」を把握しておく必要がある。しかし各国の規制は法体系も進み方もバラバラで、EUは違反すると巨額の制裁金が科され得る「ハードロー(強制力のある法律)」、日本は罰則のない「ソフトロー(指針・努力義務)」中心、米国は国全体の統一法がなく州ごとに異なる、というように前提が異なる。本ページは、日本の一般的な事業会社(ChatGPT・Gemini・Copilot・Claudeなどを業務利用する立場)が「結局どこまで気にすればよいか」を判断できるよう、各地域の規制の枠組みと、今日からできる社内対応を整理する。著作権に特化した論点は[生成AIの著作権リスクと実務での注意点](./copyright-risks-in-generative-ai.md)を参照。

**本ページは一般的な情報整理であり、法的助言ではない。** 個別の法令適用可否は弁護士に確認すること。また、この分野は法改正・施行時期の変更が非常に頻繁に起きるため、契約・大規模導入の判断時は必ず最新の一次情報を確認すること。

## 仕組み・背景

### EU AI Act: リスクの高さで義務が変わる「ハードロー」、施行スケジュールは「デジタル・オムニバス」で大きく組み替え

EU AI Act(EU人工知能法)は、AIシステムを4段階のリスクに分類し、リスクが高いほど重い義務を課す「リスクベースアプローチ」を採る、世界初の包括的なAI規制法。2024年8月1日に発効した。

| リスク区分 | 内容 | 主な例 | 義務 |
|---|---|---|---|
| 許容できないリスク(unacceptable risk) | 原則禁止 | 潜在意識に働きかける操作的AI、社会的スコアリング、無差別な顔画像スクレイピングなど | 提供・利用ともに禁止 |
| 高リスク(high-risk) | 人の権利・安全に重大な影響 | 採用選考、与信審査、教育の合否判定、重要インフラ制御など(Annex IIIに列挙)。医療機器・機械等に組み込まれるAI(Annex I)も含む | 適合性評価、人による監視、ログ保存、影響評価など重い義務 |
| 限定的リスク(limited risk) | AIだと気づかれない懸念 | チャットボット、ディープフェイク生成、AI生成コンテンツ全般 | 「AIである」ことの開示義務(透明性義務、第50条) |
| 最小リスク(minimal risk) | 上記以外の大半のAI利用 | 迷惑メールフィルタ、社内文書のAI要約など | 法的義務なし(自主的な取り組みは推奨) |

重要なのは「誰の義務か」という区分で、EU AI Actは**提供者(provider)**と**導入事業者(deployer)**を分けている。OpenAI・Google・Anthropic・MicrosoftのようにAIモデル・サービスを開発して市場に出す側が「提供者」、日本の一般的な事業会社のようにChatGPTやCopilotを業務で使う側は基本的に「導入事業者」にあたる。義務の大部分は提供者側に重く課されるが、導入事業者にも以下の義務がある。

- **AIリテラシー確保義務**(第4条、2025年2月2日から適用開始済み): 自社の役職員がAIの仕組み・限界・リスクを理解した上で使えるようにする努力義務
- **透明性義務**(第50条、限定的リスクのAI全般が対象): 自社がチャットボットで顧客対応する場合は「AIと話している」と分かるようにする、AIで画像・音声・動画を加工・生成した場合(ディープフェイク)はその旨を開示する、といった義務。**この義務は後述の「デジタル・オムニバス」による延期の対象外で、2026年8月2日に予定通り適用開始済み**(直接の対人対話、AI生成コンテンツ、感情認識・生体分類、ディープフェイク・公共性の高いAI生成文章の4類型が対象)
- **高リスクAIシステムの導入事業者としての義務**(第26条、自社が採用選考AI・与信審査AIなど高リスク用途を「自社の判断で」導入する場合のみ): 提供者の使用説明書に従った運用、人による監視の担当者配置、自動生成ログを最低6か月保存、職場で使う場合は労働者代表への事前通知、など

**2026年に入って最大の変化は、高リスクAIシステムの義務適用が大幅に延期されたこと。** 欧州委員会が2025年11月に提案した規制簡素化パッケージ「デジタル・オムニバス(Digital Omnibus on AI)」について、欧州議会が2026年6月16日、EU理事会が同月29日に最終合意し、2026年7月8日に成立、**2026年7月24日にEU官報(Official Journal)へ正式公布され、その3日後の7月27日に発効した**(高リスク義務の本来の適用開始日である8月2日の直前というギリギリのタイミングで手続きが完了した形)。これにより、当初2026年8月2日開始予定だった単独型の高リスクAIシステム(Annex III、採用選考・与信審査など)の義務は**2027年12月2日**まで、当初2027年8月2日開始予定だった医療機器・機械等に組み込まれる高リスクAIシステム(Annex I)の義務は**2028年8月2日**まで、それぞれ延期された。一方、前述のチャットボット・ディープフェイクの透明性義務(第50条)は延期対象外のまま**2026年8月2日に適用が始まっており**、欧州委員会は同日付のプレスリリースで「AI法の執行と新たな透明性要件の運用を開始した」と発表している。**「高リスク義務が延期された」というニュースだけで規制対応全体が先送りになったと誤解しないこと。**

制裁金の枠組み自体はオムニバスによる変更を受けていない: 禁止行為への違反は最大3,500万ユーロまたは全世界年間売上高の7%のいずれか高い方、高リスク要件違反は最大1,500万ユーロまたは3%、情報提供義務違反等・透明性義務違反等は最大750万ユーロ〜1,500万ユーロまたは1〜3%(区分による)。これに加え、GPAI提供者への欧州委員会・AI Office(EU AI法の執行機関)の執行権限(文書提出要求、技術評価、是正命令、市場からの撤去命令、制裁金賦課など)は**2026年8月2日に予定通り発効した**(2025年8月2日から適用済みのGPAI義務について、遡って違反を問える1年間の猶予期間が明けた形。同日以降は2025年8月2日時点まで遡って違反が問われ得る)。オムニバスではさらにAI Officeの権限が強化され、継続的な違反に対しては1日あたり全世界売上高の平均5%までの履行強制金(periodic penalty payment)を科せる仕組みも導入された。日本企業でも、EU域内の顧客・従業員にサービス・出力が届く場合は域外適用され得る点に注意。なお、オムニバスはSME(中小企業)向けの簡素化措置を新たに「small mid-cap(中堅企業)」にも拡大し、簡易な技術文書テンプレートや規制サンドボックスへの優先アクセスなどを認めている。

透明性義務(第50条)の実務対応として、欧州委員会は2026年6月10日に「AI生成コンテンツの透明性に関する行動規範(Code of Practice on Transparency of AI-Generated Content)」を公表した。罰則を伴わない任意の指針だが、欧州委員会とAI Board(加盟国当局で構成する審議機関)はこの行動規範を第50条(2)(4)(5)項の義務を果たす現時点で唯一の「妥当(adequate)」な実務手段と位置付けており、2026年7月末時点でIT・通信・教育・小売など約190の事業者が署名済み。署名事業者は一定の適合性推定を受けられる一方、未署名の事業者は個別に遵守を証明する必要があるため、AI生成コンテンツを扱う自社サービスがEU向けにある場合は署名の要否を確認する価値がある。

### 日本: 罰則のない「ソフトロー」中心、実効性は指針の運用と自主ルールの積み上げで確保

日本にはEUのような包括的なAI規制法(義務・罰則を伴う法律)はまだない。2025年5月28日に成立し、同年9月1日に全面施行された「人工知能関連技術の研究開発及び活用の推進に関する法律」(通称: AI推進法・AI新法)は、その名の通り**研究開発・活用の"推進"を目的とした法律**で、事業者への直接的な罰則規定はほとんどない。同法に基づき内閣総理大臣を本部長とする「AI戦略本部」が設置され、2025年12月にAI基本計画が閣議決定された。2026年6月19日には第4回AI戦略本部会合が開催されており、基本計画に基づく施策のフォローアップが継続的に進んでいる。

企業の実務に直接関わるのは、経済産業省・総務省が策定する「AI事業者ガイドライン」。2024年4月の初版公表以降、改訂が重ねられ、**2026年3月31日に公表された第1.2版が2026年8月時点でも最新版**(第1.3版等の後継版はまだ出ていない)。第1.2版の主な変更点は、AIエージェント(人に代わってタスクを自律実行するAI)や物理世界を操作する「フィジカルAI」を新たに定義し、これらについて「人間が最終判断できる仕組み(Human-in-the-Loop)」を求めたこと。ガイドラインは法的拘束力のない任意の指針だが、事業者・行政・生活者共通の3層構造(基本理念・共通の指針・実践のためのガイドライン)を持ち、「知らなかった」では済まされない社会的な行動規範として機能し始めている。

このほか、内閣府知的財産戦略推進事務局が2025年12月26日、生成AIサービスの学習データや設計仕様の開示を求める「生成AIの適切な利活用等に向けた知的財産の保護及び透明性に関するプリンシプル・コード(仮称)」案を公表し、2026年1月26日までパブリックコメントを実施した。強制開示ではなく「コンプライ・オア・エクスプレイン(従わない場合は理由説明)」方式のソフトルールで、2026年8月時点でも正式確定はしておらず、引き続き2026年度中の確定が見込まれている。生成AIサービスを提供する側(社内でAIエージェントやRAGシステムを一般公開する場合など)は今後の動向を要ウォッチ。

### 米国: 連邦統一法がなく、州法のパッチワーク+政権による揺り戻しが訴訟合戦に発展

米国には連邦レベルの包括的なAI規制法がなく、州ごとに異なる法律が並立する「パッチワーク」状態が続いている。2026年に入り、主要な州法が相次いで施行・改廃され、さらに連邦政権が州法を訴訟で無効化しようとする動きが本格化しており、状況は極めて流動的。

- **カリフォルニア州**: フロンティアAI(先端的な基盤モデル)開発企業に安全枠組みの公表・重大インシデント報告・内部告発者保護を義務付ける「Transparency in Frontier Artificial Intelligence Act」(SB 53)が2025年9月29日に成立し、**2026年1月1日から施行・執行が始まっている**(違反は1件あたり最大100万ドルの制裁金、州司法長官が執行)
- **テキサス州**: AIの不正利用(意図的な差別的取扱い、児童性的搾取コンテンツ生成、違法なディープフェイクなど)を禁止し、州政府によるAI利用時の開示義務も定める「Texas Responsible AI Governance Act」(TRAIGA)が2025年6月22日に成立し、**2026年1月1日から施行済み**。違反1件あたり最大20万ドルの制裁金(60日間の是正期間あり)、私人による訴訟は認めず州司法長官のみが執行
- **コロラド州**: 雇用・与信など重要な意思決定にAIを使う事業者に説明責任・影響評価を課す従来のAI法(SB24-205、通称CAIA)は、施行直前の2026年4月9日にxAIが同州を提訴して差止めを求め、同月24日には米司法省(DOJ)も「平等保護条項(Equal Protection Clause)違反」を主張して訴訟に参加、4月27日には裁判所が当事者の共同申立てを認めて**施行を一時停止**する事態となった。その最中の5月14日、ガバナーが新法(SB 26-189)に署名しCAIAを**実質的に廃止・置き換え**、「Automated Decision-Making Technology Act(ADMT法、自動意思決定技術法)」という透明性中心の狭い内容に変わったが、xAIはADMT法自体にも差止めを求める構えを見せており、**訴訟(X.AI LLC v. Weiser)の決着がつくまで施行が事実上凍結された状態**にある。ADMT法の施行日自体は**2027年1月1日**
- **連邦レベル**: トランプ政権が2025年12月11日、「Ensuring a National Policy Framework for Artificial Intelligence」と題する大統領令に署名し、州によるAI規制の乱立(パッチワーク)を問題視。同令に基づき司法省内に設置された「AI Litigation Task Force」が、前述のコロラド州訴訟のように通商条項(州際通商への不当な負担)や平等保護条項などを根拠に州のAI法へ訴訟で対抗する方針を実行に移している。商務省は2026年3月11日を期限に「負担の大きい(onerous)」州法(カリフォルニア・コロラド・テキサスなどが対象と目された)を指定する報告書を作成し、該当州はブロードバンド関連の連邦補助金(BEAD予算)で不利になり得る仕組みも検討されている。議会でも、州のAI規制を3年間凍結する「Great American Artificial Intelligence Act」の草案(下院Obernolte・Trahan両議員が2026年6月4日に公表)が議論されているが、市民団体・一部議員からの反発も強く、2026年8月時点では正式法案としては未提出。なお同種の10年間の州法プリエンプション条項は2025年半ば、予算調整法案の審議中に上院で99対1の反対多数により削除された経緯があり、連邦法による一律のプリエンプションはまだ実現していない

日本企業にとっては「米国は規制の全体像を1つの法律で押さえられない、州単位・かつ変化が速く、しかも連邦と州が訴訟で対立している」という前提を持っておくことが実務上重要で、コンプライアンス上の深追いより「進出先の州の動向を継続的にウォッチする」姿勢で十分なことが多い。特にコロラド州のように、法律が成立していても訴訟により施行が凍結されている場合があるため、「制定済み」と「実際に執行されているか」を分けて確認する必要がある。

### 参考: 中国など他地域の動き

中国は「生成式人工智能服务管理暂行办法」(2023年8月施行)に基づくサービス届出制を運用しており、2026年6月末時点で988件の生成AIサービス、598件のAI応用・機能が登録済み。2026年4月10日には、AIチャットボット等の擬人化された対話サービスを対象とする新規則「人工智能拟人化互动服务管理暂行办法」が公布され、2026年7月15日から施行されている。中国国内向けにAIチャットボット等を提供する場合は追加の届出・表示義務が生じ得るため、中国拠点・中国語圏向けサービスがある場合は個別に確認が必要。

## 使いどころ・使い分け

日本の事業会社にとって、どの規制が「自分ごと」かは、EU・米国との接点の有無と、AIの用途で変わる。

| 地域 | アプローチ | 誰に適用されるか | 日常的にChatGPT/Gemini/Copilotを使う日本企業が実際にすべきこと |
|---|---|---|---|
| EU(AI Act) | ハードロー(罰則・制裁金あり) | EU域内で提供・利用されるAI、またはEU域内の人に出力・影響が及ぶ場合は域外の会社も対象 | EU拠点・EU顧客がある場合のみ本格対応が必要。①社内でAIリテラシー教育を実施済みか確認、②チャットボットやAI生成コンテンツをEU向けに出している場合は「AI利用」の明記(透明性義務、既に2026年8月2日に適用開始済み)を確認、③採用・与信などの高リスク用途にAIを使っているかを棚卸し(高リスク義務は2027〜2028年に延期されたが、いずれ来る前提で準備) |
| 日本(AI事業者ガイドライン・AI推進法) | ソフトロー(罰則なし、努力義務) | 日本国内でAIの開発・提供・利用を行う全事業者(努力義務として) | 全社が対象。①ガイドライン第1.2版の考え方に沿った社内AI利用ポリシーの策定、②AIエージェントを使う場合はHuman-in-the-Loop(人による最終確認)の組み込み、③生成AIサービスを外部提供している場合はプリンシプル・コード(知財の開示ルール、2026年8月時点で未確定)の確定動向をウォッチ |
| 米国(州法・大統領令) | 州ごとのハードロー+連邦は訴訟で対抗 | 各州に拠点・顧客・従業員がいる企業(米国子会社がある日本企業を含む) | 米国拠点がある場合は要注意。①カリフォルニア・テキサス両州は既に施行済みのため該当事業がないか確認、②コロラド州は新法(ADMT法、2027年1月施行予定)がxAI・DOJによる訴訟で施行凍結中のため現時点で執行はされていない点を確認、③連邦と州の法廷闘争・議会での州法凍結法案(Great American AI Act)は流動的なため最新の状況を都度確認 |

判断の目安はシンプルで、「EU・米国に拠点や顧客がなく、国内向けの一般的な文章生成・要約・議事録作成などにAIを使っているだけ」であれば、当面はEU AI Act・米国州法の実務対応は不要で、日本のAI事業者ガイドラインに沿った社内ルール整備を優先すればよい。EU域内向けにチャットボットやAI生成コンテンツを提供している、採用・与信・人事評価など「人に対する重要な判断」にAIを組み込んでいる、米国(特にカリフォルニア・テキサス・コロラド)に子会社・従業員がいる、のいずれかに該当する場合は、該当地域の規制動向を継続的にウォッチする体制が必要になる。

## 実務での使い方

### 社内で今すぐ着手できるチェックリスト

1. **AI利用ポリシーを文書化する**: 「業務でAIに入力してよい情報の範囲」「AI出力をそのまま対外公開してよい条件」「利用してよいツール・モデルの一覧」を1枚のドキュメントにまとめる。AI事業者ガイドライン第1.2版の「共通の指針」(人間中心、安全性、公平性、プライバシー保護、セキュリティ確保、透明性、アカウンタビリティ、教育・リテラシー、公正競争、イノベーションなど)を項目立ての参考にすると抜け漏れが少ない
2. **利用ログを記録する仕組みを作る**: いつ・誰が・どのツール・どのモデルで・何の業務に使ったかを最低限記録しておく。EU高リスク義務の「ログ6か月保存」やコロラド州新法の「記録3年保存」のような具体的要件がなくても、社内説明責任(トラブル時に経緯を説明できること)の観点で有効
3. **高リスク用途は事前チェックを必須化する**: 採用選考、人事評価、与信審査、価格決定など「人の処遇に直結する判断」にAIを使う、または使う計画がある場合は、通常の利用ポリシーとは別に法務・人事による事前レビューを通すルールを設ける。EUの高リスク分類(Annex III)の対象領域(雇用、教育、与信、重要インフラ、法執行等)や米コロラド州新法(ADMT法、現在は訴訟で施行凍結中)が定める「重要な意思決定」領域(雇用・住宅・与信・保険・医療・教育・行政サービス)は、日本企業にとっても「重点チェック対象」の目安になる
4. **AIエージェント・自動実行系の機能にHuman-in-the-Loopを組み込む**: メール自動送信、契約書自動生成、決済・発注の自動実行など、人の確認なしにAIが最終アクションまで完結する機能を導入する際は、必ず人が最終承認するステップを残す(AI事業者ガイドライン第1.2版が明示的に求める考え方)
5. **利用ベンダーの規制対応状況を確認する**: OpenAI・Google・Microsoft・Anthropicなどの利用規約・トラストセンターで、EU AI Actへの対応方針(2026年8月2日にGPAI提供者への執行権限が発効済みである点、AI生成コンテンツの透明性行動規範への署名状況を含む)、データ処理の所在地などを確認する。特にEU顧客がいる場合、自社が「導入事業者」としての義務を果たすには、まず提供者側が使用説明書・リスク情報を適切に開示しているかが前提になる
6. **社内向けAIリテラシー研修を実施する**: 「AIは誤った情報を出し得る(ハルシネーション)」「学習データの著作権リスク」「入力情報が学習に使われる可能性」など基本的なリスクを、AIを使う全社員が理解している状態を作る。EUでは既に法的義務(第4条)だが、日本でも社内ガバナンスの土台として有効

### ツール横断での確認ポイント(規制対応の一次情報源)

| ツール | 確認すべき一次情報 |
|---|---|
| ChatGPT / OpenAI API | OpenAIのTrust portal、Enterprise Privacy、利用規約(データ利用・地域対応の記載) |
| Gemini / Vertex AI | Google Cloudのコンプライアンス関連ページ、AI原則ページ |
| Copilot | Microsoft LearnのResponsible AI関連ドキュメント、Copilotのデータ保護に関する説明 |
| Claude | AnthropicのTrust Center、利用規約・Acceptable Use Policy |

いずれも規約・対応方針の改定頻度が高いため、EU顧客向けサービスなど規制の影響が大きい用途を始める前には必ず最新版を確認する。

## 注意点・よくある誤解

- **「日本には罰則がないから何も気にしなくてよい」は誤り**: AI事業者ガイドラインは法的拘束力がないが、事故・トラブルが起きた際の「相当な注意を払っていたか」の社会的な判断基準として機能し得る。ガイドラインに沿った社内体制がないことは、レピュテーションリスクや取引先からの信用低下につながり得る
- **EU AI Actは「EUに支店がある会社だけの話」ではない**: EU域内の顧客・ユーザーに影響が及ぶAIシステムの提供・利用は、日本本社のみの会社でも域外適用の対象になり得る。越境ECやグローバル向けSaaSでAIを使っている場合は要確認
- **「高リスク義務が延期された=安心してよい」ではない**: デジタル・オムニバス(2026年7月24日公布・27日発効)による延期は高リスク(Annex III/Annex I)義務が中心(それぞれ2027年12月・2028年8月まで延期)で、チャットボット・ディープフェイクの透明性義務(第50条)やGPAI提供者への執行権限は延期されず、いずれも2026年8月2日に予定通り適用・発効済み。「延期」のニュースだけを見て全体が先送りになったと誤解しないこと
- **米国の州法は「制定されたら終わり」ではない**: コロラド州のAI法(CAIA)はxAI・DOJの訴訟により施行直前に一時停止され、事実上廃止・置き換えとなって内容も義務範囲も縮小されたが、後継のADMT法自体も同じ訴訟の対象になり施行が事実上凍結中。カリフォルニア・テキサス両州のように既に施行済みの州法もあれば、施行直前で内容が大きく変わったり訴訟で止まったりする州法もあり、「制定時点の情報」のまま止めておくと実態と乖離する
- **規制の施行時期は非常に流動的**: EU AI Actの高リスク義務は既に複数回スケジュールが見直されており、米国では連邦(大統領令・DOJ AI Litigation Task Forceの訴訟、商務省による州法認定、議会の3年間プリエンプション草案)と州法が法廷・議会の両方で対立する展開になっている。「いつ・何が施行されるか」は本ページ更新時点(2026年8月)のスナップショットであり、契約や大規模投資の判断前には必ず最新情報を確認する
- **提供者(vendor)の対応とは別に、自社の対応が必要な場面がある**: EU AI Actでは「提供者が対応していれば導入事業者は何もしなくてよい」わけではなく、人による監視の配置、ログ保存、労働者への通知など、導入事業者(自社)側の義務が独立して存在する
- **規制対応とセキュリティ対策は別軸で管理する**: 情報漏洩対策(社内データの入力制限など)は規制の有無に関わらず必要な対策であり、規制対応チェックリストと混同せず、[生成AI利用における情報漏洩対策](./information-leakage-prevention.md)は別途整備する

## 最初の一歩

自社が「EU域内の顧客・従業員がいるか」「米国(特にカリフォルニア・テキサス・コロラド)に子会社があるか」「採用・与信など人の重要な判断にAIを使っているか」の3点を洗い出し、どれにも該当しなければ、AI事業者ガイドライン第1.2版を参考に社内AI利用ポリシーの有無を確認するところから始める。

## 関連トピック

- [生成AIの著作権リスクと実務での注意点](./copyright-risks-in-generative-ai.md)
- [生成AI利用における情報漏洩対策](./information-leakage-prevention.md)

## 更新履歴

### 2026-08-14: EU施行確定・米国の訴訟合戦を反映して最新化
- **内容**: EUは「デジタル・オムニバス」が2026年7月24日にEU官報へ正式公布・7月27日発効し、高リスク義務の延期(Annex III 2027年12月2日、Annex I 2028年8月2日)が確定したこと、透明性義務(第50条)とGPAI提供者への欧州委員会・AI Office執行権限が延期対象外のまま2026年8月2日に予定通り適用・発効し、欧州委員会が同日付で執行開始を発表したことを追記。透明性義務の実務対応として2026年6月10日公表の「AI生成コンテンツの透明性行動規範」(約190事業者が署名、欧州委員会が唯一の適合性推定手段と位置付け)を新規追加。米国は最大の変化として、コロラド州の従来AI法(CAIA/SB24-205)に対しxAIが2026年4月9日に提訴・DOJが4月24日に平等保護条項違反を主張して参加、4月27日に裁判所が施行を一時停止したこと、5月14日成立の後継法ADMT法(SB 26-189)自体も同訴訟の対象となり施行が事実上凍結中であることを更新。商務省による「負担の大きい州法」認定(2026年3月11日期限、BEAD予算との連動)、下院の州法3年間凍結法案「Great American Artificial Intelligence Act」草案(2026年6月4日公表、未提出)を新規追加。日本はAI事業者ガイドライン第1.2版・知財プリンシプル・コードともに2026年8月時点で変更なし(引き続き最新版・未確定)であることを確認
- **出典**: [FASI: The Digital Omnibus AI Regulation Published in the EU Official Journal](https://fasi.eu/en/articles/strategies/29051-digital-omnibus-package.html)、[Hunton: EU Digital Omnibus on AI Enters Into Force](https://www.hunton.com/privacy-and-cybersecurity-law-blog/eu-digital-omnibus-on-ai-enters-into-force)、[European Commission: Commission starts enforcing AI Act rules and new transparency requirements on 2 August](https://digital-strategy.ec.europa.eu/en/news/commission-starts-enforcing-ai-act-rules-and-new-transparency-requirements-2-august)、[Cooley: EU AI Act - Transparency Obligations Take Effect 2 August 2026](https://www.cooley.com/news/insight/2026/2026-08-03-eu-ai-act-transparency-obligations-take-effect-2-august-2026)、[Bird & Bird: Taking the EU AI Act to Practice - The Final Transparency Code of Practice](https://www.twobirds.com/en/insights/2026/taking-the-eu-ai-act-to-practice-the-final-transparency-code-of-practice)、[European Commission: Strong backing for the Code of Practice on Transparency of AI-generated Content](https://digital-strategy.ec.europa.eu/en/news/strong-backing-code-practice-transparency-ai-generated-content)、[TECHi: EU AI Act GPAI Enforcement Begins August 2](https://www.techi.com/eu-ai-act-gpai-enforcement-august-2026/)、[Jenner & Block: DOJ Joins xAI in Lawsuit Challenging Colorado AI Act](https://www.jenner.com/en/news-insights/client-alerts/doj-joins-xai-in-lawsuit-challenging-colorado-ai-act)、[Norton Rose Fulbright: X.AI sues, DOJ intervenes, enforcement of Colorado's AI Act suspended](https://www.nortonrosefulbright.com/en-us/knowledge/publications/de3ad9de/xai-sues-doj-intervenes-enforcement-of-colorado-ai-act-suspended)、[Law and the Workplace: Major Developments Put Colorado's AI Law on Ice Ahead of Implementation](https://www.lawandtheworkplace.com/2026/05/major-developments-put-colorados-ai-law-on-ice-ahead-of-implementation/)、[Baker Botts: xAI Sues to Enjoin Colorado's AI Act Before June 30 Effective Date](https://ourtake.bakerbotts.com/post/102mpre/xai-sues-to-enjoin-colorados-ai-act-before-june-30-effective-date)、[Mondaq: Department Of Commerce Report On State Artificial Intelligence Laws Expected By March 11, 2026](https://www.mondaq.com/unitedstates/new-technology/1757200/department-of-commerce-report-on-state-artificial-intelligence-laws-expected-by-march-11-2026)、[TechPolicy.Press: Unpacking the Great American Artificial Intelligence Act of 2026](https://www.techpolicy.press/unpacking-the-great-american-artificial-intelligence-act-of-2026/)、[Roll Call: Bipartisan AI draft proposes three-year preemption of state laws](https://rollcall.com/2026/06/04/bipartisan-ai-draft-proposes-three-year-preemption-of-state-laws/)、[経済産業省: AI事業者ガイドライン(第1.2版)](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf)

### 2026-07-23: 2026年7月時点の最新動向に全面更新
- **内容**: EU AI Actの「デジタル・オムニバス」が2026年6月に欧州議会・理事会で最終合意・7月8日成立し、高リスク義務がAnnex III(2027年12月2日)・Annex I(2028年8月2日)まで延期される一方、透明性義務(第50条)とGPAI執行権限は2026年8月2日のまま変更なしであること、AI Officeの権限強化(履行強制金、規制サンドボックス、small mid-cap向け簡素化)を追記。日本はAI事業者ガイドライン第1.2版(2026年3月31日)が引き続き最新版であること、AI戦略本部の活動状況、内閣府の知財プリンシプル・コード(パブコメ実施中)を追加。米国はカリフォルニアSB53・テキサスTRAIGAが2026年1月に施行済みであること、コロラド州のCAIAが施行前に廃止され「Automated Decision-Making Technology Act」に置き換わり施行が2027年1月に再延期されたこと、連邦のDOJ AI Litigation Task Forceによる州法への訴訟方針を更新。中国の生成AI届出制度・新規則(擬人化対話サービス、2026年7月15日施行)を新規追加
- **出典**: [Gibson Dunn: EU AI Act Omnibus Agreement — Postponed High-Risk Deadlines and Other Key Changes](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/)、[Mondaq: Yes, August 2 Still Matters - The EU Approved A High-Risk AI Delay, But Most Transparency Obligations Remain](https://www.mondaq.com/unitedstates/new-technology/1818850/yes-august-2-still-matters-the-eu-approved-a-high-risk-ai-delay-but-most-transparency-obligations-remain)、[Digital Watch Observatory: Digital Omnibus on AI - The EU's AI Act simplification and new AI Office powers](https://dig.watch/updates/digital-omnibus-eu-ai-act-new-ai-office-powers)、[beam.ai: EU AI Act 2026 - GPAI Enforcement & 3% Fines Begin](https://beam.ai/agentic-insights/eu-ai-act-enforcement-august-2-2026-gpai-fines)、[TIMEWELL: EU AI Act 2026年8月「完全施行」の裏側 Digital Omnibusで何が延期され、何が前倒しになったか](https://timewell.jp/en/columns/eu-ai-act-digital-omnibus-2026)、[経済産業省: AI事業者ガイドライン(第1.2版)](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf)、[8and: AI事業者ガイドラインv1.2公表](https://8and.jp/2026/05/26/ai%E4%BA%8B%E6%A5%AD%E8%80%85%E3%82%AC%E3%82%A4%E3%83%89%E3%83%A9%E3%82%A4%E3%83%B3-v1-2%E5%85%AC%E8%A1%A8-%E7%B5%8C%E7%94%A3%E7%9C%81%EF%BC%8B%E7%B7%8F%E5%8B%99%E7%9C%81%E3%80%81/)、[内閣府: AI戦略 科学技術・イノベーション](https://www8.cao.go.jp/cstp/ai/index.html)、[国立国会図書館カレントアウェアネス: 内閣府、生成AIの知的財産保護・透明性プリンシプル・コード(仮称)案に関する意見募集](https://current.ndl.go.jp/car/268921)、[Skadden: Colorado Repeals and Replaces Its AI Act](https://www.skadden.com/insights/publications/2026/06/colorado-repeals-and-replaces-its-ai-act)、[Norton Rose Fulbright: Colorado enacts revised AI law](https://www.nortonrosefulbright.com/en-us/knowledge/publications/18733d31/colorado-enacts-revised-ai-law)、[DWT: Colorado AI Act Repealed and Replaced by Narrower Statute](https://www.dwt.com/blogs/privacy--security-law-blog/2026/05/colorado-ai-act-repeal-new-transparency-law)、[Norton Rose Fulbright: The Texas Responsible AI Governance Act](https://www.nortonrosefulbright.com/en/knowledge/publications/c6c60e0c/the-texas-responsible-ai-governance-act)、[Morrison Foerster: California Enacts AI Safety and Transparency Regulation TFAIA (SB 53)](https://www.mofo.com/resources/insights/251001-california-enacts-ai-safety-transparency-regulation-tfaia-sb-53)、[Sidley: Unpacking the December 11, 2025 Executive Order](https://datamatters.sidley.com/2025/12/23/unpacking-the-december-11-2025-executive-order-ensuring-a-national-policy-framework-for-artificial-intelligence/)、[The White House: Ensuring a National Policy Framework for Artificial Intelligence](https://www.whitehouse.gov/presidential-actions/2025/12/eliminating-state-law-obstruction-of-national-artificial-intelligence-policy/)、[JETRO: パッチワーク化が進む米国のAI規制](https://www.jetro.go.jp/biz/areareports/special/2026/0102/859d70e177ed4dc4.html)、[中央网络安全和信息化委员会办公室: 人工智能拟人化互动服务管理暂行办法](https://www.cac.gov.cn/2026-04/10/c_1777558395078289.htm)、[中央网络安全和信息化委员会办公室: 生成式人工智能服务已备案信息公告(2026年5月至6月)](https://www.sohu.com/a/1049798075_121106869)

### 2026-07-06: 初版執筆
- **内容**: EU AI Act(リスク4段階の枠組み、提供者/導入事業者の義務区分、2026年8月の透明性義務適用と高リスク義務のデジタル・オムニバスによる延期)、日本のAI推進法・AI事業者ガイドライン第1.2版(ソフトロー中心、Human-in-the-Loop要件)、米国の州法パッチワーク(コロラド州法の縮小・再延期、カリフォルニア州SB53)を整理し、日本企業向けの地域別対応比較表と社内チェックリストをまとめた
- **出典**: [EU Artificial Intelligence Act: Implementation Timeline](https://artificialintelligenceact.eu/implementation-timeline/)、[DLA Piper GENIE: The Digital AI Omnibus - Proposed deferral of high risk AI obligations](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act)、[EU Artificial Intelligence Act: Article 50 Transparency Rules](https://artificialintelligenceact.eu/transparency-rules-article-50/)、[EU Artificial Intelligence Act: Article 26 Deployer Obligations](https://artificialintelligenceact.eu/article/26/)、[EU Artificial Intelligence Act: Article 99 Penalties](https://artificialintelligenceact.eu/article/99/)、[Bratby Law: AI Act transparency obligations from 2 August](https://bratby.law/ai-act-transparency-obligations-2026/)、[経済産業省: AI事業者ガイドライン(第1.2版)](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/20260331_report.html)、[PwC Japan: 「AI事業者ガイドライン(第1.2版)」改定のポイント](https://www.pwc.com/jp/ja/knowledge/column/ai-governance/ai-guideline-03.html)、[内閣府: 人工知能関連技術の研究開発及び活用の推進に関する法律(AI法)](https://www8.cao.go.jp/cstp/ai/ai_act/ai_act.html)、[e-Gov法令検索: 人工知能関連技術の研究開発及び活用の推進に関する法律](https://laws.e-gov.go.jp/law/507AC0000000053)、[Hunton Andrews Kurth: Colorado AI Act Amended and Effective Date Delayed](https://www.hunton.com/privacy-and-cybersecurity-law-blog/colorado-ai-act-amended-and-effective-date-delayed)、[Littler: Colorado Amends its Artificial Intelligence Law](https://www.littler.com/news-analysis/asap/colorado-amends-its-artificial-intelligence-law-substantially-reducing)、[スマートガバナンス: 米トランプ政権、AI規制の「連邦統一基準」に向けた大統領令](https://smart-governance.co.jp/resource/Insights-trump-us-ai-policy-federal-standard-20260116)、[JETRO: パッチワーク化が進む米国のAI規制](https://www.jetro.go.jp/biz/areareports/special/2026/0102/859d70e177ed4dc4.html)
