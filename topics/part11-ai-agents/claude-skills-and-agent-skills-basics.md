---
title: AIエージェントのSkills(スキル)機能とは何か
part: 11
chapter: 第1章 エージェントの基礎
tags: [AIエージェント, Skills, Agent Skills, Claude, SKILL.md, MCP, カスタマイズ]
created: 2026-09-03
updated: 2026-09-03
---

# AIエージェントのSkills(スキル)機能とは何か

## これは何か

「毎回この会社のフォーマットで議事録を作ってほしい」「PDFのフォームを決まった手順で埋めてほしい」——こうした**特定タスクのやり方**をAIに教えるたびに、長い指示文を会話の冒頭に貼り付け直していないだろうか。**Skills(スキル、AnthropicではAgent Skillsとも呼ぶ)**は、この「タスク固有の手順書」をフォルダ単位のファイルとして用意しておき、関連する依頼が来たときにAIが自動で読み込んで使う仕組みである。指示文をその都度書くのではなく、「教材」として一度作れば使い回せる点が最大の価値になる。

Skillsは2025年10月にAnthropicがClaudeに導入した機能で、その後Googleが2025年11月公開のGemini CLI(2026年6月にAntigravity CLIへ統合)に「Agent Skills」として同種の仕組みを実装し、2026年7月にはMicrosoftもCopilot Studioの全面刷新でSKILL.md形式の「Skills」を採用するなど、複数ベンダーが同じ発想・同じファイル形式に収れんしつつある概念である。**MCP(外部ツール・データへの接続規格)や、GPTs/Gem/Claude Projectsのような「専用ボット作成」とは役割が異なる**。この違いを理解していないと、「Skillを作ればMCPは不要」「Skillは専用GPTの下位互換」といった誤解をしたまま導入設計を間違えてしまう。

## 仕組み・背景

### SKILL.mdという最小単位

Skillの実体は、`SKILL.md`という1つのMarkdownファイルを中心にしたフォルダである。冒頭にYAMLフロントマター(メタデータ)を置き、本文に手順を書く。

```markdown
---
name: pdf-form-filling
description: PDFフォームに決まった項目を入力する。ユーザーがPDFフォームの入力・提出書類の作成に言及したときに使う。
---

# PDFフォーム入力

## 手順
1. pdfplumberでフォーム項目を読み取る
2. 入力値をvalidate_form.pyで検証する
3. 入力済みPDFを書き出す

詳しい項目対応表は REFERENCE.md を参照。
```

Anthropicの仕様では`name`(小文字・数字・ハイフンのみ、64文字以内、"claude"や"anthropic"という語を含められない)と`description`(1024文字以内)が必須フィールドで、**この`description`に「何をするSkillか」と「いつ使うべきか」の両方を書く**ことが、AIが正しいタイミングで呼び出せるかを左右する。Gemini CLI(Antigravity CLI)の仕様もほぼ同型で、`name`と`description`を持つフロントマターが欠けているSKILL.mdは黙って無視される。

### 段階的に読み込まれる(プログレッシブ・ディスクロージャー)

Skillが効率的な理由は、内容を一度に全部読み込まないことにある。Anthropicは3段階の読み込みモデルを説明している。

| 段階 | いつ読み込まれるか | トークン消費の目安 | 内容 |
|---|---|---|---|
| レベル1: メタデータ | 常時(起動時にシステムプロンプトへ組み込み) | Skill1件あたり約100トークン | `name`と`description`のみ |
| レベル2: 本文の指示 | そのSkillが該当タスクとマッチした時 | 5,000トークン未満 | SKILL.md本文の手順・ベストプラクティス |
| レベル3: 付属リソース・スクリプト | 実際に参照・実行された時 | 参照されるまで0 | 追加のMarkdown資料、実行スクリプト、テンプレート、DBスキーマなど |

つまり、Skillを何十個インストールしても、使われないSkillは「名前と説明」の数百トークンしか消費しない。該当するSkillが見つかった時だけAIがbashコマンドでSKILL.mdを読みに行き、さらにそこで参照される補助ファイル(`FORMS.md`や`scripts/validate.py`など)だけを追加で読む・実行する。スクリプトを実行した場合、コードそのものはコンテキストに入らず、実行結果(出力)だけが渡されるため、複雑な処理を「AIに毎回コードを書かせる」よりも安定して速く済ませられる。

### MCPとの違い

[MCP(Model Context Protocol)の基本](../part09-api-development/mcp-basics.md)と混同されやすいが、担っている役割がまったく異なる。

- **MCP**は、AIを**外部のツール・データ**(Slack、Notion、社内DB、SaaSのAPIなど)に**接続する規格**。「何につながるか」を解決する
- **Skills**は、AIに**特定タスクの手順・ベストプラクティス**を**教え込む**仕組み。「つながった先(あるいは自分の手元の環境)で、どう作業するか」を解決する

両者は競合ではなく組み合わせられる。たとえば「MCPでSlackに接続」した上で、「Skillで社内特有の日報フォーマット」を教え込み、Skillの指示の中で「まとめた内容をSlackのMCPツールで投稿する」と書く、という使い方が典型例になる。

### GPTs / Gem / Claude Projectsとの違い

[Part 6 カスタムAIの作成](../part06-custom-ai/_index.md)で扱うGPTs・Gem・Claude Projectsは、**会話全体に効く「専用ボット」を作る**機能である。これに対してSkillsは**会話の途中で必要な瞬間だけ発動する部品**である。

| 観点 | Skills(スキル) | GPTs / Gem / Claude Projects |
|---|---|---|
| 単位 | 特定タスク1つぶんの手順書(フォルダ+SKILL.md) | 会話全体に適用される人格・設定一式(システムプロンプト+知識+モデル設定) |
| 発動のタイミング | 会話の途中、依頼内容とdescriptionが一致した瞬間に自動発動。1つの会話で複数Skillを併用できる | 会話を始める前にそのGPT/Gem/Projectを選んで入る。以後その会話全体に1つの設定が効き続ける |
| 組み合わせやすさ | 部品として合成可能(複数タスクをまたぐ依頼で複数Skillが同時に働く) | 基本的に1ボット=1設定。別の専門性が必要なら別のボットに移る必要がある |
| 中身 | Markdownの指示+任意でスクリプト・テンプレート・参考資料 | システムプロンプト+アップロード資料。GPTsのみ外部API連携(Actions)を追加可能 |

「特定の反復作業のやり方を教え込みたい」ならSkills、「特定の役割・キャラクターに特化した相談相手を常設したい」ならGPTs/Gem/Projects、という住み分けになる。

## 使いどころ・使い分け

3つの機能を並べると、選び方が整理しやすい。

| 状況 | 向いている選択 |
|---|---|
| 自社のPowerPointフォーマットで資料を作らせたい、PDFフォームを決まった手順で埋めさせたい | Skills(手順・テンプレートを教え込む) |
| Slack・GitHub・社内DBなど外部システムのデータを読み書きさせたい | MCP(接続そのものを規格化する) |
| 「カスタマーサポート想定の壁打ち相手」など特定の役割に固定した専用チャットを常設したい | GPTs / Gem / Claude Projects |
| 反復業務のうち「手順」はSkillに教え込み、「実行に使う外部システム」はMCPで繋ぎ、両方を1つの依頼で使わせたい | Skills + MCPの併用 |

**Skillsが向く例**:
- 決算資料・提案書など、自社のフォーマット・トーン・章立てが決まっている資料作成
- 「この種類のバグ報告が来たら、この順序で切り分ける」といったコードレビュー・デバッグの型
- 経費精算書のチェック、契約書の特定条項の確認など、手順が言語化できる定型チェック業務

**Skillsが向かない・過剰な例**:
- 1回限りの依頼(その場でプロンプトに書けば済み、フォルダ化する手間に見合わない)
- 外部システムへの接続そのものが目的(それはMCPの役割)
- 都度の裁量判断が必要で「手順」に落とし込めない業務

## 実務での使い方

### どこで使えるか(2026年9月時点)

| 提供元・製品 | 呼び方 | 対応状況 | 主な設定場所 |
|---|---|---|---|
| Anthropic Claude(claude.ai) | Skills | Pro/Max/Team/Enterpriseプランで、コード実行機能を有効にすると利用可 | 設定(Settings)→ 機能(Features)からzip形式でアップロード。個人単位で、組織一括管理はまだ非対応 |
| Anthropic Claude Code | Skills(カスタムSkill) | 標準対応。API連携不要でファイルシステムベース | `~/.claude/skills/`(個人用)または`.claude/skills/`(プロジェクト用)にフォルダを置くだけで自動検出 |
| Anthropic Claude Cowork | Skills(「Record a Skill」で録画から自動生成も可能) | 標準対応 | 左サイドバーの「Customize」→「Skills」タブ。画面操作を1回録画するだけでSkill化する機能もある |
| Anthropic Claude API | Agent Skills(`skill_id`指定) | コード実行ツール(code execution tool)必須。サンドボックス内で実行、ネットワークアクセス不可 | `/v1/skills`エンドポイントでアップロード、`container`パラメータで呼び出す。ワークスペース単位で共有 |
| Google Gemini CLI / Antigravity CLI | Agent Skills | 標準対応(Antigravity CLIはGemini CLIの主要機能として引き継ぎ) | `.gemini/skills/`(ワークスペース用)または`~/.gemini/skills/`(ユーザー用)にフォルダを配置 |
| GitHub Copilot | Skills(SKILL.md形式) | 対応 | リポジトリ内にSKILL.mdを配置 |
| Microsoft Copilot Studio | Skills | 2026年7月7日の全面刷新で追加。GitHub Copilot・Claude CodeのSKILL.md形式のSkillをそのままインポート可能とアナウンス | Build画面の「Skills」タブでMarkdownとして作成・インポート |

Anthropicが2025年10月にAgent Skillsとして提唱したSKILL.md形式が、その後Google・GitHub・Microsoftへと広がり、2026年7月のCopilot Studo刷新では「異なるツール間で同じSkillライブラリを使い回せる」ことが明示的な狙いとして語られている。**ファイル形式が事実上の業界標準になりつつある**点は、社内でSkillを資産化する際に覚えておく価値がある。

なお、**同じ「Skill」の中身は各プラットフォーム間で自動同期しない**。claude.aiにアップロードしたSkillはAPIには別途アップロードが必要で、Claude CodeのSkill(ファイルシステム上のフォルダ)ともまったく別管理になる。

### Claude Codeでの作り方(コピペで使える手順)

1. プロジェクト直下に`.claude/skills/`フォルダを作る(全プロジェクト共通にしたい場合はホームディレクトリの`~/.claude/skills/`)
2. その中にSkill名のサブフォルダを作り、`SKILL.md`を置く

```markdown
---
name: monthly-report-format
description: 月次レポートを自社フォーマット(表紙・サマリー3行・KPI表・所感)で作成する。「月次レポート」「月報」の作成を依頼されたときに使う。
---

# 月次レポート作成

## 手順
1. 冒頭に「対象月」「作成者」「作成日」を記載した表紙を作る
2. サマリーは3行以内で要点のみ書く(数値の羅列にしない)
3. KPI表は前月比・前年同月比を必ず入れる
4. 末尾に「所感・来月の重点」を箇条書きで3点まとめる

## 記入例
[実際のサンプル文面をここに貼る]
```

3. Claude Codeを再起動する(または新しいセッションを開く)と、フォルダ内のSkillが自動検出される
4. 「今月の月次レポートを作って」のように、`description`と合致する依頼をすると、Claudeが自動でSKILL.mdを読み込んで手順どおりに作業する

チームで共有したい場合は、`.claude/skills/`をリポジトリにコミットしてGit管理下に置けば、そのプロジェクトを開いた全員が同じSkillを使えるようになる。

### claude.aiでの作り方

1. アカウントアイコン→「設定」→「機能」でコード実行(Code execution)を有効化しておく
2. 同じ設定画面の「Skills」から、SKILL.mdと関連ファイルをまとめたzipファイルをアップロードする
3. アップロード後は、Anthropic提供の組み込みSkill(PowerPoint・Excel・Word・PDF)と並んで一覧に表示され、以後は該当する依頼のたびに自動で使われる

### 注意すべきセキュリティの考え方

Skillはただの説明文ではなく、AIに実行させるスクリプトやbashコマンドを含められる。Anthropicは「自分で作ったSkill、またはAnthropicが提供するSkillのみを信頼できるものとして使う」ことを明確に推奨しており、出所不明のSkillを使う場合はSKILL.md本文だけでなく同梱のスクリプトや画像まで含めて内容を精査するよう注意喚起している。特に外部URLを取得する処理を含むSkillは、取得先のコンテンツに悪意のある指示が仕込まれるリスク(間接プロンプトインジェクション)があるため要注意。Enterprise向けには、アップロードされたカスタムSkillの内容をスキャンする機能も用意されている。

## 注意点・よくある誤解

- **「Skillを入れればMCPは不要」ではない**: Skillは手順を教えるだけで、外部システムへの接続能力そのものは持たない。接続が必要ならMCP(またはAPI連携)と組み合わせる必要がある
- **各プラットフォーム間でSkillは自動同期しない**: claude.ai・Claude API・Claude Codeはそれぞれ別管理。同じSkillを複数の場所で使いたい場合は、場所ごとにアップロード・配置し直す必要がある
- **claude.aiでは組織一括管理ができない(2026年9月時点)**: 個人ごとのアップロードになり、管理者が全社に一括配布する仕組みはまだない。全社展開したい場合はClaude Code(プロジェクトにコミット)やClaude API(ワークスペース共有)を検討する
- **descriptionを曖昧に書くと発動しない・誤発動する**: 「〜を作成する」だけでなく「いつ使うべきか」の条件までdescriptionに書かないと、AIが該当タスクとSkillを結びつけられない、あるいは無関係な依頼で誤って発動してしまう
- **信頼できない配布元のSkillは実行環境ごと乗っ取られるリスクがある**: スクリプト同梱型のSkillは「ソフトウェアをインストールする」のと同程度の慎重さで扱う。社内で配布する際は、誰が作成・レビューしたSkillかを分かるようにしておく
- **名称が似た機能でも中身は別物**: Claude Cowork の「Record a Skill」(画面操作の録画からSkillを自動生成)、Microsoft Copilot Studioの「Skills」(Markdown化された指示・知識のパーツ)など、各社が同じ「Skill」という言葉を使っていても作り方・粒度・運用画面は異なる。導入時は必ずそのツールの公式ドキュメントで仕様を確認する

## 最初の一歩

自分が週に何度も同じ指示を貼り付けているタスクを1つ選び、Claude Codeを使っているなら`.claude/skills/`にサブフォルダを作って、`name`・`description`・手順3〜5行だけのミニマムなSKILL.mdを1つ書いてみる。次に同じ種類の依頼をしたとき、指示文を貼らずにSkillが自動で読み込まれるかを確認するだけで、仕組みの勘所がつかめる。

## 関連トピック

- [MCP(Model Context Protocol)の基本](../part09-api-development/mcp-basics.md)
- [Claude(Anthropic)の「プロジェクト」機能の基本](../part06-custom-ai/claude-projects-basics.md)
- [Google Antigravityの基本](google-antigravity-basics.md)
- [Claude Codeの基本](claude-code-basics.md)
- [Claude Coworkの基本](claude-cowork-basics.md)

## 更新履歴

### 2026-09-03: 初版執筆
- **内容**: Skills(Agent Skills)の定義、SKILL.mdのファイル構造とフロントマター仕様、3段階のプログレッシブ・ディスクロージャー(メタデータ→本文→付属リソース)、MCPとの役割の違い、GPTs/Gem/Claude Projectsとの違い(比較表)、Claude(claude.ai/Claude Code/Claude Cowork/Claude API)・Gemini CLI/Antigravity CLI・GitHub Copilot・Microsoft Copilot Studioでの対応状況とSKILL.md形式の業界標準化、Claude Codeでの具体的な作成手順、セキュリティ上の注意点を整理
- **出典**: [Anthropic: Agent Skills(Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)、[Anthropic: anthropics/skills(GitHub)](https://github.com/anthropics/skills)、[Anthropic: Extend Claude with skills(Claude Code Docs)](https://code.claude.com/docs/en/skills)、[Anthropic Help Center: Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude)、[Gemini CLI: Agent Skills](https://geminicli.com/docs/cli/skills/)、[Google Developers Blog: Transitioning Gemini CLI to Antigravity CLI](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)、[Microsoft Community Hub: Meet the new Copilot Studio, rebuilt for more complex, multi-step work](https://techcommunity.microsoft.com/blog/copilot-studio-blog/meet-the-new-copilot-studio-rebuilt-for-more-complex-multi-step-work/4526488)
