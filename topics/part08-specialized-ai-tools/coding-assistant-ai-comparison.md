---
title: "コーディング支援AIの選び方・比較(Cursor・GitHub Copilot・Cline・Windsurf)"
part: 8
chapter: 第2章 コーディング支援AI
tags: [Cursor, GitHub Copilot, Cline, Windsurf, Devin Desktop, コーディング支援AI, ツール選定]
created: 2026-07-30
updated: 2026-09-15
---

# コーディング支援AIの選び方・比較(Cursor・GitHub Copilot・Cline・Windsurf)

## これは何か

コーディング支援AIとは、コードエディタ・IDE(統合開発環境)の中でAIが自動補完・対話・自律的な複数ファイル編集を行うツールの総称である。代表格のCursor・GitHub Copilot・Cline・Windsurf(現Devin Desktop)は、それぞれ個別ページ([Cursorの基本](cursor-basics.md)・[GitHub Copilotの基本](github-copilot-basics.md)・[Clineの基本](cline-basics.md)・[Windsurfの基本](windsurf-basics.md))で詳しく解説しているが、「結局どれを契約すればいいのか」を判断するには4つを並べて見る必要がある。

本ページは4ツールを同じ軸(料金・使えるモデル・自律度・エディタ形態・対象ユーザー)で横並びにし、「自社・自分にはどれが合うか」を決める材料に絞って提供する。用途カテゴリそのものの選び方(検索特化AI・画像生成AIなど他カテゴリとの比較)は[特化型AIツールの選び方](specialized-ai-tools-selection-guide.md)を参照してほしい。本ページはコーディング支援AIというカテゴリの中の詳細な一騎討ち比較に特化する。

## 仕組み・背景

### 4ツールに共通する進化の方向性

いずれのツールも、当初は「次の1行を予測するコード補完」から出発し、現在は「自然言語の指示で複数ファイルを自律的に編集し、ターミナルコマンドの実行・エラー修正までループさせるエージェント」へと進化している。違いが生まれるのは主に次の3点である。

1. **エディタとの関係**: 既存IDEに後付けする「拡張機能」型(GitHub Copilot・Cline)か、VS Codeを土台にAI専用に作り直した「独立エディタ(フォーク)」型(Cursor・Windsurf/Devin Desktop)か
2. **使えるAIモデル**: 自社モデルのみか、複数ベンダーのモデルを選べるか、自分のAPIキーを持ち込むBYOK(Bring Your Own Key)方式か
3. **料金構造**: 月額固定+クレジット/クォータ消費型か、ツール自体は無料でAI利用料が実費で発生するBYOK型か

### 業界再編が進行中(2025〜2026年)

このカテゴリは2025〜2026年にかけて大型M&Aが相次ぎ、2026年9月時点でさらに動きが加速している。WindsurfはOpenAIによる買収交渉が2025年7月に決裂した後、Google DeepMindが技術・人材をライセンス取得し、最終的にCognition社(自律エージェント「Devin」の開発元)が製品を買収、2026年6月2日に「Devin Desktop」へ改称した。

Cursorの開発元Anysphere社については、2026年6月16日に発表されたSpaceXによる約600億ドル規模(株式交換)での買収が**2026年8月14日に正式完了**し、Cursorは新設された「SpaceXAI」部門の傘下に入った。さらに2026年8月28日、OpenAIはこの買収を理由に「SpaceXが利用規約の範囲内で技術を使うと確信できない」として、Cursorへのモデル提供契約を**2026年11月12日付で終了する**と通告した(Cursor CEOによれば、OpenAIモデルの利用は同社トラフィックの5%程度)。個人のAPIキー持ち込みで一部は代替できる見込みだが、全ての利用形態をカバーできるわけではないとされる。買収後はxAI(Grok)との連携も強まっており、Cursor自身が「Grok」ブランドのモデルを学習・提供する動きも出ている。つまりこのカテゴリは「今の運営元・使えるモデル・料金が数か月後も同じとは限らない」前提で選定する必要があり、特にCursorは2026年11月以降のOpenAIモデル依存度に注意が必要である。

### 市場シェア・評価の目安(2026年時点の各種調査)

JetBrains Developer Ecosystem Survey(開発者1万人超対象、2026年)によれば、利用シェアはGitHub Copilot 29%・Cursor 18%・Claude Code 18%程度とされる。別のベンダー系集計ではCopilotが有料契約者数で最大手(約470万人、前年比75%増)、Cursorは年換算収益(ARR)ベースで約20億ドル・有料ユーザー100万人超とされる一方、開発者の「最も気に入っているツール」ではClaude Codeが46%、Cursorが19%、Copilotが9%という調査もあり、「契約者数の多さ」と「満足度の高さ」は必ずしも一致しない。同調査ではエンジニアの70%が2〜4種類のAIコーディングツールを併用し、15%は5種類以上を使うとの結果もある。数字は調査方法によって振れ幅が大きいため、参考値として捉え、自社での試用結果を最優先すべきである。

## 使いどころ・使い分け

### 比較表(2026年9月時点)

| 項目 | Cursor | GitHub Copilot | Cline | Windsurf(現Devin Desktop) |
|---|---|---|---|---|
| 提供元 | SpaceXAI(旧Anysphere。2026年8月14日にSpaceXが買収完了し新設部門の傘下に) | GitHub(Microsoft) | オープンソースコミュニティ(Cline Bot Inc.) | Cognition(2025年にWindsurfを買収、2026年6月にDevin Desktopへ改称) |
| エディタ形態 | 独立エディタ(VS Codeフォーク)。JetBrainsにはACP経由でエージェントチャットのみ対応 | 既存IDEへの拡張機能(VS Code・JetBrains・Visual Studio・Neovim・Xcode等30種以上) | 既存IDEへの拡張機能(VS Code・JetBrains、OSS) | 独立エディタ(VS Codeフォーク)。40以上のIDE向けプラグインも提供 |
| 使えるモデル | Anthropic Claude・Google Gemini・xAI Grok+自社モデル(Composer 2.5・Fusion)。**OpenAIモデルは2026年11月12日にOpenAI側の都合で提供終了予定**(買収を理由にOpenAIが契約解除を通告)。Autoで自動選択も可 | Anthropic Claude・OpenAI GPT・Google Gemini・xAI Grok+オープンウェイトのKimi K2.7 Code・Kimi K3(2026年8月GA、Business/Enterprise対応、要管理者オン設定) | 30以上のプロバイダーから自分で選択・接続(BYOK)。Anthropic・OpenAI・Gemini・AWS Bedrock・GCP Vertex・Groq・Cerebras・DeepSeek・ローカルLLM(Ollama等)も可 | 自社モデルSWE-2+Claude・GPT・Gemini・Grok・Kimi・DeepSeekなど多数のモデルを選択可 |
| 個人向け最低額(有料) | Pro 20ドル/月 | Pro 10ドル/月(月15ドル分のAI Credits付属) | 0ドル(ツール自体は永続無料。AI利用料は実費) | Pro 20ドル/月 |
| 個人向け中間・最上位 | Pro+ 60ドル/月、Ultra 200ドル/月 | Pro+ 39ドル/月(2026年7月に20ドルから値上げ、AI Credits70ドル分)、Max 100ドル/月(AI Credits200ドル分) | チーム利用時20ドル/月(最初の10席は無料)+実費 | Max 200ドル/月、Teams 80ドル/月+開発者1人あたり40ドル |
| 法人向け(1ユーザー/月) | Teams 40ドル(標準)〜120ドル(プレミアム)、Enterprise個別見積 | Business 19ドル(AI Credits19ドル分)、Enterprise 39ドル(AI Credits39ドル分)。2026年6月にAI Credits制へ移行(旧Premium Request Unitsを廃止)、8月末に導入期のプロモーション分が終了し付属クレジットが縮小 | Enterprise個別見積(SSO・SLA・一元請求) | Teams・Enterprise個別見積 |
| 自律度(エージェント機能) | Agent/Composerによる複数ファイル自律編集、Background/Cloud Agent、Automations(常時稼働) | Agent Mode+Copilot coding agent(Issueへのアサイン、GA済)、Copilot CLIのAutopilotモード(2026年2月GA)、Agent HQ(Anthropic・OpenAI・Google・Cognition・xAI各社のエージェントを1つのCopilot契約で横断管理) | Plan/Actモードで人間承認を挟みやすい設計。オートアプルーブ(自動承認)やCI/CDでの自律実行も選択可 | Cascade→Devin Localによる自律編集、Agent Command Center(カンバン管理画面) |
| GitHub本体との統合 | 中(Cloud AgentがIssue→PR作成) | 強い(Issueアサイン・PR自動作成・エージェント型コードレビューが標準機能、Agent HQで他社エージェントも統合) | 弱い(拡張機能単体) | 中 |
| 規制・監査対応 | Business/EnterpriseでSOC 2 Type II | Business/EnterpriseでIP補償・SCIM | 利用するAIプロバイダー側の契約に依存 | SOC 2・HIPAA・FedRAMP High・セルフホスト対応 |
| 向いているユーザー | 新規プロトタイプを高速に作りたい個人・スタートアップ(ただしOpenAIモデル依存度が高い場合は要注意) | 社内エディタが混在、GitHub中心の開発フロー、企業ガバナンス重視 | コストを使った分だけに抑えたい、モデル選定の自由度を重視する開発者 | 大規模コードベースの理解を自動化したい、規制業種でセルフホストが必要 |

### 判断フローチャート(考え方の目安)

- **「まず何を最優先するか」で絞り込む**
  - GitHubのIssue・PR管理と一体化したい → GitHub Copilot
  - AIモデルを自分で選び、使った分だけ払いたい(コスト管理を厳密にしたい) → Cline
  - ゼロから新規アプリ・プロトタイプを高速に作りたい → Cursor
  - 大規模・複雑な既存コードベースをAIに理解させ、規制業種でセルフホストも検討したい → Windsurf(Devin Desktop)
- **社内のエディタ統一状況で絞り込む**
  - 複数のIDEが混在していて統一しない前提 → GitHub Copilot(対応範囲が最も広い)
  - VS Code系への統一に抵抗がない → Cursor・Windsurfも選択肢に入る
- **予算の立て方で絞り込む**
  - 「月いくら」と固定額で管理したい → Cursor・Copilot・Windsurfの月額プラン
  - 使った分だけ払い、モデルごとにコストを配分したい → Cline(BYOK)
- **併用も現実的な選択肢である**: 2026年の開発者調査でも複数ツールを併用する回答が多い(JetBrains調査ではエンジニアの70%が2〜4種類を併用)。「会社としてCopilotを契約しつつ、エンジニアが個人裁量でCursorやClineを併用する」というケースは珍しくない。1つに絞り込む前に、パイロット導入で複数を並行比較するのも有効
- **特定モデルへの依存度で絞り込む**: OpenAIのGPT系モデルを主力にしたい場合、Cursorは2026年11月12日にOpenAIモデルの提供が終了予定である点に注意する。GPT系を使い続けたいならGitHub Copilot・Cline(BYOKで直接契約)・Windsurf(Devin Desktop)が選択肢になる

## 実務での使い方

### コピペで使える実例:プロジェクト共通指示ファイルの書き方

いずれのツールも「プロジェクトごとのコーディング規約・注意事項をファイルに書いておき、AIに常時参照させる」仕組みを持つ。ツールによってファイル名は異なるが、書く内容の型は共通化できる。以下はそのまま使える雛形である。

```markdown
## プロジェクトについて
- Webアプリのバックエンド(言語: TypeScript、フレームワーク: NestJS)
- 本番相当のコードベースであり、動作確認なしのコードは提出しない

## コーディング規約
- 命名はキャメルケース、ファイル名はケバブケース
- 外部APIを呼ぶ処理は必ずtry-catchでエラーハンドリングする
- テストコードのないPRは作成しない(Jestで最低1ケース追加)

## やってはいけないこと
- .envファイルや認証情報を含むファイルを編集・出力しない
- package.jsonの依存関係を勝手にアップグレードしない
- 本番用データベースへの直接接続コードを書かない

## レビュー観点として重視してほしいこと
- 認証・権限・外部通信に関わる差分は変更理由をコメントで明記する
```

このテキストを保存する場所はツールごとに異なる。

| ツール | 保存場所 |
|---|---|
| Cursor | `.cursor/rules/` 配下にファイルとして配置(バージョン管理可) |
| GitHub Copilot | リポジトリ直下の `.github/copilot-instructions.md` |
| Cline | プロジェクト直下の `.clinerules` |
| Windsurf(Devin Desktop) | プロジェクト直下の `.windsurfrules` |

### 手順の例:GitHub Copilotで組織のガバナンスを効かせる設定(画面の場所)

1. ブラウザでGitHubの組織ページを開き、「Settings」→左メニューの「Copilot」→「Policies」に進む
2. 「Copilot coding agent」「サードパーティモデルへのアクセス」「オープンウェイトモデル(Kimi K2.7 Code・Kimi K3等)の利用可否」を組織単位でオン/オフする(オープンウェイトモデルは既定でオフ、管理者が有効化するまでメンバーは選択できない)
3. 「Settings」→「Billing」→「Spending limits」で、AI Credits(2026年6月にPremium Request Unitsから移行した従量課金の単位。1クレジット=0.01ドル、トークン消費量に応じて課金)の月間上限を設定する(想定外の超過課金を防ぐ。2026年8月末に導入期のプロモーション分が終了し、Business/Enterpriseの付属クレジットが縮小した点にも注意)
4. メンバー個別のライセンス種別(Business/Enterprise)を「People」タブから割り当てる

他の3ツールも同様に、Teams/Enterprise以上のプランで管理者ダッシュボード・SSO・利用上限設定が用意されている(詳細は各ツールの個別ページを参照)。

### 料金の目安(2026年9月時点、個人向け入口プラン)

| ツール | 無料プラン | 最初の有料プラン |
|---|---|---|
| Cursor | Hobby(Agentリクエスト数を制限、上限は非公開でアカウントごとに表示) | Pro 20ドル/月(Pro+ 60ドル/月、Ultra 200ドル/月の上位プランあり) |
| GitHub Copilot | Free(補完月2,000件・チャット月50件) | Pro 10ドル/月(月15ドル分のAI Credits付属。Pro+ 39ドル/月・Max 100ドル/月の上位プランあり) |
| Cline | 拡張機能自体が無期限無料 | (料金なし。ただし選んだAIプロバイダーへの実費が別途発生。目安は月15〜120ドル程度(多くは月25〜70ドルの範囲)、Opusなど高性能モデルを終日使う重度利用では月200〜500ドル規模という報告もある) |
| Windsurf(Devin Desktop) | Free(軽めのクォータ) | Pro 20ドル/月(Max 200ドル/月、Teams 80ドル/月+開発者1人あたり40ドルの上位プランあり) |

価格・利用枠は改定が頻繁なため、契約前に必ず各社公式サイト(cursor.com/pricing、github.com/features/copilot/plans、cline.bot/pricing、docs.devin.ai)で最新値を確認すること。特にGitHub Copilotは2026年6月にAI Credits制へ移行し、8月末には導入期プロモーションの終了でBusiness/Enterpriseの付属クレジットが縮小しているため、法人契約は特に確認が必須である。

## 注意点・よくある誤解

- **「自律的に動く」ことと「レビュー不要」はイコールではない**: 4ツールともAgent機能は人間の細かい指示なしに複数ファイルを編集できるが、生成コードの脆弱性・ライセンスリスク・重複コード増加は共通の懸念として複数の調査で指摘されている。特に認証・権限・外部通信に関わる差分は必ず人間がレビューする運用を前提にする
- **料金の「クレジット」「クォータ」制度は要注意**: Cursor・Copilot・Windsurfはいずれも、Auto/標準モデルは使い放題に近い一方、高性能モデルを指名すると付属クレジットやクォータを消費する仕組みを採る。「思っていたより早く上限に達した」という声が多く、管理者は利用上限(スペンドリミット)を必ず設定する。GitHub Copilotは2026年6月にPremium Request UnitsからトークンベースのAI Creditsへ移行し、さらに8月末に導入期のプロモーション分が終了してBusiness/Enterpriseの付属クレジットが縮小しているため、法人契約は特に想定外の超過課金に注意する
- **Clineの「無料」は拡張機能自体の話**: AIモデルの利用料は自己負担であり、ヘビーユーザーでは月数百ドル規模になる例もある。「Clineなら無料でAIコーディングができる」という誤解のまま導入すると、想定外のAPI利用料に驚くことになる
- **オートアプルーブ(自動承認)機能はリスクとセットで理解する**: Cline・Cursor・Windsurfとも、ファイル編集やターミナルコマンドの自動承認を有効化できるが、本番環境に近いリポジトリや機密情報が置かれた環境では、承認を必須にする運用にとどめるべきである
- **買収・ブランド変更の情報は「発表」と「完了」を区別する**: Windsurfは2026年6月に正式にDevin Desktopへ改称・完了済み、CursorのSpaceXによる買収も2026年8月14日に完了した。ただし完了後に新たな波及が起きている点に注意したい。OpenAIは買収を理由に2026年8月28日、Cursorへのモデル提供契約を2026年11月12日付で終了すると通告した(Cursor社によれば当該利用は全トラフィックの5%程度で、個人APIキー持ち込みで一部代替できる見込みだが全てはカバーできない)。OpenAIのGPT系モデルをCursorで使い続けたい組織は、11月の切り替え時期を見据えて代替ツール・代替モデルの検討を今から進めるべきである
- **買収元の性質による組織的なリスクも考慮する**: CursorはSpaceX傘下の「SpaceXAI」部門となり、xAI(Grok)との連携が強まっている。特定ベンダーの政治的・ブランド的リスクに敏感な企業は、契約前にデータの取り扱い方針や将来のロードマップ変更リスクを確認しておくとよい
- **市場シェア・満足度の数字は調査方法で大きく振れる**: 「契約者数が多い=最適」ではなく、開発者の満足度調査では別のツールが上位に来ることもある。自社のコードベース・タスクで実際に試してから判断するのが最も確実

## 最初の一歩

社内のエンジニア数名に、今週の小さな実装タスク1件を4ツールのうち無料プランで試せる2つ(例: GitHub Copilot Freeと、Cursor HobbyまたはCline)で並行して試してもらい、体感の違いを1分で共有してもらうことから始めるとよい。

## 関連トピック

- [Cursorの基本(AIコードエディタ)](cursor-basics.md)
- [GitHub Copilotの基本(コーディング支援AI)](github-copilot-basics.md)
- [Clineの基本(コーディング支援AI)](cline-basics.md)
- [Windsurfの基本(コーディング支援AI)](windsurf-basics.md)
- [特化型AIツールの選び方(用途別マップと比較)](specialized-ai-tools-selection-guide.md)
- [ローカルLLMの基本(自社PC・サーバーで動かす生成AI)](local-llm-basics.md)

## 更新履歴

### 2026-09-15: SpaceXによるCursor買収完了・OpenAIのモデル提供終了予定と、各ツールの料金・モデル一覧を最新化
- **内容**: CursorがSpaceX傘下「SpaceXAI」として2026年8月14日に買収完了したこと、OpenAIが買収を理由に2026年11月12日付でCursorへのモデル提供を終了すると通告した件を追記。比較表・料金表をCursor(Pro+ 60ドル追加、Ultra 200ドル)・GitHub Copilot(Pro+値上げ、AI Credits制への移行と8月末のプロモーション終了、Kimi K3のGA)・Cline(BYOK実費レンジの再計測)・Windsurf/Devin Desktop(SWE-2、Teams料金)で最新化し、GitHub Agent HQや組織ガバナンス手順、判断フローチャート・注意点にモデル依存度リスクを追加
- **出典**: [SpaceX officially closes its Cursor acquisition - TechCrunch](https://techcrunch.com/2026/08/15/spacex-officially-closes-its-cursor-acquisition/), [Cursor is now a part of SpaceX - Cursor Blog](https://cursor.com/blog/joining-spacex), [OpenAI to end model access to Cursor after acquisition by Elon Musk's SpaceX - CNBC](https://www.cnbc.com/2026/08/29/openai-cursor-spacex-model-access.html), [Cursor Pricing 2026: $20 Pro, $60 Pro+, $200 Ultra - DevTools Review](https://devtoolsreview.com/pricing/cursor-pricing/), [GitHub Copilot Enterprise pricing 2026: seats, AI credits, and the September cliff - CloudZero](https://www.cloudzero.com/blog/github-copilot-enterprise-pricing/), [GitHub Copilot is moving to usage-based billing - GitHub Blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/), [Kimi K3 is now available in GitHub Copilot - GitHub Changelog](https://github.blog/changelog/2026-08-06-kimi-k3-is-now-available-in-github-copilot/), [Cline Pricing 2026 - Automation Atlas](https://automationatlas.io/answers/cline-pricing-explained-2026), [Windsurf Pricing: 5 Plans and the Hidden Quota Cost - Emergent](https://emergent.sh/learn/windsurf-pricing), [AI Models - Devin Docs](https://docs.devin.ai/desktop/models), 公式料金ページ(cursor.com/pricing、github.com/features/copilot/plans、cline.bot/pricing)

### 2026-07-30: 初版執筆
- **内容**: Cursor・GitHub Copilot・Cline・Windsurf(現Devin Desktop)を料金・使えるモデル・自律度・エディタ形態・対象ユーザーの軸で横並び比較し、判断フローチャート、プロジェクト共通指示ファイルのコピペ実例(ツールごとの保存場所対応表付き)、GitHub Copilotの組織ガバナンス設定手順、市場シェア・満足度調査の数値、業界再編(買収)の注意点をまとめた初版を執筆
- **出典**: [AI Coding Assistant Market Share (2026 Survey) - Ideaplan](https://www.ideaplan.io/blog/ai-coding-assistant-market-share-2026), [GitHub Copilot Under Pressure: Cursor and Claude Code Are Eating Its Lunch (2026)](https://pasqualepillitteri.it/en/news/3392/github-copilot-cursor-claude-code-ai-coding-showdown-2026), [Cursor vs Windsurf vs Cline vs Copilot (2026): AI Coding Agent Comparison - AppScale Blog](https://appscale.blog/en/blog/cursor-vs-windsurf-vs-cline-vs-copilot-ai-coding-agents-2026), [Cursor Teams Upgrades Pricing for Predictability - StartupHub.ai](https://www.startuphub.ai/ai-news/technology/2026/cursor-teams-upgrades-pricing-for-predictability), [Kimi K2.7 now available for Copilot Business and Enterprise - GitHub Changelog](https://github.blog/changelog/2026-07-07-kimi-k2-7-now-available-for-copilot-business-and-enterprise/), [Windsurf Is Now Devin Desktop: Devin Local, ACP, and What the Rebrand Actually Changes - ChatForest](https://chatforest.com/builders-log/windsurf-devin-desktop-rebrand-devin-local-acp-builder-guide/), [SpaceX to acquire the AI coding startup Cursor for $60 billion - CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html), 各ツールの詳細な料金・機能は本リポジトリ内[Cursorの基本](cursor-basics.md)・[GitHub Copilotの基本](github-copilot-basics.md)・[Clineの基本](cline-basics.md)・[Windsurfの基本](windsurf-basics.md)の各出典を参照
