---
title: "プロンプトインジェクションとは何か(仕組みと対策)"
part: 4
chapter: 第2章 攻撃と防御
tags: [プロンプトインジェクション, セキュリティ, AIエージェント, MCP, リスク管理]
created: 2026-07-06
updated: 2026-08-19
---

# プロンプトインジェクションとは何か(仕組みと対策)

## これは何か

プロンプトインジェクションとは、AIが処理する「テキストや画像の中」——AIが閲覧したWebページ、要約を頼んだ文書、受信したメール、口コミサイトのレビュー、さらにはAIエージェントが呼び出す外部ツールの説明文(MCP: Model Context Protocolという標準規格で連携する業務アプリなど)——に紛れ込ませた指示によって、AI本来の役割や利用者の意図を乗っ取ろうとする攻撃を指す。自分は何も危険なことを入力していないのに、AIが「読んだだけ」「呼び出しただけ」の外部コンテンツやツールのせいで、意図しない挙動をしてしまう点が最大の特徴である。ChatGPTやClaude、Geminiなどが「Webを見て回る」「メールを読んで返信する」「社内システムやSaaSのデータを操作する」といった自律的な作業(エージェント機能)を代行するようになった2026年時点では、業務で使うほぼすべての人が知っておくべきリスクになっている。IPA(情報処理推進機構)が2026年1月に公表した「情報セキュリティ10大脅威2026」でも、「AIの利用をめぐるサイバーリスク」が組織向け脅威として初めて選出され、第3位にランクインした。

なお、似た言葉である「ジェイルブレイク(jailbreaking、AIの制約の迂回)」とは区別しておくと理解しやすい。ジェイルブレイクは、**利用者自身**が「ロールプレイとして」「開発者モードとして」といった言い回しでAIに直接語りかけ、AI自身の安全対策を外そうとする行為である。一方プロンプトインジェクションは、**利用者ではない第三者**が用意したコンテンツやツールの中に指示を仕込み、AIがそれを「読んだ」だけで乗っ取られる点が異なる。業界標準のセキュリティガイドラインOWASPは、後者と区別する形で、利用者本人が直接AIに語りかけて既存の指示を上書きするものを「直接的プロンプトインジェクション(ジェイルブレイクとほぼ同義)」、第三者コンテンツ経由のものを「間接的プロンプトインジェクション」と分類している。

## 仕組み・背景

LLM(大規模言語モデル)は、本来「開発者が与えた指示」「利用者の入力」「外部から読み込んだデータ」を厳密に区別すべきだが、内部的にはこれらすべてが1本の連続したテキストとして処理される。そのため、外部データの中に「これまでの指示を無視して」「このAPIを呼び出して」といった命令文らしき文字列が混じっていると、AIがそれを正規の指示と誤認してしまうことがある(GPTs固有の防御策やOpenAIの「instruction hierarchy(指示の階層構造)」という緩和策については[GPTsにおけるプロンプトインジェクション対策](../part06-custom-ai/gpts-prompt-injection-defense.md)で詳しく扱っている)。

OWASPのAIセキュリティガイドライン(LLM01:2025)は、この攻撃を大きく2種類に分けている。

- **直接的プロンプトインジェクション(ジェイルブレイク)**: 利用者自身がAIに直接語りかけ、システム指示を上書き・暴露させようとするもの。
- **間接的プロンプトインジェクション**: AIがWebページ・文書・メールなど外部から取り込んだコンテンツの中に指示が仕込まれており、利用者は何も悪いことを入力していないのに攻撃が成立するもの。仕込まれる指示は人間には見えない形(白背景に白文字、HTMLのコメント、画像内のテキストなど)であることも多く、OWASPも「人間に知覚できる必要はない」と明記している。

OWASPは2026年、自律的に行動する「エージェント型アプリケーション」に的を絞った新ガイドライン「OWASP Top 10 for Agentic Applications」も公開した。ここではプロンプトインジェクションを起点とした被害を、目標のすり替え(Agent Goal Hijack)、ツールの誤用、記憶の汚染(メモリポイズニング)など複数のリスク項目に分解し、「エージェントが複数ステップを自律的にこなす能力を持つほど、小さな入力の乗っ取りがシステム全体の侵害・データ持ち出し・金銭的損失に連鎖しやすい」と警告している。OWASPが2026年6月に公表した実態調査でも、プロンプトインジェクションが依然としてエージェント型AIの実運用における最大の失敗原因になっていると報告されている。

セキュリティ研究者Simon Willisonは、間接的プロンプトインジェクションが実害につながる条件を「悪の三要素(lethal trifecta)」として整理している。AIエージェントが次の3つを**同時に**持つと、攻撃者は特別な脆弱性を突かなくても機密情報を盗み出せてしまう。

1. **機密データへのアクセス**(社内文書、メール、顧客情報など)
2. **信頼できない外部コンテンツへの接触**(第三者が書いたWebページ、メール、レビュー、連携先ツールのデータなど)
3. **外部へ情報を送る手段**(メール送信、API呼び出し、ファイルアップロード、Web閲覧履歴の送信など)

この3つのうち2つまでなら被害は限定的だが、3つが揃うと「悪意あるコンテンツを読んだだけで機密情報が外部に送信される」といった攻撃が成立する。AIエージェント(目標だけを渡せば自律的に複数ステップの作業をやり切るAIシステム。詳しくは[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md))がWeb閲覧・メール処理・ファイル操作・外部ツール呼び出しを人間の確認なしに任されるようになるほど、この3要素が同時に揃う場面が構造的に増えていく。

2026年に入ってからは、この構図が理論ではなく現実の被害として繰り返し確認されている。

- **エージェントが呼び出す「ツール」自体が汚染される**: AIエージェントが外部サービスと連携する標準規格MCPでは、ツールの説明文(AIが「このツールは何をするものか」を理解するために読む自然文)に悪意ある指示を仕込む「ツール中毒(tool poisoning)」が知られている。2025年9月には、メール送信サービスPostmark向けのMCPサーバーを装ったnpmパッケージ「postmark-mcp」が、正規版として15回ほど更新を重ねた後にこっそり改変され、送信されるメール内容をBCCで攻撃者のドメインへ転送するコードが追加されていたことが発覚した。発覚までに実在する約300組織が影響を受けたとみられる。
- **2026年1月、5日間で立て続けに起きた実例**: 生成AI企業各社の業務エージェント製品で、短期間に複数の実被害が報告された。Anthropicの汎用エージェント「Claude Cowork」は公開からわずか2日後、セキュリティ企業PromptArmorにより、人間には見えない「1ポイントの白文字」で指示を仕込んだWord文書1つで、社会保障番号の一部を含む金融文書を攻撃者のAnthropicアカウントへアップロードさせる攻撃を実演された。同時期には、メールAIアシスタント「Superhuman」で受信メールに仕込まれた指示が要約作業を乗っ取り、受信箱内の別の機密メール(金融・法務・医療情報を含む)を攻撃者のGoogleフォームへ送信してしまう事例や、Notion AIが偽装した履歴書PDF経由で給与・採用データを持ち出される事例も確認され、IBM Bobを含め合計4件の実運用エクスプロイトが5日間で報告された。
- **Webサイトに埋め込まれた攻撃コードの実観測**: Palo Alto NetworksのUnit 42は2026年3月、実際にインターネット上で稼働しているWebサイトを調査し、それを閲覧しただけのAIエージェントに対して、Stripe決済の実行・データベースの削除・詐欺広告の承認などを行わせる攻撃コードが少なくとも22種類、実在のサイトに隠されているのを発見した。攻撃のうち14.2%はデータ破壊、9.5%はAIによるコンテンツモデレーションの回避を狙ったものだった。
- **一クリックだけで成立する攻撃**: 2026年1月には、Microsoft 365 Copilotの正規リンクを1回クリックしただけで、ユーザーとの対話なしにパーソナル情報が持ち出される「Reprompt」攻撃も報告された(Microsoftは2026年1月に修正済み)。

こうした一連の出来事は、2025年6月に発覚したMicrosoft 365 Copilotの「EchoLeak」(CVE-2025-32711、悪意あるメールをCopilotが検索・参照しただけで機密情報が持ち出されるゼロクリック脆弱性)以降、間接的プロンプトインジェクションが「起こりうる仮説」から「日常的に観測される攻撃」へと位置づけを変えたことを示している。

2026年7月には、従来の防御をすり抜ける新しい攻撃手法「Agent Data Injection(ADI、エージェントのデータ注入)」が韓国・米国の研究チームから報告された。これまでの間接的プロンプトインジェクション対策の多くは「命令文らしき指示」をフィルタリングする発想だったが、ADIは攻撃者の入力を送信者名やボタンのID、JSON形式の区切り記号(`{`や`}`など)といった「AIがもともと信頼しているデータ」に見せかけることで、命令文というフィルターをすり抜けてAIのデータ解釈そのものを狂わせる。研究チームは、Webブラウザ操作エージェント(Claude in Chrome、Google Antigravity、Nanobrowser)に対する意図しないクリックの誘発や、コーディングエージェント(Claude Code、Codex、Gemini CLI)に対する任意コード実行・サプライチェーン攻撃を実際に成立させたと報告しており、エージェント専用に作られた防御策に対しても最大50%程度の高い成功率を示した(従来型の素朴な命令注入はほぼ完全にブロックされたのと対照的)。「命令文っぽい文字列を弾けば防げる」という単純な対策では追いつかない段階に入っていることを示す事例である。

## 使いどころ・使い分け

「使うか使わないか」ではなく、「今使っているAIツールが、どれだけ危険な組み合わせを持っているか」を見極めることが実務的な判断になる。前述の悪の三要素を判断基準にすると次のように整理できる。

| AIツールの使い方 | 機密データ接続 | 信頼できない外部コンテンツへの接触 | 外部への送信・実行手段 | リスク |
|---|---|---|---|---|
| 単発の文章作成・アイデア出し(ファイル添付なし) | なし | なし | なし | 低い |
| 社内文書やPDFの要約(自分でアップロードした信頼できる資料のみ) | ややあり | なし(自分が選んだ資料のみ) | なし | 低い |
| Web検索・ブラウジング機能を使って調べ物をする | 状況次第 | **あり**(検索結果・閲覧先ページは誰が書いたか分からない) | 基本的になし(閲覧のみ) | 中程度 |
| メール・カレンダー・社内システムに接続したAIアシスタント | **あり** | **あり**(受信メールは第三者が自由に書ける) | 状況次第 | 高い(あと1つ揃うと危険) |
| MCP経由で外部ツール・SaaSに接続したエージェント | **あり** | **あり**(連携先ツールの説明文・データも信頼できるとは限らない) | **あり**(ツール呼び出しがそのまま実行になる) | 非常に高い |
| ブラウザ操作・メール送信・決済・ファイルアップロードなどを自律的に実行するエージェント機能(Claude Cowork、ChatGPTのエージェント機能など) | **あり** | **あり** | **あり** | 非常に高い |

判断基準はシンプルで、「このAIが、①機密データを持っていて、②第三者が書いた文章や連携先ツールのデータを読み、③その結果を外部に送ったり何かを実行できるなら」、悪意あるコンテンツを1つ読む・1つのツールを呼び出すだけで実害が出る状態にあると考えてよい。3つ目の「実行できる」がなければ、最悪の場合でも情報が漏れるだけで済むことが多く、リスクの深刻度は一段下がる。MCP経由でツールを追加する場合は、そのツール自体が(postmark-mcpのように)後からこっそり悪性化する供給網リスクも加わる点に注意したい。

## 実務での使い方

開発者でなくても、次のチェックと問いかけはすぐに実践できる。

### 1. 「エージェント機能」を有効にする前に権限を絞る

- ブラウジング・メール連携・MCP経由のツール接続・自動実行などの機能は、業務上本当に必要な範囲だけをオンにする(最小権限)。「使えたら便利そうだから」という理由だけで、メール送信や決済、ファイルアップロードまでできる権限を渡さない。
- 送金・送信・削除・購買・ファイルアップロードなど「後から取り消せない操作」をAIエージェントに任せる場合は、実行前に必ず人間の確認(承認ボタンを押す、内容を確認してから送信するなど)が入る設定になっているかを確認する。
- 接続するMCPサーバーや外部ツールは、素性の分かる提供元のものだけを「許可リスト」に登録して使う。有名サービス名を騙ったMCPサーバーが後から悪性化した例(postmark-mcp)があるため、「便利そうだから」で見知らぬ提供元のMCPサーバーを追加しない。

### 2. 主要ツールが用意している防御機能を確認する

| ツール | 確認すべき設定・防御機能 |
|---|---|
| ChatGPT(エージェント機能) | 2025年10月に登場した専用ブラウザアプリ「Atlas」は予告通り2026年8月9日に提供終了し、機能は刷新された「ChatGPT Work」デスクトップアプリとChrome拡張機能に統合された(Chat・Work・Codexが1つのアプリにまとまり、複数タブ・パスワード管理・パスキー対応などブラウザとしての基本機能も新アプリ側に引き継がれている)。設定の「セキュリティ」から確認できる「Lockdown Mode(ロックダウンモード)」や、エージェントが「高リスク」と判断した操作への警告ラベルは統合後も維持されている。OpenAIは強化学習でAI自身に攻撃者役を演じさせる自動レッドチームを使い、防御モデルを継続的に鍛えている |
| Claude(Computer use / Claude in Chrome / Claude Cowork) | ブラウザ拡張機能やCowork利用時のサイトごとの権限設定、購入・送信・ファイルアップロードなど特定操作の前の確認プロンプトを有効にしておく。Anthropicは2026年に入りシステムカードで攻撃成功率を数値付きで公開しており、最新モデルでも「非常に強い」単発攻撃で数%、同じ攻撃を10回・100回と試行されると成功率が数十%まで上がるとされる。もっとも公表数値を鵜呑みにはできない。Claude Chrome拡張機能では2025年12月に報告された「ShadowPrompt」(悪意あるWebページを閲覧しただけでClaudeを乗っ取れるゼロクリックの脆弱性連鎖)が2026年2月〜3月にパッチされたはずが、2026年7月時点でも別の研究者により類似の回避手口が再現されており、「対策済み=ゼロ」ではない前提で権限設計をする必要がある |
| Microsoft 365 Copilot / MCP連携アプリ全般 | 管理者はMicrosoft Purviewのデータ損失防止(DLP)ポリシーやXPIA(Cross-Prompt Injection Attempt)対策に加え、Microsoft Entra Agent IDでエージェントに非人間IDを割り当て、Defender for CloudでMCPツールの応答を監視する体制が用意されている。追加するMCPサーバーは許可リスト方式にし、レビューされていないサードパーティ製サーバーを安易に追加しない |
| Gemini / Google Workspace | Google Workspace管理コンソールでGeminiの層状防御(閲覧できるドメインを絞る仕組み、外部コンテンツにタグ付けして信頼できない入力と区別する仕組み、不審な指示を検知する分類器など)の適用状況を確認する。Googleはこの多層防御を継続的に強化していると説明している |

### 3. 社内IT・ベンダーに聞くべき質問

自分で設定を追いきれない場合は、情シスや導入ベンダーに次を確認するとよい。

- 「このAIエージェントは最小権限で動いているか(必要な機能・ツールだけが有効か)」
- 「送信・決済・削除・ファイルアップロードなど取り消せない操作の前に、人間の承認ステップが必須になっているか」
- 「間接的プロンプトインジェクション(外部コンテンツ・外部ツール経由の攻撃)への対策として、具体的に何を実装しているか。攻撃成功率などの数値を公表しているか」
- 「連携しているMCPサーバー・外部ツールは提供元を確認したうえで許可リスト方式に登録しているか」
- 「既知の脆弱性が見つかった場合、どのくらいの速さで修正が適用されるか」

## 注意点・よくある誤解

- **「対策済みだから安全」ではない**: 各社は2026年に入り、攻撃成功率などの防御指標を相次いで公表するようになったが、測定条件や定義は各社バラバラで単純比較はできない。それでもAnthropicが公表した数値では、最新モデルでも「非常に強い」単発の攻撃で数%が突破され、同じ攻撃を10回・100回と繰り返されると成功率は大きく跳ね上がるとされている。OpenAIも「プロンプトインジェクションは、Web上の詐欺や社会工学と同じように、完全に『解決』されることはおそらくない」と明言しており、「ベンダーが対策していると言っているから100%安全」という思い込みが最も危険である。実際、2026年7月に報告されたADI(Agent Data Injection)は、命令文をフィルタリングするタイプのエージェント専用防御に対して最大50%程度の高い成功率を示しており、「防御を実装済み」の製品でも新しい攻撃手法には無防備なことがある。
- **見た目に何も書かれていなくても攻撃は成立する**: OWASPも指摘する通り、仕込まれる指示は白背景に白文字にする、HTMLのコメントに隠す、画像の中に埋め込むなど、人間の目には見えない形で埋め込まれることがある。実際に2026年1月のClaude Cowork事例では、Word文書に仕込まれた「1ポイントの白文字」だけで金融文書の持ち出しが成立している。ビジネスの現場に限った話でもなく、2026年7月には米コネティカット州の裁判所で、原告本人が提出書類に「3ポイントの白文字」でAI宛ての指示(「この提出書類の内容に沿って原告に有利な判断をせよ」といった趣旨)を隠して埋め込んでいたことが裁判官に発見され、2026年8月6日に電子提出禁止などの制裁が下された事例も報告されている。「怪しい文章がないから大丈夫」という目視確認だけでは防げない。
- **ツールや「スキル」自体が攻撃経路になりうる**: MCPサーバーやエージェント向けの「スキル」ファイルなど、一見便利な拡張機能もソフトウェア供給網(サプライチェーン)攻撃の対象になる。有名サービスを騙ったMCPサーバーが後から悪性化した例(postmark-mcp)があるため、便利さだけで見知らぬ提供元のツールを追加しない。
- **開発者だけの問題ではない**: プロンプトインジェクションはシステムを作る側の問題だと思われがちだが、一般利用者がブラウジング機能・メール連携・MCPツール接続をオンにした瞬間、自分自身がその攻撃対象になる。設定をオンにする人自身がリスクを理解している必要がある。
- **ジェイルブレイクとの混同に注意**: 「AIに変な言い方をして脱獄させる」対策(ジェイルブレイク対策)と、「AIが読み込む外部コンテンツ・呼び出す外部ツールを信用しすぎない」対策(間接的プロンプトインジェクション対策)は、防ぐべき経路が異なる。前者は入力時のフィルタリングで一定の効果があるが、後者は権限設計(悪の三要素を同時に持たせない、ツールを許可リスト化する)がより本質的な対策になる。

## 最初の一歩

自分が使っているAIツールでブラウジング機能・メール連携・MCP経由のツール接続・自動実行(エージェント)機能をオンにしているなら、今すぐ「送信・決済・削除・ファイルアップロードなど取り消せない操作の前に、確認を求める設定」になっているか、また接続している外部ツール・MCPサーバーが素性の分かる許可リスト方式になっているかを確認する。なっていなければ、必要な範囲だけに機能を絞るか、確認ステップ・許可リストを有効化する。

## 関連トピック

- [生成AI利用における情報漏洩対策](information-leakage-prevention.md)
- [GPTsにおけるプロンプトインジェクション対策](../part06-custom-ai/gpts-prompt-injection-defense.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)

## 更新履歴

### 2026-08-19: 新型攻撃ADI・裁判所での実例・ChatGPT Atlas終了後の状況を反映
- **内容**: 命令文フィルタ型の防御をすり抜ける新攻撃手法「Agent Data Injection(ADI)」(Claude in Chrome・Antigravity・Nanobrowser等のブラウザ操作エージェント、Claude Code・Codex・Gemini CLI等のコーディングエージェントで実証、防御突破率最大50%、2026年7月報告)を「仕組み・背景」に追加。米コネティカット州の裁判所で原告が提出書類に3ポイントの白文字でAI宛て指示を隠していた事例(2026年8月6日に制裁)を「見た目に見えない攻撃」の新しい実例として追加。Claude Chrome拡張機能の脆弱性連鎖「ShadowPrompt」(2025年12月報告、2026年2〜3月パッチ後も7月に回避手口が再現)を反映し、「対策済み=安全」ではない実例を強化。予告通り完了したChatGPT Atlas終了(2026年8月9日、ChatGPT Work新デスクトップアプリ・Chrome拡張機能への統合)を反映
- **出典**: [The Hacker News: New Agent Data Injection Attack Can Make AI Agents Misclick or Run Attacker Commands](https://thehackernews.com/2026/07/new-agent-data-injection-attack-can.html)、[arXiv: Agent Data Injection Attacks are Realistic Threats to AI Agents](https://arxiv.org/abs/2607.05120)、[GitHub: compsec-snu/adi](https://github.com/compsec-snu/adi)、[Newsweek: First Known Hidden AI Directive in Court Filing Raises 'Massive' Concern](https://www.newsweek.com/first-known-hidden-ai-directive-in-court-filing-raises-massive-concern-12325434)、[404 Media: Person Hides Prompt Injection in Legal Filing Telling AI to Side With Them](https://www.404media.co/person-hides-prompt-injection-in-legal-filing-telling-ai-to-side-with-them/)、[BetaNews: Man sanctioned for hiding AI prompts in court filing](https://betanews.com/article/man-sanctioned-hiding-ai-prompts-court-filing/)、[SOCRadar: ShadowPrompt: Zero-Click Prompt Injection Chain in Anthropic's Claude Chrome Extension](https://socradar.io/blog/shadowprompt-zero-click-anthropics-claude/)、[The Hacker News: Claude Extension Flaw Enabled Zero-Click XSS Prompt Injection via Any Website](https://thehackernews.com/2026/03/claude-extension-flaw-enabled-zero.html)、[TechRadar: Claude's Chrome extension still has hidden security gaps](https://www.techradar.com/pro/the-bypass-is-still-six-lines-of-javascript-security-experts-warn-that-claude-for-chrome-browser-extension-could-be-hijacked-despite-it-alerting-anthropic-several-times-that-something-was-wrong)、[Koi: ShadowPrompt: How Any Website Could Have Hijacked Claude's Chrome Extension](https://www.koi.ai/blog/shadowprompt-how-any-website-could-have-hijacked-anthropic-claude-chrome-extension)、[OpenAI Help Center: ブラウザベースのエージェント型作業に向けた Atlas から ChatGPT への進化](https://help.openai.com/ja-jp/articles/20001371-%E3%83%96%E3%83%A9%E3%82%A6%E3%82%B6%E3%83%99%E3%83%BC%E3%82%B9%E3%81%AE%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E5%9E%8B%E4%BD%9C%E6%A5%AD%E3%81%AB%E5%90%91%E3%81%91%E3%81%9F-atlas-%E3%81%8B%E3%82%89-chatgpt-%E3%81%B8%E3%81%AE%E9%80%B2%E5%8C%96)、[Ledge.ai: OpenAI、AIブラウザ「ChatGPT Atlas」を8月9日に終了](https://ledge.ai/articles/openai_chatgpt_atlas_shutdown_desktop_browser)

### 2026-07-22: エージェント・MCP時代の攻撃実例と各社の最新防御を反映
- **内容**: OWASP Top 10 for Agentic Applications(2026)の追加、MCP経由のツール中毒(postmark-mcp)、2026年1月に5日間で立て続けに起きたClaude Cowork/Superhuman/Notion AI/IBM Bobでの実際の情報持ち出し事例、Unit 42によるWebサイト上の間接的プロンプトインジェクションの実観測(2026年3月)、Microsoft Copilotの「Reprompt」攻撃、Anthropicの攻撃成功率の公表状況、OpenAIのChatGPT Atlas終了(2026年8月9日)とエージェント機能のChatGPT本体への統合、IPA「情報セキュリティ10大脅威2026」でのAIリスク初選出などを反映し、実務での使い方・注意点をMCP/エージェント中心に更新
- **出典**: [NeuralTrust: A Deep Dive into the OWASP Top 10 for Agentic Applications 2026](https://neuraltrust.ai/blog/owasp-top-10-for-agentic-applications-2026)、[Help Net Security: Prompt injection still drives most agentic AI security failures in production](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)、[The Hacker News: First Malicious MCP Server Found Stealing Emails in Rogue Postmark-MCP Package](https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html)、[Snyk: Malicious MCP Server on npm postmark-mcp Harvests Emails](https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/)、[Microsoft Security Blog: Securing AI agents: When AI tools move from reading to acting](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/)、[PromptArmor: Claude Cowork Exfiltrates Files](https://www.promptarmor.com/resources/claude-cowork-exfiltrates-files)、[the-decoder: Claude Cowork hit with file-stealing prompt injection days after Anthropic's launch](https://the-decoder.com/claude-cowork-hit-with-file-stealing-prompt-injection-days-after-anthropics-launch/)、[Breached.Company: The Lethal Trifecta Strikes: Four Major AI Agent Vulnerabilities in Five Days](https://breached.company/the-lethal-trifecta-strikes-four-major-ai-agent-vulnerabilities-in-five-days/)、[Unit 42: Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/)、[The Hacker News: Researchers Reveal Reprompt Attack Allowing Single-Click Data Exfiltration From Microsoft Copilot](https://thehackernews.com/2026/01/researchers-reveal-reprompt-attack.html)、[VentureBeat: Prompt injection disclosures: 4 labs compared](https://venturebeat.com/security/anthropic-browser-agent-hijacked-31-percent-before-safeguards-engaged)、[the-decoder: Claude Opus 4.5 resists prompt injections better than rivals but still falls to strong attacks alarmingly often](https://the-decoder.com/claude-opus-4-5-resists-prompt-injections-better-than-rivals-but-still-falls-to-strong-attacks-alarmingly-often/)、[OpenAI Help Center: Evolving Atlas into ChatGPT for browser-based agentic work](https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work)、[IPA: 情報セキュリティ10大脅威2026](https://www.ipa.go.jp/security/10threats/10threats2026.html)

### 2026-07-06: 初版執筆
- **内容**: プロンプトインジェクションの定義とジェイルブレイクとの違い、直接的/間接的プロンプトインジェクションの区別、Simon Willisonの「悪の三要素(lethal trifecta)」によるリスク判断基準、EchoLeak(Microsoft 365 Copilot)の実例、ChatGPT・Claude・Copilot・Geminiの防御機能と設定確認ポイントを整理
- **出典**: [OWASP Gen AI Security Project: LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)、[Simon Willison: The lethal trifecta for AI agents](https://simonwillison.net/2025/Jun/16/the-lethal-trifecta/)、[Sentra: EchoLeak (CVE-2025-32711) prompt injection](https://sentra.io/blog/copilot-echoleak-prompt-injection)、[arXiv: EchoLeak: The First Real-World Zero-Click Prompt Injection Exploit](https://arxiv.org/html/2509.10540v1)、[TechCrunch: OpenAI says AI browsers may always be vulnerable to prompt injection attacks](https://techcrunch.com/2025/12/22/openai-says-ai-browsers-may-always-be-vulnerable-to-prompt-injection-attacks/)、[OpenAI: Continuously hardening ChatGPT Atlas against prompt injection attacks](https://openai.com/index/hardening-atlas-against-prompt-injection/)、[OpenAI: Introducing Lockdown Mode and Elevated Risk labels in ChatGPT](https://openai.com/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/)、[VentureBeat: Anthropic's browser agent got hijacked 31.5% of the time before safeguards engaged](https://venturebeat.com/security/anthropic-browser-agent-hijacked-31-percent-before-safeguards-engaged)、[Google Workspace Help: Indirect prompt injections & Google's layered defense strategy for Gemini](https://knowledge.workspace.google.com/admin/security/indirect-prompt-injections-and-googles-layered-defense-strategy-for-gemini)
