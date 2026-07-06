---
title: 生成AIによるプレゼン資料・ドキュメント作成の実務活用
part: 11
chapter: 第3章 資料・ビジュアル作成
tags: [プレゼン資料, スライド作成, PowerPoint, Google Slides, Gamma, Copilot, Gemini]
created: 2026-07-06
updated: 2026-07-06
---

# 生成AIによるプレゼン資料・ドキュメント作成の実務活用

## これは何か

「明日までにこの企画をスライド15枚にまとめて」という仕事は、白紙のスライドとにらめっこする時間が最も苦痛な業務の一つである。生成AIは、箇条書きのメモやレポートを「章立て(アウトライン)→スライド構成→見た目のあるスライド」まで一気に引き上げてくれる。ChatGPT・GeminiのようなチャットAIで構成を練るところから、Copilot in PowerPointやGemini in Google Slidesのように実際にスライドファイルを生成するツール、Gamma・Canva Magic Design・Napkinのようなプレゼン特化AIツールまで選択肢が広がっており、「何を」「どのツールで」作らせるかを使い分けられるようになっておくと、資料作成の時間の大半を占める「叩き台作り」を大幅に圧縮できる。

## 仕組み・背景

生成AIによるスライド作成には、大きく分けて2つのアプローチがある。

1つ目は「文章生成の延長」。AIはまず文章(章立て・見出し・箇条書き)を生成するのが得意で、これをスライドの「骨格」として使う。ChatGPTやClaudeにアウトラインを作らせてから、それをPowerPointやGoogle Slidesに手で移す、あるいはCopilot・Geminiの機能に読み込ませて肉付けさせる、という流れがこれにあたる。

2つ目は「レイアウト・デザインテンプレートへの流し込み」。Gamma・Canva Magic Design・Napkinのようなプレゼン特化ツールは、あらかじめ用意された数百〜数千のデザインテンプレート(配色・フォント・図版のレイアウトのセット)に、AIが生成した文章と画像を自動で流し込む仕組みを持つ。「AIが一からデザインを考えている」わけではなく、「AIが文章構成と画像を作り、テンプレートエンジンがそれを整形している」と理解しておくと、なぜ複数のAI生成スライドが似た雰囲気になりがちなのか(同じテンプレート資産を使い回しているため)が腑に落ちる。

もう一つの前提は、AIの得意・不得意が「文章生成」と「精密なビジュアル生成」で大きく異なるという点。文章の要約・構造化(見出しと箇条書きへの分解)は生成AIの得意領域だが、「正確な数値に基づいたグラフ」「ブランドガイドラインに完全準拠したデザイン」「1px単位の体裁の調整」は不得意で、最終的には人の目によるチェックと手直しが前提になる。

## 使いどころ・使い分け

| 状況・目的 | 向いているツール | 理由・使い方の要点 |
|---|---|---|
| まず構成・アウトラインだけ壁打ちしたい(スライド枚数はまだ決めていない) | ChatGPT / Claude / Geminiのチャット | ファイルを作る前に、章立て・メッセージの流れ・想定質問への答えを言語化する段階。ファイル生成機能に頼るより、対話で骨子を練り込んだ方が手戻りが少ない |
| 社内のPowerPoint標準フォーマット(会社ロゴ・配色テンプレート)を崩したくない資料 | Copilot in PowerPoint | 既存の会社テンプレート(.potx)を開いた状態でCopilotに指示すれば、そのテンプレートのレイアウト・配色を保ったまま中身を生成・追記できる。ゼロからデザインし直されるリスクが低い |
| Google Slidesで完結させたい(共同編集前提、Drive内の資料を根拠にしたい) | Gemini in Google Slides | サイドパネルのプロンプトから、Drive内の他ファイルを参照させたり、既存デックのスタイルを踏襲させたりしながら、複数枚のスライドを一括生成できる。生成後もGoogle Slidesとして通常通り共同編集できる |
| ゼロから見た目の良いスライドを最速で立ち上げたい(社内フォーマットの制約がない、提案書・ウェビナー資料など) | Gamma、Canva Magic Design | 洗練されたテンプレートに自動で流し込んでくれるため、体裁を考える時間をほぼゼロにできる。ただし社内標準フォーマットとは体裁が異なるため、社外向け・単発の資料向き |
| スライド中の1枚だけ、図解(フローチャート・比較表・ロードマップ等)が欲しい | Napkin等の text-to-visual ツール | テキストの構造を渡すと図解案を複数提示してくれる。PowerPoint/Google Slidesへの部分的な貼り込み用途に向く。デッキ全体の生成には使わない |
| ChatGPTで作った文章をそのままPowerPointファイルにしたい | ChatGPT for PowerPoint(アドイン)、またはChatGPTの直接.pptx出力 | PowerPoint内のアドインとして使うと編集可能なスライド構造を保った生成ができる。チャット画面だけで済ませたい場合は.pptx書き出し機能もあるが、体裁は簡素になりやすい |
| 既存のWord資料・Excelデータを土台にスライド化したい | Copilot in PowerPoint(ファイル取り込み) | Word・PDF・Excelを最大5ファイルまで読み込ませて、その内容を基にデッキを組み立てさせられる。ゼロから書き起こす手間を省ける |

判断の軸は2つ。「社内フォーマットへの準拠が必須か」(必須ならCopilot/Gemini、自由でよいならGamma系)と、「まだ構成が固まっていないか、もう構成は決まっていて見た目だけ欲しいか」(前者はチャットで壁打ち、後者はファイル生成ツール)。

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
2. リボンの「ホーム」タブ右上、または画面右側のCopilotアイコンから起動
3. 「新しいプレゼンテーションを作成」または既存スライドに対する指示を入力欄に入力。上記で作った構成案をそのまま貼り付けてもよい
4. 参照元としてWord・PDF・Excelファイルを最大5つまで添付でき、その内容を踏まえたスライドを生成できる
5. 生成後は通常のPowerPoint編集と同じ感覚で、フォント・配色・レイアウトを手直しする

### 手順2: Gemini in Google Slidesでゼロからデッキを作る

1. Google Slidesで新規プレゼンテーションを開く(または既存のGoogleドライブのファイル一覧から「Geminiで作成」を選ぶ)
2. 画面右側のGeminiサイドパネルにプロンプトを入力(2026年7月時点では英語での入力が中心。日本語プロンプトは今後の対応拡大を待つか、英語で構成案を渡す運用が無難)
3. 「関連するファイルを追加」でDrive内の参照資料を指定したり、既存の別デックを「このスタイルに合わせて」と指定したりできる
4. 生成前にスライドの構成(目次段階)が提示されるので、内容を確認・修正してから本生成に進む
5. 生成されたスライドは通常のGoogle Slidesファイルとして、そのまま共同編集・コメントができる

### 手順3: Gamma・Canva Magic Designでとにかく速く体裁を整える

いずれも「プロンプトまたは既存テキストを貼り付け→デザインテンプレートを選択→自動生成→気に入らない部分だけ個別に調整」という流れは共通。Gammaはテキスト量に応じて自動でスライド枚数を提案する点、Canva Magic Designはブランドキット(自社のロゴ・配色・フォントのセット)を登録しておくと以後の生成に自動反映される点が特徴。生成後は.pptx/.pdfとして書き出し、必要に応じてPowerPointやGoogle Slidesに読み込んで最終調整する。

### 料金の目安(2026年7月時点、要最新確認)

| ツール | 目安価格 | 備考 |
|---|---|---|
| Copilot in PowerPoint | Microsoft 365 Copilot ライセンスに含まれる(月額はプランにより変動) | 会社の既存Microsoft 365契約に追加する形が一般的 |
| Gemini in Google Slides | Google Workspace Business Standard以上、またはGoogle AI Pro/Ultra(個人向け)に含まれる | 2026年8月1日までは利用上限が緩和されたプロモーション期間 |
| Gamma | 無料(400クレジット、透かし付き)/Plus 8ドル程度/Pro 18ドル程度/月額(円換算は為替次第) | クレジット制。画像生成やエクスポート形式により消費量が変わる |
| Canva Magic Design | 無料プランあり/Canva Pro 月額1,300円程度〜 | Pro以上でブランドキット・全AI機能が解放 |
| Napkin | 無料(基本機能・透かしなしの範囲は要確認)/Pro 18ドル程度 | 図解1枚単位の生成に強く、デッキ全体の生成用途ではない |

料金・上限は改定が頻繁なため、契約前に必ず各社の公式料金ページで最新値を確認すること。

## 注意点・よくある誤解

- **「見た目が整った=完成」ではない**: Gamma・Canva等が出す一次生成物は見栄えが良いため、そのまま提出したくなるが、フォントサイズの不揃い、行間の詰まりすぎ、画像とテキストの重なりなど、人間の目で見て初めて気づく体裁崩れが高確率で残る。最終提出前に必ず全スライドを通しで見る工程を挟む。
- **AIはブランド・社風の機微を読めない**: 「うちの会社らしい真面目なトーン」「役員会議で好まれる簡潔な書き方」といった、明文化されていない社内の空気はAIには伝わらない。テンプレートやトーンの指定を具体的に(「装飾的な言い回しを避け、結論から書く」等)言語化するか、過去の評価の高かった資料をサンプルとして読み込ませて模倣させる必要がある。
- **グラフ・数値は鵜呑みにしない**: AIにグラフ生成やデータの可視化を頼むと、元データの読み違いや、それらしい数値の補完(ハルシネーション)が起きることがある。特に金額・パーセンテージ・比較対象の軸は、必ず元データと突き合わせて検算する。「見た目のグラフ」と「正しいグラフ」は別物と心得る。
- **社内の未公表情報をそのまま貼り付けない**: 売上見込み・人事情報・顧客の個人情報などを含むメモを外部のAIプレゼンツールに貼り付ける前に、自社の利用規約・データ取り扱いルールを確認する。特に無料プランは学習利用の可否がツールによって異なるため要確認。詳細は[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)を参照。
- **「AI特化ツールで作った資料」は社内標準フォーマットと体裁が揃わない**: GammaやCanvaで作ったスライドをそのまま社内資料集に混ぜると、フォント・配色が浮いて見える。社内向けの継続利用資料は、最初からCopilot in PowerPointやGemini in Google Slidesのように「自社テンプレート内で生成する」ツールを選ぶ方が手直しが少ない。
- **一発生成で終わらせず、部分修正を繰り返す**: どのツールも、全体を作り直させるより「このスライドだけ」「この箇条書きだけ」と対象を絞って修正を依頼した方が、意図した仕上がりに早く近づく。

## 最初の一歩

直近で作る予定の資料のメモ(箇条書きで構わない)を1つ用意し、本ページの「コピペで使えるプロンプト例」を使ってChatGPTかGeminiにスライド構成案を作らせてみる。出てきた構成の中で、数値や事実関係の記載がある箇所だけを、自分のメモと突き合わせて検算してみる。

## 関連トピック

- [生成AIによる文章作成・編集の実務活用](./ai-writing-and-editing.md)
- [生成AIに向く業務・向かない業務の切り分け](./ai-task-suitability.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: プレゼン資料・ドキュメント作成における生成AI活用の全体像を整理。チャットAIでの構成壁打ち、Copilot in PowerPoint、Gemini in Google Slides、Gamma・Canva Magic Design・Napkin等のプレゼン特化ツールの使い分け表、箇条書きメモをスライド構成に変換するコピペ用プロンプト、ツール別の具体手順、料金目安、デザイン仕上げ・データ検算・ブランドトーンに関する注意点をまとめた
- **出典**: [Microsoft Support: Create a new presentation with Copilot in PowerPoint](https://support.microsoft.com/en-us/office/create-a-new-presentation-with-copilot-in-powerpoint-3222ee03-f5a4-4d27-8642-9c387ab4854d)、[Microsoft PowerPoint: AI PowerPoint Generator](https://www.microsoft.com/en-us/microsoft-365/powerpoint/ai-powerpoint-generator)、[Google Workspace Updates: Create fully native and editable presentations with Gemini in Google Slides](https://workspaceupdates.googleblog.com/2026/06/create-fully-native-and-editable-presentations-with-Gemini-in-Google-Slides.html?m=1)、[Google Docs Editors Help: Generate a slide with Gemini in Google Slides](https://support.google.com/docs/answer/16961475?hl=en)、[Google blog: New ways to create faster with Gemini in Docs, Sheets, Slides and Drive](https://blog.google/products-and-platforms/products/workspace/gemini-workspace-updates-march-2026/)、[Gamma: Plans and pricing](https://gamma.app/pricing)、[Canva: Magic Design](https://www.canva.com/magic-design/)、[Canva: AI Presentation Maker](https://www.canva.com/create/ai-presentations/)、[Napkin AI](https://www.napkin.ai/)、[OpenAI Help Center: ChatGPT for PowerPoint](https://help.openai.com/en/articles/20001242-chatgpt-for-powerpoint)、[ChatGPT for PowerPoint](https://chatgpt.com/apps/powerpoint/)
