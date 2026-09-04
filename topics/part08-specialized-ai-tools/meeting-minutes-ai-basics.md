---
title: "議事録・文字起こしAIの基本(Notta・Rimo・tl;dv等)"
part: 8
chapter: 第6章 会議・議事録AI
tags: [議事録AI, 文字起こし, Notta, Rimo, tl;dv, Otter.ai, Fireflies.ai, Teams Copilot, Google Meet, Zoom AI Companion]
created: 2026-07-25
updated: 2026-08-28
---

# 議事録・文字起こしAIの基本(Notta・Rimo・tl;dv等)

## これは何か

会議のたびに「話を聞きながらメモも取る」のは、実は同時に2つの作業をこなす負荷の高い仕事だ。聞き漏らしを恐れてメモに集中すると議論に参加できず、議論に集中するとメモが雑になる。さらに会議後には、走り書きのメモを清書して参加者に配る手間もかかる。

議事録・文字起こしAI(会議の音声をリアルタイムまたは録音データから自動でテキスト化し、要約・決定事項・アクションアイテムまで整理してくれる生成AIサービス)は、この「聞く」と「書く」を分離してくれるツールである。Notta・Rimo Voice・tl;dv・Otter.ai・Fireflies.aiのような**専用ツール**を会議に参加させる方法と、Microsoft Teams(Copilot)・Google Meet(Gemini)・Zoom(AI Companion)のように**会議ツールに最初から組み込まれた機能**を使う方法の2系統があり、どちらを選ぶかで運用コスト・機能の幅・情報の扱いが変わる。本ページはこの2系統を横並びで整理し、使い分けの判断材料を示す。

## 仕組み・背景

議事録AIの基本的な処理の流れは、専用ツールでも会議ツール純正機能でもほぼ共通している。

1. 会議に「参加」する(専用ツールの多くは、カレンダー連携をもとにBot(自動参加プログラム)が会議にゲストとして入室する。純正機能は会議ソフト自体が音声を取得する)
2. 音声認識(ASR: Automatic Speech Recognition)でリアルタイムに文字起こしを行う
3. 話者分離(diarization、誰がいつ発言したかを声の特徴から自動で区別する技術)により発言者ごとに発言を割り振る
4. 文字起こし全文をもとに、生成AI(GPT系・Gemini系・独自モデルなど)が要約・決定事項・アクションアイテム(担当者・期限付きのタスク)を抽出する
5. 議事録フォーマットに整形し、ドキュメントやチャットツールへ共有する

専用ツールの多くは「録音Bot」が会議に自動参加する方式のため、Zoom・Google Meet・Microsoft Teams・Webexなど**会議ツールをまたいで同じフォーマットの議事録を蓄積できる**のが強みである。一方、会議ツール純正の機能(Teams CopilotのIntelligent Recap、Google MeetのGemini「Take notes for me」、Zoom AI Companion)は、その会議ツールの契約・データ管理の枠内で完結するため、追加のSaaS契約や「社外ツールに音声を渡す」という判断を挟まずに使える点が強みになる。

いずれの方式でも、精度を左右するのは「話者分離の精度」と「専門用語・固有名詞の認識精度」であり、多くのツールが**カスタム辞書(社名・製品名・人名などの読みと表記を事前登録して認識精度を上げる機能)**を用意している。

## 使いどころ・使い分け

### 専用ツール vs 会議ツール純正機能

| | 専用ツール(Notta・Rimo・tl;dv・Otter・Fireflies等) | 会議ツール純正機能(Teams Copilot・Google Meet Gemini・Zoom AI Companion) |
|---|---|---|
| 対応する会議ツール | Zoom/Meet/Teams/Webexなど横断対応が多い | 自社の機能が動くその会議ツールのみ |
| 議事録の一元管理 | 得意(ツールが違っても同じ形式で1か所に蓄積) | 苦手(会議ツールごとに議事録の置き場所・形式がバラバラになりやすい) |
| 追加契約・情報の持ち出し | 社外SaaSへ音声・文字起こしを渡すことになる | 既存契約(Microsoft 365・Google Workspace・Zoom)の範囲内で完結しやすい |
| 専用機能の豊富さ | カスタム辞書・CRM連携・検索ライブラリ・クリップ生成など専用機能が豊富 | 会議ツールの標準機能に限定されることが多い |
| 導入のしやすさ | 無料/低価格プランで個人がすぐ試せる | 上位ライセンス(Microsoft 365 Copilot、Google Workspace Business Standard/Plus以上のGemini機能等)が前提のことが多い |
| セキュリティ・情報漏洩の論点 | 社外ボットの会議参加・音声アップロードへの社内承認が要る | 既存のセキュリティ・データ保持ポリシーを流用しやすい |

判断の目安は次の通り。

- **会議ツールが社内で1つに統一されており、対象の純正AI機能(Copilot/Gemini/AI Companion)のライセンスを既に契約している** → まず純正機能で十分か試す。追加コストとツール数を増やさずに済む
- **Zoom・Teams・Google Meetなど複数の会議ツールが混在し、議事録を横断で一元管理・検索したい** → 専用ツールが向く
- **カスタム議事録テンプレート、CRM連携、複数言語混在の会議、無料で試したい** → 専用ツール(特にtl;dv・Fireflies.aiは無料枠が手厚い)
- **人事評価・M&A・契約交渉など機密度が特に高い会議** → 社外ツールへの音声アップロードを避け、純正機能または録音なしの手動メモに切り替える(後述の注意点参照)

### 専用ツール5社比較(2026年8月時点の目安)

| ツール | 開発元 | 料金目安(月額、個人向け) | 対応言語 | 特徴 | 議事録フォーマット | 連携先 |
|---|---|---|---|---|---|---|
| **Notta** | Notta株式会社(日本) | Free ¥0/Premium 月1,980円(年払い月1,185円)/Business 月4,180円(年払い月2,508円)/Enterprise 要問合せ | 58言語 | 日本語精度に定評、カスタム辞書(Premium最大200語・Business最大1,000語) | 要約+話者別文字起こし | Zoom/Google Meet/Teams/Webexに自動参加 |
| **Rimo Voice** | Rimo合同会社(日本) | 文字起こしプラン 月1,650円(年払い月1,100円)/プロ(AI議事録)プラン 月4,950円(年払い月3,300円) | 日本語特化(多言語対応も一部あり) | 国産で日本語会議に強い、録画Bot・会議AIアシスタント | AI議事録(要約・論点整理) | Zoom/Google Meet/Teams |
| **tl;dv** | tl;dv(海外) | Free ¥0(AI要約は生涯10回まで、録音・文字起こしは無制限だが3か月で自動削除)/Pro 年払い$18・月払い$22(1ユーザー)/Business 年払い$59・月払い$98(1ユーザー、40%OFFの年払いキャンペーンが継続中) | 30言語以上 | カスタムAIプロンプト・要約テンプレート、営業向けCRM連携が強い | 要約・クリップ・アクションアイテム | Zoom/Google Meet/Teams、Salesforce・HubSpot等CRM |
| **Otter.ai** | Otter.ai(海外) | Basic ¥0(月300分、1会議30分まで)/Pro 年払い$8.33・月払い$16.99(月1,200分、1会議90分まで)/Business 年払い$19.99・月払い$30(会議は無制限・1会議4時間まで+取込6,000分/人) | 主に英語が強み、日本語は精度に留意 | 共有カスタム用語集、話者タグ付け、アクションアイテムの担当者割当 | 要約+全文文字起こし | Zoom/Google Meet/Teams |
| **Fireflies.ai** | Fireflies.ai(海外) | Free $0/Pro 年払い$10・月払い$18/Business 年払い$19・月払い$29/Enterprise 年払い$39(要問合せ、すべて1ユーザー) | 100以上の言語 | 文字起こし・AI要約自体はプランを問わず無制限だが、**録音の保存容量には上限があり**Freeはチーム全体で約400分・Proは1人あたり8,000分(Business/Enterpriseは無制限)。AIクレジット数もFree 20/Pro 20+/Business 30/Enterprise 50と差がある。Perplexity連携の会議中Web検索「Talk to Fireflies」も搭載 | 要約・アクションアイテム・会議中の箇条書きノート | Zoom/Google Meet/Teams、多数のCRM・タスク管理ツール |

料金・機能・無料枠の上限は変更が非常に頻繁である。契約前には必ず各社公式サイト([Notta料金ページ](https://www.notta.ai/pricing)、[RimoVoiceプランと利用料金](https://guide.rimo.app/ja/articles/8885029-%E3%83%97%E3%83%A9%E3%83%B3%E3%81%A8%E5%88%A9%E7%94%A8%E6%96%99%E9%87%91)、[tl;dv Pricing](https://tldv.io/pricing/)、[Otter.ai Pricing](https://otter.ai/pricing)、[Fireflies.ai Pricing](https://fireflies.ai/pricing))で最新の数値を確認すること。

### 会議ツール純正の議事録機能

| | Microsoft Teams(Copilot) | Google Meet(Gemini) | Zoom(AI Companion) |
|---|---|---|---|
| 機能名 | Copilot「Intelligent Recap」(音声のみで生成する「Audio Recap」も2026年6月にGA) | 「Take notes for me」 | AI Companion 2.0の会議要約 |
| 前提ライセンス | Microsoft 365 Copilotライセンス+管理者の利用許可 | 2025年1月以降、Gemini機能はBusiness Standard/Plus・Enterprise等の有料Workspaceプランに標準搭載(単体アドオンは廃止)。Business Standard/Plusはデフォルトでオン、Enterprise系はデフォルトオフで管理者が有効化。個人向けGoogle AI Pro/Ultraでも利用可 | Zoom Workplace有料プラン(Basicは対象外) |
| 出力形式 | 論点別に整理されたMarkdown要約、決定事項・アクションアイテム | Googleドキュメントとして自動保存、要約とアクションアイテムをメール通知(2026年4月以降、要約・決定事項・次のステップ・詳細のセクションを個別にオン/オフ可能) | 要点・決定事項・アクションアイテムの要約、画面共有中の文字・図表もAIが認識(Visual Intelligence/OCR) |
| 日本語対応 | Intelligent Recap(テキスト要約)は日本語含む20言語以上に対応、音声で聞ける「Audio Recap」も2026年3月に日本語含む8言語へ拡大 | 日本語を含む8言語に対応(1回の会議で使えるのは1言語のみ) | 対応 |
| 参加者への告知 | 文字起こし開始が会議内に表示される(文字起こし・録音なしでも要約だけ生成する設定も選択可) | 開始時に全参加者へ通知、許可が必要 | 録音・要約開始が会議内に表示される |
| 新機能 | 録音・文字起こしを保存せず音声のみから要約する設定(コンプライアンス要件向け) | 2026年8月からAndroid/Web/iOSで対面(オンライン接続なし)の会議・打ち合わせもマイクで拾ってメモ生成する機能をロールアウト中 | サイドパネルのAIアシスタントで過去の会議・タスクを横断検索できる機能を追加 |

## 実務での使い方

### 想定シーン

- 週次定例・1on1・商談など日々の会議の議事録を、参加者全員分作らずに自動化する
- 出張中・多言語が混じる会議で、リアルタイム字幕や翻訳付き文字起こしを使う
- 決定事項・アクションアイテムを会議直後にチャットやタスク管理ツールへ自動連携する
- 過去の会議内容を「あのときの発言」までさかのぼって検索する

### 導入手順(画面の場所)

**Notta**
1. notta.ai でアカウント登録し、Googleカレンダー・Outlookカレンダーと連携する
2. 「設定」→「自動参加」で、Zoom/Google Meet/Teams/Webexの会議にBotを自動参加させる設定をオンにする
3. 「設定」→「カスタム辞書」(または単語登録)で、社名・製品名・人名などの読みと表記を事前登録する

**tl;dv**
1. tldv.io でサインアップし、Chrome拡張機能を追加するか、Zoom/Google Meet/Teamsの各アプリ連携を有効化する
2. 次回以降の会議にBotが自動参加し、終了後に要約・クリップ・アクションアイテムがダッシュボードに生成される
3. 「Templates」から議事録テンプレートを選択・カスタマイズし、以降の会議に自動適用する

**Microsoft Teams(Copilot)**
1. 会議を開始し、上部メニューの「Copilot」ボタンをクリックしてCopilotパネルを開く
2. 会議コントロールバーの「その他(…)」→「文字起こしを開始」をオンにする(Intelligent Recapの生成にはこの文字起こしが必須)
3. 会議終了後、Copilotの「Recap」タブ(会議詳細画面)から要約・論点別Markdown・アクションアイテムを確認する

**Google Meet(Gemini)**
1. 会議参加前の画面で「Geminiでメモを作成」をクリックするか、会議中に右上のペンマークから「メモの作成を開始」を選ぶ
2. メモを取る言語を選択する(日本語を含む8言語に対応。1回の会議で使えるのは1言語のみ)
3. 会議中に「要約」「決定事項」「次のステップ」「詳細」のどのセクションを生成するかをオン/オフで選べる
4. 会議終了後、自動生成されたGoogleドキュメントがGoogle Driveに保存され、要約とアクションアイテムがメールで通知される

**Zoom(AI Companion)**
1. 個人利用の場合は会議コントロールバーの「AI Companion」アイコンから「ミーティングの要約」を有効化する
2. 組織全体で有効化する場合は、管理者がZoom Web Portalの「設定」→「AI Companion」から機能を有効化する
3. 会議終了後、Zoom Webポータルの「レコーディング」または「AI Companion」タブから要約・文字起こしを確認する

### コピペで使える議事録フォーマット例

```
# 会議名:
# 日時:
# 参加者:

## 決定事項
- (何を決めたか。誰の承認かも明記)

## アクションアイテム
- [ ] タスク内容 (担当: 、期限: )

## 主な議論点
- (論点ごとに1〜2行で要約)

## 次回アジェンダ
- (積み残し事項・次回までに準備すること)
```

### コピペで使える要約プロンプト例(文字起こし全文を貼った上で)

```
以下は社内会議の文字起こし全文です。次の形式で議事録にまとめてください。

1. 決定事項(誰が決めたかも明記)
2. アクションアイテム(担当者・期限が本文中にあれば必ず反映。無ければ「未定」と明記)
3. 主な議論点(結論だけでなく、賛否が分かれた論点も残す)
4. 次回までの積み残し事項

固有名詞・数値は文字起こし原文の表記をそのまま使い、意味を変えるような要約はしないでください。
```

### ツール横断の対応付け

| 概念 | Notta / Rimo / tl;dv / Otter / Fireflies | Teams | Google Meet | Zoom |
|---|---|---|---|---|
| 会議への参加方法 | 録音Bot(カレンダー連携で自動参加) | 会議アプリ自体が音声取得 | 会議アプリ自体が音声取得 | 会議アプリ自体が音声取得 |
| 議事録AI機能の名称 | AI議事録・AIサマリー等 | Copilot「Intelligent Recap」 | Gemini「Take notes for me」 | AI Companionの会議要約 |
| 話者分離 | 標準搭載(精度はツールにより差) | 標準搭載 | 標準搭載 | 標準搭載 |
| カスタム辞書・用語登録 | Notta・Otterなどで搭載 | Microsoft 365全体の用語辞書に依存 | 明確な同等機能は薄い | 明確な同等機能は薄い |
| CRM・タスク管理連携 | tl;dv・Fireflies.aiが強い | Microsoft 365内の各アプリと連携 | Google Workspace内で完結 | Zoom Team Chat等と連携 |

## 注意点・よくある誤解

- **話者分離は万能ではない**: 参加人数が多い、声質が似ている、複数人が同時に話す場面では話者の取り違えが起きる。重要な議事録は、誰の発言かを人の目で最終確認する
- **専門用語・固有名詞はそのままでは精度が落ちる**: 社名・製品名・業界用語は辞書登録機能(Nottaは最大200〜1,000語、Otterは共有用語集など)に事前登録しておくと認識精度が上がる。何も設定せずに使うと誤変換が積み重なりやすい
- **AI要約への丸投げはアンチパターン**: テンプレートを何もカスタマイズせずに使うと、決定事項とアクションアイテムがぼやけた抽象的な要約になりがちである。「担当者・期限を明記させる」「賛否が分かれた論点も残す」など、プロンプトやテンプレートで明示的に指示する
- **無料プランの制限に注意**: 無料プランは録音時間・月間分数・AI要約の回数(tl;dvは生涯10回など)に上限があることが多く、日常的な業務利用では有料プランへの切り替えが前提になる場合が多い
- **セール価格・料金改定が頻繁**: 議事録AI各社は料金体系の変更やキャンペーン価格(期間限定の年払い割引など)が非常に多い。契約前に必ず公式サイトの最新表示を確認する
- **情報漏洩リスクへの配慮**: 専用ツールの多くは録音Botが会議に参加し、音声・文字起こしデータを社外のSaaS事業者のサーバーにアップロードする。人事評価・M&A・契約交渉など機密度の高い会議では、社内承認済みのツールに限定するか、そもそも録音・自動議事録化を避ける判断も必要になる。また会議参加者への事前告知(録音Bot参加への同意)を忘れないこと。詳しくは[情報漏洩防止の基本](../part04-risk-security/information-leakage-prevention.md)を参照
- **純正機能はライセンス前提**: Teams CopilotのIntelligent Recapは引き続きMicrosoft 365 Copilotライセンスが前提。Google Meetの「Take notes for me」は2025年1月のGemini機能バンドル化以降、Business Standard/Plus等の有料Workspaceプランに標準搭載されたが、「Teams/Meetを使っているから無料で使える」わけではない点に注意する(Enterprise系プランはデフォルトオフで管理者の有効化が必要)
- **「無制限」の表記は文字起こし・要約の話で、保存容量には別の上限があることが多い**: Fireflies.aiは全プランで文字起こし・AI要約自体は無制限だが、録音の保存容量(Freeはチーム全体で約400分など)は別枠で管理されている。「無制限プラン」と見て安心せず、ストレージ・クレジットなど複数の上限を確認する

## 最初の一歩

次回の社内定例会議で、Teams・Google Meet・Zoomのいずれかの純正議事録機能(Copilot Intelligent Recap / Take notes for me / AI Companion)を1回オンにしてみる。会議後に生成された要約とアクションアイテムを見て、自分が手書きでメモした場合と比べて過不足がないかを確認する。

## 関連トピック

- [特化型AIツールの選び方(用途別マップと比較)](specialized-ai-tools-selection-guide.md)
- [生成AIによる文章作成・校正の実務活用](../part12-business-practice/ai-writing-and-editing.md)
- [役員秘書・エグゼクティブアシスタント業務でのAI活用事例](../part15-job-role-cases/executive-assistant-ai-use-cases.md)
- [情報漏洩防止の基本](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-08-28: 料金プラン・機能を最新化
- **内容**: Notta・Rimo Voice・Otter.aiの料金・無料枠は2026年8月時点でも変更なしと確認。tl;dvはBusinessプランの月払い価格($98)と無料プランの3か月自動削除仕様を追記。Fireflies.aiは「全プラン無制限」の表記に加え、録音の保存容量(Free約400分/チーム、Pro 8,000分/人など)とAIクレジット数の差を追記。会議ツール純正機能は、Teams CopilotのIntelligent Recap対応言語が20言語以上に拡大し音声のみで生成する「Audio Recap」(2026年3月に8言語へ拡大、6月GA)、Google MeetはGemini機能が2025年1月にBusiness Standard/Plus等へ標準バンドル化されたためライセンス前提の記述を修正し、要約セクションの個別オン/オフ(2026年4月)・対面会議向けメモ生成(2026年8月ロールアウト中)を追記、Zoom AI Companionは2.0への機能拡張(画面内容の認識・サイドパネルAIアシスタント)を追記
- **出典**: [Fireflies Pricing 2026: Which Plan Is Right for You? | Fireflies.ai](https://fireflies.ai/blog/fireflies-pricing-which-plan-is-right-for-you/)、[What's included in the Fireflies Free plan | Fireflies Knowledge Base](https://guide.fireflies.ai/articles/4027724828-learn-about-the-fireflies-free-plan)、[tl;dv Pricing 2026: Costs, Plans & Hidden Limits | Claap](https://www.claap.io/blog/tl-dv-pricing)、[What are the limits of the Free plan? | tl;dv Help Center](https://intercom.help/tldv/en/articles/8919450-what-are-the-limits-of-the-free-plan)、[Otter AI Pricing 2026 | Claap](https://www.claap.io/blog/otter-pricing)、[Nottaの料金プラン比較｜Smarf](https://smarf.jp/article/20609/)、[Rimo Voice 料金プラン | Rimo](https://rimo.app/about/voice/plans)、[Microsoft 365 Copilot: Audio recap language expansion in Microsoft Teams | M365 Admin](https://m365admin.handsontek.net/microsoft-365-copilot-audio-recap-language-expansion-microsoft-teams/)、[Microsoft Teams: AI meeting recap without transcript to meet compliance policies | M365 Admin](https://m365admin.handsontek.net/microsoft-teams-ai-meeting-recap-without-transcript-meet-compliance-policies/)、[Gemini for Google Workspace Pricing: 2026 Guide | Redress Compliance](https://redresscompliance.com/gemini-google-workspace-licensing-whats-included)、[Google Meet Now Takes Notes at In-Person Meetings with Gemini](https://pasqualepillitteri.it/en/news/11419/google-meet-take-notes-in-person-meetings)、[Google Meet rolling out 'Take Notes' for in-person meetings | 9to5Google](https://9to5google.com/2026/08/13/google-meet-take-notes-in-person/)、[Zoom AI Companion 2.0: New Features | USC Information Technology Services](https://itservices.usc.edu/2026/03/31/zoom-ai-companion-2-0-new-features-to-enhance-your-meetings-classes/)
- **注記**: この実行環境ではネットワークegressプロキシにより外部サイトへの直接アクセス(WebFetch)がすべて遮断されており、各社公式ページへの再アクセスは試みたが実施できなかった。検索エンジンのスニペットと、公式ブログ・ヘルプセンター記事を含む複数の第三者記事の突き合わせに基づく記述である点は前回更新時と同様。料金・無料枠・保存容量の上限は変更が非常に頻繁なため目安とし、契約前には必ず公式サイトで最新値を確認すること

### 2026-07-25: 初版執筆
- **内容**: 議事録・文字起こしAIを「専用ツール(Notta・Rimo Voice・tl;dv・Otter.ai・Fireflies.ai)」と「会議ツール純正機能(Teams Copilot・Google Meet Gemini・Zoom AI Companion)」の2系統に整理し、料金・対応言語・話者分離・辞書登録・連携先を横並び比較。導入手順(画面の場所)、コピペ用議事録フォーマット・要約プロンプト、情報漏洩リスクへの注意点を整理
- **出典**: [Notta料金プラン | Notta](https://www.notta.ai/pricing)、[Notta料金プラン比較2026 | アプリの達人](https://app-tatsujin.com/notta-pricing-plans-2026/)、[【2026年最新】Nottaの料金プランと月額は？ | AI文字起こしツールガイド](https://ai-transcription-guide.jp/notta-price-plan/)、[単語登録 | Nottaヘルプセンター](https://support.notta.ai/hc/ja/articles/18639361055003-%E5%8D%98%E8%AA%9E%E7%99%BB%E9%8C%B2)、[プランと利用料金 | RimoVoice Help Center](https://guide.rimo.app/ja/articles/8885029-%E3%83%97%E3%83%A9%E3%83%B3%E3%81%A8%E5%88%A9%E7%94%A8%E6%96%99%E9%87%91)、[Rimo Voiceの料金・機能・導入事例 | BOXIL](https://boxil.jp/service/8125/)、[AI議事録「Rimo Voice」、月額1,500円からの個人向け定額プランを提供開始 | PR TIMES](https://prtimes.jp/main/html/rd/p/000000033.000064239.html)、[tl;dv Pricing 2026 | Claap](https://www.claap.io/blog/tl-dv-pricing)、[tl;dv Pricing](https://tldv.io/pricing/)、[Otter AI Pricing 2026 | Claap](https://www.claap.io/blog/otter-pricing)、[Otter.ai Pricing](https://otter.ai/pricing)、[Fireflies.ai Pricing 2026 | Claap](https://www.claap.io/blog/fireflies-pricing)、[Fireflies Pricing 2026: Which Plan Is Right for You? | Fireflies.ai](https://fireflies.ai/blog/fireflies-pricing-which-plan-is-right-for-you/)、[Copilotの議事録作成 | Otolio](https://www.smartshoki.com/blog/gijirokusakusei/use-copilot/)、[Google Meet、Geminiで「自動メモ生成」が日本語対応 | Impress Watch](https://www.watch.impress.co.jp/docs/news/1670106.html)、[Google MeetのAI文字起こし＆議事録機能「Take notes for me」を実際に試してみた | 左右公認会計士税理士事務所](https://cpasayu.com/blog/2025/11/19/google-meet%E3%81%AEai%E6%96%87%E5%AD%97%E8%B5%B7%E3%81%93%E3%81%97%EF%BC%86%E8%AD%B0%E4%BA%8B%E9%8C%B2%E6%A9%9F%E8%83%BD%E3%80%8Ctake-notes-for-me%E3%80%8D%E3%82%92%E5%AE%9F%E9%9A%9B%E3%81%AB/)、[Zoom AI Companion完全ガイド【2026年版】 | Felo字幕ブログ](https://subtitles.felo.me/ja/blog/zoom-ai-companion)、[Zoomの議事録を自動作成する方法は？ | マネーフォワード クラウド](https://biz.moneyforward.com/work-efficiency/basic/14136/)
- **注記**: Notta・Rimo Voice・tl;dv・Fireflies.aiの各公式ページの一部は本セッションから直接アクセスできず(403エラー)、検索エンジンのスニペットと複数の第三者記事(比較サイト・レビューサイトを含む)の突き合わせに基づく記述を含む。料金・無料枠の上限は各社とも変更が非常に頻繁なため目安とし、契約前には必ず公式サイトで最新値を確認すること
