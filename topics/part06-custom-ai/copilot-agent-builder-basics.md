---
title: Microsoft Copilot Studioによるカスタムエージェント作成の基本
part: 6
chapter: 第2章 主要ツールでの作り方
tags: [Copilot Studio, Microsoft 365 Copilot, エージェントビルダー, Microsoft, カスタムAI]
created: 2026-07-06
updated: 2026-07-06
---

# Microsoft Copilot Studioによるカスタムエージェント作成の基本

## これは何か

「総務への問い合わせが同じ質問ばかりで対応が追いつかない」「社内規程集はSharePointにあるのに、みんな探さずに担当者に聞いてしまう」——こうした業務は、Microsoft 365環境専用のカスタムAI(エージェント)を1つ作れば、多くを自動応答に移せる。**Copilot Studio**は、指示(プロンプト)・知識源(SharePoint/OneDriveなどの社内データ)・実行アクションを組み合わせて、Teams・SharePoint・Webサイトなど複数のチャネルに配布できる本格的なノーコード開発環境である。Microsoft 365 Copilotアプリの中には、その簡易版にあたる「**エージェントビルダー**」も内蔵されており、目的に応じてどちらを使うかを選ぶことになる。

## 仕組み・背景

MicrosoftのAIエージェント構築手段は、機能の重さで2段階に分かれている。

- **エージェントビルダー**: Microsoft 365 Copilotアプリ(Copilot Chat)に内蔵された軽量版。自然言語で「何をしてほしいか」を伝えると、AIが指示文・知識源・推奨プロンプトを自動生成する。Microsoft Graph(社内のメール・ファイル・Teams会話などの情報基盤)を前提に動き、Microsoft 365のセキュリティ・コンプライアンス設定をそのまま引き継ぐ。個人〜小規模チーム向けの「かんたん版」という位置づけ
- **Copilot Studio**: Power Platform(Microsoftのノーコード開発基盤)上に構築された本格的な開発環境。指示・知識源に加えて、複数ステップの処理(トピック・フロー)、500以上のコネクタを使った外部システム連携(CRM・ERP・チケット管理システムなど)、Teams/SharePoint/Webサイト/Slackなど複数チャネルへの配布、社外の非ライセンスユーザーへの公開まで対応する

両者は完全に別物ではなく、エージェントビルダーで作った試作を「Copilot Studioにコピー」して、後から高度な機能へ拡張する移行パスが用意されている(Microsoft Learn: Choose between Agent Builder and Copilot Studio)。

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

- **エージェントビルダー**: Microsoft 365 Copilotアプリ(copilot.cloud.microsoft、またはTeams内のCopilotアプリ)の左ペインで「エージェント」→「+新しいエージェント」。SharePointサイトの「エージェントを作成」ボタンからも同じビルダーを呼び出せる
- **Copilot Studio**: copilotstudio.microsoft.com に勤務先アカウントでサインインし、左メニュー「エージェント」→「+作成」→「新しいエージェント」

### 作成手順(共通の流れ・2026年7月時点の目安)

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
| アップロード(埋め込み)ファイル | 最大20ファイル程度 | 同様に対応 |
| SharePoint | サイト・ライブラリ単位で指定 | サイト・ライブラリ単位で指定、複数サイトの横断も可 |
| Teamsチャット | 特定チャットを最大5個程度 | – |
| 公開Webサイト | 対応 | 対応 |
| 業務システム(Dynamics 365、Salesforce、ServiceNowなど) | 非対応 | Power Platformのコネクタ(500以上)経由で対応 |
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

SharePoint文書検索特化にしたい場合は、上記の「対応範囲」を「指定したSharePointサイト内の文書検索と要約」に変え、知識源をそのサイトのライブラリ1つに絞ると、余計な情報源を参照しない絞り込み型のエージェントになる。

### 公開先チャネル

Teams、SharePoint、Microsoft 365 Copilot(Copilot Chat)、公開Webサイト、Facebook、Direct Line/API経由のカスタムアプリなどに公開できる(Copilot Studio)。エージェントビルダーで作ったエージェントは、Teams・SharePoint・Microsoft 365 Copilotアプリ内という、Microsoft 365環境の中での配布が中心になる。

### ライセンス・料金体系

| 利用形態 | 必要ライセンス | 料金の目安 |
|---|---|---|
| エージェントビルダーで社内利用 | Microsoft 365 Copilot(またはCopilot Chat)ライセンス | 追加費用なし(フェアユース前提) |
| Copilot Studioで社内利用(社員向けエージェント) | Microsoft 365 Copilotライセンス | 追加費用なし・クレジット消費なし(フェアユース前提) |
| Copilot Studioで社外公開・非ライセンスユーザーへの提供 | Copilot Studioのスタンドアロンライセンス(テナント単位) | Copilotクレジットのパック購入: 25,000クレジット/パックで$200/月(日本円目安 ¥29,985/パック/月)。従量課金(PAYG)は1クレジットあたり$0.01(パック購入よりやや割高) |

Copilotクレジットの消費量は応答の種類によって変わる。

| アクション種別 | 消費クレジットの目安 |
|---|---|
| スクリプト化された(トピックベースの)応答 | 1クレジット |
| 生成AIによる自由回答 | 2クレジット |
| エージェントのアクション実行(コネクタ呼び出しなど) | 5クレジット |
| 全社データ(Microsoft Graph)を検索根拠にした応答 | 10クレジット |
| 推論モデルでの応答 | 10応答あたり100クレジット(1応答あたり約10クレジット相当) |

### GPTs / Gem / Claude Projects との対応表

| 観点 | Microsoft(エージェントビルダー/Copilot Studio) | ChatGPTのGPTs | GeminiのGem | Claude Projects |
|---|---|---|---|---|
| 位置づけ | エージェントビルダー=個人・小チーム向け簡易版、Copilot Studio=部門・全社・社外向けの本格開発環境 | 個人〜組織向けのカスタムGPT作成機能 | 個人向けのカスタムボット作成機能 | 個人〜組織向けの資料+指示のワークスペース |
| 必要プラン | エージェントビルダーはCopilot Chat/M365 Copilotライセンスに含まれ追加費用なし。Copilot Studioの社内利用も同様。社外公開はスタンドアロンライセンス+クレジット購入が必要 | Freeでは作成不可(Go/Plus以上が必要) | 無料プランでも作成・利用可 | Freeでも作成可(上限あり) |
| 外部API・業務システム連携 | Power Platformの500以上のコネクタ、Dataverse、マルチステップワークフロー(Copilot Studio) | Actions(OpenAPIスキーマでの外部API呼び出し) | 非対応 | 非対応(Claude API側でTool Useを別途実装する必要) |
| 主な知識源 | SharePoint/OneDrive/Dataverse/公開Webサイト/Microsoft Graph横断検索 | アップロードファイル | アップロードファイル/Google Drive | アップロードファイル/Google Drive(Privateプロジェクト限定) |
| 公開・配布範囲 | Teams/SharePoint/Microsoft 365 Copilot/Webサイト/Slack等マルチチャネル、社内〜社外顧客まで | 自分のみ/リンク共有/GPTストアでの一般公開 | 非公開/リンク共有/組織内共有 | Private、またはTeam/Enterprise内でのPublic共有 |
| 外部の一般公開マーケットプレイス | なし(自組織のエージェントストアでの社内配布が基本) | あり(GPTストア) | なし | なし |
| 料金の単位 | Copilotクレジット(社外公開・大量アクション実行時に消費) | プラン料金に含まれる(追加課金なし) | プラン料金に含まれる(追加課金なし) | プラン料金に含まれる(追加課金なし) |

## 注意点・よくある誤解

- **エージェントビルダーとCopilot Studioは別ツールではない**: エージェントビルダーで作った試作を「Copilot Studioにコピー」すれば、指示・知識源を引き継いだまま高度な機能(マルチステップワークフロー・外部システム連携)へ拡張できる。最初から高機能を求めない限り、まずエージェントビルダーで小さく始めるのが無駄がない
- **知識源の権限はエージェント側で上書きされない**: SharePoint/OneDriveを知識源にした場合、質問者がアクセス権を持たないファイルの内容は回答に反映されない(同じエージェントでも質問者によって回答内容が変わる)。「知識源に追加した=誰でも中身が見える」わけではないが、逆に言えば元のファイル権限設計が甘いと、想定より広い範囲の情報がエージェント経由で見えてしまう可能性もあるため、公開前にアクセス権を確認する
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

### 2026-07-06: 初版執筆
- **内容**: Copilot Studioとエージェントビルダーの違い・使い分け、作成手順(アクセス方法・指示設定・知識源SharePoint/OneDrive等の追加・テスト・公開)、Copilotクレジットベースの料金体系(2025年9月移行、パック$200/25,000クレジット・PAYG $0.01/クレジット、応答種別ごとの消費クレジット目安)、M365 Copilotライセンスとの関係、GPTs/Gem/Claude Projectsとの4ツール対応表、社内問い合わせエージェントの指示文サンプルを整理
- **出典**: [Microsoft Learn: クイック スタート エージェントの作成と展開](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/fundamentals-get-started)、[Microsoft Learn: 請求レートと管理](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/requirements-messages-management)、[Microsoft Learn: Copilot Studio ライセンス](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/billing-licensing)、[Microsoft Learn: Choose between Agent Builder in Microsoft 365 Copilot and Copilot Studio](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/copilot-studio-experience)、[Microsoft Learn: Microsoft 365 Copilotでエージェント ビルダーを使用してエージェントをビルドする](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder-build-agents)、[Microsoft Support: Microsoft 365 Copilotを使用して独自のエージェントを構築する](https://support.microsoft.com/ja-jp/microsoft-365-copilot/build-your-own-agent-with-microsoft-365-copilot)、[CloudZero: Microsoft Copilot Studio Pricing In 2026](https://www.cloudzero.com/blog/copilot-studio-pricing/)、[Qiita: 会社で Microsoft 365 Copilot しか使えない人のための「エージェントビルダー」入門](https://qiita.com/sukimaengineer/items/15ddf5601ff29ef8d376)
