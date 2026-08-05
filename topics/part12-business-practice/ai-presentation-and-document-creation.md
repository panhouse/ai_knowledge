---
title: 生成AIによるプレゼン資料・ドキュメント作成の実務活用
part: 12
chapter: 第3章 資料・ビジュアル作成
tags: [プレゼン資料, スライド作成, PowerPoint, Google Slides, Gamma, Copilot, Gemini, Claude]
created: 2026-07-06
updated: 2026-08-02
---

# 生成AIによるプレゼン資料・ドキュメント作成の実務活用

## これは何か

「明日までにこの企画をスライド15枚にまとめて」という仕事は、白紙のスライドとにらめっこする時間が最も苦痛な業務の一つである。生成AIは、箇条書きのメモやレポートを「章立て(アウトライン)→スライド構成→見た目のあるスライド」まで一気に引き上げてくれる。ChatGPT・Gemini・ClaudeのようなチャットAIで構成を練るところから、Copilot in PowerPoint・Gemini in Google Slides・Claude for PowerPointのように実際にスライドファイルを生成するツール、Gamma・Canva Magic Design・Genspark・Napkinのようなプレゼン特化AIツールまで選択肢が広がっており、「何を」「どのツールで」作らせるかを使い分けられるようになっておくと、資料作成の時間の大半を占める「叩き台作り」を大幅に圧縮できる。

## 仕組み・背景

生成AIによるスライド作成には、大きく分けて2つのアプローチがある。

1つ目は「文章生成の延長」。AIはまず文章(章立て・見出し・箇条書き)を生成するのが得意で、これをスライドの「骨格」として使う。ChatGPT・Claude・Geminiにアウトラインを作らせてから、それをPowerPointやGoogle Slidesに手で移す、あるいはCopilot・Gemini・Claudeの機能に読み込ませて肉付けさせる、という流れがこれにあたる。

2つ目は「レイアウト・デザインテンプレートへの流し込み」。Gamma・Canva Magic Design・Genspark・Napkinのようなプレゼン特化ツールは、あらかじめ用意された数百〜数千のデザインテンプレート(配色・フォント・図版のレイアウトのセット)に、AIが生成した文章と画像を自動で流し込む仕組みを持つ。「AIが一からデザインを考えている」わけではなく、「AIが文章構成と画像を作り、テンプレートエンジンがそれを整形している」と理解しておくと、なぜ複数のAI生成スライドが似た雰囲気になりがちなのか(同じテンプレート資産を使い回しているため)が腑に落ちる。

2026年に入って、この2つのアプローチの境界は薄くなってきている。Anthropicは2026年2月11日、無料プランを含む全ユーザー向けにClaude.ai上での.pptx/.xlsx/.docx/.pdf直接生成機能を解放し、さらに5月7日にはExcel・Word・PowerPoint向けのアドイン(Outlookはベータ)をMicrosoft Marketplace経由で正式提供した。ChatGPTも2026年5月21日にPowerPoint用アドインを一般提供し、Free〜Enterpriseまで全プランで利用可能になった。「チャットで壁打ち」と「ファイルを直接生成」が同じツールの中で連続してできるようになり、ツール間を移動するコストが下がっている点が2025年までとの大きな違いである。

もう一つの前提は、AIの得意・不得意が「文章生成」と「精密なビジュアル生成」で大きく異なるという点。文章の要約・構造化(見出しと箇条書きへの分解)は生成AIの得意領域だが、「正確な数値に基づいたグラフ」「ブランドガイドラインに完全準拠したデザイン」「1px単位の体裁の調整」は不得意で、最終的には人の目によるチェックと手直しが前提になる。

## 使いどころ・使い分け

| 状況・目的 | 向いているツール | 理由・使い方の要点 |
|---|---|---|
| まず構成・アウトラインだけ壁打ちしたい(スライド枚数はまだ決めていない) | ChatGPT / Claude / Geminiのチャット | ファイルを作る前に、章立て・メッセージの流れ・想定質問への答えを言語化する段階。ファイル生成機能に頼るより、対話で骨子を練り込んだ方が手戻りが少ない |
| 社内のPowerPoint標準フォーマット(会社ロゴ・配色テンプレート)を崩したくない資料 | Copilot in PowerPoint、Claude for PowerPoint | 既存の会社テンプレート(.potx)を開いた状態でAIに指示すれば、そのテンプレートのレイアウト・配色を保ったまま中身を生成・追記できる。ゼロからデザインし直されるリスクが低い |
| Google Slidesで完結させたい(共同編集前提、Drive内の資料を根拠にしたい) | Gemini in Google Slides | サイドパネルのプロンプトから、Drive内の他ファイルを参照させたり、既存デックのスタイルを踏襲させたりしながら、複数枚のスライドを一括生成できる。生成後もGoogle Slidesとして通常通り共同編集できる。ただし2026年8月時点でもスライド生成の入力言語は英語のみ対応(日本語は順次拡大予定) |
| Excel分析→PowerPoint報告のように、複数のOfficeアプリをまたいで1つの作業を仕上げたい | Claude for Excel/PowerPoint(会話コンテキストの引き継ぎ) | Excelでデータ分析した会話の文脈を保ったまま、そのままPowerPointで結果をスライド化するよう指示できる。ファイル間でのコピペ・状況説明のやり直しが不要になる |
| ゼロから見た目の良いスライドを最速で立ち上げたい(社内フォーマットの制約がない、提案書・ウェビナー資料など) | Gamma、Canva Magic Design、Genspark AI Slides | 洗練されたテンプレートに自動で流し込んでくれるため、体裁を考える時間をほぼゼロにできる。ただし社内標準フォーマットとは体裁が異なるため、社外向け・単発の資料向き |
| スライド中の1枚だけ、図解(フローチャート・比較表・ロードマップ等)が欲しい | Napkin等の text-to-visual ツール | テキストの構造を渡すと図解案を複数提示してくれる。PowerPoint/Google Slidesへの部分的な貼り込み用途に向く。デッキ全体の生成には使わない |
| チャットで作った文章をそのままPowerPointファイルにしたい | ChatGPT for PowerPoint / Claude for PowerPoint(いずれもアドイン)、またはChatGPT・Claudeの直接.pptx出力 | アドインとして使うと、テキストプレースホルダーへの書き込みやネイティブな図形生成、テンプレートスタイルの適用まで行われ、編集可能なスライド構造を保った生成ができる。チャット画面だけで済ませたい場合は.pptx直接出力機能もあるが、体裁は簡素になりやすい |
| 既存のWord資料・Excelデータを土台にスライド化したい | Copilot in PowerPoint(ファイル取り込み)、Claude(会話に添付) | Word・PDF・Excelを読み込ませて、その内容を基にデッキを組み立てさせられる。ゼロから書き起こす手間を省ける |

判断の軸は2つ。「社内フォーマットへの準拠が必須か」(必須ならCopilot/Gemini/Claudeのアドイン、自由でよいならGamma系)と、「まだ構成が固まっていないか、もう構成は決まっていて見た目だけ欲しいか」(前者はチャットで壁打ち、後者はファイル生成ツール)。

## 実務での使い方

### コピペで使えるプロンプト例: 箇条書きメモをスライド構成に変換する

会議メモや思いつきの箇条書きを、まずChatGPT・Claude・Geminiなどのチャットで「スライド構成案」に変換してから、PowerPointやGoogle Slides、あるいはGamma等に渡すと精度が上がる。

```
あなたはプレゼン資料作成の専門家です。以下の走り書きメモを、
スライド構成案に変換してください。

## このプレゼンの目的
[例: 部長会議で新規施策の予算承認を得る]

## 聞き手
[例: 施策の詳細には詳しくないが、投資対効果には厳しい役員層]

## 想定スライド枚数
[例: 10枚以内(表紙・目次を含む)]

## 出力形式
スライドごとに、以下の3点を箇条書きで示してください。
1. スライドタイトル(1行)
2. そのスライドで伝えるべき一番重要なメッセージ(1文)
3. 使う要素(本文の箇条書き案/表/グラフ/図解 のどれが適切か)

## 含めるべき要素
- 現状の課題
- 施策の概要
- 想定コストと期待効果(数値は下記メモ内のものを使用し、勝手に数値を作らない)
- 実行スケジュール
- 想定される反対意見への回答

---
[ここに走り書きメモを貼り付け]
```

「勝手に数値を作らない」という一文は必須。AIは説得力を持たせるために、根拠のない数値や事例をもっともらしく補完してしまうことがあるため、事実は必ず自分のメモの範囲に限定させる。

### 手順1: Copilot in PowerPointで社内テンプレートを保ったまま作る

1. PowerPoint(デスクトップ版またはWeb版)で、会社の標準テンプレート(.potx)を開く
2. 画面右側のCopilotアイコン、またはキャンバス上に表示される文脈型の提案から起動(2026年に入りリボンからキャンバス埋め込み型のUIへ移行が進んでいる)
3. 「新しいプレゼンテーションを作成」または既存スライドに対する指示を入力欄に入力。上記で作った構成案をそのまま貼り付けてもよい
4. 参照元としてWord・PDF・Excelファイルを添付でき、その内容を踏まえたスライドを生成できる
5. 生成後は通常のPowerPoint編集と同じ感覚で、フォント・配色・レイアウトを手直しする。スピーカーノートの生成や、既存デックの再フォーマットも依頼できる

### 手順2: Claude for PowerPoint/Excelでデータ分析からスライド化までを一気通貫にする

1. Microsoft Marketplaceから「Claude for Excel」「Claude for PowerPoint」を導入する(利用には有料のClaudeプラン=Pro/Max/Team/Enterpriseが必要。アドイン自体のインストールは無料)
2. Excelで会話形式のパネルを開き、集計・分析をClaudeに依頼する
3. 同じ会話の文脈を保ったままPowerPointに移り、「今の分析結果を踏まえてスライド3枚にまとめて」のように依頼すると、Excel側の会話内容を引き継いだままスライドを生成できる
4. 会話画面(Claude.ai)だけで完結させたい場合は、チャットに「この内容を.pptxファイルにして」と頼むだけでも直接ファイルが生成される(2026年2月11日以降は無料プランでも利用可、ファイルサイズはアップロード・ダウンロードとも1ファイル30MBまで)

### 手順3: Gemini in Google Slidesでゼロからデッキを作る

1. Google Slidesで新規プレゼンテーションを開く(または既存のGoogleドライブのファイル一覧から「Geminiで作成」を選ぶ)
2. 画面右側のGeminiサイドパネルにプロンプトを入力。2026年6月のアップデート以降、生成されたスライドは画像ではなく通常のGoogle Slidesと同じ「編集可能な要素」で構成されるようになった。ただし2026年8月時点でもスライド生成機能自体の入力言語は英語限定のため、日本語で運用する場合は英語で構成案を渡すか、別途翻訳して入力する
3. 「関連するファイルを追加」でDrive内の参照資料を指定したり、既存の別デックを「このスタイルに合わせて」と指定したりできる
4. 生成前にスライドの構成(目次段階)が提示されるので、内容を確認・修正してから本生成に進む
5. 生成されたスライドは通常のGoogle Slidesファイルとして、そのまま共同編集・コメントができる

### 手順4: Gamma・Canva Magic Design・Genspark AI Slidesでとにかく速く体裁を整える

いずれも「プロンプトまたは既存テキストを貼り付け→デザインテンプレートを選択→自動生成→気に入らない部分だけ個別に調整」という流れは共通。Gammaはテキスト量に応じて自動でスライド枚数を提案する点、Canva Magic Designはブランドキット(自社のロゴ・配色・フォントのセット)を登録しておくと以後の生成に自動反映される点、Gensparkは調査・データ収集からスライド生成までを1つのエージェントに任せられる点が特徴。生成後は.pptx/.pdfとして書き出し、必要に応じてPowerPointやGoogle Slidesに読み込んで最終調整する。

### 料金の目安(2026年8月時点、要最新確認)

| ツール | 目安価格 | 備考 |
|---|---|---|
| Claude(チャットでの直接ファイル生成) | 無料プランで利用可(2026年2月11日〜) | ファイルサイズ上限は1ファイルあたり30MB。より高度な用途や大量利用ならPro(月20ドル)以上 |
| Claude for Excel/PowerPoint/Word(アドイン) | インストール自体は無料。利用には有料プランが必要(Pro 月20ドル/Max 月100ドル/Team・Enterprise) | Microsoft Marketplaceから導入。Outlookはベータ |
| Copilot in PowerPoint | Microsoft 365 Copilot ライセンスに含まれる。法人向けCopilot単体は月21ドル/ユーザー程度(バンドル込みのBusiness Standard+Copilotは月23.50ドル程度〜)、個人向けはMicrosoft 365 Premium(月19.99ドル程度)にCopilotが含まれる | 会社の既存Microsoft 365契約に追加する形が一般的。価格改定が多いため契約前に要確認 |
| ChatGPT for PowerPoint | Free〜Enterprise/Edu/Teachers/K-12まで全プランでアドイン自体は利用可 | Business/Enterprise向けには2026年8月6日まで無料提供。以降はExcel/Sheets向けアドインと同様のトークン従量課金に移行予定 |
| Gemini in Google Slides | Google Workspace Business Standard以上(年払いで月14ドル程度〜)、または個人向けGoogle AI Pro(月19.99ドル程度)/Ultraに含まれる | スライド生成機能自体は英語入力のみ対応 |
| Gamma | 無料(400クレジット、透かし付き、都度付与ではなく一回きり)/Plus 月8〜10ドル程度(年払い、月1,000クレジット)/Pro 月18〜20ドル程度/Ultra 月90ドル程度(年払い) | クレジット制。画像生成やエクスポート形式により消費量が変わる。チーム利用は1シートあたり月20ドル |
| Canva Magic Design | 無料プランあり/Canva Pro 月1,180円(月払い)、年払いなら月692円相当 | Pro以上でブランドキット・全AI機能が解放 |
| Genspark(AI Slides含む統合ワークスペース) | 無料プランあり/Plus 月24.99ドル/Pro 月249.99ドル | スライド専用ツールではなく、リサーチ・データ分析等を含む統合エージェントの一部。価格は2026年内の期間限定レートの可能性があり要確認 |
| Napkin | 無料プランあり(透かし・エクスポート制限あり)/Plus 月12ドル/Pro 月30ドル | 図解1枚単位の生成に強く、デッキ全体の生成用途ではない |

料金・上限は改定が頻繁なため、契約前に必ず各社の公式料金ページで最新値を確認すること。特にChatGPT for PowerPointは2026年8月6日の無料提供終了後の従量課金移行が近いため、法人利用ではコスト影響を早めに確認しておきたい。

## 注意点・よくある誤解

- **「見た目が整った=完成」ではない**: Gamma・Canva等が出す一次生成物は見栄えが良いため、そのまま提出したくなるが、フォントサイズの不揃い、行間の詰まりすぎ、画像とテキストの重なりなど、人間の目で見て初めて気づく体裁崩れが高確率で残る。最終提出前に必ず全スライドを通しで見る工程を挟む。
- **AIはブランド・社風の機微を読めない**: 「うちの会社らしい真面目なトーン」「役員会議で好まれる簡潔な書き方」といった、明文化されていない社内の空気はAIには伝わらない。テンプレートやトーンの指定を具体的に(「装飾的な言い回しを避け、結論から書く」等)言語化するか、過去の評価の高かった資料をサンプルとして読み込ませて模倣させる必要がある。
- **グラフ・数値は鵜呑みにしない**: AIにグラフ生成やデータの可視化を頼むと、元データの読み違いや、それらしい数値の補完(ハルシネーション)が起きることがある。特に金額・パーセンテージ・比較対象の軸は、必ず元データと突き合わせて検算する。「見た目のグラフ」と「正しいグラフ」は別物と心得る。
- **社内の未公表情報をそのまま貼り付けない**: 売上見込み・人事情報・顧客の個人情報などを含むメモを外部のAIプレゼンツールに貼り付ける前に、自社の利用規約・データ取り扱いルールを確認する。特に無料プランは学習利用の可否がツールによって異なるため要確認。詳細は[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)を参照。
- **「AI特化ツールで作った資料」は社内標準フォーマットと体裁が揃わない**: GammaやCanvaで作ったスライドをそのまま社内資料集に混ぜると、フォント・配色が浮いて見える。社内向けの継続利用資料は、最初からCopilot in PowerPoint・Gemini in Google Slides・Claude for PowerPointのように「自社テンプレート内で生成する」ツールを選ぶ方が手直しが少ない。
- **無料での提供条件は期間限定であることが多い**: ChatGPT for PowerPointの法人向け無料提供(2026年8月6日まで)のように、新機能は「まず無料開放して普及させ、後から従量課金に移行する」パターンが多い。無料期間中に業務フローへ組み込むと、課金開始後にコストが急増することがあるため、契約前に課金移行の予定時期を確認しておく。
- **一発生成で終わらせず、部分修正を繰り返す**: どのツールも、全体を作り直させるより「このスライドだけ」「この箇条書きだけ」と対象を絞って修正を依頼した方が、意図した仕上がりに早く近づく。

## 最初の一歩

直近で作る予定の資料のメモ(箇条書きで構わない)を1つ用意し、本ページの「コピペで使えるプロンプト例」を使ってChatGPT・Claude・Geminiのいずれかにスライド構成案を作らせてみる。出てきた構成の中で、数値や事実関係の記載がある箇所だけを、自分のメモと突き合わせて検算してみる。

## 関連トピック

- [生成AIによる文章作成・編集の実務活用](./ai-writing-and-editing.md)
- [生成AIに向く業務・向かない業務の切り分け](./ai-task-suitability.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-08-02: ツール横断の対応表と料金を最新化
- **内容**: Claudeのファイル直接生成(2026年2月11日に無料プラン含む全ユーザーへ解放)およびExcel/Word/PowerPointアドイン(2026年5月7日提供開始)を新たな選択肢として追加。ChatGPT for PowerPointの一般提供(2026年5月21日)と無料提供終了予定(2026年8月6日)、Gemini in Google Slidesの編集可能スライド化(2026年6月)と英語限定の現状、Copilot/Gemini/Gamma/Canva/Napkinの料金、Genspark AI Slidesの新規追加を反映して使いどころ表・手順・料金表・注意点を全面的に更新した
- **出典**: [Claude Help Center: Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)、[Claude by Anthropic: Claude can now create and edit files](https://claude.com/blog/create-files)、[Claude Help Center: Work across Microsoft 365 apps](https://support.claude.com/en/articles/13892150-work-across-microsoft-365-apps)、[findskill.ai: Claude Can Now Create PowerPoints and Spreadsheets — For Free](https://findskill.ai/blog/claude-free-file-creation-2026/)、[Google Workspace Updates: Create fully native and editable presentations with Gemini in Google Slides](https://workspaceupdates.googleblog.com/2026/06/create-fully-native-and-editable-presentations-with-Gemini-in-Google-Slides.html)、[note: Gemini×Google Slidesで「編集可能なスライド」を自動生成](https://note.com/comix_ceo162230/n/n7603cd0b440a?hl=en)、[Google Workspace Blog: July 2026 Workspace update](https://workspace.google.com/blog/product-announcements/july-2026-workspace-feature-drop)、[Let's Data Science: OpenAI Makes ChatGPT for PowerPoint Generally Available](https://letsdatascience.com/news/openai-makes-chatgpt-for-powerpoint-generally-available-a5fc0a3e)、[Deckary: ChatGPT for PowerPoint 2026](https://deckary.com/blog/chatgpt-for-powerpoint)、[eesel AI: Gamma pricing in 2026](https://www.eesel.ai/blog/gamma-pricing)、[note: Canva Proの最新料金(2025年)](https://note.com/bacon2/n/n14ea2d0292ec?hl=en)、[felloai: Genspark AI Pricing 2026](https://felloai.com/genspark-ai-pricing/)、[SoftwareSuggest: Napkin AI Pricing (2026)](https://www.softwaresuggest.com/napkin-ai/pricing)、[gosearch.ai: Microsoft Copilot Pricing 2026](https://www.gosearch.ai/blog/microsoft-copilot-pricing/)

### 2026-07-06: 初版執筆
- **内容**: プレゼン資料・ドキュメント作成における生成AI活用の全体像を整理。チャットAIでの構成壁打ち、Copilot in PowerPoint、Gemini in Google Slides、Gamma・Canva Magic Design・Napkin等のプレゼン特化ツールの使い分け表、箇条書きメモをスライド構成に変換するコピペ用プロンプト、ツール別の具体手順、料金目安、デザイン仕上げ・データ検算・ブランドトーンに関する注意点をまとめた
- **出典**: [Microsoft Support: Create a new presentation with Copilot in PowerPoint](https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d)、[Microsoft PowerPoint: AI PowerPoint Generator](https://www.microsoft.com/en-us/microsoft-365/powerpoint/ai-powerpoint-generator)、[Google Workspace Updates: Create fully native and editable presentations with Gemini in Google Slides](https://workspaceupdates.googleblog.com/2026/06/create-fully-native-and-editable-presentations-with-Gemini-in-Google-Slides.html?m=1)、[Google Docs Editors Help: Generate a slide with Gemini in Google Slides](https://support.google.com/docs/answer/16961475?hl=en)、[Google blog: New ways to create faster with Gemini in Docs, Sheets, Slides and Drive](https://blog.google/products-and-platforms/products/workspace/gemini-workspace-updates-march-2026/)、[Gamma: Plans and pricing](https://gamma.app/pricing)、[Canva: Magic Design](https://www.canva.com/magic-design/)、[Canva: AI Presentation Maker](https://www.canva.com/create/ai-presentations/)、[Napkin AI](https://www.napkin.ai/)、[OpenAI Help Center: ChatGPT for PowerPoint](https://help.openai.com/en/articles/20001242-chatgpt-for-powerpoint)、[ChatGPT for PowerPoint](https://chatgpt.com/apps/powerpoint/)
