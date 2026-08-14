---
title: プロンプトの基本構成要素
part: 5
chapter: 第1章 基本原則
tags: [プロンプトエンジニアリング, RACE, CO-STAR, PTCF, カスタム指示]
created: 2026-07-04
updated: 2026-08-09
---

# プロンプトの基本構成要素

## これは何か

「いい感じにまとめて」と一言だけ入力しても、生成AIは的外れな回答を返しがちである。これは指示が曖昧だからで、プロンプト(AIへの指示文)を「役割・背景・タスク・出力形式」のような決まった型に沿って組み立てるだけで、同じAIでも出力の質は大きく変わる。この型を知らないと、毎回運任せの一問一答を繰り返すことになる。

## 仕組み・背景

プロンプトエンジニアリングには数多くのフレームワークがあるが、突き詰めると以下の要素の組み合わせに過ぎない。

1. **役割(Role/Persona)**: AIに何者として振る舞ってほしいか
2. **目的・タスク(Objective/Task)**: 何をしてほしいか(具体的な動詞で)
3. **背景・文脈(Context)**: なぜそれが必要か、前提条件は何か
4. **入力データ**: 処理してほしい元データ
5. **出力形式(Format)**: どんな形式・分量で出してほしいか
6. **制約条件・トーン**: 守ってほしいルール、文体
7. **例示(Examples)**: 望む出力に近いお手本

代表的なフレームワークは、これらの要素をどこまで絞り込むかの違いでしかない。

- **RTF(Role, Task, Format)**: 役割・タスク・出力形式の3要素だけのシンプル版。日常的な指示の大半はこれで十分。
- **RACE(Role, Action, Context, Expectation)**: 役割・行動・背景・期待する結果の4要素。RTFより一段複雑なタスクに向く。
- **CO-STAR(Context, Objective, Style, Tone, Audience, Response)**: 背景・目的・文体・トーン・想定読者・出力形式の6要素。シンガポール政府機関(GovTech)のプロンプトエンジニアリング大会で優勝した手法として知られ、2026年時点でも複雑な文章生成タスク向けの定番フレームワークとして頻繁に引用される。「文体」と「想定読者」を分けているのが特徴で、「わかりやすく書いて」のような曖昧な指示を具体化しやすい。
- **PTCF(Persona, Task, Context, Format)**: 役割・タスク・背景・出力形式の4要素。Googleが公式のGemini/Workspaceプロンプトガイドで推奨しているフレームワークで、考え方はRACEやRTFとほぼ同じだが「Context」に予算・締切・想定読者などの制約条件をまとめて入れる点が特徴。

これらに加えてRISEN・CRAFT・CARE・TAGなど類似の頭字語フレームワークがプロンプト系メディアで次々に提唱されているが、2026年8月時点でもRTF・RACE・CO-STAR・PTCFの位置づけ(シンプル版・業務文書向け・全要素網羅版・Google公式)が実務での標準的な参照先であることに変わりはない。新しい頭字語が増えても中身は本節冒頭に挙げた7要素の並べ替えに過ぎないため、丸暗記よりも「今回どの要素が足りていないか」で考える方が実務的である。

OpenAI・Anthropic・Googleの各社も公式ドキュメントで共通して次のコツを挙げている(2026年8月時点でも変わらず有効)。

- **明確・直接的に書く**: 「文脈を知らない新入社員に指示する」つもりで、曖昧な形容詞(「かなり」「いい感じに」)を避け、具体的な語数・条件で指定する。Anthropicは「最小限の前提知識しかない同僚にそのプロンプトを見せて、迷わず実行できるか」を判定基準として挙げている。
- **区切り記号で構造化する**: `"""`やMarkdown見出し、`<context>`のようなXMLタグで「指示」と「参照データ」を分離すると、AIが取り違えにくくなる。最新モデルは構造がなくても文意を汲み取る精度が上がっているが、指示・背景・複数の参照データが混在する複雑なプロンプトでは引き続き有効な手法とされる。
- **例示(few-shot)を入れる**: 出力形式やトーンを制御する最も確実な方法。3〜5個程度、エッジケースを含む多様な例を用意するとよい。
- **長い参照データは先に、指示は後に置く**: 長文の資料を読み込ませる場合、資料本体を先頭に、質問や指示を末尾に置くと精度が上がりやすい(Anthropicの検証では、特に複数文書を扱う複雑なタスクで応答品質が最大30%向上したという報告もある)。
- **禁止形より肯定形で指示する**: 「マークダウンを使うな」より「滑らかな文章の段落で構成してください」のように、してほしいことを肯定形で書く方が効きやすい。

### 2026年の変化: 「ステップバイステップで考えて」は必須ではなくなった

以前は「順を追って考えてください」といったChain of Thought(思考の連鎖)を促す一言が回答精度を大きく左右した。しかし2026年時点の主要な推論(reasoning)モデル — ChatGPTの「Thinking」モード、Claudeの拡張思考・adaptive thinking、Geminiの「Deep Think」など — は、複雑な問いに対して指示がなくても内部で自動的に段階的思考を行う。これらのモードでは「ステップバイステップで」と重ねて指示しても効果が薄く、むしろ冗長な出力を招くことがある。ステップバイステップ指示が今も有効なのは、決まったフォーマットへのデータ抽出など「手順の厳密な再現性」が求められるタスクに限られる。

## 使いどころ・使い分け

| 状況 | 向いているフレームワーク |
|---|---|
| ちょっとした文章の手直し・簡単な依頼 | RTF(役割・タスク・出力形式だけ) |
| 業務メールや資料のドラフト作成 | RACE(背景と期待する結果まで書く) |
| 記事構成案・企画書など、読み手や文体まで揃えたい | CO-STAR(全要素を使う) |
| Gemini・Google Workspace(Gmail・ドキュメント等)での指示 | PTCF(Googleが公式に推奨) |
| 何度も使い回すテンプレートを作りたい | カスタム指示・システムプロンプトとして役割や制約を固定化 |
| 込み入った推論や複雑な計算をさせたい | フレームワークの型より、AIの「思考(Thinking/Deep Think)」モードを有効にする方が効果的な場合が多い |

要素を全部使う必要はない。CO-STARの6要素でも、まずはContext(背景)・Objective(目的)・Response(出力形式)の3つだけで精度は大きく上がり、そこにStyle・Tone・Audienceを段階的に足していくのが実務的な進め方。

## 実務での使い方

### コピペで使えるテンプレート例1: RACE(業務メール・資料作成向け)

```
あなたは[役割: 例 "10年の実務経験を持つ広報担当者"]です。

【背景・文脈】
[状況を2〜3行で: 例 "先月納品したWebサイトについて、クライアントから軽微な
デザイン修正依頼が来た。契約上は追加費用が発生する範囲だが、関係を悪化させたくない"]

【タスク】
[具体的な行動を動詞で指示: 例 "追加費用が発生することを角を立てずに伝え、
見積もりを提示するメール文面を作成してください"]

【制約条件】
- 文字数: [例: 300文字以内]
- トーン: [例: 丁寧だが毅然とした、ビジネスメールらしい敬語]
- 含めるべき要素: [例: 件名、修正内容の確認、見積金額の提示、次のアクション]

【出力形式】
[例: 件名と本文を分けて、そのままメールに貼り付けられる形式で出力してください]
```

### コピペで使えるテンプレート例2: CO-STAR(企画・構成案向け)

```
# Context(背景)
[誰のために、どんな状況で書くか]

# Objective(目的)
[このプロンプトで達成したいこと]

# Style(文体)
[例: 専門用語は使うが必ず一言説明を付ける]

# Tone(トーン)
[例: 先輩が親身にアドバイスするような距離感]

# Audience(対象読者)
[例: フリーランス1年目、確定申告の初心者]

# Response(出力形式)
[例: H2見出し5〜7本のMarkdown構成案]
```

### コピペで使えるテンプレート例3: PTCF(Gemini・Google Workspace向け)

```
# Persona(役割)
[例: "Google スプレッドシートの数式に詳しい業務効率化コンサルタント"として]

# Task(タスク)
[例: "下記の売上データから、店舗別・月別の前年比を自動計算する数式を提案してください"]

# Context(背景・制約)
[例: "スプレッドシートはA列に店舗名、B列に日付、C列に売上金額が入っている。
関数はSUMIFSとQUERYのみ使用可、マクロは使わない"]

# Format(出力形式)
[例: "数式そのものと、各引数が何を指しているかの一言解説をセットで出力してください"]
```

### ツール横断の対応付け(2026年8月時点)

プロンプトの「役割・背景・制約」を毎回書くのが面倒な場合は、各ツールの「固定の指示」機能に登録しておくと、以後のやり取りに自動的に反映される。ChatGPT・Claude・Geminiはいずれも「アカウント全体に効く指示」と「特定の用途だけに効く指示」の2階層構造を持つ点が共通している。

| ツール | 機能名 | 設定場所 | 備考 |
|---|---|---|---|
| ChatGPT(全体) | カスタム指示(パーソナライズ機能の一部) | プロフィールアイコン→設定→パーソナライズ→カスタム指示欄(要「カスタマイズを有効にする」トグルON。モバイルは「ChatGPTをカスタマイズ」から) | 「自分について」「回答方法」の2項目。文字数上限はFree/Goプランが各1,500字、Plus/Pro/Business/Enterprise/Educationプランは2026年7月15日のアップデートで各5,000字(従来の3倍)に拡大。「パーソナリティ」プリセットやMemory(記憶)機能と3層で重なる |
| ChatGPT(プロジェクト単位) | プロジェクトの「指示」 | 特定プロジェクト内でのみ有効な指示を個別設定 | カスタム指示より優先度が高い |
| Claude(全体) | プロフィールの指示(Instructions for Claude) | 左下のアカウントアイコン→設定→General→Profile欄の「Instructions for Claude」 | アカウント全体に効く。好みの文体・頻出用語などを記述。加えて「Styles」機能で回答トーン(Normal/Learning/Concise/Explanatory/Formalなど)を会話ごとに切り替え可能 |
| Claude(プロジェクト単位) | プロジェクトの指示(Project instructions) | 「Projects」→「+ New Project」でプロジェクト作成→プロジェクト内の指示欄に入力・保存 | プロフィールの指示が先に適用され、その上にプロジェクト指示が重なる。参照ファイルは「プロジェクトの知識」欄にアップロード可能。無料プランでもProjectsは利用可(上限あり)、企業向けは権限管理も可能 |
| Gemini(Gem) | Gem(カスタムGem) | 左メニュー「Gem」(旧「Explore Gems」)→「New Gem」→名前・指示・(任意で)Knowledgeファイルを設定→保存 | 特定用途に特化したAIを作る機能。ChatGPTのカスタムGPTsに相当。無料アカウントでも作成・利用可能 |
| Gemini(全体) | Saved Info(保存された情報) | メニュー→設定と機能→Personal Intelligence(2026年1月に旧「パーソナルコンテキスト」から改称)→Memory・Saved Infoのトグルを確認 | アカウント全体の好み・プロフィール情報を記憶させる機能。Memoryのトグルと「アクティビティの保存」の両方がONである必要がある |
| Microsoft 365 Copilot | カスタム指示(Custom instructions) | Copilotアプリ右上「その他のオプション」→チャットの設定→左メニュー「パーソナライズ」→「カスタム指示」タイル→「指示を編集」 | 組織アカウント(Microsoft 365 Copilotライセンス)向け。回答の形式・トーン・詳細度などの好みを保存でき、トグルでON/OFF可能。GitHub Copilotは別機能で、リポジトリ内の`.github/copilot-instructions.md`に指示を置く方式 |

## 注意点・よくある誤解

- **要素を全部詰め込めばよいわけではない**: 情報過多なプロンプトはかえってAIを混乱させる。まずは3要素(役割・タスク・出力形式)で試し、精度が足りない部分だけ背景や例示を足す方が効率的。
- **「ステップバイステップで考えて」は今は逆効果になることがある**: 前述の通り、推論モードを搭載した最新モデルは指示がなくても内部で段階的に考える。冗長な出力を避けたい通常の対話では、まず指示なしで試し、精度が足りない場合だけステップ指定を足す方がよい。
- **禁止形より肯定形で指示する**: 「マークダウンを使うな」より「滑らかな文章の段落で構成してください」のように、してほしいことを肯定形で書く方が効きやすいとされる。
- **指示の「理由」を添えると守られやすい**: 「三点リーダーを使うな」だけでなく「音声で読み上げるため三点リーダーは避けて」のように理由を添えると、AIが意図を汎化して守りやすくなる。
- **カスタム指示・Project instructionsは文字数上限がある**: ChatGPTのカスタム指示は最大でも各項目5,000字(無料プランは1,500字)。長大な社内マニュアルをそのまま貼り付けようとせず、要点だけに絞るか、Claudeの「プロジェクトの知識」やGeminiのファイル添付など、ファイルを直接読み込ませる機能と使い分ける。
- **業務ツールの「カスタム指示」は組織アカウント前提のものがある**: Microsoft 365 Copilotのカスタム指示は組織のCopilotライセンスに紐づく設定で、個人用のCopilot(旧Bing Chat相当)とは設定場所・挙動が異なる。GitHub Copilotの指示ファイル(`.github/copilot-instructions.md`)ともまったく別物なので、「Copilotのカスタム指示」と聞いたらどの製品の話かをまず確認する。

## 最初の一歩

直近でAIに頼んだ依頼を1つ思い出し、RTF(役割・タスク・出力形式)の3行に分解して書き直し、同じ依頼を投げ直して結果を比べてみる。

## 関連トピック

- [Zero-shot・Few-shotプロンプティング](zero-shot-and-few-shot-prompting.md)
- (今後、Chain of Thoughtなど入門〜応用手法のページを追加予定)

## 更新履歴

### 2026-08-09: ツール横断の対応表にMicrosoft 365 Copilotを追加し、Claude・Geminiの設定場所を最新化
- **内容**: Claudeの「プロフィールの指示(Instructions for Claude)」の設定場所とStyles機能、Geminiの「Saved Info」がPersonal Intelligence(2026年1月に旧パーソナルコンテキストから改称)配下に移った点、Microsoft 365 Copilotのカスタム指示(パーソナライズ→カスタム指示タイル)の設定手順を追加。RISEN・CRAFTなど類似フレームワークが増えてもRTF/RACE/CO-STAR/PTCFの位置づけは2026年8月時点でも変わっていない旨を明記
- **出典**: [OpenAI Help Center: ChatGPT Custom Instructions](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions)、[Claude Help Center: Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)、[Claude Help Center: How can I create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)、[Google Gemini Apps Help: Use Gems in Gemini Apps](https://support.google.com/gemini/answer/15146780)、[Microsoft Support: Customize how Microsoft 365 Copilot responds to you](https://support.microsoft.com/en-us/microsoft-365-copilot/customize-how-microsoft-365-copilot-responds-to-you)

### 2026-07-21: 2026年時点の最新情報に更新
- **内容**: Googleが公式に推奨するPTCF(Persona, Task, Context, Format)フレームワークを追加。推論モードを搭載した最新モデルでは「ステップバイステップで考えて」という指示が不要・逆効果になりうる点を追記。ChatGPTカスタム指示の設定場所・文字数上限(プラン別)、Claude Projectsの手順、Gemini Gemが無料プランに開放された点など、ツール横断の対応表を最新化
- **出典**: [Anthropic Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)、[Google Workspace公式ブログ「5 ways to write better AI prompts for Gemini」](https://blog.google/products-and-platforms/products/workspace/google-gemini-workspace-ai-prompt-tips/)、[OpenAI Help Center: ChatGPT Custom Instructions](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions)、[Anthropic Support: How can I create and manage projects](https://support.anthropic.com/en/articles/9519177-how-can-i-create-and-manage-projects)

### 2026-07-04: 初版執筆
- **内容**: プロンプトの基本構成要素、RTF/RACE/CO-STARなど代表フレームワークの整理、OpenAI/Anthropic/Google公式のベストプラクティス、コピペ用テンプレート、各ツールのカスタム指示設定場所をまとめた
- **出典**: [Anthropic Claude Docs](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)、[OpenAI Help Center](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)、[Google AI for Developers](https://ai.google.dev/gemini-api/docs/prompting-strategies)、[プロンプトや CO-STARガイド](https://prompt-ya.com/co-star/)、[Promptrace RACEフレームワーク解説](https://promptrace.ai/prompt-engineering-guide/race-framework)
