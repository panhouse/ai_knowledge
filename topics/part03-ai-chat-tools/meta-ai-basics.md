---
title: "Meta AIの基本"
part: 3
chapter: 第5章 主要ツール各論
tags: [Meta AI, Meta, Llama, Muse Spark, WhatsApp, Instagram, LLM]
created: 2026-08-22
updated: 2026-08-22
---

# Meta AIの基本

## これは何か

Meta AI(メタAI)は、Facebook・Instagram・Messenger・WhatsAppを運営するMeta社が提供する生成AIアシスタントで、これらSNS・メッセージアプリの中に直接組み込まれている点が最大の特徴である。ChatGPT・Claude・Geminiのような「単独のチャット画面を開いて使う」アシスタントとは異なり、Meta AIは「Instagramのダイレクトメッセージ(DM)の延長で聞く」「WhatsAppのグループチャットに@メンションで呼び出す」「Ray-Ban Metaのようなスマートグラス(AI内蔵メガネ)で話しかける」といった、既存のコミュニケーションの流れの中に自然に現れる設計になっている。ビジネスパーソンにとっての論点は2つある。1つは「社員が私用のInstagram・WhatsApp経由でMeta AIを既に使っている可能性があり、自社のAI利用ポリシーがそれを想定しているか」という**シャドーAI**(会社が把握・許可していないAI利用)のリスク管理。もう1つは「無料の個人向けMeta AIは、ChatGPT・Claude・Copilotの法人プランのような『学習に使わない』契約が存在しない」という、他の主要チャットAIとは一線を画すデータ利用方針をどう評価するかである。

## 仕組み・背景

- **提供開始と日本展開**: Meta AIは米国で2023年から段階的に提供され、2025年11月25日に日本でも「段階的な提供」が発表された。対応アプリはFacebook・Instagram・Messenger・WhatsAppに加え、単独アプリ「Meta AI」(iOS/Android)とWeb版(meta.ai)。日本ではアプリのアイコンから呼び出す、またはグループチャットで「@Meta AI」とメンションする形で使う。2026年8月時点でも「段階的」の状態が続いており、アカウント・アプリのバージョン・端末によって使える機能に差がある(後述の音声・画像生成機能はこの典型例)。
- **土台となるモデルの世代交代**: 当初のMeta AIはMetaが無償公開してきたオープンウェイト(重みデータが公開されたモデル)LLM「Llama」シリーズ(Llama 3→2025年4月公開のLlama 4)を土台にしていた。ところが2026年4月8日、Meta社内に新設された「Meta Superintelligence Labs(MSL)」が**Muse Spark**という新モデルを発表した。これはMetaとして初めて、重みを公開しない**クローズドモデル**として投入された点が大きな転換であり、「オープンなLlama」を看板にしてきたMeta AIの方針転換を象徴する出来事として報じられている。2026年7月9日には後継の**Muse Spark 1.1**が公開され、メール・カレンダー連携、スライド作成、100万トークンのコンテキスト窓(一度に読み込める文章量)を活かした長期タスクの記憶・要約、医師チームが監修した健康相談対応など、「調べて答える」だけでなく「代わりに作業を進める」エージェント的な機能が強化された。Meta AI本体への展開は2026年7月29日から一部地域で始まっており、日本では2026年8月時点で一部機能がまだ有効化されていない。回答の深さは「Instant(即答)」と「Thinking(深く考える)」の2モードで切り替えられ、将来的には最大16個の推論エージェントを並列に動かす「Contemplating」モードも計画されている。
- **画像生成は別モデル「Muse Image」が担う**: 2026年7月7日、画像生成専用モデル「Muse Image」が発表された。プロンプトからの生成に加え、写真の合成、プリセット、スケッチからの生成、生成後の反復編集(部分修正の繰り返し)に対応し、Meta AI・Instagramストーリーズ・WhatsApp上の画像生成機能を支える。広告主向けには「Advantage+」という広告クリエイティブ自動生成機能にも組み込まれる予定。日本での提供時期は2026年8月時点で未確認。
- **音声・スマートグラス連携**: 会話形式の音声モード「Live AI」は2026年5月時点で英語のみ、米国・カナダを中心にロールアウトが進められており、日本語での音声対話は現時点で限定的。一方、Meta AI内蔵のAIグラス「Ray-Ban Meta」(第2世代)は2026年5月21日に日本での販売が始まり(価格は度付き対応で約7万3,700円〜8万9,100円)、写真・動画撮影やハンズフリーでのMeta AI呼び出しに対応している。音声対話そのものの日本語対応と、AIグラスの日本発売は別のタイムラインで進んでいる点に注意。

## 使いどころ・使い分け

| 状況 | 判断の目安 |
|---|---|
| Instagram・WhatsAppのDMやグループチャットの流れで、ちょっと調べ物をしたい | Meta AIが最も手軽。既存の会話に@メンションで呼び出せ、追加のアプリ切り替えが不要 |
| Instagramストーリーズやチャットにそのまま貼れる画像を作りたい | Meta AI(Muse Image)。生成した画像をその場でSNSに投稿・送信できる導線が強み |
| Ray-Ban Metaを着けて手を使わずに質問・翻訳・写真撮影をしたい | Meta AIが唯一の選択肢(2026年8月時点でこの用途に対応する主要チャットAIは他にない) |
| 資料の下書き・長文の構造化・データ分析・コーディング支援など本格的な業務作業 | ChatGPT・Claude・Gemini・Copilotが本流。Projects/Canvas/Artifacts、Excel連携、法人向けデータ保護契約など業務利用のための機能・実績が厚い |
| 顧客の個人情報・自社の機密情報を入力する作業 | Meta AI(無料の個人向け)は避ける。学習に使わないことを契約で保証する法人プラン(ChatGPT Enterprise、Claude Team/Enterprise、Copilot Business等)を使う |
| InstagramやWhatsAppでの顧客対応(予約受付・商品案内・見込み客対応)を自動化したい | 個人向けMeta AIではなく、法人向けの「Meta Business Agent」(有料、後述)を検討する対象 |
| 社内の全社員向けに汎用AIアシスタントを導入したい | Meta AIはこの用途を想定した製品ではない。ChatGPT Enterprise・Copilot・Claude・Gemini for Workspaceが該当する |

### 主要チャットAIとの比較(2026年8月時点の目安)

| 軸 | Meta AI | ChatGPT | Claude | Gemini | Copilot | Grok |
|---|---|---|---|---|---|---|
| 最大の強み | Instagram/WhatsApp/Messengerへの直接組み込み、AIグラス連携 | 汎用性・エコシステムの広さ | 指示追従・安全性・長文構造化出力 | Google検索・Workspaceとの統合 | Microsoft 365との統合 | X上のリアルタイム投稿データ |
| 土台モデル(2026年8月時点) | Muse Spark 1.1(旧来はLlama 4) | GPT-5系 | Claude Opus/Sonnet系 | Gemini系 | GPT-5系(Azure OpenAI経由) | Grok 4.5/4.3 |
| 主戦場 | 個人の日常利用(SNS上のちょっとした調べ物・画像生成) | 業務全般の下書き・調べもの・コーディング | 業務文書・契約書・コーディングなど正確性が要る作業 | Google検索・Gmail・スプレッドシート連携業務 | Word/Excel/Outlook連携業務 | SNSの反応・トレンド把握 |
| 法人向けプラン・データ保護契約 | 「Meta Business Agent」は顧客対応の自動化に特化、社員向け汎用アシスタントの法人プランは無し | ChatGPT Enterpriseで提供 | Team/Enterpriseで提供 | Gemini for Workspaceで提供 | Copilot for Microsoft 365で提供 | Grok Business/Enterpriseで提供(実績は他社より薄い) |
| 日本語対応 | テキストは対応、音声は英語中心 | 高い | 高い | 高い | 高い | 対応するが硬さの指摘あり |
| 料金 | 基本無料(Meta One Plus/Premiumは2026年5月開始、日本での提供は未確認) | 無料〜Pro月額$200 | 無料〜Max月額$100超 | 無料〜Ultra月額$250 | Microsoft 365サブスクに同梱・別売あり | 無料〜SuperGrok Heavy月額$300前後 |

判断の目安: 「普段使っているSNS・メッセージアプリの中で完結させたい」場面ではMeta AIが便利だが、資料作成・データ分析・機密情報を扱う本格的な業務では、法人向けデータ保護契約が整っているChatGPT・Claude・Gemini・Copilotを使うのが現時点(2026年8月)での実務的な線引きになる。

## 実務での使い方

### アクセス方法

- **Instagram**: DM一覧画面の右上にあるMeta AIのアイコンをタップ、または任意のDM・グループチャットで「@Meta AI」と入力してメンションする
- **WhatsApp**: チャットリスト最上部の丸いMeta AIアイコンをタップ、または既存のグループチャットで「@Meta AI」とメンションする
- **Messenger・Facebook**: チャット一覧・検索バーからMeta AIを呼び出せる(導線はアプリのバージョンにより異なる)
- **単独アプリ・Web版**: iOS/Android向け「Meta AI」アプリ、または[meta.ai](https://meta.ai)からログインなしでも一部機能を利用できる
- **Ray-Ban Meta(AIグラス)**: 「Hey Meta」と話しかけて起動し、写真撮影・翻訳・質問応答をハンズフリーで行える

### 料金(2026年8月時点の目安)

| プラン | 料金目安 | 主な内容 |
|---|---|---|
| 無料 | ¥0 | テキスト対話、Thinkingモードでの推論、Muse Imageによる画像生成など基本機能を利用可(上限あり) |
| Meta One Plus | 月額$7.99程度(2026年5月27日発表) | Thinkingモードの利用上限拡大、画像・動画生成の生成数増加、複数ステップにわたる長い作業への対応強化 |
| Meta One Premium | 月額$19.99程度(2026年5月27日発表) | Meta AI・Instagram・Facebook・Messenger・WhatsApp・AIグラスにまたがる上位機能への拡張アクセス(対象機能はアカウントにより異なる) |
| Meta Business Agent(法人向け) | トークン課金:100万トークンあたり$2.00(2026年8月1日課金開始、無料試用期間終了後) | WhatsApp/Instagram/Messengerでの顧客対応(質問応答・商品提案・予約受付・リード対応・成約まで)を自動化する有料エージェント。1件のWhatsAppやり取りあたり数セント程度が目安 |

Meta Oneは2026年6月にシンガポール・グアテマラ・ボリビアで先行テストが始まり、その後グローバル展開が予定されている段階で、2026年8月時点で日本での提供開始は確認できていない。無料版の基本機能はどの地域でも維持される。料金・提供国は変更が頻繁なため、契約前に[Meta Help Center](https://www.meta.com/help/artificial-intelligence/)で最新情報を確認すること。

### 具体的な使い方の例

**例1: Instagramのグループチャットで日程調整**

```
@Meta AI このグループの過去の発言から、みんなが空いていそうな
今週末の候補日を1つ提案してください。
```

**例2: Muse Imageで販促用の画像素材を作る**

```
海沿いのカフェでラテを飲んでいる猫のイラストを、
水彩画風で、Instagramストーリーズに使える縦長比率で描いてください。
```

**例3: WhatsAppでの海外顧客対応の自動化(Meta Business Agent想定)**

自社の商品カタログをWhatsApp Business Platformに連携させ、Meta Business Agentに
「営業時間・在庫・価格に関する質問には自動で回答し、予約が必要な相談は
人間の担当者に引き継ぐ」という運用ルールを設定する。

### ツール横断の対応付け

| 概念 | Meta AI | ChatGPT | Claude | Gemini | Grok |
|---|---|---|---|---|---|
| 土台モデル | Muse Spark 1.1(旧Llama 4) | GPT-5系 | Claude Opus/Sonnet系 | Gemini系 | Grok 4.5/4.3 |
| 画像生成 | Muse Image | DALL-E系・Sora | 非対応 | Imagen・Veo | Grok Imagine |
| 深い推論モード | Thinking / Contemplating(計画中) | 推論モデル(o系→GPT-5 Thinking等) | 拡張思考(Extended Thinking) | Deep Think | 推論モード |
| 顧客対応の自動化(法人向け) | Meta Business Agent(WhatsApp/Instagram/Messenger) | GPTs・Agent系機能 | Claude Cowork等 | Gemini Spark | 該当機能は薄い |
| ハンズフリー・ウェアラブル連携 | Ray-Ban Meta(AIグラス) | 該当製品なし | 該当製品なし | 該当製品なし | 該当製品なし |

## 注意点・よくある誤解

- **無料の個人向けMeta AIには「学習に使わない」契約が存在しない**: Metaは、Facebook・Instagramの公開投稿・コメント・キャプション・AI機能へのやり取りなどの公開情報を生成AIの学習に利用しており、WhatsAppのような非公開メッセージの内容は対象外としているものの、公開アカウントの投稿・タグ付けされた写真・コメントでの言及は学習・生成の対象になり得る。EU・英国居住者はGDPR(EU一般データ保護規則)に基づき異議申立てフォームによるオプトアウトが用意されているが、米国や日本など他地域には包括的な「学習利用を止める」ボタンは無く、「自分の個人情報がAIの出力に含まれていた」ことを具体的に示した上で異議を申し立てる方式にとどまる。しかも、自分の写真・投稿がAIの学習・生成に使われても本人に通知は届かない。ChatGPT Team/Enterprise・Claude Team/Enterprise・Copilot Businessのような「契約上学習に使わない」保証がある法人プランとは前提が異なるため、業務の機密情報・顧客の個人情報は無料のMeta AIには入力しないこと
- **社員が私用アプリ経由で既に使っている可能性(シャドーAI)**: Meta AIはInstagram・WhatsApp・Messengerという、社員が私用で日常的に使っているアプリに標準搭載されている。会社のAI利用ポリシーが「ChatGPT・Copilotの利用ルール」しか定めていない場合、Meta AIが対象外になっているケースがあるため、ポリシーの見直し時にMeta AIも明記すること
- **日本での機能提供はまだ「段階的」**: 2025年11月の提供開始から2026年8月時点まで一貫して「段階的なロールアウト」の状態が続いており、アカウント・アプリのバージョンによって使える機能が異なる。特に音声対話(Live AI)は英語・北米中心で日本語対応は限定的、Muse Imageの日本提供時期も本稿執筆時点で未確認であり、「海外の記事に書かれている機能が日本でも同じように使える」とは限らない
- **Meta AI(製品)とLlama(オープンウェイトモデル)は別物**: これまでMeta AIはMetaが無償公開する「Llama」を土台にしてきたが、2026年4月以降の新モデル「Muse Spark」は重みを公開しないクローズドモデルである。「Meta AIは無料だからLlamaも今後すべて自社で自由に使える」という理解は誤りで、開発者・企業がLlamaのようなオープンウェイトモデルを自社基盤で動かす話と、消費者向けアプリのMeta AIを使う話は分けて考える必要がある(オープンウェイトモデルの選び方は[オープンソースAIモデルのライセンス比較](../part08-specialized-ai-tools/open-source-model-license-comparison.md)を参照)
- **Meta Business Agentは「WhatsApp前提」の設計**: 日本ではLINEが主要な顧客対応チャネルであり、WhatsAppを軸にしたMeta Business Agentの価値は海外展開・インバウンド顧客対応など一部の業態に限られる。Instagram DMを軸にしたEC・D2Cブランドの顧客対応自動化であれば検討余地があるが、「全社員向けの業務効率化ツール」としての位置づけではない点を理解しておく

## 最初の一歩

Instagram・WhatsAppなど既に使っているアプリで、個人的な調べ物(業務情報は入力しない)にMeta AIを試してみる。あわせて、自社のAI利用ポリシーに「Meta AI」が明記されているかを確認し、なければ情報システム部門・法務部門に相談する。

## 関連トピック

- [Google Geminiの基本](google-gemini-basics.md)
- [Grok(xAI)の基本](grok-basics.md)
- [Gemini・Claude・Copilotの初期設定とデータ利用オプトアウト比較](ai-chat-tools-privacy-and-setup-comparison.md)
- [オープンソースAIモデルのライセンス比較(商用利用時の論点)](../part08-specialized-ai-tools/open-source-model-license-comparison.md)

## 更新履歴

### 2026-08-22: 初版執筆
- **内容**: Meta AIの位置づけ(WhatsApp/Instagram/Facebook/Messengerへの組み込み、AIグラス連携)、日本での提供開始(2025年11月25日・段階的ロールアウト継続中)、土台モデルの変遷(Llama 4→クローズドモデルのMuse Spark/Muse Spark 1.1、画像生成のMuse Image)、ChatGPT/Claude/Gemini/Copilot/Grokとの比較表、料金(無料版・Meta One Plus/Premium・法人向けMeta Business Agentのトークン課金)、具体的な使い方の例、データ利用・オプトアウトの地域差やシャドーAIリスクなどの注意点を整理
- **出典**: [Meta about.fb.com(日本語): Meta AIを日本で段階的に提供開始](https://about.fb.com/ja/news/2025/11/meta-ai-gradual-rollout-begins-in-japan/)、[enterprisezine: 「Meta AI」を日本で段階的に提供開始](https://enterprisezine.jp/news/detail/23210)、[日本経済新聞: メタAI、日本で提供開始](https://www.nikkei.com/article/DGXZQOUC253I10V21C25A1000000/)、[About Meta: Introducing Muse Spark](https://about.fb.com/news/2026/04/introducing-muse-spark-meta-superintelligence-labs/)、[About Meta: Meta AI Doesn't Just Think, It Acts(Muse Spark 1.1)](https://about.fb.com/news/2026/07/meta-ai-muse-spark-doesnt-just-think-it-acts/)、[TechCrunch: Meta debuts the Muse Spark model in a 'ground-up overhaul' of its AI](https://techcrunch.com/2026/04/08/meta-debuts-the-muse-spark-model-in-a-ground-up-overhaul-of-its-ai/)、[VentureBeat: Goodbye, Llama? Meta launches new proprietary AI model Muse Spark](https://venturebeat.com/technology/goodbye-llama-meta-launches-new-proprietary-ai-model-muse-spark-first-since)、[AI Watch(Impress): 新モデル「Muse Spark 1.1」を採用したMeta AI提供開始](https://ai.watch.impress.co.jp/docs/news/2130031.html)、[CNBC: Meta enters AI image model race(Muse Image)](https://www.cnbc.com/2026/07/07/meta-ai-muse-image.html)、[About Meta: Introducing Muse Image](https://about.fb.com/news/2026/07/introducing-muse-image-meta-ai/)、[simonwillison.net: Meta's new model is Muse Spark](https://simonwillison.net/2026/Apr/8/muse-spark/)、[MindStudio: How to Use Meta AI's Contemplating Mode](https://www.mindstudio.ai/blog/meta-ai-contemplating-mode-parallel-agents)、[ChatForest: Meta Is Finally Charging for AI(Meta One)](https://chatforest.com/reviews/meta-ai-subscription-meta-one-plus-premium-social-media-plans-may-2026/)、[Meta Help Center: About Meta One Premium plans](https://www.meta.com/help/artificial-intelligence/1864308977565149/)、[Enterprise DNA: Meta Ends Free Window for WhatsApp AI Agents on August 1](https://enterprisedna.co/resources/news/meta-business-agent-billing-august-1-token-pricing-2026/)、[SocialDay: Meta Business Agent billing starts 1 August at $2 per million tokens](https://socialday.live/features/meta-business-agent-billing-starts-1-august-at-2-per-million-tokens)、[POKER FACE: Ray-Ban Meta AIグラスの取り扱いがスタート](https://www.pokerface-web.com/topics/49114/)、[Norton: How to opt out of Meta AI](https://us.norton.com/blog/ai/how-to-opt-out-of-meta-ai)、[MIT Technology Review: How to opt out of Meta's AI training](https://www.technologyreview.com/2024/06/14/1093789/how-to-opt-out-of-meta-ai-training/)
- **注記**: about.fb.com・aismiley.co.jp等の一部公式・準公式ページは本セッションからのネットワークアクセスが制限されており、検索エンジンの要約・複数の第三者記事の突き合わせに基づく記述を含む。Meta AI・Muse Spark/Muse Image・Meta Oneの提供国・機能範囲は変更が非常に頻繁なため目安とし、業務判断の前には必ず公式サイト・自社ポリシーで最新情報を確認すること
