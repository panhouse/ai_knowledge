---
title: "Cursorの基本(AIコードエディタ)"
part: 8
chapter: 第2章 コーディング支援AI
tags: [Cursor, AIコードエディタ, コーディング支援AI, Anysphere, 開発生産性]
created: 2026-07-06
updated: 2026-08-14
---

# Cursorの基本(AIコードエディタ)

## これは何か

Cursor(カーソル)は、Anysphere社が開発する「AIを使うために作られたコードエディタ」である。定番エディタVisual Studio Code(VS Code)を土台に、AIによる自動補完・対話・自律編集を最初から編集画面の中心に据えて作り直した点が特徴で、2025〜2026年にかけてエンジニア個人・スタートアップから大企業まで急速に採用が広がった。年間経常収益(ARR)は2025年1月の約1億ドルから2026年6月には約40億ドルに達し、生成AIコーディングツールの中で最大級の存在になっている。

非エンジニアの決裁者にとっての困りごとは、「社内のエンジニアが口を揃えて名前を挙げるCursorが、既存のGitHub Copilotと何が違い、いくらかかり、契約する価値があるのか判断できない」ことだ。本ページはコードが書けなくても、Cursorの立ち位置・料金・導入判断がわかることを目的にする(GitHub Copilotそのものの説明は[GitHub Copilotの基本(コーディング支援AI)](github-copilot-basics.md)を参照)。

## 仕組み・背景

### 「後付け拡張機能」ではなく「AI専用エディタ」

GitHub Copilotは既存のVS CodeやJetBrains系IDE(統合開発環境)に拡張機能として組み込む方式だが、CursorはVS Code自体をフォーク(コードを複製して独自開発を続けること)して作られた**独立したエディタ本体**である。そのため、AIが提案するコードの差分表示・複数ファイルの一括編集・エディタ全体の文脈把握といった体験を、拡張機能の制約を受けずに設計できる。VS Codeの拡張機能・キーバインド(キー割り当て)・設定はそのまま使えるため、乗り換えの学習コストは小さい。

なお2026年3月からは、Cursorのエージェント機能を「Agent Client Protocol(ACP)」という業界共通規格経由でJetBrains系IDE(IntelliJ IDEA・PyCharm・WebStormなど)からも呼び出せるようになった。ただしこれはチャット形式のエージェント連携に限られ、Tab補完やコンテキストメニューなど独立エディタ版の全機能が使えるわけではない点に注意が必要である。

### 主要機能

- **Tab(タブ補完)**: コードを書いていると次の1行〜複数ファイルにわたる編集案をグレー字で提案し、Tabキーで確定する。単純な次コード予測だけでなく、あるファイルの変更に応じて別ファイルの修正案も提示する「複数ファイル横断の予測」に強みがある
- **Chat(チャット)**: エディタ右側のパネルでAIと対話し、コードの説明・バグ調査・実装方針の相談ができる。ショートカットは既定で `Cmd/Ctrl + L`
- **Agent(エージェントモード)**: 「このAPIを使うログイン機能を実装して」のような大きな指示を出すと、AIが複数ファイルの作成・編集、ターミナルコマンドの実行、エラー時の自己修正までを自律的にループさせる。人間は都度の細かい指示ではなく最終レビューに専念できる
- **Composer(コンポーザー)**: 自然言語の指示をリポジトリ全体にわたる協調的な編集に変換する機能。2026年5月には自社モデルの最新版「Composer 2.5」が投入され、長時間の連続作業・複雑な指示への追従性が大きく向上した
- **Background Agent / Cloud Agent(バックグラウンド・クラウドエージェント)**: 作業をローカルPCから切り離し、クラウド上でAIに長時間タスクを進めさせる機能。人間が席を離れている間にGitHubのIssue(課題チケット)がドラフトのプルリクエスト(コード変更の提出物)になっている、という使い方ができる
- **Automations(オートメーション)**: Slack・Linear・GitHub・PagerDuty・Webhook(外部システムからの通知)などのイベントをトリガーに、常時稼働のエージェントを定義した指示に基づいて自律実行する機能
- **Rules(ルール)/ Skills**: `.cursor/rules/` 配下にプロジェクトごとのコーディング規約やAIの振る舞いをファイルとして定義し、バージョン管理(Gitでの履歴管理)できる仕組み。加えて再利用可能な作業手順を `SKILL.md` という形式でまとめ、チャットから呼び出す「Skills」機能も整備が進んでいる
- **MCP対応**: Model Context Protocol(AIと外部ツール・データベースをつなぐ共通規格)に対応し、社内DBや監視ツールなどへの接続を一度設定すれば使い回せる
- **インエディタのコードレビュー**: Agentが生成した差分を、人間のレビュアーの代わりに一次チェックする機能も追加され、レビュー負荷の軽減を狙う方向に機能拡張が続いている
- **Cursor for iOS(モバイルアプリ)**: 2026年6月にパブリックベータで登場したiPhone/iPad向けアプリ。外出先からクラウド上のエージェントを起動・監視でき、作業完了時にプッシュ通知を受け取り、差分やスクリーンショットをスマホ上でレビューしてプルリクエストをマージできる。全ての有料プラン(後述のStart/Pro/Pro+/Ultra/Teams/Enterprise)で利用可能
- **Cursor Router(Autoモードのルーティング基盤)**: 2026年7月下旬に投入された仕組みで、Autoモードを「Intelligence(最高品質優先)」「Balance(品質とコストの均衡)」「Cost(コスト優先)」の3方式から選べるようになった。指示内容・コンテキスト・タスクの複雑さ・分野を判定し、単純な修正は安価なモデルへ、複雑な設計判断はフロンティアモデルへ自動で振り分ける

### 使えるAIモデル

Cursorは自社モデルに縛らない「マルチモデル」方式を採り、2026年8月時点で選択可能なモデルは40種類以上にのぼる。主要ベンダーの内訳は、OpenAI(GPT-5.5、GPT-5.3 Codexなど)・Anthropic Claude(2026年6月末投入の「Claude Sonnet 5」、2026年7月24日投入の「Claude Opus 5」、最上位の「Claude Fable 5」など)・Google Gemini(Gemini 3.1 Pro、Gemini 3.5 Flashなど)・xAI Grok(Grok 4.5に加え、2026年8月12日から1週間限定で50%割引が付いた「Grok 4.6」)で、これらをタスクに応じて選択できるほか、OpenAI互換のエンドポイントを持ち込む「Custom Models」機能もある。Claude Opus 5はAnthropicの主力Fable 5に近い性能をおよそ半額で出すモデルとして投入され、後述のCursor Routerの自動振り分け先にも追加されている。

加えて自社開発のモデルとして、コード補完に特化した高速モデル「Fusion」(Tabを支える)と、エージェント的な大規模編集に特化したモデル「Composer」を持つ。現行の「Composer 2.5」は中国Moonshot AI社のオープンモデル「Kimi K2.5」系列をベースに大規模な追加学習を施したモデルで、コーディングのベンチマーク(SWE-Bench Multilingual)でClaude Opus 4.7とほぼ同水準(79.8%前後)のスコアを出しながら、トークン単価は標準ティアで入力100万トークンあたり0.50ドル・出力100万トークンあたり2.50ドルと、フロンティアモデルの1/10程度に抑えられている。2026年6月16日の自社イベント「Compile」では、SpaceXの計算基盤(Colossusスーパークラスタ)でゼロから事前学習する次世代モデル「Composer 3」(パラメータ数1.5兆規模、コードネーム「Vega」)が予告されたが、2026年8月14日時点では未公開で、正式リリース時期も未確定である。

何も指定しない「Auto」モードを選ぶと、2026年7月下旬に投入された「Cursor Router」がタスクの内容・複雑さに応じて適切なモデルを自動選択する(詳細は前節)。どのモデルが最新かは変化が速く、価格変動や短期の値引きキャンペーンも頻繁にあるため、契約前に必ず公式ドキュメント(docs.cursor.com/models)で確認することが望ましい。

### 会社の背景(2026年8月時点)

Cursorを開発するAnysphere社は2022年にMIT(マサチューセッツ工科大学)出身の4人によって設立され、2023年3月に製品を公開した。2025年に入って成長が急加速し、ARRは2025年1月の約1億ドルから2025年11月に10億ドル、2026年2月に20億ドル、2026年6月には約40億ドル(うちエンタープライズ向けが約26億ドル)に達したと報じられている。

2026年6月16日には、IPO(株式公開)直後のSpaceX社がAnysphereを**株式交換で600億ドル規模で買収する**と発表した。買収の背景には、SpaceXの傘下にあるxAI社が持つ大規模計算基盤(Colossusスーパークラスタ)をCursorに提供し、逆にCursorが持つ大量のコーディングデータをxAIのGrokモデルの学習に活用するという狙いがあるとされる。発表直後にはSpaceX株が急落し評価額に懐疑的な反応も出たが、2026年8月14日時点でもこの買収は**規制当局の承認待ちで完了しておらず**、SpaceXは2026年8月上旬に規制手続きの一環としてS-1(米国での株式公開登録)関連の開示手続きを進めた段階にとどまる。契約にはSpaceX側の事情で買収を完了できなかった場合の100億ドルの違約金、規制上の理由で完了できなかった場合の40億ドルの解約金が定められており、買収完了は引き続き2026年第3四半期を見込む。この間もCursor自体のモデルラインアップ・料金・運営体制に目立った変化は起きていないが、2026年8月11日にはxAIが発表した常時稼働型エージェントアプリ「Grok Bot」がCursor Ultra・Teams Premiumプランへのバンドル提供を開始しており(詳細は次節)、買収発表前には見られなかったxAIとの統合が製品面でも進み始めている。

## 使いどころ・使い分け

### そもそも導入すべきか

| 状況 | 判断の目安 |
|---|---|
| ゼロから新しいアプリ・プロトタイプを高速に作りたい(いわゆる「vibe coding」) | Cursorの得意領域。ComposerやAgentで骨格を素早く作れる |
| 既存の大規模コードベースを少人数で保守している | Agent Modeが有効だが、レビュー体制なしでは品質劣化のリスクがある |
| 社内のIDEをVS Code系に統一している/統一してよい | Cursorへの移行コストが小さく導入しやすい |
| JetBrains系IDE(IntelliJ IDEA等)を主に使っている | 2026年3月以降はACP経由でCursorのエージェントチャットを呼び出せるが、Tab補完など全機能は使えない。全機能を求めるならGitHub CopilotのAgent modeの方が対応が広い |
| 会社としてGitHub本体(Issue・PR管理)との統合を重視する | GitHub Copilot coding agentの方がGitHubとの統合が深い |
| コストを最小化し、使うAIモデルも自分で選びたい開発者中心 | Cline(オープンソース・BYOM)が候補になる |
| ターミナル中心の開発フロー・最高水準の自律コーディング精度を優先する | Claude Codeとの併用・比較が候補になる(SWE-bench Verifiedで高スコアという評価が多い) |
| セキュリティ・監査要件が厳しい(金融・官公庁等) | Business/Enterpriseのプライバシーモード・SOC 2認証を確認してから判断 |

### 競合ツールとの違い

| ツール | 提供元 | 位置づけ | 特徴 |
|---|---|---|---|
| Cursor | Anysphere(2026年6月にSpaceXが買収発表、完了は2026年Q3予定・未完了) | AI専用に作られた独立エディタ(VS Codeから派生) | エディタ全体がAI前提。Tab補完・Composer・Agentの完成度が高く、個人開発者・スタートアップからの評価が高い。複数モデルを選択可、Autoモードは2026年7月末からCursor Routerが自動最適化。2026年3月からJetBrainsでもエージェントチャットのみ利用可、2026年6月からiOSアプリでも操作可 |
| GitHub Copilot | GitHub(Microsoft) | 既存IDEへの後付け拡張機能 | GitHub本体(Issue・PR)との統合が深い。対応IDEが幅広く、企業のガバナンス機能が豊富。詳細は[GitHub Copilotの基本](github-copilot-basics.md) |
| Claude Code | Anthropic | ターミナル/CLI中心のエージェント型ツール | IDEに縛られずターミナル・VS Code拡張・JetBrains拡張から使える。自律的なコーディング精度の評価が高く、Cursorと役割分担で併用する開発者も多い |
| Windsurf(現Devin Desktop) | Cognition(2025年にWindsurfを買収、2026年6月にDevin Desktopへ改称) | AI専用の独立エディタ+自律エージェント「Devin」 | 2026年4月にDevinを統合したWindsurf 2.0を投入後、2026年6月に製品名を「Devin Desktop」へ完全移行。ローカルの補完エージェント「Cascade」は2026年7月1日に終了し、後継の「Devin Local」に置き換わった |
| Cline | オープンソースコミュニティ | VS Code/JetBrains拡張機能(OSS) | 拡張機能自体は無料で、AIモデルは自分のAPIキーで接続するBYOM(Bring Your Own Model)方式。コストを使った分だけに抑えたい開発者や、モデル選定の自由度を重視する層に向く |

いずれも「自律的に複数ファイルを編集するAgent」を持つ点は共通しており、差は「専用エディタか既存IDEへの拡張か」「自社モデルか複数モデル選択か」「GitHubとの統合の深さ」「料金体系(サブスクリプションか従量課金か)」にある。2026年の開発者調査では、複数のツールをタスクに応じて併用しているという回答も多く、どれか一つに絞る必要は必ずしもない。

## 実務での使い方

### 料金プラン(個人向け、2026年8月時点)

| プラン | 月額 | Tab補完 | Agent・Chat | 特徴 |
|---|---|---|---|---|
| Hobby(無料) | 0ドル | 制限あり | 制限あり(Agentリクエスト少数) | クレジットカード不要。エディタ全体を試せるが日常利用には心許ない |
| Pro | 20ドル | 実質無制限 | 20ドル相当のクレジットプール+Auto(自動モデル選択)は無制限 | 個人の業務利用の標準ライン。frontier(最先端)モデル・MCP・Cloud Agentも利用可 |
| Pro+ | 60ドル | 実質無制限 | Proの3倍のクレジット | クレジットを使い切りやすい重度利用者向け |
| Ultra | 200ドル | 実質無制限 | Proの20倍のクレジット | 最先端モデルでAgentを常時動かすような超重度利用者向け。新機能への優先アクセスあり。2026年8月11日からxAIの常時稼働エージェントアプリ「Grok Bot」(専用のクラウド仮想マシンを持つエージェント)がバンドルされている |

年払いにすると各プランおおむね20%程度安くなる。Auto(モデルを自動選択するモード)は使い放題だが、Claude・GPTなど特定のモデルを指名すると、プランに含まれるクレジットが消費される仕組みになっている。

なお2026年7月28日には、インド市場限定の最安プラン「Cursor Start」(月額649ルピー、約7ドル)が投入された。常時稼働のCloud Agent・iOSアプリ・MCP/hooks/skills対応など基本機能は使えるが、モデルは自社のGrok 4.5・Composer 2.5に固定され、Pro以上に含まれるOpenAI・Anthropicのフロンティアモデルは含まれない。地域限定のため日本からの契約対象ではないが、Cursorが低価格帯にも裾野を広げ始めた動きとして留意しておきたい。

### 料金プラン(組織向け、2026年8月時点)

| プラン | 月額(1人あたり) | 特徴 |
|---|---|---|
| Teams(Business)標準席 | 40ドル(月払い)/32ドル(年払い) | 一元請求、SSO(シングルサインオン)、管理者向けの利用状況ダッシュボード |
| Teams(Business)Premium席 | 120ドル(月払い)/96ドル(年払い) | 標準席の5倍の利用量枠。Agentを多用する重度利用者を1か月フルに使い切れる想定で2026年7月1日から契約更新分に順次適用開始。2026年8月11日からはUltraと同じくGrok Botもバンドルされる |
| Enterprise | 要問い合わせ | SAML SSO・SOC 2 Type IIの文書提出・SCIMによる一括アカウント管理・利用状況追跡API・専用サポートなど、監査・統制要件が厳しい組織向け |

2026年6月の改定で、各Teams席の利用枠が「Composer・Auto(自社モデル)用」と「サードパーティAPIモデル(Claude・GPT・Geminiなど)用」の2つのプールに分離され、管理者は利用状況をダッシュボードでリアルタイムに把握できるようになった。Business以上のプランでは「プライバシーモード」が既定で強制され、送信したコードをモデル学習に使わせない・処理終了後は保持しないという契約上・技術上の制御が入る。Cursor自体はSOC 2 Type II準拠のAWSインフラ上で稼働している。価格・利用枠は変更頻度が高いため、契約前に必ず公式ページ(cursor.com/pricing)で最新値を確認すること。

### 導入判断のポイント(非エンジニアの管理職向け)

- **「誰が」「どのタスクに」使うかで効果が大きく変わる**: 新規プロトタイプや個人プロジェクトでの評価は非常に高いが、既存の大規模・複雑なコードベースでは「AIが生成したコードのレビュー負荷が増える」という声も多い。全社一律導入の前に、少人数のパイロット導入で効果を測ることが望ましい
- **エンジニアの個人裁量での導入が先行しやすい**: 会社としてGitHub Copilotを契約していても、エンジニアが自分の判断でCursorを併用しているケースは多い。管理職としては「なぜそのツールを追加で使っているか」を一度聞いてみると、現場の実態(コードベースの種類・タスクの性質)がつかみやすい
- **買収の動向を注視するが、慌てて契約方針を変えない**: 2026年6月にSpaceXによる買収が発表されたが、2026年8月14日時点でも規制当局の承認待ちで未完了であり、Cursorの料金体系そのものは発表前と変わっていない。一方でGrok Bot(xAI製の常時稼働エージェント)のUltra/Teams Premiumへのバンドルなど、xAIとの製品面の統合は既に始まっている。長期契約や大規模導入を検討する場合は、買収完了(2026年第3四半期予定)後の公式発表を確認してから最終判断するのが安全
- **セキュリティ・ライセンス面の確認**: AIが生成したコードのレビューを省略しない運用を前提にすること、また学習データに起因するライセンスリスクへの対応(IP補償の有無)は、GitHub Copilotと同様にBusiness/Enterprise契約時の確認事項になる

## 注意点・よくある誤解

- **「Cursor=VS Codeの見た目を変えただけ」ではない**: 見た目こそVS Codeに近いが、AIが編集の主体になれるよう内部設計から作られており、拡張機能で後付けした場合とは補完・Agentの体験の質が異なる
- **料金の「クレジット」制度は理解しておく**: Auto(自動モデル選択)は使い放題だが、特定の高性能モデルを指名するとプランのクレジットが減る。重度利用者ほど「思っていたより早くクレジットが尽きる」という声が多く、Pro+・Ultraへの見極めが必要
- **無料のHobbyプランは評価用と考える**: Tab補完・Agentリクエストとも制限が厳しく、日常的な業務利用には向かない
- **会社としての一括契約を検討する場合はTeams/Businessから**: 個人のPro契約を複数人が使う運用は、監査ログやSSOがなく統制が効かないため推奨されない
- **「JetBrainsでも使える」は部分的な話**: 2026年3月以降JetBrains系IDEからCursorのエージェントをACP経由で呼び出せるが、これはチャットのAI連携が中心で、Tab補完やインラインの提案機能は使えない。フル機能を求める場合は独立エディタ版のCursorか、JetBrainsネイティブのAI機能・Copilotとの比較が必要
- **買収発表は完了前の情報である点に注意**: 2026年6月時点で買収は「発表・規制承認待ち」段階であり、2026年8月14日現在も完了していない(SpaceXは2026年8月上旬に規制手続きを進めた段階)。ニュースだけで契約方針を急に変える必要はない
- **モデルの型番は入れ替わりが速い**: Claude・GPT・Gemini・Grokとも数か月単位で新型番(例: Claude Sonnet 5・Opus 5、Grok 4.5/4.6)が入れ替わり、旧モデルは順次利用不可になっていく。社内マニュアルにモデル名を固定で書くのではなく「Autoモード(Cursor Router)を既定にする」運用にしておくと更新の手間が減る

## 最初の一歩

まずはHobby(無料)プランでインストールし、社内エンジニアに「使っているエディタと同じ規模のタスクをCursorのAgentモードで試してもらい、体感を1分で共有してもらう」ことから始めるとよい。

## 関連トピック

- [GitHub Copilotの基本(コーディング支援AI)](github-copilot-basics.md)
- [Windsurf(Devin Desktop)の基本](windsurf-basics.md)
- [Clineの基本](cline-basics.md)
- [ローカルLLMの基本(自社PC・サーバーで動かす生成AI)](local-llm-basics.md)
- [MCP(Model Context Protocol)の基本](../part09-api-development/mcp-basics.md)

## 更新履歴

### 2026-08-14: モデル世代交代・Cursor Router・iOSアプリ・Grok Bot・買収動向を最新化
- **内容**: AnthropicのClaude Sonnet 5(2026年6月末)・Claude Opus 5(2026年7月24日)・最上位Claude Fable 5への世代交代、xAI Grok 4.6の投入(2026年8月12日から1週間の50%割引)、Autoモードを支える新基盤「Cursor Router」(Intelligence/Balance/Costの3方式、2026年7月下旬投入)、公開ベータのモバイルアプリ「Cursor for iOS」、インド限定の廉価プラン「Cursor Start」(月額649ルピー、2026年7月28日投入)、xAIの常時稼働エージェント「Grok Bot」のUltra/Teams Premiumへのバンドル(2026年8月11日)、次世代自社モデル「Composer 3」(コードネームVega、1.5兆パラメータ、Compileで予告済み・未リリース)、SpaceXによるAnysphere買収が2026年8月14日時点でも規制承認待ちで未完了である現状(違約金・解約金の規模含む)を追記して全体を最新化
- **出典**: [Anthropic launches Claude Sonnet 5 as a cheaper way to run agents - TechCrunch](https://techcrunch.com/2026/06/30/anthropic-launches-claude-sonnet-5-as-a-cheaper-way-to-run-agents/), [Anthropic releases new model, Opus 5 - Axios](https://www.axios.com/2026/07/24/anthropic-releases-new-model-opus-5), [Anthropic releases Claude Opus 5 - Fortune](https://fortune.com/2026/07/24/anthropic-debuts-claude-opus-5-with-feature-that-lets-users-toggle-between-cost-and-capability/), [How Cursor Router chooses the right model for the task - Cursor Blog](https://cursor.com/blog/how-cursor-router-works), [Cursor Router - Cursor Changelog](https://cursor.com/changelog/router), [Cursor Router Updates Auto Intelligence and Auto Balance - AI Catchup](https://aicatchup.com/news/cursor-router-auto-intelligence-balance), [Cursor Mobile App for iOS - Cursor Changelog](https://cursor.com/changelog/ios-mobile-app), [Build from anywhere with Cursor for iOS - Cursor Blog](https://cursor.com/blog/ios-mobile-app), [Cursor Debuts ₹649 India Plan as AI Price Battle Heats Up - SQ Magazine](https://sqmagazine.co.uk/cursor-launches-india-only-plan/), [Introducing Grok Bot - x.ai](https://x.ai/news/introducing-grok-bot), [SpaceXAI's Grok Bot turns agents into persistent digital coworkers - VentureBeat](https://venturebeat.com/orchestration/spacexais-grok-bot-turns-agents-into-persistent-digital-coworkers-that-can-operate-your-apps-for-120-per-month), [Cursor Composer 3 Leaks: What We Know - Memeburn](https://memeburn.com/cursor-composer-3-leaks-what-we-know/), [Cursor Drops Composer 3, a 1.5T-Parameter Model Trained on SpaceX's Supercomputer - AlphaSignal](https://alphasignal.ai/news/cursor-drops-composer-3-a-1-5t-parameter-model-trained-on-spacex-s-supercomputer), [SpaceX Finalizes Regulatory Procedures to Close $60 Billion Acquisition of AI Platform Cursor - SatNews](https://satnews.com/2026/08/12/spacex-finalizes-regulatory-procedures-to-close-60-billion-acquisition-of-ai-platform-cursor/), [Cursor AI Models: Benchmarks & Pricing (August 2026) - BenchLM.ai](https://benchlm.ai/providers/cursor)

### 2026-07-23: 料金・モデル・買収動向・JetBrains対応を最新化
- **内容**: Composer 2.5(Kimi K2.5系列ベース)への刷新と価格・ベンチマーク、2026年6月改定のTeams料金(標準席/Premium席・利用枠の2プール化)、ACP経由のJetBrains対応(2026年3月・機能限定である点)、SpaceXによるAnysphere買収が2026年7月23日時点でも規制承認待ちで未完了である現状、ARRの成長推移(2026年6月時点で約40億ドル)、Windsurfの「Devin Desktop」への改称、Claude Codeとの比較を追記して全体を最新化
- **出典**: [Cursor Pricing July 2026: Free, Pro, Ultra and Teams Costs - NxCode](https://www.nxcode.io/resources/news/cursor-ai-pricing-plans-guide-2026), [Cursor Teams Upgrades Pricing for Predictability - StartupHub.ai](https://www.startuphub.ai/ai-news/technology/2026/cursor-teams-upgrades-pricing-for-predictability), [Cursor Teams Splits Usage Pools, Adds Premium Seat July 1 2026 - SONNET CODE](https://www.sonnetcode.com/blog/cursor-teams-composer-25-premium-seat-july-2026), [Cursor Composer 2.5: third on the Coding Agent Index and ~10-60x lower cost than rivals - Artificial Analysis](https://artificialanalysis.ai/articles/cursor-composer-2-5-coding-agent-index), [Cursor bets on cheaper coding with Composer 2.5 and Kimi K2.5 - The New Stack](https://thenewstack.io/cursor-composer-benchmarks/), [Cursor AI Models: Complete Guide 2026 - TechJack Solutions](https://techjacksolutions.com/ai-tools/cursor/cursor-models/), [Cursor Joined the ACP Registry and Is Now Live in Your JetBrains IDE - The JetBrains Blog](https://blog.jetbrains.com/ai/2026/03/cursor-joined-the-acp-registry-and-is-now-live-in-your-jetbrains-ide/), [CursorJ Plugin for JetBrains IDEs - JetBrains Marketplace](https://plugins.jetbrains.com/plugin/30583-cursorj), [SpaceX to acquire the AI coding startup Cursor for $60 billion - CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html), [SpaceX Cursor Acquisition: Deal Status, Timeline, Developer Impact - KyenAI](https://www.kyenai.com/articles/spacex-cursor-acquisition-2026), [Cursor by Anysphere Revenue 2026: $4B Est. ARR - Latka](https://getlatka.com/companies/cursor.com), [Windsurf Is Now Devin Desktop: What Users Should Do - Digital Applied](https://www.digitalapplied.com/blog/windsurf-becomes-devin-desktop-ide-migration-2026), [Cursor vs Claude Code vs GitHub Copilot 2026: The Ultimate Comparison - NxCode](https://www.nxcode.io/resources/news/cursor-vs-claude-code-vs-github-copilot-2026-ultimate-comparison), [Cursor Enterprise Security: SOC 2, Admin Policy, Self-Host Reality (2026) - vibe-eval.com](https://vibe-eval.com/ai-security/cursor-enterprise-security/)

### 2026-07-06: 初版執筆
- **内容**: CursorのTab補完・Chat・Agent・Composer・Background Agent・Automations等の主要機能、複数モデル対応と自社モデル(Fusion・Composer)、2026年6月時点の個人向け・組織向け料金プラン、GitHub Copilot・Windsurf・Cline との比較、2026年6月に発表されたSpaceXによる買収の動向、非エンジニア向けの導入判断ポイントをまとめた初版を執筆
- **出典**: [Cursor Pricing 2026: All 6 Plans - No Code MBA](https://www.nocode.mba/articles/cursor-pricing), [Improvements to Teams Pricing - Cursor Blog](https://cursor.com/blog/teams-pricing-june-2026), [Cursor AI Models: Complete Guide 2026 - TechJack Solutions](https://techjacksolutions.com/ai-tools/cursor/cursor-models/), [Cursor (company) - Wikipedia](https://en.wikipedia.org/wiki/Cursor_(company)), [SpaceX to acquire the AI coding startup Cursor for $60 billion - CNBC](https://www.cnbc.com/2026/06/16/spacex-spcx-cursor-acquisition-ipo.html), [SpaceX to acquire Cursor for $60B in stock - TechCrunch](https://techcrunch.com/2026/06/16/spacex-to-acquire-cursor-for-60b-in-stock-days-after-blockbuster-ipo/), [Windsurf Pricing In 2026 - CloudZero](https://www.cloudzero.com/blog/windsurf-pricing/), [Cognition's acquisition of Windsurf - Cognition Blog](https://cognition.com/blog/windsurf), [Cline Pricing 2026 - CostBench](https://costbench.com/software/ai-coding-assistants/cline/)
