---
title: "主要AIチャットツールのCanvas/Artifacts機能比較(ChatGPT・Gemini・Claude・Copilot)"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [Canvas, Artifacts, ChatGPT, Gemini, Claude, Copilot, ツール比較, 文書作成, コーディング, 共同編集]
created: 2026-07-07
updated: 2026-07-07
---

# 主要AIチャットツールのCanvas/Artifacts機能比較(ChatGPT・Gemini・Claude・Copilot)

## これは何か

ChatGPT・Gemini・Claude・Microsoft Copilotはいずれも、通常のチャットの流れとは別に「文書・コード・簡易アプリなどの成果物」を専用の編集画面で育てる機能を備えている。名称も体験もツールごとに異なり(ChatGPTは「Canvas」、Claudeは「Artifacts」、Geminiは「Canvas」、Copilotは「Pages」)、「どのツールならチームで共同編集できるか」「どのツールならOfficeファイルにそのまま書き出せるか」を知らずに使うと、せっかく作った成果物を活用しきれないまま終わってしまう。本ページは4ツールを横並びで比較し、目的別にどれを選ぶべきかの判断材料をまとめる。ChatGPT Canvas単体の詳しい操作は[ChatGPTのCanvas機能](chatgpt-canvas-feature.md)を参照。

## 仕組み・背景

4ツールとも「チャットの応答を、後から参照・再編集しやすい形に切り出して保持する」という発想は共通しているが、切り出す対象と体験の作り込み方には次のような違いがある。

- **ChatGPT Canvas**(2024年10月公開): 長文やコードを画面右側の別パネルに表示し、範囲をハイライトして「ここだけ直して」と頼むと、その部分だけが書き換わる。文章の部分編集とバージョン履歴が中心的な価値。
- **Claude Artifacts**(2024年6月公開): コード・Webページ・SVG図・Mermaid図・Reactコンポーネントなど「まとまった1つの成果物」をAIが自動判定して右側パネルに切り出し、リアルタイムでプレビュー表示する。文章の手動編集より、AIに指示して作り直させる運用に重心がある。
- **Gemini Canvas**(2024年12月公開、Gemini 3世代のモデルで動作): 文書・コードに加えて、簡易アプリ・ゲーム・インフォグラフィック・スライドのプロトタイピングまで幅広く対応し、作成した内容をGoogleドキュメント・スプレッドシート・Colabノートブックへそのまま送れる、Google Workspaceとの連携が特徴。
- **Microsoft Copilot Pages**(2025年1月公開): チャットの回答を「Pagesで編集」ボタン一つでブロック単位の編集可能なページに変換する機能。ページはOneDrive上にLoopファイルとして自動保存され、リンク共有で複数人が同時に共同編集できる、チーム作業への統合が特徴。なお、これとは別に手描き・自由レイアウトのホワイトボード的な新機能「Copilot Canvas」(社内コード名「Project Firenze」)の開発が2026年に報じられているが、本ページ執筆時点ではリーク情報の域を出ておらず、正式なドキュメント機能としてはPagesが実務利用の対象になる。

つまり、ChatGPTとClaudeは「1つの会話の中で1つの成果物を仕上げる」ことに寄せた設計、GeminiとCopilotは「作った成果物を他の場所(Google Workspace/Microsoft 365)に持ち出す・チームで共有する」ことに寄せた設計、というのが4ツールの大まかな性格の違いである。

## 使いどころ・使い分け

### 4ツールの横並び比較表(2026年7月時点)

| | ChatGPT(Canvas) | Google Gemini(Canvas) | Claude(Artifacts) | Microsoft Copilot(Pages) |
|---|---|---|---|---|
| 表示位置 | チャット右側の別パネル(新モデルではチャット内に直接展開する「ライティングブロック/コードブロック」に統合中) | チャット右側の別パネル | チャット右側の別パネル | Copilot Chatとは別のページ(ブロック単位のドキュメント) |
| 起動方法 | 入力欄「+」→Canvas、自動起動、「canvasを開いて」等の指示 | プロンプト入力欄の「Canvas」ツールを選択、または自動起動 | まとまったコード・文書・図表をAIが生成すると自動で開く | 回答の下に出る「Pagesで編集」ボタンをクリック |
| 得意なコンテンツ | 長文・レポートの部分編集、コードのインライン実行 | 文書・コードに加え簡易アプリ・ゲーム・インフォグラフィック・スライドの試作 | コード・Webページ・SVG図・Mermaid図・Reactコンポーネントなど「動くもの」のプレビュー | 複数のチャット回答を1つの資料にまとめる、チームでの共同編集 |
| 編集方法 | 範囲をハイライト+指示、ショートカットボタン(仕上げ・読みやすさ調整など) | プロンプトで指示、生成後にブロック単位で手直し | 主にAIへの再指示で作り直し(手動編集より生成→確認の往復が基本) | ブロックをドラッグで並べ替え、テキストを直接編集、「提案された編集」でAIレビューも可能 |
| 保存・バージョン管理 | チャット内で版が記録され巻き戻し可能(会話の一部としての保存) | 生成物をGoogleドキュメント/スプレッドシート/Colabへ書き出して保存 | チャット内で版が記録され巻き戻し可能 | OneDriveにLoopファイルとして自動保存(会話から独立して残る) |
| 共同編集・共有 | リンクでの一般公開共有機能はなし(会話の共有機能のみ) | 生成物をGoogleドキュメント等に送った先で共同編集 | 公開(Publishing、リンクで誰でも閲覧・操作可)またはチーム内共有(Sharing)。埋め込みコード取得も可能 | リンク共有で複数人が同時にリアルタイム共同編集可能(チーム作業を最初から想定) |
| エクスポート先 | コピー&ペーストが基本 | Googleドキュメント・Googleスライド・Google Colab | 埋め込みコード、公開リンク | Word/PowerPoint形式での書き出し、Teams/Outlookでの共有 |
| 対応プラン(2026年7月時点) | Free/Plus/Pro/Team/Enterprise/Eduで無償利用可 | 全ユーザーが利用可能(無料プラン含む)。AI Pro/Ultraではより高性能なモデル・大きなコンテキストで利用可 | 基本利用(公開含む)はFreeプランを含め無償。MCP連携等の高度機能はPro/Max/Team/Enterpriseが必要 | Microsoft 365 Copilot(Business/Enterprise等の有償ライセンス)が前提。無料の個人向けCopilotでの提供範囲は変更されることがあるため利用前に要確認 |

### 判断基準

| やりたいこと | 向いているツール |
|---|---|
| 長文の提案書・報告書を、部分修正しながらChatGPTの流れの中で仕上げたい | ChatGPT Canvas |
| コード・Webページ・図表など「動かして確認したいもの」をその場でプレビューし、できたものを公開リンクで共有したい | Claude Artifacts |
| ドキュメントだけでなく簡易アプリ・インフォグラフィック・スライドまで試作し、Googleドキュメント/スプレッドシートに引き継ぎたい | Gemini Canvas |
| 複数人のチームで、AIとのやり取りから生まれた内容を1つの資料に育てて共同編集し、最終的にWord/PowerPointにしたい | Microsoft Copilot Pages |

判断の目安は「すでに使っているエコシステム」と「成果物をどこに持って行きたいか」。Google WorkspaceやMicrosoft 365など既存の業務基盤に成果物を持ち出したいならGemini/Copilot、チャットの中だけで完結する試作・レビューならChatGPT/Claudeが手早い。

## 実務での使い方

### 起動方法(画面の場所)

- **ChatGPT**: 入力欄左側の「+」ボタン→「Canvas」を選択、または既存の回答の鉛筆アイコン→「canvasで開く」。プロンプトに「canvasを開いて」と書くだけでも起動する
- **Gemini**: プロンプト入力欄の下にある「Canvas」ツールを選択してから指示を送るか、生成させたい文書・コードの内容を含む指示を送ると自動で開く。gemini.google.comまたはGeminiアプリで利用可能
- **Claude**: 通常のチャットでコード・文書・図表の生成を依頼するだけで、まとまった内容ならAIが自動でArtifactsパネルを開く。手動での強制オンは不要
- **Microsoft Copilot**: Copilot Chatで回答を受け取った後、回答下に表示される「Pagesで編集」ボタンをクリックすると、その内容がページ化される。ページはブロック単位で編集でき、上部の共有アイコンからリンクを発行してチームメンバーに送れる

### コピペで使える実例(チームでの資料共同編集を想定・Copilot Pages)

```
新製品の社内向け説明資料のたたき台を作成してください。
・対象読者: 営業部門
・含める項目: 製品概要、想定価格帯、競合との違い、FAQ(3問程度)
・分量: A4 1〜2枚相当

作成後、この内容をPagesで編集できる形にしてください。
```

Pages化した後は、上部の共有アイコンからリンクを発行し、チームメンバーに「このページに直接書き込んで」と伝えると、各自がブロック単位で追記・修正できる。

### コピペで使える実例(動くプロトタイプの確認・Claude Artifacts)

```
入力した2つの数値の税込み価格を計算する、シンプルなReactの
電卓アプリを作ってください。動作するプレビューも見せてください。
```

生成後にArtifactsパネル右上の「公開(Publish)」を選ぶと、リンクを知っている人なら誰でもその場で操作できる状態になる(Free/Pro/Maxプラン)。社内メンバーだけに限定したい場合はTeam/Enterpriseプランの「共有(Sharing)」機能を使う。

## 注意点・よくある誤解

- **「同じ機能」ではなく「重心が違う機能」**: 4つとも見た目は似ているが、ChatGPT/Claudeは「1回の会話の中で成果物を仕上げる」設計、Gemini/Copilotは「作った成果物を他システムへ持ち出す・チームで共有する」設計に寄っている。「Canvas系の機能ならどれも同じ」と考えて選ぶと、共同編集やエクスポート先で期待した結果にならないことがある
- **モデルによって体験が変わる(ChatGPT)**: 2026年時点でGPT-5.5系の新しいモデルでは、独立パネル型のCanvasから、チャット内蔵の「ライティングブロック/コードブロック」への統合が進んでいる。過渡期のため、モデル選択によってボタンの見え方が変わることがある
- **Artifactsの公開範囲を確認する(Claude)**: 「公開(Publishing)」はリンクを知っている人なら誰でも閲覧・操作できる状態になる。社外秘の内容を含む場合は、Team/Enterpriseプランの「共有(Sharing)」(組織内限定)を使うか、公開自体を避ける
- **Copilot Canvas(Project Firenze)とPagesを混同しない**: 2026年に報じられている手描き・自由レイアウトのホワイトボード機能「Copilot Canvas」は、本ページで扱う文書化機能の「Copilot Pages」とは別の取り組みで、執筆時点ではリーク情報の域を出ていない。実務で今使えるのはPagesである点に注意する
- **コード実行・プレビューは簡易確認用**: いずれのツールもパネル内のコード実行・プレビューはサンドボックス上の簡易的な動作確認であり、本番相当の環境検証やセキュリティレビューの代わりにはならない
- **業務データを貼る際はプランのデータ利用設定を確認**: これらの機能自体に固有のセキュリティ機能があるわけではなく、通常のチャットと同じデータ取り扱いルールが適用される。社外秘の資料を扱う場合は法人プランの契約内容や、個人プランでのデータ利用オプトアウト設定を事前に確認する

## 最初の一歩

今すでに使っているAIチャットツール1つを選び、直近で作った長めの文章・コードを、そのツールのCanvas/Artifacts/Pages機能に切り出してみる。その上で、他のメンバーに共有したりOffice/Googleファイルに書き出したりできるかを実際に試し、自分の業務フローに合うかを確認する。

## 関連トピック

- [ChatGPTのCanvas機能](chatgpt-canvas-feature.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [Claude(Anthropic)の基本](claude-basics.md)
- [Microsoft Copilotの基本](microsoft-copilot-basics.md)
- [Claude(Anthropic)の「プロジェクト」機能の基本](../part06-custom-ai/claude-projects-basics.md)

## 更新履歴

### 2026-07-07: 初版執筆
- **内容**: ChatGPT Canvas・Gemini Canvas・Claude Artifacts・Microsoft Copilot Pagesの4機能を、表示位置・起動方法・得意なコンテンツ・共同編集/共有・エクスポート先・対応プランで横並び比較。目的別の判断基準、画面操作の手順、共同編集とプロトタイプ確認それぞれのコピペ用プロンプト例、Copilot Canvas(Project Firenze)との違いなどの注意点を執筆
- **出典**: [Introducing canvas | OpenAI](https://openai.com/index/introducing-canvas/)、[What is the canvas feature in ChatGPT and how do I use it? | OpenAI Help Center](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it)、[Gemini Canvas — write, code, & create in one space with AI | Google](https://gemini.google/overview/canvas/)、[Canvas でドキュメントやアプリなどを作成する | Gemini アプリ ヘルプ](https://support.google.com/gemini/answer/16047321)、[What are artifacts and how do I use them? | Claude Help Center](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)、[Publish and share artifacts | Claude Help Center](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts)、[Get started with Microsoft 365 Copilot Pages | Microsoft Support](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-pages)、[Microsoft Copilot Canvasのリーク報道 | Windows Latest](https://www.windowslatest.com/2026/03/01/microsofts-copilot-canvas-leak-reveals-an-ai-powered-whiteboard-with-image-generation-ai-streaming-and-more/)
