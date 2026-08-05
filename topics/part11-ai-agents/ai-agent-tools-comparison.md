---
title: 主要AIエージェントの比較と選び方
part: 11
chapter: 第4章 エージェントの選び方・比較
tags: [AIエージェント, 比較, 選び方, Devin, Manus, ツール選定]
created: 2026-08-05
updated: 2026-08-05
---

# 主要AIエージェントの比較と選び方

## これは何か

「AIエージェントを入れたい」と言われたとき、**何を基準にどれを選ぶか**を1ページで判断できるようにする。
2026年時点で製品が乱立しており、名前は違うが同じことをするもの、
名前が似ているが用途が全く違うものが混在しているため、まず地図を作る。

各製品の詳細は個別ページに譲り、ここでは**横並びの比較と選定の判断軸**に集中する。

## 仕組み・背景

### まず3つのタイプに分ける

エージェント選定で最初に間違えやすいのが、**タイプの違う製品を同じ表で比べてしまう**ことである。

| タイプ | 何を任せるか | 代表例 |
|---|---|---|
| **A. コーディングエージェント** | コードを書く・直す・テストする | Claude Code、Codex、Antigravity、Devin |
| **B. 業務エージェント** | 調査・分析・資料作成・ファイル整理 | Claude Cowork、Manus、ChatGPT Agent |
| **C. 組み込み型エージェント** | 自社の業務フローに埋め込む | Dify / n8n のエージェント、自作(MCP・A2A) |

**A と B は「誰が使うか」で分かれる**(開発者か、それ以外の職種か)。
C は「既製品を使う」のではなく「自分で組む」話なので、比較軸がそもそも別になる
(→ [ノーコードでのAIエージェント構築](../part10-nocode-lowcode/nocode-ai-agent-building.md)、
[MCPの基本](../part09-api-development/mcp-basics.md))。

### 「エージェント」と呼ばれているが違うもの

| 呼び方 | 実態 | 置き場所 |
|---|---|---|
| GPTs / Gem / Copilot Agent | 設定でカスタマイズしたチャットボット。自律実行はしない | [Part 6](../part06-custom-ai/_index.md) |
| GitHub Copilot / Cursor の補完 | エディタ内の補完・チャット。人が主体 | [Part 8](../part08-specialized-ai-tools/_index.md) |
| ChatGPT Agent / スケジュールタスク | チャットツールに付いたエージェント機能 | [Part 3](../part03-ai-chat-tools/ai-chat-tools-agent-tasks-comparison.md) |
| Claude Code / Codex / Cowork | 委任型のエージェント製品 | このパート |

## 使いどころ・使い分け

### A. コーディングエージェントの比較(2026年8月時点)

| | [Claude Code](claude-code-basics.md) | [Codex](openai-codex-basics.md) | [Antigravity](google-antigravity-basics.md) | Devin |
|---|---|---|---|---|
| 提供元 | Anthropic | OpenAI | Google | Cognition |
| 中心UI | ターミナル | アプリ / CLI / クラウド | IDE + Agent Manager | Web / Slack |
| 並列実行 | サブエージェント | クラウドで多数並列 | Agent Manager で並列 | 複数セッション |
| ブラウザ操作 | 可(コンピュータ操作) | クラウド実行が中心 | **標準機能として前面** | 可 |
| モデル選択 | Claude | GPT系 | **Gemini / Claude / gpt-oss** | 内部モデル |
| 無料枠 | なし | あり(ChatGPT Free) | **あり** | なし |
| 課金の紐付け | Claude Pro $17 / Max $100・$200 | ChatGPT プラン(実質 $100〜200/人) | Google AI Pro $20 / Ultra $100・$200 | $20/月 + 従量(ACU) |
| 特徴的な課金 | サブスク定額 | クレジット(モデル別単価) | レート上限方式 | **ACU従量**(1 ACU ≒ 15分の作業) |

**Devin の従量課金は要注意**である。Core プランは月$20 + 1 ACU あたり $2.25 で、
典型的なバグ修正が 2〜3 ACU($4.50〜6.75)、複数ファイルにまたがる移行作業は 30 ACU 超
($67.50以上)に達しうる。Team プランは月$500 で 250 ACU 込み、超過分は 1 ACU $2。
**「1タスクいくら」が見えるのは予算管理上の利点だが、重い作業のコストが跳ねる**。

### B. 業務エージェントの比較(2026年8月時点)

| | [Claude Cowork](claude-cowork-basics.md) | Manus | [ChatGPT Agent](../part03-ai-chat-tools/chatgpt-agent-mode-feature.md) |
|---|---|---|---|
| 得意 | ローカルファイルを扱う業務 | 長時間の自律リサーチ | Web操作を伴う調べもの |
| ファイル操作 | **指定フォルダを読み書き** | クラウド上で生成 | ダウンロード中心 |
| 実行場所 | 手元のPC(Web・モバイルはベータ) | クラウド | クラウド(仮想ブラウザ) |
| 料金 | Claude Pro $17 以上に含まれる | $39/月 | ChatGPT プランに含まれる |
| 権限モデル | フォルダ・ツール単位で明示指定 | クラウド内で完結 | 仮想環境内で完結 |

**「手元のファイルを触らせるか」が最大の分岐点**である。
社内資料が自分のPCや共有ドライブにあるなら Cowork、
Web上の情報収集が主なら ChatGPT Agent や Manus が向く。

### 選定フロー

```
Q1. 任せたいのはコードを書く仕事か?
  ├ はい → Q2へ
  └ いいえ → 手元のファイルを触らせる必要があるか?
              ├ はい → Claude Cowork
              └ いいえ → ChatGPT Agent / Manus

Q2. すでに契約しているAIベンダーはあるか?
  ├ ChatGPT → Codex(追加契約不要)
  ├ Claude  → Claude Code
  ├ Google  → Antigravity(無料枠から試せる)
  └ なし    → Q3へ

Q3. どう管理したいか?
  ├ ターミナルで対話しながら      → Claude Code
  ├ GUIで並列エージェントを俯瞰    → Antigravity
  ├ クラウドで大量並列            → Codex
  └ 1タスクごとのコストを見たい    → Devin
```

### 判断軸として効くもの・効かないもの

| 効く軸 | 理由 |
|---|---|
| **既存契約との整合** | 追加契約・稟議が要らないだけで導入速度が変わる |
| **課金方式** | 定額(Claude / Google)か従量(Devin)かで予算の立て方が変わる |
| **権限モデルの粒度** | 社内の情報管理ルールを満たせるか |
| **レビュー体制に合うか** | 並列で大量に出されても、人が読めなければ意味がない |
| **データの取り扱い条件** | クラウド実行で自社コード・資料が外部に渡るか |

| 効かない軸 | 理由 |
|---|---|
| ベンチマークのスコア | 数か月で入れ替わる。自社の作業での再現性は別問題 |
| 「自律的に完遂できる」という宣伝 | どの製品もレビューは必要。差は出ない |
| 対応モデルの数 | 実際に使うのは1〜2種類に落ち着く |

## 実務での使い方

### 導入前に決めておく5項目

社内展開でつまずくのは製品選定ではなく運用ルールの不在である。以下は選定と同時に決める。

```
1. 権限: 承認なしで実行してよい操作の一覧(取り消せない操作は必ず承認)
2. 対象: エージェントに渡してよいデータの範囲(機密区分ごとに可否を明記)
3. コスト: 1人あたり月額の上限と、超過時の申請フロー
4. レビュー: 誰が何を確認してからマージ・提出するか
5. 記録: 何を実行させたかのログをどこに残すか
```

権限ポリシーの雛形は[AIエージェントとは何か](ai-agent-basics.md)に、
レビュー体制の設計は
[Human in the Loop(人間参加型)の業務設計](../part12-business-practice/human-in-the-loop-basics.md)にある。

### PoC の進め方

1. **1職種・1業務に絞る。** 「全社でエージェント活用」から始めると評価できない
2. **同じタスクを2製品で試す。** 自社のコードベース・資料での差は、ベンチマークでは分からない
3. **時間ではなくレビュー工数を測る。** 「AIが5分で終えた」より
   「人の確認に何分かかったか」が導入効果を決める
4. **失敗パターンを記録する。** どういう指示で外したかが、社内ガイドラインの中身になる

効果測定の枠組みは
[生成AI導入のROI測定・効果測定の考え方](../part12-business-practice/ai-roi-measurement.md)を参照。

## 注意点・よくある誤解

- **製品選定より運用設計のほうが効果を左右する。** どれを選んでも、権限とレビューが
  決まっていなければ「怖くて使えない」か「無審査で通して事故る」のどちらかになる
- **並列実行の本数を増やしても生産性は上がらない。** 律速は人のレビューである
- **無料枠の比較は導入判断に使えない。** 無料枠は試用向けで、業務利用では必ず有料前提になる
- **従量課金は「安い」とは限らない。** Devin のように1タスク単位で見えるのは管理上の利点だが、
  重い作業では定額プランより高くつくことがある
- **ベンダーを1社に統一する必要はない。** 開発は Claude Code、非開発職は Cowork、
  ChatGPT 契約があるチームは Codex、という併用は現実的な解である
- **この分野は数か月で変わる。** 2026年に入ってからも Gemini CLI の Antigravity CLI への統合、
  Antigravity の料金改定などが起きている。**半年前の比較記事は使えない**

## 最初の一歩

いま自社が契約しているAIベンダー(ChatGPT / Claude / Google)を確認し、
**その中に含まれているエージェントから試す**。追加契約なしで始められるぶん、
比較検討より先に「自社の仕事でどこまで使えるか」の実感を得られる。

## 関連トピック

- [AIエージェントとは何か](ai-agent-basics.md)
- [Claude Codeの基本](claude-code-basics.md)
- [OpenAI Codexの基本](openai-codex-basics.md)
- [Google Antigravityの基本](google-antigravity-basics.md)
- [Claude Coworkの基本](claude-cowork-basics.md)
- [主要AIチャットツールのエージェント機能・スケジュールタスク比較](../part03-ai-chat-tools/ai-chat-tools-agent-tasks-comparison.md)
- [コーディング支援AIの選び方・比較](../part08-specialized-ai-tools/coding-assistant-ai-comparison.md)
- [ノーコードでのAIエージェント構築(Dify・n8n・Makeでの実務例)](../part10-nocode-lowcode/nocode-ai-agent-building.md)
- [生成AI導入のROI測定・効果測定の考え方](../part12-business-practice/ai-roi-measurement.md)

## 更新履歴

### 2026-08-05: 初版執筆
- **内容**: エージェント製品をコーディング型・業務型・組み込み型の3タイプに分ける整理、
  「エージェント」と呼ばれるが実態が違うもの(GPTs・エディタ補完・チャット機能)の置き場所、
  Claude Code / Codex / Antigravity / Devin の比較表(UI・並列・課金方式・無料枠)、
  Devin の ACU 従量課金の具体額、Cowork / Manus / ChatGPT Agent の業務エージェント比較、
  選定フローチャート、効く判断軸と効かない判断軸、導入前に決める5項目、PoC の進め方を整理
- **出典**: [Claude Cowork(公式)](https://claude.com/product/cowork) /
  [Claude Code(公式)](https://claude.com/product/claude-code) /
  [Codex pricing(OpenAI)](https://learn.chatgpt.com/docs/pricing) /
  [Antigravity 料金改定(公式ブログ)](https://antigravity.google/blog/changes-to-antigravity-plans) /
  [Devin・Manus の料金は各社公開情報にもとづく比較記事を参照](https://www.firecrawl.dev/blog/best-ai-coding-agents)
