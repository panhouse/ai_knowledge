---
title: サイバーセキュリティ業界における生成AI活用事例
part: 14
chapter: "第6章 IT・情報通信"
tags: [サイバーセキュリティ, AI SOC, ペネトレーションテスト, フィッシング検知, セキュリティベンダー, プロンプトインジェクション, Security Copilot, Charlotte AI, XBOW]
created: 2026-08-27
updated: 2026-08-27
---

# サイバーセキュリティ業界における生成AI活用事例

## これは何か

サイバーセキュリティ業界(セキュリティ製品・サービスを開発・提供する側)は、生成AIを
「自社の防御力を上げる道具」として使うと同時に、「自社製品にAI機能を組み込んで売る」
という2つの立場で生成AIと向き合っている珍しい業界である。SOC(Security Operation
Center、セキュリティ監視・分析を専門に行う組織)のアラート一次判定にAIコパイロットを
組み込み、ペネトレーションテスト(実際の攻撃手法を模した侵入テスト)をAIエージェントに
自動実行させ、フィッシングメールの判定にLLM(大規模言語モデル)を使う——こうした
動きがこの2〜3年で一気に製品の標準機能になった。一方で、攻撃側も同じ生成AIを使うため、
「防御のためのAI」と「攻撃を助長するAI」がせめぎ合う構図が業界そのものの競争環境と
製品開発の方向性を規定している。本ページは、この**業界全体で何が起きているか・
ビジネス上どう捉えるべきか**を整理する事例カタログである。似た名前の2ページとは
以下のように役割が異なるので、目的に応じて使い分けてほしい。

- [情報セキュリティ担当者(SOC/CISO)における生成AI活用事例](../part15-job-role-cases/information-security-ai-use-cases.md)(Part 15): **自社の情シス・SOC担当者**が、アラート対応や報告書作成といった**自分の日々の業務**に生成AIをどう使うかという、職種目線の活用パターン集
- [セキュリティ(サイバーセキュリティ)AI企業一覧](../part16-japan-ai-companies/security-ai-companies-japan.md)(Part 16): 国内のセキュリティAIベンダー**各社**のプロフィールを集めた企業ディレクトリ
- 本ページ(Part 14): セキュリティ**業界そのもの**が生成AIをどう製品・事業に組み込んでいるか、業界の力学とビジネス上の判断材料を扱う

## 仕組み・背景

生成AIがセキュリティ業界の製品開発・事業運営に急速に組み込まれている背景には、
大きく4つの流れがある。

**1. 「AI SOC」が主要ベンダー共通の製品戦略になった**: SIEM(ログを集約・相関分析する
セキュリティ監視基盤)やEDR(端末上の不審な挙動を検知・対応する仕組み)を提供する
ベンダーは軒並み、アラートの一次トリアージ・調査・報告書作成を助言・自動化する
AIコパイロット機能を主力製品に組み込んでいる。Microsoft Security Copilot、Google
Gemini in Security Operations、CrowdStrike Charlotte AI、トレンドマイクロの
TrendAI Companion(2023年7月に「Trend Companion」として提供開始し、2026年に
ブランドを刷新)などが代表例で、Gartnerは2028年までにAIアプリケーションが
インシデント対応業務の50%を担うと予測している([Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-03-17-gartner-predicts-ai-applications-will-drive-50-percent-of-cybersecurity-incident-response-efforts-by-2028))。この領域の活用シーン・プロンプト例の詳細は
[情報セキュリティ担当者における生成AI活用事例](../part15-job-role-cases/information-security-ai-use-cases.md)に譲る。

**2. 攻撃側検知(フィッシング・マルウェア判定)にLLMが実戦投入されている**: 生成AIで
作成されたフィッシングメールは年々巧妙化しており、Cofenseの調査では2025年に
19秒に1通のペースで悪意あるメールが確認され(2024年の42秒に1通からほぼ倍増)、
Hoxhuntの調査では2025年末の繁忙期にAI生成フィッシングの検知件数が急増し全報告の
56%を占めたとされる([Cofense](https://cofense.com/Blog/Cofense-Report-Reveals-AI-Powered-Phishing-Accelerated-to-One-Attack-Every-19-Seconds)、[Hoxhunt](https://hoxhunt.com/guide/phishing-trends-report))。「日本語の不自然さ」で見破れる時代ではなくなったため、防御側もLLMにメール本文を
解析させ判定理由まで提示する製品(例: NTTセキュリティ・ジャパンの「ChatSpamDetector」)
で対抗している([NTTセキュリティ・ジャパン](https://jp.security.ntt/insights_resources/tech_blog/chatspamdetector-ai/))。

**3. 脆弱性診断・ペネトレーションテストがAIエージェントによって自動化され始めている**:
自律型AIペネトレーションテストツール「XBOW」は2025年4〜6月にHackerOneの米国
バグバウンティ(脆弱性報告への報奨金制度)ランキングで人間のハッカーを抜いて
1位となり、この3か月間だけで致命的(Critical)54件・重大(High)242件を含む
多数の脆弱性を報告した([GIGAZINE](https://gigazine.net/gsc_news/en/20250625-hackerone-xbow/)、[Help Net Security](https://www.helpnetsecurity.com/2025/06/25/xbow-ai-funding/))。国内でもGMOグループの「Takumi byGMO」(2025年3月提供開始、URLを指定するだけで
AIエージェントが診断作業を再現)や「AIホワイトハッカー byGMO」のように、AIによる
自動診断と人間のホワイトハッカーによる深掘りを組み合わせるハイブリッド型の
サービスが広がっている(詳細は[セキュリティAI企業一覧](../part16-japan-ai-companies/security-ai-companies-japan.md)を参照)。Gartnerは2027年までに大企業のペネトレーションテスト業務の40%超がAI支援自動化を
取り入れると予測している([Bishop Fox調査を引用したまとめ記事](https://mindgard.ai/blog/top-ai-pentesting-tools)より)。

**4. 攻撃側の生成AI悪用が、業界の脅威モデルそのものを塗り替えている**: 2025年11月、
Anthropicは自社のClaudeが中国政府系とみられるハッカー集団(GTG-1002)によって
悪用され、世界初とみられる「AIがほぼ自律的に実行したサイバースパイ活動」を検知・
阻止したと公表した。攻撃全体の80〜90%をAIが人間の介入なしに実行し、約30の
組織(大手テック企業・金融機関・化学メーカー・政府機関)が標的にされ、一部で
侵入に成功していたとされる(AIのハルシネーションが完全自律化の壁になっている
とも指摘されている)([Anthropic](https://www.anthropic.com/news/disrupting-AI-espionage))。日本でもIPA(情報処理推進機構)が2026年1月公表の「情報セキュリティ10大脅威 2026」
組織編で、「AIの利用をめぐるサイバーリスク」を**初選出でいきなり3位**にランクイン
させており、AIによる攻撃の巧妙化・自動化を国内でも重大なリスクと位置づけている
([IPA](https://www.ipa.go.jp/pressrelease/2025/press20260129.html))。

これら4つの流れが同時に進行しているため、セキュリティ業界の製品カタログは
「防御AI」と「攻撃対応AI」の両方を素早く更新し続ける必要に迫られており、
市場規模も拡大している。Gartnerは「AIを保護する」市場(AI TRiSM: AI Trust, Risk
and Security Management)が2027年に約48億ドル規模に達すると予測しており
([Gartner](https://www.gartner.com/en/newsroom/press-releases/2026-08-26-gartner-forecasts-the-market-for-securing-ai-will-reach-almost-5-billion-in-2027))、これは「AIでセキュリティ業務を助ける」市場とは別に、「AI自体を守る」市場も
急拡大していることを示している。

## 使いどころ・使い分け

セキュリティ業界における生成AIの活用は、目的によって着目すべきポイントが大きく異なる。
自社が「セキュリティ製品を選ぶ・使う側」なのか、この業界のビジネス動向を
把握したいのかで、以下のように整理すると理解しやすい。

### 活用領域別の対応マップ

| 活用領域 | 何をAIにやらせるか | 代表的な製品・プレイヤー | 向いている組織 |
|---|---|---|---|
| SOC運用支援(AI SOC) | アラートの一次トリアージ、ログ要約、調査レポート作成 | Microsoft Security Copilot、Google Gemini in SecOps、CrowdStrike Charlotte AI、トレンドマイクロ TrendAI Companion、国内MSSPのAI SOCサービス | 24時間監視でアラート量が人力の限界を超えている組織(詳細は[Part 15の該当ページ](../part15-job-role-cases/information-security-ai-use-cases.md)) |
| 脆弱性診断・ペネトレーションテスト | 攻撃者視点での脆弱性探索・悪用検証・報告書ドラフト作成 | XBOW、NodeZero、Takumi byGMO、AIホワイトハッカー byGMO | 診断の頻度・範囲を増やしたいが人手のホワイトハッカーが不足している組織 |
| フィッシング・マルウェア検知 | メール本文・添付ファイル・通信挙動の解析、判定理由の提示 | ChatSpamDetector、各社EDR/メールセキュリティ製品のAI機能 | フィッシング被害・誤検知の削減を急ぎたい組織 |
| 脅威インテリジェンス(脅威動向調査) | 大量の脅威レポート・脆弱性情報の要約、攻撃者プロファイリング | Google Threat Intelligence、各社の脅威インテリジェンスサービス | 自社に関係する脅威動向を効率よく追いたいセキュリティ担当・経営層 |
| 生成AIアプリ自体のセキュリティ診断 | プロンプトインジェクション耐性の評価、LLMアプリの脆弱性診断 | GMO Flatt Securityのセキュリティ評価サービス等 | 自社で生成AIを使ったサービス・チャットボットを開発・運用している組織 |

### 従来型(ルールベース)セキュリティ製品 と 生成AI組み込み型製品 の使い分け

| 観点 | 従来型(シグネチャ・ルールベース) | 生成AI組み込み型 |
|---|---|---|
| 得意なこと | 既知パターンの高速・確実な検知、誤検知率の安定 | 未知パターンの推論、自然言語での説明・要約、調査の下準備 |
| 弱点 | 未知の攻撃・巧妙な言い回しに弱い、判定理由が分かりにくいことがある | 判定のブレ・ハルシネーション、モデルへの攻撃(プロンプトインジェクション等)という新しいリスク面 |
| 向く場面 | 大量・高速処理が必要な一次フィルタリング | 人間が最終判断する前の「当たりをつける」工程、文章化・報告書作成 |
| 導入判断のポイント | 検知率・誤検知率の実績、ベンダーの実績年数 | 「AIが何を根拠に判定したか」を人間が検証できる設計(説明可能性)になっているか |

いずれの領域でも共通するのは、**AIは「候補を絞る・下書きを作る」役割にとどまり、
封じ込め・パッチ適用停止・対外報告といった後戻りしにくい最終判断は人間が担う**
という設計思想がベンダー各社に共通している点である。これは業界の技術的な制約
(ハルシネーションのリスク)であると同時に、ベンダーが法的責任を回避するための
ビジネス上の選択でもある。

## 実務での使い方

### シーン1: セキュリティベンダーのAI機能を評価する

「AI搭載」を謳う製品が増えたことで、実質的な差別化要因なのか単なるマーケティング
文句(いわゆる「AIウォッシング」)なのかを見極める必要性が高まっている。ベンダーへの
質問リストを生成AIに作らせておくと、提案書のレビュー・比較検討が効率化できる。

```
セキュリティ製品のベンダー提案書を評価するための質問リストを作成してください。

【製品ジャンル】
(例: EDR / SIEM / メールセキュリティ / 脆弱性診断)

【出力条件】
1. 「AIが何を根拠にどう判定しているか」の説明可能性に関する質問
2. AIの判定の誤検知率・見逃し率の実績値を確認する質問
3. 人間による最終承認プロセス(Human in the Loop)がどう設計されているかを確認する質問
4. 学習データ・入力データの取り扱い(自社のログ・アラートが学習に使われないか)
   に関する質問
5. 障害時・誤判定時の責任分界点(SLA、保証範囲)に関する質問
質問は各項目2〜3個、合計10〜15個程度で、経営層への説明にも使える体裁にしてください
```

### シーン2: 脆弱性診断・ペネトレーションテストの発注仕様を比較する

AIエージェント型の自動診断サービスと、従来の人手中心の診断サービスを比較検討する際、
論点を整理してもらう。

```
Webアプリケーションの脆弱性診断サービスを選定しています。
「AIエージェントによる自動診断」と「人手中心の伝統的なペネトレーションテスト」
を比較する評価表を作ってください。

【出力条件】
- 評価軸: 診断スピード、費用、検出できる脆弱性の種類(自動診断が得意な種類・
  苦手な種類)、報告書の質、誤検知(false positive)の扱い、
  ビジネスロジックの欠陥(業務ルールの不備など、機械的には見つけにくい脆弱性)
  への対応力
- 自社の状況(診断対象、予算、診断頻度)を空欄にしておくので、
  記入すれば個社版の判断材料になる形式にしてください
```

発注前には、実際の診断範囲に「AIによる自動診断のみか」「人間による深掘り
(マニュアル診断)を含むか」を必ず契約条件で確認する。GMOサイバーセキュリティ
byイエラエのように「AIでは検出が難しい脆弱性や誤検出を人間が深掘りする」
ハイブリッド設計を明示しているベンダーもあれば、自動化率を前面に出すベンダーもあり、
自社のリスク許容度に応じて選ぶ。

### ツール横断の対応付け(2026年8月時点)

| カテゴリ | 製品・サービス例 | 主な機能・特徴 |
|---|---|---|
| AI SOCコパイロット | Microsoft Security Copilot、CrowdStrike Charlotte AI、Google Gemini in SecOps、トレンドマイクロ TrendAI Companion | アラート調査支援・要約・レポート作成の自動化。料金体系や国内MSSPサービスの詳細は[情報セキュリティ担当者における生成AI活用事例](../part15-job-role-cases/information-security-ai-use-cases.md)の対応表を参照 |
| AIペネトレーションテスト | XBOW、NodeZero、Takumi byGMO、AIホワイトハッカー byGMO | 攻撃者視点での脆弱性探索・悪用検証を自動化。XBOWは2025年にHackerOneの人間ランキングを上回る成果を報告。国内2社の詳細は[セキュリティAI企業一覧](../part16-japan-ai-companies/security-ai-companies-japan.md)を参照 |
| フィッシング・迷惑メール検知 | ChatSpamDetector(NTTセキュリティ・ジャパン)、各社メールセキュリティ製品のAI機能 | LLMがメール本文・送信元情報を解析し、判定理由を自然言語で提示 |
| 脅威インテリジェンス | Google Threat Intelligence、各社の脅威レポートサービス | 大量の脅威情報・脆弱性情報をLLMが要約し、自社への影響を評価する下準備を支援 |
| 生成AIアプリ自体のセキュリティ診断 | GMO Flatt Securityのセキュリティ評価サービス等 | プロンプトインジェクション耐性など、自社の生成AI活用サービスに潜む脆弱性を評価 |

## 注意点・よくある誤解

- **「AI搭載」は差別化要因とは限らない**: ほぼすべての主要セキュリティ製品がAI機能を
  謳うようになった結果、「AI搭載かどうか」ではなく「そのAIが何を根拠にどう判定し、
  誤検知率・見逃し率がどの程度か」で比較する必要がある。マーケティング文句と
  実質的な機能差を見分ける視点を持つ
- **防御と攻撃は同じ技術基盤の上でせめぎ合っている**: フィッシングメールの巧妙化も
  ペネトレーションテストの自動化も、根っこは同じ生成AI技術である。「攻撃側が
  使えることは防御側もいずれ製品化してくる」という前提で業界の動きを追うと、
  次に何が製品化されるかを先読みしやすい
- **AIによる自動診断・自動検知は大量投下という新しい副作用を生む**: XBOWのような
  自律型ペネトレーションテストツールが大量の脆弱性報告を生成できるようになった
  ことで、質の低い誤検知報告が大量に投下され、審査側(バグバウンティ運営者・
  診断結果を受け取る担当者)の負荷がかえって増えるという懸念も指摘されている
  ([BigGoニュース](https://biggo.jp/news/202506250113_AI_Tool_XBOW_Tops_Bug_Bounty_Rankings))。「自動化=品質向上」と単純に捉えない
- **AIエージェントが攻撃にほぼ自律的に使われる時代が現実に始まっている**:
  Anthropicが2025年11月に公表した事例では、生成AIが攻撃工程の80〜90%を
  人間の介入なしに実行した。ハルシネーションが完全自律化の妨げになっている
  ものの、今後この壁が薄れていく可能性を前提に、自社のセキュリティ製品選定・
  内製の防御体制の両方を見直す必要がある
- **セキュリティ製品自体が生成AIを組み込むほど、その製品自体がプロンプト
  インジェクション(AIへの悪意ある指示混入)の標的になりうる**: AIコパイロットや
  AIエージェントを組み込んだセキュリティ製品は、攻撃者から見れば「新たな攻撃対象」
  でもある。導入時は、その製品自体のAI機能がどのような入力(ログ・メール本文・
  Webページの内容など)を処理しているか、そこに悪意ある指示が紛れ込む余地が
  ないかを確認する(仕組みは[プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md)を参照)

## 最初の一歩

自社が導入している、または導入を検討しているセキュリティ製品を1つ選び、
シーン1のプロンプトでベンダー向けの質問リスト(説明可能性・誤検知率・人間の
最終承認プロセス)を作ってみる。ベンダーとの次回打ち合わせで、その質問リストを
そのまま使って「AI搭載」の中身を確認するところから始められる。

## 関連トピック

- [情報セキュリティ担当者(SOC/CISO)における生成AI活用事例](../part15-job-role-cases/information-security-ai-use-cases.md)
- [セキュリティ(サイバーセキュリティ)AI企業一覧](../part16-japan-ai-companies/security-ai-companies-japan.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)
- [ガードレール(生成AIの入出力安全対策)の基本](../part04-risk-security/ai-guardrails-basics.md)
- [シャドーAI(無許可利用)対策](../part04-risk-security/shadow-ai-basics.md)
- [IT・情報通信における生成AI活用事例](it-telecom-ai-use-cases.md)

## 更新履歴

### 2026-08-27: 初版執筆
- **内容**: サイバーセキュリティ業界における生成AI活用を、(1) AI SOC(主要ベンダーの
  コパイロット製品戦略)、(2) LLMによるフィッシング・マルウェア検知、(3) AIエージェント
  によるペネトレーションテストの自動化(XBOWのHackerOneランキング1位、国内のTakumi
  byGMO等)、(4) 攻撃側の生成AI悪用(AnthropicのGTG-1002事例、IPA「情報セキュリティ
  10大脅威2026」でのAIリスク初選出3位)の4つの流れとして整理。業界動向を俯瞰する
  ビジネス目線の内容とし、SOC/CISOの職種別ページ・国内AI企業ディレクトリと役割分担
  して構成。ベンダーのAI機能を評価する質問リスト・診断サービス比較のコピペ用
  プロンプト例、活用領域別・従来型と生成AI組み込み型の比較表を追加
- **出典**: [Anthropic: Disrupting the first reported AI-orchestrated cyber espionage campaign](https://www.anthropic.com/news/disrupting-AI-espionage)、[IPA: 情報セキュリティ10大脅威2026(プレスリリース)](https://www.ipa.go.jp/pressrelease/2025/press20260129.html)、[GIGAZINE: XBOWがHackerOneランキングで人間を抜いて1位に](https://gigazine.net/gsc_news/en/20250625-hackerone-xbow/)、[Help Net Security: XBOW's AI reached the top ranks on HackerOne](https://www.helpnetsecurity.com/2025/06/25/xbow-ai-funding/)、[BigGoニュース: XBOWの大量脆弱性報告への懸念](https://biggo.jp/news/202506250113_AI_Tool_XBOW_Tops_Bug_Bounty_Rankings)、[Cofense: AI-Powered Phishing Accelerated to One Attack Every 19 Seconds](https://cofense.com/Blog/Cofense-Report-Reveals-AI-Powered-Phishing-Accelerated-to-One-Attack-Every-19-Seconds)、[Hoxhunt: Phishing Trends Report](https://hoxhunt.com/guide/phishing-trends-report)、[NTTセキュリティ・ジャパン: ChatSpamDetector](https://jp.security.ntt/insights_resources/tech_blog/chatspamdetector-ai/)、[Gartner: AI Applications Will Drive 50% of Cybersecurity Incident Response Efforts by 2028](https://www.gartner.com/en/newsroom/press-releases/2026-03-17-gartner-predicts-ai-applications-will-drive-50-percent-of-cybersecurity-incident-response-efforts-by-2028)、[Gartner: Forecasts the Market for Securing AI Will Reach $4.8 Billion in 2027](https://www.gartner.com/en/newsroom/press-releases/2026-08-26-gartner-forecasts-the-market-for-securing-ai-will-reach-almost-5-billion-in-2027)、[Mindgard: Best AI Pentesting Tools in 2026](https://mindgard.ai/blog/top-ai-pentesting-tools)
