---
title: Devinの基本(Cognition社の自律コーディングエージェント)
part: 11
chapter: 第2章 コーディングエージェント
tags: [AIエージェント, Devin, Cognition, コーディングエージェント, ACU, クォータ制, SWE-2]
created: 2026-08-07
updated: 2026-09-26
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
機能が充実している。開発元Cognitionは2026年5月に10億ドルを調達し評価額約250億ドルに達したのに続き、
同年9月時点では評価額400億ドル台での新規調達交渉が報じられるなど急成長しており、
年間経常収益(ARR)は2025年5月の約3,700万ドルから2026年時点で約4.92億ドルまで拡大したと報じられている
(Bloomberg・TechCrunchなど複数メディアの報道。数値は交渉中の評価額を含み今後変わり得る)。

本ページが扱う「Devin」は、Slackやダッシュボードから依頼してPRを受け取る**クラウド型の自律エージェント**
であり、旧「Windsurf」から改称されたAI専用エディタ「[Devin Desktop](../part08-specialized-ai-tools/windsurf-basics.md)」
(旧Cascade、現Devin Local)とは別製品である。どちらもCognitionの「Devin」ブランドに統合されているため、
社内で名称を混同しないよう注意する。

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

### クォータ制課金への移行(2026年3月〜)

Devinは当初、作業量を**ACU(Agentic Compute Unit)**という独自単位(1 ACU ≒ 15分間の自律作業)で
計測する従量課金だったが、2026年3月19日、セルフサーブ(Free/Pro/Max/Teams)プランについては
**日次・週次で自動リフレッシュする「クォータ(利用枠)」制**に切り替わった。消費量はACU換算ではなく
モデルごとのトークン使用量で決まり、クォータを使い切った分はドル建てで従量課金される。
**ACUという単位そのものはなくなっておらず、Enterprise契約では引き続きACU建てで請求される**
(発注書に記載のレート)点に注意する。

| プラン区分 | 課金方式 | 特徴 |
|---|---|---|
| Free / Pro / Max / Teams(セルフサーブ) | トークン使用量に応じたクォータ制 | クォータは日次・週次で自動回復。超過分は従量課金 |
| Enterprise | ACU従量課金(発注書ベース) | 旧来のACU単位がそのまま残る |

セルフサーブ移行前(〜2026年3月)の実額目安として、Core プランでは典型的なバグ修正が2〜3 ACU
($4.50〜$6.75)、複数ファイルにまたがる移行作業が30 ACU超($67.50以上)という水準だった。
現行のクォータ制でも「軽い作業は消費が少なく、重い作業ほど消費が増える」という感覚自体は同じだが、
**「1 ACU=◯ドル」という単純な換算では見積もれなくなった**点が実務上の変化である。

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

### 使えるプラン(2026年9月時点)

2026年3月のクォータ制移行にあわせてプラン体系も刷新され、旧来の「Core $20」「Team $500」構成から
以下に変わった。

| プラン | 月額 | 内容 |
|---|---|---|
| Free | $0 | Devin Desktop(タブ補完・インライン編集)は無制限。クラウドエージェント・API等は利用不可 |
| Pro | $20 | クォータ増、フロンティアモデル全種を利用可、クラウドエージェント・API利用可 |
| Max | $200 | Proよりさらに大幅増量したクォータ |
| Teams | 基本$80+開発者1席$40(最大200席) | Proの内容に加え、共有・共同編集、一元請求、管理ダッシュボード |
| Enterprise | 個別見積 | SSO、専用アカウント管理、ACU従量課金(発注書ベース) |

**無料プラン(Free)が2026年3月に新設された**が、自律的にタスクをこなすクラウドエージェント機能は
Pro以上が前提で、実質的には月$20〜から使う製品という位置づけは変わっていない。
2026年9月10日には自社モデル「SWE-2」(Moonshot AIの基盤モデル「Kimi K3」をベースに後学習)が
Proプランにバンドルされる形でリリースされ、2026年10月10日までは無料で利用できる。

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
- **クォータ・ACUとも重い作業で消費が跳ねる**: 移行作業のような大きなタスクを丸ごと投げると、
  想定よりクォータ消費やコストが大きくなることがある。タスクを小さく切って依頼すると見通しが立てやすい
- **PRは必ず人がレビューする**: Devin Reviewによる自動修正・CI通過は「マージしてよい」ことを
  意味しない。差分・テスト内容・設計判断の妥当性は人が確認する
- **間接プロンプトインジェクション**: Issueやコメント、取り込む依存パッケージに仕込まれた指示に
  従ってしまう可能性がある([プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md))
- **料金・機能は変わりやすい**: 本ページの数値は2026年9月時点。2026年3月にも課金方式そのものが
  ACUからクォータ制へ変わっており、導入判断のたびに公式サイト(devin.ai/pricing)で確認する

## 最初の一歩

小さく影響範囲の限定されたバグ修正を1件選び、Devinに依頼してACU消費と成果物の質を確認する。
**最初から重い移行作業を任せない**ことが、コスト感をつかむ最短路になる。

## 関連トピック

- [AIエージェントとは何か](ai-agent-basics.md)
- [主要AIエージェントの比較と選び方](ai-agent-tools-comparison.md)
- [Windsurf(Devin Desktop)の基本](../part08-specialized-ai-tools/windsurf-basics.md)
- [Claude Codeの基本](claude-code-basics.md)
- [OpenAI Codexの基本](openai-codex-basics.md)
- [Google Antigravityの基本](google-antigravity-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)

## 更新履歴

### 2026-09-26: 課金方式の変更・新モデル・企業動向を反映して最新化
- **内容**: 2026年3月19日にセルフサーブプラン(Free/Pro/Max/Teams)の課金がACU従量課金から
  日次・週次のクォータ制へ移行したこと(Enterprise契約は引き続きACU建て)を反映。
  プラン体系を旧Core($20)/Team($500)構成から新Free($0)/Pro($20)/Max($200)/Teams(基本$80+席$40)/
  Enterprise構成に更新。2026年9月10日リリースの新モデル「SWE-2」(Kimi K3ベース、2026年10月10日まで
  無料)を追記。Windsurfが2026年6月に「Devin Desktop」としてDevinブランドに統合されたことに触れ、
  クラウド型のDevin(本ページ)と混同しないよう関連トピックにリンクを追加。Cognitionの資金調達・
  評価額急上昇(2026年5月に評価額約250億ドル、9月時点で400億ドル台の交渉報道)を仕組み・背景に追記
- **出典**: [Cognition公式ブログ「New self-serve plans for Devin」](https://cognition.com/blog/new-self-serve-plans-for-devin)、
  [Devin公式ドキュメント「Quota-Based Usage」](https://docs.devin.ai/desktop/accounts/quota)、
  [Devin公式ドキュメント「Billing」](https://docs.devin.ai/admin/billing)、
  [VentureBeat「Devin 2.0 is here」](https://venturebeat.com/programming-development/devin-2-0-is-here-cognition-slashes-price-of-ai-software-engineer-to-20-per-month-from-500)、
  [TechCrunch「AI coding startup Cognition raises $1B at $25B pre-money valuation」](https://techcrunch.com/2026/05/27/ai-coding-startup-cognition-raises-1b-at-25b-pre-money-valuation/)、
  [runtimewire.com「Cognition ships SWE-2」](https://runtimewire.com/article/cognition-swe-2-coding-model-scott-wu)

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
