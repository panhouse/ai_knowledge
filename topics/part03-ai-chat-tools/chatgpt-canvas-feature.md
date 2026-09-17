---
title: "ChatGPTのCanvas機能"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [ChatGPT, Canvas, ライティングブロック, コードブロック, ChatGPT Work, GPT-6 Astra, 文書作成, コーディング, バージョン管理]
created: 2026-07-06
updated: 2026-09-15
---

# ChatGPTのCanvas機能

## これは何か

Canvas(キャンバス)とは、長文の文章やコードを、通常のチャットの流れとは別の**専用の編集画面(右側パネル)**でAIと一緒に育てていく機能として2024年10月に登場した。通常のチャットで長文を直させると、1箇所直したいだけなのに文章・コードが丸ごと再生成され、差分を目で追って確認し直す手間が発生する。Canvasはこれを解決するために作られたもので、文章やコードを画面右側に固定表示し、気になる部分だけをハイライトして「ここを直して」と頼めば、その部分だけが書き換わる、という体験を提供していた。

**2026年9月15日時点では、独立パネルとしてのCanvasは完全に終了しており、ChatGPTの編集体験はチャットの応答内にそのまま展開される「ライティングブロック」「コードブロック」に一本化されている。** OpenAIは2026年5月28日、主力モデルのGPT-5.5 Instant/GPT-5.5 Thinkingから右側パネル型のCanvasを削除し、この方式に統合した([Working with writing blocks and code blocks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt))。その後登場したGPT-5.6(Sol/Terra/Luna、2026年7月9日)、そして最新の主力モデルGPT-6 Astra(2026年9月3〜4日ロールアウト開始)も、いずれもこのブロック方式を引き継いでおり、独立パネル型のCanvasは搭載していない([GPT-6 Astra - Wikipedia](https://en.wikipedia.org/wiki/GPT-6_Astra))。パネル型Canvasを唯一使い続けられていたレガシーモデルo3は、予告どおり2026年8月26日にChatGPTから退役し、これによって独立パネル型のCanvasは実質的に姿を消した([OpenAI Retired o3 From ChatGPT Today | Forkast](https://forkast.news/openai-retired-o3-from-chatgpt-today-the-real-cost-is-the-churn-it-forces-on-everyone-else/))。本ページでは、現在の主役である「ライティングブロック/コードブロック」を中心に解説する(呼び方の慣習として、以後もまとめて「Canvas」と呼ぶ)。

## 仕組み・背景

Canvasは2024年10月に発表され、それまでのチャット形式では「長い文章・コードを少しずつ改善する」作業がしにくいという弱点を補うために導入された([Introducing canvas | OpenAI](https://openai.com/index/introducing-canvas/))。中核となる考え方は次の3つで、これは現在のライティングブロック/コードブロックにもそのまま引き継がれている。

- **部分編集**: 直したい範囲だけをハイライトし、指示を出すと、その範囲だけが書き換わる。文章全体を再生成しないため、差分確認の手間が減る
- **ショートカットコマンド**: よく使う編集操作がボタン化されており、指示文を考えなくてもワンクリックで実行できる。文章用には「編集を提案」「長さの調整」「読みやすさ(reading level)の調整」「最終仕上げ(誤字脱字・一貫性チェック)」、コード用には「バグを修正」「他言語に移植」「コードレビュー」などがある
- **バージョン履歴・インライン実行**: 編集のたびに版が記録され、過去の状態に戻せる。Python・JavaScript・HTMLなどのコードはその場で実行してエラーや出力結果を確認できる。2026年2月には、コードブロックがその場で「書く・直す・プレビューする」を一体で行える双方向対応に強化されており、この操作性はGPT-5.6・GPT-6 Astra世代でも引き継がれている

### 2026年の変化: パネルからブロックへ、そしてGPT-6 Astraへ

2026年に入ってからの変化は次のタイムラインの通り。パネル型Canvasは単なる過渡期を経て、実際に終了まで進んでいる。

- **2026年5月28日**: OpenAIはGPT-5.5 Instant/GPT-5.5 Thinkingのアップデートで、独立した右側パネルとしてのCanvasを削除。以後は長文やコードを生成すると、チャットの応答の中に直接「ライティングブロック(文章用)」「コードブロック(コード用)」が展開され、その場で編集・実行できる方式に一本化された([OpenAI Help Center](https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt))。理由としてOpenAIは、スマホ・タブレット・Web・デスクトップアプリで表示が揃わない別パネル方式より、チャットに埋め込む方式の方が全端末で一貫した体験になる点を挙げている
- **2026年6月27日**: パネル型Canvasを使い続けられていたレガシーモデルのうちGPT-4.5が退役し、Canvasへのアクセス経路が1つ減った
- **2026年7月9日**: 新しい主力モデル群GPT-5.6(Sol/Terra/Luna)が登場。GPT-5.5と同様にブロック方式を採用しており、独立パネル型のCanvasは搭載していない([OpenAI launches its new family of models with GPT-5.6 | TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/))。同日、複数ステップの作業を自律的にこなして資料・スプレッドシート・Webアプリを仕上げる新機能「ChatGPT Work」も発表されたが、これはCanvasの後継ではなく別の機能である(詳しくは後述)
- **2026年8月26日**: パネル型Canvasを使える最後のレガシーモデルであるo3が予告どおり退役。o3-proは引き続きPro/Business/Enterprise/Eduで利用できるが、Canvasパネルは提供対象外のため、これによりChatGPTから独立パネル型のCanvasは実質的に姿を消した([OpenAI Retired o3 From ChatGPT Today | Forkast](https://forkast.news/openai-retired-o3-from-chatgpt-today-the-real-cost-is-the-churn-it-forces-on-everyone-else/))
- **2026年9月3〜4日**: 最新の主力モデルGPT-6 Astraが登場(Plus/Pro/Business/Enterprise向けに順次ロールアウト)。「コンピュータ操作(computer use)」など大きな新機能が話題になったが、文章・コードの編集体験はGPT-5.6と同じくライティングブロック/コードブロックのままで、独立パネル型Canvasは復活していない([GPT-6 Astra - Wikipedia](https://en.wikipedia.org/wiki/GPT-6_Astra))

つまり「別パネルを開く」という体験そのものは完全に終わったが、「文書やコードをその場でピンポイント編集し、バージョン管理できる」という中核の価値は、ライティングブロック/コードブロックという形で存続しており、最新のGPT-6 Astraでもこの方式が引き継がれている。

## 使いどころ・使い分け

| 場面 | 向いている方法 |
|---|---|
| その場で答えが欲しい質問、短い文面の下書き | 通常のチャット |
| 数百〜数千字の提案書・報告書・長文メールを、部分修正しながら仕上げる | ライティングブロック(旧Canvas) |
| 関数単位・ファイル単位のコードを書き、バグ修正やレビューを繰り返す | コードブロック(旧Canvas) |
| ブレインストーミングや方針を決めるための対話そのもの | 通常のチャット(ブロックに載せる「成果物」がまだ無い段階) |
| 複数ステップの調査・作業を丸ごと任せ、資料やスプレッドシートを自律的に仕上げたい | ChatGPT Work(ブロックとは別の自律実行機能。Plus以上のプランが対象で、Free/Goでは利用不可) |
| 表計算・グラフ化などデータ分析中心の作業 | データアナリスト機能(ブロックとは別機能) |

判断の目安は従来と変わらず「編集対象が“1つの成果物”として育っていくかどうか」。何度もやり取りしながら1つの文書・1つのコードを完成させていくならブロック(旧Canvas)、その場限りの受け答えで完結するなら通常のチャットでよい。ChatGPT自身が「10行を超える文章やコードを生成しそうだ」と判断すると、指示していなくても自動でブロックが展開される点は、従来のCanvasの自動起動と同じ挙動である。

## 実務での使い方

### 起動方法(2026年9月時点)

特別な操作は不要。GPT-6 Astra・GPT-5.6(Sol/Terra/Luna)・GPT-5.5などの現行モデルで長文やコードの生成を依頼すると、応答の中に自動でライティングブロック/コードブロックが展開される。ブロック内の直したい範囲をハイライトして修正指示を書けば、その部分だけが書き換わる。「編集用のブロックで書いて」「canvasを開いて」と明示的に頼む言い方も引き続き通じ、生成物がブロックとして展開される。

2026年8月26日のo3退役をもって、独立パネル型Canvasへのアクセス経路(レガシーモデル経由)は完全に閉じた。従来の別パネル操作に慣れた業務マニュアルが残っている場合は、ブロック方式を前提にした案内へ更新しておく。

**対応プラン(2026年9月時点)**: ライティングブロック/コードブロックは、無償のFreeプランを含む全プラン(Free・Go・Plus・Pro・Business・Enterprise・Edu)で無償利用できる。プラン体系は次の通り([ChatGPT pricing | OpenAI](https://openai.com/chatgpt/pricing/)、[ChatGPT Business Rename FAQ | OpenAI Help Center](https://help.openai.com/en/articles/12111915-chatgpt-business-rename-faq))。

| プラン | 料金(2026年9月時点) | 備考 |
|---|---|---|
| Free | 無料 | 2026年8月からテキスト会話の回数上限が撤廃され、デフォルトモデルはGPT-5.6 Luna |
| Go | 月額8ドル | 2026年1月にグローバル展開。FreeとPlusの間を埋める廉価プラン |
| Plus | 月額20ドル | 個人向け主力プラン。ChatGPT Work・Deep Research等も利用可 |
| Pro | 月額100ドルまたは200ドル | 2026年4月に100ドルの中間ティアを追加。200ドル版がより高い利用上限 |
| Business(旧Team) | Standardが月額20〜25ドル/席、Premiumが月額100〜125ドル/席 | 2025年8月に「Team」から名称変更。Premiumは2026年8月追加で、5時間ごとの利用上限が撤廃され利用量もStandardの5倍 |
| Enterprise / Edu | 個別見積もり | 組織向け。管理機能・データ保護契約(DPA)などが付く |

なお「ChatGPT Business」はもともと「ChatGPT Team」が2025年8月に改称されたプランで、2026年7月に登場した自律実行機能「ChatGPT Work」とは別物である。名前が紛らわしいため注意する。

### コピペで使える実例

提案書の下書きをブロックで作り、一部だけ直す例:

```
以下の条件で新規取引先向けの提案書のたたき台を書いてください。
・対象: 中小製造業の購買部門
・目的: 在庫管理クラウドサービスの導入提案
・分量: A4 1枚程度、見出し付き
```

```
(展開されたライティングブロック上で「価格」の段落をハイライトしてから)
この段落だけ、初期費用と月額費用を分けた箇条書きに書き換えてください。
他の段落はそのままにしてください。
```

コードのバグ修正・レビューを頼む例:

```
CSVを読み込んで列ごとに合計を出すPython関数を書いてください。
```

```
(該当のfor文をハイライトしてから)
ここだけ処理速度が遅くなっている原因を調べて、改善案を反映してください。
```

「canvasを開いて◯◯を書いて」という言い方も、現行モデルに対する指示としては引き続き通じ、生成物がライティングブロック/コードブロックとして展開される。慣れた言い回しをそのまま使ってよい。

### ツール横断の対応付け

ChatGPTのライティングブロック/コードブロックに相当する機能は、Claudeでは「Artifacts」、Geminiでは「Canvas」、Microsoft Copilotでは「Pages」と呼ばれる。表示位置(チャット内蔵か別パネルか)・起動方法・対応プラン・エクスポート先まで含めた4ツールの詳しい横並び比較は[主要AIチャットツールのCanvas/Artifacts機能比較](ai-chat-tools-canvas-artifacts-comparison.md)にまとめてあるため、そちらを参照。本ページではChatGPT自身の仕様に絞って解説する。

## 注意点・よくある誤解

- **もう「別画面」ではない(完了済み)**: 2026年5月のアップデート以降、Canvasは独立したパネルではなく、チャットの応答に埋め込まれた「ライティングブロック/コードブロック」として体験される。2026年8月26日のo3退役により、レガシーモデル経由での別パネルアクセスも閉じた。「Canvasのボタンを探したが見当たらない」という場合、機能が無くなったのではなく体験の置き場所がチャット内に移っている
- **ハイライトしないと全体が書き換わることがある**: 部分修正をしたいのに範囲を選択せずに指示すると、文章・コード全体が再生成される場合がある。狙った箇所だけを直したいときは、必ず対象をハイライトしてから指示する
- **バージョン履歴は「保存」ではない**: 巻き戻しはできるが、チャット外部に別途保存されるわけではないので、完成した文書・コードは都度コピーしてWordやリポジトリなど本来の保存先に移す
- **コード実行はあくまで簡易確認用**: ブロック内のコード実行はサンドボックス上の簡易的な動作確認であり、本番相当の環境検証やセキュリティレビューの代わりにはならない。重要なコードは通常の開発環境・レビュー体制でも必ず確認する
- **「ChatGPT Work」「ChatGPT Business」と混同しない**: 2026年7月9日に登場した「ChatGPT Work」は、複数ステップの作業を自律的にこなして資料・スプレッドシート・Webアプリなどを仕上げる自律実行機能で、ユーザーが範囲をハイライトして細かく直していくブロック(旧Canvas)とは目的が異なる。また「ChatGPT Business」は2025年8月に「ChatGPT Team」プランが改称されたものであり、Workとは無関係の料金プラン名なので混同しない
- **業務データを貼る際はプランの学習利用設定を確認**: ブロック機能自体に固有のセキュリティ機能があるわけではなく、通常のチャットと同じデータ取り扱いルールが適用される。社外秘の資料を扱う場合は、Business/Enterprise等の法人プランか、個人プランならデータ利用のオプトアウト設定を事前に確認する([ChatGPTの初期設定とデータ利用のオプトアウト](./chatgpt-initial-setup-and-opt-out.md)も参照)

## 最初の一歩

今取り組んでいる長めの文書(提案書・報告書・長文メールのいずれか)を1つ選び、「〇〇のたたき台を書いて」と入力し、応答内に展開されたライティングブロックの1段落だけをハイライトして「ここだけ簡潔にして」と修正を頼んでみる。独立パネル型のCanvasはすでに終了しているため、今後はブロック方式を前提に業務フローを組み立てる。

## 関連トピック

- [主要AIチャットツールのCanvas/Artifacts機能比較](ai-chat-tools-canvas-artifacts-comparison.md)
- [ChatGPTのモデル一覧と使い分け](./chatgpt-model-lineup.md)
- [Claude(Anthropic)の基本](claude-basics.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [Microsoft Copilotの基本](microsoft-copilot-basics.md)

## 更新履歴

### 2026-09-15: パネル型Canvasの完全終了とGPT-6 Astra登場を反映し最新化
- **内容**: 2026年8月26日にo3が予告どおり退役し、レガシーモデル経由のパネル型Canvasアクセスが完全に閉じたこと、2026年9月3〜4日に登場した最新モデルGPT-6 Astraもブロック方式を引き継いでいることを反映。プラン体系をFree・Go($8)・Plus($20)・Pro(100/200ドルの2段階)・Business(Standard/Premium、旧Team)・Enterprise/Eduの最新構成に更新し、「ChatGPT Work」と「ChatGPT Business」を混同しないよう注意点に追記。サイブリングページ([主要AIチャットツールのCanvas/Artifacts機能比較](ai-chat-tools-canvas-artifacts-comparison.md))と重複していた4ツール比較表は撤去し、リンク参照に一本化
- **出典**: [Working with writing blocks and code blocks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt)、[OpenAI Retired o3 From ChatGPT Today | Forkast](https://forkast.news/openai-retired-o3-from-chatgpt-today-the-real-cost-is-the-churn-it-forces-on-everyone-else/)、[GPT-6 Astra - Wikipedia](https://en.wikipedia.org/wiki/GPT-6_Astra)、[OpenAI launches its new family of models with GPT-5.6 | TechCrunch](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)、[ChatGPT Business Rename FAQ | OpenAI Help Center](https://help.openai.com/en/articles/12111915-chatgpt-business-rename-faq)、[ChatGPT pricing | OpenAI](https://openai.com/chatgpt/pricing/)

### 2026-07-30: パネル型Canvas終了のタイムラインを反映し全面改訂
- **内容**: 2026年5月28日のGPT-5.5アップデートでパネル型Canvasが削除されライティングブロック/コードブロックに統合された経緯、GPT-4.5退役(6月27日)・GPT-5.6(Sol/Terra/Luna)登場(7月9日)・o3退役予定(8月26日)という2026年のタイムライン、レガシーモデル経由でのパネル型Canvas利用方法、新機能「ChatGPT Work」との違いを反映し、「これは何か」「仕組み・背景」「使いどころ・使い分け」「実務での使い方」「ツール横断の対応付け」「注意点」を全面的に書き換え
- **出典**: [Working with writing blocks and code blocks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt)、[ChatGPT Canvas sunset: key dates, impacts, migration guidance | AI CERTs](https://www.aicerts.ai/news/chatgpt-canvas-sunset-key-dates-impacts-migration-guidance/)、[The new GPT-5.6 family: Luna, Terra, Sol | Simon Willison](https://simonw.substack.com/p/the-new-gpt-56-family-luna-terra)、[Model Release Notes | OpenAI Help Center](https://help.openai.com/en/articles/9624314-model-release-notes)、[OpenAI launches ChatGPT Work and unveils unified desktop app with Codex built in | Neowin](https://www.neowin.net/news/openai-launches-chatgpt-work-and-unveils-unified-desktop-app-with-codex-built-in/)

### 2026-07-06: 初版執筆
- **内容**: Canvasの仕組み(部分編集・ショートカットコマンド・バージョン履歴)、起動方法、対応プラン、GPT-5.5系モデルでのライティングブロック/コードブロックへの統合という2026年の変化、Claude Artifacts・Gemini Canvas・Microsoft Copilot Pagesとの比較表を整理
- **出典**: [Introducing canvas | OpenAI](https://openai.com/index/introducing-canvas/)、[What is the canvas feature in ChatGPT and how do I use it? | OpenAI Help Center](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it)、[モデルリリースノート | OpenAI Help Center](https://help.openai.com/ja-jp/articles/9624314-model-release-notes)、[ChatGPTでのライティングブロックとコードブロックの使用 | OpenAI Help Center](https://help.openai.com/ja-jp/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt)、[What are artifacts and how do I use them? | Claude Help Center](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)、[Gemini Canvas — write, code, & create in one space with AI | Google](https://gemini.google/overview/canvas/)、[Get started with Microsoft 365 Copilot Pages | Microsoft Support](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-pages)
