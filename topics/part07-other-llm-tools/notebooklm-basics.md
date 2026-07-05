---
title: NotebookLMの使い方
part: 7
chapter: 第1章 Google Gemini
tags: [NotebookLM, Google, RAG, 資料要約]
created: 2026-07-05
updated: 2026-07-05
---

# NotebookLMの使い方

## これは何か

NotebookLMは、Googleが提供する「アップロードした資料だけを情報源にするAI」ノートアプリ。議事録・マニュアル・レポートなど手元の資料を読み込ませると、その中身**だけ**を根拠に要約・Q&A・音声解説などを生成してくれる。ChatGPTのような汎用チャットAIは学習済みの一般知識やWeb検索も使って何でも答えようとするため、社内資料の内容が一般論と混ざって不正確になったり、根拠が分からなくなったりしがちである。NotebookLMは回答の一文ごとに元資料への引用リンクを付けるため、「社内資料の中身を正確に把握・要約したい」という場面に向いている。

## 仕組み・背景

- **動作原理**: アップロードした資料をNotebookLMが読み込み、質問が来るとその資料の中から関連箇所を検索し、その範囲内でGeminiモデルに回答文を作らせる(RAG = Retrieval-Augmented Generation、検索で見つけた情報を根拠に回答を組み立てる仕組み)。回答文の脚注番号をクリックすると元資料の該当箇所にジャンプする「グラウンディング(根拠提示)」が最大の特徴。
- **対応できる情報源**: PDF、Googleドキュメント/スライド、Word、テキストの貼り付け、Webページのリンク、YouTube動画、音声ファイル、画像(OCRで文字認識)、CSVなど。1つの情報源につき最大50万語または200MBまで。
- **Studioパネルの出力形式**: 音声解説(Audio Overview)、動画解説(Video Overview。Ultraプランでは動画生成モデルVeo 3を使ったより高精細な「Cinematic Video Overview」も選べる)、マインドマップ、レポート/ブリーフィングドキュメント、FAQ、スライド、インフォグラフィック、データテーブル、クイズ、フラッシュカードなど、資料を多様な形式に自動変換できる。
- **Discover Sources機能**: 2025年後半に追加された機能で、調べたいトピックを説明するとWeb上から関連しそうな情報源候補をAIが探して提案してくれる。ただしこれは「情報源を探す手間を省く」機能であり、見つかった候補をノートブックに追加して初めて回答の根拠として使われる。何もしなくても勝手にWeb全体を検索して回答するわけではなく、「渡した資料の中だけで答える」という基本原則は変わらない。

## 使いどころ・使い分け

| 観点 | ChatGPT・Geminiアプリ(汎用チャットAI) | NotebookLM |
|---|---|---|
| 回答の根拠 | 学習済みの一般知識(+Web検索機能) | アップロードした資料のみ(引用元付き) |
| 得意な用途 | アイデア出し・文章作成・雑多な質問・コーディング | 社内資料の要約・Q&A・複数資料の横断調査 |
| 出典の明示 | 機能や設定次第で曖昧になりやすい | 回答の一文ごとに出典箇所へのリンクが付く |
| ハルシネーション(もっともらしい誤答) | 一般知識と混ざるため起こりやすい | 資料の範囲に限定されるため相対的に少ない(ゼロではない) |
| 音声/動画コンテンツ化 | 標準では非対応(別ツールが必要) | Audio/Video Overviewとして標準搭載 |

使い分けの目安:
- 「この資料に書いてあることを正確に知りたい・要約したい」→ NotebookLM
- 「資料を踏まえつつ、一般知識も交えて新しいアイデアを広げたい」→ ChatGPT・Geminiアプリ
- 「資料の内容を人に聞かせる形(音声・動画)に加工して共有したい」→ NotebookLMのStudio機能

## 実務での使い方

### 基本操作の手順

1. notebooklm.google.com にアクセスし、Googleアカウントでログイン
2. 「新しいノートブックを作成」をクリック
3. 「ソースを追加」ボタンから、PDF・Googleドライブ・テキストの貼り付け・URL・YouTube動画などを選んでアップロード(1ノートブックに追加できる情報源数はプランにより上限あり。下記参照)
4. アップロードが完了すると自動で概要が生成される
5. 画面下部のチャット欄に質問を入力すると、資料の中身だけを根拠に回答が返ってくる。回答文中の脚注番号をクリックすると元資料の該当箇所がハイライト表示される
6. 右側の「Studio」パネルにある Audio Overview・Video Overview・マインドマップ・クイズなどのボタンを押すと、その情報源をもとにしたコンテンツが自動生成される

### コピペで使える実例

議事録からアクションアイテムを抽出するプロンプト例:

```
アップロードしたすべての議事録から、未完了のアクションアイテムを
「担当者・期限・内容」の一覧表にまとめてください。
期限が明記されていないものは「期限未設定」としてください。
```

Audio Overviewをカスタマイズする指示例:

```
この資料をもとに、生成AIに詳しくない新入社員向けに、
専門用語が出てきたらそのつど一言説明を入れながら、
対話形式で10分程度の日本語Podcastを作ってください。
```

### 料金プラン(2026年7月時点の目安)

2026年5月のGoogle I/Oで、NotebookLM単体のプランはGoogle AIサブスクリプション(Google AI Plus / Pro / Ultra)に統合された。

| プラン | 月額目安 | ノートブックあたりの情報源数上限 | Audio Overview 1日の生成上限 | 備考 |
|---|---|---|---|---|
| 無料 | ¥0 | 50個 | 3回 | Audio/Video Overviewも利用可 |
| Google AI Plus | 7.99ドル程度 | 100個 | 無料より拡大 | |
| Google AI Pro | 19.99ドル程度 | 300個 | 無料より拡大 | |
| Google AI Ultra | 99.99〜200ドル程度(ストレージ量で2段階) | 500〜600個 | 最大200回/日 | Veo 3を使う高精細な「Cinematic Video Overview」はUltra限定 |

1情報源あたりの上限(最大50万語または200MB)はどのプランでも共通。料金・上限は2026年に入ってから改定されたばかりで、今後も変わる可能性が高い。契約前に必ず[Google公式のNotebookLMプランページ](https://notebooklm.google/plans)で最新の金額を確認すること。

### 法人・教育機関向け

個人向けプランとは別に、Google WorkspaceアカウントでもNotebookLMを利用でき、契約プランに応じて情報源数などの上限が拡大される。さらに大規模組織向けには、Google Cloud上でセキュリティ・コンプライアンス要件を満たす「NotebookLM Enterprise」という別製品も用意されている(個人向けPro/Ultraとは別ライン)。

### ツール横断の対応付け

「手元の資料だけを根拠に回答させる」という発想は、他ツールにも近い機能がある。

| 概念 | NotebookLM | ChatGPT | Geminiアプリ |
|---|---|---|---|
| 資料限定のQ&A | ノートブックにソースを追加するだけで自動的に資料限定になる | カスタムGPTsの「Knowledge」にファイル添付+Web検索オフに設定 | ファイルをアップロードし「この資料の内容だけで答えて」と明示的に指示 |
| 音声解説の自動生成 | Audio Overview(標準機能) | 標準機能なし(外部ツール併用が必要) | 標準機能なし(NotebookLMとの連携で代替) |

## 注意点・よくある誤解

- **アップロードした資料の学習利用**: 個人のGoogleアカウントでは、フィードバックを送らない限りアップロードした資料や会話はモデルの学習に使われない。Google Workspaceアカウントで利用した場合は、人によるレビューにもモデルの学習にも使われない、とGoogleは説明している。社外秘の資料を扱う場合は、自分がどちらのアカウント種別で使っているかを必ず確認すること。
- **「資料の中だけで答える」は完璧ではない**: グラウンディングによりハルシネーションは大きく減るが、ゼロにはならない。資料の記述があいまいな箇所や、複数資料で内容が矛盾する箇所では誤った要約が出ることがあるため、重要な意思決定に使う場合は脚注から元資料を必ず確認する。
- **Discover Sourcesは「勝手にWeb全体を根拠にする」機能ではない**: あくまで情報源の候補をAIが探して提案するだけで、ノートブックに追加しない限り回答には使われない。この違いを理解していないと「NotebookLMなのに古い・誤った一般知識が混ざった」と誤解しやすい。
- **情報源数・生成回数の上限に達しやすい**: 無料プランは1ノートブックあたり情報源50個、Audio Overviewは1日3回までなど上限が低め。大量の資料を横断分析したい、日常的にAudio Overviewを使いたいという場合は有料プランへの移行を検討する。

## 最初の一歩

手元にある議事録や社内マニュアルを1つNotebookLMにアップロードし、「このドキュメントの要点を3行で」と質問して、回答の脚注から元資料にジャンプする感覚を確認してみる。

## 関連トピック

- [Google Geminiの基本](../part07-other-llm-tools/google-gemini-basics.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: NotebookLMの基本的な仕組み(RAGによる資料限定の回答・引用元表示)、ChatGPT/Geminiアプリとの使い分け、情報源追加の手順、Audio/Video Overview等のStudio機能、2026年5月のGoogle I/O後のプラン体系(Free/Plus/Pro/Ultra)と情報源数上限、データの学習利用に関する注意点を整理
- **出典**: [Google公式ヘルプ: NotebookLM でマインドマップを使用する](https://support.google.com/notebooklm/answer/16212283?hl=ja)、[Google Blog: What's new in NotebookLM: Video Overviews and an upgraded Studio](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-video-overviews-studio-upgrades/)、[Google Blog: NotebookLM Discover Sources](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-discover-sources/)、[Google公式ヘルプ: 仕事用または学校用のGoogleアカウントでNotebookLMを使用する](https://support.google.com/notebooklm/answer/16337734?hl=ja)、[Google Cloud: NotebookLM for enterprise](https://cloud.google.com/resources/notebooklm-enterprise)、[マネーフォワード クラウド: NotebookLMの使い方とは](https://biz.moneyforward.com/ai/basic/927/)、[マネーフォワード クラウド: NotebookLMのセキュリティは?](https://biz.moneyforward.com/ai/basic/5905/)、[TSクラウド: 【企業向け】NotebookLMに学習させない対策](https://googleworkspace.tscloud.co.jp/gemini/notebooklm-opt-out)、[elephas.app: NotebookLM Limits Explained (2026)](https://elephas.app/blog/notebooklm-source-limits)、[elephas.app: Is NotebookLM Free? Free vs Plus vs Pro Pricing (2026)](https://elephas.app/blog/notebooklm-free-vs-plus)
- **注記**: Google公式のプラン価格ページへの直接アクセスができなかったため、料金・情報源数の上限値は複数の第三者情報の突き合わせに基づく目安。正確な最新値は公式サイトで要確認
