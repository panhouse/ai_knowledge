---
title: "ChatGPTのエージェント機能(旧ChatGPT Agent→ChatGPT Work)とスケジュールタスク(Tasks)"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [ChatGPT, ChatGPT Work, ChatGPT Agent, Work, Tasks, タスク自動化, ブラウザ操作]
created: 2026-07-06
updated: 2026-07-27
---

# ChatGPTのエージェント機能(旧ChatGPT Agent→ChatGPT Work)とスケジュールタスク(Tasks)

## これは何か

通常のChatGPTは、1回の質問に1回の回答を返すだけで、「このサイトを開いて」「フォームに入力して」「予約を確定して」といった実際の操作はユーザー自身がやるしかない。**ChatGPT Work(チャットGPT・ワーク)**は、ChatGPTに組み込まれた仮想のブラウザ・コンピュータ環境を使って、ChatGPT自身がWebサイトを開き、検索・クリック・フォーム入力・ファイル作成といった複数ステップの作業を、人間の代わりに最後までやり切る機能である。「競合5社を調べて比較表を作る」「ある商品をカートに入れて確認画面まで進める」のような、これまで人が何度もブラウザを往復して行っていた作業を、目的(ゴール)を渡すだけで代行し、スプレッドシート・スライド・ドキュメント・簡単なWebアプリといった**完成した成果物**として返してくれる。

このChatGPT Workは、2026年7月9日にOpenAIが発表した名称で、それまで「**ChatGPT Agent**」「エージェントモード」と呼ばれていた機能が改名・拡張されたものである。ヘルプセンターの「ChatGPT agent」ページも現在は「ChatGPT agentは提供終了し、複数ステップの作業と成果物の作成にはChatGPT Workを使ってほしい」という案内に切り替わっている([ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275))。本ページや社内の過去のやり取りで「ChatGPT Agent」「エージェントモード」という表記を見かけた場合は、現行のChatGPT Workのことだと読み替えてよい。

これとは別に、**Tasks(タスク/スケジュールタスク)**という機能もある。こちらはブラウザ操作を伴わない軽量な仕組みで、「毎週月曜9時に業界ニュースを要約して送って」のように、決まった時刻・周期でChatGPTに同じ依頼を自動的に繰り返させるものである。「都度お願いするのを忘れる」「毎回同じ質問を打つのが手間」という悩みを解決する。本ページでは、この2つ(能動的に操作を代行するChatGPT Workと、時間で自動起動するTasks)をまとめて「ChatGPTの自律実行系機能」として扱う。

## 仕組み・背景

### ChatGPT Agentの成り立ちと「ChatGPT Work」への改名(2026年7月)

現在のChatGPT Workは、もともと2つの機能が統合されて生まれたものである。

- **Operator**: 2025年1月に発表された、仮想ブラウザを操作してWebサイト上のタスク(予約・注文フォーム入力など)を代行する専用ツール
- **Deep Research**: Web上の情報を自律的に調べ回り、出典付きの長文レポートにまとめる調査特化のモード(詳しくは[Deep Research機能](../part11-business-practice/ai-research-and-information-gathering.md)を参照)

2025年7月17日、OpenAIはこの2つと通常のChatGPTの対話能力を統合し、単一の「ChatGPT agent」として再構成した([Introducing ChatGPT agent | OpenAI](https://openai.com/index/introducing-chatgpt-agent/))。単体ツールとしてのOperatorは2025年8月31日で提供終了し、その機能はChatGPT Agentに一本化された。

その後、2026年7月9日にOpenAIは新モデルファミリー「GPT-5.6」の投入に合わせ、ChatGPTを**Chat(通常の対話)・Work(複数ステップの自律作業)・Codex(ソフトウェア開発)**という3モード構成に再編し、旧「ChatGPT agent(エージェントモード)」は「**ChatGPT Work**」という名称に一本化された。OpenAIはこれを「答えを作るAIから、仕事を仕上げるAIへ」という位置付けで発表しており、数時間かかるような複雑なプロジェクトを小さなステップに分解し、独力で進め続けられる点を強調している([ChatGPT is now a partner for your most ambitious work | OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/))。

なお、「調査だけしてほしい(Deep Research相当)」の入口は今回の再編後も別モードとして残っており、2026年7月時点でdeep researchはChatGPT Workに統合されず、ツールメニューの中に独立した選択肢として引き続き存在している。「調べるだけ」か「操作・成果物作成までしてほしい」かで使い分ける構図に変わりはない。

### 動作の仕組み

ChatGPT Workは、画面内に表示される**仮想コンピュータ(サンドボックス化されたブラウザ環境)**の中で作業する。ユーザーは、AIがマウス操作・クリック・入力を行っている様子をリアルタイムの画面としてそのまま眺めることができ、途中で止めたり指示を追加したりできる。仮想環境の中で検索・サイト巡回・フォーム入力に加えて、コードの実行や、スプレッドシート・スライド・簡易なWebアプリ(「Sites」と呼ばれる成果物形式)の作成まで行える。

Gmail・Googleカレンダー・Google ドライブ・GitHub・Outlook・SharePoint・Dropbox・Box・HubSpot・Linear・Teams・Slack・Salesforce・Figma・Adobe Acrobat・Zoom・Canvaなどの外部サービスは、「**Plugins**」という接続機能を通じて連携できる。この呼び方は2025年12月に「コネクタ(connectors)」から「アプリ(apps)」へ、2026年7月にさらに「Plugins」へと名称が変わったもので、機能自体は既存の連携を土台に対象サービスを拡張している([Connectors in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt))。社内カレンダーの空き時間を見てメールを起草する、Salesforceの商談ステータスを更新する、といった横断作業も可能になっている。

安全面では、次の仕組みが引き続き用意されている。

- **テイクオーバーモード(takeover mode)**: ログインのパスワードや決済情報の入力が必要な場面では、AIに直接教えるのではなく、ユーザーが画面を一時的に引き取って自分の手で入力する。入力した内容をChatGPT側が記録・保存することはない
- **確認プロンプト**: メール送信・注文確定など、後戻りしにくい(消費者にとって重要な)操作の直前で、AIが自動的に停止し「実行してよいか」を確認してくる
- **ウォッチモード(watch mode)**: 金融機関のサイトなど特に慎重な扱いが必要なサイトのカテゴリでは、ユーザーが画面を見て見守っていることを前提に動作し、目を離すと一時停止する

### 関連する製品群(2026年7月時点)

- **ChatGPT Workspace agents**: チームで共有・スケジュール実行できる、より本格的な業務ワークフロー向けのエージェント機能(週次の指標レポート作成、ITチケットの一次対応など)。Business/Enterprise/Edu向けの機能として、個人向けのChatGPT Workとは別のヘルプページ・設定画面で案内されている([ChatGPT Workspace Agents for Enterprise and Business | OpenAI Help Center](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business))。本ページで扱う個人向けのChatGPT Work/Tasksとは別物で、対象読者(チーム管理者)や設定場所が異なる
- **ChatGPT Atlas(ブラウザ)**: 2025年10月に登場したOpenAI製Webブラウザで、ブラウザ自体に「エージェントモード」が内蔵されており、ChatGPT Workと同じ仕組みをより高速に動かせる(Plus/Pro/Business向け)
- **Codexモード**: 今回の3モード再編で新設された、ソフトウェア開発に特化したモード。コーディング支援AIとしての位置付けであり、業務資料の作成・調査・操作の代行を目的とする本ページのChatGPT Workとは用途が異なる
- **呼び方は今後も変わりうる**: ChatGPTのエージェント系機能は「Operator→ChatGPT Agent→ChatGPT Work」と1年半で2度名称が変わっており、今後も呼び方・提供形態が変わる可能性がある点は念頭に置いておきたい

### Tasksの仕組み

Tasksは、ChatGPT Workのような仮想ブラウザ・コンピュータは使わない、より軽量な機能である。指定した日時・周期でChatGPTへの依頼(プロンプト)を自動的に再実行するだけの仕組みで、リマインダー・定期的な要約・簡単な監視(「値下げがあったら教えて」など、Web検索を伴う範囲まで)に向いている。ヘルプセンターの案内ページも、従来の「Scheduled tasks in ChatGPT」から「**Tasks in ChatGPT**」という見出しに変わっており、ChatGPT Work配下の一機能として位置付けられている([Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt))。

## 使いどころ・使い分け

| 機能 | 何をしてくれるか | かかる時間 | 向いている場面 |
|---|---|---|---|
| 通常のチャット(Chatモード) | その場で1回答える | 数秒 | 一般知識の相談、下書き、アイデア出し |
| [Web検索機能](./chatgpt-web-search-feature.md) | 1〜数回検索し、その場で要約して答える | 数秒〜数十秒 | 鮮度が必要な単発の事実確認 |
| deep research(調査モード) | 自律的に多数のサイトを読み回り、出典付きレポートを作る(**読み取りのみ**、操作は行わない) | 数分〜数十分 | 競合比較・市場調査など複数ソースの横断調査。詳細は[Deep Research機能](../part11-business-practice/ai-research-and-information-gathering.md) |
| **ChatGPT Work(旧ChatGPT Agent/エージェントモード)** | 仮想ブラウザ・コンピュータで実際にクリック・入力・購入・ファイル作成まで**操作を実行**し、完成した成果物(表・資料・簡易Webアプリ)として返す | 数分〜数時間 | 予約・注文・フォーム提出・複数サイトを横断した作業の代行、成果物の作成まで一括で頼みたいとき |
| **Tasks(スケジュールタスク)** | 指定した日時・周期でプロンプトを自動再実行する(ブラウザ操作なし) | 実行のたびに数秒〜数分 | 定期リマインダー、週次・日次の定型要約、簡易な定期監視 |
| Codexモード | コードの生成・修正・実行に特化 | 数分〜 | ソフトウェア開発(本ページの対象外) |

判断の目安は次の2つ。

1. **「調べるだけ」か「実際に操作・成果物作成までしてほしい」か**: 読み取りだけならdeep research、フォーム送信・注文・予約・ファイル作成など「後戻りしにくい操作」や「完成品が欲しい」場合はChatGPT Work
2. **「今すぐ1回」か「決まった周期で繰り返す」か**: 今すぐ1回で完結する作業ならChatGPT Work、同じ依頼を定期的に繰り返したいならTasks(Tasksの実行内容が調査中心であればdeep research相当の処理が、操作を含む場合はWork相当の処理が、裏側で毎回走る)

なお、「ChatGPT Work」はOpenAIというひとつの提供元の実装名であり、Google・Anthropic・Microsoftなど各社にもブラウザ操作型・業務自動化型のエージェントが存在する。ベンダーを横断した「AIエージェントとは何か」という概念・分類・導入の判断軸は[AIエージェントとは何か](../part12-ai-trends/ai-agent-basics.md)で扱っているので、社内でエージェント導入の方針を検討する際はそちらも参照してほしい。本ページはChatGPTというツールに閉じた「画面のどこで・どう使うか」の実務ガイドに徹する。

## 実務での使い方

### ChatGPT Workの使い方(2026年7月時点)

1. デスクトップアプリ・Web版とも、画面上部(左上)のモード切り替えから「**Work**」を選ぶ。旧バージョンの「+」ボタンから「エージェントモード」を選ぶ導線は、3モード構成への刷新に伴い「Work」への切り替えに置き換わっている
2. 依頼内容を入力すると、画面内に仮想ブラウザの実行画面が表示され、AIが検索・クリック・入力を進めていく様子がそのまま見える。長時間かかる依頼は、裏側で処理を継続させたまま他の作業に移ることもできる
3. ログインや決済情報の入力が必要な場面になると、テイクオーバーモードに切り替わる通知が出るので、その場面だけ自分の手で入力する
4. メール送信や注文確定など後戻りしにくい操作の前には、確認ダイアログが出るので、内容を確認してから許可する
5. 完了すると、作業結果(作成したファイル・調べた内容の要約・実行済み操作の記録)がチャット欄に返ってくる

**対応プラン**: 2026年7月9日の発表後、Web版・モバイル版ではPro・Enterprise・Eduから展開が始まり、数日以内にPlus・Businessにも順次拡大された。デスクトップアプリでは、Free(無料)プランを含む全プランでChat・Work・Codexの3モードが利用できる(グローバル提供)。一方、低価格プランの「Go」はWork/Codexの展開対象に含まれていない。利用回数は既存の「クレジット」(エージェント利用枠)制度がそのまま使われており、Codexモードと共通の枠を消費する。クレジットは付与から一定期間有効で、消費した分だけ追加購入もできる(Business/Enterpriseは追加クレジット購入が可能)([ChatGPT is now a partner for your most ambitious work | OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)、[ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275))。

### コピペで使える実例

読み取り中心で、後戻りしにくい操作を含まない依頼(初めて試すのに向く):

```
Workモードで、来週の月曜〜水曜に東京→大阪を新幹線で移動する場合の
時間帯別の空席状況と料金を調べて、比較しやすい表にまとめてください。
チケットの購入や予約は行わず、調査結果の報告だけをお願いします。
```

操作(注文確定手前まで)を含む依頼(確認プロンプトが挟まることを前提に):

```
Workモードで、〇〇(通販サイト名)で△△(商品名)を検索し、
条件に近い上位3件を比較したうえで、最も条件に合う商品をカートに入れてください。
購入の確定は行わず、確認画面の手前で止めて私に知らせてください。
```

### Tasksの設定・管理方法

1. 依頼文の中で日時・周期を明示して頼む(例:「毎週月曜の朝9時に、業界ニュースを3行で要約して送って」)、または回答画面の時計アイコンから「タスクとして保存」を選ぶ
2. サイドバーの「タスク(Tasks)」一覧から、設定済みのタスクを確認できる。次回実行時刻・実行内容が表示される
3. 各タスクは一覧から一時停止・再開・内容の編集・削除ができる
4. 実行結果は通知として届き、チャット履歴にも残る。長期間反応がないまま放置されたタスクは、自動的に一時停止扱いになることがある

**対応プラン・上限**: Tasksは2026年7月時点でGo・Plus・Pro・Business・Enterprise・Eduで利用でき、同時に有効化できるタスク数の上限はGoが3件、Plusが5件、Business/Eduが10件、Pro/Enterpriseが15件となっている。1つのタスクを1時間に2回以上実行するような高頻度の設定はできない([Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt))。

コピペで使える例:

```
毎週月曜日の朝9時に、直近1週間の生成AI関連の主要ニュースをWeb検索で調べて、
3行以内の日本語サマリーで送ってください。個別の製品リリースよりも、
業務での使い方に影響しそうな話題を優先してください。
```

### 主要ツールでの対応付け

| 概念 | ChatGPT(OpenAI) | Google | Anthropic | Microsoft |
|---|---|---|---|---|
| 呼び方 | ChatGPT Work(旧ChatGPT Agent/Operator+Deep Research) | Gemini Spark(旧Project Mariner系機能を統合) | Computer Use(Claude・Claude Code経由)/Claude Cowork | Copilot Cowork / Copilot Studio |
| スケジュール実行 | Tasks | Gemini内のスケジュール機能 | Cowork内のスケジュールタスク/Claude Code Routines(開発者向け) | Copilot Tasks |

各社の詳しい分類・導入判断は[AIエージェントとは何か](../part12-ai-trends/ai-agent-basics.md)、機能名・対応プランの横並び比較は[主要AIチャットツールのエージェント機能・スケジュールタスク比較](./ai-chat-tools-agent-tasks-comparison.md)にまとめているので、そちらを参照してほしい。

## 注意点・よくある誤解

- **「エージェントモード」という表記は現行UIには残っていない**: 2026年7月9日以降、画面上の呼び方は「Work」に統一された。社内マニュアルやブックマークした手順書に「+ボタン→エージェントモード」と書いてある場合は、モード切り替えから「Work」を選ぶ手順に読み替える必要がある
- **確認プロンプトがあっても「丸投げして安全」にはならない**: 送信・注文・予約の直前には確認が入る設計だが、確認画面自体の内容を読まずに許可してしまえば事故は防げない。重要な操作を含む依頼では、確認ダイアログの内容を必ず読んでから許可する
- **プロンプトインジェクションのリスクは解消されていない**: OpenAIは2025年12月、ChatGPT AgentやAtlasのようなブラウザ操作型AIに対するプロンプトインジェクション(閲覧先のページに埋め込まれた悪意ある指示にAIが誘導される攻撃)について、「完全に解決できない可能性がある」と公表しており、英国のNCSC(国家サイバーセキュリティセンター)も同様の注意を呼びかけている([OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/))。OpenAIはその後もAtlas/Work向けの防御強化を継続しており、内部の自動レッドチーム(AIによる攻撃側シミュレーション)で新たな攻撃パターンを洗い出し、敵対的学習させた検知モデルの追加などの対策を重ねていると説明している([Continuously hardening ChatGPT Atlas against prompt injection attacks | OpenAI](https://openai.com/index/hardening-atlas-against-prompt-injection/))。見知らぬサイト・怪しいメールを読ませる作業では特に注意し、重要な操作は最終確認を人間が行う
- **社内システムへの接続は権限を絞る**: Gmail・カレンダー・GitHub・Salesforceなどを「Plugins」として接続すると、ChatGPT Workがその中のデータを読み書きできるようになる。業務で使う場合は、必要最小限のサービスだけを接続し、機密性の高いメール・ファイルを扱うアカウントでの利用は事前に社内ルールを確認する
- **クレジット・実行回数はすぐに消費する**: 1つの依頼で何ステップも「検索→クリック→確認」を繰り返すため、通常のチャットより消費量が大きい。WorkとCodexは共通のクレジット枠を消費するため、重要でない検証にWorkを使いすぎると、コーディング用途も含めた月間の上限を早く使い切ってしまう
- **deep researchとChatGPT Workを混同しない**: 「調べて」だけの依頼ならdeep research(読み取り専用)で十分。「実際に操作(注文・予約・送信)や成果物作成まで」進めたい場合だけWorkモードを選ぶ。逆に、操作が必要な依頼をdeep researchに投げても実行はされない

## 最初の一歩

まずは購入や送信を含まない、読み取り中心の依頼(上記の新幹線の比較調査の例など)をWorkモードで1回試し、AIが画面をどう操作しているかを実際に眺めてみる。慣れてきたら、毎週決まって確認している定型作業(業界ニュースの要約など)を1つ選び、Tasksとしてスケジュール登録してみるとよい。

## 関連トピック

- [ChatGPTのWeb検索機能](./chatgpt-web-search-feature.md)
- [AIエージェントとは何か](../part12-ai-trends/ai-agent-basics.md)
- [生成AIによる情報収集・リサーチの実務活用(Deep Research機能)](../part11-business-practice/ai-research-and-information-gathering.md)
- [ChatGPTのプラン比較](./chatgpt-plan-comparison.md)
- [主要AIチャットツールのエージェント機能・スケジュールタスク比較](./ai-chat-tools-agent-tasks-comparison.md)

## 更新履歴

### 2026-07-27: ChatGPT Agentが「ChatGPT Work」へ改名・再編されたことを反映し全面更新
- **内容**: 2026年7月9日にOpenAIがChatGPTをChat/Work/Codexの3モード構成に再編し、旧「ChatGPT Agent(エージェントモード)」が「ChatGPT Work」に改名・拡張されたことを反映。ヘルプセンターの旧「ChatGPT agent」ページが提供終了案内に切り替わっている点、外部連携が「アプリ(apps)」から「Plugins」へ再度改称された点、対応プランの展開状況(Web/モバイルはPro/Enterprise/Edu先行→Plus/Businessへ拡大、デスクトップはFree含む全プラン)、Tasksのヘルプページ名称変更(「Tasks in ChatGPT」)、deep researchが引き続き独立モードとして残っている点、プロンプトインジェクション対策の継続的強化を追記し、コピペ例・手順・対応表・注意点を現行の名称・挙動に合わせて書き換えた
- **出典**: [ChatGPT is now a partner for your most ambitious work | OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)、[ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275)、[ChatGPT Workspace Agents for Enterprise and Business | OpenAI Help Center](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business)、[Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt)、[Connectors in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)、[Continuously hardening ChatGPT Atlas against prompt injection attacks | OpenAI](https://openai.com/index/hardening-atlas-against-prompt-injection/)、[OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/)

### 2026-07-06: 初版執筆
- **内容**: ChatGPT Agentの成り立ち(Operator+Deep Researchの統合、2025年7月)、仮想ブラウザ・コンピュータの仕組み、テイクオーバーモード・確認プロンプト・ウォッチモードといった安全設計、Workspace agents・ChatGPT Atlasとの関係、対応プラン(Plus/Pro/Business/Enterprise/Edu、クレジット制)、Tasks(スケジュールタスク)の仕組み・設定手順・プラン別の上限、deep research/Web検索/AIエージェント全般との使い分け、プロンプトインジェクション等の注意点を整理
- **出典**: [Introducing ChatGPT agent | OpenAI](https://openai.com/index/introducing-chatgpt-agent/)、[ChatGPT agent | OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent)、[ChatGPT agent release notes | OpenAI Help Center](https://help.openai.com/en/articles/11794368-chatgpt-agent-release-notes)、[Connectors in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)、[Scheduled tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)、[Introducing workspace agents in ChatGPT | OpenAI](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)、[OpenAI launches a general purpose agent in ChatGPT | TechCrunch](https://techcrunch.com/2025/07/17/openai-launches-a-general-purpose-agent-in-chatgpt/)、[The glaring security risks with AI browser agents | TechCrunch](https://techcrunch.com/2025/10/25/the-glaring-security-risks-with-ai-browser-agents/)、[OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/)、[OpenAIが「ChatGPT agent」を発表 | Impress Watch](https://forest.watch.impress.co.jp/docs/news/2032283.html)、[「ChatGPT」に自律型AIエージェント機能 | ITmedia](https://www.itmedia.co.jp/aiplus/articles/2507/18/news053.html)
