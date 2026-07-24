---
title: Google Geminiの基本
part: 3
chapter: 第5章 主要ツール各論
tags: [Gemini, Google, Gem, NotebookLM, Gemini Notebook]
created: 2026-07-04
updated: 2026-07-19
---

# Google Geminiの基本

## これは何か

Google Geminiは、ChatGPTと並ぶ代表的な生成AIだが、モデルの世代(Flash/Pro等)や周辺機能(Gem、NotebookLM改め「Gemini Notebook」)の呼び方がGoogle独自で分かりにくい。しかも2026年に入ってからプラン体系・料金・製品名が立て続けに変わっており、ChatGPTを使い慣れた人はもちろん、以前Geminiを触ったことがある人でも「あれ、前と名前が違う」と戸惑いやすい。ここではGeminiのラインナップと周辺機能の関係を、2026年7月時点の最新状態で整理する。

## 仕組み・背景

2026年7月時点でのGeminiのモデルラインナップは「Gemini 3」世代が中心で、性能・速度のバランスで複数段階に分かれている。

- **Gemini 3 Flash-Lite**: 低遅延・高頻度処理向けの最軽量モデル
- **Gemini 3 Flash / Gemini 3.5 Flash**: 汎用のワークホースモデル。コストと品質のバランス型で、無料版の既定モデルにもなっている
- **Gemini 3.1 Pro**: 現行のフラッグシップモデル(2026年2月公開)。複雑なタスク・専門用途向けで、応答時に「思考レベル」をLOW/MEDIUM/HIGHの3段階から選べ、HIGHにすると簡易版の並列推論モード(通称「Deep Think Mini」)として振る舞う
- **Deep Think**: Google AI Ultra限定の最上位モード。Gemini 3.1 Proをベースにした本格的な並列推論で、国際数学オリンピック(IMO)金メダル相当のスコアを記録するなど、最も難しい調査・エンジニアリング用途向け

なお、次期モデル「Gemini 3.5 Pro」は2026年5月のGoogle I/Oで予告されたものの、品質面の作り直しにより一般提供が数回延期されており、2026年7月19日時点でもまだ正式リリースされていない(エンタープライズ向けにVertex AIで限定プレビューのみ)。「もう使える」とする記事も出回っているが、Google公式のアナウンスが出るまでは未確定情報として扱うのが安全。

画像生成は「Nano Banana」シリーズという名称で展開されている。2026年2月26日にGeminiアプリの既定画像生成モデルが「Nano Banana 2」(高速・低コスト重視)に切り替わり、より高精度な文字入れ・複雑な構図・実データに基づいた描写が必要な場合は上位モデルの「Nano Banana Pro」(Gemini 3 Pro Image、2026年6月一般提供)を使う、という2段構成になっている。

モデル・製品名の世代交代は非常に速く、2026年7月には音声・文書系ツールの「NotebookLM」が「Gemini Notebook」に改称される(後述)など、名前自体が変わることもある。記事や社内資料に具体的なモデル名・製品名を書く場合は、必ず[Google公式のGeminiリリースノート](https://gemini.google/release-notes/)で最新の呼称を確認することを推奨する。

## 使いどころ・使い分け

| 用途 | 向いているモデル・機能 |
|---|---|
| 簡単な質問・チャット | Gemini 3 Flash系(無料版の既定モデル) |
| 複雑な分析・専門的なタスク | Gemini 3.1 Pro |
| 最難関の調査・研究・エンジニアリング | Deep Think(Ultra限定) |
| 大量・高頻度の軽い処理 | Flash-Lite |
| 高速・低コストの画像生成 | Nano Banana 2 |
| 高精度な文字入れ・複雑な構図の画像生成 | Nano Banana Pro |
| 手元の資料だけを根拠に正確に調べたい | Gemini Notebook(旧NotebookLM) |
| 幅広い一般知識も使って発想を広げたい | Geminiアプリ本体 |

GeminiアプリとGemini Notebook(旧NotebookLM)の使い分けが特によく混同される。**Geminiアプリは「外の世界の知識」も使う汎用AI**であるのに対し、**Gemini Notebookは「ユーザーが渡した資料だけ」を根拠に回答するリサーチ特化ツール**という違いがある。手元の資料から正確に情報を引き出したいならGemini Notebook、既存資料を踏まえつつ新しいアイデアを広げたいならGeminiアプリ、という選び方になる。なお2026年4月以降はGeminiアプリのサイドバーに「Notebooks」セクションが新設され、Geminiアプリを離れずにノートブックの作成・参照ができるようになっているため、両者はほぼシームレスに行き来できる。

## 実務での使い方

### 個人向けプラン(2026年7月時点の目安)

2026年5月のGoogle I/Oでプラン体系そのものが再編され、その後も価格改定が続いている。以下は執筆時点の目安。

| プラン | 月額目安(日本) | 特徴 |
|---|---|---|
| 無料 | ¥0 | Gemini 3 Flash系が既定モデル。Gemsも無料版で作成・利用可(回数制限あり)。Deep Researchは月5回程度まで、画像生成は1日あたり上限あり |
| Google AI Plus | ¥725(2026年6月に値下げ、ストレージも200GB→400GBに倍増) | 無料版の2倍程度の利用枠、コンテキスト窓12.8万トークン、Omni Flashによる動画生成、Gemini Notebookの利用枠拡大など |
| Google AI Pro | ¥2,900(ストレージは2026年4月に2TB→5TBへ増量、価格据え置き) | Gemini 3.1 Pro、Nano Banana Pro、Veo 3.1 Fast、Deep Research(1日20回目安)、Gemini Notebookの利用枠拡大、コーディングエージェント「Jules」、エージェント型IDE「Antigravity」などフロンティア機能一式 |
| Google AI Ultra(5x) | ¥14,500 | ストレージ20TB。Proの5倍の利用量上限、Deep Research 1日120回目安 |
| Google AI Ultra(20x) | ¥32,000 | ストレージ30TB。Proの20倍の利用量上限、Deep Think、Veo 3.1のフル機能、Project Mariner(エージェント型ブラウザ操作)、YouTube Premium同梱など最上位機能 |

Ultraは以前は単一プランだったが、I/O 2026でエントリー帯(5x)と最上位帯(20x)の2階層に再編され、最上位帯はむしろ値下げされた。料金は今後も変更される可能性が高いため、契約前に必ず[Google公式のプランページ](https://one.google.com/about/google-ai-plans/)で最新の金額を確認すること。

### Gem機能(ChatGPTのGPTsに相当)

Gemは「どんなトピックにも対応できる自分専用のカスタムAI」で、毎回の会話で前提説明を繰り返す手間を省ける。2026年時点では無料版でも基本的なGem作成・利用ができるが、利用回数や使えるモデルの性能は有料プランほど広くなる。

作成手順の目安:
1. gemini.google.com を開き、左側メニューの「Gemを表示」をクリック
2. 「Gemを作成」を選択し、名前を付ける
3. 指示欄に、ペルソナ(役割・口調)・タスク(してほしいこと)・コンテキスト(背景情報)・出力形式を書く(「Geminiを使用」ボタンで簡単な目的文を詳しい指示文に自動リライトさせることも可能)
4. 右側のプレビューで確認しながら「保存」

作成したGemはGeminiモバイルアプリやGoogle Workspaceのサイドパネルからも呼び出せる。

### Gemini Notebook(旧NotebookLM)

2026年7月16日、Googleは長らく「NotebookLM」の名称で提供してきたリサーチツールを「Gemini Notebook」に改称した。スタンドアロンのツールとして存続しつつ、Geminiアプリ・Google検索(AIモード)との連携が強化されている。同時に、各ノートブックに専用の「セキュアなクラウドコンピュータ」が付与され、アップロードした資料をもとにコードを書いて実行し、複雑なデータ分析まで行えるようになった。手元の資料を読み込ませて質問すると、根拠となる該当箇所を示しながら回答してくれる点は従来どおり。

### 法人向け(Google Workspace with Gemini)

個人向けプランとは別に、法人向けは「Google Workspace with Gemini」という名称で提供されている。GmailやGoogleドキュメント、スプレッドシート、Meetなど業務ツール群にGeminiが統合されており、Business Starterプラン(月額目安800〜950円/ユーザー)からも標準で利用できる(上位プランほど利用できる範囲が広がる)。Microsoft 365のCopilotのように追加課金が必要な構成ではなく、対象プランであれば追加費用なしでGemini機能が使える点が特徴。

## 注意点・よくある誤解

- **モデル名・製品名・料金の変更頻度が非常に高い**: 2026年だけでもGoogle I/Oでのプラン再編、AI Plusの値下げ、Proのストレージ増量、そしてNotebookLMから「Gemini Notebook」への改称と、立て続けに変化している。本ページの数値・名称は目安であり、契約前・執筆前に必ず公式サイトで確認すること。
- **「NotebookLM」の名前はもう存在しない**: 2026年7月16日以降、公式には「Gemini Notebook」に統一されている。過去の資料や検索結果には旧名の「NotebookLM」が数多く残っているため、社内資料を書く際はどちらの名前でも通じるよう両方併記しておくと親切。
- **Gemini 3.5 Proは「もう使える」という情報を鵜呑みにしない**: 2026年5月のI/Oで予告されて以降、複数回リリースが延期されており、7月19日時点でも一般提供はされていない。ブログ記事の中には未確定の噂を確定情報のように書いているものもあるため注意。
- **無料版でGemが使えるかどうかは要確認**: 無料版でも基本的なGem作成・利用は可能になったが、利用回数や使えるモデルの性能には上限がある。実際の挙動は公式ヘルプで確認するのが確実。

## 最初の一歩

手元にある社内マニュアルやプロジェクト資料を1つGemini Notebook(旧NotebookLM)に読み込ませ、内容についての質問を投げて、根拠付きで答えが返ってくる感覚を試してみる。

## 関連トピック

- [ChatGPTのプラン比較](../part03-ai-chat-tools/chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-19: プラン体系・モデル名・NotebookLM改称を最新化
- **内容**: 2026年5月のGoogle I/OによるGoogle AI Plus/Pro/Ultraのプラン再編と価格(Ultraの5x/20x2階層化、Plusの値下げ、Proのストレージ増量)、モデルラインナップをGemini 3.1 Pro/Deep Think/Gemini 3.5 Pro(未リリース)中心に更新、画像生成をNano Banana 2/Nano Banana Proの2段構成に修正、2026年7月16日のNotebookLM→「Gemini Notebook」への改称を反映
- **出典**: [9to5google: NotebookLM is now Gemini Notebook](https://9to5google.com/2026/07/16/notebooklm-gemini-notebook/)、[窓の杜: 「NotebookLM」が「Gemini Notebook」へ改称](https://forest.watch.impress.co.jp/docs/news/2125948.html)、[9to5google: Google AI Plus price drop](https://9to5google.com/2026/06/08/google-ai-plus-price-drop/)、[PC Watch: Google AI Ultraに月額1万4,500円の新プラン](https://pc.watch.impress.co.jp/docs/news/2110129.html)、[Google DeepMind: Gemini 3.1 Pro](https://deepmind.google/models/gemini/pro/)、[Google Blog: Nano Banana Pro (Gemini 3 Pro Image)](https://blog.google/technology/ai/nano-banana-pro/)、[romptn Magazine: Gemini Deep Researchの回数制限](https://romptn.com/article/97411)
- **注記**: Google公式サイト(gemini.google.com、one.google.com)への直接アクセスができず複数の第三者情報の突き合わせに基づく目安。特に料金・ストレージ容量・回数上限は変動が速いため、正確な最新値は公式サイトで要確認

### 2026-07-04: 初版執筆
- **内容**: Geminiのモデルラインナップ(Flash-Lite/Flash/Pro)、個人向け・法人向けプランの概要、Gem機能の作成手順、NotebookLMとの使い分けを整理
- **出典**: [Google Blog: Gemini Omni Flash / Nano Banana 2発表](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)、[Google公式ヘルプ: カスタムGem作成のヒント](https://support.google.com/gemini/answer/15235603?hl=ja)、[マネーフォワード クラウド: Google Workspace with Gemini解説](https://biz.moneyforward.com/ai/basic/863/)、[アイスマイリー: GeminiとNotebookLMの違い](https://aismiley.co.jp/ai_news/gemini-notebooklm/)
- **注記**: Google公式サイトへの直接アクセスができなかったため、料金・モデル名の一部は複数の第三者情報の突き合わせに基づく目安。正確な最新値は公式サイトで要確認
