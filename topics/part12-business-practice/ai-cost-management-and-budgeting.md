---
title: "生成AI利用コストの管理・予算配分"
part: 12
chapter: 第1章 導入の設計
tags: [コスト管理, 予算配分, チャージバック, トークン課金, FinOps, AIエージェント]
created: 2026-07-25
updated: 2026-08-28
---

# 生成AI利用コストの管理・予算配分

## これは何か

生成AIの利用が広がるほど、経営企画・情報システム部門には「結局、AIに毎月いくら使っているのか」「どの部署がどれだけコストを負担すべきか」という問いが降ってくる。ChatGPT・Copilot・ClaudeなどのシートライセンスとAPIの従量課金が混在し、しかも従量課金は使う人・使う機能次第で桁が変わるため、通常のソフトウェアのように「ライセンス数×単価」だけでは予算が読めない。本ページは、この**費用の見積もり・部門への配分・可視化**という、お金の管理に焦点を当てる。

似たテーマに[生成AI導入のROI測定・効果測定の考え方](ai-roi-measurement.md)があるが、目的が異なる。ROI測定は「投じた費用に対してどれだけ成果(時短・売上・コスト削減)が出たか」という**効果検証**の話であるのに対し、本ページは「そもそも費用がいくらかかり、それを組織内でどう見積もり・配分・統制するか」という**予算管理**の話である。ROI測定の分母(コスト)を正しく作るための前提知識、と位置づけるとよい。

## 仕組み・背景

### コストの発生源は大きく2種類

生成AIのコストは、契約形態によって性質がまったく異なる2つに分かれる。

- **シート課金(定額)**: ChatGPT Business/Enterprise、Microsoft 365 Copilot、Claude Team/Enterprise、Gemini for Google Workspaceなど、「1ユーザーあたり月額◯円」で契約する形態。利用量にかかわらず費用は一定で、予算化しやすい
- **従量課金(API)**: OpenAI API・Anthropic API・Google Gemini APIなど、開発者向けにモデルを直接呼び出す契約。「トークン(文章を分割した処理単位)」の入出力量に応じて課金され、使うほど・呼び出す回数が増えるほど費用が線形以上に増える

[トークンとは何か](../part02-llm-basics/what-are-tokens.md)で扱っているとおり、API課金は「入力トークン」と「出力トークン」で単価が異なり(出力側が3〜6倍程度高いのが一般的)、さらにモデルのグレード(上位モデルほど高性能・高単価)によっても単価が数倍〜数十倍変わる。同じ業務でも「どのモデルを使うか」の選択だけでコストが大きく変動するのが、生成AIの予算管理が従来のITコスト管理と最も違う点である。

### なぜ従来のIT予算管理より難しいのか

- **単価がモデル・世代ごとに変わる**: 数か月おきに新モデルが出るたびに単価表が更新され、去年の見積もりがそのまま使えない
- **1回の利用が複数回のAI呼び出しに分解される**: 後述する「AIエージェント」型の使い方では、ユーザーの1回の依頼が裏側で何十回ものAI呼び出しに展開されることがあり、見た目の作業1件とコストが比例しない
- **シートと従量課金が混在する**: 同じ社内に「ChatGPT Businessのシート契約」と「Difyやカスタム開発で使うOpenAI APIの従量課金」が併存し、片方だけ見ていると全社の生成AI支出を把握できない

## 使いどころ・使い分け

### シート課金 vs 従量課金、どちらで契約すべきか

| 観点 | シート課金(ChatGPT Business/Enterprise、Copilot、Claude Team/Enterprise等) | 従量課金(API) |
|---|---|---|
| 向く利用シーン | 全社員・部署単位での日常的なチャット利用。利用量が人によって大きくは変わらない | 社内システム・チャットボットへの組み込み、バッチ処理、利用量が業務量に応じて変動する用途 |
| 予算の読みやすさ | 読みやすい(人数×単価で確定) | 読みにくい(利用量次第で青天井になり得る) |
| 向かないケース | 利用量が極端に多い一部の人・部署がいると割高になることがある(逆に大量利用者にはむしろ得) | 全社員に均等に配るような定常利用には不向き(管理コストが見合わない) |
| 典型的な失敗 | 使わない人にもシートを配り続けて空席コストが発生する | 利用上限を設けずに配布し、想定外の高額請求(いわゆる「請求書ショック」)を招く |

**判断の目安**: 「業務として恒常的に・多くの人が使う」対話的な利用はシート課金、「システムに組み込む・処理量が変動する・一部の開発チームだけが使う」用途は従量課金、という住み分けが基本形。実務では両方を併用する企業がほとんどで、全社ヘルプデスク的な用途はシート契約、社内ツールへの組み込みはAPIという二本立てにするのが典型的な構成である。

### 見積もりが甘くなりやすい場面

- **AIエージェント(自律的に計画・実行するAI)を使ったワークフロー**: 1回のユーザー依頼が、内部では「調べる→考える→ツールを呼ぶ→結果を確認する→もう一度考える」という多段階のAI呼び出しに展開される。単純なチャット応答に比べてトークン消費が大きく増える構造的リスクがあるため、通常のチャット利用の感覚で予算を組むと大きく外れる(詳細は後述)
- **推論(思考)モードを使う高性能モデル**: 回答前に内部で長い思考過程を生成するモデル・機能は、画面に見えない「思考トークン」も課金対象になり、体感より請求が高くなりやすい

## 実務での使い方

### 1. 法人契約でよくあるコスト構造(2026年8月時点の目安)

シート課金型の主要ツールの価格帯は次のとおり。**モデル同様、料金は数か月単位で改定されるため、契約前に必ず公式ページ・営業担当に最新価格を確認すること。** 特にChatGPT Enterprise・Gemini Enterprise等の見積もり制プランは、ここに記載の水準感はあくまで目安である。

| ツール | プラン | 目安価格(1ユーザー/月額) | 契約単位・条件 |
|---|---|---|---|
| OpenAI | ChatGPT Business(旧Team) Standard | 年契約$20、月契約$25 | 最低2席。2026年4月2日に旧価格(年契約$25・月契約$30)から値下げされた |
| OpenAI | ChatGPT Business Premium(新設) | 年契約$100、月契約$125 | 2026年8月に新設されたシート種別。Standard比で利用量5倍・回答生成の5時間ごとの上限撤廃。1ワークスペース内でStandardとPremiumを混在させられる |
| OpenAI | ChatGPT Enterprise | 個別見積り(非公開) | 業界筋では「$45〜75程度(平均$60前後)・最低150席」という情報が出回っているが、OpenAI公式の確認は取れていない未確認情報。契約前に必ず営業担当に確認する |
| Microsoft | Microsoft 365 Copilot(E3/E5への追加) | $30 | M365 E3/E5等の対象ライセンスが前提 |
| Microsoft | Microsoft 365 Copilot Business(〜300ユーザー向け) | 年契約$18(2026年7月1日〜12月31日の期間限定価格、通常$21)、月契約$25.20 | Microsoft 365 Businessプランが前提。期間限定価格の終了日は公式ページで複数回延長されており、契約時に最新の終了日を必ず確認する |
| Anthropic | Claude Team(Standard) | 年契約$20、月契約$25 | 2026年7月20日にシート数下限が5席→2席に緩和。上限は150席(超える場合はEnterpriseへ移行) |
| Anthropic | Claude Team(Premium) | 年契約$100、月契約$125 | 同上 |
| Anthropic | Claude Enterprise | $20(シート料。使用量は含まれず別途API従量課金) | セルフサーブは最低20席、営業担当経由は最低50席。「シートに使用量をバンドルする」方式から「フラットなシート料+従量課金を完全分離」する方式になっている |
| Google | Gemini(Google Workspace) | Business Starter 目安$7、Standard 目安$14、Plus 目安$22 | 2025年3月以降、Geminiは単体アドオンではなく各Workspaceプランに標準搭載される方式に変更された |
| Google | Gemini Enterprise(エージェント基盤、Workspaceとは別製品) | 目安$21〜(Business)、Standard/Plusはさらに上 | Workspaceの「Gemini」とは別契約の製品なので混同しないよう注意 |

**従量課金(API)側のメーター課金の例**として、Microsoft 365 CopilotのAgent機能・Copilot Studioは、月額固定のシートとは別に「Copilot Studioクレジット」を使うメーター制が用意されている(25,000クレジットで月額$200、または従量課金なら1クレジット$0.01)。クレジットの消費量は機能によって大きく異なり、シンプルな回答が1クレジット程度なのに対し、自律的に動く「エージェントのアクション」1回で25クレジット以上を消費することもある。エージェント機能を使うほどこの従量課金部分が積み上がる点は、後述する「エージェントのコスト構造」の理解に直結する。

**参考: 開発者向けAIコーディングツールの実コスト感**として、Anthropicは自社ドキュメントで、企業導入におけるClaude Codeの平均利用額は開発者1人・稼働1日あたり約$13、月あたり$150〜250程度と公表している(利用者の9割は1日あたり$30未満に収まる)。シート課金の外側にあるAPI従量課金がどの程度の規模になり得るかの目安として、予算組みの参考にできる。

トークン単価そのもの(入力/出力の非対称性、モデルごとの単価差)については[トークンとは何か](../part02-llm-basics/what-are-tokens.md)の料金表を参照。

### 2. 部門別予算配分・社内チャージバックの設計

社内の複数部署が同じAI契約を使う場合、コストを「見える化するだけ(ショーバック)」か「実際に部門予算へ請求するか(チャージバック)」の2段階で設計する。

| 方式 | 内容 | 向くタイミング |
|---|---|---|
| ショーバック(Showback) | 部門ごとの利用量・概算コストを可視化して共有するが、実際の予算配分・請求はしない | 導入初期。まず「誰がどれだけ使っているか」の実態を把握する段階 |
| チャージバック(Chargeback) | 部門ごとの利用実績に応じて、実際にコストを各部門の予算から差し引く(社内請求する) | 利用実績の按分方法(誰にどう振り分けるか)の精度に自信が持てるようになった段階 |

**進め方の目安**: いきなりチャージバックから始めると、按分方法への不満(「うちの部署はそんなに使っていないはずだ」等)がガバナンス導入への抵抗を生みやすい。まずは数か月間ショーバックで実態を共有し、按分ロジックが妥当だと合意できてからチャージバックに移行するのが実務上こなれたやり方である。

**按分の軸(タグ付け)の決め方**: 部門別に費用を割り振るには、利用実績に次のようなタグを付けて集計する。

- 部門・チーム名(コストセンターコード)
- プロジェクト名・案件名
- 利用環境(本番/検証)
- 使用モデル名(高性能モデルほど単価が高いため、モデル別の内訳も見えるようにしておく)

APIを直接契約している場合は、次のような仕組みで部門別の予算上限・可視化を設定できる。

- **OpenAI API「プロジェクト」機能**: 組織内を複数の「プロジェクト」に分割し、プロジェクトごとに専用APIキー・利用可能モデル・月間予算上限を設定できる。ただし**この上限は「超過時に通知が来る」仕組みであり、リクエスト自体を強制停止するハード制限ではない点に注意**が必要(確実に止めたい場合は、自動チャージ(オートリチャージ)を無効化したプリペイド残高運用にする)
- **Anthropic Console「Workspace」機能**: 組織内を複数のワークスペースに分割し、ワークスペースごとに月間利用上限・レート制限(1分あたりのリクエスト数・トークン数)を設定し、閾値到達時にメール通知を受け取れる
- **Azure OpenAI Service**: サービス自体には部門別の課金分割機能はないため、デプロイごとに「コストセンター」「チーム」「プロジェクト」といったタグを付与し、Azure Cost Managementでタグ別に絞り込んで集計する運用になる(Microsoftの「FinOpsツールキット」やFOCUS仕様の活用が推奨されている)
- **Microsoft 365 Copilotの利用状況レポート**: 管理センターで、部署・地域・ライセンス状況別に「Copilot Chat利用状況レポート」「エージェント利用状況レポート」「Copilot検索利用状況レポート」を7/28/90/180日単位で確認できる

### 3. コストの可視化

日常的な支出の把握には、次の3層で可視化の仕組みを持つと運用しやすい。

| 層 | 見るもの | 主な手段 |
|---|---|---|
| ツール単体の管理画面 | 各ツールの利用状況・請求額 | ChatGPT Enterprise/Business・Microsoft 365 Copilot・Claude・Geminiの管理者向けUsageダッシュボード |
| API利用の実測値 | 呼び出しごとの入出力トークン数・実コスト | 各社APIのレスポンスに含まれる`usage`フィールド、Anthropic ConsoleのWorkspace別利用状況、OpenAIのProject別Usageダッシュボード |
| 全社横断の集計 | 複数ツール・複数部門をまたいだ支出の合算 | クラウドコスト管理ツール(Azure Cost Management等)へのタグ集約、社内で独自に組むダッシュボード(スプレッドシート集計でも初期段階では十分) |

FinOps(クラウドコストを財務・エンジニアリング・事業部門が協働して管理する運用手法)の業界団体であるFinOps Foundationは、「FinOps for AI」を2026年の最重点テーマに掲げており、実務担当者1,192人を対象にした「State of FinOps 2026」調査では**FinOps担当者のうちAI関連支出を管理している割合が、2年前の31%から98%へ急増した**と報告している。同調査では**AI予算全体を超過した企業が73%に達し、個々のエージェント型AIプロジェクトに限ると当初予算の平均2.4倍まで膨らんでいた**ことも明らかになっており、「トークン単価は2023年半ば以降おおむね8割下落したのに、全社のAI支出総額は2024年から2026年にかけて約4.8倍に増えた」という一見矛盾した状況が起きている(単価が下がった分、より多くの・より高性能なモデルを使うようになったため)。生成AIのコスト管理は、もはや情報システム部門だけの仕事ではなく、財務・各事業部門を巻き込んだ全社的な運用テーマになりつつある。

### 4. コピペで使える部門別コスト配分シート(ひな形)

```
【部署】〇〇部
【対象期間】2026年◯月

| 項目 | 内容 |
|---|---|
| シート課金コスト | ライセンス数 × 単価 = ◯◯円 |
| 従量課金コスト(API) | 入力トークン数 × 入力単価 + 出力トークン数 × 出力単価 = ◯◯円 |
| 内訳(モデル別) | 高性能モデル利用分 ◯◯円 / 標準モデル利用分 ◯◯円 |
| 内訳(用途別) | チャット利用 ◯◯円 / エージェント・自動化ワークフロー利用 ◯◯円 |
| 合計 | ◯◯円 |
| 前月比 | +◯% (増減理由: 例)新規プロジェクトでAPI呼び出しが増加) |
```

この表を部署ごとに毎月作成し、増減理由(特にAPI従量課金・エージェント利用分の急増)を一言添えるだけで、ショーバックの基礎資料として機能する。

## 注意点・よくある誤解

- **無制限の従量課金APIキーを現場に配布しない**: 「とりあえず使ってみて」と予算上限を設定しないままAPIキーを開発チームに渡すと、青天井の請求につながる。実際、ある調査(372社対象)では、AIコストの実績が予算の想定内(誤差10%以内)に収まった企業はわずか15%で、4社に1社近くは50%以上の予測乖離があったと報告されている。前述の「State of FinOps 2026」でも企業の73%がAI予算を超過しており、「単価が下がれば費用も下がる」という思い込みは危険である(リトライ処理やバックグラウンドでの推論など、見えにくい部分の呼び出し回数が増えていることが一因とされる)
- **「予算上限の設定」と「利用の強制停止」は別物と理解する**: OpenAI APIのプロジェクト予算上限のように、多くのプラットフォームの「予算アラート」は閾値到達時に通知が来るだけで、リクエスト自体を止めない仕組みであることが多い。確実に費用の上限を守りたい場合は、プリペイド残高方式にして自動チャージを無効化するなど、ハードに止まる設定を別途行う必要がある
- **公開・放置されたAPIキーのリスク**: 認証情報(APIキー)がコードやリポジトリに誤って公開されると、第三者に悪用され短時間で高額請求が発生する事例が報告されている(数万件規模の不正リクエストによって、想定していた予算上限を大幅に超過したケースなど)。APIキーはコードに直書きせず、環境変数・シークレット管理の仕組みで扱う
- **AIエージェントの多重呼び出しでコストが跳ね上がる構造を理解する**: Gartnerは2026年3月、エージェント型AIのタスクは通常のチャット応答に比べて**タスクあたり5〜30倍程度のトークンを消費する**と指摘している(エージェントは複数ステップの処理のたびに、それまでの会話履歴・システムプロンプトを含む文脈全体を毎回モデルに読み込ませ直すため、同じ文脈に何度も課金される構造になっているのが主因)。さらに2026年8月には、「トークン単価は2030年までに9割下がる見通しである一方、エージェント型ワークフロー1件あたりの推論コストは2028年までに5倍超に増える」という一見矛盾した予測(Gartnerはこれを「推論のパラドックス」と呼ぶ)を発表しており、モデルの世代が上がるほど、より複雑で・より高価なトークンを使うようになる構造が背景にある。Gartnerは2025年6月時点でも、ガバナンス不足・投資対効果の不透明さ・コストの制御不能を主な理由に、**2027年末までにエージェント型AIプロジェクトの4割超が中止に追い込まれる**と予測しており、エージェント活用を広げる際は「1件あたりの呼び出し回数の上限」「1タスクあたりのコスト上限」を事前に設計しておくことが欠かせない
- **大企業でも青天井になった実例がある**: 報道によれば、ある大手企業では開発者向けAIコーディングツールの利用が数か月で社内に急拡大し、年間のAI予算を数か月で使い切ったとされる。また、社内に一律で制限のないAI利用権限を与えた結果、月間の請求額が非常に高額に達したという事例も報道されているが、こちらは企業名が明らかにされていない伝聞情報であり、裏付けの取れた統計ではなく「起こり得るリスクの実例」として参考にとどめるべきである
- **ChatGPTなどのサブスク契約とAPI従量課金は別会計**: 「ChatGPT Plus/Businessを契約しているから、API経由の利用も安くなる・含まれる」と誤解しやすいが、両者は完全に別契約・別請求である。社内のどこかの部署がAPIを直接契約して使っている場合、シート課金の請求書だけを見ていては全社の生成AI支出を把握できない

## 最初の一歩

自社で契約している生成AIツール(ChatGPT・Copilot・Claude・Gemini等)とAPIキーを洗い出し、それぞれの管理画面で直近1か月の利用状況・請求額を確認する。特にAPIキーについては、予算上限が「通知だけ」なのか「実際に止まる」設定なのかを必ず確認しておく。

## 関連トピック

- [生成AI導入のROI測定・効果測定の考え方](ai-roi-measurement.md)
- [生成AI導入の社内展開・浸透のすすめ方](ai-adoption-rollout-basics.md)
- [生成AIに向く業務・向かない業務の切り分け](ai-task-suitability.md)
- [トークンとは何か](../part02-llm-basics/what-are-tokens.md)

## 更新履歴

### 2026-08-28: 料金プラン・統計データを最新化
- **内容**: ChatGPT Businessに5倍利用量・5時間上限撤廃の新シート「Premium」($125/$100)が2026年8月に新設された点、Microsoft 365 Copilot Businessの特別価格($18)の適用期間が2026年12月31日まで延長された点、Claude Teamのシート数下限が2026年7月20日に5席→2席へ緩和され上限150席が明示された点、Claude Enterpriseがセルフサーブ最低20席・営業経由最低50席である点を反映。FinOps Foundation「State of FinOps 2026」の新データ(AI予算超過企業73%、エージェント型プロジェクトの予算超過率2.4倍、トークン単価8割下落に対しAI支出総額は4.8倍に増加)、Gartnerが2026年8月に発表した「推論のパラドックス」(トークン単価は下がるがエージェント型ワークフローの推論コストは2028年までに5倍超に増加)を追加。Anthropic公式のClaude Code実コスト目安(開発者1人・1日$13、月$150〜250)、Copilot Studioクレジットの機能別消費量(エージェントのアクション1回で25クレジット以上)を新たに追記
- **出典**: [ChatGPT Business Pricing: The New $125 Premium Seats - tokenkarma](https://tokenkarma.app/blog/chatgpt-business-premium-seats-pricing-2026/)、[ChatGPT Business Adds $125 Premium Seat for Power Users Hitting Five-Hour Cap - Tech Times](https://www.techtimes.com/articles/323905/20260811/chatgpt-business-adds-125-premium-seat-power-users-hitting-five-hour-cap.htm)、[Microsoft 365 Copilot Plans and Pricing (公式)](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)、[Claude Team Now Starts at 2 Seats - Pasquale Pillitteri](https://pasqualepillitteri.it/en/news/8545/claude-team-2-seats-small-teams)、[Anthropic Cuts Claude Team Plan Minimum to Two Seats - AI News Blitz](https://www.ainewsblitz.com/brief/ue66jgUJWFuS)、[What is the Team plan? - Anthropic Help Center](https://support.claude.com/en/articles/9266767-what-is-the-team-plan)、[Claude Pricing 2026 - CloudZero](https://www.cloudzero.com/blog/claude-pricing/)、[Manage costs effectively - Claude Code Docs](https://code.claude.com/docs/en/costs)、[State of FinOps 2026 Report - FinOps Foundation](https://data.finops.org/)、[AI FinOps in 2026: 73% Blow Budget, 98% Now Track - THE D*AI*LY BRIEF](https://www.beri.net/article/ai-finops-2026-73-percent-blow-budget-cfo-fix)、[The State of FinOps 2026 Report - Revenium](https://www.revenium.ai/post/the-2026-state-of-finops-report)、[Gartner Predicts AI Inference Costs Per Agentic Workflow Will Increase More Than Fivefold Through 2028 (公式)](https://www.gartner.com/en/newsroom/press-releases/2026-08-17-gartner-predicts-ai-inference-costs-per-agentic-workflow-will-increase-more-than-fivefold-through-2028)、[Agentic AI costs set to balloon fivefold by 2028 - The Register](https://www.theregister.com/ai-and-ml/2026/08/17/agentic-ai-costs-set-to-balloon-fivefold-by-2028/)、[Agentic AI Inference Cost: Why Agents Burn 5-30x Tokens - Spheron](https://www.spheron.network/blog/agentic-ai-inference-cost-2026/)、[Gartner Predicts Over 40% of Agentic AI Projects Will Be Canceled by End of 2027 (公式)](https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-predicts-over-40-percent-of-agentic-ai-projects-will-be-canceled-by-end-of-2027)、[Copilot Studio Pricing in 2026: What Credits Actually Cost - Coworker](https://coworker.ai/blog/copilot-studio-pricing)

### 2026-07-25: 初版執筆
- **内容**: トークン課金の基本構造(シート課金と従量課金の違い)、ChatGPT Business/Enterprise・Microsoft 365 Copilot・Claude Team/Enterprise・Gemini for Workspaceの2026年7月時点の価格帯、部門別予算配分・社内チャージバック(ショーバック→チャージバックの段階的導入、OpenAI Projects・Anthropic Workspaces・Azure Cost Managementタグ付けによる可視化)、AIエージェントの多重呼び出しによるコスト増大リスク(Gartnerのトークン消費倍率・プロジェクト中止予測)、無制限APIキー配布や公開APIキー流出による請求書ショックの実例を整理
- **出典**: [ChatGPT Enterprise Pricing - Coworker](https://coworker.ai/blog/chatgpt-enterprise-pricing)、[ChatGPT for Work Pricing - eesel AI](https://www.eesel.ai/blog/chatgpt-work-pricing)、[Microsoft 365 Copilot Pricing (公式)](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing)、[Microsoft 365 Copilot Studio Pricing (公式)](https://www.microsoft.com/en-us/microsoft-365-copilot/pricing/copilot-studio)、[Claude Enterprise Pricing - tl;dv](https://tldv.io/blog/claude-enterprise-pricing/)、[Google includes Gemini in Workspace with new pricing model - AppXite](https://www.appxite.com/blog/google-includes-gemini-ai-into-workspace-with-new-pricing-model)、[Gemini Enterprise Pricing - Coworker](https://coworker.ai/blog/gemini-enterprise-pricing)、[FinOps for AI Overview - FinOps Foundation](https://www.finops.org/wg/finops-for-ai-overview/)、[FinOps X 2026 Day 1 Keynote - FinOps Foundation](https://www.finops.org/insights/finops-x-2026-day-1-keynote/)、[LLM Cost Management: AI Showback and Chargeback - Kong](https://konghq.com/blog/enterprise/llm-cost-management-ai-showback-and-chargeback)、[OpenAI Spend Limit: How to Cap Your API Bill - Alephant](https://blog.alephant.io/openai-spend-limit-how-to-cap-your-api-bill-2026/)、[Creating and Managing Workspaces in the Claude Console - Claude Help Center](https://support.claude.com/en/articles/9796807-creating-and-managing-workspaces-in-the-claude-console)、[Managing Azure OpenAI Costs with the FinOps Toolkit and FOCUS - Microsoft Tech Community](https://techcommunity.microsoft.com/blog/finopsblog/managing-azure-openai-costs-with-the-finops-toolkit-and-focus-turning-tokens-int/4413886)、[Microsoft Copilot Usage Reports - Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/admin/activity-reports/microsoft-copilot-usage)、[AI Agent Token Sprawl - Tentoro](https://tentoro.ai/blog/ai-agent-token-sprawl/)、[Agentic AI Costs at Scale - Cockroach Labs](https://www.cockroachlabs.com/blog/agentic-ai-costs-at-scale/)、[Uber CTO Shows Claude Code Can Blow AI Budgets - The Information](https://www.theinformation.com/newsletters/applied-ai/uber-cto-shows-claude-code-can-blow-ai-budgets)、[Uber Burns Its 2026 AI Budget In Four Months On Claude Code - Forbes](https://www.forbes.com/sites/janakirammsv/2026/05/17/uber-burns-its-2026-ai-budget-in-four-months-on-claude-code/)、[Claude AI Costs Climb: Company Spent Half a Billion Dollars in a Single Month - Fast Company](https://www.fastcompany.com/91550884/claude-ai-costs-climb-company-spent-half-a-billion-dollars-in-a-single-month-report)、[The Agentic AI Tax: Why Your Token Budget Is About To Explode - VamsiTalksTech](https://www.vamsitalkstech.com/ai/the-agentic-ai-tax-why-your-token-budget-is-about-to-explode/)、[Google Cloud Customer Wakes Up to $18,000 Bill Despite $7 Budget - Tom's Hardware](https://www.tomshardware.com/tech-industry/artificial-intelligence/google-cloud-customer-wakes-up-to-usd18-000-bill-despite-usd7-budget-thanks-to-forgotten-public-api-key-attacker-put-in-60-000-requests-and-blasted-through-usd1-400-spending-cap)
