---
title: 生成AIによるプレゼン資料・ドキュメント作成の実務活用
part: 12
chapter: 第3章 資料・ビジュアル作成
tags: [プレゼン資料, スライド作成, PowerPoint, Google Slides, Gamma, Copilot, Gemini, Claude]
created: 2026-07-06
updated: 2026-09-28
---

# 生成AIによるプレゼン資料・ドキュメント作成の実務活用

## これは何か

「明日までにこの企画をスライド15枚にまとめて」という仕事は、白紙のスライドとにらめっこする時間が最も苦痛な業務の一つである。生成AIは、箇条書きのメモやレポートを「章立て(アウトライン)→スライド構成→見た目のあるスライド」まで一気に引き上げてくれる。ChatGPT・Gemini・ClaudeのようなチャットAIで構成を練るところから、Copilot in PowerPoint・Gemini in Google Slides・Claude for PowerPointのように実際にスライドファイルを生成・編集するツール、Gamma・Canva Magic Design・Genspark・Napkinのようなプレゼン特化AIツールまで選択肢が広がっている。2026年に入ってからは、これらのツールが「提案するだけ」から「ファイルへ直接書き込んで仕上げる」エージェント型に切り替わりつつあり、「何を」「どのツールで」「どこまで自動で任せるか」を使い分けられるようになっておくと、資料作成の時間の大半を占める「叩き台作り」を大幅に圧縮できる。

## 仕組み・背景

生成AIによる資料作成には、大きく分けて3つのアプローチがある。

1つ目は「文章生成の延長」。AIはまず文章(章立て・見出し・箇条書き)を生成するのが得意で、これをスライドの「骨格」として使う。ChatGPT・Claude・Geminiにアウトラインを作らせてから、それをPowerPointやGoogle Slidesに手で移す、あるいは各社の機能に読み込ませて肉付けさせる、という流れがこれにあたる。

2つ目は「レイアウト・デザインテンプレートへの流し込み」。Gamma・Canva Magic Design・Genspark・Napkinのようなプレゼン特化ツールは、あらかじめ用意された数百〜数千のデザインテンプレート(配色・フォント・図版のレイアウトのセット)に、AIが生成した文章と画像を自動で流し込む仕組みを持つ。「AIが一からデザインを考えている」わけではなく、「AIが文章構成と画像を作り、テンプレートエンジンがそれを整形している」と理解しておくと、なぜ複数のAI生成スライドが似た雰囲気になりがちなのか(同じテンプレート資産を使い回しているため)が腑に落ちる。

3つ目が、2026年に入って急速に広がった「エージェントによる直接操作」。Microsoft Copilotの「エージェント モード」は2026年4月22日に一般提供され、これまでのように文章案を提示して人が貼り直す方式から、Copilotがスライドの構成変更・翻訳・グラフ更新などを指示に従って直接ファイルへ実行する方式に変わった(会議・メール・過去資料からの文脈把握=Work IQによるグラウンディングも組み込まれている)。同様にAnthropicは2026年7月7日、Claudeの「Microsoft 365コネクタ」に書き込み機能を追加し、管理者の許可があれば、ClaudeがOneDrive・SharePoint上のファイルを直接作成・更新できるようになった。「チャットで壁打ち」「アドインでファイルを操作」「バックグラウンドでエージェントがファイルへ書き込む」の3層が同じ会話の延長でできるようになり、ツール間を移動するコストが下がっている点が2025年までとの大きな違いである。

もう一つの前提は、AIの得意・不得意が「文章生成」と「精密なビジュアル生成」で大きく異なるという点。文章の要約・構造化(見出しと箇条書きへの分解)は生成AIの得意領域だが、「正確な数値に基づいたグラフ」「ブランドガイドラインに完全準拠したデザイン」「1px単位の体裁の調整」は不得意で、最終的には人の目によるチェックと手直しが前提になる。エージェント化が進んでも、この不得意領域自体は変わっていない。

なお、ChatGPTは2026年5月28日に、チャット画面に埋め込まれていた「Canvas」(文章・コードを別パネルで編集する機能)を廃止し、その役割を通常のチャット応答内の「ライティングブロック」「コードブロック」に統合した。資料・ドキュメント作成の実体は、①チャット単体での下書き(ライティングブロック、書き出しはPDF・Word形式まで)、②ChatGPT Work(2026年7月提供開始。Google Workspace連携時はGoogleドキュメント・スプレッドシート・スライドをネイティブ形式で作成でき、Excelはアドイン経由。2026年9月時点ではPowerPoint単体のネイティブ生成はこのWorkのフローには含まれない)、③ChatGPT for PowerPoint(PowerPoint単体のアドイン)、の3つの経路に分かれていることを踏まえて使い分ける必要がある。

## 使いどころ・使い分け

| 状況・目的 | 向いているツール | 理由・使い方の要点 |
|---|---|---|
| まず構成・アウトラインだけ壁打ちしたい(スライド枚数はまだ決めていない) | ChatGPT / Claude / Geminiのチャット | ファイルを作る前に、章立て・メッセージの流れ・想定質問への答えを言語化する段階。ファイル生成機能に頼るより、対話で骨子を練り込んだ方が手戻りが少ない |
| 社内のPowerPoint標準フォーマット(会社ロゴ・配色テンプレート)を崩したくない資料、かつ既存デックの更新・翻訳・再構成まで任せたい | Copilot in PowerPoint(エージェント モード)、Claude for PowerPoint | Copilotのエージェント モードは、会社のBrand Kit(ロゴ・配色・フォントのセット)を適用したまま、指示どおりにスライドを直接書き換える。ただし多段階の変更履歴を追うため、ファイルがOneDrive/OneDrive for Business/SharePointに保存されていることが前提。Claude for PowerPointも既存の.potxテンプレートを保った生成・追記ができる |
| Google Slidesで完結させたい(共同編集前提、Drive内の資料を根拠にしたい) | Gemini in Google Slides | サイドパネルのプロンプトから、Drive内の他ファイルを参照させたり、既存デックのスタイルを踏襲させたりしながら、複数枚のスライドを一括生成できる。生成後もGoogle Slidesとして通常通り共同編集できる。ただし2026年9月時点でも、この複数枚一括生成機能の入力・出力は英語(米国)限定(日本語対応の時期は未発表) |
| Excel分析→PowerPoint報告のように、複数のOfficeアプリをまたいで1つの作業を仕上げたい | Claude for Excel/PowerPoint(会話コンテキストの引き継ぎ) | Excelでデータ分析した会話の文脈を保ったまま、そのままPowerPointで結果をスライド化するよう指示できる。ファイル間でのコピペ・状況説明のやり直しが不要になる |
| 定型レポートを、人が開かなくてもSharePoint/OneDrive上の所定フォルダに自動で置いてほしい | Claudeの Microsoft 365コネクタ(書き込み機能) | 2026年7月7日追加。管理者(Microsoft Entra)が許可した場合のみ有効になる機能で、既定はオフ。有効化されていれば、Claudeとの会話の中で「この内容をOneDriveの◯◯フォルダに保存して」のように指示し、ファイルの新規作成・更新までを任せられる |
| ゼロから見た目の良いスライドを最速で立ち上げたい(社内フォーマットの制約がない、提案書・ウェビナー資料など) | Gamma、Canva Magic Design、Genspark AI Slides | 洗練されたテンプレートに自動で流し込んでくれるため、体裁を考える時間をほぼゼロにできる。ただし社内標準フォーマットとは体裁が異なるため、社外向け・単発の資料向き |
| スライド中の1枚だけ、図解(フローチャート・比較表・ロードマップ等)が欲しい | Napkin等の text-to-visual ツール | テキストの構造を渡すと図解案を複数提示してくれる。PowerPoint/Google Slidesへの部分的な貼り込み用途に向く。デッキ全体の生成には使わない |
| チャットで作った文章をそのままプレゼン・文書ファイルにしたい | ChatGPT Work(Google Workspace連携時)、ChatGPT for PowerPoint(アドイン)、Claude for PowerPoint(アドイン)、またはClaudeへの直接依頼(.pptx直接出力) | どの経路を使うかで出力形式が変わる。Googleドキュメント/スライドで完結させたいならChatGPT WorkとGoogle Workspace連携、.pptxファイルそのものが欲しいならPowerPoint向けの各アドイン、チャット画面だけで済ませたいならClaudeの直接ファイル生成が手軽 |
| 既存のWord資料・Excelデータを土台にスライド化したい | Copilot in PowerPoint(ファイル取り込み・Work IQによる会議/メールからのグラウンディング)、Claude(会話に添付) | Word・PDF・Excelを読み込ませて、その内容を基にデッキを組み立てさせられる。Copilotの場合はさらに関連する会議やメールの文脈も自動で拾える。ゼロから書き起こす手間を省ける |

判断の軸は3つ。「社内フォーマットへの準拠が必須か」(必須ならCopilot/Gemini/Claudeのアドイン、自由でよいならGamma系)、「まだ構成が固まっていないか、もう構成は決まっていて見た目だけ欲しいか」(前者はチャットで壁打ち、後者はファイル生成ツール)、そして「AIにファイルへの書き込み権限そのものを与えてよいか」(Copilotのエージェント モードやClaudeのMicrosoft 365書き込み機能は、管理者の許可設定と保存場所の制約があるため、情報システム部門との事前調整が要る場合がある)。

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

### 手順1: Copilot in PowerPointでエージェント モードを使う

1. 対象のPowerPointファイルをOneDrive・OneDrive for Business・SharePointのいずれかに保存する(エージェント モードは複数手順の変更履歴をクラウド上で追跡するため、ローカル保存のみのファイルには使えない)
2. 会社の標準テンプレート(.potx)、または既存デックを開く
3. 画面右側のCopilotパネル、またはCopilot Chatから「PowerPoint」エージェントを@メンションして呼び出す
4. 「新しいプレゼンテーションを作成」、または「この3枚を英語に翻訳して、箇条書きを2行以内に短縮し、図版を左揃えにして」のような複数手順の指示を一度に入力する。Word・Excel・PDF・SharePoint上の資料、直近の会議・メールの内容(Work IQ)も参照材料にできる
5. 会社のBrand Kit(ロゴ・配色・フォントのセット)を登録しておけば、生成・編集のたびに自動で適用される
6. 生成後は通常のPowerPoint編集と同じ感覚で、フォント・配色・レイアウトを手直しする

### 手順2: Claude for PowerPoint/Excelでデータ分析からスライド化までを一気通貫にする

1. Microsoft Marketplaceから「Claude for Excel」「Claude for PowerPoint」を導入する(2026年5月7日に一般提供。利用には有料のClaudeプラン=Pro/Max/Team/Enterpriseが必要。アドイン自体のインストールは無料。Outlook向けは引き続きベータ)
2. Excelで会話形式のパネルを開き、集計・分析をClaudeに依頼する
3. 同じ会話の文脈を保ったままPowerPointに移り、「今の分析結果を踏まえてスライド3枚にまとめて」のように依頼すると、Excel側の会話内容を引き継いだままスライドを生成できる
4. 会話画面(Claude.ai)だけで完結させたい場合は、チャットに「この内容を.pptxファイルにして」と頼むだけでも直接ファイルが生成される(無料プランでも利用可、ファイルサイズはアップロード・ダウンロードとも1ファイル30MBまで)
5. 社内のSharePoint・OneDriveに置かれたファイルへ直接出力・更新したい場合は、管理者がMicrosoft 365コネクタの「書き込み機能」(2026年7月7日追加、既定オフ)を有効化しているかを確認する。有効であれば、会話の中で保存先フォルダを指定して直接ファイルを作成・更新できる

### 手順3: Gemini in Google Slidesでゼロからデッキを作る

1. Google Slidesで新規プレゼンテーションを開く(または既存のGoogleドライブのファイル一覧から「Geminiで作成」を選ぶ)。この一括生成機能はBusiness Standard/Plus、Enterprise Standard/Plus、個人向けGoogle AI Pro/Ultra、教育向けAI Pro等のプランで利用できる
2. 画面右上の「Geminiに相談」アイコンからプロンプトを入力する。2026年6月29日のロールアウト以降、生成されたスライドは画像ではなく通常のGoogle Slidesと同じ「編集可能な要素」で構成される。ただし2026年9月時点でもこの一括生成機能自体はパソコン・英語限定で、日本語での提供時期は未発表(サイドパネルでの個別スライドの文章改良・画像生成など一部機能は日本語でも利用可)
3. 「関連するファイルを追加」でDrive内の参照資料を指定したり、既存の別デックを「このスタイルに合わせて」と指定したりできる
4. 生成前にスライドの構成(目次段階)が提示されるので、内容を確認・修正してから本生成に進む
5. 生成されたスライドは通常のGoogle Slidesファイルとして、そのまま共同編集・コメントができる。なお2026年8月1日までの提供時にあった生成回数の優遇枠は終了しており、以降は通常のプラン別利用上限が適用される

### 手順4: Gamma・Canva Magic Design・Genspark AI Slidesでとにかく速く体裁を整える

いずれも「プロンプトまたは既存テキストを貼り付け→デザインテンプレートを選択→自動生成→気に入らない部分だけ個別に調整」という流れは共通。Gammaはテキスト量に応じて自動でスライド枚数を提案する点、Canva Magic Designはブランドキット(自社のロゴ・配色・フォントのセット)を登録しておくと以後の生成に自動反映される点、Gensparkは調査・データ収集からスライド生成までを1つのエージェントに任せられる点が特徴。生成後は.pptx/.pdfとして書き出し、必要に応じてPowerPointやGoogle Slidesに読み込んで最終調整する。

### 料金の目安(2026年9月時点、要最新確認)

| ツール | 目安価格 | 備考 |
|---|---|---|
| Claude(チャットでの直接ファイル生成) | 無料プランで利用可 | ファイルサイズ上限は1ファイルあたり30MB。より高度な用途や大量利用ならPro(月20ドル)以上 |
| Claude for Excel/PowerPoint/Word(アドイン)+Microsoft 365コネクタ(書き込み機能) | インストール自体は無料。利用には有料プランが必要(Pro 月20ドル/Max 月100ドル〜/Team Standard 月25ドル・年払い月20ドル/席/Team Premium 月125ドル・年払い月100ドル/席/Enterprise) | アドインはMicrosoft Marketplaceから導入。コネクタの書き込み機能は管理者の許可が別途必要 |
| Copilot in PowerPoint | Microsoft 365 Copilot(法人向けEnterprise相当)は月30ドル/ユーザー(年契約)、Business向けは月21ドル(2026年12月31日まで月18ドルに割引中)。個人向けはMicrosoft 365 Premium(月19.99ドル程度、旧Copilot Pro相当を統合)にCopilotが含まれる | 会社の既存Microsoft 365契約に追加する形が一般的。価格改定が多いため契約前に要確認 |
| ChatGPT Work(Docs/Sheets/Slidesのネイティブ生成)・ChatGPT for PowerPoint(アドイン) | Business/Enterpriseに含まれる。Plus/Proはプランに含まれる利用枠を消費し、枠を超えるとクレジット従量課金 | ChatGPT for PowerPointは2026年8月6日で無料提供期間が終了し、以降はトークン量に応じたクレジット従量課金(1タスクあたり目安10〜50クレジット、テンプレートの使い回し・キャッシュ活用でコストを下げられる)に移行した |
| Gemini in Google Slides | Google Workspace Business Standard(月14ドル程度〜、Gemini機能はプランに標準搭載でアドオン契約は不要)以上、または個人向けGoogle AI Pro(月19.99ドル)/AI Ultra(5x:月99.99ドル、20x:月199.99ドル)に含まれる | スライド一括生成機能自体は英語入力のみ対応 |
| Gamma | 個人向け: 無料(400クレジット)/Plus 月9ドル程度(年払い)/Pro 月18ドル程度(年払い)/Ultra 月90ドル程度(年払い)。チーム向け: Team 月240ドル/席(2席以上、月6,000クレジット)/Business 月480ドル/席(10席以上、月10,000クレジット) | クレジット制。追加クレジットは1,500クレジットあたり6ドルで購入可能 |
| Canva Magic Design | 無料プランあり/Canva Pro 月1,180円(月払い)、年払いなら月692円相当 | Pro以上でブランドキット・全AI機能が解放 |
| Genspark(AI Slides含む統合ワークスペース) | 無料プランあり/Plus 月24.99ドル(年払い月19.99ドル)/Pro 月249.99ドル(年払い月199.99ドル)/Team 月30ドル/席(2〜150席、月12,000クレジット) | 2026年9月18日以降、Super Agent・AI Slides・AI Sheets・AI Docs等の標準モードタスクに無料クレジット枠が付与された(2026年12月31日までの条件付き) |
| Napkin | 無料プランあり(週500クレジット、透かし・エクスポート制限あり)/Plus 月9ドル/Pro 月22ドル | 図解1枚単位の生成に強く、デッキ全体の生成用途ではない |

料金・上限は改定が頻繁なため、契約前に必ず各社の公式料金ページで最新値を確認すること。特にChatGPT for PowerPointは無料提供終了後のクレジット従量課金に移行済みのため、法人利用ではコスト影響を早めに確認しておきたい。

## 注意点・よくある誤解

- **「見た目が整った=完成」ではない**: Gamma・Canva等が出す一次生成物は見栄えが良いため、そのまま提出したくなるが、フォントサイズの不揃い、行間の詰まりすぎ、画像とテキストの重なりなど、人間の目で見て初めて気づく体裁崩れが高確率で残る。最終提出前に必ず全スライドを通しで見る工程を挟む。
- **AIはブランド・社風の機微を読めない**: 「うちの会社らしい真面目なトーン」「役員会議で好まれる簡潔な書き方」といった、明文化されていない社内の空気はAIには伝わらない。テンプレートやトーンの指定を具体的に(「装飾的な言い回しを避け、結論から書く」等)言語化するか、過去の評価の高かった資料をサンプルとして読み込ませて模倣させる必要がある。
- **グラフ・数値は鵜呑みにしない**: AIにグラフ生成やデータの可視化を頼むと、元データの読み違いや、それらしい数値の補完(ハルシネーション)が起きることがある。特に金額・パーセンテージ・比較対象の軸は、必ず元データと突き合わせて検算する。「見た目のグラフ」と「正しいグラフ」は別物と心得る。
- **社内の未公表情報をそのまま貼り付けない**: 売上見込み・人事情報・顧客の個人情報などを含むメモを外部のAIプレゼンツールに貼り付ける前に、自社の利用規約・データ取り扱いルールを確認する。特に無料プランは学習利用の可否がツールによって異なるため要確認。詳細は[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)を参照。
- **「AI特化ツールで作った資料」は社内標準フォーマットと体裁が揃わない**: GammaやCanvaで作ったスライドをそのまま社内資料集に混ぜると、フォント・配色が浮いて見える。社内向けの継続利用資料は、最初からCopilot in PowerPoint・Gemini in Google Slides・Claude for PowerPointのように「自社テンプレート内で生成する」ツールを選ぶ方が手直しが少ない。
- **「チャットで作る」の意味がツールによって変わった**: ChatGPTは2026年5月28日にCanvas(別パネルでの編集機能)を廃止し、通常のチャット応答内の「ライティングブロック」に統合した。文書として書き出せるのはPDF・Word形式までで、.pptx/.xlsxそのものが欲しい場合は、Google Workspace連携時のChatGPT Work、またはPowerPoint専用のアドイン(ChatGPT for PowerPoint)といった別の経路を使う必要がある。「ChatGPTでスライドを作る」と一括りにせず、どの経路を使っているかを意識する。
- **エージェントの「書き込み権限」は既定オフで、管理者の許可が前提**: CopilotのAgentモードやClaudeのMicrosoft 365コネクタ書き込み機能は、いずれもファイルへの直接書き込みという強い権限を伴うため、既定では無効、または利用に組織の設定変更が必要になっている。情報システム部門が許可していない環境では、想定した自動化ができない・エラーになることがあるため、導入前に確認する。
- **無料での提供条件は期間限定であることが多い**: ChatGPT for PowerPointの法人向け無料提供(2026年8月6日まで)のように、新機能は「まず無料開放して普及させ、後から従量課金に移行する」パターンが多い。無料期間中に業務フローへ組み込むと、課金開始後にコストが急増することがあるため、料金体系の変更予定を定期的に確認する。
- **一発生成で終わらせず、部分修正を繰り返す**: どのツールも、全体を作り直させるより「このスライドだけ」「この箇条書きだけ」と対象を絞って修正を依頼した方が、意図した仕上がりに早く近づく。

## 最初の一歩

直近で作る予定の資料のメモ(箇条書きで構わない)を1つ用意し、本ページの「コピペで使えるプロンプト例」を使ってChatGPT・Claude・Geminiのいずれかにスライド構成案を作らせてみる。出てきた構成の中で、数値や事実関係の記載がある箇所だけを、自分のメモと突き合わせて検算してみる。

## 関連トピック

- [生成AIによる文章作成・編集の実務活用](./ai-writing-and-editing.md)
- [生成AIに向く業務・向かない業務の切り分け](./ai-task-suitability.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-09-28: エージェント化の進展と料金体系の変更を反映して全面更新
- **内容**: Copilot in PowerPointのエージェント モード一般提供(2026年4月22日、Brand Kit・Work IQによるグラウンディング・クラウド保存の必須化)、ClaudeのMicrosoft 365コネクタへの書き込み機能追加(2026年7月7日、管理者許可制でOneDrive/SharePointへ直接ファイル作成・更新)、ChatGPTのCanvas廃止(2026年5月28日)とChatGPT Work・ChatGPT for PowerPointへの機能分化、ChatGPT for PowerPointの無料提供終了(2026年8月6日)後のクレジット従量課金への移行、Gemini in Google Slidesの一括生成機能が2026年9月時点でも英語限定である現状、Microsoft 365 Copilot・Google Workspace(Gemini標準搭載化)・Google AI Ultra(5x/20xへの分割)・Gamma・Genspark・Napkinの料金改定を反映し、仕組み・背景/使いどころ・使い分け表/手順/料金表/注意点を全面的に更新した
- **出典**: [Microsoft AI at Work Blog: Copilot's agentic capabilities in Word, Excel, and PowerPoint are generally available](https://www.microsoft.com/en-us/copilot/blog/2026/04/22/copilots-agentic-capabilities-in-word-excel-and-powerpoint-are-generally-available/)、[Microsoft Community Hub: Using the Microsoft 365 Connector for Claude](https://techcommunity.microsoft.com/discussions/microsoft-365/using-the-microsoft-365-connector-for-claude/4509576)、[Claude Help Center: Connect to Microsoft 365](https://support.claude.com/en/articles/15183774-connect-to-microsoft-365)、[Claude Help Center: Set up the Microsoft 365 connector](https://support.claude.com/en/articles/12542951-set-up-the-microsoft-365-connector)、[ClaudeKit: Claude for Microsoft 365 — Excel, PowerPoint, and Word now GA, Outlook joins in beta](https://claudekit.io/en/updates/claude-for-microsoft-365/)、[Claude by Anthropic: Claude pricing](https://claude.com/pricing)、[OpenAI Help Center: ChatGPT Release Notes / Model Release Notes](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)、[AI Toolbox: ChatGPT Canvas in 2026: What Happened and What Replaced It](https://www.ai-toolbox.co/chatgpt-management-and-productivity/how-to-use-chatgpt-canvas-guide-2026)、[Windows News: Free ChatGPT in PowerPoint Has an Expiration Date: August 6, 2026](https://windowsnews.ai/article/free-chatgpt-in-powerpoint-has-an-expiration-date-august-6-2026.436927)、[Digital Applied: ChatGPT for PowerPoint Is GA: Automating Client Decks](https://www.digitalapplied.com/blog/chatgpt-powerpoint-agent-marketing)、[AIToolHunt: ChatGPT Work Docs, Sheets, and Slides Explained](https://aitoolhunt.co/blog/chatgpt-work-docs-spreadsheets-slides-2026)、[Google Workspace Updates: Create fully native and editable presentations with Gemini in Google Slides](https://workspaceupdates.googleblog.com/2026/06/create-fully-native-and-editable-presentations-with-Gemini-in-Google-Slides.html)、[Google ドキュメント エディタ ヘルプ: Gemini in Google スライドでスライドを生成する](https://support.google.com/docs/answer/16961475?hl=ja)、[itechguides: Google Workspace Gemini Included: Prices and Changes Now](https://www.itechguides.com/google-already-made-gemini-a-core-part-of-workspace-what-changed-and-what-it-costs-now/)、[Engadget: The Google AI Ultra plan now starts at $100 a month](https://www.engadget.com/2176060/the-google-ai-ultra-plan-now-starts-at-100-a-month/)、[gosearch.ai: Microsoft Copilot Pricing 2026](https://www.gosearch.ai/blog/microsoft-copilot-pricing/)、[eesel AI: Gamma pricing in 2026](https://www.eesel.ai/blog/gamma-pricing)、[Lindy: Genspark Pricing 2026](https://www.lindy.ai/blog/genspark-pricing)、[SoftwareSuggest: Napkin AI Pricing (2026)](https://www.softwaresuggest.com/napkin-ai/pricing)

### 2026-08-02: ツール横断の対応表と料金を最新化
- **内容**: Claudeのファイル直接生成(2026年2月11日に無料プラン含む全ユーザーへ解放)およびExcel/Word/PowerPointアドイン(2026年5月7日提供開始)を新たな選択肢として追加。ChatGPT for PowerPointの一般提供(2026年5月21日)と無料提供終了予定(2026年8月6日)、Gemini in Google Slidesの編集可能スライド化(2026年6月)と英語限定の現状、Copilot/Gemini/Gamma/Canva/Napkinの料金、Genspark AI Slidesの新規追加を反映して使いどころ表・手順・料金表・注意点を全面的に更新した
- **出典**: [Claude Help Center: Create and edit files with Claude](https://support.claude.com/en/articles/12111783-create-and-edit-files-with-claude)、[Claude by Anthropic: Claude can now create and edit files](https://claude.com/blog/create-files)、[Claude Help Center: Work across Microsoft 365 apps](https://support.claude.com/en/articles/13892150-work-across-microsoft-365-apps)、[findskill.ai: Claude Can Now Create PowerPoints and Spreadsheets — For Free](https://findskill.ai/blog/claude-free-file-creation-2026/)、[Google Workspace Updates: Create fully native and editable presentations with Gemini in Google Slides](https://workspaceupdates.googleblog.com/2026/06/create-fully-native-and-editable-presentations-with-Gemini-in-Google-Slides.html)、[note: Gemini×Google Slidesで「編集可能なスライド」を自動生成](https://note.com/comix_ceo162230/n/n7603cd0b440a?hl=en)、[Google Workspace Blog: July 2026 Workspace update](https://workspace.google.com/blog/product-announcements/july-2026-workspace-feature-drop)、[Let's Data Science: OpenAI Makes ChatGPT for PowerPoint Generally Available](https://letsdatascience.com/news/openai-makes-chatgpt-for-powerpoint-generally-available-a5fc0a3e)、[Deckary: ChatGPT for PowerPoint 2026](https://deckary.com/blog/chatgpt-for-powerpoint)、[eesel AI: Gamma pricing in 2026](https://www.eesel.ai/blog/gamma-pricing)、[note: Canva Proの最新料金(2025年)](https://note.com/bacon2/n/n14ea2d0292ec?hl=en)、[felloai: Genspark AI Pricing 2026](https://felloai.com/genspark-ai-pricing/)、[SoftwareSuggest: Napkin AI Pricing (2026)](https://www.softwaresuggest.com/napkin-ai/pricing)、[gosearch.ai: Microsoft Copilot Pricing 2026](https://www.gosearch.ai/blog/microsoft-copilot-pricing/)

### 2026-07-06: 初版執筆
- **内容**: プレゼン資料・ドキュメント作成における生成AI活用の全体像を整理。チャットAIでの構成壁打ち、Copilot in PowerPoint、Gemini in Google Slides、Gamma・Canva Magic Design・Napkin等のプレゼン特化ツールの使い分け表、箇条書きメモをスライド構成に変換するコピペ用プロンプト、ツール別の具体手順、料金目安、デザイン仕上げ・データ検算・ブランドトーンに関する注意点をまとめた
- **出典**: [Microsoft Support: Create a new presentation with Copilot in PowerPoint](https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d)、[Microsoft PowerPoint: AI PowerPoint Generator](https://www.microsoft.com/en-us/microsoft-365/powerpoint/ai-powerpoint-generator)、[Google Workspace Updates: Create fully native and editable presentations with Gemini in Google Slides](https://workspaceupdates.googleblog.com/2026/06/create-fully-native-and-editable-presentations-with-Gemini-in-Google-Slides.html?m=1)、[Google Docs Editors Help: Generate a slide with Gemini in Google Slides](https://support.google.com/docs/answer/16961475?hl=en)、[Google blog: New ways to create faster with Gemini in Docs, Sheets, Slides and Drive](https://blog.google/products-and-platforms/products/workspace/gemini-workspace-updates-march-2026/)、[Gamma: Plans and pricing](https://gamma.app/pricing)、[Canva: Magic Design](https://www.canva.com/magic-design/)、[Canva: AI Presentation Maker](https://www.canva.com/create/ai-presentations/)、[Napkin AI](https://www.napkin.ai/)、[OpenAI Help Center: ChatGPT for PowerPoint](https://help.openai.com/en/articles/20001242-chatgpt-for-powerpoint)、[ChatGPT for PowerPoint](https://chatgpt.com/apps/powerpoint/)
