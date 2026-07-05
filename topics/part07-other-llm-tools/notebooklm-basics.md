---
title: NotebookLMの基本と使い方
part: 7
chapter: 第1章 Google Gemini
tags: [NotebookLM, Google, RAG, リサーチ]
created: 2026-07-05
updated: 2026-07-05
---

# NotebookLMの基本と使い方

## これは何か

NotebookLMは、Googleが提供する「渡した資料だけを根拠に回答する」AIリサーチアシスタントである。ChatGPTやGeminiアプリのような通常のチャットAIは、学習済みの一般知識やウェブ検索も動員して答えるため、社内の非公開資料に基づく調べ物では的外れな回答(ハルシネーション、事実に基づかない出力)が混ざりやすい。NotebookLMはユーザーがアップロードした資料(ソース)の範囲内でしか回答しないよう設計されており、回答の各文には根拠となったソースの引用が付く。「社内マニュアルや複数の長文PDFを、間違いなく要約・検索したい」という場面に特化したツールである。

## 仕組み・背景

NotebookLMは裏側でGoogleのGeminiモデルを使っているが、回答の作り方が通常のチャットAIと異なる。アップロードしたソースをその場で解析・分割し、ノートブック(資料をまとめる作業スペースの単位)内だけを検索対象にしたうえで回答を生成する。この「ソースを検索して見つけた箇所を根拠に回答を組み立てる」方式はRAG(Retrieval-Augmented Generation、検索拡張生成)と呼ばれる仕組みの一種で、NotebookLMはこれを前面に押し出した製品と言える。

回答文中には引用番号が付き、クリックするとソースの該当箇所(PDFの該当ページなど)にジャンプできるため、「AIが本当にその資料を読んで言っているのか」を人間が検証しやすい。これが「ソースグラウンデッド(source-grounded、根拠資料に基づく)」と呼ばれるNotebookLMの中核的な特徴であり、一般的なチャットAIとの最大の違いになっている。

## 使いどころ・使い分け

| 場面 | 向いているツール | 理由 |
|---|---|---|
| 社内マニュアル・契約書・議事録など複数の長文資料を根拠に調べ物・要約したい | NotebookLM | ソース範囲内でしか答えないためハルシネーションが起きにくく、出典箇所を確認できる |
| 資料がない状態でアイデア出し・ブレスト・雑談したい | ChatGPT / Geminiアプリ | 学習済みの一般知識を幅広く使って発想を広げられる |
| 最新のウェブ情報も踏まえて調べたい | ChatGPT / Geminiアプリ(検索機能付き) | NotebookLMは基本的にアップロードしたソースの外には出ない |
| 資料を音声・動画・マインドマップなど別形式に変換して共有したい | NotebookLM | Audio Overview・Video Overview・マインドマップなどの変換機能が充実 |
| コードを書く・一般的な文章を生成する | ChatGPT / Geminiアプリ / Claude | NotebookLMは執筆・コーディング用途には向いていない |

判断基準はシンプルで、「答えの正確さより発想の広さが欲しいか」「渡した資料の中だけで正確に答えてほしいか」で選ぶ。前者ならChatGPTやGeminiアプリ、後者ならNotebookLMになる。なお2026年にはGeminiアプリ内にもNotebookLMと同期する「ノートブック」機能が追加され、境界が徐々に近づいているが、本稿執筆時点ではNotebookLM単体の方が資料管理・変換機能(後述のStudio機能)が充実している。

## 実務での使い方

### 対応ファイル形式・上限(2026年7月時点)

| 項目 | 内容 |
|---|---|
| 対応ファイル形式 | PDF、Google ドキュメント/スプレッドシート/スライド(最大100枚)、Word(docx)、テキスト(txt)、Markdown(md)、CSV、PowerPoint(pptx)、ePub、画像、コピー&ペーストしたテキスト、ウェブURL、字幕付きの公開YouTube動画URL、音声ファイル(mp3・wav・m4aなど) |
| ソースあたりの上限 | 最大50万語 または 200MB |
| ノートブックあたりのソース数 | 無料版は最大50件 |
| Googleスプレッドシート | 10万トークンまでの制限あり |

### 料金プラン(個人向け、2026年7月時点の目安)

| プラン | 月額目安 | ソース数/ノートブック | 1日の質問数 | Audio Overview |
|---|---|---|---|---|
| Free(無料) | ¥0 | 50 | 50問 | 1日3本まで |
| Plus(Google AI Plusに付属) | 約$7.99〜 | 無料版のおおむね2倍 | 増加 | 増加 |
| Pro(Google AI Proに付属) | 約$19.99〜 | さらに拡大 | さらに拡大 | さらに拡大 |
| Ultra(Google AI Ultraに付属) | 約$99.99〜/$200〜 | 500〜600 | 2,500〜5,000問 | 1日最大200本 |

法人向けはGoogle Workspaceの契約に含まれる形で提供され、Business Standard以上のプランでNotebookLM Plus相当の機能が使えるようになる。より厳格なセキュリティ・コンプライアンス要件がある組織向けには「NotebookLM Enterprise」がGoogle Cloud経由で提供され、データが自社のGoogle Cloudプロジェクト内に留まる点が特徴。料金体系・上限は変更が頻繁なため、契約前に[Google Workspaceの料金ページ](https://workspace.google.co.jp/pricing?hl=ja)や[NotebookLM Enterprise公式ページ](https://cloud.google.com/resources/notebooklm-enterprise)で最新値を確認すること。

### 基本操作手順

1. [notebooklm.google.com](https://notebooklm.google.com/) にアクセスし、Googleアカウントでログイン
2. 「新規作成」をクリックしてノートブックを作成
3. 「ソースを追加」から、PDFやWordファイルのアップロード、Google Driveからの読み込み、URLの貼り付け、テキストの直接貼り付けのいずれかでソースを登録(1ノートブックに複数ソースをまとめて追加できる)
4. 画面中央のチャット欄に質問を入力すると、登録したソースだけを根拠に回答が返る。回答文中の引用番号をクリックすると元資料の該当箇所が右側にハイライト表示される
5. 画面右側の「Studio」パネルから、Audio Overview(音声解説)・Video Overview(動画解説)・マインドマップ・スライド・インフォグラフィック・データ表・クイズ・フラッシュカードなどをワンクリックで生成できる
6. 作成したノートブックやAudio Overviewは、「共有」ボタンから「リンクを知っている全員が閲覧可能」な形で外部公開できる(閲覧者はチャットで質問できるが、ソースの追加・編集はできない)

### コピペで使えるQ&Aプロンプト例

```
このノートブックに登録した資料だけを根拠に、以下を回答してください。
資料に記載がない場合は「資料に記載がありません」と明示してください。

1. [製品名]の料金プランは何種類あり、それぞれの違いは何か
2. 契約解除に関する条件・注意事項をすべて箇条書きで列挙してほしい
3. 複数の資料間で内容に矛盾・食い違いがあれば指摘してほしい
```

質問を「箇条書きで」「表形式で」など出力形式まで指定すると、複数ソースを横断した要約の精度が上がりやすい。

### ツール横断の対応付け

| 概念 | NotebookLM | ChatGPT / Geminiアプリ |
|---|---|---|
| 資料に基づくAI | ノートブック単位のソース | カスタムGPTsのファイル添付 / Geminiの「ノートブック」機能 |
| 音声化 | Audio Overview | (標準機能としては非搭載) |
| 動画化 | Video Overview | (標準機能としては非搭載) |
| 図解化 | マインドマップ生成 | プロンプトで手動指示が必要 |

## 注意点・よくある誤解

- **一般知識では答えない**: NotebookLMは登録したソースの範囲内でしか回答しない設計のため、雑談や一般的な知識を尋ねても「資料に記載がありません」といった回答になることが多い。ChatGPTのように何でも答えてくれるAIだと期待すると使い勝手を誤解しやすい。
- **日本語対応は機能ごとに時期が異なる**: Audio Overview(音声解説)は2025年4月に日本語を含む50以上の言語に対応し、その後日本語を含む80以上の言語に拡大した。Video Overview(動画解説)も2025年8月に日本語を含む80言語に対応済み。一方、2026年に追加された縦型ショート動画「Short Video Overviews」は本稿執筆時点では英語のみの対応で、日本語の長尺音声も英語版(30分以上)に比べてまだ短い(10分弱)などの制約が残る。使う前に最新の対応言語・尺を公式ヘルプで確認するのが安全。
- **無料版には複数の上限がある**: ノートブックあたりソース50件、1日の質問数50問、Audio Overview1日3本など、無料版には細かい上限が設定されている。業務で日常的に使うならPlus以上への移行を検討する。
- **共有時は公開範囲に注意**: ノートブックやAudio Overviewは「リンクを知っている全員」に公開できる手軽さの裏返しで、社外秘資料を含むノートブックを誤って公開範囲にしてしまうリスクがある。共有前に必ず公開設定を確認すること。
- **機密情報を扱う場合は契約形態を確認**: 個人向けの無料・Plus・Pro・Ultraと、法人向けのWorkspace経由・NotebookLM Enterprise(Google Cloud経由)ではデータの扱いやセキュリティ要件が異なる。機密性の高い資料を扱う場合は、契約中のプランがどのデータ取り扱い方針に該当するかを確認してから利用する。

## 最初の一歩

手元にある社内マニュアルや報告書のPDFを1つNotebookLMに読み込ませ、「この資料の要点を3つに要約して」と質問し、引用リンクから元の記載箇所に飛べることを確認してみる。

## 関連トピック

- [Google Geminiの基本](../part07-other-llm-tools/google-gemini-basics.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: NotebookLMの基本概念(ソースグラウンデッドなRAGベースのリサーチアシスタント)、通常のチャットAIとの使い分け、対応ファイル形式・上限、料金プラン(Free/Plus/Pro/Ultra/Enterprise)、基本操作手順、Q&Aプロンプト例、Audio/Video Overviewの日本語対応状況、共有機能の注意点を整理
- **出典**: [DigitalOcean: What Is NotebookLM? Features and How to Use It in 2026](https://www.digitalocean.com/resources/articles/what-is-notebooklm)、[felloai: NotebookLM Pricing 2026](https://felloai.com/notebooklm-pricing/)、[NotebookLM ヘルプ: ノートブックの新しいソースを追加または検索する](https://support.google.com/notebooklm/answer/16215270?hl=ja)、[Google Blog(日本版): NotebookLMのビデオ解説が日本語を含む80言語に対応](https://blog.google/intl/ja-jp/company-news/technology/notebooklm-80/)、[Google Blog(日本版): NotebookLMの音声概要が日本語を含む50以上の言語で利用可能に](https://blog.google/intl/ja-jp/company-news/technology/notebooklm-50/)、[gihyo.jp: Short Video Overviews追加、英語でWeb版全ユーザーに展開](https://gihyo.jp/article/2026/07/notebooklm-short-video-overview)、[ITmedia: NotebookLMに一般公開機能、リンクを知っていれば誰でも見られる形で共有可能に](https://www.itmedia.co.jp/aiplus/articles/2506/03/news091.html)、[Google Cloud: NotebookLM for enterprise](https://cloud.google.com/resources/notebooklm-enterprise)
