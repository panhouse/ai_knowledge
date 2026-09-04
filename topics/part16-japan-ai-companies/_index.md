---
title: "Part 16: 国内AI企業マップ"
part: 16
---

# Part 16: 国内AI企業マップ

日本国内でAI関連の事業を展開している企業を、カテゴリ別に一覧できる場所。
「どこに頼めばいいか」「競合・提携先としてどんな会社があるか」を調べる際の
リファレンスとして育てる。

Part 1〜13 が「概念・手法の教科書」、Part 14 が「業種別の活用事例カタログ」、
Part 15 が「職種別の活用事例カタログ」であるのに対し、
Part 16 は **企業そのものの一覧カタログ**。教科書ページのような深掘りの解説記事ではなく、
「一言で何をしている会社か」を短くまとめたディレクトリ形式で書く。

## このパート特有のルール

- **カタログであり教科書ではない**: `templates/topic-page.md` の8セクション構成は使わない。
  `templates/company-directory-page.md` を雛形とし、企業ごとに
  「一言で / 代表プロダクト・サービス / 特徴・強み / 料金の目安 / 最終確認日」の軽量フォーマットで書く
- **1ページ = 1カテゴリ(章の中のサブジャンル)**: 個社1ページではなく、
  同じカテゴリの企業を複数社まとめて1ページに収録する(例:「議事録AI企業」ページに
  Notta・Rimo・tl;dv提供元などをまとめて掲載)
- **`最終確認日`を各社エントリに必須で入れる**: 資金調達・買収・サービス終了・社名変更などで
  情報がすぐ古くなるため、企業ごとに個別の日付を管理する(ページ全体の`updated`だけでは粒度が粗い)
- **中立的な事実ベースで書く**: 一次情報(公式サイト・プレスリリース)を優先し、
  評判や優劣の主観的な評価は避ける
- **どのカテゴリにも当てはまらない企業は第6章「その他・未分類」に一旦置く**。
  これは一時的な受け皿であり、内容が育って独立した章にできる場合は移動してよい
- **定期的(月1回程度)に見直し**、体系への移動・新しい章としての昇格・情報の陳腐化チェックを
  ユーザーに提案してよい(勝手に体系を変更しない)

## 章構成(分類の地図)

### 第1章 コンサル・SIer系
- 大手コンサル・SIerのAI部門(アクセンチュア、PwC、NTTデータ、富士通、NECなど)
- AI専業コンサルティングファーム

### 第2章 基盤モデル・研究開発系
- 国産LLM・基盤モデルの開発企業(Preferred Networks、Sakana AI、ELYZA、SB Intuitionsなど)

### 第3章 業務ドメイン特化ツール系
- 業務ドメインごとに章内でページを分けて育てる(想定される切り口の例。
  最初から全部は埋めず、主要ドメインから順に着手する)
  - 議事録・文字起こしAI
  - 契約書・法務AI
  - 経理・会計AI
  - 営業支援(SDR・商談支援)AI
  - 人事・採用AI
  - カスタマーサポートAI

### 第4章 ノーコード・エージェント基盤系
- 国産のノーコードAI開発・AIエージェント基盤を提供する企業

### 第5章 研修・人材育成系
- 生成AI研修・AI人材育成を手がける企業(自社(パンハウス)の競合・近接領域でもあり、
  客観的な事実ベースでの整理が特に重要)

### 第6章 その他・未分類
- 上記のどの章にも当てはまらない/分類が難しい企業の一時受け皿

## 収録ページ

- [研修・人材育成系の国内AI企業一覧](ai-training-hr-development-companies-japan.md)
- [ノーコード・エージェント基盤系の国内AI企業一覧](nocode-agent-platform-ai-companies-japan.md)
- [人事・採用AI企業一覧](hr-recruiting-ai-companies-japan.md)
- [経理・会計AI企業一覧](accounting-ai-companies-japan.md)
- [税理士・社労士向けAI SaaS企業一覧](tax-labor-consultant-ai-companies-japan.md)
- [営業支援AI企業一覧](sales-support-ai-companies-japan.md)
- [カスタマーサポートAI企業一覧](customer-support-ai-companies-japan.md)
- [カスタマーサクセス(CS)AI企業一覧](customer-success-ai-companies-japan.md)
- [議事録・文字起こしAI企業一覧](meeting-minutes-ai-companies-japan.md)
- [契約書・法務AI企業一覧](legal-contract-ai-companies-japan.md)
- [国産基盤モデル・研究開発系AI企業一覧](foundation-model-companies-japan.md)
- [コンサル・SIer系のAI企業一覧](consulting-sier-ai-companies.md)
- [物流・SCM AI企業一覧](logistics-scm-ai-companies-japan.md)
- [マーケティング・広告AI企業一覧](marketing-advertising-ai-companies-japan.md)
- [不動産・建設AI企業一覧](realestate-construction-ai-companies-japan.md)
- [医療・ヘルスケアAI企業一覧](healthcare-ai-companies-japan.md)
- [教育・EdTech AI企業一覧](edtech-ai-companies-japan.md)
- [飲食店経営支援AI企業一覧](restaurant-management-ai-companies-japan.md)
- [保険(インシュアテック)AI企業一覧](insurance-insurtech-ai-companies-japan.md)
- [小売・EC特化AI企業一覧(国内)](retail-ec-ai-companies-japan.md)
- [データ分析・BI AI企業一覧(国内)](data-analytics-bi-ai-companies-japan.md)
- [画像・動画生成AI企業一覧(国内)](image-video-generation-ai-companies-japan.md)
- [セキュリティ(サイバーセキュリティ)AI企業一覧](security-ai-companies-japan.md)
- [製造業向け画像検査・予知保全AI企業一覧](manufacturing-inspection-ai-companies-japan.md)
- [翻訳・多言語化AI企業一覧](translation-ai-companies-japan.md)
- [AI専業コンサルティングファーム一覧](ai-specialized-consulting-firms-japan.md)
- [データアノテーション・ラベリングAI企業一覧](data-labeling-annotation-ai-companies-japan.md)
- [気象・防災AI企業一覧](weather-disaster-prevention-ai-companies-japan.md)
- [人事評価・タレントマネジメントAI企業一覧](talent-management-ai-companies-japan.md)
- [カーボンニュートラル・ESG(GHG算定・報告)AI企業一覧](carbon-esg-reporting-ai-companies-japan.md)
- [IT運用監視(AIOps)AI企業一覧](aiops-it-operations-ai-companies-japan.md)
- [与信審査・融資AI企業一覧](credit-screening-lending-ai-companies-japan.md)
- [フードテックAI企業一覧(国内)](foodtech-ai-companies-japan.md)
- [ゲーム開発支援AI企業一覧(国内)](game-development-ai-companies-japan.md)
- [創薬AI企業一覧(国内)](drug-discovery-ai-companies-japan.md)
- [RPA・AI-OCR企業一覧(国内)](rpa-ai-ocr-companies-japan.md)
- [スポーツ・フィットネス業界向けAI企業一覧(国内)](sports-fitness-ai-companies-japan.md)
- [研究開発・特許調査AI企業一覧(国内)](rd-patent-research-ai-companies-japan.md)
- [旅行・観光業界向けAI企業一覧(国内)](travel-tourism-ai-companies-japan.md)
- [官公庁・自治体向けGovTech AI企業一覧(国内)](govtech-ai-companies-japan.md)
- [音声合成・音声認識AI企業一覧(国内)](voice-synthesis-recognition-ai-companies-japan.md)
- [農業テック(アグリテック)AI企業一覧(国内)](agritech-ai-companies-japan.md)
