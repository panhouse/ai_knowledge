---
title: ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方
part: 6
chapter: 第2章 ChatGPTによるデータ分析
tags: [ChatGPT, データ分析, Advanced Data Analysis, Code Interpreter, Excel]
created: 2026-07-05
updated: 2026-07-05
---

# ChatGPTのデータ分析機能(Advanced Data Analysis)の使い方

## これは何か

ExcelやCSVファイルをChatGPTにアップロードすると、ChatGPTが裏側でPythonコードを自動生成・実行して、集計・グラフ作成・簡単な統計処理までしてくれる機能。関数やピボットテーブルの操作に自信がなくても、「月別の売上合計を出して」と日本語で頼むだけで、正確な計算結果とグラフが返ってくる。Excel作業を代行してもらう窓口だと考えると使い方がイメージしやすい。

## 仕組み・背景

この機能は2023年7月に「Code Interpreter」というベータ機能としてChatGPT Plusに搭載され、同年8月に「Advanced Data Analysis(ADA)」へ改称された。現在(2026年7月時点)はOpenAIのヘルプページ上でも「Advanced Data Analysis」または単に「データ分析」機能と呼ばれているが、UI上で独立したトグルスイッチがあるわけではなく、ファイルを添付した時点でChatGPTが自動的にこの分析モードを使う設計になっている。GPTストアには「Data Analyst」という名前のカスタムGPTも存在するが、これは第三者が作成したものであり、標準搭載のデータ分析機能とは別物なので混同しないこと。

仕組みとしては、ユーザーがアップロードしたファイルをChatGPTが専用のサンドボックス環境(隔離されたPython実行環境)に読み込み、指示内容に応じてpandas(表計算ライブラリ)やmatplotlib(グラフ描画ライブラリ)などを使ったPythonコードをその場で書いて実行する。ChatGPT本体(大規模言語モデル)は「言葉で答えを作文する」のが基本動作だが、この機能を使うと実際にコードを動かして計算するため、桁の大きい集計や複雑な条件抽出でも計算過程に誤りが生じにくい。

## 使いどころ・使い分け

| やりたいこと | 適した方法 |
|---|---|
| ちょっとした概算・桁数の小さい暗算 | 通常のチャット回答でも答えられるが、あくまで言葉として生成した数値なので過信しない |
| 正確な合計・平均・件数集計、条件付き抽出 | ファイルを添付してデータ分析機能を使う。実際にコードを実行するため計算過程に誤りが生じにくい |
| グラフ化・可視化(棒グラフ、折れ線、散布図など) | データ分析機能。日本語の指示だけでグラフの種類・タイトル・軸ラベルまで指定できる |
| Excelのピボットテーブルや関数(SUMIFS・VLOOKUPなど)で完結する定型集計 | 使い慣れているならExcel側で処理した方が速い。ChatGPTに投げる価値が出るのは、条件が複雑・自由記述で毎回変わる・複数シートを横断するなど、定型の関数では組みにくい場面 |
| 数十万行超の大規模データ、マイナンバーや個人情報を含む機密データ | 安易にアップロードせず、社内のBI基盤や自社導入のプライベートな分析環境を検討する |

判断基準はシンプルで、「答えの数字が1つでも間違っていたら困るか」で考えるとよい。困るなら必ずファイルを渡して計算させ、雑談レベルの概算でよいなら通常のチャットでも構わない。

## 実務での使い方

### 操作手順(画面の場所)

1. ChatGPTの入力欄の左側にある「+」ボタン(PC・スマホとも同じ位置)をクリック(タップ)する
2. 表示されたメニューから「写真とファイルを追加する」を選び、手元のCSV/Excelファイルを選択する。Google DriveやMicrosoft OneDriveに保存したファイルを直接選ぶこともできる
3. アップロード完了を確認したら、チャット欄に分析してほしい内容を具体的に入力して送信する
4. ChatGPTが裏側でPythonコードを生成・実行している間、「分析中」といった実行中の表示が出る
5. 出力された表やグラフを確認し、必要に応じて「もっと〇〇して」「色を変えて」などと追加で指示する
6. グラフやExcelファイルなど生成された出力物は、チャット内に表示されるカードの右上にあるダウンロードアイコンから保存できる

### コピペで使える実例プロンプト

```
添付のCSVファイルには customer_id(顧客ID)、order_date(注文日)、
product_category(商品カテゴリ)、sales_amount(売上金額)の列があります。

1. order_dateから「年-月」を取り出し、月別のsales_amount合計を集計してください
2. 集計結果を縦棒グラフにしてください。タイトルは「月別売上推移」にしてください
3. 集計に使ったPythonコードも見せてください
```

```
このExcelファイルのSheet1にある売上データについて、product_category別の
売上合計と件数を集計した表を作成し、その表をExcelファイル(.xlsx)として
ダウンロードできる形式で出力してください。
```

```
先ほど集計した月別売上のうち、金額が大きい上位3か月を教えてください。
どのようにフィルタ・並べ替えをしたか、実行したコードも合わせて示してください。
```

### 生成されたコードを必ず確認する

出力結果の下やチャット内の折りたたみ部分に、実際に実行されたPythonコードが表示される。ブラックボックスのまま結果だけを信用せず、「どの列を対象に」「どういう条件で」集計したかを一度は目で追うこと。列の指定違いや期間の解釈違いなど、AIが意図と異なる集計をしてしまうことは珍しくない。

### 利用できるプラン・ファイルの制限(2026年7月時点)

| 項目 | 内容 |
|---|---|
| 利用可能プラン | Free(無料版)でも基本的なアップロード・分析は可能。ただしFreeは1日3ファイルまでという制限があり、大きめのファイルは不安定になりやすい。日常的に安定して使うなら実質Plus以上が前提 |
| 1ファイルの上限サイズ | 一般ファイルは最大512MB。ただしCSV/Excelなどの表データは、実務上は数十MBを超えると読み込みが遅くなったりタイムアウトしやすい |
| テキスト・PDF文書の上限 | 1ファイルあたり最大約200万トークン(トークンは文章をAIが処理する際の最小単位。日本語では1文字が1〜2トークン程度) |
| 添付できる数 | 有料プランは3時間で最大80ファイル、1回のメッセージに添付できるのはPCで最大20ファイル程度(スマホはやや少ない)。Freeは1日3ファイルまで |
| 対応ファイル形式 | CSV、Excel(.xlsx/.xls)、JSON、PDF、画像など。Google DriveやOneDrive上のGoogleスプレッドシート・Excelファイルにも直接アクセスできる |

### ツール横断の対応付け

| ツール | 呼び方・呼び出し方 | 特徴 |
|---|---|---|
| ChatGPT | データ分析機能(Advanced Data Analysis、旧Code Interpreter)。「+」ボタンからファイルを添付するだけで自動的に発動 | Google Drive/OneDrive連携、Plus以上で安定利用 |
| Gemini | ファイルアップロードによる分析(Geminiアプリ)。裏側でGoogle Colab(Googleのノートブック型Python実行環境)と連携する使い方も可能 | Googleスプレッドシートを開いた状態でサイドパネルのGeminiに直接指示することもできる |
| Claude | 分析ツール(Analysis tool、code executionとも呼ばれる)。claude.aiにCSV/Excelを添付するとPythonを実行し、結果をArtifact(会話横に表示される成果物パネル)として表示。Excel文書に組み込む「Claude for Excel」という別機能もある | 1ファイルあたり最大30MBとChatGPTより上限が小さい |

## 注意点・よくある誤解

- **アップロードしたデータが学習に使われる可能性がある**: 個人向けプランでは、アカウントアイコン→設定→データコントロールの画面で「すべての人のためにモデルを改善する」に類するトグルをオフにすることで、チャット内容をモデル学習に使わせない設定にできる。Business以上の法人プランはこの設定がデフォルトでオフになっている。機密データを扱う前に必ず設定を確認すること
- **機密情報・個人情報を含むファイルは安易にアップロードしない**: 氏名・連絡先・マイナンバーなど特定個人を識別できる情報や取引先固有の機密情報は、ダミー値への置き換えや列の削除など匿名化をしてから渡すのが原則
- **大きすぎるファイルは不安定**: 数十MBを超えるCSV/Excelや数十万行を超えるデータは、読み込みエラーやタイムアウト、途中までしか処理されないといった不具合が起きやすい。事前に不要な列・行を削って渡す
- **計算結果を鵜呑みにしない**: Pythonを実行しているため四則演算そのものは正確だが、集計対象の列やフィルタ条件をAIが誤って解釈することはある。生成されたコードを確認し、可能であれば結果の一部を手元のExcelで検算する
- **ファイルを添付せずに聞くと不正確になりやすい**: 「これとこれの合計は?」と数値を文章だけで質問すると、コードを実行せず言葉として“それらしい数字”を答えてしまうことがある。正確さが必要な集計は必ずファイルを渡して計算させる

## 最初の一歩

手元のExcel売上データ(なければサンプルのCSVでもよい)を1つ、ChatGPTの「+」ボタンからアップロードし、「月別の合計を棒グラフにして、使ったコードも見せて」と指示してみる。

## 関連トピック

- [AIが扱いやすいデータ形式](./ai-friendly-data-formats.md)
- [ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)
- [ChatGPTの初期設定とデータ利用のオプトアウト](../part02-chatgpt-basics/chatgpt-initial-setup-and-opt-out.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: ChatGPTのデータ分析機能(Advanced Data Analysis、旧Code Interpreter)の名称の経緯、利用可能プラン、ファイル制限、操作手順とコピペ用プロンプト例、Gemini・Claudeとのツール横断比較、注意点を整理
- **出典**: [Pluralsight: ChatGPT's Code Interpreter is now Advanced Data Analysis](https://www.pluralsight.com/resources/blog/ai-and-data/ChatGPT-Advanced-Data-Analytics)、[QWE AI Academy: ChatGPT Advanced Data Analysis File Upload Guide](https://www.qwe.edu.pl/tutorial/chatgpt-advanced-data-analysis-upload-files/)、[AI総合研究所: ChatGPTにファイルを読み込ませる方法](https://www.ai-souken.com/article/loading-files-into-chatgpt)、[アドネスラボ: ChatGPT無料版の制限](https://addness.co.jp/media/chatgpt-free-limit/)、[AI Market: ChatGPTのAdvanced Data Analysis機能](https://ai-market.jp/services/chatgpt-code-interpreter/)、[Google Geminiヘルプ: ファイルをアップロードして分析する](https://support.google.com/gemini/answer/14903178?hl=ja)、[Claude Help Center: Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)、[datastudios.org: Claude AI Spreadsheet Uploading](https://www.datastudios.org/post/claude-ai-spreadsheet-uploading-excel-and-csv-file-support-data-analysis-features-formula-handlin)
