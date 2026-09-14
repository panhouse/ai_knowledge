---
title: Microsoft Copilot Studioによるカスタムエージェント作成の基本
part: 6
chapter: 第2章 主要ツールでの作り方
tags: [Copilot Studio, Microsoft 365 Copilot, エージェントビルダー, Microsoft, カスタムAI]
created: 2026-07-06
updated: 2026-09-09
---

# Microsoft Copilot Studioによるカスタムエージェント作成の基本

## これは何か

「総務への問い合わせが同じ質問ばかりで対応が追いつかない」「社内規程集はSharePointにあるのに、みんな探さずに担当者に聞いてしまう」——こうした業務は、Microsoft 365環境専用のカスタムAI(エージェント)を1つ作れば、多くを自動応答に移せる。**Copilot Studio**は、指示(プロンプト)・知識源(SharePoint/OneDriveなどの社内データ)・実行アクションを組み合わせて、Teams・SharePoint・Webサイトなど複数のチャネルに配布できる本格的なノーコード開発環境である。Microsoft 365 Copilotアプリの中には、その簡易版にあたる「**エージェントビルダー**」も内蔵されており、目的に応じてどちらを使うかを選ぶことになる。

## 仕組み・背景

MicrosoftのAIエージェント構築手段は、機能の重さで2段階に分かれている。

- **エージェントビルダー**: Microsoft 365 Copilotアプリ(Copilot Chat)に内蔵された軽量版。自然言語で「何をしてほしいか」を伝えると、AIが指示文・知識源・推奨プロンプトを自動生成する。Microsoft Graph(社内のメール・ファイル・Teams会話などの情報基盤)を前提に動き、Microsoft 365のセキュリティ・コンプライアンス設定をそのまま引き継ぐ。個人〜小規模チーム向けの「かんたん版」という位置づけ
- **Copilot Studio**: Power Platform(Microsoftのノーコード開発基盤)上に構築された本格的な開発環境。指示・知識源に加えて、複数ステップの処理(トピック・フロー)、1,400以上のコネクタを使った外部システム連携(CRM・ERP・チケット管理システムなど)、Teams/SharePoint/Webサイト/Slackなど複数チャネルへの配布、社外の非ライセンスユーザーへの公開まで対応する

両者は完全に別物ではなく、エージェントビルダーで作った試作を「Copilot Studioにコピー」して、後から高度な機能へ拡張する移行パスが用意されている(Microsoft Learn: Choose between Agent Builder and Copilot Studio)。

2026年7月7日、MicrosoftはCopilot Studioを土台から作り直す「リビルド」を世界向けに正式提供(GA)した。個別のトピック・フローを積み上げる従来の設計から、新しい「エージェント型オーケストレーター」が複数ステップの複雑な作業を自動的に組み立てる方式へ移行し、構造化されたステップとエージェント的な判断を1つのキャンバス上で組み合わせられる「ワークフローデザイナー」も2026年8月3日にGAした。設定タブは9個から4個に整理され、指示や知識源をMarkdown形式の再利用可能な部品として扱う「Skills」、エージェントビルダーで作ったエージェントを社内向けの「エージェントストア」に申請・公開する仕組みも加わっている。Microsoft社内の検証では、新オーケストレーターへの刷新で応答品質(評価スコア)が約20%向上し、消費トークン量は半減したと報告されている(2026年9月時点でも全テナントへのロールアウトが継続中)。

料金の単位も2025年9月に変わった。以前は「メッセージ」単位の課金だったが、現在は**Copilotクレジット**という単位に統一され、応答の種類ごとに消費量が異なる仕組みになっている(詳細は後述)。

## 使いどころ・使い分け

| 場面 | 向いている機能 |
|---|---|
| 自分や数人の小さなチームだけで使う簡単なFAQボットをすぐ作りたい | エージェントビルダー |
| SharePoint/OneDriveの文書検索に特化したQ&Aボットを最短で作りたい | エージェントビルダー(知識源にSharePoint/OneDriveを指定するだけで完結) |
| 部門・全社・社外の顧客向けに配布したい | Copilot Studio |
| CRM/ERPからデータを取得したり、チケット起票・承認フロー・他部署への振り分けなど複数ステップの処理をさせたい | Copilot Studio(トピック・アクション・コネクタ) |
| 将来的に本格運用へ育てたい試作をまず軽く作りたい | エージェントビルダーで作成→必要になった時点でCopilot Studioへコピーして拡張 |
| ライセンスを持たない社外ユーザーにも使わせたい | Copilot Studio(スタンドアロンライセンスでの公開が前提) |

## 実務での使い方

### アクセス方法

- **エージェントビルダー**: 2026年8月以降、個人向けCopilotアプリと業務向けMicrosoft 365 Copilotアプリが「Microsoft Copilot」アプリ1つに統合され、Webアドレスも順次 copilot.cloud.microsoft に一本化されている(旧URLのm365.cloud.microsoftからは自動リダイレクト。ロールアウトは2026年8月中旬〜9月にかけて段階的で、Windows/Mac版アプリへの反映は9月中旬から)。個人アカウントと勤務先アカウントを間違えないよう、背景色の違いやナビゲーションの「Work」ラベルで見分けられるようになった。同アプリ(またはTeams内のCopilotアプリ)の左ペインで「エージェント」→「+新しいエージェント」を開く。SharePointサイトの「エージェントを作成」ボタンからも同じビルダーを呼び出せる
- **Copilot Studio**: copilotstudio.microsoft.com に勤務先アカウントでサインインし、左メニュー「エージェント」→「+作成」→「新しいエージェント」

### 作成手順(共通の流れ・2026年9月時点の目安)

1. エージェントにしてほしいことを自然言語で1〜2文(最大1,024文字程度)入力すると、AIが名前・説明・指示(手順)を自動生成する
2. 「構成」タブを開き、指示・知識・機能を手動で調整する
3. 「知識を追加」からソースの種類(SharePoint/OneDrive/アップロードファイル/公開Webサイト/Dataverseなど)を選び、対象を指定して「エージェントに追加」
4. (Copilot Studioのみ)「トピック」「アクション」「ツール」タブで、多段階の処理や外部システム連携(コネクタ)を追加する
5. 画面上部の「テスト」でテストパネルを開き、実際の応答を確認しながら指示を調整する
6. 「公開」ボタンで公開し、配布先チャネル(Teams/SharePoint/Microsoft 365 Copilot/Webサイトなど)を選択する

### 知識源として使えるものの目安(表)

| 項目 | エージェントビルダー | Copilot Studio |
|---|---|---|
| OneDriveファイル | 最大50ファイル程度 | サイト・フォルダ単位で指定可 |
| アップロードファイル(2026年8月以降「添付ファイル/Attachments」に呼称変更、機能自体は同じ) | 最大20ファイル程度 | 同様に対応 |
| SharePoint | サイト・ライブラリ単位で指定 | サイト・ライブラリ単位で指定、複数サイトの横断も可 |
| Teamsチャット | 特定チャットを最大5個程度 | – |
| 公開Webサイト | 対応 | 対応 |
| 業務システム(Dynamics 365、Salesforce、ServiceNowなど) | 非対応 | Power Platformのコネクタ(1,400以上)経由で対応 |
| Dataverse(業務データベース) | 非対応 | 対応 |
| 全社データ(Microsoft Graphによる横断検索) | 対応(範囲は限定的) | 対応(Tenant Graph Groundingとして本格利用可) |

### コピペで使える指示欄のテンプレート例(社内問い合わせエージェント)

```
## 役割
あなたは社内の総務・人事に関する問い合わせに答える社内FAQエージェントです。

## 対応範囲
- 就業規則、福利厚生、経費精算に関する質問
- 添付の知識源(SharePoint「総務部規程集」)の内容を根拠に回答する

## 回答のルール
- 知識源に記載がない内容は、推測せず「規程集に記載がありませんので、総務部(soumu@example.com)にご確認ください」と答える
- 回答の最後に、根拠にした規程名・章番号を示す
- 個人の給与・評価など機微な内容の質問には回答せず、担当窓口の案内のみ行う
```

SharePoint文書検索特化にしたい場合は、上記の「対応範囲」を「指定したSharePointサイト内の文書検索と要約」に変え、知識源をそのサイトのライブラリ1つに絞ると、余計な情報源を参照しない絞り込み型のエージェントになる(ただし後述の通り、これは「優先」であって完全な「遮断」ではない点に注意)。

2026年8月のアップデートで、新規に作るエージェントビルダーのエージェントは既定で機能(Web検索・コード実行など)が有効な状態で作成されるようになった(以前は個別にオンにする必要があった)。従来どおり個々の機能をオフにして絞り込むことも可能。

### 公開先チャネル

Teams、SharePoint、Microsoft 365 Copilot(Copilot Chat)、公開Webサイト、Facebook、Direct Line/API経由のカスタムアプリなどに公開できる(Copilot Studio)。エージェントビルダーで作ったエージェントは、Teams・SharePoint・Microsoft 365 Copilotアプリ内という、Microsoft 365環境の中での配布が中心になる。

### ライセンス・料金体系

| 利用形態 | 必要ライセンス | 料金の目安(2026年9月時点) |
|---|---|---|
| エージェントビルダーで社内利用 | Microsoft 365 Copilot(またはCopilot Chat)ライセンス | 追加費用なし(フェアユース前提) |
| Copilot Studioで社内利用(社員向けエージェント) | Microsoft 365 Copilotライセンス | 追加費用なし・クレジット消費なし(フェアユース前提) |
| Copilot Studioで社外公開・非ライセンスユーザーへの提供 | Copilot Studioのスタンドアロンライセンス(テナント単位) | Copilotクレジットのパック購入: 25,000クレジット/パックで$200/月(1クレジットあたり$0.008、日本円目安 ¥29,985/パック/月)。従量課金(PAYG)は1クレジットあたり$0.01(パック購入よりやや割高) |

「社内利用は追加費用なし」の前提となるMicrosoft 365 Copilotライセンス自体の価格は次のとおり(いずれも別途M365 E3/E5やBusiness Standard/Premium等のベースライセンスが必要)。

| プラン | 対象 | 料金の目安(2026年9月時点) |
|---|---|---|
| Microsoft 365 Copilot Business | 従業員300人以下の組織向け | 通常$21/ユーザー/月。2026年9月30日までの導入プロモーションで$18/ユーザー/月 |
| Microsoft 365 Copilot Enterprise | 全組織向け(年間契約) | $30/ユーザー/月 |

なお、2026年7月1日にMicrosoft 365自体のベースライセンス料金も値上げされており(例: E3が$36→$39/ユーザー/月、E5が$57→$60、F3が$8→$10)、Copilotクレジットの単価自体は変わらないものの、Copilotライセンスを載せる土台となるM365ライセンスのコストは上昇している。全社展開のコスト試算をする際は、Copilotクレジットの費用・Copilotライセンス料金・ベースライセンス値上げの3点を合わせて確認するとよい。

Copilotクレジットの消費量は応答の種類によって変わる。

| アクション種別 | 消費クレジットの目安 |
|---|---|
| スクリプト化された(トピックベースの)応答 | 1クレジット |
| 生成AIによる自由回答 | 2クレジット |
| エージェントのアクション実行(コネクタ呼び出しなど) | 5クレジット |
| 全社データ(Microsoft Graph)を検索根拠にした応答 | 10クレジット |
| 推論モデルでの応答 | 10応答あたり100クレジット(1応答あたり約10クレジット相当) |

**注意: これらは「どれか1つが適用される」のではなく、1回の応答の中で該当する要素が積み上がる。** 例えば「全社データ(Microsoft Graph)を検索根拠にした生成AIの自由回答」は 10 + 2 = 12クレジット、そこにアクション実行(コネクタ呼び出し)が2件加わると 12 + 5 + 5 = 22クレジットになる。推論モデルを使う高度な応答はさらに上乗せされ、1応答が100クレジット超になることもあるため、大量アクセスが見込まれるエージェントほど事前の試算が重要になる。

### GPTs / Gem / Claude Projects との対応表

| 観点 | Microsoft(エージェントビルダー/Copilot Studio) | ChatGPTのGPTs | GeminiのGem | Claude Projects |
|---|---|---|---|---|
| 位置づけ | エージェントビルダー=個人・小チーム向け簡易版、Copilot Studio=部門・全社・社外向けの本格開発環境 | 個人〜組織向けのカスタムGPT作成機能 | 個人向けのカスタムボット作成機能 | 個人〜組織向けの資料+指示のワークスペース |
| 必要プラン | エージェントビルダーはCopilot Chat/M365 Copilotライセンスに含まれ追加費用なし。Copilot Studioの社内利用も同様。社外公開はスタンドアロンライセンス+クレジット購入が必要 | Freeでは作成不可(Go/Plus以上が必要) | 無料プランでも作成・利用可 | Freeでも作成可(上限あり) |
| 外部API・業務システム連携 | Power Platformの1,400以上のコネクタ、Dataverse、マルチステップワークフロー(Copilot Studio) | Actions(OpenAPIスキーマでの外部API呼び出し) | 非対応 | 非対応(Claude API側でTool Useを別途実装する必要) |
| 主な知識源 | SharePoint/OneDrive/Dataverse/公開Webサイト/Microsoft Graph横断検索 | アップロードファイル | アップロードファイル/Google Drive | アップロードファイル/Google Drive(Privateプロジェクト限定) |
| 公開・配布範囲 | Teams/SharePoint/Microsoft 365 Copilot/Webサイト/Slack等マルチチャネル、社内〜社外顧客まで | 自分のみ/リンク共有/GPTストアでの一般公開 | 非公開/リンク共有/組織内共有 | Private、またはTeam/Enterprise内でのPublic共有 |
| 外部の一般公開マーケットプレイス | なし(自組織のエージェントストアでの社内配布が基本) | あり(GPTストア) | なし | なし |
| 料金の単位 | Copilotクレジット(社外公開・大量アクション実行時に消費) | プラン料金に含まれる(追加課金なし) | プラン料金に含まれる(追加課金なし) | プラン料金に含まれる(追加課金なし) |

## 注意点・よくある誤解

- **エージェントビルダーとCopilot Studioは別ツールではない**: エージェントビルダーで作った試作を「Copilot Studioにコピー」すれば、指示・知識源を引き継いだまま高度な機能(マルチステップワークフロー・外部システム連携)へ拡張できる。最初から高機能を求めない限り、まずエージェントビルダーで小さく始めるのが無駄がない
- **知識源の権限はエージェント側で上書きされない**: SharePoint/OneDriveを知識源にした場合、質問者がアクセス権を持たないファイルの内容は回答に反映されない(同じエージェントでも質問者によって回答内容が変わる)。「知識源に追加した=誰でも中身が見える」わけではないが、逆に言えば元のファイル権限設計が甘いと、想定より広い範囲の情報がエージェント経由で見えてしまう可能性もあるため、公開前にアクセス権を確認する
- **「指定したソースのみを使用する」は完全な遮断ではなく優先順位付け**: エージェントビルダーの「Only use specified sources」トグルをオンにしても、公式には一般的なAIの知識を完全にはブロックしない仕様と説明されている。指定した知識源の情報を優先はするが、それだけに厳密に限定した回答をさせたい場合(コンプライアンス上、規程集以外の一般論を絶対に混ぜたくない等)は、より厳密な制御ができるCopilot Studio側のトピック・入力変数での制御を検討する
- **「メッセージ課金」という呼び方は2025年9月から変わっている**: 現在は「Copilotクレジット」単位の課金に統一されている。「1メッセージ=いくら」という古い記事の説明は、現在の実態(応答種別ごとに消費クレジット数が異なる)と食い違うことがある
- **社内利用なら基本無料、社外公開や大量のアクション実行では課金が発生する**: M365 Copilotライセンス保有者が社内向けに使う範囲では基本的に追加費用がかからないが、社外の顧客向けに公開したり、コネクタ経由のアクションを多用するエージェントを大量展開すると、Copilotクレジットの追加購入が必要になる。全社展開の前にコスト試算をしておく
- **個人の判断だけで全社展開はできない**: エージェントビルダーの利用可否やSharePoint連携の有効・無効は、Microsoft 365管理センターやPower Platform管理センターの設定(管理者ポリシー)に依存する。情報システム部門との事前調整が必要になる場合が多い

## 最初の一歩

Microsoft 365 Copilotアプリの「エージェントビルダー」で、自分やチームがよく聞かれる質問に答えるだけの簡単なFAQエージェントを1つ作ってみる(知識源はSharePointの1フォルダだけに絞り、公開範囲も自分のみで十分)。

## 関連トピック

- [GPTsの作り方と公開設定](gpts-creation-basics.md)
- [Gem(Geminiのカスタムボット機能)の基本](gemini-gem-feature.md)
- [Claude(Anthropic)の「プロジェクト」機能の基本](claude-projects-basics.md)
- [Microsoft Copilotの基本](../part03-ai-chat-tools/microsoft-copilot-basics.md)

## 更新履歴

### 2026-09-09: アプリ統合・料金・知識源の仕様変更を反映して最新化
- **内容**: (1)アクセス方法を更新——個人向けCopilotアプリとMicrosoft 365 Copilotアプリが「Microsoft Copilot」アプリに統合され、Webアドレスもcopilot.cloud.microsoftへ2026年8月〜9月に順次移行中である旨を追記。(2)Copilot Studioのワークフローデザイナーが2026年8月3日にGAしたこと、新オーケストレーターで評価スコアが約20%向上・消費トークンが半減したという社内検証値を追記。(3)Copilotクレジットの消費は要素ごとに積み上がる(スタッキングする)仕様である旨を、具体例(全社検索+生成AI回答+アクション2件=22クレジット)とともに明記。(4)社内利用が無料になる前提のMicrosoft 365 Copilotライセンス自体の料金(Business $18〜21/ユーザー/月、Enterprise $30/ユーザー/月)を新規に追加。(5)2026年8月のエージェントビルダー更新(新規エージェントは機能が既定で有効、「アップロードファイル」→「添付ファイル(Attachments)」への呼称変更)を追記。(6)「指定したソースのみを使用する」設定が完全な遮断ではなく優先順位付けである点を注意点に追加
- **出典**: [Office Watch: Two Copilot Apps Become One](https://office-watch.com/2026/copilot-apps-merge/)、[futurework.blog: Microsoft Copilot app – one app, new name, new icon, new URL!](https://futurework.blog/2026/08/14/microsoft-copilot-app-one-app-new-name-new-icon-new-url/)、[RPABOTS.WORLD: Copilot Studio Rebuilt: Workflow Designer GA, CUA, and Run-Only Sharing Explained](https://rpabotsworld.com/microsoft-copilot-studio-august-2026-rebuilt-agent-platform-guide/)、[CloudZero: Microsoft Copilot Studio Pricing In 2026](https://www.cloudzero.com/blog/copilot-studio-pricing/)、[Velosio: Microsoft 365 Copilot Pricing Calculator (2026)](https://www.velosio.com/blog/m365-copilot-pricing-calculator/)、[GoSearch Blog: Microsoft Copilot Pricing 2026](https://www.gosearch.ai/blog/microsoft-copilot-pricing/)、[m365admin: Agent Builder capabilities update](https://m365admin.handsontek.net/agent-builder-capabilities-update/)、[Qiita: 会社で Microsoft 365 Copilot しか使えない人のための「エージェントビルダー」入門](https://qiita.com/sukimaengineer/items/15ddf5601ff29ef8d376)

### 2026-07-28: Copilot Studioのリビルドとコネクタ数・料金情報を更新
- **内容**: 2026年7月7日のCopilot Studioの全面リビルド(エージェント型オーケストレーター、ワークフローデザイナー、設定タブの9→4整理、Skills、エージェントストアへの公開)を追記。コネクタ数を「500以上」から現状の「1,400以上」に修正。2026年7月1日のMicrosoft 365ベースライセンス値上げ(E3 $36→$39等)を料金面の注記として追加
- **出典**: [Microsoft Tech Community: Meet the new Copilot Studio, rebuilt for more complex multi-step work](https://techcommunity.microsoft.com/blog/copilot-studio-blog/meet-the-new-copilot-studio-rebuilt-for-more-complex-multi-step-work/4526488)、[ChatForest: Microsoft Copilot Studio Rebuilt July 2026](https://chatforest.com/builders-log/microsoft-copilot-studio-rebuilt-july-2026-orchestrator-workflow-designer-builder-guide/)、[EPC Group: Copilot Studio Enterprise Agent Development 2026](https://www.epcgroup.net/answers/copilot-studio-enterprise-agent-development-2026)、[Kesslernity: M365 Copilot Agents Cost Model](https://www.kesslernity.com/blog/m365-copilot-agents-cost-model)

### 2026-07-06: 初版執筆
- **内容**: Copilot Studioとエージェントビルダーの違い・使い分け、作成手順(アクセス方法・指示設定・知識源SharePoint/OneDrive等の追加・テスト・公開)、Copilotクレジットベースの料金体系(2025年9月移行、パック$200/25,000クレジット・PAYG $0.01/クレジット、応答種別ごとの消費クレジット目安)、M365 Copilotライセンスとの関係、GPTs/Gem/Claude Projectsとの4ツール対応表、社内問い合わせエージェントの指示文サンプルを整理
- **出典**: [Microsoft Learn: クイック スタート エージェントの作成と展開](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/fundamentals-get-started)、[Microsoft Learn: 請求レートと管理](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-messages-management)、[Microsoft Learn: Copilot Studio ライセンス](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/billing-licensing)、[Microsoft Learn: Choose between Agent Builder in Microsoft 365 Copilot and Copilot Studio](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/copilot-studio-experience)、[Microsoft Learn: Microsoft 365 Copilotでエージェント ビルダーを使用してエージェントをビルドする](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder-build-agents)、[Microsoft Support: Microsoft 365 Copilotを使用して独自のエージェントを構築する](https://support.microsoft.com/ja-jp/microsoft-365-copilot/build-your-own-agent-with-microsoft-365-copilot)、[CloudZero: Microsoft Copilot Studio Pricing In 2026](https://www.cloudzero.com/blog/copilot-studio-pricing/)、[Qiita: 会社で Microsoft 365 Copilot しか使えない人のための「エージェントビルダー」入門](https://qiita.com/sukimaengineer/items/15ddf5601ff29ef8d376)
