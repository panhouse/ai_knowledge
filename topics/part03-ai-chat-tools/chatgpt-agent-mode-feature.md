---
title: "ChatGPTのエージェント機能(旧ChatGPT Agent→ChatGPT Work)とスケジュールタスク(Tasks)"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [ChatGPT, ChatGPT Work, ChatGPT Agent, Work, Tasks, タスク自動化, ブラウザ操作, クラウドブラウザ]
created: 2026-07-06
updated: 2026-09-05
---

# ChatGPTのエージェント機能(旧ChatGPT Agent→ChatGPT Work)とスケジュールタスク(Tasks)

## これは何か

通常のChatGPTは、1回の質問に1回の回答を返すだけで、「このサイトを開いて」「フォームに入力して」「予約を確定して」といった実際の操作はユーザー自身がやるしかない。**ChatGPT Work(チャットGPT・ワーク)**は、ChatGPTに組み込まれた**クラウドブラウザ**(OpenAI側のサーバー上で動く仮想ブラウザ環境)を使って、ChatGPT自身がWebサイトを開き、検索・クリック・フォーム入力・ファイル作成といった複数ステップの作業を、人間の代わりに最後までやり切る機能である。「競合5社を調べて比較表を作る」「ある商品をカートに入れて確認画面まで進める」「ログインが必要な会計ソフトに請求書を提出する」のような、これまで人が何度もブラウザを往復して行っていた作業を、目的(ゴール)を渡すだけで代行し、スプレッドシート・スライド・ドキュメント・簡単なWebアプリといった**完成した成果物**として返してくれる。

このChatGPT Workは、2026年7月9日にOpenAIが発表した名称で、それまで「**ChatGPT Agent**」「エージェントモード」と呼ばれていた機能が改名・拡張されたものである。ヘルプセンターの「ChatGPT agent」ページも現在は「ChatGPT agentは提供終了し、複数ステップの作業と成果物の作成にはChatGPT Workを使ってほしい」という案内に切り替わっている([ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275))。本ページや社内の過去のやり取りで「ChatGPT Agent」「エージェントモード」という表記を見かけた場合は、現行のChatGPT Workのことだと読み替えてよい。

これとは別に、**Tasks(タスク/スケジュールタスク)**という機能もある。こちらはクラウドブラウザを伴わない軽量な仕組みで、「毎週月曜9時に業界ニュースを要約して送って」のように、決まった時刻・周期でChatGPTに同じ依頼を自動的に繰り返させるものである。「都度お願いするのを忘れる」「毎回同じ質問を打つのが手間」という悩みを解決する。本ページでは、この2つ(能動的に操作を代行するChatGPT Workと、時間で自動起動するTasks)をまとめて「ChatGPTの自律実行系機能」として扱う。

## 仕組み・背景

### ChatGPT Agentの成り立ちと「ChatGPT Work」への改名(2026年7月)

現在のChatGPT Workは、もともと2つの機能が統合されて生まれたものである。

- **Operator**: 2025年1月に発表された、仮想ブラウザを操作してWebサイト上のタスク(予約・注文フォーム入力など)を代行する専用ツール
- **Deep Research**: Web上の情報を自律的に調べ回り、出典付きの長文レポートにまとめる調査特化のモード(詳しくは[Deep Research機能](../part12-business-practice/ai-research-and-information-gathering.md)を参照)

2025年7月17日、OpenAIはこの2つと通常のChatGPTの対話能力を統合し、単一の「ChatGPT agent」として再構成した([Introducing ChatGPT agent | OpenAI](https://openai.com/index/introducing-chatgpt-agent/))。単体ツールとしてのOperatorは2025年8月31日で提供終了し、その機能はChatGPT Agentに一本化された。

その後、2026年7月9日にOpenAIは新モデルファミリー「GPT-5.6」の投入に合わせ、ChatGPTを**Chat(通常の対話)・Work(複数ステップの自律作業)・Codex(ソフトウェア開発)**という3モード構成に再編し、旧「ChatGPT agent(エージェントモード)」は「**ChatGPT Work**」という名称に一本化された。OpenAIはこれを「答えを作るAIから、仕事を仕上げるAIへ」という位置付けで発表しており、数時間かかるような複雑なプロジェクトを小さなステップに分解し、独力で進め続けられる点を強調している([ChatGPT is now a partner for your most ambitious work | OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/))。

なお、「調査だけしてほしい(Deep Research相当)」の入口は今回の再編後も別モードとして残っており、2026年9月時点でもdeep researchはChatGPT Workに統合されず、ツールメニューの中に独立した選択肢として引き続き存在している。「調べるだけ」か「操作・成果物作成までしてほしい」かで使い分ける構図に変わりはない。

### 「ChatGPT Atlas」終了とクラウドブラウザへの一本化(2026年8月)

独自ブラウザ「ChatGPT Atlas」(2025年10月提供開始)は、公開から1年足らずの**2026年8月9日にサービスを終了した**。OpenAIは7月9日の時点で終了を予告しており、Atlasが持っていたブラウザ型エージェント機能(エージェントモード・ブラウザ記憶)は、ChatGPT本体(デスクトップアプリ)・Chrome拡張機能・Codexへと統合された([OpenAIのブラウザ「ChatGPT Atlas」終了へ 公開から1年足らずで | ITmedia NEWS](https://www.itmedia.co.jp/news/articles/2607/13/news090.html))。ブックマーク・Cookie・ログインセッションは自動移行されないため、Atlasを使っていた場合は終了前にエクスポート・記録が必要だった。現在「AI内蔵ブラウザでの操作」を試したい場合は、ChatGPT Work(本体)またはChrome拡張機能(Claude in Chromeのような他社の拡張版に相当)を使う形に一本化されている。

### 動作の仕組み(2026年8月更新: クラウドブラウザ化)

ChatGPT Workは、2026年8月の更新で**クラウドブラウザ**(OpenAI側のサーバー上で常時動くブラウザ環境)に切り替わり、デスクトップアプリだけでなくWeb版・モバイル版からもアクセスできるようになった。ユーザーは、AIがマウス操作・クリック・入力を行っている様子をリアルタイムの画面としてそのまま眺めることができ、途中で止めたり指示を追加したりできる。クラウド上で動くため、PCの電源を切ったり画面を閉じたりしても、裏側で作業を継続させたまま他の作業に移ることができる。仮想環境の中で検索・サイト巡回・フォーム入力に加えて、コードの実行や、スプレッドシート・スライド・簡易なWebアプリ(「Sites」と呼ばれる成果物形式)の作成まで行える。

Gmail・Googleカレンダー・Google ドライブ・GitHub・Outlook・SharePoint・Dropbox・Box・HubSpot・Linear・Teams・Slack・Salesforce・Figma・Adobe Acrobat・Zoom・Canvaなどの外部サービスは、「**Plugins(プラグイン)**」ディレクトリを通じて連携できる。この呼び方は2025年12月に「コネクタ(connectors)」から「アプリ(apps)」へ、2026年7月にさらに「Plugins」へと変わったが、正確には「Plugins」は個々の連携(スキル・アプリ・テンプレート)を束ねて発見・有効化しやすくする**カタログ(ディレクトリ)の呼び名**で、Gmail・Slackのような個別の連携そのものは引き続き「**アプリ(apps)**」と呼ばれている([Apps in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt))。社内カレンダーの空き時間を見てメールを起草する、Salesforceの商談ステータスを更新する、といった横断作業も可能になっている。

安全面では、次の仕組みが用意されている。

- **セキュアなサインインフォーム(2026年8月25日〜)**: ログインが必要なサイトの操作を頼むと、専用の安全なサインイン画面が表示され、ユーザーがそこにID・パスワードを入力する。入力内容はChatGPT(AIモデル)側からは一切見えず、保存もされない仕組みになっている。2要素認証(2FA)の入力もこの画面内で行える。一度サインインすると、そのサイトのログインセッションはクラウドブラウザ上に保持され、次回以降の依頼でも再ログインなしで作業を継続できる([ChatGPT Work、ログイン必要なサイトも操作可能に「パスワードは一切見ない」| ITmedia NEWS](https://www.itmedia.co.jp/aiplus/article/2608/26/2000000788/)、[ChatGPTでのクラウドブラウザーの使用 | OpenAI Help Center](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt))。保持されたセッションは、設定画面の「**設定→クラウドブラウザ**」からサイトごとに一覧・削除でき、まとめて「すべてクリア」することもできる
- **テイクオーバーモード(takeover mode)**: 決済情報の入力など、上記のサインインフォームでカバーされない機微な操作が必要な場面では、ユーザーが画面を一時的に引き取って自分の手で入力する。入力した内容をChatGPT側が記録・保存することはない
- **確認プロンプト**: メール送信・注文確定・予約確定など、後戻りしにくい(消費者にとって重要な)操作の直前で、AIが自動的に停止し「実行してよいか」を確認してくる。この確認を省略する「常に許可する(Always allow)」設定も用意されているが、認証・決済が絡む操作では毎回の確認を残すことが推奨されている
- **ウォッチモード(watch mode)**: 金融機関のサイトなど特に慎重な扱いが必要なサイトのカテゴリでは、ユーザーが画面を見て見守っていることを前提に動作し、目を離すと一時停止する

### 関連する製品群(2026年9月時点)

- **ChatGPT Workspace agents**: チームで共有・スケジュール実行できる、より本格的な業務ワークフロー向けのエージェント機能(週次の指標レポート作成、ITチケットの一次対応など)。Business/Enterprise/Edu向けの機能として、個人向けのChatGPT Workとは別のヘルプページ・設定画面で案内されている([ChatGPT Workspace Agents for Enterprise and Business | OpenAI Help Center](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business))。本ページで扱う個人向けのChatGPT Work/Tasksとは別物で、対象読者(チーム管理者)や設定場所が異なる
- **ChatGPT Atlas(ブラウザ)は終了済み**: 2025年10月に登場したOpenAI製の独立ブラウザは2026年8月9日にサービスを終了し、機能はChatGPT本体・Chrome拡張機能・Codexに統合された(前述)
- **Codexモード**: 3モード再編で新設された、ソフトウェア開発に特化したモード。コーディング支援AIとしての位置付けであり、業務資料の作成・調査・操作の代行を目的とする本ページのChatGPT Workとは用途が異なる。WorkとCodexは利用枠(クレジット)を共有する
- **GPT-6 Astra(2026年9月3日発表、展開開始直後)**: OpenAIが「コンピュータ操作」に特化した新世代モデルとして発表した最新モデル。既存アプリのUIを画面越しに直接操作できる「computer use」機能を持ち、ChatGPT Workと組み合わせることで、既存のテンプレート・書式に沿ったスライド・資料・スプレッドシート作成の精度向上が見込まれている。発表当日は招待制の「Daybreak」プログラム参加企業から先行提供され、数日以内にPlus・Pro・Business・Enterprise(API・AWS含む)へ順次拡大するとされているが、本ページ執筆時点(2026年9月5日)ではまだ展開の初期段階であり、対応範囲・料金体系は流動的な点に注意したい([OpenAI announces rollout of GPT-6 Astra model | CNBC](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html))
- **呼び方は今後も変わりうる**: ChatGPTのエージェント系機能は「Operator→ChatGPT Agent→ChatGPT Work」と1年半で2度名称が変わり、周辺機能も「Atlas終了→クラウドブラウザへ統合」「connectors→apps→Plugins」と目まぐるしく変化している。今後も呼び方・提供形態が変わる可能性がある点は念頭に置いておきたい

### Tasksの仕組み

Tasksは、ChatGPT Workのようなクラウドブラウザは使わない、より軽量な機能である。指定した日時・周期でChatGPTへの依頼(プロンプト)を自動的に再実行するだけの仕組みで、リマインダー・定期的な要約・簡単な監視(「値下げがあったら教えて」など、Web検索を伴う範囲まで)に向いている。ヘルプセンターの案内ページも、従来の「Scheduled tasks in ChatGPT」から「**Tasks in ChatGPT**」という見出しに変わっており、ChatGPT Work配下の一機能として位置付けられている([Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt))。

## 使いどころ・使い分け

| 機能 | 何をしてくれるか | かかる時間 | 向いている場面 |
|---|---|---|---|
| 通常のチャット(Chatモード) | その場で1回答える | 数秒 | 一般知識の相談、下書き、アイデア出し |
| [Web検索機能](./chatgpt-web-search-feature.md) | 1〜数回検索し、その場で要約して答える | 数秒〜数十秒 | 鮮度が必要な単発の事実確認 |
| deep research(調査モード) | 自律的に多数のサイトを読み回り、出典付きレポートを作る(**読み取りのみ**、操作は行わない) | 数分〜数十分 | 競合比較・市場調査など複数ソースの横断調査。詳細は[Deep Research機能](../part12-business-practice/ai-research-and-information-gathering.md) |
| **ChatGPT Work(旧ChatGPT Agent/エージェントモード)** | クラウドブラウザで実際にクリック・入力・購入・ログイン・ファイル作成まで**操作を実行**し、完成した成果物(表・資料・簡易Webアプリ)として返す | 数分〜数時間 | 予約・注文・フォーム提出・ログインが必要な社内SaaSを含む複数サイト横断作業の代行、成果物の作成まで一括で頼みたいとき |
| **Tasks(スケジュールタスク)** | 指定した日時・周期でプロンプトを自動再実行する(クラウドブラウザなし) | 実行のたびに数秒〜数分 | 定期リマインダー、週次・日次の定型要約、簡易な定期監視 |
| Codexモード | コードの生成・修正・実行に特化 | 数分〜 | ソフトウェア開発(本ページの対象外) |

判断の目安は次の2つ。

1. **「調べるだけ」か「実際に操作・成果物作成までしてほしい」か**: 読み取りだけならdeep research、フォーム送信・注文・予約・ログイン・ファイル作成など「後戻りしにくい操作」や「完成品が欲しい」場合はChatGPT Work
2. **「今すぐ1回」か「決まった周期で繰り返す」か**: 今すぐ1回で完結する作業ならChatGPT Work、同じ依頼を定期的に繰り返したいならTasks(Tasksの実行内容が調査中心であればdeep research相当の処理が、操作を含む場合はWork相当の処理が、裏側で毎回走る)

なお、「ChatGPT Work」はOpenAIというひとつの提供元の実装名であり、Google・Anthropic・Microsoftなど各社にもブラウザ操作型・業務自動化型のエージェントが存在する。ベンダーを横断した「AIエージェントとは何か」という概念・分類・導入の判断軸は[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)で扱っているので、社内でエージェント導入の方針を検討する際はそちらも参照してほしい。本ページはChatGPTというツールに閉じた「画面のどこで・どう使うか」の実務ガイドに徹する。

## 実務での使い方

### ChatGPT Workの使い方(2026年9月時点)

1. デスクトップアプリ・Web版・モバイル版とも、画面上部(左上)のモード切り替えから「**Work**」を選ぶ
2. 依頼内容を入力すると、画面内にクラウドブラウザの実行画面が表示され、AIが検索・クリック・入力を進めていく様子がそのまま見える。クラウド上で実行されるため、PCをスリープ・シャットダウンしても裏側で処理が継続し、他の作業やモバイルからの進捗確認に移ることもできる
3. ログインが必要な場面になると、セキュアなサインインフォームが表示されるので、その場でID・パスワード(必要なら2FA)を入力する。入力内容はAIモデル側には見えず、次回以降の依頼ではこのログインセッションが自動的に再利用される
4. パスワード入力の枠に収まらない決済情報の入力などは、従来どおりテイクオーバーモードに切り替わる通知が出るので、その場面だけ自分の手で入力する
5. メール送信や注文確定など後戻りしにくい操作の前には、確認ダイアログが出るので、内容を確認してから許可する(「常に許可する」は認証・決済が絡む操作では避ける)
6. 完了すると、作業結果(作成したファイル・調べた内容の要約・実行済み操作の記録)がチャット欄に返ってくる
7. 特定サイトへのログイン状態を維持したくない場合は、「設定→クラウドブラウザ」からそのサイトのセッションを個別に削除するか、「ブラウザデータをすべてクリア」で一括削除する

**対応プラン・利用量(2026年9月5日時点)**:

- **Web・モバイル版**: Plus・Pro・Business・Enterprise・Eduで利用可能。Free・Goは対象に含まれない
- **デスクトップアプリ**: Free・Goでも「限定的なアクセス」として利用でき、使用モデルはGPT-5.6 Terra(軽量ティア)に固定される。Plus以上ではSol/Terra/Lunaを状況に応じて使い分けられる
- **利用量**: Codexと共通の「エージェント利用枠(クレジット)」を消費する。**2026年8月25日、Plusプランに「5時間ごとのローリング制限」が復活**し、Work/Codexの利用がこの枠を共有するようになった(Proは当面この制限の対象外)。Plusでは5時間ごとの上限に加えて週単位の上限もあり、上限に達すると時間経過を待つか、追加クレジットを購入して継続する([ChatGPT Workが要ログインサイトの作業も代行。Plusは5時間制限復活 | PC Watch](https://pc.watch.impress.co.jp/docs/news/2135792.html))
- **Business**: 同時期に、5倍相当の利用枠を持ち5時間制限が撤廃される「**Premiumシート**」(1ユーザー月払い$125程度)が新設され、従来の「Standardシート」と混在させて割り当てられるようになった(詳しくは[ChatGPTのプラン比較](./chatgpt-plan-comparison.md)を参照)
- **ログイン必要サイトへの対応**: 2026年9月5日時点でPlus・Pro・Businessに展開済み。Free・Goは対象外、Enterprise・Eduは本ページ執筆時点でまだ対応が案内されていない
- **GPT-6 Astra**: 2026年9月3日の発表直後で、Daybreakプログラム参加企業からの先行提供が始まった段階。Plus/Pro/Business/Enterpriseへの展開は「数日以内」とされているが、確定的な提供状況は変わりやすいため、利用時は画面上の表示・OpenAIの最新告知で確認する

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

ログインが必要な社内サイトを含む依頼(2026年8月以降の新機能を使う例):

```
Workモードで、経費精算システム(社内SaaS)にログインし、
今月分の交通費の入力状況を確認してください。未入力の項目があれば
一覧にして教えてください。新規の申請や承認操作は行わないでください。
```

### Tasksの設定・管理方法

1. 依頼文の中で日時・周期を明示して頼む(例:「毎週月曜の朝9時に、業界ニュースを3行で要約して送って」)、または回答画面の時計アイコンから「タスクとして保存」を選ぶ
2. サイドバーの「タスク(Tasks)」一覧から、設定済みのタスクを確認できる。次回実行時刻・実行内容が表示される
3. 各タスクは一覧から一時停止・再開・内容の編集・削除ができる
4. 実行結果は通知として届き、チャット履歴にも残る。長期間反応がないまま放置されたタスクは、自動的に一時停止扱いになることがある

**対応プラン・上限**: Tasksは2026年9月時点でGo・Plus・Pro・Business・Enterprise・Eduで利用でき(Freeは対象外)、同時に有効化できるタスク数の上限はGoが3件、Plusが5件、Business/Eduが10件、Pro/Enterpriseが15件となっている。1つのタスクを1時間に2回以上実行するような高頻度の設定はできない([Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt))。

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

各社の詳しい分類・導入判断は[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)、機能名・対応プランの横並び比較は[主要AIチャットツールのエージェント機能・スケジュールタスク比較](./ai-chat-tools-agent-tasks-comparison.md)にまとめているので、そちらを参照してほしい。

## 注意点・よくある誤解

- **「エージェントモード」という表記も「ChatGPT Atlas」という独立ブラウザも、現行UIにはもう存在しない**: 2026年7月9日以降、画面上の呼び方は「Work」に統一され、2026年8月9日にはブラウザ単体アプリの「ChatGPT Atlas」自体が終了した。社内マニュアルやブックマークした手順書に古い名称が書いてある場合は、モード切り替えから「Work」を選ぶ手順に読み替える
- **ログインセッションがクラウド側に保持される点に注意**: 2026年8月以降、一度サイトにサインインすると、そのログインセッションはOpenAIのサーバー(クラウドブラウザ)上に保持され、次回以降の依頼で再利用される。共有PC・退職者アカウントの整理・機密性の高い社内システム(経理・人事など)を扱った後は、「設定→クラウドブラウザ」からセッションを都度クリアする運用ルールを決めておく
- **「常に許可する(Always allow)」設定は慎重に使う**: 確認プロンプトを省略できる設定だが、ログイン・決済・送信など後戻りしにくい操作にまで適用すると、確認なしに実行されてしまう。認証・決済が絡む操作では毎回確認する設定のままにしておく
- **確認プロンプトがあっても「丸投げして安全」にはならない**: 送信・注文・予約の直前には確認が入る設計だが、確認画面自体の内容を読まずに許可してしまえば事故は防げない。重要な操作を含む依頼では、確認ダイアログの内容を必ず読んでから許可する
- **プロンプトインジェクションのリスクは解消されていない**: ブラウザ操作型AIに対するプロンプトインジェクション(閲覧先のページに埋め込まれた悪意ある指示にAIが誘導される攻撃)を完全に防ぐ方法は業界全体として確立されておらず、OpenAIも「完全に解決できない可能性がある」との立場を続けている([OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/))。ログイン機能でアクセスできる範囲が広がった2026年8月以降は、見知らぬサイト・怪しいメールを読ませる作業では特に注意し、重要な操作は最終確認を人間が行う
- **社内システムへの接続は権限を絞る**: Gmail・カレンダー・GitHub・Salesforceなどを「アプリ」として接続すると、ChatGPT Workがその中のデータを読み書きできるようになる。2026年8月以降はログインが必要な社内SaaSにも直接アクセスできるようになったため、業務で使う場合は必要最小限のサービス・アカウントだけを接続し、機密性の高いメール・ファイルを扱うアカウントでの利用は事前に社内ルールを確認する
- **クレジット・実行回数はすぐに消費する**: 1つの依頼で何ステップも「検索→クリック→確認」を繰り返すため、通常のチャットより消費量が大きい。加えて2026年8月25日にPlusプランで5時間ごとのローリング制限が復活し、WorkとCodexで共通の枠を消費するため、重要でない検証にWorkを使いすぎると、コーディング用途も含めた利用枠を早く使い切ってしまう(Business Premiumシートやクレジット追加購入で緩和は可能)
- **deep researchとChatGPT Workを混同しない**: 「調べて」だけの依頼ならdeep research(読み取り専用)で十分。「実際に操作(注文・予約・送信)や成果物作成まで」進めたい場合だけWorkモードを選ぶ。逆に、操作が必要な依頼をdeep researchに投げても実行はされない
- **GPT-6 Astraは発表直後で流動的**: 2026年9月3日に発表されたばかりのモデルで、本ページ執筆時点では一部企業向けの先行提供段階にある。「使えるはず」という前提で業務フローを組む前に、自分の契約プランで実際に選択肢に表示されるかを確認する

## 最初の一歩

まずは購入や送信を含まない、読み取り中心の依頼(上記の新幹線の比較調査の例など)をWorkモードで1回試し、AIが画面をどう操作しているかを実際に眺めてみる。慣れてきたら、毎週決まって確認している定型作業(業界ニュースの要約など)を1つ選び、Tasksとしてスケジュール登録してみるとよい。

## 関連トピック

- [ChatGPTのWeb検索機能](./chatgpt-web-search-feature.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [生成AIによる情報収集・リサーチの実務活用(Deep Research機能)](../part12-business-practice/ai-research-and-information-gathering.md)
- [ChatGPTのプラン比較](./chatgpt-plan-comparison.md)
- [主要AIチャットツールのエージェント機能・スケジュールタスク比較](./ai-chat-tools-agent-tasks-comparison.md)

## 更新履歴

### 2026-09-05: クラウドブラウザ化・ログイン機能・Atlas終了・GPT-6 Astraを反映し全面更新
- **内容**: 2026年8月9日にブラウザ単体アプリ「ChatGPT Atlas」が終了し機能がChatGPT本体・Chrome拡張・Codexへ統合された点、同8月にWorkの実行環境が「クラウドブラウザ」(サーバー上で常時動作、Web/モバイルからもアクセス可)へ切り替わった点、8月25日にログインが必要なサイトを安全に操作できる新機能(セキュアなサインインフォーム、セッション保持、設定→クラウドブラウザでの管理)が追加された点、同日Plusプランに5時間ごとのローリング制限が復活しBusinessにPremiumシートが新設された点、Free・Goでのデスクトップ限定・Terra固定という対応プランの実態、9月3日発表の新モデル「GPT-6 Astra」の位置づけと展開状況(先行提供段階)、「Plugins」と「アプリ」の呼び分けを反映し、対応プラン・注意点・コピペ例を現行の挙動に合わせて全面的に書き換えた
- **出典**: [ChatGPT Work、ログイン必要なサイトも操作可能に「パスワードは一切見ない」| ITmedia NEWS](https://www.itmedia.co.jp/aiplus/article/2608/26/2000000788/)、[ChatGPT Workが要ログインサイトの作業も代行。Plusは5時間制限復活 | PC Watch](https://pc.watch.impress.co.jp/docs/news/2135792.html)、[OpenAIのブラウザ「ChatGPT Atlas」終了へ 公開から1年足らずで | ITmedia NEWS](https://www.itmedia.co.jp/news/articles/2607/13/news090.html)、[ChatGPTでのクラウドブラウザーの使用 | OpenAI Help Center](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)、[OpenAI announces rollout of GPT-6 Astra model | CNBC](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)、[Apps in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)、[ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275)、[Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt)

### 2026-07-27: ChatGPT Agentが「ChatGPT Work」へ改名・再編されたことを反映し全面更新
- **内容**: 2026年7月9日にOpenAIがChatGPTをChat/Work/Codexの3モード構成に再編し、旧「ChatGPT Agent(エージェントモード)」が「ChatGPT Work」に改名・拡張されたことを反映。ヘルプセンターの旧「ChatGPT agent」ページが提供終了案内に切り替わっている点、外部連携が「アプリ(apps)」から「Plugins」へ再度改称された点、対応プランの展開状況(Web/モバイルはPro/Enterprise/Edu先行→Plus/Businessへ拡大、デスクトップはFree含む全プラン)、Tasksのヘルプページ名称変更(「Tasks in ChatGPT」)、deep researchが引き続き独立モードとして残っている点、プロンプトインジェクション対策の継続的強化を追記し、コピペ例・手順・対応表・注意点を現行の名称・挙動に合わせて書き換えた
- **出典**: [ChatGPT is now a partner for your most ambitious work | OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)、[ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275)、[ChatGPT Workspace Agents for Enterprise and Business | OpenAI Help Center](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business)、[Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt)、[Connectors in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)、[Continuously hardening ChatGPT Atlas against prompt injection attacks | OpenAI](https://openai.com/index/hardening-atlas-against-prompt-injection/)、[OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/)

### 2026-07-06: 初版執筆
- **内容**: ChatGPT Agentの成り立ち(Operator+Deep Researchの統合、2025年7月)、仮想ブラウザ・コンピュータの仕組み、テイクオーバーモード・確認プロンプト・ウォッチモードといった安全設計、Workspace agents・ChatGPT Atlasとの関係、対応プラン(Plus/Pro/Business/Enterprise/Edu、クレジット制)、Tasks(スケジュールタスク)の仕組み・設定手順・プラン別の上限、deep research/Web検索/AIエージェント全般との使い分け、プロンプトインジェクション等の注意点を整理
- **出典**: [Introducing ChatGPT agent | OpenAI](https://openai.com/index/introducing-chatgpt-agent/)、[ChatGPT agent | OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent)、[ChatGPT agent release notes | OpenAI Help Center](https://help.openai.com/en/articles/11794368-chatgpt-agent-release-notes)、[Connectors in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)、[Scheduled tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)、[Introducing workspace agents in ChatGPT | OpenAI](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)、[OpenAI launches a general purpose agent in ChatGPT | TechCrunch](https://techcrunch.com/2025/07/17/openai-launches-a-general-purpose-agent-in-chatgpt/)、[The glaring security risks with AI browser agents | TechCrunch](https://techcrunch.com/2025/10/25/the-glaring-security-risks-with-ai-browser-agents/)、[OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/)、[OpenAIが「ChatGPT agent」を発表 | Impress Watch](https://forest.watch.impress.co.jp/docs/news/2032283.html)、[「ChatGPT」に自律型AIエージェント機能 | ITmedia](https://www.itmedia.co.jp/aiplus/articles/2507/18/news053.html)
