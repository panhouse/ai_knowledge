---
title: ブラウザ操作型AIエージェントの基本(Perplexity Comet・OpenAI Atlas等)
part: 11
chapter: "第6章 その他・未分類"
tags: [AIエージェント, ブラウザエージェント, Comet, Atlas, Copilot Mode, Dia, Opera Neon, プロンプトインジェクション]
created: 2026-08-18
updated: 2026-08-18
---

# ブラウザ操作型AIエージェントの基本(Perplexity Comet・OpenAI Atlas等)

## これは何か

**ブラウザ操作型AIエージェント**とは、ブラウザそのものにAIエージェント(目標を渡すと
自分で計画を立てて実行するAI)が組み込まれ、**クリック・入力・スクロール・画面遷移**
といった「人がふだんブラウザで行う操作」を代わりに実行してくれる製品群である。
Perplexity Comet、OpenAI Atlas(2026年8月時点では後述の理由で終了)、
Microsoft EdgeのCopilot機能、Google ChromeのGeminiエージェント機能、Dia、Opera Neon
などがこの分類に入る。

普通の「Web検索できるチャットボット」との違いは、**ページを読んで答えるだけでなく、
実際にページの状態を変える**点にある。フォームに入力して送信する、
複数サイトを渡り歩いて比較する、購読解除ボタンを押す、といった「実行」までを担う。
このページでは、こうした**ブラウザ単体・ブラウザ拡張として提供される独立製品**を扱う。
チャットUIに付属する調べもの機能(ChatGPT Agent など)は
[主要AIチャットツールの基本](../part03-ai-chat-tools/_index.md)、
自分でブラウザ操作エージェントを組む話はPart 9のMCP・Computer Use系APIを参照。

## 仕組み・背景

### 基本的な動作ループ

```
1. ユーザーが目標を自然文で渡す(例:「この3社の料金ページを開いて表にまとめて」)
2. エージェントが現在のページのDOM(画面の構造データ)やスクリーンショットを読み取る
3. 次に取るべき操作(クリック・入力・スクロール・別タブを開く等)を1手ずつ計画する
4. 操作を実行し、結果の画面を確認する
5. 目標達成 or 確認が必要な局面(ログイン・決済など)まで2〜4を繰り返す
```

### 最大の特徴は「本人のログイン状態」で動くこと

これらのエージェントは、多くの場合**ユーザー本人がログイン済みのブラウザセッション**
(Cookieや保存済みパスワードを含む)の上で動く。だからこそ「会員サイトの中身を見て
比較する」「予約フォームに自分の情報で入力する」といった、ログインが要る作業まで
代行できる。裏返せば、**そのセッションを乗っ取られると本人になりすまして操作される**
リスクも同時に持つ、というのがこの分類固有の設計上の緊張関係である
(詳細は「注意点」参照)。

### 制御方式の違い

| 方式 | 何をするか | 採用例 |
|---|---|---|
| 実行前プレビュー | 操作計画を提示し、ユーザーが承認してから実行 | Comet、Opera Neon |
| ドメイン許可制 | IT管理者が承認したサイトでしか操作させない | Edge for Business |
| 閲覧専用モード | 「読んで答える」だけに制限し、操作は禁止 | Comet Enterprise(ポリシーで選択) |
| 地域・プラン制限 | 特定の国・契約プランのみ機能を解放 | Chrome自動操作(米国先行) |

## 使いどころ・使い分け

### 主要製品比較(2026年8月時点)

| 製品 | 提供元 | 形態 | 使用モデル | 価格 | 対応OS | 得意 |
|---|---|---|---|---|---|---|
| **Comet** | Perplexity | Chromium独立ブラウザ | Sonar / Claude Opus 4.6(既定) / GPT-5.4 / Gemini 3.1 Pro / Kimi K2.5 など選択可 | 基本機能は無料(2026年3月にパブリック化)。Pro $20/月・Max $200/月で上限拡張。法人はComet Enterprise(別料金) | Win/Mac/iOS/Android | リサーチ・比較・要約+定型操作の代行 |
| **Atlas → ChatGPTブラウザ機能** | OpenAI | 独立ブラウザ(**2026年8月9日に提供終了**)→ChatGPTデスクトップアプリの内蔵ブラウザ・Chrome拡張へ統合 | GPT系(Agent mode) | ChatGPTの有料プラン(Plus/Pro/Business)に含む | Atlas時代はMacのみ。統合後はChrome拡張経由で主要OSから利用可 | 複雑な調べもの+タブをまたぐ実行 |
| **Edge(Browse with Copilot、旧Copilot Actions)** | Microsoft | 既存Edgeの内蔵機能 | Copilot(GPT系) | Edge自体は無料。一般機能はMicrosoftアカウントでログインすれば追加課金なし。業務利用の高度な統制はMicrosoft 365 Copilotライセンスと連携 | Win/Mac | 予約・購読解除など定型操作、IT統制下での業務利用 |
| **Chrome自動操作(auto browse)** | Google | 既存ChromeのGeminiサイドバー機能 | Gemini 3 | Google AI Pro($20/月)以上のサブスクで解放(2026年1月28日提供開始、米国先行) | Win/Mac/ChromeOS | フォーム入力・価格比較の自動化 |
| **Dia** | The Browser Company(Atlassian傘下) | Chromium独立ブラウザ | 複数モデルを切替(非公開) | 無料+Pro $20/月 | Macのみ(Windowsは開発中) | タブ横断の要約・チャット(「スキル」機能中心) |
| **Opera Neon** | Opera | Chromium独立ブラウザ | Gemini 3 Pro / GPT-5.1 / Veo 3.1 / Nano Banana Pro などを選択 | $19.90/月(無料枠なし) | Win/Mac | チャット・タスク実行・簡易Webアプリ生成の3モード |

**Atlasの提供終了は、この分野の変化の速さを象徴する出来事である。** 2025年10月21日に
Macのみでローンチし、2026年8月9日に終了(292日)。Windows・iOS・Android版は
ベータすら出ないまま終わった。OpenAIは技術をChatGPT本体・Codexに統合する方針に転換しており、
「ブラウザ単体製品として独立させる」戦略自体が難しいことを示す事例といえる。

**DiaはAtlas・Cometほど「操作を実行する」ことに強くない。** タブの内容を読んで答える
比重が大きく、クリック・入力を伴う自律操作は他社より限定的である。「読んで理解する」用途か
「実際に操作させる」用途かで、この2種類を混同しないこと。

### 選び方の判断軸

```
Q1. 会社としてIT管理下で使う必要があるか?
  ├ はい → Edge for Business(ドメイン許可リスト)か Comet Enterprise(MDM配布)
  └ いいえ → Q2へ

Q2. すでに契約しているAIベンダーはあるか?
  ├ ChatGPT → 統合後のChatGPTブラウザ機能・拡張を使う(Atlasは既に終了)
  ├ Google  → Chromeのauto browse(Google AI Pro以上が必要)
  ├ Microsoft → Edgeの標準機能(追加課金なし)
  └ なし    → Cometの無料枠から試す

Q3. 「実行」より「タブ横断で理解したい」が主目的か?
  └ はい → Dia
```

## 実務での使い方

### 画面操作の場所(2026年8月時点)

| 製品 | 起動場所 |
|---|---|
| Comet | ブラウザ右上の「Assistant」パネルを開き、自然文でタスクを入力 |
| Edge | アドレスバー横のCopilotアイコン、または `edge://settings/copilot` から機能を確認 |
| Chrome | 右上の星マーク(Gemini)アイコンからサイドバーを開き、タスク実行を指示 |
| Opera Neon | 左サイドの「Chat / Do / Make」の3タブを切り替え、「Do」でタスクを入力 |

### コピペで使える依頼例

```
この3社(A社・B社・C社)の料金ページを開いて、プラン名・月額・上限を
表にまとめて。ログインが必要な画面が出たら操作せずに止めて教えて。
```

```
受信トレイの未読プロモーションメールを開かずにアーカイブして。
決済・退会に関わるメールは対象外にして、件名一覧を最後に見せて。
```

**「ログイン・決済・退会が必要になったら必ず止める」という一文を毎回入れる**のが、
この種のエージェントを使う際の基本作法である。

### ツール横断の対応付け

| 概念 | Comet | Edge | Chrome | Opera Neon |
|---|---|---|---|---|
| 実行前の承認 | アクションプレビュー | 確認ダイアログ | 実行前ステップ表示 | タスク実行前プレビュー |
| 操作範囲の制限 | Comet Enterpriseのポリシー(閲覧専用/実行可を選択) | Edge for Businessの許可・ブロックリスト | 消費者向けのみ、法人統制は未整備 | 個人向けのみ |
| 監査ログ | Comet Enterprise(MDM経由でテレメトリ・監査ログ) | Microsoft Purview連携 | なし(消費者向け) | なし |

### 法人導入時に見るべきポイント

1. **消費者版をそのまま業務に使わない。** Comet Enterprise版・Edge for Business版など、
   IT管理者がドメイン許可・操作範囲を制御できるプランに乗せる
2. **監査ログの有無を確認する。** 「何のサイトで何を実行したか」が後から追えるか
3. **接続するアカウントを限定する。** 全社共通の管理者アカウントなどをログインさせたまま
   自律操作させない

## 注意点・よくある誤解

- **「ブラウジングできるチャットボット」と「操作するエージェント」は別物**。
  前者はページを読んで答えるだけ、後者はクリック・入力まで行う。導入判断の前にどちらの機能か確認する
- **間接プロンプトインジェクションが実際に報告されている**。
  Cometでは2025年8月にBrave社が、隠しテキスト(白背景に白文字など)や
  カレンダー招待に埋め込まれた指示に従ってしまい、認証情報やワンタイムパスワードを
  盗まれる脆弱性を報告している。2026年3月にはZenity Labsが、
  ユーザー操作なしでファイルや1Passwordの認証情報が抜き取られる
  ゼロクリックの脆弱性を確認した。**「ページの内容を読む」機能を持つエージェントは
  すべて、この種の攻撃を原理的に完全には防げない**という前提で使う
- **ログイン・CAPTCHA・決済の画面は自動化させない**。攻撃者は「ニセのCAPTCHAを解かせる」
  形でファイルダウンロードを誘発するなど、正規の作業に見せかけて悪意ある操作を紛れ込ませる。
  依頼文に「決済・退会・パスワード変更の手前で必ず止める」と明記しても、
  100%守られる保証はない。**重要な操作は人が画面を見て実行する**
- **1製品への依存を避ける**。Atlasは2025年10月のローンチから10か月足らずで終了した。
  ブックマーク・保存済み設定は自動で移行されないため、**乗り換えを前提にデータを
  こまめにエクスポートする**運用が安全
- **無料枠だけで導入判断をしない**。Cometのように無料化された直後の製品もあれば、
  Opera Neonのように無料枠自体が存在しない製品もある。個人の試用と法人導入は別基準で見る

## 最初の一歩

Comet(基本機能は無料)などで、**業務用の主要アカウントを繋がず**に、
リスクの低い定型タスク(複数サイトの価格比較、未読プロモーションメールの整理など)を
1つ試し、実行前プレビューでどこまで内容を確認できるかを体感してみる。

## 関連トピック

- [AIエージェントの自律度レベルと権限設計の基本](ai-agent-autonomy-levels-and-permission-design.md)
- [主要AIエージェントの比較と選び方](ai-agent-tools-comparison.md)
- [AIエージェント運用のガバナンス設計(権限ポリシー・監査ログ・コスト管理)](ai-agent-governance-basics.md)

## 更新履歴

### 2026-08-18: 初版執筆
- **内容**: ブラウザ操作型AIエージェント(ページを読むだけでなくクリック・入力まで代行する製品群)の定義と、
  チャットUI付属のエージェント機能・自作エージェントとの切り分け、ログイン済みセッション上で動く仕組みと
  そのリスク、実行前プレビュー/ドメイン許可制/閲覧専用モードといった制御方式の違い、
  Comet・Atlas(→ChatGPTブラウザ機能へ統合・2026年8月9日提供終了)・Edge(Browse with Copilot)・
  Chrome自動操作・Dia・Opera Neonの比較表(価格・対応OS・使用モデル)、法人導入時の統制ポイント、
  Cometで報告された間接プロンプトインジェクション事例(Brave 2025年8月・Zenity Labs 2026年3月)を整理
- **出典**: [Perplexity Comet Pricing 2026(eesel AI)](https://www.eesel.ai/blog/perplexity-comet-pricing)、
  [Evolving Atlas into ChatGPT for browser-based agentic work(OpenAI Help Center)](https://help.openai.com/en/articles/20001371-evolving-atlas-into-chatgpt-for-browser-based-agentic-work)、
  [OpenAI explains what will happen when ChatGPT Atlas shuts down this weekend(9to5Mac)](https://9to5mac.com/2026/08/04/openai-explains-what-will-happen-when-chatgpt-atlas-shuts-down-this-weekend/)、
  [Copilot in Microsoft Edge Brings AI Memory, Tab-Aware Answers & Agentic Browsing(Windows Forum)](https://windowsforum.com/threads/copilot-in-microsoft-edge-brings-ai-memory-tab-aware-answers-agentic-browsing.418390/)、
  [Edge for Business Agentic Browsing: Copilot Can Act—Under IT Rules(Windows Forum)](https://windowsforum.com/threads/edge-for-business-agentic-browsing-copilot-can-act-under-it-rules.419324/)、
  [Chrome auto-browse: How to use Gemini's new AI agent feature(eesel AI)](https://www.eesel.ai/blog/chrome-auto-browse-how-to-use-geminis-new-ai-agent-feature)、
  [Dia Browser Review 2026(buildfastwithai)](https://www.buildfastwithai.com/ai-tools/dia-browser-co)、
  [Opera wants you to pay $20 a month to use its AI-powered browser Neon(TechCrunch)](https://techcrunch.com/2025/12/11/opera-wants-you-to-pay-20-a-month-to-use-its-ai-powered-browser-neon/)、
  [Agentic Browser Security: Indirect Prompt Injection in Perplexity Comet(Brave)](https://brave.com/blog/comet-prompt-injection/)、
  [Zero-Click Prompt Injection in Perplexity's Comet AI Browser Enables Credential Theft(OECD.AI)](https://oecd.ai/en/incidents/2026-03-03-3fd7)、
  [Comet for Enterprise(Perplexity Help Center)](https://www.perplexity.ai/help-center/en/articles/12781449-comet-for-enterprise)
