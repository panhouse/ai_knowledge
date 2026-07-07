---
title: 主要AIチャットツールのメモリ・プロジェクト機能比較(Gemini・Claude・Copilot)
part: 3
chapter: 第3章 記憶・文脈の管理
tags: [Gemini, Claude, Microsoft Copilot, メモリ機能, プロジェクト機能, パーソナライズ, ツール比較]
created: 2026-07-07
updated: 2026-07-07
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

これらの管理は「設定→パーソナルコンテキスト(Personal context)」画面に集約されており、「これまでのチャット」トグルと「指示(Instructions)」の追加欄がまとまっている([Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en))。なお、上記の「メモリ/Saved info/Personal Intelligence」は個人のGoogleアカウント(18歳以上)向けの機能で、職場・学校アカウントや保護者管理下のアカウントでは提供されない。企業向けには別建てで「Gemini Enterprise」の管理コンソールに「Memory and customization」という設定項目があり、組織の管理者がテナント全体でオン/オフを切り替えられる([Google Cloud: Gemini Enterprise パーソナライズ設定](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization))。Google Workspace版のGemini機能全般も、管理コンソールの「生成AI→Gemini for Workspace」から組織単位・組織部門(OU)単位でオン/オフできる([Google Workspace ヘルプ: Gemini機能へのアクセス管理](https://knowledge.workspace.google.com/admin/gemini/manage-access-to-gemini-features-in-workspace-services))。

Geminiにはもう1つ、自分で作る「Gem(ジェム)」という役割特化ボット機能があるが、これはメモリとは別物であり、詳細は「[Gem(Geminiのカスタムボット機能)の基本](../part06-custom-ai/gemini-gem-feature.md)」に譲る。Geminiには「案件ごとに資料と会話を積み上げる」という意味でのプロジェクト機能(ChatGPTのプロジェクトやClaudeのProjectsに相当するもの)は2026年7月時点で存在せず、近い役割はGem、またはGoogleドライブ連携・NotebookLM(ノートブック機能)が担っている。

### Claude: Memory機能とProjectsの記憶

Anthropicは2025年9月、Team・Enterpriseプラン向けにメモリ機能の提供を開始し([Anthropic: Bringing memory to teams](https://www.anthropic.com/news/memory))、2026年3月には無料プランを含む全プランに展開した。Claudeは会話をおよそ24時間ごとにバックグラウンドで処理し、長期的に価値のある情報を要約して「メモリプロフィール」に蓄積、以降のすべての新規チャットに自動で読み込む([Claude Help Center](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context))。

重要なのは、Claudeのメモリには「プロジェクト単位のメモリ」と「プロジェクトをまたぐメモリ」の2階層があることである。Projects(プロジェクト、詳細は「[Claude(Anthropic)の「プロジェクト」機能の基本](../part06-custom-ai/claude-projects-basics.md)」)内で交わした会話は、まずそのプロジェクト専用のメモリとして蓄積され、既定では他のプロジェクトや通常チャットには持ち出されない。一方、プロジェクトに属さない通常チャットでの会話は、プロジェクトをまたいで参照される全体メモリに蓄積される。「A社案件の話がB社案件のチャットに混ざる」ことを避けたい場合は、案件ごとにプロジェクトを分けて使うことが実質的な情報隔離になる。

### Microsoft Copilot: Memory & personalizationとCopilot Notebooks

Microsoft 365 Copilotは2025年後半に「Copilot Memory」を発表し、2026年1月からアップデートされたメモリ設定画面の一般提供(GA)を開始、2026年5月頃までに順次展開が完了する計画になっている([Microsoft Learn: Manage Copilot personalization and memory](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory)、[Message Center Archive MC1158329](https://mc.merill.net/message/MC1158329))。メモリは「カスタム指示(Custom instructions)」「保存されたメモリ(Saved memories)」「チャット履歴」の3種類で構成され、設定→パーソナライズ画面にまとまっている。

Copilotには、案件・テーマ単位で資料と会話をまとめる「Copilot Notebooks(コパイロットノートブック、旧称Copilot Pages/現在はPagesの発展形として統合)」という機能もある。Notebooksはファイル・チャット・Copilot Pages・メモをひとまとめにし、Copilotがそれらを横断して参照できる永続的なワークスペースで、Microsoft LoopベースのPages自体はライセンス不要で使える一方、Notebooksの機能はMicrosoft 365 Copilotライセンスが必要になる([Microsoft Support: How Microsoft 365 Copilot Notebooks works](https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works))。位置づけとしては、ChatGPTのプロジェクト・ClaudeのProjectsに最も近いのがCopilot Notebooksであり、Pagesは単体では「AIとの共同編集ドキュメント」に近い。

## 使いどころ・使い分け

4ツールの記憶・文脈管理機能を1つの表にまとめる(2026年7月時点)。

| 観点 | ChatGPT | Gemini | Claude | Microsoft Copilot |
|---|---|---|---|---|
| メモリ機能の呼称 | メモリ(保存されたメモリ+チャット履歴を参照) | メモリ(旧称「過去のチャット」)+ Saved info + Personal Intelligence | メモリ(Memory) | メモリ(Memory & personalization) |
| 有無・展開状況 | Plus以降が本格版、Freeは軽量版 | 個人アカウント(18歳以上)向けに提供、既定オン(EEA・英国・スイスは既定オフ) | 2025年9月にTeam/Enterprise、2026年3月に無料・Pro含む全プランへ展開 | 2026年1〜5月にかけてGA展開中(順次ロールアウト) |
| プロジェクト系機能の呼称 | プロジェクト(Projects) | 該当なし(近いのはGem・NotebookLM連携) | Projects | Copilot Notebooks(旧Copilot Pagesを内包) |
| 管理・削除方法(個人) | 設定→パーソナライズ→メモリを管理(個別削除/すべて削除) | 設定→パーソナルコンテキスト→Saved infoの一覧から個別削除、Memoryトグルでオフ | 設定→Capabilities→Memory(個別削除/Pause/Reset) | プロフィールアイコン→設定→パーソナライズ→メモリ(個別削除/すべて削除) |
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
2. 「設定(Settings)」を開き、左メニューの「Capabilities」を選択
3. 「Memory」欄で、記録済みのメモリ一覧を確認できる。各項目の横から個別削除が可能
4. 新しい記憶を作りたくないが既存の記憶は残したい場合は「Pause memory」を選ぶ(一時停止。記憶自体は保持される)
5. すべての記憶を消したい場合は「Reset memory」を選ぶ(プロジェクトメモリを含め完全削除。取り消し不可)
6. 特定の会話だけ記憶に残したくない場合は、その会話を「Incognito chat」として開始する(会話履歴にもメモリにも残らない)

コピペで使える確認プロンプト。

```
私についてどんなことを覚えているか教えてください。
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

案件単位で資料と会話をまとめたい場合は、メモリではなくCopilot Notebooksを使う。Microsoft 365 Copilotライセンスを持つユーザーが、Notebooksの新規作成画面からファイル・既存のCopilot Pages・チャットを1つのノートブックにまとめられる。

## 注意点・よくある誤解

- **メモリは「案件をまたいで漏れる」前提で使う**: どのツールも、いったんメモリに保存された情報は無関係な新規チャットにも自動的に読み込まれ得る。取引先名や未公表の内部情報は、雑談の中で触れただけでも記憶される可能性があるため、機密性の高い相談は一時チャット・シークレットモード・Incognitoを使う
- **メモリが古くなると回答がずれる**: 異動・担当変更・プロジェクト終了後に古い記憶が残り続け、実態と合わない前提で回答が返ってくることがある。定期的に各ツールのメモリ一覧を見直す
- **Geminiの「メモリ」「Saved info」「Personal Intelligence」「Gem」は全て別物**: 名前が近く混同しやすいが、メモリ・Saved infoは自動蓄積、GemとPersonal Intelligeng連携先の選択は自分で設定する固定的な仕組みという違いがある。Personal Intelligenceで連携するGoogleアプリ(Gmail・写真など)は、業務用アカウントの共有端末では特に慎重に選ぶ
- **地域・アカウント種別で挙動が異なる**: Geminiのメモリ・Saved infoはEEA・英国・スイスでは既定オフ、個人向け機能自体が職場・学校・保護者管理下アカウントでは提供されない。海外拠点や社用アカウントのメンバーと同じ設定になっていると思い込まない
- **法人プランでは管理者の設定が優先される**: Claude Team/Enterprise、Google Workspace/Gemini Enterprise、Microsoft 365いずれも、組織の管理者がテナント単位でメモリ機能をオフにできる。会社アカウントで「メモリが効かない」場合は、個人設定ではなく管理者側の設定を確認する
- **CopilotのPagesとNotebooksを混同しない**: Pagesはライセンス不要のAI共同編集ドキュメントで案件全体をまとめる箱ではない。ChatGPTのプロジェクトやClaude Projectsに相当するのはCopilot Notebooksの方で、こちらはMicrosoft 365 Copilotライセンスが必要
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

### 2026-07-07: 初版執筆
- **内容**: ChatGPT以外の主要AIチャットツール(Gemini・Claude・Microsoft Copilot)のメモリ・プロジェクト系機能を横断比較。Geminiのメモリ/Saved info/Personal Intelligenceの3層構造とGem・Workspace管理者権限との関係、ClaudeのMemory機能(2025年9月Team/Enterprise展開、2026年3月全プラン展開)とProjectsとの記憶の階層関係、Microsoft CopilotのMemory & personalizationとCopilot Notebooks(旧Pages)の違いを整理。メモリ機能の有無・呼称/プロジェクト系機能の呼称/管理削除方法/組織管理者による制御可否の比較表、画面の場所まで書いた管理手順、コピペ確認プロンプトを収録
- **出典**: [Claude Help Center: Use Claude's chat search and memory to build on previous context](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context)、[Anthropic: Bringing memory to teams](https://www.anthropic.com/news/memory)、[Gemini公式: Personal Intelligence](https://gemini.google/overview/personal-intelligence/)、[Android Authority: Gemini gets personal as Google rolls out a big memory upgrade](https://www.androidauthority.com/google-gemini-personal-intelligence-rollout-3632287/)、[Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en)、[Google Cloud: Configure personalization and memory (Gemini Enterprise)](https://docs.cloud.google.com/gemini/enterprise/docs/configure-personalization)、[Google Workspace ヘルプ: Manage access to Gemini features in Workspace services](https://knowledge.workspace.google.com/admin/gemini/manage-access-to-gemini-features-in-workspace-services)、[Microsoft Learn: Manage Copilot personalization and memory](https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-personalization-memory)、[Microsoft 365 Message Center Archive: MC1158329](https://mc.merill.net/message/MC1158329)、[Microsoft Support: How Microsoft 365 Copilot Notebooks works](https://support.microsoft.com/en-us/microsoft-365-copilot/how-microsoft-365-copilot-notebooks-works)
