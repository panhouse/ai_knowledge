---
title: "ローカルLLMの基本(自社PC・サーバーで動かす生成AI)"
part: 8
chapter: 第4章 ローカル・オープンモデル
tags: [ローカルLLM, Ollama, LM Studio, オープンウェイト, セキュリティ, オンプレミス]
created: 2026-07-06
updated: 2026-08-22
---

# ローカルLLMの基本(自社PC・サーバーで動かす生成AI)

## これは何か

ChatGPT・Claude・Gemini APIは、入力した文章をインターネット経由で各社のサーバーに送り、処理結果を受け取る仕組みである。これに対し「ローカルLLM」は、Llama(Meta)・Gemma(Google)・Mistral・DeepSeek・Qwen(Alibaba)・GLM(Zhipu/Z.ai)といった、モデルの重み(パラメータそのもののデータ)が公開されている「オープンウェイトモデル」を自社のPCやサーバーにダウンロードし、その機材の中だけで動かす方式を指す。最大の特徴は、入力したデータが一切外部に送信されないこと。契約書・顧客の個人情報・未公開の経営情報など、外部のクラウドサービスに預けたくないデータを扱う業務で、「AIを使いたいが情報漏洩は避けたい」というジレンマを解決する選択肢になる。2026年に入り、国内でもインテックのようなSIerがオンプレミス生成AI導入の支援サービスを立ち上げるなど、「技術的に可能」から「実際に企業が採用する」段階へと移りつつある。

## 仕組み・背景

### Ollama・LM Studioという「入り口」

かつてローカルLLMを動かすにはPython環境の構築やコマンドラインでの細かい設定が必要で、非エンジニアには敷居が高かった。この状況を変えたのが[Ollama](https://ollama.com/)と[LM Studio](https://lmstudio.ai/)という2つのツールである。

- **Ollama**: コマンド1行でモデルのダウンロードから起動までを済ませられる無料ツール。GUI(画面操作)はシンプルだが、裏側でモデル管理・GPU活用・API提供までを自動でこなしてくれる。2026年8月時点でv0.32.14が最新で、Llama系・Gemma・DeepSeek・Qwen・Mistral・GLM・Muse Glimmer(後述)・OpenAIが公開した「gpt-oss」など数百種類のモデルを[公式ライブラリ](https://ollama.com/library)から`ollama pull`コマンド1つで取得できる。直近の更新ではモデルのメタデータをリクエスト間でキャッシュする改良により初回応答までの時間がほぼ半減するなど、地味だが実用上効くパフォーマンス改善が続いている。素の`ollama`コマンドを実行するだけでチャット・コード生成・Web検索・タスク委任までこなす「エージェント」としての位置づけも定着してきている
- **LM Studio**: マウス操作だけで完結するデスクトップアプリ。「Discover」タブでモデルを検索すると、ダウンロード前に「このモデルを動かすにはRAM・VRAM(グラフィックボードのメモリ)がどれくらい必要か」を表示してくれるため、非エンジニアでも「自分のPCで動くか」を事前に判断しやすい。ChatGPTのような画面でそのままチャットでき、社内文書(PDF・Word等)を読み込ませて質問することもできる。2026年8月時点でv0.4.21系が最新。7月末には「Bionic」という自律型AIエージェント機能が追加され、ローカルモデルに複数ステップの作業をまとめて任せられるようになった。社内の1台をサーバー化して他のPCから使わせる「LM Link」(暗号化トンネル経由でリモート接続)や、コマンド1つでLinuxサーバー・クラウドVMに導入できる「llmster」というヘッドレス配布モードも継続提供されており、個人利用からチーム利用への橋渡しがしやすくなっている

どちらも「モデル本体(重み)」と「動かすためのツール(推論エンジン)」がセットで、モデルはHugging Face等で配布されているオープンウェイトのものを使う。有料のクラウドAPIと違って、動かすための電気代・機材代以外の追加課金は基本的に発生しない。

### パラメータ数とPCスペックの関係(ざっくり目安)

モデルの大きさは「パラメータ数」(Bはbillion=10億の略。例: 7B=70億パラメータ)で表され、数字が大きいほど賢い傾向がある一方、動かすために必要なメモリも大きくなる。実際にはモデルを軽量化する「量子化」(精度を少し落として容量を圧縮する処理。ダウンロード時に自動で選べることが多い)を経て配布されるため、目安としては次のようなイメージで捉えておけば十分である。

| モデルの目安 | 必要メモリの目安 | 動作イメージ |
|---|---|---|
| 7B〜8B程度(小型) | 8GB前後 | 一般的なノートPC(GPUなし・メモリのみ)でも動く。反応はやや遅め |
| 13B〜30B程度(中型) | 16〜24GB前後(GPU搭載推奨) | ゲーミングPC・ワークステーション級のGPUで実用速度 |
| 70B前後(大型) | 40GB以上(業務用GPU相当) | 個人PCでは厳しく、サーバー・クラウドGPUでの運用が現実的 |

数字は量子化の方式やソフトによって変動する目安に過ぎないが、「パラメータ数が2倍になれば必要なメモリもおおよそ2倍になる」という感覚を持っておくと、ツールが表示する推奨スペックの意味を理解しやすい。GPU(画像処理用の演算装置。AIの計算にも使われる)がないPCでもCPU・メモリだけで動かせるが、速度はかなり落ちる。より具体的な機材選びの目安としては、次のような相場観を持っておくと判断しやすい。

- **最低ライン**: システムメモリ16GB以上・VRAM(グラフィックボードのメモリ)6GB以上のGPU、またはApple Silicon搭載Mac。ここまであれば3B〜7B級モデルを量子化した状態で動かせる(Ollama自体はGPUなし・メモリ8GB・空き容量10GB程度でも起動する)
- **実用的な「ちょうどいい」ライン**: VRAM24GB前後のGPUなら、後述するQwen 3.8系(27B)のような中型モデルを量子化した状態で無理なく動かせる。VRAM16GB程度でもGemma 4の12B相当モデルなら動作の余地がある
- **大型モデルを試したい場合**: Apple Silicon Macの統合メモリ(GPU・CPUで共有するメモリ)は96GBあれば70B級モデルを高精度な量子化で動かせるなど、Mac 1台でも相応の規模まで手が届く
- **Windows・Linux + AMD製GPUの場合**: AMD純正の計算基盤「ROCm」を導入していないと、30B級を超えるモデルではGPUが使われずCPUだけの動作に切り替わり速度が大きく落ちる。ROCm 7系はLinuxでは安定するが、Windowsでは動作にばらつきが出やすい点に注意する

注意したいのは、DeepSeek・Qwen・GLM・gpt-oss・NVIDIA Nemotron(後述)など最近の大型モデルの多くが「MoE(Mixture of Experts、専門家混合)」という構造を採っている点である。これは「総パラメータ数」は数百B〜1T超と巨大でも、1回の応答生成では一部の「専門家」だけが動く仕組みで、実際に必要なメモリは総パラメータ数よりかなり少なく済むことが多い。ただしモデル全体を保持するためのストレージ・メモリ自体は総パラメータ数に応じて必要になるため、「MoEだから軽い」と早合点せず、ツールが示す実測の推奨スペックを必ず確認すること。

## 使いどころ・使い分け

クラウドAPI(ChatGPT・Claude・Gemini API等)とローカルLLMは対立する選択肢ではなく、扱うデータや用途に応じて使い分けるのが実務的である。

| 比較軸 | ローカルLLM | クラウドAPI(ChatGPT/Claude/Gemini等) |
|---|---|---|
| 情報漏洩リスク | 低い(データが自社機材の外に出ない) | 各社の法人向けプラン・データ保護契約に依存する |
| 性能・最新機能 | 同世代のクラウド最大モデルには見劣りしやすい | 最先端の大規模モデル・最新機能をいち早く使える |
| コスト構造 | 初期のハードウェア投資が中心(以降は電気代程度) | 使った分だけの従量課金・月額課金が中心 |
| 導入の手間 | ツールのインストール・モデル選定・運用の手間がかかる | アカウント登録だけですぐ使える |
| オフライン対応 | 可能(インターネット接続不要で動かせる) | 不可(通信が前提) |
| 精度・応答の安定感 | モデル・設定次第でばらつきが出やすい | 各社がチューニング済みで安定していることが多い |

判断の目安は次のとおり。

- **機密性の高いデータ(契約書・顧客情報・未公開の技術情報等)を扱う業務、あるいは工場・研究所などオフライン環境が前提の業務**: ローカルLLMが有力な選択肢になる
- **最新・最高性能を求める用途(高度な推論、最新の一般知識、マルチモーダル処理など)、あるいは導入の手間を最小限にしたい場合**: クラウドAPI・クラウドサービスが優位
- **どちらか一方に絞る必要はなく**、「機密データの下処理・社内文書検索はローカルLLM、それ以外の一般的な作業はクラウドのChatGPT等」という併用も現実的な選択肢

## 実務での使い方

### 導入方法1: Ollama(コマンド操作に抵抗がない場合)

1. [ollama.com/download](https://ollama.com/download)から自社のOS(Windows/Mac/Linux)向けインストーラーをダウンロードし、案内に従ってインストールする
2. インストール後、ターミナル(Windowsは「コマンドプロンプト」または「PowerShell」)を開き、以下のように入力するだけでモデルのダウンロードと起動が同時に行われる(コピペ可)
   ```bash
   ollama run llama3.2
   ```
   初回はモデルのダウンロードに数分〜数十分かかるが、2回目以降はすぐに起動する。プロンプトが表示されたら、そのままチャット感覚で質問を入力できる
3. 他のモデルを試したい場合は、モデル名だけを変えて実行する(例: `ollama run gemma4:e2b`、`ollama run qwen3.8`、`ollama run gpt-oss`、`ollama run muse-glimmer`)
4. 社内システムから呼び出したい場合は、Ollamaが自動で立ち上げるAPI(既定で`http://localhost:11434`)に対して、ChatGPTのAPIとほぼ同じ形式でリクエストを送れる。社内ツールの開発を担当するエンジニアに「Ollama互換API」と伝えれば話が通じる

### 導入方法2: LM Studio(マウス操作で完結させたい場合)

1. [lmstudio.ai](https://lmstudio.ai/)からデスクトップアプリをダウンロード・インストールする(無料)
2. アプリ左側の「Discover」タブでモデル名(例: Gemma、Llama、Qwen)を検索し、自分のPCで動くか(必要なRAM/VRAM)を確認してからダウンロードする
3. 「Chat」タブでChatGPTのような画面が開き、そのまま日本語で質問できる。PDFやWordファイルをドラッグ&ドロップして「この資料の要点をまとめて」のように質問することも可能
4. 社内システムと連携したい場合は「Developer」タブからローカルサーバーを起動すると、OpenAIのAPI形式に互換のエンドポイントが立ち上がり、既存のAI連携ツールをほぼそのまま向け先だけ変えて使える
5. 1台のPC・サーバーを部署内で共有したい場合は「LM Link」機能を使うと、暗号化されたトンネル経由で他の端末からも安全に同じモデルへアクセスできる。個人PCでの検証から小規模なチーム利用へ広げる際の選択肢になる

### 主なオープンウェイトモデルの特徴(2026年8月時点の目安)

自社PC・自社サーバー1〜数台で現実的に動かせる規模のモデルとしては、以下が定番である。

| モデル | 提供元 | ライセンスの目安 | 特徴 |
|---|---|---|---|
| Muse Glimmer | Meta(Meta Superintelligence Labs) | Apache 2.0 | 30Bのマルチモーダル・エージェント特化モデル。単一の民生用GPU(24〜32GB級VRAM)やMac1台で動作する設計で、2026年8月に登場。従来のLlama系より緩いApache 2.0で公開された点が話題になった |
| Llama 4(Scout/Maverick) | Meta | 独自ライセンス(月間利用者7億人超は別途契約要) | Scoutは最大1,000万トークンという長大なコンテキスト(一度に読み込める文章量)が強み。後継の超大型モデル「Behemoth」は2026年8月時点でも重み未公開のまま |
| Gemma 4 | Google | Apache 2.0(商用利用可、ただしGoogleが利用条件を変更する余地あり) | E2B〜31Bの4サイズ展開。軽量〜中規模で省メモリ設計。ノートPC・エッジ端末向けの定番 |
| Mistral(Large 3/Small 4) | Mistral AI(フランス) | Apache 2.0 | Large 3はMoE構造(総675B・実働41B程度)、Small 4は推論・画像理解・コーディング機能を統合した軽量級。80以上の言語に対応 |
| Qwen 3.8(27B)/Qwen 3.6 | Alibaba(中国) | Apache 2.0(上位の超大型モデルQwen 3.8-Maxは独自ライセンス) | 27B前後の密モデルで26万〜100万トークン級の長文脈に対応。日本語含む多言語性能に定評があり、24GB前後のGPUでも動かしやすい |
| gpt-oss(120b/20b) | OpenAI | Apache 2.0 | ChatGPTの主力モデルとは別物のオープンウェイト版。20bは16GBメモリ程度、120bは80GB級GPU1枚で動作する設計。2026年8月時点で仕様に大きな変更はない |
| DeepSeek V4(Flash/Pro) | DeepSeek(中国) | MIT | MoE構造・100万トークン級の長文脈。Flash(実働13B程度)でも個人PCでは重く、Proは実働49B程度でサーバークラスタ前提。詳細は[DeepSeekの基本](../part03-ai-chat-tools/deepseek-basics.md)を参照 |
| NVIDIA Nemotron 3.5 Lightning | NVIDIA | OpenMDW-1.1(重み・学習データ・学習手順まで公開) | MoE構造(総30B・実働3.6B程度)。gpt-oss-120bに匹敵する性能を4分の1程度の規模で実現し、推論速度を重視するエージェントの「実行役」に向く設計。学習データまで含めて公開する珍しく開放的なライセンス |

このほか、GLM-5.2(Zhipu/Z.ai・MITライセンス)やKimi K3(Moonshot・MITベース、オープンウェイトの性能ランキングで2026年8月時点の上位)のような総パラメータ数が数百B〜1Tを超える最先端のオープンウェイトモデルも登場しているが、実運用にはハイエンドGPUを何枚も束ねたサーバー環境が前提になり、自社の一般的なPC・サーバーで手軽に動かす対象ではない。「オープンウェイト=誰でも自社で動かせる」わけではなく、モデルごとに必要なハードウェア規模を確認する必要がある。

日本語特化の選択肢としては、Preferred Networksの「PLaMo」(旗艦モデルのPLaMo 3.0 Primeは重み非公開のAPI提供だが、8Bクラスの小型版はPFN独自の「PLaMo Community License」でHugging Face上に重みが公開されており、個人・中小企業は無償で商用利用できる。大企業が商用利用する場合はPFNへの連絡が必要)、ソフトバンク系のSB Intuitionsによる「Sarashina」(2026年8月時点の現行世代はSarashina3系。mini/nano/guard/embedding/rerankとタスク別に分かれ、日英30兆トークンで事前学習。一部モデルはHugging Face上で重みが公開されているが、商用利用不可のライセンス条件が付くものもある)がある。いずれも日本語の精度を重視する場合の候補になるが、ライセンス条件がモデルごとに異なるため、商用利用前に必ず確認すること。

料金・性能・ライセンス条件は数か月単位で更新されるため、実際の導入判断の際は各社公式サイト・Hugging Face上の最新のモデルカードを必ず確認すること。

### 社内で試すための最初のステップ

いきなり業務システムに組み込むのではなく、まずは情シス部門や有志のPC1台にOllamaまたはLM Studioを入れ、社内文書の要約・議事録の下書きなど機密性の低いタスクで試し、応答品質と必要なPCスペックの感触をつかむところから始めるのが無難である。手応えが得られたら、LM Studioの「LM Link」やOllamaのAPIを使って1台のサーバーを部署内で共有する形に広げ、それでも性能・運用体制が整ってから本格導入を検討するという段階を踏むと失敗が少ない。自社での構築・運用に不安がある場合は、インテックのようにローカルLLM導入支援を提供するSIerに相談する選択肢もある。

## 注意点・よくある誤解

- **同世代のクラウド最大モデルには性能面で見劣りする傾向がある**: 個人・中小企業が用意できる規模のPCで動かせるモデルは、ChatGPTやClaudeの最上位モデルと比べて複雑な推論・専門知識の精度で劣ることが多い。「クラウドを完全に代替する」のではなく「機密データの下処理を担う」用途で考えるのが現実的
- **GPU等のハードウェア投資が必要になりやすい**: 中〜大型のモデルを実用速度で動かすには相応のGPU(グラフィックボード)が必要で、初期投資と電気代がかかる。小型モデルであればノートPCでも動くが、その分性能は限定的というトレードオフがある
- **ライセンス(商用利用の可否)はモデルごとに必ず確認する**: 「オープンウェイト」だからといって無条件に商用利用できるわけではない。上表のとおりモデルによって条件が異なり、特にLlamaのような独自ライセンスは利用者数などの条件で追加契約が必要になる場合があるほか、日本語特化モデルの一部にも商用利用不可のライセンスが付くものがある。導入前にモデルカードのライセンス条項を確認する
- **「オープンウェイト」でも自社で動かせるとは限らない**: GLM-5.2やKimi K3(2026年8月時点のオープンウェイト性能ランキングでも上位)のように総パラメータ数が数百B〜1Tを超えるモデルは、重みが公開されていても実運用にはハイエンドGPUを複数枚束ねたサーバークラスタが必要で、一般的な企業のPC・サーバー1台で動かせる規模ではない。自社導入を検討する際は、まず必要メモリ・GPU台数の実測値を確認する。逆にNVIDIA Nemotron 3.5 Lightningのように「総パラメータ数は数十B級でも実働はごく一部」というMoE設計を活かし、比較的軽い機材でも動かせるよう最適化されたモデルも登場しており、性能表だけでなく実働パラメータ数・推奨機材を必ず確認する
- **AMD製GPUではROCm(AMD純正の計算基盤)の導入状況で挙動が変わる**: 30B級を超えるモデルをAMD GPUで動かす場合、ROCmが入っていないとGPUが使われずCPUのみの動作に切り替わり大幅に遅くなる。LinuxではROCm 7系が安定して動くが、Windowsでは対応状況にばらつきがあるため、AMD環境で本格運用する場合はOS込みで事前検証すること
- **「ローカルだから情報漏洩リスクゼロ」ではない**: 外部のクラウドにデータを送らない点は大きなメリットだが、モデルを動かす端末・サーバー自体の管理(アクセス権限、退職者アカウントの整理、端末の紛失対策等)が甘ければ、別の経路で情報が漏れるリスクは残る。ローカルLLMは対策の一つであって万能ではない
- **運用・保守の手間を過小評価しない**: モデルの入れ替え、アップデート、社内からの問い合わせ対応など、クラウドサービスなら提供元が担ってくれる部分を自社で負うことになる。技術的な保守体制がない場合は、まず小規模な検証から始めるべき

## 最初の一歩

自分のPC(できればメモリ16GB以上)にOllamaかLM Studioのどちらかをインストールし、`ollama run gemma4:e2b`(またはLM StudioのDiscoverタブから軽量モデルを1つ選択)を実行して、機密性のない文章の要約を1つ試してみる。

## 関連トピック

- [DeepSeekの基本](../part03-ai-chat-tools/deepseek-basics.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-08-22: Ollama/LM Studioの最新版、Meta「Muse Glimmer」の登場、ハードウェア選定の目安を最新化
- **内容**: Ollama v0.32.14(TTFT高速化等)、LM Studio v0.4.21系(自律エージェント機能「Bionic」追加)に更新。オープンウェイトモデル表にMetaが新たにApache 2.0で公開した「Muse Glimmer」(30B・マルチモーダル・エージェント特化)とNVIDIA「Nemotron 3.5 Lightning」(総30B・実働3.6B程度のMoE、学習データまで公開するOpenMDW-1.1ライセンス)を追加し、QwenはQwen 3.8-27B(Apache 2.0)を軸に更新。ハードウェア選定の目安を「最低ライン/ちょうどいいライン/大型モデル/AMD GPU利用時の注意」の4段階に整理し、AMD GPUのROCm対応状況に関する注意点を追加。日本語特化モデルをPLaMo Community License(8Bクラスの小型版)・Sarashina3系(mini/nano/guard/embedding/rerank)の現行世代情報に更新
- **出典**: [Ollama Release Notes - Releasebot](https://releasebot.io/updates/ollama)、[LM Studio Bionic for Home Labs in 2026 - runaihome.com](https://runaihome.com/blog/lm-studio-bionic-local-ai-agent-hardware-guide-2026/)、[Muse Glimmer from Meta Superintelligence Labs is now available - Ollama Blog](https://ollama.com/blog/muse-glimmer)、[Meta returns to open source with Muse Glimmer - VentureBeat](https://venturebeat.com/technology/meta-returns-to-open-source-with-muse-glimmer-an-apache-2-0-licensed-30b-parameter-ai-model-optimized-for-agents-available-now)、[NVIDIA AI Releases Nemotron 3.5 Lightning - MarkTechPost](https://www.marktechpost.com/2026/08/11/nvidia-ai-releases-nemotron-3-5-lightning-and-nemo-switchyard/)、[Is Nemotron 3.5 Lightning Free? License and Costs - Layer3labs](https://www.layer3labs.io/guides/is-nemotron-3-5-lightning-free)、[Alibaba's Qwen team releases Qwen 3.8 models with open weights under the Apache 2.0 license - THE DECODER](https://the-decoder.com/alibabas-qwen-team-releases-qwen-3-8-models-with-open-weights-under-the-apache-2-0-license/)、[Alibaba Opens Qwen3.8-27B as Max Model Adds License Limits - eWeek](https://www.eweek.com/news/alibaba-qwen3-8-27b-license-apac-china/)、[Local LLM Hardware Requirements in 2026 - Overchat AI](https://overchat.ai/ai-hub/llm-hardware-requirements)、[Ollama System Requirements 2026 - Local AI Master](https://localaimaster.com/blog/ollama-system-requirements)、[Open Source LLM Leaderboard 2026 - Vellum](https://www.vellum.ai/open-llm-leaderboard)、[PLaMo 2の8Bモデルをオープンなライセンスで公開 - Preferred Networks Tech Blog](https://tech.preferred.jp/ja/blog/plamo-community-license/)、[pfnet/plamo-3-nict-8b-base - Hugging Face](https://huggingface.co/pfnet/plamo-3-nict-8b-base)、[Sarashinaとは?モデル一覧・使い方・ライセンス - issoh.co.jp](https://www.issoh.co.jp/tech/details/11856/)

### 2026-07-24: Ollama/LM Studioの最新版とオープンウェイトモデルの顔ぶれを最新化
- **内容**: Ollama v0.32系(エージェント化したCLI)、LM Studio v0.4系(LM Link・llmsterによるチーム利用対応)に更新。オープンウェイトモデル表をLlama 4 Scout・Gemma 4・Mistral Large 3/Small 4・Qwen 3.6・gpt-oss・DeepSeek V4に更新し、GLM-5.2やKimi K3など総パラメータ数が数百B〜1Tを超える最先端モデルは自社PC・サーバーでは動かしにくい旨を追記。MoE(Mixture of Experts)構造に関する注意点、日本語特化のPLaMo・Sarashinaの動向、インテック等によるオンプレミス生成AI導入支援の国内動向を追加
- **出典**: [Ollama Release Notes - Releasebot](https://releasebot.io/updates/ollama)、[Ollama Latest Version - Local AI Master](https://localaimaster.com/blog/ollama-version-history)、[LM Studio Review 2026 - infobro.ai](https://infobro.ai/reviews/lm-studio-review-2026-the-best-way-to-run-local-llms-on-your-own-hardware)、[LM Studio vs Ollama 2026 - kunalganglani.com](https://www.kunalganglani.com/blog/lm-studio-vs-ollama)、[Open Source LLM Comparison Table 2026 - ComputingForGeeks](https://computingforgeeks.com/open-source-llm-comparison/)、[Qwen 3.6 vs Gemma 4 vs Llama 4 vs GLM-5.1 vs DeepSeek V4 Comparison - Lushbinary](https://lushbinary.com/blog/qwen-3-6-vs-gemma-4-llama-4-glm-5-1-deepseek-v4-open-source-comparison/)、[Introducing gpt-oss - OpenAI](https://openai.com/index/introducing-gpt-oss/)、[Kimi K3 vs DeepSeek V4 Pro vs GLM-5.2 - MarkTechPost](https://www.marktechpost.com/2026/07/18/kimi-k3-vs-deepseek-v4-pro-vs-glm-5-2-open-trillion-scale-moe-models-compared-on-benchmarks-license-and-serving-cost/)、[インテック: オンプレミス環境で生成AIを活用できるローカルLLMの導入支援を開始](https://www.intec.co.jp/news/2026/0129_1.html)、[PLaMo 2.2 Prime リリース - Preferred Networks Tech Blog](https://tech.preferred.jp/ja/blog/plamo-2-2-prime-release/)、[sbintuitions/sarashina-embedding-v2-1b - Hugging Face](https://huggingface.co/sbintuitions/sarashina-embedding-v2-1b)

### 2026-07-06: 初版執筆
- **内容**: ローカルLLMの位置づけ(オープンウェイトモデルを自社機材で動かす方式、データが外部に出ない特徴)、Ollama・LM Studioの使い方、パラメータ数とPCスペックの関係の目安、クラウドAPIとの比較表、Llama/Gemma/Mistral/DeepSeek/Qwen/gpt-ossのライセンス一覧、注意点・最初の一歩を整理
- **出典**: [Ollama公式](https://ollama.com/)、[Ollama Download](https://ollama.com/download)、[Ollama library](https://ollama.com/library)、[GitHub: ollama/ollama](https://github.com/ollama/ollama)、[LM Studio公式](https://lmstudio.ai/)、[LM Studio Docs](https://lmstudio.ai/docs/app)、[Joshua Schultz: Every Open-Weight AI Model Worth Running in 2026](https://joshuaschultz.com/cheatsheets/open-weight-models-2026/)、[codersera: Best Open-Source LLM in May 2026](https://codersera.com/blog/best-open-source-llm-2026-llama-4-qwen-3-5-deepseek-v4-gemma-4-mistral/)、[computingforgeeks: Ollama Models Cheat Sheet 2026](https://computingforgeeks.com/ollama-models-cheat-sheet/)、[zeroka: なぜいまローカルLLMなのか](https://zeroka.jp/column/%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%ABllm%E3%81%AE%E3%83%A1%E3%83%AA%E3%83%83%E3%83%88%E8%B3%87%E7%94%A3%E5%8C%96%E3%81%A8%E3%82%B3%E3%82%B9%E3%83%88%E5%89%8A%E6%B8%9B%E3%81%AE%E5%8A%B9%E6%9E%9C)、[arte: ローカルLLMの必要スペック VRAM・GPU早見](https://arte.itlibra.com/ja/articles/local-llm-hardware-requirements)
