---
title: カスタマーサクセス職における生成AI活用事例
part: 15
chapter: 第4章 カスタマーサポート・カスタマーサクセス
tags: [カスタマーサクセス, ヘルススコア, チャーン予測, QBR, オンボーディング, Gainsight, ChurnZero, HubSpot, AIエージェント]
created: 2026-07-14
updated: 2026-08-11
---

# カスタマーサクセス職における生成AI活用事例

## これは何か

カスタマーサクセス(CS)は、契約後の顧客を能動的にフォローし、オンボーディング・利用定着・解約防止・アップセル(上位プランへの契約変更)提案までを担う職種で、SaaS企業を中心に定着している。同じ「顧客対応」でも、[カスタマーサポート職における生成AI活用事例](customer-support-ai-use-cases.md)が問い合わせという**受動的**な業務(ヘルプデスク・コールセンター)を扱うのに対し、CSは問い合わせが来る前に「この顧客は離脱しそうか・追加提案の余地はあるか」を**能動的**に見極めて動く点が異なる。1人のCSM(カスタマーサクセスマネージャー)が数十〜数百社を担当することも珍しくなく、全顧客の状況を人力で把握するのは限界がある。生成AIは、利用ログ・問い合わせ履歴・商談メモといった散在するデータを束ねてヘルススコア(顧客の健全度を表す指標)やQBR(四半期ビジネスレビュー、顧客と四半期ごとに実施する振り返り会)資料の下書きを自動生成することで、この「全顧客を見渡す」作業を支援する。

## 仕組み・背景

CS領域の生成AI活用は、次の3つの技術要素の組み合わせで成り立っている。

1. **ヘルススコアの自動算出・説明生成**: 契約情報・プロダクトの利用ログ(ログイン頻度・機能利用状況)・サポートチケット・議事録・メールなどの非構造化データをAIが横断的に読み込み、スコアだけでなく「なぜこのスコアなのか」を自然文で説明する。Gainsightは2025年に買収したStaircase AIを「Insight Agent」として自社製品に統合し、メール・会議・サポートのやり取りを分析して手動設定なしに「Sentiment(感情)」を含む4種類のサブスコア(各0〜100点)を自動算出する機能を展開している。従来からの「Scorecard Optimizer」(過去の解約実績とスコアの相関を分析してスコアの重み付け自体を調整する機能)と組み合わせ、ヘルススコアの立ち上げそのものを省力化する方向に進化している。
2. **予兆検知とネクストアクションの提案**: ルールベース(利用率が◯%を下回ったらアラート、といった固定条件)から一歩進み、複数シグナルの組み合わせから解約の予兆を数カ月前倒しで検知し、「いつ・誰に・何をすべきか」までAIが提案する仕組みが広がっている。ChurnZeroの「Engagement AI」のように、提案だけでなくアウトリーチ文面の下書き・送信までを自律的に行うAIエージェントも出てきている。
3. **要約・資料生成によるドキュメント作業の圧縮**: 商談・オンボーディング面談・QBRの議事録をAIが要約し、CRMの所定項目へ自動反映したり、QBR資料のたたき台を生成したりする。Gainsightの「AI Cheat Sheet」のような生成AIアシスタントは、メール・通話・チケット・プロダクトデータから要約とネクストアクション案を横断的に作成する。従来の「Sally」「Atlas」というアシスタント機能は、2026年に入り「AI-Native Services(AINS)」という事業単位に発展し、既製エージェントを使う(buy)・自社データで独自エージェントを構築する(build)・ベンダーに運用委託する(hire)の3通りから選べる形に再編されている。

これらは独立した機能ではなく、「ヘルススコアが下がった顧客を自動検知」→「AIが要因と推奨アクションを提示」→「CSMが最終判断してAIが下書きした文面を調整・送信」という一連の流れとして設計されるのが基本形だが、2026年4月にGainsightがCS領域で初めてMCP(Model Context Protocol、AIエージェントと外部システムを繋ぐ標準規格)対応を発表し、ClaudeやChatGPTなどの外部AIエージェントがGainsight上のデータを直接読み書きして解約リスクの検知や更新プレイの立案までを代行できるようになるなど、「AIが提案するダッシュボード」から「AIエージェントに定型業務そのものを任せる基盤」へと役割が広がりつつあるのが2026年8月時点の潮流である。

## 使いどころ・使い分け

代表的な6つの活用場面と、全自動化の可否の目安は以下の通り。

| 活用場面 | 何をするか | 全自動化 vs 人間介在 |
|---|---|---|
| オンボーディング支援 | 導入初期のタスク・進捗をAIが整理し、遅延している顧客を検知 | 進捗の可視化は自動化してよいが、つまずいている顧客への個別フォローは人間が行う |
| ヘルススコア算出・解約予兆検知 | 利用ログ・問い合わせ履歴・商談メモを横断してAIがスコアと要因を算出 | スコア算出とアラートは自動化、解約リスクへの具体的な対応方針の決定は人間 |
| 解約リスク顧客へのアウトリーチ下書き | 状況に応じたフォローメール・提案文をAIが下書き | 下書きは自動化、顧客ごとの関係性を踏まえた最終調整・送信判断は人間 |
| アップセル・クロスセル機会の発見 | 利用データから追加提案の余地がある顧客をAIが抽出 | 抽出は自動化、提案内容・価格交渉は人間(営業・CSMの判断) |
| QBR・EBR(年次ビジネスレビュー)資料作成 | 利用実績・成果指標・今後の提案をAIが資料のたたき台に整理 | たたき台は自動化、顧客固有の文脈や関係性を踏まえた仕上げは人間 |
| 議事録要約・CRM入力 | 商談・オンボーディング面談の記録をAIが要約しCRMに反映 | 要約生成は自動化、公式記録として使う前に軽く目視確認するのが望ましい |

判断の軸は法務・サポートと同様に、「間違えたときの被害が『言い直せば済む』レベルか、『顧客との関係悪化・契約解除に直結する』レベルか」。ヘルススコアやアウトリーチ文面はあくまで「一次案」であり、顧客との関係を最終的に築くのは人間のCSMという前提を崩さないことが実務上のコツになる。

## 実務での使い方

### 1. ヘルススコア算出・解約予兆検知のプロンプト例

CSツールにAI機能がない場合や、ツール導入前に汎用AIで簡易的に試す場合の例。CRMエクスポートデータ・利用ログのサマリーを貼り付けて使う。

```
あなたはSaaS企業のカスタマーサクセスマネージャーです。
以下の顧客データをもとに、解約リスクを分析してください。

## 顧客データ
- 契約プラン・契約金額:
- 契約開始日・直近の更新日:
- 直近3カ月のログイン頻度(週あたり):
- 主要機能の利用率(導入時と比較):
- 直近のサポート問い合わせ件数・内容:
- 直近の商談・面談メモ:

## 出力形式
1. 解約リスク(高・中・低)とその判断根拠を3点以内で
2. リスクが高い場合、想定される要因(利用定着の失敗/価格への不満/
   意思決定者の異動 など)を推測し、断定せず「〜の可能性がある」と表現する
3. 今週中にCSMが取るべき具体的なネクストアクションを1〜2個提案する
4. データが不足していて判断できない項目があれば明記する
```

### 2. 解約リスク顧客へのアウトリーチ下書き

```
以下の顧客に対し、解約防止のためのフォローメール文面を下書きしてください。

【顧客の状況】
- 導入から8カ月、主要機能Aの利用率が導入時の半分に低下
- 直近1カ月、担当者からのログインなし
- 3カ月前の問い合わせで「使い方が分かりにくい」という声あり

【条件】
- 責めるような表現・売り込み色の強い表現は避け、
  「お困りごとがないか伺う」姿勢で書く
- 具体的な数字や期日は本文に書かず、担当CSMが個別に確認・追記する前提の
  プレースホルダー({{ }}で囲む)にする
- 件名・本文合わせて200文字程度
```

### 3. QBR資料のたたき台作成

```
以下の情報をもとに、顧客向けQBR(四半期ビジネスレビュー)資料の
アウトラインを作成してください。

【今期の実績データ】
- 主要KPI(導入目的に対する成果指標)の推移:
- 利用状況のサマリー:
- 発生した問い合わせ・障害とその対応:

【アウトプット】
1. エグゼクティブサマリー(3行)
2. 今期のハイライト(成果が出た点を2〜3点)
3. 課題・改善が必要な点(1〜2点、事実ベースで断定しすぎない表現)
4. 次期の提案(利用拡大・追加機能の提案候補を1〜2点)
5. 各スライドのタイトル案(8〜10枚構成)
```

### 4. 議事録要約→CRM入力

```
以下はオンボーディング面談の文字起こしです。
下記のCRM入力フォーマットに沿って要約してください。
記載のない項目は「情報なし」と明記し、推測で埋めないこと。

## CRM入力フォーマット
- 顧客の導入目的:
- 現在のオンボーディング進捗(未着手/進行中/完了):
- 顧客が挙げた懸念・要望:
- 次回アクション・フォロー予定日:
- 解約・アップセルにつながりそうな発言の有無:

## 文字起こし
{{文字起こしテキストがここに入る}}
```

### 主なCSツールのAI機能・料金比較(2026年8月時点)

| ツール | 位置づけ | 主なAI機能 | 料金の目安 |
|---|---|---|---|
| Gainsight CS | 海外CSプラットフォームの最大手、エンタープライズ向け | 2025年買収のStaircase AIを統合した「Insight Agent」が通話・メール・チケットを分析し手動設定なしでヘルススコアを自動算出、自社データでAIエージェントを構築できる「Agentic Studio」(Claude採用)を提供、2026年4月にMCP対応し外部AIエージェントからの直接操作にも対応 | Essentials 150ドル/ユーザー/月〜、Enterprise 300ドル/ユーザー/月〜(第三者推計、Gainsightは公式の1人あたり価格を公開していない)。契約は原則年間で、エンタープライズ導入では別途5万〜12万ドル程度の導入費が加わる例も報告されている |
| ChurnZero | 中堅〜大企業向け、解約防止・アップセル検知に強み | Engagement AIが解約リスクシグナルをもとにパーソナライズした働きかけ文面を自動生成・送信、Snapshot AIがアカウント状況のサマリーを都度生成、Customer Success AIとAIエージェント群でシグナル検知〜次善アクションの提案までを一体運用 | 非公開の見積制。2025〜2026年の実勢では年額1.5万〜8万ドル程度が中心帯(小規模契約は1万ドル強〜、大企業向けは18万ドルを超える例も)で、定価から45〜70%程度の値引き交渉が一般化しているとの報告がある |
| Totango + Catalyst | 2024年に両社が統合、Salesforce連携に強み | Totangoのヘルススコアリングとcatalystのアウトカム(成果)ベースのスコアリングを統合。Catalystの予測AIエンジン「Unison」を軸に、解約予測・拡張機会の発見を強化する開発が進行中(2026年8月時点) | 非公開の見積制(統合後の移行に伴うデータ不整合の報告もあり、導入時は要確認) |
| HubSpot Service Hub(カスタマーサクセスワークスペース) | HubSpotのSmart CRMに統合されたCS機能、中小〜中堅向け | Breeze AIのCustomer Health Agentが解約リスクの高いアカウントをリアルタイムに検知・優先順位付けしネクストアクションを提案。問い合わせ対応を担うBreeze Customer Agentは2026年4月から成果報酬型の課金に移行 | カスタマーサクセスワークスペースはProfessionalプラン以上で利用可能。Service Hub Professional 90ドル/席/月〜(年払い、初期費用1,500〜3,500ドル別途)。Breeze Customer Agentは解決した会話1件ごとに0.50ドル(50クレジット、2026年3月までは1件1.00ドルだった) |
| HiCustomer | 国内SaaS企業向けの国産CSツール | ヘルススコアの自由設計、解約・アップセルの兆候を検知する独自アラート、SFA/CRMとのAPI連携。運営元は購買・オンボーディング支援に特化した別プロダクト「Arch by HiCustomer」も展開している | 要問い合わせ(生成AIによる要約・提案機能は各社比較でGainsight等の海外大手に比べ限定的な範囲にとどまる) |

日本ではSansanが2018年からGainsightを導入し、カスタマーサクセスを組織文化として根づかせてきた事例が公表されている。同社は2025年を「AIファースト」の年と位置づけ、社内アンケートで生成AI業務活用率99%・「仕事の質が向上した」との回答98%・「1日30分以上の時短を実感」との回答71%という結果を公表しており、CS部門を含む全社的な生成AI活用が進んでいる。2026年2月にSansanが実施した企業のAI活用実態調査(担当者1,077名対象)では、直近1年以内に生成AIを導入した企業が72.5%に達した一方、AI活用の前提となる社内データベースが「完璧に整っている」と回答した企業は22.2%にとどまり、個人レベルの業務改善は進んでも経営インパクトを伴う成果はまだ限定的という結果も出ている。CS部門でヘルススコアや解約予兆検知の精度を上げる際も、この「データ基盤の整備」が土台になる点は変わらない。

判断基準は「解約防止・ヘルススコアの精度を専用ツールの学習済みモデルに任せたいか、汎用AIで手元のデータをその都度分析する運用で足りるか」。担当顧客数が数百社規模になり、シグナルの見落としが事業インパクトに直結する段階では専用CSツールの導入価値が高く、担当顧客数が少ない・導入初期の段階では汎用AI+スプレッドシートの運用でも十分に効果を出せる。

## 注意点・よくある誤解

- **AIが出すヘルススコアは「答え」ではなく「仮説」**: スコアの精度は入力データの質に強く依存する。利用ログの計測が不十分だったり、CRMの入力が疎かだったりすると、実態とかけ離れたスコアになる(いわゆるガベージイン・ガベージアウト)。スコアが下がった顧客には必ず人間が状況を確認してから動くこと
- **「予兆検知の自動化」は「関係構築の自動化」ではない**: AIが解約リスクを早期に検知しても、実際に顧客との信頼関係を立て直すのは人間のCSMの仕事である。アウトリーチ文面をAIに全任せして機械的な一斉送信にすると、かえって「テンプレ対応をされた」という不信感を招きかねない
- **公称の解約率改善・時短効果は好条件下の数値であることが多い**: ベンダーの事例や記事に出てくる「解約率半減」「議事録作成6分の1」といった数値は、特定の条件・母数での実績であることが多く、自社のデータ品質や運用体制によって効果は変わる。導入前にトライアルで自社データを使って検証する
- **チャーン予測AIは「導入するだけで差がつく」機能ではなくなりつつある**: 海外の調査(2025年のGartnerによるCS部門調査)では、解約予測モデルを運用しているCS組織の63%が、モデルを使っていない組織と比べてNRR(純収益維持率)の改善を実感できていないと回答している。予測精度そのものより、予測結果を営業・CSMのアクションにどうつなげるかという運用設計のほうが成果を左右する
- **専用CSツールは「定価」だけで比較すると判断を誤りやすい**: Gainsightのようなエンタープライズ向けツールは公式の1人あたり価格を公開しておらず、契約規模によっては年間契約額に加えて数万〜十数万ドル規模の導入費が発生する。ChurnZeroのように定価から45〜70%程度の値引き交渉が一般化しているツールもあるため、複数社から見積を取り、総所有コスト(TCO)で比較するのが実務的
- **顧客データを外部AIに入力する際の情報漏洩リスク**: 契約金額・利用状況・商談メモには顧客の機密情報が含まれることが多い。無料プランの汎用AIやAPIの設定によっては入力内容が学習に使われる場合があるため、法人向けプラン(学習利用オプトアウトが標準)を使う、または専用CSツールのようにデータ利用方針が明示されたサービスを使うのが基本線になる
- **AIエージェントによる自動送信機能は「解約防止に効く」とは限らない**: ChurnZeroのEngagement AIのように文面生成から送信までを自律化できる機能もあるが、送信前に人間が確認するステップを挟むか、少なくとも初期は承認制で運用し、顧客からの反応を見ながら自動化の範囲を広げていくのが安全な導入手順

## 最初の一歩

自分が担当する(または身近な)顧客1社分のデータ(契約プラン・直近の利用状況・問い合わせ履歴)を簡単なメモにまとめ、上記の「ヘルススコア算出・解約予兆検知」のプロンプトをChatGPTやClaudeにそのまま試してみて、AIが提示する根拠とネクストアクションが自分の肌感覚と一致するかを確認してみる。

## 関連トピック

- [カスタマーサポート職における生成AI活用事例](customer-support-ai-use-cases.md)
- [生成AIに向く業務・向かない業務の切り分け](../part12-business-practice/ai-task-suitability.md)
- [Human in the Loop(人間参加型)の業務設計](../part12-business-practice/human-in-the-loop-basics.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-08-11: 主要ツールのAI機能・料金・統計を最新化
- **内容**: 「仕組み・背景」を更新し、Gainsightの2025年Staircase AI買収による「Insight Agent」(自動ヘルススコア算出)、Claude採用の「Agentic Studio」、2026年4月のMCP対応(外部AIエージェントからの直接操作)を反映。ツール比較表を2026年8月時点に更新し、ChurnZeroの実勢価格帯(年額1.5万〜8万ドル中心、値引き45〜70%が一般化)、Totango+Catalystの予測AIエンジン「Unison」、HubSpot Breeze Customer Agentの成果報酬型課金への移行(2026年4月、1件0.50ドル)、HiCustomerの関連プロダクト「Arch by HiCustomer」を追記。SansanのAI活用実態調査(2026年2月、導入率72.5%だがデータ基盤整備率22.2%)を追加し、注意点にチャーン予測AIの効果の限界(Gartner調査で予測モデル運用組織の63%がNRR改善を実感できず)とTCOで比較する重要性を追加
- **出典**: [Gainsight Opens Its Platform with MCP, Bringing Customer Retention Into the Agentic Era](https://www.gainsight.com/press/gainsight-opens-its-platform-with-mcp-bringing-customer-retention-into-the-agentic-era/)、[Gainsight Launches the Agentic Stack for Customer Retention](https://www.globenewswire.com/news-release/2026/05/28/3303094/0/en/gainsight-launches-the-agentic-stack-for-customer-retention.html)、[Insight Agent (Staircase AI) Overview - Gainsight](https://support.gainsight.com/gainsight_nxt/Insight_Agent_(Staircase_AI)/About/Insight_Agent_(Staircase_AI)_Overview)、[Gainsight Features 2026: Complete Guide to Health Scores, Playbooks & Hidden Costs](https://www.oliv.ai/blog/gainsight-features)、[Gainsight Pricing 2026: 2 Plans from $150–$300/user/month](https://costbench.com/software/customer-success/gainsight/)、[ChurnZero Pricing Breakdown: Per-User Costs, Hidden Fees, and Negotiation Tips](https://www.oliv.ai/blog/churnzero-pricing-breakdown-per-user-costs)、[ChurnZero Pricing in 2026 (Real Numbers, Not Marketing)](https://churntools.com/blog/churnzero-pricing)、[Coming to Catalyst: Post-Sales Revenue Rigor with AI Forecasting | Totango Webinar](https://www.totango.com/events/coming-to-catalyst-post-sales-revenue-rigor-with-ai-forecasting)、[Best AI Customer Success Platforms in 2026: Gainsight vs ChurnZero vs Totango vs Catalyst](https://www.techno-pulse.com/2026/05/best-ai-customer-success-platforms-in.html)、[HubSpot's Customer Agent and Prospecting Agent: Now you pay when the task is complete](https://www.hubspot.com/company-news/hubspots-customer-agent-and-prospecting-agent-now-you-pay-when-the-task-is-complete)、[HubSpot Breeze AI Pricing: The Real Cost Breakdown](https://myaskai.com/blog/hubspot-breeze-ai-pricing-explained)、[生成AI「直近1年以内に導入」企業は7割超も課題感 Sansan調査](https://officenomikata.jp/news/17781/)、[Sansan、企業のAI活用実態調査を実施 AI成果の実感は個人業務中心に限定的](https://bizzine.jp/news/detail/12727)、[AI in Churn Reduction: What G2's 2026 Expert Survey Found](https://learn.g2.com/ai-in-churn-reduction)、[「Arch by HiCustomer」の製品サイトをリニューアル](https://prtimes.jp/main/html/rd/p/000000018.000039915.html)

### 2026-07-14: 初版執筆
- **内容**: カスタマーサクセス(CS)職における生成AI活用を、オンボーディング支援・ヘルススコア算出/解約予兆検知・解約リスク顧客へのアウトリーチ・アップセル機会発見・QBR資料作成・議事録要約の6場面に整理。カスタマーサポート(受動的な問い合わせ対応)との違いを明確化した上で、Gainsight/ChurnZero/Totango+Catalyst/HubSpot Service Hub/HiCustomerの機能・料金比較表、SansanのGainsight導入事例、コピペ用プロンプト4種、注意点を記載
- **出典**: [Gainsight's AI-Powered Customer Success Features](https://support.gainsight.com/Gainsight_AI/02_AI_Supported_Features_in_Gainsight_Products/01_Customer_Success_(CS)/01_Gainsight's_AI-Powered_Customer_Success_Features_(WIP))、[AI for Customer Success Leaders: How to Get Started | Gainsight Software](https://www.gainsight.com/blog/ai-for-customer-success-leaders-how-to-get-started/)、[Gainsight Pricing 2026: 2 Plans from $150–$300/user/month](https://costbench.com/software/customer-success/gainsight/)、[Gainsight Pricing 2026: Complete Per-User Costs, Hidden Fees, and Negotiation Tactics](https://www.oliv.ai/blog/gainsight-pricing-cost-per-user)、[Best AI Customer Success Platforms in 2026: Gainsight vs ChurnZero vs Totango vs Catalyst](https://www.techno-pulse.com/2026/05/best-ai-customer-success-platforms-in.html)、[Totango and Catalyst Merge](https://www.totango.com/press/totango-and-catalyst-merge)、[Customer Success AI - ChurnZero](https://churnzero.com/features/customer-success-ai/)、[ChurnZero Pricing Breakdown: Per-User Costs, Hidden Fees, and Negotiation Tips](https://www.oliv.ai/blog/churnzero-pricing-breakdown-per-user-costs)、[HubSpot Service Hub pricing guide](https://blog.hubspot.com/service/hubspot-service-hub-pricing)、[HubSpot Service Hub Pricing Explained (2026): Plans & Real Costs](https://www.getmacha.com/blog/hubspot-service-hub-pricing)、[HiCustomer(ハイカスタマー)の特徴・料金・機能 | 起業LOG SaaS](https://kigyolog.com/tool.php?id=995)、[顧客視点のデータ一元化×CTAで売上も向上!Sansanカスタマーサクセスの最新ツール活用 | Gainsight](https://www.gainsight.co.jp/casestudy/sansan)、[Sansan、社員の生成AI活用率99%を達成](https://jp.corp-sansan.com/news/2025/0514.html)、[【2026年最新】カスタマーサクセス×AI 完全ガイド|チャーン予測と解約防止](https://aigyomunote.com/customer-success-ai-guide-2026/)、[【2026年最新】AIで解約防止・カスタマーサクセス｜SaaS3社の90日チャーン半減ストーリー](https://uravation.com/media/ai-customer-success-churn-prevention-story-2026/)
