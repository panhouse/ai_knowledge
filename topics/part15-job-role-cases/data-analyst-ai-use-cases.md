---
title: データアナリスト/BIアナリスト職における生成AI活用事例
part: 15
chapter: 第5章 企画・プロダクト・データ分析
tags: [データアナリスト, BI, text-to-SQL, ダッシュボード, Power BI, Looker, QuickSight, BigQuery, pandas]
created: 2026-07-15
updated: 2026-07-15
---

# データアナリスト/BIアナリスト職における生成AI活用事例

## これは何か

データアナリスト・BI(Business Intelligence、経営判断に使うデータを可視化・分析する仕組み)アナリストの仕事は、「SQLを書いてデータを取り出す」「ダッシュボードを作る・保守する」「数字の変化を非エンジニアの関係者にわかりやすく説明する」という3つの作業が中心になる。このうち特に時間を食うのが、SQLを書く手間そのものよりも「ビジネス側の曖昧な質問(『先月の売上、なんか落ちてない?』)を、集計すべき指標・条件に翻訳する」工程と、「出てきた数字が何を意味するかを言葉で説明する」工程である。生成AIはこの2つの"翻訳"作業、および定型的なSQL・Pythonコードの下書きを高速化できる一方、生成されたSQLや統計処理が一見もっともらしく動いてしまうために**間違いに気づきにくい**という、この職種特有のリスクも抱える。本ページは、データアナリスト/BIアナリストの実務シーン別に、使うツール・コピペで使えるプロンプト・検証の仕方を整理する。

## 仕組み・背景

生成AIによるSQL生成(自然言語で書いた依頼をSQLクエリに変換する処理。text-to-SQLとも呼ばれる)は、LLM(大規模言語モデル)がテーブル名・カラム名・データ型といったスキーマ情報を読み込み、それに対応する構文を組み立てる仕組みで動いている。ポイントは、**AIはスキーマの「形」を理解しているだけで、そのカラムが業務上何を意味するか(例: `status`列の値が「キャンセル」を指すといった暗黙のルール)までは知らない**ことである。そのため、テーブル定義だけを渡した生成AIは、文法的に正しいが業務的には誤ったSQL(例: キャンセル行を除外し忘れて売上を過大集計する)を平気で返すことがある。この弱点を補うために登場したのが、あらかじめ指標定義・カラムの意味・結合ルールを整備した「セマンティックレイヤー(データの意味・計算ルールを定義した中間層)」で、Looker・ThoughtSpotのようなBIツール組み込みのAI機能は、この社内で定義済みのセマンティックレイヤー経由でAIに質問させることで、汎用チャットAIに素のテーブルを見せるより誤集計のリスクを抑えている。

もう1つの仕組み上の要点は、「コードを書かせて実行させる」方式と「言葉で数字を答えさせる」方式の違いである。ChatGPTのデータ分析機能(Advanced Data Analysis、詳細は[ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方](../part07-data-analysis/chatgpt-advanced-data-analysis.md)を参照)やClaude.aiの分析ツールのように、実際にPythonコードを生成してサンドボックス(隔離された実行環境)内で実行し、その実行結果を返す仕組みは、少なくとも「計算自体の誤り」は起きにくい。一方、ファイルを渡さずに「これとこれの平均は?」と会話だけで聞くと、コードを実行せず"それらしい"数値を文章として生成してしまうことがある。BIツール組み込みのAI機能(Power BI Copilot、Amazon Qなど)も、裏側では既存の集計エンジン(DAX・SQLエンジン)を呼び出して数値自体は正しいクエリ結果を使うが、その数値に添える「解釈・要因分析のコメント」の部分はLLMが言葉で生成しているため、コメント側にハルシネーション(もっともらしい誤りを生成する現象、詳細は[ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)を参照)が混じる余地が残る。

## 使いどころ・使い分け

### 主な活用シーンとツールの対応

| 活用シーン | 向くツール・機能 | 理由 |
|---|---|---|
| ビジネス側の曖昧な質問を分析設計に翻訳する | 汎用チャットAI(ChatGPT / Claude / Gemini) | 対話で前提・粒度を詰める「壁打ち」に強い |
| SQLクエリの下書き・既存クエリの解説 | Gemini in BigQuery、Copilot in Power BI(DAX)、汎用チャットAI | スキーマを渡せばクエリのたたき台が作れる。ただし業務ルールの反映は要確認 |
| ダッシュボードのナレーティブ要約・エグゼクティブサマリー | Power BI Copilot、Amazon Q in QuickSight、Tableau Pulse、Gemini in Looker(Conversational Analytics) | 数値そのものは既存の集計エンジンが計算し、AIは説明文を生成する構成のため実務利用が進んでいる |
| 異常値・トレンド変化の一次要因分析ドラフト | 汎用チャットAIのデータ分析機能、BIツールのAI要約機能 | 「考えられる仮説」を洗い出す壁打ちには強い。因果の断定はできない |
| 手元データでのアドホックなPython/pandas処理 | ChatGPTのデータ分析機能、Claude.aiの分析ツール、Julius AI、Hex | コードを実際に実行して結果を返すため検算しやすい |
| 大規模・継続更新のダッシュボード構築 | BIツール本体(Power BI、Looker、Tableau、QuickSight) | AI機能はあくまで既存BI基盤の上に乗る補助機能。基盤の権限・更新設計はBIツール側で行う |

判断の軸は2つある。1つは「数値の計算」と「数値の解釈」を分けて考えること。前者はコードを実行する仕組み(サンドボックス型のデータ分析機能、BIツールの集計エンジン)に任せた方が事故が少なく、後者(なぜそうなったかの説明文)はAIが得意とはいえ、必ず人が検算・裏取りする前提で使う。もう1つは「一度きりの調査か、継続的にビジネス側が見る資料か」で、前者は汎用チャットAIで素早く済ませ、後者はBIツール側のAI機能(セマンティックレイヤー経由で誤集計のリスクが低い)に寄せるのが実務的である。

### BIツール組み込みAI機能の比較(2026年7月時点)

| ツール・機能名 | 提供元 | 主な機能 | 必要なライセンス・料金の目安 |
|---|---|---|---|
| Gemini in BigQuery(SQL生成・Data Canvas・データインサイト) | Google Cloud | 自然言語からのSQL生成・説明、Pythonコード生成、対話形式でのデータ探索(Data Canvas)、テーブルの自動要約・関係性の可視化 | 基本機能はBigQueryの利用料金に含まれ追加コストなし。高度なエージェント機能はGemini Code Assistのシート課金または従量課金が別途必要な場合あり |
| Gemini in Looker(Conversational Analytics) | Google Cloud | 自然言語での質問応答、インサイトの自動生成、Looker/Looker Studio双方に対応 | 2026年9月末までは公正利用の範囲で無料提供。10月以降は「データトークン」課金(入力100万トークンあたり3ドル、出力100万トークンあたり20ドルが案内されている) |
| Copilot in Power BI | Microsoft | 自然言語からのDAX(Power BIの数式言語)生成・解説・最適化、レポートのナレーティブ要約、質問に応じた自動ビジュアル作成 | Power BI Pro 14ドル/ユーザー/月、Premium Per User(PPU)24ドル/ユーザー/月、またはFabricのF64以上の容量が必要(利用のたびにFabric容量を消費) |
| Amazon Q in QuickSight | AWS | 自然言語でのQ&A、ダッシュボードのエグゼクティブサマリー自動生成、自然言語からの新規ダッシュボード作成 | QuickSight Enterprise Edition内で、Reader Pro 20ドル/ユーザー/月・Author Pro 50ドル/ユーザー/月に加え、Q機能を1人でも有効化するとアカウントごとに月額250ドルの追加費用が発生 |
| Tableau Pulse | Salesforce(Tableau) | 指標の自動監視と変化の通知、変化要因のAIによる説明文生成 | Tableau+のAI機能として、既存シート課金に上乗せする形で提供(具体的な追加額は契約形態により変動するため要見積もり) |
| ThoughtSpot Spotter | ThoughtSpot | 社内で定義済みの指標・関係性(セマンティックモデル)を土台にした自然言語検索・エージェント型分析 | ライセンス体系はプランにより異なり、月額25ドル程度からと案内されるプランも存在(要見積もり) |

判断基準は「すでにそのBIツールを全社導入しているかどうか」。既にPower BIやLookerが会社の標準ダッシュボード基盤になっているなら、追加のライセンス費用を払ってでも組み込みAI機能を使う価値が高い。BIツールを持たない部署でのアドホックな分析には、汎用チャットAIのデータ分析機能で十分間に合うことが多い。

## 実務での使い方

### シーン1: ビジネス側の曖昧な質問を分析設計に翻訳する

依頼者から「先月の売上が落ちてる気がするので見てほしい」のような粒度の粗い依頼が来たとき、いきなり集計を始めず、まずAIとの壁打ちで分析設計(何を・どの粒度で・何と比較して見るか)を固めると手戻りが減る。

```
あなたはBIアナリストの分析設計を手伝うアシスタントです。以下のビジネス側からの
依頼を、実際に集計・分析に着手できるレベルの分析計画に落とし込んでください。

【依頼内容】
先月の売上が落ちている気がするので、原因を調べてほしい

【出力してほしいもの】
1. この依頼を成立させるために確認すべき前提条件(期間の定義、比較対象、対象範囲など)を
   5つ程度、質問形式でリストアップする
2. 想定される要因の仮説を、需要側(顧客・市場)と供給側(自社の施策・在庫・体制)に
   分けて5〜8個洗い出す
3. 各仮説を検証するために必要な集計軸(商品別、地域別、チャネル別など)を提案する
4. 分析の優先順位(まず何から見るべきか)を提案する

【条件】
- 実際のデータはまだ渡していない段階なので、憶測での結論は出さないこと
- 「このデータがあれば検証できる」という形で、必要なデータの種類を明記すること
```

このやり取りで固まった分析計画を依頼者と共有してから集計に入ると、「見てほしかったのはそこじゃない」という手戻りを防ぎやすい。

### シーン2: SQLクエリの下書き・既存クエリの解説

テーブル定義(スキーマ)を渡してSQLの下書きを作らせる、または他人が書いた複雑なクエリを解説させる使い方。Gemini in BigQueryのSQL生成機能を使う場合は、BigQueryのクエリエディタ上部の入力欄に自然言語で依頼を書くと、対象テーブルのスキーマを踏まえたSQL案が生成される。汎用チャットAIを使う場合は、スキーマ情報をプロンプトに明示する。

```
以下のテーブル定義をもとに、依頼内容に沿ったSQL(BigQuery標準SQL)を作成してください。

【テーブル定義】
orders(order_id, customer_id, order_date, status, amount)
  ※ statusは 'completed' / 'cancelled' / 'pending' のいずれか
customers(customer_id, region, signup_date)

【依頼内容】
2026年6月の地域別売上合計を出したい。ただし売上として集計してよいのは
statusが'completed'の注文のみとする。

【出力条件】
- クエリ本体に加えて、なぜそのJOIN・WHERE条件にしたかを1〜2行で説明する
- statusの除外条件など、業務ルールに関わる部分にはコメントを付ける
- 集計結果の件数が0件になりうる条件(データが存在しない月など)があれば指摘する
```

「'completed'のみ集計」のような業務ルールは、渡さなければAIは存在を知らないため、必ずプロンプトまたは社内のセマンティックレイヤー側で明示する。生成されたSQLは、必ず**件数の桁感(既知の実績とオーダーが合っているか)**をその場で確認してから使う。

### シーン3: ダッシュボードのナレーティブ要約・エグゼクティブサマリー作成

BIツール組み込みのAI機能(Power BI Copilot、Amazon Q in QuickSightなど)は、既存のダッシュボード・レポートに対して自然言語で要約文を生成する。Power BI Desktopでの操作手順は以下の通り。

1. Power BI Desktopでレポートを開き、リボンの「ホーム」タブから「Copilot」アイコンをクリックする(Fabric F64以上の容量、またはPremium Per Userライセンスが必要)
2. Copilotペインが開いたら、「このページのサマリーを作成して」のように自然言語で依頼する
3. 生成された要約文をレポート内のテキストボックスに貼り付け、実際の数値・グラフと突き合わせて誤りがないか確認する

コピペで使えるプロンプト例(BIツールのAI機能・汎用チャットAI共通):

```
以下は今月の売上ダッシュボードの主要指標です。経営層向けのエグゼクティブサマリーを
3〜4行で作成してください。

【主要指標】
- 総売上: 1.2億円(前月比 -8%、前年同月比 +3%)
- 客単価: 4,800円(前月比 +2%)
- 新規顧客数: 320人(前月比 -15%)
- 主な変動: 地域Aの売上が前月比-22%、他地域はほぼ横ばい

【条件】
- 事実(数値)の記述と、考えられる要因の推測を明確に分けて書く
- 推測部分には「〜と考えられる」「要因は未確認」など、断定を避ける表現を使う
- 経営層が次に確認したくなるであろう論点を1つ、末尾に問いかけとして添える
```

### シーン4: 異常値・トレンド変化の要因分析ドラフト

普段と異なる動き(急な落ち込み・急上昇)を見つけたとき、原因調査の初動としてAIに仮説出しをさせる。ここは「壁打ち」であり結論ではないことを明示する。

```
以下は日次の会員登録数データです(CSVを添付)。7月10日前後から急激に登録数が
落ち込んでいます。考えられる原因の仮説を、社内要因(施策・システム・体制)と
社外要因(市場・競合・季節性)に分けてリストアップしてください。

各仮説について、
1. その仮説が正しい場合に、データ上どんな追加の兆候が見えるはずか
2. その兆候を確認するために追加で見るべきデータ
を1〜2行で添えてください。断定はせず、あくまで検証すべき仮説として整理してください。
```

ファイルを添付してChatGPTのデータ分析機能やClaude.aiの分析ツールに投げると、実際にコードを実行して急落前後のグラフ・統計量を出力させながら仮説出しをさせられる(データ分析機能の基本操作は[ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方](../part07-data-analysis/chatgpt-advanced-data-analysis.md)を参照)。

### シーン5: アドホックなPython/pandas処理の下書き

BIツールに載せるほどでもない、一度きりの集計・データ整形をコードで済ませたいとき、コード自体をAIに書かせて自分の手元(Jupyter・VSCodeなど)で実行する使い方も定番である。

```
以下の要件を満たすPython(pandas)のコードを書いてください。実行環境は
JupyterNotebookで、変数dfにすでにCSVを読み込んだDataFrameが入っている前提です。

【dfの列】order_date(日付), region(文字列), amount(数値), status(文字列)

【要件】
1. statusが'completed'の行のみを対象にする
2. order_dateを月次に丸め、region別・月別の合計amountをピボットテーブルにする
3. 前月比(%)の列を追加する
4. 欠損値がある行があれば、除外せずに件数を表示してから警告を出す

コードにはコメントを付け、なぜその処理にしたかも簡潔に説明してください。
```

## 注意点・よくある誤解

- **文法的に正しいSQL・コードでも、業務ルールを反映できていないことがある**: AIはテーブルのスキーマ(列名・型)は理解できても、「キャンセル済みの注文は売上に含めない」「退会済み会員は分母から除く」といった暗黙の業務ルールまでは知らない。生成されたクエリ・コードは、必ず既知の実績値と桁感が合っているか、条件分岐(WHERE句・フィルタ)が業務ルール通りかを人が確認してから使う。特に金額・件数が意思決定に直結する集計は、独立した別の方法(手動集計・既存レポートとの突き合わせ)で検算する
- **ダッシュボードの「解釈コメント」は数値そのものより誤りやすい**: Power BI CopilotやAmazon Qのような機能は、集計エンジンが計算した数値自体は正確でも、その数値に添える「要因の解釈」部分はLLMが言葉で生成しているため、もっともらしいが根拠のない因果関係を書いてしまうことがある。生成されたナレーティブ要約は、事実(数値)の記述と推測(要因の解釈)を分けて確認し、推測部分は必ず人がレビューしてから配布する
- **セマンティックレイヤーがないまま生のテーブルを渡すと誤集計のリスクが上がる**: LookerのConversational AnalyticsやThoughtSpot Spotterのように、指標定義・結合ルールを事前に整備した「セマンティックレイヤー」経由でAIに質問させる仕組みは、汎用チャットAIに素のテーブル定義だけを渡すよりも誤集計のリスクが低い。継続利用するダッシュボードでは、可能な限りこうした指標定義済みの基盤上でAI機能を使う
- **統計処理の妥当性はコードの実行結果でも検証が必要**: データ分析機能(サンドボックスでコードを実行する仕組み)は計算自体の誤りは起きにくいが、「集計軸の解釈違い」「外れ値の扱い」「相関と因果の混同」は起こりうる。相関係数や回帰分析の結果をそのまま「原因」として報告書に書かない。因果関係の主張には、それを裏付ける追加の検証(A/Bテストなど)が必要である
- **顧客データ・売上データを無料プランや個人アカウントのAIに入力しない**: 分析対象のデータには個人情報・取引先情報が含まれることが多い。法人契約(学習への非利用がデフォルトの契約)や、社内承認済みのBIツール・AI機能を使う。詳細は[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)を参照
- **BIツール組み込みAI機能はライセンス・容量課金が想定より高くつくことがある**: Power BI CopilotはFabricのF64以上の容量が必要、Amazon Q in QuickSightはPro系ロールに加えアカウントごとの月額固定費が発生するなど、組み込みAI機能は基本プランの延長では使えない場合が多い。試験導入の際は、対象ユーザー数と利用頻度を見積もった上でコストを確認する

## 最初の一歩

直近で作成した、または依頼を受けたことのある集計・ダッシュボードを1つ選び、シーン1のプロンプト例を使って「分析設計への翻訳」を試し、出てきた仮説・確認事項が自分の当初の想定と一致するか見比べてみる。

## 関連トピック

- [研究開発(R&D)職における生成AI活用事例](./rd-ai-use-cases.md)
- [企画職における生成AI活用](./planning-ai-use-cases.md)
- [ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方](../part07-data-analysis/chatgpt-advanced-data-analysis.md)
- [AIが扱いやすいデータ形式](../part07-data-analysis/ai-friendly-data-formats.md)
- [ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)

## 更新履歴

### 2026-07-15: 初版執筆
- **内容**: データアナリスト/BIアナリスト職での生成AI活用シーン(分析設計への翻訳、SQL下書き・解説、ダッシュボードのナレーティブ要約、異常値・トレンド要因分析ドラフト、アドホックなPython/pandas処理)を整理し、各シーンのコピペ用プロンプト例、Gemini in BigQuery/Looker(Conversational Analytics)・Copilot in Power BI・Amazon Q in QuickSight・Tableau Pulse・ThoughtSpot Spotterの機能・料金比較表、Power BI Desktopでの操作手順、text-to-SQLがセマンティックレイヤーなしでは業務ルールを反映できないリスクや解釈コメントのハルシネーションリスクを執筆
- **出典**: [Gemini in BigQuery features are now generally available | Google Cloud Blog](https://cloud.google.com/blog/products/data-analytics/gemini-in-bigquery-features-are-now-ga)、[Gemini in BigQuery overview | Google Cloud Docs](https://docs.cloud.google.com/bigquery/docs/gemini-overview)、[Conversational Analytics overview | Looker Docs](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview)、[Looker pricing (data tokens) | Colrows](https://colrows.com/blogs/looker-pricing/)、[Power BI pricing | Microsoft](https://www.microsoft.com/en-us/power-platform/products/power-bi/pricing)、[Power BI Copilot: Complete Guide 2026 | Power BI Consulting](https://powerbiconsulting.com/blog/power-bi-copilot-complete-guide-2026)、[Power BI Premium vs Premium Per User | EPC Group](https://www.epcgroup.net/power-bi-premium-vs-premium-per-user)、[Amazon Q in QuickSight brings new user roles and pricing to Amazon QuickSight Enterprise Edition | AWS Business Intelligence Blog](https://aws.amazon.com/blogs/business-intelligence/amazon-q-in-quicksight-brings-new-user-roles-and-pricing-to-amazon-quicksight-enterprise-edition/)、[Conversational analytics software comparison | getdot.ai](https://www.getdot.ai/blog/conversational-analytics-software)、[ThoughtSpot competitors and alternatives | Astrato](https://www.astrato.io/blog/thoughtspot-competitors)、[How to use Claude AI for data analytics | Coupler.io](https://blog.coupler.io/how-to-use-claude-ai-for-data-analytics/)、[Claude Connectors | Anthropic](https://claude.com/connectors)
