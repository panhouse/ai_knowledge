---
title: NotebookLM(Gemini Notebook)の基本
part: 8
chapter: 第1章 検索・リサーチ特化
tags: [NotebookLM, Gemini Notebook, Google, RAG, 要約]
created: 2026-07-05
updated: 2026-08-03
---

# NotebookLM(Gemini Notebook)の基本

## これは何か

NotebookLMは、Googleが提供する「AIノートブック」で、ChatGPTやGeminiアプリのような汎用チャットAIとは違い、**ユーザーが自分でアップロードした資料(ソース)の中だけ**を根拠に質問に答えたり要約を作ったりするツールである。2026年7月16日、Googleはこのサービスの名称を**「Gemini Notebook」に改称**した。既存の共有リンクやURLはそのまま使え(URLの一部は `notebooklm.google.com` のまま、ヘルプページは `support.google.com/gemininotebook` に移行済み)、機能面での破壊的な変更もなかった。改称から2週間以上が経ち画面上の表記・ロゴは「Gemini Notebook」へほぼ切り替わっているが、日本語の第三者記事や旧来の社内資料では引き続き「NotebookLM」表記も多く残るため、本ページでも定着している呼び名として「NotebookLM」を併記する。社内資料や大量のPDF・議事録を読み込ませて「この資料群について聞く専用AI」を作れるイメージで、一般知識で適当に答えてしまう(いわゆるハルシネーション)リスクを大きく抑えられるのが最大の特徴。「大量の資料を読み込んで整理する時間がない」「AIに聞いても出典が不明で信用できない」という悩みを解決する。

## 仕組み・背景

NotebookLMは「ソースグラウンデッド(source-grounded)」という設計思想を採っている。ユーザーがPDF・Googleドキュメント/スプレッドシート・Word・PowerPoint・テキスト/Markdown・Webページのリンク・YouTube動画・音声ファイルなどをノートブックに「ソース」として追加すると、NotebookLMはその内容だけを検索・参照して回答を生成する。回答文には引用番号([1][2]など)が付き、クリックすると元のソースの該当箇所にジャンプできるため、「AIの言っていることが本当に資料に書いてあるか」をその場で検証できる。

2026年6月8日には、内部で動くAIモデルが**Gemini 3.5**に切り替わり、Googleのコーディングツール「Antigravity」由来の100種類超の「ソフトウェアスキル」が組み込まれた大型アップデートが実施された。これに合わせて、各ノートブックに**「セキュアなクラウドコンピュータ」**が割り当てられ、ノートブック内でコードを実際に記述・実行してデータ分析や複雑な処理を行えるようになった(Pro以上のプランを中心に順次から標準機能へ移行が進んでいる)。

もう一つの目玉が、**チャットから資料集めそのものを始められる**ようになったことである。従来の「Deep Research」機能(テーマ名からGoogle検索・外部Webの関連情報源を自動収集する機能)をさらに一歩進め、2026年6月のアップデート以降は「まだ資料が手元にない、漠然としたテーマや疑問」をチャットで伝えるだけで、AIが調査方針を立てながらソース候補を提案し、承認するとそのままノートブックのソースとして追加してくれる。「白紙のノートブックに何を入れればいいか分からない」という最初のハードルがさらに下がった形だが、これも「候補を提案し、ユーザーが承認してソースに追加する」仕組みである点は変わらず、勝手に外部知識だけで答えてしまうわけではない。この「ソースの範囲でしか答えない」という制約こそがNotebookLMの価値であり、Geminiアプリのような汎用AIとの根本的な違いになる。

画面構成は「ソース(左)・チャット(中央)・Studio(右)」の3カラムレイアウトで、同じ種類のStudio成果物(音声概要を複数パターンなど)を1つのノートブック内に並行して保存・比較できる。

主な出力機能は次の通り(2026年8月時点)。

- **チャットQ&A**: ソースの内容について質問し、引用付きで回答を得る。チャットを起点にソース候補の提案・追加まで行えるようになった点は前述の通り
- **音声概要(Audio Overview)**: アップロードした資料をもとに音声コンテンツを自動生成。二人のホストが掘り下げて対話する既定の「Deep Dive」に加え、一人語りで2分程度に要点をまとめる「Brief」、批評的にフィードバックする「Critique」、賛否両論を戦わせる「Debate」など複数フォーマットを選べる。対応言語は80以上に拡大している
- **動画概要(Video Overview)**: 資料の要点をナレーション付きスライド・図解形式でまとめる標準版に加え、2026年3月には「Cinematic Video Overview」が追加された。Gemini系モデルが構成・演出を決める「監督」役を担い、Veo・Nano Banana Pro系のモデルが本格的なアニメーション動画を生成する。2026年8月時点でも**Google AI Ultraプラン限定**の提供が続いており、他プランへの展開時期は明言されていない
- **マインドマップ**: 資料内の概念同士のつながりを図で可視化。各ノードをクリックすると、そのトピックに絞ったチャットをその場で開始できる
- **ノート・学習ガイド・要約レポート・スライド・インフォグラフィック・フラッシュカード・クイズ・データテーブルの自動生成**: いずれもStudioパネルからワンクリックで生成
- **オフィス形式へのエクスポート**: 2026年6月のアップデートで出力形式が大幅に拡充され、PDF・Word(DOCX)・Markdown・テキストに加え、Excel(XLSX)・PowerPoint(PPTX)、CSV・JSON、PNG/JPG/GIFなどの画像・図表も直接生成・エクスポートできるようになった。社内向け報告資料をそのままOffice形式で作りたい場合に有効
- **ノート内でのコード実行**: 前述の「セキュアなクラウドコンピュータ」により、資料データの複雑な分析のためにノートブック内でコードを直接記述・実行できる

## 使いどころ・使い分け

| | NotebookLM(Gemini Notebook) | ChatGPT・Geminiアプリなど汎用チャットAI |
|---|---|---|
| 回答の根拠 | ユーザーが渡した資料のみ(ソースグラウンデッド) | 学習済みの一般知識+Web検索など(既定では手元資料に限定されない) |
| ハルシネーションのリスク | 低い(出典を明示し、該当箇所にジャンプできる) | 相対的に高い(出典が曖昧なことが多い) |
| 得意なこと | 大量資料の横断要約、資料に基づく正確なQ&A、資料の音声・動画化 | 発想の壁打ち、資料にない知識との掛け合わせ、文章作成・翻訳など汎用タスク |
| 向かないこと | 資料に書いていないことへの回答(そもそも答えない設計) | 「この資料だけを根拠に」という厳密な使い方 |

判断の目安はシンプルで、**「手元の資料だけを根拠に正確に調べたい・要約したい」ならNotebookLM**、**「資料を踏まえつつ一般知識も交えて発想を広げたい」ならGeminiアプリやChatGPT**、という使い分けになる。両方を組み合わせ、NotebookLMで資料を整理・要約してから、その要約をGeminiアプリやChatGPTに渡して企画に発展させる、という流れも実務的に有効。2026年4月からGeminiアプリ側にも「ノートブック」機能が追加され、Google AI Ultra/Pro/Plusのウェブ版ユーザーを対象にNotebookLM(Gemini Notebook)側のノートブックと**双方向に同期**するようになった。Geminiアプリ側で作ったノートブックがNotebookLM側にもそのまま現れる(逆も同様)ため、両者の境目は実質的にかなり薄くなっている。

## 実務での使い方

### 想定シーン

- 大量の調査レポート・議事録・PDFをまとめて要約し、共通する論点を洗い出す
- 会議前に関連資料一式を読み込ませておき、「この案件の経緯を教えて」と聞いて短時間でキャッチアップする
- 契約書や社内規程など複数文書を横断して、条件の違いを質問する
- 通勤中や移動中に音声概要を再生し、資料の内容を「ながら聞き」でインプットする
- 手元に資料がまだない段階で、チャットで漠然としたテーマや疑問を投げかけ、AIに関連情報源を提案・収集させてノートブックの土台を作る
- 生成した要約レポート・データテーブルを社内共有用にPDFやExcel・PowerPoint形式でそのままエクスポートする

### 基本の操作手順(画面の場所)

1. ブラウザで notebooklm.google.com にアクセスし、Googleアカウントでログイン(2026年7月の「Gemini Notebook」への改称後もこのURLは有効で、既存の共有リンクも引き続き機能する)
2. 「新規作成」(または「+ Chat with your sources」)をクリックしてノートブックを作成
3. 「ソースを追加」から、PDFやWord・PowerPointなどのファイルをドラッグ&ドロップ、Googleドライブから選択、WebページのURLやYouTubeのURLを貼り付け、またはテキストを直接貼り付けてソースを登録する(1ノートブックあたりのソース数・1ソースあたりの容量には上限があるため、大きすぎる場合は分割するかトピックごとにノートブックを分ける)。まだ資料がない場合は、チャット欄に調べたいテーマや疑問を入力すると、AIが関連ソース候補を提案してくれる(承認するとそのままソースに追加される)
4. 中央のチャット欄に質問を入力すると、登録したソースだけを根拠に回答が返り、回答中の引用番号をクリックすると元のソースの該当箇所が開く
5. 右側の「Studio」パネルから「音声概要」を選ぶと、資料をもとにした音声を自動生成できる。フォーマット(Deep Dive/Brief/Critique/Debate)や長さ、AIホストに注目してほしいポイントをプロンプトで指定することも可能。「動画概要」では標準のナレーション付きスライドに加えて、Ultraプランでは映像生成モデルによる「Cinematic Video Overview」も選べる。同じパネルから「マインドマップ」「要約レポート」「スライド」「クイズ」なども生成でき、複数の成果物を並行して保存・比較できる
6. 生成したレポートやデータテーブルは、Studioパネルの出力メニューからPDF・Word(DOCX)・Excel(XLSX)・PowerPoint(PPTX)・CSV/JSONなど用途に応じた形式でエクスポートできる

### コピペで使える質問例

```
このノートブックに追加した資料をもとに、以下を教えてください。

1. 全体を300字で要約してください
2. 各資料で意見や数値が食い違っている点があれば列挙してください
3. 会議で確認すべき論点を3つ、根拠となる資料番号付きで挙げてください
```

### ツール横断の対応付け

| 概念 | ChatGPT | Gemini | NotebookLM(Gemini Notebook) |
|---|---|---|---|
| 資料を読み込ませて根拠にする | ファイル添付+都度指示(会話が長いと参照が薄れがち) | ファイル添付、または「ノートブック」機能(NotebookLMのノートブックと同期する統合が進行中) | ソース追加が標準機能。ソース以外を使わないことが前提 |
| 音声で要約を聞く | 標準機能としては弱い(読み上げは別途) | 標準機能としては弱い | 音声概要(4フォーマット・80言語以上)が主力機能 |
| テーマだけから資料を集める | 検索連携機能に依存 | 検索連携機能に依存 | チャットに投げるだけでAIがソース候補を提案・収集(2026年6月〜) |
| 資料をOffice形式で書き出す | Word/Excel等の生成に対応 | Word/Excel等の生成に対応 | PDF・DOCX・XLSX・PPTX・CSV/JSONなどをStudioから直接エクスポート(2026年6月〜) |

### 料金プラン(2026年8月時点の目安)

2026年5月のGoogle I/Oでの発表を機に、NotebookLM(Gemini Notebook)は個人向けサブスクリプション「Google AI」のStandard(無料)/Plus/Pro/Ultra(5x・20xの2段階)という枠組みに再編され、各プランのノートブック数・ソース数・チャット回数・音声/動画生成回数の上限がそのまま連動する形になった。**NotebookLM単体で契約できるプランは存在せず**、Google AIプラン、対象のGoogle Workspaceプラン、またはGoogle Cloud経由のNotebookLM Enterpriseライセンスのいずれかに含まれる形でのみ利用できる。

| プラン | 日本向け目安月額(税込) | 想定利用者 | ソース数・チャット回数の目安 |
|---|---|---|---|
| Standard(無料) | 0円 | 個人 | 1ノートブックあたりソース50件、1日あたりチャット50回・音声生成3件程度 |
| Google AI Plus | 725円 | 個人・ライトユーザー | ソース100件程度まで拡大 |
| Google AI Pro | 2,900円 | 個人・仕事利用のヘビーユーザー | ソース300件程度、チャット回数も大幅増、ノート内コード実行などが標準機能化 |
| Google AI Ultra 5x | 14,500円 | 高頻度利用の個人・チーム | ソース500〜600件程度、チャット1日数百〜2,500回程度 |
| Google AI Ultra 20x | 32,000円 | 大容量・最大級の利用が必要な個人 | Ultra 5xよりさらに上限が大きく、チャットは1日最大5,000回程度、Cinematic Video Overviewなど最新機能への先行アクセス |
| Google Workspace経由 | プランによる | 企業・チーム | Business/Enterprise系プランに含まれる形で解放。共有・管理機能が強化される |
| NotebookLM Enterprise | 個別見積り | 大企業・要セキュリティ対応組織 | Google Cloud経由でライセンス購入。VPC-SCなどのセキュリティ要件対応、監査ログ、モデル学習への非利用などガバナンス面が強化される |

具体的なソース数上限・1日の生成回数・料金は改定が非常に頻繁で、かつ本稿執筆時点でもGoogle公式ヘルプ・公式ブログへ直接アクセスできず(WebFetchが403を返す)、複数の第三者情報源(価格比較系メディア、2026年7月20日時点の確認情報を含む)の突き合わせによる推定値を含む。1ソースあたりの容量上限はプラン共通でおおむね50万語・200MB程度とされる。契約・運用前には必ず[Google公式のGemini Notebookヘルプ(FAQ)](https://support.google.com/gemininotebook/answer/16269187?hl=ja)、[Gemini Notebook Pro 料金ページ](https://notebooklm.google/plans?hl=ja)、[Google AIプラン比較ページ](https://one.google.com/about/google-ai-plans/)、法人利用の場合は[NotebookLM Enterprise(Google Cloud)](https://cloud.google.com/resources/notebooklm-enterprise)で最新の数値を確認すること。

## 注意点・よくある誤解

- **名称変更(NotebookLM→Gemini Notebook)による混乱**: 2026年7月16日にサービス名が「Gemini Notebook」へ変更された。既存の共有リンク・ブックマークはリダイレクトされ、機能面での破壊的な変更もないが、社内マニュアルや研修資料に残る「NotebookLM」という表記・スクリーンショットは今後の画面変更に合わせて定期的に見直す
- **最新機能はプラン・言語で提供範囲が異なる**: 2026年3月に追加されたCinematic Video Overviewは2026年8月時点でもGoogle AI Ultraプラン限定であるように、新機能は特定プラン・特定言語への先行提供から始まることが多い。「使えるはずの機能が見当たらない」場合は、自分のプランと言語設定を先に確認する
- **要約・言い換えは行われる**: 「資料の範囲だけで答える」といっても、回答は資料の丸写しではなく要約・言い換えを経ている。金額・日付・数量など間違えると業務に直結する情報は、引用リンクから元のソースの該当箇所を必ず開いて目視確認する
- **アップロードしていない情報は知らない(仕様であり不具合ではない)**: NotebookLMは意図的に一般知識を使わない設計のため、「なぜ常識的なことも答えてくれないのか」と戸惑う新規ユーザーが多い。これはハルシネーション対策としての仕様
- **ソース数・容量に上限がある**: 1ノートブックあたりのソース数はプランによって50〜600件程度、1ソースあたりの容量は共通でおおむね50万語・200MB程度が上限とされる。大量の資料を扱う場合は、トピックや案件単位でノートブックを分けるか、上位プランの利用を検討する
- **チャットからのソース自動収集の挙動を理解しておく**: 2026年6月のアップデート以降、チャットに投げた漠然としたテーマからAIがWeb・Google検索の関連情報を提案・追加できるようになったが、追加された時点でそれも「ソース」として扱われる。何を根拠に回答しているか不明瞭にならないよう、自動追加されたソースの中身も確認する習慣を持つ
- **ノート内コード実行(セキュアなクラウドコンピュータ)は取り扱いに注意**: 2026年6月に追加された機能で、ノートブック内でAIがコードを書いて実行できるようになった。数値集計やデータ整形が捗る一方、実行結果の妥当性は必ず人が確認し、機密データを扱う場合は自社のデータ利用条件と照らして可否を判断する
- **機密情報の扱い**: 個人向け無料版と法人向け(Google Workspace/Enterprise)ではデータの取り扱いポリシーが異なる場合がある。社外秘の資料を読み込ませる際は、自社の契約プランのデータ利用条件(モデル学習に使われないか等)を事前に確認する

## 最初の一歩

手元にある社内マニュアルやプロジェクト資料を1つNotebookLM(Gemini Notebook)に読み込ませ、「この資料の要点を300字で教えて」と質問し、引用番号をクリックして元の資料の該当箇所にジャンプする感覚を試してみる。あわせて、画面のロゴや名称が「Gemini Notebook」に変わっているかどうかも確認しておく。

## 関連トピック

- [Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)

## 更新履歴

### 2026-08-03: Gemini 3.5への切り替え、チャットからのソース自動収集、Office形式エクスポート、料金プランの具体的な数値を反映

- **内容**: 2026年6月8日のアップデートで内部モデルがGemini 3.5に切り替わったこと、Antigravity由来のソフトウェアスキルとノート内コード実行(セキュアなクラウドコンピュータ)がPro以上で標準機能化したことを仕組み・背景と注意点に追記。従来の「Deep Research」を発展させ、チャットに漠然としたテーマを投げるだけでAIがソース候補を提案・自動収集する機能を反映。PDF・DOCX・XLSX・PPTX・CSV/JSONなどへの直接エクスポート機能を追加。Cinematic Video Overviewが2026年8月時点でもGoogle AI Ultraプラン限定であることを明記。2026年4月からGeminiアプリの「ノートブック」機能とNotebookLM(Gemini Notebook)が双方向同期する統合が本格化したことを使い分けの節に反映。料金プランを日本向けの具体的な月額目安(Standard 0円/Plus 725円/Pro 2,900円/Ultra 5x 14,500円/Ultra 20x 32,000円)とソース数・チャット回数の目安に更新
- **出典**: [TechCrunch: NotebookLM's new update will help you build source repository from chat](https://techcrunch.com/2026/06/08/notebooklms-new-update-will-help-you-build-source-repository-from-chat/)、[9to5Google: NotebookLM rolling out big Gemini 3.5 & Antigravity upgrade with more outputs](https://9to5google.com/2026/06/08/notebooklm-gemini-3-5-antigravity/)、[9to5Google: NotebookLM is now Gemini Notebook, with 3.5 + Antigravity upgrade coming to AI Pro](https://9to5google.com/2026/07/16/notebooklm-gemini-notebook/)、[Google Workspace Updates: NotebookLM is now Gemini Notebook](https://workspaceupdates.googleblog.com/2026/07/notebooklm-now-gemini-notebook.html)、[heise online: NotebookLM now exports to Excel, PowerPoint, and PDF](https://www.heise.de/en/news/NotebookLM-now-exports-to-Excel-PowerPoint-and-PDF-11326059.html)、[Google Blog: Google introduces Notebooks in Gemini, a project management tool synced with NotebookLM](https://blog.google/innovation-and-ai/products/gemini-app/notebooks-gemini-notebooklm/)、[pasqualepillitteri.it: NotebookLM April 2026: Mobile for Everyone, Cinematic Video and Gemini Sync](https://pasqualepillitteri.it/en/news/1697/notebooklm-april-2026-mobile-cinematic-video-gemini-sync)、[SHIFT AI TIMES: Gemini Notebook(旧NotebookLM)の料金は?](https://shift-ai.co.jp/blog/50019/)、[elephas.app: NotebookLM Limits Explained (2026)](https://elephas.app/blog/notebooklm-source-limits)、[Admina by Money Forward: Gemini Notebook(旧NotebookLM)とは?](https://admina.moneyforward.com/jp/blog/gemini-notebook-enterprise-guide)
- **注記**: 本セッションでもGoogle公式ページ(support.google.com/gemininotebook、blog.google等)へのWebFetchは403で直接アクセスできず、検索結果のスニペットおよび複数の第三者記事(価格比較・解説メディア)の突き合わせに基づく記述を含む。料金・ソース数上限・チャット回数の具体的な数値は変更が頻繁なため目安とし、契約・運用前には必ず公式サイトで最新値を確認すること

### 2026-07-19: サービス名の「Gemini Notebook」への改称、料金プランの4段階再編、2026年の機能アップデートを反映
- **内容**: 2026年7月16日にNotebookLMが「Gemini Notebook」へ改称されたことをこれは何か・実務での使い方・注意点の各所に反映。2026年5月のGoogle I/Oを機に料金プランがGoogle AI Free/Plus/Pro/Ultraの4段階(+Workspace/Enterprise)に再編されたことを整理。音声概要の4フォーマット(Deep Dive/Brief/Critique/Debate)・80言語以上への対応拡大、Cinematic Video Overview(Gemini 3・Veo 3・Nano Banana Proによる映像生成、Ultra/英語先行)、Deep Researchによるテーマからの自動ソース収集、クリックでチャットに展開できるマインドマップ、3カラムのStudioパネル、ノート内コード実行などの新機能を追記
- **出典**: [Google Blog: NotebookLM is now Gemini Notebook](https://blog.google/innovation-and-ai/products/gemini-notebook/notebooklm-gemini-notebook/)、[TechCrunch: Google continues its renaming streak by turning NotebookLM to Gemini Notebook](https://techcrunch.com/2026/07/16/google-continues-its-renaming-streak-by-turning-notebooklm-to-gemini-notebook/)、[9to5Google: NotebookLM is now Gemini Notebook, with 3.5 + Antigravity upgrade coming to AI Pro](https://9to5google.com/2026/07/16/notebooklm-gemini-notebook/)、[Impress Watch: グーグルNotebookLM、「Gemini Notebook」に名称変更](https://www.watch.impress.co.jp/docs/news/2125930.html)、[PC Watch: 「NotebookLM」が「Gemini Notebook」に改名。コード実行も可能に](https://pc.watch.impress.co.jp/docs/news/2126004.html)、[Google Blog: Generate your own Cinematic Video Overviews in NotebookLM](https://blog.google/innovation-and-ai/products/notebooklm/generate-your-own-cinematic-video-overviews-in-notebooklm/)、[Android Police: NotebookLM now uses Gemini, Nano Banana, and Veo to animate your Video Overviews](https://www.androidpolice.com/notebooklm-now-has-cinematic-video-overviews/)、[Google Blog: NotebookLM's Video Overviews are now available in 80 languages](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebook-lm-audio-video-overviews-more-languages-longer-content/)、[9to5Google: NotebookLM rolling new Audio Overview formats: Brief, Critique & Debate](https://9to5google.com/2025/09/02/notebooklm-audio-overview-debate/)、[Google Workspace Updates: Take your notebooks further by adding NotebookLM as a source in the Gemini app](https://workspaceupdates.googleblog.com/2026/01/take-notebooks-further-notebooklm-gemini.html)、[felloai.com: NotebookLM Pricing 2026: Free vs Plus vs Pro vs Ultra](https://felloai.com/notebooklm-pricing/)、[elephas.app: NotebookLM Limits Explained (2026)](https://elephas.app/blog/notebooklm-source-limits)
- **注記**: 本セッションではWebFetchが全ドメインで403を返しGoogle公式ページ(support.google.com、blog.google等)に直接アクセスできなかったため、上記の一次情報タイトルは検索エンジンの検索結果一覧・スニペットから存在と概要を確認したものであり、ソース数上限・料金の具体的な数値は複数の第三者価格比較サイトの突き合わせによる推定値を含む。契約・運用前には必ず公式サイトで最新値を確認すること

### 2026-07-05: 初版執筆
- **内容**: NotebookLMのソースグラウンデッドという設計思想、チャットQ&A・音声概要・動画概要・マインドマップなどの機能、汎用チャットAIとの使い分け、ノートブック作成からソース追加・質問・音声概要生成までの操作手順、料金プランの構成(無料版/NotebookLM in Pro/Google Workspace/Enterprise)を整理
- **出典**: [Google NotebookLM ヘルプ「NotebookLMをアップグレードする」](https://support.google.com/notebooklm/answer/16213268)、[Google NotebookLM ヘルプ「ノートブックの新しいソースを追加または検索する」](https://support.google.com/notebooklm/answer/16215270?hl=ja)、[Google Cloud: NotebookLM for enterprise](https://cloud.google.com/resources/notebooklm-enterprise)、[TechCrunch: Google's NotebookLM rolls out Video Overviews](https://techcrunch.com/2025/07/29/googles-notebooklm-rolls-out-video-overviews/)、[Google Blog: What's new in NotebookLM: Video Overviews and an upgraded Studio](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-video-overviews-studio-upgrades/)、[XenoSpectrum: NotebookLM「提供元を見る」機能](https://xenospectrum.com/google-notebooklm-announces-new-discover-sources-feature-to-automatically-gather-information-sources-for-web-searches/)、[G-gen Tech Blog: NotebookLM in Pro（旧称NotebookLM Plus）を使ってみた](https://blog.g-gen.co.jp/entry/how-to-use-notebooklm-plus)、[アイスマイリー: NotebookLMとは？使い方や料金・活用事例5選](https://aismiley.co.jp/ai_news/what-is-notebooklm-5/)
- **注記**: 一部の一次情報ページ(support.google.com等)は本セッションから直接アクセスできず、検索エンジンのスニペットおよび複数の第三者記事の突き合わせに基づく記述を含む。ソース数上限・1日あたりの生成回数・料金の具体的な数値は変更が頻繁なため目安とし、契約・運用前には必ず公式サイトで最新値を確認すること
