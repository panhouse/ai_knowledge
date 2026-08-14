---
title: 品質管理・QA職における生成AI活用事例
part: 15
chapter: 第12章 研究開発・品質管理
tags: [QA, ソフトウェアテスト, テストケース生成, バグトリアージ, 品質管理, 検査報告書, ISO9001, ハルシネーション, 情報漏洩, エージェンティックQA]
created: 2026-07-14
updated: 2026-08-11
---

# 品質管理・QA職における生成AI活用事例

## これは何か

QA(Quality Assurance、品質保証)・品質管理の担当者は、ソフトウェア開発ではテストケースの作成・実行・バグ報告の整理、製造業では検査報告書の作成・不良原因の記録・品質マニュアルの整備といった「大量の文書を正確に作る」作業に多くの時間を割いている。生成AIはこうした文書作成・要約・下書き作業を高速化できるが、テストが本当に必要な観点を網羅しているか、不良原因の記述が事実に即しているかは、最終的に人間のQA担当者が判断する必要がある。本ページは、[Part 14 製造業における生成AI活用事例](../part14-industry-cases/manufacturing-ai-use-cases.md)が扱う**外観検査AI(カメラ画像から不良品を自動判定する画像認識・異常検知モデル)を工場のラインに導入する話**、および[研究開発(R&D)職における生成AI活用事例](rd-ai-use-cases.md)が扱う**実験・研究の文献調査や技術文書作成**とは異なり、ソフトウェア・製造業を問わず**QA・品質管理という職種の担当者本人が、日々の業務(テストケース作成、バグ報告の要約、検査報告書のドラフト作成など)で生成AIをどう使うか**に焦点を当てる。

## 仕組み・背景

QA領域での生成AI活用には、性質の異なる2つの技術が関わっている点をまず区別しておく必要がある。

- **異常検知・画像認識AI(機械学習)**: 工場の外観検査AIのように、大量の良品・不良品画像を学習させて「これは不良品か」を判定するモデル。これは生成AIではなく従来型の機械学習(画像分類・異常検知)であり、[Part 14 製造業における生成AI活用事例](../part14-industry-cases/manufacturing-ai-use-cases.md)で扱う領域である。
- **生成AI(LLM)によるテキスト生成・要約**: 本ページで扱うのはこちら。要求仕様書・過去のバグ報告・検査データ・作業手順書といった**テキスト・構造化データ**を読み込ませ、テストケースの下書き、バグ報告の要約、検査報告書やマニュアルの文章化を行わせる使い方である。LLM(大規模言語モデル)は学習データ上の頻出パターンから「それらしい」テストケースや文章を組み立てる仕組みのため、要求仕様に書かれていない業務知識(実際の障害発生条件、現場特有の判断基準など)までは補えない。

ソフトウェアQAでは、GitHub CopilotやClaude Codeのようなコーディング支援AIがテストコード(Playwright・Cypress・pytestなど)の生成に、Xray(Jira向けテスト管理ツール)のAI Test Case Generationのような専用機能が要求仕様からのテストケース起票に使われている。製造業QAでは、ChatGPTやCopilotのような汎用AIに過去の検査データやメモを読み込ませて報告書の文章部分を生成させる使い方が中心で、手書き帳票が残る現場ではAI-OCR(手書き・印字文字を読み取るAI)と組み合わせて使われることが多い。

2026年に入り、QAツール業界では「AIが下書きを作る」段階から一歩進んだ**エージェンティックQA(Agentic QA、自律型テストエージェント)**という言葉が広がっている。これは、AIが単発の指示に応えて文章・コードを生成する(レベル1: AI-Assisted)だけでなく、テストデータ生成やUI変更時のロケータ自動修復(セルフヒーリング)を自律的にこなす(レベル2: AI-Augmented)、さらには要件やリスクの変化を読み取ってテスト計画の立案から実行・是正まで一連の作業を人の指示を都度挟まずに回す(レベル3: Agentic)という段階分けで語られる整理である。mabl の「Agentic Tester」やXrayの自動スクリプト生成機能はレベル2〜3寄りの機能にあたるが、**自律度が上がるほど「AIが何を判断し、どこまで実行してよいか」の権限設計とログ監査が重要になる**点は本ページの他の使い方と変わらない(考え方は[AIエージェントの自律度レベルと権限設計の基本](../part11-ai-agents/ai-agent-autonomy-levels-and-permission-design.md)を参照)。

## 使いどころ・使い分け

QA・品質管理の業務は「AIに下書きを作らせてよい範囲」と「人が判断・確認すべき範囲」の線引きが特に重要になる。

| 活用シーン | AIが担う範囲 | 人が必ず担う範囲 |
|---|---|---|
| テストケース・テスト観点の生成(ソフトウェア) | 要求仕様からのたたき台生成、境界値・異常系の観点出し | 業務知識にもとづく抜け漏れの補完、優先度・リスクベースの取捨選択 |
| テスト自動化スクリプトの生成(Playwright/Cypress等) | ロケータ・アサーションを含むコードの下書き生成 | 実行結果の確認、UIが変わった際のメンテナンス方針の判断 |
| バグ報告の要約・トリアージ支援 | 重複バグの検出補助、再現手順の整理、影響範囲の一次分類 | 重大度・優先度の最終判定、リリース可否の意思決定 |
| 探索的テストのチャーター(探索範囲・観点)設計 | リスクの高い機能領域の洗い出し、テストシナリオの提案 | 実際の操作・観察による発見、暗黙知にもとづく「違和感」の判断 |
| 検査報告書のドラフト作成(製造業) | 測定データ・メモからの文章化、定型フォーマットへの流し込み | 数値の正確性確認、判定基準への当てはめの最終確認 |
| 不良原因分析の文書化(製造業) | 過去事例の類似検索、原因候補の整理、報告書の下書き | 実機・現物確認にもとづく原因の特定、再発防止策の妥当性判断 |
| ISO・品質マニュアル等の文書作成 | 既存文書の構成たたき台、規格要求事項に沿った章立て提案 | 自社の実態と規格要求の整合性確認、監査対応としての最終承認 |

判断基準は法務・R&D領域と同様に「この出力を鵜呑みにしてリリース・出荷したら、誤りがあった場合に誰にどんな損害が出るか」。**テストケースの数を増やす・文章を速く仕上げるのはAIが得意な領域だが、「何を検査すべきか」「これは本当に不良か」という品質の最終判断は人が担う**という一線を越えないことが実務上のコツになる。

## 実務での使い方

### 1. テストケース・テスト観点の生成(ソフトウェアQA)

要求仕様やユーザーストーリーを貼り、テストケースのたたき台を作らせる。ChatGPT・Claude・Geminiのような汎用AIでも十分使えるほか、Jira向けテスト管理ツールXrayには「AI Test Case Generation」という専用機能があり、Jira画面上でチケットの要求内容から手動テストケース・BDD形式(Given-When-Then)のテストケースを数秒で自動生成できる(Standard/Advanced/Enterpriseプランで利用可、データはJira環境内で処理されモデルの学習には使われない仕様)。

```
あなたはソフトウェアQAエンジニアです。以下の機能要件からテストケースを作成してください。

【機能要件】
ECサイトのクーポン適用機能。ユーザーはカート画面でクーポンコードを入力し、
「適用」ボタンを押すと割引後の合計金額が表示される。
1注文につきクーポンは1つまで併用可。有効期限・利用条件(最低購入金額)あり。

【出力形式】
1. 正常系・異常系・境界値のテストケースを表形式で(No / 前提条件 / 手順 / 期待結果)
2. 特にセキュリティ・不正利用の観点(同一クーポンの二重適用、期限切れ直後など)を
   別枠で5件以上出してほしい
3. 要件に明記されていないが確認すべき仕様の曖昧な点があれば、末尾に質問として列挙する
```

### 2. テスト自動化スクリプトの生成

GitHub CopilotやClaude CodeなどのAIコーディング支援は、VS Code上でテストコードの生成に使える。VS CodeでCopilot Chatを開き、対象のソースファイルをコンテキストに含めた状態で `/tests` コマンド、またはチャットに直接指示すると、Playwright・Cypress・pytest・JUnitなど既存のテストフレームワークに沿った形式でテストコードの下書きが生成される。GitHub Copilotのエージェントモード(Agent Mode)を使うと、テストの生成だけでなく実行・失敗時の修正まで複数ステップを自律的に繰り返させることもできるが、生成されたテストが「本当に検証すべき仕様」を捉えているかは依然として人によるレビューが前提になる。

```
このコンポーネント(CouponInput.tsx)に対するPlaywrightのE2Eテストを作成してください。

- 正常系(有効なクーポンコード入力→割引反映)
- 異常系(無効なコード、期限切れコード、最低購入金額未達)
- クーポン欄を空にして「適用」を押した場合の挙動
既存のテストファイル(tests/cart.spec.ts)の書き方・命名規則に合わせること
```

食べログのQAチームでは、手動テストケースの実装を生成AIで支援する取り組みを進めており、直近の案件では手動実施399件のテストケースのうち304件をAIで実装することに成功し、テスト実行工数を52%削減、月あたり1.7人月相当の工数削減につながったと報告している。ポイントは「AIに丸ごと任せる」のではなく、プロンプトのノウハウ(既存コードの書き方をコンテキストに含める、対象範囲を絞るなど)を蓄積して精度を上げている点である。

### 3. バグ報告の要約・トリアージ支援

起票されたバグ報告(再現手順・ログ・スクリーンショット)を、開発者や上位者向けに整理する。

```
以下はQAチームが起票したバグ報告(生の記述)です。開発者への引き継ぎ用に整理してください。

【出力形式】
1. タイトル(1行、影響と現象がわかる形)
2. 再現手順(番号付き、曖昧な記述は「要確認」と明記)
3. 期待結果 / 実際の結果
4. 影響範囲(想定できる範囲のみ。断定できない場合は「要調査」と書く)
5. 重大度の一次案(Critical/High/Medium/Low)とその理由

【生のバグ報告】
(ここに担当者が書いたメモ・チャットログなどを貼付)

※ 実際のログや原因は記載内容からのみ判断し、記載のない原因を推測で断定しないこと
```

### 4. 探索的テストのチャーター設計

探索的テスト(仕様書通りの手順ではなく、テスト担当者の裁量で自由に操作しながらバグを見つける手法)は、AIに「探索の切り口」を提案させると、闇雲に触るより効率的に進められる。

```
新機能「クーポン適用」について、探索的テストのチャーター(探索の目的・範囲・
着眼点をまとめた指示書)を3本作成してください。

【機能概要】(ここに機能概要を記載)
【想定ユーザー】ECサイトの一般利用者、まれに複数タブ・複数デバイスから同時操作するユーザー
【出力形式】各チャーターに「目的(何を確かめたいか)」「範囲(触る画面・操作)」
「着眼点(過去の類似機能で問題になりやすいパターン)」を含める
```

### 5. 検査報告書のドラフト作成(製造業QA)

過去の検査データやメモから、報告書の文章部分をAIに下書きさせる。数値そのものは検査データの原本から一字一句コピーし、AIには文章化・体裁の整形のみを任せるのが安全な運用になる。ある金属加工メーカーでは、過去の検査データをChatGPTに読み込ませて報告書のドラフトを生成させたところ、30分かかっていた作成作業が5分に短縮し記載漏れがゼロになったと報告されている。手書き帳票が残る現場では、AI-OCR(手書き・印字文字を読み取るAI、2026年時点で印字文字は99%台・手書き文字は丁寧に書かれていれば90%超が目安、ツールによっては99%超をうたうものもある)でデータ化してから生成AIに読み込ませる二段構えが実務的である。

より大規模な事例としては、パナソニック コネクトが2026年2月に発表した「Manufacturing AIエージェント」がある。図面・部品図・技術仕様書といったPDF形式の非構造化データからAIが材質・仕上げなどの項目を自動照合する仕組みで、従来目視で50〜340分かかっていた図面照合作業を10分に短縮し、作業時間を最大97%削減したと公表している。検査報告書のドラフト作成も、これと同様に「非構造化データからの情報抽出→定型フォーマットへの整形」という構造で捉えると、自社のどの工程に応用できるかが検討しやすい。

```
以下は本日の受入検査データ(箇条書きメモ)です。社内の検査報告書フォーマットに
沿って文章化してください。

【フォーマット】検査対象 / 検査日 / 検査項目と測定値 / 判定基準との比較 / 総合判定 / 特記事項
【検査データ】
(測定値・検査項目のメモをここに貼付。数値は絶対に書き換えない)

【条件】
- 記載のない数値・判定を新たに作り出さないこと
- 判定基準に照らして「合格/不合格/要確認」のいずれかを明記すること
- 曖昧な記述がある場合は「要確認」として本文中に明記すること
```

### 6. 不良原因分析の文書化

```
以下は不良品の現物観察メモと過去の類似不良の記録です。不良原因分析報告書の
下書きを作成してください。

【今回の不良現象】(現象・発生工程・発生頻度を記載)
【現物観察メモ】(担当者の観察結果を箇条書きで貼付)
【過去の類似不良記録】(参考となる過去の記録を貼付)

【出力形式】
1. 不良現象の要約
2. 推定される原因候補を複数挙げ、それぞれの根拠(観察事実 or 過去記録との類似性)を明記
3. 現物・工程を確認しないと特定できない点は「要現物確認」と明記
4. 再発防止策のたたき台(実施前提でなく「検討案」として)
```

日立製作所は2026年6月、大みか事業所での実証をもとにした品質保証支援AIエージェント「品質ナレッジシステム」(HMAX Industryの一部として提供)を発表した。熟練者の暗黙知(過去のトラブル対応記録・マニュアルの判断基準)を形式知化してAIに組み込み、自然言語の質問やメール文面から類似の過去事例を検索できるようにした結果、トラブル対応事例の検索時間を約9割削減、対応レポートの作成時間を120分から15分に、不具合の原因分析時間を16時間から3時間に短縮したと報告している。ポイントは、AIが「原因を断定する」のではなく「過去の類似事例を高速に検索し、判断材料を揃える」役割に徹している点で、上記プロンプト例の「要現物確認」「検討案」といった書き方の考え方と一致する。

### 7. ISO・品質マニュアル等の文書作成

```
ISO 9001の「8.5 製造及びサービス提供」に対応する社内作業標準書の構成案を
作成してください。

【対象工程】(工程名を記載)
【現行の作業手順メモ】(箇条書きで貼付)
【出力形式】ISO 9001の該当要求事項の見出しに沿った章立てとし、各章に
「現行手順の要約」「規格が求める記載事項との対応」を分けて示すこと
※ 規格解釈が必要な箇所は断定せず「品質保証部門・審査機関への確認事項」として注記する
```

### ツール横断の対応付けと料金の目安(2026年8月時点)

| 用途 | 主なツール | 特徴・料金の目安 |
|---|---|---|
| テストケース生成(Jira/Xray) | Xray「AI Test Case Generation」/「AI Test Model Generation」 | Sembi IQというAI基盤を採用し、要求仕様から手動・BDD形式のテストケースをStandard/Advanced/Enterpriseの全プランで生成可能(データは学習に非利用)。要件から視覚的なテストモデルを自動生成する「AI Test Model Generation」はEnterprise限定。Xray自体の料金はJiraの全ユーザー数に連動する課金で、Cloud版は月額換算で1ユーザーあたり6ドル台が目安、10ユーザーまでの最小プランで年額100ドル程度から |
| テスト自動化スクリプト生成 | GitHub Copilot(VS Code) | 2026年6月1日にトークン量に応じた「AI Credits」の従量課金へ移行(個人向けPro 10ドル/月・Pro+ 39ドル/月・Max 100ドル/月にそれぞれ月15/70/200ドル相当のクレジット付与、コード補完自体は無料)。チーム向けはBusiness 19ドル/席/月・Enterprise 39ドル/席/月で、2026年9月1日までは移行特典として付与クレジットが上乗せされる |
| ノーコードのAIテスト自動化・自己修復・自律実行 | mabl | プラン名はStarter/Growth/Enterpriseに整理され、Growth以上でUI変化への自己修復に加え「Agentic Tester」(目的ベースでテストを自律実行する機能)が使える。価格は個別見積りだが、第三者情報ではStarterが月450〜600ドル程度、Growthが月1,200〜3,000ドル程度、Enterpriseは要見積り |
| ビジュアル回帰テスト(画面の見た目のAI比較) | Applitools | チェックポイント(スクリーンショット1枚)課金制。無料枠は月100チェックポイントで変わらず、有料は小規模チームで月1,000ドル前後〜大規模で月1万ドル超まで幅がある(公開の料金表はなく個別見積り) |
| 汎用AIによるバグ報告要約・報告書ドラフト | ChatGPT / Claude / Gemini | 汎用プランで対応可。法人向け(Business/Enterprise、学習への非利用が標準)の利用を推奨 |
| 手書き検査帳票のデータ化 | AI-OCR各種サービス | 印字文字は99%台、手書き文字は丁寧な記入であれば90%超が目安(製品によっては99%超をうたうものもあるが実測にはばらつきがある)。重要な数値は人による二重確認が前提 |

判断基準は「その業務がテスト管理・実行基盤への組み込みを必要とするか」。CI/CDパイプラインに組み込んで自動実行まで求める場合は専用ツール(Xray・mabl・Applitools)、単発のドラフト作成・要約・壁打ちには汎用AIチャットで十分なことが多い。mabl・Xrayのように「AIに実行まで任せる」機能(Agentic Tester、自動スクリプト生成)を使う場合は、通常のツール選定基準に加えて「AIがどこまで自律的に判断・実行してよいか」を事前に取り決めておく。

## 注意点・よくある誤解

- **「AIが生成したテストケースの数が多い」=「テストの質が高い」ではない**: AIは要求仕様に書かれたパターンから機械的にテストケースを増やせるが、業務知識にもとづく「ここは過去に事故が起きやすい」といった暗黙知までは反映できない。テストケースは必ず人がレビューし、リスクの高い領域が網羅されているかを確認する。
- **バグ報告の要約・原因分析にもハルシネーション(もっともらしい誤情報を生成する現象)のリスクがある**: 特に「影響範囲」「原因」を記載のない情報から断定的に書いてしまうことがある。プロンプトで「記載のない情報を推測で断定しない」ことを明記し、出力された原因・影響範囲は必ず一次情報(ログ・現物)と突き合わせる。詳細は[ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)を参照。
- **バグ報告・検査データには機密情報が含まれやすい**: 顧客情報を含む障害ログ、取引先の検査データ、未公開の不具合情報などを無料プランの汎用AIに入力すると、学習データとして利用される規約になっている場合がある。法人向けプラン(学習への非利用がデフォルト)を使う、社外秘データはマスキングしてから入力するなど、[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)に沿った運用を徹底する。
- **検査報告書・不良原因分析の数値は絶対にAIに創作させない**: AIは文章の体裁を整えるのは得意だが、記載のない数値を「それらしく」補完してしまうことがある。報告書の数値部分は必ず検査データの原本から転記し、AIには文章化・要約のみを任せる運用にする。
- **AIによる異常検知(画像認識)と生成AIによる文書作成を混同しない**: 「AIを導入すれば検査業務が自動化される」と期待されがちだが、外観検査AI(画像認識モデル)と本ページで扱う生成AI(文書作成支援)は別の技術であり、それぞれ得意分野が異なる。両者を組み合わせて初めて「検査(画像認識)→報告書作成(生成AI)」という一連の業務が効率化できる。
- **AIが下書きした品質マニュアル・作業標準書は規格適合性を保証しない**: ISO 9001などの規格要求事項への適合性は品質保証部門・審査機関が最終判断するものであり、AIの出力はあくまで構成のたたき台として扱う。
- **「AIエージェントに任せる範囲」が広がるほど権限設計が重要になる**: mablの「Agentic Tester」やXrayの自動スクリプト生成、Copilotのエージェントモードのように、2026年時点のQAツールは「下書きを作る」段階から「テストの実行・修正まで自律的に回す」段階へ機能が広がりつつある。テスト実行がステージング環境の書き換えを伴う場合など、失敗時の影響が大きい操作をAIに自律実行させる前には、どこまで自動化しどこで人の承認を挟むかを取り決めておく(詳細は[AIエージェントの自律度レベルと権限設計の基本](../part11-ai-agents/ai-agent-autonomy-levels-and-permission-design.md)を参照)。

## 最初の一歩

直近で起票した(または対応した)バグ報告1件、または検査報告書1件を選び、上記の要約・ドラフト作成プロンプトに貼って試し、AIの出力と自分が本来書く内容を見比べて、抜け漏れや誤った断定がないかを確認してみる(社外秘の実データではなく、匿名化・仮の数値に置き換えたサンプルで試すこと)。

## 関連トピック

- [製造業における生成AI活用事例](../part14-industry-cases/manufacturing-ai-use-cases.md)
- [研究開発(R&D)職における生成AI活用事例](rd-ai-use-cases.md)
- [生成AIに向く業務・向かない業務の切り分け](../part12-business-practice/ai-task-suitability.md)
- [ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)
- [AIエージェントの自律度レベルと権限設計の基本](../part11-ai-agents/ai-agent-autonomy-levels-and-permission-design.md)

## 更新履歴

### 2026-08-11: エージェンティックQAの動向・料金表・国内新事例を反映して最新化
- **内容**: (1)「エージェンティックQA(自律型テストエージェント)」という2026年の潮流を仕組み・背景と注意点に追加し、mablの「Agentic Tester」・Xrayの自動スクリプト生成・GitHub Copilotのエージェントモードを自律度の観点で整理、AIエージェントの自律度レベルと権限設計ページへ相互リンクを追加。(2)ツール横断の料金表を2026年8月時点に更新: GitHub Copilotが2026年6月からトークン従量課金の「AI Credits」制に移行した点(個人Pro/Pro+/Max、チームBusiness 19ドル/Enterprise 39ドル/席/月)、XrayのAI機能がSembi IQ基盤に刷新されEnterprise限定の「AI Test Model Generation」が追加された点、mablのプラン名がStarter/Growth/Enterpriseに整理された点を反映。(3)検査報告書・不良原因分析の節に、パナソニック コネクトの図面照合AIエージェント(作業時間最大97%削減)、日立製作所の品質ナレッジシステム(トラブル対応検索時間約9割削減、レポート作成120分→15分、原因分析16時間→3時間)という2026年の国内新事例を追加
- **出典**: [Updates to GitHub Copilot billing and plans - GitHub Changelog](https://github.blog/changelog/2026-06-01-updates-to-github-copilot-billing-and-plans/)、[GitHub Copilot is moving to usage-based billing - The GitHub Blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/)、[GitHub Copilot Pricing 2026 | Automation Atlas](https://automationatlas.io/answers/github-copilot-pricing-explained-2026/)、[Xray Launches AI-Powered, Human-Guided Test Capabilities with Sembi IQ](https://www.getxray.app/blog/ai-powered-test-case-test-model-generation-in-xray)、[AI Test Model Generation in Xray Enterprise - Xray Blog](https://www.getxray.app/blog/introducing-ai-test-model-generation-xray-enterprise)、[Xray Pricing 2026: What It Actually Costs | BesTest](https://getbestest.com/xray-pricing/)、[Mabl Pricing 2026: Plans, Cost & Comparison | Bug0](https://bug0.com/knowledge-base/mabl-pricing)、[Mabl Pricing, Decoded | Autonoma AI](https://getautonoma.com/blog/mabl-pricing)、[Applitools Pricing: Cost Per Snapshot at Scale | Autonoma AI](https://getautonoma.com/blog/applitools-pricing)、[QA trends for 2026: AI, agents, and the future of testing - Tricentis](https://www.tricentis.com/blog/qa-trends-ai-agentic-testing)、[What Is Agentic QA? | Katalon](https://katalon.com/resources-center/blog/what-is-agentic-qa-the-complete-guide-for-2026)、[図面の照合業務を最大97%削減 パナソニック コネクト - ASCII](https://ascii.jp/elem/000/004/375/4375661/?rss=)、[パナソニック コネクト、図面/製品仕様の照合業務をAIで効率化 | IT Leaders](https://it.impress.co.jp/articles/-/29019)、[生成AIを活用した品質保証支援を実証、日立大みか事業所 - MONOist](https://monoist.itmedia.co.jp/mn/articles/2507/07/news022.html)、[日立製作所、製造業向けAIエージェント「品質ナレッジシステム」開発 | レスポンス](https://response.jp/article/2026/06/10/412486.html)、[日立、熟練ノウハウを形式知化し品質保証業務を効率化するAIエージェントをHMAX Industryとして提供開始 | PR TIMES](https://prtimes.jp/main/html/rd/p/000000068.000141666.html)、[【2026年版】手書きAI-OCRの精度を99%超に引き上げる実践ガイド | OptiMax](https://www.optimax.co.jp/ai-information/ai-ocr-handwriting/)

### 2026-07-14: 初版執筆
- **内容**: ソフトウェアQA(テストケース生成、テスト自動化スクリプト生成、バグ報告の要約・トリアージ、探索的テストのチャーター設計)と製造業QA(検査報告書ドラフト作成、不良原因分析の文書化、ISO品質マニュアル作成)の双方について、コピペ用プロンプト例、GitHub Copilot/Xray AI Test Case Generation/mabl/Applitoolsなどのツール横断の対応付けと料金、食べログQAチームのテスト工数52%削減事例、AI-OCRの認識精度、生成AIとAI画像認識(外観検査)の違いを整理
- **出典**: [GitHub Copilot Pricing 2026: Pro $10, Pro+ $39, Max $100 | Automation Atlas](https://automationatlas.io/answers/github-copilot-pricing-explained-2026/)、[Writing tests with GitHub Copilot - GitHub Docs](https://docs.github.com/en/copilot/tutorials/write-tests)、[Approaching how we adopt AI for test: Exploring Xray's AI Test Case Generation](https://www.getxray.app/blog/how-assurity-adopts-ai-for-test-exploring-xray-ai-test-case-generation)、[AI Test Case Generation - Xray Cloud Documentation](https://docs.getxray.app/space/XRAYCLOUD/392921171/AI+Test+Case+Generation)、[Mabl Pricing 2026: Plans, Cost & Comparison | Bug0](https://bug0.com/knowledge-base/mabl-pricing)、[mabl Pricing | mabl](https://www.mabl.com/pricing)、[Applitools Pricing: How Much Does Visual Testing Cost in 2026? | Delta-QA](https://delta-qa.com/en/blog/applitools-pricing-2026/)、[Platform - Pricing - AI-Powered End-to-End Testing | Applitools](https://applitools.com/platform-pricing/)、[AIによる手動QAの自動化：自動テストコーディングのAI化でテスト実行工数を52%削減 - Tabelog Tech Blog](https://tech-blog.tabelog.com/entry/ai-for-qa-automation-test)、[AIによる手動QAの自動化：食べログQAチームの挑戦、その第一歩 - Tabelog Tech Blog](https://tech-blog.tabelog.com/entry/ai-manual-qa-automation-first-step)、[品質検査報告書をAIで自動作成！テンプレートと導入方法を解説 | AI総合研究所](https://www.ai-souken.com/article/ai-quality-inspection-report-automation)、[品質管理のChatGPT活用事例～生成AIを品質管理に活かす３つの方向性～ – 製造部 SEIZO-BU](https://seizo-bu.com/qc-pro/%E5%93%81%E8%B3%AA%E7%AE%A1%E7%90%86%E3%81%AB%E3%81%A4%E3%81%84%E3%81%A6/%E5%93%81%E8%B3%AA%E7%AE%A1%E7%90%86%E3%81%AEchatgpt%E6%B4%BB%E7%94%A8%E4%BA%8B%E4%BE%8B%EF%BD%9E%E7%94%9F%E6%88%90ai%E3%82%92%E5%93%81%E8%B3%AA%E7%AE%A1%E7%90%86%E3%81%AB%E6%B4%BB%E3%81%8B%E3%81%99/)、[生成AI によるよりスマートなテスト：探索的なアイデアから自動スクリプトまで | Qt Group](https://www.qt.io/ja-jp/blog/smarter-testing-with-genai-from-exploratory-ideas-to-automated-scripts)、[Mastering AI-Driven Exploratory Testing for Quality Engineering](https://cakehurstryan.com/2026/07/02/yes-you-can-run-exploratory-testing-with-ai/)
