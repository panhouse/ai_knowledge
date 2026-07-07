---
title: "主要AIチャットツールのデータ分析機能比較(ChatGPT・Gemini・Claude・Copilot)"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [データ分析, ChatGPT, Gemini, Claude, Copilot, Code Interpreter]
created: 2026-07-07
updated: 2026-07-07
---

# 主要AIチャットツールのデータ分析機能比較(ChatGPT・Gemini・Claude・Copilot)

## これは何か

CSV・Excelファイルをアップロードするだけでチャット型AIが集計・グラフ化まで済ませてくれる「データ分析」機能は、ChatGPT・Google Gemini・Claude・Microsoft Copilotの主要4ツールすべてに搭載されている。しかし裏側の実行環境(使用言語・サンドボックスの有無)、対応ファイル形式・サイズ上限、生成したコードが見えるかどうか、必要なプランがツールごとに大きく異なる。違いを知らずに使うと、「無料プランで使えると思っていた機能が実は有料限定だった」「機密データを想定より緩いデータ保護方針のプランにアップロードしてしまった」といった事故につながる。本稿は4ツールを横並びで比較し、業務で選ぶ際の判断材料をまとめる。なお、ChatGPTの機能自体をさらに深掘りした内容は「[ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方](../part07-data-analysis/chatgpt-advanced-data-analysis.md)」を参照してほしい。

## 仕組み・背景

4ツールの実行方式は大きく2系統に分かれる。

1. **Code Interpreter型(ChatGPT・Gemini・Claude)**: チャットにファイルを添付すると、裏側のサンドボックス(外部と隔離された使い捨ての実行環境)でAIがコードを生成・実行し、その結果(表・グラフ・生成ファイル)をチャットに返す。
2. **ネイティブ編集型(Copilot in Excel)**: チャットで対話しながら、開いているExcelのワークブックそのものをその場で編集する。分析結果が別のファイルとして出てくるのではなく、既存のシートに反映される。

使用言語も異なる。ChatGPT・Gemini・Copilotはいずれも**Python**(データ分析の定番言語で、pandas・matplotlib・scikit-learnなどの分析用ライブラリを使う)でコードを生成・実行するのに対し、Claudeの「分析ツール(Analysis tool)」は**JavaScript**をブラウザ内のWeb Worker(メインの画面から隔離されたブラウザの裏側の実行スレッド)で動かす方式を採る。この違いにより、統計・機械学習ライブラリの豊富さや、生成物をコードとして再利用しやすいかが変わってくる。

Geminiにはさらに2つの経路がある。(a) `gemini.google.com` のチャットにCSV・Excelファイルを直接アップロードして質問する方法(Gemini 2.0以降のcode execution機能でPythonコードを自動生成し、matplotlibでグラフを描画する)、(b) Google Sheetsに組み込まれたサイドパネルや`=AI()`関数でシートそのものを直接分析する方法。後者は「ファイルをアップロードする」のではなく、既存のスプレッドシートを対象にする点が他ツールと発想が異なる。

## 使いどころ・使い分け

### 4ツール比較表

| 比較軸 | ChatGPT | Google Gemini | Claude | Microsoft Copilot(Excel) |
|---|---|---|---|---|
| 機能名 | データ分析(旧Advanced Data Analysis/Code Interpreter) | Geminiアプリのファイル分析(code execution)+ Gemini in Google Sheets | 分析ツール(Analysis tool) | Copilot in ExcelのPythonによる高度な分析(Edit with Copilotの一部) |
| 実行言語・環境 | Python(サーバー側サンドボックス、ステートフルなJupyter型) | Python(サーバー側code execution。Sheetsは内部エンジン) | JavaScript(ブラウザ内Web Worker) | Python(Excel内のPython連携基盤) |
| 起動方法 | チャットにファイルを添付するだけで自動起動 | チャットにファイルを添付/Sheetsのスパークルアイコンからサイドパネルを開く | 設定でオンにした上でファイルを添付、または明示的に依頼 | Excelのリボン→Copilot→「高度な分析」から依頼 |
| 生成コードの可視性 | 回答内に表示され、開いて確認できる | 表示されるが折りたたみ表示が中心 | 回答内に表示され、開いて確認できる | チャット欄に表示され、新しいシートに分析ステップが残る |
| 対応ファイル形式 | CSV、Excel、PDF、画像など。Googleドライブ/OneDrive/Googleスプレッドシートも直接読み込み可 | CSV、XLS、XLSX、Googleスプレッドシート、テキスト等 | CSV、TSV、Excel(コード実行を有効化した場合)、テキスト系が中心 | 開いているExcelブック内のシート・テーブル(複数シート横断はベータ) |
| ファイルサイズ・件数の目安 | 1ファイル最大512MB(表形式は実質50MB程度が目安)、1会話あたり10件前後 | 1ファイル最大100MB、1プロンプトあたり最大10件 | 1ファイル最大30MB、1会話最大20件 | Excelのブックサイズ上限に準拠(ファイルアップロードという概念がない) |
| グラフ・チャート生成 | ○(matplotlib/seabornベース、ダウンロード可) | ○(matplotlibベース) | ○(JavaScriptの描画ライブラリで生成、Artifactとして表示) | ○(Excelのグラフ機能と連動し、シートに直接挿入) |
| 対応プラン・料金目安 | Free(制限あり)/Plus 月$20/Pro 月$200/Business/Enterprise | 個人:Google AIプラン(有料)で強化、無料枠は制限あり/法人:Workspace Business Standard以上(月$14〜)にGemini機能が標準搭載 | Free(設定でコード実行をオンにすれば利用可)/Pro/Max/Team/Enterprise | Microsoft 365 Copilot(法人向けアドオン、月額$30目安)。個人向けCopilot Proは対象外の場合が多い |
| 日本語での分析結果の質 | 高い。要約・考察も自然な日本語で出力 | 高いが、シート内の`=AI()`はセル単位の短い出力向き | 高いが、コードのコメントは英語になりやすい | 高い。Excelの用語(ピボット、関数名)に沿った説明が得意 |
| 強み | ファイル形式を選ばず使い捨ての分析に強い。エコシステムが最も成熟 | Googleスプレッドシートを編集不要でそのまま分析できる。Colabとの連携で本格的なノートブックも生成可能 | コードと成果物(Artifact)を並べて確認しやすい。無料でも試せる | 分析結果が最初からExcelのシート・グラフとして残り、社内フォーマットを崩さない |
| 弱み | セッションが切れるとファイル再アップロードが必要 | 法人向け機能はWorkspaceプラン依存で個人利用がやや複雑 | ファイルサイズ上限が4ツール中もっとも小さい | Microsoft 365 Copilotライセンスが前提で、個人ユーザーには縁遠い |

### どのツールを選ぶか(判断チェックリスト)

- **とにかく手早く使い捨てで集計したい・ファイル形式を問わず投げたい** → ChatGPT。実績・対応形式の広さで最も無難
- **すでにGoogleスプレッドシートで管理している数字をその場で聞きたい** → Gemini(Sheetsのサイドパネル)。アップロードの手間がない
- **無料で試してみたい、コードも一緒に確認したい** → Claude。Freeプランでも設定から分析ツールを有効化できる
- **分析結果を最終的にExcelの体裁(表・グラフ・関数)のまま社内に配りたい** → Copilot in Excel。ただしMicrosoft 365 Copilotライセンスが前提
- **数百万行級の大規模データや複数人での継続利用が前提** → いずれのチャットAIも本業ではない。BIツール(Tableau、Power BIなど)との併用を検討する

## 実務での使い方

### ChatGPT: 基本手順

1. `chatgpt.com` のチャット入力欄左のクリップアイコンからCSV・Excelを添付する
2. 「月別・店舗別の売上を集計してグラフにして」のように日本語で依頼する。ツールの手動選択は不要
3. 生成されたPythonコードと表・グラフが返る。グラフやExcelファイルはダウンロードリンクから保存する

詳細な手順・プロンプト例・注意点は「[ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方](../part07-data-analysis/chatgpt-advanced-data-analysis.md)」にまとめてある。

### Gemini: 基本手順(チャット添付/Sheets連携の2通り)

**チャットでファイルを分析する場合**
1. `gemini.google.com` にログインし、入力欄の「+」アイコンからCSV・Excelファイルを選択する
2. 「このデータから売れ筋商品トップ5をグラフにして」のように依頼すると、Python実行(code execution)が自動的に走り、表・グラフが返る

**Google Sheetsに組み込まれたシートを直接分析する場合**
1. Google Sheetsでファイルを開き、右上の★(スパークル)アイコンをクリックしてGeminiのサイドパネルを開く
2. 「A列の売上をB列の地域別に集計して」のように話しかけるか、セルに `=AI("売上上位3商品を教えて", A1:C100)` のように関数として埋め込む
3. 個人利用ではGoogle AIプラン、法人利用ではGoogle Workspace Business Standard以上の契約でGemini機能が有効になっている必要がある

### Claude: 基本手順

1. `claude.ai` の左下のアカウント名→「設定」→「機能」(Capabilities)で「コード実行とファイル作成」をオンにする(Free/Pro/Max/Team/Enterpriseいずれの契約でも設定自体は可能)
2. チャットにCSV・Excelファイル(1ファイル30MBまで)を添付し、「このデータを分析して傾向をグラフで見せて」と依頼する
3. Claudeが生成したJavaScriptコードと実行結果が、会話の右側に表示される「Artifact(成果物パネル)」に表示される

### Copilot(Excel): 基本手順

1. 分析したいExcelファイルをOneDrive上に保存した状態で開く(ローカル保存のみのファイルでは利用できない場合がある)
2. リボンの「ホーム」タブから「Copilot」をクリックし、右側にサイドパネルを開く
3. サイドパネル内で「高度な分析」を選び、「Pythonを使ってこのデータを分析し、月次の売上推移グラフを作成して」のように依頼する
4. Copilotが生成したPythonコードと分析結果が新しいシートに追加され、既存のブック内でそのまま確認・編集できる

### コピペで使える依頼文サンプル(ツール共通で使える表現)

```
添付のCSVは過去1年分の日次売上データです。列構成は
「日付, 店舗名, 商品カテゴリ, 売上金額, 客数」です。

1. まず列名・データ型・欠損値の有無を確認し、解釈を箇条書きで教えてください
2. 店舗×月ごとの売上合計を集計してください
3. 全店舗合計の月次売上推移を折れ線グラフにしてください(横軸:年月、縦軸:売上金額)
4. 使用したコード(Python/JavaScript)を省略せずに表示してください
```

「①解釈の確認 ②集計軸 ③グラフの種類と軸 ④コードを見せる指示」の4点を入れておくと、ツールを問わず手戻りが少ない。

## 注意点・よくある誤解

- **機密データのアップロード先を必ず確認する**: 個人向けの無料・安価なプランでは、会話やアップロードしたファイルがモデルの学習に使われる設定がデフォルトになっている場合がある。氏名・取引先名・個人情報を含むデータは、匿名化(ダミー値への置き換え)をしてから渡すか、学習への非利用がデフォルトの法人向けプラン(ChatGPT Business/Enterprise、Gemini for Workspace、Claude Team/Enterprise、Microsoft 365 Copilot)を使う
- **「コードが見える=正しい」ではない**: 生成されたコードが表示されるツール(ChatGPT・Claude・Copilot)でも、集計軸の解釈違い(日付の年度区切り、重複データの二重カウントなど)は起こり得る。重要な数値は必ずコードの中身を確認し、一部は手元のExcelやSQLの結果と突き合わせて検算する
- **ファイルサイズ上限の違いを把握しておく**: 同じ「数十万行のCSV」でも、Claudeの30MB上限では読み込めずGemini・ChatGPTでは通る、というケースがある。大きいファイルは事前に列や期間を絞り込んでから渡す
- **Copilotは「Excelブックが前提」**: ChatGPT・Gemini・Claudeのように任意のファイルを都度アップロードする発想ではなく、開いているExcelファイルそのものを対象にする。他システムから出力したCSVをまずExcelに読み込んでから使う一手間が必要になる場合がある
- **セッション・分析環境は保存されない(Copilot以外)**: ChatGPT・Gemini・Claudeでの分析はチャットが終わると実行環境が消え、翌日また使うにはファイルの再アップロードが必要。継続的に更新するダッシュボードには向かず、Excel(Copilot)やBIツールの方が適している
- **日本語グラフの文字化けは共通の落とし穴**: いずれのツールも、環境に日本語フォントが入っていないとグラフのラベルが「豆腐(□□□)」化することがある。応急処置は「グラフのラベルは英語にしてください」と頼むこと

## 最初の一歩

普段使っているAIチャットツール1つに、手元の売上や経費のCSV・Excelファイルを1件アップロード(またはCopilotならブックを開いた状態でリボンから起動)し、「月次で集計してグラフにして」と頼んでみる。返ってきたコードや集計結果が意図通りかを確認し、他のツールでも同じファイルを試して違いを体感してみるとよい。

## 関連トピック

- [ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方](../part07-data-analysis/chatgpt-advanced-data-analysis.md)
- [AIが扱いやすいデータ形式](../part07-data-analysis/ai-friendly-data-formats.md)
- [Google Geminiの基本](./google-gemini-basics.md)
- [Claude(Anthropic)の基本](./claude-basics.md)
- [Microsoft Copilotの基本](./microsoft-copilot-basics.md)
- [ChatGPTのプラン比較](./chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-07: 初版執筆
- **内容**: ChatGPT・Gemini・Claude・Copilotのデータ分析機能をツール横断で比較。実行言語(Python/JavaScript)・実行方式(Code Interpreter型/ネイティブ編集型)の違い、対応ファイル形式・サイズ上限、対応プラン、選定チェックリスト、機密データ取り扱いの注意点をまとめた
- **出典**: [Create and edit files with Claude | Claude Help Center](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- **出典**: [Introducing the analysis tool in Claude.ai | Claude by Anthropic](https://claude.com/blog/analysis-tool)
- **出典**: [The new Claude analysis JavaScript code execution tool | Simon Willison](https://simonw.substack.com/p/the-new-claude-analysis-javascript)
- **出典**: [Gemini in Google Sheets | Google Workspace](https://workspace.google.com/resources/spreadsheet-ai/)
- **出典**: [Gemini in Google Sheets can now analyze data across multiple tables | Google Workspace Updates](https://workspaceupdates.googleblog.com/2025/10/gemini-in-google-sheets-analyze-data.html)
- **出典**: [Gemini AI features now included in Google Workspace subscriptions | Google Workspace Admin Help](https://knowledge.workspace.google.com/admin/gemini/gemini-ai-features-now-included-in-google-workspace-subscriptions)
- **出典**: [コードの実行 | Gemini API - Google AI for Developers](https://ai.google.dev/gemini-api/docs/code-execution)
- **出典**: [Gemini アプリでファイルをアップロードして分析する | Gemini アプリ ヘルプ](https://support.google.com/gemini/answer/14903178?hl=ja)
- **出典**: [What's New in Excel (April 2026) | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/excelblog/whats-new-in-excel-april-2026/4502696)
- **出典**: [Introducing Copilot support for Python in Excel: Advanced Data Analysis Using Natural Language | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/excelblog/introducing-copilot-support-for-python-in-excel-advanced-data-analysis-using-nat/3928120)
- **出典**: [Get advanced data analysis using Copilot in Excel App Skills | Microsoft Support](https://support.microsoft.com/en-gb/office/get-advanced-data-analysis-using-copilot-in-excel-app-skills-364e4ae9-9343-4d56-952a-5f62b0f70db6)
- **出典**: [Excel の Copilot の使用を開始する | Microsoft Support](https://support.microsoft.com/ja-jp/office/excel-%E3%81%AE-copilot-%E3%81%AE%E4%BD%BF%E7%94%A8%E3%82%92%E9%96%8B%E5%A7%8B%E3%81%99%E3%82%8B-d7110502-0334-4b4f-a175-a73abdfc118a)
- **出典**: [Claude AI Spreadsheet Uploading | Datastudios](https://www.datastudios.org/post/claude-ai-spreadsheet-uploading-excel-and-csv-file-support-data-analysis-features-formula-handlin)
- **出典**: [ChatGPT file upload sizes explained across all plans | Datastudios](https://www.datastudios.org/post/chatgpt-file-upload-sizes-explained-across-all-plans)
