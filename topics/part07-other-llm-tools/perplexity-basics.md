---
title: "Perplexityの基本"
part: 7
chapter: "第3章 検索特化型AI"
tags: [Perplexity, 検索特化型AI, 引用, ファクトチェック, 情報収集]
created: 2026-07-06
updated: 2026-07-06
---

# Perplexityの基本

## これは何か

昔ながらのGoogle検索は「10本の青いリンク」を並べるだけで、答えを組み立てるのは自分自身の作業になる。一方ChatGPTやGeminiのような汎用チャットAIは、質問すればすぐ答えをくれるが、根拠となる出典が明示されないことが多く、事実と異なる内容を自信満々に答える「幻覚(ハルシネーション、AIが事実でないことをもっともらしく生成してしまう現象)」のリスクが常に付きまとう。

Perplexityは、この2つの弱点を橋渡しする**「アンサーエンジン(answer engine)」**、すなわち検索特化型AI(ライブのWeb検索を行い、回答のたびに出典を明示するタイプの生成AI)である。質問を投げると、その場でWebを検索し、根拠となったページへのリンクを回答文中に番号付きで示してくれる。「検索結果を自分で読む手間」と「AIの回答を信じるしかない不安」の両方を、検証可能な形で減らすのがPerplexityの価値である。本ページは、この第3章「検索特化型AI」の最初のトピックとして、Perplexityを軸にこのカテゴリの考え方を整理する。

## 仕組み・背景

Perplexityの回答は、基本的に次の流れで作られる。

1. 質問(プロンプト)を受け取り、検索に適したクエリに分解する
2. リアルタイムでWebを検索し、複数のページを取得・要約する
3. 取得した内容をもとに回答文を生成し、根拠となったページを文中に `[1][2]` のような番号で引用として明示する
4. 回答の下に参照元サイトの一覧を表示する

この「毎回のトークン生成の裏で必ずWeb検索を行い、出典を紐付ける」設計は、いわゆるRAG(Retrieval-Augmented Generation、検索で得た外部情報を根拠に回答を生成する手法)を検索エンジンの形で実装したものと理解すると分かりやすい。無料版・標準検索の裏側では、Perplexity自身が開発した軽量モデル「Sonar」(Meta社のLlama 3.3をベースに、事実の正確さと読みやすさを重視して追加学習したモデル)が使われており、高速に動作する。

有料プランでは「Pro Search」というモードが使え、質問の複雑さに応じて複数回の検索・複数ステップの推論を行い、回答に使うAIモデル(GPT-5、Claude、Gemini、Grokなど主要モデルや、Perplexity自身のSonarファミリー)をユーザーが選択できる。さらに、通常のPro Searchより踏み込んで自律的に大量の情報源を巡回・統合する「Deep Research(Research)」モード、複数のスレッドや資料をまとめて共同作業できる「Spaces」、参照元を学術論文・SNS・動画などに絞り込む「Focus(フォーカス)」モードといった機能が用意されている。2025年にはChromiumベースのAIブラウザ「Comet」も投入され、ブラウザ内でページ要約やタスクの自動実行までPerplexityが担う方向に広がっている。

## 使いどころ・使い分け

### 検索特化型AI(アンサーエンジン)というカテゴリの位置づけ

| | 従来の検索エンジン(Google等) | 汎用チャットAI(ChatGPT・Geminiアプリ等) | 検索特化型AI(Perplexity等) |
|---|---|---|---|
| 出すもの | リンクの一覧 | 文章としての回答 | 出典付きの文章としての回答 |
| 根拠の見えやすさ | リンク先を自分で読めば分かる | 出典が示されないことが多い | 回答中に引用番号でリンクが埋め込まれる |
| 得意なこと | 網羅的な一覧性、専門検索(画像・地図等) | 発想の壁打ち、文章作成、コーディングなど汎用タスク | 「調べて根拠を示す」ことに特化した一問一答 |
| ハルシネーションへの耐性 | 該当しない(AIが生成しないため) | 相対的に低い(出典なしで断定しがち) | 出典が見えるため検証しやすい(ゼロにはならない) |

### Perplexity vs ChatGPT・Geminiの「Web検索」機能

ChatGPTやGeminiアプリにも検索連携(グラウンディング)機能があり、質問に応じて自動でWeb検索し出典を示すことができる。違いは「主戦場がどこか」にある。

| | Perplexity | ChatGPT・Geminiアプリの検索機能 |
|---|---|---|
| 主な用途 | 検索・調査そのものが本業 | チャット・文章作成・コーディングなどが本業で、検索はその一部機能 |
| 引用の一貫性 | 毎回の回答にほぼ確実に出典リンクが付く(平均5件程度と言われる) | 質問内容によって出典が付く/付かないがあり、ばらつきが大きい |
| 検索対象の絞り込み | Focusモードで学術論文・SNS・動画などに絞れる | 標準では絞り込みの選択肢が少ない |
| 発想・創作・コーディングへの強さ | 相対的に弱い(検索特化) | 強い(汎用モデルとしての作り込みが深い) |

判断の目安は、「事実確認・出典付きの調べもの」が目的ならPerplexity、「文章作成・企画立案・コーディングなど汎用タスク」が目的ならChatGPTやGeminiアプリ、という住み分けになる。

### Perplexity内での使い分け(Focus / Pro Search / Deep Research)

| 場面 | 向いている機能 |
|---|---|
| 単発の事実確認・簡単な調べもの | 標準検索(無料でも利用可) |
| 学術的な裏付けが欲しい | Focusモードの「学術(Academic)」 |
| SNS上の反応・トレンドを知りたい | Focusモードの「ソーシャル(Social)」 |
| やや複雑な質問で、モデルを選んで精度を上げたい | Pro Search |
| 競合比較・市場調査など、大量の情報源を横断してレポート化したい | Deep Research(Research)モード |
| 案件やプロジェクト単位で複数の調べものをまとめて管理したい | Spaces |

**Deep Researchについては、ChatGPT・Gemini・Claudeの同種機能との比較を[生成AIによる情報収集・リサーチの実務活用(Deep Research機能)](../part10-business-practice/ai-research-and-information-gathering.md)で詳しく整理しているので、そちらを参照。本ページではPerplexity単体の基本機能に絞る。**

### 向かない使い方

- 創作・ブレインストーミング(検索を経由しない自由な発想には不向き)
- コーディング・複雑なコード生成(汎用LLMの方が実装は得意)
- 社外秘資料だけを根拠にした質問(PerplexityはWeb検索が前提。社内資料限定ならNotebookLMなどが向く)

## 実務での使い方

### 想定シーン

- 競合他社の最新の料金・機能・ニュースを、出典付きでさっと確認する
- 自分やチームが書いた原稿・提案書の数値や主張を、実際に裏付けが取れるかファクトチェックする
- 市場調査・トレンド調査のとっかかりとして、複数の記事を横断的に要約させる
- レポートや記事に載せる出典リンクの候補を、テーマを渡して収集する

### 基本の操作手順(画面の場所)

1. ブラウザで perplexity.ai にアクセス(アカウント登録なしでも基本検索は利用可能。Pro機能を使うには登録が必要)
2. 検索窓の下にあるボタンで「Focus」を選び、必要に応じて対象を「Web」「学術」「SNS」などに絞り込む
3. 検索窓に質問を日本語で入力して送信すると、回答文中に `[1][2]` のような引用番号付きで回答が返り、回答の下に参照元サイトの一覧が表示される
4. 検索窓の下(または「Pro Search」トグル)から使用するAIモデルを選べる(有料プランの場合。「Best」を選ぶと質問内容に応じて自動選択される)
5. さらに踏み込んで調査したい場合は、モード切り替えから「Research」(Deep Research)を選んで質問を送信すると、数分かけて数十〜100件超の情報源を横断した長文レポートが生成される
6. 複数の調べものを1つのプロジェクトとしてまとめたい場合は、左側メニューの「Spaces」から新規スペースを作成し、資料のアップロードやカスタム指示の設定、関連スレッドの整理ができる

### コピペで使える質問例(ファクトチェック)

```
以下は自社レポートに書いた文章です。数値や固有名詞に誤りがないか、
出典付きで確認してください。裏付けが取れない主張には「未確認」と明記してください。

「国内の会議室予約SaaS市場は2025年時点で約120億円規模とされ、
主要3社が合計シェアの6割を占めている」
```

### コピペで使える質問例(競合比較の下調べ)

```
会議室予約SaaSの国内主要5社について、以下を出典付きで整理してください。
1. 各社の料金プラン(初期費用・月額)
2. 直近1年の新機能リリース・価格改定
3. 導入企業のレビューで頻出する不満点
表形式で、各項目に参照元URLを明記してください。
```

### ツール横断の対応付け

| 概念 | Perplexity | ChatGPT | Gemini |
|---|---|---|---|
| 出典付きWeb検索 | 標準検索(常時) | 「検索」トグル・質問内容による自動判定 | 「Web検索でグラウンディング」機能 |
| 本格リサーチモード | Deep Research(Research) | deep research | Deep Research |
| 検索対象の絞り込み | Focusモード(Web/学術/SNS等) | 明確な同等機能は薄い | 明確な同等機能は薄い |
| プロジェクト単位の整理 | Spaces | プロジェクト機能・GPTs | Gem・ノートブック機能 |
| 専用ブラウザ | Comet(Chromiumベース) | Atlas | Chrome統合(拡張機能等) |

### 料金プラン(2026年7月時点の目安)

| プラン | 料金 | 主な内容 |
|---|---|---|
| Free | ¥0 | 標準検索は無制限。Pro Search(高度な検索)は1日5回程度までに制限。フロンティアモデルの選択はできない |
| Pro | 月額$20(年払いで$200、月あたり約$16.67) | Pro Searchが無制限、Deep Researchの利用、GPT-5・Claude・Geminiなど主要モデルの選択、Labs(レポート・表・簡易Webアプリの自動生成)などが解放 |
| Max | 月額$200(年払いで$2,000) | Proの全機能に加え、複数モデルを組み合わせて自律的に作業する上位のエージェント機能や、より高い利用上限を提供。AIをコア業務基盤として使うプロフェッショナル向け |
| Enterprise Pro | 1シートあたり月額$40(年払い$400) | Proの機能に加え、SSO・SCIM・監査ログなどチーム管理・セキュリティ機能を追加 |
| Enterprise Max | 1シートあたり月額$325(年払い$3,250) | Enterprise Proの機能に、より高い利用上限と優先アクセスを追加した最上位プラン |
| Education Pro | 月額$10程度 | 大学等に在籍する学生・教職員向けの割引プラン(SheerIDなどでの本人確認が必要) |

料金・上限は変更が非常に頻繁なため、契約前には必ず[Perplexity公式の料金ページ](https://www.perplexity.ai/pro)、[Perplexity Enterprise料金ページ](https://www.perplexity.ai/enterprise/pricing)、[Perplexityヘルプセンター「どのプランが自分に合っているか」](https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you)で最新の数値を確認すること。

## 注意点・よくある誤解

- **「出典が付いている」=「正しい」ではない**: Perplexityは根拠となったページを示すが、そのページの内容自体が間違っている場合や、AIがページの内容を誤読・要約しすぎて原文の意味を変えてしまう場合がある。重要な数値・固有名詞は、引用リンクを実際に開いて元の文脈と一致するか確認する
- **参照元の質にばらつきがある**: 標準検索の引用元にはSNS(Reddit等)やまとめサイトなど、一次情報とは言えないサイトが混じることがある。ビジネス文書に使う場合は、Focusモードで学術・公式サイトなどに絞る、または引用元のドメインを目視で確認する習慣を持つ
- **創作・コーディングには向かない**: 検索特化型のため、アイデア発想の自由度やコード生成の精度はChatGPT・Gemini・Claudeなど汎用LLMに劣る場面が多い。用途によってツールを切り替える
- **無料版の上限に注意**: 無料版はPro Search(高度な検索)が1日数回程度に制限される。頻繁に高度な検索を使う業務利用ではPro以上の契約が前提になる
- **Max・Enterprise Maxは高額**: Max($200/月)やEnterprise Max(1シート$325/月)は個人の一般的な利用には過剰な場合が多い。まずはPro($20/月)で十分か検討し、Deep Researchや上位モデルの利用頻度が業務上どれだけ必要かで判断する
- **社外秘情報の扱い**: PerplexityはWeb検索が前提の設計のため、社内文書のみを根拠にした質問には向かない。Enterprise版ではデータの取り扱い・学習利用に関する契約条件が個人向けと異なるため、業務利用前に確認する

## 最初の一歩

最近自分が書いた資料やSNSで見かけた数値の主張を1つ選び、Perplexityの検索窓に貼って「出典付きで裏付けを確認して」と聞いてみる。返ってきた回答の引用リンクを実際に1つ開き、記載内容と元記事が一致しているかを確認する。

## 関連トピック

- [生成AIによる情報収集・リサーチの実務活用(Deep Research機能)](../part10-business-practice/ai-research-and-information-gathering.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [NotebookLMの基本](notebooklm-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: 検索特化型AI(アンサーエンジン)というカテゴリの位置づけ、Perplexityの仕組み(Sonarモデル・引用付き回答・Pro Search・Focus・Deep Research・Spaces・Cometブラウザ)、従来検索/汎用チャットAIとの使い分け、基本操作手順、ファクトチェック・競合比較のプロンプト例、料金プラン(Free/Pro/Max/Enterprise Pro/Enterprise Max/Education Pro)、注意点を整理
- **出典**: [Perplexity Pro | Perplexity](https://www.perplexity.ai/pro)、[Perplexity Enterprise Pricing](https://www.perplexity.ai/enterprise/pricing)、[Which Perplexity Subscription Plan is right for you? | Perplexity Help Center](https://www.perplexity.ai/help-center/en/articles/11187416-which-perplexity-subscription-plan-is-right-for-you)、[Perplexity Max | Perplexity Help Center](https://www.perplexity.ai/help-center/en/articles/11680686-perplexity-max)、[Perplexity Pricing in 2026 for Individuals, Orgs & Developers | Finout](https://www.finout.io/blog/perplexity-pricing-in-2026)、[Perplexity Pricing 2026: Pro $20/mo, Enterprise $40/user & Sonar API Costs | ScreenApp](https://screenapp.io/blog/perplexity-pricing)、[Perplexity Pricing 2026: Free, Pro, Max, Enterprise & API | ToolColumn](https://www.toolcolumn.com/pricing/perplexity-pricing)、[Introducing Perplexity Deep Research](https://www.perplexity.ai/hub/blog/introducing-perplexity-deep-research)、[Introducing Perplexity Labs](https://www.perplexity.ai/hub/blog/introducing-perplexity-labs)、[Perplexity's new tool can generate spreadsheets, dashboards, and more | TechCrunch](https://techcrunch.com/2025/05/29/perplexitys-new-tool-can-generate-spreadsheets-dashboards-and-more/)、[Meet New Sonar | Perplexity](https://www.perplexity.ai/hub/blog/meet-new-sonar)、[All Perplexity models available in 2025 | Datastudios](https://www.datastudios.org/post/all-perplexity-models-available-in-2025-complete-list-with-sonar-family-gpt-5-claude-gemini-and)、[Comet (browser) - Wikipedia](https://en.wikipedia.org/wiki/Comet_(browser))、[A Complete How-To Guide to Perplexity AI | Learn Prompting](https://learnprompting.org/blog/guide-perplexity)、[Perplexity Comet とは？AIブラウザの新機能、料金プラン、使い方、ChatGPT Atlasとの比較 | アイスマイリー](https://aismiley.co.jp/ai_news/perplexity-comet-chatgpt-atlas/)
- **注記**: perplexity.ai配下のヘルプセンター・公式ブログの一部は本セッションから直接アクセスできず(403エラー)、検索エンジンのスニペットおよび複数の第三者記事の突き合わせに基づく記述を含む。プラン名・料金・利用上限は変更が非常に頻繁なため目安とし、契約・運用前には必ず公式サイトで最新値を確認すること
