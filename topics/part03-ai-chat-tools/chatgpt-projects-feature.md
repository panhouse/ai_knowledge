---
title: ChatGPTの「プロジェクト」機能
part: 3
chapter: 第3章 記憶・文脈の管理
tags: [ChatGPT, プロジェクト, Projects, カスタム指示, ファイル管理, ワークスペース]
created: 2026-07-06
updated: 2026-09-14
---

# ChatGPTの「プロジェクト」機能

## これは何か

プロジェクト(Projects)は、特定の案件・クライアント・テーマごとに「チャット」「参照ファイル」「カスタム指示」をひとまとめにして保管できるワークスペース機能。通常のチャットは1件ずつ独立していて、同じ資料を毎回アップロードし直したり、同じ前提を毎回説明し直したりする手間が発生するが、プロジェクトを使うとその手間をなくし、関連する会話を1か所に集約して迷子にならずに管理できる。

## 仕組み・背景

プロジェクトは「フォルダ+専属アシスタント」のようなイメージの機能で、以下の3要素を1つの箱にまとめる。

- **チャット**: そのプロジェクト内で開始した会話、または既存チャットから移動した会話
- **ファイル(Sources)**: PDF・Word・Excel・コードなど、プロジェクトにひもづくアップロード資料。一度アップロードすれば、そのプロジェクト内のすべてのチャットから参照できる
- **カスタム指示(Instructions)**: そのプロジェクト専用の口調・前提条件・出力形式の指定

重要な仕組みとして、プロジェクト内の指示・ファイルは**そのプロジェクトの外には影響しない**。逆に、アカウント全体に設定するグローバルな「カスタム指示」よりも、プロジェクト内で個別に設定した指示の方が優先される。また各プロジェクトは「デフォルト(アカウント全体の記憶を参照)」と「プロジェクト限定(project-only)」のどちらかの記憶モードを持ち、project-only を選ぶとプロジェクト内の会話だけを踏まえて回答し、他のプロジェクトや通常チャットの記憶・保存済みメモリは参照しない(逆にproject-only側の記憶が外に漏れ出すこともない)。2026年8月14日のアップデート以降は、共有していない既存プロジェクトであればこのモードを作成後からいつでも設定画面で切り替えられるようになり、以前のように「project-onlyにするには新規プロジェクトを作り直す」必要はなくなった(共有プロジェクトは引き続きproject-only固定、現時点ではWeb版のみ対応)。

## 使いどころ・使い分け

「普通のチャット」「プロジェクト」「カスタムGPT(GPTs)」はいずれもChatGPTをカスタマイズする手段だが、目的が異なる。

| 観点 | 普通のチャット | プロジェクト | カスタムGPT(GPTs) |
|---|---|---|---|
| 主な用途 | その場限りの単発の質問・作業 | 特定の案件・クライアント・継続業務を1か所にまとめる「引き出し」 | 特定の役割に特化した「専用アシスタント」を作る |
| 資料の扱い | チャットごとに毎回アップロードし直す | プロジェクトに一度上げれば全チャットで共有 | GPT作成時に「知識」として登録し、そのGPTの全チャットで共有 |
| 指示の適用範囲 | 直前のプロンプト、またはアカウント全体のカスタム指示 | そのプロジェクト内の全チャットに適用(グローバル指示より優先) | そのGPTの全チャットに適用 |
| 共有・配布 | 不可(個人利用) | 「共有プロジェクト(Shared Projects)」で特定の相手・組織メンバーと共同編集できる(2025年10月以降、Free/Plus/Go/Proは招待制、Business/Enterprise/Eduはワークスペースメンバー向けリンク共有) | GPTストアで社内外に配布・公開できる |
| 向いている場面 | 継続性のない雑多な質問、ちょっとした下書き | 「A社案件」「〇〇プロジェクトの議事録一式」など、資料と会話が積み上がっていく継続業務 | 「見積書レビュー専用」など、繰り返し使う定型タスクを他人にも配りたい場合 |

判断の目安はシンプルで、**「資料と会話が時間とともに積み上がる継続案件」ならプロジェクト**、**「同じ動作をするツールとして人に配りたい」ならカスタムGPT**、**「一回きりの相談」なら普通のチャット**、と考えるとよい。両者は排他的ではなく、プロジェクト内のチャットで `@` を使えばそのチャット限りでカスタムGPTを呼び出すこともできる。ただし逆にカスタムGPTの画面から直接始めたチャットは通常の「最近のチャット」側に残り、後からプロジェクトへ移動することはできない点に注意。

## 実務での使い方

### 対応プラン(2026年9月時点)

プロジェクト機能自体は2025年9月にFree(無料)プランにも開放され、現在はFreeを含む全プランで利用できる。プランによる違いは主に「1プロジェクトあたりのアップロードできるファイル数」と「共有プロジェクトに招待できる人数」で、以下の上限が確認できる。

| プラン | 1プロジェクトあたりのファイル数上限 | 共有プロジェクトの招待人数上限 |
|---|---|---|
| Free | 5ファイル | 5人 |
| Plus / Go / Edu | 25ファイル | 10人 |
| Pro / Business(旧Team) / Enterprise | 40ファイル | 100人 |

なお1回のアップロード操作でまとめて追加できるのは最大10ファイルまでで、上限までは複数回に分けてアップロードする必要がある。ファイル自体には、1ファイルあたり512MB、テキスト・文書ファイルは1ファイルあたり最大200万トークン、画像は1枚20MBといった個別の上限もある。数値は改定が多いため、大量の資料を扱う前には[OpenAI公式のファイルアップロードFAQ](https://help.openai.com/en/articles/8555545-file-uploads-faq)で最新値を確認するとよい。

### 作成手順(目安)

1. ChatGPT(Web・デスクトップアプリ)を開き、左側サイドバーの「プロジェクト」欄にある「+」(新規作成)をクリック
2. プロジェクト名を入力して作成する(名前は「クライアント名+案件内容+時期」のように具体的にすると後で探しやすい。例:「A社_オンボーディング資料改訂_2026Q3」)
3. プロジェクト名の右にある設定アイコン(歯車マーク、または「…」の3点メニュー)から「Instructions(指示)」を開き、そのプロジェクト専用の前提・口調・出力形式を記入する
4. 「ファイルを追加する(Add files/Sources)」からPDF・Excel・Word・コードなどをドラッグ&ドロップでアップロードする
5. 以後、そのプロジェクト内で新規チャットを開始すると、自動的に手順3・4の指示とファイルを踏まえて回答が返ってくる
6. 既存のチャットをプロジェクトに移したい場合は、チャット一覧からそのチャットを対象プロジェクトへドラッグ、またはチャットメニューから「プロジェクトに移動」を選ぶ(カスタムGPTの画面から直接開始したチャットは対象外で、後からプロジェクトへ移せない)
7. プロジェクトを切り替えるときは、サイドバーのプロジェクト一覧から対象プロジェクト名をクリックするだけでよい(会話・ファイル・指示はプロジェクトごとに独立して保持される)
8. 他の人と共同編集したい場合は、プロジェクト名の右の「共有(Share)」から相手をメールアドレスや共有リンクで招待する(Free/Plus/Go/Proは個人を招待、Business/Enterprise/Eduはワークスペースのメンバー向けにリンクを発行)。招待時に「編集(指示の変更・ファイルの追加削除・他メンバーの招待が可能)」と「チャットのみ(閲覧・会話は可だが招待や指示変更は不可)」の2段階の権限を選べる

### プロジェクトと連携するエージェント機能「ChatGPT Work」(2026年9月時点)

2026年7月9日、OpenAIは新モデル世代「GPT-5.6」とあわせて、複数時間にわたる作業をプロジェクトの文脈を踏まえて代行するエージェント機能「**ChatGPT Work**」を発表した。プロジェクト内で「チャット」として質問するか、「Work」として長時間タスクを任せるかを選べ、Work側のスレッドもそのプロジェクトのファイル・指示・(project-only設定なら)プロジェクト記憶を踏まえて動く。プロジェクトはデスクトップアプリにも表示され、Workのスレッドは Web・モバイル・デスクトップ間で同期される。

その後の拡張として、作業内容を承認前に確認できる「Plan mode(実行計画のプレビュー)」、Workの成果物をURLで共有できるインタラクティブなWebアプリとして公開する「Sites」(パブリックベータ)が追加され、2026年7月14日には**プロジェクト・チャット・画像・ファイルを横断して検索できる統合検索**が全プランに無料展開されるなど、プロジェクトをまたいだ情報の見つけやすさも改善されている。エージェント機能自体の詳しい使い方・料金は[ChatGPTのエージェント機能(ChatGPT Agent)とスケジュールタスク(Tasks)](chatgpt-agent-mode-feature.md)を参照。

### コピペで使えるプロジェクト指示の例

```
## このプロジェクトについて
A社向けの月次レポート作成専用プロジェクトです。

## 前提
- 読み手はA社の経営層(非エンジニア)
- 数値は必ず前月比・前年同月比をセットで示す
- 専門用語には初出で一言説明を付ける

## 出力形式
- 見出し+箇条書きを基本とする
- 結論を冒頭に書く(結論→根拠の順)
- 「ですます調」で統一する
```

### ツール横断の対応付け

| 概念 | ChatGPT | Claude | Gemini |
|---|---|---|---|
| 案件単位のワークスペース | プロジェクト(サイドバーの「+」で作成) | Projects(claude.ai/projects → 「+ 新規プロジェクト」) | 直接対応する機能はなし。Gem(後述)が近いが「資料+会話の蓄積」という設計ではなく「役割特化のアシスタント」寄り |
| プロジェクト単位の指示 | Instructions欄 | 「カスタム指示」欄 | Gemのカスタム指示欄 |
| プロジェクト単位の参照資料 | ファイル(Sources)欄 | 「ナレッジ」欄 | Gemの知識(ファイルやGoogleドライブ資料)欄、またはNotebookLMのノートブック |
| 役割特化・配布用の専用アシスタント | カスタムGPT(GPTs、GPTストアで配布可) | 該当なし(Projects+Skillsで代替) | Gem(gemini.google.com → 「Gemを作成」) |

Claudeのプロジェクト機能の詳細は「[Claude(Anthropic)の基本](claude-basics.md)」、カスタムGPTの作り方は「[GPTs(カスタムGPT)作成の基本](../part06-custom-ai/gpts-creation-basics.md)」を参照。

## 注意点・よくある誤解

- **「共有」は明示的な操作が必要**: 2025年10月以降はFree/Plus/Go/Proでも共有プロジェクトが使えるが、初期状態のプロジェクトは自分専用。共有するには自分で「共有」から相手を招待する操作が必要で、招待していない相手には見えない。またカスタムGPTのようにGPTストアで不特定多数に配布する機能ではなく、あくまで招待した特定の相手・組織メンバーとの共同作業用
- **プロジェクトの指示はグローバルなカスタム指示より優先される**: アカウント全体のカスタム指示と矛盾する内容をプロジェクトの指示に書くと、そのプロジェクト内ではプロジェクト側が勝つ。「思った通りの回答が返ってこない」と感じたらプロジェクト側の指示を確認する
- **古い資料を放置しない**: 資料が改訂されたのに古いバージョンをプロジェクトに残しておくと、AIがどちらを参照すべきか判断できず精度が落ちる。ファイル名に版数・日付を入れ、古い版は削除する運用にする
- **ファイル数上限は無料プランで特に厳しい(5ファイル)**: 大量の資料を扱う業務ではPlus以上へのアップグレードを検討する
- **プロジェクトを削除すると中身も削除される**: チャット・ファイル・指示はプロジェクトに紐づいているため、プロジェクトごと削除すると復元できない場合がある。重要な会話は事前に別途保存しておく

## 最初の一歩

現在担当している案件や継続業務を1つ選び、ChatGPTでプロジェクトを新規作成して、その案件でよく使う資料を1つアップロードし、簡単な前提(口調・読み手など)をInstructionsに書いてみる。

## 関連トピック

- [GPTs(カスタムGPT)作成の基本](../part06-custom-ai/gpts-creation-basics.md)
- [Claude(Anthropic)の基本](claude-basics.md)
- [ChatGPTの初期設定とカスタム指示の書き方](./chatgpt-custom-instructions.md)
- [ChatGPTのエージェント機能(ChatGPT Agent)とスケジュールタスク(Tasks)](chatgpt-agent-mode-feature.md)

## 更新履歴

### 2026-09-14: 共有プロジェクト・プロジェクト記憶の切り替え・ChatGPT Workの拡張を反映して最新化
- **内容**: 「共有プロジェクト(Shared Projects)」が2025年10月以降Free/Plus/Go/Proにも拡大され招待制で共同編集できる点(Business/Enterprise/Eduはワークスペースリンク共有)、共有プロジェクトの招待人数上限(Free 5人/Plus・Go 10人/Pro・Business・Enterprise 100人)、1回のアップロードは最大10ファイルまでという制限、2026年8月14日以降は既存の非共有プロジェクトでも「デフォルト/project-only」の記憶モードを作り直さずに切り替えられるようになった点、ChatGPT Workの拡張(Plan mode、Webアプリを公開する「Sites」ベータ、2026年7月のプロジェクト横断統合検索)、プロジェクト内でのカスタムGPT呼び出し(`@`メンション)の挙動を反映し、使い分け表・注意点・実務手順を書き換え
- **出典**: [OpenAI Help Center: Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)、[OpenAI: More ways to work with your team and tools in ChatGPT](https://openai.com/index/more-ways-to-work-with-your-team/)、[OpenAI on X: Shared Projects expanding to Free, Plus, and Pro](https://x.com/OpenAI/status/1981432799212249119)、[Search Engine Journal: OpenAI Releases Shared Project Feature To All Users](https://www.searchenginejournal.com/openai-releases-shared-project-feature-to-all-users/559136/)、[avisainewsletter: How to Use ChatGPT's New Project-only Memory](https://avisainewsletter.substack.com/p/chatgpt-project-only-memory)、[OpenAI: ChatGPT is now a partner for your most ambitious work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)、[Elephas: ChatGPT Projects Limits: Files, Size and How Many Projects](https://elephas.app/resources/chatgpt-projects-limits-files-size-and-how-many-projects)

### 2026-07-28: 新エージェント機能「ChatGPT Work」との連携を追記
- **内容**: 2026年7月9日のGPT-5.6発表とあわせて登場した新エージェント機能「ChatGPT Work」(複数時間タスクをプロジェクトの文脈を踏まえて代行)の概要と提供プラン、7月16日以降のデスクトップアプリでのプロジェクト表示・Work スレッドのマルチデバイス同期を追記
- **出典**: [OpenAI: ChatGPT for your most ambitious work](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)、[MacRumors: OpenAI Announces GPT-5.6 And ChatGPT Work](https://www.macrumors.com/2026/07/09/openai-chatgpt-work/)、[9to5Mac: OpenAI updating ChatGPT desktop app with GPT Voice for talking through Work](https://9to5mac.com/2026/07/23/openai-updating-chatgpt-desktop-app-with-gpt-voice-for-talking-through-work/)

### 2026-07-06: 初版執筆
- **内容**: ChatGPTのプロジェクト機能の概要(チャット・ファイル・カスタム指示をまとめるワークスペース)、普通のチャット/プロジェクト/カスタムGPTの使い分け比較表、作成〜ファイル追加〜切り替えの手順、プラン別ファイル数上限(Free 5/Plus・Go・Edu 25/Pro・Business・Enterprise 40)、Claude ProjectsとGemini Gemsとの対応表を整理
- **出典**: [OpenAI Help Center: Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt)、[OpenAI Help Center: File uploads FAQ](https://help.openai.com/en/articles/8555545-file-uploads-faq)、[マネーフォワード クラウド: ChatGPTのプロジェクト機能とは？機能や利用手順・指示例を解説](https://biz.moneyforward.com/ai/basic/272/)、[GPT Master: ChatGPTに新機能「プロジェクト」登場！基本的な使い方を解説](https://chatgpt-enterprise.jp/blog/chatgpt-project/)、[Ravensight AI: Custom GPTs and ChatGPT Projects: A Simple Guide for Small Business Owners](https://ravensightai.com/custom-gpts-and-chatgpt-projects-a-simple-guide-for-small-business-owners/)、[Google Gemini アプリ ヘルプ: カスタムGem作成のヒント](https://support.google.com/gemini/answer/15235603?hl=ja)
