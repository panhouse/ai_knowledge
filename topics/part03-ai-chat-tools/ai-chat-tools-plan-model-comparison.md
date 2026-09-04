---
title: 主要AIチャットツールのプラン・料金・モデル横断比較(ChatGPT/Gemini/Claude/Copilot)
part: 3
chapter: 第1章 プラン・モデルの選び方
tags: [ChatGPT, Gemini, Claude, Copilot, 料金比較, モデル比較, ツール選定]
created: 2026-07-06
updated: 2026-08-20
---

# 主要AIチャットツールのプラン・料金・モデル横断比較(ChatGPT/Gemini/Claude/Copilot)

## これは何か

「会社でAIチャットツールを1本契約するなら、ChatGPT・Gemini・Claude・Copilotのどれにすべきか」「個人契約はPlusでいいのか、Claude Proにすべきか」という質問に、単体ツールの解説ページだけでは答えられない。各ツールは料金体系・モデルの呼び方・法人向けガバナンス機能の作り方がそれぞれ異なり、横に並べて初めて「自社にとっての正解」が見えてくる。本ページはChatGPT・Google Gemini・Claude(Anthropic)・Microsoft Copilotの4ツールを、無料/個人有料/法人プランの料金と、モデルラインナップの粒度で横並びにし、選定の判断軸を示す。各ツール単体の詳しい機能解説は末尾の関連トピックに譲る。

## 仕組み・背景

4ツールはいずれも「無料プラン→個人有料プラン→法人プラン」という3層構造を取るが、法人プランへの入り方が大きく異なる点を最初に理解しておく必要がある。

- **ChatGPT・Claude**: 単体の生成AIサービスとして、個人向けプランとは別に法人向けプラン(Business/Team、Enterprise)を単独契約する
- **Gemini**: 個人向けの「Google AIサブスクリプション」(Free/Plus/Pro/Ultra)と、法人向けの「Google Workspace」(Business Starter/Standard/Plus/Enterprise)へのGemini機能の**同梱**という2つの入口がある。法人利用は多くの場合Workspaceのプラン経由になる
- **Copilot**: Microsoft 365という基盤ライセンスに対する追加機能という位置づけが強く、単体では原則契約できない。個人向けはMicrosoft 365 Premiumへの統合が進み、法人向けは既存のMicrosoft 365ライセンスに「Microsoft 365 Copilot」を追加する形になる

### 無料プラン比較(2026年8月時点)

| ツール | 主なモデル | できること | 制約 |
|---|---|---|---|
| ChatGPT (Free) | GPT-5.6 Luna(2026年8月6日〜13日にかけてFree/Go向けの既定モデルに切替、テキストチャットは無制限化) | 基本的なチャット、画像生成・音声など一部機能。高度な質問は「Think」ボタンで追加の推論を呼び出せる | 2026年7月22日、自己サーブの広告出稿の仕組み「Advertise in ChatGPT」が日本を含む7か国・地域(米・加・英・豪・NZ・韓・日)向けに開始。実際の広告表示は現時点では米国の成人ログインユーザーのFree/Goティアが中心だが、今後表示国が広がる見込み。画像生成・音声など一部機能には引き続き5時間あたり数回程度の利用制限 |
| Gemini (Free) | Gemini 3.6 Flash(2026年7月21日投入、無料版Gemini appの既定モデル) | Gemini appでのチャット、Google Oneストレージ15GB、コンテキスト32Kトークン | 新設のGemini 3.7 Flash(2026年8月13日投入、コーディング・エージェント向けの低コストモデル)はGemini app内では有料プラン限定の「Spark」機能経由でのみ使え、無料版は引き続きGemini 3.6 Flashが上限。高性能モデル・Deep Researchなどは月間の利用回数がごく少数に制限 |
| Claude (Free) | Claude系の標準モデル(上位モデルは制限的) | 基本的なチャット | 1日あたりおおむね30〜100件程度(プロンプトの複雑さで変動) |
| Copilot (Free) | GPT-5.6(「Quick Response」)、高度な回答は「Think Deeper」でGPT-5.6 Sol | ブラウザ・Copilotアプリでのチャット、画像生成(1日15ブースト程度) | 2026年4月15日、Word/Excel/PowerPoint/OneNote内蔵のCopilot Chatが**シート数2,000以上の大企業テナントでは無償利用不可**となり有償ライセンス($30/月)が必須に。2,000シート未満の組織は引き続き無償利用できるが、混雑時は速度が絞られ有償プランへの誘導表示が出る |

### 個人有料プラン比較(2026年8月時点、月額・米ドル/日本円目安)

| ツール | プラン | 価格(USD) | 価格(JPY目安) | 位置づけ |
|---|---|---|---|---|
| ChatGPT | Go | $8程度 | ¥1,500 | Freeより高い利用上限が欲しい個人向け(2026年1月に日本含む170カ国以上へ展開) |
| ChatGPT | Plus | $20 | ¥3,000 | 業務で日常的に使う標準プラン |
| ChatGPT | Pro(下位) | $100 | ¥16,800 | 2026年4月新設。$200プランと同じモデル構成(GPT-5.6 Sol Pro含む)だが利用量はPlusの5倍 |
| ChatGPT | Pro(上位) | $200 | ¥30,000 | 利用量はPlusの20倍。Sora無制限生成・Operatorエージェント・高度な音声モードなど上位専用機能あり |
| Gemini | Google AI Plus | $4.99(2026年6月に$7.99から値下げ) | ¥725 | Gemini 3系・NotebookLM・Google Oneストレージ400GB(同時に200GBから倍増) |
| Gemini | Google AI Pro | $19.99 | ¥2,900 | 100万トークンのコンテキスト(Gemini 3.1 Pro)、Deep Research1日20回、Google Oneストレージ5TB(2026年4月に2TBから増量) |
| Gemini | Google AI Ultra 5x | $99.99 | ¥14,500 | Gemini appでPro比5倍の利用量、Google Oneストレージ20TB。開発者・上級クリエイター向けの新設プラン |
| Gemini | Google AI Ultra 20x | $199.99(2026年5月に$250から値下げ) | ¥32,000 | Gemini appでPro比20倍の利用量、Google Oneストレージ30TB、YouTube Premium込み |
| Claude | Pro | $20(年払いなら$17/月) | 実質¥3,400程度(2026年6月から日本の消費税10%が別途加算) | 業務での日常利用の標準プラン。2026年7月24日投入のClaude Opus 5が選べる最上位モデル |
| Claude | Max 5x | $100 | ― | Proの5倍の利用量。Claude Opus 5が既定モデル |
| Claude | Max 20x | $200 | ― | Proの20倍の利用量、コーディング等の大量利用向け。Claude Opus 5が既定モデル |
| Copilot | Microsoft 365 Premium | $19.99程度 | ― | 旧「Copilot Pro」の後継。Copilot Proは2026年8月1日にサポートを終了し、Premiumまたはpersonal/Family(Copilot同梱)への移行が完了している |

Gemini 3.5 Pro(Gemini 3.1 Proの後継として2026年5月のGoogle I/Oで予告)は、品質面の作り込みを理由に一般提供が繰り返し延期されており、2026年8月20日時点でもまだ未リリース(一部大企業向けの限定プレビューのみ)。そのためGoogle AI Pro/Ultraで日常的に使える最上位の汎用モデルは、当面Gemini 3.1 Proのままである点に注意する。なお2026年8月13日に投入されたGemini 3.7 Flashは汎用モデルの後継ではなく、コーディング・エージェント用途に特化した低コストモデルという位置づけである。

### 法人プラン比較(2026年8月時点、1ユーザー・月額目安)

| ツール | プラン | 価格目安 | 主なガバナンス機能 |
|---|---|---|---|
| ChatGPT | Business(旧Team) | 年払い$20/月払い$25程度(2席以上) | データの学習非利用が既定、セルフサーブのSAML SSO |
| ChatGPT | Enterprise | 非公開・要見積もり(実勢は$45〜75/席程度、平均$60前後との報告あり。150席以上・年払いが前提で下限は年間10万ドル超) | SSO+SCIM自動プロビジョニング、RBAC、データレジデンシー |
| Gemini | Workspace Business Starter | $7〜8.40程度(年払い) | Gemini機能は基本的なチャット中心で範囲が限定的。まず基盤(Gmail/Docs等)を安価に揃えたい小規模組織向け |
| Gemini | Workspace Business Standard | $14程度(年払い) | Gmail/Docs/Sheets/Slides/MeetにGemini標準同梱(2026年に単体アドオンから統合に移行)、学習利用なしが既定 |
| Gemini | Workspace Business Plus | $22程度(年払い) | Standardの機能に加え高度な管理・セキュリティ機能 |
| Gemini | Workspace Enterprise | 非公開・要見積もり | 高度な管理コンソール、DLP等の既存Workspaceセキュリティ機能をAI利用にも適用 |
| Claude | Team Standard | 年払い$20/月払い$25程度(5席以上) | SSO対応、データの学習非利用が既定、Microsoft 365連携、Claude Code/Cowork込み |
| Claude | Team Premium | 年払い$100/月払い$125程度 | Standardの5倍の利用量。標準・プレミアム席を組織内で混在させることも可能 |
| Claude | Enterprise | 2026年からセルフサーブ提供を開始。目安は$20/席/月+API従量課金(20席以上・年払いが前提)。個別見積もりのセールス経由プランも継続 | SSO(任意のIdP)+SCIM、監査ログ、Compliance API、データレジデンシー、ネットワークアクセス制御・IPアローリスト |
| Copilot | Microsoft 365 Copilot Business(アドオン) | $21程度(年払い、〜300ユーザー。2026年9月末まで$18程度の割引価格あり) | 既存M365ライセンスへの追加が前提。Work IQ・既製エージェント・モデル選択オプションあり |
| Copilot | Business Standard/Premium with Copilot(バンドル) | Standard $23.50・Premium $32程度(年払い、300ユーザーまで) | 2026年7月1日にSMB向け恒久プランとして正式化。M365本体とCopilotを1本の契約にまとめられ、単体アドオンを別途足すより割安になるケースが多い |
| Copilot | Microsoft 365 Copilot Enterprise | $30程度(年払い) | 大規模組織向け。2026年5月GA の上位バンドル「Microsoft 365 E7」($99/席)はM365 E5・Copilot・Entra Suite・Agent 365を一本化 |

法人向けは基本的に非公開の個別見積もりが多く、上記は複数の第三者情報から見た目安である点に注意する。

### モデルラインナップの対応表(2026年8月時点)

各社ともモデル名が数か月おきに変わるため、「今どのグレードの頭脳を使っているか」という**役割**で対応させると理解しやすい。

| 役割 | ChatGPT | Gemini | Claude | Copilot |
|---|---|---|---|---|
| 軽量・高速(単純作業向け) | GPT-5.6 Luna(Free/Goの既定モデル) | Gemini 3.5 Flash-Lite | Claude Haiku 4.5 | GPT-5.6(「Quick Response」の一部) |
| 標準・汎用 | GPT-5.6 Sol(2026年8月6日にInstant/Thinkingの区別を統合し、スライダーで思考量を調整する1本のモデルに) | Gemini 3.1 Pro(後継のGemini 3.5 Proは一般提供が延期中)。コーディング・エージェント用途にはGemini 3.7 Flash(8月13日投入)も選択肢 | Claude Sonnet 5(2026年6月30日投入。$2/$10という導入価格を2026年8月10日に恒久化し、予定していた値上げを撤回) | GPT-5.6(2026年7月9日から既定・優先モデル) |
| 高性能・推論(reasoning) | GPT-5.6 Sol(スライダーで「High」「Extra High」相当まで引き上げ) | Gemini 3.1 Pro Deep Think(深い推論モード) | Claude Opus 5(2026年7月24日投入、旧Opus 4.8を刷新。Maxプランの既定モデル、Proプランでも選択可能な最上位) | 「Think Deeper」モードでGPT-5.6上位設定、または手動でClaude Opus 5・Claude Sonnet 5を選択可(2026年7月下旬追加) |
| 最上位・特殊用途 | GPT-5.6 Sol Pro(Pro/Enterprise限定) | Gemini 3 Deep Think(最難問向け)、Gemini Omni(動画生成・編集) | Claude Fable 5(一般提供の最上位、1Mトークンコンテキスト。6月に一時提供停止も7月1日に復旧・再開)、Claude Mythos 5(招待制のProject Glasswing経由のみ) | Copilot Cowork(社内向けの複数タスク自動実行機能)ではClaude Fable 5も選択可(既定オフ) |

OpenAIは2026年8月6日、ChatGPTの日常利用モデルをGPT-5.6 Sol 1本に統合し、対話ごとにどれだけ「考える」かをスライダーで指定できるようにした(Plus/Pro向け)。従来の「Instant/Medium/High/Extra High/Pro」という5段階の推論強度選択、およびGPT-5.5 Instantとの二択は廃止され、Solが自動または手動スライダーで思考量を調整する一体型モデルになった。同時期にFree/Goプランの既定モデルもGPT-5.6 Lunaに切り替わり、テキストチャットが無制限になった(高度な質問には「Think」ボタンで追加の推論を呼び出せる)。最上位のGPT-5.6 Sol ProはPro/Enterpriseプラン限定のまま。同じGPT-5.6は2026年7月9日以降、GitHub CopilotおよびMicrosoft 365 Copilotの既定・優先モデルにも採用されており、OpenAIの新モデルが自社製品より先に(あるいは同時に)Copilot側に反映されるスピード感も特徴になっている。

Copilotのもう一つの特徴は、2026年3月にAnthropicとの提携が発表されて以降、**OpenAIのGPTとAnthropicのClaudeという他社モデルを1つの画面で選べる**ようになった点にある。2026年7月下旬にはAnthropicの最新モデルClaude Opus 5がWord/Excel/PowerPoint/Copilot Chat/Copilot Cowork/Copilot Studioの選択肢に追加され、既定のGPT-5.6系に加えて長文の構造的な分析が必要な場面ではClaude Opus 5・Claude Sonnet 5を明示的に選べるようになった(商用テナントは既定で有効、EU/UK地域は既定で無効な機能もある)。Copilot Coworkでは(既定オフながら)最上位のClaude Fable 5まで選択肢に含まれる。ChatGPT・Gemini・Claudeが自社モデルのみで完結しているのに対し、Copilotはモデル選択の観点でも「マルチベンダーの窓口」という独自の立ち位置になっている。

## 使いどころ・使い分け

### 無料→個人有料→法人、乗り換えのサイン

| 状況 | 判断 |
|---|---|
| 試しに使ってみたい、月に数回程度の利用 | 無料プランで十分。ただし従業員2,000人以上の大企業がCopilotを使う場合は、Word/Excel/PowerPoint内蔵チャットが2026年4月以降ほぼ有料専用になった点に注意 |
| 1日に何度も利用上限に達する、軽量モデルへの自動切替が頻発する | 個人有料プラン(Plus/AI Pro/Pro/Premium)へ移行するサイン |
| 高度な推論モデル(Thinking/Deep Think/Opus級)を毎日のように使う、コーディングや大量調査で上限を頻繁に超える | 上位プラン(Pro/Ultra/Max)への移行、またはコーディング特化製品(Codex・Claude Code)の追加契約を検討 |
| 会社の機密情報・顧客情報を扱うようになった | 個人向けプランのままにせず、法人プラン(Business/Team/Workspace/Copilot Business以上)への移行を検討する最大のサイン。個人向けプランにはSSOやデータレジデンシーの指定機能がない |
| 従業員が数十〜数百人規模で、監査ログ・SCIM自動プロビジョニング・データ保存地域の指定が必要 | Enterprise級プラン(ChatGPT Enterprise/Workspace Enterprise/Claude Enterprise/Copilot Enterprise)を検討する。Team/Business級ではSSOはあっても監査ログ・SCIMは未対応というケースが多い |

### どの業種・環境ならどのツールが向くか

| 状況 | 向いているツール | 理由 |
|---|---|---|
| すでにMicrosoft 365(Word/Excel/Outlook/Teams)を全社導入している | Microsoft Copilot | 追加のID管理・請求体系が不要で、既存の業務アプリの中でそのまま使える |
| すでにGoogle Workspaceを全社導入している | Gemini | Business Standard以上ならGmail/Docs/Sheets等にGemini機能が同梱され、追加のセキュリティ設定が最小限で済む |
| 特定ツールに縛られておらず、汎用的な対話・アイデア出しの質を重視 | ChatGPT | ユーザー数・エコシステム(GPTs、Codex等)が大きく、情報も充実している |
| 長文の読解・要約・契約書チェック・構造的な文章作成の精度を特に重視 | Claude | 長文処理や日本語の文章生成の評価が高く、2026年7月投入のClaude Opus 5で推論性能がさらに刷新された。Claude Code・Cowork等のエージェント機能も展開が早い |
| ソフトウェア開発を大量に自動化したい | ChatGPT(Codex)またはClaude(Claude Code) | いずれもコーディング特化のエージェント機能を主力プランに統合している。Office/Workspace系のCopilot・Gemini単体では専用性が低い |

### 乗り換え・複数契約の考え方

「1本化」か「併用」かは、組織の情報システム部門の管理コストと、現場が求める専門性のどちらを優先するかで決まる。

- **1本化が向くケース**: 管理コンソール・ID管理・請求を一元化したい、社内のAIリテラシーがまだ高くなく選択肢を絞りたい場合。多くの企業はまず「既存の業務基盤(M365またはWorkspace)に付随するツール」を全社の標準にするところから始める
- **併用が向くケース**: 全社標準ツール(Copilot/Gemini)に加えて、コーディング部門だけClaude Code/Codexを追加契約する、広報・法務など文章品質を特に重視する部署だけClaude Proを追加する、といった「用途特化の少数精鋭契約」を重ねる形。契約数が増えるほど費用対効果の管理は煩雑になるため、追加契約は「その部署で明確に上限に達している」「その業務でツール横断の比較検証をした結果、明確な差があった」といった根拠を伴わせるのが望ましい

## 実務での使い方

### 選定の進め方(社内提案の骨子)

1. まず自社の業務基盤(Microsoft 365かGoogle Workspaceか、どちらでもないか)を確認する
2. 基盤がある場合は、その基盤に付随するCopilot/Geminiを第一候補として費用対効果を見積もる(既にライセンス費用を払っている基盤への追加コストで済むため)
3. 基盤に依存しない全社ツールとしてChatGPT/Claudeを検討する場合は、無料または個人Plusプランで数週間試用し、実際の利用頻度と上限到達の頻度を確認したうえでBusiness/Team級への契約を判断する
4. 情報を扱う部署(法務・人事・経理等)がある場合は、法人プランのデータ学習利用オプトアウトの既定値・SSO対応・データ保存地域の指定可否を必ず比較する

### 法人導入で確認すべき項目チェックリスト

- **データの学習利用**: 個人向け無料/Plus級プランでは既定でオプトアウトされていない場合がある(要契約規約確認)一方、法人向けBusiness/Team級以上は既定で「学習に利用しない」設定になっているのが4社共通の傾向
- **SSO(シングルサインオン)**: ChatGPT Business、Claude Team、Copilot(M365経由)、Gemini(Workspace経由)のいずれも法人プランからSSOに対応。ただしSCIMによる自動プロビジョニングや監査ログは、いずれのツールも「一段上のEnterprise級プラン」でなければ使えないことが多い
- **管理コンソール**: 利用状況の可視化、部署単位のアクセス制御、利用上限の設定ができるか
- **既存基盤との統合コスト**: Copilot/GeminiはM365/Workspaceのライセンスが前提。ChatGPT/Claudeは基盤に依存しない分、SSO連携などを個別に設定する手間がある

### コピペで使える比較検討メモの型

社内で複数ツールを比較する際、以下のような表形式で整理すると意思決定が速い。

```
【AIチャットツール選定メモ】
比較対象: ChatGPT Business / Gemini(Workspace Business Plus) / Claude Team / Copilot Business

1. 現状の業務基盤: (M365 / Google Workspace / どちらでもない)
2. 想定利用部署と人数: 
3. 扱うデータの機密度(社外秘・個人情報の有無): 
4. 重視する用途(文章作成・コーディング・データ分析・Office連携等): 
5. 各ツールの月額見積もり(人数×単価): 
6. SSO・データ学習オプトアウト・データ保存地域の対応状況: 
7. トライアル期間中の利用上限到達頻度: 
→ 結論: 
```

## 注意点・よくある誤解

- **価格・モデル名は非常に頻繁に変わる**: 2026年に入ってからもChatGPT ProのTier新設(4月)とGPT-5.6投入(7月)・Sol統合とLuna無料化(8月)、Gemini AI Plusの値下げ・ストレージ倍増(6月)とGemini 3.6 Flash投入(7月)・3.7 Flash投入(8月)、Claude Fable 5の一般提供開始と一時停止・復旧(6〜7月)・Opus 5投入とSonnet 5の価格恒久化(7〜8月)、Copilotの大企業向けOffice統合有料化(4月)・SMB向けバンドルの恒久化(7月)・Claude Opus 5追加(7月)など、ほぼ毎月なにかしらの条件が変わっている。契約前には必ず各社の公式料金ページで最新情報を確認する
- **「Copilotは無料でOfficeにAIが使える」は組織規模によって答えが変わる**: 2026年4月以降、Word・Excel・PowerPoint・OneNote内蔵のCopilot Chatは、従業員2,000人以上の大企業テナントでは無償利用不可(有料ライセンス必須)になった一方、2,000人未満の組織は引き続き無償利用でき、混雑時に速度制限とアップグレード案内が出る程度にとどまる。自社の規模でどちらに該当するかを必ず確認する
- **GeminiはWorkspaceの契約形態によって「同じGemini」でも使える範囲が違う**: Business Starterは機能が制限され、Standard/Plus以上で本格的にDocs/Sheets等に統合される。「Gemini=Google Workspaceなら全部使える」と思い込まない
- **法人プランでも「Team/Business級」と「Enterprise級」でガバナンス機能の段差が大きい**: SSOはTeam/Business級でも対応するツールが多いが、監査ログ・SCIM・データレジデンシーの指定はEnterprise級でなければ使えないケースが目立つ。「SSOがあるから十分」と判断せず、必要な統制レベルを事前に洗い出す
- **Enterprise級の価格は基本的に非公開**: ネット上の推計額(本ページの数値含む)はあくまで目安。正式な見積もりは各社の営業窓口経由でしか取得できない。例外的にClaude Enterpriseは2026年からセルフサーブでの契約開始が可能になったが、その場合は席料に加えてAPI従量課金が乗るため、利用量が読めないうちは総額が見えにくい点に注意する
- **モデルの「賢さ」だけで選ぶと業務基盤との統合コストを見落とす**: 単体の生成品質ではClaude/ChatGPTが優位という評価が多いが、既存の業務基盤(M365/Workspace)との統合コストや情報システム部門の運用負荷を無視すると、導入後に「使われない高性能ツール」になりがちである
- **Copilotは「既存M365への単体アドオン」と「Copilot込みの新バンドル」を混同しやすい**: 2026年7月にBusiness Standard/Premium with Copilotという300ユーザーまでのバンドルSKUが恒久化されたが、既にM365 Business Standard/Premiumを契約済みの組織は単体アドオンを追加する形になり、どちらが安いかは既存契約の切替コスト次第で変わる。新規契約か既存契約への追加かで必ず両方の総額を比較する

## 最初の一歩

自社(または自分)が今契約しているAIチャットツールのプラン名と月額を一度書き出し、本ページの「無料プラン比較」「個人有料プラン比較」の表と照らして、上限到達の頻度や必要なガバナンス機能とプランが見合っているかを確認してみる。

## 関連トピック

- [ChatGPTのプラン比較](chatgpt-plan-comparison.md)
- [ChatGPTのモデル一覧と使い分け](chatgpt-model-lineup.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [Claude(Anthropic)の基本](claude-basics.md)
- [Microsoft Copilotの基本](microsoft-copilot-basics.md)

## 更新履歴

### 2026-08-20: 料金・モデルラインナップを2026年8月時点の最新状況に更新
- **内容**: ChatGPT(8月6日にGPT-5.5 Instant/GPT-5.6 Sol系の区別を廃止しSol 1本+思考量スライダーに統合、同時にFree/GoがGPT-5.6 Lunaへ切替・テキスト無制限化)、Gemini(8月13日投入のGemini 3.7 Flashとその位置づけ、Google AI Ultraの5x/20xを$99.99/$199.99・ストレージ20TB/30TBで精緻化、Workspace Business Starter層を追加)、Claude(7月24日投入のClaude Opus 5がMaxの既定・Proの最上位に、Sonnet 5の$2/$10価格を8月10日に恒久化し予定していた値上げを撤回)、Copilot(7月下旬にClaude Opus 5・Claude Fable 5をモデル選択肢に追加、7月1日にBusiness Standard/Premium with CopilotのSMBバンドルを恒久化、Copilot Proのサポート終了完了)を裏取りし、各比較表・モデル対応表・注意点を最新化した
- **出典**: [OpenAI: Improving GPT-5.6 Sol in ChatGPT—and expanding access to GPT-5.6 Luna for free users](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/)、[9to5Mac: OpenAI updating ChatGPT with a smarter GPT-5.6 Sol and unlimited free chats](https://9to5mac.com/2026/08/06/openai-updating-chatgpt-with-a-smarter-gpt-5-6-sol-and-unlimited-free-chats/)、[9to5Google: Gemini 3.7 Flash launch](https://9to5google.com/2026/08/13/gemini-3-7-flash-launch/)、[Bloomberg: Google Unveils Gemini 3.7 Flash Model as Gemini 3.5 Pro Delay Persists](https://www.bloomberg.com/news/articles/2026-08-13/google-debuts-new-gemini-flash-while-top-ai-model-still-delayed)、[9to5Google: Google clarifies its slightly confusing pair of AI Ultra plans](https://9to5google.com/2026/05/25/google-one-ai-ultra-clarification/)、[Engadget: The Google AI Ultra plan now starts at $100 a month](https://www.engadget.com/2176060/the-google-ai-ultra-plan-now-starts-at-100-a-month/)、[Anthropic: Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)、[TechCrunch: Anthropic launches Opus 5](https://techcrunch.com/2026/07/24/anthropic-launches-opus-5/)、[explainx.ai: Claude Sonnet 5 Pricing Locked at $2/$10](https://explainx.ai/blog/anthropic-sonnet-5-permanent-pricing-august-2026)、[Microsoft Community Hub: Available today: Anthropic Claude Opus 5 in Microsoft 365 Copilot](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/available-today-anthropic-claude-opus-5-in-microsoft-365-copilot/4540524)、[Windows Forum: Microsoft 365 Business Plans With Copilot Go Permanent for SMBs](https://windowsforum.com/threads/microsoft-365-business-plans-with-copilot-go-permanent-for-smbs-july-2026.425116/)、[Microsoft 365 Copilot Pricing公式(en-us)](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)

### 2026-07-23: 料金・モデルラインナップを2026年7月時点の最新状況に全面更新
- **内容**: ChatGPT(GPT-5.6 Sol/Terra/Luna投入とPro二段階の詳細、Business/Enterprise料金)、Gemini(AI Plusの値下げ・ストレージ倍増、Ultraの5x/20x再編、Gemini 3.6 Flash/3.5 Flash-Lite投入とGemini 3.5 Pro延期)、Claude(Sonnet 5への刷新、Fable 5の一時停止・復旧、Enterpriseのセルフサーブ化)、Copilot(GPT-5.6採用、Anthropicモデル追加、Office無償提供の組織規模別の扱い、E7バンドル)を裏取りし、日本円の目安価格も追加。無料・個人有料・法人プランの比較表とモデル対応表、注意点の記述を総入れ替えした
- **出典**: [OpenAI: GPT-5.6](https://openai.com/index/gpt-5-6/)、[OpenAI Help Center: GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001354)、[TechCrunch: ChatGPT finally offers $100/month Pro plan](https://techcrunch.com/2026/04/09/chatgpt-pro-plan-100-month-codex/)、[GIGAZINE: ChatGPT新Proプラン](https://gigazine.net/gsc_news/en/20260410-chatgpt-new-pro-subscription/)、[OpenAI: Testing ads in ChatGPT](https://openai.com/index/testing-ads-in-chatgpt/)、[Google公式ブログ: Everything new in our Google AI subscriptions, fresh from I/O 2026](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/)、[Google (X/@NewsFromGoogle): AI Plus値下げとストレージ倍増](https://x.com/NewsFromGoogle/status/2064066310393209100)、[Impress Watch: Google AI Plusが725円に値下げ](https://www.watch.impress.co.jp/docs/news/2115528.html)、[9to5Google: Gemini 3.6 Flash launch](https://9to5google.com/2026/07/21/gemini-3-6-flash-launch/)、[9to5Google: Gemini 3.5 Pro delays](https://9to5google.com/2026/07/16/gemini-3-5-pro-delays/)、[Anthropic: Redeploying Claude Fable 5](https://www.anthropic.com/news/redeploying-fable-5)、[Anthropic: Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)、[Anthropic Platform Docs: Introducing Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)、[tl;dv: Claude Enterprise Pricing 2026](https://tldv.io/blog/claude-enterprise-pricing/)、[Tygart Media: Claude Team Pricing 2026](https://tygartmedia.com/claude-team-pricing-2026-standard-premium-seats/)、[Microsoft 365 Copilot Pricing公式(ja-jp)](https://www.microsoft.com/ja-jp/microsoft-365-copilot/pricing)、[Computerworld: Microsoft backtracks on Copilot Chat access in M365 apps](https://www.computerworld.com/article/4150022/microsoft-backtracks-on-copilot-chat-access-in-m365-apps.html)、[gHacks: Microsoft Removes Copilot Chat From Office Apps for Unlicensed Users on April 15](https://www.ghacks.net/2026/03/18/microsoft-removes-copilot-chat-from-office-apps-for-unlicensed-users-on-april-15/)、[IT Pro: Microsoft 365 E7](https://www.itpro.com/software/microsoft-365-e7-ai-enterprise-bundle)、[Microsoft 365 Blog: Expanding model choice in Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365/blog/2025/09/24/expanding-model-choice-in-microsoft-365-copilot/)、[OpenAI: GPT-5.6 is now the preferred model in Microsoft 365 Copilot](https://openai.com/index/gpt-5-6-preferred-model-microsoft-365-copilot/)

### 2026-07-06: 初版執筆
- **内容**: ChatGPT/Gemini/Claude/Copilotの無料・個人有料・法人プランの料金とモデルラインナップ(軽量・標準・高性能・最上位)を横並びで整理し、乗り換えの判断基準・法人導入チェックリスト・日本企業での選定傾向・複数契約の考え方をまとめた
- **出典**: [Google公式ブログ: Everything new in our Google AI subscriptions, fresh from I/O 2026](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/)、[Claude公式: Plans & Pricing](https://claude.com/pricing)、[Claude Help Center: Choose a Claude plan](https://support.claude.com/en/articles/11049762-choose-a-claude-plan)、[Microsoft 365 Copilot Pricing公式](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)、[Microsoft Community Hub: Claude + GPT | Multi-model intelligence in Copilot](https://techcommunity.microsoft.com/blog/microsoftmechanicsblog/claude--gpt--multi-model-intelligence-in-copilot/4509773)、[Google DeepMind: Gemini 3 Flash](https://blog.google/products/gemini/gemini-3-flash/)、[Google Workspace Help: Google Workspace with Gemini FAQ](https://knowledge.workspace.google.com/admin/gemini/gemini-for-google-workspace-faq)
- **注記**: 法人プラン(特にEnterprise級)の価格は非公開の個別見積もりが基本であり、本ページの数値は複数の第三者情報に基づく目安。契約前には必ず各社の公式最新情報([ChatGPT](https://chatgpt.com/pricing)、[Gemini](https://gemini.google/subscriptions/)、[Claude](https://claude.com/pricing)、[Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing))を確認すること
