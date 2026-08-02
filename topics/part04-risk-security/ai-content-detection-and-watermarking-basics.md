---
title: "AI生成コンテンツの検出・電子透かし(C2PA・SynthIDなど)の基本"
part: 4
chapter: 第4章 法務・ガバナンス
tags: [C2PA, SynthID, 電子透かし, ディープフェイク, コンテンツ真正性, EU AI Act]
created: 2026-07-07
updated: 2026-08-02
---

# AI生成コンテンツの検出・電子透かし(C2PA・SynthIDなど)の基本

## これは何か

取引先から届いた画像や文章、採用選考のエッセイ、問い合わせフォームの文章が「生成AIで作られたものかどうか」を判断しなければならない場面が増えている。しかし「AI検出ツールにかければ白黒はっきりする」という期待は、現時点の技術水準では危険な誤解になりやすい。この分野の技術は大きく2系統に分かれる。1つは、画像・動画・文章を生成した時点で出所情報を埋め込んでおく**電子透かし・来歴(provenance、コンテンツがいつ・どこで・どう作られたかの記録)情報の付与方式**(C2PA/Content Credentials、Google DeepMindのSynthIDなど)。もう1つは、出所情報がない完成品を後から統計的な特徴で判定する**事後的なAI検出ツール**(文章・画像の判定サービス)。本ページはこの2系統の違いと、それぞれの実務での使いどころ・限界を整理する。加えて、2026年8月2日にEU AI Act(EU AI法)の透明性義務(第50条)が施行され、AI生成コンテンツの表示が一部企業にとって法的義務になった点も本ページで扱う。生成AI自体の規制動向は[生成AIの規制・ガバナンス動向](./ai-regulation-and-governance-trends.md)、著作権面の論点は[生成AIの著作権リスクと実務での注意点](./copyright-risks-in-generative-ai.md)を参照。

## 仕組み・背景

### 系統1: 生成時に出所情報を埋め込む方式(C2PA・SynthID)

**C2PA(Coalition for Content Provenance and Authenticity)**は、Adobe・Microsoft・Google・OpenAI・BBCなど主要企業が参加する標準化団体で、2026年1月時点で会員・関連団体は6,000を超え、画像・動画・文章の真正性確認における事実上の世界標準になりつつある。その技術仕様に基づき付与される来歴情報を**Content Credentials**と呼ぶ。仕組みは「デジタルの成分表示」に近い。ファイルに「いつ・どのツールで生成したか」「どんな編集を経たか」という記録(マニフェスト)を暗号署名付きメタデータとしてJUMBF(JPEG Universal Metadata Box Format)というコンテナ形式で埋め込み、コンテンツ本体のハッシュ値(SHA-256)も一緒に記録する。ピクセル単位で1つでも改変が加わるとハッシュが一致しなくなり、改ざんが検出できる仕組みになっている。カメラでの撮影時点(Leica M11・Q3・SL3、Sony Alpha 1 II・Alpha 9 III、Nikon Z8・Z9〈ファームウェア対応〉、Canon EOS R1・R5 Mark II、Samsung Galaxy S26シリーズなど)、生成AIでの作成時点(Adobe Firefly、ChatGPT画像生成など)、編集ソフト(Photoshop、Premiere Proなど)のそれぞれで署名が積み重なり、撮影から公開までの「編集履歴の連鎖」を後から検証できる。2025年12月公開のC2PA 2.3ではライブ配信への対応(CMAFセグメント単位での署名)も加わったが、後述のとおりプラットフォームを経由する過程でメタデータが失われる問題は解決していない。

**SynthID**はGoogle DeepMindが開発した電子透かし技術で、C2PAとはアプローチが異なる。メタデータとして付帯情報を「添付」するのではなく、画像・動画・音声のピクセルや音声波形、文章の単語選択確率そのものに、人間には知覚できないレベルの微細な統計的パターンを「埋め込む」方式。これにより、メタデータが失われがちなスクリーンショットや軽い圧縮・トリミングを経ても痕跡が残りやすいという特性がある(ただし完全ではない)。専用の検出器(SynthID Detector)でスキャンすると、透かしが「ある/ない/判定不能」のいずれかを示す。

両者は競合ではなく補完関係にあり、併用が主流になりつつある。OpenAIは2026年5月19日、ChatGPT・Codex・OpenAI APIで生成する画像についてC2PA準拠(Content Credentialsの付与)とSynthID透かしの両方を組み込む方針を発表し、同年7月31日にはOpenAIツールで生成する音声にもSynthID透かしの対応を広げた。NVIDIAも2026年1月、動画生成基盤モデルCosmosの出力にSynthIDを統合している。

### 系統2: 完成品を後から判定する事後検出ツール

出所情報が最初から付いていない(埋め込みに対応していないツールで作られた、あるいは意図的に加工で剥がされた)コンテンツについては、後から統計的特徴でAI生成らしさを推定するしかない。文章検出ツール(GPTZero、Turnitin、Originality.aiなど)は、単語の予測しやすさ(困惑度・パープレキシティ)や文の均一性など、人間の文章とAI生成文章の統計的な傾向差を手がかりにスコアを出す。画像検出ツール(Hive Moderationなど)は、生成モデル特有のピクセルパターン・ノイズの癖を学習した分類モデルで判定する。いずれも「証拠」ではなく「確率的な推定」に過ぎない点が、電子透かし・来歴方式との決定的な違いになる。

## 使いどころ・使い分け

どちらの系統を使うべきかは、「自分が生成する側か、他人が作ったものを判定する側か」「証明したいのは何か」で変わる。

| 状況 | 適した手段 | 理由 |
|---|---|---|
| 自社が作った画像・動画・文章の真正性を対外的に証明したい | C2PA(Content Credentials)の付与 | 生成時点から来歴を記録でき、検証可能な形で「本物」を示せる。事後検出より確実 |
| 取引先から届いた画像がAI生成か確認したい | まずContent Credentialsの有無を確認、次にSynthID Detector等の透かし検出 | 来歴情報や透かしがあれば高い確度で判定できる。何もなければ「未検出」であり「人間が作った証拠」にはならない点に注意 |
| 社内レポート・メールが「AIで書かれたものか」を検出ツールで判定したい | 原則として避ける、または参考情報にとどめる | 文章検出ツールは誤判定(特に人間の文章をAI生成と誤る偽陽性)が構造的に避けられない問題であり、懲戒・評価などの根拠にするのは危険 |
| 採用選考のエッセイがAI生成かどうかを判定したい | 検出ツールの結果を単独の合否基準にしない。面談・口頭試問等の代替手段と併用する | 検出ツールのスコアだけを理由に不合格にすると、実際は本人が書いた文章を誤って排除するリスクがある |
| ニュース素材・報道写真の出所を確認したい | C2PAのContent Credentials確認を優先 | BBC、CBC、NYT、WSJ、ロイター、AFP、NHK、AP、ワシントン・ポストなど主要報道機関がC2PA署名付きの配信を進めており、業界標準になりつつある |
| ディープフェイク動画・音声の疑いがある場合 | 来歴情報の有無の確認+複数の検出ツールでのクロスチェック、専門家への相談 | 単一ツールの判定に頼らず、複数の手がかりを組み合わせる。悪意ある偽情報は透かしを回避する目的で作られている可能性が高い |
| EU域内向けにチャットボット・AI生成コンテンツ・ディープフェイクを提供/利用している | 2026年8月2日以降、EU AI Act第50条の透明性義務(下記参照)への対応を最優先で確認 | 罰則(最大1,500万ユーロまたは全世界年間売上高の3%)を伴う法的義務であり、社内ガイドラインレベルの話ではない |

判断の軸はシンプルで、**「自分が生成する立場なら電子透かし・来歴情報を積極的に付与する」「他人の生成物を判定する立場なら、来歴情報の有無を最初に確認し、それがない場合の事後検出ツールの結果は"参考情報"以上の重みを持たせない」**という2点に集約される。加えて、EU向け事業がある場合は「表示するかどうか」がそもそも任意ではなくなった点を押さえておく。

## 実務での使い方

### Content Credentials(C2PA)の確認手順

1. 画像・動画のファイルを[Content Credentials Verify](https://contentcredentials.org/verify)のような検証サイトにアップロードする、またはAdobe製品・対応ブラウザ上で画像を右クリックして来歴情報を表示する
2. 「いつ・どのツール(例: Adobe Firefly、ChatGPT、Google Geminiなど)で生成されたか」「どんな編集が加えられたか」の来歴が表示されれば、その情報の信頼性(署名した組織が実在し、証明書が有効か)を確認する
3. 来歴情報が「ない」場合、それは「人間が作った証拠」ではない。対応していないツールで作られた、SNS等へのアップロード時にメタデータが失われた、意図的に除去された、のいずれの可能性もある

### SynthIDの確認手順(2026年8月時点)

Google DeepMindが提供する SynthID Detector は、画像・音声・動画・文章の断片をアップロードすると、SynthIDの透かしが「検出された/されなかった/判定不能」のいずれかと、該当箇所を示すポータル。2026年5月のGoogle I/Oで報道関係者・研究者向けの早期アクセスが開始されたが、2026年8月時点でも一般向けは順番待ちリスト経由のままで、全面公開には至っていない。GoogleはGemini、Google検索、ChromeなどGoogle製品側でもSynthID・C2PAの検証機能組み込みを進めている。OpenAI・Kakao・ElevenLabsなど他社もSynthIDの採用を表明済み。

### 主要ツールでの電子透かし・来歴表示対応(2026年8月時点の目安)

| ツール・企業 | 対応状況 |
|---|---|
| OpenAI(ChatGPT/Codex/API) | 2026年5月19日以降、ChatGPT・Codex・APIで生成する画像にC2PA Content CredentialsとSynthID透かしの両方を付与。同年7月31日から生成音声にもSynthIDを拡大。専用の検証ツール(アップロードでC2PA/SynthIDの有無を確認)を提供 |
| Google(Gemini/Veo/Imagen) | 画像・動画・音声・文章(Geminiアプリ)にSynthIDを埋め込み。Google検索・Chromeでの検証表示(右クリックでAIコンテンツかを確認)にも展開 |
| Adobe(Firefly/Photoshop/Premiere Pro) | Fireflyで生成した画像には既定でC2PA Content Credentialsを付与。Photoshop・Premiere Proは既存のContent Credentialsを保持・追記 |
| Microsoft(Copilot/M365) | 画像へのウォーターマーク付与(Copilotアイコンやテキスト表示)を2026年2月からユーザー制御で提供開始。動画・音声への視覚的/音声的ウォーターマーク付与ポリシーを2026年4月にクラウドポリシー経由で追加。無効化してもC2PA相当のメタデータは残る |
| Meta(Facebook/Instagram) | アップロード時にC2PA情報を読み取り「AI情報」ラベルを表示 |
| X(旧Twitter) | 2026年3月からPremiumユーザー向けにContent Credentials表示に対応 |
| 報道機関(BBC、CBC、NYT、WSJ、ロイター、AFP、NHK、AP、ARD/ZDF、ワシントン・ポスト等) | C2PA署名付きでの配信・取材素材の管理を拡大 |
| カメラメーカー(Leica、Sony、Nikon、Canon、Samsung) | 撮影時点でのC2PA署名に対応する機種が拡大。Apple・Google Pixel・富士フイルムは対応を表明済みだが2026年8月時点で未出荷 |

料金・対応範囲は各社とも変更頻度が高いため、対外的な信頼性担保に使う前には必ず各社の最新情報を確認すること。

### EU AI Act(第50条)の透明性義務(2026年8月2日施行)

EU域内でチャットボットやAI生成コンテンツ(画像・音声・動画・文章)、ディープフェイク生成システムを提供・運用する事業者には、2026年8月2日からEU AI Act第50条の透明性義務が直接適用される。日本企業でもEU向けにサービス提供している場合は対象になり得るため、以下を確認しておく必要がある。

- **チャットボット等との対話**: 利用者に「AIと対話している」ことを知らせる義務(欺く意図の有無を問わない)
- **AI生成コンテンツ**: 合成音声・画像・動画・文章について、機械可読な形式でのマーキングと、AI生成物であると検知可能な状態にする義務(既存システムへの機械可読マーキング義務のみ2026年12月2日まで猶予あり)
- **ディープフェイク**: 実在の人物・出来事に酷似したコンテンツは「人工的に生成・加工されたもの」である旨の開示が必要(欺く意図がなくても対象)
- **罰則**: 違反時は最大1,500万ユーロまたは全世界年間売上高の3%の制裁金

なお、日本国内では総務省・経済産業省の「AI事業者ガイドライン(第1.2版、2026年3月31日公表)」でも電子透かし等によるコンテンツの来歴表示は引き続き「推奨」にとどまり、2026年8月時点でAI生成である旨の表示自体を一律に義務付ける国内法はない。EU向け事業の有無で対応の緊急度が大きく変わる点に注意する。

### コピペで使えるチェック文面(取引先への確認依頼)

素材の真正性が重要な場面(広告素材、報道写真の引用、契約書に添付する証跡画像など)では、次のような一文を添えて先方に確認するとよい。

```
恐れ入りますが、ご提供いただいた画像/動画について、生成AIの利用有無および
Content Credentials(C2PA)などの来歴情報の有無をご教示いただけますでしょうか。
社内の真正性確認プロセスの一環として確認させていただいております。
```

## 注意点・よくある誤解

- **AI文章検出ツールの精度は実務で信頼できる水準にない**: 2026年の独立検証では、GPTZeroなどの検出ツールが公表する精度(99%程度)と実際の精度には大きな乖離があり、コンテンツの種類によって実測精度は62〜88%程度にとどまるとの報告がある。人間の文章を誤ってAI生成と判定する偽陽性も一定割合発生し、Stanfordの調査ではTOEFLエッセイ(非ネイティブ英語話者の文章)の61%が誤ってAI生成と判定されたとの報告もある。こうした偽陽性の構造的な問題を理由に、MIT・イェール・ジョージタウン・UCLA・ウォータールー大学など50を超える大学が検出ツールの利用を禁止・無効化・非推奨としている(2026年3月時点)。**検出結果を単独の証拠として懲戒・不合格・評価に使うのは避けるべき**
- **AI画像検出ツールも「いたちごっこ」の途上にある**: 既知の生成モデル(Midjourney、DALL-E、Stable Diffusionなど)に対しては高い検出率を示すツールでも、新しい生成モデルや、ノイズ付加・実写との合成といった検出回避を意図した加工に対しては精度が大きく落ちる。生成技術の進化に検出技術が追いつききれない構造は今後も続くと見ておく
- **「透かしがない=人間が作った証拠」ではない**: 電子透かし・来歴情報がないことは、単に「対応していないツールで作られた」「途中でメタデータが失われた」可能性を示すだけで、AI生成を否定する根拠にはならない。逆に「透かしがある=100%確実」でもなく、SynthID Detectorも判定不能というグレーな結果を返すことがある
- **メタデータ方式(C2PA)は「署名する」ことより「連鎖を維持する」ことの方が難しい**: 撮影・生成の時点で署名しても、メールクライアント、メッセージアプリ、多くのCMSはC2PAメタデータを保持せず、アップロード・トランスコード時に情報が失われる。スクリーンショット問題も未解決。C2PAは「証明」というより「来歴シグナル」と捉え、過信しないこと
- **社内の生成AI利用チェックに事後検出ツールを使うのは特にリスクが高い**: 社員が書いたレポート・メールを「AIっぽいから」という理由で問題視すると、実際は本人が書いた文章を誤って疑うことになりかねない。生成AI利用の是非は、検出ツールではなく利用ルール(いつ・どこまでAIを使ってよいかの明文化)と申告制で運用する方が実務的
- **「表示するかどうか」は既にEUでは任意ではない**: 2026年8月2日以降、EU域内でAI生成コンテンツやチャットボットを提供・運用する事業者は、EU AI Act第50条により表示・マーキングが法的義務になった。日本の法規制(AI事業者ガイドライン)は現時点でも推奨止まりだが、EU向け事業がある企業は国内基準だけで判断しないこと
- **対外的な信頼性の担保にはC2PA的な来歴表示の方が実務的**: 「これはAIで作っていない」ことを証明したい場面では、統計的推定に頼る検出ツールより、生成・撮影の時点から来歴を残すC2PA/Content Credentialsのような仕組みを自社の運用に組み込む方が確実性が高い

## 最初の一歩

自社が普段使っている画像生成AI(ChatGPT、Gemini、Adobe Fireflyなど)の生成物にContent Credentials(C2PA)やSynthIDの透かしが付与されているかを1つ試しにアップロードして確認し、EU向け事業がある場合はEU AI Act第50条の対象になっていないかを法務・コンプライアンス部門に確認するところから始める。

## 関連トピック

- [生成AIの規制・ガバナンス動向(企業が押さえるべきポイント)](./ai-regulation-and-governance-trends.md)
- [生成AIの著作権リスクと実務での注意点](./copyright-risks-in-generative-ai.md)
- [ハルシネーションとは何か・対策](./hallucination-and-countermeasures.md)

## 更新履歴

### 2026-08-02: C2PA普及状況・SynthIDの拡大・EU AI Act第50条を反映して最新化
- **内容**: C2PA会員数(6,000超)・C2PA 2.3・対応カメラ機種を追記。OpenAIが2026年5月にC2PA準拠+SynthID画像透かしを開始、同年7月には音声にも拡大したことを反映。SynthID Detectorが2026年8月時点も早期アクセス段階にとどまることを明記。Microsoft 365のウォーターマーク機能(画像は2026年2月、動画・音声は同年4月開始)とX(Premium)のContent Credentials表示を追記。AI文章検出ツールの実測精度(62〜88%)・Stanfordの偽陽性調査(TOEFLエッセイ61%誤判定)・50超の大学が検出ツール利用を禁止している事実を追加。2026年8月2日施行のEU AI Act第50条(透明性義務・罰則・機械可読マーキングの2026年12月猶予)を新設の節で解説し、使いどころ表・注意点にEU向け事業者への言及を追加
- **出典**: [C2PA Adoption Tracker: Which Platforms Support Content Credentials in 2026 | Editors Weblog](https://editorsweblog.org/2026/04/12/c2pa-adoption-tracker-platforms-content-credentials-2026)、[C2PA Adoption in 2026: Hardware Platforms and Verification Reality | SoftwareSeni](https://www.softwareseni.com/c2pa-adoption-in-2026-hardware-platforms-and-verification-reality/)、[The C2PA Trust Layer in 2026: Where It Works and Where It Breaks | SoftwareSeni](https://www.softwareseni.com/the-c2pa-trust-layer-in-2026-where-it-works-and-where-it-breaks/)、[SynthID Detector — a new portal to help identify AI-generated content | Google](https://blog.google/innovation-and-ai/products/google-synthid-ai-content-detector/)、[SynthID AI Watermark Google I/O 2026: Search and Chrome](https://magicshot.ai/news/synthid-ai-watermark-google-io-2026-updates/)、[Advancing content provenance for a safer, more transparent AI ecosystem | OpenAI](https://openai.com/index/advancing-content-provenance/)、[C2PA and SynthID in OpenAI-generated images | OpenAI Help Center](https://help.openai.com/en/articles/8912793-c2pa-in-chatgpt-images)、[OpenAI Gets Serious About Detecting Fake Images | PetaPixel](https://petapixel.com/2026/05/20/openai-gets-serious-about-detecting-fake-images/)、[Microsoft 365 adds AI watermarks for Copilot content | Windows Central](https://www.windowscentral.com/artificial-intelligence/microsoft-copilot/microsoft-365-now-watermarks-your-ai-content-because-nothing-says-fun-like-metadata-tracking)、[Add watermarks to content generated or altered by using AI in Microsoft 365 | Microsoft Learn](https://learn.microsoft.com/en-us/microsoft-365/copilot/watermarks)、[Is GPTZero Accurate? We Tested It Against 5 Other AI Detectors (2026)](https://blog.aibusted.com/is-gptzero-accurate/)、[GPTZero Review 2026: Accuracy, Pricing, and Verdict | Fastio](https://fast.io/resources/gptzero-ai-detector-review-2026/)、[Article 50 transparency obligations: the AI Act deadline of 2 August 2026 that has not been postponed | aiactblog.nl](https://www.aiactblog.nl/en/posts/article-50-transparency-deadline-2-august-2026)、[The EU AI Act's Transparency Rules: A Practical Guide to Article 50 | artificialintelligenceact.eu](https://artificialintelligenceact.eu/transparency-rules-article-50/)、[EU AI Act Update: Timeline Relief, Targeted Simplification, and New Prohibitions | Inside Privacy](https://www.insideprivacy.com/artificial-intelligence/eu-ai-act-update-timeline-relief-targeted-simplification-and-new-prohibitions/)、[【2026年最新】AI事業者ガイドライン改訂の要点 | GVA法律事務所](https://gvalaw.jp/blog/i20260303/)、[AI事業者ガイドライン(第1.2版)| 総務省・経済産業省](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_1.pdf)

### 2026-07-07: 初版執筆
- **内容**: AI生成コンテンツの真正性確認手段を「生成時に出所情報を埋め込む電子透かし・来歴方式(C2PA/Content Credentials、SynthID)」と「完成品を後から判定する事後検出ツール」の2系統に整理し、C2PAのマニフェスト・ハッシュ署名の仕組み、SynthIDのピクセル/トークンレベル埋め込みの仕組み、AI文章検出ツールの誤判定が構造的な問題であるとする2026年の研究、AI画像検出ツールの「いたちごっこ」の実情、OpenAI/Google/Adobe/Microsoft/Meta/主要報道機関の対応状況比較表、社内での検出ツール濫用を避けるべき理由をまとめた
- **出典**: [C2PA Adoption Tracker: Which Platforms Support Content Credentials in 2026 | Editors Weblog](https://editorsweblog.org/2026/04/12/c2pa-adoption-tracker-platforms-content-credentials-2026)、[The State of Content Authenticity in 2026 | Content Authenticity Initiative](https://contentauthenticity.org/blog/the-state-of-content-authenticity-in-2026)、[C2PA Adoption Status 2026 | eyesift](https://www.eyesift.com/faq/c2pa-content-credentials-2026-cryptographic-provenance-adoption/)、[C2PA FAQ](https://c2pa.org/faqs/)、[C2PA and Content Credentials Explainer(C2PA Specifications)](https://spec.c2pa.org/specifications/specifications/2.4/explainer/Explainer.html)、[Watermarking AI-generated text and video with SynthID — Google DeepMind](https://deepmind.google/blog/watermarking-ai-generated-text-and-video-with-synthid/)、[SynthID AI Watermark Google I/O 2026: Search and Chrome](https://magicshot.ai/news/synthid-ai-watermark-google-io-2026-updates/)、[OpenAI Adopts Google SynthID AI Watermarking | Framia](https://framia.converge.ai/page/en-US/news/openai-adopts-synthid-ai-watermarking-c2pa)、[AI Text Detectors Flag Polished Human Writing as AI: New Studies Expose a Built-In Paradox | Tech Times](https://www.techtimes.com/articles/319137/20260626/ai-text-detectors-flag-polished-human-writing-ai-new-studies-expose-built-paradox.htm)、[AI Detector False Positive Rates: 2026 Data Compared | GradPilot](https://gradpilot.com/news/ai-detector-false-positive-rates-compared)、[AI Text Detection Bias: What Our ACL 2026 Study Found | Pindrop](https://www.pindrop.com/article/ai-text-detection-bias/)、[The AI Image Generation Arms Race: Why 2026 Is the Year Everything Changes](https://miraflow.ai/blog/ai-image-generation-arms-race-2026-everything-changes)、[Best AI Image Detectors in 2026: Free and Paid Options Accuracy Tested | ddiy](https://ddiy.co/ai-image-detection-tools/)、[AI事業者ガイドライン(第1.2版)概要 総務省・経済産業省](https://www.meti.go.jp/shingikai/mono_info_service/ai_shakai_jisso/pdf/20260331_2.pdf)、[総務省: AI事業者ガイドライン掲載ページ](https://www.soumu.go.jp/main_sosiki/kenkyu/ai_network/02ryutsu20_04000019.html)
