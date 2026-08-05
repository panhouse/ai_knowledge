---
title: 主要AIチャットツールのメモリ・プロジェクト機能比較(Gemini・Claude・Copilot)
part: 3
chapter: 第3章 記憶・文脈の管理
tags: [Gemini, Claude, Microsoft Copilot, メモリ機能, プロジェクト機能, パーソナライズ, ツール比較]
created: 2026-07-07
updated: 2026-08-03
---

# 主要AIチャットツールのメモリ・プロジェクト機能比較(Gemini・Claude・Copilot)

## これは何か

ChatGPT・Gemini・Claude・Microsoft Copilotを併用していると、「メモリ」「プロジェクト」に相当する機能がツールごとに別の名前・別の画面に隠れていて、どこで何を管理できるのか分からなくなりやすい。ChatGPTのメモリ・プロジェクト機能はそれぞれ「[ChatGPTのメモリ(Memory)機能](chatgpt-memory-feature.md)」「[ChatGPTの「プロジェクト」機能](chatgpt-projects-feature.md)」で詳しく扱っているが、本ページはその続編として、**Gemini・Claude・Microsoft Copilotの記憶・文脈管理機能を横並びで整理する**。複数ツールを使い分けている読者が「この会社の情報はどこまでどのツールに覚えられているのか」「削除したいときにどこを見ればよいか」を即座に判断できることがゴールである。

## 仕組み・背景

どのツールも、記憶・文脈の仕組みは大きく2種類に分かれる。

- **自動蓄積型の「メモリ」**: ユーザーが指示しなくても、会話の中からAIが「覚えておくと便利」と判断した事実を自動で貯めていき、以降の**別の新しいチャットでも**踏まえて回答する仕組み
- **自分で作る「プロジェクト/ワークスペース」**: 特定の案件・テーマ用に、指示文と参照資料をひとまとめにした箱を自分で作り、その箱の中でだけ効かせる仕組み(ChatGPTのプロジェクト、ClaudeのProjects、GeminiのGemなど)

この2つは別物であり、多くのツールで併用できる設計になっている。以下、Gemini・Claude・Copilotそれぞれの実装を見ていく。

### Gemini: Personal Intelligence(パーソナルインテリジェンス)

Geminiの記憶機能は名前が変わりやすく、2026年時点では次の3層で構成されている。

1. **Memory(メモリ、旧称「過去のチャット」)**: 過去の会話から学んだ、ユーザーの興味・関心・進行中のタスクなどを指す。2026年にGoogleは「過去のチャット」という呼び方を「メモリ」に統一する変更を進めている([Android Authority](https://www.androidauthority.com/google-gemini-personal-intelligence-rollout-3632287/))
2. **Saved info(保存済み情報)**: ユーザーが明示的に「覚えておいて」と伝えた事実、またはGeminiが会話から拾って書き出した短い記述の一覧。`gemini.google.com/saved-info` で一覧確認・編集・削除ができる
3. **Personal Intelligence(パーソナルインテリジェンス)**: 2026年に導入された上位概念で、Gmail・カレンダー・写真・ドライブなど連携したGoogleアプリの中身と、上記の会話メモリを組み合わせて回答する仕組み。あくまでオプトイン(初期状態では連携なし)であり、どのアプリと連携するかはユーザーが個別に選ぶ。Googleは、連携したメールや写真の内容をAIモデルの学習データには使わないと説明している([Gemini公式: Personal Intelligence](https://gemini.google/overview/personal-intelligence/))

Personal Intelligenceは2026年1月にGoogle AI Plus/Pro/Ultraの有料プラン向けに先行提供され、3月には米国の無料ユーザーにも拡大、4月14日には米国外(EEA・英国・スイスを除く)への世界展開が始まった([9to5Google](https://9to5google.com/2026/04/14/gemini-personal-intelligence-global/))。当初はGDPR・AI Act対応を理由にEEA・英国・スイスが除外されていたが、5月以降はこれらの地域にも順次展開が始まっており、今後は地域による機能差が縮小していく見込みである([NPowerUser: Gemini Personal Intelligence Rolls Out in Europe](https://nokiapoweruser.com/gemini-personal-intelligence-europe-rollout/))。有効化後は既定でオンになり、都度オフにしたい場合はプロンプト入力欄の「ツール」メニューのトグルで切り替えられ、生成された回答には参照した個人データを示す「ソース」ボタンが表示される。

これらの管理は「設定→パーソナルコンテキスト(Personal context)」画面に集約されており、「これまでのチャット」トグルと「指示(Instructions)」の追加欄がまとまっている([Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en))。なお、上記の「メモリ/Saved info/Personal Intelligence」は個人のGoogleアカウント(18歳以上)向けの機能で、職場・学校アカウントや保護者管理下のアカウントでは提供されない。企業向けには別建てで「Gemini Enterprise」の管理コンソールに「Memory and customization」という設定項目があり、組織の管理者がテナント全体でオン/オフを切り替えられる([Google Cloud: Gemini Enterprise パーソナライズ設定](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization))。Google Workspace版のGemini機能全般も、管理コンソールの「生成AI→Gemini for Workspace」から組織単位・組織部門(OU)単位でオン/オフできる([Google Workspace ヘルプ: Gemini機能へのアクセス管理](https://knowledge.workspace.google.com/admin/gemini/manage-access-to-gemini-features-in-workspace-services))。

Geminiにはもう1つ、自分で作る「Gem(ジェム)」という役割特化ボット機能があるが、これはメモリとは別物であり、詳細は「[Gem(Geminiのカスタムボット機能)の基本](../part06-custom-ai/gemini-gem-feature.md)」に譲る。Geminiには「案件ごとに資料と会話を積み上げる」という意味でのプロジェクト機能(ChatGPTのプロジェクトやClaudeのProjectsに相当するもの)は2026年8月時点でも存在せず、近い役割はGem、またはGoogleドライブ連携・NotebookLM(ノートブック機能)が担っている。

### Claude: Memory機能とProjectsの記憶

Anthropicは2025年9月、Team・Enterpriseプラン向けにメモリ機能の提供を開始し([Anthropic: Bringing memory to teams](https://www.anthropic.com/news/memory))、2026年3月には無料プランを含む全プランに展開した。当初は会話をおよそ24時間ごとにバックグラウンドで処理し、要約を1つの「メモリプロフィール」にまとめる方式だったが、2026年7月9〜10日のアップデートでこの仕組みが刷新され、Claudeが会話の中でその都度メモリ項目を作成・更新し、カテゴリー別(仕事の進め方、好み、進行中のプロジェクトなど)に整理して一覧表示する方式に変わった。ユーザーは各項目を個別に確認し、「Tell Claude what to change or remove」欄への指示、または会話中の指示で個々の項目単位で編集・削除できる([LumiChats: Claude Memory 2026](https://lumichats.com/blog/claude-memory-2026-complete-guide-how-to-use))。あわせて、月次でClaudeとのやり取りの傾向(よく話したトピック、利用が多かった曜日・時間帯など)を振り返る「Reflect(設定→Reflect)」機能もベータで追加された。Free・Pro・Maxプランのウェブ版・Claude Desktopで利用でき、メモリ機能がオンになっていることが前提となる([eWeek: Anthropic Reflect Links Claude Memory to a New AI Usage Recap](https://www.eweek.com/news/anthropic-reflect-claude-memory/))。

重要なのは、Claudeのメモリには「プロジェクト単位のメモリ」と「プロジェクトをまたぐメモリ」の2階層があることである。Projects(プロジェクト、詳細は「[Claude(Anthropic)の「プロジェクト」機能の基本](../part06-custom-ai/claude-projects-basics.md)」)内で交わした会話は、まずそのプロジェクト専用のメモリとして蓄積され、既定では他のプロジェクトや通常チャットには持ち出されない。一方、プロジェクトに属さない通常チャットでの会話は、プロジェクトをまたいで参照される全体メモリに蓄積される。「A社案件の話がB社案件のチャットに混ざる」ことを避けたい場合は、案件ごとにプロジェクトを分けて使うことが実質的な情報隔離になる。

### Microsoft Copilot: Memory & personalizationとCopilot Notebooks

Microsoft 365 Copilotは2025年後半に「Copilot Memory」を発表し、2026年1月からアップデートされたメモリ設定画面の一般提供(GA)を開始した。当初は2026年5月頃までの展開完了を予定していたが、実際の全面展開完了は2026年7月にずれ込んでいる([Microsoft Learn: Manage Copilot personalization and memory](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory)、[Message Center Archive MC1158329](https://mc.merill.net/message/MC1158329))。メモリは「カスタム指示(Custom instructions)」「保存されたメモリ(Saved memories)」「チャット履歴」の3種類で構成され、設定→パーソナライズ画面にまとまっている。音声チャット(Voice)でもメモリを参照できるようになった。

Copilotには、案件・テーマ単位で資料と会話をまとめる「Copilot Notebooks(コパイロットノートブック、旧称Copilot Pages/現在はPagesの発展形として統合)」という機能もある。Notebooksはファイル・チャット・Copilot Pages・メモをひとまとめにし、Copilotがそれらを横断して参照できる永続的なワークスペースで、2026年6月にプレビュー、7月に一般提供(GA)が始まった([support.microsoft.com: Get started with Microsoft 365 Copilot Notebooks](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-notebooks))。当初はMicrosoft 365 Copilotの追加ライセンスが必須だったが、GA後は「Microsoft 365 Copilot Chat(Basic)」「M365 Copilot(Basic)」といった軽量ライセンスのユーザーにも対象が拡大しており、ノートブックを新規作成するにはSharePointまたはOneDriveのライセンスが必要という条件に変わっている([Message Center Archive MC1384425](https://mc.merill.net/message/MC1384425))。Microsoft LoopベースのPages自体はライセンス不要で使える。位置づけとしては、ChatGPTのプロジェクト・ClaudeのProjectsに最も近いのがCopilot Notebooksであり、Pagesは単体では「AIとの共同編集ドキュメント」に近い。

## 使いどころ・使い分け

4ツールの記憶・文脈管理機能を1つの表にまとめる(2026年8月時点)。

| 観点 | ChatGPT | Gemini | Claude | Microsoft Copilot |
|---|---|---|---|---|
| メモリ機能の呼称 | メモリ(2026年6月に裏側の合成エンジンを「Dreaming」に刷新) | メモリ(旧称「過去のチャット」)+ Saved info + Personal Intelligence | メモリ(Memory、カテゴリー別の個別項目として管理) | メモリ(Memory & personalization) |
| 有無・展開状況 | Plus/Pro(米国)は新方式に移行済み、Free・Go・他地域は順次展開中 | 個人アカウント(18歳以上)向けに提供、既定オン。2026年4月に米国外へ拡大、5月以降EEA・英国・スイスにも順次展開中 | 2025年9月にTeam/Enterprise、2026年3月に無料・Pro含む全プランへ展開、2026年7月にメモリ表示方式を刷新 | 2026年1月にGA開始、当初予定より遅れ7月にほぼ全展開完了 |
| プロジェクト系機能の呼称 | プロジェクト(Projects) | 該当なし(近いのはGem・NotebookLM連携) | Projects | Copilot Notebooks(旧Copilot Pagesを内包、2026年7月GA) |
| 管理・削除方法(個人) | 設定→パーソナライズ→メモリを管理(個別削除/すべて削除) | 設定→パーソナルコンテキスト→Saved infoの一覧から個別削除、Memoryトグルでオフ | 設定→Memory(またはCapabilities→Memory)でカテゴリー別に一覧表示、項目単位で編集・削除/Pause/Reset | プロフィールアイコン→設定→パーソナライズ→メモリ(個別削除/すべて削除) |
| 組織管理者による制御可否 | Business/Enterprise/Eduでワークスペース単位のオン/オフが可能 | Google Workspace管理コンソール、またはGemini Enterprise管理コンソールでテナント単位のオン/オフが可能 | Team/Enterpriseの組織設定でメモリ自体を無効化可能 | Microsoft 365管理センターでテナント単位のロールアウト管理・機能制御が可能 |
| 記憶を残さない一時利用 | 一時的なチャット(Temporary Chat) | シークレットモード相当 | Incognito chats(履歴・メモリ両方に残らない) | プライベートセッション相当(順次整備中) |

判断の目安は次のように整理できる。

- **同じ話を毎回のように繰り返している(自分の役職・好み・進行中の案件など)** → 各ツールのメモリに任せる。ただし「絶対に外してはいけない前提」は、メモリまかせにせずカスタム指示や明示的な指示文で毎回渡す
- **特定の案件・クライアントに関する資料と会話が積み上がっていく** → ChatGPTのプロジェクト、ClaudeのProjects、Copilot Notebooksのような「箱」を作る。Geminiだけは同等機能がなく、Gemかドライブ連携・NotebookLMで代替する
- **一度きりの質問、または機密情報を含む相談** → メモリを使わない一時チャット・シークレットモード・Incognitoを選ぶ
- **社内の複数人に同じ設定のAIを配りたい** → メモリではなく、GPTs・Gem・Claude Projects(組織内共有)のような「自分で作る役割特化ボット」を使う

## 実務での使い方

### Geminiでのメモリ管理手順

1. Geminiアプリ(gemini.google.com またはスマホアプリ)を開き、画面左下または右上の自分のアカウントアイコンをクリック
2. 「設定」→「パーソナルコンテキスト(Personal context)」を選択
3. 「これまでのチャット」(Memory)のトグルでオン/オフを切り替える。オフにすると新しい記憶が作られなくなる(既存の記憶は個別に消さない限り残る)
4. 保存されている情報を直接見たい場合は、ブラウザで `gemini.google.com/saved-info` に直接アクセスすると一覧が表示され、各項目の右のメニューから個別削除ができる
5. Gmail・カレンダー・写真・ドライブなどとの連携(Personal Intelligence)は、同じパーソナルコンテキスト画面、またはアプリごとの連携設定から個別にオン/オフできる。使う予定のないアプリは連携しないままにしておくのが安全

コピペで使える確認プロンプト。

```
私についてこれまで何を覚えていますか。一覧で教えてください。
```

```
〇〇プロジェクトの件はもう終了したので、関連する記憶を忘れてください。
```

### Claudeでのメモリ管理手順

1. claude.aiにログインし、画面左下の自分のアカウント名(またはアイコン)をクリック
2. 「設定(Settings)」を開き、「Memory」(または左メニューの「Capabilities」→「View and edit memory」)を選択
3. カテゴリー(仕事の進め方・好み・進行中のプロジェクトなど)別に記録済みのメモリ項目が一覧表示される。項目を選ぶと詳細が見られ、「Tell Claude what to change or remove」欄に指示を書くか「Delete」を選ぶことで、項目単位で編集・削除できる(会話中に「この件は忘れて」と伝えるだけでも反映される)
4. 新しい記憶を作りたくないが既存の記憶は残したい場合は「Pause memory」を選ぶ(一時停止。記憶自体は保持される)
5. すべての記憶を消したい場合は「Reset memory」を選ぶ(プロジェクトメモリを含め完全削除。取り消し不可)
6. 特定の会話だけ記憶に残したくない場合は、その会話を「Incognito chat」として開始する(会話履歴にもメモリにも残らない)
7. 月ごとの利用傾向を振り返りたい場合は「設定→Reflect」(ベータ)を開く。メモリ機能がオンであることが前提

コピペで使える確認プロンプト。

```
私についてどんなことを覚えているか教えてください。
```

```
〇〇の件はプロジェクトが終了したので、その記憶は削除してください。
```

Team/Enterpriseプランの管理者は、組織設定からメモリ機能自体をテナント全体で無効化できる(無効化するとメンバー個人の設定によらず新規の記憶が作られなくなる)。

### Microsoft Copilotでのメモリ管理手順

1. Copilot(Web版・Windows/Edgeアプリ・モバイルアプリ)を開き、画面のプロフィールアイコンをクリック
2. 「設定(Settings)」→「パーソナライズ(Personalization)」を選択(モバイルアプリではメニュー→プロフィールアイコン→「メモリ」→「パーソナライズとメモリ」の順)
3. 「カスタム指示」「保存されたメモリ」「チャット履歴」の3項目が並んでおり、それぞれ個別に確認・編集できる
4. 画面下部のトグルでメモリ機能自体をオン/オフできる
5. すべての記憶を削除したい場合は、プロフィールアイコン→「メモリ」→「すべてのメモリを削除(Delete all Memory)」を選ぶ(会話履歴自体は削除されない)

コピペで使える確認プロンプト。

```
私について何を知っていますか。
```

```
このことは覚えておいてください:毎週月曜の朝に週次レポートのたたき台を作成する担当です。
```

案件単位で資料と会話をまとめたい場合は、メモリではなくCopilot Notebooksを使う。2026年7月のGA後は、Microsoft 365 CopilotのフルライセンスだけでなくCopilot Chat(Basic)/M365 Copilot(Basic)のユーザーでも利用でき、Notebooksの新規作成画面からファイル・既存のCopilot Pages・チャットを1つのノートブックにまとめられる(ただし新規ノートブックの作成にはSharePointまたはOneDriveのライセンスが必要)。

## 注意点・よくある誤解

- **メモリは「案件をまたいで漏れる」前提で使う**: どのツールも、いったんメモリに保存された情報は無関係な新規チャットにも自動的に読み込まれ得る。取引先名や未公表の内部情報は、雑談の中で触れただけでも記憶される可能性があるため、機密性の高い相談は一時チャット・シークレットモード・Incognitoを使う
- **メモリが古くなると回答がずれる**: 異動・担当変更・プロジェクト終了後に古い記憶が残り続け、実態と合わない前提で回答が返ってくることがある。定期的に各ツールのメモリ一覧を見直す。ChatGPTは2026年6月の「Dreaming」導入で、日付が過ぎたタスク(「出張の予定」など)を自動的に「過去のこと」として扱い直すなど時間経過に応じた自動修正を強化しているが、他ツールは基本的に手動での見直しが前提である([OpenAI: Dreaming — Better memory for a more helpful ChatGPT](https://openai.com/index/chatgpt-memory-dreaming/))
- **Geminiの「メモリ」「Saved info」「Personal Intelligence」「Gem」は全て別物**: 名前が近く混同しやすいが、メモリ・Saved infoは自動蓄積、GemとPersonal Intelligeng連携先の選択は自分で設定する固定的な仕組みという違いがある。Personal Intelligenceで連携するGoogleアプリ(Gmail・写真など)は、業務用アカウントの共有端末では特に慎重に選ぶ
- **地域・アカウント種別で挙動が異なる**: GeminiのPersonal Intelligenceは2026年5月以降EEA・英国・スイスにも展開が始まったが、時期・対象は地域ごとに異なりまだ全員に揃ってはいない。個人向け機能自体が職場・学校・保護者管理下アカウントでは提供されない点は変わらない。海外拠点や社用アカウントのメンバーと同じ設定になっていると思い込まない
- **法人プランでは管理者の設定が優先される**: Claude Team/Enterprise、Google Workspace/Gemini Enterprise、Microsoft 365いずれも、組織の管理者がテナント単位でメモリ機能をオフにできる。会社アカウントで「メモリが効かない」場合は、個人設定ではなく管理者側の設定を確認する
- **CopilotのPagesとNotebooksを混同しない**: Pagesはライセンス不要のAI共同編集ドキュメントで案件全体をまとめる箱ではない。ChatGPTのプロジェクトやClaude Projectsに相当するのはCopilot Notebooksの方で、2026年7月のGA後はCopilot Chat(Basic)などの軽量ライセンスでも使えるようになったが、新規ノートブックの作成にはSharePoint/OneDriveライセンスが要る点に注意
- **メモリを消してもチャット自体は残り、チャットを消してもメモリは自動では消えない**: 4ツールとも、メモリの削除とチャット履歴の削除は別操作である。完全に痕跡を消したい場合は両方を個別に確認する

## 最初の一歩

普段使っているGemini・Claude・Copilotのいずれか1つを開き、「私について何を覚えていますか」と聞いてみて、表示された内容に業務上の機密情報や実態と合わなくなった項目がないか確認し、あれば1件削除してみる。

## 関連トピック

- [ChatGPTのメモリ(Memory)機能](chatgpt-memory-feature.md)
- [ChatGPTの「プロジェクト」機能](chatgpt-projects-feature.md)
- [Google Geminiの基本](google-gemini-basics.md)
- [Claude(Anthropic)の基本](claude-basics.md)
- [Gem(Geminiのカスタムボット機能)の基本](../part06-custom-ai/gemini-gem-feature.md)
- [Claude(Anthropic)の「プロジェクト」機能の基本](../part06-custom-ai/claude-projects-basics.md)

## 更新履歴

### 2026-08-03: Gemini・Claude・Copilotの記憶機能の最新動向を反映して最新化
- **内容**: 各社の2026年4月〜7月の変更を反映。Geminiは4月に米国外(EEA・英国・スイスを除く)へPersonal Intelligenceを拡大した後、5月以降はEEA・英国・スイスにも順次展開が始まったことを追記。Claudeは2026年7月9〜10日に、24時間ごとの単一要約だったメモリを「カテゴリー別の個別項目をリアルタイムに作成・編集・削除できる」方式へ刷新したこと、および月次利用傾向を振り返る新機能「Reflect」(ベータ)を追加。Microsoft Copilotは、メモリ設定のGA完了が5月予定から7月にずれ込んだこと、Copilot Notebooksが2026年7月にGAし、Microsoft 365 Copilotのフルライセンスがなくても軽量な「Copilot Chat(Basic)」等でも使えるようになったこと(ノートブック新規作成にはSharePoint/OneDriveライセンスが必要)を追記。あわせて比較表・手順・注意点の記述を上記に整合させ、参考としてChatGPTの記憶合成エンジン刷新「Dreaming」(2026年6月)にも触れた
- **出典**: [9to5Google: Gemini app starts rolling out Personal Intelligence globally](https://9to5google.com/2026/04/14/gemini-personal-intelligence-global/)、[NPowerUser: Gemini Personal Intelligence Rolls Out in Europe](https://nokiapoweruser.com/gemini-personal-intelligence-europe-rollout/)、[LumiChats: Claude Memory 2026 - What It Stores & How to Delete It](https://lumichats.com/blog/claude-memory-2026-complete-guide-how-to-use)、[eWeek: Anthropic Reflect Links Claude Memory to a New AI Usage Recap](https://www.eweek.com/news/anthropic-reflect-claude-memory/)、[Microsoft Support: Get started with Microsoft 365 Copilot Notebooks](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-microsoft-365-copilot-notebooks)、[Microsoft 365 Message Center Archive: MC1384425](https://mc.merill.net/message/MC1384425)、[OpenAI: Dreaming — Better memory for a more helpful ChatGPT](https://openai.com/index/chatgpt-memory-dreaming/)

### 2026-07-07: 初版執筆
- **内容**: ChatGPT以外の主要AIチャットツール(Gemini・Claude・Microsoft Copilot)のメモリ・プロジェクト系機能を横断比較。Geminiのメモリ/Saved info/Personal Intelligenceの3層構造とGem・Workspace管理者権限との関係、ClaudeのMemory機能(2025年9月Team/Enterprise展開、2026年3月全プラン展開)とProjectsとの記憶の階層関係、Microsoft CopilotのMemory & personalizationとCopilot Notebooks(旧Pages)の違いを整理。メモリ機能の有無・呼称/プロジェクト系機能の呼称/管理削除方法/組織管理者による制御可否の比較表、画面の場所まで書いた管理手順、コピペ確認プロンプトを収録
- **出典**: [Claude Help Center: Use Claude's chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)、[Anthropic: Bringing memory to teams](https://www.anthropic.com/news/memory)、[Gemini公式: Personal Intelligence](https://gemini.google/overview/personal-intelligence/)、[Android Authority: Gemini gets personal as Google rolls out a big memory upgrade](https://www.androidauthority.com/google-gemini-personal-intelligence-rollout-3632287/)、[Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en)、[Google Cloud: Configure personalization and memory (Gemini Enterprise)](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization)、[Google Workspace ヘルプ: Manage access to Gemini features in Workspace services](https://knowledge.workspace.google.com/admin/gemini/manage-access-to-gemini-features-in-workspace-services)、[Microsoft Learn: Manage Copilot personalization and memory](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory)、[Microsoft 365 Message Center Archive: MC1158329](https://mc.merill.net/message/MC1158329)、[Microsoft Support: How Microsoft 365 Copilot Notebooks works](https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works)
