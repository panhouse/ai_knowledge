---
title: "主要AIチャットツールのデータ分析機能比較(ChatGPT・Gemini・Claude・Copilot)"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [データ分析, ChatGPT, Gemini, Claude, Copilot, Code Interpreter]
created: 2026-07-07
updated: 2026-08-05
---

# 主要AIチャットツールのデータ分析機能比較(ChatGPT・Gemini・Claude・Copilot)

## これは何か

CSV・Excelファイルをアップロードするだけでチャット型AIが集計・グラフ化まで済ませてくれる「データ分析」機能は、ChatGPT・Google Gemini・Claude・Microsoft Copilotの主要4ツールすべてに搭載されている。しかし裏側の実行環境(使用言語・サンドボックスの有無)、対応ファイル形式・サイズ上限、生成したコードが見えるかどうか、必要なプランがツールごとに大きく異なる。違いを知らずに使うと、「無料プランで使えると思っていた機能が実は有料限定だった」「機密データを想定より緩いデータ保護方針のプランにアップロードしてしまった」といった事故につながる。本稿は4ツールを横並びで比較し、業務で選ぶ際の判断材料をまとめる。なお、ChatGPTの機能自体をさらに深掘りした内容は「[ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方](../part07-data-analysis/chatgpt-advanced-data-analysis.md)」を参照してほしい。

## 仕組み・背景

4ツールの実行方式は大きく2系統に分かれる。

1. **Code Interpreter型(ChatGPT・Gemini・Claude)**: チャットにファイルを添付すると、裏側のサンドボックス(外部と隔離された使い捨ての実行環境)でAIがコードを生成・実行し、その結果(表・グラフ・生成ファイル)をチャットに返す。
2. **ネイティブ編集型(Copilot in Excel)**: チャットで対話しながら、開いているExcelのワークブックそのものをその場で編集する。分析結果が別のファイルとして出てくるのではなく、既存のシートに反映される。

使用言語も異なる。ChatGPT・Gemini・Copilotはいずれも**Python**(データ分析の定番言語で、pandas・matplotlib・scikit-learnなどの分析用ライブラリを使う)でコードを生成・実行する。Claudeはやや複雑で、2つの仕組みが併存している。1つは2024年10月に登場した「**分析ツール(Analysis tool)**」で、**JavaScript**をブラウザ内のWeb Worker(メインの画面から隔離されたブラウザの裏側の実行スレッド)で動かし、素早い集計やグラフを会話右側の「Artifact(成果物パネル)」に表示する方式。もう1つは2025年後半以降に追加された「**コード実行とファイル作成(Code execution and file creation)**」で、こちらはサンドボックス化されたコンテナ内で**Python・Bash**を実行し、実際に開いて編集できるExcel(.xlsx、数式付き)・Word(.docx)・PowerPoint(.pptx)・PDFファイルそのものを生成する。同じ「Claudeでデータ分析する」でも、軽い集計はJavaScript版のArtifact、報告書やExcelファイルとして納品したい場合はPython版のファイル作成、と裏側の仕組みが使い分けられている。

Geminiにはさらに2つの経路がある。(a) `gemini.google.com` のチャットにCSV・Excelファイルを直接アップロードして質問する方法(code execution機能でPythonコードを自動生成し、matplotlibでグラフを描画する)、(b) Google Sheetsに組み込まれたサイドパネルや`=AI()`関数でシートそのものを直接分析する方法。後者は2026年4月の機能拡張で「分析するだけ」から一歩進み、複数テーブルをまたいだ集計・数式(XLOOKUPなど)の自動生成・書式設定まで、シートの構築・編集そのものをGeminiに任せられるようになった。

## 使いどころ・使い分け

### 4ツール比較表(2026年8月時点)

| 比較軸 | ChatGPT | Google Gemini | Claude | Microsoft Copilot(Excel) |
|---|---|---|---|---|
| 機能名 | データ分析(旧Advanced Data Analysis/Code Interpreter) | Geminiアプリのファイル分析(code execution)+ Gemini in Google Sheets(構築・編集も可能) | 分析ツール(Analysis tool、軽量な集計・グラフ用)+ コード実行とファイル作成(Excel等の実ファイル生成用) | Copilot in Excelの「編集」機能(Edit with Copilot)にPythonによる高度な分析が統合 |
| 実行言語・環境 | Python(サーバー側サンドボックス、ステートフルなJupyter型) | Python(サーバー側code execution。Sheetsは内部エンジン) | 分析ツール:JavaScript(ブラウザ内Web Worker) / ファイル作成:Python・Bash(サンドボックスコンテナ) | Python(Excel内のPython連携基盤、モデルはMicrosoft既定モデルのほかGPT系・Claude Opus系から選択可) |
| 起動方法 | チャットにファイルを添付するだけで自動起動 | チャットにファイルを添付/Sheetsのスパークルアイコンからサイドパネルを開く | 設定でオンにした上でファイルを添付、または明示的に依頼 | Excelのリボン→Copilot→「編集」モードで依頼(Pythonは必要に応じ自動起動、または明示指定も可) |
| 生成コードの可視性 | 回答内に表示され、開いて確認できる | 表示されるが折りたたみ表示が中心 | 回答内に表示され、開いて確認できる | チャット欄に表示され、新しいシートや変更履歴に分析ステップが残る |
| 対応ファイル形式 | CSV、Excel、PDF、画像など。Googleドライブ/OneDrive/Googleスプレッドシートも直接読み込み可 | CSV、XLS、XLSX、Googleスプレッドシート、テキスト等 | CSV、TSV、Excel(コード実行を有効化した場合)。出力側はxlsx・docx・pptx・pdfの実ファイルも生成可能 | 開いているExcelブック内のシート・テーブル(複数シート横断はベータ〜順次GA) |
| ファイルサイズ・件数の目安 | 1ファイル最大512MB(表形式は実質50MB程度が目安)、1会話あたり10件前後 | 1ファイル最大100MB(動画は最大2GB)、1プロンプトあたり最大10件 | 1ファイル最大30MB(アップロード・生成ファイルとも)、1会話最大20件 | Excelのブックサイズ上限に準拠(ファイルアップロードという概念がない) |
| グラフ・チャート生成 | ○(matplotlib/seabornベース、ダウンロード可) | ○(matplotlibベース) | ○(分析ツールはArtifact上に描画、ファイル作成機能はExcel内のグラフとして生成) | ○(Excelのグラフ機能と連動し、シートに直接挿入) |
| 対応プラン・料金目安 | Free(利用可だが上限が厳しい)/Go 月$8/Plus 月$20/Pro 月$200/Business(旧Team、2026年4月改定で年払い月$20〜/月払い月$25、2席以上)/Enterprise | 個人:Google AIプラン(有料、上位ほど利用上限が広い)で強化/法人:Google Workspace Business Standard以上(月$14前後〜)にGemini機能が標準搭載・追加料金なし | Free/Pro/Max/Team/Enterprise。「コード実行とファイル作成」は2026年時点で**全プラン(Freeも含む)**に開放済み | Microsoft 365 Copilotライセンス(法人向けアドオン)が前提。Pythonによる高度な分析部分は2026年もプレビュー〜順次展開の段階 |
| 日本語での分析結果の質 | 高い。要約・考察も自然な日本語で出力 | 高いが、シート内の`=AI()`はセル単位の短い出力向き | 高いが、コードのコメントは英語になりやすい | 高い。Excelの用語(ピボット、関数名)に沿った説明が得意 |
| 強み | ファイル形式を選ばず使い捨ての分析に強い。エコシステムが最も成熟 | Googleスプレッドシートを編集不要でそのまま分析・構築できる。Colabとの連携で本格的なノートブックも生成可能 | 無料プランでも本物のExcelファイル(数式付き)を生成できるようになった。コードと成果物(Artifact)を並べて確認しやすい | 分析結果が最初からExcelのシート・グラフとして残り、社内フォーマットを崩さない。GPT系・Claude系などモデルを選べる |
| 弱み | セッションが切れるとファイル再アップロードが必要 | 法人向け機能はWorkspaceプラン依存で個人利用がやや複雑 | ファイルサイズ上限が4ツール中もっとも小さい。分析ツールとファイル作成機能の使い分けがわかりにくい | Microsoft 365 Copilotライセンスが前提で、個人ユーザーには縁遠い。Pythonの高度な分析はまだ展開途上 |

### どのツールを選ぶか(判断チェックリスト)

- **とにかく手早く使い捨てで集計したい・ファイル形式を問わず投げたい** → ChatGPT。実績・対応形式の広さで最も無難
- **すでにGoogleスプレッドシートで管理している数字をその場で聞きたい・シートの構築自体も任せたい** → Gemini(Sheetsのサイドパネル)。アップロードの手間がなく、2026年からは複数テーブル横断の集計・シート編集まで頼める
- **無料で試したい、かつ成果物を本物のExcelファイル(数式付き)として受け取りたい** → Claude。2026年時点で「コード実行とファイル作成」がFreeプランでも有効化でき、Microsoft 365 Copilotライセンスがなくても実ファイルを作れる
- **分析結果を最終的にExcelの体裁(表・グラフ・関数)のまま、既存ブックに直接反映したい** → Copilot in Excel。ただしMicrosoft 365 Copilotライセンスが前提
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

**Google Sheetsに組み込まれたシートを直接分析・構築する場合**
1. Google Sheetsでファイルを開き、右上の★(スパークル)アイコンをクリックしてGeminiのサイドパネルを開く
2. 「A列の売上をB列の地域別に集計して」のように話しかけるか、セルに `=AI("売上上位3商品を教えて", A1:C100)` のように関数として埋め込む
3. 2026年4月以降は「シート内の複数テーブルをまたいだ集計」「XLOOKUPなど数式の自動生成」「表の書式設定」まで依頼できる
4. 個人利用ではGoogle AIプラン、法人利用ではGoogle Workspace Business Standard以上の契約でGemini機能が有効になっている必要がある(法人向けは追加課金なしで標準搭載)

### Claude: 基本手順

1. `claude.ai` の左下のアカウント名→「設定」→「Capabilities(機能)」で「コード実行とファイル作成(Code execution and file creation)」をオンにする。2026年時点でFree/Pro/Max/Team/Enterpriseいずれの契約でも有効化できる
2. チャットにCSV・Excelファイル(1ファイル30MBまで、1会話最大20件)を添付し、「このデータを分析して傾向をグラフで見せて」と依頼すると、まず軽量な分析ツール(JavaScript)が動き、会話右側の「Artifact(成果物パネル)」に表やグラフが表示される
3. 「分析結果を数式付きのExcelファイルにして」のように成果物の形式を明示すると、Python・Bashのサンドボックスコンテナを使う「コード実行とファイル作成」機能に切り替わり、実際に開いて編集できる.xlsx/.docx/.pptx/.pdfファイルが生成される(こちらも30MBまで)

### Copilot(Excel): 基本手順

1. 分析したいExcelファイルをOneDrive上に保存した状態で開く(ローカル保存のみのファイルでは利用できない場合がある)
2. リボンの「ホーム」タブから「Copilot」をクリックし、右側にサイドパネルを開く
3. パネル上部の「チャット/編集」切り替えで「編集(Edit with Copilot)」を選び、「Pythonを使ってこのデータを分析し、月次の売上推移グラフを作成して」のように依頼する(Copilotが必要と判断すれば明示しなくてもPythonを自動起動する)
4. モデル選択アイコンから既定モデルのほか、GPT系・Claude Opus系など複数モデルを選べる場合がある(選択肢は更新が速いため画面上の表示で都度確認する)
5. Copilotが生成したPythonコードと分析結果が新しいシートや変更履歴に追加され、既存のブック内でそのまま確認・編集できる。この高度な分析機能はMicrosoft 365 Copilotライセンスが前提で、2026年時点も段階的な展開が続いている

### コピペで使える依頼文サンプル(ツール共通で使える表現)

```
添付のCSVは過去1年分の日次売上データです。列構成は
「日付, 店舗名, 商品カテゴリ, 売上金額, 客数」です。

1. まず列名・データ型・欠損値の有無を確認し、解釈を箇条書きで教えてください
2. 店舗×月ごとの売上合計を集計してください
3. 全店舗合計の月次売上推移を折れ線グラフにしてください(横軸:年月、縦軸:売上金額)
4. 使用したコード(Python/JavaScript)を省略せずに表示してください
```

「①解釈の確認 ②集計軸 ③グラフの種類と軸 ④コードを見せる指示」の4点を入れておくと、ツールを問わず手戻りが少ない。Claudeで実ファイル(Excel等)として受け取りたい場合は、上記に加えて「⑤数式付きのExcelファイルとして出力してください」と一文足すとよい。

## 注意点・よくある誤解

- **機密データのアップロード先を必ず確認する**: 個人向けの無料・安価なプランでは、会話やアップロードしたファイルがモデルの学習に使われる設定がデフォルトになっている場合がある。氏名・取引先名・個人情報を含むデータは、匿名化(ダミー値への置き換え)をしてから渡すか、学習への非利用がデフォルトの法人向けプラン(ChatGPT Business/Enterprise、Gemini for Workspace、Claude Team/Enterprise、Microsoft 365 Copilot)を使う
- **「コードが見える=正しい」ではない**: 生成されたコードが表示されるツール(ChatGPT・Claude・Copilot)でも、集計軸の解釈違い(日付の年度区切り、重複データの二重カウントなど)は起こり得る。重要な数値は必ずコードの中身を確認し、一部は手元のExcelやSQLの結果と突き合わせて検算する
- **ファイルサイズ上限の違いを把握しておく**: 同じ「数十万行のCSV」でも、Claudeの30MB上限では読み込めずGemini・ChatGPTでは通る、というケースがある。大きいファイルは事前に列や期間を絞り込んでから渡す
- **Claudeの「分析ツール」と「コード実行とファイル作成」は別物**: 同じ設定トグルの下にあるが、前者は軽量な集計・グラフ表示(JavaScript、Artifact表示のみ)、後者は実際に開けるExcel/Word/PowerPoint/PDFファイルを生成する(Python)。「Excelファイルとして欲しい」と明示しないと軽量な分析ツール止まりになることがある
- **Copilotは「Excelブックが前提」**: ChatGPT・Gemini・Claudeのように任意のファイルを都度アップロードする発想ではなく、開いているExcelファイルそのものを対象にする。他システムから出力したCSVをまずExcelに読み込んでから使う一手間が必要になる場合がある。Pythonによる高度な分析はMicrosoft 365 Copilotライセンス前提で、2026年時点もまだ展開途中の機能がある
- **モデル名・提供モデルの選択肢は数か月単位で変わる**: Copilot in Excelのモデル選択肢(GPT系・Claude Opus系など)は頻繁に更新される。特定バージョン名を鵜呑みにせず、実際に使う際は画面上の表示を確認する
- **セッション・分析環境は保存されない(Copilot以外)**: ChatGPT・Gemini・Claudeでの分析はチャットが終わると実行環境が消え、翌日また使うにはファイルの再アップロードが必要。継続的に更新するダッシュボードには向かず、Excel(Copilot)やBIツールの方が適している
- **日本語グラフの文字化けは共通の落とし穴**: いずれのツールも、環境に日本語フォントが入っていないとグラフのラベルが「豆腐(□□□)」化することがある。応急処置は「グラフのラベルは英語にしてください」と頼むこと

## 最初の一歩

普段使っているAIチャットツール1つに、手元の売上や経費のCSV・Excelファイルを1件アップロード(またはCopilotならブックを開いた状態でリボンから起動)し、「月次で集計してグラフにして」と頼んでみる。返ってきたコードや集計結果が意図通りかを確認し、他のツールでも同じファイルを試して違いを体感してみるとよい。Claudeを使う場合は、設定で「コード実行とファイル作成」がオンになっているか併せて確認する。

## 関連トピック

- [ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方](../part07-data-analysis/chatgpt-advanced-data-analysis.md)
- [AIが扱いやすいデータ形式](../part07-data-analysis/ai-friendly-data-formats.md)
- [Google Geminiの基本](./google-gemini-basics.md)
- [Claude(Anthropic)の基本](./claude-basics.md)
- [Microsoft Copilotの基本](./microsoft-copilot-basics.md)
- [ChatGPTのプラン比較](./chatgpt-plan-comparison.md)

## 更新履歴

### 2026-08-05: 全ツールの最新状況を反映して増強
- **内容**: Claudeの「分析ツール(JavaScript/Artifact)」と新しい「コード実行とファイル作成(Python/Bash、実際のExcel/Word/PowerPoint/PDFを生成、2026年時点でFreeプランにも開放)」の違いを追記。Gemini in Google Sheetsが2026年4月に複数テーブル横断の集計・数式生成・シート構築まで対応した点、ChatGPT Team→Business改称と2026年4月の料金改定($20/席・年払い、2席以上)、Copilot in Excelの「編集」モードへのPython統合とGPT系・Claude Opus系のモデル選択機能を反映。ファイルサイズ上限など既存の数値は公式ヘルプで裏取りし維持
- **出典**: [File Uploads FAQ | OpenAI Help Center](https://help.openai.com/en/articles/8555545-file-uploads-faq)
- **出典**: [Data analysis with ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt)
- **出典**: [Create and edit files with Claude | Claude Help Center](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- **出典**: [Claude can now create and edit files | Claude by Anthropic](https://claude.com/blog/create-files)
- **出典**: [Notes on the new Claude analysis JavaScript code execution tool | Simon Willison](https://simonwillison.net/2024/Oct/24/claude-analysis-tool/)
- **出典**: [Gemini アプリでファイルをアップロードして分析する | Gemini アプリ ヘルプ](https://support.google.com/gemini/answer/14903178?hl=ja)
- **出典**: [Google Workspace Updates: Build and edit complex spreadsheets with Gemini in Google Sheets (2026-04)](https://workspaceupdates.googleblog.com/2026/04/build-and-edit-complex-spreadsheets-with-Gemini-in-Google-Sheets.html)
- **出典**: [Google Workspace Updates: Gemini in Google Sheets can now analyze data across multiple tables](https://workspaceupdates.googleblog.com/2025/10/gemini-in-google-sheets-analyze-data.html)
- **出典**: [What's New in Excel (April 2026) | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/excelblog/whats-new-in-excel-april-2026/4502696)
- **出典**: [Unlock the power of Copilot in Excel, now generally available | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/excelblog/unlock-the-power-of-copilot-in-excel-now-generally-available/4242810)
- **出典**: [ChatGPT Team Is Now ChatGPT Business: What Changed and How to Migrate](https://www.madewell.ai/blog/chatgpt-team-now-business)

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
