---
title: NPO・非営利団体における生成AI活用事例
part: 14
chapter: "第12章 その他・未分類"
tags: [NPO, 非営利団体, 生成AI活用事例, 助成金申請, ファンドレイジング, Google for Nonprofits, Claude for Nonprofits, OpenAI for Nonprofits, やさしい日本語, NotebookLM]
created: 2026-07-18
updated: 2026-11-21
---

# NPO・非営利団体における生成AI活用事例

## これは何か

NPO(Non-Profit Organization、非営利団体)は、少人数のスタッフで助成金申請書・寄付募集チラシ・年次報告書・問い合わせ対応まで幅広い文書業務をこなす一方、専任の広報・IT担当者を置けない団体が多く、生成AIによる業務効率化の恩恵を最も受けやすい組織形態の一つである。2025年末から2026年にかけて、Anthropic(Claude)・OpenAI(ChatGPT)・Google・Microsoftの主要ベンダーが非営利団体向けの割引・無償プログラムを拡充し、営利企業よりも大幅に低いコストで生成AIを導入できる環境がほぼ出揃った。本ページは、助成金申請書作成・ファンドレイジング(寄付募集)・多言語相談対応・議事録や事務処理、そして2026年に顕在化した災害支援の場面まで、NPO特有の業務における生成AIの使いどころと、実名団体の導入事例を整理する。

## 仕組み・背景

NPOにおける生成AI活用は、大きく5つの領域に分かれる。

1. **助成金申請書の作成**: 助成金申請は、フォーマットが決まっており、過去の採択事例が公開されており、評価軸が明文化されていることが多いため、NPO業務の中でも生成AIとの相性が特に良い領域とされる([AI PICKS](https://aipicks.jp/mag/npo-ai-guide-2026))。TechSoupとTapp Networkが1,300名超のNPO専門職の回答をもとにまとめた「State of AI in Nonprofits: 2025」では、85.6%がAIツールを試している一方で正式な活用戦略を持つ団体は24%にとどまり、助成金申請書の作成にAIを使っている団体は24.6%だった。また年間予算100万ドル超の団体は予算規模の小さい団体の約2倍のペースでAIを導入しており(66% vs 34%)、資金力による「AI格差」が広がっている点にも注意が必要である([NonprofitPro](https://www.nonprofitpro.com/article/2025-ai-benchmark-report-how-artificial-intelligence-is-changing-the-nonprofit-sector/))。国内では、日本NPOセンターが2025年2〜3月に実施した調査(回答320団体)で、生成AIを「試しで利用している」団体が42.8%と最も多く、「業務に本格的に取り入れている」は7.5%にとどまった。課題・懸念の上位は「データの正確性」(65.6%)、「技術的な理解」(52.8%)、「ノウハウの不足」(52.5%)である([日本NPOセンター](https://www.jnpoc.ne.jp/wp-content/uploads/2025/08/IT-report_2025.pdf))。
2. **ファンドレイジング(寄付募集)・広報**: 寄付呼びかけチラシ・SNS投稿・年次報告書のデザインを内製化する動きが広がっている。Canvaは登録非営利団体向けに「Canva for Nonprofits」を無償提供しており、デザインテンプレートと生成AI機能を組み合わせて広報物を作成できる([AI PICKS](https://aipicks.jp/mag/npo-guide-2026))。
3. **多言語相談対応・やさしい日本語**: 外国人支援・国際協力・難民支援系のNPOでは、相談者の文化的背景に配慮した訳し方や、日本の制度に不案内な相談者向けの噛み砕いた説明まで、Claude・ChatGPTなどを使ったAI翻訳・下訳の活用が広がっている。教育系NPOでは、文章を生成AIで「やさしい日本語」(外国の人にも分かるように配慮した日本語)に変換するツールを自ら開発し、学校に無償提供する例も出てきた(下記「導入事例カタログ」のeboard)。
4. **議事録・事務処理の自動化**: 理事会・総会の議事録作成、ボランティアの問い合わせ対応、日程調整、連絡先リストの更新など、定型的な事務作業をAIで効率化する動きも出てきている([DevelopersIO](https://dev.classmethod.jp/articles/nonprofit-ai-lab-02-generative-ai-use-cases-for-nonprofits/))。定款・所轄庁のガイドブックをNotebookLMに読み込ませ、その月にやるべき法定の事務手続を洗い出させるといった、NPO法人特有の使い方も中間支援団体から紹介されている(下記カタログのセイエン)。
5. **災害支援における活用(2026年に顕在化)**: 2026年7月28日、熊本県熊本地方を震源とするマグニチュード7.1(暫定値)・最大震度7の地震(令和8年熊本地震)が発生した([気象庁](https://www.jma.go.jp/jma/menu/20260728_kumamoto_jishin.html))。御船町の避難所に身を寄せていた住民が、スマートフォンで生成AIを使い、思い立ってから数時間で生活情報掲示板「イマココナビ」を開発・公開し、営業再開した店舗や炊き出し場所などの情報共有に16万人超が利用した([時事通信/リスク対策.com](https://www.risktaisaku.com/articles/-/114226))。これとは別に、NPO担当者・自治体職員・教職員なども申請できる形で、災害復興アプリ向けの生成AIインフラ(API)を2026年10月31日まで追加課金なしで提供する民間の取り組みもあり、災害支援NPOが自前でAI活用の仕組みを立ち上げるハードルが下がりつつある([AICU](https://corp.aicu.ai/ja/kumamoto260728))。一方で同じ被災地では、生成AIで作られたとみられる偽の被災映像もSNSで出回り、功罪の両面が指摘されている点は要注意である([時事通信/リスク対策.com](https://www.risktaisaku.com/articles/-/114226))。

2026年11月時点で、主要ベンダーの非営利団体向けプログラムは次のとおり。

- **Anthropic「Claude for Nonprofits」**: 2025年12月2日(Giving Tuesday)に発表。適格な非営利団体はTeam・Enterpriseプランを最大75%割引で利用できる。寄付者管理・ファンドレイジングのBlackbaud、企業寄付プラットフォームのBenevity(240万超の認証済み非営利団体のデータ)、非営利団体・助成財団のデータを持つCandidとのコネクタ(MCP=Model Context Protocol、AIと外部ツールをつなぐ共通規格)も同時に公開され、GivingTuesdayと共同開発した無償講座「AI Fluency for Nonprofits」も提供されている([Anthropic](https://www.anthropic.com/news/claude-for-nonprofits))。2026年10月には、Teamプランを2人の団体から使えるようにし、Claude Codeを追加料金なしで含め、低・中所得国の認証済み非営利団体向けには約90%割引(標準Teamシートで1ユーザーあたり月3ドル)を設けるなど対象を広げた([Claude公式ブログ](https://claude.com/blog/expanding-claude-for-nonprofits))。また2026年6月には、初期資金1.5億ドルで若手人材を12か月間非営利団体に派遣し、Claudeの活用を支援するフェローシップ「Claude Corps」も発表している([Anthropic](https://www.anthropic.com/news/claude-corps))。
- **OpenAI「OpenAI for Nonprofits」**: 2024年5月30日に開始(当初はChatGPT Team〔現Business〕20%割引)。2026年2月6日の更新で、ChatGPT Business・Enterpriseを最大75%割引で利用できるよう拡充された([OpenAI](https://openai.com/index/introducing-openai-for-nonprofits/))。2026年11月時点のヘルプでは、Businessの標準シートが年払いで1ユーザーあたり月8ドル、月払いで月10ドル(Premiumシートは割引対象外)、Enterpriseは営業窓口経由で最大75%割引。資格審査は提携先Goodstackが行う([OpenAI ヘルプ](https://help.openai.com/en/articles/9359041-openai-for-nonprofits))。
- **Google for Nonprofits**: Google Workspace for Nonprofitsの対象団体は、最新のGeminiアプリとコンプライアンス機能を無料で利用でき、上位のGoogle Workspaceエディションへのアップグレードも標準価格から最大75%割引になる。非営利団体向けのプロンプト集やファンドレイジング・マーケティングの動画教材も用意されている([Google 非営利団体ヘルプ](https://support.google.com/nonprofits/answer/15873832?hl=ja))。
- **Microsoft for Nonprofits**: Microsoft 365 Copilotを適格な非営利団体向けに年払いで1ユーザーあたり月25.50ドル(15%割引)で提供している(別途、対象となるMicrosoft 365ライセンスが必要)。従業員300人未満の団体向けの特典として、年間2,000ドル分のAzureクレジットも用意されている([Microsoft Nonprofit Offers Guide](https://www.microsoft.com/content/dam/microsoft/msc/documents/presentations/nonprofits/pdfs/Microsoft-Nonprofit-Offers-Guide.pdf))。

こうした割引・無償プログラムの整備により、月数千円、あるいは無償に近い規模で生成AIを導入できる環境が広がっている一方、資金力のある団体ほど活用が先行する「AI格差」も同時に進行している([AI PICKS](https://aipicks.jp/mag/npo-guide-2026))。

## 使いどころ・使い分け

| 業務 | 生成AIが向く | 向かない/慎重にすべき理由 |
|---|---|---|
| 助成金申請書のドラフト作成 | 向く(過去の採択事例・フォーマットを参考にした下書き) | 団体固有の実績・数値・独自性は人が加筆し、事実確認を行う |
| 自団体に合う助成金の探索 | 向く(助成金情報と定款・事業報告書を突き合わせた候補出し) | 締切・応募要件は必ず募集要項の原文で確認する |
| 寄付募集チラシ・SNS投稿文の作成 | 向く(Canva等のデザインツールとの組み合わせ) | 団体のブランドトーン・受益者への配慮は人が最終確認する |
| 多言語相談対応の一次対応・翻訳・やさしい日本語化 | 向く(定型的な問い合わせ・翻訳の下訳・文章の平易化) | 深刻な相談内容・専門的な法的助言は人の専門職が対応する |
| 議事録作成・法定事務のリマインド | 向く(定型業務の自動化・抜け漏れチェック) | 意思決定に関わる機微な議論内容や法定手続の要否は人が確認する(AIの洗い出しには漏れが出る) |
| 災害時の生活情報の集約・発信 | 向く(炊き出し場所・支援物資情報などの即時共有) | 未検証の情報や生成AIによる偽の被災映像の拡散リスクがあり、一次情報の裏取りを徹底する |
| 受益者(支援対象者)の個人情報を扱う相談記録 | 慎重に扱う | 機微な個人情報の学習利用リスクがあるため、法人契約の範囲・データ保護方針を確認してから使う |

## 実務での使い方

### プロンプト例1: 助成金申請書のドラフト作成

```
以下の助成金の募集要項と、当団体の活動概要をもとに、申請書の「事業の目的・必要性」セクションの
下書きを作成してください。
- 募集要項に記載された評価基準に沿った構成にする
- 数値データ(受益者数・実施回数等)は[  ]の形でプレースホルダーにし、後で差し替えられるようにする

## 募集要項の抜粋
[助成金の目的・評価基準を貼り付け]

## 当団体の活動概要
[団体の活動内容・実績を記載]
```

出力はあくまで下書きであり、団体固有の実績・数値は必ず事実確認の上で加筆する。

### プロンプト例2: 寄付募集のSNS投稿文作成

```
以下の活動報告をもとに、寄付を呼びかけるSNS投稿文を3パターン作成してください。
- 1つは「支援した人の声」を中心にした共感重視のトーン
- 1つは「具体的な成果数値」を中心にした説得重視のトーン
- 1つは「緊急性」を伝えるトーン
各150字程度で、最後に寄付ページへの誘導文を添えてください。

[活動報告の内容を記載]
```

受益者のプライバシーに配慮し、実名や特定可能な情報を含める場合は必ず本人・保護者の同意を確認する。

### プロンプト例3: 理事会議事録の要約作成

```
以下は理事会の音声文字起こしです。この内容を議事録の形式で要約してください。
- 決定事項、保留事項、次回までのアクションアイテムを分けて整理する
- 発言者名は明記せず、議論の内容を中心にまとめる

[文字起こしテキストを貼り付け]
```

要約後、決定事項の正確性を必ず出席者が確認してから正式な議事録として保管する。

### プロンプト例4: 今月の法定事務手続の洗い出し(NotebookLM等に定款を読み込ませて使う)

```
あなたはNPO法人の事務に詳しいベテラン担当者です。
ソースとして読み込んだ「定款」「所轄庁の手引き」「年間運営スケジュール表」をもとに、
当法人が[◯月]中に行うべき手続を一覧にしてください。
- 手続名・期限・根拠(定款の条文や手引きの該当箇所)・担当者がやることを表にする
- 当法人の事業年度は[◯月〜◯月]、税務上の扱いは[収益事業の有無]、職員の雇用は[有無]
- 判断がつかない項目は「要確認」として残す
```

税務・雇用の状況をソースやプロンプトに含めると精度が上がる一方、本部事務所での書類備置のような項目が漏れた例も報告されている([NPOWEB/セイエン](https://www.npoweb.jp/2026/04/%E3%80%90%E9%9A%8F%E6%99%82%E6%9B%B4%E6%96%B0%E3%80%91%E7%94%9F%E6%88%90ai%E6%B4%BB%E7%94%A8%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7%E3%82%A2%E3%83%BC%E3%82%AB%E3%82%A4%E3%83%96/))。出力はチェックリストの叩き台として使い、所轄庁の手引きで最終確認する。

### ツール横断の対応表

| 用途 | ツール例 |
|---|---|
| 助成金申請書・文書作成全般 | Microsoft 365 Copilot(Microsoft for Nonprofits経由)、Claude Team(Claude for Nonprofits経由)、ChatGPT Business/Enterprise(OpenAI for Nonprofits経由)、Gemini(Google for Nonprofits経由) |
| 定款・手引きなど自団体資料に基づく調べもの | NotebookLM、Claudeのプロジェクト、ChatGPTのプロジェクト |
| 寄付募集チラシ・SNS投稿デザイン | Canva for Nonprofits |
| 助成金・寄付者データの参照 | Claude for Nonprofits(Candid・Blackbaud・Benevityのコネクタ) |
| 非営利団体向け割引・無償プログラム | Google for Nonprofits、Microsoft for Nonprofits、Claude for Nonprofits、OpenAI for Nonprofits |

いずれの割引プログラムも、提携先(Goodstack等)による法人格・活動内容の審査を経て初めて適用される。まずは自団体がGoogle・Microsoft・Anthropic・OpenAIのいずれかの非営利団体向けプログラムの利用資格を満たすか確認し、割引・無償枠を活用してから、必要に応じて有料プランを検討するのが費用対効果の高い順序である。

## 導入事例カタログ

ここでは、**出典で生成AI(LLM)の利用が確認できる実名の非営利団体の事例**を、共通カード書式で集める(2026年11月時点)。国内では、効果まで公表している事例はまだ少なく、教育系NPOのツール開発と、中間支援団体の自団体での試行の2件を載せた。海外は、ベンダーの非営利団体向けプログラムの発表や導入事例として公表されたものを3件載せた。

### NPO法人eboard(教育系NPO・ICT教材eboardは1万2,000超の学校・教育現場で利用) — 対象業務: 外国につながる子ども等への「やさしい日本語」化支援
- **導入形態**: 内製
- **段階**: 部門展開(全国の学校での実証を経て、2027年3月末まで学校・教育委員会・教育関係団体に無償提供)
- **やったこと**: 生成AIを使い、貼り付けた文章を「やさしい日本語」に変換する変換ツール、音声を即時に翻訳して画面に表示するリアルタイム翻訳、言葉をやさしい日本語と画像で説明する辞典の3機能からなるツールを開発した(使用モデルは非公表)。カメラで撮影した文字の読み取りやふりがなの表示切り替えにも対応する。生成AIの利用費用は企業・財団の助成で賄ってきたが、助成期間が2026年3月31日で終了したため、2026年4月から1年間は自己資金で無償提供を続け、2027年4月以降に向けて寄付を募っている
- **効果**: 2024〜2025年度の全国の学校での実証で、「文章が読みやすくなり、自分で読めると感じた」と答えた児童生徒が、外国につながる子どもで約4人に3人、ディスレクシア(読み書きの困難)のある子どもで約5人に4人、軽度知的障害のある子どもで約4人に3人(2026年5月時点・自社公表。実証参加者の回答で、参加人数は非公表。本番展開後の数値ではない)
- **学べること**: 生成AIの利用料は継続費用になるため、助成で始めたツールは「助成終了後に誰が払うか」を最初から設計しておく必要がある
- **出典**: [PR TIMES(eboard)](https://prtimes.jp/main/html/rd/p/000000052.000070582.html)、[トヨタ財団 JOINT No.46](https://www.toyotafound.or.jp/activity/joint/contribution/joint46_contribution01.html) / 最終確認日: 2026-11-21

### NPO法人セイエン(NPO法の制度提言・情報提供を行う中間支援団体、旧シーズ・市民活動を支える制度をつくる会の事業を継承) — 対象業務: 助成金リサーチ・法定事務手続のリマインド
- **導入形態**: 汎用チャットAI活用
- **段階**: PoC(自団体での試行を会員向け配信で紹介)
- **やったこと**: NotebookLM(PROライセンス)に、自団体サイトNPOWEBの過去の助成金情報アーカイブ(配信時点で417件)と、定款・事業報告書・団体サイトを読み込ませ、「自団体に合った助成金をピックアップして」と指示して候補を出させた。別の回では、年間運営スケジュール表・所轄庁(東京都)の手引き・定款・団体情報を読み込ませ、ベテラン事務担当者の役割を与えて3月中に行うべき手続(総会の招集通知、事業報告書の3月31日までの提出、貸借対照表の公告など)を洗い出させた
- **効果**: 数値公表なし(2026年4月時点・自社公表)。助成金の候補出しは担当者が「なかなかの精度」と評価した一方、事務手続の洗い出しでは本部事務所での書類備置などの項目が漏れたとし、個人情報・著作権・ハルシネーションの課題も併記している
- **学べること**: 定款や所轄庁の手引きを読み込ませると「一般論でなく自団体向けの答え」になるが、漏れは出る前提でチェックリストの叩き台として使う
- **出典**: [NPOWEB(NPO法人セイエン)「生成AI活用記事一覧アーカイブ」](https://www.npoweb.jp/2026/04/%E3%80%90%E9%9A%8F%E6%99%82%E6%9B%B4%E6%96%B0%E3%80%91%E7%94%9F%E6%88%90ai%E6%B4%BB%E7%94%A8%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7%E3%82%A2%E3%83%BC%E3%82%AB%E3%82%A4%E3%83%96/) / 最終確認日: 2026-11-21

### International Rescue Committee(海外事例・米国拠点の国際人道支援NGO) — 対象業務: 避難民・被災者向けの情報提供、現場データ分析
- **導入形態**: 内製(AIエージェント構築基盤「Signpost AI」)+汎用チャットAI活用(Claude Enterprise)
- **段階**: PoC(Signpost AIのエージェントは8か国で試験運用)
- **やったこと**: 2015年から約30か国で避難民などに情報を届けてきた「Signpost」に、役割・安全手順・ガードレール(禁止事項の歯止め)・知識の範囲を個別に定めたAIエージェントを組み込み、初期の試験では回答を人が確認してから送る体制をとった。ナイジェリア北東部3州では教員向けの学習チャットボット「aprendIA」も運用している。Anthropicは計算資源・技術面の協力先の一つで、組織内ではClaude Enterpriseをデータ分析や現地パートナー支援の効率化に使っている
- **効果**: 初期の試験運用で、AIの回答が品質基準を満たしたのは約75%、スタッフの生産性は約70%向上。aprendIAの利用教員は約400人から4,700人に増加(いずれも2026年3月時点・自社公表。Signpost AIの数値は試験運用段階のもので、本番展開後の数値ではない)
- **学べること**: 相談・支援の現場では、「約4回に1回は品質基準に届かない」前提で、人の確認と引き継ぎを組み込んでから対象を広げる
- **出典**: [International Rescue Committee「From Promise to Practice」](https://www.rescue.org/irc-responsible-ai-humanitarian-sector)、[Anthropic「Claude for Nonprofits」](https://www.anthropic.com/news/claude-for-nonprofits) / 最終確認日: 2026-11-21

### Infoxchange(海外事例・アジア太平洋地域の非営利ソーシャルエンタープライズ。3万5,000超の地域団体・行政等と協働) — 対象業務: 非営利団体向けAI研修プログラムの設計
- **導入形態**: 汎用チャットAI活用(NotebookLM)
- **段階**: 部門展開(研修チームで採用)
- **やったこと**: 自団体のデータと背景調査の資料をNotebookLMに読み込ませ、「AI懐疑派」「AI試行派」「AI導入派」「AI推進派」の4つの受講者像ごとに資料を確認し、不足している情報から研修テーマを洗い出し、テーマごとの学習目標に展開した
- **効果**: 手作業では1週間以上かかっていた新規研修の調査・計画が、半日で研修モジュールの叩き台を作れるようになった(2025年6月時点・ベンダー公表〔Google Workspace公式ブログ〕)
- **学べること**: 研修や講座を作る団体は、「受講者像×手持ち資料」をAIに読ませて不足テーマを洗い出すと、設計の初動を大きく縮められる
- **出典**: [Google Workspace Blog「Infoxchange crafts educational resources in hours instead of days with NotebookLM」](https://workspace.google.com/blog/customer-stories/infoxchange-crafts-educational-resources-hours-instead-days-notebooklm) / 最終確認日: 2026-11-21

### Epilepsy Foundation(海外事例・米国のてんかん患者支援団体) — 対象業務: 患者・家族への24時間の情報提供
- **導入形態**: 内製(AWSとClaudeで構築)
- **段階**: 全社展開(一般向けサービスとして提供)
- **やったこと**: 2万5,000ページ超のてんかんに関する専門知識を学習・参照させたAIコンパニオン「Sage」をAWSとClaudeで構築し、米国の約340万人のてんかん患者に向けて5言語・24時間の支援を提供している
- **効果**: 数値公表なし(2025年12月時点・ベンダー公表〔Anthropic発表内の団体コメント〕。340万人は対象となる患者数で、利用者数ではない)
- **学べること**: 専門団体が持つ大量の解説資料は、それ自体が「いつでも答えられる相談窓口」の材料になる
- **出典**: [Anthropic「Claude for Nonprofits」](https://www.anthropic.com/news/claude-for-nonprofits) / 最終確認日: 2026-11-21

### 事例から見える傾向(2026年11月時点)

- **国内で効果まで公表されたNPOの生成AI事例はまだ少ない**。日本NPOセンターの調査でも「本格導入」は7.5%にとどまり、今回の調査で確認できた国内の実名事例は、ツールを開発して外部に提供する教育系NPOと、中間支援団体による自団体での試行が中心だった。社会福祉協議会や福祉系団体では研修や利用状況の調査は進んでいるが、実名・効果つきの公表事例は確認できなかった
- **「自団体の資料を読み込ませる」使い方が共通している**。セイエンの定款・手引き、Infoxchangeの調査資料、Epilepsy Foundationの専門知識のように、汎用的な回答ではなく自団体の文書を根拠に答えさせる形(RAG=検索拡張生成やNotebookLM)が多い
- **継続費用と人の確認が導入の前提になる**。eboardは助成終了後の費用負担を課題として明示し、IRCは品質基準を満たす回答が約75%という試験結果を公表したうえで人の確認を組み込んでいる。割引プログラムで入口のコストは下がったが、運用費と確認体制の設計は団体側に残る

## 注意点・よくある誤解

- **受益者の個人情報・相談内容を安易に入力しない**: 支援対象者の氏名・相談内容など機微な個人情報を汎用チャットAIに入力すると、意図せずデータが学習・保存されるリスクがある。法人契約でオプトアウトされているか、非営利団体向けプランのデータ保護方針を確認する([生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md))。
- **助成金申請書の「独自性」は必ず人が書く**: AIが作った下書きをそのまま提出すると、他団体と似通った表現になりがちで、審査員に「オリジナリティがない」と判断されるリスクがある。団体固有のエピソード・実績は必ず人が加筆し、助成元がAI利用について定めた要項があればそれに従う。
- **非営利団体向け割引プログラムは審査・登録が必要**: 各社のプログラムは提携先(Goodstack等)による法人格の種類や活動内容の審査があり、即日利用できるとは限らない。導入を検討する際は早めに申請する。
- **「AI格差」に注意する**: 予算規模の大きい団体ほどAI導入が先行し、小規模団体との差が広がっている。国内でも生成AIは「お試し」段階の団体が多く、「データの正確性」「ノウハウの不足」が上位の懸念に挙がっている。まずは簡易な利用ルール(入力禁止情報の線引きや、出力を誰が確認するか)を定めることが導入の第一歩になる。
- **災害時の生成AI活用は「功罪」両面を理解する**: 被災地での生活情報の即時共有には効果がある一方、生成AIによる偽の被災映像・デマの拡散リスクも同時に指摘されている。NPOが情報発信に使う場合は、一次情報の出典を明示し、未確認情報の拡散を避ける運用ルールを決めておく。
- **AIによる翻訳・多言語対応は専門的な内容に限界がある**: 定型的な問い合わせ対応には有効だが、法的助言や深刻な相談内容の翻訳は誤訳のリスクを考慮し、専門通訳者・専門職員の確認を挟む。
- **助成で始めたAIツールは継続費用を見込む**: 生成AIのAPI利用料は使われるほど増える継続費用である。助成金で開発・試行したツールは、助成終了後の費用負担(自己資金・寄付・有料化)を計画段階で決めておく。

## 最初の一歩

Google for Nonprofits・Microsoft for Nonprofits・Claude for Nonprofits・OpenAI for Nonprofitsのいずれかについて、自団体が非営利法人としての利用資格を満たすか確認し、直近の助成金申請書またはSNS投稿文の下書き作成にチャットAIを試してみる。

## 関連トピック

- [公共・自治体における生成AI活用事例](public-sector-ai-use-cases.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)
- [生成AIによる文章作成・編集の実務活用](../part12-business-practice/ai-writing-and-editing.md)

## 更新履歴

### 2026-11-21: 導入事例カタログを新設(eboard・セイエン・International Rescue Committee・Infoxchange・Epilepsy Foundation)
- **内容**: 「導入事例カタログ」節を新設し、国内2件(NPO法人eboardの「やさしい日本語」化ツール、NPO法人セイエンのNotebookLM試行)と海外3件(IRCのSignpost AI、InfoxchangeのNotebookLM、Epilepsy Foundationの「Sage」)をカード書式で追加し、「事例から見える傾向」を記載。本文では、出典で確認できなかった記述(匿名の地域NPOの採択率・時間削減の事例、AI利用ポリシー未整備76%、Claude Teamの価格・最低シート数・対象モデル・Cowork同梱、OpenAI Enterpriseの割引後価格と資格要件、Google AI Opportunity Fundの金額・個別コーチング、海外助成財団のAI生成開示の動き)を削除または修正。OpenAI for Nonprofitsの開始時期(2024年5月、2026年2月に拡充)とNotebookLMの表記を訂正し、Claude for Nonprofitsの2026年10月の拡充とClaude Corps(2026年6月発表)、日本NPOセンターの2025年調査を追記。リンク切れの出典(Yahoo!ニュース)を差し替え
- **出典**: [PR TIMES(eboard): AIを活用した「やさしい日本語」化ツールを2027年3月末まで無償提供](https://prtimes.jp/main/html/rd/p/000000052.000070582.html)、[トヨタ財団 JOINT No.46: 生成AIを活用した教育現場での「やさしい日本語」の活用実証](https://www.toyotafound.or.jp/activity/joint/contribution/joint46_contribution01.html)、[NPOWEB(NPO法人セイエン): 生成AI活用記事一覧アーカイブ](https://www.npoweb.jp/2026/04/%E3%80%90%E9%9A%8F%E6%99%82%E6%9B%B4%E6%96%B0%E3%80%91%E7%94%9F%E6%88%90ai%E6%B4%BB%E7%94%A8%E8%A8%98%E4%BA%8B%E4%B8%80%E8%A6%A7%E3%82%A2%E3%83%BC%E3%82%AB%E3%82%A4%E3%83%96/)、[International Rescue Committee: From Promise to Practice](https://www.rescue.org/irc-responsible-ai-humanitarian-sector)、[Google Workspace Blog: Infoxchange crafts educational resources in hours instead of days with NotebookLM](https://workspace.google.com/blog/customer-stories/infoxchange-crafts-educational-resources-hours-instead-days-notebooklm)、[Anthropic: Claude for Nonprofits](https://www.anthropic.com/news/claude-for-nonprofits)、[Claude公式ブログ: Expanding Claude for Nonprofits](https://claude.com/blog/expanding-claude-for-nonprofits)、[Anthropic: Introducing Claude Corps](https://www.anthropic.com/news/claude-corps)、[OpenAI: Introducing OpenAI for Nonprofits](https://openai.com/index/introducing-openai-for-nonprofits/)、[OpenAI ヘルプ: OpenAI for Nonprofits](https://help.openai.com/en/articles/9359041-openai-for-nonprofits)、[Google 非営利団体ヘルプ](https://support.google.com/nonprofits/answer/15873832?hl=ja)、[Microsoft Nonprofit Offers Guide](https://www.microsoft.com/content/dam/microsoft/msc/documents/presentations/nonprofits/pdfs/Microsoft-Nonprofit-Offers-Guide.pdf)、[日本NPOセンター: 非営利団体のIT活用のための実態調査2025年報告書](https://www.jnpoc.ne.jp/wp-content/uploads/2025/08/IT-report_2025.pdf)、[気象庁: 令和8年熊本地震](https://www.jma.go.jp/jma/menu/20260728_kumamoto_jishin.html)

### 2026-08-15: 非営利団体向け割引プログラムの最新化と災害支援事例を追加
- **内容**: Anthropic「Claude for Nonprofits」(2025年12月発表、最大75%割引・Benevity/Blackbaud/CandidとのMCP連携・Claude Corps)、OpenAI「OpenAI for Nonprofits」(2026年2月発表)、Google/Microsoftの最新プログラム内容を具体化。TechSoup/Tapp Networkの調査データ(AI活用戦略の有無・団体規模によるAI格差)、地域NPOの助成金申請での時間削減事例を追加。2026年7月の令和8年熊本地震における個人開発の生活情報掲示板「イマココナビ」とNPO向け災害支援AIインフラの無償提供事例を新設し、災害時の生成AI活用の功罪(偽映像リスク)にも言及
- **出典**: [NBC News: Anthropic offers nonprofits discounts for Giving Tuesday](https://www.nbcnews.com/tech/tech-news/giving-tuesday-ai-anthropic-offers-nonprofits-discounts-rcna246770)、[Forbes: How Anthropic And Claude For Nonprofits Are Putting AI In The Hands Of Changemakers](https://www.forbes.com/sites/afdhelaziz/2025/12/02/how-anthropic-and-claude-for-nonprofits-is-putting-ai-in-the-hands-of-changemakers/)、[NonprofitPro: 2025 AI Benchmark Report](https://www.nonprofitpro.com/article/2025-ai-benchmark-report-how-artificial-intelligence-is-changing-the-nonprofit-sector/)、[Mixflow: Generative AI in 2026 - Grant Writing and Donor Engagement](https://mixflow.ai/blog/generative-ai-in-2026-revolutionizing-grant-writing-and-donor-engagement-for-non-profits/)、[Yahoo!ニュース/時事通信: 生成AI、被災地照らす 避難者自ら情報掲示板開発](https://news.yahoo.co.jp/articles/0bd9405236b3b9483a0cfa7b522e0981dbefa868)、[AICU: 令和8年熊本地震 災害支援のAIインフラを無償提供](https://corp.aicu.ai/ja/kumamoto260728)、[リスク対策.com: 生成AI、被災地照らす=避難者自ら情報掲示板開発-偽映像も、浮かぶ功罪・熊本](https://www.risktaisaku.com/articles/-/114226)

### 2026-07-18: 初版執筆
- **内容**: NPO・非営利団体における生成AI活用として、助成金申請書作成(TechSoup×Microsoft 365 Copilotの事例)、ファンドレイジング・広報、多言語相談対応、議事録・事務処理の4領域を整理。Google/Microsoft/Claude/OpenAIの非営利団体向け割引プログラムと、受益者の個人情報取り扱いにおける注意点を明示
- **出典**: [AI PICKS: NPO AIで何ができる?社団法人の実務7用途と注意点](https://aipicks.jp/mag/npo-ai-guide-2026)、[TechSoup: Case Study - Nonprofits Leveraging Microsoft 365 Copilot for Impact](https://blog.techsoup.org/en-us/posts/case-study-nonprofits-leveraging-microsoft-365-copilot-for-impact)、[AI PICKS: NPO向けAIツール7選](https://aipicks.jp/mag/npo-guide-2026)、[DevelopersIO: 非営利組織のためのAI活用ラボ第2回](https://dev.classmethod.jp/articles/nonprofit-ai-lab-02-generative-ai-use-cases-for-nonprofits/)
