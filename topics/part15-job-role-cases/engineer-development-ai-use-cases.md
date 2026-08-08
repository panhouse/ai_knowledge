---
title: エンジニア・開発職における生成AI活用事例
part: 15
chapter: 第11章 エンジニア・開発
tags: [ソフトウェア開発, コードレビュー, DORA, セキュリティ, 技術的負債, スキル低下]
created: 2026-08-06
updated: 2026-08-06
---

# エンジニア・開発職における生成AI活用事例

## これは何か

GitHub Copilot・Cursor・Claude Code・OpenAI Codexといったツール自体の機能や選び方は[Part 8: 特化型AIツール](../part08-specialized-ai-tools/_index.md)の「コーディング支援AI」章にすでに整理されている。本ページはツールの説明を繰り返さず、**ソフトウェア開発のライフサイクル(SDLC)のどの工程にAIが組み込まれているか**、そして**チームとして品質・セキュリティ・技術的負債をどう担保するか**という運用側の論点に絞って整理する。「AIにコードを書かせれば速くなる」という単純な話ではなく、「レビューの負担がどこに移り、何を人が見なければならないか」を具体的な数字とともに押さえることが、開発チームを率いる立場にとって特に重要になる。

## 仕組み・背景

生成AIは2025年前後から、コード生成だけでなくSDLCの複数工程に組み込まれるようになった。特徴的な変化が2つある。

1. **「仕様書ドリブン開発」への揺り戻し**: 思いつきでプロンプトを打ってコードを生成させる「vibe coding」への反省から、AIエージェントに渡す前に構造化された仕様書を書く手法が急速に広がった。GitHubの「Spec Kit」やAWSの「Kiro」はEARS記法(Easy Approach to Requirements Syntax、要件を「When〈条件〉, the system shall〈振る舞い〉」の形で書く記法)で要件→設計→タスク分解の順に整理してからコード生成に入る。メルカリも独自の「Agent Spec Driven Development(ASDD)」を推進しており、要件を先に固めてからエージェントに実装させる流れが実務の主流になりつつある([出典](https://engineering.mercari.com/blog/entry/20251209-d0de07214d/))。
2. **レビューの主戦場が「構文」から「意図・アーキテクチャ適合性」に移る**: スタイルや構文的な誤りはAI自身やリンターが検出できるため、人間のレビューは「このコードはなぜこう書かれているか」「設計として妥当か」という判断に集中させる、という再配分がチーム運用の共通認識になりつつある。

生産性への影響については、Google Cloud/DORAの2025年版レポート(公式)が重要な知見を示している。AI利用率は90%(前年比+14ポイント)に達し、80%超が生産性向上を実感、59%がコード品質への好影響を報告した一方、**AI導入は開発スループットとは正の相関、安定性(信頼性)とは負の相関**という結果も出ている。同レポートは「AIは増幅器である(強いチームはより強く、弱いチームは問題が増幅される)」と総括しており、AIを入れれば自動的に良くなるわけではなく、元々のチームの開発プラクティスの質が結果を左右することを示している([出典](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report))。

## 使いどころ・使い分け

### SDLC工程別のAI活用マップ

| 工程 | 主なタスク | AIの向き・不向き | 人が必ず見るべきこと |
|---|---|---|---|
| 要件・仕様策定 | 仕様書のドラフト作成、EARS記法での要件整理 | 向く(たたき台作成) | ビジネス要件との整合性 |
| コード生成 | 実装、既存コードの拡張 | 向く(定型パターンほど速い) | ロジックの妥当性、意図との一致 |
| コードレビュー | AIによる一次レビュー、人間コードのチェック | 向く(機械的なチェックの一次フィルタ) | アーキテクチャ適合性、セキュリティ、意図 |
| テスト生成 | ユニットテスト・テストケースのドラフト | 向く(定型的なテストの網羅) | 境界値・異常系の網羅性、テストの意味 |
| 障害調査・ログ解析 | アラート要約、過去インシデントの自然言語検索 | 向く(大量ログの一次整理) | 原因特定の妥当性、対応の緊急性判断 |
| レガシー解析・モダナイゼーション | 処理フローの可視化、移行計画のたたき台 | 向く(理解の補助)。一括の全面書き換え提案は要警戒 | 段階移行計画の妥当性、影響範囲の見落とし |

### 「AIが書いたコード」をどこまで信用するか

判断の軸は「認証・決済・インフラ・データマイグレーション・公開API・個人情報(PII)関連の変更は必ず人間のサインオフを要求し、低リスクな変更のみ自動化の余地を検討する」というリスクベースの区分けである。多くの実務記事がこの発想を共通して推奨している([出典](https://www.metacto.com/blogs/establishing-code-review-standards-for-ai-generated-code))。

## 実務での使い方

### 1. AI利用の開示ルールを決める(OSSコミュニティの動きが参考になる)

オープンソースコミュニティでは「AIがどこまで書いたか」を明示する規約の標準化が急速に進んでいる。

- **Linuxカーネル**: `Assisted-by:` トレーラーでAI利用を記録。AIエージェントは法的にDCO(Developer Certificate of Origin、コードの出所を保証する仕組み)を証明できないため、`Signed-off-by:` タグの付与自体を禁止している
- **Electron**: 同様に `Assisted-by:` トレーラーでの開示を推奨
- **一部プロジェクト**: 「完全AI生成(人間はレビューのみ)」「主にAI生成(人間が大幅修正)」「主に人間執筆(AIは補助のみ)」の3段階で開示するプロジェクトもある

調査対象118件のAI利用ポリシーのうち51%(60件)が開示を必須化しているという報告もあり([出典](https://allthingsopen.org/articles/open-source-ai-contributions-assisted-by-git-trailer-standard))、社内開発でも「PRの説明欄にAI生成箇所を明記する」「AIエージェントが作成したPRにはラベルを付ける」といった最小限のルールを決めておくと、後からレビュー負担の分析や品質トラブルの切り分けがしやすくなる。

### 2. コピペで使えるプロンプト例

**PR説明文の自動生成**

```
以下のdiffを読み、次の5項目でPR descriptionを日本語で作成してください。

1. 変更の目的(なぜこの変更が必要か)
2. 主な変更点(箇条書き)
3. 影響範囲(他モジュール・APIへの波及有無)
4. テスト観点(どのように動作確認したか・すべきか)
5. レビュアーへの確認事項(特に注意して見てほしい箇所)

【diff】
(貼り付け)
```

**多観点でのコードレビューチェックリスト**

```
以下のPull Requestを、次の4観点でレビューしてください。
1. セキュリティ(入力値検証、権限チェック、機密情報のログ出力有無)
2. パフォーマンス(不要なループ・N+1クエリ等)
3. 可読性(命名、関数の責務分割)
4. 既存コーディング規約との整合性

指摘は重要度(High/Medium/Low)で分類し、Highは必ず理由を添えてください。
なお、このレビューは一次チェックであり、最終承認は人間のレビュアーが行います。

【対象コード・差分】
(貼り付け)
```

**レガシーコードのモダナイゼーション計画(一括書き換えを防ぐ指示つき)**

```
このコードベースの主要な処理フローを整理してください。以下の順で提案し、
一度に全面書き換えを提案しないでください。

1. 技術的負債のリスト(何が古い設計か・なぜ問題か)
2. 影響範囲マップ(変更が波及しうる箇所)
3. 段階的な移行計画(小さく安全に分割したステップ)
4. 各ステップで実施すべきテスト戦略

【対象コード】
(貼り付け)
```

### 3. 国内企業の活用実例

- **メルカリ**: 2025年8月5日の決算説明会で、社内AIツール利用率95%、開発量64%増を公表([出典](https://type.jp/et/feature/28981/))
- **LayerX**: CTOがClaude Code + Claude 4の組み合わせを高く評価し、エンジニア全員にClaude Maxアカウントを支給。1人あたり1日200ドル相当の利用でも生産性向上効果があると判断している([出典](https://tech.layerx.co.jp/entry/2025/06/05/161631))
- **DMM**: 2025年7月、Claude Code ActionでPRの自動承認フローを構築([出典](https://developersblog.dmm.com/entry/2025/12/02/110000))

## 注意点・よくある誤解

- **「構文的に正しい」と「安全」は別物**: Veracodeの2025年GenAI Code Security Reportによると、100以上のLLM・80のコーディングタスクを分析した結果、**AI生成コードの45%にセキュリティ脆弱性**が含まれていた。構文的な正解率は95%超に達している一方、セキュリティの合格率は約55%で、この2年ほぼ横ばいという結果も報告されている([出典](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/))。「動くコード」と「安全なコード」は別の基準で検証する必要がある。
- **AI生成コードへの過信ギャップ**: Snykの調査では、開発者の75%が「AI生成コードの方が人間のコードより安全」だと信じている一方、実際にはAI生成コードの48%が安全でないという結果が出ている。AI生成コードをスキャンしている開発者はわずか10%にとどまるとも報告されている([出典](https://snyk.io/blog/ai-code-generation-code-security-quality-benefits-risks-top-tools/))。「AIが書いたから安全だろう」という思い込みを捨て、静的解析ツール(SCA)との併用を徹底する。
- **パッケージハルシネーションによるサプライチェーン攻撃リスク**: AIが存在しないOSSパッケージ名を提案し、それを悪意ある第三者が実際に登録して配布する攻撃手法が指摘されている。AIが提案した依存パッケージは、追加する前に実在と信頼性を確認する。
- **著作権・ライセンスリスク**: GitHub Copilotを巡る集団訴訟が2022年11月から進行中で、生成コードが学習データと構造・変数名・コメント等で実質的に類似する場合、元コードの著作権者の許諾が必要になりうるとの指摘がある。マイクロソフトは2023年10月から「Copilot著作権コミットメント」(Business/Enterpriseプラン限定、コンテンツフィルター有効化が条件で訴訟対応費用を負担)を提供しているが、個人・無料プランはこの補償の対象外である点に注意する([出典](https://levtech.jp/media/article/column/detail_340/))。
- **スキルの空洞化(オーバーリライアンス)**: Anthropic自身が2026年に発表した研究では、ジュニアPython開発者を対象にしたランダム化比較試験で、AIにコードを丸投げする使い方をした群は理解度テストのスコアが17ポイント低下した一方、「概念について質問する」使い方をした群は65%超のスコアを維持した。丸投げか、対話しながら理解を深めるかで、スキル形成に明確な差が出ることを示している([出典](https://www.anthropic.com/research/AI-assistance-coding-skills))。新人・若手には特に「答えだけをコピーさせない」運用が重要になる。
- **開発ツールの権限モデルは製品ごとに思想が異なる**: Claude Codeは「Allow/Ask/Deny」の3段階権限とサンドボックス機能を持つ「開発者が都度制御する」設計、Devinのような自律型エージェントは「複数日がかりの作業を自律的に計画してPRを出す」設計というように、どこまで人の承認を挟むかの思想が製品によって異なる。どの製品を使うかに関わらず、認証情報・本番デプロイへの書き込み権限は組織側で別途ガードレールを設ける必要がある(権限設計・監査ログの詳細は[AIエージェント運用のガバナンス設計](../part11-ai-agents/ai-agent-governance-basics.md)を参照)。

## 最初の一歩

直近のPRを1つ選び、上記の「多観点でのコードレビューチェックリスト」プロンプトをそのまま試してみる。AIの指摘のうち「High」に分類されたものだけを実際にレビュー観点として使えるか確認し、まずは低リスクな変更からAIレビューを一次フィルタとして併用する運用を検討する。

## 関連トピック

- [コーディング支援AIの選び方・比較(Cursor・GitHub Copilot・Cline・Windsurf)](../part08-specialized-ai-tools/coding-assistant-ai-comparison.md)
- [Claude Codeの基本](../part11-ai-agents/claude-code-basics.md)
- [AIエージェント運用のガバナンス設計(権限ポリシー・監査ログ・コスト管理)](../part11-ai-agents/ai-agent-governance-basics.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)
- [プロンプトの検証・反復改善の進め方](../part05-prompt-engineering/prompt-testing-and-iteration.md)

## 更新履歴

### 2026-08-06: 初版執筆
- **内容**: Part 15第11章「エンジニア・開発」の未執筆枠として、SDLC工程別のAI活用マップ、仕様書ドリブン開発(Spec Kit・Kiro・メルカリASDD)、AI利用開示規約(Linuxカーネル等OSSの`Assisted-by`トレーラー)、PR説明文・コードレビュー・レガシー解析のプロンプト例、DORA 2025レポートの生産性指標、Veracode/Snykのセキュリティリスク統計、著作権・スキル低下リスクを整理
- **出典**: [Google Cloud Blog: 2025 DORA report](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report)、[メルカリEngineering: Agent Spec Driven Development](https://engineering.mercari.com/blog/entry/20251209-d0de07214d/)、[Veracode 2025 GenAI Code Security Report](https://www.veracode.com/resources/analyst-reports/2025-genai-code-security-report/)、[Snyk: AI code generation risks](https://snyk.io/blog/ai-code-generation-code-security-quality-benefits-risks-top-tools/)、[Anthropic: AI assistance and coding skills](https://www.anthropic.com/research/AI-assistance-coding-skills)、[All Things Open: AI disclosure trailer standard](https://allthingsopen.org/articles/open-source-ai-contributions-assisted-by-git-trailer-standard)、[エンジニアtype: メルカリ決算説明会](https://type.jp/et/feature/28981/)、[LayerX Tech Blog](https://tech.layerx.co.jp/entry/2025/06/05/161631)
