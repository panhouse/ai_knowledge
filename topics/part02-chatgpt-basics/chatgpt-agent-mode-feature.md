---
title: "ChatGPTのエージェント機能(ChatGPT Agent)とスケジュールタスク(Tasks)"
part: 2
chapter: "第3章 主要機能"
tags: [ChatGPT, ChatGPT Agent, Agent, Tasks, タスク自動化, ブラウザ操作]
created: 2026-07-06
updated: 2026-07-06
---

# ChatGPTのエージェント機能(ChatGPT Agent)とスケジュールタスク(Tasks)

## これは何か

通常のChatGPTは、1回の質問に1回の回答を返すだけで、「このサイトを開いて」「フォームに入力して」「予約を確定して」といった実際の操作はユーザー自身がやるしかない。**ChatGPT Agent(チャットGPT・エージェント)**は、ChatGPTに組み込まれた仮想のブラウザ・コンピュータ環境を使って、ChatGPT自身がWebサイトを開き、検索・クリック・フォーム入力・ファイル作成といった複数ステップの作業を、人間の代わりに最後までやり切る機能である。「競合5社を調べて比較表を作る」「ある商品をカートに入れて確認画面まで進める」のような、これまで人が何度もブラウザを往復して行っていた作業を、目的(ゴール)を渡すだけで代行してくれる。

これとは別に、**Tasks(スケジュールタスク)**という機能もある。こちらはブラウザ操作を伴わない軽量な仕組みで、「毎週月曜9時に業界ニュースを要約して送って」のように、決まった時刻・周期でChatGPTに同じ依頼を自動的に繰り返させるものである。「都度お願いするのを忘れる」「毎回同じ質問を打つのが手間」という悩みを解決する。本ページでは、この2つ(能動的に操作を代行するChatGPT Agentと、時間で自動起動するTasks)をまとめて「ChatGPTの自律実行系機能」として扱う。

## 仕組み・背景

### ChatGPT Agentの成り立ち

ChatGPT Agentは最初から1つの機能として作られたわけではなく、2つの機能が統合されて生まれた。

- **Operator**: 2025年1月に発表された、仮想ブラウザを操作してWebサイト上のタスク(予約・注文フォーム入力など)を代行する専用ツール
- **Deep Research**: Web上の情報を自律的に調べ回り、出典付きの長文レポートにまとめる調査特化のモード(詳しくは[Deep Research機能](../part10-business-practice/ai-research-and-information-gathering.md)を参照)

2025年7月17日、OpenAIはこの2つと通常のChatGPTの対話能力を統合し、単一の「**ChatGPT agent**」として再構成した([Introducing ChatGPT agent | OpenAI](https://openai.com/index/introducing-chatgpt-agent/))。単体ツールとしてのOperatorは2025年8月31日で提供終了し、その機能はChatGPT Agentに一本化された。2026年7月時点でもこの「ChatGPT agent」という名称に変更はなく、現行の正式な機能名として使われている([ChatGPT agent | OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent))。

なお、実際の画面上では「調査だけしてほしい(Deep Research相当)」と「実際に操作までしてほしい(Operator相当)」を分けて選べる設計が引き継がれており、「deep research」という調査特化モードと、実際にブラウザを操作して行動まで行う「エージェントモード」が、ツール選択メニューの中に別項目として残っている。

### 動作の仕組み

ChatGPT Agentは、画面内に表示される**仮想コンピュータ(サンドボックス化されたブラウザ環境)**の中で作業する。ユーザーは、AIがマウス操作・クリック・入力を行っている様子をリアルタイムの画面としてそのまま眺めることができ、途中で止めたり指示を追加したりできる。仮想環境の中で検索・サイト巡回・フォーム入力に加えて、コードの実行や、スプレッドシート・スライドなどのファイル作成まで行える。

Gmail・Googleカレンダー・Google ドライブ・GitHub・Outlook・SharePoint・Dropbox・Box・HubSpot・Linear・Teamsなどの外部サービスは、「アプリ(apps)」という接続機能(2025年12月に「コネクタ(connectors)」から名称変更)を通じて連携でき、社内カレンダーの空き時間を見てメールを起草する、といった横断作業も可能になっている([Connectors in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt))。

安全面では、次の仕組みが用意されている。

- **テイクオーバーモード(takeover mode)**: ログインのパスワードや決済情報の入力が必要な場面では、AIに直接教えるのではなく、ユーザーが画面を一時的に引き取って自分の手で入力する。入力した内容をChatGPT側が記録・保存することはない
- **確認プロンプト**: メール送信・注文確定など、後戻りしにくい(消費者にとって重要な)操作の直前で、AIが自動的に停止し「実行してよいか」を確認してくる
- **ウォッチモード(watch mode)**: 金融機関のサイトなど特に慎重な扱いが必要なサイトのカテゴリでは、ユーザーが画面を見て見守っていることを前提に動作し、目を離すと一時停止する

### 関連する製品群(2026年7月時点)

- **Workspace agents**: チームで共有・スケジュール実行できる、より本格的な業務ワークフロー向けのエージェント機能(週次の指標レポート作成、ITチケットの一次対応など)。Codexを基盤にした別の新機能で、Business/Enterprise/Edu/Teachers向けのリサーチプレビューとして提供されている([Introducing workspace agents in ChatGPT | OpenAI](https://openai.com/index/introducing-workspace-agents-in-chatgpt/))。本ページで扱う個人向けのChatGPT Agent/Tasksとは別物で、対象読者(チーム管理者)や設定場所が異なる
- **ChatGPT Atlas(ブラウザ)**: 2025年10月に登場したOpenAI製Webブラウザで、ブラウザ自体に「エージェントモード」が内蔵されており、ChatGPT Agentと同じ仕組みをより高速に動かせる(Plus/Pro/Business向け)
- **統合の方向性**: 2026年3月、OpenAIは社内向けにChatGPT・Atlas・Codexを1つのデスクトップアプリに統合する構想を示したと報じられているが、2026年7月時点で実際にリリースはされていない。ChatGPTのエージェント機能の呼び方・提供形態は今後さらに変わる可能性がある点は念頭に置いておきたい

### Tasksの仕組み

Tasksは、ChatGPT Agentのような仮想ブラウザ・コンピュータは使わない、より軽量な機能である。指定した日時・周期でChatGPTへの依頼(プロンプト)を自動的に再実行するだけの仕組みで、リマインダー・定期的な要約・簡単な監視(「値下げがあったら教えて」など、Web検索を伴う範囲まで)に向いている([Scheduled tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt))。

## 使いどころ・使い分け

| 機能 | 何をしてくれるか | かかる時間 | 向いている場面 |
|---|---|---|---|
| 通常のチャット | その場で1回答える | 数秒 | 一般知識の相談、下書き、アイデア出し |
| [Web検索機能](./chatgpt-web-search-feature.md) | 1〜数回検索し、その場で要約して答える | 数秒〜数十秒 | 鮮度が必要な単発の事実確認 |
| deep research(調査モード) | 自律的に多数のサイトを読み回り、出典付きレポートを作る(**読み取りのみ**、操作は行わない) | 数分〜数十分 | 競合比較・市場調査など複数ソースの横断調査。詳細は[Deep Research機能](../part10-business-practice/ai-research-and-information-gathering.md) |
| **ChatGPT Agent(エージェントモード)** | 仮想ブラウザ・コンピュータで実際にクリック・入力・購入・ファイル作成まで**操作を実行**する | 数分〜数十分 | 予約・注文・フォーム提出・複数サイトを横断した作業の代行、成果物(表・資料)の作成まで一括で頼みたいとき |
| **Tasks(スケジュールタスク)** | 指定した日時・周期でプロンプトを自動再実行する(ブラウザ操作なし) | 実行のたびに数秒〜数分 | 定期リマインダー、週次・日次の定型要約、簡易な定期監視 |

判断の目安は次の2つ。

1. **「調べるだけ」か「実際に操作までしてほしい」か**: 読み取りだけならdeep research、フォーム送信・注文・予約など「後戻りしにくい操作」を含むならChatGPT Agent
2. **「今すぐ1回」か「決まった周期で繰り返す」か**: 今すぐ1回で完結する作業ならChatGPT Agent、同じ依頼を定期的に繰り返したいならTasks(Tasksの実行内容が調査中心であればdeep research相当の処理が、操作を含む場合はエージェント相当の処理が、裏側で毎回走る)

なお、「ChatGPT Agent」はOpenAIというひとつの提供元の実装名であり、Google・Anthropic・Microsoftなど各社にもブラウザ操作型・業務自動化型のエージェントが存在する。ベンダーを横断した「AIエージェントとは何か」という概念・分類・導入の判断軸は[AIエージェントとは何か](../part11-ai-trends/ai-agent-basics.md)で扱っているので、社内でエージェント導入の方針を検討する際はそちらも参照してほしい。本ページはChatGPTというツールに閉じた「画面のどこで・どう使うか」の実務ガイドに徹する。

## 実務での使い方

### ChatGPT Agentの使い方(2026年7月時点)

1. メッセージ入力欄の「+」(ツール)ボタンをクリックし、一覧から「エージェントモード」(agent mode)を選ぶ。プロンプトの中に「エージェントモードで〇〇して」と明示的に書いても起動できる
2. 依頼内容を入力すると、画面内に仮想ブラウザの実行画面が表示され、AIが検索・クリック・入力を進めていく様子がそのまま見える
3. ログインや決済情報の入力が必要な場面になると、テイクオーバーモードに切り替わる通知が出るので、その場面だけ自分の手で入力する
4. メール送信や注文確定など後戻りしにくい操作の前には、確認ダイアログが出るので、内容を確認してから許可する
5. 完了すると、作業結果(作成したファイル・調べた内容の要約・実行済み操作の記録)がチャット欄に返ってくる

**対応プラン**: 2026年7月時点でChatGPT Agentが使えるのはPlus・Pro・Business・Enterprise・Eduで、Free・Go(グローバル向けの低価格プラン)では利用できない。利用回数は共通の「クレジット」制に統一されており、プランごとに月間の付与量が異なる(Proは他プランより多くの回数を実行できる)。クレジットは付与から12か月間有効で、消費した分だけ追加購入もできる([ChatGPT agent | OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent)、関連リリースノート: [ChatGPT agent release notes](https://help.openai.com/en/articles/11794368-chatgpt-agent-release-notes))。

### コピペで使える実例

読み取り中心で、後戻りしにくい操作を含まない依頼(初めて試すのに向く):

```
エージェントモードで、来週の月曜〜水曜に東京→大阪を新幹線で移動する場合の
時間帯別の空席状況と料金を調べて、比較しやすい表にまとめてください。
チケットの購入や予約は行わず、調査結果の報告だけをお願いします。
```

操作(注文確定手前まで)を含む依頼(確認プロンプトが挟まることを前提に):

```
エージェントモードで、〇〇(通販サイト名)で△△(商品名)を検索し、
条件に近い上位3件を比較したうえで、最も条件に合う商品をカートに入れてください。
購入の確定は行わず、確認画面の手前で止めて私に知らせてください。
```

### Tasksの設定・管理方法

1. 依頼文の中で日時・周期を明示して頼む(例:「毎週月曜の朝9時に、業界ニュースを3行で要約して送って」)、または回答画面の時計アイコンから「タスクとして保存」を選ぶ
2. サイドバーの「タスク(Scheduled)」一覧から、設定済みのタスクを確認できる。次回実行時刻・実行内容が表示される
3. 各タスクは一覧から一時停止・再開・内容の編集・削除ができる
4. 実行結果は通知として届き、チャット履歴にも残る

**対応プラン・上限**: Tasksは2026年7月時点でGo・Plus・Pro・Business・Enterprise・Eduで利用でき、同時に有効化できるタスク数の上限はGoが3件、Plusが5件、Business/Eduが10件、Pro/Enterpriseが15件となっている。1つのタスクを1時間に2回以上実行するような高頻度の設定はできない([Scheduled tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt))。

コピペで使える例:

```
毎週月曜日の朝9時に、直近1週間の生成AI関連の主要ニュースをWeb検索で調べて、
3行以内の日本語サマリーで送ってください。個別の製品リリースよりも、
業務での使い方に影響しそうな話題を優先してください。
```

### 主要ツールでの対応付け

| 概念 | ChatGPT(OpenAI) | Google | Anthropic | Microsoft |
|---|---|---|---|---|
| 呼び方 | ChatGPT Agent(旧Operator+Deep Research) | Gemini Spark(旧Project Mariner系機能を統合) | Computer Use(Claude・Claude Code経由) | Copilot Agents / Copilot Studio |
| スケジュール実行 | Tasks(スケジュールタスク) | Gemini内のスケジュール機能 | Claude Agent SDK側でスケジューリングを組む(標準UIでの定期実行は限定的) | Copilot Studio上でのトリガー設定 |

各社の詳しい分類・導入判断は[AIエージェントとは何か](../part11-ai-trends/ai-agent-basics.md)にまとめているので、そちらを参照してほしい。

## 注意点・よくある誤解

- **確認プロンプトがあっても「丸投げして安全」にはならない**: 送信・注文・予約の直前には確認が入る設計だが、確認画面自体の内容を読まずに許可してしまえば事故は防げない。重要な操作を含む依頼では、確認ダイアログの内容を必ず読んでから許可する
- **プロンプトインジェクションのリスクは解消されていない**: OpenAIは2025年12月、ChatGPT AgentやAtlasのようなブラウザ操作型AIに対するプロンプトインジェクション(閲覧先のページに埋め込まれた悪意ある指示にAIが誘導される攻撃)について、「完全に解決できない可能性がある」と公表しており、英国のNCSC(国家サイバーセキュリティセンター)も同様の注意を呼びかけている([OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/))。2025年10月にはTechCrunchが、悪意あるページの隠れた指示によって意図しない購入や操作が起きうる懸念を報じている([The glaring security risks with AI browser agents | TechCrunch](https://techcrunch.com/2025/10/25/the-glaring-security-risks-with-ai-browser-agents/))。見知らぬサイト・怪しいメールを読ませる作業では特に注意し、重要な操作は最終確認を人間が行う
- **社内システムへの接続は権限を絞る**: Gmail・カレンダー・GitHubなどを「アプリ」として接続すると、ChatGPT Agentがその中のデータを読み書きできるようになる。業務で使う場合は、必要最小限のサービスだけを接続し、機密性の高いメール・ファイルを扱うアカウントでの利用は事前に社内ルールを確認する
- **クレジット・実行回数はすぐに消費する**: 1つの依頼で何ステップも「検索→クリック→確認」を繰り返すため、通常のチャットより消費量が大きい。重要でない検証にエージェントモードを使うと、月間の上限を早く使い切ってしまう
- **deep researchとChatGPT Agentを混同しない**: 「調べて」だけの依頼ならdeep research(読み取り専用)で十分。「実際に操作(注文・予約・送信)まで」進めたい場合だけエージェントモードを選ぶ。逆に、操作が必要な依頼をdeep researchに投げても実行はされない
- **セキュリティ更新は継続中**: 2026年2月には、ChatGPTのDNS(ドメイン名の仕組み)を利用したデータ漏えいの脆弱性が報告・修正されている(悪用が確認された事例はないが、ログイン中のメール・カレンダーへのアクセス権を与える際の一般的な留意点として押さえておきたい)

## 最初の一歩

まずは購入や送信を含まない、読み取り中心の依頼(上記の新幹線の比較調査の例など)をエージェントモードで1回試し、AIが画面をどう操作しているかを実際に眺めてみる。慣れてきたら、毎週決まって確認している定型作業(業界ニュースの要約など)を1つ選び、Tasksとしてスケジュール登録してみるとよい。

## 関連トピック

- [ChatGPTのWeb検索機能](./chatgpt-web-search-feature.md)
- [AIエージェントとは何か](../part11-ai-trends/ai-agent-basics.md)
- [生成AIによる情報収集・リサーチの実務活用(Deep Research機能)](../part10-business-practice/ai-research-and-information-gathering.md)
- [ChatGPTのプラン比較](./chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: ChatGPT Agentの成り立ち(Operator+Deep Researchの統合、2025年7月)、仮想ブラウザ・コンピュータの仕組み、テイクオーバーモード・確認プロンプト・ウォッチモードといった安全設計、Workspace agents・ChatGPT Atlasとの関係、対応プラン(Plus/Pro/Business/Enterprise/Edu、クレジット制)、Tasks(スケジュールタスク)の仕組み・設定手順・プラン別の上限、deep research/Web検索/AIエージェント全般との使い分け、プロンプトインジェクション等の注意点を整理
- **出典**: [Introducing ChatGPT agent | OpenAI](https://openai.com/index/introducing-chatgpt-agent/)、[ChatGPT agent | OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent)、[ChatGPT agent release notes | OpenAI Help Center](https://help.openai.com/en/articles/11794368-chatgpt-agent-release-notes)、[Connectors in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)、[Scheduled tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)、[Introducing workspace agents in ChatGPT | OpenAI](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)、[OpenAI launches a general purpose agent in ChatGPT | TechCrunch](https://techcrunch.com/2025/07/17/openai-launches-a-general-purpose-agent-in-chatgpt/)、[The glaring security risks with AI browser agents | TechCrunch](https://techcrunch.com/2025/10/25/the-glaring-security-risks-with-ai-browser-agents/)、[OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/)、[OpenAIが「ChatGPT agent」を発表 | Impress Watch](https://forest.watch.impress.co.jp/docs/news/2032283.html)、[「ChatGPT」に自律型AIエージェント機能 | ITmedia](https://www.itmedia.co.jp/aiplus/articles/2507/18/news053.html)
