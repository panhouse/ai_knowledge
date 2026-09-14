---
title: "モデルの種類と選び方(マルチモーダル・パラメータ数・SLM・VLM)"
part: 2
chapter: 第2章 モデルの種類と選び方
tags: [マルチモーダル, SLM, VLM, パラメータ数, モデル選び, モデル世代]
created: 2026-07-06
updated: 2026-09-05
---

# モデルの種類と選び方(マルチモーダル・パラメータ数・SLM・VLM)

## これは何か

「ChatGPTとGeminiとClaude、結局どれが良いのか」「モデル選択画面に並ぶGPT-6 AstraとGPT-5.6 Sol・Terra・Lunaの違いが分からず、いつも既定のままにしている」——モデル選びで迷う人の多くは、実は「賢さ」という1本の物差ししか持っていない。実際には、AIモデルは**扱えるデータの種類(マルチモーダル・VLM)**と**モデルの規模(パラメータ数・SLM)**という、賢さとは別の2つの軸で性格が大きく変わる。この2軸を知らないと、画像を読ませたいのにテキスト専用モデルを使って失敗したり、簡単な定型作業に高額な最上位モデルを使い続けてコストを無駄にしたりする。本ページは、この2軸と、モデル名から世代・性能傾向を読み取るコツを整理し、「今の作業にはどのモデルを選ぶべきか」を判断できるようにすることを目的とする。

なお、「即答モデルか推論モデルか」というもう1つの軸(考える時間をかけるかどうか)は、[推論モデル(Reasoning Model)とは何か](reasoning-model-basics.md)で詳しく扱っているため、本ページでは深入りしない。

## 仕組み・背景

### パラメータ数:モデルの「脳の大きさ」

パラメータ(parameter)とは、モデルが学習の過程で獲得した数値の集合で、入力された文章から次にどんな言葉が続くかを予測するための「重み」のようなものだ。パラメータ数は「7B」「70B」のように表記され、B(billion=10億)が単位になる(7B=70億パラメータ)。一般に、パラメータ数が多いほど複雑な文脈把握・推論・専門知識を扱う力が上がる傾向があるが、その分だけ計算量・メモリ消費・料金・応答速度も重くなる。つまりパラメータ数は「賢さのダイヤル」であると同時に「コストと速度のダイヤル」でもあり、この2つはトレードオフの関係にある。

OpenAI・Anthropic・Googleなどのクローズドな最上位モデルは、実際のパラメータ数を公表していない(GPT-6 AstraやClaude Fable 5.1、Claude Opus 5のパラメータ数は非公開)。一方、Meta・Google・Microsoftが公開している「オープンウェイト」モデル(パラメータの中身そのものをダウンロードできるモデル)は、パラメータ数がはっきり分かる。たとえばGoogleのGemma 4はE2B・E4B(モバイル・ブラウザ向けの超小型)・12B・26B A4B(MoE)・31Bの5サイズ構成、MicrosoftのPhi系は3.8Bの小型版から2026年に投入されたPhi-5(14B前後、数学・コーディングで大型モデルに迫る精度をうたう)まで幅がある。MetaのLlama 4 Scoutは合計1090億パラメータのうち実際の計算で使うのは170億パラメータ程度という「MoE(Mixture of Experts、専門家混合。質問ごとに一部のパラメータだけを選んで使う設計)」を採用している。同じ「パラメータ数が多い」でも、全部を毎回使うか一部だけ使うかでコスト構造が変わる点は覚えておくとよい。

なお、Metaのオープンウェイト路線は2026年に入って迷走が続いている。次世代の大型モデル「Behemoth」は投入時期が事実上凍結され、一時は非公開の「Muse Spark」系に軸足を移す動きも報じられたが、2026年8月にはApache 2.0ライセンスの新モデル「Muse Glimmer」(30B、常時稼働のローカルエージェント向け)を公開し、オープンウェイトに回帰した。同じベンダーの中でも「どの世代が今の主力オープンモデルか」が数か月単位で入れ替わりうる、という好例といえる。

### SLM(Small Language Model、小規模言語モデル):軽さで選ぶモデル

**SLM**とは、数億〜数百億パラメータ程度に規模を絞り、スマートフォン・ノートPC・社内サーバーでも動かせるように設計された言語モデルの総称。GPT-6 AstraやClaude Fable 5.1のような数千億パラメータ級の「LLM(大規模言語モデル)」と対になる概念で、明確なパラメータ数の境界線があるわけではないが、実務上は「クラウドの巨大データセンターがなくても動く規模のモデル」と捉えれば十分だ。代表例はMicrosoftのPhiシリーズ(Phi-4・Phi-5)、GoogleのGemma 4・Gemini Nano、MetaのMuse Glimmer(30B、Apache 2.0)、フランスMistral AIの小型モデル(Mistral Small系)など。SLMが選ばれる理由は「賢さでLLMに勝つ」ためではなく、次の3点にある。

- **コスト**: クラウドAPIの従量課金と比べ、自社サーバーやPC上でSLMを動かせば、初期のハードウェア投資後はほぼ電気代のみで運用でき、運用コストをLLMのAPI利用の5〜20%程度まで圧縮できるとする試算もある
- **プライバシー・コンプライアンス**: 契約書・顧客の個人情報・医療データなど、外部のクラウドに一切送信したくないデータを扱う場合、SLMを社内(オンプレミス)や端末上で完結させれば情報が外に出ない。欧州の金融機関がGDPR(EUの個人データ保護規則)対応のため、融資審査書類の分析や不正検知をオンプレミスのSLMで処理している例もある
- **速度(レイテンシ)**: ネットワーク越しにクラウドへ問い合わせる必要がなく、端末やオフィスのサーバー内で完結するため応答が速い。オフライン環境でも動く

裏を返せば、SLMは複雑な多段階の論理展開・幅広い一般知識を要する質問では大型モデルに劣る場面が多く、「軽く・速く・安く・情報を出さずに」使いたい定型タスクに向くモデル、と捉えるのが実務的な理解だ。

### マルチモーダル・VLM:文字以外を読み書きできるモデル

**マルチモーダル(multimodal)**とは、テキストだけでなく画像・音声・動画など複数の種類(モダリティ)のデータを1つのモデルで統合的に扱える性質を指す。2026年9月に投入されたOpenAIの最新世代GPT-6 Astraは、旧来のテキスト・画像・音声・動画を単一システムで処理する「ネイティブ・オムニモーダル」設計に加えて、画面を見ながら操作する「コンピュータ操作(computer use)」やブラウジングでもOpenAI社内で最高水準の性能を打ち出しており、「モダリティを扱う」だけでなく「モダリティを介して行動する」方向に進化している。GeminiシリーズもGemini 1.5世代以降、画像・音声・動画理解を標準搭載している。一方でClaude(Sonnet 5・Opus 5・最上位のFable 5.1含む)は、モデル自体(API)が直接受け付けるのはテキストと画像までで、音声・動画のネイティブ理解は主要機能として提供されていない。claude.aiアプリの「音声モード」は2026年7月にSonnet・Opusでも使えるよう拡張されたが、これは音声認識(音声→テキスト変換)と読み上げを組み合わせた体験であり、GPT・Geminiのようにモデルが音声波形そのものを直接理解する仕組みとは異なる点に注意したい。「マルチモーダル対応」と一口に言っても、どのモダリティまで・どんな仕組みで扱えるかはベンダー・モデルによって差がある。

**VLM(Vision Language Model、視覚言語モデル)**は、マルチモーダルモデルのうち特に「画像・映像を理解して言語で説明・応答する」ことに特化した種類を指す言葉として使われる。仕組みを大づかみに言うと、画像を認識する部分(画像を特徴の集合に変換するビジョンエンコーダ)と、文章を生成する言語モデル部分を組み合わせ、画像の内容を言語モデルが理解できる形式に変換して橋渡しする構造になっている。GPT-4o以降のGPT系・Gemini・Claudeのように汎用チャットAIに画像理解機能として組み込まれる形と、製造業の外観検査や現場作業員の安全管理のように特定の業務に特化して調整される形の両方がある。日立ソリューションズ・テクノロジーは現場作業員の安全管理・業務効率化を目的にVLMの実証実験を2025年から進めており、2026年度の実用化を見据えている。

## 使いどころ・使い分け

### モデル規模(パラメータ数)の選び方

判断の軸は「タスクの複雑さ」と「データを外に出せるか・コストをどこまで許容できるか」。

| タスクの性質 | 向いている規模 | 理由 |
|---|---|---|
| 契約書・企画書の論点整理、複雑な分析、専門知識を要する質問 | 大型モデル(フラッグシップ級) | 幅広い知識と多段階の論理展開が必要 |
| メールの下書き・要約・分類・簡単な翻訳などの定型作業を大量にこなす | 中型〜軽量モデル | 精度は大型に近く、速度とコストで有利 |
| 顧客の個人情報・医療データ・機密資料を扱う、外部送信そのものがNGな業務 | SLM(オンプレミス・端末上で運用) | データを外に出さずに処理できる |
| チャットボット・音声アシスタントなど、大量アクセスをさばく必要がある常時稼働サービス | SLM・軽量モデル | 1回あたりのコストと応答速度が業務の成否を左右する |
| オフライン環境・ネットワークが不安定な現場(工場・店舗・車両内など)での利用 | SLM(端末上で完結) | クラウド接続が前提の大型モデルは使えない |

迷ったら「まず安い・軽いモデルで試し、精度不足を感じたら1段階上のモデルに切り替える」順番がコスト効率的にはよい。逆に、機密情報を扱う可能性がある業務は、精度を試す前に「外部送信して良いデータか」を先に確認する。

### マルチモーダル・VLMが必要かどうかの判断

| やりたいこと | 必要な機能 | 具体例 |
|---|---|---|
| 文章の作成・要約・分析だけで完結する | テキスト専用でも可 | メール下書き、議事録要約、企画書のたたき台作成 |
| 紙の書類・レシート・名刺・ホワイトボードの写真を読み取らせたい | 画像入力対応(マルチモーダル/VLM) | 経費精算のレシート読み取り、名刺のデータ化、手書きメモのテキスト化 |
| グラフ・図表・スクリーンショットの内容を説明・分析させたい | 画像入力対応(VLM) | 決算資料のグラフ読み取り、UIのバグをスクリーンショットで説明 |
| 製造ラインの外観検査、現場作業員の安全確認など映像を継続的に監視したい | 動画理解対応の業務特化VLM | 工場の不良品検知、危険行動の検知 |
| 会議や電話の音声をリアルタイムで文字起こし・要約・対話したい | 音声対応(マルチモーダル) | 議事録の自動作成、音声アシスタント、コールセンターの自動応答 |

汎用のマルチモーダルモデルは「幅広く画像・音声を扱える」が、業務特有の見た目のパターン(特定製品の傷、特定様式の帳票)を高精度で扱うには、業務特化型のVLM(追加学習・専用チューニングを施したもの)の方が実用精度に達しやすい点も覚えておく。

## 実務での使い方

### 主要モデルの規模・料金の目安(2026年9月時点)

パラメータ数が非公開のクローズドモデルも多いため、実務ではAPI料金(処理速度・規模のおおよその代理指標になる)で規模感をつかむのが分かりやすい。金額は1トークン(文章を処理する最小単位)あたりではなく、100万トークンあたりの目安。

| 層 | 提供元・モデル例 | 入力/出力 料金(100万トークンあたり) | 想定用途 |
|---|---|---|---|
| 特別階層(限定提供) | Anthropic Claude Mythos 5.1 | 非公開(サイバー防御・ライフサイエンス系の認定組織のみ利用可) | 国家級のセキュリティ対応・先端科学研究など特殊用途 |
| 最上位(新世代) | OpenAI GPT-6 Astra | $10 / $50 | コンピュータ操作・ブラウジング・ソフトウェア工学・サイバーセキュリティ・科学研究など最難関タスク(2026年9月3日提供開始) |
| 最上位(新世代) | Anthropic Claude Fable 5.1 | $10 / $50(キャッシュ読込は$0.25) | 高度なコーディング・長時間の自律エージェント・複数ステップの調査などの専門知識労働 |
| フラッグシップ級 | OpenAI GPT-5.6 Sol | $4 / $20(2026年8月22日値下げ後。11月21日まで据え置き保証) | 最重要タスクだが特別階層ほどのコストはかけたくない場合 |
| フラッグシップ級 | Anthropic Claude Opus 5 | $5 / $25 | 難易度の高いコード・長時間のエージェントタスク(Fable 5.1に迫る精度を半額程度で) |
| フラッグシップ級 | Google Gemini 3.1 Pro | $2〜4 / $12〜18(200Kトークン超で単価上昇) | 複雑な分析・専門知識を要する業務全般(後継の3.5 Proは発表から延期が続き2026年9月時点も未提供) |
| 標準(汎用チャット既定) | OpenAI GPT-5.6 Terra | $2 / $12 | 日常的な業務全般 |
| 標準(汎用チャット既定) | Anthropic Claude Sonnet 5 | $2 / $10(2026年9月に予定されていた$3/$15への値上げは撤回され据え置き) | 日常的な業務全般。コーディング・エージェント用途にも強い |
| 軽量・高速 | OpenAI GPT-5.6 Luna | $0.20 / $1.20(2026年8月22日値下げ後) | コストを最優先する高頻度タスク |
| 軽量・高速 | Anthropic Claude Haiku 4.5 | $1 / $5 | 大量処理・定型タスク・チャットボットの土台 |
| 軽量・高速 | Google Gemini 3.8 Flash | $0.75 / $3.75(2026年内の導入価格。2027年から$1.50/$7.50) | バランス重視の高頻度処理 |
| 軽量・高速 | Google Gemini 3.5 Flash-Lite | $0.30 / $2.50 | 大量アクセスをさばく常時稼働サービス、書類の高速処理 |
| SLM(公開パラメータ数あり・自社運用向け) | Google Gemma 4(E2B/E4B/12B/26B A4B/31B) | 自社サーバー・PCで運用(ダウンロード無料、電気代のみ) | オンプレミス・端末上での業務、機密データ処理 |
| SLM(公開パラメータ数あり・自社運用向け) | Microsoft Phi-4/Phi-5系(3.8B〜14B程度) | 同上 | スマートフォン・ノートPC上での軽量処理 |
| SLM(常時稼働エージェント向け) | Meta Muse Glimmer(30B、Apache 2.0) | 同上 | ローカルで動かす常駐エージェント・関数呼び出し・コーディング支援 |
| 中〜大規模オープンウェイト | Meta Llama 4 Scout(総計1090億・実処理170億パラメータのMoE) | 自社運用、またはクラウド経由のAPI提供あり | 自社ホスティングでのコスト最適化。ただしMetaは大型後継Behemothの投入時期を明言しておらず、最新の主力オープンモデルは軽量なMuse Glimmerに移っている |

補足: 同じベンダーでも複数の価格帯・規模のモデルが並行して提供されるのが2026年時点の標準的な構成。呼び名の付け方はベンダーごとに変わりつつある。OpenAIはGPT-5.6から「mini/nano」の代わりに、世代番号(5.6)とは別に恒久的な階層名(Sol=最上位、Terra=標準、Luna=軽量)を組み合わせる方式に変更し、2026年9月にはさらに上の新世代GPT-6 Astraを投入したが、Sol・Terra・Lunaの3階層はそのまま併売を続けている。まずは標準(無印・Terra・Sonnet系)モデルで様子を見て、コストが気になれば軽量版、精度が足りなければ上位モデル、という順で調整するのが実務的。なお、AnthropicはOpus 4.8→Opus 5(7月)→Fable 5.1/Mythos 5.1(9月)という具合に、既存のOpus/Sonnet/Haikuの3階層のさらに上に位置する最上位モデルを数か月単位で更新しており、常に「今一番上にあるのはどれか」を確認する意識が要る。

### マルチモーダル対応のツール横断比較

| ツール | 画像入力 | 音声対話 | 動画理解 | 補足 |
|---|---|---|---|---|
| ChatGPT(GPT-6 Astra・GPT-5.6系) | 対応(写真・スクリーンショットをドラッグ&ドロップまたはクリップアイコンから添付) | 対応(「音声モード」、Realtime API経由でリアルタイム対話も可能) | 対応(テキスト・画像・音声・動画を単一システムで扱うオムニモーダル設計。Astraは画面を見ながら操作する「コンピュータ操作」も強化) | モデル選択とは別に、機能自体が有効かはプラン・地域によって異なる場合がある |
| Gemini | 対応(入力欄にファイルを添付) | 対応(音声入力・読み上げ) | 対応(YouTube動画のURL共有や動画ファイルの読み込みに対応) | Geminiアプリの「ファイルを追加」または画面下部のマイクアイコンから利用 |
| Claude(claude.ai) | 対応(入力欄のクリップアイコンから画像を添付、PDF内の図表も画像として解釈) | 対応(「音声モード」。2026年7月にSonnet・Opusにも拡大)。ただし音声認識+読み上げの組み合わせで、モデルが音声波形を直接理解する仕組みではない | 非対応 | 動画をモデルに直接理解させたい業務では、この点でChatGPT・Geminiとの機能差を考慮する必要がある |

### コピペで使える例(画像を読み込ませて構造化データを取り出す)

経費精算のレシートや名刺のような定型書類は、次のように「出力形式を指定して」画像を読み込ませると後工程(表計算ソフトへの転記など)に流用しやすい。

```
添付した画像はレシートです。以下の項目をJSON形式で抽出してください。
読み取れない項目は null にしてください。

{
  "店舗名": "",
  "日付": "",
  "合計金額": 0,
  "内訳": [{"品目": "", "金額": 0}]
}
```

VLMの出力を業務システムに自動連携する場合、1文字のズレがデータ破損につながるため、抽出後は必ず人が目視で数件サンプルチェックする工程を挟むこと。

### モデル名から世代・性能傾向を読み取るコツ

モデル名は一見暗号のようだが、次のパターンを知っておくと画面を見ただけである程度の性格を推測できる。

| 名前に含まれる要素 | 意味の目安 | 例 |
|---|---|---|
| バージョン番号(数字)が大きい | 基本的には新しい世代。旧世代より総合力が高い傾向 | GPT-6はGPT-5.6より新しい、Claude Sonnet 5はSonnet 4.6より新しい |
| 「Pro」「Ultra」「Opus」 | 同じ世代の中で最上位・最高精度クラス | Gemini 3.1 Pro、Claude Opus 5 |
| 「mini」「nano」「Flash」「Flash-Lite」「Haiku」 | 同じ世代の軽量・高速・低価格クラス | Gemini 3.8 Flash・3.5 Flash-Lite、Claude Haiku 4.5 |
| 世代番号とは別の「恒久的な階層名」 | バージョンが上がっても同じ階層名を使い回すことで、階層の意味を毎回覚え直さなくて済むようにした命名方式。数字は世代を、階層名は性格(最上位・標準・軽量)を表す、という役割分担 | OpenAIがGPT-5.6から採用したSol(最上位)・Terra(標準)・Luna(軽量) |
| 新しい世代番号が追加されても旧世代の階層はそのまま併売される | フラッグシップの新世代(番号違い)を投入しても、旧世代の標準・軽量モデルは価格・速度の選択肢として残り続けることがある。「一番新しい名前=今使うべきモデル」とは限らない | 2026年9月、OpenAIはGPT-6 Astraを投入したが、GPT-5.6 Sol・Terra・Lunaは引き続き併売されている |
| 「Thinking」「Reasoning」「Deep Think」等の付記 | 答えを出す前に長く考える推論モデル系統(詳細は[推論モデルとは何か](reasoning-model-basics.md)) | GPT-5.5 Thinking、Gemini 3 Deep Think |
| 日付・スナップショットのID(例: gpt-5.6-2026-06-26) | 特定時点で固定されたバージョン。API開発者向けに、モデルが勝手に更新されて動作が変わらないよう固定する目的 | 主にAPI(開発者向け呼び出し)で使う表記で、一般ユーザー向けチャット画面では意識しなくてよいことが多い |
| コードネーム的な名称(Scout、Maverick、Glimmer等) | オープンウェイトモデルに多い、規模やパラメータ構成を表さない固有名 | Llama 4 ScoutとMaverickは同世代でも規模・特性が異なる。MetaのMuse Glimmerは30Bのエージェント特化モデル |
| 既存の階層構造の「さらに上」に追加される新しい呼称 | ベンダーが従来の最上位モデルよりもさらに高精度なモデルを投入する際、既存の命名パターン(Pro/Opus等)を使わず新しい呼称を新設することがある。提供範囲が限定的(法人・特定用途向けのみ)なケースも多い | Anthropicの「Mythos級」モデル(公開版がFable 5.1、限定提供版がMythos 5.1)は、Opus 5よりさらに上に位置づけられる新設の階層 |

注意点として、これらの命名規則はベンダーごとにバラバラで、統一ルールがあるわけではない。「番号が大きいから必ず高性能」と鵜呑みにせず、特に世代をまたぐ比較(例: 旧世代の上位モデル vs 新世代の軽量モデル)では、軽量な新モデルの方が旧世代の上位モデルに性能で追いつく・逆転することも珍しくない。また、階層名(Pro/Opus/Sol等)の位置づけ自体も、上記のように新しい最上位階層の新設によって変わることがあるため、「このモデル名は今そのベンダーの中で何番目に位置するか」は名前だけで判断せず、迷ったら公式サイトの比較表・ベンチマークで確認するのが確実。逆に、発表された新モデルがそのまま計画どおり出てくるとも限らない。Googleは2026年5月の発表会でGemini 3.5 Proの「1か月以内の提供」を予告したが、2026年9月時点で3回延期が続き、正式な提供日も定まっていない。アナウンスは「予定」であって「今日使えるもの」ではない、という前提で情報を追うとよい。

## 注意点・よくある誤解

- **「パラメータ数が多い=そのタスクに最適」ではない**: 定型作業・大量処理では、軽量モデルの方が精度をほぼ落とさずコストと速度で圧倒的に有利なことが多い。まず軽量モデルで試すのが無駄のない順番
- **SLMは「性能が低いモデル」ではなく「規模を絞ったモデル」**: 用途に合えば大型モデルと遜色ない結果を出すことも多く、「安かろう悪かろう」と決めつけない。ただし幅広い一般知識・複雑な多段階推論が必要なタスクでは大型モデルに劣る場面が多い
- **マルチモーダル対応の範囲はモデルごとに違う**: 「画像は読めるが音声・動画は非対応」のように、モダリティごとに対応状況が異なる。使いたい入力形式に本当に対応しているか、導入前に必ず確認する
- **VLMの画像認識は完璧ではない**: 手書き文字の癖が強い書類、低画質・不鮮明な画像、複雑なレイアウトの帳票では読み取り誤りが発生する。業務システムに自動連携する前に、必ずサンプルで精度を検証する工程を挟む
- **モデル名・料金・スペックは数か月おきに変わる**: 本ページで挙げた名称・価格(GPT-6 Astra、GPT-5.6、Claude Fable 5.1・Opus 5・Sonnet 5、Gemini 3.1 Pro・3.8 Flash、Gemma 4等)は執筆時点の目安であり、実際の画面表示・最新の料金は都度公式サイトで確認する
- **「今の最上位」は数か月で入れ替わる**: 2026年だけでもAnthropicはOpus 4.8→Opus 5→Fable 5.1、OpenAIはGPT-5.6 Sol→GPT-6 Astraと、最上位モデルを短いサイクルで更新している。半年前の記事・資料に書かれた「最上位モデル」を鵜呑みにせず、業務で使う直前に画面上の選択肢を確認する
- **クローズドモデルのパラメータ数は公式には非公開**: 「GPT-5.5は◯兆パラメータ」といった数字がネット上で語られることがあるが、多くは推測・非公式情報であり、公式発表として鵜呑みにしない

## 最初の一歩

普段使っているAIツールのモデル選択画面を開き、いま既定になっているモデルが「標準」「軽量」「Pro」のどの層にあたるかを確認する。次に、直近で行った定型的な作業(要約・分類・下書きなど)を1つ選び、より軽量なモデルに切り替えて同じ作業をやらせてみて、精度と速度の違いを体感してみる。

## 関連トピック

- [推論モデル(Reasoning Model)とは何か](reasoning-model-basics.md)
- [コンテキストウィンドウの基本(なぜ大切か・モデル別の違い)](context-window-basics.md)
- [LLMの得意・不得意と挙動の特性](llm-strengths-and-limitations.md)
- [ChatGPTのモデル一覧と使い分け](../part03-ai-chat-tools/chatgpt-model-lineup.md)
- [ローカルLLMの基本(自社PC・サーバーで動かす生成AI)](../part08-specialized-ai-tools/local-llm-basics.md)

## 更新履歴

### 2026-09-05: 主要モデルの世代・料金・オープンウェイト動向を2026年9月時点に更新
- **内容**: OpenAIが2026年9月3日にGPT-6 Astra($10/$50、コンピュータ操作・サイバーセキュリティ・科学等で最高性能をうたう新世代)を投入した一方、GPT-5.6 Sol・Terra・Lunaも併売が続いていることを反映し、料金を8月22日の値下げ後の水準(Sol $4/$20、Terra $2/$12、Luna $0.20/$1.20)に更新。AnthropicがClaude Opus 5($5/$25、7月24日)とClaude Fable 5.1・Mythos 5.1($10/$50、9月1日、Mythosは認定組織限定)を投入したこと、Sonnet 5の値上げ予定($3/$15への変更)が撤回され$2/$10のまま据え置かれたことを追記。GoogleはGemini 3.1 Proが依然フラッグシップで、後継の3.5 Proが発表から3回延期され2026年9月時点も未提供であること、軽量層がGemini 3.8 Flash($0.75/$3.75、導入価格)・3.5 Flash-Lite($0.30/$2.50)に更新されたことを反映。オープンウェイト勢は、GoogleがGemma 4(E2B/E4B/12B/26B A4B/31Bの5サイズ)を投入したこと、MicrosoftがPhi-5(14B前後)を展開しつつあること、MetaがLlama後継Behemothの投入を事実上凍結し一時は非公開の「Muse Spark」路線に転じた後、2026年8月にオープンウェイトの常駐エージェント向けモデル「Muse Glimmer」(30B、Apache 2.0)で回帰したことを追記。あわせて、Claudeの音声モードが2026年7月にSonnet・Opusへ拡大された(ただし音声認識+読み上げ方式でネイティブ音声理解ではない)ことをマルチモーダル比較表に反映し、「発表された新モデル・階層は必ずしも計画通りに出荷されない」「最上位モデルは数か月単位で入れ替わる」という実務上の注意点を追加した
- **出典**: [OpenAI: GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/)、[Axios: OpenAI releases new model GPT-6 Astra, says it may represent AGI](https://www.axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman)、[aipricing.guru: OpenAI API Pricing (September 2026): GPT-6 Astra & GPT-5.6](https://www.aipricing.guru/openai-pricing/)、[Anthropic: Introducing Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)、[MacRumors: Anthropic Launches Claude Fable 5.1 With Lower Costs and Fewer False Positives](https://www.macrumors.com/2026/09/01/anthropic-claude-fable-5-1/)、[Axios: Anthropic releases new model, Opus 5](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5)、[BenchLM.ai: Claude API Pricing (September 2026)](https://benchlm.ai/anthropic/api-pricing)、[Fortune: Google shipped four Gemini Flash models in 106 days. But its flagship frontier model is still nowhere to be seen.](https://fortune.com/2026/09/03/google-shipped-four-gemini-flash-models-in-106-days-but-its-flagship-frontier-model-is-still-nowhere-to-be-seen/)、[devtk.ai: Gemini 3.1 Pro Preview API Pricing](https://devtk.ai/en/models/gemini-3-1-pro/)、[eesel AI: Gemini 3.8 Flash review 2026](https://www.eesel.ai/blog/gemini-3-8-flash)、[Google AI for Developers: Gemma 4 model overview](https://ai.google.dev/gemma/docs/core)、[Google Developers Blog: Gemma 4 12B: The Developer Guide](https://developers.googleblog.com/gemma-4-12b-the-developer-guide/)、[VentureBeat: Meta returns to open source with Muse Glimmer](https://venturebeat.com/technology/meta-returns-to-open-source-with-muse-glimmer-an-apache-2-0-licensed-30b-parameter-ai-model-optimized-for-agents-available-now)、[InfoQ: Meta Open-Sources Muse Glimmer](https://www.infoq.com/news/2026/08/meta-muse-glimmer/)、[Computerworld: Meta hits pause on 'Llama 4 Behemoth' AI model amid capability concerns](https://www.computerworld.com/article/3987990/meta-hits-pause-on-llama-4-behemoth-ai-model-amid-capability-concerns.html)、[TechCrunch: Anthropic updates Claude voice mode with more capable models](https://techcrunch.com/2026/07/23/anthropic-updates-claude-voice-mode-with-more-capable-models/)、[Spheron: Deploy Microsoft Phi-5 on GPU Cloud](https://www.spheron.network/blog/deploy-phi-5-gpu-cloud/)

### 2026-07-27: 主要モデルの世代・料金例と命名規則の節を最新化
- **内容**: 2026年7月時点の最新ラインナップに合わせて更新。OpenAIがGPT-5.6でSol(最上位)・Terra(標準)・Luna(軽量)という、世代番号と恒久的な階層名を切り離す新しい命名方式を採用したことを追記。Anthropicが既存のOpus/Sonnet/Haikuの3階層のさらに上に「Mythos級」(公開版Fable 5・限定提供版Mythos 5)という新階層を新設した動きを、命名規則の注意点として追加。Google Gemini 3.6 Flash・3.5 Flash-Lite(2026年7月21日発表)とGemini 3.1 Pro(現行フラッグシップ、3.5 Proはテスト中)の料金を反映。主要モデルの規模・料金比較表とツール横断のマルチモーダル対応表のモデル名表記を更新
- **出典**: [OpenAI: GPT-5.6](https://openai.com/index/gpt-5-6/)、[TechCrunch: OpenAI launches its new family of models with GPT-5.6](https://techcrunch.com/2026/07/09/openai-launches-its-new-family-of-models-with-gpt-5-6/)、[aipricing.guru: GPT-5.6 Pricing (July 2026)](https://www.aipricing.guru/openai-pricing/)、[CNBC: Anthropic releases Mythos-like AI model to the public, Claude Fable 5](https://www.cnbc.com/2026/06/09/anthropic-mythos-claude-fable-5.html)、[Anthropic: Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)、[Al Jazeera: US lifts restrictions on Anthropic's powerful AI models Fable and Mythos](https://www.aljazeera.com/economy/2026/7/1/us-lifts-restrictions-on-powerful-ai-models-fable-mythos-anthropic-says)、[TechCrunch: Google releases three new Gemini models — but no 3.5 Pro](https://techcrunch.com/2026/07/21/google-releases-three-new-gemini-models-but-no-3-5-pro/)、[Google Blog: Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)、[eesel AI: Gemini 3.5 Pro pricing (2026)](https://www.eesel.ai/blog/gemini-3-5-pro-pricing)

### 2026-07-06: 初版執筆
- **内容**: モデル選びを左右する2軸(扱えるデータの種類=マルチモーダル・VLM、モデルの規模=パラメータ数・SLM)を整理。パラメータ数と性能・コストのトレードオフ、SLMが選ばれる理由(コスト・プライバシー・速度)、マルチモーダル/VLMの仕組みと業務活用例、2026年7月時点の主要モデルの規模・料金比較表、ツール横断のマルチモーダル対応表、画像読み取りのコピペ用プロンプト例、モデル名から世代・性能傾向を読み取るコツと注意点をまとめた
- **出典**: [Harmonic Society: SLM(小規模言語モデル)とは？](https://harmonic-society.co.jp/what-is-slm-small-language-model/)、[HP Tech&Device TV: SLM徹底比較ガイド2026](https://jp.ext.hp.com/techdevice/ai/ai_explained_42/)、[Smart Generative Chat: SLM導入ガイド｜エッジAIで低コスト化する方法](https://smart-generative-chat.com/2025/12/15/slm-edge-ai-cost-reduction-guide/)、[KPMG: マルチモーダルLLM時代における視覚言語モデル（VLM）の構成とビジネス活用の課題](https://kpmg.com/jp/ja/insights/2026/06/alh-vision-language-model.html)、[日立ソリューションズ・テクノロジー: VLM活用実証実験開始](https://www.hitachi-solutions-tech.co.jp/corporate/news/2025/nr251113.html)、[note(Fushiki): ChatGPT/OpenAI 2026年春アップデート徹底解説](https://note.com/zouplans/n/n201761e26abf)、[OpenAI: Introducing gpt-realtime](https://openai.com/index/introducing-gpt-realtime/)、[Hikari's Notebook: GPT-5.4 / mini / nano Pricing and Performance Comparison](https://www.hikari-dev.com/en/blog/2026/04/18/gpt-54-pricing-comparison/)、[Uravation: GPT-5.4にminiとnano追加｜推論コスト最大92%減](https://uravation.com/media/gpt-54-mini-nano-api-cost-92-percent-cut-2026/)、[Uravation: Gemini 3.1 Flashとは？料金・性能・GPT-4o比較](https://uravation.com/media/gemini-31-flash-guide/)、[サーバーワークスエンジニアブログ: Claude Sonnet 5 リリース！](https://blog.serverworks.co.jp/2026/07/01/084500)、[Anthropic: Introducing Claude Haiku 4.5](https://www.anthropic.com/news/claude-haiku-4-5)、[pricepertoken: Claude Haiku 4.5 API Pricing 2026](https://pricepertoken.com/pricing-page/model/anthropic-claude-haiku-4.5)、[Google Developers Blog: Introducing Gemma 3](https://developers.googleblog.com/en/introducing-gemma3/)、[arXiv: Phi-3 Technical Report: A Highly Capable Language Model Locally on Your Phone](https://arxiv.org/pdf/2404.14219)
