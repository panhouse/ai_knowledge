---
title: ハルシネーションとは何か・対策
part: 4
chapter: 第3章 ハルシネーション対策
tags: [ハルシネーション, リスク管理, ファクトチェック, RAG]
created: 2026-07-05
updated: 2026-08-22
---

# ハルシネーションとは何か・対策

## これは何か

生成AIが、存在しない事実や文献をもっともらしい文章で答えてしまう現象を「ハルシネーション」(hallucination、幻覚)と呼ぶ。厄介なのは、嘘だとわかる書き方ではなく、本当の事実と同じ自信度・同じ文体で出力される点にある。読者が「変だな」と気づけないまま資料や顧客対応にそのまま使ってしまうと、存在しない判例を裁判所に提出して弁護士が制裁を受けたケースや、航空会社のチャットボットが誤った規定を案内して敗訴したケース(Moffatt v. Air Canada, 2024年)のように、実害のある事故につながる。生成AIを業務で使うなら、ハルシネーションは「まれに起きる不具合」ではなく「常に一定確率で起きる仕様」として、検知・防止の仕組みをセットで運用する必要がある。

## 仕組み・背景

ハルシネーションが起きる理由は、生成AIの仕組みそのものに根ざしている。

- **次に来そうな言葉を予測しているだけ**: 大規模言語モデル(LLM、大量のテキストで学習した言語生成AI)は「事実データベースを検索して答える」のではなく、「文脈から統計的にもっともらしい次の単語」を並べて文章を作る。学習データに答えがそのまま存在しない質問でも、文体としては自然な回答を生成できてしまう。
- **「わからない」と言うより、それらしく答える方が評価で得をする**: OpenAIが2025年に公開した研究では、モデルの学習・評価の仕組み自体が「自信を持って(誤っていても)答える」ことを「わかりません」と答えるよりも高く評価してしまう構造になっていると指摘されている。試験で答えがわからなくても空欄より適当に書いた方が得点が入りやすいのと同じ構造で、モデルは「推測してでも答える」方向に最適化されやすい。
- **知識のカットオフと情報の欠落**: モデルは学習時点までの情報しか「知識」として持たない。学習データにない最新の出来事・社内限定の情報・ニッチな統計値を聞かれると、近そうな情報から推測で埋めてしまう。
- **数値・固有名詞は特に弱い**: 文章の流れとしての自然さは得意でも、「厳密に1つだけ正しい値」を要求される数値計算・日付・URL・文献の書誌情報などは、似た形式のもっともらしい値を作文してしまいやすい。
- **独立系ベンチマークでも「ゼロにはならない」ことが確認されている**: Vectaraのハルシネーション評価(HHEM、要約タスクで事実と矛盾する内容が混じっていないかを測る指標)の定番リーダーボード(HHEM-2.3、7,700件超の記事で評価)は2026年5月時点で、上位のAntgroup/Finix S1が1.8%、OpenAI/GPT-5.4-nanoが3.1%、Google/Gemini 2.5 Flash-Liteが3.3%という結果で、下位はMistral AI/Ministral 3 3Bが24.2%、Microsoft/Phi-4-mini-instructが23.5%、OpenAI/o3-proが23.3%だった。これに加えて、より長く難易度の高い記事(最大32Kトークン)を使う次世代版ベンチマーク(HHEM単体に加え、判定を厳しくしたFaithJudgeという評価軸も併用)では、単純な要約設定でもClaude・GPT・Grok・Geminiの最新世代モデルの多くが10%を超える幻覚率を記録しており、ベンチマークの難易度を上げるほど幻覚率は跳ね上がる。「最新の高性能モデルだから起きない」とは言えない。
- **測るタスクによって数字がまったく変わる**: 同じ最新モデルでも、手元の資料を要約させるグラウンディングされたタスクでは幻覚率が数%に収まる一方、外部資料なしで知識だけを問うタスク(AA-Omniscienceのようなベンチマーク)では正答率が数十%にとどまり、裏を返せば残りの大半が誤り(幻覚)という結果が珍しくない。集計元によって具体的な順位や数値の報告に幅があるが、「要約では優秀」「知識問答では低調」という同一モデル内のギャップ自体は複数のベンチマークで一貫して確認されている。「幻覚率◯%」という数字を見るときは、必ず「何を測った数字か(要約か、素の知識問答か)」を確認する。
- **「賢いモデル」ほど安全とは限らない**: OpenAIは2026年に入りGPT-5.2からGPT-5.5 Instant、GPT-5.6と段階的にモデルを改良し、GPT-5.5では医療・法律・金融のような高リスク領域のプロンプトで幻覚を最大52.5%削減したと発表した。2026年8月にリリースされたGPT-5.6では、評価方法自体も変更され、ユーザーが「事実の誤りがある」と実際に報告した過去のChatGPT会話を再現させ、同じ誤りを繰り返すかどうかを測る手法が使われている。この評価でGPT-5.6はGPT-5.5よりわずかに誤りが少なく、過去に指摘された誤りを再現する割合も下がったと報告されているが、評価対象が「幻覚が起きやすいと分かっている場面」に絞られているため、通常利用全体での改善幅をそのまま示す数字ではない。OpenAI自身の説明によれば、幻覚削減の主因はモデルそのものが「賢く」なったからではなく、ツールの使い方・自己検証・自信過剰な誤答へのペナルティといった学習後の調整(post-training)の工夫による。モデルの世代が新しくなったからといって自動的に幻覚が減るとは限らない。

## 使いどころ・使い分け

ハルシネーションのリスクは、業務の性質によって大きく変わる。「生成AIを使うかどうか」ではなく「どこまで生成AIの出力を鵜呑みにできるか」を、次の基準で切り分けるのが実務的。

| リスクの高さ | 業務の特徴 | 具体例 |
|---|---|---|
| 高い(必ず人間が原典で確認) | 一意の正解があり、誤りが外部に公開・法的効力を持つ | 判例・法令の引用、学術文献の参照、契約条件の要約、財務・統計数値の引用、顧客への公式回答 |
| 中程度(要点だけ照合) | 社内向けだが意思決定に影響する | 市場調査のまとめ、競合分析、社内向けレポートの下書き |
| 低い(そのまま使ってよい) | 正解が一つに定まらない、誤りがあっても実害が小さい | アイデア出し・ブレインストーミング、文章のトーン調整、要約対象のテキストが手元にあるRAG的な使い方、下書きの言い回し改善 |

判断基準はシンプルに「この回答が間違っていたら、誰にどんな損害が出るか」。損害が「自分の作業のやり直し」で済むなら生成AI単独でも使ってよいが、「対外的な発言」「金額」「法的判断」に関わるなら、必ず人間による原典確認の工程を挟む。

## 実務での使い方

### 1. Web検索・RAGを使い、モデルの「知識」だけに頼らせない

RAG(Retrieval-Augmented Generation、検索拡張生成)は、質問に答える前に外部の文書やWebを検索し、その内容を根拠にして回答を作らせる方式。モデルの記憶だけで作文させるより幻覚が減るが、「検索結果を正しく反映できず幻覚が残る」こともあるため過信は禁物。

| ツール | Web検索・引用機能 | 有効化の場所 |
|---|---|---|
| ChatGPT | 検索を使った回答には本文中にインライン引用が付き、ホバーで出典を確認、クリックで遷移できる。引用が本文に出ない場合も、回答下の「Sources」から出典一覧を確認可能 | メッセージ入力欄の検索(地球儀)ボタン、または設定でデフォルトの検索利用をオンに |
| Claude | Web検索トグルは無料プランを含む全プランで利用可能。検索結果を使った回答には自動でインライン引用が付き、そのままクリックして原文を確認できる | チャット入力欄下の「検索」トグル。API利用時は `web_search` ツール(1,000回あたり10ドル) |
| Gemini | 「Google検索でのグラウンディング」機能により、回答の文中にインラインの引用リンクが自動で付与される | 回答下の出典表示、または開発者向けAPIでは `google_search` ツールを有効化 |
| Microsoft Copilot | Bing連携の検索が標準で有効。回答とあわせて参照したWebサイトの一覧が表示される | 標準で有効(設定不要) |
| Perplexity | 検索エンジン型のAIで、回答は原則すべて番号付き出典リンク付き。リアルタイムでWebを検索するため学習データの古さに起因する幻覚を抑えやすい | 標準で有効(設定不要) |

なおClaudeのAPIには、参照文書を渡すと回答の該当箇所をその文書内の具体的な一文にひも付けるCitations(引用機能)があり、ある企業ではこの機能の導入で「出典の誤り」が10%から0%に減ったという報告もある。

社内の文書・マニュアルを対象にする場合は、DifyやNotebookLM、社内RAGツールのように「参照元のドキュメントを指定してから質問する」形にすると、モデルの記憶に頼る割合を減らせる。特にGoogleの「NotebookLM」は「ソースグラウンディング」と呼ばれる仕組みで、インターネット全体の知識ではなくアップロードした資料のみを参照するため、資料にない内容を答えにくい設計になっている。使うときは次のようなプロンプトを添えると精度が上がる。

```
アップロードした資料に書かれている内容のみを根拠に回答してください。
資料に記載がない場合は、推測で補わずに
「アップロードされた資料には記載がありません」と答えてください。
回答の該当箇所を資料から引用してください。
```

### 2. 出典を求める・自己検証させるプロンプトを使う

そのままコピペで使えるプロンプト例:

```
以下の質問に回答してください。回答の際は次のルールを厳守してください。

1. 事実・数値・法令名・文献名など検証可能な情報には、必ず出典(URL・文献名・発行年)を明記する
2. 出典を明示できない情報は、断定せず「未確認」「一般的にはこう言われているが出典未確認」と明記する
3. 推測で埋めた部分と、根拠のある部分を明確に区別する
4. わからないことは「わかりません」とだけ答え、それらしい代替案を作文しない

質問: (ここに質問を書く)
```

回答が出た後の自己検証(セルフチェック)を追加させるプロンプト例:

```
直前の回答に含まれる事実・数値・引用を1つずつ箇条書きにし、それぞれについて
「出典から直接確認できる(◯)」「推測・一般論であり未確認(△)」「出典を示せない(✕)」
のいずれかを付けて再提示してください。✕の項目は本文から削除してください。
```

Geminiの場合は、この検証作業を「回答を再確認」機能(回答下部の「その他」メニューから実行)がワンクリックで代行してくれる。回答の各部分がGoogle検索のソースと一致していれば緑色、古い・確認できない場合はオレンジ色で表示されるため、業務資料に使う前のセルフチェックとして活用できる。

数値・計算を含む場合は、ステップバイステップで検算させると誤りに気づきやすい。

```
この計算結果について、途中の計算式を1行ずつ書き出し、最後にもう一度
別の手順で計算して2つの結果が一致するか確認してください。一致しない場合は
両方の計算過程を示し、どちらが正しいか判断してください。
```

### 3. 人間によるファクトチェック工程を業務プロセスに組み込む

- **原典確認が必須な項目を明文化する**: 判例・法令・統計数値・引用文献・金額は、生成AIの回答をそのまま転記せず、必ず元の資料(判例データベース、官公庁統計、社内正式資料など)と突き合わせる。
- **対外的に出す文書は「二段階チェック」にする**: 作成者がAIで下書き→本人が原典確認→別の担当者が最終レビュー、という最低2人の目を通すルールにする。
- **チェック済みの印を残す**: 稟議書・提案書のテンプレートに「AI生成部分の出典確認済み」のチェック欄を設けると、確認漏れを防ぎやすい。
- **リスクの高い業務ほどRAG+人間確認を併用**: 法務・財務・広報向けの用途では、検索拡張生成(RAG)を使わせた上で、出てきた出典元の文書自体を担当者が開いて確認するまでを「完了」の定義にする。

### 4. 社内ルール化のポイント

- 「AIの回答は下書き・一次情報ではない」ことを全社員向けに明文化する
- 判例・統計・引用文献は「生成AIが提示した出典URLが実在し、内容が一致するか」を必ず確認する、というルールを一文で徹底する
- ハルシネーションで問題が起きた事例(誤った判例引用、誤った規定案内など)を社内共有し、「他人事ではない」という意識を持たせる

## 注意点・よくある誤解

- **「Web検索を有効にすれば幻覚はなくなる」は誤解**: 検索結果を参照しても、モデルが検索結果を誤読・誤って要約して幻覚が残ることがある。引用が付いていても、リンク先を実際に開いて内容が一致するか確認する習慣が必要。
- **引用そのものが幻覚のこともある**: 出典らしいURLや文献名を提示されても、そのURLが実在しない・内容が食い違っているケースがある。「出典が付いている=正しい」ではなく、「出典を確認できる状態になった」に過ぎない。
- **法律分野は特にハルシネーション率が高い**: スタンフォード大学の研究(Dahl et al., 2024)では、法律に関する質問でChatGPT-4が58%、Llama 2が88%の割合で何らかの法的な幻覚(存在しない判例・誤った判示内容など)を含む回答をしたと報告されている。専門分野の質問ほど、原典確認を省略してはならない。
- **架空判例の提出による制裁は減るどころか急増している**: 2023年にはニューヨークの弁護士がChatGPTに生成させた実在しない判例6件を法廷に提出し、5,000ドルの制裁金と裁判所への謝罪状送付を命じられた(Mata v. Avianca事件)。2026年5月にはオレゴン州の弁護士2名が23件の架空引用を含む書面を提出し、米国の同種事案で過去最高額となる合計11万ドルの制裁を受けた。2026年8月に入っても事案は途切れておらず、コネチカット州連邦地裁のBarteca Holdings v. Tacobarn事件(8月4日)では、Open Law・Claude・ChatGPTの3種類のAIツールを使って書面を作成した弁護士が、架空の引用4件と誤った判示内容4件を含んだとして3,500ドルの制裁金と州弁護士会への懲戒付託を受けた。同じ連邦地裁のBooker v. U.S. Bank事件(8月5日)では、本人訴訟の当事者が4種類のAIツールに相互チェックさせたにもかかわらず架空の引用4件を含む書面を提出しており、「複数のAIに確認させれば安全」という思い込みが誤りであることを示している。テネシー州中部連邦地裁のIn re BFI Waste Systems of Tennessee事件(8月6日)では、弁護士が公の場での戒告と1,500ドルの制裁金を受けた。法律アナリストのDamien Charlotin氏が運営する事例データベースでは、2026年8月11日時点で世界で1,870件の「裁判所がAI生成の虚偽引用への依拠を認定した」事案が登録されており、1年前は月1件程度だったペースが2026年には毎日1件以上のペースに加速している。こうした事態を受け、米国の連邦裁判所では書面作成時のAI利用の申告と人間によるレビューを義務付ける標準命令(スタンディングオーダー)の導入が広がっており、裁判所によっては「教育」から「懲戒付託」へと対応を強めている。
- **ベンチマークの数値は鵜呑みにしない**: 「ハルシネーション率◯%」という数値はベンチマークの設計(要約対象の文書の長さ・難易度、外部資料ありの要約か資料なしの知識問答か)によって数倍〜数十倍も変わる。同じモデルでも参照する評価軸が違えば「幻覚率3%」にも「88%」にもなり得るため、「このモデルは幻覚が少ない」という宣伝文句だけで安全側に倒し切るのは危険。自社の使い方(RAGで資料を渡すのか、モデルの知識だけに頼るのか)に近い条件で測定されたベンチマークかを確認する。
- **チャットボットの回答も企業の公式見解として扱われる**: Air Canadaの事例のように、自社のチャットボットが誤った案内をした場合、企業側がその内容に対して法的責任を負うと判断された前例がある。社外向けにAIチャットボットを設置する場合は、この前提で運用ルールを作る必要がある。
- **AIの誤りに対する企業の法的責任は「過失の有無」を問わない方向に進んでいる**: EUのAI法(AI Act)は2026年8月2日に適用範囲が拡大し、汎用目的AI(GPAI)モデルに関する義務などが本格適用された。これと並行して、AI搭載製品を対象に含む改正EU製造物責任指令(Directive 2024/2853)は、利用者が過失を証明できなくても欠陥のある製品(ソフトウェアを含む)について製造者側に責任を負わせる「無過失責任」の枠組みを導入しており、加盟各国は2026年12月9日までに自国法へ反映する必要がある。EU域内で事業を行う場合、「AIが勝手に間違えた」という説明では免責されない前提でチャットボット・生成AI機能の品質保証体制を整える必要がある。
- **「ハルシネーションしないで」だけでは効果が薄い**: 精神論的な指示より、「わからない場合は分からないと言う」「出典を明示する」など、具体的な行動を指定するプロンプトの方が効果が出やすい。
- **社内文書をRAG・NotebookLMに使う場合の機密管理**: 社内文書をアップロードする際は、機密情報の有無と、アップロード先サービスのデータの扱い(学習利用の有無、保存期間、アクセス権限)を事前に確認する(詳細は情報漏洩対策のページを参照)。

## 最初の一歩

次に生成AIに数値や法令・文献の引用を含む回答を作らせるときは、上記の「出典を求めるプロンプト」を実際にコピペして使い、出てきた出典URLを1つでも実際に開いて内容が一致するか確認してみる。

## 関連トピック

- [生成AI利用における情報漏洩対策](information-leakage-prevention.md)
- [プロンプトの基本構造](../part05-prompt-engineering/prompt-basic-structure.md)
- [AIフレンドリーなデータ形式](../part07-data-analysis/ai-friendly-data-formats.md)

## 更新履歴

### 2026-08-22: Vectara定番リーダーボードの最新値、GPT-5.6の評価手法、8月の法的トラブル事例とEUの無過失責任規制を追記

- **内容**: 「仕組み・背景」にVectaraの定番HHEM-2.3リーダーボード(2026年5月時点、上位Finix S1 1.8%・GPT-5.4-nano 3.1%・Gemini 2.5 Flash-Lite 3.3%、下位Ministral 3 3B 24.2%等)の具体的な数値を追加し、AA-Omniscience系の知識問答ベンチマークの記述は集計元による数値のばらつきを踏まえて「要約と知識問答で同一モデルでも結果が大きく変わる」という論点にフォーカスするよう調整。OpenAIのGPT-5.6(2026年8月)による幻覚評価の手法変化(ユーザーが報告した誤りの再現率を測る方式)とその限界(評価対象が幻覚しやすい場面に限定)を追記。「注意点」の法的トラブル事例をDamien Charlotin氏のデータベース最新値(2026年8月11日時点で世界1,870件)に更新し、2026年8月の新規事案3件(Barteca Holdings v. Tacobarn、Booker v. U.S. Bank、In re BFI Waste Systems of Tennessee)を追加。EU AI Actの適用拡大(2026年8月2日)と改正EU製造物責任指令による無過失責任の規制動向を新規に追記
- **出典**: [vectara/hallucination-leaderboard | GitHub](https://github.com/vectara/hallucination-leaderboard)、[Latest AI Hallucination Rates & Benchmarks for New AI Models August 2026 | Suprmind](https://suprmind.ai/hub/ai-hallucination-rates-and-benchmarks/)、[AI Model Hallucination Rates 2026 | CodingFleet](https://codingfleet.com/blog/ai-model-hallucination-rates-2026/)、[GPT-5.6: The System Card | Don't Worry About the Vase (Zvi Mowshowitz)](https://thezvi.wordpress.com/2026/06/28/gpt-5-6-the-system-card/)、[GPT-5.6 Preview System Card | OpenAI Deployment Safety Hub](https://deploymentsafety.openai.com/gpt-5-6-preview/introduction)、[A Spoonful Of Sugar: Bryan Sugar's AI Litigation Insights - August 2026 | Mondaq](https://www.mondaq.com/unitedstates/new-technology/1832336/a-spoonful-of-sugar-%7C-bryan-sugars-ai-litigation-insights-august-2026)、[AI Hallucination Cases Database – Damien Charlotin](https://www.damiencharlotin.com/hallucinations/)、[AI Hallucination Cases: The 1,598/1,870-Case Sanctions Tracker | HAQQ](https://www.haqq.ai/blog/ai-legal-hallucination-audit)、[AI Act | Shaping Europe's digital future | European Commission](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)、[How to Draft an AI Vendor Contract Addendum to Meet the EU AI Act and Reduce Model Hallucination Liability in 2026 | Attorneys.Media](https://attorneys.media/how-to-draft-an-ai-vendor-contract-addendum-to-meet-the-eu-ai-act-and-reduce-model-hallucination-liability-in-2026/)

### 2026-07-24: ベンチマーク数値と法的トラブル事例を最新化
- **内容**: 「仕組み・背景」のVectaraベンチマーク記述を2026年の次世代版(HHEM+FaithJudge)に基づく数値に更新し、要約タスクと知識問答タスクでは同じモデルでも幻覚率が大きく異なる点(例: Gemini 3 Proが要約では低くAA-Omniscienceでは約88%)を追加。OpenAIのGPT-5.2〜5.5 Instantによる幻覚率削減(最大52.5%)とその要因(モデル改良ではなくpost-trainingの工夫)を追記。「注意点」の法的トラブル事例をDamien Charlotin氏のデータベース最新値(2026年6月時点で世界1,598件)、インディアナ州連邦地裁の制裁事案、City of Aberdeen事件、連邦裁判所のAI開示標準命令の最新状況(300人超の連邦判事・30以上の地裁)に更新
- **出典**: [AI Model Hallucination Rates 2026: Vectara HHEM & AA-Omniscience Rankings | CodingFleet](https://codingfleet.com/blog/ai-model-hallucination-rates-2026/)、[Introducing the Next Generation of Vectara's Hallucination Leaderboard](https://www.vectara.com/blog/introducing-the-next-generation-of-vectaras-hallucination-leaderboard)、[GPT-5.5 Instant reduces hallucinations by 52.5% | rollingout](https://rollingout.com/2026/05/05/openais-gpt-5-5-instant-reduces/)、[GPT-5.5 didn't cut hallucinations 60%. Here's what it did. | Wire Blog](https://usewire.io/blog/gpt-5-5-hallucination-drop-is-a-context-engineering-win/)、[AI Hallucination Cases Database – Damien Charlotin](https://www.damiencharlotin.com/hallucinations/)、[1,227 Fabricated Citations and Counting | PlatinumIDS Blog](https://blog.platinumids.com/blog/ai-hallucination-crisis-courts-2026)、[AIが生成した「架空の判例」を使用した弁護士に1万5,000ドルの制裁金 | Ledge.ai](https://ledge.ai/articles/ai_generated_fake_cases_legal_sanction)、[Court AI Disclosure Requirements: A Tracker | Tracelaw Knowledge Base](https://trace.law/kb/court-ai-disclosure-orders)

### 2026-07-06: 重複ページの統合
- **内容**: 重複していた hallucination-countermeasures.md と hallucination-mitigation.md を本ページに統合。推論モデルの幻覚率(o3のPersonQA約33%)、Copilot/Perplexityの検索機能、Claude Citationsの効果(出典誤り10%→0%)、NotebookLMのソースグラウンディングとプロンプト例、Geminiの「回答を再確認」機能、弁護士制裁事例の詳細(Mata v. Avianca、オレゴン州11万ドル制裁、連邦地裁の標準命令)を取り込み
- **出典**: [Introducing Citations on the Anthropic API](https://claude.com/blog/introducing-citations-api)、[How does Perplexity work? | Perplexity Help Center](https://www.perplexity.ai/help-center/en/articles/10352895-how-does-perplexity-work)、[NY Lawyer Fined $5,000 for ChatGPT Fake Citations | Spellbook](https://spellbook.com/learn/lawyer-who-used-chatgpt)、[A New Wrinkle in AI Hallucination Cases | LawSites](https://www.lawnext.com/2025/09/a-new-wrinkle-in-ai-hallucination-cases-lawyers-dinged-for-failing-to-detect-opponents-fake-citations.html)、[AI Hallucination Rates Across Different Models 2026](https://www.aboutchromebooks.com/ai-hallucination-rates-across-different-models/)、[Google Gemini アプリ ヘルプ](https://support.google.com/gemini/answer/14143489?hl=ja)、[アスカゼ: NotebookLMのハルシネーション対策](https://asukaze.co.jp/notebooklm-hallucination/)

### 2026-07-05: 初版執筆
- **内容**: ハルシネーションの定義・発生要因(OpenAIの2025年研究に基づく仕組みの解説)、業務でのリスク判断基準、Web検索・RAGの活用法、出典要求・自己検証プロンプト例、ファクトチェック工程の設計、ChatGPT/Claude/Geminiの引用表示機能の比較、法律分野の幻覚率・Air Canadaの訴訟事例などを整理
- **出典**: [Why language models hallucinate | OpenAI](https://openai.com/index/why-language-models-hallucinate/)、[Computerworld](https://www.computerworld.com/article/4059383/openai-admits-ai-hallucinations-are-mathematically-inevitable-not-just-engineering-flaws.html)、[OpenAI Help Center: ChatGPT Search](https://help.openai.com/en/articles/9237897-chatgpt-search)、[Claude web search now available globally on all plans | Anthropic](https://www.anthropic.com/news/web-search)、[Claude Web Search Tool | Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/web-search-tool)、[Grounding with Google Search | Gemini API](https://ai.google.dev/gemini-api/docs/google-search)、[Vectara Hallucination Leaderboard解説 | CodingFleet](https://codingfleet.com/blog/ai-model-hallucination-rates-2026/)、[ChatGPT虚偽判例でユタ州弁護士が制裁処分 | innovatopia](https://innovatopia.jp/tech-social/tech-social-news/56141/)、[生成AIに騙される弁護士がいまだに相次ぐ | JBpress](https://jbpress.ismedia.jp/articles/-/86872)、[What Air Canada Lost In 'Remarkable' Lying AI Chatbot Case | Forbes](https://www.forbes.com/sites/marisagarcia/2024/02/19/what-air-canada-lost-in-remarkable-lying-ai-chatbot-case/)、[Moffatt v. Air Canada: A Misrepresentation by an AI Chatbot | McCarthy Tétrault](https://www.mccarthy.ca/en/insights/blogs/techlex/moffatt-v-air-canada-misrepresentation-ai-chatbot)
