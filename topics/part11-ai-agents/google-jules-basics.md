---
title: Google Julesの基本(非同期コーディングエージェント)
part: 11
chapter: 第2章 コーディングエージェント
tags: [AIエージェント, Jules, Google, コーディングエージェント, GitHub]
created: 2026-08-07
updated: 2026-08-07
---

# Google Julesの基本(非同期コーディングエージェント)

## これは何か

Jules は Google が提供する**非同期型**のコーディングエージェントである。
「バグを直して」「依存パッケージを更新して」のようにタスクを渡すと、
GitHubリポジトリをクラウドの仮想マシンにクローンし、対話なしで自律的に実装・テストを進め、
**プルリクエスト(PR)として結果を返す**。

同じGoogleのコーディングエージェントである[Antigravity](google-antigravity-basics.md)は
IDE・CLIで**対話しながら**進める設計であるのに対し、Julesは**タスクを投げて後で結果を回収する**
という使い方が前提になっている点が最大の違いである。なお、Julesの前身にあたる単体の
「Gemini CLI」は2026年6月18日にAntigravity CLIへ統合されており、Julesはこの統合後も
**独立したサービスとして存続している**別製品である。

## 仕組み・背景

### タスクの依頼方法は3つ

| 方法 | 使い方 |
|---|---|
| JulesのWeb画面 | 対象リポジトリ・ブランチを選び、タスクを自然文で記述。対象ファイルをファイルセレクターで絞り込める |
| CLI | ターミナルからタスクを投げる |
| GitHub Issueのラベル | 既存のIssueに`jules`ラベルを付けるだけでタスクとして着手させられる |

### 実行フロー

```
1. リポジトリ・ブランチをクラウドVMにクローンする
2. 実装計画を立てる
3. 計画に沿って実装・テストを行う
4. 差分(diff)を提示し、ユーザーの承認を求める
5. 承認後、PRを作成する
```

完了報告には**音声による変更内容のサマリー(audio changelog)**が添えられる点が、
他のコーディングエージェントと比べて独特な特徴である。

## 使いどころ・使い分け

### 向く仕事・向かない仕事

| 向く | 向かない |
|---|---|
| 範囲が明確なバグ修正・依存パッケージの更新 | 対話しながら方針を決めていく設計作業 |
| CI落ちの修正、定型的なメンテナンス作業 | リアルタイムに近い応答を必要とする作業 |
| 「投げて後で結果を見る」運用がしたい | ターミナル・IDEで並列エージェントを俯瞰したい(→[Antigravity](google-antigravity-basics.md)) |
| GitHub Issueの棚卸し・一括対応 | 密結合な大規模リファクタ(タスクを大きく渡しすぎない) |

### Antigravityとの使い分け

| | Jules | [Antigravity](google-antigravity-basics.md) |
|---|---|---|
| 使い方 | 非同期(投げて後で回収) | 対話型(IDE・CLIでやりとりしながら進める) |
| 実行場所 | クラウドVM | ローカルIDE+クラウド実行を併用 |
| 向く場面 | スコープが明確な単発タスクの積み上げ | 継続的な開発・大規模リファクタ・並列管理 |
| 提供状態(2026年8月時点) | パブリックベータ | 正式提供(2.0) |

## 実務での使い方

### 使えるプラン(2026年8月時点)

| プラン | モデル | タスク数/日 | 同時実行数 |
|---|---|---|---|
| Free | Gemini 2.5 Pro | 15 | 3 |
| Pro(Google AI Proに含む) | Gemini 3 Pro | 100 | 15 |
| Ultra(Google AI Ultraに含む) | Gemini 3 Pro | 300 | 60 |

**タスク数の上限は個人単位で、チーム内でプールされない。** 5人チームがFreeプランを使う場合、
「15タスク/日をチームで共有」ではなく「1人あたり15タスク/日」になる。

### 始め方

1. JulesのサイトでGoogleアカウントでログインし、対象のGitHubリポジトリを接続する
2. 新規タスクを作成し、対象ブランチ・対象ファイル(任意)・依頼内容を入力する
3. 提示された実装計画と差分を確認し、承認する
4. 作成されたPRをレビューし、マージするかどうかを判断する

GitHub Issueに直接`jules`ラベルを付ける方法なら、既存の課題管理フローに乗せたまま
タスクを割り振れる。

## 注意点・よくある誤解

- **Gemini CLIの後継ではない**: 2026年6月にGemini CLIが統合されたのはAntigravity CLIであり、
  Julesは統合前から別サービスとして存在する独立製品である。「Gemini CLIがJulesになった」という
  誤解をしないよう注意する
- **PRは必ず人がレビューする**: 差分承認のステップがあっても、それは「実行してよいか」の確認であり、
  「マージしてよいか」の保証ではない。テスト内容・設計判断の妥当性は人が確認する
- **タスクは小さく明確に切る**: スコープが曖昧な大きなタスクを渡すと、非同期で進む分だけ
  方向性のズレに気づくのが遅れる。範囲を絞ったタスクを積み重ねる使い方が向く
- **パブリックベータ段階である**: 2026年8月時点でJulesはベータであり、機能・料金・上限は
  変わりやすい。導入判断のたびに公式情報を確認する
- **間接プロンプトインジェクション**: Issueやコードコメントに埋め込まれた指示に従ってしまう
  可能性がある([プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md))

## 最初の一歩

範囲が明確なGitHub Issue(依存パッケージの更新など)を1件選び、`jules`ラベルを付けて
挙動を確認してみる。**対話せずに完了まで進む**という非同期の使い勝手を、
影響の小さいタスクで体感することが最短路になる。

## 関連トピック

- [AIエージェントとは何か](ai-agent-basics.md)
- [Google Antigravityの基本](google-antigravity-basics.md)
- [主要AIエージェントの比較と選び方](ai-agent-tools-comparison.md)
- [Claude Codeの基本](claude-code-basics.md)
- [OpenAI Codexの基本](openai-codex-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)

## 更新履歴

### 2026-08-07: 初版執筆
- **内容**: Julesの位置づけ(非同期型のコーディングエージェント、Antigravityとの対話型/非同期型の対比)、
  Web画面・CLI・GitHub Issueラベルの3つの依頼方法、クローン→計画→実装→差分承認→PR作成の実行フロー、
  音声による変更内容サマリー(audio changelog)、2026年6月のGemini CLI→Antigravity CLI統合とは
  別の独立製品である点、2026年8月時点のプラン(Free/Pro/Ultra、タスク数・同時実行数の上限)、
  タスク上限が個人単位でプールされない点を整理
- **出典**: [Jules: Google's autonomous AI coding agent(Google公式)](https://blog.google/innovation-and-ai/models-and-research/google-labs/jules/) /
  [FAQ(Jules公式)](https://jules.google/docs/faq/) /
  [Google Jules Pricing 2026(HackUp)](https://hackup.ai/ai-plans/jules/) /
  [An important update: Transitioning Gemini CLI to Antigravity CLI(Google Developers Blog)](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/)
