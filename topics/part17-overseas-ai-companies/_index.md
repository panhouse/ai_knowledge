---
title: "Part 17: 海外AI企業マップ"
part: 17
---

# Part 17: 海外AI企業マップ

海外(日本国外)でAI関連の事業を展開している企業を、カテゴリ別に一覧できる場所。
Part 16「国内AI企業マップ」の海外版で、「OpenAI・Anthropicのような大手基盤モデル企業は
今どんな立ち位置・戦略を取っているか」「このカテゴリで海外にはどんな会社があるか」を
調べる際のリファレンスとして育てる。

**Part 3・Part 9 との役割分担**: ChatGPT・Claude・Geminiのような大手の「製品としての使い方・
料金プラン・APIの詳細」は、Part 3(AIチャットツールの基本)・Part 9(API・開発連携)の
個別ページ(例: [Claudeの基本](../part03-ai-chat-tools/claude-basics.md)、
[Anthropic APIの基本](../part09-api-development/anthropic-api-basics.md))で深掘りしている。
本パートはそれらと重複させず、**企業としてのプロフィール(資金調達・戦略・提携・強み)**に
絞った軽量カタログとして書く。業界構造・提携動向のより深い分析は
[生成AI業界の主要プレイヤーと動向](../part13-ai-trends/ai-industry-major-players-trends.md)
(Part 13)を参照。

Part 1〜13 が「概念・手法の教科書」、Part 14 が「業種別の活用事例カタログ」、
Part 15 が「職種別の活用事例カタログ」、Part 16 が「国内AI企業マップ」であるのに対し、
Part 17 は **海外企業版の一覧カタログ**。教科書ページのような深掘りの解説記事ではなく、
「一言で何をしている会社か」を短くまとめたディレクトリ形式で書く。

## このパート特有のルール

- **カタログであり教科書ではない**: `templates/topic-page.md` の8セクション構成は使わない。
  `templates/company-directory-page.md` を雛形とし、企業ごとに
  「一言で / 代表プロダクト・サービス / 特徴・強み / 料金の目安 / 最終確認日」の軽量フォーマットで書く
- **1ページ = 1カテゴリ(章の中のサブジャンル)**: 個社1ページではなく、
  同じカテゴリの企業を複数社まとめて1ページに収録する
- **既にPart 3・Part 9に深掘りページがある企業(OpenAI・Anthropic・Google・Microsoft・
  Amazon・Meta・xAIなど)は、製品機能・料金の詳細を重複させない**。「料金の目安」欄は
  当該ページへの内部リンクで済ませ、本パートで書くのは企業としての立ち位置・資金調達・
  戦略・提携に絞る
- **`最終確認日`を各社エントリに必須で入れる**: 資金調達・買収・上場・組織再編などで
  情報がすぐ古くなるため、企業ごとに個別の日付を管理する
- **中立的な事実ベースで書く**: 一次情報(公式サイト・プレスリリース・決算資料)を優先し、
  評判や優劣の主観的な評価は避ける
- **どのカテゴリにも当てはまらない企業は最終章「その他・未分類」に一旦置く**。
  これは一時的な受け皿であり、内容が育って独立した章にできる場合は移動してよい
- **定期的(月1回程度)に見直し**、体系への移動・新しい章としての昇格・情報の陳腐化チェックを
  ユーザーに提案してよい(勝手に体系を変更しない)

## 章構成(分類の地図)

### 第1章 基盤モデル・フロンティアAI系
- OpenAI、Anthropic、Google(Alphabet/DeepMind)、Microsoft、Amazon(AWS)、Meta、
  xAI(SpaceXAI)など欧米の大手基盤モデル企業
- Mistral AI、Cohereなど新興の基盤モデル企業
- DeepSeek、Alibaba(Qwen)、Moonshot AI、Zhipu AIなど中国発の基盤モデル企業
  (章内でページを分けて育てる)

### 第2章 AI半導体・インフラ系
- NVIDIA、AMD、Broadcom、Groq、Cerebrasなど、AI向け半導体・計算基盤を提供する企業

### 第3章 業務ドメイン特化ツール系
- 海外発の業務ドメイン特化AI SaaS企業(章内でページを分けて育てる。想定される切り口の例。
  最初から全部は埋めず、主要ドメインから順に着手する)

### 第4章 その他・未分類
- 上記のどの章にも当てはまらない/分類が難しい企業の一時受け皿

## 収録ページ

- [海外の主要基盤モデル企業一覧(フロンティアAI企業)](foundation-model-companies-overseas.md)
- [欧州発の新興基盤モデル企業一覧](emerging-foundation-model-companies-europe-overseas.md)
- [中国発の基盤モデル企業一覧](china-foundation-model-companies-overseas.md)
- [海外のAI半導体・インフラ企業一覧](ai-chip-infrastructure-companies-overseas.md)
- [海外の契約書・法務AI企業一覧](legal-contract-ai-companies-overseas.md)
- [海外の営業支援AI企業一覧](sales-support-ai-companies-overseas.md)
- [海外のカスタマーサポートAI企業一覧](customer-support-ai-companies-overseas.md)
- [海外のマーケティングAI企業一覧](marketing-ai-companies-overseas.md)
- [海外の人事・採用AI企業一覧](hr-recruiting-ai-companies-overseas.md)
- [海外のデータ分析・BI AI企業一覧](data-analytics-bi-ai-companies-overseas.md)
- [海外の経理・会計AI企業一覧](finance-accounting-ai-companies-overseas.md)
- [海外の会議・文字起こしAI企業一覧](meeting-minutes-ai-companies-overseas.md)
- [海外のコーディング支援AI企業一覧](coding-assistant-ai-companies-overseas.md)
- [海外の画像・動画生成AI企業一覧](image-video-generation-ai-companies-overseas.md)
