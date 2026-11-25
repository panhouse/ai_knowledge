# 執筆候補の台帳(BACKLOG)

毎朝のルーティンが**スキャン**で見つけた「書くべきネタ」を積む場所。
ルーティンはこの台帳の上位から、その日に扱うトピックを選ぶ。

台帳があることで、同じネタの重複執筆を防ぎ、「なぜそのトピックを書いたのか」を
後から追えるようにする。

## 書式

| 候補 | 想定Part/章 | 種別 | 根拠URL | 発見日 | 優先度 | 状態 |
|---|---|---|---|---|---|---|

- **候補**: 書こうとしているページのタイトル案(既存ページの更新なら既存のタイトル)
- **想定Part/章**: `14/第1章` のようにパート番号と章を書く。迷ったら `?` でよい
- **種別**: `新規` / `更新` / `事例追加` のいずれか
- **根拠URL**: その候補を見つけた一次情報。複数あれば `/` で区切って並べる
- **発見日**: スキャンで見つけた日(`YYYY-MM-DD`)
- **優先度**:
  - **A** — 研修で聞かれる頻度が高い、または制度変更・提供終了など期限がある
  - **B** — 通常
  - **C** — 様子見(単発の発表で、まだ記事の材料として弱い)
- **状態**: `未着手` → `着手済` → `完了`(日付を添える) / `見送り`(理由を1行で併記)

完了した行と見送った行は**削除せず残す**。重複執筆の検知と、判断履歴の記録を兼ねる。

## 曜日別のスキャン対象

1日あたり検索5〜8本程度に収める。全部を毎日見ないこと。

| 曜日 | スキャン対象 | 主に効くPart |
|---|---|---|
| 月 | 主要ベンダーの公式リリース(OpenAI・Anthropic・Google・Microsoft) | 3, 9, 11, 13 |
| 火 | 国内プレスリリース(PR TIMES などの生成AI導入発表) | 14, 15, 16 |
| 水 | 省庁・公的機関(デジタル庁・経産省・IPA・総務省・個人情報保護委員会) | 4, 12, 13 |
| 木 | 業界メディア(日経クロステック・ITmedia)の特集・連載 | 14, 15 |
| 金 | 海外(TechCrunch・企業テックブログ・HBR など) | 13, 17 |
| 土日 | スキャンは省略してよい(台帳の消化に充てる) |  |

## ニュース化を防ぐ歯止め

このリポジトリは**ニュースを単体で蓄積しない**。スキャンを入れると速報の寄せ集めに
崩れやすいので、次を必ず守る。

- **まず「既存ページの更新ネタ」として扱う。**
  見つけた出来事は、既存のどのページの本文を書き換える材料になるかを先に考える。
  新規ページにするのは、既存のどのページにも収まらないと判断できたときだけ

見つけた候補は、発見したその日に着手してよい。

## 候補

| 候補 | 想定Part/章 | 種別 | 根拠URL | 発見日 | 優先度 | 状態 |
|---|---|---|---|---|---|---|
| (スキャンで見つけた候補をここに追記する) | | | | | | |
| 小売・流通・ECにおける生成AI活用事例 | 14/第2章 | 事例追加 | https://www.watch.impress.co.jp/docs/news/2014409.html / https://www.lycorp.co.jp/ja/news/release/016840/ | 2026-11-11 | B | 完了(2026-11-11、PR #801) |
| 内部監査職における生成AI活用事例 | 15/第7章 | 事例追加 | https://jpn.nec.com/ad/onlinetv/ax-challenge-audit-ai.html / https://www.ally.com/tech/auditors-are-innovators-using-ai-to-realize-the-future-of-audit/ | 2026-11-11 | B | 完了(2026-11-11、PR #802) |
| 品質管理・QA職における生成AI活用事例 | 15/第12章 | 事例追加 | https://www.nsk.com/jp-ja/company/news/2025/ai-application-20250623/ / https://atmarkit.itmedia.co.jp/ait/articles/2605/28/news007.html | 2026-11-12 | B | 完了(2026-11-12、PR #804) |
| 介護業界における生成AI活用事例 | 14/第12章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000013.000049236.html / https://digitalpr.jp/r/131285 | 2026-11-12 | B | 完了(2026-11-12、PR #805) |
| 人材育成・研修(L&D)担当における生成AI活用事例 | 15/第6章 | 事例追加 | https://dime.jp/company_news/detail/?pr=2660602 / https://it.impress.co.jp/articles/-/29799 / https://zaikei.co.jp/releases/3358322/ | 2026-11-12 | B | 完了(2026-11-12、PR #808) |
| 経理・財務職における生成AI活用事例 — 追記ネタ: 味の素フィナンシャル・ソリューションズの経費精算承認を担う経理AIエージェント(工数76%削減との報道)を事例カードに | 15/第7章 | 事例追加 | https://www.itmedia.co.jp/business/spv/2606/19/news033.html | 2026-11-12 | B | 完了(2026-11-13、PR #810) |
| 医療・ヘルスケアにおける生成AI活用事例 — 追記ネタ: AISI「ヘルスケア領域におけるAIセーフティ評価観点ガイド」(2026年4月)を注意点・導入時の評価観点に反映 | 14/第4章 | 更新 | https://aisi.go.jp/output/output_information/260402/ | 2026-11-12 | C | 完了(2026-11-13、PR #814) |
| 産業用ロボット・FA(ファクトリーオートメーション)メーカーにおける生成AI活用事例 — 追記ネタ: AISI「AIロボティクスに関するセーフティ評価観点ガイド」(2026年7月)を反映 | 14/第1章 | 更新 | https://aisi.go.jp/output/output_information/260723/ | 2026-11-12 | C | 完了(2026-11-20。AISIロボティクスガイドの節を追加、FAセル向けではない点を明記) |
| AIレッドチーミングの基本(実施体制・頻度・外部ベンダー活用) — 追記ネタ: AISI「AIセーフティに関する評価観点ガイド」第1.20版=2026年7月、AIエージェント向け評価観点の拡充を反映 | 4/第2章 | 更新 | https://aisi.go.jp/output/output_framework/guide_to_evaluation_perspective_on_ai_safety/ | 2026-11-11 | B | 完了(2026-11-12、PR #806) |
| 日本における生成AI動向(採用状況・主要プレイヤー・政策) — 追記ネタ: 総務省 令和8年版情報通信白書の企業の生成AI業務利用率などを反映 | 13/第4章 | 更新 | https://www.soumu.go.jp/johotsusintokei/whitepaper/ja/r08/html/nd121130.html | 2026-11-11 | B | 完了(2026-11-12、PR #807) |
| 証券・資産運用業界における生成AI活用事例 | 14/第3章 | 事例追加 | https://www.smd-am.co.jp/news/news/2025/NewsRelease_20251022/ / https://www.watch.impress.co.jp/docs/news/2133776.html | 2026-11-13 | B | 完了(2026-11-13、PR #812) |
| 知財・特許担当者における生成AI活用事例 | 15/第8章 | 事例追加 | https://jpn.nec.com/press/202601/20260119_01.html / https://monoist.itmedia.co.jp/mn/articles/2604/02/news040.html | 2026-11-13 | B | 完了(2026-11-13、PR #813) |
| 生産管理・SCM(サプライチェーンマネジメント)担当における生成AI活用事例 | 15/第13章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000314.000053341.html / https://prtimes.jp/main/html/rd/p/000000040.000134983.html | 2026-11-13 | B | 完了(2026-11-13、PR #815) |
| 海外の主要基盤モデル企業一覧(フロンティアAI企業) — 追記ネタ: OpenAIが評価額1.25兆ドルで約110億ドルの第1回クロージング(Bloomberg報道、2026年11月6日。総額最大200億ドルの可能性、OpenAIはコメントせず)。Part13「生成AI業界の主要プレイヤーと動向」も合わせて更新 | 17/第1章 | 更新 | https://gvwire.com/2026/11/06/openai-secures-11-billion-funding-at-1-25-trillion-valuation-bloomberg-news-reports/ | 2026-11-13 | B | 完了(2026-11-14。AnthropicのIPO申請・仮条件も併せて反映。Part13側も同日更新) |
| AIエージェント運用のガバナンス設計(権限ポリシー・監査ログ・コスト管理) — 追記ネタ: HBR「Research: Why You Shouldn't Treat AI Agents Like Employees」(2026年5月6日、大規模実験にもとづく研究)。エージェントを「従業員扱い」する組織設計の副作用。本文は要確認(有料記事) | 11/第5章 | 更新 | https://hbr.org/2026/05/research-why-you-shouldnt-treat-ai-agents-like-employees | 2026-11-13 | C | 未着手 |
| SRE・インフラエンジニアにおける生成AI活用事例 | 15/第11章 | 事例追加 | https://tech.asken.inc/entry/2026/09/11/170000 / https://developers.play.jp/entry/2026/11/09/181049 | 2026-11-14 | B | 完了(2026-11-14。カタログ未保有ページから選定) |
| 化粧品業界における生成AI活用事例 | 14/第1章 | 事例追加 | https://www.itmedia.co.jp/enterprise/articles/2609/18/news020.html / https://news.mynavi.jp/techplus/article/20260831-4860665 | 2026-11-14 | B | 完了(2026-11-14。カタログ未保有ページから選定) |
| 経営コンサルティング業界における生成AI活用事例 | 14/第11章 | 事例追加 | https://workspace.google.com/blog/ja/customer-stories/funai-soken-maximizes-the-value-of-consulting-services-with-ai / https://www.bain.com/insights/how-to-accelerate-progress-on-ai/ | 2026-11-14 | B | 完了(2026-11-14。カタログ未保有ページから選定) |
| 人材紹介エージェント(キャリアアドバイザー)における生成AI活用事例 | 15/第18章 | 事例追加 | https://go.miitel.jp/hubfs/case/pdf/pdf-adecco.pdf / https://mendan.biz/case/massmedian | 2026-11-14 | B | 完了(2026-11-14。カタログ未保有ページから選定) |
| ドライバー・配送スタッフにおける生成AI活用事例 | 15/第18章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000002.000159082.html / https://www.aboutamazon.com/news/operations/amazon-ai-innovations-delivery-forecasting-robotics | 2026-11-14 | B | 完了(2026-11-14。カタログ未保有ページから選定。国内の実名事例は1件のみ確認) |
| 会計事務所・税理士法人における生成AI活用事例 | 14/第11章 | 事例追加 | https://biz.moneyforward.com/mfc-partner/case/11974/ / https://note.com/eiichiro49/n/n92c8075b021d | 2026-11-15 | B | 完了(2026-11-15。カタログ未保有ページから選定) |
| 医療機器製造業における生成AI活用事例 | 14/第4章 | 事例追加 | https://ai-keiei.shift-ai.co.jp/interview-f7-terumo/ / https://www.sbbit.jp/article/st/187303 | 2026-11-15 | B | 完了(2026-11-15。カタログ未保有ページから選定) |
| 歯科業界における生成AI活用事例 | 14/第4章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000012.000131402.html / https://ivry.jp/case/astershika/ | 2026-11-15 | B | 完了(2026-11-15。カタログ未保有ページから選定) |
| 労務・給与担当者における生成AI活用事例 | 15/第6章 | 事例追加 | https://it.impress.co.jp/articles/-/27265 / https://business.ntt-east.co.jp/content/cloudsolution/ih_column-215.html | 2026-11-15 | B | 完了(2026-11-15。カタログ未保有ページから選定) |
| 秘書・エグゼクティブアシスタント職における生成AI活用事例 | 15/第9章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000011.000023376.html / https://www.local.gov.uk/case-studies/buckinghamshire-council-early-adoption-microsoft-copilot | 2026-11-15 | B | 完了(2026-11-15。カタログ未保有ページから選定) |
| 鉄鋼・金属加工業における生成AI活用事例 | 14/第1章 | 事例追加 | https://www.microsoft.com/ja-jp/customers/story/23624-nippon-steel-corporation-microsoft-365-copilot / https://www.googlecloudpresscorner.com/2026-04-22-Tata-Steel-Partners-with-Google-Cloud-To-Deploy-a-Unified-Agentic-AI-Across-its-Global-Value-Chain | 2026-11-16 | B | 完了(2026-11-16。カタログ未保有ページから選定) |
| 自動車部品サプライヤー(ティア1・ティア2)業界における生成AI活用事例 | 14/第1章 | 事例追加 | https://www.jbs.co.jp/news/2026/0312-2 / https://digitalpr.jp/r/105357 | 2026-11-16 | B | 完了(2026-11-16。カタログ未保有ページから選定) |
| 旅客輸送(バス・タクシー・ライドシェア)業界における生成AI活用事例 | 14/第10章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000049.000137033.html / https://www.lyft.com/blog/posts/aws-and-lyft-bringing-agentic-ai-to-life-for-riders-and-drivers | 2026-11-16 | B | 完了(2026-11-16。カタログ未保有ページから選定) |
| 金融アドバイザー・FP(ファイナンシャルプランナー)における生成AI活用事例 | 15/第18章 | 事例追加 | https://www.atpress.ne.jp/news/533412 / https://www.silicon.co.uk/press-release/morgan-stanley-wealth-management-announces-latest-game-changing-addition-to-suite-of-genai-tools | 2026-11-16 | B | 完了(2026-11-16。カタログ未保有ページから選定) |
| 大学教員・研究者における生成AI活用事例 | 15/第12章 | 事例追加 | https://ai.vt.edu/content/dam/ai_vt_edu/ChatGPT-Edu-Pilot-Findings-Report.pdf / https://prtimes.jp/main/html/rd/p/000000105.000006186.html | 2026-11-16 | B | 完了(2026-11-16。カタログ未保有ページから選定) |
| Claudeの基本 — 追記ネタ: Claude Fable 5.2/Mythos 5.2 の公開(2026年11月9日。Mythos 5.2は審査済み組織向けの限定提供、API料金・速度向上の数値は公式で要確認)。Part 2「推論モデル」・Part 9 のAPI料金ページへの波及も確認 | 3/第5章 | 更新 | https://www.anthropic.com/news/claude-fable-and-mythos-5-2 / https://9to5mac.com/2026/11/09/anthropic-upgrades-claude-with-new-fable-5-2-model-details-here/ | 2026-11-16 | A | 完了(2026-11-17。5.5世代とMax/Ultra改称も併せて反映) |
| Microsoft Copilotの基本 — 追記ネタ: 2026年10〜11月の更新(ChatとCoworkの統合ホーム、常時稼働のクラウド型個人エージェント「Autopilot」〈Frontier〉、ProjectsとSkillsのCopilot Chatへの拡大、PowerPointでSonnet 5.5モデル)。Ignite(11月17〜20日)の発表後に着手するとよい | 3/第5章 | 更新 | https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/what's-new-in-microsoft-copilot--october-2026/4568528 | 2026-11-16 | B | 完了(2026-11-18。Ignite初日の発表まで反映) |
| AIエージェントの基本 — 追記ネタ: OpenAI DevDay 2026(2026年9月下旬)で発表された常時稼働エージェント「Dots」(専用のクラウド環境で自律的に動く)。モデル名は報道間で食い違いがあるため公式で要確認 | 11/第1章 | 更新 | https://fastcompany.com/91615778/openai-reveals-slew-launches-annual-conference-after-shelving-new-model-over-safety-concerns / https://www.1news.co.nz/2026/09/30/openai-unveils-always-on-ai-agent-after-model-shelved-over-safety-risk/ | 2026-11-16 | B | 完了(2026-11-20。dots・Gemini Spark・Microsoft Scoutを常時稼働型として追加、Cowork統合を反映。モデル名は報道で食い違うため不掲載) |
| 鉄鋼・金属加工業における生成AI活用事例 — 要確認: 本文のJFEスチール「実装・単体テスト工程で約68%削減」の数値は、引用元リンクが404で一次情報を確認できなかった(2026-11-16の事例追加時に判明)。一次情報が見つからなければ本文から削除する | 14/第1章 | 更新 | https://monoist.itmedia.co.jp/mn/articles/2504/08/news006.html | 2026-11-16 | B | 完了(2026-11-17。日刊産業新聞で68%=検証結果を確認、20%は見込みと訂正、3割目標は出典未確認のため削除) |
| 海運・港湾業界における生成AI活用事例 | 14/第10章 | 事例追加 | https://exawizards.com/archives/29558 / https://www.nyk.com/news/2025/20251218_03.html | 2026-11-17 | B | 完了(2026-11-17、PR #837。カタログ未保有ページから選定) |
| 警備業界における生成AI活用事例 | 14/第12章 | 事例追加 | https://www.alsok.co.jp/company/news/pdf/20250401.pdf / https://sierra.ai/customers/adt | 2026-11-17 | B | 完了(2026-11-17、PR #840。カタログ未保有ページから選定) |
| 臨床開発・治験担当者(CRA・CRC)における生成AI活用事例 | 15/第12章 | 事例追加 | https://aws.amazon.com/jp/blogs/news/genai-usecase-iqvia-serviceis/ / https://www.nttdata.com/global/ja/news/topics/2026/063001 | 2026-11-17 | B | 完了(2026-11-17、PR #839。カタログ未保有ページから選定) |
| 不動産管理(プロパティマネジメント)担当者における生成AI活用事例 | 15/第18章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000216.000073738.html / https://prtimes.jp/main/html/rd/p/000000177.000038148.html | 2026-11-17 | B | 完了(2026-11-17、PR #841。カタログ未保有ページから選定) |
| 倉庫管理・在庫管理担当者における生成AI活用事例 | 15/第13章 | 事例追加 | https://www.mitsui-soko.com/news/20260727 / https://www.supplychaindive.com/news/4-walmart-supply-chain-ai-uses/760891/ | 2026-11-17 | B | 完了(2026-11-17。カタログ未保有ページから選定) |
| 医療・ヘルスケアにおける生成AI活用事例 — 追記ネタ: 長野市民病院が電子カルテ連携の生成AIアシスタント(ユニリタ「SecuAiGent」)を50種類以上開発し、年間5,472時間の業務効率化を試算(2025年4月〜2026年1月の利用実績、アンケートベース)。一次リリースの原文で要確認。医療事務・医師の文書作成系ページへの相互リンクも検討 | 14/第4章 | 事例追加 | https://www.tv-tokyo.co.jp/plus/external-pr/entry/53966.html / https://digital-gorilla.co.jp/ai-lab/?p=656 | 2026-11-17 | B | 完了(2026-11-20。長野市民病院・相澤病院・武蔵ヶ丘病院の3件を追加) |
| 製薬業界における生成AI活用事例 — 追記ネタ: 塩野義製薬×日立の規制文書作成支援(CSR約50%・プロトコル約20%削減、社内PoC)は職種ページ(CRA・CRC)にカード化済み。Part 14側の本文から1行リンクに整理する | 14/第4章 | 更新 | https://www.shionogi.com/content/dam/shionogi/jp/news/pdf/2026/2月/J20260224.pdf | 2026-11-17 | C | 未着手 |
| 訪問看護・在宅医療における生成AI活用事例 | 14/第4章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000128.000044577.html / https://www.itmedia.co.jp/news/articles/2509/17/news002.html | 2026-11-18 | B | 完了(2026-11-18。カタログ未保有ページから選定) |
| スポーツ業界における生成AI活用事例 | 14/第12章 | 事例追加 | https://aws.amazon.com/jp/blogs/news/genai-case-study-san-en-neophoenix/ / https://www.premierleague.com/en/news/4338015/premier-league-announces-partnership-with-microsoft | 2026-11-18 | B | 完了(2026-11-18。カタログ未保有ページから選定) |
| 製造・建設現場の作業員・現場監督における生成AI活用事例 | 15/第18章 | 事例追加 | https://it.impress.co.jp/articles/-/29733 / https://www.rodo.co.jp/news/222027/ | 2026-11-18 | B | 完了(2026-11-18。カタログ未保有ページから選定) |
| 医療事務・クリニック受付職における生成AI活用事例 | 15/第18章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000217.000048083.html / https://ascii.jp/elem/000/004/234/4234172/ | 2026-11-18 | B | 完了(2026-11-18。カタログ未保有ページから選定。受付・電話・レセプト点検の生成AI実名事例は未発見) |
| 介護職員における生成AI活用事例 | 15/第18章 | 事例追加 | https://aws.amazon.com/jp/solutions/case-studies/yasashii-te / https://www.jf-cmca.jp/attach/kenkyu/honbu/r7/seisei-ai.pdf | 2026-11-18 | B | 完了(2026-11-18。カタログ未保有ページから選定) |
| 公共・自治体における生成AI活用事例 — 追記ネタ: デジタル庁 源内のAIエージェント利用環境(2026年10月〜順次展開)と「源内基準」第1版(2026年10月20日) | 14/第9章 | 更新 | https://www.digital.go.jp/en/policies/genai/agent-safety-standard | 2026-11-18 | A | 完了(2026-11-18) |
| 学習塾・予備校における生成AI活用事例 | 14/第8章 | 事例追加 | https://kyodonewsprwire.jp/release/202405170941 / https://www.softbank.jp/biz/customer-success-stories/202509/kawaijuku/ / https://zaikei.co.jp/releases/3236686/ | 2026-11-18 | B | 完了(2026-11-19。3件とも効果の数値は公表なし) |
| AIエージェント運用のガバナンス設計 — 追記ネタ: デジタル庁「源内基準」第1版(2026年10月20日)のAIエージェント統制措置(目的・権限の限定、重要処理の確認・承認、ログ保存、利用停止機能、スキル審査)と、生成AI調達・利活用ガイドライン次期改訂の検討(総務省 第32回AIガバナンス検討会 資料2-1、2026年10月。最小権限・HITL・MCPの監査・承認疲れ等) | 11/第5章 | 更新 | https://www.digital.go.jp/en/policies/genai/agent-safety-standard / https://www.soumu.go.jp/main_content/001099156.pdf | 2026-11-18 | B | 完了(2026-11-19。源内基準とAI事業者ガイドライン第1.2版を反映。総務省資料2-1はPDFの本文を確認できず未反映) |
| AI規制・ガバナンスの動向 — 追記ネタ: AI事業者ガイドライン次期更新の検討開始(総務省・経産省 第32回AIガバナンス検討会、2026年10月30日。AIエージェント・フィジカルAIの記述追加など。公表時期は要確認) | 4/第4章 | 更新 | https://www.soumu.go.jp/main_content/001099499.pdf | 2026-11-18 | C | 未着手 |
| 日本における生成AI動向 — 追記ネタ: AISI事業実証WG ビジョンペーパー第2.0版(2026年10月6日。医療・ロボティクス・教育・Geo AIの4分野) | 13/第4章 | 更新 | https://aisi.go.jp/output/output_information/261006/ | 2026-11-18 | C | 未着手 |
| プロンプトインジェクション/攻撃と防御 — 参考: IPA「AIセキュリティ短信 2026年11月号」(2026年11月13日。AIエージェント攻撃基盤の拡散、AI開発ツールの侵害など。要約はAI生成を含むためIPAは正確性を保証せず、一次情報をたどって使う) | 4/第2章 | 更新 | https://www.ipa.go.jp/digital/ai/security/rcu1hd0000007gji-att/2026-5_1113.pdf | 2026-11-18 | C | 未着手 |
| 社会保険労務士(社労士)における生成AI活用事例 | 15/第8章 | 事例追加 | https://ascii.jp/elem/000/004/401/4401136/ / https://digirise.ai/case/bizarqsama/ | 2026-11-19 | B | 完了(2026-11-19。カタログ未保有ページから選定。3件ともベンダー公表) |
| アニメ・映像制作業界における生成AI活用事例 | 14/第7章 | 事例追加 | https://kai-you.net/article/95123 / https://weekly.ascii.jp/elem/000/004/432/4432332/ | 2026-11-19 | B | 完了(2026-11-19。カタログ未保有ページから選定。謝罪事例を含む) |
| 獣医師における生成AI活用事例 | 15/第18章 | 事例追加 | https://ascii.jp/elem/000/004/375/4375471/ / https://www.prnewswire.com/news-releases/veg-er-for-pets-partners-with-vetrec-to-advance-ai-powered-documentation-across-emergency-veterinary-care-302798165.html | 2026-11-19 | B | 完了(2026-11-19。カタログ未保有ページから選定) |
| 動画配信・OTTプラットフォーム業界における生成AI活用事例 | 14/第7章 | 事例追加 | https://www.bnnbloomberg.ca/business/artificial-intelligence/2025/07/18/netflix-says-it-used-genai-in-argentine-tv-series/ / https://www.engadget.com/entertainment/amazon-halts-ai-anime-dub-beta-after-widespread-ridicule-141501051.html | 2026-11-19 | B | 完了(2026-11-19。カタログ未保有ページから選定。撤回・謝罪事例を含む) |
| 司法書士・行政書士における生成AI活用事例 | 15/第8章 | 事例追加 | https://www.bengo4.com/times/articles/996160973781/ | 2026-11-19 | B | 未着手(2026-11-19に調査。実名で裏取りできたのは司法書士法人みつ葉グループ〈GPTs・Gemで債務整理のLINE返信下書き、電話ヒアリングの聞き漏れチェック〉の1件のみで3件に届かず見送り。司法書士会の機関誌などで追加の実名事例を探す) |
| AI生成物の品質管理(「ワークスロップ」対策)— 追記ネタ: HBRの「workslop」(低品質なAI生成物が受け手に手戻りを押し付ける現象。BetterUp Labs・スタンフォード大の調査、2025年9月)と2026年の続報(作り手側の要因、Holweg・Davenportの「knowledge decay」)。Human in the Loopの業務設計またはAI文章作成ページの注意点に反映。HBR原文の数値は要確認(二次報道のみ確認) | 12/第1章 | 更新 | https://thenextweb.com/news/ai-workslop-knowledge-decay-harvard-business-review-productivity / https://www.techspot.com/news/109591-companies-losing-money-ai-workslop-slows-everything-down.html | 2026-11-20 | B | 完了(2026-11-21。Human in the Loopの業務設計にワークスロップ対策の節を新設。HBR原文は書誌情報・要約のみ確認し、調査値はBetterUp公表値をもとに、出典間で一致する数値だけを採用) |
| 生成AIとイノベーション(アイデア出しの画一化リスク)— 追記ネタ: HBR「Research: The Innovation Problems AI Can't Solve」(2026年8月14日、De Freitasほか)と元論文のHBSワーキングペーパー「Innovating with Generative AI: A Human Bottleneck Framework」(No.26-094)。LLMの典型的なアイデアへのアンカリング。AIの得意・不得意(タスク適性)ページの更新ネタ | 12/第1章 | 更新 | https://tagteam.harvard.edu/hub_feeds/924/feed_items/18620563 / https://aiinstitute.hbs.edu/idea-flow-the-machine/ | 2026-11-20 | C | 未着手 |
| 主要AIチャットツールのエージェント機能・スケジュールタスク比較 / ChatGPTのエージェント機能 — 追記ネタ: OpenAI dots(DevDay 2026、常時稼働型エージェント)が未反映。Part11「AIエージェントとは何か」には2026-11-20に反映済み | 3/第4章 | 更新 | https://thenextweb.com/news/openai-dots-always-on-ai-agents-cloud-computers-devday / https://openai.com/index/introducing-dots/ | 2026-11-20 | B | 完了(2026-11-22。ChatGPTのエージェント機能ページは2026-11-21、比較ページ ai-chat-tools-agent-tasks-comparison.md は2026-11-22にdots・Autopilotを反映) |
| 美容業界(理美容・エステ・ネイル)における生成AI活用事例 | 14/第12章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000229.000056805.html / https://beautymatter.com/articles/madison-reed-turns-to-ai-agent-madi-to-improve-beauty-retail-traffic | 2026-11-20 | B | 未着手(2026-11-20に調査。阪南理美容〈IVRy音声AI〉・ビアンカクリニック・Madison Reed〈Madi〉・Sport Clips〈SOCi〉の4件は実在を確認したが、うち3件は出典で「生成AI/LLM」の利用が確認できず見送り。生成AIであることが明記された事例を探し直す) |
| エンジニア・開発職における生成AI活用事例 | 15/第11章 | 事例追加 | https://www.cyberagent.co.jp/news/detail/id=33582 / https://news.mynavi.jp/article/20260304-4183369/ | 2026-11-21 | B | 完了(2026-11-21。サイバーエージェント・DeNA・マネーフォワード・freeeの4件を追加。主要職種でカタログ3件のページから選定) |
| カスタマーサポート職における生成AI活用事例 | 15/第4章 | 事例追加 | https://news.mynavi.jp/techplus/article/20250902-3429129/ / https://www.jri.co.jp/company/release/2026/0218/ | 2026-11-21 | B | 完了(2026-11-21。JCOM・三井住友銀行・かんぽ生命保険・三井住友海上火災保険の4件を追加。かんぽ生命はPoC値、JCOMは担当者の報告値) |
| 図書館・博物館業界における生成AI活用事例 | 14/第9章 | 事例追加 | https://current.ndl.go.jp/e2885 / https://www.clevelandart.org/about/press/cleveland-museum-art-announces-artlens-reimagined-opening-july-23-2026 | 2026-11-21 | B | 完了(2026-11-21。カタログ未保有ページから選定。生成AI利用が出典で明記された実名事例5件〈国内3・海外2〉でカタログ新設、本文の未確認記述を修正) |
| NPO・非営利団体における生成AI活用事例 | 14/第12章 | 事例追加 | https://prtimes.jp/main/html/rd/p/000000052.000070582.html / https://www.rescue.org/irc-responsible-ai-humanitarian-sector | 2026-11-21 | B | 完了(2026-11-21。カタログ未保有ページから選定。eboard・セイエン・IRC・Infoxchange・Epilepsy Foundationの5件を追加、国内は効果公表事例が少なく海外3件を併載。未確認記述を削除・修正) |
| 情報システム(IT)部門における生成AI活用事例 | 15/第10章 | 事例追加 | https://www.softbank.jp/business/content/blog/202510/genai-in-action / https://note.com/itg_corpit/n/na2ab55d41864 | 2026-11-21 | B | 完了(2026-11-21。事例追加: ソフトバンク・日鉄興和不動産・CAMPFIRE・グリーホールディングスの国内4件。日鉄興和不動産は見込み値・ベンダー公表、ソフトバンクの工数削減は担当者の体感、グリーは数値公表なし) |
| 情報システム(IT)部門における生成AI活用事例 — 追記ネタ: 既存のServiceNowカードの「120日以内に年間50 FTE相当」「デフレクション14ポイント向上」が見込み値/14%の誤読でないか、公式ページ(2026-11-21時点で403)で再確認する | 15/第10章 | 更新 | https://www.servicenow.com/ | 2026-11-21 | C | 未着手 |
| Google Geminiの基本 / 主要AIチャットツールのエージェント機能・スケジュールタスク比較 / AIエージェントとは何か — 追記ネタ: Gemini Sparkが2026年10月に「Task」へ改称され通常チャットに統合、日本など6か国で有料プランなしで利用可に(公式ヘルプで確認済み。各論ページ gemini-spark-basics.md は2026-11-22に反映済み)。比較ページのGemini列(料金・プラン・「Spark」表記)が未反映 | 3/第4章 | 更新 | https://support.google.com/gemini/answer/17094507?hl=en / https://9to5google.com/2026/10/12/gemini-spark-task-redesign/ | 2026-11-22 | B |一部完了(2026-11-23、Google Geminiの基本に反映。7日ルールにより、AIエージェントとは何かは2026-11-27以降・比較ページは2026-11-29以降に反映) |
| 美容業界(理美容・エステ・ネイル)における生成AI活用事例 — 事例追加: 2026-11-22の調査では美容室チェーン・ホットペッパービューティーの実名の生成AI導入事例が見つからず見送り(化粧品メーカー・小売の事例は化粧品業界ページに追加済み) | 14/第12章 | 事例追加 | — | 2026-11-22 | C | 見送り(実名のサロン事例が3件に満たない) |
| Google Gemini APIの基本 — 追記ネタ: Gemini 4ファミリー(Hydrogen $1.50/$7.50、Neon $3/$15、Carbon・Argonは11月30日まで$2/$10→以降$4/$20)へのAPIモデル交代。ページは2026-08-09更新で3.x系のまま | 9/第1章 | 更新 | https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/ / https://9to5google.com/2026/11/10/gemini-app-4-carbon/ | 2026-11-23 | A | 完了(2026-11-23) |
| 主要AIチャットツールのプラン・モデル比較 — 追記ネタ: Gemini 4ファミリー、ChatGPTのGPT-6 Sol/GPT-6.2(Work・Codex)、Google AI Plusの月額¥1,200への反映。ページは2026-08-20更新 | 3/第1章 | 更新 | https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt / https://one.google.com/intl/ja_jp/about/google-ai-plans/ | 2026-11-23 | A |完了(2026-11-23) |
| ChatGPTのモデル一覧と使い分け | 3/第1章 | 更新 | https://help.openai.com/en/articles/20001354-gpt-6-and-other-models-in-chatgpt / https://openai.com/index/introducing-gpt-6-2-astra-sol/ | 2026-11-23 | A | 完了(2026-11-23) |
| 教育における生成AI活用事例 | 14/第8章 | 事例追加 | https://www.kyoiku.metro.tokyo.lg.jp/ja/information/press/2025/05/2025051201 / https://blog.google/innovation-and-ai/models-and-research/google-deepmind/ai-classroom-northern-ireland/ | 2026-11-23 | B | 完了(2026-11-23、PR #885) |
| 物流・運輸における生成AI活用事例 | 14/第10章 | 事例追加 | https://it.impress.co.jp/articles/-/28094 / https://prtimes.jp/main/html/rd/p/000000003.000179911.html | 2026-11-23 | B | 完了(2026-11-23、PR #886) |
| 経営者・管理職における生成AI活用事例 | 15/第17章 | 事例追加 | https://www.sbbit.jp/article/cont1/184955 / https://www.smfg.co.jp/news/pdf/j20250805_01.pdf | 2026-11-23 | B | 完了(2026-11-23、PR #887) |
| デザイナー・クリエイティブ職における生成AI活用事例 | 15/第14章 | 事例追加 | https://www.businessinsider.jp/article/2611-rakuten-adobe-firefly-branding/ / https://www.figma.com/customers/how-findable-moved-50-percent-faster-with-figma-make/ | 2026-11-23 | B | 完了(2026-11-23、PR #888) |
| 購買・調達職における生成AI活用事例 | 15/第9章 | 事例追加 | https://www.soumu.go.jp/denshijiti/digital_transformation_portal/case/pdf/r07_dx3_23.pdf / https://newsroom.bmwgroup.com/global/greater-efficiency-and-productivity-with-artificial-intelligence---generative-ai-in-bmw-group-purchasing | 2026-11-23 | B | 完了(2026-11-23) |
| 海運業界における生成AI活用事例 — 追記ネタ: 川崎汽船のexaBase 生成AI全社導入(月間削減時間420→2,770時間、ベンダー公表)を事例カードに。2026-11-23の物流ページ調査で裏取り済み | 14/? | 事例追加 | https://exawizards.com/archives/29558 / https://www.logi-today.com/727918 | 2026-11-23 | B | 未着手 |
| 生成AI導入のROI測定・効果測定の考え方 — 追記ネタ: パナソニック コネクトの2025年度実績(総労働時間の3.4%・78.8万時間削減、2030年10%目標) | 12/第1章 | 更新 | https://news.panasonic.com/jp/press/jn260729-1 | 2026-11-24 | B | 完了(2026-11-24、PR #890) |
| 広報・PR職における生成AI活用事例 | 15/第3章 | 事例追加 | https://www.advertimes.com/?p=549072 / https://www.bcg.com/news/13october2025-how-ai-is-transforming-communications-function | 2026-11-24 | B | 完了(2026-11-24、PR #891。電通「河南2号」は広告記事のみで見送り) |
| 企画職における生成AI活用 | 15/第5章 | 事例追加 | https://www.lawson.co.jp/company/news/detail/1532206_2504.html / https://www.nttdata.com/global/ja/news/topics/2026/031900 | 2026-11-24 | B | 完了(2026-11-24、PR #892) |
| 看護師・医療従事者における生成AI活用事例 | 15/第18章 | 事例追加 | https://jpn.nec.com/medical_healthcare/jirei/data/Itvision_hasimoto_202607.pdf / https://prtimes.jp/main/html/rd/p/000000216.000048083.html | 2026-11-24 | B | 完了(2026-11-24、PR #893) |
| 自動車業界における生成AI活用事例 | 14/第12章 | 事例追加 | https://codezine.jp/article/detail/28873 / https://venturebeat.com/ai/gm-redesigned-its-engineering-workflows-around-ai-agents-and-tripled-its-merged-pull-requests | 2026-11-24 | B | 完了(2026-11-24、PR #894) |
| 家電量販店業界における生成AI活用事例 | 14/第2章 | 事例追加 | https://www.ceconomy-mms.com/en/article/reta-award-2026-mediamarktsaturn-uberzeugt-mit-ki-losungen-fur-kunden-und-mitarbeitende / https://pc.watch.impress.co.jp/docs/release/atpress/1629213.html | 2026-11-24 | B | 完了(2026-11-24。カタログ未保有ページから選定) |
| 自動車部品サプライヤー業界における生成AI活用事例 — 追記ネタ: デンソー人事部門のキャリア支援レポート自動生成・人事FAQ作成(経団連「HR部門におけるAI等の活用に関する報告書」2026年4月14日。約5,400時間→約15時間は試算値) | 14/第1章 | 事例追加 | https://www.keidanren.or.jp/policy/2026/016_jirei06.pdf | 2026-11-24 | C | 未着手 |
| 造船業における生成AI活用事例 | 14/第1章 | 事例追加 | https://www.marinelink.com/news/kr-hd-hyundai-samho-complete-aipowered-539972 / https://www.logi-today.com/969748 | 2026-11-25 | B | 完了(2026-11-25。カタログ未保有ページから選定。常石造船のAI駆動開発は生成AIの利用が出典で明示されず見送り) |
