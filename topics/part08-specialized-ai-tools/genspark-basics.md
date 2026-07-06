---
title: "GenSparkの基本"
part: 8
chapter: 第1章 検索・リサーチ特化
tags: [GenSpark, 検索特化型AI, AIエージェント, スライド生成, リサーチ]
created: 2026-07-06
updated: 2026-07-06
---

# GenSparkの基本

## これは何か

「競合を調べて、そのままスライドや表にまとめてほしい」——調べものと資料化を別々のツールで往復する手間をなくしたい、というニーズに応えるのがGenSpark(ジェンスパーク)である。単一のAIモデルに質問を投げるのではなく、**複数のLLM(大規模言語モデル)を役割分担させて1つのタスクをこなす「Mixture-of-Agents(混合エージェント)」というアーキテクチャ**を採用したAI検索・AIエージェントのプラットフォームで、検索結果の要約にとどまらず、スライド・表計算・資料の自動生成や、電話代行のような自律的なタスク実行まで扱えるのが特徴である。2024年6月にAI検索エンジンとしてスタートし、2025年4月には自律実行型の「Super Agent」を軸にしたAIワークスペースへと軸足を移している。

## 仕組み・背景

GenSparkは、Baidu(百度)出身のEric Jing・Kay Zhuらが2023年に創業した米MainFunc社が開発している。2024年6月の公開当初は、検索結果をリンク一覧ではなく質問ごとにリアルタイム生成する専用ページ「Sparkpage」として提示するAI検索エンジンだった。

その裏側にあるのが「Mixture-of-Agents」という設計思想である。1つの質問に対して単一のモデルが最初から最後まで答えるのではなく、まず司令塔役のモデルがユーザーの目的をサブタスクに分解し、OpenAI・Anthropic・Googleなど複数社のLLM(現在は9種類程度のモデルと言われる)の中から、そのサブタスクに最も適したモデルへ振り分けて処理させ、最後に結果を統合する。「検索」「要約」「表への整形」「スライドのデザイン」といった工程ごとに得意なモデルを使い分けることで、単一モデルよりも質の高い成果物を作ろうという発想である。

2025年4月には、この仕組みを土台にした自律実行型AIエージェント「Super Agent」を投入した。ユーザーが「◯◯を調べてスライドにまとめて」のように工程をまたぐ指示を出すと、リサーチ・情報整理・資料化までを人手を介さずに実行する。同時期にOpenAIのRealtime API(音声対話をリアルタイムに処理する仕組み)を使って実際に電話をかけて予約や問い合わせを代行する「Call For Me」機能も話題になった。2026年には法人向けプラン「Genspark for Business」も展開しており、月間アクティブユーザー数は200万人超、有料契約は10万シート規模、評価額は2026年6月時点で26億ドルに達したと報じられている。

## 使いどころ・使い分け

### 検索特化型AI・AIエージェント同士の比較

| | GenSpark | Perplexity | ChatGPT(検索・Agent機能) | Gemini(Web検索連携) |
|---|---|---|---|---|
| 出すもの | 質問ごとに生成される専用ページ(Sparkpage)、スライド・表・資料などの成果物 | 出典付きの文章としての回答 | 文章としての回答、Agent機能で一部自動化 | 文章としての回答 |
| 強み | 複数モデルの使い分けによる資料化(スライド・表・ドキュメント)、自律的なマルチステップ実行(Super Agent) | 出典の明示・引用の一貫性、事実確認のスピード | 汎用対話力・コーディング・エコシステムの広さ | Google系サービス(Workspace等)との連携 |
| 弱み | 出典表示や事実検証のわかりやすさはPerplexityに劣るとされる、日本語UIは未整備 | 資料の自動生成機能は薄い(Labsで一部対応) | 検索の一貫性にばらつき | 検索特化としての作り込みは薄い |
| 料金モデル | クレジット制(機能ごとに消費量が異なる) | ほぼ定額制(Pro Search回数はプランで制限) | 定額制 | 定額制(Google One AI Premium等) |
| 向いている用途 | 「調べて、資料の形にする」までを一気に終わらせたい業務(競合調査→提案資料、リサーチ→スプレッドシート化など) | 「事実確認・出典付きの調べもの」に特化した一問一答 | 汎用対話・文章作成・コーディング | Google系ツールとの統合作業 |

判断の目安は、**「調べた内容をそのまま資料の形(スライド・表・ドキュメント)にまで仕上げたい」ならGenSpark**、**「出典を明示した事実確認をすばやく行いたい」ならPerplexity**、**「汎用的な対話・創作・コーディング」ならChatGPTやGemini**という住み分けになる。検索特化型AIの位置づけ全般については[Perplexityの基本](./perplexity-basics.md)も参照。

### 向かない使い方

- 出典の一次情報を1件ずつ丁寧に検証したい場合(Perplexityの方が引用の一貫性が高いとされる)
- 機密情報・個人情報を扱う調べもの(入力内容がサービス改善に利用される場合があるとされ、社外秘情報の投入は避けるべき)
- 日本語での厳密な用語統一が必要な資料(訳揺れ・カタカナ表記のばらつきが生じることがある)

## 実務での使い方

### 主な機能

- **AI検索・Sparkpage**: 質問を入力すると、リンク一覧ではなく質問内容に応じて構成されたページ(Sparkpage)がその場で生成される
- **Super Agent**: 「競合他社を調べてスライドにまとめて」のような複数工程を含む指示を渡すと、リサーチ・整理・資料化までを自律的に実行する
- **AI Slides**: プロンプトからスライド資料を自動生成する機能。テーマやキーワードを入力するだけで構成案・デザインまで作成する
- **AI Sheets**: 裏側でリサーチを行い、その結果を表形式(スプレッドシート)にまとめる機能
- **AI Docs**: 調査結果や指示内容をもとに文書・レポートを生成する機能
- **Call For Me**: 音声対話AIが実際に電話をかけ、予約変更や問い合わせなどの用件をユーザーに代わってこなす機能
- **AI Meeting Notes・AI Pods・AI Developer・Chrome拡張機能・Teams(チーム利用)など**: 議事録作成、ポッドキャスト風音声コンテンツ生成、簡易開発支援、ブラウザ連携、複数人での共同利用に対応する機能群も用意されている

### 基本の操作手順(画面の場所)

1. ブラウザでgenspark.aiにアクセスし、アカウントを登録する(無料でも基本機能は利用可能)
2. トップ画面の入力欄に日本語で質問や指示を入力する。UIは英語だが、日本語で入力すれば自動的に日本語で回答が返る
3. 単純な調べものであれば、そのままSparkpage形式の回答が生成される
4. スライド・表・資料を作りたい場合は、画面上部やサイドメニューから「AI Slides」「AI Sheets」「AI Docs」などの機能を選び、テーマや構成の指示を入力する
5. 複数工程をまとめて任せたい場合は「Super Agent」を選び、「◯◯について調べて△△の形式でまとめて」のように最終成果物の形まで指定して指示を出す

### コピペで使える指示例(競合調査→スライド化)

```
会議室予約SaaSの国内主要5社について、料金プラン・直近の新機能・
導入企業の口コミで多い不満点を調査し、
社内検討用のスライド資料(10枚程度)としてまとめてください。
各スライドの根拠となった情報源も末尾に一覧で示してください。
```

### ツール横断の対応付け

| 概念 | GenSpark | Perplexity | ChatGPT |
|---|---|---|---|
| 出典付きAI検索 | AI検索・Sparkpage | 標準検索 | 「検索」機能 |
| 自律的なマルチステップ実行 | Super Agent | Deep Research(調査に特化) | Agent機能・deep research |
| スライド自動生成 | AI Slides | 標準では非対応(Labsで一部生成物に対応) | 標準では非対応(GPTsやCanvasで部分的に代替) |
| 表・スプレッドシート自動生成 | AI Sheets | 標準では非対応 | 標準では非対応 |
| 音声での用件代行 | Call For Me | 非搭載 | 非搭載(音声対話機能はあるが電話代行は非搭載) |

### 料金プラン(2026年7月時点の目安)

| プラン | 料金 | クレジット・主な内容 |
|---|---|---|
| Free | ¥0(クレジットカード登録不要) | 1日100クレジット、ストレージ約1GB。基本的なAI検索・Sparkpageは実務でも使える水準とされる |
| Plus | 月額$24.99(年払いで月$19.99相当) | 月10,000クレジット、ストレージ50GB、優先的に上位モデルへアクセス可能 |
| Pro | 月額$249.99(年払いで月$199.99相当) | 月125,000クレジット(Plusの12.5倍)、ストレージ1TB |
| Business(チーム向け) | 1シートあたり月額$30程度 | 組織向けの契約プラン。2025年11月開始で、2026年時点で1,000社超が利用と報じられている |

AIチャットや画像生成は2026年12月31日まではクレジット消費ゼロとするキャンペーンが実施されているなど、料金・クレジット消費のルールは変更が頻繁である。契約前には必ず[GenSpark公式の料金ページ](https://www.genspark.ai/pricing)、[GenSparkヘルプセンター(会員プラン)](https://www.genspark.ai/helpcenter?doc=general_Membership_Plans)で最新の数値を確認すること。

## 注意点・よくある誤解

- **情報の正確性は必ず出典を確認する**: GenSparkはリサーチ結果を要約・資料化する能力に優れる一方、Perplexityほど引用の一貫性や出典の見えやすさが徹底されているわけではないとされる。重要な数値・固有名詞を含む資料は、生成後に一次情報へさかのぼって裏取りする
- **機能・料金の変更が非常に頻繁**: 2023年創業とまだ新しいツールで、2024年6月のAI検索エンジンとしての公開から2025年4月のSuper Agent軸への転換まで短期間で製品の重心が変わってきた経緯がある。料金プラン・クレジット消費ルール・搭載モデルも変更が多いため、業務で使う際は都度公式情報を確認する
- **日本語UIは未整備**: 画面(UI)自体は英語のままで、入力・出力を日本語で行う形になる。専門用語やカタカナ表記の訳揺れが生じることがあるため、社外向け資料にそのまま使う場合は表記統一を人手でチェックする
- **入力内容の取り扱いに注意**: 入力した内容がサービス改善(AIの学習等)に利用される場合があるとされ、個人が特定される情報や社外秘の内容の入力は避ける
- **日本での知名度はまだ発展途上**: 米国では評価額26億ドル(2026年6月時点)・月間アクティブユーザー200万人超と急成長しているが、日本国内での利用実績・レビューの蓄積はPerplexityやChatGPTに比べるとまだ少ない。組織導入の際は、まず個人アカウントの無料枠で使用感を確認してから展開範囲を広げるのが無難

## 最初の一歩

genspark.aiに無料登録し、直近で調べたい競合や市場のテーマを1つ選んで「◯◯について調べてスライドにまとめて」とSuper Agentに指示してみる。出てきたスライドの根拠情報を1つ選んで、実際の一次情報と内容が一致しているかを確認する。

## 関連トピック

- [Perplexityの基本](./perplexity-basics.md)
- [生成AIによる情報収集・リサーチの実務活用(Deep Research機能)](../part11-business-practice/ai-research-and-information-gathering.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: GenSparkの概要(Mixture-of-Agentsアーキテクチャ、Sparkpage、Super Agent、Call For Me等の主要機能)、Perplexity・ChatGPT・Geminiとの比較表、料金プラン(Free/Plus/Pro/Business)、日本語対応状況、注意点を整理
- **出典**: [Genspark Pricing Page(公式)](https://www.genspark.ai/pricing)、[Genspark Membership Plans(公式ヘルプセンター)](https://www.genspark.ai/helpcenter?doc=general_Membership_Plans)、[Genspark AI Pricing 2026: Free, Plus & Pro Plans Compared | Felloai](https://felloai.com/genspark-ai-pricing/)、[Genspark（ジェンスパーク）とは？AIエージェント機能の使い方・料金、ChatGPTとの違い | mieru-ca](https://mieru-ca.com/ai-seo/genspark/)、[Genspark（ジェンスパーク）の使い方とは？ | アイスマイリー](https://aismiley.co.jp/ai_news/what-is-genspark/)、[Genspark AIとは？Perplexityとの違いや便利機能を解説 | WEEL](https://weel.co.jp/media/innovator/genspark-ai/)、[Genspark - AI Wiki](https://aiwiki.ai/wiki/genspark)、[Genspark ships no-code personal agents with GPT-4.1 and OpenAI Realtime API | OpenAI](https://openai.com/index/genspark/)、[Hands-On Guide to Genspark: Super Agent, Tools, Use Cases | whytryai](https://www.whytryai.com/p/genspark-beginner-guide)、[How Genspark Went From $0 to $2.6 Billion in Under Two Years | TIGI](https://theimpactfulglobalindian.com/articles/genspark-s-2-6-billion-valuation-shows-the-ai-funding-frenzy-isn-t-slowing)、[Genspark.ai Extends Series B to $485M, at $2.6 Billion Valuation | FinSMEs](https://www.finsmes.com/2026/06/genspark-ai-extends-series-b-to-485m-at-2-6-billion-valuation.html)、[Genspark Expands Its "AI Workspace" With OpenAI, Anthropic, and Microsoft | Tech Times](https://www.techtimes.com/articles/319240/20260629/genspark-expands-its-ai-workspace-openai-anthropic-microsoft.htm)、[GenSparkは日本語対応しているの？設定方法と利用 | ai-dounyu](https://www.ai-dounyu.com/articles/genspark-japanese)
- **注記**: genspark.ai公式サイト・アイスマイリー・WEEL等の一部ページは本セッションから直接アクセスできず(403エラー)、検索エンジンのスニペットおよび複数の第三者記事の突き合わせに基づく記述を含む。GenSparkはサービスの重心・料金体系の変更が非常に頻繁なため、業務利用・記事化の前には必ず公式サイトで最新情報を確認すること
