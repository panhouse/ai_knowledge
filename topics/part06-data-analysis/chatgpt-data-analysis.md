---
title: ChatGPTのデータ分析(Advanced Data Analysis)機能
part: 6
chapter: 第2章 ChatGPTによるデータ分析
tags: [ChatGPT, データ分析, Code Interpreter, Advanced Data Analysis]
created: 2026-07-05
updated: 2026-07-05
---

# ChatGPTのデータ分析(Advanced Data Analysis)機能

## これは何か

ChatGPTに売上データのCSVやアンケート結果のExcelをアップロードすると、ChatGPTが裏側でPython(プログラミング言語)のコードを自動生成・実行し、集計・グラフ作成・統計処理までこなしてくれる機能が「データ分析」ツールである。かつては「Advanced Data Analysis」「Code Interpreter(コードインタープリター)」と呼ばれていた機能で、名称は変わったが中身は同じ。Excelで数十分かけていたピボット集計やグラフ作成が、自然な日本語の指示だけで数十秒で終わる。関数やVBAを書けなくても、統計的に妥当な分析を任せられるのが最大の価値である。

## 仕組み・背景

ChatGPTはファイルがアップロードされ、分析を求める指示を受け取ると、サンドボックス化された(外部から隔離された)Python実行環境を起動する。この環境はpandas(表データ処理)・Matplotlib(グラフ描画)・NumPy・scikit-learnなど数百のライブラリがあらかじめ入ったJupyterノートブック的な環境で、インターネットには接続できない。ChatGPTは会話の流れに応じてPythonコードを自動生成し、その場で実行して結果(表・グラフ・統計量)をチャットに返す。生成したコードは「実行したコードを見せて」と頼めばそのまま表示され、内容を検証できる。

以前は「Advanced Data Analysis」という機能名がChatGPTのメニューに表示され、GPT-4時代は手動でオンにする必要があった時期もあったが、現在のChatGPT(GPT-5系モデル)ではファイルをアップロードして分析系の指示を出せば自動的に発動し、ユーザーが機能名を意識する場面は少ない。名称としてはOpenAIのヘルプセンターでも現在は単に「データ分析(data analysis)」と表記されることが多い。ただし、自作の「GPTs(カスタムGPT)」を作る際は、GPT Builderの「Capabilities」欄で「Code Interpreter & Data Analysis」を明示的にONにする必要がある。

## 使いどころ・使い分け

| 場面 | 使う/使わない |
|---|---|
| 数千行程度のCSV・Excelの集計・グラフ化 | 使う。ピボット集計やグラフ作成を自然言語の指示だけで済ませられる |
| 相関分析・t検定・回帰分析などの統計処理 | 使う。ただしモデルが選んだ手法・前提条件の妥当性は必ず自分で確認する |
| アンケートの自由記述の分類・要約と数値回答の集計を同時にやりたい | 使う。テキストとしての理解とPythonでの集計を両方一度に頼めるのが強み |
| 個人情報・取引先情報など機密データを含むファイル | 使うにしても、学習に利用されない設定・プラン(Business/Enterprise、あるいは個人プランでの学習オプトアウト設定)を確認してから渡す |
| 100万行を超える大規模データ、リアルタイム更新が必要な分析 | 使わない。処理が遅くなったりメモリエラーが出たりする。BIツール(Looker StudioやTableau等)やSQLでの集計が適する |
| 元のExcel/スプレッドシートをそのまま更新し続けたい共同編集の表 | 使わない。ChatGPTの分析結果は別ファイルとして書き出されるだけで元データは更新されない。Geminiのスプレッドシート統合や通常のExcel関数の方が向く |

## 実務での使い方

### 対応プランと使える範囲(2026年7月時点)

| プラン | データ分析機能の利用 |
|---|---|
| Free | 利用は可能だが、1日あたりのファイル添付数・利用回数が数回程度に限定される |
| Go | Freeより上限は緩和されるが、Plusより制限は厳しい |
| Plus($20/月) | 3時間あたり最大80ファイルまで添付可能など、業務利用に十分な上限 |
| Pro($100・$200/月) | Plusよりさらに高い上限 |
| Business(旧Team)・Enterprise | 組織向けにより高いアップロード上限。デフォルトで会話データがモデル学習に使われない設定 |

プラン名・料金体系は変更が頻繁なため、最新の対応可否は[ChatGPT公式の料金ページ](https://chatgpt.com/pricing)で確認すること(プラン体系の詳細は[ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)を参照)。

### 対応ファイル形式とサイズの上限

- **対応形式**: CSV・TSV・Excel(.xlsx/.xls)・JSON・PDF・画像・Word/PowerPoint・コードファイルなど幅広く対応
- **ファイルサイズ**: 1ファイルあたり最大512MBというハード上限があるが、CSV・Excelなど表データは各行のサイズにもよるが実質50MB程度が目安。テキスト・文書系ファイルは1ファイルあたり最大200万トークンという別の上限もある
- **アップロード数**: Freeは1日3ファイル程度、Plusは3時間あたり80ファイルまで
- **保存容量**: 1ユーザーあたり25GB、組織全体で100GBという上限がある

### 画面での操作手順

1. ChatGPTのチャット入力欄の左にある「+」(ファイルを追加)アイコンをクリック
2. 「写真とファイルを追加」からパソコン内のCSV・Excel・PDFなどを選択してアップロード
3. アップロード後、そのまま「〜を分析して」「〜のグラフを作って」と日本語で指示するとPythonコードが自動生成・実行され、結果が表やグラフで返ってくる
4. 生成されたグラフは右クリック(または画像上のダウンロードアイコン)で画像として保存、加工後のデータはCSV/Excelとしてダウンロード可能

自作のGPTsで常にこの機能を使わせたい場合は、GPT編集画面の「Configure」タブ→「Capabilities」欄で「Code Interpreter & Data Analysis」のチェックボックスをONにする。

### コピペで使えるプロンプト例

**① 部門別売上のグラフ化**
```
アップロードしたCSVを分析して、部門別の月次売上を積み上げ棒グラフにしてください。
列名は「部門」「年月」「売上金額」です。売上の少ない部門から多い部門の順に凡例を並べ、
グラフの下に売上上位3部門のコメントを2〜3行で添えてください。
```

**② アンケートの集計と自由記述の分類**
```
このアンケート回答データ(Q1〜Q10は5段階評価、Q11は自由記述)を分析してください。
・Q1〜Q10は設問ごとの平均点と回答分布を表とグラフでまとめる
・Q11の自由記述はよくある意見を3〜5個のカテゴリーに分類し、件数の多い順に一覧化する
・数値評価が低い設問と自由記述の内容に関連がありそうな場合はその傾向も指摘する
```

**③ データクリーニング**
```
このExcelファイルについて、重複行・欠損値・表記ゆれ(全角/半角の混在、会社名の新旧表記など)
を検出してください。検出した問題点を一覧表にした上で、クリーニング後のデータを
ダウンロードできる形式(CSV)で出力してください。
```

**④ 統計的な有意差の検証**
```
A群とB群の売上データに統計的に有意な差があるか検定してください。
検定手法を選ぶ前に正規性・等分散性を確認し、どの検定(t検定・Mann-Whitney U検定等)を
選んだ理由を説明してください。有意水準は5%とします。
```

**⑤ 要因分析・相関の可視化**
```
各列(価格、広告費、来店数、天気、売上)の相関関係をヒートマップで可視化してください。
売上に最も影響していそうな変数を3つ挙げ、それぞれ相関係数と考えられる理由を添えてください。
```

### ツール横断の対応付け(Geminiとの比較)

Google Geminiにも同種の機能があるが、実行される「場所」がChatGPTとは異なる。

| 観点 | ChatGPT(データ分析) | Gemini |
|---|---|---|
| 機能名 | データ分析(旧Advanced Data Analysis/Code Interpreter) | コード実行機能(Geminiアプリのチャット内) / Gemini in Google Sheets(スプレッドシートのサイドパネル) |
| 実行場所 | チャット内の隔離されたPython環境 | アプリのチャットはPythonコード実行(CSV・テキスト入力対応)、スプレッドシート版はシート上で直接動作 |
| 対応プラン | Free(制限あり)/Go/Plus/Pro/Business/Enterprise | アプリのコード実行は個人アカウントで利用可。スプレッドシート版はGoogle Workspace Business Standard以上(Business Starterは対象外)、または個人向けGoogle AI Pro/Ultraが必要 |
| 対応ファイル | CSV/TSV/Excel/JSON/PDF/画像など | CSV/TXT/XLS/PDF/Googleスプレッドシートなど |
| 強み | 複雑な多段階集計・統計検定に強く、生成コードを開いて検証できる | スプレッドシート版は元の表に直接関数や要約を反映できるため、社内で使い続ける資料としてそのまま残せる |
| 弱み | 分析結果はチャット内の別ファイルとして出力され、元のExcel自体は更新されない | スプレッドシート版は複雑な統計解析には不向きで、関数提案・単純集計向き。実行時間の上限(30秒程度)もあり大規模データの重い処理には向かない |

「元の表をそのまま更新し続けたい」ならGeminiのスプレッドシート統合、「複雑な統計処理や多段階のデータ加工を任せたい」ならChatGPTのデータ分析、という使い分けが基本になる(Geminiの概要は[Google Geminiの基本](../part07-other-llm-tools/google-gemini-basics.md)を参照)。

## 注意点・よくある誤解

- **元のExcelファイルは更新されない**: 分析結果はチャット内で新たに生成された表・グラフ・ファイルであり、アップロード元のファイル自体が書き換わるわけではない。必要な結果は都度ダウンロードして保存する。
- **自動生成されたコード・統計手法を無条件に信じない**: モデルが選んだ集計方法や検定手法が最適とは限らない。「実行したコードを見せて」と頼んでロジックを確認し、重要な数値は手元の値と突き合わせて検算する。
- **大規模データは処理が不安定になる**: 明示的な行数上限はないが、100万行を超えると処理が遅くなったり途中でメモリエラーが出たりすることがある。事前に必要な列・期間だけに絞ってから渡す。
- **セッションは一定時間で切れる**: 操作がない状態が続くとPython実行環境のセッションがタイムアウトし、それまでの中間変数やアップロード済みファイルの状態は失われる。長い分析は要所でこまめに結果をダウンロードしておく。
- **削除してもサーバーからの完全消去には時間がかかる**: アップロードしたファイルを削除すると自分の画面からは即座に消えるが、OpenAI側のサーバーから完全に消去されるまで最大30日かかるとされている。機密データを扱う前に、社内の情報取り扱いルールを確認する([生成AI利用における情報漏洩対策](../part03-risk-security/information-leakage-prevention.md)も参照)。
- **プランごとの上限は変更が頻繁**: ファイルサイズ・アップロード数の上限は本ページ執筆時点の目安であり、今後変わる可能性がある。業務で使う前に[ChatGPT公式ヘルプ](https://help.openai.com/en/articles/8555545-file-uploads-faq)で最新値を確認する。

## 最初の一歩

手元にある数百行程度の売上データやアンケート結果のExcel・CSVを1つChatGPTにアップロードし、「部門別の月次売上を棒グラフにして」のように具体的に指示して、実際にどんなコードが動いてグラフができるかを一度試してみる。

## 関連トピック

- [AIが扱いやすいデータ形式](ai-friendly-data-formats.md)
- [ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)
- [Google Geminiの基本](../part07-other-llm-tools/google-gemini-basics.md)
- [生成AI利用における情報漏洩対策](../part03-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: ChatGPTのデータ分析(旧Advanced Data Analysis/Code Interpreter)機能の仕組み、対応プラン・ファイル形式・サイズ上限、活用シーンごとのコピペ用プロンプト例、Geminiのコード実行機能・Gemini in Google Sheetsとの比較を整理
- **出典**: [OpenAI Help Center: Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt)、[OpenAI Help Center: File uploads FAQ](https://help.openai.com/en/articles/8555545-file-uploads-faq)、[OpenAI Academy: Analyzing data with ChatGPT](https://openai.com/academy/data-analysis/)、[Fastio: ChatGPT File Upload Limit 2026](https://fast.io/resources/chatgpt-file-upload-limit/)、[datastudios.org: ChatGPT Spreadsheet Uploading](https://www.datastudios.org/post/chatgpt-spreadsheet-uploading-excel-and-csv-file-support-data-analysis-features-formula-handling)、[AIsmiley: Gemini×Googleスプレッドシート活用のコツ](https://aismiley.co.jp/ai_news/gemini-google-sheets/)、[Google Workspace Help: Compare Google AI expansion add-ons](https://knowledge.workspace.google.com/admin/getting-started/editions/compare-google-ai-expansion-add-ons)、[Google AI for Developers: コードの実行](https://ai.google.dev/gemini-api/docs/code-execution)、[Google Gemini アプリ ヘルプ: ファイルをアップロードして分析する](https://support.google.com/gemini/answer/14903178?hl=ja)
- **注記**: OpenAIヘルプセンターの一部ページへの直接アクセスができなかったため、ファイルサイズ・アップロード数などの一部数値は複数の第三者情報のクロスチェックに基づく目安。正確な最新値は[ChatGPT公式ヘルプ](https://help.openai.com/en/articles/8555545-file-uploads-faq)で要確認
