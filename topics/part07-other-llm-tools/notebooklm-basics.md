---
title: NotebookLMの基本と使い方
part: 7
chapter: 第1章 Google Gemini
tags: [NotebookLM, Google, RAG, 音声概要]
created: 2026-07-05
updated: 2026-07-05
---

# NotebookLMの基本と使い方

## これは何か

議事録・契約書・リサーチレポート・YouTube動画など、大量の資料を読み込ませて要約させたりQ&Aさせたりしたいが、ChatGPTに1つずつコピペ・アップロードするのは非効率だし、AIが「それらしいがどこにも書いていないこと」を混ぜて答えてしまう不安もある。NotebookLMはGoogleが提供する「資料特化型」のAIノートアプリで、アップロードした資料(ソース)の中身だけを根拠に回答し、根拠箇所への引用リンクも示してくれる。さらに資料を2人の会話形式の音声(Audio Overview、音声概要)や解説動画(Video Overview)に自動変換できる点が最大の特徴で、移動中の耳学問や社内展開用のダイジェスト作成に使われている。

## 仕組み・背景

NotebookLMの回答は、RAG(Retrieval Augmented Generation、検索拡張生成。AIが回答時に外部文書を検索し、その内容を根拠に答えを組み立てる仕組み)に近い設計になっている。ユーザーがアップロードした資料(ソース)だけを検索対象とし、その中から関連箇所を取り出して回答を生成する。そのため一般的なチャットAIのように学習済みの知識だけで答えることはなく、回答の各文には脚注のような引用マークが付き、クリックすると元のソースの該当箇所にジャンプできる。これにより「もっともらしいが根拠のない回答(ハルシネーション)」のリスクを抑えられるが、資料の解釈自体を誤ることはあるため過信は禁物である。

生成された要約や音声・動画も同じ原則で作られる。画面右側の「Studio(スタジオ)」パネルには、音声概要・動画概要・マインドマップ・レポート(FAQ、学習ガイド、ブリーフィングドキュメント、タイムラインなど)の生成ボタンが並び、いずれもノートブックに追加したソースの内容だけを素材にする。音声概要は2025年前半に登場した目玉機能で、AIが台本を作成し、2人の合成音声がポッドキャスト風に資料を解説し合う形式になっている。2025年7月にはスライド形式で資料を解説する動画概要(Video Overview)が追加され、2026年3月には完全にアニメーション化された「Cinematic Video Overview」、2026年6月末には縦型60秒程度の「Short Video Overview」も発表されるなど、機能拡張が続いている。

## 使いどころ・使い分け

「手元の資料の中身だけを根拠に、正確に要約・質問応答させたい」場面に向く。逆に、Web上の最新情報を調べさせたり、資料にない一般知識で自由に文章を作らせたりする用途には向かない。

| 用途 | 向いているツール | 理由 |
|---|---|---|
| 契約書・議事録・社内資料の要約、根拠付きQ&A | NotebookLM | 資料以外の情報を混ぜず、引用元を明示できる |
| 複数の競合レポートを横断して比較・分析 | NotebookLM | ソースを束ねてマインドマップやレポートに変換できる |
| 資料の内容を音声で「ながら聞き」したい | NotebookLM | Audio Overview / Video Overviewが唯一無二の機能 |
| 最新ニュースを調べながら文章を書く | ChatGPT / Gemini(通常チャット) | Web検索と一般知識を組み合わせられる |
| コーディング、汎用的な壁打ち・ブレスト | ChatGPT / Claude | 資料の有無に関わらず自由度の高い対話ができる |
| 大量のコードベースや長大な資料を一度に扱う | Claude Projects | 長文コンテキストの扱いに強い |

NotebookLMは既定でWeb検索を行わず、詳細なシステムプロンプト(AIへの役割設定の指示文)によるキャラクター付けもできない。「資料に忠実な参謀役」であり、「何でも屋のアシスタント」ではないと理解しておくと使い分けを間違えない。

## 実務での使い方

### ノートブックの作り方とソースの追加

1. ブラウザで notebooklm.google.com を開き、Googleアカウントでログイン
2. 「新規作成」→ノートブック名を入力
3. 「ソースを追加」から、次の形式を取り込める
   - ファイルアップロード: PDF、Google ドキュメント、Google スライド、テキストファイル、音声ファイル(mp3など)
   - リンクを貼り付け: ウェブサイトのURL、YouTube動画のURL(字幕・音声から内容を読み取る)
   - テキストを直接貼り付け
   - Google ドライブから選択
4. ソースを追加すると自動で概要が生成され、画面下部のチャット欄で質問できる。回答には引用番号が付き、クリックすると該当ソースの箇所が開く

### 音声概要(Audio Overview)の作り方

1. 右側の「Studio」パネルで「音声概要」を選択
2. 「カスタマイズ」から出力言語(日本語を含む80以上の言語に対応。ソースが英語でも出力を日本語に指定可能)、トーン、長さ、注目してほしいトピックなどをプロンプトで指示できる
3. 「生成」を押すと数分で2人の会話形式の音声が完成し、再生・ダウンロードが可能

活用例: 経営会議の資料一式をソースに入れ、「若手メンバー向けに専門用語をかみ砕いて解説して」と指示して音声概要を作り、通勤中の予習用に配布する、といった使い方ができる。

### 動画概要(Video Overview)の作り方

1. 「Studio」パネルで「動画」を選択し、生成方式(スライド調にソースの図表・引用を差し込むタイプ、AIが映像を新規生成する「Cinematic」タイプなど)を選ぶ
2. Cinematic Video Overview(完全アニメーション生成)はGoogle AI Ultraプランで先行提供、Short Video Overview(縦型60秒程度)はUltra/Proから順次展開されている(2026年7月時点)

### 料金プラン(2026年7月時点の目安)

Googleの料金体系は変更が頻繁なため、契約前に必ず公式ページで最新の数値を確認すること。

| プラン | 月額目安(個人向け) | ノート内ソース数上限 | ノートブック数上限 | 1日のチャット質問数 | 備考 |
|---|---|---|---|---|---|
| NotebookLM(無料) | 0円 | 50件 | 100個 | 50回 | 音声概要は1日3回まで |
| NotebookLM Plus(Google AI Plusに同梱) | 725円(2026年6月に値下げ後の日本価格) | 100件 | 200個 | 200回 | Gemini 3.1 Pro等も利用可 |
| NotebookLM Pro(Google AI Proに同梱) | 2,900円 | 300件 | 500個 | 500回 | ストレージ5TB等も付帯 |
| NotebookLM Ultra(Google AI Ultraに同梱) | 14,500円(20TB)/32,000円(30TB)の2階層(2026年5月に再編) | 500〜600件 | 500個 | 5,000回 | Cinematic Video Overview等を先行提供 |
| NotebookLM Business/Enterprise | Google Workspace Business Standard(1,600円〜)/Business Plus(2,500円〜)に同梱、大規模組織向けはGoogle Cloud経由の「NotebookLM Enterprise」 | Proプラン相当以上 | Proプラン相当以上 | Proプラン相当以上 | 管理者による一元管理・監査ログ・データガバナンスが付く |

### 他ツールとの対応関係(資料に根拠を限定してAIに質問する機能)

「複数資料をまとめてアップロードし、その中身だけを根拠にAIに質問する」機能は各ツールに存在するが、設定場所と挙動が異なる。

| ツール | 機能名 | 検索対象の挙動 | 設定場所 |
|---|---|---|---|
| NotebookLM | ソース(Sources) | アップロード資料のみに厳格に限定し、引用箇所を表示 | notebooklm.google.com→ノートブック作成→「ソースを追加」 |
| ChatGPT | プロジェクトのプロジェクトファイル | アップロードファイルに加え、ChatGPT自身の一般知識・Web検索も併用可能 | 左サイドバー「プロジェクト」→新規作成→ファイルを追加、指示を設定 |
| Claude | プロジェクトのプロジェクトナレッジ | アップロード資料を優先根拠にしつつ、Claude自身の知識でも補完 | 左サイドバー「Projects」→新規作成→「プロジェクトの知識」に追加、カスタム指示を設定 |
| Gemini | Gemのカスタム指示+ファイル添付 | 会話ごとに手動添付する形が基本で、ソースの蓄積管理はNotebookLMほど強力ではない | Gemini画面「Gemマネージャー」→Gem作成→カスタム指示 |

「資料の外側に一切はみ出させたくない」ならNotebookLM、「資料+一般知識を織り交ぜて自然な文章を書かせたい」ならChatGPTやClaudeのプロジェクト機能、という使い分けが基本になる。

## 注意点・よくある誤解

- **無料版でも学習データには使われないが、ガバナンスは別問題**: Googleは無料版・有料版とも、NotebookLMでのやり取りをAIモデルの再学習には使わないとしている。ただし個人のGmailアカウント(無料版)に会社の機密資料を入れると、会社側の管理者が閲覧・監査・削除をコントロールできず、退職時のデータ持ち出しリスクも残る。業務利用ではGoogle Workspace経由のBusiness/Enterprise版を使うのが安全である。
- **引用があっても鵜呑みにしない**: 引用元へのリンクは「その箇所を参照した」ことは示すが、要約や解釈が正確とは限らない。特に数値や契約条件など重要な情報は、必ずリンク元の原文を人間の目で確認する。
- **表・グラフ中心の資料は不得意**: スプレッドシートやデータベースファイルは直接ソースとして追加できない。数値分析が主目的の資料はCSV化・テキスト化するか、別のAIツールに任せる方が向いている。
- **プラン改定が頻繁**: 2025年後半〜2026年にかけてGoogle AI Plus/Pro/Ultraの価格や容量、NotebookLMのソース数上限は何度も変更されている。社内稟議や契約更新の前に必ず公式ページで最新情報を確認する。

## 最初の一歩

手元にある会議資料や契約書PDFを1つNotebookLM(無料)にアップロードし、「この資料の要点を3つ挙げて」と質問して回答の引用リンクをクリックしてみる。続けて「Studio」パネルから音声概要を1本生成し、実際に再生して品質を体感する。

## 関連トピック

- [Google Geminiの基本](./google-gemini-basics.md)
- [AIが扱いやすいデータ形式](../part06-data-analysis/ai-friendly-data-formats.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: NotebookLMの仕組み(資料に根拠を限定する検索拡張生成的な設計)、ソース追加手順、音声概要・動画概要の作り方、2026年7月時点の料金プラン比較(無料/Plus/Pro/Ultra/Business・Enterprise)、ChatGPT Projects・Claude Projectsとの機能対応表を執筆した。
- **出典**: [NotebookLMは無料でどこまで使える？2026年最新の制限と有料プランが必要なケースを解説 | office masui](https://office-masui.com/notebooklm-free-vs-paid-limits-2026/)
- **出典**: [NotebookLM Audio Overviews are now available in over 50 languages | Google Blog](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-audio-overviews-50-languages/)
- **出典**: [NotebookLM's Video Overviews are now available in 80 languages | Google Blog](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebook-lm-audio-video-overviews-more-languages-longer-content/)
- **出典**: [Google's NotebookLM rolls out Video Overviews | TechCrunch](https://techcrunch.com/2025/07/29/googles-notebooklm-rolls-out-video-overviews/)
- **出典**: [What's new in NotebookLM: Video Overviews and an upgraded Studio | Google Workspace Updates](https://workspaceupdates.googleblog.com/2025/07/video-overviews-studio-panel-updates-notebooklm.html)
- **出典**: [NotebookLM Cinematic Video Overview: Full Guide (2026) | Build Fast with AI](https://www.buildfastwithai.com/blogs/notebooklm-cinematic-video-overview-full-guide-2026)
- **出典**: [Google Adds Short Video Overviews to NotebookLM | Tech Times](https://www.techtimes.com/articles/319540/20260702/google-adds-short-video-overviews-notebooklm-powered-nano-banana-2-lite.htm)
- **出典**: [Google AI Ultraとは？Pro版との違いや料金、限定機能を徹底解説 | AI総合研究所](https://www.ai-souken.com/article/google-ai-ultra-guide)
- **出典**: [Google AI Plusとは？月額725円に値下げ・ストレージ倍増・Gemini Advancedとの関係を完全解説【2026年6月速報】 | AI革命株式会社メディア](https://ai-revolution.co.jp/media/what-is-google-ai-plus/)
- **出典**: [Google AI Plus を提供開始 | Google Japan Blog](https://blog.google/intl/ja-jp/company-news/technology/google-ai-plus/)
- **出典**: [月2,900円の価値はある？「Google AI Pro」をChatGPT有料勢が徹底レビュー | TCD](https://tcd-theme.com/2025/10/google-ai-pro.html)
- **出典**: [【2026年版】「NotebookLM」迷子に送る、Google Workspace版とGoogle Cloud版、あなたの会社に必要なのはどっち？ | ソフトバンク クラウドテクノロジーブログ](https://www.softbank.jp/biz/blog/cloud-technology/articles/202601/notebooklm-guide/)
- **出典**: [【企業向け】NotebookLM に学習させない対策｜安全性の実態と運用ルール | 株式会社TSクラウド](https://googleworkspace.tscloud.co.jp/gemini/notebooklm-opt-out)
- **出典**: [NotebookLM vs Claude Projects (2026): Which Is Better for Research? | Elephas](https://elephas.app/blog/notebooklm-vs-claude-projects)
