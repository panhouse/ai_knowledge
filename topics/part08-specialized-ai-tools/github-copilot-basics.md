---
title: "GitHub Copilotの基本(コーディング支援AI)"
part: 8
chapter: 第2章 コーディング支援AI
tags: [GitHub Copilot, コーディング支援AI, AIエディタ, 開発生産性]
created: 2026-07-06
updated: 2026-07-20
---

# GitHub Copilotの基本(コーディング支援AI)

## これは何か

GitHub Copilot(ギットハブ・コパイロット)は、Microsoft傘下のGitHubが提供するAIコーディング支援ツールである。もともとは「次に書きそうなコードを予測して自動補完する」機能だけだったが、対話しながらコードを書く「Chat」、指示を出すと複数ファイルを自律的に編集する「Agent Mode」、GitHub上のIssue(課題管理チケット)を丸ごと任せられる「Copilot coding agent」まで機能が広がり、今では「開発チームのAIプラットフォーム」と呼べる規模になっている。

非エンジニアの決裁者にとっての困りごとは、「エンジニアが当たり前のように使っているCopilotやCursorが何をするツールで、いくらかかり、他社製品と何が違うのか判断材料がない」ことだ。本ページはコードが書けなくても、価値・料金・選定基準がわかることを目的にする。

## 仕組み・背景

### 機能進化の経緯

1. **コード補完(2021年10月 一般提供開始)**: エディタでコードを書いていると、次の1行〜数行をグレーの薄字で提案し、Tabキーで確定する。OpenAIのCodexモデルをベースにスタートした。
2. **Copilot Chat(2023年)**: エディタ内のサイドパネルでAIと対話しながら、コードの説明・バグ修正・テスト生成などを依頼できるようになった。ChatGPTのコーディング版をエディタに埋め込んだイメージ。
3. **Agent Mode(2024〜2025年)**: 「このAPIを使うようにログイン機能を実装して」のような大きな指示を出すと、AIが複数ファイルを横断して編集し、ターミナルコマンドを実行し、エラーが出れば自分で修正するというループを自律的に回す。人間は都度の細かい指示ではなく、最終確認とレビューに専念できる。
4. **Copilot coding agent(自律型コーディングエージェント)**: GitHub上のIssue(不具合報告や機能要望のチケット)に人間の代わりに「Copilot」をアサインすると、クラウド上のサンドボックス環境で自律的に調査・実装し、ドラフトのプルリクエスト(コード変更の提出物)を作成する。CI(自動テスト)の結果やレビューコメントを見て自己修正し、完了したら人間に通知する。
5. **マルチエージェント化(2025年後半〜)**: GitHub上でCopilot自身のエージェントだけでなく、Anthropic の Claude や OpenAI の Codex など**サードパーティのエージェントも同じ画面から呼び出して働かせられる**ようになった。進捗管理用の「Copilot デスクトップアプリ」で、複数エージェントの作業状況を一元的に追跡・レビュー・マージできる(旧「Copilot Workspace」の発展形)。2026年7月には、このデスクトップアプリがFreeプランを含む**全プランで無料利用可能**になり、さらに「BYOK(Bring Your Own Key、自分のAPIキーを持ち込む)」を使えば、Copilotのサブスクリプション自体を契約せずに自前のAnthropic・OpenAI・Ollamaなどのモデルでアプリを動かすことも可能になった。

### 使えるAIモデル

Copilotは自社専用モデルに縛られず、Anthropic Claude、OpenAI GPT系、Google Geminiなど複数のモデルから用途に応じて選べる「モデル選択」の仕組みを持つ。速度重視・精度重視・コスト重視で使い分けられる点は、単一モデルしか使えないツールとの差別化ポイントになっている。2026年7月には、自社ホスト以外の「オープンウェイトモデル(重みが公開されており自由に検証・改変できるモデル)」として Moonshot AI の「Kimi K2.7 Code」がモデル選択肢に初めて加わった。低コストな選択肢として使えるが、Business/Enterpriseでは管理者が設定でオプトインするまで既定で無効になっており、セキュリティ・コンプライアンス上のレビューを経てから有効化することが推奨されている。

### 料金の仕組み(2026年6月に大きく変更)

Copilotは2026年6月1日から、それまでの「プレミアムリクエスト(高性能モデルを使うたびに1回分を消費する権利)」制度を廃止し、**AI Credits(AIクレジット)による従量課金**に全面移行した。1クレジット=0.01米ドルで、利用したモデルと消費したトークン数(入力・出力・キャッシュ分すべて含む)に応じてクレジットが差し引かれる仕組みである。コード補完とNext Edit Suggestions(次の編集箇所の提案)はどのプランでもクレジットを消費しない。各プランには毎月一定額のクレジットが含まれており、使い切ると追加購入(従量課金)になる。組織向けプランでは、複数ユーザー分のクレジットをプールして融通できる。

なお、既存のBusiness/Enterprise契約者には移行の激変緩和として、2026年6月〜8月の3か月間は通常より多いクレジット(Businessは月3,000クレジット、Enterpriseは月7,000クレジット相当)が付与される販促措置が取られている。2026年9月以降は本記事の表にある通常付与量(Business 1,900クレジット、Enterprise 3,900クレジット)に戻るため、予算計画を立てる際はこの点を織り込んでおく必要がある。Agentモードでの大規模な自律編集やOpusなどプレミアムモデルの多用はクレジット消費が大きく、実際に「請求額が想定の数十倍に跳ね上がった」という利用者報告も出ている。管理者は組織設定でユーザーごとの利用上限(スペンドリミット)を必ず設定しておくことが望ましい。

## 使いどころ・使い分け

### そもそも導入すべきか

| 状況 | 判断の目安 |
|---|---|
| 定型的なコードを書く量が多い(CRUD処理、テストコード等) | 補完だけでも効果が出やすい。まずFree/Proで様子見 |
| 仕様が曖昧な大きな機能を任せたい | Agent Mode・coding agentが有効。ただしレビュー体制が前提 |
| 社内に複数のIDE・エディタが混在 | Copilotは対応範囲が広く、統一しやすい |
| 特定モデル(Claude Codeなど)への強いこだわりがある | Copilot経由でも呼び出せるが、専用ツールの方が最適化されている場合がある |
| セキュリティ・監査要件が厳しい(金融・官公庁等) | Business/Enterpriseの管理機能やIP補償を確認してから判断 |

### 料金プラン(個人向け、2026年7月時点)

| プラン | 月額(1人あたり) | コード補完 | チャット・Agent | 含まれるAI Credits | 特徴 |
|---|---|---|---|---|---|
| Free | 0ドル | 月2,000件まで | 月50リクエストまで(Copilot Edits含む) | なし | Claude Haiku 4.5、GPT-5 miniなど利用可。クレジットカード不要。Agent Modeも試用可 |
| Pro | 10ドル | 無制限 | 無制限(付属クレジット消費) | 15ドル分 | モデル選択可。クラウドエージェント・コードレビュー機能付き。Claude・Codexなど外部エージェントも利用可 |
| Pro+ | 39ドル | 無制限 | 無制限(付属クレジット消費) | 70ドル分 | Opusなどプレミアムモデルにアクセス可。監査ログあり。Proの4倍超の利用枠 |
| Max | 100ドル | 無制限 | 無制限(付属クレジット消費) | 200ドル分 | 新モデル・新機能への優先アクセス。Pro+の2.9倍超の利用枠 |

### 料金プラン(組織向け、2026年7月時点)

| プラン | 月額(1人あたり) | 含まれるAI Credits | 特徴 |
|---|---|---|---|
| Business | 19ドル | 1,900クレジット分 | IDE・CLI・GitHub Mobileでの利用が中心。組織のポリシー管理、IP(知的財産)補償あり |
| Enterprise | 39ドル | 3,900クレジット分(GitHub Enterprise Cloud限定) | Businessの全機能に加え、自社コードベースのインデックス化、モデルのファインチューニング(追加学習によるカスタマイズ)、新機能への優先アクセス |

いずれのプランを超過利用した場合は1クレジット=0.01ドルで従量課金される(管理者は利用上限を設定可能)。価格・クレジット付与量は変更が入りやすいため、契約前に必ず公式ページ(github.com/features/copilot/plans)で最新値を確認すること。

### 対応IDE・エディタ

Visual Studio Code、Visual Studio、JetBrains系IDE(IntelliJ IDEA等)、Neovim、Xcode、Eclipse、Raycast、GitHub CLI(ターミナル)など、主要な開発環境をほぼ網羅している。社内のエディタが統一されていなくても導入しやすいのが強みである。

### 競合ツールとの違い

| ツール | 提供元 | 位置づけ | 特徴 |
|---|---|---|---|
| GitHub Copilot | GitHub(Microsoft) | 既存IDEへの後付け拡張機能 | GitHub本体(Issue・PR)との統合が深い。複数モデル・複数エージェントを横断管理できる。企業導入実績・ガバナンス機能が豊富 |
| Cursor | Anysphere | AI専用に作られた独立エディタ(VS Codeから派生) | エディタ全体がAI前提で設計されており、複数ファイル編集(Composer)の完成度が高い。個人開発者評価が高い。2026年6月にSpaceXが買収を発表(全株式取得・約600億ドル規模、2026年第3四半期に完了予定)しており、今後の製品方針変更に注意 |
| Devin Desktop(旧Windsurf) | Cognition | AI専用の独立エディタ | 2026年6月にCognitionの「Devin」ブランドへ統合され、旧来の自社エージェント「Cascade」は同年7月にRust製の新エージェント「Devin Local」へ置き換え。外部エージェント(Codex、Claude Agent等)を同一エディタ内で動かせる共通規格「ACP(Agent Client Protocol)」を採用 |
| Cline | オープンソースコミュニティ | VS Code拡張機能(OSS) | 無料・オープンソースで、好きなAIモデルを自分で接続できる(BYOM = Bring Your Own Model)。コスト重視・カスタマイズ重視の開発者に支持される |

いずれも「自律的にコードを編集するAgent」を持つ点は共通しており、差は「既存IDEへの後付けか専用エディタか」「自社モデルか複数モデル選択か」「GitHub本体との統合の深さ」にある。社内で複数ツールを併用しているケースも多い。なお、AI専用エディタ勢は2026年に入り買収・ブランド統合が相次いでおり(Cursor→SpaceX、Windsurf→Cognition/Devin)、業界再編の途上にあることも選定時の判断材料になる。

## 実務での使い方

### エンジニアがCopilotを使う典型的な場面

- 定型的なコード(APIのエンドポイント、テストコード、設定ファイル)を書く時間を削減する
- 使ったことのないライブラリの使い方をChatで聞きながら実装する
- バグ報告のIssueをそのままCopilot coding agentにアサインし、調査・修正・PR作成まで任せて、人間はレビューだけ行う
- プルリクエストの自動コードレビュー(Copilotのコードレビュー機能は、Copilotライセンスを持たないメンバーのPRに対しても組織設定で有効化できる)

### 導入判断のポイント(非エンジニアの管理職向け)

- **生産性向上のエビデンス**: GitHub自身の調査ではタスク完了速度が最大55%向上したとの報告がある一方、独立した第三者調査(2025年時点)では、AIが関与したコードでコードクローン(重複コード)が増加した、AIが関与したPRでレビュー指摘が多くなったといった報告もある。効果はコードベースの複雑さやレビュー体制の有無に大きく左右されるため、「導入すれば必ず生産性が上がる」と単純化せず、自社での試験導入(パイロット)で効果を測ることが望ましい
- **セキュリティ・ライセンス面の懸念**: AIが生成したコードは、人間が書いたコードと同等かそれ以上の頻度で脆弱性を含みうるとの研究がある。生成コードをレビューせずにそのままマージする運用はリスクが高い。また、学習データに起因するライセンス上のリスクに備え、Business/Enterprise以上のプランではIP(知的財産)補償が提供される点も契約時の確認材料になる
- **コード品質への影響**: 「早く書けるが、後から読みにくい・保守しにくいコードが増える」というのが実務上よく指摘される懸念点である。コードレビューのルールやAI生成コードの検証プロセスを、導入と同時に整備することが重要
- **組織の管理機能**: 利用状況の可視化、利用モデルの制限、監査ログ、IP補償など、組織として統制を効かせたい場合はBusiness以上を検討する

## 注意点・よくある誤解

- **「Copilot=コード補完ツール」という理解は古い**: 現在はAgent Modeやcoding agentにより、仕様の一部を丸ごと任せられる「自律型の開発パートナー」に近づいている。導入検討時は補完機能だけでなくAgent機能の価値も評価対象に入れるべき
- **料金プランの前提が2026年6月に大きく変わった**: 「プレミアムリクエスト◯回まで」という従来の説明は既に古く、現在は「AI Credits(トークン消費に応じた従量課金)」が基準になっている。古い記事やスライドの料金説明を鵜呑みにしない
- **「付属クレジット分だけ」と油断しない**: Agentモードやプレミアムモデル(Opusなど)の多用は消費するクレジットが大きく、想定外の超過課金につながりやすい。特にBusiness/Enterpriseの2026年6〜8月の販促クレジットは9月以降通常量に戻るため、9月以降の実利用量を早めに見積もり、管理者は利用上限(スペンドリミット)を設定しておく
- **無料プランでも侮れないが、業務利用ならProから検討**: Freeプランは月2,000件の補完・50件のチャットという制限があり、日常的な開発業務にはやや心許ない。個人の業務利用ならProが最低ライン
- **生成コードのレビューを省略しない**: Agent機能が「自律的に動く」ことと「レビュー不要」であることはイコールではない。特にセキュリティに関わる部分(認証・権限・外部通信)は人間のレビューを必須にする
- **Cursor等の専用エディタとは共存できる**: 「会社としてCopilotを契約している=他のツールを使ってはいけない」ではない。エンジニアが個人の裁量でCursorやClineを併用しているケースは多く、ライセンス費用の重複よりも生産性を優先する判断がされることもある。管理職としては「なぜそのツールを使っているか」を一度エンジニアに聞いてみると実態がつかみやすい

## 最初の一歩

まずはGitHubアカウントで無料プランを有効化し(クレジットカード不要)、社内エンジニアに「Agent Modeとcoding agentを実際の小さなタスクで試してもらい、体感を1分で共有してもらう」ことから始めるとよい。

## 関連トピック

- [MCP(Model Context Protocol)の基本](../part09-api-development/mcp-basics.md)
- [ローカルLLMの基本(自社PC・サーバーで動かす生成AI)](local-llm-basics.md)

## 更新履歴

### 2026-07-20: モデル・料金・競合動向を最新化
- **内容**: オープンウェイトモデル「Kimi K2.7 Code」のモデル選択肢への追加、Copilotデスクトップアプリの全プラン無料化とBYOK対応、Business/Enterprise向け販促クレジット(2026年6〜8月)と超過課金リスクの注意点、CursorのSpaceXによる買収発表・WindsurfのDevin Desktopへのブランド統合という競合動向を反映して本文を更新
- **出典**: [Kimi K2.7 Code is generally available in GitHub Copilot - GitHub Changelog](https://github.blog/changelog/2026-07-01-kimi-k2-7-is-now-available-in-github-copilot/), [Kimi K2.7 now available for Copilot Business and Enterprise - GitHub Changelog](https://github.blog/changelog/2026-07-07-kimi-k2-7-now-available-for-copilot-business-and-enterprise/), [GitHub Copilot app available to all - GitHub Changelog](https://github.blog/changelog/2026-07-07-github-copilot-app-available-to-all/), [SpaceX to acquire the AI coding startup Cursor for $60 billion - CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html), [Windsurf is now Devin Desktop - Devin(Cognition公式ブログ)](https://devin.ai/blog/windsurf-is-now-devin-desktop), [GitHub Copilot is moving to usage-based billing - The GitHub Blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)

### 2026-07-06: 初版執筆
- **内容**: GitHub Copilotの機能進化(コード補完→Chat→Agent Mode→自律型coding agent)、2026年6月の従量課金(AI Credits)移行後の最新料金プラン、Cursor/Windsurf/Clineとの比較、非エンジニア向けの導入判断ポイントをまとめた初版を執筆
- **出典**: [GitHub Copilot Plans & pricing](https://github.com/features/copilot/plans), [GitHub Copilot is moving to usage-based billing - The GitHub Blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/), [Does GitHub Copilot improve code quality? - The GitHub Blog](https://github.blog/news-insights/research/does-github-copilot-improve-code-quality-heres-what-the-data-says/), [AI Coding Agents 2026 comparison - Lushbinary](https://lushbinary.com/blog/ai-coding-agents-comparison-cursor-windsurf-claude-copilot-kiro-2026/)
