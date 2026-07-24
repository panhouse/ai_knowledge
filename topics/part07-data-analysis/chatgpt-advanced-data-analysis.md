---
title: ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方
part: 7
chapter: 第2章 チャットAIによるデータ分析
tags: [ChatGPT, データ分析, Advanced Data Analysis, Code Interpreter, Python, Excel, ライブラリ]
created: 2026-07-05
updated: 2026-07-21
---

# ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方

## これは何か

ExcelのVLOOKUPやピボットテーブルが苦手でも、売上データや顧客データのCSV・Excelファイルをそのままアップロードして「月次で集計してグラフにして」と日本語で頼むだけで、ChatGPTが裏側で集計・分析・グラフ作成までこなしてくれる機能である。もともとは「Code Interpreter(コードインタープリター)」、その後「Advanced Data Analysis」と呼ばれてきた機能で、2026年時点では特別なモード切り替えをしなくても、ファイルをアップロードした瞬間に自動で起動する標準機能になっている。

## 仕組み・背景

この機能の正体は、ChatGPTが裏側でPython(データ分析によく使われるプログラミング言語)のコードを自分で書き、サンドボックス(外部に影響を与えない隔離された実行環境)の中でそのコードを実際に動かして結果を返す仕組みである。集計・加工にはpandas、グラフ描画にはmatplotlib・seaborn、数値計算・統計にはnumpy・scipy、機械学習にはscikit-learnなど、データ分析の定番ライブラリ(あらかじめ用意された処理部品群)があらかじめ使える状態になっている。この実行環境は「ステートフル」なJupyterノートブック型(会話の間、変数やデータの状態を保持し続けるPython実行環境)であり、同じ会話内なら「今度は地域別に分けて」「前年同月比も追加して」と条件を変えながら追い込んでいける。なお、このサンドボックスはセキュリティ上の理由で外部ネットワークから遮断されているため、株価をAPIで取得する・Webサイトから最新データを取ってくるといった処理はできず、分析対象は事前にアップロードしたファイルに限られる。

名称の変遷は、2023年7月に「Code Interpreter」としてベータ公開され、同年8月に「Advanced Data Analysis」へ改称、現在のChatGPTのヘルプセンターでは単に「データ分析(Data Analysis)」というツール名で案内されている。GPT-4o以降のモデルでは、ユーザーがツールを手動で選ばなくても、ファイルが添付され分析が必要と判断されると自動的にPythonコードの生成・実行に切り替わる(2026年7月時点の主力モデルはGPT-5.6系。7月9日にGPT-5.6 Sol/Terra/Lunaが正式提供され、旧世代のGPT-5.4は同月23日に廃止予定だが、いずれの世代でもデータ分析の自動起動という挙動自体は変わらない)。回答の中に生成されたコードが表示されるため、「何を根拠にその数字が出たか」を確認できる点が、単なる自然言語での要約と異なる大きな特徴である。なお、GPTストアには「Data Analyst」という名前のカスタムGPTも存在するが、標準搭載のデータ分析機能とは別物なので混同しないこと。

2026年3月には、アップロードしたファイルやChatGPTが生成したファイルを会話をまたいで自動保存し、サイドバーの「ライブラリ(Library)」タブから呼び出して再利用できる機能が追加された。これにより、翌日また同じファイルを分析したいときにファイルそのものを再アップロードする手間は減ったが、Pythonの実行環境(変数やデータの状態)自体は新しい会話ごとにリセットされる点は変わらない。詳細は後述の「実務での使い方」「注意点」を参照。

## 使いどころ・使い分け

| 用途 | ChatGPTのデータ分析 | Excel(関数・ピボット) | BIツール(Tableau、Power BIなど) |
|---|---|---|---|
| 単発の集計・グラフ化 | ◎ 得意。指示するだけで完結 | ○ 手作業で可能だが時間がかかる | △ 準備(接続設定)が必要で単発には不向き |
| 複数ファイルの結合・整形 | ◎ 表記ゆれの吸収や日付形式の統一も自動化しやすい | △ VLOOKUP・パワークエリなど習熟が必要 | ○ ETL機能はあるが設計工数がかかる |
| 統計分析(相関、回帰、検定など) | ◎ コードベースで正確に実行 | △ 分析ツールアドインが必要、操作が煩雑 | △ 専用アドオンや外部ツール連携が必要 |
| 継続的に更新されるダッシュボード | △ ファイル自体は「ライブラリ」に保存され再アップロードは不要になったが、集計・グラフ作成の指示は会話ごとにやり直しになる | △ 手動更新が前提 | ◎ 得意分野。自動更新・共有に強い |
| 数百万行級の大規模データ | △ 行数が多いとサンプリングされたり処理が重くなる | × 動作が重くなりがち | ◎ 得意分野 |
| 社内の誰もが編集できる形で残す | △ 出力はコピーや添付ファイルの形になる | ◎ 使い慣れたファイル形式で共有できる | ○ 権限管理された共有がしやすい |

判断基準はシンプルで、「一回限りの調査・試算・レポート作成」ならChatGPT、「継続的に更新し複数人で見る資料」ならExcelやBIツールに軍配が上がる。ChatGPTでの分析結果をたたき台にして、最終的な資料はExcelやBIツールに落とし込む、という併用が実務では現実的である。もう1つの判断軸は「答えの数字が1つでも間違っていたら困るか」。困る集計は必ずファイルを渡してコードで計算させること。ファイルを添付せずに「これとこれの合計は?」と文章だけで聞くと、コードを実行せず言葉として"それらしい数字"を答えてしまうことがある。

## 実務での使い方

### 基本の操作手順(ChatGPT Webブラウザ版)

1. `chatgpt.com` にログインし、チャット入力欄の左側にあるクリップアイコン(📎)をクリックする
2. 「パソコンからアップロード」を選び、分析したいCSV・Excel・PDFなどのファイルを選択する(Googleドライブ・OneDriveからの直接読み込みにも対応し、Googleスプレッドシートも変換せずそのまま読み込める)
3. アップロードが完了すると、行・列をスクロールして中身を確認できる「インタラクティブテーブル」が表示されるので、列名や行数がイメージ通り読み込まれているかを確認し、そのまま日本語で依頼文を入力する(例:「月別・店舗別の売上を集計してグラフにして」)。ツールの選択操作は不要で、ファイルが添付された時点で自動的にデータ分析モードに切り替わる
4. ChatGPTが生成したPythonコードと実行結果(表・グラフ)が返ってくる。グラフ画像やExcelファイルは、メッセージ内のリンクからダウンロードできる
5. 「このコードのロジックを説明して」「集計対象を今年度だけに絞って」のように追加の指示を出せば、コードを書き直して再実行してくれる
6. アップロードしたファイルとChatGPTが生成したファイルは、自動的に画面左サイドバーの「ライブラリ」タブにも保存される。翌日以降、別の会話で同じファイルを使いたいときは、クリップアイコンから「ライブラリから追加」を選べば再アップロードせずに呼び出せる(2026年3月導入。Plus・Pro・Businessで利用可能、Free・Goにも順次拡大中)

### コピペで使える実例プロンプト(月次売上集計とグラフ化)

```
以下のCSVファイルは、過去2年分の日次売上データです。
列構成: 日付, 店舗名, 商品カテゴリ, 売上金額, 客数

次の作業をお願いします。
1. 店舗×月ごとの売上合計を集計した表を作成する
2. 全店舗合計の月次売上推移を折れ線グラフにする(横軸:年月、縦軸:売上金額)
3. 各店舗の前年同月比(YoY成長率)を計算し、伸び率が高い上位3店舗をコメントで指摘する
4. 集計結果をExcelファイル(.xlsx)としてダウンロードできる形で出力する
```

このように「①集計軸 ②グラフの種類と軸 ③追加の分析観点 ④出力形式」の4点を具体的に指定すると、手戻りが少ない。

### 用途別の実例プロンプト

**複数ファイルの結合・データクリーニング**
```
アップロードした2つのExcelファイルを「顧客ID」列で結合してください。
結合後、値が欠損している行、重複している行があれば件数と内容を教えてください。
```

**比較・異常値の発見**
```
先月と今月の売上データを比較して、前月比の変化率が大きい上位10商品を教えてください。
集計に使ったPythonコードも見せてください。
```

**分析結果のアウトプット化**
```
これまでの分析結果を、社内報告用にスライド構成の骨子(章立てと各章の要点)としてまとめてください。
グラフはどのスライドに使うと効果的かも提案してください。
```

### 実務のコツ①: いきなり集計せず「解釈の確認」を先に入れる

列名が曖昧なデータでは、依頼文の最初に「まず列名と各列のデータ型、欠損値の有無を確認し、あなたがどう解釈したかを箇条書きで教えてください」という1ステップを入れると、ChatGPTがどの列を何だと理解したかを集計前に確認でき、誤読による誤集計を防ぎやすくなる。あわせて「金額の単位は円です。日付は yyyy-mm-dd 形式です」のように単位・形式を明示しておくと解釈のブレが減る。

### 実務のコツ②: 日本語グラフの文字化け(豆腐化)対策

ChatGPTのグラフ生成環境には標準で日本語フォントが入っていないため、グラフの日本語ラベルが「豆腐(□□□)」に化けることがある。対策は、Google Fontsなどで配布されている「Noto Sans JP」のフォントファイル(.ttf)をChatGPTにアップロードし、「アップロードした日本語フォントを使ってグラフを描画してください」と明示的に指示すること。カスタムGPTを作る場合は、フォントファイルを「知識」に登録し、指示文に「グラフは常にこのフォントを使うこと」と書いておくと毎回のアップロードが不要になる。急ぎの場合は「グラフのラベルは英語にしてください」と頼むのが最も手軽。

### ツール横断の対応関係

| 概念 | ChatGPT | Gemini(Google) | Copilot(Excel) | Claude(Anthropic) |
|---|---|---|---|---|
| 機能名 | データ分析(旧Advanced Data Analysis / Code Interpreter) | Gemini in Google Sheets(サイドパネル対話・`=AI()`関数) | Copilot in Excel のPythonによる高度な分析(2026年は「Edit with Copilot」の一部として提供) | 分析ツール(Analysis tool / code execution)。Excel文書に組み込む「Claude for Excel」という別機能もある |
| 起動方法 | ファイルをアップロードして質問するだけで自動起動 | Sheetsを開き右上のスパークルアイコンからサイドパネルを開く、またはセルに`=AI()`と入力 | Excelのリボンから「Copilot」を開き、チャットでPythonによる分析を依頼 | claude.aiにCSV/Excelを添付して依頼。結果はArtifact(会話横に表示される成果物パネル)にも表示 |
| 前提プラン | Free(利用回数は限定)/ Go・Plus・Pro・Business・Enterprise | Google Workspace(Business Standard以上)+ Gemini機能、Personalでも一部利用可 | Microsoft 365 Copilotライセンスが必須(Business Standard/Premium等 + Copilotアドオン) | Free / Pro / Team / Enterprise |
| 強み | ファイル形式を選ばず使い捨ての分析に強い | シート自体をライブ編集でき、アップロード不要 | Excelファイルそのものを直接編集し、社内フォーマットを崩さない | コードと成果物を並べて確認しやすい。ただしファイル上限は1件30MBとChatGPTより小さい |

### 料金・アップロード上限の目安(2026年7月時点)

- ファイルサイズの上限は1ファイルあたり512MBが上限だが、CSV・Excelなどの表形式ファイルは行数の多さによって実質50MB程度が目安になる
- テキスト・文書ファイルは1ファイルあたり最大200万トークン(トークン=AIが処理するテキストの最小単位)まで、画像は1枚20MBまで
- 1回の会話で添付できるファイル数はおおむね10件程度(GPTs機能を使うと20件まで拡張可能)
- Plus・Businessプランは3時間あたり80ファイルまでアップロード可能、Proプランは実質無制限。無料プランはファイル添付が1日3件程度に制限され、大きめのファイルの分析は不安定になりやすいため、日常的に使うなら有料プランが前提になる
- 2025年に日本でも提供が始まった低価格プラン「ChatGPT Go」(月額1,500円程度)でも、無料プランの10倍相当のファイルアップロード枠でデータ分析機能を使える。Plusの月額3,000円まで出せない場合の現実的な入口になる
- どのプランでこの機能が使えるかは、Free(制限付き)・Go・Plus・Pro・Business(旧Team)・Enterpriseのいずれでも利用可能で、Business/Enterpriseでは組織のデータガバナンス設定が優先される。プランごとの料金・機能差の詳細は[ChatGPTのプラン比較](../part03-ai-chat-tools/chatgpt-plan-comparison.md)を参照
- 前述の「ライブラリ」に保存できる総容量はプランごとに上限があり、目安はFree 500MB・Go 4GB・Plus/Business 20GB・Pro 100GBである。ライブラリから手動で削除したファイルは、30日以内にシステムから完全に消去される

## 注意点・よくある誤解

- **出力された数字を鵜呑みにしない**: コード実行に基づく集計なので単純な計算ミスは起きにくいが、「集計軸の解釈違い」(例:日付の年度区切りのずれ、重複データの二重カウント)は起こり得る。エラーが出ないまま、意図と違う条件で集計した結果を「正しい答え」として返してくることもある。回答内に表示されるPythonコードを開いて意図した条件で集計しているかを確認し、重要な数値は一部を手元のExcelやSQLの結果と突き合わせて検算する習慣をつけるとよい
- **大きすぎるファイルはサンプリングされることがある**: 行数が非常に多いCSVでは、全行を読み込まずに一部だけで処理が進んでしまう場合がある。「全行を対象に計算しましたか」と聞き返す、または集計前の行数を確認させると安全。数十万行を超えるデータは事前にSQL/BigQueryなどで集計・絞り込みをしてから渡すか、必要な列・期間だけに分割して渡す
- **サンドボックスにインターネット接続はない**: 実行環境は外部ネットワークから遮断されているため、最新の株価をAPIで取得する、社内データベースに直接クエリする、Webサイトをスクレイピングするといった処理はできない。分析対象は事前にアップロードしたファイルに限られる
- **ファイルは残っても、分析の続きはできない**: 2026年3月に「ライブラリ」機能が加わり、アップロード済み・生成済みのファイルそのものは会話が終わっても消えず、別の会話から呼び出して使い回せるようになった(旧版では会話ごとに再アップロードが必要だったが、この点は改善済み)。ただし、Pythonの実行環境(それまでに計算した変数やコードの状態)は依然として会話ごとにリセットされるため、Excelのように「ファイルを開けば集計の続きから」とはいかず、新しい会話では集計・グラフ化の指示を最初からやり直す必要がある。生成されたグラフやExcelファイルのダウンロードリンクも時間が経つと切れることがあるため、重要な出力はその場でダウンロードしておく
- **機密情報の扱いに注意**: 個人情報や社外秘の数値を含むデータをアップロードする際は、会社のルールとプラン(Business/Enterpriseは学習への非利用がデフォルトなど)を確認したうえで行う。個人向けプランでは、アカウントアイコン→設定→データコントロールで「すべての人のためにモデルを改善する」をオフにすれば会話をモデル学習に使わせない設定にできるが、それでも第三者サービスに機微情報を送ること自体のリスクは残るため、氏名・取引先名などはダミー値への置き換えや列の削除で匿名化してから渡すのが原則
- **元データが汚いと結果も崩れる**: セル結合や複数行の見出し、日付フォーマットの不統一があると集計の土台からズレる。渡す前にデータを整えるコツは「[AIが扱いやすいデータ形式](./ai-friendly-data-formats.md)」を参照
- **継続利用が前提の資料には向かない**: 毎週更新するようなダッシュボードは、ライブラリのおかげでファイルの再アップロードこそ不要になったものの、集計・グラフ化の指示は会話ごとにやり直しになり自動更新はされない。BIツールやExcelの自動更新機能に任せた方がよい。また、デフォルトのグラフは配色・体裁が簡素なため、社外向け資料に使う場合は色・凡例・タイトルを追加で指示するか、出力後に他のツールで整える

## 最初の一歩

手元にある売上や経費のCSV・Excelファイルを1つ用意し、ChatGPTの入力欄にアップロードして「月次で集計してグラフにして」と頼んでみる。返ってきたPythonコードにも目を通し、集計ロジックが意図通りかを確認してみるとよい。

## 関連トピック

- [AIが扱いやすいデータ形式](./ai-friendly-data-formats.md)
- [ChatGPTのプラン比較](../part03-ai-chat-tools/chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-21: ファイル「ライブラリ」機能の追加とGPT-5.6・ChatGPT Goを踏まえて最新化
- **内容**: 2026年3月に追加された、アップロード・生成ファイルを会話をまたいで保存・再利用できる「ライブラリ」機能(プラン別の保存容量、削除後30日で完全消去、Free/Goへの拡大)を反映し、「セッションは保存されない」としていた記述をファイルは残るが分析の実行状態はリセットされるという正確な内容に書き換えた。あわせて主力モデルがGPT-5.6系に進んだことと、低価格プラン「ChatGPT Go」(月額1,500円程度)でもデータ分析機能が使える点を追記した
- **出典**: [File storage and Library in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/20001052-file-storage-and-library-in-chatgpt)、[ChatGPT Library Gives Paid Users Persistent File Storage | Winbuzzer](https://winbuzzer.com/2026/03/26/openai-chatgpt-library-persistent-file-storage-paid-users-xcxwbn/)、[Introducing ChatGPT Go | OpenAI](https://openai.com/index/introducing-chatgpt-go/)、[What is ChatGPT Go? | OpenAI Help Center](https://help.openai.com/en/articles/11989085-what-is-chatgpt-go)、[OpenAI Announces ChatGPT Work and GPT-5.6 | Thurrott](https://www.thurrott.com/a-i/openai-a-i/338707/openai-announces-chatgpt-work-and-gpt-5-6)

### 2026-07-06: 重複ページの統合
- **内容**: chatgpt-data-analysis-feature.md / chatgpt-data-analysis.md / chatgpt-data-analyst.md を本ページに統合。サンドボックスのネット非接続・ステートフルなJupyter環境、「解釈の確認」を先に入れるプロンプト術、日本語グラフの豆腐化対策(Noto Sans JPアップロード)、用途別プロンプト例、Claudeとの対応関係、学習オプトアウト設定の場所、Data AnalystカスタムGPTとの混同注意を追記
- **出典**: [Improvements to data analysis in ChatGPT | OpenAI](https://openai.com/index/improvements-to-data-analysis-in-chatgpt/)
- **出典**: [豆腐文字(□□□)を解消！ChatGPTで日本語が崩れないグラフを作る方法 | Qiita](https://qiita.com/rrwatanabe/items/a37a866b9b1469134990)
- **出典**: [Create and edit files with Claude | Claude Help Center](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)
- **出典**: [Claude AI Spreadsheet Uploading | Datastudios](https://www.datastudios.org/post/claude-ai-spreadsheet-uploading-excel-and-csv-file-support-data-analysis-features-formula-handlin)
- **出典**: [ChatGPT file upload sizes explained across all plans | Datastudios](https://www.datastudios.org/post/chatgpt-file-upload-sizes-explained-across-all-plans)
- **出典**: [ChatGPT's Code Interpreter is now Advanced Data Analysis | Pluralsight](https://www.pluralsight.com/resources/blog/ai-and-data/ChatGPT-Advanced-Data-Analytics)

### 2026-07-05: 初版執筆
- **内容**: ChatGPTのデータ分析機能(旧Code Interpreter / Advanced Data Analysis)について、2026年時点の名称・使い方・ファイルアップロード上限・対応プラン・Gemini/Copilotとの対応関係をまとめた
- **出典**: [File Uploads FAQ | OpenAI Help Center](https://help.openai.com/en/articles/8555545-file-uploads-faq)
- **出典**: [Data analysis with ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt)
- **出典**: [ChatGPT Plans | Free, Go, Plus, Pro, Business, and Enterprise](https://chatgpt.com/pricing/)
- **出典**: [Gemini in Google Sheets | Google Workspace](https://workspace.google.com/resources/spreadsheet-ai/)
- **出典**: [Get advanced data analysis using Copilot in Excel App Skills | Microsoft Support](https://support.microsoft.com/en-gb/office/get-advanced-data-analysis-using-copilot-in-excel-app-skills-364e4ae9-9343-4d56-952a-5f62b0f70db6)
- **出典**: [What's New in Excel (April 2026) | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/excelblog/whats-new-in-excel-april-2026/4502696)
- **出典**: [【2026年最新】ChatGPT Advanced Data Analysis(コードインタープリター)完全ガイド | AI PICKS マガジン](https://aipicks.jp/mag/chatgpt-advanced-data-analysis-guide-2026)
