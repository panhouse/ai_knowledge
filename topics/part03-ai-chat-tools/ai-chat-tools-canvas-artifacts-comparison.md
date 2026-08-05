---
title: "主要AIチャットツールのCanvas/Artifacts機能比較(ChatGPT・Gemini・Claude・Copilot)"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [Canvas, Artifacts, ChatGPT, Gemini, Claude, Copilot, ツール比較, 文書作成, コーディング, 共同編集]
created: 2026-07-07
updated: 2026-08-05
---

# 主要AIチャットツールのCanvas/Artifacts機能比較(ChatGPT・Gemini・Claude・Copilot)

## これは何か

ChatGPT・Gemini・Claude・Microsoft Copilotはいずれも、通常のチャットの流れとは別に「文書・コード・簡易アプリなどの成果物」を専用の編集画面で育てる機能を備えている。名称も体験もツールごとに異なり(Claudeは「Artifacts」、Geminiは「Canvas」、Copilotは「Pages」)、「どのツールならチームで共同編集できるか」「どのツールならOfficeファイルにそのまま書き出せるか」を知らずに使うと、せっかく作った成果物を活用しきれないまま終わってしまう。加えてこの分野は変化が速く、**ChatGPTの独立パネル型Canvasは2026年5月に主力モデルから廃止され、チャット内蔵の「ライティングブロック/コードブロック」に置き換わった**。本ページは現行の4ツールを横並びで比較し、目的別にどれを選ぶべきかの判断材料をまとめる。

## 仕組み・背景

4ツールとも「チャットの応答を、後から参照・再編集しやすい形に切り出して保持する」という発想は共通しているが、切り出す対象と体験の作り込み方には次のような違いがある。

- **ChatGPT(旧Canvas→ライティング/コードブロックへ移行、2024年10月公開〜2026年5月廃止)**: 長文やコードを画面右側の別パネルに表示し、範囲をハイライトして「ここだけ直して」と頼むと、その部分だけが書き換わる機能として2024年に登場した。しかし2026年5月28日、OpenAIはGPT-5.5 Instant/Thinkingへのモデル更新に合わせてCanvasパネルを廃止し、同じ役割をチャット内に直接表示される「ライティングブロック」「コードブロック」に統合した。スマホ・タブレット・Web・デスクトップで表示が揃わない独立パネルの保守負担を減らすことが理由とされる。旧モデル(o3など)を有効にしたレガシーアクセスでは従来のCanvasパネルがまだ残っているが、o3自体が2026年8月26日に廃止予定のため、実務上は「後継のブロック機能を前提に考える」段階に入っている
- **Claude Artifacts**(2024年6月公開、以降大幅拡張): コード・Webページ・SVG図・Mermaid図・Reactコンポーネントなど「まとまった1つの成果物」をAIが自動判定して右側パネルに切り出し、リアルタイムでプレビュー表示する。2025年後半以降、パネル内で完結する静的な成果物から一歩進み、成果物自身がClaudeのAPIを呼び出して動く「AIパワードArtifacts」、20MBまでのデータを保存できる永続ストレージ、Googleカレンダー・Gmail・Slackなどの外部サービスに接続するMCP(Model Context Protocol、AIが外部ツール・データにつながるための標準規格)連携が順次追加され、簡易的なミニアプリ基盤としての性格が強くなった。2026年4月には、開いた時点の最新データで自動更新される「Live Artifacts」もデスクトップアプリ向けに追加されている
- **Gemini Canvas**(2024年12月公開、Gemini 3世代のモデルで動作): 文書・コードに加えて、簡易アプリ・ゲーム・インフォグラフィック・スライドのプロトタイピングまで幅広く対応し、作成した内容をGoogleドキュメント・スプレッドシート・Colabノートブックへそのまま送れる、Google Workspaceとの連携が特徴。2026年に入り、Google検索の「AIモード」内でもCanvasが使えるようになったほか、Google Classroomへの共有ボタンが追加されるなど、教育・検索領域への展開も進んでいる
- **Microsoft Copilot Pages**(2025年1月公開): チャットの回答を「Pagesで編集」ボタン一つでブロック単位の編集可能なページに変換する機能。ページはOneDrive上にLoopファイルとして自動保存され、リンク共有で複数人が同時に共同編集できる、コメント・@メンション・PowerPoint生成などチーム作業への統合が特徴。なお、これとは別に、消費者向けCopilotをサイドバーから「常駐するワークスペース」へ拡張する新機能「Copilot Canvas」が2026年6月のMicrosoft Build 2026で公開デモされた。ファイル・画像・コードスニペット・Webウィジェットをドロップして扱える点や、外部アプリのプラグインマーケットプレイスと組み合わせる構想が示されているが、これは本ページで扱う文書共同編集ツール「Pages」とは別の取り組みであり、業務での文書作成・共同編集に使うのは引き続きPagesである

つまり、ClaudeとGeminiは「1つのパネルの中で成果物を仕上げ、動かし、必要なら外部に持ち出す」ことに寄せた設計、Copilotは「作った成果物をチームで共有・共同編集する」ことに寄せた設計であるのに対し、ChatGPTは独立パネルという体験自体をやめてチャットに溶け込ませる方向へ舵を切った、というのが2026年8月時点での4ツールの大まかな性格の違いである。

## 使いどころ・使い分け

### 4ツールの横並び比較表(2026年8月時点)

| | ChatGPT(旧Canvas→ライティング/コードブロック) | Google Gemini(Canvas) | Claude(Artifacts) | Microsoft Copilot(Pages) |
|---|---|---|---|---|
| 表示位置 | チャット内に直接展開する「ライティングブロック/コードブロック」(独立パネル型Canvasは主力モデルで廃止済み) | チャット右側の別パネル | チャット右側の別パネル | Copilot Chatとは別のページ(ブロック単位のドキュメント) |
| 起動方法 | 長文・コードを含む回答を生成すると自動でブロック表示される。旧Canvasパネルはレガシーモデル(o3、2026年8月26日廃止予定)を有効にした場合のみ利用可 | プロンプト入力欄の「Canvas」ツールを選択、または自動起動 | まとまったコード・文書・図表をAIが生成すると自動で開く | 回答の下に出る「Pagesで編集」ボタンをクリック |
| 得意なコンテンツ | 長文・レポートのインライン編集、コードのインライン実行(パネル分離はしない) | 文書・コードに加え簡易アプリ・ゲーム・インフォグラフィック・スライドの試作 | コード・Webページ・SVG図・Mermaid図・Reactコンポーネントなど「動くもの」のプレビュー。AI呼び出し・外部サービス連携を組み込んだミニアプリも作成可 | 複数のチャット回答を1つの資料にまとめる、チームでの共同編集 |
| 編集方法 | ブロック内を直接編集、AIへの再指示で書き換え | プロンプトで指示、生成後にブロック単位で手直し | 主にAIへの再指示で作り直し(手動編集より生成→確認の往復が基本) | ブロックをドラッグで並べ替え、テキストを直接編集、「提案された編集」でAIレビューも可能 |
| 保存・バージョン管理 | チャット内で版が記録され巻き戻し可能(会話の一部としての保存) | 生成物をGoogleドキュメント/スプレッドシート/Colabへ書き出して保存 | チャット内で版が記録され巻き戻し可能。Live Artifactsは開くたびに最新データへ自動更新 | OneDriveにLoopファイルとして自動保存(会話から独立して残る)。過去バージョンへの復元も可能 |
| 共同編集・共有 | リンクでの一般公開共有機能はなし(会話の共有機能のみ) | 生成物をGoogleドキュメント等に送った先で共同編集 | 公開(Publishing、リンクで誰でも閲覧・操作可)またはチーム内共有(Sharing)。埋め込みコード取得も可能 | リンク共有で複数人が同時にリアルタイム共同編集可能。コメント・@メンションにも対応 |
| エクスポート先 | コピー&ペーストが基本 | Googleドキュメント・Googleスライド・Google Colab | 埋め込みコード、公開リンク | Word/PowerPoint形式での書き出し、Teams/Outlookでの共有 |
| 対応プラン(2026年8月時点) | Free/Plus/Pro/Team/Enterprise/Eduで無償利用可(旧Canvasのレガシーアクセスは有償プランのみ・期間限定) | 全ユーザーが利用可能(無料プラン含む)。有償のAI Plus/AI Pro/AI Ultraではより高性能なモデル・大きなコンテキストで利用可 | 基本的な成果物の作成・公開(HTML/React/SVG/Mermaid/コード/文書など)はFreeプランを含め無償。永続ストレージ・AIパワードArtifacts・Live ArtifactsはPro/Max/Team/Enterpriseが必要 | Microsoft 365 Copilot(Business/Enterprise等の有償ライセンス)が前提。無料の個人向けCopilotでの提供範囲は変更されることがあるため利用前に要確認 |

### 判断基準

| やりたいこと | 向いているツール |
|---|---|
| 長文の提案書・報告書を、ChatGPTのチャットの流れの中でインラインに仕上げたい | ChatGPT(ライティングブロック) |
| コード・Webページ・図表など「動かして確認したいもの」をその場でプレビューし、できたものを公開リンクで共有したい。外部サービスと連携するミニアプリまで作りたい | Claude Artifacts |
| ドキュメントだけでなく簡易アプリ・インフォグラフィック・スライドまで試作し、Googleドキュメント/スプレッドシートに引き継ぎたい | Gemini Canvas |
| 複数人のチームで、AIとのやり取りから生まれた内容を1つの資料に育てて共同編集し、最終的にWord/PowerPointにしたい | Microsoft Copilot Pages |

判断の目安は「すでに使っているエコシステム」と「成果物をどこに持って行きたいか」。Google WorkspaceやMicrosoft 365など既存の業務基盤に成果物を持ち出したいならGemini/Copilot、チャットの中だけで完結する試作・レビューならChatGPT/Claudeが手早い。なお「独立したパネルでじっくり編集したい」という用途は、現時点ではGemini CanvasかClaude Artifactsの2択になっている点に注意(ChatGPTは廃止、Copilot Pagesは別ページ遷移が前提)。

## 実務での使い方

### 起動方法(画面の場所)

- **ChatGPT**: 通常のチャットで長文・コードの生成を依頼するだけで、回答内に「ライティングブロック」「コードブロック」として表示される。以前のような「+」ボタンからのCanvas起動は主力モデル(GPT-5.5系)では廃止済み。もし従来型の独立パネルが必要な場合は、設定でレガシーモデル(o3等)を有効化する必要があるが、これらのモデル自体が順次廃止されるため長期利用は前提にしない
- **Gemini**: プロンプト入力欄の下にある「Canvas」ツールを選択してから指示を送るか、生成させたい文書・コードの内容を含む指示を送ると自動で開く。gemini.google.comまたはGeminiアプリ、Google検索の「AIモード」でも利用可能
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

生成後にArtifactsパネル右上の「公開(Publish)」を選ぶと、リンクを知っている人なら誰でもその場で操作できる状態になる(Freeプランを含め全プランで無償)。社内メンバーだけに限定したい場合はTeam/Enterpriseプランの「共有(Sharing)」機能を使う。なお、外部データと連携させたり、開くたびに最新情報へ更新される「Live Artifacts」を作る場合はPro/Max/Team/Enterpriseプラン(デスクトップアプリ)が必要になる。

## 注意点・よくある誤解

- **「同じ機能」ではなく「重心も存続状況も違う機能」**: 見た目が似ていても、Claude/Geminiは独立パネルでの試作・共同編集に寄せた設計、Copilotは資料をチームで育てる設計、ChatGPTはパネル自体を廃止してチャットに溶け込ませる方向、と2026年時点で方向性が分かれている。「Canvas系の機能ならどれも同じ」と考えて選ぶと、共同編集やエクスポート先、そもそも独立パネルの有無で期待した結果にならないことがある
- **ChatGPT Canvasは実質的に廃止済み(要確認)**: 2026年5月28日のGPT-5.5更新でCanvasパネルは主力モデルから削除され、チャット内蔵の「ライティングブロック/コードブロック」に置き換わった。レガシーモデル経由でのCanvasアクセスも、o3が2026年8月26日に廃止されると事実上使えなくなる見込み。過去にCanvasの使い方を案内した資料・社内マニュアルがあれば、この移行を踏まえて更新が必要
- **Artifactsの公開範囲を確認する(Claude)**: 「公開(Publishing)」はリンクを知っている人なら誰でも閲覧・操作できる状態になる。社外秘の内容を含む場合は、Team/Enterpriseプランの「共有(Sharing)」(組織内限定)を使うか、公開自体を避ける
- **ClaudeのAI連携機能はプラン差・コスト差が大きい**: 永続ストレージ・AIパワードArtifacts・MCP連携・Live Artifactsは無償のFreeプランでは使えず、Pro以上が前提。加えてAIパワードArtifactsは閲覧者ごとにAPI呼び出しが発生するため、社外に広く公開すると想定外のコストにつながりうる。社外公開する成果物は「静的なプレビューで十分か、動的な呼び出しが本当に必要か」を作る前に見極める
- **Copilot Canvas(Build 2026で公開デモ)とPagesを混同しない**: 2026年6月のMicrosoft Build 2026で紹介された「Copilot Canvas」は、消費者向けCopilotをサイドバーから常駐ワークスペースへ拡張する構想であり、本ページで扱う文書共同編集機能の「Copilot Pages」とは別の取り組み。実務で今使えるのはPagesである点に注意する
- **コード実行・プレビューは簡易確認用**: いずれのツールもパネル内・ブロック内のコード実行・プレビューはサンドボックス上の簡易的な動作確認であり、本番相当の環境検証やセキュリティレビューの代わりにはならない
- **業務データを貼る際はプランのデータ利用設定を確認**: これらの機能自体に固有のセキュリティ機能があるわけではなく、通常のチャットと同じデータ取り扱いルールが適用される。社外秘の資料を扱う場合は法人プランの契約内容や、個人プランでのデータ利用オプトアウト設定を事前に確認する

## 最初の一歩

今すでに使っているAIチャットツール1つを選び、直近で作った長めの文章・コードを、そのツールのCanvas/Artifacts/Pages(またはChatGPTならライティングブロック/コードブロック)に切り出してみる。その上で、他のメンバーに共有したりOffice/Googleファイルに書き出したりできるかを実際に試し、自分の業務フローに合うかを確認する。

## 関連トピック

- [ChatGPTのCanvas機能](chatgpt-canvas-feature.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [Claude(Anthropic)の基本](claude-basics.md)
- [Microsoft Copilotの基本](microsoft-copilot-basics.md)
- [Claude(Anthropic)の「プロジェクト」機能の基本](../part06-custom-ai/claude-projects-basics.md)

## 更新履歴

### 2026-08-05: 各ツールの最新状況に合わせて全面改訂
- **内容**: ChatGPTの独立パネル型Canvasが2026年5月28日のGPT-5.5更新で廃止され、チャット内蔵の「ライティングブロック/コードブロック」に統合されたことを反映。Claude Artifactsの永続ストレージ・AIパワードArtifacts・MCP連携・Live Artifacts(2026年4月)などプラン別の新機能、Gemini CanvasのGoogle検索AIモード・Google Classroom連携、Microsoft Build 2026で公開デモされた「Copilot Canvas」(Pagesとは別物)の位置付けを追記し、比較表・判断基準・注意点を全面的に更新
- **出典**: [OpenAI Drops Canvas From GPT-5.5, Bakes Writing and Coding Into Chat | Krasa.ai](https://www.krasa.ai/news/openai-gpt-5-5-instant-writing-coding-blocks-canvas-removed-may-2026)、[ChatGPT Canvas sunset: key dates, impacts, migration guidance | AI CERTs News](https://www.aicerts.ai/news/chatgpt-canvas-sunset-key-dates-impacts-migration-guidance/)、[Model Release Notes | OpenAI Help Center](https://help.openai.com/en/articles/9624314-model-release-notes)、[Turn ideas into interactive AI-powered apps | Claude by Anthropic](https://claude.com/blog/build-artifacts)、[Are Claude Artifacts Free? Free vs Pro Features (2026) | ShareDuo](https://www.shareduo.com/blog/claude-artifacts-free)、[Use live artifacts in Claude Cowork | Claude Help Center](https://support.claude.com/en/articles/14729249-use-live-artifacts-in-claude-cowork)、[Educators and students can now share Gemini Canvas creations directly to Google Classroom | Google Workspace Updates](https://workspaceupdates.googleblog.com/2026/06/educators-and-students-can-now-share-Gemini-Canvas-creations-directly-to-Google-Classroom.html)、[Gemini's Canvas in AI Mode Available in Google Search in US | AI Business](https://aibusiness.com/generative-ai/gemini-s-canvas-in-ai-mode-available-in-us)、[Microsoft Copilot Is Now a Super App | ChatForest](https://chatforest.com/builders-log/microsoft-copilot-super-app-plugin-marketplace-builder-guide/)

### 2026-07-07: 初版執筆
- **内容**: ChatGPT Canvas・Gemini Canvas・Claude Artifacts・Microsoft Copilot Pagesの4機能を、表示位置・起動方法・得意なコンテンツ・共同編集/共有・エクスポート先・対応プランで横並び比較。目的別の判断基準、画面操作の手順、共同編集とプロトタイプ確認それぞれのコピペ用プロンプト例、Copilot Canvas(Project Firenze)との違いなどの注意点を執筆
- **出典**: [Introducing canvas | OpenAI](https://openai.com/index/introducing-canvas/)、[What is the canvas feature in ChatGPT and how do I use it? | OpenAI Help Center](https://help.openai.com/en/articles/9930697-what-is-the-canvas-feature-in-chatgpt-and-how-do-i-use-it)、[Gemini Canvas — write, code, & create in one space with AI | Google](https://gemini.google/overview/canvas/)、[Canvas でドキュメントやアプリなどを作成する | Gemini アプリ ヘルプ](https://support.google.com/gemini/answer/16047321)、[What are artifacts and how do I use them? | Claude Help Center](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)、[Publish and share artifacts | Claude Help Center](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts)、[Get started with Microsoft 365 Copilot Pages | Microsoft Support](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-pages)、[Microsoft Copilot Canvasのリーク報道 | Windows Latest](https://www.windowslatest.com/2026/03/01/microsofts-copilot-canvas-leak-reveals-an-ai-powered-whiteboard-with-image-generation-ai-streaming-and-more/)
