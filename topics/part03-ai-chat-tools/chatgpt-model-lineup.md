---
title: ChatGPTのモデル一覧と使い分け
part: 3
chapter: 第1章 プラン・モデルの選び方
tags: [ChatGPT, モデル選択, GPT, 推論モデル, GPT-5.6, GPT-5.6 Luna]
created: 2026-07-05
updated: 2026-09-04
---

# ChatGPTのモデル一覧と使い分け

## これは何か

ChatGPTの画面には、速度・精度・コストのバランスが異なる複数のモデル(またはモデルの「考える深さ」を調整するスライダー)が用意されている。デフォルトのまま使い続けても多くの場面で困らないが、複雑な分析やコーディングでは推論(reasoning、回答前にモデル内部で段階的に考えること)に力を入れたレベルに切り替えるだけで回答の質が大きく変わる。逆に単純な作業に重い設定を使うと、応答が遅くなるうえ利用回数の上限(レートリミット)を早く消費してしまう。自分のタスクに合ったレベルを選べるようになっておくと、同じ契約プランでもアウトプットの質と使える回数の両方が変わってくる。

## 仕組み・背景

2026年9月4日時点のChatGPTは、大きな地殻変動の直後にある。9月3日、OpenAIは次世代フラッグシップ「**GPT-6 Astra**」を発表し、まずエンタープライズ向け審査制プログラム「Daybreak」経由の一部組織から提供を開始、Plus・Pro・Business・Enterpriseの各プランには「数日かけて」順次展開すると告知した(Free/Goは対象外)。本ページ執筆時点はロールアウトの初日〜数日目にあたり、モデルピッカーへの反映状況はアカウントによってばらつきがある。Astraへの移行が完了するまでの過渡期として、直前まで主力だった「GPT-5.6」世代(Sol・Terra・Luna、7月9日一般提供開始)を土台にした仕組みも大部分がそのまま生きている。

- **Plus/Pro以上(個人プラン)**: モデルピッカー内の**推論エフォート・スライダー**で、「Instant/Medium/High/Extra High/Pro」の5段階を1本のバーとして直接指定する構造は変わらない。Instant〜Extra Highはこれまで**GPT-5.6 Sol**が担当してきたが、これを置き換える新フラッグシップとして**GPT-6 Astra**が、最上位の「Pro」枠を置き換える存在として**GPT-6 Pro**(Astraの高性能版)がPro・Business・Enterpriseから順次利用可能になっている。スライダーを右に寄せる(エフォートを上げる)ほど内部で考える時間が増えて精度が上がる代わりに応答が遅くなるという基本構造は従来通り。ロールアウトが完了するまでは、アカウントによってSol/Sol Proのまま、またはAstra/Astra Proに切り替わった状態が混在しうる
- **Free/Go(無料・低価格プラン)**: 引き続き既定モデルは**GPT-5.6 Luna**(GPT-6版のLuna相当モデルは本ページ執筆時点で未発表)で、テキストチャットの回数制限は事実上撤廃されたまま。ワンタップで深く考えさせられる「**Think**」ボタンも従来通り使え、普段はLunaのまま、重要な質問のときだけそのメッセージに限って深く考えさせる、という使い方ができる
- **Business/Enterprise(組織向けプラン)**: 個人プランのような単一スライダーではなく、管理者の設定次第でモデルごとに効果レベルを個別設定できる、より柔軟な構成である点は変わらない。Business Standardは月15件、Business PremiumはPro相当のメッセージが週50件の目安で、いずれもGPT-6 ProとGPT-5.6 Sol Proの合算枠として消費される

GPT-6 Astraは、コンピュータ操作(ブラウザ操作やフォーム入力・CRM更新などを人間のように代行する「computer use」)・コーディング・サイバーセキュリティ・科学分野で軒並みGPT-5.6 Solを上回るとOpenAIは説明しており、OSWorld 2.0(コンピュータ操作ベンチマーク)ではSol比で作業時間を約47%短縮しつつ高スコアを達成したという。一方でサイバーセキュリティ能力がOpenAI自身の安全基準で「Critical」域に達したとされ、エクスプロイト構築のような高リスク機能は引き続き審査制のDaybreakプログラムの管理下に置かれている。API価格は入力100万トークンあたり10ドル・出力100万トークンあたり50ドル、コンテキストウィンドウは約1.05Mトークンで、ChatGPT契約の利用上限とは別枠の目安として押さえておくとよい。

なお、Astraのロールアウトはまだ進行中で、「Instant/Medium/High/Extra High」の各段階がAstraに完全に置き換わるのか、Sol系と並走する期間が続くのかなど細部は流動的である。契約プランでの表示・挙動は都度、実際の画面とOpenAIのヘルプページで確認するのが安全。

このほか、直前まで主力だったGPT-5.6にも、Sol・Terra・Lunaを土台にした特殊な派生版がある。

- **Ultrafast(プレビュー、2026年8月13日発表)**: 半導体企業Cerebrasとの提携により、GPT-5.6 Sol Standardと同じ知性を保ったまま最大14倍の速度・毎秒最大750トークンで応答する新しい提供形態。現時点ではAPIの一部顧客向けプレビューで、通常のChatGPT画面では選べない
- **GPT-5.6-Cyber(2026年8月10日発表)**: サイバーセキュリティの専門家向けにゼロデイ脆弱性の発見・エクスプロイト構築などに特化した派生モデル。OpenAIの審査制プログラム「Daybreak」(Blue/Redの2階層)を通じて本人確認と用途審査を通った組織のみが利用でき、通常のChatGPTユーザーが日常業務で触れる対象ではない

このほかに、次の2種類も押さえておく必要がある。

- **下位モデル(Terra)**: GPT-5.6 Lunaは前述の通りFree/Goの既定モデルとして表舞台に出てきた一方、Terra(5.5相当の性能をより低コストで出すモデル)はBusiness/Enterpriseの管理者設定やCodex(コーディング専用エージェント)・開発者向けAPIからの利用が中心で、通常のPlus/Pro個人プランのモデルピッカーでは選べない
- **レガシーモデル**: 旧世代のモデルも、設定で明示的にオンにすれば移行期間中は選択肢に残るが、順次終了が決まっている。2026年2月にGPT-4o・GPT-4.1・GPT-4.1 mini・o4-miniが、3月にGPT-5.1系列(Instant/Thinking/Pro)が、6月上旬にGPT-5.2とGPT-5.3-Codexが、6月26日にGPT-4.5が、7月23日にGPT-5.4が、そして**8月26日にo3も予定通り終了**しており、本ページ執筆時点(9月4日)では「Show additional models」からオプトインで選べるレガシーモデルは事実上なくなっている

なお「モデル」と「プラン」は別の話である点も最初に押さえておきたい。プラン(Free/Go/Plus/Pro/Business/Enterprise)は「いくら払っていくつ使えるか」という契約の話、モデル(またはスライダーの位置)は「同じ会話の中でどれだけ考えさせるか」という話で、プランは「箱の大きさ」、モデル・スライダーは「箱の中でどれだけ力を入れるか」と考えると整理しやすい。

このほか、通常の「答えを返す」モデルとは毛色の異なる特殊モードとして、次の3つがある。いずれも今回(8月6日)のチャット向けアップデートの対象外で、変更されていない。

- **Codex**: コーディングに特化し、自律的にコードを読み書き・実行してPull Requestまで作成する専用エージェント
- **エージェントモード(ChatGPT agent)**: ブラウザ操作を伴う半自律タスクをこなす機能。入力欄のツールメニュー上で「エージェントモード」として選べる
- **ChatGPT Work**: 業務成果物(表計算・スライド・文書・簡易Webページなど)を仕上げるところまで担うビジネス向けエージェント。GPT-5.6とCodexの技術基盤の上に構築されている

Deep Research(高度な調査レポート機能)のような専用機能も、モデル選択とは別枠でその機能自体を呼び出す形になる点は変わらない。

## 使いどころ・使い分け

### 業務シーン別の選び方

| 業務シーン | 向いている設定 | 理由 |
|---|---|---|
| メール・チャット文面の作成、要約、雑談的な壁打ち | スライダー: Instant(Plus以上はGPT-6 Astra/GPT-5.6 Sol、Free/GoはGPT-5.6 Luna) | 待ち時間がほぼなく、多くのメッセージを回せる。デフォルトのままでよい |
| 大量の問い合わせ下書きを次々にこなす | Free/GoならGPT-5.6 Luna(テキストチャットは事実上無制限) | 品質より処理件数のスピードが重要な場面。無料・低価格プランでも数をこなせる |
| 複雑な数値分析、契約書などの長文精読、多段階の論理展開が必要な企画書 | スライダー: Medium〜High(GPT-6 Astra/GPT-5.6 Sol) | 内部で考える時間を確保することで見落としが減る |
| プログラムのコード生成・デバッグ | スライダー: High〜Extra High(GPT-6 Astra/GPT-5.6 Sol)/Codex | コードは一発で正解を出しにくく、推論の深さが精度に直結する。自律的に大量のコーディングを任せたい場合はChatGPTの汎用モデルではなく、コーディング特化のCodexの利用も検討する |
| 経営判断に関わる調査、法務・財務など誤りが許されない検討 | スライダー: Pro(GPT-6 Pro/GPT-5.6 Sol Pro) | 最も精度が高いが、Apps・Memory・Canvas・画像生成が使えない点に注意 |
| フォーム入力・CRM更新・予約代行など画面操作そのものを任せたい業務 | GPT-6 Astraの「computer use(コンピュータ操作)」/エージェントモード(ChatGPT agent) | AstraはOSWorld系のブラウザ・PC操作ベンチマークでSolより高速・高精度と報告されており、代行系タスクとの相性が今後さらに上がる見込み |
| 複数サイトを横断した情報収集、フォーム入力・予約などの代行 | エージェントモード(ChatGPT agent) | ブラウザ操作を伴う半自律タスクを任せられる(モデル選択ではなく入力欄のツールメニューから起動) |
| 資料・簡易Webページなど「完成品」まで一気に仕上げたい業務タスク | ChatGPT Work | ゴールを渡すと表計算・スライド・文書・簡易サイトなどの成果物として返してくれるビジネス向けエージェント |
| 過去のGPTsやワークフローが旧モデル前提で作られている | 現行のGPT-5.6/GPT-6系への移行確認 | 2026年8月26日のo3終了により旧世代のオプトイン選択肢は事実上なくなった。動作確認が済んでいなければ早めに |

判断の目安はシンプルで、「**すぐ返事が欲しい・内容が軽い→スライダーはInstant寄り**」「**込み入っている・裏取りが必要・コードを書く→スライダーをHigh〜Extra High寄りに**」「**失敗が許されない重要な一発勝負→Pro**」の3段階で考えればよい。迷ったらスライダーを中央(Medium)のままにしておけば、複雑な質問には内部で自動的にある程度の推論が加わる。社内ルールで思考の深さを固定したい場合は手動でスライダーを動かす。

### 比較表(速度・精度・コスト)

| 設定 | 速度 | 精度・推論力 | 主なコスト面の制約 | 主な利用可能プラン |
|---|---|---|---|---|
| GPT-6 Astra(2026年9月3日発表、順次展開中) | 標準〜(コンピュータ操作系タスクはSol比で約47%高速との報告) | Sol比でコーディング・コンピュータ操作・科学分野などが向上。サイバーセキュリティ評価が「Critical」域に達し高リスク機能はDaybreak審査制 | API価格は入力$10/出力$50(100万トークンあたり)が目安。ChatGPT契約内では追加課金なしで通常の利用枠を消費 | Plus/Pro/Business/Enterpriseに順次展開(Free/Go非対応) |
| Instant/Medium/High/Extra High(スライダー、Plus以上はGPT-6 Astra移行中/GPT-5.6 Sol、Free/GoはGPT-5.6 Luna) | Instantは最速、右に寄せるほど数秒〜数十秒の思考時間 | 段階を上げるほど精度も待ち時間も増加 | Free/Goはテキストチャットが事実上無制限。Plus以上は5時間あたりの上限がプランと段階で変動(Plusは目安十数〜100件程度)。Businessは週3,000件程度の目安 | Free/Go/Plus/Pro/Business/Enterprise全て |
| Pro(GPT-6 Pro移行中/GPT-5.6 Sol Pro) | 最も遅い(場合により数分) | 最高精度、コンテキスト約1.05Mトークン(Astra) | Pro/Business/Enterpriseの一部。BusinessはGPT-6 ProとGPT-5.6 Sol Proの合算で月15件(Standard)/週50件(Premium)程度が目安 | Pro/Business/Enterpriseの一部 |
| GPT-5.6 Luna(Free/Go既定、Business/Enterpriseは選択制) | 最速・最安 | 簡易タスク向け(旧世代のnano相当)。GPT-6版のLuna相当は本ページ執筆時点で未発表 | Free/Goはテキストチャット無制限。Business/Enterpriseは管理者設定による選択制 | Free/Go/Business/Enterprise |
| GPT-5.6 Terra | Lunaより高精度・Solより高速 | 5.5相当の性能をより低コストで提供 | 通常のPlus/Pro個人プランのモデルピッカーでは選択不可。Codex・API・Business/Enterprise管理者設定から利用 | Codex/API/Business/Enterprise(プランにより異なる) |
| Ultrafast(プレビュー、GPT-5.6 Sol基盤・Cerebras提携) | 標準の最大14倍・毎秒最大750トークン | Sol Standardと同等の知性 | API限定の少数顧客向けプレビュー。通常のChatGPT画面では選択不可 | API(一部顧客のみ) |
| レガシーモデル | ― | ― | 2026年8月26日のo3終了により、本ページ執筆時点で「Show additional models」から選べる旧世代モデルは事実上なくなった | ― |

## 実務での使い方

### モデル(推論エフォート)の切り替え手順(Web版・Plus/Pro以上)

1. チャット画面のモデルピッカー(またはメッセージ入力欄の設定アイコン)を開くと、推論エフォートの**スライダー**が表示される
2. スライダーを左右にドラッグして「Instant/Medium/High/Extra High/Pro」の5段階から選ぶ。左に寄せるほど速く安く、右に寄せるほど遅く賢くなる。初期位置はMedium
3. 2026年9月のGPT-6 Astraロールアウト期間中は、同じ画面でも実体モデルがGPT-5.6 Sol系のままか、GPT-6 Astra系に切り替わっているかがアカウントによって異なりうる。モデルピッカー内の詳細表示や設定画面で現在どちらが割り当てられているか確認できる

### Free/Goプランでの操作

モデルピッカー自体は表示されず、既定でGPT-5.6 Lunaが使われる。難しい質問だけ深く考えさせたいときは、入力欄の「**Think**」ボタンをオンにしてから送信する(そのメッセージだけ処理時間が長くなる)。

### モバイルアプリでの切り替え

チャット画面上部のモデル名またはスライダーをタップすると同様の操作ができる。基本操作はWeb版と同じ。

### 旧モデルを使いたい場合

設定(Settings)→General→「Show additional models」をオンにすると、移行期間中のレガシーモデルが選択肢に表示される仕組み自体は変わらない。ただし2026年8月26日にo3が予定通り終了したことで、本ページ執筆時点(9月4日)ではオプトインで選べる旧世代モデルは事実上なくなっている。今後もレガシーモデルは個別に終了予定日が公表され、恒久的な選択肢ではない前提で使う。

### プランによる違い(モデル選択の観点)

- **Free**: 既定モデルはGPT-5.6 Lunaで、テキストチャットは事実上無制限(ファイルアップロード・画像生成など他機能の上限は従来通り)。GPT-6 Astraは9月4日時点でFreeプランには展開されていない。「Think」ボタンで個別メッセージだけ深く考えさせられる
- **Go(月額8ドル程度)**: FreeプランとほぼGPT-5.6 Lunaの内容で、こちらもテキストチャットが事実上無制限。GPT-6 Astraは同様に非対応(スライダーによる細かい調整はPlus以上が前提)
- **Plus(月額20ドル)**: Instant〜Extra Highのスライダー調整が利用可(Proは非対応)。実体モデルはGPT-5.6 Solから**GPT-6 Astra**への切り替えが進行中で、9月4日時点ではロールアウトの初期段階にあたる
- **Pro(月額100ドル/200ドル)**: 2026年4月に新設された100ドルの中間プランと、従来の200ドルプランの違いは主に利用量上限(100ドルはPlusの5倍、200ドルは20倍が目安)。スライダーの全段階に加え最上位の「Pro」枠(GPT-5.6 Sol Pro→**GPT-6 Pro**へ移行中)まで利用可能な点は両プランで共通
- **Business/Enterprise**: 個人プランの単一スライダーとは異なり、管理者の設定次第でモデルごとに効果レベルを設定できる。Instant相当はほぼ無制限、Medium〜Extra High相当も週数千件規模まで利用可。Pro相当(GPT-6 Pro/GPT-5.6 Sol Pro)はBusiness Standardで月15件、Business Premiumで週50件程度が目安(両モデルの合算枠)。Proの可否は管理者のワークスペース設定による

Codex・エージェントモード・ChatGPT Workの利用可否・上限もプランによって段階的に異なる(Plusで基本機能、Pro/Businessでヘビーユース向けに上限拡大)。プランごとの料金・機能・ガバナンスの全体像は[ChatGPTのプラン比較](chatgpt-plan-comparison.md)を参照。本ページはモデル選びに絞って解説する。

### コピペで使える例(モデルの実力を引き出すプロンプトの一言)

スライダーをMedium以上に上げるだけでなく、プロンプト内でも「じっくり検討してほしい」旨を明示すると、思考ステップを増やす方向に働きやすい。

```
このプロンプトは複数の前提条件を比較検討する必要があります。
結論を急がず、以下の手順で考えてください。
1. 論点を洗い出す
2. それぞれの論点についてメリット・デメリットを整理する
3. 最後に総合的な結論と根拠を述べる
```

## 注意点・よくある誤解

- **モデル名・区分は数か月おきに変わる**: GPT-5登場(2025年8月)以降、5.1〜5.6を経て2026年9月3日に次世代フラッグシップ「GPT-6 Astra」が発表されるなど、短いスパンで世代交代が続いている。本ページの数値・名称は執筆時点の目安であり、実際の画面表示を都度確認する
- **GPT-6 Astraへの切り替えはロールアウト中で、アカウントによって表示が異なる**: 2026年9月3日の発表直後は、企業向け審査制プログラム経由の一部組織のみが先行利用でき、Plus/Pro/Business/Enterpriseへは「数日かけて」順次展開される段階にある。同じスライダーの「Instant〜Pro」という操作感は変わらないが、内部で動くモデルがGPT-5.6 Sol系かGPT-6 Astra系かはアカウントごとに異なりうる。Free/GoはGPT-5.6 Lunaのままで、Astraの展開対象に含まれていない
- **「Instant」は簡易な別モデルという理解のままだと戸惑う**: Plus以上ではInstantも含めてMedium・High・Extra Highまですべて同じフラッグシップモデル(移行状況によりGPT-5.6 SolまたはGPT-6 Astra)が担当し、違いは「どれだけ考える時間を与えるか」というエフォートの差になった。Free/GoだけはGPT-5.6 Lunaという別モデルが既定である
- **「常に一番賢い設定を使えばよい」は誤り**: スライダーを右に寄せるほど待ち時間が長く、利用回数の上限も早く消費する。日常的なやり取りはInstant寄りのままで十分なことが多い。まずInstantで試し、物足りなければ一段階ずつ右に動かすのが効率的
- **「モデル」と「プラン」を混同しない**: 「Plusに入っているのに込み入った質問がうまく処理されない」といった相談は、実際にはスライダーをInstant寄りのまま操作していたというケースが多い。契約プランとスライダーの位置は別の階層の話
- **無料・Goプランも2026年8月から様変わりした**: 以前は「Free/Goは軽量モデル止まり」だったが、GPT-5.6 Lunaの既定化とテキストチャット無制限化により、日常的な文章作成であれば無料プランでも回数を気にせず使えるようになった。ただしファイルアップロード・画像生成などの上限は残るため、業務利用にはPlus以上への移行が引き続き有効な選択肢
- **Codex・エージェントモード・ChatGPT Workは今回のアップデートの対象外**: 同じGPT-5.6系列の技術を使っていても、8月6日のスライダー導入はチャット画面向けの変更であり、Codex・エージェントモード・Workの挙動やモデルは変わっていない。別のUI・別の利用上限で動いている点に注意する
- **Proモデルは一部機能が使えない**: Apps・Memory・Canvas・画像生成などがPro実行中は利用できない場合がある。これらの機能が必要ならInstant〜Extra Highに切り替える
- **GPT-5.6-Cyber・Ultrafastは一般業務の対象外**: サイバーセキュリティ特化のGPT-5.6-Cyberは審査制のDaybreakプログラム経由、Ultrafastは高速化に特化したAPI向けプレビューで、いずれも通常のChatGPT画面からは使えない。一般的な業務利用では気にする必要はない
- **レガシーモデルは「いつか消える」前提で使う**: 過去のGPTsやワークフローが旧モデルに依存している場合、公表されている終了予定日までに新モデルでの動作確認を済ませておく。2026年に入ってからだけでもGPT-4o系(2月)、GPT-5.1系(3月)、GPT-5.2・GPT-5.3-Codex(6月)、GPT-4.5(6月)、GPT-5.4(7月)、o3(8月26日)と、ほぼ毎月のように何らかのモデルが終了しており、9月4日時点でオプトイン可能な旧世代モデルは事実上残っていない
- **利用回数の上限に関する細部は要確認**: スライダー統合後、自動的にエフォートが引き上げられた分が利用回数の上限をどう消費するかなど、細かい仕様は公式ヘルプの更新を都度確認するのが安全

## 最初の一歩

今使っているChatGPTの画面でモデルピッカー(またはスライダー)を開き、Instant〜Proのどの位置になっているか、また実体モデルがGPT-6 Astra系に切り替わっているかを確認してみる。次に、いま抱えている複雑な分析タスクを一つ選び、Instantのままの回答とスライダーをHigh寄りに動かした回答を見比べてみる。

## 関連トピック

- [ChatGPTのプラン比較](chatgpt-plan-comparison.md)
- [ChatGPTのエージェント機能(ChatGPT Agent)とスケジュールタスク(Tasks)](chatgpt-agent-mode-feature.md)

## 更新履歴

### 2026-09-04: 次世代フラッグシップ「GPT-6 Astra」の発表・ロールアウト開始を反映して最新化
- **内容**: 2026年9月3日に発表された次世代フラッグシップ「GPT-6 Astra」(および上位版「GPT-6 Pro」)の登場を反映。Daybreakプログラム経由の一部組織への先行提供を皮切りに、Plus/Pro/Business/Enterpriseへ数日かけて順次展開中でFree/Goは対象外であること、コンピュータ操作・コーディング・サイバーセキュリティ・科学分野でGPT-5.6 Solを上回るとされる点、サイバーセキュリティ評価が「Critical」域に達しDaybreak管理下に置かれている点、API価格(入力$10/出力$50・100万トークンあたり)とコンテキスト約1.05Mトークンを追記。ロールアウトがまだ進行中でアカウントにより表示が異なりうる旨の注記を各所に追加した。あわせて、2026年8月26日にo3が予定通り終了し、本ページ執筆時点でオプトイン可能な旧世代(レガシー)モデルが事実上なくなったことを反映し、業務シーン別の使い分け表・比較表・プラン別の違いを更新した
- **出典**: [OpenAI: GPT-6 Astra: A new generation of intelligence](https://openai.com/index/gpt-6-astra/)、[OpenAI Help Center: GPT-5.6 and GPT-6 Pro in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-56-and-gpt-6-pro-in-chatgpt)、[9to5Google: OpenAI launches GPT-6 Astra, 'the world's most intelligent and aligned model' that you can't use just yet](https://9to5google.com/2026/09/03/openai-gpt-6-astra-launch/)、[9to5Mac: OpenAI releasing major upgrade to ChatGPT and Codex with GPT-6 Astra, details here](https://9to5mac.com/2026/09/03/openai-releasing-major-upgrade-to-chatgpt-and-codex-with-gpt-6-astra-details-here/)、[Axios: OpenAI releases new model GPT-6 Astra, says it may represent AGI](https://www.axios.com/2026/09/03/openai-astra-gpt-6-agi-brockman)、[CNBC: OpenAI announces rollout of GPT-6 Astra model](https://www.cnbc.com/2026/09/03/open-ai-astra-gpt-6-cyber.html)、[Bloomberg: OpenAI Launches GPT-6 Astra With Enhanced Cybersecurity Safeguards](https://www.bloomberg.com/news/articles/2026-09-03/openai-rolls-out-gpt-6-astra-model-with-added-cyber-guardrails)、[MarkTechPost: OpenAI Releases GPT-6 Astra: A 1.05M-Context Computer-Use Model Gated Behind a 'Critical' Cyber Threshold](https://www.marktechpost.com/2026/09/03/openai-releases-gpt-6-astra-a-1-05m-context-computer-use-model-gated-behind-a-critical-cyber-threshold/)
- **注記**: OpenAI公式サイト・ヘルプセンターへの直接アクセスができなかったため、検索エンジンのプレビュー経由での参照および複数の第三者情報のクロスチェックに基づく内容。GPT-6 Astraの発表は本ページ執筆日の前日(9月3日)であり、ChatGPT画面への反映は「数日かけて」進行中の段階のため、スライダーの各段階(Instant/Medium/High/Extra High/Pro)が最終的にどこまでAstra系に置き換わるか、Business/Enterpriseの詳細な利用上限などは今後変わる可能性が高い。正確な最新値は契約中のプランの設定画面および[公式料金ページ](https://chatgpt.com/pricing)で要確認

### 2026-08-14: モデル選択の仕組みがスライダー型に変わったことを反映して最新化
- **内容**: 2026年8月6日のアップデートにより、Plus以上ではInstant/Thinkingという別モデル切り替えから、GPT-5.6 Sol1本を軸に「Instant/Medium/High/Extra High/Pro」の推論エフォートをスライダーで指定する方式へ変わったことを反映。Free/GoではGPT-5.6 Lunaが既定モデルとなりテキストチャットが事実上無制限化されたこと、Thinkボタンの追加、Business/EnterpriseはSol/Terra/Lunaを個別設定できる構成であること、API向けのUltrafast(最大14倍速)とセキュリティ特化のGPT-5.6-Cyber(Daybreakプログラム限定)の登場を追記し、業務シーン別の使い分け表・比較表・操作手順・プラン別の違いを全面的に書き換えた
- **出典**: [OpenAI: Improving GPT-5.6 Sol in ChatGPT—and expanding access to GPT-5.6 Luna for free users](https://openai.com/index/improving-gpt-5-6-sol-in-chatgpt/)、[OpenAI Help Center: GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001354-gpt-56-in-chatgpt)、[9to5Mac: OpenAI updating ChatGPT with a smarter GPT-5.6 Sol and unlimited free chats](https://9to5mac.com/2026/08/06/openai-updating-chatgpt-with-a-smarter-gpt-5-6-sol-and-unlimited-free-chats/)、[TechCrunch: ChatGPT brings unlimited text chats to free users](https://techcrunch.com/2026/08/06/openai-brings-unlimited-chatgpt-text-chats-to-free-users/)、[the-decoder: OpenAI improves GPT-5.6 Sol in ChatGPT and restricts free users to its weakest model](https://the-decoder.com/openai-improves-gpt-5-6-sol-in-chatgpt-and-restricts-free-users-to-its-weakest-model/)、[MacRumors: Free ChatGPT Users Get Unlimited Text Chats and GPT-5.6 Luna](https://www.macrumors.com/2026/08/06/chatgpt-free-unlimited-text-chats/)、[OpenAI: Previewing Ultrafast mode: GPT-5.6 Sol at up to 14X the speed](https://openai.com/index/previewing-ultrafast/)、[TechCrunch: OpenAI introduces 'Ultrafast,' a new mode that makes GPT-5.6 Sol work at 14x the speed](https://techcrunch.com/2026/08/13/openai-introduces-ultrafast-a-new-mode-that-makes-gpt-5-6-sol-work-at-14x-the-speed/)、[SecurityWeek: OpenAI Unveils New Cybersecurity Model GPT-5.6-Cyber](https://www.securityweek.com/openai-unveils-new-cybersecurity-model-gpt-5-6-cyber/)、[OpenAI: Expanding Daybreak as the Cyber Defense Window Narrows](https://openai.com/index/expanding-daybreak-as-the-cyber-defense-window-narrows/)
- **注記**: OpenAI公式ヘルプセンター・公式ブログへの直接アクセスができなかったため、検索エンジンのプレビュー経由での参照および複数の第三者情報のクロスチェックに基づく内容。特にスライダー統合後の利用回数上限の消費ルール、Business/Enterprise向けの詳細な選択肢はソースにより記述の粒度が異なり、正確な最新値は契約中のプランの設定画面および[公式料金ページ](https://chatgpt.com/pricing)で要確認

### 2026-07-23: GPT-5.6世代へのモデル交代とレガシーモデル終了スケジュールを最新化
- **内容**: 2026年7月9日のGPT-5.6(Sol/Terra/Luna)一般提供開始により、ThinkingとProの実体モデルがGPT-5.5からGPT-5.6 Sol・Sol Proに交代したことを反映。GPT-5.5 Instant Miniへのフォールバック交代(7月6日)、Autoルーターの自動切り替えがThinking週間上限を消費しない仕様、GPT-5.1〜GPT-5.4の順次終了(3月・6月・7月23日)、新設のビジネス向けエージェント「ChatGPT Work」、Proプランの100ドル/200ドルの2階層化を追記
- **出典**: [OpenAI: GPT-5.6: Frontier intelligence that scales with your ambition](https://openai.com/index/gpt-5-6/)、[OpenAI Help Center: GPT-5.6 in ChatGPT](https://help.openai.com/en/articles/20001325-a-preview-of-gpt-56-sol-terra-and-luna)、[OpenAI Help Center: Retiring GPT-4o and other ChatGPT models](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)、[9to5Mac: OpenAI unveils ChatGPT Work agent, GPT-5.6 models now available](https://9to5mac.com/2026/07/09/openai-announcing-the-next-chapter-for-chatgpt-today-watch-here/)、[the-decoder: OpenAI staffer maps out which of GPT-5.6 Sol's five reasoning levels fits which task complexity](https://the-decoder.com/openai-staffer-maps-out-which-of-gpt-5-6-sols-five-reasoning-levels-fits-which-task-complexity/)、[reconn-ai: July 6, 2026 — GPT-5.5 Instant Mini in ChatGPT](https://reconn-ai.com/chatgpt-july-6-2026-gpt-5-5-instant-mini-in-chatgpt)、[ghacks: OpenAI Upgrades GPT-5.5 Instant and Confirms Retirement of o3 and GPT-4.5 Models](https://www.ghacks.net/2026/06/03/openai-upgrades-gpt-5-5-instant-and-confirms-retirement-of-o3-and-gpt-4-5-models/)、[thenextweb: OpenAI's new $100 ChatGPT Pro plan targets Claude Max](https://thenextweb.com/news/openais-new-100-chatgpt-pro-plan-targets-claude-max-with-five-times-the-codex-access)、[note: 【2026年7月版】ChatGPT WorkとはーCodex統合とSitesで何が変わるか](https://note.com/kazu_t/n/nb664dad5f627)、[uravation: ChatGPT Workとは｜できること・料金・使い方【2026年7月】](https://uravation.com/media/chatgpt-work-guide-2026/)
- **注記**: OpenAI公式ヘルプセンター・公式ブログへの直接アクセスができなかったため、検索エンジンのプレビュー経由での参照および複数の第三者情報のクロスチェックに基づく内容。モデル名・利用回数上限・コンテキストサイズは特に変化が速いため、正確な最新値は契約中のプランの設定画面および[公式料金ページ](https://chatgpt.com/pricing)で要確認

### 2026-07-06: 重複ページの統合
- **統合元**: chatgpt-model-comparison.md(本ページをベースに、「モデル」と「プラン」の混同への注意、Codex・エージェントモード・Deep Researchとの関係、シーン別の3段階の判断目安、Goプランでの Thinking 利用手順を統合)
- **出典**: [OpenAI公式ブログ: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)、[OpenAI Help Center: ChatGPT エージェント](https://help.openai.com/ja-jp/articles/11752874-chatgpt-agent)、[OpenAI: Codex](https://openai.com/codex/)、[TechRadar: ChatGPT just made it easier to pick the right model](https://www.techradar.com/ai-platforms-assistants/chatgpt/chatgpt-just-made-it-easier-to-pick-the-right-model-just-like-gemini-does-heres-when-to-use-instant-thinking-or-pro)

### 2026-07-05: 初版執筆
- **内容**: ChatGPTのモデルピッカー(Instant/Thinking/Pro)の構成、業務シーン別の使い分け、プランごとの利用可否・上限、モデル切り替えの画面操作手順、レガシーモデルの終了スケジュールを整理
- **出典**: [OpenAI Help Center: GPT-5.5 in ChatGPT](https://help.openai.com/en/articles/11909943-gpt-55-in-chatgpt)、[OpenAI Help Center: ChatGPT Business - Models & Limits](https://help.openai.com/en/articles/12003714-chatgpt-business-models-limits)、[OpenAI Help Center: ChatGPT Enterprise and Edu - Models & Limits](https://help.openai.com/en/articles/11165333-chatgpt-enterprise-and-edu-models-limits)、[OpenAI Help Center: Legacy Model Access for Enterprise and Edu Users](https://help.openai.com/en/articles/11954883-legacy-model-access-for-enterprise-and-edu-users)、[OpenAI Help Center: Retiring GPT-4o and other ChatGPT models](https://help.openai.com/en/articles/20001051-retiring-gpt-4o-and-other-chatgpt-models)、[OpenAI公式ブログ: Retiring GPT-4o, GPT-4.1, GPT-4.1 mini, and OpenAI o4-mini in ChatGPT](https://openai.com/index/retiring-gpt-4o-and-older-models/)、[GIGAZINE: 'GPT-5.5 Instant' is now available](https://gigazine.net/gsc_news/en/20260507-openai-gpt-5-5-instant/)、[9to5Mac: PSA: OpenAI will soon remove several models from ChatGPT](https://9to5mac.com/2026/01/30/psa-openai-will-remove-several-models-from-chatgpt-next-month/)、[knightli.com: GPT-5.5 Instant vs Thinking vs Pro](https://knightli.com/en/2026/05/07/gpt-5-5-instant-thinking-pro-differences/)、[genai-ai.co.jp: 【2026年7月最新】ChatGPTのバージョン一覧](https://genai-ai.co.jp/ai-kanri/blog/cc-chatgpt-version-guide/)
- **注記**: OpenAI公式ヘルプセンター(help.openai.com)への直接アクセスができなかったため、検索エンジンのプレビュー経由での参照および複数の第三者情報のクロスチェックに基づく内容。モデル名・利用回数上限は特に変化が速いため、正確な最新値は契約中のプランの設定画面および[公式料金ページ](https://chatgpt.com/pricing)で要確認
