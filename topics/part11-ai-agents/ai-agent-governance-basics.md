---
title: AIエージェント運用のガバナンス設計(権限ポリシー・監査ログ・コスト管理)
part: 11
chapter: 第5章 運用・ガバナンス
tags: [AIエージェント, ガバナンス, 権限管理, 監査ログ, コスト管理, プロンプトインジェクション]
created: 2026-08-06
updated: 2026-08-06
---

# AIエージェント運用のガバナンス設計(権限ポリシー・監査ログ・コスト管理)

## これは何か

Claude Code・GitHub Copilotのコーディングエージェント・Google Antigravity・Claude Coworkのような「委任型」のAIエージェント製品は、導入すること自体は簡単だが、**どこまで承認なしで動かせるようにするか**を決めないまま使い始めると、意図しないファイル削除・機密情報の送信・想定外のコスト発生といった事故につながる。本ページは、各製品が実際にどんな権限設定・監査ログ・コスト管理の機能を持っているか、そして企業として何を追加で決めておくべきかを整理する。個別ツールの基本機能は[Claude Codeの基本](claude-code-basics.md)等の各論ページに譲り、ここでは**運用として何を設計すべきか**に絞る。

## 仕組み・背景

AIエージェントのガバナンスが必要になる理由は単純で、エージェントは「チャットに答えるだけ」の生成AIと違い、**実際にファイルを編集し、コマンドを実行し、時にはメール送信や決済のような取り消せない操作まで行う**ためである。OWASP(Webアプリケーションセキュリティの国際コミュニティ)が2025年12月に公開した「Top 10 for Agentic Applications 2026」は、この分野のリスクを整理した業界標準的なチェックリストで、**「最小権限の原則(principle of least agency)」**――エージェントに与える自律性・ツールアクセス・認証情報のスコープを、その作業に必要な最小限にとどめる――を軸に据えている([出典](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/))。

ガバナンス設計は大きく3つの要素に分かれる。

1. **権限ポリシー**: どの操作を自動実行してよく、どこで人の承認を挟むか
2. **監査ログ**: 誰が・いつ・何を実行したかを後から追跡できるか
3. **コスト管理**: エージェントはチャットの数倍〜数十倍のトークンを消費しうるため、使いすぎをどう防ぐか

これに加えて、エージェントがWebページやメール・ドキュメントを自律的に読み込む場合は、悪意ある指示が紛れ込む「間接プロンプトインジェクション」というエージェント特有のセキュリティリスクも生じる(詳細は後述)。

## 使いどころ・使い分け

### 主要製品の権限モデル比較(2026年8月時点)

| 製品 | 権限の仕組み | 企業向けロックダウン機能 |
|---|---|---|
| Claude Code | `default`(都度確認)/`acceptEdits`(編集は自動承認)/`plan`(読み取り専用で調査のみ)/`bypassPermissions`(全スキップ)のモード。ツールごとに`allow`/`ask`/`deny`ルールを`settings.json`で設定可能 | 管理設定(`allowManagedPermissionRulesOnly`)でIT部門のルールのみを強制、`bypassPermissions`モード自体を組織単位で無効化する設定もある([出典](https://code.claude.com/docs/en/settings)) |
| OpenAI Codex CLI | 「サンドボックス(read-only/workspace-write/danger-full-access)」と「承認方針(untrusted/on-request/never)」の2軸で制御 | 組織のポリシーで既定値を固定可能。OpenAI社内では機械的な「Auto-review」が本来必要な人手レビューの約99%を自動承認しているとの報告もある(自社内トラジェクトリでの測定値、2026年3月時点、[出典](https://alignment.openai.com/auto-review/)) |
| GitHub Copilot コーディングエージェント | リポジトリ/組織単位でのファイアウォール(既定で有効、アウトバウンド通信を許可リストに制限) | 組織管理者がファイアウォール・許可リストを組織全体に強制可能(2026年4月〜)。エージェントは自分が作ったPRを自己承認できない設計で、本番デプロイはGitHub Actionsの環境保護ルール(必須レビュアー、自己承認禁止)で別途ゲートする([出典](https://github.blog/changelog/2026-04-03-organization-firewall-settings-for-copilot-cloud-agent/)) |
| Google Antigravity | 「Allow/Ask/Deny」の3段階をファイル操作・URL/ブラウザ操作・MCP接続それぞれに適用する「統一権限システム」。「Ask」では承認前にスコープを編集できる | プロジェクト単位で権限のデフォルトを継承・上書き([出典](https://antigravity.google/blog/google-io-2026-feature-deep-dive)) |
| Claude Cowork | 機能単位のオン/オフが中心で、Claude Codeほど細かい行動単位の許可・拒否ルールはない | Teamプランはグループ・カスタムロール単位で機能制限、Enterpriseは組織全体でのオン/オフ切り替え。決済・契約更新・削除・外部投稿など高リスク操作は、製品側の自動区分がないため、どのフォルダ・コネクタ・ブラウザ操作範囲を与えるかを**人間があらかじめ線引きする**運用が実務では推奨されている |

### 何を自動実行させ、何を人の承認に残すか

判断の軸は「取り消せるか、取り消せないか」である。ファイルの下書き作成・調査・ドラフト生成のような**やり直しが効く操作**は自動化の余地があるが、削除・送信・課金・本番環境へのpush・契約行為のような**取り消せない操作**は、必ず人の承認を残す。

## 実務での使い方

### 1. 権限ポリシーの最小設計(小さな企業でもすぐ決められる項目)

- **自動承認してよい操作**: ファイルの読み取り、ドラフト作成、ローカル環境でのテスト実行
- **都度確認させる操作**: ファイルの上書き・削除、外部ネットワークへのアクセス、Gitへのpush
- **原則禁止する操作**: 本番データベースへの書き込み、決済・契約行為、社外への一括送信

Claude Codeであれば、これを`settings.json`に次のような形で書ける(実際のプロジェクト構成に応じて調整する)。

```json
{
  "permissions": {
    "allow": ["Read(*)", "Bash(npm test)"],
    "ask": ["Edit(*)", "Bash(git push*)"],
    "deny": ["Bash(rm -rf*)", "Read(./.env)"]
  }
}
```

### 2. 監査ログの最低ライン

各製品が提供する監査ログの粒度には差がある。導入前に「誰が・いつ・何を実行したか、事後に追跡できるか」を確認しておく。

- **Claude Enterprise**: 認証イベント・モデル呼び出し・ファイル操作を記録する監査ログ(Admin Consoleで既定30日保持、JSON/CSVエクスポートやSIEM連携が可能)に加え、認証・組織管理・ロール変更・APIキーのライフサイクルなどを網羅する専用の「Compliance API」を提供している。ただし2026年5月時点でClaude Coworkの操作ログはこのCompliance APIの対象外とされており、詳細な追跡が必要な場合は別途の記録手段(OpenTelemetry連携等)を検討する必要がある([出典](https://platform.claude.com/docs/en/manage-claude/compliance-api))
- **GitHub Copilot**: エージェントが作成したコミットには`Agent-Logs-Url`という形でセッションログへのリンクが自動的に付与される。2026年7月には、クラウドエージェント・CLI・各種IDEのセッション記録をSIEMへストリーミングできる機能がパブリックプレビューとして公開された([出典](https://github.blog/changelog/2026-07-02-copilot-agent-session-streaming-is-now-in-public-preview/))
- **Microsoft Copilot Studio**: Microsoft Purviewと連携した監査ログ・保持ポリシー管理に加え、開発→ステージング→本番の段階的デプロイと本番昇格前の承認必須化、稼働中エージェントの一覧・利用状況・コンプライアンス状態を可視化する管理ダッシュボードを提供している([出典](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance))

### 3. コスト管理の勘所

エージェントはサブエージェントの並列実行や長時間のループにより、通常のチャット利用より大幅に多いトークンを消費する。具体的な倍率は情報源によってばらつきが大きく(数倍〜数十倍という記述が複数あるが、いずれも一次のベンチマーク資料までは確認できていない)、正確な倍率を断定するより「エージェントは想定より大幅にコストがかさむ前提で予算設計する」姿勢が重要になる。

- **Anthropic Console**: 組織・ワークスペース単位でRPM(1分あたりのリクエスト数)やトークンレートの上限を設定でき、利用階層(Start/Build/Scale/Custom)ごとに月次の支出上限が設定されている。管理者はユーザー・ワークスペース単位の支出上限や、閾値に達した際のアラートを設定できる([出典](https://tygartmedia.com/anthropic-console-developer-guide-2026/))
- **OpenAI(ChatGPT Enterprise)**: 2026年6月18日に管理コンソールの分析・支出管理機能が拡張され、製品・モデル・ユーザー単位の利用状況の可視化、部門・グループ単位でのデフォルト利用上限の設定、上限超過時に理由を添えて追加枠を申請できるフローが追加された([出典](https://openai.com/index/chatgpt-enterprise-spend-controls/))
- 現時点では、主要なエージェント製品のいずれも「実行前にドル建ての予算上限で自動停止する」機能は一般的でなく、トークン消費は事後的に観測・集計する形が主流である。この点を踏まえ、「使ってみてから決める」のではなく、事前にレート制限・支出アラートを設定してから展開するのが実務上のリスク低減策になる。

### 4. サンドボックス化と本番環境の分離

複数のエージェントを並行して動かす場合、Gitのワークツリー(作業ディレクトリを分けて複数ブランチを同時に扱う仕組み)は手軽だが、OSパッケージや環境変数、認証情報は共有されたままのため、**セキュリティ境界にはならない**点に注意が必要である。より確実な分離が必要な場合は、コンテナ単位での分離(ファイルシステム・プロセス・ネットワークを個別に隔離する仕組み)を追加で組み合わせる。本番環境への書き込み権限は、GitHub Actionsの環境保護ルールのように「必須レビュアーの設定」「自己承認の禁止」を製品側の機能として設定できる仕組みを活用するのが、現時点で最も具体的に実装しやすい方法の1つである。

### 5. 間接プロンプトインジェクションへの備え

エージェントがWebページやメール・ドキュメントを自律的に読み込む場合、そのコンテンツに人間には見えない(CSSで隠す、ゼロサイズのフォントを使う、HTMLコメント内に埋め込む等の)悪意ある指示が仕込まれ、エージェントがそれに従ってしまうリスクがある(間接プロンプトインジェクション)。ReAct型のエージェントを対象にした研究では、こうした攻撃が24〜47%の確率で成功したという報告もある([出典](https://www.sentinelone.com/cybersecurity-101/cybersecurity/indirect-prompt-injection-attacks/))。対策の基本は「エージェントがどの情報源を信頼できる指示として扱ってよいか」を制限する設計であり、Webブラウジングや外部ドキュメント読み込みを許可する範囲は、業務上必要な最小限にとどめる。

### 日本国内の動向

経済産業省・総務省は2026年3月31日に「AI事業者ガイドライン」の第1.2版を公表したとされ、複数の解説記事によれば、AIエージェント(環境を認識し自律的に目標に向けて行動するAIシステム)を業務に委任する前に、**対象業務・操作範囲・承認者・ログ保存方法**を明記した申請を行い、情報システム責任者の承認を得ることを求める内容が盛り込まれたと報じられている(本文の正確な条文は一次資料での確認を推奨する)。国内企業の実例としては、LINEヤフーが2023年の経営統合時に「AI倫理ガバナンス部門」を新設し、人事総務領域のAI活用ではこの部門と各事業部門が業務内容・データの機微性・影響範囲に応じて利用可否を判断する体制を敷いている([出典](https://www.lycorp.co.jp/ja/sustainability/esg/social/responsible-ai/))。

## 注意点・よくある誤解

- **「エージェント製品にガバナンス機能がある」と「組織にガバナンス体制がある」は別**: 各製品はそれぞれの安全機能(権限モード、ファイアウォール、監査ログ)を持つが、それらを組み合わせて「誰が・どの業務で・どこまでの権限を与えるか」を決める全体設計は、製品が代わりにやってくれるわけではない。自社で権限ポリシーの一覧表を作り、定期的に見直す運用が必要になる。
- **「サンドボックス」という言葉の粒度に注意する**: Gitワークツリーによる分離とコンテナによる分離は、どちらも「サンドボックス」と呼ばれることがあるが、安全性のレベルが大きく異なる。前者は複数エージェントの作業衝突を防ぐ程度の分離であり、認証情報の漏洩やホスト環境への影響を防ぐセキュリティ境界にはならない。
- **コスト超過は「気づいたら上限に達していた」形で起きやすい**: 多くの製品は事前のドル建て予算上限で自動停止する機能を持たないため、レート制限・支出アラートを事前に設定し、想定外の高額請求を防ぐ運用を怠らない。
- **監査ログの対象範囲を過信しない**: 製品によっては特定の機能(例: Claude Coworkの操作)が標準の監査ログ・コンプライアンスAPIの対象外になっているなど、「ログを取っているつもりが実は取れていない」領域が存在しうる。導入前に監査ログの対象範囲を必ず確認する。
- **「自律的にできる」という宣伝文句をそのまま信じない**: 各社のマーケティングは自律性の高さを強調しがちだが、実際にどこまで人の確認なしで進められるかは、権限設定・組織のリスク許容度次第で変わる。導入時は保守的な設定から始め、実績を見ながら緩めていく方が事故が少ない。

## 最初の一歩

自社で使っている(または導入予定の)エージェント製品について、「取り消せない操作(削除・送信・課金・本番デプロイ)」を1つ書き出し、それが自動承認の対象になっていないか設定を確認する。なっていた場合は、都度確認(ask)または禁止(deny)に変更する。

## 関連トピック

- [Claude Codeの基本](claude-code-basics.md)
- [主要AIエージェントの比較と選び方](ai-agent-tools-comparison.md)
- [AIエージェントとは何か](ai-agent-basics.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)
- [生成AI利用コストの管理・予算配分](../part12-business-practice/ai-cost-management-and-budgeting.md)

## 更新履歴

### 2026-08-06: 初版執筆
- **内容**: Part 11第5章「運用・ガバナンス」の未執筆枠として、Claude Code・OpenAI Codex・GitHub Copilotコーディングエージェント・Google Antigravity・Claude Coworkの権限モデル比較、監査ログの実装状況(Claude Compliance API、GitHub Agent-Logs-Url等)、コスト管理(Anthropic Console・OpenAI管理コンソールの支出制御)、サンドボックス化と本番分離、間接プロンプトインジェクションへの備え、AI事業者ガイドライン第1.2版・LINEヤフーの国内動向を整理
- **出典**: [OWASP Top 10 for Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)、[Claude Code Docs: Settings](https://code.claude.com/docs/en/settings)、[GitHub Changelog: Organization firewall settings](https://github.blog/changelog/2026-04-03-organization-firewall-settings-for-copilot-cloud-agent/)、[GitHub Changelog: Agent session streaming](https://github.blog/changelog/2026-07-02-copilot-agent-session-streaming-is-now-in-public-preview/)、[Claude Platform Docs: Compliance API](https://platform.claude.com/docs/en/manage-claude/compliance-api)、[Microsoft Learn: Security and governance in Copilot Studio](https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-and-governance)、[OpenAI: New usage analytics and spend controls for enterprises](https://openai.com/index/chatgpt-enterprise-spend-controls/)、[SentinelOne: Indirect Prompt Injection](https://www.sentinelone.com/cybersecurity-101/cybersecurity/indirect-prompt-injection-attacks/)、[LY Corporation: 責任あるAIへの取り組み](https://www.lycorp.co.jp/ja/sustainability/esg/social/responsible-ai/)
