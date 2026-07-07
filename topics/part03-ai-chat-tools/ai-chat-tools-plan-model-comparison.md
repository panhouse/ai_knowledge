---
title: 主要AIチャットツールのプラン・料金・モデル横断比較(ChatGPT/Gemini/Claude/Copilot)
part: 3
chapter: 第1章 プラン・モデルの選び方
tags: [ChatGPT, Gemini, Claude, Copilot, 料金比較, モデル比較, ツール選定]
created: 2026-07-06
updated: 2026-07-06
---

# 主要AIチャットツールのプラン・料金・モデル横断比較(ChatGPT/Gemini/Claude/Copilot)

## これは何か

「会社でAIチャットツールを1本契約するなら、ChatGPT・Gemini・Claude・Copilotのどれにすべきか」「個人契約はPlusでいいのか、Claude Proにすべきか」という質問に、単体ツールの解説ページだけでは答えられない。各ツールは料金体系・モデルの呼び方・法人向けガバナンス機能の作り方がそれぞれ異なり、横に並べて初めて「自社にとっての正解」が見えてくる。本ページはChatGPT・Google Gemini・Claude(Anthropic)・Microsoft Copilotの4ツールを、無料/個人有料/法人プランの料金と、モデルラインナップの粒度で横並びにし、選定の判断軸を示す。各ツール単体の詳しい機能解説は末尾の関連トピックに譲る。

## 仕組み・背景

4ツールはいずれも「無料プラン→個人有料プラン→法人プラン」という3層構造を取るが、法人プランへの入り方が大きく異なる点を最初に理解しておく必要がある。

- **ChatGPT・Claude**: 単体の生成AIサービスとして、個人向けプランとは別に法人向けプラン(Business/Team、Enterprise)を単独契約する
- **Gemini**: 個人向けの「Google AIサブスクリプション」(Free/Plus/Pro/Ultra)と、法人向けの「Google Workspace」(Business Starter/Standard/Plus/Enterprise)へのGemini機能の**同梱**という2つの入口がある。法人利用は多くの場合Workspaceのプラン経由になる
- **Copilot**: Microsoft 365という基盤ライセンスに対する追加機能という位置づけが強く、単体では原則契約できない。個人向けはMicrosoft 365 Premiumへの統合が進み、法人向けは既存のMicrosoft 365ライセンスに「Microsoft 365 Copilot」を追加する形になる

### 無料プラン比較(2026年7月時点)

| ツール | 主なモデル | できること | 制約 |
|---|---|---|---|
| ChatGPT (Free) | GPT-5.5 Instant(上限超過で軽量版に自動切替) | 基本的なチャット、画像生成・音声など一部機能 | 米国では広告表示が導入済み、他地域にも拡大予定。5時間あたり数回程度の利用制限 |
| Gemini (Free) | Gemini系の軽量モデル | Gemini appでのチャット、Google Oneストレージ15GB | 高性能モデル・Deep Researchなどは月間の利用回数がごく少数に制限 |
| Claude (Free) | Claude系の標準モデル(上位モデルは制限的) | 基本的なチャット | 1日あたりおおむね30〜100件程度(プロンプトの複雑さで変動) |
| Copilot (Free) | GPT-5.5 Instant相当 | ブラウザ・Copilotアプリでのチャット、画像生成(1日15回程度のブースト) | 2026年4月15日以降、Word・Excel・PowerPoint・OneNote内でのCopilot Chat利用が不可に変更され、Office統合はほぼ有料プラン専用になった |

### 個人有料プラン比較(2026年7月時点、月額・米ドル目安)

| ツール | プラン | 価格 | 位置づけ |
|---|---|---|---|
| ChatGPT | Go | $8程度(2026年1月に日本含む170カ国以上に展開) | Freeより高い利用上限が欲しい個人向け |
| ChatGPT | Plus | $20 | 業務で日常的に使う標準プラン |
| ChatGPT | Pro | $100 / $200(2026年4月に$100の下位ティアを新設) | ヘビーユーザー・コーディング用途 |
| Gemini | Google AI Plus | $7.99 | 強化されたGemini・NotebookLM・Google One 200GB |
| Gemini | Google AI Pro | $19.99 | 100万トークンのコンテキスト、Deep Research1日20回、Google One 2TB |
| Gemini | Google AI Ultra | $99.99〜(上位に$200程度のプランも) | Gemini appでPro比20倍の利用量、開発者・上級クリエイター向け |
| Claude | Pro | $20(年払いなら$17/月) | 業務での日常利用の標準プラン |
| Claude | Max 5x | $100 | Proの5倍の利用量 |
| Claude | Max 20x | $200 | Proの20倍の利用量、コーディング等の大量利用向け |
| Copilot | Microsoft 365 Premium | $19.99程度 | 旧「Copilot Pro」の後継。Copilot Proは2026年8月1日にサポート終了予定 |

### 法人プラン比較(2026年7月時点、1ユーザー・月額目安)

| ツール | プラン | 価格目安 | 主なガバナンス機能 |
|---|---|---|---|
| ChatGPT | Business(旧Team) | 年払い$20/月払い$25程度 | データの学習非利用が既定、セルフサーブのSAML SSO |
| ChatGPT | Enterprise | 非公開・要見積もり | SSO+SCIM自動プロビジョニング、RBAC、データレジデンシー |
| Gemini | Workspace Business Standard | $14程度(年払い) | Gmail/Docs/Sheets等にGemini同梱、学習利用なしが既定 |
| Gemini | Workspace Business Plus | $22程度(年払い) | Standardの機能に加え高度な管理・セキュリティ機能 |
| Gemini | Workspace Enterprise | 非公開・要見積もり | 高度な管理コンソール、DLP等の既存Workspaceセキュリティ機能をAI利用にも適用 |
| Claude | Team Standard | 年払い$20/月払い$25程度(5〜150席) | SSO対応、データの学習非利用が既定、Microsoft 365連携 |
| Claude | Team Premium | 年払い$100/月払い$125程度 | Standardの5倍の利用量 |
| Claude | Enterprise | 非公開・要見積もり(小規模でも$60/席程度からとの情報あり) | SSO(任意のIdP)+SCIM、監査ログ、Compliance API、データレジデンシー、BAA/HIPAA対応 |
| Copilot | Microsoft 365 Copilot Business | $21程度(年払い、〜300ユーザー。2026年9月末まで$18程度の割引価格あり) | 既存M365ライセンスへの追加が前提 |
| Copilot | Microsoft 365 Copilot Enterprise | $30程度(年払い) | 大規模組織向け。2026年5月からはCopilotを含む「Microsoft 365 E7」($99程度)という上位バンドルも登場 |

法人向けは基本的に非公開の個別見積もりが多く、上記は複数の第三者情報から見た目安である点に注意する。

### モデルラインナップの対応表(2026年7月時点)

各社ともモデル名が数か月おきに変わるため、「今どのグレードの頭脳を使っているか」という**役割**で対応させると理解しやすい。

| 役割 | ChatGPT | Gemini | Claude | Copilot |
|---|---|---|---|---|
| 軽量・高速(単純作業向け) | GPT-5.5 Instant(上限超過時の軽量版へ自動切替) | Gemini 3.1 Flash-Lite | Claude Haiku 4.5 | GPT-5.5 Instant相当(既定モデル) |
| 標準・汎用 | GPT-5.5 Instant | Gemini 3.5 Flash(2026年6月投入、Flashだが旧Pro級の性能) | Claude Sonnet 5 | 「Auto」「Quick Response」で内部的にGPT-5.5 Instantを使用 |
| 高性能・推論(reasoning) | GPT-5.5 Thinking | Gemini 3.1 Pro / Deep Think(深い推論モード) | Claude Opus 4.8 | 「Think Deeper」モード、または手動でClaude Opus 4.8を選択可 |
| 最上位・特殊用途 | GPT-5.5 Pro(コンテキスト272K) | Gemini 3 Deep Think(最難問向け)、Gemini Omni(動画生成・編集) | Claude Fable 5(一般提供の最上位、1Mトークンコンテキスト)、Claude Mythos 5(招待制の限定提供) | (Copilot単体に最上位専用モデルはなく、Claude Opus選択が実質的な最上位) |

Copilotの最大の特徴は、2026年5月ごろから**OpenAIのGPTとAnthropicのClaudeという他社モデルを1つの画面で選べる**ようになった点にある。Microsoft 365 Copilot Chatでは既定のGPT-5.5 Instantに加えて、長文の構造的な分析が必要な場面ではAnthropicのClaude Opus 4.8を明示的に選べる。ChatGPT・Gemini・Claudeが自社モデルのみで完結しているのに対し、Copilotはモデル選択の観点でも「マルチベンダーの窓口」という独自の立ち位置になっている。

## 使いどころ・使い分け

### 無料→個人有料→法人、乗り換えのサイン

| 状況 | 判断 |
|---|---|
| 試しに使ってみたい、月に数回程度の利用 | 無料プランで十分。ただしCopilotはOffice統合が2026年4月以降ほぼ使えなくなった点に注意 |
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
| 長文の読解・要約・契約書チェック・構造的な文章作成の精度を特に重視 | Claude | 長文処理や日本語の文章生成の評価が高く、Claude Code・Cowork等のエージェント機能も展開が早い |
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

- **価格・モデル名は非常に頻繁に変わる**: 2026年に入ってからもChatGPT ProのTier新設(4月)、Gemini 3.5 Flashの投入(6月)、Claude Fable 5の登場(6月)、Copilotの無料プランからのOffice統合除外(4月)など、数か月単位で条件が変わっている。契約前には必ず各社の公式料金ページで最新情報を確認する
- **「Copilotは無料でOfficeにAIが使える」は2026年4月以降は誤り**: Word・Excel・PowerPoint・OneNoteでのCopilot Chat利用は有料ライセンス前提になった。無料で使えるのはブラウザ・アプリ上のチャットのみ
- **GeminiはWorkspaceの契約形態によって「同じGemini」でも使える範囲が違う**: Business Starterは機能が制限され、Standard/Plus以上で本格的にDocs/Sheets等に統合される。「Gemini=Google Workspaceなら全部使える」と思い込まない
- **法人プランでも「Team/Business級」と「Enterprise級」でガバナンス機能の段差が大きい**: SSOはTeam/Business級でも対応するツールが多いが、監査ログ・SCIM・データレジデンシーの指定はEnterprise級でなければ使えないケースが目立つ。「SSOがあるから十分」と判断せず、必要な統制レベルを事前に洗い出す
- **Enterprise級の価格は基本的に非公開**: ネット上の推計額(本ページの数値含む)はあくまで目安。正式な見積もりは各社の営業窓口経由でしか取得できない
- **モデルの「賢さ」だけで選ぶと業務基盤との統合コストを見落とす**: 単体の生成品質ではClaude/ChatGPTが優位という評価が多いが、既存の業務基盤(M365/Workspace)との統合コストや情報システム部門の運用負荷を無視すると、導入後に「使われない高性能ツール」になりがちである

## 最初の一歩

自社(または自分)が今契約しているAIチャットツールのプラン名と月額を一度書き出し、本ページの「無料プラン比較」「個人有料プラン比較」の表と照らして、上限到達の頻度や必要なガバナンス機能とプランが見合っているかを確認してみる。

## 関連トピック

- [ChatGPTのプラン比較](chatgpt-plan-comparison.md)
- [ChatGPTのモデル一覧と使い分け](chatgpt-model-lineup.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [Claude(Anthropic)の基本](claude-basics.md)
- [Microsoft Copilotの基本](microsoft-copilot-basics.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: ChatGPT/Gemini/Claude/Copilotの無料・個人有料・法人プランの料金とモデルラインナップ(軽量・標準・高性能・最上位)を横並びで整理し、乗り換えの判断基準・法人導入チェックリスト・日本企業での選定傾向・複数契約の考え方をまとめた
- **出典**: [Google公式ブログ: Everything new in our Google AI subscriptions, fresh from I/O 2026](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/)、[Claude公式: Plans & Pricing](https://claude.com/pricing)、[Claude Help Center: Choose a Claude plan](https://support.claude.com/en/articles/11049762-choose-a-claude-plan)、[Microsoft 365 Copilot Pricing公式](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)、[Microsoft Community Hub: Claude + GPT | Multi-model intelligence in Copilot](https://techcommunity.microsoft.com/blog/microsoftmechanicsblog/claude--gpt--multi-model-intelligence-in-copilot/4509773)、[Google DeepMind: Gemini 3 Flash](https://blog.google/products/gemini/gemini-3-flash/)、[Google Workspace Help: Google Workspace with Gemini FAQ](https://knowledge.workspace.google.com/admin/gemini/gemini-for-google-workspace-faq)
- **注記**: 法人プラン(特にEnterprise級)の価格は非公開の個別見積もりが基本であり、本ページの数値は複数の第三者情報に基づく目安。契約前には必ず各社の公式最新情報([ChatGPT](https://chatgpt.com/pricing)、[Gemini](https://gemini.google/subscriptions/)、[Claude](https://claude.com/pricing)、[Microsoft 365 Copilot](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing))を確認すること
