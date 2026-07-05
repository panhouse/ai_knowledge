---
title: ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方
part: 6
chapter: 第2章 ChatGPTによるデータ分析
tags: [ChatGPT, データ分析, Advanced Data Analysis, Code Interpreter]
created: 2026-07-05
updated: 2026-07-05
---

# ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方

## これは何か

ExcelのVLOOKUPやピボットテーブルが苦手でも、売上データや顧客データのCSV・Excelファイルをそのままアップロードして「月次で集計してグラフにして」と日本語で頼むだけで、ChatGPTが裏側で集計・分析・グラフ作成までこなしてくれる機能である。もともとは「Code Interpreter(コードインタープリター)」、その後「Advanced Data Analysis」と呼ばれてきた機能で、2026年時点では特別なモード切り替えをしなくても、ファイルをアップロードした瞬間に自動で起動する標準機能になっている。

## 仕組み・背景

この機能の正体は、ChatGPTが裏側でPython(データ分析によく使われるプログラミング言語)のコードを自分で書き、サンドボックス(外部に影響を与えない隔離された実行環境)の中でそのコードを実際に動かして結果を返す仕組みである。集計・統計処理には主にpandas、グラフ描画にはmatplotlibなど、データ分析の定番ライブラリ(あらかじめ用意された処理部品群)が使われる。

2023年に「Code Interpreter」から「Advanced Data Analysis」へ改称された経緯があり、現在のChatGPTのヘルプセンターでは単に「データ分析(Data Analysis)」というツール名で案内されている。GPT-4o以降・GPT-5系のモデルでは、ユーザーがツールを手動で選ばなくても、ファイルが添付され分析が必要と判断されると自動的にPythonコードの生成・実行に切り替わる。回答の中に生成されたコードが表示されるため、「何を根拠にその数字が出たか」を確認できる点が、単なる自然言語での要約と異なる大きな特徴である。

## 使いどころ・使い分け

| 用途 | ChatGPTのデータ分析 | Excel(関数・ピボット) | BIツール(Tableau、Power BIなど) |
|---|---|---|---|
| 単発の集計・グラフ化 | ◎ 得意。指示するだけで完結 | ○ 手作業で可能だが時間がかかる | △ 準備(接続設定)が必要で単発には不向き |
| 複数ファイルの結合・整形 | ◎ 表記ゆれの吸収や日付形式の統一も自動化しやすい | △ VLOOKUP・パワークエリなど習熟が必要 | ○ ETL機能はあるが設計工数がかかる |
| 統計分析(相関、回帰、検定など) | ◎ コードベースで正確に実行 | △ 分析ツールアドインが必要、操作が煩雑 | △ 専用アドオンや外部ツール連携が必要 |
| 継続的に更新されるダッシュボード | × セッションが消えると再アップロードが必要 | △ 手動更新が前提 | ◎ 得意分野。自動更新・共有に強い |
| 数百万行級の大規模データ | △ 行数が多いとサンプリングされたり処理が重くなる | × 動作が重くなりがち | ◎ 得意分野 |
| 社内の誰もが編集できる形で残す | △ 出力はコピーや添付ファイルの形になる | ◎ 使い慣れたファイル形式で共有できる | ○ 権限管理された共有がしやすい |

判断基準はシンプルで、「一回限りの調査・試算・レポート作成」ならChatGPT、「継続的に更新し複数人で見る資料」ならExcelやBIツールに軍配が上がる。ChatGPTでの分析結果をたたき台にして、最終的な資料はExcelやBIツールに落とし込む、という併用が実務では現実的である。

## 実務での使い方

### 基本の操作手順(ChatGPT Webブラウザ版)

1. `chatgpt.com` にログインし、チャット入力欄の左側にあるクリップアイコン(📎)をクリックする
2. 「パソコンからアップロード」を選び、分析したいCSV・Excel・PDFなどのファイルを選択する(Googleドライブ・OneDriveからの直接読み込みにも対応)
3. アップロード完了後、そのまま日本語で依頼文を入力する(例:「月別・店舗別の売上を集計してグラフにして」)。ツールの選択操作は不要で、ファイルが添付された時点で自動的にデータ分析モードに切り替わる
4. ChatGPTが生成したPythonコードと実行結果(表・グラフ)が返ってくる。グラフ画像やExcelファイルは、メッセージ内のリンクからダウンロードできる
5. 「このコードのロジックを説明して」「集計対象を今年度だけに絞って」のように追加の指示を出せば、コードを書き直して再実行してくれる

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

### ツール横断の対応関係

| 概念 | ChatGPT | Gemini(Google) | Copilot(Excel) |
|---|---|---|---|
| 機能名 | データ分析(旧Advanced Data Analysis / Code Interpreter) | Gemini in Google Sheets(サイドパネル対話・`=AI()`関数) | Copilot in Excel のPythonによる高度な分析(2026年は「Edit with Copilot」の一部として提供) |
| 起動方法 | ファイルをアップロードして質問するだけで自動起動 | Sheetsを開き右上のスパークルアイコンからサイドパネルを開く、またはセルに`=AI()`と入力 | Excelのリボンから「Copilot」を開き、チャットでPythonによる分析を依頼 |
| 前提プラン | Free(利用回数は限定)/ Plus・Pro・Business・Enterprise | Google Workspace(Business Standard以上)+ Gemini機能、Personalでも一部利用可 | Microsoft 365 Copilotライセンスが必須(Business Standard/Premium等 + Copilotアドオン) |
| 強み | ファイル形式を選ばず使い捨ての分析に強い | シート自体をライブ編集でき、アップロード不要 | Excelファイルそのものを直接編集し、社内フォーマットを崩さない |

### 料金・アップロード上限の目安(2026年7月時点)

- ファイルサイズの上限は1ファイルあたり512MBが上限だが、CSV・Excelなどの表形式ファイルは行数の多さによって実質50MB程度が目安になる
- テキスト・文書ファイルは1ファイルあたり最大200万トークン(トークン=AIが処理するテキストの最小単位)まで、画像は1枚20MBまで
- 1回の会話で添付できるファイル数はおおむね10件程度(GPTs機能を使うと20件まで拡張可能)
- Plusプランは3時間あたり80ファイルまでアップロード可能。無料プランはデータ分析の利用回数自体が1日数回程度に制限される
- どのプランでこの機能が使えるかは、Free(制限付き)・Plus・Pro・Business(旧Team)・Enterpriseのいずれでも利用可能で、Business/Enterpriseでは組織のデータガバナンス設定が優先される。プランごとの料金・機能差の詳細は[ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)を参照

## 注意点・よくある誤解

- **出力された数字を鵜呑みにしない**: コード実行に基づく集計なので単純な計算ミスは起きにくいが、「集計軸の解釈違い」(例:日付の年度区切りのずれ、重複データの二重カウント)は起こり得る。回答内に表示されるPythonコードを開いて、意図した条件で集計しているかを確認する習慣をつけるとよい
- **大きすぎるファイルはサンプリングされることがある**: 行数が非常に多いCSVでは、全行を読み込まずに一部だけで処理が進んでしまう場合がある。「全行を対象に計算しましたか」と聞き返す、または集計前の行数を確認させると安全
- **セッションは保存されない**: 分析に使ったファイルやPythonの実行環境は会話が終わると消える。翌日また同じファイルで分析したい場合は再アップロードが必要で、Excelのように「ファイルを開けば続きから」とはいかない
- **機密情報の扱いに注意**: 個人情報や社外秘の数値を含むデータをアップロードする際は、会社のルールとプラン(Business/Enterpriseは学習への非利用がデフォルトなど)を確認したうえで行う
- **継続利用が前提の資料には向かない**: 毎週更新するようなダッシュボードは、都度ファイルをアップロードし直す運用になり非効率。BIツールやExcelの自動更新機能に任せた方がよい

## 最初の一歩

手元にある売上や経費のCSV・Excelファイルを1つ用意し、ChatGPTの入力欄にアップロードして「月次で集計してグラフにして」と頼んでみる。返ってきたPythonコードにも目を通し、集計ロジックが意図通りかを確認してみるとよい。

## 関連トピック

- [AIが扱いやすいデータ形式](./ai-friendly-data-formats.md)
- [ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: ChatGPTのデータ分析機能(旧Code Interpreter / Advanced Data Analysis)について、2026年時点の名称・使い方・ファイルアップロード上限・対応プラン・Gemini/Copilotとの対応関係をまとめた
- **出典**: [File Uploads FAQ | OpenAI Help Center](https://help.openai.com/en/articles/8555545-file-uploads-faq)
- **出典**: [Data analysis with ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt)
- **出典**: [ChatGPT Plans | Free, Go, Plus, Pro, Business, and Enterprise](https://chatgpt.com/pricing/)
- **出典**: [Gemini in Google Sheets | Google Workspace](https://workspace.google.com/resources/spreadsheet-ai/)
- **出典**: [Get advanced data analysis using Copilot in Excel App Skills | Microsoft Support](https://support.microsoft.com/en-gb/office/get-advanced-data-analysis-using-copilot-in-excel-app-skills-364e4ae9-9343-4d56-952a-5f62b0f70db6)
- **出典**: [What's New in Excel (April 2026) | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/excelblog/whats-new-in-excel-april-2026/4502696)
- **出典**: [【2026年最新】ChatGPT Advanced Data Analysis(コードインタープリター)完全ガイド | AI PICKS マガジン](https://aipicks.jp/mag/chatgpt-advanced-data-analysis-guide-2026)
