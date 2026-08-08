---
title: Devinの基本(Cognition社の自律コーディングエージェント)
part: 11
chapter: 第2章 コーディングエージェント
tags: [AIエージェント, Devin, Cognition, コーディングエージェント, ACU]
created: 2026-08-07
updated: 2026-08-07
---

# Devinの基本(Cognition社の自律コーディングエージェント)

## これは何か

Devin は、米スタートアップ Cognition が開発するコーディングエージェントである。
タスクを依頼すると、専用のクラウド環境(ターミナル・エディタ・ブラウザ付き)を自分で立ち上げ、
計画・実装・テストまでを自律的に進め、**GitHub上のプルリクエスト(PR)として結果を届ける**。

[Claude Code](claude-code-basics.md)・[Codex](openai-codex-basics.md)・
[Antigravity](google-antigravity-basics.md)が主要AIベンダーの一角(Anthropic/OpenAI/Google)による
製品であるのに対し、Devin は**コーディングエージェント専業のスタートアップ**が作った独立製品という
位置づけが特徴で、Slack起点の依頼やPRレビューの自動化など、**チームの開発フローに乗せる**方向の
機能が充実している。

## 仕組み・背景

### Slackから頼み、PRで受け取る

DevinはSlack連携が前面に出ている点が実務上のポイントである。エンジニアはSlackのスレッドで
「@Devin」とメンションしてタスクを割り当てられ、進行状況もSlack上で確認できる。
完成した変更は自動でPRとして作成され、Slackの通知には「Devin Review」へのリンクが添付される。

### Devin Review(PRの自動レビュー・自動修正)

**Devin Review**は、大きく複雑なPRを整理されたdiffと説明に変換して読みやすくする機能である。
Devin Reviewや連携するGitHub上のBotが問題を検出した場合、**Devinが自動でPRを修正し、
CI・lintのチェックが通るまで対応を続ける**。人間のレビューは「直してもらった後の最終確認」に
回せるため、レビュー往復の負荷が下がる。

### 画像・動画からのバグ報告に対応

UIのモックアップ(画像・Figma)や画面録画の動画を渡すだけで、見た目の不具合を理解して
修正できる機能が追加されている。テキストで説明しにくい表示崩れなどの報告に向く。

## 使いどころ・使い分け

### ACU(Agentic Compute Unit)課金の実額感

Devin最大の特徴は、作業量を**ACU(Agentic Compute Unit)**という独自単位で計測する
従量課金である。1 ACU ≒ 15分間の自律作業に相当する。

| 作業の重さ | ACU目安 | Core プランでの費用目安 |
|---|---|---|
| 典型的なバグ修正 | 2〜3 ACU | $4.50〜$6.75 |
| 複数ファイルにまたがる移行作業 | 30 ACU超 | $67.50以上 |

**「1タスクいくら」が見える**のは予算管理上の利点だが、**重い作業ほどコストが跳ねる**ため、
サブスク定額のClaude Code・Antigravityとは予算の立て方が根本的に異なる。

### 向く場面・向かない場面

| 向く | 向かない |
|---|---|
| Slack中心の開発コミュニケーション | ターミナル・IDEで直接対話しながら進めたい |
| PRレビューの往復を減らしたい | 1タスクあたりのコストを気にせず使いたい(従量課金) |
| 画像・動画でしかうまく説明できない不具合 | 既にAnthropic/OpenAI/Googleと契約があり、そこに寄せたい |
| 独立したIssueを多数チームに割り振りたい | 軽い作業を頻繁に投げる(ACU消費が積み上がる) |

他のコーディングエージェントとの横並び比較(UI・並列実行・無料枠の有無など)は
[主要AIエージェントの比較と選び方](ai-agent-tools-comparison.md)を参照。

## 実務での使い方

### 使えるプラン(2026年8月時点)

| プラン | 月額 | ACU料金 |
|---|---|---|
| Core | $20 | $2.25/ACU |
| Team | $500 | 250 ACU込み、超過分は$2/ACU |
| Enterprise | 個別見積 | 個別契約 |

無料プランはなく、最初から従量課金が発生する点はClaude Code・Codex(いずれも無料枠あり)との
明確な違いになる。

### 始め方

1. Cognitionのアカウントを作成し、対象のGitHubリポジトリを接続する
2. SlackワークスペースにDevinを追加する(任意だが実務上は推奨)
3. Slackで「@Devin」にタスクを依頼、またはWebのDevinダッシュボードから直接依頼する
4. 作成されたPRを確認し、Devin Reviewのリンクからdiffの要点を確認する

### コピペで使える依頼文の型

```
## お願いしたいこと
`user-service`リポジトリで、決済APIのタイムアウトエラーを調査して修正してください。

## 制約
- 既存のテストは全て通す状態にしてください
- 新しい外部ライブラリは追加しないでください
- 修正方針に複数の選択肢がある場合は、PRの説明に選択肢と選んだ理由を書いてください

## 出力
- 修正はPRとして提出してください。マージは私が行います
```

## 注意点・よくある誤解

- **ローンチ当初(2024年)のデモは誇張だと批判された経緯がある**: 初期の実演動画は
  条件のよいタスクを選んで見せていたとの指摘があり、公表されたベンチマーク成績も
  「対象を絞った一部のみ」を評価したものだった。2026年時点の製品は当時から機能が拡張されているが、
  **「自律的に完遂できる」という宣伝文句をそのまま信じず、自社のコードベースで実際に試す**姿勢が重要
- **ACU従量課金は重い作業でコストが跳ねる**: 移行作業のような大きなタスクを丸ごと投げると、
  想定より高くつくことがある。タスクを小さく切って依頼するとコストの見通しが立てやすい
- **PRは必ず人がレビューする**: Devin Reviewによる自動修正・CI通過は「マージしてよい」ことを
  意味しない。差分・テスト内容・設計判断の妥当性は人が確認する
- **間接プロンプトインジェクション**: Issueやコメント、取り込む依存パッケージに仕込まれた指示に
  従ってしまう可能性がある([プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md))
- **料金・機能は変わりやすい**: 本ページの数値は2026年8月時点。導入判断のたびに公式サイトで確認する

## 最初の一歩

小さく影響範囲の限定されたバグ修正を1件選び、Devinに依頼してACU消費と成果物の質を確認する。
**最初から重い移行作業を任せない**ことが、コスト感をつかむ最短路になる。

## 関連トピック

- [AIエージェントとは何か](ai-agent-basics.md)
- [主要AIエージェントの比較と選び方](ai-agent-tools-comparison.md)
- [Claude Codeの基本](claude-code-basics.md)
- [OpenAI Codexの基本](openai-codex-basics.md)
- [Google Antigravityの基本](google-antigravity-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)

## 更新履歴

### 2026-08-07: 初版執筆
- **内容**: Devinの位置づけ(Cognition社によるコーディングエージェント専業スタートアップの製品)、
  Slack連携によるタスク割り当てとPR提出のワークフロー、Devin ReviewによるPR自動レビュー・
  CI/lint通過までの自動修正、画像・動画からのバグ報告対応、ACU(Agentic Compute Unit)従量課金の
  実額目安(バグ修正2〜3 ACU/$4.50〜6.75、大規模移行30 ACU超/$67.50以上)、
  2026年8月時点のプラン(Core $20+$2.25/ACU、Team $500/250 ACU込み+$2/ACU、Enterprise)、
  2024年ローンチ時のデモ誇張批判の経緯、レビューの実務を整理
- **出典**: [Devin(Cognition公式)](https://cognition.com/) /
  [How Cognition Uses Devin to Build Devin](https://cognition.com/blog/how-cognition-uses-devin-to-build-devin) /
  [Devin Pricing 2026(Lindy)](https://www.lindy.ai/blog/devin-pricing) /
  [Devin AU/ACU FAQ 2026](https://cursor-alternatives.com/blog/devin-faq/)
