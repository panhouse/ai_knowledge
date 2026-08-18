---
title: NPO・非営利団体における生成AI活用事例
part: 14
chapter: "第12章 その他・未分類"
tags: [NPO, 非営利団体, 生成AI活用事例, 助成金申請, ファンドレイジング, Google for Nonprofits, Claude for Nonprofits, OpenAI for Nonprofits]
created: 2026-07-18
updated: 2026-08-15
---

# NPO・非営利団体における生成AI活用事例

## これは何か

NPO(Non-Profit Organization、非営利団体)は、少人数のスタッフで助成金申請書・寄付募集チラシ・年次報告書・問い合わせ対応まで幅広い文書業務をこなす一方、専任の広報・IT担当者を置けない団体が多く、生成AIによる業務効率化の恩恵を最も受けやすい組織形態の一つである。2025年末から2026年前半にかけて、Anthropic(Claude)・OpenAI(ChatGPT)・Google・Microsoftの主要ベンダーが相次いで非営利団体向けの正式な割引・無償プログラムを整備し、営利企業よりも大幅に低いコストで生成AIを導入できる環境がほぼ出揃った。本ページは、助成金申請書作成・ファンドレイジング(寄付募集)・多言語相談対応・議事録や事務処理、そして2026年に顕在化した災害支援の場面まで、NPO特有の業務における生成AIの使いどころを整理する。

## 仕組み・背景

NPOにおける生成AI活用は、大きく5つの領域に分かれる。

1. **助成金申請書の作成**: 助成金申請は、フォーマットが決まっており、過去の採択事例が公開されており、評価軸が明文化されていることが多いため、NPO業務の中でも生成AIとの相性が特に良い領域とされる([AI PICKS](https://aipicks.jp/mag/npo-ai-guide-2026))。TechSoupとTapp Networkが1,300名超のNPO専門職を対象に行った「State of AI in Nonprofits」調査では、85.6%がAIツールを試している一方で正式な活用戦略を持つ団体は24%にとどまり、AI利用ポリシーを持たない団体も76%に上るなど、関心と体制整備のギャップが指摘されている。また年間予算100万ドル超の団体は予算規模の小さい団体の約2倍のペースでAIを導入しており(66% vs 34%)、資金力による「AI格差」が広がっている点にも注意が必要である([NonprofitPro](https://www.nonprofitpro.com/article/2025-ai-benchmark-report-how-artificial-intelligence-is-changing-the-nonprofit-sector/))。助成金申請に限れば24.6%が既にAIを活用しているとの報告もあり、ある地域NPOでは提案書のドラフト作成にAIを使い、人によるレビューを経て採択率75%を維持しながら準備時間を4割削減した事例も紹介されている([Mixflow](https://mixflow.ai/blog/generative-ai-in-2026-revolutionizing-grant-writing-and-donor-engagement-for-non-profits/))。
2. **ファンドレイジング(寄付募集)・広報**: 寄付呼びかけチラシ・SNS投稿・年次報告書のデザインを内製化する動きが広がっている。Canvaは登録非営利団体向けに「Canva for Nonprofits」を無償提供しており、デザインテンプレートと生成AI機能を組み合わせて広報物を作成できる([AI PICKS](https://aipicks.jp/mag/npo-guide-2026))。
3. **多言語相談対応**: 外国人支援・国際協力・難民支援系のNPOでは、相談者の文化的背景に配慮した訳し方や、日本の制度に不案内な相談者向けの噛み砕いた説明まで、Claude・ChatGPTなどを使ったAI翻訳・下訳の活用が広がっている。
4. **議事録・事務処理の自動化**: 理事会・総会の議事録作成、ボランティアの問い合わせ対応、日程調整、連絡先リストの更新など、定型的な事務作業をAIエージェントで自動化する動きも出てきている([DevelopersIO](https://dev.classmethod.jp/articles/nonprofit-ai-lab-02-generative-ai-use-cases-for-nonprofits/))。
5. **災害支援における活用(2026年に顕在化)**: 2026年7月28日、熊本県熊本地方を震源とするマグニチュード7.1・最大震度7の地震(令和8年熊本地震)が発生した際、被災した個人が避難所からスマートフォンで生成AIを使い、数時間で生活情報掲示板「イマココナビ」を開発・公開し、営業再開した店舗や炊き出し場所の情報を住民同士で共有する用途で16万人超に利用された([Yahoo!ニュース/時事通信](https://news.yahoo.co.jp/articles/0bd9405236b3b9483a0cfa7b522e0981dbefa868))。これを受けて、NPO担当者・自治体職員・教職員なども申請できる形で、災害支援向けの生成AIインフラを2026年10月31日まで無償提供する取り組みも始まっており、災害支援NPOが自前でAI活用の仕組みを立ち上げるハードルが下がりつつある([AICU](https://corp.aicu.ai/ja/kumamoto260728))。一方で同じ被災地では生成AIによる偽の被災映像も出回り、功罪の両面が指摘されている点は要注意である([時事通信/リスク対策.com](https://www.risktaisaku.com/articles/-/114226))。

2026年時点で、主要ベンダーの非営利団体向け割引プログラムが出揃っている。

- **Anthropic「Claude for Nonprofits」**: 2025年12月2日(Giving Tuesday)に発表。適格な非営利団体はTeam・Enterpriseプランを最大75%割引で利用でき、Teamプランは1ユーザーあたり月8ドル程度(最低5シートから)。Sonnet 4.5・Haiku 4.5に加え、Enterpriseでは申請によりOpus 4.5も利用可能で、Claude CodeとCoworkも全シートに含まれる。寄付管理システムBlackbaud(Raiser's Edge NXT)・企業ボランティア/寄付プラットフォームBenevity(240万団体超のデータベース)・助成金情報データベースCandidとMCP(Model Context Protocol)連携しており、Claudeから直接これらのデータを参照できる。総額1.5億ドル規模の「Claude Corps」フェローシップやAI活用研修「AI Fluency for Nonprofits」も無償提供している([Forbes](https://www.forbes.com/sites/afdhelaziz/2025/12/02/how-anthropic-and-claude-for-nonprofits-is-putting-ai-in-the-hands-of-changemakers/)、[NBC News](https://www.nbcnews.com/tech/tech-news/giving-tuesday-ai-anthropic-offers-nonprofits-discounts-rcna246770))。
- **OpenAI「OpenAI for Nonprofits」**: 2026年2月6日に発表。ChatGPT Business/Enterpriseを最大75%割引で利用でき、Businessは年払いで1ユーザーあたり月8ドル程度、Enterpriseは割引後で月15ドル程度が目安となる。米国501(c)(3)相当の非営利法人格を持ち、政治団体・政府機関と関係がないことが条件で、提携先Goodstackを通じて審査を受ける。
- **Google for Nonprofits**: Gemini appとNotebookLM(旧Gemini Notebook)が、Google Workspace for Nonprofitsのプランに無償で含まれるようになり、上位のGoogle Workspaceエディションへのアップグレードも最大75%割引で可能。ファンドレイジング・マーケティング・業務効率化に関する無償オンライン講座や専門家による個別コーチングも提供され、AI Opportunity Fund(総額7,500万ドルの一部として、非営利団体の学習・導入支援に1,700万ドルをAPAC等の地域に配分)による資金支援もある。
- **Microsoft for Nonprofits**: Microsoft 365 Copilotを適格な非営利団体向けに年払いで1ユーザーあたり月25.50ドルで提供し、Copilot ChatはMicrosoft 365サブスクリプションに追加費用なしで含まれる。加えて年間2,000ドル分のAzureクレジットが付与される。

こうした割引・無償プログラムの整備により、月数千円、あるいは無償に近い規模で生成AIを導入できる環境が広がっている一方、資金力のある団体ほど活用が先行する「AI格差」も同時に進行している([AI PICKS](https://aipicks.jp/mag/npo-guide-2026))。

## 使いどころ・使い分け

| 業務 | 生成AIが向く | 向かない/慎重にすべき理由 |
|---|---|---|
| 助成金申請書のドラフト作成 | 向く(過去の採択事例・フォーマットを参考にした下書き) | 団体固有の実績・数値・独自性は人が加筆し、事実確認を行う |
| 寄付募集チラシ・SNS投稿文の作成 | 向く(Canva等のデザインツールとの組み合わせ) | 団体のブランドトーン・受益者への配慮は人が最終確認する |
| 多言語相談対応の一次対応・翻訳 | 向く(定型的な問い合わせ・翻訳の下訳) | 深刻な相談内容・専門的な法的助言は人の専門職が対応する |
| 議事録作成・日程調整・事務処理 | 向く(定型業務の自動化) | 意思決定に関わる機微な議論内容は要約の精度を人が確認する |
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

### ツール横断の対応表

| 用途 | ツール例 |
|---|---|
| 助成金申請書・文書作成全般 | Microsoft 365 Copilot(Microsoft for Nonprofits経由)、Claude Team(Claude for Nonprofits経由)、ChatGPT Business/Enterprise(OpenAI for Nonprofits経由)、Gemini(Google for Nonprofits経由) |
| 寄付募集チラシ・SNS投稿デザイン | Canva for Nonprofits |
| 助成金・寄付者データの参照 | Claude for Nonprofits(Candid・Blackbaud・BenevityとのMCP連携) |
| 非営利団体向け割引・無償プログラム | Google for Nonprofits、Microsoft for Nonprofits、Claude for Nonprofits、OpenAI for Nonprofits |

いずれの割引プログラムも、提携先(Goodstack等)による法人格・活動内容の審査を経て初めて適用される。まずは自団体がGoogle・Microsoft・Anthropic・OpenAIのいずれかの非営利団体向けプログラムの利用資格を満たすか確認し、割引・無償枠を活用してから、必要に応じて有料プランを検討するのが費用対効果の高い順序である。

## 注意点・よくある誤解

- **受益者の個人情報・相談内容を安易に入力しない**: 支援対象者の氏名・相談内容など機微な個人情報を汎用チャットAIに入力すると、意図せずデータが学習・保存されるリスクがある。法人契約でオプトアウトされているか、非営利団体向けプランのデータ保護方針を確認する([生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md))。
- **助成金申請書の「独自性」は必ず人が書く**: AIが作った下書きをそのまま提出すると、他団体と似通った表現になりがちで、審査員に「オリジナリティがない」と判断されるリスクがある。団体固有のエピソード・実績は必ず人が加筆する。海外では大手助成財団がAI利用に関するガイドラインを助成先向けに公表し始めており、申請書がAI生成であることの開示を求める動きも出てきている。
- **非営利団体向け割引プログラムは審査・登録が必要**: 各社のプログラムは提携先(Goodstack等)による法人格の種類や活動内容の審査があり、即日利用できるとは限らない。導入を検討する際は早めに申請する。
- **「AI格差」に注意する**: 予算規模の大きい団体ほどAI導入が先行し、小規模団体との差が広がっている。AI利用ポリシーを持たない団体が全体の76%に上るとの調査もあり、まずは簡易な利用ルール(入力禁止情報の線引きなど)を定めることが導入の第一歩になる。
- **災害時の生成AI活用は「功罪」両面を理解する**: 被災地での生活情報の即時共有には効果がある一方、生成AIによる偽の被災映像・デマの拡散リスクも同時に指摘されている。NPOが情報発信に使う場合は、一次情報の出典を明示し、未確認情報の拡散を避ける運用ルールを決めておく。
- **AIによる翻訳・多言語対応は専門的な内容に限界がある**: 定型的な問い合わせ対応には有効だが、法的助言や深刻な相談内容の翻訳は誤訳のリスクを考慮し、専門通訳者・専門職員の確認を挟む。

## 最初の一歩

Google for Nonprofits・Microsoft for Nonprofits・Claude for Nonprofits・OpenAI for Nonprofitsのいずれかについて、自団体が非営利法人としての利用資格を満たすか確認し、直近の助成金申請書またはSNS投稿文の下書き作成にチャットAIを試してみる。

## 関連トピック

- [公共・自治体における生成AI活用事例](public-sector-ai-use-cases.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)
- [生成AIによる文章作成・編集の実務活用](../part12-business-practice/ai-writing-and-editing.md)

## 更新履歴

### 2026-08-15: 非営利団体向け割引プログラムの最新化と災害支援事例を追加
- **内容**: Anthropic「Claude for Nonprofits」(2025年12月発表、最大75%割引・Benevity/Blackbaud/CandidとのMCP連携・Claude Corps)、OpenAI「OpenAI for Nonprofits」(2026年2月発表)、Google/Microsoftの最新プログラム内容を具体化。TechSoup/Tapp Networkの調査データ(AI活用戦略の有無・団体規模によるAI格差)、地域NPOの助成金申請での時間削減事例を追加。2026年7月の令和8年熊本地震における個人開発の生活情報掲示板「イマココナビ」とNPO向け災害支援AIインフラの無償提供事例を新設し、災害時の生成AI活用の功罪(偽映像リスク)にも言及
- **出典**: [NBC News: Anthropic offers nonprofits discounts for Giving Tuesday](https://www.nbcnews.com/tech/tech-news/giving-tuesday-ai-anthropic-offers-nonprofits-discounts-rcna246770)、[Forbes: How Anthropic And Claude For Nonprofits Are Putting AI In The Hands Of Changemakers](https://www.forbes.com/sites/afdhelaziz/2025/12/02/how-anthropic-and-claude-for-nonprofits-is-putting-ai-in-the-hands-of-changemakers/)、[NonprofitPro: 2025 AI Benchmark Report](https://www.nonprofitpro.com/article/2025-ai-benchmark-report-how-artificial-intelligence-is-changing-the-nonprofit-sector/)、[Mixflow: Generative AI in 2026 - Grant Writing and Donor Engagement](https://mixflow.ai/blog/generative-ai-in-2026-revolutionizing-grant-writing-and-donor-engagement-for-non-profits/)、[Yahoo!ニュース/時事通信: 生成AI、被災地照らす 避難者自ら情報掲示板開発](https://news.yahoo.co.jp/articles/0bd9405236b3b9483a0cfa7b522e0981dbefa868)、[AICU: 令和8年熊本地震 災害支援のAIインフラを無償提供](https://corp.aicu.ai/ja/kumamoto260728)、[リスク対策.com: 生成AI、被災地照らす=避難者自ら情報掲示板開発-偽映像も、浮かぶ功罪・熊本](https://www.risktaisaku.com/articles/-/114226)

### 2026-07-18: 初版執筆
- **内容**: NPO・非営利団体における生成AI活用として、助成金申請書作成(TechSoup×Microsoft 365 Copilotの事例)、ファンドレイジング・広報、多言語相談対応、議事録・事務処理の4領域を整理。Google/Microsoft/Claude/OpenAIの非営利団体向け割引プログラムと、受益者の個人情報取り扱いにおける注意点を明示
- **出典**: [AI PICKS: NPO AIで何ができる?社団法人の実務7用途と注意点](https://aipicks.jp/mag/npo-ai-guide-2026)、[TechSoup: Case Study - Nonprofits Leveraging Microsoft 365 Copilot for Impact](https://blog.techsoup.org/en-us/posts/case-study-nonprofits-leveraging-microsoft-365-copilot-for-impact)、[AI PICKS: NPO向けAIツール7選](https://aipicks.jp/mag/npo-guide-2026)、[DevelopersIO: 非営利組織のためのAI活用ラボ第2回](https://dev.classmethod.jp/articles/nonprofit-ai-lab-02-generative-ai-use-cases-for-nonprofits/)
