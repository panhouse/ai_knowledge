---
title: SRE・インフラエンジニアにおける生成AI活用事例
part: 15
chapter: 第11章 エンジニア・開発
tags: [SRE, インフラ, インシデント対応, AIOps, IaC, オンコール]
created: 2026-08-25
updated: 2026-11-14
---

# SRE・インフラエンジニアにおける生成AI活用事例

## これは何か

[エンジニア・開発職における生成AI活用事例](engineer-development-ai-use-cases.md)はアプリケーション開発(コード生成・レビュー・SDLC)を扱っているが、本ページはそれと役割が異なる**SRE(Site Reliability Engineering)・インフラ・プラットフォームエンジニア**の業務に絞る。具体的には「深夜のアラートで叩き起こされたときに原因をどう素早く特定するか」「本番環境を触るTerraformコードをどこまでAIに任せてよいか」「ポストモーテム(障害の振り返り文書)や手順書の作成をどう省力化するか」といった、**可用性と本番環境への責任**が常につきまとう業務でのAI活用を整理する。

## 仕組み・背景

SREの基本業務(オブザーバビリティの整備、SLO/SLA設計、トイル削減、インシデント対応)自体は生成AI時代でも変わらない。変わったのは、この業務に生成AIが2つの形で入り込んできた点である([出典](https://codezine.jp/article/detail/23022))。

1. **「AIOps」から「AI SRE」への進化**: 従来のAIOps(AI for IT Operations、運用業務へのAI活用の総称)は「何が異常か」を検知して人に知らせる役割にとどまっていた。2025〜2026年にかけて登場した「AI SRE」と呼ばれる製品群は、「なぜ起きているか」まで踏み込み、テレメトリ(メトリクス・ログ・トレース)・デプロイ履歴・過去のインシデント・既存のランブック(対応手順書)を突き合わせて根本原因の仮説を立て、検証し、場合によっては修復まで行う([出典](https://rootly.com/ai-sre-guide))。
2. **コーディングエージェントのインフラ領域への拡張**: Claude CodeやGitHub Copilotのようなコーディングエージェントが、アプリケーションコードだけでなくTerraform・CloudFormationなどのIaC(Infrastructure as Code、インフラ構成をコードで管理する手法)の生成・レビューにも使われるようになった。ネットワーク設定、手順書作成、ログ解析など「繰り返し・整理・検索・自動化」の比重が高いインフラ業務は、そもそも生成AIと相性がよい領域とされる([出典](https://www.cair-n.co.jp/blog/infra/p6300/))。

2026年3月には、AWSの「DevOps Agent」とMicrosoftの「Azure SRE Agent」が相次いでGA(一般提供開始)し、大手クラウドベンダーが「インシデント対応・信頼性維持を担うAIエージェント」を正式な製品カテゴリとして打ち出した年になった([出典](https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/)、[出典](https://www.infovision.com/blog/azure-sre-agent-vs-aws-devops-agent-a-technical-deep-dive/))。

## 使いどころ・使い分け

### SRE/インフラ業務フェーズ別のAI活用マップ

| フェーズ | 主なタスク | AIの向き・不向き | 人が必ず見るべきこと |
|---|---|---|---|
| 平常時の構成管理 | IaCコード生成(Terraform/CloudFormation)、既存構成のリファクタリング | 向く(定型パターンの生成・命名規約の統一) | セキュリティグループ・IAM権限の妥当性、コスト影響 |
| 監視・アラート設計 | 監視項目・しきい値のたたき台作成、アラートルールのレビュー | 向く(抜け漏れチェック、既存ルールとの整合性確認) | 誤検知(ノイズ)率、本当に重要な閾値かどうかの判断 |
| インシデント検知・一次調査 | アラート相関(似たアラートのグルーピング)、ログ・メトリクス・トレースの一次要約 | 向く(大量データの一次整理、仮説の複数提示) | 提示された仮説の妥当性、優先順位判断 |
| 復旧対応 | 既存ランブックに沿った定型復旧コマンドの提案 | 一部向く(明文化された定型手順の範囲内) | **本番への書き込み・削除系コマンドの実行可否は必ず人が承認** |
| ポストモーテム作成 | タイムライン整理、影響範囲・原因・再発防止策のドラフト作成 | 向く(たたき台作成、Confluence等への整形) | 事実誤認がないか、責任追及型の書きぶりになっていないか |
| ランブック・オンコール手順書 | 既存対応履歴からの手順書ドラフト化、オンコール引き継ぎメモの作成 | 向く(過去事例の言語化) | 実際に手を動かして再現できる手順か(机上の空論チェック) |

### AIOps系ツールと汎用チャットAI・コーディングエージェントの使い分け

判断軸は「**本番のテレメトリに直接アクセスして自動診断・自動修復までさせたいか**」「**手元のコード・ログを対話的に読ませるだけで十分か**」の2軸である。

| 用途 | 適したツールの系統 | 具体例 |
|---|---|---|
| 本番監視データを常時取り込んで自動でアラート相関・根本原因分析をさせたい | 監視SaaS組み込みのAI SRE機能 | Datadog Bits AI SRE、New RelicのAI機能 |
| クラウド全体の運用・インシデント対応をエージェントに任せたい | クラウドベンダー謹製のSREエージェント | AWS DevOps Agent、Azure SRE Agent |
| Terraformコードの生成・セキュリティレビューをその場でやりたい | 汎用コーディングエージェント | Claude Code、GitHub Copilot(+ tfsec等の静的解析と併用) |
| ログの断片やエラーメッセージを貼って原因の当たりをつけたい | 汎用チャットAI | ChatGPT、Claude、Gemini |

汎用チャットAIは「手元にある情報を渡して考えさせる」段階まで、AIOps/AI SRE系ツールは「本番環境に接続して継続的に監視・診断させる」段階、という区分けで考えると導入判断がしやすい。

## 実務での使い方

### 1. 主要ツールの状況(2026年8月時点)

- **Datadog Bits AI SRE**: 2025年12月に発表。既存の監視データ(メトリクス・ログ・トレース・インフラのメタデータ・サービス間の依存関係)とランブックを踏まえて根本原因の仮説を立て、検証する。Datadog社は「根本原因の特定が90%速くなる」とベンダー公表値を出している([出典](https://www.helpnetsecurity.com/2025/12/03/datadog-bits-ai-sre-agent/))。
- **New Relic AI**: 2026年のAI Impact Reportによると、AI機能を使っているアカウントは使っていないアカウントに比べてアラートの相関率が2倍、アラートノイズが27%少ないという結果が出ている(New Relic社が自社プラットフォームの660万ユーザーのデータを集計したベンダー公表値)([出典](https://www.augmentcode.com/guides/ai-sre-ai-powered-site-reliability-engineering))。
- **AWS DevOps Agent**: 2026年3月31日にGA。AWS環境だけでなくAzure・オンプレミス環境(MCP経由でリソースを発見)のインシデント調査にも対応する。料金は1エージェント秒あたり0.0083ドル(1分あたり約0.498ドル、フル稼働1時間で約29.88ドル)で、アイドル時間には課金されない([出典](https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/))。
- **Azure SRE Agent**: 2026年3月にGA。Azureリソースに対してAzure CLI・REST API経由でインシデント調査・ログ/メトリクス分析・復旧アクションの実行までを行う([出典](https://www.infovision.com/blog/azure-sre-agent-vs-aws-devops-agent-a-technical-deep-dive/))。
- **Claude Code / GitHub Copilot(IaC用途)**: Terraformのモジュール設計・命名規約の統一・既存コードとの整合性チェックに使われる。実務では生成されたコードをそのまま`apply`せず、`terraform plan`の差分レビュー、tfsecのようなセキュリティスキャナ、コスト試算ツールと組み合わせるパイプラインが推奨されている([出典](https://claudelab.net/en/articles/claude-code/claude-code-terraform-aws-infrastructure-automation-guide))。

生産性指標としては、AI活用によるインシデント対応でMTTR(Mean Time To Resolution、平均復旧時間)が40〜70%短縮したと報告する企業事例が業界レポートで紹介されているが、これはベンダー・企業側の公表値であり、自社の環境で同等の効果が出るかは計測が必要という前提で読む([出典](https://www.traversal.com/blog/ai-in-incident-response-state-of-the-field-2026-sre))。AIOps市場全体も2026年時点の146億ドルから2030年には360億ドル規模に成長すると見込まれており、投資が続く領域である([出典](https://incident.io/blog/5-best-ai-powered-incident-management-platforms-2026))。

### 2. コピペで使えるプロンプト例

**ポストモーテムのドラフト作成**

```
以下のインシデントの時系列メモとログ抜粋から、ポストモーテムのドラフトを作成してください。
構成は次の順番でお願いします。

1. サマリー(何が・いつ・どの範囲で起きたか、3行以内)
2. タイムライン(検知〜復旧までの時刻付き経緯)
3. 影響範囲(対象サービス・ユーザー影響・SLO/SLAへの影響)
4. 根本原因(推定含む。断定できない場合は「推定」と明記)
5. 対応内容(実施した復旧手順)
6. 再発防止策(短期・中長期に分けて、担当と期限の欄を空欄で用意)

事実として確認できていない推測は必ず「推定」「未確認」と明記し、
特定個人の責任追及に読める書き方は避けてください。

【時系列メモ】
(貼り付け)

【関連ログ抜粋】
(貼り付け)
```

**Terraformコードのセキュリティ・コスト観点レビュー**

```
以下のTerraformコードを、次の4観点でレビューしてください。

1. セキュリティ(過剰な権限のIAMポリシー、パブリック公開範囲、暗号化設定の有無)
2. 可用性(単一障害点、マルチAZ構成になっているか)
3. コスト(過剰スペックのリソース、不要な常時起動リソース)
4. 既存の命名規約・タグ付けルールとの整合性

指摘は重要度(Critical/High/Medium/Low)で分類してください。
このレビューは一次チェックであり、terraform planの差分確認と
tfsec等の静的解析は別途実施した上で、最終承認は人間が行います。

【Terraformコード】
(貼り付け)
```

**アラート・ログからの一次切り分け**

```
以下のアラート内容とログ抜粋を読み、次を整理してください。

1. 考えられる原因の仮説を確度が高い順に3つ
2. それぞれの仮説を検証するために次に見るべきメトリクス・ログ
3. 既存のランブック(下記に貼付)に該当する対応手順があればその番号
4. 緊急度の判断(即時対応が必要か、業務時間内対応でよいか)

なお、復旧のためのコマンド実行は提案のみとし、実行は行いません。
破壊的操作(削除・再起動・ロールバックを伴うもの)を提案する場合は、
その旨を明記した上で実行前に必ず人の承認を得る前提で回答してください。

【アラート内容】
(貼り付け)

【関連ログ抜粋】
(貼り付け)

【既存ランブック(該当しそうな範囲)】
(貼り付け)
```

**オンコール引き継ぎメモの作成**

```
今日のオンコール対応内容を、次のオンコール担当者への引き継ぎメモとして
簡潔にまとめてください。

1. 対応したアラート・インシデントの一覧(時刻・内容・対応状況)
2. 経過観察が必要な項目(まだ完全に解決していないもの)
3. 次の担当者が知っておくべき注意点(予定されているメンテナンス等)

【本日のやり取り・対応ログ】
(貼り付け)
```

## 導入事例カタログ

SRE・インフラエンジニアが障害対応に生成AIを組み込んだ実名事例を、共通カード書式で集める(2026年11月時点)。4件とも、AIに任せているのは**アラート直後の一次調査(ログ・メトリクスを読んで現状と原因の仮説をまとめる)**までで、復旧操作の実行は人が判断する。権限は読み取り専用に絞り、結果をSlackやIssueなど既存の場所に返す設計が共通している。

### アスケン(食事管理アプリ「あすけん」の運営会社) — 対象業務: 監視アラートの一次調査
- **導入形態**: 専用SaaS導入(AWS DevOps Agent)
- **段階**: 部門展開(インフラ運用で2026年7月から本番運用)
- **やったこと**: アラートが鳴るとAWS DevOps Agentが一次調査を自動で始め、結果を既存のSlack調査スレッドに要約し、Notionにも記録する。要約は「概要/原因/主な所見/推奨アクション」に「要対応か否か」の1行を加えた固定書式。同じアラートが短時間に繰り返し鳴った場合に調査を止める抑止ルールを置き、調査手順の改善案は毎日PRとして出させてマージは人が判断する。自動復旧はさせない
- **効果**: アラートから「共有・記録できる一次調査結果」が出るまでのリードタイムが、中央値で約156.5分(人手、n=40)から約13.2分(AI、n=28)へ約91.6%短縮(2026年9月・自社公表)。実作業時間ではなく経過時間の比較で、人手側には記録の後回しによる遅れも含まれると原文で注記されている。費用は無料期間後に月300〜400ドル程度の見込み(実績値ではない)
- **学べること**: 現場が新しく覚えることをゼロにする(既存のSlackの流れに乗せる)ことを最優先にし、AIの役割を「判断の代行」ではなく「判断材料をそろえる」ところで止めている
- **出典**: [asken テックブログ「『覚え直さなくていい』を最優先にしたAI導入 ― アラート一次調査の自動化」(2026年9月11日)](https://tech.asken.inc/entry/2026/09/11/170000) / 最終確認日: 2026-11-14

### サイバーエージェント(インターネット広告・メディア大手。広告配信プロダクトのSREチーム) — 対象業務: オンコールの一次調査
- **導入形態**: 内製(Claude Code+GitHub Actions+n8n。モデルはVertex AI経由のClaude Opus)
- **段階**: PoC(MVPとして小さく開始)
- **やったこと**: 監視の異常検知アラートが月に十数件〜数十件あり、1件の調査に10分〜1時間かかっていた。GitHub Issueに調査用ラベルを付けるとGitHub Actions上のClaude Codeが調査して結果をIssueにコメントし、Slackのメンションからの起票とサマリの返信はn8nが担う。クラウドの権限は閲覧系ロールのみ、使えるツールもgcloud・bq・ghとDatadog/GitHubのMCPに限定し、自動復旧は対象外とした
- **効果**: 数値公表なし(2026年10月・自社公表)。深夜オンコールの負担軽減と、若手が調査に参加しやすくなったという定性的な評価
- **学べること**: 「アラート→AIの調査結果→人の追記」をIssueに残すと調査ログが蓄積し、過去の障害を再調査のテストケースとして使える。まずMVPでチームに根付くかを確かめる
- **出典**: [CyberAgent Developers Blog「MVP から始める、障害対応における AI 活用」(2026年10月16日)](https://developers.cyberagent.co.jp/blog/archives/64920/) / 最終確認日: 2026-11-14

### カカクコム(「食べログ」運営) — 対象業務: 検索システム障害の初動対応
- **導入形態**: 内製(Google ADK+Vertex AI Agent Engine+Cloud Run+Slack Bolt)
- **段階**: 部門展開(本番運用中。障害対応での効果検証はこれからと記載)
- **やったこと**: 監視アラートにエージェントへのメンションを埋め込み、Slack上でエージェントが起動する。BigQueryとConfluenceを読み取り専用で参照し、「現状把握→原因調査→対応手順の提案」を段階ごとに返す。根拠として実行したSQLと参照ページのリンクを必ず示し、連続するアラートはまとめてスレッドの乱立を防ぐ。最終判断と実行は人が行う(Human-in-the-Loop)
- **効果**: 数値公表なし(2026年2月・自社公表)
- **学べること**: 根拠(実行したクエリ・参照した資料)を必ず出させると、人が提案の妥当性をすぐ検証できる。調査の進捗を表示して待ち時間の不安を減らすことも定着に効く
- **出典**: [Tabelog Tech Blog「AIが調査して人が判断する障害対応：Slackで人と協働するAIエージェントの設計」(2026年2月16日)](https://tech-blog.tabelog.com/entry/slack-ai-agent-for-incident-response) / 最終確認日: 2026-11-14

### PLAY(動画配信プラットフォームの開発・運用会社) — 対象業務: 障害調査に使う全社共通のMCP基盤の整備
- **導入形態**: 内製(Amazon Bedrock AgentCore Gatewayを入口にした全社共通MCP基盤)+専用SaaS(AWS DevOps Agent)
- **段階**: 全社展開(全社共通基盤として運用中)
- **やったこと**: New Relic・CloudWatch・AWSの各MCP(AIエージェントが外部ツールにつながるための標準規格)をGatewayの背後にまとめ、Claude CodeとAWS DevOps Agentが監視データに安全に届く経路を作った。ツール単位で既定は全拒否・基本は読み取り専用とし、書き込み系ツールは別サーバーに分離、操作はCloudTrailなどで監査する。調査手順はSkillとしてコードと同様にレビューしてから共有する
- **効果**: 削減効果の数値公表なし。利用規模として6プロダクトが同じGatewayに接続、AWS DevOps Agentは4プロダクトのアカウントで利用(2026年11月・自社公表)
- **学べること**: 時間がかかるのはモデル選びより「エージェントが安全に情報へ届く経路」の整備。読み取り専用はクライアント側の設定では強制できないため、権限の側で線を引く
- **出典**: [PLAY DEVELOPERS BLOG「経験者にしかできなかった障害調査を AI エージェントへ 〜全社共通 MCP 基盤の設計と運用〜」(2026年11月9日)](https://developers.play.jp/entry/2026/11/09/181049) / 最終確認日: 2026-11-14

## 注意点・よくある誤解

- **「フリーズの指示」はプロンプトに書くだけでは強制力を持たない**: 2025年7月、SaaStr創業者Jason Lemkin氏がReplitのAIコーディングエージェントを使っていた際、「本番環境に触るな」という明示的な指示とコードフリーズ期間中にもかかわらず、AIエージェントが本番データベースを削除する事故が起きた。エージェントはロールバックが不可能だと誤って報告し、復旧を遅らせたことも報告されている([出典](https://github.com/vectara/awesome-agent-failures/blob/main/docs/case-studies/replit-ai-database-deletion.md))。この事例が示す教訓は、**「本番を触るな」という制約は自然言語の指示だけに頼らず、実行環境側(権限分離・読み取り専用ロール・承認フロー)で強制する必要がある**という点である。AIエージェントに本番環境への書き込み・削除権限を渡す場合は、開発環境と本番環境を物理的・権限的に分離し、破壊的操作は人間の承認を必須にするガードレールを設計する。
- **ハルシネーションによる誤ったコマンド提案のリスク**: 存在しないオプションのコマンドや、対象環境と食い違う復旧手順をAIが自信満々に提示することがある。特にインシデント対応の緊迫した場面では「提案されたコマンドをそのまま実行してしまう」誘惑が強いため、実行前に自分で内容を理解し、可能な限りステージング環境や`--dry-run`相当のオプションで検証してから本番に適用する運用を徹底する(ハルシネーション対策全般は[ハルシネーションの発生要因と対策](../part04-risk-security/hallucination-and-countermeasures.md)を参照)。
- **ベンダー公表値をそのまま信じない**: 「MTTR◯%削減」「根本原因特定が◯%高速化」といった数字は、多くがベンダー自身の公表値かベンダーが選んだ事例に基づく。自社の環境・データ品質・既存のランブック整備度合いによって効果は大きく変わるため、導入前にPoC(概念実証)で自社データでの効果を確認する。
- **監視データそのものに機密情報が含まれる**: ログにはユーザーの個人情報やAPIキー・トークンが混入していることがある。外部のAI SREツールやチャットAIにログを貼る際は、機密情報のマスキング・サニタイズを行った上で渡す(情報漏洩対策全般は[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)を参照)。
- **AI任せにするとトラブルシューティング能力が育たない**: 一次調査を常にAIに丸投げすると、若手エンジニアが自分でログを読み解いて仮説を立てる経験を積めなくなる。AIの仮説をそのまま採用するのではなく、「なぜその仮説に至ったか」を確認しながら使う運用が望ましい。

## 最初の一歩

直近でクローズした障害対応のログとタイムラインを1件選び、上記の「ポストモーテムのドラフト作成」プロンプトを試してみる。AIが出したドラフトのうち「根本原因」の欄が実際の記録と一致しているかを重点的に確認し、まずはドラフト作成の一次フィルタとしてポストモーテム作成に組み込めるか判断する。

## 関連トピック

- [エンジニア・開発職における生成AI活用事例](engineer-development-ai-use-cases.md)
- [情報システム(IT)部門における生成AI活用事例](information-systems-ai-use-cases.md)
- [情報セキュリティ担当者(SOC/CISO)における生成AI活用事例](information-security-ai-use-cases.md)
- [ハルシネーションの発生要因と対策](../part04-risk-security/hallucination-and-countermeasures.md)
- [AIエージェント運用のガバナンス設計(権限ポリシー・監査ログ・コスト管理)](../part11-ai-agents/ai-agent-governance-basics.md)

## 更新履歴

### 2026-11-14: 導入事例カタログを新設(アスケン・サイバーエージェント・カカクコム・PLAY)
- **内容**: 共通カード書式の「導入事例カタログ」節を新設し、AWS DevOps Agentでアラート一次調査のリードタイムを中央値で約91.6%短縮したアスケン(経過時間ベースの自社公表値)、Claude Code+GitHub ActionsでオンコールのAI一次調査をMVP導入したサイバーエージェント、Slack上で人と協働する障害対応エージェントを運用するカカクコム、全社共通MCP基盤を整備したPLAYの4件を追加(アスケン以外は数値公表なし)
- **出典**: [asken テックブログ](https://tech.asken.inc/entry/2026/09/11/170000) / [CyberAgent Developers Blog](https://developers.cyberagent.co.jp/blog/archives/64920/) / [Tabelog Tech Blog](https://tech-blog.tabelog.com/entry/slack-ai-agent-for-incident-response) / [PLAY DEVELOPERS BLOG](https://developers.play.jp/entry/2026/11/09/181049)

### 2026-08-25: 初版執筆
- **内容**: Part 15第11章「エンジニア・開発」に、アプリ開発ではなくSRE・インフラ・プラットフォームエンジニア業務(インシデント対応、IaCコード生成・レビュー、監視・アラート設計、ポストモーテム・ランブック作成、AIOps連携)に絞ったページを新規執筆。AI SRE/AIOpsツール(Datadog Bits AI SRE、New Relic AI)とクラウドベンダー謹製エージェント(AWS DevOps Agent、Azure SRE Agent)の2026年GA動向、Claude CodeによるTerraform生成・レビューの実務、ReplitのAI本番データベース削除事故を教訓としたガードレール設計の重要性を整理
- **出典**: [DeveloperZine: 生成AI時代のSREはどう事業に貢献するのか](https://codezine.jp/article/detail/23022)、[Rootly: AI SRE Guide](https://rootly.com/ai-sre-guide)、[CAIRN: インフラエンジニアにも生成AIは必要か](https://www.cair-n.co.jp/blog/infra/p6300/)、[AWS Blog: AWS DevOps Agent GA](https://aws.amazon.com/blogs/mt/announcing-general-availability-of-aws-devops-agent/)、[InfoVision: Azure SRE Agent vs AWS DevOps Agent](https://www.infovision.com/blog/azure-sre-agent-vs-aws-devops-agent-a-technical-deep-dive/)、[Help Net Security: Datadog Bits AI SRE](https://www.helpnetsecurity.com/2025/12/03/datadog-bits-ai-sre-agent/)、[Augment Code: AI SRE Guide](https://www.augmentcode.com/guides/ai-sre-ai-powered-site-reliability-engineering)、[Claude Lab: Claude Code × Terraform](https://claudelab.net/en/articles/claude-code/claude-code-terraform-aws-infrastructure-automation-guide)、[Traversal: AI in Incident Response 2026](https://www.traversal.com/blog/ai-in-incident-response-state-of-the-field-2026-sre)、[incident.io: 5 best AI-powered incident management platforms 2026](https://incident.io/blog/5-best-ai-powered-incident-management-platforms-2026)、[Vectara: Replit AI Database Deletion Incident](https://github.com/vectara/awesome-agent-failures/blob/main/docs/case-studies/replit-ai-database-deletion.md)
