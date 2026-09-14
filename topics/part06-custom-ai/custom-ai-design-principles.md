---
title: "カスタムAIの基礎(共通設計原則)"
part: 6
chapter: 第1章 カスタムAIの基礎
tags: [GPTs, Gem, Claude Projects, Copilot Agent Builder, カスタムAI, システムプロンプト, ガバナンス]
created: 2026-07-06
updated: 2026-09-07
---

# カスタムAIの基礎(共通設計原則)

## これは何か

GPTs(ChatGPT)、Gem(Gemini)、Projects(Claude)、Agent Builder(Microsoft 365 Copilot)は、いずれも「指示」と「参照資料」をあらかじめ設定しておき、以降はワンクリックで同じ役割のAIを呼び出せるようにする機能である。名前も画面もツールごとにバラバラだが、中身の設計原則はほぼ共通している。本ページは特定ツールの操作手順ではなく、**どのツールを使う場合にも通用する「良いカスタムAIの作り方」の考え方**を扱う。個別ツールの画面操作・料金・上限値は、それぞれの各論ページ([GPTsの作り方と公開設定](gpts-creation-basics.md)、[Gemの基本](gemini-gem-feature.md)、[Claude Projectsの基本](claude-projects-basics.md))を参照してほしい。

これがないと、「指示文には何でも詰め込めばよい」「とりあえず作ってみたが誰も使わない」「気づいたら社内に似たようなbotが10個も乱立していた」といった失敗を、ツールを変えるたびに繰り返すことになる。

## 仕組み・背景

呼び方は違っても、主要なカスタムAI機能はほぼ同じ4つの部品からできている。

| 部品 | 役割 | GPTs | Gem | Claude Projects | Copilot Agent Builder |
|---|---|---|---|---|---|
| 指示 | 全会話に適用される役割・トーン・ルール(システムプロンプト相当) | Instructions | カスタム指示 | project instructions | 指示 |
| ナレッジ | 参照させる資料(検索拡張生成=RAGで部分的に検索される) | ナレッジ | ナレッジ | プロジェクトの知識 | 知識ソース(SharePoint等) |
| 外部連携 | 最新データの取得・外部システムの操作 | Actions(OpenAPI) | 非対応 | 非対応(Claude API側でTool Useが必要) | Microsoft Graphコネクタ、Power Platform連携 |
| 公開範囲 | 誰が使えるようにするか | 自分のみ/リンク共有/GPTストア公開 | 非公開/リンク共有/組織内 | Private/Public(組織内) | 個人利用/Microsoft 365 Copilotへの組織内配布 |

つまり「指示文をどう書くか」「ナレッジをどう与えるか」「誰に公開するか」という設計判断は、ツールをまたいで**そのまま使い回せるスキル**である。実体は、毎回の会話冒頭に同じシステムプロンプトと参照資料を自動で読み込ませているだけであり、魔法のような仕組みが動いているわけではない。裏側の技術的な仕組み(RAGによる検索、トークン数の上限)は[GPTsのナレッジファイルとアクション連携](gpts-knowledge-and-actions.md)で詳しく扱っている。

Microsoft 365 CopilotのAgent Builderは他の3つとやや毛色が異なり、「指示+公開Webサイトの知識」だけで作るエージェントは無料で使えるが、SharePointや社内データ(Microsoft Graphコネクタ経由)を参照させるエージェントは、Microsoft 365 Copilotライセンスまたは従量課金の対象になる([Microsoft Learn: Agents for Microsoft 365 Copilot Chat](https://learn.microsoft.com/en-us/copilot/agents))。2026年に入り、ナレッジソースにOneDriveのフォルダ・最大50ファイルを追加できるようになるなど機能拡張が続いている一方([Microsoft Learn: Microsoft 365 Copilotで宣言型エージェントにナレッジソースを追加する](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder-add-knowledge))、SharePoint上に作ったエージェントについては、Microsoft 365 Copilotライセンスを持たない利用者からの利用を1インタラクションあたりの従量課金(Copilot Studioのpay-as-you-goメーターで消費)で許可する仕組みも整備されつつある([Microsoft Tech Community: Consumption-based pricing for agents built in SharePoint](https://techcommunity.microsoft.com/blog/spblog/consumption-based-pricing-for-agents-built-in-sharepoint/4389591))。社内データに触れさせるかどうかで、必要なライセンス・ガバナンスの重さが変わる点は、他ツールにはない特徴である。エージェントの名前は30文字、説明は1,000文字、指示は8,000文字、知識源は最大20件(SharePointサイトやコネクタ単位)という上限も設けられており、1つのエージェントに情報を詰め込みすぎない設計を促す作りになっている([Microsoft Learn: Microsoft 365 CopilotのAgent Builderを使用してエージェントを構築する](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder-build-agents))。

なお2026年に入り、GPTs/Gem/Projects/Agent Builderのような「1つの箱に指示・ナレッジ・公開範囲をまとめて呼び出す」型の**ボット**とは別に、「特定タスクの手順書」を`SKILL.md`という共通形式(YAMLフロントマター+Markdown本文)のファイルにまとめ、該当するタスクが来たときだけAIが自動で読み込む**Skills**という仕組みが、Anthropic(Claude、2025年10月〜)・Google(Gemini CLI/Antigravity CLI、2025年11月〜)・Microsoft(Copilot Studio、2026年7月の全面刷新〜)と複数ベンダーで足並みを揃えて広がりつつある。カスタムAI(ボット)が「役割・トーン・参照資料をまるごと固定する」ためのものであるのに対し、Skillsは「特定の作業手順だけを必要な時にだけ読み込ませる」ためのものであり、両者は排他的ではなく併用できる概念である。詳しい仕組み(プログレッシブ・ディスクロージャー、MCPとの違い)は[AIエージェントのSkills(スキル)機能とは何か](../part11-ai-agents/claude-skills-and-agent-skills-basics.md)を参照。なおGoogleについては、2026年8月以降、無料機能である現行のGemを2026年10月20日に終了し、Gemini Spark内の有料機能「Skills」への移行を促す告知が一部ユーザー向けに表示されているとの報道が海外メディア複数から出ているが、2026年9月時点でGoogle公式の正式発表はまだない(詳細は[Gem(Geminiのカスタムボット機能)の基本](gemini-gem-feature.md)を参照)。

## 使いどころ・使い分け

### 作るべきか、作らないべきかの判断基準

| 状況 | 判断 |
|---|---|
| 同じ前提説明・同じフォーマット指定を3回以上コピペしている | 作る価値が高い(投資対効果が出やすい) |
| チームメンバーが同じ質問を繰り返し受けている(問い合わせ対応の一次窓口など) | 作る価値が高い(ナレッジ+共有機能を使う) |
| 一度きりの相談、毎回内容が大きく変わる雑多な質問 | 作らない(素のチャットで十分。Gem化・GPT化するほどの再利用性がない) |
| 参照させたい情報が機密性の高い個人情報・未公開の契約条件を含む | 慎重に判断する。ナレッジに置かず都度貼り付ける運用や、Team/Enterprise等の法人契約下での作成を検討([GPTsにおけるプロンプトインジェクション対策](gpts-prompt-injection-defense.md)を参照) |
| 「常に最新の値を取得したい」「システムを実行させたい」 | 指示文やナレッジでは実現できない。Actions/コネクタなど外部連携機能が使えるツールを選ぶ |
| 社内で誰が保守するか決まっていない | 作らない、または保守担当者を決めてから作る(放置されたカスタムAIは内容が古くなり誤情報源になる) |

### 公開範囲は「段階を飛ばさない」

どのツールも公開範囲は概ね次の3〜4段階で設計されている。

1. **自分のみ(Private)**: 個人の作業効率化。まずここから始める
2. **リンクを知っている人・チーム限定**: 特定プロジェクトのメンバーだけに共有
3. **組織内全体**: 社内の誰でも使える状態。ここから先はガバナンスの検討が必須になる
4. **一般公開(GPTストア等)**: ChatGPTのGPTsのみ対応。社外の不特定多数が使える

「作ってみたら便利だったので、確認せずに全社リンクを共有した」という広げ方は避ける。特に機密情報を含むナレッジを持たせている場合、公開範囲を1段階広げるごとに閲覧者が増えることを意味する。

### 社内での「乱立」を防ぐ

個人が思い思いにカスタムAIを作れる手軽さは長所であると同時に、管理が及ばない「野良AI(シャドーAI)」を増やす原因にもなる。似た用途のGPT/Gemが部署ごとに何個も作られ、どれが最新か誰も把握していない、という状態は典型的な失敗パターンである([ITmedia: 「ChatGPTの利用禁止」だけでは組織を守れない](https://atmarkit.itmedia.co.jp/ait/articles/2602/22/news004.html))。IPA(情報処理推進機構)が公表した「情報セキュリティ10大脅威 2026」(組織編)でも「AIの利用をめぐるサイバーリスク」が初めて選出され第3位にランクインしており、私物のアカウントや未承認のカスタムAIに業務データを入力してしまうことによる情報漏えいが、組織のリスクとして公式に認識される段階に入っている([IPA: 情報セキュリティ10大脅威 2026](https://www.ipa.go.jp/security/10threats/10threats2026.html))。対策として、以下のような軽量な運用ルールを組織内で決めておくと乱立を防ぎやすい。

- 組織内共有・公開する前に、既存の類似カスタムAIがないか一覧で確認する(簡単な社内台帳・スプレッドシートでもよい)
- 各カスタムAIに「作成者」「更新日」「用途」を指示文や説明欄に明記する
- 一定期間(例: 半年)更新がないものは棚卸しして統合・廃止する

## 実務での使い方

### 指示文(システムプロンプト)を書く共通の型

ツールを問わず、以下の4ブロックで指示文を組み立てると、抽象的な指示(「親切に」「専門的に」)よりも安定した挙動になりやすい。「親切で専門的に」のような形容詞だけの指示は、AIにとって何通りにも解釈できてしまい、結局は当たり障りのない平均的な回答に寄ってしまうためである。

```
## 役割
あなたは[具体的な役職・専門性]として振る舞ってください。

## 背景・前提
[想定ユーザー像、業務・会社の背景情報]

## タスク
[何をしてほしいか。動詞で具体的に]

## 出力ルール
- [出力形式(見出し・箇条書き・文字数など)]
- [トーン(ですます調、断定を避ける等)]
- [ナレッジファイルがある場合]添付資料に書かれていないことは推測せず「記載がありません」と答える
- [してはいけないこと]
```

このテンプレートの「役割」欄はChatGPT/Gem/Claude Projects/Copilot Agent Builderのいずれでも「指示」欄にそのまま貼り付けられる。各ツール固有のテンプレート例(議事録要約、経理FAQなど具体的な文面)は、[GPTsの作り方と公開設定](gpts-creation-basics.md)や[Gemの基本](gemini-gem-feature.md)、[Claude Projectsの基本](claude-projects-basics.md)にツールごとの実例を掲載している。

### ナレッジ(参照資料)を与える共通のコツ

- **Q&A形式に分解する**: 長い説明文よりも「Q. 〜ですか? / A. 〜です。」の1問1答形式の方が、RAGの検索にヒットしやすい(詳細は[GPTsのナレッジファイルとアクション連携](gpts-knowledge-and-actions.md)を参照)
- **目次・免責事項・ページ番号は削る**: 本文の答えを含まない部分は検索のノイズになりやすい
- **全文を毎回読ませたいのか、一部を検索させたいのかを区別する**: ナレッジは「関連しそうな断片」を検索して渡す仕組みであり、資料全体を踏まえた要約・添削のような作業には向かない。全文を踏まえてほしい場合は会話の都度ファイルを添付する
- **更新は基本的に手動**: 元ファイルを更新してもカスタムAI側には自動反映されない(GoogleドライブやSharePointと連携する場合を除く)。更新頻度が高い情報は、そもそもナレッジに固定せず外部連携(Actions・コネクタ)で都度取得する設計に切り替える

### ツール横断の対応付け(作成画面の入口)

| ツール | 作成画面への入口 | 必要プラン(2026年9月時点の目安) |
|---|---|---|
| ChatGPT(GPTs) | 左サイドバー「GPTを探す」→「＋作成する」 | GPT Builder(作成機能)はPlus以上が必要。無料の「Free」および低価格の「Go」(2026年に日本を含む主要国へ展開)はストア内の既成GPTを使うことはできるが、自分で新規作成はできない([OpenAI Help Center: Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-a-gpt)) |
| Gemini(Gem) | 「Gemを表示」→「Gemを作成」([Google Gemini アプリ ヘルプ](https://support.google.com/gemini/answer/15146780)) | 無料プランでも作成・利用可(動作モデルの性能や利用回数は有料プランの方が優遇される)。※Gem自体が2026年10月に終了する可能性が報じられている(未確認情報、下記注参照) |
| Claude(Projects) | 左サイドバー「Projects」→「+ New project」 | Freeでも作成可だが上限5件まで。Pro/Max/Team/Enterpriseは無制限かつRAG(検索拡張生成)の参照容量も拡大される |
| Microsoft 365 Copilot(Agent Builder) | Copilotアプリの「エージェントの作成」 | 公開Web知識のみのエージェントは無料。SharePoint等の社内データ参照はMicrosoft 365 Copilotライセンス、またはCopilot Studioの従量課金(pay-as-you-goメーター)が必要 |

料金・上限値は変更が頻繁なため、実際に作る直前に各ツールの公式ヘルプで最新情報を確認すること。特にGemini Gemは前述の通り終了の可能性が報じられており、この表よりも[Gem(Geminiのカスタムボット機能)の基本](gemini-gem-feature.md)の最新の注意書きを優先して確認してほしい。

## 注意点・よくある誤解

- **指示文は「約束」であって「制約」ではない**: 「この内容は非公開」「機密情報は答えない」と指示文に書いても、外部から与えられた文書やAPIレスポンスに紛れ込ませた指示によって突破される可能性がある(プロンプトインジェクション)。機密情報の保護を指示文だけに頼らないこと。詳細は[GPTsにおけるプロンプトインジェクション対策](gpts-prompt-injection-defense.md)を参照
- **作って終わりにしない**: カスタムAIは一度作ったら完成、ではなく、実際に使ってみて指示文やナレッジを調整する反復作業が前提になる。テスト対話をせずに公開範囲を広げると、期待外れの回答が広く共有されてしまう
- **公開範囲を広げるほど責任も重くなる**: 個人利用のPrivateな設定なら気軽に試行錯誤できるが、組織内共有・一般公開に進めるほど、内容の正確性・機密情報の扱い・保守体制について説明責任が生じる
- **「便利だから」で無制限に増やさない**: 1つ1つは有用でも、似たような役割のカスタムAIが乱立すると、どれを使えばよいか分からなくなり、結局誰も使わなくなる。新しく作る前に、既存のカスタムAIを拡張・統合できないか検討する
- **ツールが変わっても考え方は使い回せる**: 「指示+ナレッジ+公開範囲」という設計の型を理解しておけば、GPTsで学んだコツはGemやClaude Projects、Copilot Agent Builderにもほぼそのまま応用できる
- **機能自体がベンダー都合で終了・置き換えられることがある**: 2026年8月には、Googleが無料機能のGemを終了し有料の「Skills」への移行を促すとの未確認報道が出るなど、カスタムAI機能そのものの存続は保証されていない。指示文やナレッジの構成案は、そのツール専用画面だけでなく社内ドキュメント(GoogleドキュメントやNotionなど)にも控えを残しておくと、仕様変更や終了が実際に起きたときにゼロから作り直さずに済む

## 最初の一歩

自分が業務で3回以上同じ前提を説明してからAIに質問している作業を1つ書き出し、上記の指示文テンプレート(役割/背景/タスク/出力ルール)に当てはめて、まずは自分のみ公開のカスタムAIを1つ作ってみる。

## 関連トピック

- [GPTsの作り方と公開設定](gpts-creation-basics.md)
- [Gem(Geminiのカスタムボット機能)の基本](gemini-gem-feature.md)
- [Claude(Anthropic)の「プロジェクト」機能の基本](claude-projects-basics.md)
- [GPTsのナレッジファイルとアクション連携](gpts-knowledge-and-actions.md)
- [GPTsにおけるプロンプトインジェクション対策](gpts-prompt-injection-defense.md)
- [ロール(役割)プロンプティング](../part05-prompt-engineering/role-prompting.md)
- [AIエージェントのSkills(スキル)機能とは何か](../part11-ai-agents/claude-skills-and-agent-skills-basics.md)

## 更新履歴

### 2026-09-07: 「Skills」の台頭とGemini Gem終了報道を反映し最新化
- **内容**: 「仕組み・背景」に、GPTs/Gem/Projects/Agent Builderのようなボット型カスタムAIとは別に、`SKILL.md`形式(YAMLフロントマター+Markdown本文)で特定タスクの手順を必要な時だけ読み込ませる「Skills」がAnthropic・Google・Microsoft複数ベンダーで足並みを揃えて広がりつつある動きを追記し、Part11の詳細ページへリンク。Microsoft 365 Copilot Agent Builderの技術上限(指示8,000文字・知識源最大20件など)を追記。Googleが2026年8月以降、無料のGemを2026年10月20日に終了し有料の「Skills」への移行を促すとの未確認報道が出ている件を、ツール横断の対応表・注意点の両方に反映(2026年9月時点でGoogle公式発表はなし)。ChatGPTの料金体系がFree/Go/Plus/Pro/Business/Enterpriseの6段階で安定していることを確認し、GPTs作成にPlus以上が必要な点・Claude Projects無料プランの上限5件を2026年9月時点の情報として再確認
- **出典**: [Microsoft Learn: Microsoft 365 CopilotのAgent Builderを使用してエージェントを構築する](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder-build-agents)、[AIエージェントのSkills(スキル)機能とは何か](../part11-ai-agents/claude-skills-and-agent-skills-basics.md)、[TestingCatalog: Google may retire Gems in October, forcing migration to Skills](https://www.testingcatalog.com/google-may-retire-gems-in-october-forcing-migration-to-skill/)、[Android Authority: Google could retire a free Gemini feature in favor of a paid one](https://www.androidauthority.com/google-retire-gemini-gems-leak-3696240/)、[OpenAI Help Center: Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-a-gpt)

### 2026-07-24: 各ツールのプラン・機能条件を再検証し最新化
- **内容**: ツール横断の対応付け表を実態に合わせて修正(ChatGPTはGPT Builderの利用にPlus以上が必要な点を明確化、GeminiのGem作成画面の入口をGoogle公式ヘルプの表記に合わせて修正、Claude Projectsの無料プランの上限が「5件」であることを明記)。Microsoft 365 Copilot Agent BuilderについてOneDriveの知識ソース対応拡張(フォルダ・最大50ファイル)とSharePointエージェントの従量課金(pay-as-you-go)の仕組みを追記。「社内での乱立を防ぐ」節に、IPA「情報セキュリティ10大脅威2026」でAI利用リスク(シャドーAI含む)が組織向け脅威として初めて第3位に選出された事実を追加し、乱立対策の裏付けを補強
- **出典**: [OpenAI Help Center: Creating and editing GPTs](https://help.openai.com/en/articles/8554397-creating-a-gpt)、[Google Gemini アプリ ヘルプ: Gemini アプリで Gem を使用する](https://support.google.com/gemini/answer/15146780)、[Claude Help Center関連の無料プラン上限に関する複数の解説記事(freeacademy.ai: Claude Free Plan Limits 2026)](https://freeacademy.ai/blog/claude-free-plan-limits-2026)、[Microsoft Learn: Microsoft 365 Copilotで宣言型エージェントにナレッジソースを追加する](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder-add-knowledge)、[Microsoft Tech Community: Consumption-based pricing for agents built in SharePoint](https://techcommunity.microsoft.com/blog/spblog/consumption-based-pricing-for-agents-built-in-sharepoint/4389591)、[IPA: 情報セキュリティ10大脅威 2026](https://www.ipa.go.jp/security/10threats/10threats2026.html)

### 2026-07-06: 初版執筆
- **内容**: GPTs/Gem/Claude Projects/Microsoft 365 Copilot Agent Builderに共通する「指示・ナレッジ・外部連携・公開範囲」という設計の型、作るべきか/作らないべきかの判断基準、公開範囲を段階的に広げる考え方、社内での野良AI(シャドーAI)乱立を防ぐ運用ルール、ツール横断で使い回せる指示文テンプレート、ナレッジの与え方の共通のコツを整理
- **出典**: [Microsoft Learn: Agent Builder in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder)、[Microsoft Learn: Agents for Microsoft 365 Copilot Chat](https://learn.microsoft.com/en-us/copilot/agents)、[ITmedia: 「ChatGPTの利用禁止」だけでは組織を守れない AIとどう向き合い、管理すべきか](https://atmarkit.itmedia.co.jp/ait/articles/2602/22/news004.html)、[株式会社homula: 「野良AI」が企業を蝕む](https://www.homula.jp/blog/shadow-ai-enterprise-risk)、[OpenAI Help Center: Prompt engineering best practices for ChatGPT](https://help.openai.com/en/articles/10032626-prompt-engineering-best-practices-for-chatgpt)
