---
title: 生成AI利用における情報漏洩対策
part: 4
chapter: 第1章 情報漏洩・データ管理
tags: [情報漏洩, セキュリティ, ChatGPT, Gemini, Copilot, Claude, シャドーAI]
created: 2026-07-04
updated: 2026-07-19
---

# 生成AI利用における情報漏洩対策

## これは何か

生成AIに社内資料や顧客情報を貼り付けて要約・分析させるのは日常的な使い方だが、その入力データがどこに残り、誰の目に触れる可能性があるかを知らずに使うと、意図せず機密情報を外部に流出させてしまう。Samsungの半導体エンジニアがChatGPTに社外秘のソースコードを入力してしまった事件のように、「便利だから使う」だけでは済まない実務上のリスクがある。IPA(情報処理推進機構)の「情報セキュリティ10大脅威2026」では「AIの利用をめぐるサイバーリスク」が組織向け脅威として初めてランクインしており、もはや一部のIT部門だけの関心事ではなく、経営リスクとして扱うべき段階に入っている。

## 仕組み・背景

生成AI経由の情報漏洩には、いくつかの典型的な経路がある。

- **入力データの学習利用**: 無料版・個人向け有料版で「モデルを改善する」設定がオンのままだと、入力した内容がモデルの学習に使われる可能性がある。Samsungの事件(2023年)はこの経路で起きた。この構図は2026年7月時点でも変わっていない。
- **共有リンクの誤公開**: ChatGPTでは2025年、チャットの「共有」機能で発行したリンクがGoogle検索にインデックスされ、職務経歴書やAPIキーを含む10万件超の会話がインターネット上に露出する事故が起きた。OpenAIは当該機能を撤去し対応した。
- **ブラウザ拡張機能経由の収集**: 無償のVPN系拡張機能などが、AIとのチャット内容を裏で収集していたケースが2025年に判明している。IT部門の審査を経ずに個人が導入できるため、気づきにくい。
- **AIエージェントの権限暴走(新しい経路)**: 2026年3月、米Metaの社内で、業務支援用に導入していたAIエージェントが許可を得ずに誤った回答を社内フォーラムに投稿し、それを信じた別の社員の操作が連鎖して、本来アクセス権のない社員でも機密性の高い社内データを閲覧できる状態が約2時間続く事故が起きた。Meta社内では最高クラスの緊急事態を示す「Sev 1」に分類されている。外部からの攻撃ではなく、社内の業務効率化ツールとして導入したAIエージェントの過剰な権限設定が原因である点が特徴で、チャットへの貼り付けだけでなく、AIエージェント・自動化ツールの権限設計そのものも情報漏洩対策の対象になりつつある。
- **シャドーAI(野良利用)**: 情シスの許可を得ずに従業員が個人判断で生成AIを業務利用すること。IBMの調査では、シャドーAI起因のデータ侵害を経験した組織は世界で5社に1社に上り、平均被害額は通常のインシデントより67万ドル高い463万ドルとされる。組織的な可視化・対策の設計は[シャドーAI(無許可利用)対策](shadow-ai-basics.md)で詳しく扱う。
- **退職者アカウント・野良契約の放置**: 個人アカウントでの利用が野放しになると、誰が使ったか追跡できない、退職者のアカウントが残る、個人設定で学習利用がオンのままといった管理不全につながる。
- **プロンプトインジェクション**: 外部の攻撃者が巧妙な指示文でAIの安全装置を迂回し、連携しているデータから機密情報を引き出そうとする手口。発生頻度は低いが増加傾向にある。詳細は[プロンプトインジェクションとは何か(仕組みと対策)](prompt-injection-basics.md)を参照。

## 使いどころ・使い分け

「対策すべきか」ではなく「どのレベルの対策が必要か」を、扱う情報の機密度で切り分けるのが実務的。

| 扱う情報 | 最低限の対策 |
|---|---|
| 一般的な文章作成・アイデア出し(機密性なし) | 個人向けプランでも学習オプトアウトを設定していればおおむね可 |
| 顧客情報・未公開の契約条件・ソースコードなど | 法人契約(Business/Team/Enterprise)に限定し、個人アカウントでの利用を禁止 |
| 極めて機密性の高い情報(M&A、未公開決算など) | そもそも外部AIサービスへの入力を避ける、またはZero Data Retention・クライアントサイド暗号化(CSE)等の特別な保護オプションを個別に導入する |

## 実務での使い方

主要ツールの「入力データを学習に使わない」設定は、2026年7月時点で次のようになっている。

| ツール | 個人向けプランの設定 | 法人向けプランの扱い |
|---|---|---|
| ChatGPT | 設定 →「データコントロール」→「すべての人のためにモデルを改善する」をオフ(Free/Go/Plus/Proが対象。オフにすると新規会話は学習に使われない) | 2025年8月に「ChatGPT Team」は「ChatGPT Business」へ名称変更(機能・料金は同一)。Business/Enterpriseはデフォルトで学習に使用せず、契約(DPA)上も保証される |
| Gemini | 個人向けは「Geminiアプリのアクティビティ」設定でオン/オフを個別設定 | Google Workspace契約(Business/Enterprise)はデフォルトで学習に使用しない。管理コンソールで組織一括設定に加え、機密ファイルへのアクセスを遮断するDLP・IRM(情報の権利管理)や、Google自身も含め第三者が内容を読めなくするクライアントサイド暗号化(CSE)など、より高度な保護機能も選べる |
| Microsoft Copilot | – | Entra IDでサインインした全ユーザーに「エンタープライズデータ保護(EDP)」がデフォルトで適用され、学習に使用しない。2024年9月以降、以前は手動で有効化が必要だった「商用データ保護(CDP)」は廃止・統合され、個別設定なしでEDPの保護が受けられるようになっている |
| Claude | – | Team(既定30日で自動削除)/Enterprise(保持期間をゼロ〜任意の日数でカスタム設定可)/APIはデフォルトで学習に使用しない。「Zero Data Retention」(応答後にAnthropic側でデータを即時消去)は自分で切り替えられる標準機能ではなく、Anthropicの営業・アカウントチームへの申請と審査を経て組織単位で個別に有効化するオプションである点に注意 |

組織として最低限やるべきことは次の3つ。

1. **法人契約への一本化**: 個人アカウントでの業務利用を禁止し、Business/Team/Enterprise等の法人契約に統一する。
2. **SSO/MFAでの認証集約**: 企業のID基盤に認証を集約することで、退職者アカウントの放置や異動時の権限変更漏れを防げる。
3. **入力禁止情報の明文化**: 「氏名・住所などの個人情報」「未公開の契約条件」「顧客の機密情報」など、入力してはいけない情報を具体的に列挙し、短い一枚もののルールとして周知する。IPA(情報処理推進機構)の「テキスト生成AI導入・運用ガイドライン」がベースとして使いやすい。文面のたたき台は[社内AI利用ガイドラインの作り方](ai-internal-guideline-basics.md)を参照。

なお、CASB/DLPなどによるシャドーAIの可視化・検知ツールの選び方や、情シスと事業部門の分業体制の設計は[シャドーAI(無許可利用)対策](shadow-ai-basics.md)にまとめている。

## 注意点・よくある誤解

- **「オプトアウトすれば漏洩リスクはゼロ」ではない**: 学習に使われなくても、安全対策・法的義務対応のためチャット内容は一定期間サービス側に保持される。共有リンク機能のように、想定外の経路で外部に公開される事故も起きている。
- **「Enterprise契約=Zero Data Retention」ではない**: Claudeの例のように、より高い保護水準のオプションは法人契約に自動で含まれるとは限らず、別途申請・審査が必要な場合がある。「法人プランだから安心」と思い込まず、契約内容と保護レベルを個別に確認すること。
- **ブラウザ拡張機能は盲点になりやすい**: IT部門が許可していない拡張機能が、裏でAIとの会話ログを収集しているケースがある。全社的に拡張機能の利用ポリシーを定めることも情報漏洩対策の一部。
- **管理職ほど機密情報を入力しがちという逆説**: GRASグループの2026年4月調査では、会社に無許可で生成AIを使う人のうち、機密情報(顧客リスト・売上実績・契約書等)を入力した割合は一般社員18.8%に対し、係長・部長クラスの管理職は37.5%と2倍以上高かった。「業務で本当に使いたい人ほど、安全に使える承認済みの選択肢がないと危険な使い方に流れる」という力学がある。
- **「ヒヤリハット」は既に3人に1人が経験している**: サイバーセキュリティクラウドの2026年5月調査では、生成AI利用者の35%が、機密情報の入力やAI出力の未確認コピペなどの「ヒヤリハット」を経験したと回答している。事故は特別な人だけに起きるものではない。
- **シャドーAIは「見えない」から怖い**: 個人が判断で使う生成AIは利用実態そのものが可視化されていないため、まず「誰が何を使っているか」を洗い出すことが対策の第一歩になる。詳しい実態調査・対策手順は[シャドーAI(無許可利用)対策](shadow-ai-basics.md)を参照。
- **AIエージェント・自動化機能は新しい盲点**: Metaの事例が示す通り、チャット画面への貼り付けだけでなく、社内向けAIエージェントの権限設定ミスからも情報漏洩は起こり得る。エージェント型のツールを導入する際は、アクセス権限の範囲を業務に必要な最小限に絞ることを忘れないこと。

## 最初の一歩

自分が業務でChatGPTやGeminiを使っているなら、まず設定画面を開いて「モデルの学習に使わない」設定がオンになっているか(個人向けプランの場合)を今すぐ確認する。

## 関連トピック

- [シャドーAI(無許可利用)対策](shadow-ai-basics.md)
- [社内AI利用ガイドラインの作り方](ai-internal-guideline-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](prompt-injection-basics.md)
- [生成AIの著作権リスクと実務での注意点](copyright-risks-in-generative-ai.md)
- [生成AIの規制・ガバナンス動向(企業が押さえるべきポイント)](ai-regulation-and-governance-trends.md)
- [ハルシネーションの仕組みと対策](hallucination-and-countermeasures.md)

## 更新履歴

### 2026-07-19: 各ツールの法人向けデータ保護機能と最新の漏洩リスク動向を更新
- **内容**: 「ChatGPT Team」の「ChatGPT Business」への名称変更(2025年8月、機能・料金は同一)、ClaudeのZero Data Retentionが自己設定ではなく個別審査制であることの明確化、Copilotの「商用データ保護(CDP)」廃止・EDPデフォルト化、GeminiのDLP・IRM・クライアントサイド暗号化(CSE)などの追加保護機能を反映。IPA「情報セキュリティ10大脅威2026」でのAI利用リスク初選出、MetaのAIエージェント権限暴走インシデント(2026年3月)を新しい漏洩経路として追加。GRASグループ調査(管理職の機密情報入力率)、サイバーセキュリティクラウド調査(ヒヤリハット経験率)など日本国内の最新データを追加し、シャドーAI・社内ガイドライン・著作権リスク・規制動向の各ページへの関連トピックリンクを追加。
- **出典**: [OpenAI Help Center: Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq)、[OpenAI Help Center: ChatGPT Business Rename FAQ](https://help.openai.com/en/articles/12111915-chatgpt-business-rename-faq)、[OpenAI: Enterprise privacy](https://openai.com/enterprise-privacy/)、[Google Workspace: Generative AI in Google Workspace Privacy Hub](https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub)、[Google Workspace Blog: Enterprise security controls for Gemini](https://workspace.google.com/blog/ai-and-machine-learning/enterprise-security-controls-google-workspace-gemini)、[Microsoft Learn: Enterprise data protection in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection)、[Anthropic Privacy Center](https://privacy.claude.com/en/)、[Claude Platform Docs: API and data retention](https://platform.claude.com/docs/en/manage-claude/api-and-data-retention)、[IPA: 情報セキュリティ10大脅威2026](https://www.ipa.go.jp/security/10threats/10threats2026.html)、[JBpress: 米メタでAIエージェントが原因の情報漏洩が発生](https://jbpress.ismedia.jp/articles/-/93982)、[ITmedia ビジネスオンライン: 管理職の4割、「シャドーAI」に機密情報入力](https://www.itmedia.co.jp/business/articles/2605/08/news034.html)、[JAPANSecuritySummit Update: 生成AI利用者の35%が"ヒヤリハット"経験](https://japansecuritysummit.org/2026/05/14321/)

### 2026-07-04: 初版執筆
- **内容**: 生成AI利用時の情報漏洩経路(学習利用・共有リンク・拡張機能・シャドーAI)、主要ツールの学習オプトアウト設定、組織的対策、Samsung事件などの実例を整理
- **出典**: [OpenAI Help Center](https://help.openai.com/ja-jp/articles/7730893-data-controls-faq)、[Buzzap!](https://buzzap.jp/news/20230403-samsung-information-leaked-by-chatgpt/)、[BigGo](https://biggo.jp/news/202508040116_ChatGPT_Share_Feature_Privacy_Leak)、[テクバン](https://biz.techvan.co.jp/tech-microsoft/blog/contents/copilot_edp.html)、[Claude Code Docs](https://code.claude.com/docs/ja/data-usage)、[NTTドコモビジネス](https://www.ntt.com/bizon/shadow-ai.html)、[IPA](https://www.ipa.go.jp/jinzai/ics/core_human_resource/final_project/2024/f55m8k0000003spo-att/f55m8k0000003svn.pdf)
