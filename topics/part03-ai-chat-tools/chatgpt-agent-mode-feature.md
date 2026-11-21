---
title: "ChatGPTのエージェント機能(ChatGPT Work・dots)とスケジュールタスク"
part: 3
chapter: 第4章 生成・分析の主要機能
tags: [ChatGPT, ChatGPT Work, dots, ChatGPT Agent, 常時稼働型エージェント, スケジュールタスク, タスク自動化, ブラウザ操作, クラウドブラウザ]
created: 2026-07-06
updated: 2026-11-21
---

# ChatGPTのエージェント機能(ChatGPT Work・dots)とスケジュールタスク

## これは何か

通常のChatGPTは、1回の質問に1回の回答を返すだけで、「このサイトを開いて」「フォームに入力して」「資料を仕上げて」といった実際の作業はユーザー自身がやるしかない。2026年11月時点のChatGPTには、この「作業そのもの」を任せるための仕組みが3つある。

- **ChatGPT Work(ワーク)**: 入力欄の上でモードを「Work」に切り替えて依頼すると、ChatGPTが**クラウドブラウザ**(OpenAI側のサーバー上で動く仮想ブラウザ)やアプリ連携を使い、検索・クリック・フォーム入力・ファイル作成といった複数ステップの作業を最後までやり切り、スプレッドシート・スライド・ドキュメントなどの**完成した成果物**として返す。「依頼したら動く」**依頼型**のエージェント
- **dots(ドッツ)**: 2026年9月29日のDevDay 2026で発表された**常時稼働型**のエージェント。1つひとつの「dot」が専用のクラウドコンピュータを持ち、利用者が画面を閉じている間も目標に向けて下調べ・定期チェック・提案を続ける。ChatGPTのほか、Slack・Microsoft Teamsからも話しかけられる「専属アシスタント」に近い存在
- **スケジュールタスク(Scheduled)**: 「毎週月曜9時に業界ニュースを要約して」のように、決まった時刻・周期、あるいは「新着メールが来たら」といったイベントをきっかけに、同じ依頼を自動で繰り返させる仕組み

旧称の「**ChatGPT Agent**」「エージェントモード」(2025年7月〜)は、2026年7月9日に「ChatGPT Work」へ改名・拡張された。社内の古いマニュアルでこの表記を見かけた場合は、現行のChatGPT Workのことだと読み替えてよい。

## 仕組み・背景

### 成り立ち: Operator → ChatGPT Agent → ChatGPT Work → dots

- **Operator(2025年1月)**: 仮想ブラウザでWebサイト上の操作(予約・フォーム入力など)を代行する専用ツール。2025年8月31日に単体提供を終了
- **ChatGPT agent(2025年7月17日)**: OperatorとDeep Research(出典付きレポートを作る調査モード)と通常の対話を統合した機能([Introducing ChatGPT agent | OpenAI](https://openai.com/index/introducing-chatgpt-agent/))
- **ChatGPT Work(2026年7月9日)**: ChatGPTが**Chat(通常の対話)・Work(複数ステップの作業と成果物作成)・Codex(ソフトウェア開発)**の3モード構成に再編され、旧エージェントモードは「Work」に一本化された([ChatGPT is now a partner for your most ambitious work | OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/))
- **dots(2026年9月29日)**: Workが「頼まれた仕事を仕上げる」のに対し、dotsは「会話の外でも動き続け、自分から仕事を見つけて進める」常時稼働型として追加された([Introducing dots | OpenAI](https://openai.com/index/introducing-dots/))

独自ブラウザ「ChatGPT Atlas」(2025年10月提供開始)は2026年8月9日に終了し、ブラウザ型エージェントの機能はChatGPT本体(クラウドブラウザ・デスクトップアプリ)などに統合されている。

### ChatGPT Workの動き方

- **クラウドブラウザ**: OpenAIのサーバー上で動くブラウザを使うため、デスクトップ・Web・モバイルのどこから依頼しても、PCを閉じても作業が続く。AIが操作する様子は画面で確認でき、途中で止めたり指示を足したりできる。クラウドブラウザは手元の端末のログイン状態を使わず、独自のセッションを持つ([ChatGPTでのクラウドブラウザーの使用 | OpenAI Help Center](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt))
- **ローカルファイル**: デスクトップアプリのWorkは、許可したフォルダ・ファイルを扱える。Web・モバイルからは手元PCのファイルにはアクセスできない([ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275))
- **Plugins(プラグイン)とアプリ連携**: Gmail・Slack・GitHubなどの外部サービスとの連携(「アプリ」)を、Pluginsというカタログから有効化して使う。2026年11月発表のGPT-6.2系モデルは、タスクに応じてプラグイン経由の連携とcomputer use(画面を直接操作する機能)を使い分けるとされる([Introducing GPT-6.2 Astra and Sol | OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol))
- **音声**: Workでは音声での対話(Voice)も使える(Web・iOS・Android、およびデスクトップアプリ)
- **モデル(2026年11月時点)**: Workのモデル選択(model picker)では、2026年11月17日に追加された**GPT-6.2 Astra**(難しい専門業務・コーディング向けの上位モデル)と**GPT-6.2 Sol**(日常業務向けの効率型モデル)が中心で、プランやワークスペース設定によってGPT-6.1 Sol・GPT-6.1 Terra・GPT-6 Sol・GPT-6 Lunaなども表示される([ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275)、[ChatGPT release notes | OpenAI Help Center](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))

#### 安全のための仕組み(クラウドブラウザ)

- **セキュアなサインインフォーム**: ログインが必要なサイトでは作業が一時停止し、専用フォームにID・パスワード(必要なら2要素認証コード)を入力する。入力内容はリモートのブラウザに直接渡り、AIモデルからは見えず、ChatGPTにも保存されない。フォームを出す前に、フィッシングや欺瞞がないかを別の審査モデルがチェックする。サインイン済みのセッションは有効期限まで次回以降の作業で再利用される
- **Webサイトへのアクセス許可**: 「設定→クラウドブラウザ」で、既定の動作を「**Always ask**(毎回確認)」「**Auto approve**(URLを審査し、危険そうなときだけ停止)」「**Always allow**(すべて許可。非推奨)」から選べ、サイトごとの許可・ブロックも設定できる
- **確認プロンプト**: 予約の確定や支払いなど、取り消しにくい操作の前にはチャット上で確認を求める。サイトを「許可」していてもこの確認は省略されない
- **テイクオーバー(Take over)**: AIが行き詰まったときや自分で入力したいときは、スマホやPCからクラウドブラウザの操作を引き取り、終わったら「Return control」で返す
- **セッションの削除**: 「設定→クラウドブラウザ→Browser data→Cookies」から、全サイトまたはサイト単位で保存データを消せる(消すとそのサイトからはサインアウトされる)

### dotsの動き方(2026年11月時点)

- **専用のクラウドコンピュータ**: 各dotは自分専用のクラウドコンピュータとブラウザを持ち、利用者のPCとは切り離されている(手元PCへのアクセスは初期状態でオフ。デスクトップアプリから「Allow access」で許可し、「Revoke access」で取り消せる)
- **常時稼働・自発的な下調べ**: 指示がなくても、接続したアプリの情報を確認し、バックグラウンドで「proactive research(先回りの調査)」を行って提案する。この**バックグラウンドの調査は接続アプリへの読み取り専用のツールに制限**されている
- **好みを学習**: ChatGPTのメモリーを引き継ぎつつ、フィードバックや接続アプリから独自のメモリーも作る
- **4,000以上のアプリと連携**: Pluginsを通じて4,000を超えるアプリに接続できる。必要に応じてCodexやChatGPT Workに作業を振ることもできる
- **話しかける場所**: ChatGPTのデスクトップ・Web・モバイル(メッセージまたは通話)、SlackとMicrosoft Teams。2026年11月19日にはモバイルアプリの新デザインでdot専用のタブが追加された(Pro先行)。米国などの一部Pro向けにはテキストメッセージ(iMessage/RCS)でのやり取りがベータ提供されている
- **搭載モデル**: GPT-6 Astraを基盤とし、作業の部分ごとに別のモデルを使い分ける(2026年11月3日の更新でGPT-6.1 Terraも追加)
- **安全策**: 監視システムが安全上の懸念を検知すると作業を一時停止・中止する。後述の「カスタムルール」で操作ごとの扱いを決められ、アカウントに影響する操作や情報共有につながる操作は自動レビュー(Auto-review)でチェックされる。パスワード変更のような機微な操作は常に利用者本人に残る。対応サイトでは保存済みパスワードを、モデルに見せずにサインインに使える。進捗はActivity View(アクティビティ表示)で追える([Introducing dots | OpenAI](https://openai.com/index/introducing-dots/))
- **購入(米国のみ)**: 2026年11月13日から、米国の18歳以上のPro利用者向けに「ChatGPT Wallet」がdotsで段階展開され、利用者が生体認証で注文を承認したうえでdotが買い物を行える

### スケジュールタスクの仕組み

ChatGPTに「指定した日時・周期で同じ依頼を自動実行させる」軽量な仕組み。2026年11月時点のヘルプでは「**Scheduled**」という画面で管理する。

- **時刻ベース**: 1回だけ・毎日・毎週などの周期で実行。有料プランは最短1時間に1回まで、正確な時刻を指定できる。Freeは1日1回までで、「朝・午後・夜」のような幅のある時間帯での実行になる
- **イベントトリガー(Plus以上)**: Gmailの新着メール、Slackチャンネルの新着メッセージ、GitHubのプルリクエストの動きなど、接続アプリの変化をきっかけにWorkのタスクを起動できる(全イベントトリガー合計で1時間30回・1日720回まで)
- **共有**: 対象のクラウド上のスケジュールタスクは他の人に共有でき、受け取った側には別のコピーが作られる(チャット履歴やファイルは引き継がれない)

([Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt)、[ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275))

### 関連する製品

- **ChatGPT workspace agents(Business・Enterprise向け)**: 管理者・業務担当者がテンプレートやビルダーで反復業務用のエージェントを作り、チームに共有・スケジュール実行・Slackで利用できる機能。個人のWork/dotsとは別のヘルプページ・管理画面で案内されている(Enterpriseでは初期状態でオフ)([ChatGPT Workspace Agents for Enterprise and Business | OpenAI Help Center](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business))
- **Codexモード**: ソフトウェア開発向けのモード。WorkとCodexは料金体系・クレジット・利用上限を共有する
- **deep research**: 「調べるだけ」の調査モード。操作は行わない。詳しくは[Deep Research機能](../part12-business-practice/ai-research-and-information-gathering.md)

## 使いどころ・使い分け

### 機能の一覧

| 機能 | 何をしてくれるか | 動くタイミング | 向いている場面 |
|---|---|---|---|
| 通常のチャット(Chat) | その場で1回答える | 依頼したとき | 相談、下書き、アイデア出し |
| [Web検索](./chatgpt-web-search-feature.md) | 数回検索して要約する | 依頼したとき | 鮮度が必要な単発の事実確認 |
| deep research | 多数のサイトを読み回り出典付きレポートを作る(**読み取りのみ**) | 依頼したとき | 市場調査・競合比較 |
| **ChatGPT Work** | クラウドブラウザ・アプリ連携・ローカルファイルで**操作を実行**し、資料・表・ドキュメントなどの成果物を返す | 依頼したとき(数分〜数時間) | 成果物づくり、複数サイト横断作業、ログインが必要なSaaSでの作業 |
| **dots** | 専用クラウドコンピュータで**常に待機・稼働**し、下調べ・定期チェック・提案・Work/Codexへの作業の振り分けを行う | 常時(利用者が見ていない間も) | 継続的に追う仕事(案件・顧客・プロジェクトの見張り役)、Slack/Teamsからの気軽な依頼 |
| **スケジュールタスク** | 決まった時刻・周期・イベントで依頼を自動再実行 | 指定した時刻・イベント | 定期レポート、新着メールへの一次対応の下書き |
| Codex | コードの生成・修正・実行 | 依頼したとき | ソフトウェア開発(本ページの対象外) |

### ChatGPT Work と dots の使い分け

| 観点 | ChatGPT Work(依頼型) | dots(常時稼働型) |
|---|---|---|
| 起点 | 利用者が依頼したとき | 依頼に加え、dot自身が気づいて動く |
| 仕事の単位 | 1件のタスク・成果物(資料1本、表1つ) | 継続する目標・担当領域(「この案件を見張って」) |
| 実行環境 | クラウドブラウザ(デスクトップ版はローカルファイルも可) | dot専用のクラウドコンピュータ(手元PCへのアクセスは任意でオン) |
| 話しかける場所 | ChatGPT(デスクトップ・Web・モバイル) | ChatGPTに加え、Slack・Teams、一部Pro向けにテキストメッセージ(ベータ) |
| 利用上限(2026年11月時点) | Codexと共通の利用枠を消費 | dotとの会話は利用上限に数えない。dotが始めたWork/Codexのタスクは通常どおり消費 |
| 対象プラン(2026年11月時点) | Free〜Enterpriseの各プランに含まれる(クラウドブラウザは有料プランのみ) | Pro・Business Premiumが中心(Plus・Business Standardは一部で段階展開、Enterpriseは管理者経由) |
| 向く人 | 「この作業を片付けて」と単発で頼みたい人 | 同じ領域を毎日追っていて、先回りしてほしい人 |

判断の目安は次の3つ。

1. **「調べるだけ」か「操作・成果物まで」か**: 読むだけならdeep research、成果物や操作が必要ならWork
2. **「今回1回」か「繰り返し・継続」か**: 1回ならWork、決まった時刻やイベントで同じ依頼を回すならスケジュールタスク、何を見張るべきかの判断ごと任せたいならdots
3. **「自分が指示する」か「AIに気づいてほしい」か**: 指示が明確に書けるならWork+スケジュールタスクで足りる。何が起きるか事前に決めきれない継続業務(顧客対応の進捗、プロジェクトの変更追従など)はdotsが向く

なお「ChatGPT Work」「dots」はOpenAIの製品名であり、Google・Anthropic・Microsoftにも依頼型・常時稼働型のエージェントがある。ベンダー横断の分類と導入判断は[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)で扱っている。本ページはChatGPTの「画面のどこで・どう使うか」の実務ガイドに徹する。

## 実務での使い方

### ChatGPT Workの使い方(2026年11月時点)

1. **Web・モバイル**: ChatGPTを開き「**Work**」を選ぶ(モバイルはドロップダウンでChat/Workを切り替え)。**デスクトップアプリ**: メニューから「ChatGPT」を選び、トグルで「Work」を選ぶ
2. 必要ならWorkのモデル選択でモデルを選ぶ(目的のモデルが表示されない場合、デスクトップアプリは「メニュー→Check for Updates」で更新)
3. 依頼内容を入力する。クラウドブラウザでの操作の様子が表示され、PCを閉じても作業は続く
4. ログインが必要な場面ではセキュアなサインインフォームに自分で入力する。行き詰まったら「Take over」で操作を引き取り、終わったら「Return control」で返す
5. 予約確定・支払いなど取り消しにくい操作の前に確認が出るので、内容を読んでから許可する
6. 結果(成果物・実行した操作の記録)がチャットに返る。クラウド上のWorkのチャットはWeb・モバイル・デスクトップで同期される
7. 不要になったログイン状態は「設定→クラウドブラウザ→Browser data→Cookies」から削除する

**対応プラン・利用量(2026年11月時点)**:

- **プランへの含まれ方**: ChatGPT WorkとCodexはFree・Go・Plus・Pro・Business・Edu・Enterpriseの各プランに含まれ、料金体系・クレジット・利用上限を共有する。ただしWeb・モバイルでのWorkは対象の有料プラン向けで、**クラウドブラウザはFree・Goでは使えない**。Enterprise・EduではWorkの利用にEKM(Enterprise Key Management)が必要で、管理者がオフにしない限り既定ロールで有効になっている
- **料金の目安**: Plus月額20ドル、Proは月額100ドル・200ドル・500ドルの3段階(いずれも2026年11月時点)。Business・Enterpriseの詳細は[ChatGPTのプラン比較](./chatgpt-plan-comparison.md)を参照
- **上限の構造**: PlusとBusiness Standardは「5時間ごと」の上限(モデルによって目安が大きく異なる)があり、加えて週単位の上限がかかることもある。**Proは2026年11月時点で5時間ごとの上限なし**。上限に達したPlus・Proはクレジットを追加購入して続行できる。2026年10月29日にはPro 100とPro 500のWork/Codex利用枠が従来の2倍になった([Pricing | ChatGPT Learn](https://learn.chatgpt.com/docs/pricing)、[ChatGPT release notes | OpenAI Help Center](https://help.openai.com/en/articles/6825453-chatgpt-release-notes))
- **モデルの使える範囲**: GPT-6.2 Astra・Solは、Plus・Pro・Enterprise・EduのWorkとCodexで利用可能(Enterprise・Eduは管理者の有効化が必要)。GPT-6 Astraについては、Pro(100ドル・200ドル)とBusiness Premiumは含まれる利用枠をすべて使える一方、PlusとBusiness Standardは限定的な利用で、その後はクレジットで追加する形になっている

### dotsの始め方(2026年11月時点)

**対象プラン**:

- **Pro**: 18歳以上で、EEA(欧州経済領域)・スイス・英国以外の利用者が対象
- **Business Premium**: 対応地域で、ワークスペースの条件を満たす場合
- **Plus**: EEA・英国・スイス以外の一部の利用者に段階展開中(サポートに頼んでも有効化できない)
- **Business Standard**: 米国で展開中(利用上限あり)
- **Enterprise・Edu・Healthcare**: 2026年11月18日までは管理者が有効化した場合のプレビュー。その後は管理者がオプトアウトしない限り既定で利用可能になる。1メンバーにつき個人用のdotは1つ。2027年1月13日までは無料で、2027年1月14日から作業の種類ごとの定額で課金が始まる(dotから起動したWork/Codexのスレッドは別課金)
- **料金**: Pro・Business Premiumでは**最初の1つのdotはプランに含まれ追加料金なし**。追加のdotや処理量の拡張は今後提供予定とされ、価格は未公表

([Getting started with your dot | OpenAI Help Center](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)、[Introducing dots | OpenAI](https://openai.com/index/introducing-dots/))

**手順**:

1. ChatGPTのデスクトップアプリ(Windows版含む)、デスクトップのWebブラウザ版、またはiOS/Androidアプリ(最新版)でdotを作成し、オンボーディングの案内に従う(モバイルのWebブラウザ版は非対応)
2. セットアップ中にdotの名前を付ける。名前やアバターを変えるときは、dotの名前かアバターを選んでプロフィールを開き、鉛筆アイコンを選ぶ
3. アプリをつなぐ: モバイルではプロフィールの「**Customize→Plugins**」から、権限を確認して接続する。Slackとの接続はデスクトップのChatGPTから行う
4. ルールを決める: モバイルの「**Customize→Custom rules**」で既定のルールを確認し、ルールを追加する(下記のコピペ例)
5. 仕事を頼む: 会話で内容と詳細を伝える。「+」からファイルや写真を添付できる。リマインダーや定期チェックも会話で頼める
6. 進捗を見る: デスクトップでプロフィールを開くと、活動が「In progress(進行中)」「Scheduled(予定)」「Completed(完了)」に分けて表示される。プロフィールからdotのクラウドコンピュータを開いて操作を見たり、自分で操作したりもできる
7. 止める・消す: プロフィールの「•••(その他のオプション)」→「Pause」で一時停止、「Delete」で削除(取り消し不可。dot自身のメモリーは削除され、メインの会話はアーカイブされる)

### コピペで使える実例

#### dotsのカスタムルール

カスタムルールは「対象の操作」を文章で書き、動作を次の4つから選ぶ: 「**Take action without asking**(確認なしで実行)」「**Take action if pre-approved**(依頼文で明示した場合のみ実行)」「**Ask before taking action**(実行前に確認)」「**Hand off to you**(利用者に引き渡す)」。最初は次のような保守的な設定から始めるとよい。

```
ルール1
対象の操作: 社外の相手へのメール・Slack・Teamsメッセージの送信
動作: Ask before taking action(実行前に確認)

ルール2
対象の操作: 共有ドライブ・CRM・タスク管理ツール上のデータの削除、または上書き保存
動作: Ask before taking action(実行前に確認)

ルール3
対象の操作: 支払い・購入・契約・申込みの確定
動作: Hand off to you(利用者に引き渡す)

ルール4
対象の操作: 自分宛ての下書き作成、自分だけが見るメモやドキュメントへの追記
動作: Take action without asking(確認なしで実行)
```

ヘルプには「下書きを頼んでも、送信を許可したことにはならない」「ルールはアプリやコンピュータへのアクセス権を与えるものではなく、組み込みの安全策も上書きしない」と明記されている。

#### dotsへの最初の依頼(継続業務の見張り役)

```
あなたには「〇〇社案件」の見張り役をお願いします。
- 毎朝9時に、接続しているGmail・Slack・カレンダーから、この案件に関する
  前日以降の新しい動きを確認し、3行で要約して知らせてください
- 先方からの質問や依頼で、48時間以上返信していないものがあれば、
  返信の下書きを作って私に確認を求めてください(送信はしないでください)
- 打合せが入ったら、前日までに過去のやり取りをもとに論点メモを作ってください
- 判断に迷うこと、社外に何かを送ること、データを消すことは必ず先に聞いてください
```

#### ChatGPT Work: 読み取り中心の依頼(初めて試すのに向く)

```
来週の月曜〜水曜に東京→大阪を新幹線で移動する場合の
時間帯別の空席状況と料金を調べて、比較しやすい表にまとめてください。
チケットの購入や予約は行わず、調査結果の報告だけをお願いします。
```

#### ChatGPT Work: 操作を含む依頼(確定の手前で止める)

```
〇〇(通販サイト名)で△△(商品名)を検索し、条件に近い上位3件を比較したうえで、
最も条件に合う商品をカートに入れてください。
購入の確定は行わず、確認画面の手前で止めて私に知らせてください。
```

#### ChatGPT Work: ログインが必要な社内SaaS(読み取りのみ)

```
経費精算システム(社内SaaS)にログインし、今月分の交通費の入力状況を確認してください。
未入力の項目があれば一覧にして教えてください。新規の申請や承認操作は行わないでください。
```

### スケジュールタスクの設定・管理方法(2026年11月時点)

1. **作成**: 「Scheduled」を開いてスケジュールを設定する。会話の中で「毎週月曜の朝9時に〜して」と頼んでもよい
2. **一覧の確認**: 「Scheduled」を開く、または「設定→通知→Manage tasks」。会話からは「•••」メニュー→「See scheduled tasks」
3. **編集・一時停止・削除**: 会話内のタスク名を選んでタスクパネルを開く
4. **通知**: 「設定→通知」で管理する
5. **イベントトリガー**: 「設定→アプリ」で対象アプリ(Gmail・Slack・GitHubなど)を接続してから、Workでタスクを作成する

**同時に有効にできるタスク数(2026年11月時点)**: Free・Goが3件、Plusが5件、Business・Eduが10件、Pro・Enterpriseが15件。イベントトリガー型はPlus以上(Free・Go、FedRAMPワークスペースは対象外)([Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt))。

コピペで使える例(時刻ベース):

```
毎週月曜日の朝9時に、直近1週間の生成AI関連の主要ニュースをWeb検索で調べて、
3行以内の日本語サマリーで送ってください。個別の製品リリースよりも、
業務での使い方に影響しそうな話題を優先してください。
```

コピペで使える例(イベントトリガー。Workで作成):

```
Gmailに「見積」または「請求」を件名に含むメールが届いたら、
送信者・金額・期限を抜き出して一覧に追記し、
返信が必要なものは返信の下書きだけ作ってください。送信はしないでください。
```

### 主要ツールでの対応付け(2026年11月時点)

| 概念 | ChatGPT(OpenAI) | Google | Anthropic | Microsoft |
|---|---|---|---|---|
| 依頼型(作業・成果物の代行) | ChatGPT Work | Gemini Spark(Workspaceアプリと深く統合されたエージェント型アシスタント) | Claude(2026年9月16日にCoworkを通常のチャットへ統合し、1つの会話から作業を任せられる) | Copilot |
| 常時稼働型 | dots | — | — | Microsoft Scout(常時稼働型の「Autopilot」。限定プレビュー) |
| 定期・自動実行 | Scheduled(時刻ベース・イベントトリガー) | Spark(毎朝のメール・カレンダー確認などのタスク) | 会話の中で定期実行を依頼 | 比較ページ参照 |

各社の分類・導入判断は[AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)、機能名・対応プランの横並び比較は[主要AIチャットツールのエージェント機能・スケジュールタスク比較](./ai-chat-tools-agent-tasks-comparison.md)を参照。

## 注意点・よくある誤解

- **「エージェントモード」「ChatGPT Atlas」は現行UIに存在しない**: 2026年7月9日以降は「Work」に統一され、Atlasは2026年8月9日に終了した。古い手順書は「Workを選ぶ」に読み替える
- **dotsは「見ていない時間」に動く前提で権限を絞る**: バックグラウンドの下調べは読み取り専用に制限されているが、会話で頼んだ作業では送信・更新も行える。OpenAI自身が「dotは間違えることがある(ルールに従う場面でも)」として重要な成果物の確認を求めている。最初はカスタムルールで送信・削除・購入を「確認」または「引き渡し」にしておき、慣れてから緩める
- **dotを一時停止しても、別に動いているタスクは止まらない**: Pauseはdot本体の停止で、dotから起動したWork/Codexのタスクや個別に設定したスケジュールタスクは動き続けることがある。止めたいときはそれぞれ止める
- **アプリの切断で、取得済みの情報は消えない**: dotからアプリを切断しても、それまでに得た情報は削除されない。機密性の高いアカウントは最初からつながない
- **dotsのテキストメッセージはエンドツーエンド暗号化されていない**: 配信は第三者事業者(Linq)経由で、OpenAIはやり取りをdotの会話として保存する。機密情報はアプリ内で扱う
- **「dotとの会話は無料」でも、その先は利用枠を消費する**: dotとの会話自体はChatGPTの利用上限に数えないが、dotがWork/Codexに作業を振ると通常どおり消費する。Plusは5時間ごとの上限もあるため、検証で使いすぎるとコーディング用途の枠まで減る
- **クラウドブラウザのログイン状態はサーバー側に残る**: 経理・人事など機微なシステムを扱った後や異動・退職時は、「設定→クラウドブラウザ→Browser data→Cookies」から削除する運用を決めておく。「Always allow」は非推奨とされている
- **プロンプトインジェクションは解消されていない**: 閲覧先ページに埋め込まれた悪意ある指示にAIが誘導される攻撃は、業界全体で完全な対策が確立されておらず、OpenAIも「完全には解決できない可能性がある」との立場である([OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/))。常時稼働のdotsは見知らぬメールやページに触れる機会が多いため、送信・購入などの最終判断は人間が行う
- **サイト側がエージェントを拒否することがある**: 自動化されたブラウザからのアクセスを制限するサイトがあり、最後の手続きは自分で行う必要がある場合もある
- **呼び方・対象プランは数か月単位で変わる**: dotsは9月の発表時点からPlus・Business Standard・Enterpriseへと対象が広がり続けている。業務フローに組み込む前に、自分の契約で実際に表示されるかを確認する

## 最初の一歩

まずWorkで、購入や送信を含まない読み取り中心の依頼(上記の新幹線の比較調査など)を1回試し、AIの操作を眺めてみる。dotsが使えるプランなら、作成直後に「Customize→Custom rules」で「社外への送信は実行前に確認」のルールを1つ追加してから、見張ってほしい案件を1つだけ任せてみるとよい。

## 関連トピック

- [ChatGPTのWeb検索機能](./chatgpt-web-search-feature.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [生成AIによる情報収集・リサーチの実務活用(Deep Research機能)](../part12-business-practice/ai-research-and-information-gathering.md)
- [ChatGPTのプラン比較](./chatgpt-plan-comparison.md)
- [主要AIチャットツールのエージェント機能・スケジュールタスク比較](./ai-chat-tools-agent-tasks-comparison.md)

## 更新履歴

### 2026-11-21: 常時稼働型エージェント「dots」を追加し、Work・スケジュールタスクの仕様を2026年11月時点に最新化
- **内容**: DevDay 2026(2026年9月29日)発表のdots(専用クラウドコンピュータ、読み取り専用のバックグラウンド調査、4,000以上のアプリ連携、Slack・Teams・テキスト、カスタムルールの4つの動作、プラン別の提供状況とEnterpriseの課金開始日、作成・Pause・Deleteの画面手順)を新設し、Work/dotsの使い分け表とカスタムルール・依頼文のコピペ例を追加。Workのアクセス手順・モデル(GPT-6.2 Astra/Sol、2026年11月17日)・プラン別の利用上限(Pro 3段階、Proは5時間上限なし、Pro 100/500の利用枠2倍)・クラウドブラウザのアクセス許可設定(Always ask/Auto approve/Always allow)とCookie削除の場所を現行に更新。スケジュールタスクの画面名(Scheduled)・Free対応・頻度上限・イベントトリガーを反映。終了済みのウォッチモードや展開初期のGPT-6 Astra・Atlas関連の古い記述を削除・整理
- **出典**: [Introducing dots | OpenAI](https://openai.com/index/introducing-dots/)、[Getting started with your dot | OpenAI Help Center](https://help.openai.com/en/articles/20001530-getting-started-with-your-dot)、[OpenAI launches dots, always-on AI agents with their own cloud computers | The Next Web](https://thenextweb.com/news/openai-dots-always-on-ai-agents-cloud-computers-devday)、[ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275)、[ChatGPTでのクラウドブラウザーの使用 | OpenAI Help Center](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)、[Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt)、[ChatGPT release notes | OpenAI Help Center](https://help.openai.com/en/articles/6825453-chatgpt-release-notes)、[Introducing GPT-6.2 Astra and Sol | OpenAI](https://openai.com/index/introducing-gpt-6-2-astra-sol)、[Pricing | ChatGPT Learn](https://learn.chatgpt.com/docs/pricing)、[ChatGPT Workspace Agents for Enterprise and Business | OpenAI Help Center](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business)、[Claude Cowork and chat are now one Claude | Claude by Anthropic](https://claude.com/blog/cowork-is-now-claude)、[Google is expanding access to its Gemini Spark agentic AI assistant | Engadget](https://engadget.com/2222303/google-expanding-access-gemini-spark)、[Introducing Microsoft Scout | Microsoft 365 Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2026/06/02/introducing-microsoft-scout/)

### 2026-09-05: クラウドブラウザ化・ログイン機能・Atlas終了・GPT-6 Astraを反映し全面更新
- **内容**: 2026年8月9日にブラウザ単体アプリ「ChatGPT Atlas」が終了し機能がChatGPT本体・Chrome拡張・Codexへ統合された点、同8月にWorkの実行環境が「クラウドブラウザ」(サーバー上で常時動作、Web/モバイルからもアクセス可)へ切り替わった点、8月25日にログインが必要なサイトを安全に操作できる新機能(セキュアなサインインフォーム、セッション保持、設定→クラウドブラウザでの管理)が追加された点、同日Plusプランに5時間ごとのローリング制限が復活しBusinessにPremiumシートが新設された点、Free・Goでのデスクトップ限定・Terra固定という対応プランの実態、9月3日発表の新モデル「GPT-6 Astra」の位置づけと展開状況(先行提供段階)、「Plugins」と「アプリ」の呼び分けを反映し、対応プラン・注意点・コピペ例を現行の挙動に合わせて全面的に書き換えた
- **出典**: [ChatGPT Work、ログイン必要なサイトも操作可能に「パスワードは一切見ない」| ITmedia NEWS](https://www.itmedia.co.jp/aiplus/article/2608/26/2000000788/)、[ChatGPT Workが要ログインサイトの作業も代行。Plusは5時間制限復活 | PC Watch](https://pc.watch.impress.co.jp/docs/news/2135792.html)、[OpenAIのブラウザ「ChatGPT Atlas」終了へ 公開から1年足らずで | ITmedia NEWS](https://www.itmedia.co.jp/news/articles/2607/13/news090.html)、[ChatGPTでのクラウドブラウザーの使用 | OpenAI Help Center](https://help.openai.com/en/articles/20001280-using-cloud-browser-in-chatgpt)、[OpenAI announces rollout of GPT-6 Astra model | CNBC](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)、[Apps in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)、[ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275)、[Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt)

### 2026-07-27: ChatGPT Agentが「ChatGPT Work」へ改名・再編されたことを反映し全面更新
- **内容**: 2026年7月9日にOpenAIがChatGPTをChat/Work/Codexの3モード構成に再編し、旧「ChatGPT Agent(エージェントモード)」が「ChatGPT Work」に改名・拡張されたことを反映。ヘルプセンターの旧「ChatGPT agent」ページが提供終了案内に切り替わっている点、外部連携が「アプリ(apps)」から「Plugins」へ再度改称された点、対応プランの展開状況(Web/モバイルはPro/Enterprise/Edu先行→Plus/Businessへ拡大、デスクトップはFree含む全プラン)、Tasksのヘルプページ名称変更(「Tasks in ChatGPT」)、deep researchが引き続き独立モードとして残っている点、プロンプトインジェクション対策の継続的強化を追記し、コピペ例・手順・対応表・注意点を現行の名称・挙動に合わせて書き換えた
- **出典**: [ChatGPT is now a partner for your most ambitious work | OpenAI](https://openai.com/index/chatgpt-for-your-most-ambitious-work/)、[ChatGPT Work and Codex | OpenAI Help Center](https://help.openai.com/en/articles/20001275)、[ChatGPT Workspace Agents for Enterprise and Business | OpenAI Help Center](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business)、[Tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-tasks-in-chatgpt)、[Connectors in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)、[Continuously hardening ChatGPT Atlas against prompt injection attacks | OpenAI](https://openai.com/index/hardening-atlas-against-prompt-injection/)、[OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/)

### 2026-07-06: 初版執筆
- **内容**: ChatGPT Agentの成り立ち(Operator+Deep Researchの統合、2025年7月)、仮想ブラウザ・コンピュータの仕組み、テイクオーバーモード・確認プロンプト・ウォッチモードといった安全設計、Workspace agents・ChatGPT Atlasとの関係、対応プラン(Plus/Pro/Business/Enterprise/Edu、クレジット制)、Tasks(スケジュールタスク)の仕組み・設定手順・プラン別の上限、deep research/Web検索/AIエージェント全般との使い分け、プロンプトインジェクション等の注意点を整理
- **出典**: [Introducing ChatGPT agent | OpenAI](https://openai.com/index/introducing-chatgpt-agent/)、[ChatGPT agent | OpenAI Help Center](https://help.openai.com/en/articles/11752874-chatgpt-agent)、[ChatGPT agent release notes | OpenAI Help Center](https://help.openai.com/en/articles/11794368-chatgpt-agent-release-notes)、[Connectors in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/11487775-connectors-in-chatgpt)、[Scheduled tasks in ChatGPT | OpenAI Help Center](https://help.openai.com/en/articles/10291617-scheduled-tasks-in-chatgpt)、[Introducing workspace agents in ChatGPT | OpenAI](https://openai.com/index/introducing-workspace-agents-in-chatgpt/)、[OpenAI launches a general purpose agent in ChatGPT | TechCrunch](https://techcrunch.com/2025/07/17/openai-launches-a-general-purpose-agent-in-chatgpt/)、[The glaring security risks with AI browser agents | TechCrunch](https://techcrunch.com/2025/10/25/the-glaring-security-risks-with-ai-browser-agents/)、[OpenAI says prompt injection is a problem it may never fully solve | CyberScoop](https://cyberscoop.com/openai-chatgpt-atlas-prompt-injection-browser-agent-security-update-head-of-preparedness/)、[OpenAIが「ChatGPT agent」を発表 | Impress Watch](https://forest.watch.impress.co.jp/docs/news/2032283.html)、[「ChatGPT」に自律型AIエージェント機能 | ITmedia](https://www.itmedia.co.jp/aiplus/articles/2507/18/news053.html)
