---
title: "ChatGPTのWeb検索機能"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [ChatGPT, Web検索, ChatGPT search, 検索連携, グラウンディング, 出典, ハルシネーション]
created: 2026-07-06
updated: 2026-09-05
---

# ChatGPTのWeb検索機能

## これは何か

ChatGPTの回答は基本的に学習データの時点までの知識に基づいている。そのため「今日の株価は?」「このソフトの最新バージョンの機能は?」のように鮮度が問われる質問をすると、古い情報をそのまま答えたり、知らないと返してきたりして業務に使えないことがある。**ChatGPTのWeb検索機能(「ChatGPT search」)**は、質問に応じてChatGPTがその場でWeb上の情報を検索し、出典(引用リンク)付きで回答に反映する機能で、この「知識の鮮度切れ」を補う役割を持つ。2024年10月に有料プラン向けに先行公開され、2025年2月5日には無料プラン・ログインしていないユーザーにも開放されて以降、現在はほぼ全プランで標準搭載の機能になっている。2026年9月時点でも呼び方(「ChatGPT search」)や基本的な使い方に大きな変更はないが、裏側で実行される検索クエリの組み立て方(後述の「fan-out」化)や周辺の収益化施策(広告表示)は2026年に入ってからも段階的に変化し続けている。

なお2026年7月14日には、過去の自分のチャット履歴・プロジェクト・画像・ドキュメントを横断して探す「検索」機能がサイドバーに追加された。これは自分のアカウント内を探す機能であり、本ページで扱う「Web上の情報を検索する」Web検索機能とは別物なので混同しないよう注意する。また、2025年10月に登場したスタンドアロンのAIブラウザー「ChatGPT Atlas」は2026年8月9日に提供終了となり、その自律的なブラウジング機能はChatGPTデスクトップアプリとChrome拡張機能に統合された。Atlasは「Webページを自律的に操作するエージェント機能」であり、本ページのWeb検索(質問に答えるための出典付き検索)とは目的が異なる別機能だった点も合わせて押さえておく。

## 仕組み・背景

検索エンジンとしては長らくMicrosoft Bingの検索インデックスをベースに利用し、これにOpenAI自身のクローラー「OAI-SearchBot」による個別ページの補完クロールを組み合わせてきた。ただし2026年に入り、この内訳には変化が見られる。SEO分析企業Profoundの調査によれば、ChatGPTの引用元とBingの検索順位との一致率は26%から8%に低下する一方、Googleの検索順位との一致率は12%から33%に上昇しており、OpenAIが独自インデックスを強化しつつBingへの依存度を下げている可能性が指摘されている(一方でSeer Interactive社の別の分析では引用の87%がBing上位10位と一致するとの逆の結果も出ており、算出方法によって数字は大きく振れる。OpenAI自身はこの構成変更を公式には認めていない)。実務上重要なのは検索エンジンの内訳そのものよりも、自社サイトをChatGPTのWeb検索結果に載せたい場合は`robots.txt`でOAI-SearchBotのアクセスを拒否していないか確認するという原則で、これは検索エンジンの構成が変わっても変わらず有効である。BingやGoogleでの検索順位が高くても、OAI-SearchBotを拒否しているサイトはChatGPTのWeb検索結果には出てこない。なお、Web検索の結果として実際にユーザーの質問に応じてページ本文を読みに来るクローラーは「ChatGPT-User」であり、検索対象への掲載可否を左右する「OAI-SearchBot」とは役割が異なる(両者はrobots.txtで個別に許可・拒否を設定できる)。

回答が生成されるまでの流れは、おおむね次の4段階で進む。

1. ユーザーの質問を、検索に適したクエリに書き換える
2. 書き換えたクエリでWeb検索を実行する
3. 検索で見つかった候補ページを開き、内容をチャンク(部分)単位で読み込む
4. 読み込んだ内容をもとに、出典を付けて回答文を生成する

2026年8月以降で実務上押さえておきたいのは、ステップ1〜2の「クエリ書き換え」が単発の1問1答ではなく、1つの質問を裏側で複数の検索クエリに分解して並列実行する「fan-out(ファンアウト)」型に進化している点である。特に2026年8月8日には、特定サイトに絞り込んで検索する`site:`演算子を使うクエリの比率が全体の0.4%前後から17%前後へと1日で急増したと報告されており、1回の回答あたりの検索実行回数もほぼ倍増したとされる。実務上の含意は、自社サイトの情報がChatGPTの回答に反映されるかどうかは「Googleでの掲載順位」よりも「ChatGPTが自社ドメインを名指しして`site:`検索してくれるかどうか」に左右される場面が増えているということで、自社名・製品名で指名検索されたときに正しい情報が出るよう、公式サイト側の情報を整理しておく価値が増している。

Web検索を使うかどうかは、質問文の内容からChatGPT側の判定ロジック(モデル選択と合わせて動く「ルーター」)が自動的に決めている。たとえば「今日の東京の天気は?」のような質問は高い確率でWeb検索が発動する一方、雑談や過去の一般知識で答えられる質問では検索は行われない。ユーザー側から明示的に「検索して」と指示しなくても自動で切り替わるが、後述の手順で手動でWeb検索を強制することもできる。

位置情報については、IPアドレスから推定したおおまかな位置(国・都道府県・市区町村レベル)を検索クエリの書き換えに使うことがある(例:「近くのおすすめレストランは?」→「東京 渋谷 おすすめレストラン」に書き換えて検索)。ただしIPアドレスそのものやアカウント情報が検索プロバイダーに渡ることはない。デバイスの精密な位置情報(GPSなど)の共有はオプションでデフォルトはオフになっており、設定で切り替えられる。

## 使いどころ・使い分け

| 場面 | 向いている機能 |
|---|---|
| 一般知識の相談、文章の下書き、アイデア出しなど、鮮度が問われない相談 | 通常のチャット(検索なし)で十分。検索を挟むと回答が遅くなる・ノイズが増える場合がある |
| 今日のニュース・株価・天気・最新ソフトのバージョンなど、鮮度が必須の1問1答 | ChatGPTのWeb検索(自動判定または手動オン) |
| 競合5社の料金・機能比較のような、複数サイトを横断してレポートにまとめたい調査 | [Deep Research機能](../part12-business-practice/ai-research-and-information-gathering.md)。Web検索は1〜数回の検索で即答するのに対し、Deep Researchは数分〜数十分かけて数十〜数百件のページを自律的に読み込みレポート化する |
| 社内文書・非公開の契約書や議事録など、社外秘の情報を根拠にしたい | Web検索・Deep Researchのどちらも不向き(公開Web限定)。社内RAGツールやファイルアップロードでの要約を使う |

判断基準はシンプルで、「1回〜数回の検索で足りる事実確認」ならWeb検索、「複数ソースを横断した比較・長文レポート」ならDeep Research、「鮮度を問わない相談」なら検索なしの通常チャットが最も速くて無駄がない。

## 実務での使い方

### 使い方の手順(2026年9月時点)

- **自動で使われる場合**: 何も操作せず質問するだけで、鮮度が必要と判断されればChatGPTが自動でWeb検索を行う。回答中に番号付きの引用リンクが表示されていれば、Web検索が使われた証拠になる。
- **手動で明示的にオンにする場合**: メッセージ入力欄の「+」アイコンをクリックし、表示されるメニューから「Web検索」を選択する(または入力欄で半角の「/」を入力し、出てくるメニューから「Web検索」を選ぶ)。これで次の質問には必ずWeb検索が使われる。
- **出典の確認方法**: 回答中に表示される番号付きの引用をクリック(またはタップ)すると、出典元のページが開く。引用番号が本文中に表示されない回答の場合は、回答の下にある「ソース」ボタンをクリックすると、参照したサイトの一覧パネルが開く。

### 対応プラン・料金

Web検索自体に追加料金はかからず、Free・Go・Plus・Pro・Business・Enterprise・Eduの全プランの通常の利用枠の中で使える(Goプランは2026年1月に日本を含む世界展開され、日本では月額1,400円・米国では月額8ドル前後で、上位プランより少ない利用枠で提供されている)。2025年2月5日以降は、ログインしていない未登録ユーザーでも利用できる。Enterprise・Eduプランでは、管理者が管理設定の「Web search」項目からワークスペース単位・ロール単位でWeb検索の許可/禁止を切り替えられ、社外情報を業務に混ぜたくない企業向けに無効化する選択肢もある。

**広告表示との違いに注意**: 2026年2月に米国のFree・Goプランで先行導入された、回答の下へ「スポンサー」ラベル付きの広告(Sponsored Recommendations)は、2026年5月以降に日本・英国・韓国・ブラジル・メキシコなどへ拡大し、日本では同年6月19日から表示が始まった(国内のローンチパートナーは電通デジタル・博報堂DYワン・サイバーエージェントなど)。2026年8月には広告の選定ロジックが明確化され、過去のチャット履歴や記憶(メモリ)ではなく、**その場の会話の話題・おおまかな位置情報・利用デバイス**を基に広告が選ばれる仕様であることが公式に説明された。広告は回答の生成内容そのものには影響しないとされ、Web検索の引用リンクとは別枠で視覚的に区別して表示される。Plus・Pro・Business・Enterprise・Eduのユーザーには広告は表示されず、Free・Goプランでも広告のオプトアウト(その代わりメッセージ上限が下がる)や、パーソナライズの抑制(「過去のチャットとメモリ」設定をオフにする)を選べる。業務でWeb検索の結果を人に共有する際は、引用リンク(出典)と広告(スポンサー表示)を混同しないこと。

### 他ツールでの同様の機能(対応表)

| 概念 | ChatGPT | Google Gemini | Microsoft Copilot | Perplexity |
|---|---|---|---|---|
| 呼び方 | Web検索(ChatGPT search) | Google検索によるグラウンディング(grounding) | Web検索(Bing統合) | 検索そのものがサービスの中核(常時Web検索ベース) |
| 裏側の検索エンジン | Bing中心+OpenAI独自クローラー(OAI-SearchBot)。Googleへの依存度が増しているとの分析もある | Google検索(世界最大級のインデックス) | Bing | 自社クローリング+複数エンジンの併用 |
| 手動で切り替える場所 | 入力欄の「+」→「Web検索」 | 基本は自動判定(明示トグルは限定的) | 会話モード内で概ね自動 | 検索モードの切り替えで制御(通常時から検索前提。無料のAIブラウザー「Comet」も展開) |
| 特徴・強み | ChatGPTの汎用的な対話の中で使え、無料プランでも利用可能。1回答あたりの検索回数が増え、幅広いソースを横断しやすい | Google検索の網羅性、Google Workspaceとの連携。市場シェアの大きいインデックスを使う分、鮮度・網羅性で優位との評価が多い | Outlook・SharePoint・Teamsなど社内データとの統合がしやすい | 出典の粒度が細かく、文単位での引用・検証がしやすいと評価されることが多い |

(各社の検索精度・シェアは第三者の検証記事によって数値がまちまちなため、本ページでは仕組みと使い分けの整理に留め、精度の優劣は個別の検証記事や自分の業務データで確認すること)

### コピペで使えるプロンプト例

```
2026年9月時点での、日本国内における法人向け給与計算SaaSの主要3社
(A社、B社、C社)について、Web検索を使って最新の料金プランと
直近3か月以内の機能アップデートを調べてください。

【出力形式】
- 会社名・プラン名・月額料金・対象従業員規模を表にまとめる
- 各社の直近アップデート内容を1行で要約する
- 情報の出典URLを必ず明記する

【注意】
- 2025年以前の古い料金情報は参考にせず、各社の公式サイトなど
  一次情報を優先してください
- 情報源が見つからない項目は「不明」と書き、推測で埋めないでください
```

Web検索を手動でオンにしてから送っても、自動判定に任せて送ってもよい。回答が返ってきたら、表中の料金など重要な数値は必ず引用リンクを開いて一次情報と一致するか確認する。

## 注意点・よくある誤解

- **出典が付いていても正しさの保証にはならない**: Web検索は1〜数回の検索結果をその場で要約するだけで、内容を突き合わせて検証しているわけではない。ページの一部だけを読んで文脈を誤解したり、複数の出典の内容を混同したりする誤り(ハルシネーション)は依然として起こる。詳しくは[ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)を参照し、重要な数値・固有名詞は必ず引用元のページを実際に開いて確認する
- **「検索窓」ではなく「要約装置」だと理解する**: 従来のGoogle検索のように複数の候補リンクから自分で選ぶのではなく、AIが選んだ少数のページの要約が返ってくる。知りたい情報が少数派の意見・一次資料そのものである場合は、通常の検索エンジンで自分で探した方が確実な場合もある
- **自社サイトが検索結果に出ない理由になりうる設定**: 自社サイトの内容をChatGPTのWeb検索に反映させたい場合は、`robots.txt`でOAI-SearchBotを拒否していないか確認する(実際にページ本文を読みに来るのは別のクローラー「ChatGPT-User」だが、そもそも検索対象として拾われるかどうかはOAI-SearchBotの許可設定に左右される)。逆に、社外秘の情報はそもそもWeb上に公開しないことが前提になる(Web検索は公開情報しか読めない)
- **位置情報の扱い**: デフォルトでIPアドレスからおおよその位置を推定して検索クエリに反映することがある。特定の地域を基準にしたい業務(店舗展開の地域比較など)では、位置情報の自動推定に任せず、プロンプトに地域名を明示した方が確実
- **Deep Researchと混同しない**: Web検索は1〜数回の検索で即答する軽量な機能であり、[Deep Research](../part12-business-practice/ai-research-and-information-gathering.md)は数分〜数十分かけて自律的に数十〜数百件のページを調べる別モード。両方を同じ「検索機能」として捉えると使い分けを誤り、単純な事実確認にDeep Researchの待ち時間を使ってしまったり、逆に本格リサーチにWeb検索だけで済ませて調査不足になったりする
- **「チャット内検索」「ChatGPT Atlas」と混同しない**: 2026年7月に追加された、自分の過去のチャット・プロジェクト・画像・ドキュメントを横断して探す検索機能や、2026年8月に提供終了しChatGPTデスクトップアプリ・Chrome拡張機能に統合された自律ブラウジング機能「ChatGPT Atlas」は、いずれも本ページのWeb検索(Web上の情報を検索して出典付きで回答する機能)とは別物。名前や見た目が似ているため、社内で「ChatGPTの検索機能」と話すときはどれを指しているか明確にする
- **引用リンクと広告(スポンサー表示)を混同しない**: Free・Goプランでは2026年6月から日本でも回答下に「スポンサー」ラベル付きの広告が挿入されることがある。広告はその場の会話の話題をもとに選ばれており(過去のチャット履歴そのものを使うわけではない)、視覚的に区別されているとはいえWeb検索の出典リンクと近い位置に並ぶため、資料に転記する際は誤って広告主のリンクを一次情報として引用しないよう確認する

## 最初の一歩

今日の業務で「これって今も同じ値段・同じ仕様だっけ?」と思った質問を1つ選び、ChatGPTの入力欄の「+」→「Web検索」を明示的に選んで質問してみる。回答に表示される引用リンクを1つクリックし、出典ページの内容と回答の記述が一致しているかを確認する。

## 関連トピック

- [生成AIによる情報収集・リサーチの実務活用(Deep Research機能)](../part12-business-practice/ai-research-and-information-gathering.md)
- [ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)
- [ChatGPTのプラン比較](chatgpt-plan-comparison.md)
- [ChatGPTのモデル一覧と使い分け](chatgpt-model-lineup.md)

## 更新履歴

### 2026-09-05: 検索クエリのfan-out化・広告の選定ロジック・Atlas終了を反映して最新化
- **内容**: (1) 2026年8月8日以降、ChatGPT検索が1つの質問を複数の`site:`演算子付きクエリに分解して並列実行する「fan-out」検索へ大きく比重を移したこと(`site:`演算子の使用率が0.4%前後→17%前後に急増、検索回数もほぼ倍増)を仕組みの節に追記。あわせて、検索対象への掲載可否を左右する「OAI-SearchBot」と、実際にページ本文を読みに来る「ChatGPT-User」クローラーの役割の違いを明記。(2) Bing/Google一致率については、Profoundの分析(Bing一致率26%→8%、Google一致率12%→33%)に対しSeer Interactive社が逆の結果(Bing上位10位との一致率87%)を出している点を追記し、算出方法によって数字が振れることを明示。(3) 広告(Sponsored Recommendations)について、日本を含む主要国への展開時期を整理した上で、2026年8月にOpenAIが公式に説明した「過去のチャット履歴ではなく、その場の会話・おおまかな位置情報・デバイスを基に選定する」という仕組みを追記。(4) Goプランの日本での料金(月額1,400円)を明記。(5) 2026年8月9日にスタンドアロンのAIブラウザー「ChatGPT Atlas」が提供終了しChatGPTデスクトップアプリ・Chrome拡張機能に統合されたことを、本ページのWeb検索とは別機能である旨とあわせて追記
- **出典**: [ChatGPT search now uses the site: operator at scale | Promptwatch](https://promptwatch.com/data/chatgpt-site-operator-fanouts)、[Inside ChatGPT Search: how web.run and fan-out queries shape AI visibility | Search Engine Land](https://searchengineland.com/inside-chatgpt-search-web-run-fan-out-queries-ai-visibility-477339)、[OpenAI user agents (ChatGPT-User/OAI-SearchBot) | xSeek Docs](https://www.xseek.io/docs/openai-crawlers-and-user-agents)、[AI Search Shift: ChatGPT's growing alignment with Google's index | Profound](https://www.tryprofound.com/blog/ai-search-shift)、[Why ChatGPT Citations Come From Bing, Not Google | Seer Interactive分析まとめ](https://www.brandcited.ai/blog/chatgpt-citations-bing-not-google)、[Free ChatGPT users get ads picked from whatever they just asked about | Help Net Security](https://www.helpnetsecurity.com/2026/08/31/chatgpt-ads-privacy-policy/)、[OpenAI Expands ChatGPT Ads Test to UK, Mexico, Brazil, Japan, and South Korea | gHacks](https://www.ghacks.net/2026/08/13/openai-expands-chatgpt-ads-test-to-uk-mexico-brazil-japan-and-south-korea/)、[OpenAI to introduce ads to ChatGPT in Japan | The Japan Times](https://www.japantimes.co.jp/business/2026/06/19/companies/openai-chatgpt-advertisements/)、[【2026年最新】ChatGPT Goプランを知らない人、損してますよ](https://shin-nakauchi.com/blog/chatgpt-go-plan-price-japan-2026/)、[OpenAI shuts down its Atlas browser after not even a year | TechRadar](https://www.techradar.com/pro/openai-shuts-down-its-atlas-browser-after-not-even-a-year)、[Evolving Atlas into ChatGPT for browser-based agentic work | OpenAI Help Center](https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work)

### 2026-07-27: 検索エンジン構成・広告表示・関連の新機能を反映して最新化
- **内容**: (1) 裏側の検索エンジン構成について、Bing一致率の低下(26%→8%)とGoogle一致率の上昇(12%→33%)という2026年の分析を追記しつつ、robots.txtでOAI-SearchBotを拒否しないという実務原則は変わらないことを明記。(2) 2026年6月19日から日本を含む一部国のFree・Goプランに導入された「スポンサー」表示の広告(Sponsored Recommendations)を、Web検索の引用リンクと混同しないよう対応プラン節と注意点に追記。(3) 2026年7月14日に追加された、チャット履歴・プロジェクト・画像・ドキュメントを横断する「チャット内検索」機能が本ページのWeb検索とは別機能である旨を明記。(4) Goプランの世界展開(2026年1月、月額8ドル前後)を反映
- **出典**: [AI Search Shift: ChatGPT's growing alignment with Google's index | Profound](https://www.tryprofound.com/blog/ai-search-shift)、[「ChatGPT広告」日本上陸 無料版と「Go」で表示、電通・博報堂など支援 | ITmedia](https://www.itmedia.co.jp/aiplus/article/2606/19/2000000107/)、[ChatGPT、日本で広告表示開始 | Impress Watch](https://www.watch.impress.co.jp/docs/news/2118443.html)、[OpenAI、「ChatGPT」に新しい検索機能 | Impress Watch](https://forest.watch.impress.co.jp/docs/news/2125169.html)、[Introducing ChatGPT Go, now available worldwide | OpenAI](https://openai.com/index/introducing-chatgpt-go/)、[ChatGPT Rolls Out Search Across Chats, Projects, Images, and Documents | Progressive Robot](https://www.progressiverobot.com/2026/07/14/chatgpt-rolls-out-search-across-chats-projects-images-and-documents/)

### 2026-07-06: 初版執筆
- **内容**: ChatGPTのWeb検索機能(ChatGPT search)の定義、Bing・OAI-SearchBotによる仕組みと4段階の処理フロー、自動判定と手動オンの手順、出典の確認方法、対応プラン(無料プラン含め全プランで利用可・Enterprise/Eduの管理者設定)、Deep Researchとの使い分け、他ツール(Gemini/Copilot/Perplexity)との対応表、位置情報の扱い、出典があっても検証が必要という注意点を執筆
- **出典**: [ChatGPT Search | OpenAI Help Center](https://help.openai.com/en/articles/9237897-chatgpt-search)、[Introducing ChatGPT search | OpenAI](https://openai.com/index/introducing-chatgpt-search/)、[ChatGPT search for Enterprise and Edu | OpenAI Help Center](https://help.openai.com/en/articles/10093903-chatgpt-search-for-enterprise-and-edu)、[ChatGPT Search Is Now Free To Use Without An Account | Forbes](https://www.forbes.com/sites/kateoflahertyuk/2025/02/07/chatgpt-search-is-now-free-to-use-without-an-account-is-it-safe/)、[ChatGPT search is now available to all free users | Search Engine Land](https://searchengineland.com/chatgpt-search-available-free-users-449367)、[Does ChatGPT Use Bing or Google? The Full Search Architecture Explained (2026) | AI+Automation](https://aiplusautomation.com/blog/chatgpt-bing-or-google)、[How ChatGPT reads your content and sees the web | LLMrefs](https://llmrefs.com/blog/how-gpt-sees-the-web)、[ChatGPT uses my IP location to search the web without asking | OpenAI Developer Community](https://community.openai.com/t/chatgpt-uses-my-ip-location-to-search-the-web-without-asking/1011012)、[Best AI Search Engines in 2026: ChatGPT vs Perplexity vs Gemini vs Copilot | AIapps](https://www.aiapps.com/blog/ai-search-engines-comparison-chatgpt-perplexity-gemini-copilot-2026/)
