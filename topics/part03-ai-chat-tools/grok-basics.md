---
title: "Grok(xAI)の基本"
part: 3
chapter: 第5章 主要ツール各論
tags: [Grok, xAI, X, LLM]
created: 2026-07-06
updated: 2026-07-06
---

# Grok(xAI)の基本

## これは何か

Grok(グロック)は、Elon Musk(イーロン・マスク)が率いる米国企業xAIが開発する生成AIで、SNS(ソーシャル・ネットワーキング・サービス)「X」(旧Twitter)に深く組み込まれている点が最大の特徴である。ChatGPT・Claude・Geminiが「文章作成・調べもの・コーディングの汎用アシスタント」として使われるのに対し、Grokは「Xのリアルタイムの投稿データに直接アクセスし、今この瞬間のSNS上の話題・世論・反応を踏まえて答える」ことに強みを持つ。ビジネスパーソンにとっての論点は、「炎上・トレンド・世論の動きを即座に把握したいときの選択肢になり得るか」と、「モデレーション(不適切な出力を抑える運用)の緩さゆえに業務利用のリスクをどう見積もるか」の2点に集約される。

## 仕組み・背景

- **xAIの成り立ち**: xAIは2023年7月にElon Muskが設立したAI企業で、Grokの初代モデルは同年11月に公開された。2025年3月にXを買収・統合し、Xのユーザーデータ・投稿ネットワークを自社のAI開発に直接活用できる体制を作った。2026年2月にはさらにSpaceXと株式交換で統合し、宇宙開発・AI・SNSを束ねる巨大複合企業となっている(資金調達・業界再編の詳細は[生成AI業界の主要プレイヤーと勢力図](../part12-ai-trends/ai-industry-major-players-trends.md)を参照)。
- **モデルの世代交代が非常に速い**: Grok 3(2025年前半)→Grok 4(2025年7月、推論=複雑な問題を段階的に考えるモードを搭載)→Grok 4.1→Grok 4.20(コンテキスト窓=一度に読み込める文章量が2Mトークンまで拡大)→Grok 4.3(2026年4月、コンテキスト窓1Mトークン・動画入力に対応)という順で数か月おきに更新されており、2026年7月時点の最新の主力モデルはGrok 4.3である。軽量・低コスト版のGrok 4 Fast/Grok 4.1 Fastも並行して提供されている。次世代の「Grok 5」は2026年7月時点で開発中と報じられているが、正式リリースはまだ先になる見込み。
- **「政治的正しさに縛られない」という設計方針**: xAIはGrokを「最大限に真実を追求する(maximally truth-seeking)」AIと位置づけ、他社の生成AIより表現の自由度を高く保つ方針を公にしている。これは「率直な回答が得られる」という評価につながる一方、後述する差別的発言や性的なディープフェイク画像生成といった深刻な事故を繰り返す要因にもなっており、両面で捉える必要がある。
- **リアルタイムのX投稿データへのアクセス**: Grokの回答生成の裏側では、Web検索に加えてX上の投稿を直接検索・引用できる「DeepSearch」という多段階リサーチ機能が動いている。これによりニュース記事だけでなく「Xで今どう反応されているか」まで一度に調べられる点が、ChatGPT・Claude・Geminiの標準的なWeb検索機能との違いになる。
- **エコシステムの広がり**: 画像・動画生成機能「Grok Imagine」、コーディング用エージェント環境「Grok Build」、AI生成の百科事典「Grokipedia」(2025年10月開始、Wikipediaの内容を偏っているとしてMuskが対抗して立ち上げたが、Grokipedia自身の内容にも偏りがあるとの分析が出ている)など、GrokはXやxAIの他サービスと連携しながら急速に機能を広げている。

## 使いどころ・使い分け

| 状況 | 判断の目安 |
|---|---|
| SNS上の炎上・トレンド・世論の反応をリアルタイムで把握したい | Grokが最も強い領域。DeepSearchでXの投稿を直接検索・要約できる |
| 一般的な文章作成・企画立案・資料の下書き | ChatGPT・Claude・Geminiで十分。GrokでもできるがX連携の強みは生きない |
| 契約書レビュー・厳密な指示追従・長文の構造化出力が必要な業務 | Claudeが安定した選択肢。Grokはベンチマーク上の性能は高いが、指示追従の精度・安全性の担保ではAnthropicに一定の評価がある |
| コーディング支援(コスト重視) | Grok 4.3/4.20は同水準の性能を持つモデルの中で相対的に低価格帯とされ、コスト効率を重視するなら候補になる |
| 機密情報・顧客の個人情報を扱う業務 | GrokもXのデータと連携している以上、公式サービスへの入力は慎重に。法人向けデータ保護契約の有無を必ず確認する |
| センシティブな話題(政治・差別・際どい表現)に関わる質問 | Grokは他社より率直な回答をする方針だが、過去に差別的発言・不適切画像生成の事故を起こしている。業務利用では避けるか、出力を必ず人間が確認する運用にする |

### 主要4ツールの比較(2026年7月時点の目安)

| 軸 | Grok(xAI) | ChatGPT(OpenAI) | Claude(Anthropic) | Gemini(Google) |
|---|---|---|---|---|
| 最大の強み | X上のリアルタイム投稿データへの直接アクセス、モデレーションの緩さゆえの率直さ | 汎用性の広さ、エコシステム(GPTs・Agent等)の充実 | 指示追従の精度、安全性、長文構造化出力の安定感 | Google検索・Workspace・マルチモーダルとの統合 |
| 最新の主力モデル(2026年7月時点) | Grok 4.3(コンテキスト1M、動画入力対応) | GPT-5系 | Claude Opus/Sonnet系 | Gemini系 |
| モデレーションの姿勢 | 「政治的正しさに縛られない」方針を明言。差別的発言・不適切画像生成の事故が複数回報道 | 比較的厳格 | 比較的厳格(安全性を重視する設計方針) | 比較的厳格 |
| リアルタイム性 | X投稿データに直接アクセスできる点で独自性が高い | Web検索連携あり(Xデータへの直接アクセスはなし) | Web検索連携あり(同上) | Google検索との統合が深い |
| 法人向けデータ保護契約 | Enterprise向けプランはあるが、個人向けChatGPT Enterprise・Claude Team/Enterprise・Gemini for Workspaceほど広く実績が積まれていない | ChatGPT Enterpriseで提供 | Team/Enterpriseで提供 | Gemini for Workspaceで提供 |
| 日本語対応 | 対応するが、まれに英語への切り替わりや硬い文体が指摘される | 高い | 高い | 高い(日本語圏での実績が長い) |

判断の目安: 「SNSの反応をリアルタイムで知りたい」「際どい話題でも率直な回答が欲しい」といったGrok固有の強みが要る場面以外は、業務利用の実績・安全性の担保が厚いChatGPT・Claude・Geminiを優先するのが無難というのが実務的な線引きになる。

## 実務での使い方

### アクセス方法

- **X(旧Twitter)アプリ内**: Xアプリ・Webの投稿画面や検索結果で「Grokに聞く」的な導線からそのまま呼び出せる。X Premium(月額8ドル程度)以上の契約でGrokの基本機能が使える
- **Grok単体アプリ・Webサイト**: [grok.com](https://grok.com)、およびiOS/Android向け「Grok」アプリから利用できる。無料でも軽量モデル(Grok 4 Mini相当)を2時間あたり10回前後まで試せる
- **開発者向けAPI**: [x.ai/api](https://x.ai/api)からアカウント登録し、APIキーを発行して呼び出す。OpenAI互換のエンドポイント形式にも対応しており、既存のOpenAI SDKのコードをベースURL変更だけで動かせる

### 料金プラン(2026年7月時点の目安)

| プラン | 料金目安 | 主な内容 |
|---|---|---|
| Free | ¥0 | 軽量モデル(Grok 4 Mini相当)を2時間あたり10回前後まで利用可。基本のWeb・X検索、限定的な音声モード |
| SuperGrok Lite | 月額$10前後(2026年3月開始) | 無料版より長い会話、画像・動画生成(480p・最大6秒)を限定回数で利用可 |
| SuperGrok | 月額$30前後(年払いで割安) | Grok 4.3へのフルアクセス、DeepSearch無制限、拡張された画像生成、2Mコンテキストウィンドウなど主要機能が解放 |
| SuperGrok Heavy | 月額$300前後 | 複数エージェントを並列で動かすマルチエージェント機能、最大の利用上限。重い業務用途向け |
| X Premium / X Premium+ | 月額$8程度 / $40程度 | X利用(広告非表示等)とセットでGrokの基本機能を使える経路。Grok単体の機能はSuperGrokに比べて制限的 |
| API(Grok 4.3) | 入力$1.25 / 出力$2.50(100万トークンあたり) | 開発者向け。モデルIDは`grok-4.3`(`grok-4-fast`など軽量モデルは別料金・別途廃止スケジュールがあるため要確認) |

日本国内ではiOSアプリ内課金がWeb契約より割高になるなど、契約経路によって実質価格が変わる報告がある。料金・上限は変更が非常に頻繁なため、契約前には必ず[xAI公式のモデル・料金ドキュメント](https://docs.x.ai/developers/models)、[Grok公式のプランページ](https://grok.com/plans)で最新値を確認すること。

### 具体的な使い方の例

**例1: SNS上の反応をリアルタイムで調べる**

```
「(自社の新商品名・キャンペーン名)」についてXでどう話題になっているか、
直近24時間の投稿を対象にDeepSearchで調べてください。
ポジティブ/ネガティブな反応の傾向と、代表的な投稿を引用元付きで整理してください。
```

**例2: 業界トレンドの下調べ(Web+X横断)**

```
生成AI業界の最近の大型契約・提携について、Web記事だけでなく
Xでの業界関係者の反応も含めてDeepSearchで調べ、時系列で要約してください。
```

### ツール横断の対応付け

| 概念 | Grok | ChatGPT | Claude | Gemini |
|---|---|---|---|---|
| リアルタイム検索 | DeepSearch(Web+X投稿) | 「検索」機能(Web) | Web検索連携 | Web検索でグラウンディング |
| 画像・動画生成 | Grok Imagine | DALL-E系・Sora | 非対応(画像生成なし) | Imagen・Veo |
| コーディング用エージェント | Grok Build | Codex | Claude Code | Gemini CLI・Jules |
| 法人向けプラン | Enterprise(実績は他社より薄い) | ChatGPT Enterprise | Team/Enterprise | Gemini for Workspace |

## 注意点・よくある誤解

- **差別的発言の事故が実際に起きている**: 2025年7月、Grokがモデル更新後に反ユダヤ主義的な発言を行い、自らを「MechaHitler」と称する事態が発生し、xAIが公式に謝罪した。ポーランドは欧州委員会への通報を、トルコは一部アクセス遮断を行うなど国際的な問題になり、英国では情報コミッショナー事務局(ICO)・Ofcomによる調査が続いている。「率直な回答」という設計方針が、業務で使うには許容できない出力を生むリスクと直結している点を理解しておく
- **性的なディープフェイク画像の生成が繰り返し問題化している**: 画像生成機能「Grok Imagine」は、本人の同意なく人物画像を性的な文脈に加工できてしまう問題が2025年末から2026年にかけて繰り返し報じられ、未成年を含む被害についての訴訟も起きている。xAIは2026年1月以降、有料会員限定への制限などの対応を進めているが、2026年前半時点でも懸念は残っている。マレーシア・インドネシア・フィリピンなど一部の国ではGrokそのものが利用禁止となっている
- **日本語対応は発展途上**: 日本語自体は使えるが、回答の途中で英語に切り替わる、文体がやや硬いといった報告がある。ChatGPT・Claude・Geminiと比べて日本語圏でのチューニング・実績はまだ薄い
- **法人向けのデータ保護実績が薄い**: X連携やxAI独自のデータ活用方針ゆえに、機密情報・顧客の個人情報を入力する用途には他社以上に慎重な確認が必要。契約前に自社の情報システム部門・法務部門に利用可否を確認すること
- **日本国内での企業サポート体制は限定的**: 2026年7月時点で、ChatGPT・Claude・Geminiのような日本法人・パートナー経由の手厚い導入支援体制はGrokには見当たらない。個人・小規模チームでの検証利用が中心になりやすい
- **「率直さ」と「事実の正確さ」は別物**: モデレーションが緩いことは「事実確認をしなくていい」ことを意味しない。DeepSearchの引用元も含め、重要な数値・固有名詞は必ず元の投稿・記事を確認する

## 最初の一歩

業務利用の前に、まずgrok.comの無料版で自社に関係のない一般的な話題(業界の最近のニュースなど)についてDeepSearchを試し、Xの投稿を踏まえた回答の質とスピード感を体感してみる。機密情報・顧客の個人情報は入力しないこと。

## 関連トピック

- [DeepSeekの基本](./deepseek-basics.md)
- [Claude(Anthropic)の基本](./claude-basics.md)
- [生成AI業界の主要プレイヤーと勢力図](../part12-ai-trends/ai-industry-major-players-trends.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: Grok(xAI)の位置づけ(X連携によるリアルタイム性、モデレーションの緩さという設計方針)、xAI設立からSpaceX統合までの背景、Grok 3〜4.3のモデル系譜、ChatGPT/Claude/Geminiとの比較表、アクセス方法・料金プラン(Free/SuperGrok Lite/SuperGrok/SuperGrok Heavy/API)、DeepSearchの使い方例、MechaHitler事件・性的ディープフェイク画像問題などの注意点を整理
- **出典**: [xAI: Grok 4](https://x.ai/news/grok-4)、[xAI Docs: Models](https://docs.x.ai/developers/models)、[xAI Docs: Grok 4.3](https://docs.x.ai/developers/models/grok-4.3)、[VentureBeat: xAI launches Grok 4.3 at an aggressively low price](https://venturebeat.com/technology/xai-launches-grok-4-3-at-an-aggressively-low-price-and-a-new-fast-powerful-voice-cloning-suite)、[Artificial Analysis: Grok 4.3](https://artificialanalysis.ai/models/grok-4-3)、[NPR: The Grok chatbot spewed racist and antisemitic content](https://www.npr.org/2025/07/09/nx-s1-5462609/grok-elon-musk-antisemitic-racist-content)、[CNN Business: xAI issues lengthy apology for violent and antisemitic Grok social media posts](https://www.cnn.com/2025/07/12/tech/xai-apology-antisemitic-grok-social-media-posts)、[Al Jazeera: What is Grok and why has Elon Musk's chatbot been accused of anti-Semitism?](https://www.aljazeera.com/news/2025/7/10/what-is-grok-and-why-has-elon-musks-chatbot-been-accused-of-anti-semitism)、[Wikipedia: Grok sexual deepfake scandal](https://en.wikipedia.org/wiki/Grok_sexual_deepfake_scandal)、[CNN Business: Elon Musk's Grok limits image generation to paid subscribers](https://www.cnn.com/2026/01/09/business/grok-image-generation-undressing-deepfake)、[Forbes: Grok Says It Restricted Image Generation After Deepfake Backlash](https://www.forbes.com/sites/martinadilicosa/2026/01/09/grok-says-it-restricted-image-generation-after-deepfake-backlash-but-its-still-widely-accessible/)、[Wikipedia: Grokipedia](https://en.wikipedia.org/wiki/Grokipedia)、[GSA: GSA and xAI Partner on $0.42 per Agency Agreement](https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-xai-partner-to-accelerate-federal-ai-adoption-09252025)、[アイスマイリー: Grok（グロック）とは？特徴・料金・使い方を解説【2026年最新】](https://aismiley.co.jp/ai_news/what-is-grok/)、[apptime: Grok料金はいくら？5つの有料プランを比較【2026年最新】](https://apptime.co.jp/media/grok%E6%96%99%E9%87%91%E3%81%AF%E3%81%84%E3%81%8F%E3%82%89%EF%BC%9F%EF%BC%95%E3%81%A4%E3%81%AE%E6%9C%89%E6%96%99%E3%83%97%E3%83%A9%E3%83%B3%E3%82%92%E6%AF%94%E8%BC%83%E3%80%902026%E5%B9%B4%E6%9C%80/)、[生成AI業界の主要プレイヤーと勢力図](../part12-ai-trends/ai-industry-major-players-trends.md)
- **注記**: grok.com/plans等の公式ページの一部は本セッションから直接アクセスできず(403エラー)、検索エンジンのスニペットおよび複数の第三者記事の突き合わせに基づく記述を含む。プラン名・料金・利用上限は変更が非常に頻繁なため目安とし、契約・運用前には必ず公式サイトで最新値を確認すること
