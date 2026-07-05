---
title: ChatGPTのデータアナリスト機能(Advanced Data Analysis)
part: 6
chapter: 第2章 ChatGPTによるデータ分析
tags: [ChatGPT, データ分析, Code Interpreter, Python, CSV, Excel]
created: 2026-07-05
updated: 2026-07-05
---

# ChatGPTのデータアナリスト機能(Advanced Data Analysis)

## これは何か

ChatGPTにExcelやCSVファイルをアップロードすると、裏側でPython(プログラミング言語の一つ)のコードを自動で書いて実行し、集計・グラフ化・統計分析までこなしてくれる機能。関数を組んだりピボットテーブルを作ったりする手間なしに、「このデータから何が言えるか」を自然言語で聞くだけで答えが返ってくる。旧称は「Code Interpreter」で、現在は「Advanced Data Analysis」と呼ばれる(ChatGPT上では単に「ファイルを添付してデータについて質問する」という操作に統合されており、機能名を意識せず使えるようになっている)。

## 仕組み・背景

ChatGPTは通常、テキストを生成するだけで実際の計算は不得意(桁数の大きい掛け算を間違えるなど)だが、この機能をオンにするとOpenAIが用意したサンドボックス(隔離された実行環境)上でPythonコードを実際に書いて動かし、その実行結果を読んでから回答する。表計算ソフトの数式のように「値を返すだけ」ではなく、コード自体が生成されるため、集計ロジックを後から確認・検証できるのが最大の特徴。

サンドボックスにはインターネット接続がないため、外部API連携や最新のWebデータ取得はできず、あくまでアップロードされたファイルの範囲内で処理が完結する。GPT-4o以降のモデルではファイルを添付するだけで自動的にこの機能が有効になり、以前のように「Advanced Data Analysisモードに切り替える」という操作は不要になっている。

## 使いどころ・使い分け

| 得意なこと | 不得意・リスクがあること |
|---|---|
| 大きな表の集計・並べ替え・ピボット表のような多軸集計 | 数十万行を超える巨大ファイルの高速処理(ファイルサイズ上限や処理時間の制約に当たりやすい) |
| 折れ線・棒・散布図などのグラフ生成 | 見た目を細かく作り込んだ資料用グラフ(色・フォント調整はExcel/PowerPointの方が早い) |
| 外れ値・欠損値・重複データの検出 | 列の意味を早合点した集計(列名が曖昧だと誤解釈されやすい、後述) |
| 平均・相関・簡単な回帰など軽めの統計分析 | 高度な統計モデリングや厳密な検定が必要な学術・規制対応の分析 |
| 「このコードで合っているか」を人が読んで検算できる作業 | 個人情報・機密情報を含む生データをそのままアップロードする用途(下記「注意点」参照) |
| 複数ファイルの突合・マージ | 数式の再現性を社内で担保したい経理・監査業務(Excelのネイティブ数式の方が安全) |

## 実務での使い方

### 画面での操作手順

1. ChatGPT(Plus/Team/Enterprise、または法人向けプラン)にログインし、チャット入力欄のクリップアイコンからCSV・Excel(.xlsx/.xls)・JSON・PDFなどのファイルを添付する
2. ファイルが読み込まれたら、日本語で分析したい内容を指示する(モード切り替えは不要。ファイルを添付した時点で自動的にコード実行が有効になる)
3. ChatGPTが生成したPythonコードと実行結果(表・グラフ)が返る。グラフ画像やCSVは出力欄からダウンロードできる
4. 集計ロジックが正しいか不安なときは「使ったコードを見せて」「なぜこの外れ値を外れ値と判断したか説明して」と追加質問し、根拠を確認する

### コピペで使えるプロンプト例

```
添付した売上データ(CSV)を読み込んでください。
以下を実施してください。

1. 月別・地域別の売上推移を折れ線グラフにする(地域ごとに色分け)
2. 前月比・前年同月比を計算し、増減が大きい月を指摘する
3. 売上金額の外れ値(異常に高い・低い値)があれば、該当する行と考えられる原因を指摘する
4. 分析に使ったPythonコードも合わせて提示する
```

### プラン・料金の目安

Advanced Data Analysisは無料版では使えず、Plus(月額20ドル程度)・Team・Enterprise・Business系の有料プランで利用できる。無料プランはファイルアップロード自体が1日3回までに制限される。プランごとの詳細な機能差は[ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)を参照。

### ファイルサイズ・件数の目安

- CSV・スプレッドシート: 1ファイルあたり概ね50MB程度が上限の目安(行数が多いほど実際に扱える上限は下がる)
- PDFなどのドキュメント: 1ファイル512MBまで、テキスト量は1ファイル200万トークンまで
- 1メッセージに添付できるファイル数: 最大10件程度、3時間あたり80ファイルまでという投稿頻度の制限もある
- 無料アカウントの保存容量は1ユーザーあたり25GB程度が上限

これらの数値はOpenAI側の運用でたびたび調整されるため、大容量ファイルを扱う前に一度小さめのファイルで試し、エラーが出ないか確認するとよい。

### 他ツールでの同等機能

同じ「アップロードしたデータにAIがコードを書いて分析する」という機能は、ツールによって呼び名・実行環境が異なる。

| ツール | 呼び名・実体 | 特徴 |
|---|---|---|
| ChatGPT | Advanced Data Analysis(旧Code Interpreter) | ファイル添付で自動起動。Pythonをサーバー側サンドボックスで実行 |
| Google Gemini | Colabの「データサイエンスエージェント」(Gemini搭載) | 分析計画をGeminiが提案し、承認するとColabのノートブック上でPythonコードを生成・実行 |
| Microsoft Copilot(Excel) | 「Copilot in Excel」のPython連携(`PY()`関数など) | Excelのセル・シート上でPythonコードをCopilotが生成し、クラウドのサンドボックスで実行、結果がシートに戻る |
| Claude | チャット標準搭載の「Analysis」ツール | Excel/CSVを添付すると自動で有効化。ブラウザ内のJavaScriptサンドボックスで動作し、API経由の「Code execution tool」はPython実行に対応 |

## 注意点・よくある誤解

- **列の意味を早合点しやすい**: 列名が「A」「値1」のように曖昧だと、ChatGPTが売上額なのか数量なのかを誤って解釈したまま集計を進めてしまうことがある。列名は`sales_amount`のように内容が一意にわかる名前にしておくと誤読が減る(詳細は[AIが扱いやすいデータ形式](./ai-friendly-data-formats.md)を参照)
- **エラーが出ない=正しいとは限らない**: 実際にコードが実行されて数値らしきものが返るため信頼しがちだが、集計の前提条件(欠損値の扱い、日付の解釈など)を間違えたまま計算が完走することがある。重要な数値は必ず元データの一部と手計算・Excelで突き合わせて検算する
- **機密データのアップロードはリスクを伴う**: 個人情報や取引先情報を含む生データをそのままアップロードする前に、匿名化・仮名化やプランごとの学習利用有無を確認する。詳しくは[生成AI利用における情報漏洩対策](../part03-risk-security/information-leakage-prevention.md)を参照。Team/Enterprise/Business系プランでは入力データがモデル学習に使われない扱いになっているが、Free/Plus個人プランでは設定次第で学習に使われる場合がある
- **インターネットに接続していない**: サンドボックス内のPythonは外部APIや最新のWeb情報にアクセスできない。「最新の為替レートを取得して計算して」のような指示は成立しない
- **コードを見せてもらう習慣をつける**: 「使ったコードを表示して」と一言添えるだけで、集計ロジックが検証可能になる。ブラックボックスのまま結果だけを鵜呑みにしないことが実務では重要

## 最初の一歩

手元にある売上や勤怠などのCSV・Excelファイルを1つChatGPTに添付し、「月別の推移を折れ線グラフにして、外れ値があれば指摘して」と指示してみて、出てきたグラフの数値を元データの数行と突き合わせて検算してみる。

## 関連トピック

- [AIが扱いやすいデータ形式](./ai-friendly-data-formats.md)
- [生成AI利用における情報漏洩対策](../part03-risk-security/information-leakage-prevention.md)
- [ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: ChatGPTのAdvanced Data Analysis(旧Code Interpreter)の仕組み、画面での操作手順、コピペ用プロンプト例、得意・不得意の判断基準、ファイルサイズ上限、Gemini/Copilot/Claudeとの対応付け、機密データアップロードの注意点を整理
- **出典**: [OpenAI: Improvements to data analysis in ChatGPT](https://openai.com/index/improvements-to-data-analysis-in-chatgpt/)、[Pluralsight: ChatGPT's Code Interpreter is now Advanced Data Analysis](https://www.pluralsight.com/resources/blog/ai-and-data/ChatGPT-Advanced-Data-Analytics)、[fast.io: ChatGPT File Upload Limit 2026](https://fast.io/resources/chatgpt-file-upload-limit/)、[datastudios.org: ChatGPT file upload sizes explained across all plans](https://www.datastudios.org/post/chatgpt-file-upload-sizes-explained-across-all-plans)、[QWE AI Academy: ChatGPT Advanced Data Analysis File Upload Guide](https://www.qwe.edu.pl/tutorial/chatgpt-advanced-data-analysis-upload-files/)、[Google Developers Blog: Data Science Agent in Colab](https://developers.googleblog.com/en/data-science-agent-in-colab-with-gemini/)、[Microsoft Community Hub: What's New in Excel (April 2026)](https://techcommunity.microsoft.com/blog/excelblog/whats-new-in-excel-april-2026/4502696)、[datastudios.org: Claude for data analysis](https://www.datastudios.org/post/claude-for-data-analysis-how-anthropic-s-assistant-handles-files-charts-code-and-context)、[Claude Platform Docs: Code execution tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/code-execution-tool)
