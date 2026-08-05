---
title: Google Antigravityの基本
part: 11
chapter: 第2章 コーディングエージェント
tags: [AIエージェント, Antigravity, Google, Gemini, コーディングエージェント, IDE]
created: 2026-08-05
updated: 2026-08-05
---

# Google Antigravityの基本

## これは何か

Antigravity は Google の**エージェント前提の開発プラットフォーム**である。
VS Code をベースにしたIDEだが、「人がコードを書き、AIが補完する」のではなく、
**複数のAIエージェントを同時に走らせ、人はそれを管理する**という前提で設計されている。

象徴的なのが **Agent Manager** で、これは並列で動く複数エージェントの司令塔にあたる。
「エディタでコードを書く画面」ではなく「動いているエージェントの一覧を見る画面」が中心にある点が、
従来のIDEとの一番大きな違いである。

もう一つの特徴は**ブラウザ操作**を標準で持つことである。エージェントが実際にブラウザを開いて
画面を確認し、フォームに入力し、動作を検証するところまで行う。
フロントエンド開発で「実装して、画面を見て、直す」ループをAI側で閉じられる。

なお、**Gemini CLI は Antigravity CLI に統合された**。2026年6月18日をもって、
Gemini CLI は Google AI Pro / Ultra および無料の個人アカウントに対するリクエスト提供を終了し、
これらの利用者は Antigravity CLI に移行する形になった
([Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/))。
Gemini CLI を使っていた人にとって、Antigravity は「後継」として押さえる必要がある。

## 仕組み・背景

### 経緯

2025年11月18日に、Gemini 3 と同時に公開された。VS Code のフォークとして作られており、
拡張機能やキーバインドの資産をある程度引き継げる。その後 **Antigravity 2.0** で
Agent Manager が強化され、会話をプロジェクト単位でまとめて管理できるようになった。

### 4つの提供形態

| 形態 | 位置づけ |
|---|---|
| **IDE** | VS Code ベースの本体。エディタとエージェント管理を統合 |
| **Antigravity 2.0(Agent Manager)** | 複数のローカルエージェントを並列管理するダッシュボード |
| **CLI** | ターミナル中心の自律コーディング。Go 製で軽快。Gemini CLI の後継 |
| **SDK** | Python でカスタムエージェントを試作する |

Antigravity CLI は Gemini CLI の主要機能(Agent Skills、Hooks、サブエージェント、
拡張機能=Antigravity プラグイン)を引き継いでおり、複数エージェントをバックグラウンドで
並列実行できる。大規模なリファクタや並行リサーチでターミナルを占有しない。

### マルチモデル対応

Antigravity の実務上重要な特徴が、**Google 以外のモデルも同じ環境で使える**ことである。
2026年8月時点で、Gemini 系(Gemini 3.6 Flash / 3.5 Flash / 3.1 Pro)に加えて
Claude Sonnet / Opus 4.6、gpt-oss-120b が選べる。
タスクに応じてモデルを切り替えられるため、「速さ重視はFlash、難しい設計はOpus」といった使い分けができる。

### Artifacts(成果物)

エージェントの作業結果を、コード差分だけでなく**計画・スクリーンショット・検証結果**といった
「成果物」として残す仕組みを持つ。エージェントが何をしたかを後から追えるため、
レビューのしやすさに直結する。

## 使いどころ・使い分け

### 向く場面・向かない場面

| 向く | 向かない |
|---|---|
| フロントエンドの実装+画面確認をまとめて任せる | 既存のエディタ環境を変えたくない場合 |
| 複数の作業を並列で走らせて時間を稼ぐ | 1つのタスクに集中して丁寧に進めたい場合 |
| Gemini CLI から移行する必要がある | ターミナル1本で完結させたい(CLI単体で使う手はある) |
| モデルを使い分けたい | 組織の承認済みツールが他社製品に固定されている |
| 無料枠でエージェント開発を試したい | 業務での安定稼働(2026年8月時点でまだプレビュー扱いの機能がある) |

### 他のコーディングエージェントとの違い

| | Antigravity | [Claude Code](claude-code-basics.md) | [Codex](openai-codex-basics.md) |
|---|---|---|---|
| 中心的なUI | IDE + Agent Manager(GUI) | ターミナル(CLI) | アプリ / CLI / IDE拡張 / クラウド |
| ブラウザ操作 | 標準機能として前面に出る | コンピュータ操作として可能 | クラウド実行が中心 |
| モデル | Gemini + Claude + gpt-oss を選択可 | Claude | GPT系 |
| 無料枠 | あり(週次のレート制限) | なし(Pro $17〜) | あり(ChatGPT Free に含まれる) |
| 課金の紐付け | Google AI Pro / Ultra | Claude Pro / Max | ChatGPT プラン |

**GUIで並列エージェントを俯瞰したいなら Antigravity、ターミナルで完結させたいなら Claude Code**
という選び方が実務的である。

## 実務での使い方

### 始め方

1. 公式サイトから自分のマシン向けビルド(Apple Silicon / Intel など)をダウンロード
2. Google アカウントでサインイン。無料プランならそのまま使い始められる
3. プロジェクトフォルダを開き、Agent Manager からタスクを投げる
4. ブラウザ操作を伴うタスクでは、エージェントがブラウザを立ち上げる許可を求めてくる

CLI だけ使う場合は Antigravity CLI を導入する。Gemini CLI を使っていたなら、
Agent Skills や Hooks の設定はおおむね引き継げる。

### 料金(2026年8月時点)

2026年5月19日にプラン体系が改定され、次の3階層になっている
([Antigravity 公式ブログ](https://antigravity.google/blog/changes-to-antigravity-plans))。

| プラン | 月額 | レート上限の目安 |
|---|---|---|
| 無料(Individual) | $0 | 週次の基本レート制限。タブ補完・コマンド実行は無制限 |
| Google AI Pro | $20 | 基準(1倍) |
| Google AI Ultra(中位) | $100 | Pro の 5倍のトークン量 |
| Google AI Ultra(上位) | $200 | Pro の 20倍のトークン量(旧 $250 から値下げ) |
| Organization | 従量 | Google Cloud 経由、API 料金ベース |

改定の要点:

- Gemini Flash と Gemini Pro を**単一のレート上限に統合**し、API料金ベースで消費する形になった
- **AIクレジットが基本プランから外れ**、代わりに枠(entitlement)が増えた
- Gemini 以外のモデル(Claude、gpt-oss)は**別枠の固定レート上限**を持つ

つまり Claude や gpt-oss を多用する場合は Gemini 系とは別の上限で管理されるため、
「どのモデルでどれだけ使うか」を意識する必要がある。

### 使い方のコツ

- **並列に投げすぎない。** Agent Manager で5本走らせると、レビューが追いつかず
  結局どれも取り込めない状態になりやすい。最初は2本までにする
- **ブラウザ操作は確認範囲を指定する。** 「ログインが必要な画面には入らない」
  「テスト環境のURLだけを開く」を明示する
- **Artifacts を読む。** 差分だけ見て通すのではなく、エージェントが立てた計画と
  検証結果を見て、意図した手順で進んだかを確認する

## 注意点・よくある誤解

- **Gemini CLI はもう個人向けには使えない。** 2026年6月18日で Google AI Pro / Ultra と
  無料個人アカウントへの提供が終了している。ただし **Gemini Code Assist の Standard /
  Enterprise ライセンス経由や、Google Cloud 経由の Gemini Code Assist for GitHub は
  影響を受けず継続**する。組織で使っている場合はどの契約で使っているかを確認する
- **無料枠は「試す」ためのもの。** 週次のレート制限があり、業務で回すには足りない
- **VS Code フォークであってVS Code ではない。** 拡張機能の互換性は完全ではなく、
  組織のセキュリティポリシーで「承認済みエディタ」が決まっている場合は別途審査が必要になる
- **ブラウザ操作は権限が強い。** ログイン済みブラウザを操作させると、
  そのアカウントでできることはすべてできてしまう。認証情報の扱いは
  [AIエージェントとは何か](ai-agent-basics.md)の「ログイン情報をどう扱うか」を参照
- **プレビュー段階の機能が混ざる。** 業務の基幹作業を依存させる前に、
  自分の用途で必要な機能が正式提供かを確認する
- **料金体系が短期間で変わっている。** 2026年5月に上位プランが $250→$200 に下がり、
  クレジットの扱いも変わった。**導入判断のたびに公式ページで確認する**

## 最初の一歩

無料プランで Antigravity をインストールし、既存の小さなプロジェクトを開いて
「このアプリを起動して、トップ画面のスクリーンショットを撮って、
UIの改善点を3つ挙げて」と頼んでみる。ブラウザ操作と Artifacts の挙動が一度で分かる。

## 関連トピック

- [AIエージェントとは何か](ai-agent-basics.md)
- [主要AIエージェントの比較と選び方](ai-agent-tools-comparison.md)
- [Claude Codeの基本](claude-code-basics.md)
- [OpenAI Codexの基本](openai-codex-basics.md)
- [コーディング支援AIの選び方・比較](../part08-specialized-ai-tools/coding-assistant-ai-comparison.md)
- [Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)

## 更新履歴

### 2026-08-05: 初版執筆
- **内容**: Antigravity のエージェント前提設計(Agent Manager・Artifacts・ブラウザ操作)、
  IDE / Agent Manager / CLI / SDK の4形態、Gemini・Claude・gpt-oss のマルチモデル対応、
  2026年6月18日の Gemini CLI から Antigravity CLI への移行(Gemini Code Assist 経由は継続)、
  2026年5月19日改定後の料金(無料 / AI Pro $20 / Ultra $100・$200)とレート上限の統合、
  Claude Code・Codex との比較表、ブラウザ操作の権限に関する注意点を整理
- **出典**: [Antigravity(公式)](https://antigravity.google/) /
  [Changes to Antigravity Plans(公式ブログ)](https://antigravity.google/blog/changes-to-antigravity-plans) /
  [Transitioning Gemini CLI to Antigravity CLI(Google Developers Blog)](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/) /
  [Choosing Antigravity or Gemini CLI(Google Cloud Blog)](https://cloud.google.com/blog/topics/developers-practitioners/choosing-antigravity-or-gemini-cli)
