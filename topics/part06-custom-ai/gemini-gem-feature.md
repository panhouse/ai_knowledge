---
title: "Gem(Geminiのカスタムボット機能)の基本"
part: 6
chapter: 第2章 主要ツールでの作り方
tags: [Gemini, Gem, カスタムGPT, プロンプト管理, Google Workspace]
created: 2026-07-06
updated: 2026-07-23
---

# Gem(Geminiのカスタムボット機能)の基本

## これは何か

Gem(ジェム)は、Geminiに「役割」と「指示」を固定で覚え込ませ、参照資料(ナレッジファイル)まで紐づけて保存できる、自分専用のカスタムAIを作る機能である。これがないと、「議事録を決まった形式で要約して」「この口調でメールをチェックして」といった前提説明を、チャットを開くたびに毎回コピペし直す羽目になる。GemはChatGPTの「GPTs(カスタムGPT)」、Claudeの「Projects」に相当する機能で、一度作れば以後はワンクリックで同じ役割のAIを呼び出せる。

似た名前の「保存済み情報(Saved info)」という別機能もあり、この2つは混同されやすい。本ページはGemに絞って、作り方・使いどころ・注意点を整理する。

## 仕組み・背景

Gemは「指示(カスタム指示)」+「ナレッジ(任意で添付する参照ファイル)」の組み合わせを1つの名前付きボットとして保存する仕組みである。作成・編集・一覧管理は「Gemマネージャー」という専用画面で行う。

もともとGemは有料の「Gemini Advanced」(現在のGoogle AI Pro相当)などの契約者限定機能だったが、2025年3月にGoogle公式ブログで無料ユーザーへの展開が発表され、2026年7月時点でも無料プランでGemの作成・利用ができる状態が続いている([Google公式ブログ](https://blog.google/products/gemini/new-gemini-app-features-march-2025/)、[9to5Google](https://9to5google.com/2025/03/25/gemini-gems-free-mobile/))。ネット上の解説記事には「Gemはpro以上の機能」と書かれたものも残っているが、これは古い情報か、法人向けプランの話と混同している可能性が高い。無料プランと有料プランの違いは「作れるかどうか」ではなく、**そのGemが動くモデルの性能と使える回数**にある。2026年7月時点では無料プランのGeminiアプリは軽量モデルの「Gemini 3.6 Flash」(2026年7月21日公開)がデフォルトで動作し、Google AI Pro/Ultraなどの有料プランではより高性能なPro系モデルや、無料プランより多い利用枠でGemを動かせる([Google公式ブログ: Gemini 3.6 Flash発表](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)、[9to5Google](https://9to5google.com/2026/07/21/gemini-3-6-flash-launch/))。モデル名はGoogleのアップデート頻度が高く数か月単位で変わるため、正確な現行モデルはGeminiアプリのモデル選択メニューで都度確認するのが確実である。

また2026年5月には、Geminiアプリ全体の利用上限の仕組みが「1日◯回」という固定回数制から、プロンプトの複雑さや会話の長さを加味した「コンピュート使用量ベース+5時間ごとにリセット、週次でも上限あり」という方式に切り替わった。この変更はGemの利用にもそのまま適用されるため、Gemを多用する業務では有料プランの利用枠(変更直後の反発を受けて有料プランは利用枠が3倍に引き上げられている)を踏まえて運用するとよい([9to5Google: Gemini app now has compute-based usage limits](https://9to5google.com/2026/05/19/google-ai-ultra-100/)、[9to5Google: Google adjusts Gemini's new usage limits](https://9to5google.com/2026/05/28/gemini-new-usage-limits/))。

Gemと紛らわしいのが「**保存済み情報(Saved info)**」という機能である。両者は目的も挙動もまったく違う。なお2026年1月に、この機能を含むGoogleアカウント全体の個人設定エリアが「パーソナライズ」から「**Personal Intelligence**」という名称に統合され、Gmail・写真などの連携アプリの管理と合わせて扱われるようになった。保存済み情報自体の管理は引き続き `gemini.google.com/saved-info` または「設定→Personal Intelligence」からアクセスできる([Google公式ヘルプ: Connect your Google apps to personalize your Gemini experience](https://support.google.com/gemini/answer/16598406?hl=en))。

| 項目 | Gem | 保存済み情報(Saved info) |
|---|---|---|
| 何を保存するか | 自分で書いた役割・指示文と、任意で添付した参照ファイル | 会話の中でGeminiが「覚えておくと便利」と判断した、あなた自身に関する事実(職種・好み・進行中の案件など) |
| 更新のされ方 | 自分で編集しない限り変わらない(固定) | 会話のたびに自動で追加・更新される(ChatGPTの「メモリ」に相当) |
| 使う場面 | 特定の業務・役割用に、毎回同じルールで動く専用ボットを呼び出したいとき | 素のGemini(通常のチャット)や各Gemが、あなたの背景を踏まえて回答の精度を上げてほしいとき |
| 管理画面 | Gemマネージャー | gemini.google.com/saved-info、または設定→Personal Intelligence(旧パーソナライズ) |

重要なのは、この2つは**併用される**という点である。Gem自体は外部の情報を勝手に取りに行かないため、Gemの指示文に「私の好みは常にこう」と毎回書きたくない場合は、保存済み情報側にその情報を覚えさせておくと、どのGemを使ってもその内容が加味されるようになる(例: 「出張プランGem」を役割として作りつつ、好みの航空会社や予算感は保存済み情報に任せる、という組み合わせ方)。

## 使いどころ・使い分け

| 場面 | 向いている機能 |
|---|---|
| 特定の業務(議事録要約、メールチェック、企画書のたたき台作成など)を毎回同じフォーマット・ルールで実行したい | Gem |
| 会話の中で自然に蓄積されればよい、自分自身に関する緩やかな情報(役職・好み・継続案件) | 保存済み情報 |
| 一度きりの質問や、毎回内容が変わる雑多な相談 | 素のGeminiチャット(Gem化するほどでもない) |
| 手元の特定資料**だけ**を根拠に正確に調べたい(社内マニュアルなど) | NotebookLM([Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)を参照)。GemのナレッジもRAG(検索拡張生成)的に使えるが、正確な出典追跡が主目的ならNotebookLMの方が向く |
| 複数人のチームで同じ役割のAIを使い回したい | Gemの共有機能(後述)、または法人向けGoogle Workspace with Gemini |
| Google Drive上のフォルダ・メール・カレンダーをまとめて1つの作業空間として扱いたい | Gemより粒度が広い「Google Driveプロジェクト」機能(後述、Gemとは別物) |

判断の目安はシンプルで、「同じ指示を3回以上コピペしている業務」があればGem化の候補になる。

## 実務での使い方

### Gemの作成手順(2026年7月時点の目安)

1. gemini.google.com を開き、左側メニューの「Gemを表示」をクリック
2. 「Gemマネージャー」画面が開くので、「+新しいGem」を選択
3. 以下の項目を入力する

| 項目 | 内容 |
|---|---|
| 名前 | 用途が一目で分かる短い名称(例: 「議事録要約Gem」) |
| 指示 | 役割(ペルソナ)・してほしいタスク・前提知識・出力形式をまとめて記述するシステムプロンプト相当の欄。「Geminiを使用」ボタンで簡単な目的文を詳しい指示文に自動リライトさせることもできる |
| ナレッジ(任意) | 端末からのファイルアップロードまたはGoogle Driveのファイルを紐づけられる。同時に追加できるファイルは最大10個、1ファイルあたり100MBまでが目安([Google公式ヘルプ: Tips for creating custom Gems](https://support.google.com/gemini/answer/15235603?hl=en))。Google Driveのファイルを参照させた場合は常に最新版が参照される |

4. 右側のプレビューでテスト対話をしながら内容を調整し、「保存」をクリック

作成したGemはGeminiのWeb版・モバイルアプリ・Google Workspaceのサイドパネルに加え、2026年にはGoogle Drive内の「Ask Gemini」画面(drive.google.comで右上の「Ask Gemini」→左上メニューから「Gems」を選択)からも直接呼び出せるようになった([Google公式ヘルプ: Use Gems with Gemini in Google Drive](https://support.google.com/drive/answer/16684485?hl=en)、[Google Workspace Updates: Ask Gemini in Drive now generally available](https://workspaceupdates.googleblog.com/2026/04/ask-gemini-in-drive-now-generally-available.html))。似た名前の「Google Driveプロジェクト」は、特定のフォルダ・メール・予定をひとまとめにした作業空間を作る別機能で、Gem(役割・指示の保存)とは目的が異なる点に注意する。

### コピペで使える指示欄のテンプレート例

**議事録要約Gem**

```
## 役割
あなたは会議の議事録を、決まったフォーマットで要約する専門アシスタントです。

## タスク
渡された会議の文字起こし・メモから、以下の見出しで要約を作成してください。
- 決定事項
- 次のアクション(担当者・期限がわかれば併記)
- 保留・要検討事項
- その他共有事項

## 出力ルール
- 「ですます調」で書く
- 発言者名は原則出さず、内容ベースでまとめる
- 文字起こしに書かれていない内容は推測せず補わない
```

**メール文面チェックGem**

```
## 役割
あなたは社外向けビジネスメールの文面をチェックする校閲担当です。

## チェック観点
- 敬語・言い回しに失礼な表現がないか
- 結論(依頼・お礼など)が冒頭で分かる構成になっているか
- 誤字脱字、数字や日付の誤り

## 出力形式
1. 修正版の全文
2. 変更箇所とその理由を箇条書きで(3〜5点程度)
```

### 共有機能(2025年9月〜)

作成したGemは他のユーザーに共有できる。共有範囲は「非公開(自分のみ)」「リンクを知っている全員」「組織内(同じ職場・学校のGoogleアカウントを持つ人なら誰でも)」の3段階から選べる([Google公式ヘルプ: Share a Gem from Gemini Apps](https://support.google.com/gemini/answer/16504957?hl=en))。Google Workspaceの管理者は、管理コンソール側でユーザーにGemの共有自体を許可するかどうかを組織部門・グループ単位で制御できる([Google公式ヘルプ: Turn Gem sharing on or off](https://knowledge.workspace.google.com/admin/gemini/turn-gem-sharing-on-or-off))。なお、ナレッジに添付したファイルの種類によっては共有できない組み合わせがある(端末アップロードやGoogle Driveのファイルは共有対象になるが、一部のファイル形式は共有時に外れる場合がある)。

Gemの共有はGoogle Driveのファイル共有と同じ権限管理の仕組みに乗っており、個別ユーザーに共有する際は「有効期限を追加」でアクセス権が切れる日時をピンポイントで指定できる。プロジェクト期間中だけ社外パートナーや期間限定メンバーに使わせたい場合に、権限の消し忘れ(渡しっぱなし)を防げるため、業務利用では積極的に使うとよい。なお、共有されたGemへのアクセス権が取り消されると、そのGemは相手のGoogle Drive上からも削除される([TSクラウド: Geminiの Gem 共有方法](https://googleworkspace.tscloud.co.jp/gemini/gem-sharing))。

### 他ツールとの対応関係

| 項目 | Geminiの「Gem」 | ChatGPTの「GPTs」 | Claudeの「Projects」 | Microsoft 365 Copilotの「エージェント ビルダー」 |
|---|---|---|---|---|
| 固定できるもの | 指示文(役割・出力形式)+ナレッジファイル | 指示(Instructions)+ナレッジ+Web検索/画像生成/Actions(外部API連携)のオンオフ | カスタム指示+ナレッジファイル | 自然言語の指示+SharePoint/OneDriveなど社内データ連携+実行トリガー |
| 設定場所 | gemini.google.com左メニュー「Gemを表示」→Gemマネージャー(Google Driveの「Ask Gemini」画面からも利用可) | ChatGPT左サイドバー「GPTを探す」→GPT Builder | claude.ai/projects | Microsoft 365 Copilotアプリ左ペインの「エージェントの作成」 |
| 必要プラン | 無料プランでも作成・利用可(動作モデルの性能・利用枠は有料プランほど高い) | Freeプランでは作成不可(利用のみ)。作成にはPlus以上が必要 | 2026年2月以降、無料プランでも最大5件まで作成可。無制限・大容量のナレッジはPro以上 | Copilot ChatまたはMicrosoft 365 Copilotライセンスが必要。社内データ(SharePoint等)との連携には追加のライセンス条件がある |
| 共有・公開範囲 | 非公開/リンクを知っている全員/組織内、の3段階(管理者が可否を制御可) | 自分のみ/リンクを知っている人のみ/GPTストアで一般公開 | 自分のみ、Team/Enterpriseならワークスペース内共有 | 組織内で発行(パブリッシュ)し、Teams・SharePoint等に配置。管理者ポリシーで制御 |
| 外部の一般公開ストア | なし(組織内共有が中心) | あり(GPTストア) | なし | なし(組織内配布が基本) |

## 注意点・よくある誤解

- **GemとGPTs・Projectsは「保存できる範囲」が微妙に違う**: GPTsはActions(外部API呼び出し)まで組み込めるが、Gemは指示文とナレッジファイルの範囲にとどまる。外部システム連携までやりたい場合はGemだけでは不十分な場合がある
- **「Gemは有料プラン限定」という古い情報に注意**: 2025年3月以降は無料プランでも作成・利用できる。ネット記事の中には移行前の情報のまま止まっているものがあるため、実際の挙動は自分のアカウントで確認するのが確実
- **利用上限は「1日◯回」ではなくなった**: 2026年5月の仕様変更で、Geminiアプリ全体(Gemを含む)の利用上限はプロンプトの複雑さ・会話の長さを踏まえたコンピュート使用量ベースに変わり、5時間ごと・週次の二段構えでリセットされる方式になった。Gemを業務で多用する場合、無料プランでは上限に達しやすい点を踏まえておく
- **Gemは会話の内容を自動で学習しない**: Gemの指示文は自分で編集しない限り変わらない。会話の中で自然に個人情報を蓄積してほしい場合は、保存済み情報(Saved info、現在は設定の「Personal Intelligence」配下)側の役割であり、両者を混同すると「毎回同じ質問をしているのに覚えてくれない」という誤解につながる
- **ナレッジファイルは機密情報の扱いに注意**: 共有範囲を「組織内」や「リンクを知っている全員」にすると、添付したナレッジファイルの内容も共有相手が閲覧できる状態になる。社外秘の資料を含むGemは、共有範囲を「非公開」のままにするか、法人向けのアクセス権管理と合わせて運用する
- **ファイルの追加数・サイズには上限がある**: 一度に追加できるナレッジファイルは目安として10個・1ファイル100MBまでで、大量の社内資料を横断的に検索させたい用途には、Gemより NotebookLM や Google Workspace側の検索機能の方が向く場合がある

## 最初の一歩

自分が毎回同じ前提・フォーマットを説明してからGeminiに頼んでいる業務を1つ選び、その指示を書き込んだGemを1つ作ってみる(共有範囲は「非公開」で十分)。

## 関連トピック

- [Google Geminiの基本](../part03-ai-chat-tools/google-gemini-basics.md)
- [GPTsの作り方と公開設定](../part06-custom-ai/gpts-creation-basics.md)
- [ChatGPTのメモリ(Memory)機能](../part03-ai-chat-tools/chatgpt-memory-feature.md)

## 更新履歴

### 2026-07-23: モデル・利用上限・Personal Intelligence改称などを最新化
- **内容**: 無料プランのデフォルトモデルがGemini 3.6 Flash(2026年7月21日公開)へ更新されたこと、2026年5月からGeminiアプリ全体の利用上限が「コンピュート使用量+5時間ごと/週次リセット」方式に変わりGemの利用にも影響すること、「保存済み情報」を含む個人設定エリアが2026年1月に「Personal Intelligence」へ改称されたこと、Google DriveのAsk Gemini画面からGemを直接呼び出せるようになったこと(2026年4月GA)、Claude Projectsが2026年2月以降無料プランでも最大5件まで作成可能になったことを反映し、他ツール対応表・注意点を更新
- **出典**: [Google公式ブログ: Introducing Gemini 3.6 Flash, 3.5 Flash-Lite, and 3.5 Flash Cyber](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-6-flash-3-5-flash-lite-3-5-flash-cyber/)、[9to5Google: Google launches Gemini 3.6 Flash and 3.5 Flash-Lite](https://9to5google.com/2026/07/21/gemini-3-6-flash-launch/)、[9to5Google: Gemini app now has compute-based usage limits](https://9to5google.com/2026/05/19/google-ai-ultra-100/)、[9to5Google: Google adjusts Gemini's new usage limits in response to complaints](https://9to5google.com/2026/05/28/gemini-new-usage-limits/)、[Google公式ヘルプ: Connect your Google apps to personalize your Gemini experience](https://support.google.com/gemini/answer/16598406?hl=en)、[Google公式ヘルプ: Use Gems with Gemini in Google Drive](https://support.google.com/drive/answer/16684485?hl=en)、[Google Workspace Updates: Ask Gemini in Drive now generally available](https://workspaceupdates.googleblog.com/2026/04/ask-gemini-in-drive-now-generally-available.html)、[Google公式ヘルプ: Tips for creating custom Gems](https://support.google.com/gemini/answer/15235603?hl=en)、[Google公式ヘルプ: Share a Gem from Gemini Apps](https://support.google.com/gemini/answer/16504957?hl=en)

### 2026-07-06: 初版執筆
- **内容**: Gemの定義・作成手順(Gemマネージャーでの操作)、保存済み情報(Saved info)との違い、無料/有料プランでの利用可否(2026年7月時点でもGemini 2.5 Flashベースの無料プランでGemの作成・利用が可能なことをWeb検索で再確認)、ナレッジファイルの上限(最大10個・100MB)、共有機能(2025年9月〜、Google Driveと同じ権限管理に基づく個別ユーザー単位の共有期限設定を追加)、GPTs/Claude Projects/Microsoft 365 Copilotエージェントビルダーとの対応表、議事録要約・メール文面チェックのGem指示文テンプレートを整理
- **出典**: [Google公式ブログ: Gemini app updates: Deep Research, connected apps, personalization](https://blog.google/products/gemini/new-gemini-app-features-march-2025/)、[9to5Google: Free Gemini users can now access Gems on Android, iOS](https://9to5google.com/2025/03/25/gemini-gems-free-mobile/)、[Google公式ヘルプ: Gemini アプリでファイルをアップロードして分析する](https://support.google.com/gemini/answer/14903178?hl=ja)、[Google公式ヘルプ: Gemini アプリで Gem を共有する](https://support.google.com/gemini/answer/16504957?hl=ja)、[Google公式ヘルプ: Gem の共有を有効または無効にする(管理者向け)](https://support.google.com/a/answer/16460551?hl=ja)、[Microsoft Learn: Microsoft 365 Copilotでエージェント ビルダーを使用してエージェントをビルドする](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder-build-agents)、[GEO Toolbox: Gemini Gems: What They Are and How to Build One (2026)](https://geotoolbox.ai/blog/gemini-gems)、[TSクラウド: Geminiの Gem 共有方法。ビジネス活用事例と注意点を解説](https://googleworkspace.tscloud.co.jp/gemini/gem-sharing)
