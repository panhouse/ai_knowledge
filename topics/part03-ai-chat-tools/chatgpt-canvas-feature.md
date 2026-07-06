---
title: "ChatGPTのCanvas機能"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [ChatGPT, Canvas, 文書作成, コーディング, バージョン管理, ツール比較]
created: 2026-07-06
updated: 2026-07-06
---

# ChatGPTのCanvas機能

## これは何か

Canvas(キャンバス)とは、長文の文章やコードを、通常のチャットの流れとは別の**専用の編集画面(右側パネル)**でAIと一緒に育てていく機能である。通常のチャットで長文を直させると、1箇所直したいだけなのに文章・コードが丸ごと再生成され、差分を目で追って確認し直す手間が発生する。Canvasはこれを解決するために作られたもので、文章やコードを画面右側に固定表示し、気になる部分だけをハイライトして「ここを直して」と頼めば、その部分だけが書き換わる。

2026年に入り、ChatGPTの一部の新しいモデル(GPT-5.5系)では、Canvasの機能自体はチャット画面に内蔵された「ライティングブロック」「コードブロック」という形に統合されつつある。つまり「別パネルを開く」という体験は今まさに変わりつつある過渡期にあるが、「文書やコードをその場でピンポイント編集し、バージョン管理できる」という中核の価値は変わらない。本ページでは以後「Canvas」という呼び方で、この一連の編集体験を扱う。

## 仕組み・背景

Canvasは2024年10月に発表された機能で、それまでのチャット形式では「長い文章・コードを少しずつ改善する」作業がしにくいという弱点を補うために導入された([Introducing canvas | OpenAI](https://openai.com/index/introducing-canvas/))。仕組みのポイントは次の3つ。

- **部分編集**: 直したい範囲だけをドラッグしてハイライトし、指示を出すと、その範囲だけが書き換わる。文章全体を再生成しないため、差分確認の手間が減る
- **ショートカットコマンド**: よく使う編集操作がボタン化されており、指示文を考えなくてもワンクリックで実行できる。文章用には「編集を提案」「長さの調整」「読みやすさ(reading level)の調整」「最終仕上げ(誤字脱字・一貫性チェック)」「絵文字を追加」、コード用には「ログを追加」「コメントを追加」「バグを修正」「他言語に移植」「コードレビュー」がある
- **バージョン履歴**: 編集のたびに版が記録され、画面上部の巻き戻しボタンでいつでも過去の状態に戻せる。「さっきの案の方が良かった」というときに、遡って手戻りできる

コードのCanvasでは、Python・JavaScript・HTMLなどをその場で実行してエラーや出力結果を確認できる「インライン実行」にも対応しており、コードを書いては別ツールにコピーして動かす、という往復が減る。

**2026年時点の重要な変化**: OpenAIは最新モデル群(GPT-5.5 Instant/GPT-5.5 Thinking)において、独立した右側パネルとしてのCanvasを提供せず、同等の機能をチャットの応答中に直接展開される「ライティングブロック」「コードブロック」として統合する方針に転換している。有料プランのユーザーは、GPT-5.5系がまだ主力でなかった時期のレガシーモデルを選べば、当面の間は従来型のCanvas(独立パネル)を使い続けられるが、レガシーモデルが提供終了になれば、体験はブロック形式に一本化される見込みである([モデルリリースノート | OpenAI Help Center](https://help.openai.com/ja-jp/articles/9624314-model-release-notes)、[ChatGPTでのライティングブロックとコードブロックの使用 | OpenAI Help Center](https://help.openai.com/ja-jp/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt))。使う画面の見た目は変わっても、「部分編集」「ショートカット」「バージョン管理」という考え方自体は引き継がれている。

## 使いどころ・使い分け

| 場面 | 向いている方法 |
|---|---|
| その場で答えが欲しい質問、短い文面の下書き | 通常のチャット |
| 数百〜数千字の提案書・報告書・長文メールを、部分修正しながら仕上げる | Canvas |
| 関数単位・ファイル単位のコードを書き、バグ修正やレビューを繰り返す | Canvas(コード) |
| ブレインストーミングや方針を決めるための対話そのもの | 通常のチャット(Canvasに載せる「成果物」がまだ無い段階) |
| 表計算・グラフ化などデータ分析中心の作業 | データアナリスト機能(Canvasとは別機能) |

判断の目安は「編集対象が“1つの成果物”として育っていくかどうか」。何度もやり取りしながら1つの文書・1つのコードを完成させていくならCanvas、その場限りの受け答えで完結するなら通常のチャットでよい。ChatGPT自身が「10行を超える文章やコードを生成しそうだ」「編集用のインターフェースがあった方が便利そうだ」と判断すると、指示していなくても自動でCanvasが開くことがある点も覚えておくと使い勝手が上がる。

## 実務での使い方

### 起動方法(2026年7月時点)

1. 入力欄左側の「+」(ツール)ボタンをクリックし、一覧から「Canvas」を選ぶ
2. すでに出ている回答に対しては、回答の右上に出る鉛筆アイコン(編集)から「canvasで開く」を選ぶと、その内容がCanvasに移る
3. プロンプトの中に「canvasを使って」「canvasを開いて〇〇を書いて」と書くだけでも起動できる(自動判定でも開くが、明示すると確実)
4. 入力欄で半角スラッシュ「/」を入力し、コマンド候補から「canvas」を選ぶ方法もある
5. Canvasが開いたら、直したい範囲をドラッグしてハイライトし、下部の入力欄に修正指示を書く。右下の鉛筆アイコンからショートカットメニューを開けば、ボタン一つで「最終仕上げ」「読みやすさ調整」などを実行できる
6. 画面上部の巻き戻し矢印でバージョン履歴を遡れる

利用可能プランは、2026年7月時点でFree・Plus・Pro・Team・Enterprise・Eduを含む主要プランで無償利用でき、Web版・Windows版・macOS版アプリで使える([What is the canvas feature in ChatGPT and how do I use it? | OpenAI Help Center](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it))。Freeプランでは全体のメッセージ数の上限に達しやすい点以外、Canvas自体の機能制限はない。

### コピペで使える実例

提案書の下書きをCanvasで作り、一部だけ直す例:

```
canvasを開いて、以下の条件で新規取引先向けの提案書のたたき台を書いてください。
・対象: 中小製造業の購買部門
・目的: 在庫管理クラウドサービスの導入提案
・分量: A4 1枚程度、見出し付き
```

```
(Canvas上で「価格」の段落をハイライトしてから)
この段落だけ、初期費用と月額費用を分けた箇条書きに書き換えてください。
他の段落はそのままにしてください。
```

コードのバグ修正・レビューを頼む例:

```
canvasでこの関数を書いて。CSVを読み込んで列ごとに合計を出すPython関数。
```

```
(該当のfor文をハイライトしてから)
ここだけ処理速度が遅くなっている原因を調べて、改善案を反映してください。
```

### ツール横断の対応付け

| 概念 | ChatGPT | Claude | Gemini | Microsoft Copilot |
|---|---|---|---|---|
| 名称 | Canvas(一部モデルでは「ライティングブロック/コードブロック」に統合中) | Artifacts(アーティファクト) | Canvas | Copilot Pages |
| 表示位置 | チャット右側の別パネル(新モデルではチャット内に直接展開) | チャット右側の別パネル | チャット右側の別パネル | Copilot Chatと並ぶ別ウィンドウ/ページ |
| 起動方法 | +ボタン→Canvas、自動起動、「canvasを開いて」等のフレーズ | まとまったコード・文書・図表を生成すると自動で開く | Toolsメニュー(+)からCanvasを選択 | Copilot Chatの回答を「ページに保存」、またはBusiness Chatから作成 |
| 対応プラン(2026年7月時点) | Free/Plus/Pro/Team/Enterprise/Eduで無償利用可([OpenAI Help Center](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it)) | HTML/React/SVG/Mermaid/コード/文書の基本利用はFreeプランを含め無償。MCP連携やLive Artifacts等の高度機能は有料プラン(Pro/Max/Team/Enterprise)が必要([Claude Help Center](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)) | 全ユーザーが利用可能。Google AI Pro/Ultraでは、より高性能なモデルと大きなコンテキスト(処理できる文章量)で利用できる([Gemini Canvas | Google](https://gemini.google/overview/canvas/)) | Microsoft 365 Copilotの有料ライセンス(Business Basic/Standard/Premium等の対象プラン+Copilotアドオン)が必要 |
| 得意分野 | 文章の部分編集+コード実行・レビュー | コード・Webページ・図表など「動くもの」のプレビューとMCP連携によるライブデータ取り込み | ドキュメント作成に加え、簡易アプリ・ゲームのプロトタイピング | Word/PowerPoint形式への書き出しやTeams/Outlookでのチーム共有 |

3社(OpenAI/Anthropic/Google)とも「チャットの流れと切り離した編集専用パネルを持つ」という設計は共通しており、Microsoft Copilot Pagesも考え方は同じだが、位置づけとしてはチーム共同編集・Office文書への書き出しに寄せている。

## 注意点・よくある誤解

- **Canvas=別機能ではなく「チャットの延長」**: Canvas内のやり取りも同じ会話の一部であり、Canvasを閉じてもチャット欄に戻って会話を続けられる。「別の場所に切り出した」わけではなく「表示の仕方が変わった」だけと捉えるとよい
- **ハイライトしないと全体が書き換わることがある**: 部分修正をしたいのに範囲を選択せずに指示すると、文章・コード全体が再生成される場合がある。狙った箇所だけを直したいときは、必ず対象をハイライトしてから指示する
- **モデルによって使えない・体験が違う**: 2026年時点でGPT-5.5系の新しいモデルでは、独立パネル型のCanvasではなく、チャット内蔵の「ライティングブロック/コードブロック」に置き換わりつつある。「Canvasのボタンが見当たらない」という場合、選択しているモデルが影響している可能性がある
- **バージョン履歴は「保存」ではない**: 巻き戻しはできるが、チャット外部に別途保存されるわけではないので、完成した文書・コードは都度コピーしてWordやリポジトリなど本来の保存先に移す
- **コード実行はあくまで簡易確認用**: Canvas内のコード実行はサンドボックス上の簡易的な動作確認であり、本番相当の環境検証やセキュリティレビューの代わりにはならない。重要なコードは通常の開発環境・レビュー体制でも必ず確認する
- **業務データを貼る際はプランの学習利用設定を確認**: Canvas自体に固有のセキュリティ機能があるわけではなく、通常のチャットと同じデータ取り扱いルールが適用される。社外秘の資料を扱う場合は、Enterprise/Team等の法人プランか、個人プランならデータ利用のオプトアウト設定を事前に確認する([ChatGPTの初期設定とデータ利用のオプトアウト](./chatgpt-initial-setup-and-opt-out.md)も参照)

## 最初の一歩

今取り組んでいる長めの文書(提案書・報告書・長文メールのいずれか)を1つ選び、「canvasを開いて〇〇のたたき台を書いて」と入力し、出てきた文章の1段落だけをハイライトして「ここだけ簡潔にして」と修正を頼んでみる。

## 関連トピック

- [ChatGPTのモデル一覧と使い分け](./chatgpt-model-lineup.md)
- [Claude(Anthropic)の基本](claude-basics.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [Microsoft Copilotの基本](microsoft-copilot-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: Canvasの仕組み(部分編集・ショートカットコマンド・バージョン履歴)、起動方法、対応プラン、GPT-5.5系モデルでのライティングブロック/コードブロックへの統合という2026年の変化、Claude Artifacts・Gemini Canvas・Microsoft Copilot Pagesとの比較表を整理
- **出典**: [Introducing canvas | OpenAI](https://openai.com/index/introducing-canvas/)、[What is the canvas feature in ChatGPT and how do I use it? | OpenAI Help Center](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it)、[モデルリリースノート | OpenAI Help Center](https://help.openai.com/ja-jp/articles/9624314-model-release-notes)、[ChatGPTでのライティングブロックとコードブロックの使用 | OpenAI Help Center](https://help.openai.com/ja-jp/articles/20001246-working-with-writing-blocks-and-code-blocks-in-chatgpt)、[What are artifacts and how do I use them? | Claude Help Center](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)、[Gemini Canvas — write, code, & create in one space with AI | Google](https://gemini.google/overview/canvas/)、[Get started with Microsoft 365 Copilot Pages | Microsoft Support](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-pages)
