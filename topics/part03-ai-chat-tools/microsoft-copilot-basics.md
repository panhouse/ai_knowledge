---
title: Microsoft Copilotの基本
part: 3
chapter: 第5章 主要ツール各論
tags: [Copilot, Microsoft, Microsoft 365, GitHub Copilot, Windows]
created: 2026-07-06
updated: 2026-08-19
---

# Microsoft Copilotの基本

## これは何か

「Copilot(コパイロット)」は、Microsoftが自社のほぼ全製品に付けているAI機能の名前で、Windows・Word・Excel・Outlook・Teams・GitHubなど、まったく別物の機能に同じ「Copilot」という名前が使われている。そのため「会社にCopilotが入っていると聞いたが、自分が使っているのはどれなのか」「無料のCopilotと有料のCopilotで何が違うのか」が分からず混乱する人が非常に多い。加えて2026年8月からは、個人向けCopilotアプリと法人向けMicrosoft 365 Copilotアプリそのものが1つに統合され始めており、混乱に拍車がかかっている。このページでは、名前が重複する複数の「Copilot」を整理し、それぞれが何をするツールで、どこで使え、誰向けなのかを一枚の地図にする。

## 仕組み・背景

Microsoftは2023年以降、生成AI機能を横展開する際にブランド名を統一する方針を取り、Bing Chat・Microsoft 365 Chat・GitHub Copilot Chatなど別々に育っていた機能を軒並み「Copilot」の名称に揃えていった。その結果、技術的な中身も対象データも違う複数の製品が同じ名前を名乗ることになった。見分けるポイントは大きく3つある。

1. **土台になっているデータが「社内データ」か「Web」か**: 無料のCopilotはWeb上の一般知識だけを使う。有料の「Microsoft 365 Copilot」は、Microsoft Graph(社内のメール・ファイル・会議・チャット履歴などをひとまとめに扱う仕組み)から自分がアクセス権を持つ社内データを取り込んで回答する(この仕組みを「グラウンディング」と呼ぶ)
2. **組み込まれている場所がOS(Windows)かアプリ(Word等)か開発環境(GitHub)か**
3. **契約の単位が個人向けかMicrosoft 365ライセンスの追加(アドオン)か開発者向けか**

これを踏まえて主要な「Copilot」を整理すると次のようになる。

| 製品名 | 何をするか | どこで使うか | 主な対象者 |
|---|---|---|---|
| **Copilot(無料版)** | Web検索を土台にした汎用チャットAI。画像生成・音声対話・簡単な文章作成ができる | Microsoft Copilotアプリ(Web/iOS/Android)、Windows 11のタスクバー、Microsoft Edge | 個人利用全般。社内データへのアクセスはなし |
| **Microsoft 365 Copilot Chat** | 無料版と同じWeb中心のチャットに加え、エンタープライズ向けのデータ保護(後述)が適用され、簡易的なエージェント機能も使える。ただし2026年4月15日以降、Word/Excel/PowerPoint/OneNote内蔵チャットの扱いが組織規模で変わった(後述) | Microsoft 365(旧Office)アプリ内のサイドパネル、Teams、Outlook | Microsoft 365ライセンスを持つ組織のユーザー全員(追加課金なしで利用可。ただしWord/Excel/PowerPoint/OneNote内での利用条件に制限あり) |
| **Microsoft 365 Copilot(旧称: Copilot for Microsoft 365)** | Word・Excel・PowerPoint・Outlook・Teamsの中に組み込まれ、自分がアクセス権を持つ社内のメール・ファイル・会議録などを根拠に文書作成・要約・分析を行う。既定モデルはOpenAIのGPT-5.6(2026年7月9日以降) | Word/Excel/PowerPoint/Outlook/Teams内の「Copilot」ボタン、Copilotアプリ | Microsoft 365ライセンス保有企業のうち、追加のCopilotライセンスを購入したユーザー |
| **Microsoft 365 Copilot Cowork(新)** | 「議事録を要約して」のような一問一答ではなく、複数ステップにまたがる長時間タスク(大量ファイルの横断比較、バージョン差分の洗い出し、営業パイプラインの分析と次アクション提案など)を計画立案から完了までまるごと任せる自律型エージェント。2026年6月16日に一般提供(GA)開始。GA時点ではAnthropicのClaude Opus 4.8・Sonnet 4.6を採用しており、「Copilot」ブランドの中でもOpenAI以外のモデルが使われている代表例 | Microsoft 365 Copilotアプリ内 | Microsoft 365 Copilotライセンス保有者(利用量に応じた従量課金が別途発生) |
| **Copilot Pro / Microsoft 365 Premium** | 個人(コンシューマー)向けに、Word・Excel・PowerPoint・OutlookでのAI機能や優先的なモデルアクセスを提供。Copilot Proは2026年8月1日にサポート終了済みで、現在はMicrosoft 365 Premiumが唯一の個人向け統合プラン | Microsoft 365 Personal/Familyのアプリ内 | 会社のライセンスではなく個人で契約する個人事業主・フリーランス等 |
| **GitHub Copilot** | ソースコードの自動補完・チャットでのコード生成・自律的なコーディングエージェント | VS Code等のIDE、GitHub.com上のチャット | ソフトウェア開発者 |
| **Copilot in Windows** | Windows 11のOS機能として、設定変更・アプリ操作の補助やチャットを提供 | Windows 11のタスクバーアイコン | Windows 11ユーザー全般 |

「Copilot」とだけ言われたら、まず「無料のWeb版か」「会社のMicrosoft 365に統合された有料版か」「開発者向けのGitHub Copilotか」の3択に絞ると混乱しにくい。

**2026年8月、個人向けCopilotアプリと法人向けMicrosoft 365 Copilotアプリの統合が始まった点に注意。** Microsoftは同月、consumer(個人)アカウントと会社・学校アカウントを1つの「Microsoft Copilot」アプリの中でアカウント切り替え(account switcher)によって使い分けられるよう、両アプリの統合ロールアウトを開始した。Web/モバイル版が先行し、Windows/Mac版は2026年9月以降に順次展開される予定。ポイントは以下の3つ。

- **アプリ・ブランドは統合されるが、データとライセンスの境界は変わらない**: 個人アカウントで入力した内容が会社アカウント側に混ざることはなく、逆も同様(Microsoft Entraによるテナント分離が引き続き機能する)。Enterprise Data Protection(後述)は従来どおり組織アカウントにのみ適用され、個人アカウントには適用されない
- **法人向けアクセスURLの変更**: 法人向けCopilotのWebアクセス先が`m365.cloud.microsoft`から`copilot.cloud.microsoft`へ移行しつつある。社内マニュアルやブックマークにURLを直書きしている場合は更新が必要
- **個人向け機能の一部終了**: この統合に伴い、個人のCopilotアプリにあったDeep Research・Copilot Podcasts・Group Chatなどの機能が2026年8月18日から順次終了・移行の対象になった

**2026年4月15日、「無料で使えるCopilot Chat」の範囲も縮小している(こちらは現在も有効)。** Microsoftは2025年9月にWord/Excel/PowerPoint/OneNote内のCopilot Chatを追加課金なしで開放していたが、2026年4月15日以降は組織規模によって扱いが分かれている。

- **ユーザー数2,000人超の組織**: 有料のMicrosoft 365 Copilotライセンスを持たないユーザーは、Word/Excel/PowerPoint/OneNote内のCopilot Chatにアクセスできなくなった
- **ユーザー数2,000人以下の組織**: 引き続き無料で使えるが「standard access」という混雑時に品質・応答速度が落ちる制限付きアクセスになり、有料ライセンスへのアップグレード訴求が表示される
- **どちらの場合もOutlookとWeb版のCopilot Chatは影響を受けず、従来どおり利用できる**

したがって「Word/ExcelでCopilotボタンが急に使えなくなった/重くなった」という問い合わせは、多くの場合この2026年4月の変更が原因である。

さらに2026年8月には、Agent 365(社内で個別開発・ガバナンスした業務エージェントを一元管理する仕組み)上で公開したエージェントを、Microsoft 365 Copilot Chatや自作の宣言型エージェント(declarative agent)から「連携エージェント」として呼び出せるようにする機能が一般提供(GA)の対象になっている(呼び出されるエージェント側はAgent2Agent、通称A2Aというエージェント間連携プロトコルへの対応が必要)。1つの専門エージェントを全社で作り込み、複数の業務エージェントから使い回せるようになる点が実務上のメリットだが、この仕組み自体の構築・運用はエージェント開発の話題であり、詳細はPart 11(AIエージェント)側で扱う。

## 使いどころ・使い分け

ビジネスパーソンが日常業務で比較検討することが多いChatGPT・Gemini・Claudeとの違いは、「汎用AIとしての賢さ」ではなく「自社のOffice文書・メール・会議データにどれだけ深く食い込めるか」にある。

| 軸 | 強いツール | 理由 |
|---|---|---|
| Word/Excel/PowerPoint/Outlook/Teamsに入っている実データを根拠にした作業(会議の議事録要約、受信箱の整理、既存資料をもとにした資料作成) | Microsoft 365 Copilot | Microsoft Graphによって自分の権限内の社内データを直接参照できるため |
| 複数ステップ・長時間にまたがる定型業務をまるごと任せたい(大量ファイルの横断比較、バージョン差分の洗い出し等) | Microsoft 365 Copilot Cowork | 一問一答のチャットではなく、計画立案から完了までを自律的に実行するために設計されているため |
| 汎用的な調べ物・アイデア出し・雑多な質問への幅広い対応力 | ChatGPT、Claude、Gemini | 学習データ・モデルの汎用的な賢さで先行している場面が多い |
| Google Workspace(Gmail・スプレッドシート等)との連携 | Gemini | GoogleエコシステムとGeminiの統合はMicrosoftの逆パターン |
| 長文の要約・複雑な指示への追従・自律的なコーディング作業 | Claude | 長文コンテキスト処理とコーディングエージェントに強い傾向 |
| 社内のセキュリティ・ガバナンス要件(監査ログ、テナント内へのデータ封じ込め)を重視する大企業での全社導入 | Microsoft 365 Copilot | 既存のMicrosoft 365の権限管理・コンプライアンス基盤をそのまま流用できるため |
| すでにGitHub/VS Codeで開発している組織のコーディング支援 | GitHub Copilot | IDEへの統合度と豊富なコード補完実績 |

判断の目安: 「すでに全社でMicrosoft 365(Word・Excel・Outlook・Teams)を使っていて、その中のデータを扱う作業を効率化したい」ならMicrosoft 365 Copilotが第一候補になる。逆に、社内データに紐づかない一般的な調べ物・文章生成・コーディングであれば、ChatGPT・Claude・Geminiと機能面で大きな差はなく、既存の契約や好みで選んでよい。単発のチャット応答では済まない「丸ごと任せたい定型業務」が繰り返し発生するなら、Copilot Coworkの従量課金コストと削減できる作業時間を比較して導入を検討するとよい。

## 実務での使い方

### 料金プラン(2026年8月時点の目安)

**個人向け:**

| プラン | 月額目安 | 内容 |
|---|---|---|
| Copilot(無料) | $0 | Copilotアプリ・Windows・Edgeで利用可。社内データへのアクセスなし |
| Microsoft 365 Premium | $19.99/月 | Word/Excel/PowerPoint/Outlook/OneNoteでのAI機能、優先的なモデルアクセス、6TBストレージ等を含む個人向け統合プラン。旧「Copilot Pro」の実質的な後継であり、現在は唯一の個人向け有料統合プラン |
| Copilot Pro | 販売終了 | 2025年後半に新規募集を終了し、既存契約者向けの提供も**2026年8月1日にサポート終了済み**。未移行だった場合は速やかにMicrosoft 365 Premiumへ切り替える必要がある |

**法人向け(Microsoft 365 Copilot、要:対象のMicrosoft 365ベースライセンス):**

| プラン | 月額目安(1ユーザーあたり、年払い) | 対象 |
|---|---|---|
| Microsoft 365 Copilot Chat | 追加課金なし | 対象のMicrosoft 365ライセンス保有者は全員利用可(Web中心+簡易エージェント。Word/Excel/PowerPoint/OneNote内での利用は前述の組織規模による制限あり) |
| Microsoft 365 Copilot Business(中小企業向け、300ユーザーまで、アドオン単体) | $18/ユーザー(2026年9月30日までの割引価格、以降は通常価格$21に戻る予定) | Business Basic/Standard/Premiumに追加するアドオン |
| Microsoft 365 Business Standard + Copilot(バンドルSKU) | $23.50/ユーザー(年払い) | ベースライセンス込みの統合プラン |
| Microsoft 365 Business Premium + Copilot(バンドルSKU) | $32/ユーザー(年払い) | ベースライセンス込みの統合プラン。Teams・1TBストレージ・高度なセキュリティ込み |
| Microsoft 365 Copilot(エンタープライズ向け、アドオン単体) | $30/ユーザー(年契約) | E3/E5等のエンタープライズライセンスに追加するアドオン |
| Microsoft 365 Copilot Cowork(利用量課金、要Copilotライセンス) | PayGo方式で1クレジット$0.01。まとめて先払いする「P3」プランなら割引あり | 上記いずれかのMicrosoft 365 Copilotライセンス保有者が追加で使う自律型エージェント。モデル利用・検索・ツール呼び出し・実行時間に応じてクレジットを消費する従量課金 |

Copilotは単体販売されておらず、必ず対象のMicrosoft 365ベースライセンス(Business Basic/Standard/Premium、E3/E5等)を保有したうえでの追加(アドオン)購入になる点に注意。2026年7月1日には、Copilotとは別にMicrosoft 365本体のライセンス価格自体も値上げされている(Business Basicが月$6→$7、Business Standardが月$12.50→$14、E3が月$36→$39、E5が月$57→$60。Business Premiumは月$22で据え置き)。Copilotアドオン($30、エンタープライズ向け)と合算すると、実質負担額はE3契約で月$69程度、E5契約で月$90程度になる。Coworkを使う場合はここにクレジット従量課金が上乗せされる。契約前には必ず[Microsoft公式の料金ページ](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)で最新の金額・条件を確認すること。

**開発者向け(GitHub Copilot、2026年8月時点):**

| プラン | 月額目安 | 内容 |
|---|---|---|
| GitHub Copilot Free | $0 | コード補完は月2,000件まで、モデルは自動選択、機能・利用量に制限 |
| GitHub Copilot Pro | $10/月 | 月$15相当のAI Credits(利用量に応じて消費するクレジット制)込み。コード補完自体は無制限 |
| GitHub Copilot Pro+ | $39/月 | 月$70相当のAI Credits込み、Claude Opus等の上位モデルへのアクセス |
| GitHub Copilot Max | $100/月 | 月$200相当のAI Credits込み。エージェント機能を高頻度で使う開発者向けの新プラン(2026年に新設) |
| GitHub Copilot Business | $19/ユーザー/月 | 組織向け、一元管理・ポリシー制御 |
| GitHub Copilot Enterprise | $39/ユーザー/月 | Business同等機能に加え優先アクセス・大容量のAI Credits |

2026年6月1日からGitHub Copilotは全プランで従量課金制(1 AI Credit = $0.01として、チャット・エージェント利用やCLI等の利用量に応じてクレジットを消費する仕組み)に移行した。コード補完(オートコンプリート)自体はクレジットを消費せず無制限のままだが、チャット・エージェントモードでの利用が多い開発者は、プランに含まれるクレジットを超えると追加課金が発生する点に注意。なお、Business/Enterprise向けには移行措置として2倍のAI Creditsを付与するキャンペーンが実施されているが、こちらは2026年8月末で終了予定のため、対象組織は利用量の見直しを早めに行っておくとよい。

### 社内データの扱い方(commercial data protection)

Microsoft 365 CopilotとMicrosoft 365 Copilot Chat(および利用量課金のCowork)には「Enterprise Data Protection(企業向けデータ保護)」と呼ばれる契約上の保護が適用される。ポイントは以下の4つ。

- **Microsoft Graphによるグラウンディング**: Copilotが回答を作る際、ユーザー本人がアクセス権を持つ範囲のメール・ファイル・チャット・会議データだけをMicrosoft Graph経由で参照する。他人の権限外データは参照されない
- **プロンプト・応答はAIモデルの学習に使われない**: Copilotへの入力(プロンプト)や出力(応答)、Graph経由で読み込んだデータは「顧客データ」として扱われ、基盤モデルの追加学習には使われない契約になっている
- **無料版のCopilotには適用されない**: 無料のCopilot(個人アカウント)にはこの企業向け保護は適用されず、社内データへのアクセスもない。業務で社内文書を扱いたい場合は、必ずMicrosoft 365 Copilot(またはCopilot Chat)を使う必要がある。2026年8月のアプリ統合後も、個人アカウントと組織アカウントのデータ境界はMicrosoft Entraによって維持されるため、この原則自体は変わっていない
- **Copilot Chatの企業向け保護そのものは無料枠でも有効**: 2026年4月以降のWord/Excel/PowerPoint/OneNote内アクセス制限は「利用できるか・品質が落ちるか」の話であり、利用できる範囲においてはCopilot Chat(無料枠)にも引き続きEnterprise Data Protectionが適用される

### 導入時の基本手順の目安

1. 自社のMicrosoft 365契約が対象ライセンス(Business Basic/Standard/Premium、E3/E5等)かをIT管理者に確認する
2. Microsoft 365管理センターで対象ユーザーにCopilotライセンスを割り当てる
3. Word/Excel/PowerPoint/Outlook/Teamsを開くと、リボンやサイドパネルに「Copilot」ボタンが表示されるようになる
4. Teams会議では「レコーディング」をオンにすると、会議後にCopilotへ「今日の決定事項をまとめて」のように指示して議事録を要約できる
5. アプリ統合後にブックマークやマニュアルの`m365.cloud.microsoft`リンクが開かなくなった場合は、`copilot.cloud.microsoft`への切り替えを確認する

## 注意点・よくある誤解

- **「Copilot」という名前だけでは製品を特定できない**: 社内で「Copilotを使って」と言われたら、無料版か、Microsoft 365 Copilotか、Cowork(自律型エージェント)か、GitHub Copilotかを必ず確認する。ライセンス費用も機能も別物である
- **無料のCopilotに社内文書を貼り付けない**: 無料版は社内データへのアクセス権もエンタープライズ向けデータ保護もない。機密情報の要約・分析は必ずMicrosoft 365 CopilotかCopilot Chat(いずれも対象ライセンス保有者向け)で行う。2026年8月のアプリ統合でアイコンや見た目が近づいたため、社員がアカウントの種類(個人か会社か)を見誤りやすくなっている点にも注意が必要
- **Copilot単体では契約できない**: 必ず対象のMicrosoft 365ベースライセンスが前提になるため、見積もりは「アドオン価格」だけでなく「ベースライセンス+アドオン」の合計で比較する
- **Coworkは「基本料金+従量課金」の二段構え**: Microsoft 365 Copilotライセンス自体の月額に加えて、Coworkのタスク実行分はクレジット従量課金が別途かかる。試験導入時はタスクの種類ごとに消費クレジットを記録し、想定外の高額請求を防ぐ
- **料金・呼称の変更頻度が高い**: 2025年後半にCopilot Proが実質Microsoft 365 Premiumに統合され、2026年7月にはMicrosoft 365本体のライセンス価格も値上げ、同年8月にはアプリ自体の統合も始まるなど、短期間で名称・料金体系・UIが変わっている。本ページの数値は目安であり、契約前には必ず公式サイトで確認する
- **「無料で使えるCopilot Chat」の範囲は組織規模で変わる**: 2026年4月15日以降、ユーザー数2,000人超の組織では有料ライセンスなしのWord/Excel/PowerPoint/OneNote内Copilot Chatが使えなくなった。全社導入前に自社の対象人数を確認し、必要な範囲は有料のMicrosoft 365 Copilotライセンスで賄う前提で予算を組む
- **精度は「社内データの整備状況」に左右される**: SharePointやOneDriveのファイル権限・命名規則が乱雑だと、Copilotが正しいデータを見つけられず回答の質が落ちる。導入効果を出すには、Copilot導入前にファイル整理・アクセス権の棚卸しを行うのが実務上のコツ

## 最初の一歩

自社がMicrosoft 365を契約している場合は、Outlookで受信済みの長いメールスレッドを開き、右上の「Copilot」または「まとめる」ボタンで要約を試してみる(Copilot Chatが有効なら追加課金なしで試せる)。個人で試したいだけなら、まずMicrosoft Copilotアプリ(無料)で簡単な文章生成を1つ試すところから始めるとよい。

## 関連トピック

- [Claude(Anthropic)の基本](./claude-basics.md)
- [Google Geminiの基本](./google-gemini-basics.md)

## 更新履歴

### 2026-08-19: アプリ統合・Cowork・GPT-5.6・Agent 365連携を反映して最新化
- **内容**: 2026年8月に始まった個人向けCopilotアプリと法人向けMicrosoft 365 Copilotアプリの統合(アカウント切り替え型の単一アプリ化、アクセスURLの`m365.cloud.microsoft`→`copilot.cloud.microsoft`移行、Deep Research/Podcasts/Group Chat等の個人向け機能終了、データ境界は維持)を「仕組み・背景」に追記。2026年6月16日GAの自律型エージェント「Microsoft 365 Copilot Cowork」(GA時点でAnthropicのClaude Opus 4.8/Sonnet 4.6を採用、PayGo/P3の従量課金)を新しい「Copilot」製品として製品表・料金表・使い分け表に追加。Microsoft 365 Copilotの既定モデルがOpenAIのGPT-5.6に切り替わった点(2026年7月9日)、Agent 365上のエージェントをCopilot Chat・宣言型エージェントから呼び出せる連携機能がGA対象になっている点を追記。Copilot Proのサポート終了(2026年8月1日)を「予定」から「終了済み」に更新。GitHub CopilotのBusiness/Enterprise向け2倍クレジットキャンペーンの終了時期(2026年8月末)を追記
- **出典**: [Microsoft 365 Blog: Copilot Cowork is now generally available](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/16/copilot-cowork-is-now-generally-available/)、[OpenAI: GPT-5.6 is now the preferred model in Microsoft 365 Copilot](https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot/)、[TechCrunch: OpenAI says GPT 5.6 is the 'preferred model' for Microsoft Copilot 365 amid breakup chatter](https://techcrunch.com/2026/07/09/openai-says-gpt-5-6-is-the-preferred-model-for-microsoft-copilot-amid-breakup-chatter/)、[Windows Central: Microsoft begins unified Copilot app rollout](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-begins-unified-copilot-app-rollout-reveals-major-plan-to-merge-copilot-and-microsoft-365-copilot-across-all-platforms-along-with-updated-branding)、[Computerworld: Microsoft brings Copilot apps together ahead of 'super app' overhaul](https://www.computerworld.com/article/4209764/microsoft-brings-copilot-apps-together-ahead-of-super-app-overhaul.html)、[Microsoft Learn: Release notes for Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/release-notes)、[Microsoft Support: About Microsoft Copilot Pro](https://support.microsoft.com/en-us/microsoft-365-copilot/about-microsoft-copilot-pro)

### 2026-07-20: 料金プランとCopilot Chatの無料枠制限を最新化
- **内容**: 2026年4月15日に実施されたユーザー数2,000人超の組織でのWord/Excel/PowerPoint/OneNote内Copilot Chat(無料枠)の利用制限を追記。GitHub Copilotの新プラン「Max」($100/月、$200相当のAI Credits)を追加し、Pro/Pro+のAI Credits金額($15/$70)およびEnterprise価格($39/ユーザー)を実際の数値に訂正。Microsoft 365本体のライセンス価格値上げ(2026年7月1日、Business Basic $6→$7、Business Standard $12.50→$14、E3 $36→$39、E5 $57→$60)とCopilot Businessアドオンの割引期限(2026年9月30日まで)を反映し、法人向け料金表をバンドルSKU価格を含めて更新。Copilot Proの個人向けサポート終了(2026年8月1日)が目前に迫っている旨を強調
- **出典**: [Microsoft公式: Microsoft 365 Copilot Plans and Pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)、[Microsoft 365 Blog: Advancing Microsoft 365: New capabilities and pricing update](https://www.microsoft.com/en-us/microsoft-365/blog/2025/12/04/advancing-microsoft-365-new-capabilities-and-pricing-update/)、[GitHub公式: GitHub Copilot Plans & pricing](https://github.com/features/copilot/plans)、[Office Watch: Microsoft Kills Free Copilot Chat in Word, Excel and PowerPoint: What Happens on April 15](https://office-watch.com/2026/microsoft-removes-copilot-chat-word-excel-powerpoint-april-2026/)、[Computerworld: Microsoft backtracks on Copilot Chat access in M365 apps](https://www.computerworld.com/article/4150022/microsoft-backtracks-on-copilot-chat-access-in-m365-apps.html)

### 2026-07-06: 初版執筆
- **内容**: 「Copilot」を名乗る複数の製品(無料Copilot、Microsoft 365 Copilot Chat、Microsoft 365 Copilot、Copilot Pro/Microsoft 365 Premium、GitHub Copilot、Copilot in Windows)の違いを整理し、2026年7月時点の料金プラン、Microsoft Graphによるグラウンディングとエンタープライズ向けデータ保護の仕組み、ChatGPT/Gemini/Claudeとの使い分けをまとめた
- **出典**: [Microsoft公式: Microsoft 365 Copilot Plans and Pricing](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)、[Microsoft Learn: Enterprise data protection in Microsoft 365 Copilot and Microsoft 365 Copilot Chat](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection)、[Microsoft Learn: Decide which Copilot is right for you](https://learn.microsoft.com/en-us/microsoft-365/copilot/which-copilot-for-your-organization)、[GitHub公式: GitHub Copilot Plans & pricing](https://github.com/features/copilot/plans)、[GitHub Blog: GitHub Copilot is moving to usage-based billing](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)、[Microsoft Community Hub: Act Now: Lock in Current Pricing on Microsoft 365 Copilot Business Bundles](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/act-now-lock-in-current-pricing-on-microsoft-365-copilot-business-bundles/4502628)
