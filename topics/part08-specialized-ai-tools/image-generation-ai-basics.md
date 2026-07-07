---
title: 画像生成AIの基本(Midjourney・Stable Diffusion・GPT Image/DALL-E 3などの選び方)
part: 8
chapter: 第3章 画像・動画・音声の生成AI
tags: [画像生成AI, Midjourney, Stable Diffusion, DALL-E3, GPT Image, Nano Banana, Adobe Firefly, プロンプト]
created: 2026-07-06
updated: 2026-07-06
---

# 画像生成AIの基本(Midjourney・Stable Diffusion・GPT Image/DALL-E 3などの選び方)

## これは何か

バナー画像・資料の挿絵・SNS投稿画像を作るたびに、デザイナーに依頼したりストックフォトを探し回ったりしていると、ちょっとした画像1枚でも時間とコストがかかる。画像生成AI(テキストの指示から新しい画像を作り出す生成AI)を使えば、文章で指示するだけで数十秒〜数分でオリジナル画像の候補が何パターンも手に入る。

ただしツールごとに得意なテイスト・料金体系・商用利用のしやすさが大きく異なり、「とりあえずMidjourney」「とりあえずChatGPT」では業務用途に合わないことがある。本ページは、2026年7月時点で実務で使われている主要な画像生成AI(Midjourney、Stable Diffusion、ChatGPT〈GPT Image、旧DALL-E 3〉、Google Gemini〈Nano Banana〉、Adobe Firefly)を横並びで整理し、業務での選び方とコピペで使えるプロンプト例をまとめる。著作権・法務面の詳しい注意点は[生成AIの著作権リスクと実務での注意点](../part04-risk-security/copyright-risks-in-generative-ai.md)に譲り、本ページはツールの選び方と実務での使い方に絞る。

## 仕組み・背景

現在の画像生成AIは、大きく2つの仕組みに分かれる。

- **拡散モデル(diffusion model)**: ランダムなノイズ画像から出発し、テキストの指示に沿って少しずつノイズを取り除いていくことで画像を作り上げる方式。Midjourney、Stable Diffusion、Adobe Fireflyの基盤モデルはこの方式で、写実的な質感や独特の画風を出しやすい
- **自己回帰(autoregressive)型のマルチモーダルモデル**: 文章を生成するのと同じ仕組み(次の要素を予測して並べていく)で、画像も「トークン」の並びとして生成する方式。ChatGPTの画像生成(GPT Image)やGoogle Geminiの「Nano Banana」系モデルはこちらに近く、対話の流れの中で「さっきの画像の背景だけ変えて」のような指示追従・部分編集に強く、画像内の文字も比較的正確に描ける

2023年頃まではDALL-E 3(拡散モデル、ChatGPTからAPI経由で呼び出される別モデルという位置づけ)が主流だったが、OpenAIは2025年にChatGPTへ画像生成を直接統合した新モデル(GPT Image)に切り替えており、DALL-E 3はAPIとして2026年5月12日にサポートが終了している。「DALL-E 3を使う」という表現は、2026年7月時点では実質的に「ChatGPTの画像生成(GPT Image)を使う」と読み替えてよい。同様にGoogleも「Nano Banana」というブランド名でGeminiの画像生成モデルを頻繁に更新しており(Nano Banana Pro、Nano Banana 2、Nano Banana 2 Liteなど)、ツール名とモデル名の対応は流動的である点を前提に、契約・比較のたびに現行モデル名を確認する必要がある。

## 使いどころ・使い分け

| ツール | 提供元・利用方法 | 強み | 弱み・注意点 | 向いている業務用途 |
|---|---|---|---|---|
| Midjourney(V7) | midjourney.com(Web版)/Discord | 芸術性・質感の美しさに定評があり、独特の作風を出しやすい。パラメータで細かく画風を制御できる | チャット的な対話編集や正確な文字入れは弱い。無料プランがなくサブスク必須 | コンセプトアート、SNSで映える画像、資料の世界観づくりのビジュアル |
| Stable Diffusion(SD3.5/SDXL系、オープンウェイト) | ローカルPC(ComfyUI等)/Stability AI API/DreamStudio | ローカル実行なら無料、追加学習(ファインチューニング)や大量生成の自動化が可能。企業データを外部に出さずに運用できる | 環境構築にある程度の技術知識が必要。商用利用は年間売上等の条件で有償ライセンスが必要になる場合がある | 同じキャラクター・ブランド画像の量産、社内システムへの組み込み、社外に出せない要件がある生成 |
| ChatGPT(GPT Image、旧DALL-E 3) | ChatGPT内でプロンプトを入力するだけ | 対話しながら「ここだけ直して」と部分修正できる。画像内の文字(英語)の描画精度が高い。ChatGPTの他機能(文章作成・資料作成)とシームレスに使える | 1枚あたりの画風の作り込みはMidjourneyに劣る場合がある。無料枠は少ない | 資料の挿絵、文章作成の延長で作る簡易バナー、アイキャッチ画像 |
| Google Gemini(Nano Banana系モデル) | Geminiアプリ/API | 生成速度が速くコストが低い。複数の画像を合成したり、同一人物・キャラクターの一貫性を保った編集がしやすい | 画風の個性はMidjourneyほど強くない | SNS投稿画像・バナーの量産、既存の写真・ロゴを使った合成・加工 |
| Adobe Firefly | firefly.adobe.com/Photoshop等のCreative Cloud統合 | 学習データがAdobe Stockのライセンス済み素材・パブリックドメイン中心で、商用利用時の権利侵害リスクを比較的抑えやすい。企業向けには著作権侵害の補償(indemnification)も提供 | 画風の幅・生成の自由度は他ツールに比べて控えめな評価もある | 広告のメインビジュアル、パッケージなど権利リスクを避けたい商用利用、Photoshopでの仕上げ作業前提の素材 |
| (参考)Canva Magic Media等の簡易ツール | Canva等のデザインツール内 | デザインテンプレートと一体化しており、非デザイナーでもレイアウトまで含めて仕上げやすい | 画像生成そのものの精度・柔軟性は専業ツールに劣る | 社内向けの簡易バナー、テンプレートに沿ったSNS画像を素早く仕上げたい場合 |

判断の目安は次の3つ。

1. **画風の個性を優先するか、業務への組み込みやすさを優先するか**: 「作品としての完成度」を求めるならMidjourney、「対話しながら手早く」ならChatGPT・Gemini
2. **商用利用時の権利リスクをどこまで気にするか**: 広告のメインビジュアルなど露出・収益規模が大きい用途ほど、Adobe Fireflyのような学習データの出自が明確なツールや、契約に補償(indemnification)が付くツールを優先する(詳細は[生成AIの著作権リスクと実務での注意点](../part04-risk-security/copyright-risks-in-generative-ai.md))
3. **量産・自動化が必要か**: 同じキャラクターやフォーマットの画像を大量に作る、社内システムに組み込みたい場合はStable Diffusion(API・ローカル)が向く。単発利用ならサブスク型のMidjourney・ChatGPT・Geminiで十分

## 実務での使い方

### 想定シーン

- 社内資料・提案書に貼る挿絵・アイコン的な画像を、ストックフォトを探す代わりに作る
- Webサイト・広告・メールマガジンのバナー画像を複数パターン試作する
- SNS(X、Instagram等)投稿用の画像を、決まったフォーマット(正方形・縦長など)で量産する
- ブログ記事のアイキャッチ画像を作る

### 基本の操作手順(画面の場所)

- **ChatGPT**: chatgpt.com にログイン → チャット入力欄に「〇〇の画像を作って」と直接入力(画像生成専用のボタンは不要で、依頼内容から自動判定される)→ 生成後は「この部分を〇〇に変えて」と続けて指示すれば部分修正できる
- **Google Gemini**: gemini.google.com にログイン → 入力欄に画像生成の指示を入力(またはツール選択欄で「画像を作成」を選ぶ)→ 既存の画像をアップロードして「この写真の背景を変えて」のように編集を指示することも可能
- **Midjourney**: midjourney.com のWeb版にログイン(2026年時点でDiscordを使わずWeb上で生成・管理が可能)→ プロンプト入力バーに指示文とパラメータ(後述)を入力 → 生成された4枚の中から気に入った1枚を拡大(Upscale)・部分編集(Vary Region)する
- **Adobe Firefly**: firefly.adobe.com にログイン(Adobe IDが必要)→「テキストから画像生成」を選び、プロンプトを入力 → アスペクト比・スタイル(写real / イラスト等)をUIのプルダウンから指定して生成
- **Stable Diffusion**: 技術的知識がない場合はDreamStudio(dreamstudio.ai)などのWeb版から、社内で運用したい場合はComfyUIやAUTOMATIC1111などのローカル環境、またはStability AIのAPIを利用する

### コピペで使えるプロンプト例(Webバナー・アイキャッチ)

```
16:9の横長のWebバナー画像を作ってください。
テーマ:「夏の会員限定セール」
雰囲気:明るく爽やかな配色(青と白を基調)、写実的なビーチの背景
構成:画面の左3分の1程度に余白を残し、そこにテキストを後から入れられるようにしてください
画像内に文字は入れないでください(テキストは後で別途配置します)
```

(画像内に文字を正確に描かせるのは現状どのツールでも精度が不安定なため、文字は画像編集ソフトやスライドソフト側で別途重ねる運用が安全)

### コピペで使えるプロンプト例(資料の挿絵)

```
ビジネス資料に使う挿絵を作ってください。
テーマ:「チームでのブレインストーミング」
スタイル:フラットデザインのイラスト、線が細く、彩度を抑えた配色(会社のコーポレートカラーは紺色と黄色)
背景は透明または単色の無地にしてください
写実的な人物ではなく、シンプルな線画のキャラクターにしてください
```

### コピペで使えるプロンプト例(Midjourney、パラメータ付き)

```
minimalist flat illustration of a team brainstorming around a whiteboard,
soft navy and yellow color palette, clean lines, no text --ar 16:9 --stylize 150 --v 7
```

Midjourneyでよく使うパラメータ:

| パラメータ | 役割 |
|---|---|
| `--ar 16:9` / `--ar 1:1` / `--ar 9:16` | アスペクト比(横長・正方形・縦長)を指定。用途に応じて選ぶ(バナーは16:9、SNS投稿は1:1、ストーリーズは9:16が目安) |
| `--stylize`(0〜1000、デフォルト100) | 数値が高いほどAIが独自の芸術表現を強く加える。プロンプトに忠実にしたい場合は低め(50前後)、作品性を出したい場合は高め(500以上)にする |
| `--v 7` | 使用するモデルのバージョン指定(2026年7月時点の最新はV7系) |

### ツール横断の対応付け

| やりたいこと | Midjourney | ChatGPT | Google Gemini | Adobe Firefly |
|---|---|---|---|---|
| アスペクト比の指定 | `--ar 16:9`等のパラメータ | 自然文で「16:9で」と指示 | 自然文または画面上の比率選択 | 生成前にUIでサイズを選択 |
| 部分的な修正・編集 | Vary Region(範囲指定して再生成) | 続けて会話で「〇〇を変えて」と指示 | 会話または画像アップロードで指示 | Generative Fill(範囲指定して生成) |
| 商用利用の可否 | 有料プラン加入者は可(規約の範囲内) | Plus以上で可(規約の範囲内) | 有料プランで可(規約の範囲内) | 標準で商用利用可、企業向けには著作権侵害の補償あり |

### 料金プラン(2026年7月時点の目安)

| ツール | プラン | 料金 | 内容の目安 |
|---|---|---|---|
| Midjourney | Basic | 月額$10(年払い相当$8) | Fast GPU時間 3.3時間/月 |
| Midjourney | Standard | 月額$30(年払い相当$24) | Fast GPU時間15時間/月、Relaxモード(低速だが無制限)利用可 |
| Midjourney | Pro | 月額$60(年払い相当$48) | Fast GPU時間30時間/月、Stealthモード(非公開生成)利用可 |
| Midjourney | Mega | 月額$120(年払い相当$96) | Fast GPU時間60時間/月、同時生成数が最大 |
| ChatGPT | Free | ¥0 | 画像生成は1日あたり数枚程度に制限 |
| ChatGPT | Plus | 月額$20 | 3時間あたり目安50枚程度まで生成可能 |
| ChatGPT API(GPT Image) | 従量課金 | 1024×1024で1枚あたり約$0.01〜$0.17(画質設定による) | 自社システムへの組み込み向け |
| Google Gemini | Free | ¥0 | Nano Banana系モデルを回数制限付きで利用可 |
| Google AI Pro | 月額$19.99 | Gemini上位モデル・画像生成の利用上限が拡大 |
| Google AI Ultra | 月額$99.99〜$199.99 | さらに高い利用上限、開発者向け機能を含む上位プラン |
| Adobe Firefly | Standard | 月額$9.99 | 生成クレジット2,000/月 |
| Adobe Firefly | Pro | 月額$19.99 | 生成クレジット4,000/月 |
| Adobe Firefly | Premium | 月額$199.99 | 生成クレジット50,000/月 |
| Stable Diffusion | ローカル実行 | 無料 | 商用利用は年間売上等の条件でライセンスが必要になる場合がある |
| Stability AI API | 従量課金 | 1枚あたり約$0.01〜$0.06(モデル・解像度による) | 自社システムへの組み込み向け |

料金・利用上限・モデル名は改定頻度が非常に高いため、契約前には必ず各社公式サイトの最新情報を確認すること。

## 注意点・よくある誤解

- **画像内の文字は依然不安定**: GPT Imageなど文字描画が改善したモデルもあるが、日本語の看板・ロゴ的な文字表現は崩れやすい。重要な文字情報は画像生成後に画像編集ソフト・スライドソフト側で別途配置する方が安全
- **手指・小物・背景の不整合(アーティファクト)は完全には無くなっていない**: 一目で見落としやすい破綻(手の指の数、透明なグラスの中の物体など)が残ることがあるため、対外公開前には人の目で必ず確認する
- **著作権・商標・肖像権の問題は別ページで整理している**: 実在の作家・作品・キャラクター・著名人に似せた生成は侵害リスクが高い。用途別のリスクの目安や公開前チェックリストは[生成AIの著作権リスクと実務での注意点](../part04-risk-security/copyright-risks-in-generative-ai.md)を参照
- **モデル名・ツール名の変遷が速い**: DALL-E 3は2026年5月にAPIサポートが終了しGPT Imageに置き換わっており、Google側も「Nano Banana」ブランドの中でモデルが頻繁に更新される。社内マニュアルやプロンプト集に古いモデル名を書いたままにしないよう、半年〜1年に一度は見直す
- **無料プラン・低価格プランは商用利用不可の場合がある**: 例えばStable Diffusionのコミュニティライセンスは、年間売上が一定額(目安1億円強)を超える企業には別途有償ライセンスが必要になる。契約前に利用規約の商用利用条件を確認する
- **ブランド・ロゴの一貫性を保つのは苦手**: 同じキャラクター・ロゴを毎回まったく同一に再現するのは、一貫性維持を強化した最新モデルでも完全ではない。ブランド素材として繰り返し使う画像は、1枚を人の手で仕上げてテンプレート化する方が安定する
- **Web用途と印刷用途で必要な解像度が違う**: 生成AIの標準出力はWeb表示を想定した解像度が中心のため、大判ポスターなど印刷用途にはアップスケール(高解像度化)処理が別途必要になることが多い

## 最初の一歩

今日中に使う予定のある画像(資料の挿絵やSNS投稿用画像など)を1つ選び、手元で使っているChatGPTまたはGeminiの既存プランでプロンプトを1つ試してみる。生成後は、契約しているプランの利用規約で「商用利用の可否」を確認する。

## 関連トピック

- [生成AIの著作権リスクと実務での注意点](../part04-risk-security/copyright-risks-in-generative-ai.md)
- [生成AIによるプレゼン資料・ドキュメント作成の実務活用](../part11-business-practice/ai-presentation-and-document-creation.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: Midjourney・Stable Diffusion・ChatGPT(GPT Image、旧DALL-E 3)・Google Gemini(Nano Banana系)・Adobe Fireflyを横並びで比較し、拡散モデル/自己回帰型モデルという仕組みの違い、DALL-E 3のAPIサポート終了(2026年5月)とGPT Imageへの移行、業務用途別の選び方、画面の場所まで書いた操作手順、バナー・挿絵・Midjourneyパラメータのプロンプト例、ツール横断の対応表、2026年7月時点の料金プラン比較、画像生成AI特有の注意点(文字描画・アーティファクト・ブランド一貫性・解像度)を整理した
- **出典**: [Midjourney pricing in 2026: Plans, GPU hours, and what it actually costs | eesel AI](https://www.eesel.ai/blog/midjourney-pricing)、[Comparing Midjourney Plans | Midjourney](https://docs.midjourney.com/hc/en-us/articles/27870484040333-Comparing-Midjourney-Plans)、[Midjourney V7の使い方と料金｜月$10から始める設定とプロンプトのコツ](https://aipicks.jp/mag/midjourney-complete-guide-2026)、[Stability AI - Developer Platform Pricing](https://platform.stability.ai/pricing)、[Stable Diffusion in 2026: Features, Pricing, License, and Alternatives | Merlio](https://merlio.app/blog/stable-diffusion-features-pricing-license-and-alternatives)、[ChatGPT Plus for AI Image Generation in 2026: Pricing, Limits, and What You Actually Get | AVB](https://aivideobootcamp.com/blog/chatgpt-plus-image-generation-complete-guide-2026/)、[AI Image Pricing 2026: Google Gemini vs. OpenAI GPT Cost Analysis | IntuitionLabs](https://intuitionlabs.ai/articles/ai-image-generation-pricing-google-openai)、[DALL·E 3 Model | OpenAI API Developer Docs](https://developers.openai.com/api/docs/models/dall-e-3)、[Google Launches Nano Banana 2 Lite for Low-Cost, High-Throughput AI Image Generation | gHacks](https://www.ghacks.net/2026/07/02/google-launches-nano-banana-2-lite-for-low-cost-high-throughput-ai-image-generation/)、[Google Imagen 4 & Nano Banana Pricing 2026 | Rogue Marketing](https://the-rogue-marketing.github.io/google-nano-banana-imagen-4-image-generation-pricing-may-2026/)、[Everything new in our Google AI subscriptions, fresh from I/O 2026 | Google Blog](https://blog.google/products-and-platforms/products/google-one/google-ai-subscriptions/)、[The Google AI Ultra plan now starts at $100 a month | Engadget](https://www.engadget.com/2176060/the-google-ai-ultra-plan-now-starts-at-100-a-month/)、[Adobe Firefly Pricing 2026: Plans from $9.99 to $199.99/mo | costbench](https://costbench.com/software/ai-image-generators/adobe-firefly/)、[Midjourneyプロンプト完全ガイド｜基本の書き方・カテゴリ別実例集](https://genai-ai.co.jp/ai-kanri/blog/cc-midjourney-prompts-guide/)
- **注記**: 各社公式サイトの一部ページには本セッションから直接アクセスできず、検索エンジンのスニペットおよび複数の第三者記事の突き合わせに基づく記述を含む。料金・モデル名・利用上限は変更が非常に頻繁なため目安とし、契約・運用前には必ず公式サイトで最新値を確認すること
