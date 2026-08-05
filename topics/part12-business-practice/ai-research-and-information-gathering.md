---
title: "生成AIによる情報収集・リサーチの実務活用(Deep Research機能)"
part: 12
chapter: 第4章 情報収集・リサーチ
tags: [Deep Research, リサーチ, 情報収集, 競合分析, ハルシネーション, プロンプト設計, Microsoft Copilot]
created: 2026-07-06
updated: 2026-08-01
---

# 生成AIによる情報収集・リサーチの実務活用(Deep Research機能)

## これは何か

競合の動向調査や市場規模の把握、ツール比較のようなリサーチ業務は、複数のサイトを開いては読み、また検索し直すという地道な作業の繰り返しで、担当者1人で半日〜数日かかることが珍しくない。ChatGPT・Gemini・Perplexity・Claude・Microsoft 365 Copilotなど主要な生成AIツールには、この「調べて・比較して・まとめる」という一連の作業をAIが自律的に代行する「Deep Research(ディープリサーチ)」型の機能が搭載されている。テーマを与えるだけで、AIが数十〜数百件のWebサイト(ツールによっては社内文書・メールなど非公開データも)を自分で巡回し、数分〜数十分かけて出典付きの長文レポートを作成してくれる。普通のチャット+Web検索とは別物の「時間のかかる本格リサーチ用モード」として理解しておくと使い分けやすい。

## 仕組み・背景

通常のチャットにおけるWeb検索(グラウンディング)は、1〜2回検索して見つかった情報をその場で文章に反映するだけで、数秒〜十数秒で回答が返ってくる。これに対してDeep Research系の機能は、次のような「エージェント型」の動き方をする。

1. 与えられたテーマを、AI自身がいくつかの調査観点・サブクエスチョンに分解する(多くのツールでは、実行前に「調査計画」として提示され、着手前に人が修正できる)
2. 観点ごとに検索クエリを立て、実際に複数のWebページ(や、ツールによっては社内データ)を開いて内容を読み込む
3. 得られた情報をもとに、さらに追加で調べるべき点(矛盾点・情報不足)を自分で判断し、追加検索を繰り返す
4. 最終的に、章立てのある長文レポートとして出典付きでまとめる

この「自分で調査計画を立て、複数ステップにわたって自律的に検索・閲覧を繰り返す」点が、いわゆるAIエージェント(人間が逐一指示しなくても、目的に向けて自律的にタスクを実行するAI)としての性質であり、通常の検索連携チャットとの決定的な違いになる。その分、処理には数分〜数十分という「待ち時間」が発生し、利用回数もプランごとに制限されている。

2026年に入ってからは、単に「Web上の公開情報を集める」だけでなく、(1)実行前に調査計画を編集できる、(2)調査対象のサイトを絞り込める、(3)MCP(Model Context Protocol、AIと外部ツールをつなぐ標準規格)や社内データ(メール・会議メモ・共有ドライブなど)も情報源に加えられる、という方向に各社が機能拡張を進めている。「Web専用の調査ツール」から「社内外の情報を横断するリサーチエージェント」へと役割が広がりつつある点が、直近1年の大きな変化点。

## 使いどころ・使い分け

### 主要ツールの比較(2026年8月時点)

| ツール・機能名 | 所要時間の目安 | 参照ソース数の目安 | 出力形式 | 利用可能プラン・回数の目安 |
|---|---|---|---|---|
| ChatGPT「deep research」 | 5〜30分 | 20〜50件程度 | 出典付きの長文レポート(本文中に引用リンク、フルスクリーン表示可) | Free(軽量版・月5回)/Plus($20、月10〜25回程度)/Pro $100(月50回程度、2026年4月新設の中間プラン)/Pro $200(月250回)/Business・Enterprise(組織ごとに上限を設定可) |
| Gemini「Deep Research」 | 数分〜10分程度 | 100件超(150件以上に及ぶ例も報告) | 複数ページの構造化レポート、Googleドキュメントへのエクスポート可 | 無料(月5回まで)/Google AI Plus(月額725円/$4.99、1日12回)/Google AI Pro(月額2,900円/$19.99、1日20回)/Google AI Ultra(月額14,500円〜、Proの5〜20倍相当) |
| Perplexity「Deep Research」 | 数分程度 | 数十〜100件超 | 出典番号付きの長文レポート | Free(1日3〜5回程度)/Pro(月額$20、1日20回)/Max(月額$200、実質無制限)/Enterprise Max(1ユーザー月500回) |
| Claude「Research」 | 数分〜最大45分(内容の複雑さで自動調整) | 数百件規模に及ぶ例も報告 | 出典付きの長文レポート | Pro/Max/Team/Enterprise(有料プランのみ、Freeでは利用不可)。ベータ提供中で、米国・日本・ブラジルなど順次拡大 |
| Microsoft 365 Copilot「Researcher」 | 数分程度 | Web+社内データ(メール・Teams会議・SharePoint/OneDrive文書など)を横断 | 出典・参照元付きの構造化レポート | Microsoft 365 Copilotライセンス(1ユーザー月額$30目安の追加ライセンス)または Microsoft 365 Premium個人プランに含まれ、追加費用なしで月25クエリ程度 |

(利用回数・料金は変更されやすいため、実際に使う前に各社の公式ヘルプページで最新の上限を確認すること)

### 使うべき場面 / 使わない方がよい場面

| 場面 | Deep Research系機能 | 通常のチャット+自分でWeb検索 |
|---|---|---|
| 「◯◯社の株価は今いくらか」のような単発の事実確認 | 不向き(数分待つだけ無駄) | 向く(数秒で済む) |
| 競合5社の料金・機能を横並びで比較したい | 向く(自動で複数サイトを巡回し表にまとめてくれる) | 手間がかかる |
| ある市場のざっくりした規模感・トレンドを把握したい | 向く | 断片的な情報しか得られないことが多い |
| 特定の1本の記事やPDFの内容を要約したい | 不向き(自律巡回は不要、対象を直接読ませれば十分) | 向く(ファイルを渡して要約させるだけでよい) |
| 新規取引先・提携候補の背景を一通り洗い出したい(デューデリジェンスの下調べ) | 向く | 手間がかかる |
| 社内の会議メモ・メール・過去資料を根拠に社内向けレポートをまとめたい | Microsoft 365 Copilot「Researcher」は向く(社内データ+Webを横断)/その他のDeep Researchは不向き(Web巡回が前提) | 状況による |

判断基準はシンプルで、「答えが1つの事実で、検索1回で見つかる」ならDeep Researchは過剰装備。「複数の情報源を横断して比較・統合する必要がある」ならDeep Researchが時間対効果で勝る。さらに、調査対象が「社内の非公開情報を含む」場合は、Web専用のDeep Research(ChatGPT・Gemini・Perplexity・Claudeの標準構成)ではなく、社内データに接続できるMicrosoft 365 CopilotのResearcherや、自社導入済みのRAG(検索拡張生成)ツールを選ぶ。

## 実務での使い方

### 起動場所(2026年8月時点)

- **ChatGPT**: メッセージ入力欄の「+」またはツール選択メニューから「deep research」を選択してプロンプトを入力。実行前に調査計画が表示されるようになり、着手前に編集したり、実行中に途中で方向修正の指示を挟んだりできる。「特定のサイトだけを調べてほしい」場合はサイトを指定して調査範囲を絞ることも可能
- **Gemini**: Geminiアプリのモデル選択・ツールメニューから「Deep Research」を選び、テーマを入力すると、AIがまず調査計画(リサーチプラン)を提示してくるので、必要に応じて修正してから実行を承認する
- **Perplexity**: 検索窓の下にあるモード切り替えで「Research」を選択して質問を入力
- **Claude**: チャット入力欄左下の「Research」ボタンをクリックして有効化(青色になれば有効)してから質問を送信。有効化するとWeb検索に加えて、接続済みのGoogle Workspaceや外部ツール(Integrations/MCP連携)も情報源として使われる
- **Microsoft 365 Copilot**: Copilotチャット画面のエージェント選択(または「Researcher」と入力して起動)からResearcherエージェントを呼び出し、調査テーマを入力する。組織のMicrosoft Graphデータ(メール・Teams・SharePoint等)へのアクセス許可はすでに付与されている前提で、Web情報と横断的に調査してくれる

### プロンプトの書き方のコツ

Deep Researchは「調査範囲が曖昧なまま丸投げする」と、論点がずれたレポートになりがちで、数分〜数十分の待ち時間が無駄になる。次の4点を明示すると精度が上がる。

1. **調査目的とアウトプットの使い道**(何のためのリサーチか)
2. **調査対象の範囲**(業界・地域・期間・比較対象の企業名など)
3. **欲しいアウトプットの構成**(比較表がほしい、章立てを指定するなど)
4. **除外してほしい情報**(古い情報、特定領域を除くなど)

そのままコピペで使えるプロンプト例(競合分析):

```
あなたはSaaS業界のリサーチアナリストです。以下の条件でDeep Researchを実行してください。

【目的】自社の会議室予約SaaS「◯◯」の価格戦略を見直すための競合比較資料を作成する
【調査対象】国内向けに提供されている会議室予約・座席予約SaaSのうち、
  従業員300〜1,000人規模の企業をメインターゲットとしている主要5社程度
【調べてほしい項目】
  1. 各社の料金プラン(初期費用・月額・課金単位)
  2. 主要機能の一覧と、他社にない差別化機能
  3. 直近1年以内の新機能リリース・価格改定の動き
  4. 導入企業の口コミ・レビューで頻出する不満点
【アウトプット形式】
  - 上記4項目を横並びで比較できる表を作成
  - 各項目の情報源URLを明記
  - 最後に「自社が価格改定を検討する際の論点」を3つ提案
【除外条件】
  - 個人・フリーランス向けの小規模プランは対象外
  - 2023年以前の古い情報は参考程度にとどめ、本文には反映しない
```

ChatGPT・Claudeのように調査計画を事前に確認できるツールでは、この段階で「この観点が抜けている」「この業界は対象外にしたい」と一言指示を返してから本実行に進むと、やり直しの手戻りが減る。

### 出てきたレポートの活用フロー

1. レポート内の比較表・要約部分を、社内向け資料や記事の「材料」としてそのままコピー&要約に使う
2. 数値・固有名詞・「◯位」「◯%」といった定量的な主張は、次の「注意点」に従って裏取りする
3. 重要な意思決定(契約・投資・公表)に使う場合は、レポートを「一次情報ではなく仮説の束」として扱い、原典を人が確認してから資料に落とし込む

## 注意点・よくある誤解

- **Deep Researchも幻覚(ハルシネーション)を起こす**: 自律的に多数のサイトを巡回するとはいえ、内部で使われているのは同じ生成AIモデルであり、出典を誤読したり、複数のソースの内容を混同して事実と異なる要約を作ったりすることがある。Deep Research特有の失敗として「存在するが的外れなソースを引用する」「ページの一部だけを読んで文脈を取り違える」ケースも報告されている。ハルシネーションそのものの仕組みや対策は[ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)を参照し、Deep Researchのレポートにもそのまま適用する
- **「出典が付いている=正しい」ではない**: レポート中の引用リンクは「確認できる状態になった」だけであり、「確認済み」ではない。特に数値・統計・「業界No.1」のような比較優位の主張は、レポートを鵜呑みにせず検証する
- **具体的な検証ワークフロー**: (1)レポート中で重要な結論を左右している主張・数値を3〜5個ピックアップする、(2)それぞれの出典リンクを実際に開き、レポートの記述と原文が一致しているか確認する、(3)一致しない・リンク切れ・出典が見当たらない場合は、その主張を資料から削除するか「未確認」と明記する、という3ステップを対外資料に使う前に必ず行う
- **待ち時間・回数制限に注意**: 数分〜数十分かかる上に、有料プランでも月間・日次(あるいは5時間ごとに補充される計算量クォータのような形式)の利用回数に上限がある。単純な事実確認にDeep Researchを使うと、時間もクォータも無駄にする。特にGeminiは2026年に「1日◯回」という単純な回数制から、一定時間ごとに補充される計算量クォータ方式に変更されており、Deep Researchのような重い処理は消費が大きい点に注意
- **調査計画の提示を確認・修正する**: 実行前にAIが調査プランを提示するツール(ChatGPT・Gemini・Claudeなど)では、明後日の方向を調べようとしていないか確認してから実行を承認する。プロンプトが曖昧なまま実行すると、欲しかった論点が抜け落ちたレポートになりやすい
- **社内データを扱う機能は権限管理とセット**: Microsoft 365 CopilotのResearcherのように社内データ(メール・会議・文書)まで横断できる機能は便利な反面、本人がアクセス権を持つ範囲を超えて情報が混ざることはないが、レポートの共有範囲を誤ると社外秘情報が想定外の相手に渡るリスクがある。共有前に宛先を必ず確認する
- **Web専用のDeep Researchは社内文書の根拠付けには使えない**: ChatGPT・Gemini・Perplexity・ClaudeのDeep ResearchはWeb上の公開情報を巡回する機能であり、社内文書を根拠にしたい場合はMicrosoft 365 CopilotのResearcher、NotebookLM、社内RAGツールなど別の仕組みを使う

## 最初の一歩

自分が最近時間をかけて調べた競合・ツール比較のテーマを1つ選び、上記のプロンプト例の形式(目的・調査対象・調べてほしい項目・アウトプット形式・除外条件)に当てはめて、手元のツールのDeep Research機能で実行し、出てきたレポートの出典リンクを2〜3個実際に開いて内容が一致するか確認してみる。

## 関連トピック

- [生成AIに向く業務・向かない業務の切り分け](ai-task-suitability.md)
- [ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)
- [Google Gemini の基本](../part03-ai-chat-tools/google-gemini-basics.md)
- [Microsoft Copilot の基本](../part03-ai-chat-tools/microsoft-copilot-basics.md)

## 更新履歴

### 2026-08-01: 料金・回数上限・新機能を2026年8月時点に最新化、Microsoft 365 Copilot「Researcher」を比較表に追加
- **内容**: ChatGPTのPro $100中間プラン新設と回数見直し、GeminiのGoogle AI Plus新設(725円/$4.99・1日12回)とクォータ方式変更、PerplexityのFree/Pro/Max/Enterprise Maxの回数、Claude Researchの提供地域拡大(米国・日本・ブラジル)とGoogle Workspace/MCP連携対応を反映。新たにMicrosoft 365 Copilotの「Researcher」エージェント(社内データ+Web横断、月25クエリ)を比較表・使い分け表に追加し、社内データを扱う場合の注意点を追記
- **出典**: [What is ChatGPT Go? | OpenAI Help Center](https://help.openai.com/en/articles/11989085-what-is-chatgpt-go)、[Deep research in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10500283-deep-research-faq)、[ChatGPT Pricing 2026: Free vs Go vs Plus vs Pro | CometAPI](https://www.cometapi.com/chatgpt-pricing-2026-free-vs-go-vs-plus-vs-pro/)、[Is ChatGPT Free? Free Plan Limits in 2026 | FelloAI](https://felloai.com/is-chatgpt-free/)、[Google AI Plus Is Now $4.99 | FindSkill.ai](https://findskill.ai/blog/google-ai-plus-4-99-worth-it/)、[「Google AI Plus」が月額725円に値下げ | ケータイ Watch](https://k-tai.watch.impress.co.jp/docs/news/2115643.html)、[Google AI Proとは？ | AI総合研究所](https://www.ai-souken.com/article/google-ai-guide)、[Perplexity Pricing in 2026 | Finout](https://www.finout.io/blog/perplexity-pricing-in-2026)、[Is Perplexity AI Free? Free Plan Limits in 2026 | FelloAI](https://felloai.com/is-perplexity-ai-free/)、[Claude takes research to new places | Claude by Anthropic](https://claude.com/blog/research)、[Claude's AI research mode now runs for up to 45 minutes | Harvard TagTeam](https://tagteam.harvard.edu/hub_feeds/3382/feed_items/13720721/content)、[Microsoft 365 Copilotでの研究者の概要 | Microsoft サポート](https://support.microsoft.com/ja-jp/microsoft-365-copilot/get-started-with-researcher-in-microsoft-365-copilot)、[M365 Copilot契約してるなら Researcher使わないのは損すぎる | Zenn](https://zenn.dev/syoshida07/articles/8268188a97d8e5)

### 2026-07-06: 初版執筆
- **内容**: ChatGPT・Gemini・Perplexity・ClaudeのDeep Research系機能の仕組み・所要時間・参照ソース数・料金プランを比較整理し、競合分析プロンプト例、出典検証ワークフロー、単純な事実確認との使い分け基準を執筆
- **出典**: [Introducing deep research | OpenAI](https://openai.com/index/introducing-deep-research/)、[ChatGPT Deep Research - Wikipedia](https://en.wikipedia.org/wiki/ChatGPT_Deep_Research)、[ChatGPT Deep Research Is Now Available To Free Users | BGR](https://www.bgr.com/tech/chatgpt-deep-research-is-now-available-to-free-users/)、[ChatGPT Plans | Free, Go, Plus, Pro, Business, and Enterprise](https://chatgpt.com/pricing/)、[Gemini Deep Research - あなたのニーズに応えるリサーチ アシスタント](https://gemini.google/jp/overview/deep-research/?hl=ja)、[Gemini Deep Researchとは？料金や使い方、終わらない時の対処法まで解説 | マネーフォワード クラウド](https://biz.moneyforward.com/ai/basic/857/)、[Gemini 料金プラン完全ガイド【2026年最新】 | はてなベース株式会社](https://hatenabase.jp/blog/gemini-pricing-guide-2026/)、[Perplexity Pricing in 2026 for Individuals, Orgs & Developers | Finout](https://www.finout.io/blog/perplexity-pricing-in-2026)、[How Much Does Perplexity Cost in 2026? | Studio Global AI](https://www.studioglobal.ai/discover/answers/searching-with-cited-sources-for-how-much-6a37798ab29eeaced030281f)、[Use research on Claude | Claude Help Center](https://support.claude.com/en/articles/11088861-use-research-on-claude)、[Claudeの最新機能「Research」が実現する情報探索の革新 | チャエンのAI研究所](https://digirise.ai/chaen-ai-lab/claude-research-2/)、[Claudeのリサーチ（Research）機能とは？ | マスタング](https://mustang.vc/blog/2026/02/25/claude%E3%81%AE%E3%83%AA%E3%82%B5%E3%83%BC%E3%83%81%EF%BC%88research%EF%BC%89%E6%A9%9F%E8%83%BD%E3%81%A8%E3%81%AF%EF%BC%9F%E4%BD%BF%E3%81%84%E6%96%B9%E3%83%BB%E6%B4%BB%E7%94%A8%E4%BE%8B%E3%83%BB/)
