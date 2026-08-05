---
title: "GenSparkの基本"
part: 8
chapter: 第1章 検索・リサーチ特化
tags: [GenSpark, 検索特化型AI, AIエージェント, スライド生成, リサーチ]
created: 2026-07-06
updated: 2026-07-23
---

# GenSparkの基本

## これは何か

「競合を調べて、そのままスライドや表にまとめてほしい」——調べものと資料化を別々のツールで往復する手間をなくしたい、というニーズに応えるのがGenSpark(ジェンスパーク)である。単一のAIモデルに質問を投げるのではなく、**複数のLLM(大規模言語モデル)を役割分担させて1つのタスクをこなす「Mixture-of-Agents(混合エージェント)」というアーキテクチャ**を採用したAI検索・AIエージェントのプラットフォームで、検索結果の要約にとどまらず、スライド・表計算・資料の自動生成、メールやチームチャットの代行、自律的なタスク実行まで扱えるのが特徴である。2024年6月にAI検索エンジンとして出発し、2025年4月の自律実行型「Super Agent」投入を経て、2026年7月時点では、仕事に関する情報を継続的に記憶する「SecondBrain」を核とした統合ワークスペース「Genspark AI Workspace」(2026年7月21日公開の最新版はバージョン6.0)へと発展している。

## 仕組み・背景

GenSparkは、Baidu(百度)出身のEric Jing・Kay Zhuらが2023年に創業した米MainFunc社が開発している。2024年6月の公開当初は、検索結果をリンク一覧ではなく質問ごとにリアルタイム生成する専用ページ「Sparkpage」として提示するAI検索エンジンだった。

その裏側にあるのが「Mixture-of-Agents」という設計思想である。1つの質問に対して単一のモデルが最初から最後まで答えるのではなく、まず司令塔役のモデルがユーザーの目的をサブタスクに分解し、OpenAI・Anthropic・Googleなど複数社のLLMの中から、そのサブタスクに最も適したモデルへ振り分けて処理させ、最後に結果を統合する。「検索」「要約」「表への整形」「スライドのデザイン」といった工程ごとに得意なモデルを使い分けることで、単一モデルよりも質の高い成果物を作ろうという発想である。

2025年4月には、この仕組みを土台にした自律実行型AIエージェント「Super Agent」を投入した。以降、GenSparkは「AI Workspace」と称する統合製品を数か月おきに大型改訂しており、進化のペースが非常に速い。

- **2025年11月**: 法人向け「Genspark for Business」を開始
- **2026年3月**: 「AI Workspace 3.0」を公開。ユーザーに代わって複数ステップの作業をこなす“最初のAI社員”と位置づける「Genspark Claw」を投入し、シリーズBを3.85億ドル・評価額約16億ドルに拡大
- **2026年4月**: 「AI Workspace 4.0」で「Claw for Desktop」(ローカルのファイルを直接扱えるデスクトップ版)とMicrosoft Office連携を追加
- **2026年6月**: シリーズBをさらに1億ドル追加した4.85億ドル(累計調達額は約6.45億ドル)に拡大し、評価額は26億ドルに到達
- **2026年7月21日**: 「AI Workspace 6.0」を公開。仕事に関する情報(メール・会議メモ・通話・文書・CRMなど)を横断的に記憶し続ける「SecondBrain」、それを補うハードウェア端末「SecondBrain Note」(会話を自動で録音・記憶させる名刺サイズのデバイス、価格199ドル・導入記念価格179ドル)、人とAIエージェントが同じチャット空間で共同作業する「GenTeam」、ユーザーの文体や人間関係を学習するメールクライアント「GenMail」、プロンプト一つで画像・プロトタイプ・ブランド資産を作る「AI Design」、ノーコードで業務アプリ(簡易CRM・ダッシュボード等)を組み立てられる「AgentBase」を一挙に追加した

この結果、年換算売上(ARR)は2025年の約5,000万ドルから2026年には2.5億ドルへ急拡大し、法人契約数は7,000社超、月間アクティブユーザー数は200万人超と報じられている。競合ひしめくAI検索・エージェント市場で短期間に規模を伸ばしている一方、製品の重心(検索→エージェント→記憶・コラボレーション基盤)が数か月単位で変わり続けている点は、業務導入の際に念頭に置く必要がある。

## 使いどころ・使い分け

### 検索特化型AI・AIエージェント同士の比較

| | GenSpark | Perplexity | NotebookLM | ChatGPT(検索・Agent機能) |
|---|---|---|---|---|
| 出すもの | 質問ごとに生成される専用ページ(Sparkpage)、スライド・表・資料・アプリなどの成果物 | 出典付きの文章としての回答、Labsによるレポート・表生成 | アップロードした資料に根拠づけられた要約・Q&A・音声解説 | 文章としての回答、Agent機能で一部自動化 |
| 強み | 複数モデルの使い分けによる資料化(スライド・表・ドキュメント・簡易アプリ)、自律的なマルチステップ実行(Super Agent・Claw)、SecondBrainによる継続的な文脈記憶 | 出典の明示・引用の一貫性、Pro/Maxでは複数モデルを横断比較するModel Council機能もあり | 「自社の資料だけ」に根拠を限定できるため誤情報の混入が少ない、出典箇所への逆リンクが明確 | 汎用対話力・コーディング・エコシステムの広さ |
| 弱み | 出典表示や事実検証のわかりやすさはPerplexityに劣るとされる、日本語UIは未整備、機能変化が速く操作を覚え直す頻度が高い | 資料の自動生成機能はLabsで補われつつあるがGenSparkほど多彩ではない | 調べもの自体(未知の情報の探索)には向かない、自分で資料を用意する手間がある | 検索の一貫性にばらつき |
| 料金モデル | クレジット制(機能ごとに消費量が異なる) | ほぼ定額制(Free枠は検索回数に制限、Pro/Maxは主要機能が無制限) | 定額制(Google One AI Premium等に内包) | 定額制 |
| 向いている用途 | 「調べて、資料の形にする」までを一気に終わらせたい業務(競合調査→提案資料、リサーチ→スプレッドシート化など) | 「事実確認・出典付きの調べもの」に特化した一問一答 | 社内資料・議事録・論文など「手元にある資料」の理解・要約 | 汎用対話・文章作成・コーディング |

判断の目安は、**「調べた内容をそのまま資料の形(スライド・表・ドキュメント・簡易アプリ)にまで仕上げたい」ならGenSpark**、**「出典を明示した事実確認をすばやく行いたい」ならPerplexity**、**「手元にある自社資料だけを根拠にした要約・Q&Aをしたい」ならNotebookLM**、**「汎用的な対話・創作・コーディング」ならChatGPT**という住み分けになる。検索特化型AIの位置づけ全般については[Perplexityの基本](./perplexity-basics.md)・[NotebookLMの基本](./notebooklm-basics.md)も参照。

### 向かない使い方

- 出典の一次情報を1件ずつ丁寧に検証したい場合(Perplexityの方が引用の一貫性が高いとされる)
- 自社の契約書・議事録など「手元の資料の中だけ」で回答してほしい場合(NotebookLMのようにアップロード資料に根拠を限定するタイプの方が誤情報混入のリスクが低い)
- 機密情報・個人情報を扱う調べもの(入力内容がサービス改善に利用される場合があるとされ、社外秘情報の投入は避けるべき。特にSecondBrainはメール・会議・通話内容まで継続的に記憶する機能のため、扱う情報の機密度には一段の注意が要る)
- 日本語での厳密な用語統一が必要な資料(訳揺れ・カタカナ表記のばらつきが生じることがある)

## 実務での使い方

### 主な機能

- **AI検索・Sparkpage**: 質問を入力すると、リンク一覧ではなく質問内容に応じて構成されたページ(Sparkpage)がその場で生成される
- **Super Agent**: 「競合他社を調べてスライドにまとめて」のような複数工程を含む指示を渡すと、リサーチ・整理・資料化までを自律的に実行する
- **Genspark Claw / Claw for Desktop**: “AI社員”と位置づけられる自律エージェント。クラウド上の専用マシン(Genspark Cloud Computer)やデスクトップ版を通じて、ブラウザ操作・ローカルファイルの整理・複数アプリをまたぐ作業を代行する
- **AI Slides / AI Sheets / AI Docs**: プロンプトからスライド・表計算・文書を自動生成する機能。テーマやキーワードを入力するだけで構成案・デザインまで作成する
- **AI Design**: プロンプト一つで画像・プロトタイプ・ブランド素材(ロゴ・バナー等)を生成する機能(Workspace 6.0で追加)
- **AgentBase**: コーディングなしで簡易CRMやダッシュボードなど業務用の小規模アプリを組み立てる機能(Workspace 6.0で追加)
- **SecondBrain / SecondBrain Note**: メール・会議メモ・通話・文書・CRMなど仕事に関する情報を横断的に記憶し続ける機能。専用ハードウェア「SecondBrain Note」(199ドル、名刺サイズ、最大35時間録音)を使うと対面の会話も自動で記録・記憶させられる(Workspace 6.0で追加。個人情報・第三者との会話を記録する性質上、利用前に社内ルールの確認が必須)
- **GenTeam / GenMail**: GenTeamは人とAIエージェントが同じチャット空間で共同作業するコラボレーション機能、GenMailはユーザーの文体・人間関係・優先度を学習するメールクライアント(いずれもWorkspace 6.0で追加)
- **Custom Super Agent / Super Agent Store**: プロンプト一つで自分専用のエージェントを作成し、社内外で再利用・共有・公開できる機能(2026年1〜3月頃に追加)
- **Genspark AIブラウザ**: 閲覧中のあらゆるWebページ上でSuper Agentが動作するブラウザアプリ(macOS版が先行、Windows版は展開中)。価格比較・YouTube要約・自動巡回(Autopilotモード)などに対応
- **Call For Me・AI Meeting Notes・AI Pods・Chrome拡張機能など**: 電話代行、議事録作成、ポッドキャスト風音声コンテンツ生成、ブラウザ連携といった従来からの機能群も引き続き提供されている

### 基本の操作手順(画面の場所)

1. ブラウザでgenspark.aiにアクセスし、アカウントを登録する(無料でも基本機能は利用可能)
2. トップ画面の入力欄に日本語で質問や指示を入力する。UIは英語だが、日本語で入力すれば自動的に日本語で回答が返る
3. 単純な調べものであれば、そのままSparkpage形式の回答が生成される
4. スライド・表・資料を作りたい場合は、画面上部やサイドメニューから「AI Slides」「AI Sheets」「AI Docs」などの機能を選び、テーマや構成の指示を入力する
5. 複数工程をまとめて任せたい場合は「Super Agent」を選び、「◯◯について調べて△△の形式でまとめて」のように最終成果物の形まで指定して指示を出す
6. メール整理やチームでの共同作業まで任せたい場合は、サイドメニューの「GenMail」「GenTeam」を有効化する(いずれもメール・チャットへのアクセス権限付与が必要なため、社内の情報取り扱いルールを事前に確認する)

### コピペで使える指示例(競合調査→スライド化)

```
会議室予約SaaSの国内主要5社について、料金プラン・直近の新機能・
導入企業の口コミで多い不満点を調査し、
社内検討用のスライド資料(10枚程度)としてまとめてください。
各スライドの根拠となった情報源も末尾に一覧で示してください。
```

### ツール横断の対応付け

| 概念 | GenSpark | Perplexity | NotebookLM | ChatGPT |
|---|---|---|---|---|
| 出典付きAI検索 | AI検索・Sparkpage | 標準検索 | 資料に基づくQ&A(Webは検索しない) | 「検索」機能 |
| 自律的なマルチステップ実行 | Super Agent・Claw | Deep Research(調査に特化) | 非搭載 | Agent機能・deep research |
| スライド自動生成 | AI Slides | 標準では非対応(Labsで一部生成物に対応) | 非対応 | 標準では非対応(GPTsやCanvasで部分的に代替) |
| 表・スプレッドシート自動生成 | AI Sheets | Labsで一部対応 | 非対応 | 標準では非対応 |
| 継続的な文脈・記憶の蓄積 | SecondBrain | 非搭載 | ノートブック単位での資料保持 | Memory機能(会話履歴中心) |
| 音声での用件代行 | Call For Me | 非搭載 | 非搭載 | 非搭載(音声対話機能はあるが電話代行は非搭載) |

### 料金プラン(2026年7月時点の目安)

| プラン | 料金 | クレジット・主な内容 |
|---|---|---|
| Free | ¥0(クレジットカード登録不要) | 1日100〜200クレジット、ストレージ約1GB。基本的なAI検索・Sparkpageは実務でも使える水準とされる。Genspark AIブラウザ・Custom Super Agentなど一部機能は無料でも利用可 |
| Plus | 月額$24.99(年払いで月$19.99相当) | 月10,000クレジット、ストレージ50GB。上位モデル(GPT系・Claude系・Gemini系など)へのAIチャット、画像生成が2026年12月31日までクレジット消費ゼロになるキャンペーン中 |
| Pro | 月額$249.99(年払いで月$199.99相当) | 月125,000クレジット(Plusの12.5倍)、ストレージ1TB |
| Team(法人向け) | 1シートあたり月額$30程度(2〜150シート) | シートあたり月12,000クレジット。管理者向け機能・SSO/SAML・一括請求に対応する唯一のプラン |
| Enterprise(法人向け) | 個別見積もり | 営業担当への問い合わせが必要。大規模組織向けにカスタムの契約条件を提供 |

上記の「AIチャット・画像生成がクレジット消費ゼロ」というPlus/Pro向けの優遇や、Team/Enterpriseの価格は2026年12月31日までの期間限定条件を含むとされる。契約前には必ず[GenSpark公式の料金ページ](https://www.genspark.ai/pricing)、[GenSparkヘルプセンター(会員プラン)](https://www.genspark.ai/helpcenter/membership-plans)、[Genspark for Business](https://www.genspark.ai/business)で最新の数値を確認すること。

## 注意点・よくある誤解

- **情報の正確性は必ず出典を確認する**: GenSparkはリサーチ結果を要約・資料化する能力に優れる一方、Perplexityほど引用の一貫性や出典の見えやすさが徹底されているわけではないとされる。重要な数値・固有名詞を含む資料は、生成後に一次情報へさかのぼって裏取りする
- **機能・料金の変更が非常に頻繁**: 2023年創業とまだ新しいツールで、2024年6月のAI検索エンジンとしての公開から、2025年4月のSuper Agent、2026年3〜7月だけでもAI Workspace 3.0→4.0→6.0と、数か月おきに製品の重心が変わってきた経緯がある。料金プラン・クレジット消費ルール・搭載モデルも変更が多いため、業務で使う際は都度公式情報を確認する
- **SecondBrainなど「常時記憶」系機能の情報管理には特に注意**: 2026年7月に追加されたSecondBrainは、メール・会議・通話内容などを横断的かつ継続的に記憶する機能であり、専用ハードウェア「SecondBrain Note」を使うと対面の会話まで自動録音・記憶される。第三者との会話が本人の同意なく記録・保存される懸念があるため、導入前に自社の情報管理ポリシーや録音に関する法令(録音同意の要否など)を確認する
- **日本語UIは未整備**: 画面(UI)自体は英語のままで、入力・出力を日本語で行う形になる。専門用語やカタカナ表記の訳揺れ、長文・専門的内容での精度低下が生じることがあるため、社外向け資料にそのまま使う場合は表記・内容を人手でチェックする
- **入力内容の取り扱いに注意**: 入力した内容がサービス改善(AIの学習等)に利用される場合があるとされ、個人が特定される情報や社外秘の内容の入力は避ける
- **日本での知名度はまだ発展途上**: 米国では評価額26億ドル(2026年6月時点、累計調達額約6.45億ドル)・年換算売上2.5億ドル・月間アクティブユーザー200万人超・法人契約7,000社超と急成長しているが、日本国内での利用実績・レビューの蓄積はPerplexityやChatGPTに比べるとまだ少ない。組織導入の際は、まず個人アカウントの無料枠で使用感を確認してから展開範囲を広げるのが無難

## 最初の一歩

genspark.aiに無料登録し、直近で調べたい競合や市場のテーマを1つ選んで「◯◯について調べてスライドにまとめて」とSuper Agentに指示してみる。出てきたスライドの根拠情報を1つ選んで、実際の一次情報と内容が一致しているかを確認する。SecondBrainやGenMailなどメール・会話へのアクセス権限を求める機能は、社内の情報管理ルールを確認したうえで使うかどうかを判断する。

## 関連トピック

- [Perplexityの基本](./perplexity-basics.md)
- [NotebookLMの基本](./notebooklm-basics.md)
- [生成AIによる情報収集・リサーチの実務活用(Deep Research機能)](../part12-business-practice/ai-research-and-information-gathering.md)

## 更新履歴

### 2026-07-23: 2026年7月時点の最新機能・料金・企業動向に更新
- **内容**: 2026年7月21日公開の「AI Workspace 6.0」(SecondBrain・SecondBrain Note・GenTeam・GenMail・AI Design・AgentBase)を反映し、2026年3〜6月のWorkspace 3.0/4.0・Claw for Desktop・シリーズB拡大(評価額26億ドル、累計調達額約6.45億ドル)・ARR2.5億ドル・法人契約7,000社超などの最新数値を追記。比較表にNotebookLMを追加し、Perplexityの料金・機能変化(無制限Pro Search、Labsの表・レポート生成)を反映。SecondBrain等の常時記憶機能に関する情報管理上の注意点を新設
- **出典**: [Genspark Unveils AI Workspace 6.0(Morningstar/BusinessWire転載)](https://www.morningstar.com/news/business-wire/20260721503339/genspark-unveils-ai-workspace-60-betting-ais-next-breakthrough-isnt-models-its-context)、[Genspark Unveils "AI Workspace 6.0" with "SecondBrain" Memory System and First-Ever Hardware | BigGo Finance](https://finance.biggo.com/news/e3a7966e-8c4f-4a13-84ad-517f81c529e5)、[Genspark Unveils AI Workspace 6.0 | Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/genspark-unveils-ai-workspace-6-150700549.html)、[Genspark Launches Genspark Claw for Desktop and Microsoft Office Integration with AI Workspace 4.0 | Morningstar](https://www.morningstar.com/news/business-wire/20260408545044/genspark-launches-genspark-claw-for-desktop-and-microsoft-office-integration-with-ai-workspace-40-bringing-ai-to-local-files-and-everyday-work-apps)、[Genspark Claw Launches as Genspark's First "AI Employee", Alongside AI Workspace 3.0 | BusinessWire](https://www.businesswire.com/news/home/20260312641003/en/Genspark-Claw-Launches-as-Gensparks-First-AI-Employee-Alongside-Genspark-AI-Workspace-3.0-as-the-Company-Surpasses-%24200M-Annual-Run-Rate-and-Extends-Series-B-to-%24385M-and-Reaches-near-%241.6B-Valuation)、[Genspark - 2026 Company Profile, Funding & Competitors | Tracxn](https://tracxn.com/d/companies/genspark/__DlTsNPTygT2CGPOJLBFzdx5Sw1bv2C7rP7f8bbYirtg)、[Genspark.ai Extends Series B to $485M at $2.6B Post-Money Valuation | Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/genspark-ai-extends-series-b-131000248.html)、[Genspark launches Custom Super Agent and Super Agent Store | TestingCatalog](https://www.testingcatalog.com/genspark-launches-custom-super-agent-and-super-agent-store/)、[New Genspark browser brings AI assistant to every webpage | TestingCatalog](https://www.testingcatalog.com/new-genspark-browser-brings-ai-assistant-to-every-webpage/)、[Genspark AI Pricing 2026: Free, Plus & Pro Plans Compared | Felloai](https://felloai.com/genspark-ai-pricing/)、[Genspark Pricing Plans In 2026 | AffiliateBooster](https://www.affiliatebooster.com/genspark-pricing/)、[Team & Enterprise Plans | Genspark Help Center(検索結果からの要約)](https://www.genspark.ai/helpcenter/team-enterprise-plans)、[Perplexity Pricing 2026 | Finout](https://www.finout.io/blog/perplexity-pricing-in-2026)、[Perplexity vs NotebookLM (2026) | T-Minus AI](https://www.tminusai.com/ai-tools/compare/perplexity-vs-notebooklm)、[Genspark使い方登録から全機能を完全解説【2026年5月版】| dospara](https://www.dospara.co.jp/ai-pc/tfc-ai-genspark-how-to-use-guide.html)
- **注記**: genspark.ai公式サイト(pricing・blog・helpcenter配下のページ)は本セッションから直接アクセスできず(403エラー)、検索エンジンのスニペットおよび複数の第三者記事・プレスリリース転載記事の突き合わせに基づく記述を含む。GenSparkはサービスの重心・料金体系の変更が非常に頻繁なため、業務利用・記事化の前には必ず公式サイトで最新情報を確認すること

### 2026-07-06: 初版執筆
- **内容**: GenSparkの概要(Mixture-of-Agentsアーキテクチャ、Sparkpage、Super Agent、Call For Me等の主要機能)、Perplexity・ChatGPT・Geminiとの比較表、料金プラン(Free/Plus/Pro/Business)、日本語対応状況、注意点を整理
- **出典**: [Genspark Pricing Page(公式)](https://www.genspark.ai/pricing)、[Genspark Membership Plans(公式ヘルプセンター)](https://www.genspark.ai/helpcenter?doc=general_Membership_Plans)、[Genspark AI Pricing 2026: Free, Plus & Pro Plans Compared | Felloai](https://felloai.com/genspark-ai-pricing/)、[Genspark（ジェンスパーク）とは？AIエージェント機能の使い方・料金、ChatGPTとの違い | mieru-ca](https://mieru-ca.com/ai-seo/genspark/)、[Genspark（ジェンスパーク）の使い方とは？ | アイスマイリー](https://aismiley.co.jp/ai_news/what-is-genspark/)、[Genspark AIとは？Perplexityとの違いや便利機能を解説 | WEEL](https://weel.co.jp/media/innovator/genspark-ai/)、[Genspark - AI Wiki](https://aiwiki.ai/wiki/genspark)、[Genspark ships no-code personal agents with GPT-4.1 and OpenAI Realtime API | OpenAI](https://openai.com/index/genspark/)、[Hands-On Guide to Genspark: Super Agent, Tools, Use Cases | whytryai](https://www.whytryai.com/p/genspark-beginner-guide)、[How Genspark Went From $0 to $2.6 Billion in Under Two Years | TIGI](https://theimpactfulglobalindian.com/articles/genspark-s-2-6-billion-valuation-shows-the-ai-funding-frenzy-isn-t-slowing)、[Genspark.ai Extends Series B to $485M, at $2.6 Billion Valuation | FinSMEs](https://www.finsmes.com/2026/06/genspark-ai-extends-series-b-to-485m-at-2-6-billion-valuation.html)、[Genspark Expands Its "AI Workspace" With OpenAI, Anthropic, and Microsoft | Tech Times](https://www.techtimes.com/articles/319240/20260629/genspark-expands-its-ai-workspace-openai-anthropic-microsoft.htm)、[GenSparkは日本語対応しているの？設定方法と利用 | ai-dounyu](https://www.ai-dounyu.com/articles/genspark-japanese)
- **注記**: genspark.ai公式サイト・アイスマイリー・WEEL等の一部ページは本セッションから直接アクセスできず(403エラー)、検索エンジンのスニペットおよび複数の第三者記事の突き合わせに基づく記述を含む。GenSparkはサービスの重心・料金体系の変更が非常に頻繁なため、業務利用・記事化の前には必ず公式サイトで最新情報を確認すること
