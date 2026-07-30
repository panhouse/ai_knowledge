---
title: "ChatGPTのCanvas機能"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [ChatGPT, Canvas, ライティングブロック, コードブロック, ChatGPT Work, 文書作成, コーディング, バージョン管理, ツール比較]
created: 2026-07-06
updated: 2026-07-30
---

# ChatGPTのCanvas機能

## これは何か

Canvas(キャンバス)とは、長文の文章やコードを、通常のチャットの流れとは別の**専用の編集画面(右側パネル)**でAIと一緒に育てていく機能として2024年10月に登場した。通常のチャットで長文を直させると、1箇所直したいだけなのに文章・コードが丸ごと再生成され、差分を目で追って確認し直す手間が発生する。Canvasはこれを解決するために作られたもので、文章やコードを画面右側に固定表示し、気になる部分だけをハイライトして「ここを直して」と頼めば、その部分だけが書き換わる、という体験を提供していた。

**2026年7月30日時点では、独立パネルとしてのCanvasはすでに「終わりつつある機能」である。** OpenAIは2026年5月28日、主力モデルのGPT-5.5 Instant/GPT-5.5 Thinkingから右側パネル型のCanvasを削除し、同じ編集体験をチャットの応答内にそのまま展開される「ライティングブロック」「コードブロック」に統合した([Working with writing blocks and code blocks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt))。2026年7月9日に登場した新しい主力モデル群GPT-5.6(Sol/Terra/Luna)もこのブロック方式を引き継いでおり、パネル型Canvasは退役予定のレガシーモデル(o3。2026年8月26日退役予定)を選んだ場合にのみ、期限付きで使い続けられる状態になっている([ChatGPT Canvas sunset: key dates, impacts, migration guidance | AI CERTs](https://www.aicerts.ai/news/chatgpt-canvas-sunset-key-dates-impacts-migration-guidance/))。本ページでは、現在の主役である「ライティングブロック/コードブロック」を中心に、期限付きで残るパネル型Canvasの位置づけも合わせて解説する(呼び方の慣習として、以後もまとめて「Canvas」と呼ぶ)。

## 仕組み・背景

Canvasは2024年10月に発表され、それまでのチャット形式では「長い文章・コードを少しずつ改善する」作業がしにくいという弱点を補うために導入された([Introducing canvas | OpenAI](https://openai.com/index/introducing-canvas/))。中核となる考え方は次の3つで、これは現在のライティングブロック/コードブロックにもそのまま引き継がれている。

- **部分編集**: 直したい範囲だけをハイライトし、指示を出すと、その範囲だけが書き換わる。文章全体を再生成しないため、差分確認の手間が減る
- **ショートカットコマンド**: よく使う編集操作がボタン化されており、指示文を考えなくてもワンクリックで実行できる。文章用には「編集を提案」「長さの調整」「読みやすさ(reading level)の調整」「最終仕上げ(誤字脱字・一貫性チェック)」、コード用には「バグを修正」「他言語に移植」「コードレビュー」などがある
- **バージョン履歴・インライン実行**: 編集のたびに版が記録され、過去の状態に戻せる。Python・JavaScript・HTMLなどのコードはその場で実行してエラーや出力結果を確認できる

### 2026年の大きな変化: パネルからブロックへ

2026年に入ってからの変化は次のタイムラインの通りで、単なる過渡期ではなく、パネル型Canvasが実際に終了へ向かっている段階まで進んでいる。

- **2026年5月28日**: OpenAIはGPT-5.5 Instant/GPT-5.5 Thinkingのアップデートで、独立した右側パネルとしてのCanvasを削除。以後は長文やコードを生成すると、チャットの応答の中に直接「ライティングブロック(文章用)」「コードブロック(コード用)」が展開され、その場で編集・実行できる方式に一本化された([Working with writing blocks and code blocks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt))。理由としてOpenAIは、スマホ・タブレット・Web・デスクトップアプリで表示が揃わない別パネル方式より、チャットに埋め込む方式の方が全端末で一貫した体験になる点を挙げている
- **2026年6月27日**: パネル型Canvasを使い続けられていたレガシーモデルのうちGPT-4.5が退役し、Canvasへのアクセス経路が1つ減った
- **2026年7月9日**: 新しい主力モデル群GPT-5.6(Sol/Terra/Luna)が登場。GPT-5.5と同様にブロック方式を採用しており、独立パネル型のCanvasは搭載していない([The new GPT-5.6 family: Luna, Terra, Sol | Simon Willison](https://simonw.substack.com/p/the-new-gpt-56-family-luna-terra))。同日、複数ステップの作業を自律的にこなして資料・スプレッドシート・Webアプリを仕上げる新機能「ChatGPT Work」も発表されたが、これはCanvasの後継ではなく別の機能である(詳しくは後述)
- **2026年8月26日(予定)**: パネル型Canvasを使える最後のレガシーモデルであるo3が退役予定。これが実施されると、ChatGPTからパネル型のCanvasは実質的に姿を消し、編集体験はライティングブロック/コードブロックに完全統合される見込み([ChatGPT Canvas sunset: key dates, impacts, migration guidance | AI CERTs](https://www.aicerts.ai/news/chatgpt-canvas-sunset-key-dates-impacts-migration-guidance/))

つまり「別パネルを開く」という体験そのものはまもなく終わるが、「文書やコードをその場でピンポイント編集し、バージョン管理できる」という中核の価値は、ライティングブロック/コードブロックという形で存続する。

## 使いどころ・使い分け

| 場面 | 向いている方法 |
|---|---|
| その場で答えが欲しい質問、短い文面の下書き | 通常のチャット |
| 数百〜数千字の提案書・報告書・長文メールを、部分修正しながら仕上げる | ライティングブロック(旧Canvas) |
| 関数単位・ファイル単位のコードを書き、バグ修正やレビューを繰り返す | コードブロック(旧Canvas) |
| ブレインストーミングや方針を決めるための対話そのもの | 通常のチャット(ブロックに載せる「成果物」がまだ無い段階) |
| 複数ステップの調査・作業を丸ごと任せ、資料やスプレッドシートを自律的に仕上げたい | ChatGPT Work(ブロックとは別の自律実行機能) |
| 表計算・グラフ化などデータ分析中心の作業 | データアナリスト機能(ブロックとは別機能) |

判断の目安は従来と変わらず「編集対象が“1つの成果物”として育っていくかどうか」。何度もやり取りしながら1つの文書・1つのコードを完成させていくならブロック(旧Canvas)、その場限りの受け答えで完結するなら通常のチャットでよい。ChatGPT自身が「10行を超える文章やコードを生成しそうだ」と判断すると、指示していなくても自動でブロックが展開される点は、従来のCanvasの自動起動と同じ挙動である。

## 実務での使い方

### 起動方法(2026年7月30日時点)

**通常利用(GPT-5.6などの現行モデル)**: 特別な操作は不要。長文やコードの生成を依頼すると、応答の中に自動でライティングブロック/コードブロックが展開される。ブロック内の直したい範囲をハイライトして修正指示を書けば、その部分だけが書き換わる。「編集用のブロックで書いて」と明示的に頼むこともできる。

**パネル型Canvas(レガシー、2026年8月26日まで)**: 有料プラン(Plus/Pro/Team/Enterprise/Edu)で設定画面から「追加のモデルを表示(Show additional models)」を有効にし、モデル選択でo3を選ぶと、従来どおりの右側パネル型Canvasが使える。この経路はo3の退役(2026年8月26日予定)とともに終了する見込みのため、パネル型の操作感が必要な業務がある場合は早めに切り替え先を検討しておく。なお、o3の後継にあたる推論モデルo3-proではCanvasは提供されていない([Model Release Notes | OpenAI Help Center](https://help.openai.com/en/articles/9624314-model-release-notes))。

利用可能プランは、2026年7月時点でFree・Plus・Pro・Team・Enterprise・Eduを含む主要プランで、ライティングブロック/コードブロックとも無償利用できる。パネル型Canvas(レガシー経由)のみ、o3自体がPlus以上の有料プランでの提供だったため無料プランでは利用できない。

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

| 概念 | ChatGPT | Claude | Gemini | Microsoft Copilot |
|---|---|---|---|---|
| 名称 | ライティングブロック/コードブロック(旧称・レガシー経由のみ「Canvas」) | Artifacts(アーティファクト) | Canvas | Copilot Pages |
| 表示位置 | チャット内に直接展開(2026年8月26日のo3退役まではレガシーモデルで従来の別パネル型も選択可) | チャット右側の別パネル | チャット右側の別パネル | Copilot Chatと並ぶ別ウィンドウ/ページ |
| 起動方法 | 自動起動が基本。「canvasを開いて」「編集用のブロックで書いて」等のフレーズでも起動 | まとまったコード・文書・図表を生成すると自動で開く | Toolsメニュー(+)からCanvasを選択 | Copilot Chatの回答を「ページに保存」、またはBusiness Chatから作成 |
| 対応プラン(2026年7月時点) | ブロック機能はFree/Plus/Pro/Team/Enterprise/Eduで無償利用可。パネル型Canvas(レガシー)はPlus以上限定で2026年8月26日終了予定([OpenAI Help Center](https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt)) | HTML/React/SVG/Mermaid/コード/文書の基本利用はFreeプランを含め無償。MCP連携やLive Artifacts等の高度機能は有料プラン(Pro/Max/Team/Enterprise)が必要([Claude Help Center](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)) | 全ユーザーが利用可能。Google AI Pro/Ultraでは、より高性能なモデルと大きなコンテキスト(処理できる文章量)で利用できる([Gemini Canvas | Google](https://gemini.google/overview/canvas/)) | Microsoft 365 Copilotの有料ライセンス(Business Basic/Standard/Premium等の対象プラン+Copilotアドオン)が必要 |
| 得意分野 | 文章の部分編集+コード実行・レビュー | コード・Webページ・図表など「動くもの」のプレビューとMCP連携によるライブデータ取り込み | ドキュメント作成に加え、簡易アプリ・ゲームのプロトタイピング | Word/PowerPoint形式への書き出しやTeams/Outlookでのチーム共有 |

3社(OpenAI/Anthropic/Google)とも「チャットの流れの中で成果物を育てる」という設計は共通しているが、ChatGPTはブロックをチャットに埋め込む方式へ舵を切ったのに対し、Claude・Geminiは引き続き別パネル方式を維持している。Microsoft Copilot Pagesはチーム共同編集・Office文書への書き出しに寄せた位置づけである。4ツールの詳しい横並び比較は[主要AIチャットツールのCanvas/Artifacts機能比較](ai-chat-tools-canvas-artifacts-comparison.md)を参照。

## 注意点・よくある誤解

- **もう「別画面」ですらなくなりつつある**: 2026年5月のアップデート以降、多くのユーザーにとってCanvasは独立したパネルではなく、チャットの応答に埋め込まれた「ライティングブロック/コードブロック」として体験される。「Canvasのボタンを探したが見当たらない」という場合、機能が無くなったのではなく体験の置き場所がチャット内に移っている
- **パネル型Canvasは期限付き**: 従来の別パネル型を使い続けられるのは、レガシーモデルのo3を選んだ場合のみで、2026年8月26日の退役予定とともにこの経路も閉じる見込み。パネル表示に依存した業務フロー・マニュアルがある場合は、ブロック方式への切り替えを早めに済ませておく
- **ハイライトしないと全体が書き換わることがある**: 部分修正をしたいのに範囲を選択せずに指示すると、文章・コード全体が再生成される場合がある。狙った箇所だけを直したいときは、必ず対象をハイライトしてから指示する
- **バージョン履歴は「保存」ではない**: 巻き戻しはできるが、チャット外部に別途保存されるわけではないので、完成した文書・コードは都度コピーしてWordやリポジトリなど本来の保存先に移す
- **コード実行はあくまで簡易確認用**: ブロック内のコード実行はサンドボックス上の簡易的な動作確認であり、本番相当の環境検証やセキュリティレビューの代わりにはならない。重要なコードは通常の開発環境・レビュー体制でも必ず確認する
- **「ChatGPT Work」と混同しない**: 2026年7月9日に登場した「ChatGPT Work」は、複数ステップの作業を自律的にこなして資料・スプレッドシート・Webアプリなどを仕上げる別の新機能であり、ユーザーが範囲をハイライトして細かく直していくブロック(旧Canvas)とは目的が異なる。「資料を作る」という見た目は似ていても、手を動かしながら部分編集したいのか、丸ごと自律的に任せたいのかで使い分ける
- **業務データを貼る際はプランの学習利用設定を確認**: ブロック機能自体に固有のセキュリティ機能があるわけではなく、通常のチャットと同じデータ取り扱いルールが適用される。社外秘の資料を扱う場合は、Enterprise/Team等の法人プランか、個人プランならデータ利用のオプトアウト設定を事前に確認する([ChatGPTの初期設定とデータ利用のオプトアウト](./chatgpt-initial-setup-and-opt-out.md)も参照)

## 最初の一歩

今取り組んでいる長めの文書(提案書・報告書・長文メールのいずれか)を1つ選び、「〇〇のたたき台を書いて」と入力し、応答内に展開されたライティングブロックの1段落だけをハイライトして「ここだけ簡潔にして」と修正を頼んでみる。従来のパネル型操作を体験しておきたい場合は、設定でレガシーモデル(o3)を有効にして試す(2026年8月26日の退役まで)。

## 関連トピック

- [主要AIチャットツールのCanvas/Artifacts機能比較](ai-chat-tools-canvas-artifacts-comparison.md)
- [ChatGPTのモデル一覧と使い分け](./chatgpt-model-lineup.md)
- [Claude(Anthropic)の基本](claude-basics.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [Microsoft Copilotの基本](microsoft-copilot-basics.md)

## 更新履歴

### 2026-07-30: パネル型Canvas終了のタイムラインを反映し全面改訂
- **内容**: 2026年5月28日のGPT-5.5アップデートでパネル型Canvasが削除されライティングブロック/コードブロックに統合された経緯、GPT-4.5退役(6月27日)・GPT-5.6(Sol/Terra/Luna)登場(7月9日)・o3退役予定(8月26日)という2026年のタイムライン、レガシーモデル経由でのパネル型Canvas利用方法、新機能「ChatGPT Work」との違いを反映し、「これは何か」「仕組み・背景」「使いどころ・使い分け」「実務での使い方」「ツール横断の対応付け」「注意点」を全面的に書き換え
- **出典**: [Working with writing blocks and code blocks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt)、[ChatGPT Canvas sunset: key dates, impacts, migration guidance | AI CERTs](https://www.aicerts.ai/news/chatgpt-canvas-sunset-key-dates-impacts-migration-guidance/)、[The new GPT-5.6 family: Luna, Terra, Sol | Simon Willison](https://simonw.substack.com/p/the-new-gpt-56-family-luna-terra)、[Model Release Notes | OpenAI Help Center](https://help.openai.com/en/articles/9624314-model-release-notes)、[OpenAI launches ChatGPT Work and unveils unified desktop app with Codex built in | Neowin](https://www.neowin.net/news/openai-launches-chatgpt-work-and-unveils-unified-desktop-app-with-codex-built-in/)

### 2026-07-06: 初版執筆
- **内容**: Canvasの仕組み(部分編集・ショートカットコマンド・バージョン履歴)、起動方法、対応プラン、GPT-5.5系モデルでのライティングブロック/コードブロックへの統合という2026年の変化、Claude Artifacts・Gemini Canvas・Microsoft Copilot Pagesとの比較表を整理
- **出典**: [Introducing canvas | OpenAI](https://openai.com/index/introducing-canvas/)、[What is the canvas feature in ChatGPT and how do I use it? | OpenAI Help Center](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it)、[モデルリリースノート | OpenAI Help Center](https://help.openai.com/ja-jp/articles/9624314-model-release-notes)、[ChatGPTでのライティングブロックとコードブロックの使用 | OpenAI Help Center](https://help.openai.com/ja-jp/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt)、[What are artifacts and how do I use them? | Claude Help Center](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)、[Gemini Canvas — write, code, & create in one space with AI | Google](https://gemini.google/overview/canvas/)、[Get started with Microsoft 365 Copilot Pages | Microsoft Support](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-pages)
