---
title: "Windsurfの基本(コーディング支援AI)"
part: 8
chapter: 第2章 コーディング支援AI
tags: [Windsurf, Devin Desktop, Cascade, コーディング支援AI, AIエディタ, Cognition]
created: 2026-07-06
updated: 2026-07-06
---

# Windsurfの基本(コーディング支援AI)

## これは何か

Windsurf(ウィンドサーフ)は、AIによる自律的なコード編集を前提に作られた**スタンドアロンのコードエディタ**である。土台はMicrosoftのVS Code(オープンソースのコードエディタ)を分岐(フォーク)して作られており、GitHub Copilotのような「既存エディタへの後付け拡張機能」ではなく、エディタそのものがAI専用に設計されている点が特徴である。目玉機能は「Cascade(カスケード)」と呼ばれるエージェント機能で、指示を出すとコードベース全体を理解した上で複数ファイルを横断編集し、ターミナルコマンドの実行やエラー修正までを自律的に行う。

まず押さえておくべき最重要事項がある。開発元Cognition(コグニション)社は2026年6月2日、Windsurfを自社の看板エージェント「Devin(デビン)」ブランドに統合し、**製品名を「Devin Desktop」に変更した**。旧Cascadeも後継の「Devin Local」に置き換えられ、旧Cascadeは2026年7月1日に提供終了(EOL)している。つまり本ページ執筆時点(2026年7月)では「Windsurf」という名称自体が過去のものになりつつある。社内でツール選定の相談を受ける立場としては、この名称変更を知らずに古い記事やスクリーンショットを参考にすると混乱するため、本ページでは旧称「Windsurf」で解説しつつ、随所で現在の呼称「Devin Desktop」を併記する。

## 仕組み・背景

### Cascadeというエージェント機能

Cascade(現Devin Local)は、単発のコード補完ではなく「タスクの完了」を目的に動くエージェントである。以下のような処理を自律的に連鎖(カスケード)させる。

- コードベース全体を自動的に読み込み、関連する箇所を自分で探し出す(手動でファイルをタグ付けする必要が少ない)
- 複数ファイルにまたがる変更を一度に提案・適用する
- ターミナルコマンドを実行し、テストやビルドのエラーを見て自分で修正する
- 変更前に承認を求める「Write Mode」と、確認なしで進める設定など、人間の介在度を選べる

### 買収の顛末(2025〜2026年)

Windsurfを開発したCodeium社は2025年、複数の大手から争奪戦の対象になった。

1. **OpenAIとの買収交渉(2025年5月〜)**: OpenAIがWindsurfを約30億ドルで買収する契約を結んだが、独占交渉権の期限だった2025年7月11日までに取引が成立せず、契約は失効した。背景には、OpenAIの出資者であるMicrosoftが2030年まで持つ「OpenAIが獲得した知財への閲覧権」をWindsurf側が拒んだ事情があったと報じられている。
2. **Google DeepMindによる人材・技術のライセンス取得**: 交渉決裂の直後、GoogleがWindsurfのCEOだったVarun Mohan氏や共同創業者、主要研究者を引き抜き、約24億ドルでWindsurfの技術をライセンス供与する契約を結んだ。これは会社そのものの買収ではなく、人材とライセンスの取得である。
3. **Cognitionによる会社(製品)の買収(2025年7月〜12月)**: 経営陣が抜けた後、自律コーディングエージェント「Devin」で知られるCognition社が、Windsurfの製品・ブランド・残った従業員を買収した(報道額は約2.5億ドル)。以降、Windsurfの開発はCognitionの下で継続された。

### Cognition傘下での進化とDevin Desktopへの統合(2026年)

Cognitionは買収後、自社のコーディング専用モデル「SWE-1」シリーズを投入し、高速版の「SWE-1.5」「SWE-1.6」をWindsurfに組み込んだ。あわせて、コードベースの構造を図として可視化する「Codemaps(コードマップ)」、大規模コードベースから関連コードを高速検索する「Fast Context」といった独自機能を追加した。

そして2026年6月2日、Cognitionは自動更新を通じてWindsurfを「Devin Desktop」として再出荷した。既存ユーザーの設定・契約プラン・拡張機能・キーバインドはそのまま引き継がれている。主な変更点は以下の通り。

- Cascadeの後継として、Rustで書き直された新しいローカルエージェント「Devin Local」を搭載
- ローカルとクラウド上のエージェント作業を一覧管理する「Agent Command Center(カンバン形式の管理画面)」が標準搭載
- Anthropic Claude Agent、OpenAI Codexなど他社エージェントも同じエディタ内で動かせる業界標準プロトコル「ACP(Agent Client Protocol)」に対応

## 使いどころ・使い分け

### そもそも導入すべきか

| 状況 | 判断の目安 |
|---|---|
| 大規模・複雑なコードベースをAIに理解させたい | Codemapsやコードベース全体理解の仕組みが強み。向いている |
| 既存のJetBrains・Vimなど複数エディタを使い分けている | 40以上のIDE向けプラグインも提供しているが、本領はスタンドアロン版。エディタ統一に抵抗がなければ検討 |
| 金融・医療など高い規制・監査要件がある | SOC 2 Type II、HIPAA、FedRAMP High(米国政府向け)などの認証を持ち、クラウド/ハイブリッド/自社運用(セルフホスト)を選べる。要件が厳しい組織にも選択肢がある |
| Cursorを既に契約していて乗り換えを迷っている | 機能・価格帯はほぼ同水準。決定的な差はコードベース理解のアプローチとエコシステム。無料枠で両方試して相性を見るのが早い |
| ライセンス費用をかけずAIコーディングを試したい | まずはCline(無料・OSS・API従量課金のみ)やCopilotの無料プランを検討する余地もある |

### 料金プラン(2026年7月時点)

Windsurf(Devin Desktop)は2026年3月19日に、それまでの「クレジット消費制」を廃止し、**日次・週次のクォータ(利用上限)制**に移行した。Cascade(現Devin Local)にメッセージを送るたびにクォータが消費される。

| プラン | 月額 | 主な内容 |
|---|---|---|
| Free | 0ドル | 軽めの日次・週次クォータ(目安として週2〜3日分程度の利用量)。Tab補完は無制限 |
| Pro | 20ドル | 標準クォータ(日次・週次でリセット)。SWE-1.6、Claude Sonnet系、GPT-5系、Gemini系など主要モデルを選択可。Tab補完・インライン編集(Command)は無制限 |
| Teams | 40ドル(1人あたり) | Proの内容に加え、一括請求・利用状況の管理者向け分析・優先サポート |
| Max | 200ドル | 大容量クォータ。CursorのUltraプランやClaude Codeの上位プランと同格の重量級ユーザー向け |
| Enterprise | 個別見積り | SSO・RBAC(権限管理)、ハイブリッド/自社運用、SOC 2・HIPAA・FedRAMP High等の認証、監査ログなど組織向け機能一式 |

料金・クォータの基準は改定が入りやすいため、契約前に必ず公式サイト(windsurf.com、または統合先のdevin.ai)の最新情報を確認すること。

### 競合ツールとの比較

| ツール | 提供元 | 位置づけ | 特徴 |
|---|---|---|---|
| Windsurf(現Devin Desktop) | Cognition | AI専用スタンドアロンエディタ(VS Codeフォーク) | Cascade→Devin Localによる自律編集。自社モデル(SWE-1.6等)、Codemapsによるコードベース可視化。SOC 2/HIPAA/FedRAMP対応で規制業種にも強い |
| Cursor | Anysphere | AI専用スタンドアロンエディタ(VS Codeフォーク) | 複数ファイル編集(Composer)・専用エージェントワークスペースの完成度が高い。個人開発者からの評価が高い |
| GitHub Copilot | GitHub(Microsoft) | 既存IDEへの後付け拡張機能 | 40種以上のIDE・エディタに対応。GitHub本体(Issue・PR)との統合が深い |
| Cline | OSSコミュニティ | VS Code拡張機能(オープンソース・無料) | ツール自体は無料でAPIキーを自分で用意するBYOM方式。コスト・カスタマイズ重視の開発者向け(詳細は別ページ参照) |

Windsurf/Devin DesktopとCursorはどちらも「AI専用に作られたエディタ」という点で似ているが、思想には違いがある。Cursorは「隣に座って提案してくるアシスタント」に近く、必要なときに呼び出す使い方が主。Windsurf/Devin Desktopは「共著者」に近く、コードベース全体を自動で読み込んで先回りし、任せれば人間の指示が少なくても作業を進める設計が強調される。GitHub Copilotは既存の開発環境を変えずに導入できる点が最大の強みで、Clineは費用を抑えつつモデルを自由に選びたい場合の選択肢になる。

## 実務での使い方

### 導入手順

1. 公式サイト(windsurf.com。2026年6月以降はdevin.aiのDevin Desktopページに統合されている)からOS(Windows/Mac/Linux)に応じたインストーラをダウンロードする
2. 初回起動時のオンボーディング画面で、「新規に始める」「VS Codeから設定を取り込む」「Cursorから設定を取り込む」のいずれかを選ぶ。VS Codeからの移行を選ぶと、拡張機能・キーバインド・settings.jsonなどが自動で引き継がれる(移行前にVS Code本体は終了しておく)
3. GitHubアカウントまたはメールでログインし、プラン(Free/Pro等)を選択する
4. 画面右側に表示される「Cascade」パネル(Devin Local移行後の名称も同パネル)がAIとの対話窓口になる。ここにチャット形式で指示を出す

### 初期設定の場所

- **モデル選択**: Cascadeパネル上部のモデル切り替えメニューから、SWE-1.6・Claude・GPT系・Gemini系などを都度選べる
- **プロジェクト固有のルール**: プロジェクトのルートフォルダに `.windsurfrules` ファイルを置くと、コーディング規約やスタックの前提知識をAIに常時渡せる(いわゆるカスタム指示)
- **MCP(外部ツール連携)設定**: Cascadeパネル右上の「MCP」アイコン→「Configure」から設定ファイル(`~/.codeium/windsurf/mcp_config.json`、Windowsは`%USERPROFILE%\.codeium\windsurf\mcp_config.json`)を編集するか、内蔵マーケットプレイスから追加する

### 典型的な使い方

- レガシーな大規模コードベースに初めて触るとき、Codemapsで構造を可視化してから着手する
- 「このAPI仕様に沿って認証機能を実装して」のような大きめの指示をCascade(Devin Local)に出し、複数ファイルの変更・テスト実行・エラー修正までを一括で任せ、人間は差分レビューに専念する
- 規制業種で自社サーバー内にコードを留めたい場合、Enterpriseプランのハイブリッド/セルフホスト構成を検討する

### 導入判断のポイント(非エンジニアの管理職向け)

- **ツール名の変遷に注意**: 社内で「Windsurf導入検討」という話が出ている場合、それが指すのは実質的に現在の「Devin Desktop」である。見積りや資料の日付が2026年6月以前なら価格・機能が古い可能性が高い
- **Cursorとの機能差は縮まっている**: 2026年の料金改定でPro同士は同額(20ドル)になり、機能面の差は「コードベース理解の自動化度」「認証・デプロイ形態の柔軟さ」に絞られてきている。単純な値段比較だけで選ばず、実際にエンジニアに両方触ってもらうのが最も確実
- **企業導入なら認証・データ保持設定を確認**: 有料プランはデフォルトでゼロデータ保持(コードを学習に使わない設定)だが、リモートインデックスやメモリ機能を有効化すると挙動が変わる。契約前にデータ保持ポリシーを必ず確認する

## 注意点・よくある誤解

- **「Windsurf」は現在「Devin Desktop」という名称**: 2026年6月2日の自動更新で名称が変わっており、旧Cascadeは2026年7月1日に提供終了している。今後、既存ユーザーの画面表示や公式ドキュメントは「Devin Desktop」「Devin Local」に統一されていくため、社内資料も更新しておくとよい
- **買収の経緯が複雑なため、現在の運営会社を誤解しやすい**: OpenAIが買収する予定だったが決裂し、Googleは技術のライセンス取得と人材引き抜きのみを行い、会社(製品)自体を買収したのはCognitionである。現在Windsurf/Devin DesktopはOpenAIともGoogleとも資本関係はなく、Cognitionの製品ラインの一部である
- **「AI専用エディタ=乗り換えが大変」ではない**: VS Codeフォークであるため、拡張機能・設定・キーバインドの移行はほぼワンステップで済む。乗り換えのハードルは思ったより低い
- **自律的に動くこととレビュー不要は別**: Cascade/Devin Localが複数ファイルを一括変更しても、認証・権限・外部通信に関わる差分は人間のレビューを必須にする運用が望ましい
- **料金比較は改定タイミングに注意**: 2026年3月にクレジット制からクォータ制に変わっており、それ以前の記事の「クレジット○○回まで」という説明は既に古い

## 最初の一歩

まずはFreeプランでDevin Desktop(旧Windsurf)をインストールし、既存のVS Code設定を取り込んで、社内の小さな修正タスク1件をCascade(Devin Local)に任せてみて、Cursorや使用中のGitHub Copilotとの手触りの違いをエンジニアから1分で共有してもらうとよい。

## 関連トピック

- [GitHub Copilotの基本(コーディング支援AI)](github-copilot-basics.md)
- [ローカルLLMの基本(自社PC・サーバーで動かす生成AI)](local-llm-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: AI専用エディタWindsurfの基本機能(Cascade)、OpenAI買収交渉決裂→Google DeepMindによる人材・ライセンス取得→Cognitionによる会社買収という経緯、2026年6月のDevin Desktopへの改称とCascade終了(2026年7月1日EOL)、2026年3月のクォータ制移行後の最新料金プラン、Cursor/GitHub Copilot/Clineとの比較を含む初版を執筆
- **出典**: [OpenAI's $3 billion deal with AI coding startup Windsurf collapses - Fortune](https://fortune.com/2025/07/11/the-exclusivity-on-openais-3-billion-acquisition-for-coding-startup-windsfurf-has-expired/), [Windsurf's CEO goes to Google; OpenAI's acquisition falls apart - TechCrunch](https://techcrunch.com/2025/07/11/windsurfs-ceo-goes-to-google-openais-acquisition-falls-apart/), [Windsurf is now Devin Desktop - Devin(Cognition公式blog)](https://devin.ai/blog/windsurf-is-now-devin-desktop/), [Windsurf Codemaps: Understand Code, Before You Vibe It - Cognition](https://cognition.com/blog/codemaps), [Windsurf Pricing 2026: Plans, Quotas & What Changed - Verdent](https://www.verdent.ai/guides/windsurf-pricing-2026), [Windsurf vs Cursor - 公式比較ページ](https://windsurf.com/compare/windsurf-vs-cursor), [Cascade MCP Integration - Devin Docs](https://docs.windsurf.com/windsurf/cascade/mcp)
