---
title: Microsoft Copilotの基本
part: 7
chapter: 第2章 その他のLLM
tags: [Copilot, Microsoft, Microsoft 365, GitHub Copilot, Windows]
created: 2026-07-06
updated: 2026-07-06
---

# Microsoft Copilotの基本

## これは何か

「Copilot(コパイロット)」は、Microsoftが自社のほぼ全製品に付けているAI機能の名前で、Windows・Word・Excel・Outlook・Teams・GitHubなど、まったく別物の機能に同じ「Copilot」という名前が使われている。そのため「会社にCopilotが入っていると聞いたが、自分が使っているのはどれなのか」「無料のCopilotと有料のCopilotで何が違うのか」が分からず混乱する人が非常に多い。このページでは、名前が重複する複数の「Copilot」を整理し、それぞれが何をするツールで、どこで使え、誰向けなのかを一枚の地図にする。

## 仕組み・背景

Microsoftは2023年以降、生成AI機能を横展開する際にブランド名を統一する方針を取り、Bing Chat・Microsoft 365 Chat・GitHub Copilot Chatなど別々に育っていた機能を軒並み「Copilot」の名称に揃えていった。その結果、技術的な中身も対象データも違う複数の製品が同じ名前を名乗ることになった。見分けるポイントは大きく3つある。

1. **土台になっているデータが「社内データ」か「Web」か**: 無料のCopilotはWeb上の一般知識だけを使う。有料の「Microsoft 365 Copilot」は、Microsoft Graph(社内のメール・ファイル・会議・チャット履歴などをひとまとめに扱う仕組み)から自分がアクセス権を持つ社内データを取り込んで回答する(この仕組みを「グラウンディング」と呼ぶ)
2. **組み込まれている場所がOS(Windows)かアプリ(Word等)か開発環境(GitHub)か**
3. **契約の単位が個人向けかMicrosoft 365ライセンスの追加(アドオン)か開発者向けか**

これを踏まえて主要な「Copilot」を整理すると次のようになる。

| 製品名 | 何をするか | どこで使うか | 主な対象者 |
|---|---|---|---|
| **Copilot(無料版)** | Web検索を土台にした汎用チャットAI。画像生成・音声対話・簡単な文章作成ができる | copilot.microsoft.com、Windows 11のタスクバー、Microsoft Edge、Copilotアプリ(iOS/Android) | 個人利用全般。社内データへのアクセスはなし |
| **Microsoft 365 Copilot Chat** | 無料版と同じWeb中心のチャットに加え、エンタープライズ向けのデータ保護(後述)が適用され、簡易的なエージェント機能も使える | Microsoft 365(旧Office)アプリ内のサイドパネル、Teams | Microsoft 365ライセンスを持つ組織のユーザー全員(追加課金なしで利用可) |
| **Microsoft 365 Copilot(旧称: Copilot for Microsoft 365)** | Word・Excel・PowerPoint・Outlook・Teamsの中に組み込まれ、自分がアクセス権を持つ社内のメール・ファイル・会議録などを根拠に文書作成・要約・分析を行う | Word/Excel/PowerPoint/Outlook/Teams内の「Copilot」ボタン、Copilotアプリ | Microsoft 365ライセンス保有企業のうち、追加のCopilotライセンスを購入したユーザー |
| **Copilot Pro / Microsoft 365 Premium** | 個人(コンシューマー)向けに、Word・Excel・PowerPoint・OutlookでのAI機能や優先的なモデルアクセスを提供 | Microsoft 365 Personal/Familyのアプリ内 | 会社のライセンスではなく個人で契約する個人事業主・フリーランス等 |
| **GitHub Copilot** | ソースコードの自動補完・チャットでのコード生成・自律的なコーディングエージェント | VS Code等のIDE、GitHub.com上のチャット | ソフトウェア開発者 |
| **Copilot in Windows** | Windows 11のOS機能として、設定変更・アプリ操作の補助やチャットを提供 | Windows 11のタスクバーアイコン | Windows 11ユーザー全般 |

「Copilot」とだけ言われたら、まず「無料のWeb版か」「会社のMicrosoft 365に統合された有料版か」「開発者向けのGitHub Copilotか」の3択に絞ると混乱しにくい。

## 使いどころ・使い分け

ビジネスパーソンが日常業務で比較検討することが多いChatGPT・Gemini・Claudeとの違いは、「汎用AIとしての賢さ」ではなく「自社のOffice文書・メール・会議データにどれだけ深く食い込めるか」にある。

| 軸 | 強いツール | 理由 |
|---|---|---|
| Word/Excel/PowerPoint/Outlook/Teamsに入っている実データを根拠にした作業(会議の議事録要約、受信箱の整理、既存資料をもとにした資料作成) | Microsoft 365 Copilot | Microsoft Graphによって自分の権限内の社内データを直接参照できるため |
| 汎用的な調べ物・アイデア出し・雑多な質問への幅広い対応力 | ChatGPT、Claude、Gemini | 学習データ・モデルの汎用的な賢さで先行している場面が多い |
| Google Workspace(Gmail・スプレッドシート等)との連携 | Gemini | GoogleエコシステムとGeminiの統合はMicrosoftの逆パターン |
| 長文の要約・複雑な指示への追従・自律的なコーディング作業 | Claude | 長文コンテキスト処理とコーディングエージェントに強い傾向 |
| 社内のセキュリティ・ガバナンス要件(監査ログ、テナント内へのデータ封じ込め)を重視する大企業での全社導入 | Microsoft 365 Copilot | 既存のMicrosoft 365の権限管理・コンプライアンス基盤をそのまま流用できるため |
| すでにGitHub/VS Codeで開発している組織のコーディング支援 | GitHub Copilot | IDEへの統合度と豊富なコード補完実績 |

判断の目安: 「すでに全社でMicrosoft 365(Word・Excel・Outlook・Teams)を使っていて、その中のデータを扱う作業を効率化したい」ならMicrosoft 365 Copilotが第一候補になる。逆に、社内データに紐づかない一般的な調べ物・文章生成・コーディングであれば、ChatGPT・Claude・Geminiと機能面で大きな差はなく、既存の契約や好みで選んでよい。

## 実務での使い方

### 料金プラン(2026年7月時点の目安)

**個人向け:**

| プラン | 月額目安 | 内容 |
|---|---|---|
| Copilot(無料) | $0 | copilot.microsoft.com・Windows・Edgeで利用可。社内データへのアクセスなし |
| Microsoft 365 Premium | $19.99/月 | Word/Excel/PowerPoint/Outlook/OneNoteでのAI機能、優先的なモデルアクセス、6TBストレージ等を含む個人向け統合プラン。旧「Copilot Pro」の実質的な後継 |
| Copilot Pro(既存契約者のみ) | $20/月 | 2025年後半に新規募集を終了。既存ユーザーは2026年8月1日のサポート終了まで継続利用可 |

**法人向け(Microsoft 365 Copilot、要:対象のMicrosoft 365ベースライセンス):**

| プラン | 月額目安(1ユーザーあたり、年払い) | 対象 |
|---|---|---|
| Microsoft 365 Copilot Chat | 追加課金なし | 対象のMicrosoft 365ライセンス保有者は全員利用可(Web中心+簡易エージェント) |
| Microsoft 365 Copilot(中小企業向け、300ユーザーまで) | 約$18〜21/ユーザー(2026年9月まで割引価格、以降値上げ予定) | Business Basic/Standard/Premiumに追加するアドオン |
| Microsoft 365 Copilot(エンタープライズ向け) | $30/ユーザー(年契約) | E3/E5等のエンタープライズライセンスに追加するアドオン |

Copilotは単体販売されておらず、必ず対象のMicrosoft 365ベースライセンス(Business Basic/Standard/Premium、E3/E5等)を保有したうえでの追加(アドオン)購入になる点に注意。ベースライセンス込みの実質負担額は、中小企業向けで月$34〜43程度、エンタープライズ向けで月$66〜87程度になるとの試算もある。契約前には必ず[Microsoft公式の料金ページ](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)で最新の金額・条件を確認すること。

**開発者向け(GitHub Copilot、2026年7月時点):**

| プラン | 月額目安 | 内容 |
|---|---|---|
| GitHub Copilot Free | $0 | 自動モデル選択のみ、機能・利用量に制限 |
| GitHub Copilot Pro | $10/月 | 月$10相当のAI Credits(利用量に応じて消費するクレジット制)込み |
| GitHub Copilot Pro+ | $39/月 | 月$39相当のAI Credits込み、上位モデルへのアクセス |
| GitHub Copilot Business | $19/ユーザー/月 | 組織向け、一元管理・ポリシー制御 |
| GitHub Copilot Enterprise | 要問い合わせ | Business同等機能に加え優先アクセス・大容量クレジット |

2026年6月からGitHub Copilotは従量課金制(利用量に応じてクレジットを消費する仕組み)に移行しており、各プランの「基本料金に含まれる利用量」を超えると追加課金が発生する設計になっている。

### 社内データの扱い方(commercial data protection)

Microsoft 365 CopilotとMicrosoft 365 Copilot Chatには「Enterprise Data Protection(企業向けデータ保護)」と呼ばれる契約上の保護が適用される。ポイントは以下の3つ。

- **Microsoft Graphによるグラウンディング**: Copilotが回答を作る際、ユーザー本人がアクセス権を持つ範囲のメール・ファイル・チャット・会議データだけをMicrosoft Graph経由で参照する。他人の権限外データは参照されない
- **プロンプト・応答はAIモデルの学習に使われない**: Copilotへの入力(プロンプト)や出力(応答)、Graph経由で読み込んだデータは「顧客データ」として扱われ、基盤モデルの追加学習には使われない契約になっている
- **無料版のCopilotには適用されない**: 無料のCopilot(copilot.microsoft.com、Windows版)にはこの企業向け保護は適用されず、社内データへのアクセスもない。業務で社内文書を扱いたい場合は、必ずMicrosoft 365 Copilot(またはCopilot Chat)を使う必要がある

### 導入時の基本手順の目安

1. 自社のMicrosoft 365契約が対象ライセンス(Business Basic/Standard/Premium、E3/E5等)かをIT管理者に確認する
2. Microsoft 365管理センターで対象ユーザーにCopilotライセンスを割り当てる
3. Word/Excel/PowerPoint/Outlook/Teamsを開くと、リボンやサイドパネルに「Copilot」ボタンが表示されるようになる
4. Teams会議では「レコーディング」をオンにすると、会議後にCopilotへ「今日の決定事項をまとめて」のように指示して議事録を要約できる

## 注意点・よくある誤解

- **「Copilot」という名前だけでは製品を特定できない**: 社内で「Copilotを使って」と言われたら、無料版か、Microsoft 365 Copilotか、GitHub Copilotかを必ず確認する。ライセンス費用も機能も別物である
- **無料のCopilotに社内文書を貼り付けない**: 無料版は社内データへのアクセス権もエンタープライズ向けデータ保護もない。機密情報の要約・分析は必ずMicrosoft 365 CopilotかCopilot Chat(いずれも対象ライセンス保有者向け)で行う
- **Copilot単体では契約できない**: 必ず対象のMicrosoft 365ベースライセンスが前提になるため、見積もりは「アドオン価格」だけでなく「ベースライセンス+アドオン」の合計で比較する
- **料金・呼称の変更頻度が高い**: 2025年後半にCopilot Proが個人向けでは実質Microsoft 365 Premiumに統合されるなど、短期間で名称・料金体系が変わっている。本ページの数値は目安であり、契約前には必ず公式サイトで確認する
- **精度は「社内データの整備状況」に左右される**: SharePointやOneDriveのファイル権限・命名規則が乱雑だと、Copilotが正しいデータを見つけられず回答の質が落ちる。導入効果を出すには、Copilot導入前にファイル整理・アクセス権の棚卸しを行うのが実務上のコツ

## 最初の一歩

自社がMicrosoft 365を契約している場合は、Outlookで受信済みの長いメールスレッドを開き、右上の「Copilot」または「まとめる」ボタンで要約を試してみる(Copilot Chatが有効なら追加課金なしで試せる)。個人で試したいだけなら、まずcopilot.microsoft.com(無料)で簡単な文章生成を1つ試すところから始めるとよい。

## 関連トピック

- [Claude(Anthropic)の基本](./claude-basics.md)
- [Google Geminiの基本](./google-gemini-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: 「Copilot」を名乗る複数の製品(無料Copilot、Microsoft 365 Copilot Chat、Microsoft 365 Copilot、Copilot Pro/Microsoft 365 Premium、GitHub Copilot、Copilot in Windows)の違いを整理し、2026年7月時点の料金プラン、Microsoft Graphによるグラウンディングとエンタープライズ向けデータ保護の仕組み、ChatGPT/Gemini/Claudeとの使い分けをまとめた
- **出典**: [Microsoft公式: Microsoft 365 Copilot Plans and Pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)、[Microsoft Learn: Enterprise data protection in Microsoft 365 Copilot and Microsoft 365 Copilot Chat](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection)、[Microsoft Learn: Decide which Copilot is right for you](https://learn.microsoft.com/en-us/microsoft-365/copilot/which-copilot-for-your-organization)、[GitHub公式: GitHub Copilot Plans & pricing](https://github.com/features/copilot/plans)、[GitHub Blog: GitHub Copilot is moving to usage-based billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)、[Microsoft Community Hub: Act Now: Lock in Current Pricing on Microsoft 365 Copilot Business Bundles](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/act-now-lock-in-current-pricing-on-microsoft-365-copilot-business-bundles/4502628)
