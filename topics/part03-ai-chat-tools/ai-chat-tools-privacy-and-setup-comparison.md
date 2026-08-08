---
title: Gemini・Claude・Copilotの初期設定とデータ利用オプトアウト比較
part: 3
chapter: 第2章 初期設定とデータ保護
tags: [Gemini, Claude, Copilot, 初期設定, データ利用, オプトアウト, プライバシー, カスタム指示]
created: 2026-07-07
updated: 2026-08-08
---

# Gemini・Claude・Copilotの初期設定とデータ利用オプトアウト比較

## これは何か

ChatGPT以外のAIチャットツール(Gemini・Claude・Microsoft Copilot)にも、「入力した会話をモデルの学習に使わせない」オプトアウト設定と、「毎回の前提を教える」カスタム指示の仕組みがある。ただし呼び方も設定場所も、個人向け・法人向けでの既定値(デフォルト)もツールごとにバラバラで、ChatGPTの感覚のまま他ツールを触ると「どこにあるか分からない」「実は学習に使われていた」という事故が起きやすい。本ページは、ChatGPTの詳細を扱った[ChatGPTの初期設定とデータ利用のオプトアウト](chatgpt-initial-setup-and-opt-out.md)・[ChatGPTの初期設定とカスタム指示の書き方](chatgpt-custom-instructions.md)の対になる、Gemini・Claude・Copilot版の設定ガイド兼、4ツール横断の比較表である。

## 仕組み・背景

4ツールに共通するのは、「①学習利用のオプトアウト」「②カスタム指示(自分専用の前提)」「③会話から自動で溜まる記憶」という3層構造がある点である(3層構造そのものは[ChatGPTの初期設定とデータ利用のオプトアウト](chatgpt-initial-setup-and-opt-out.md)で詳述)。本ページで扱う①と②について、2026年8月時点の実装は次のように整理できる。

- **Gemini**: 学習利用への同意は、2025年9月に「Gemini Appsアクティビティ」から名称変更された「アクティビティを保存(Keep Activity)」というオン/オフの履歴保存設定に統合されている。オンのままだと、チャット履歴に加えてアップロードしたファイル・写真の一部が匿名化されたうえで人間のレビュアーに読まれ、モデル改善(学習)に使われる可能性がある。オフにすると以後の会話・アップロードは人間レビュー・学習の対象から外れる。「アクティビティを保存しない」ことと「学習に使わない」ことが1つのトグルにまとまっている点がChatGPT・Claudeと異なる
- **Claude**: 「Help improve Claude」という個別トグルがプライバシー設定内にある。2025年8月に予告され同年10月8日に適用が始まった規約変更で、それまで学習利用がなかった個人向け(Free/Pro/Max)にも「学習に使うかどうかをユーザーが選ぶ(強制選択式)」仕組みが導入され、既定はオン(要オプトアウト)になった
- **Microsoft Copilot(個人向け)**: 「モデルのトレーニング」という独立したプライバシー項目があり、既定でオン。カスタム指示・記憶(メモリ)のオン/オフとは別のスイッチとして管理されている
- **共通する非対称構造**: いずれのツールも「個人向けプランは既定で学習利用オン(要オプトアウト)」「法人・エンタープライズ向けプランは契約上、既定で学習利用オフ(オプトアウト操作が不要、またはトグル自体が表示されない)」という構図になっている

## 使いどころ・使い分け

| 利用者像 | まず確認すべきこと |
|---|---|
| 個人でGemini/Claude/Copilotを無料または個人課金プランで使っている | 学習利用オプトアウトのトグルを必ず自分でオフにする(既定はほぼ全ツールでオン) |
| 会社のGoogle Workspace / Claude for Work(Team・Enterprise) / Microsoft 365ライセンスで使っている | 契約上すでに学習非利用が既定になっていることが多いが、個人アカウントを併用していないかを確認する |
| Gemini・Claudeのカスタム指示を初めて使う | 「自分について」「どう応答してほしいか」を書く。ChatGPTと違い1入力欄にまとめるツールが多い |
| EU・EEA・英国・スイス在住でGeminiを使っている | Geminiの「パーソナルコンテキスト(保存した情報・Instructions for Gemini)」機能自体が提供されていない地域があるため、代わりに毎回プロンプト冒頭に前提を書く運用になる |
| 機密性の高い相談を一度きりでしたい | Geminiは「一時チャット(Temporary Chat)」、Claudeは右上のゴースト(幽霊)アイコンから入る「Incognito」、Copilotは右上ドロップダウンの「Temporary chat」を使う。いずれも履歴・記憶・学習には使われないが、不正利用対策のため一定期間(目安72時間〜30日)はバックエンドに一時保持される点は共通 |

判断に迷ったら、「学習利用オプトアウト」と「カスタム指示・記憶」は別スイッチであることを前提に、両方を個別に確認する。片方だけ設定して安心しないことが実務上のポイントになる。

## 実務での使い方

### 1. 4ツール比較表(2026年8月時点)

| ツール | 学習利用のデフォルト(個人向け) | 学習利用のデフォルト(法人向け) | オプトアウトの設定場所 | カスタム指示の設定場所 |
|---|---|---|---|---|
| **ChatGPT** | オン(Free/Go/Plus/Pro) | オフ(Business/Enterprise/Edu) | 設定→データコントロール→「すべての人のためにモデルを改善する」 | 設定→パーソナライズ→カスタム指示 |
| **Gemini** | オン(EEA/英国/スイス以外の無料・Google AI Pro/Ultra) | オフ(Google Workspace with Gemini。契約上除外、操作不要) | myactivity.google.com(またはGeminiアプリの「設定とヘルプ」→アクティビティ)→「アクティビティを保存(Keep Activity)」をオフ | 「設定とヘルプ」→Personal Intelligence→「Geminiへの指示」 |
| **Claude** | オン(Free/Pro/Max、2025年10月8日〜) | オフ(Team/Enterprise/API/Claude for Government) | 設定→プライバシー→「Help improve Claude」をオフ | 設定→プロフィール→「Claudeへの指示」 |
| **Microsoft Copilot(個人向け)** | オン | オフ(Microsoft 365 Copilot/Copilot Chat。Enterprise Data Protectionで契約上除外) | プロフィールアイコン→プロフィール名→プライバシー→「モデルのトレーニング」(モバイル: アカウント→プライバシー→「会話アクティビティのトレーニング」) | プロフィールアイコン→プロフィール名→「メモリ」→「パーソナライズと記憶」内のカスタム指示 |

法人向けの「Microsoft 365 Copilot」「Google Workspace with Gemini」「Claude for Work」の細かな契約条件・料金は、それぞれ[Microsoft Copilotの基本](microsoft-copilot-basics.md)、[Google Geminiの基本](google-gemini-basics.md)、[Claude(Anthropic)の基本](claude-basics.md)を参照。

### 2. Geminiの設定手順

**学習利用のオプトアウト(アクティビティを保存/Keep Activity)**

1. ブラウザで myactivity.google.com/product/gemini を開く、またはGeminiアプリ右上のプロフィールアイコン→「設定とヘルプ」→「アクティビティ」を開く
2. ページ上部にカードで表示される「アクティビティを保存(Keep Activity)」のトグルをオフにする(2025年9月まで「Gemini Appsアクティビティ」という名称だったが、機能はほぼ同じまま改称された)
3. オフにする際は「オフにする」(今後のアクティビティのみ対象外にする)と「オフにしてアクティビティを削除」(過去の履歴も削除する)の2択が表示されることがある
4. オンのままだと、チャット履歴に加えて、Geminiにアップロードしたファイル・写真・画面共有の一部もサンプルとしてGoogleサービスの改善(学習)に使われ得る。オフにすると以後の会話・アップロードは人間レビュー・学習の対象から外れる。ただし過去にさかのぼって除外されるわけではなく、サービス提供・不具合対応のため一時的に(目安72時間程度)は保持され、この間は「72時間以上経過した会話は再開できない」という制約が働く
5. Google Workspace with Gemini(法人向け)ライセンスの場合、この設定を触らなくても契約上、組織外への学習利用・人間レビューは行われない

**カスタム指示(Geminiへの指示)**

1. Geminiアプリのプロフィールアイコン→「設定とヘルプ」→「Personal Intelligence」→「Geminiへの指示」を開く
2. 「+」から指示を追加し、名前を付けて保存する(用途別に複数保存し、チャットごとに切り替えられる)
3. 「保存した情報」機能と合わせて使うと、明示的に指示していない過去のやり取りからも回答の前提を汲み取れるようになる(この自動推論機能は個人アカウント限定で、職場・学校・保護者管理アカウントおよびEEA・英国・スイスでは提供されていない)

コピペで使える記入例(Geminiへの指示欄に貼る内容、1指示あたりの目安は数百文字程度):

```
私は中堅の製造業で購買・調達を担当しています。
専門用語は使ってよいですが、法務・会計の専門用語は初出で一言説明してください。
回答は結論を最初の1〜2行でまとめてから、理由を箇条書きで示してください。
断定できない情報は「推測ですが」と明示してください。
```

### 3. Claudeの設定手順

**学習利用のオプトアウト**

1. 左下のプロフィールアイコン→「設定」→「プライバシー」を開く
2. 「Help improve Claude」というトグルをオフにする
3. オフにすると以後の新しい会話・コーディングセッションはモデルの追加学習に使われなくなり、通常のデータ保持期間も5年から30日に短縮される。2025年8月に予告され同年10月8日から適用された規約変更により、個人向け(Free/Pro/Max)は既定でオン(強制選択式で未回答のユーザーも学習利用ありの5年保持に設定)になっているため、未設定のアカウントは必ず確認する
4. Team・Enterprise・API経由の利用・Claude for Governmentは、個人が何もしなくても既定で学習利用の対象外

**一度きりの相談に使うIncognito(一時チャット)**

1. 新規チャット画面右上のゴースト(幽霊)アイコン、またはショートカット Ctrl+Shift+I(Macは Cmd+Shift+I)でIncognitoモードに入る
2. Incognitoは無料プランを含む全プランで利用でき、チャット履歴・メモリ(記憶)に残らず、モデルの学習にも使われない
3. ただし「アカウントから見えない」だけで「Anthropicから見えない」わけではない点に注意。不正利用検知・安全性審査のため、Incognitoの会話も既定で30日程度は一時的に保持される

**カスタム指示(プロフィール設定)**

1. 左下のプロフィールアイコン(イニシャル)→「設定」→「プロフィール」を開く
2. 「Claudeはあなたの回答にどのような点を考慮すべきですか?」といった欄(Custom Instructions/Preferences)に記入する
3. 目安の上限は1,500文字程度。全チャット共通で適用され、無料プランでも利用できる。案件ごとに変えたい場合は、有料プランのプロジェクト機能内の指示欄を使う

コピペで使える記入例(プロフィール欄に貼る内容):

```
## 私について
- 職種: 経営企画部門の担当者(中堅メーカー)
- 主な業務: 経営会議資料のドラフト作成、業界動向のリサーチ要約
- 前提知識: 財務諸表は読めるが、統計・データサイエンス用語は初心者向けに説明してほしい

## 回答の形式
- 結論を最初の1〜2行でまとめてから詳細を続ける
- 見出しと箇条書きを積極的に使う
- 断定できない場合は「推測ですが」と明示する
- 日本語の丁寧語(です・ます調)で回答する
```

### 4. Microsoft Copilot(個人向け)の設定手順

**学習利用のオプトアウト**

1. copilot.com・Windows版・macOS版: 右上のプロフィールアイコン→プロフィール名→「プライバシー」→「モデルのトレーニング」をオフにする
2. モバイルアプリ: メニュー→プロフィールアイコン→「アカウント」→「プライバシー」→「会話アクティビティのトレーニング」「音声会話のトレーニング」をそれぞれオフにする
3. オプトアウトしても、広告・不正利用対策・セキュリティ・コンプライアンス目的での利用までは除外されない点に注意。会話履歴自体は既定で18か月保持される(個別削除・全削除も可能)
4. Microsoft 365 Copilot・Microsoft 365 Copilot Chat(法人向け)は、Enterprise Data Protection(企業向けデータ保護)により、プロンプト・応答・参照した社内データがモデルの追加学習に使われない契約になっている(詳細は[Microsoft Copilotの基本](microsoft-copilot-basics.md)を参照)
5. 一度きりの相談には、チャット画面右上のドロップダウンから選べる「Temporary chat」を使う。会話履歴・メモリには残らず、学習にも使われないが、組織側で保持ポリシーが設定されている法人向け利用の場合はコンプライアンス目的でバックエンドに記録が残る場合がある

**カスタム指示・パーソナライズ**

1. プロフィールアイコン→プロフィール名→「メモリ」→「パーソナライズと記憶」を開く
2. 「カスタム指示」で自分についての情報や回答スタイルを記入する。学習利用をオフにしたままでもパーソナライズ機能自体は使える(会話の記憶を使った応答の個別最適化と、モデル訓練への利用は別物)
3. Microsoft 365 Copilot(法人向け)では、Copilotアプリ右上「Copilot chats and more」→「設定」→左側メニューの「パーソナライゼーション」から「カスタム指示」「作業プロファイル(Work profile)」を設定する。作業プロファイルは組織のプロフィール情報からCopilotが何を参照しているかを確認・調整する機能

## 注意点・よくある誤解

- **「学習利用オフ」と「会話履歴を残さない」は別物**: Gemini・Claude・Copilotいずれも、学習利用をオフにしても、不正利用監視・法令対応・サービス提供のための保持は別枠で行われる(Copilotは既定18か月、Geminiは一時的に約72時間、Claudeはオプトアウト後30日)
- **Claudeの学習利用オプトアウトには2026年7月7日から「安全レビューの例外」がある**: Anthropicが2026年6月8日に公表し同年7月7日発効の改定プライバシーポリシーにより、オプトアウトしていても「安全性レビューにフラグが立った会話」は学習・分類スコア算出に利用され得る。何が「フラグ」の対象になるかは公開されておらず、ユーザーへの個別通知もない。オプトアウト設定を過信せず、機密情報を書き込まないという前提は変わらない
- **Geminiの「アクティビティをオフ」は地域によって既定値が異なる**: EEA(欧州経済領域)・英国・スイスの個人アカウントは既定が異なる扱いになっており、パーソナルコンテキスト機能自体が提供されていない。海外拠点のメンバーがいる場合、同じ手順が通用しない可能性がある
- **Geminiの学習利用オプトアウトは「テキストだけ」ではなくなった**: 2025年9月の「アクティビティを保存(Keep Activity)」への改称に合わせて、学習に使われうる対象がチャット本文だけでなく、アップロードしたファイル・写真・画面共有の一部にも広がっている。以前に確認したときの理解のまま止まっている担当者には、この対象範囲の変更を周知する必要がある
- **「Copilot」という名前だけで判断しない**: Microsoft社内には無料の個人向けCopilot、Microsoft 365 Copilot(法人向け)、GitHub Copilot(開発者向け)という別物の製品が同名で存在し、学習利用の既定値もそれぞれ異なる(GitHub Copilot Free/Pro/Pro+は2026年4月24日からコード関連の対話データがデフォルトで学習対象になった)。混同すると誤った説明を社内にしてしまうので、[Microsoft Copilotの基本](microsoft-copilot-basics.md)で製品の切り分けを確認してから設定を案内する
- **法人向けプランでも個人アカウントの併用には無力**: 会社がGoogle Workspace with Gemini・Claude for Work・Microsoft 365 Copilotを契約していても、従業員が個人アカウントでGemini/Claude/Copilotを使っていれば、その分は個人向けプランの既定(学習利用オン)のまま使われる。社内ルールで個人アカウント利用を制限し、法人契約に一本化することが前提になる
- **画面名称・設定場所は変更されやすい**: 本ページの手順・文言は2026年8月時点の構成に基づく。実際、Geminiは2025年9月に設定名が変わったばかりであり、各社ヘルプセンターへの直接アクセスが環境の制約で一部できなかったため、複数の第三者情報のクロスチェックと検索結果の要約に基づいている。契約・運用前に必ず実際の設定画面で最新の表記を確認すること

## 最初の一歩

今使っているGemini・Claude・Copilotのうち1つを開き、上記の手順で学習利用のオプトアウト設定(アクティビティを保存/Help improve Claude/モデルのトレーニング)が実際にオフになっているかを確認する。

## 関連トピック

- [ChatGPTの初期設定とデータ利用のオプトアウト](chatgpt-initial-setup-and-opt-out.md)
- [ChatGPTの初期設定とカスタム指示の書き方](chatgpt-custom-instructions.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-08-08: Geminiの設定名変更・Claudeの一時チャット・オプトアウト適用日を最新化
- **内容**: Geminiの学習利用オプトアウト設定が2025年9月に「Gemini Appsアクティビティ」から「アクティビティを保存(Keep Activity)」に改称され、対象がアップロードしたファイル・写真にも拡大したことを反映。Claudeの個人向けオプトアウト既定オン化の適用日を「2025年8月予告・同年10月8日適用」に精緻化し、一度きりの相談に使えるGeminiの「一時チャット」・Claudeの「Incognito」・Copilotの「Temporary chat」の名称と挙動を追記した
- **出典**: [Google Blog: Gemini app personalizes responses based on past chats, plus new privacy controls](https://blog.google/products/gemini/temporary-chats-privacy-controls/)、[jetstream.blog: Gemini アプリ アクティビティ「アクティビティを保存」変更展開](https://jetstream.blog/2025/09/08/gemini-app-activity-renamed-to-keep-activity-rollout/)、[Anthropic: Updates to Consumer Terms and Privacy Policy](https://www.anthropic.com/news/updates-to-our-consumer-terms)、[Cape: Claude AI Privacy Policy: Takeaways for Everyday Users](https://www.cape.co/blog/claude-ai-privacy-policy)、[vibecodingacademy.ai: Claude Incognito Mode: Privacy Features and Limits](https://www.vibecodingacademy.ai/blog/claude-incognito-mode)、[office365itpros.com: Copilot's Temporary Chat](https://office365itpros.com/2025/11/14/temporary-chat-copilot/)、[Microsoft Support: Privacy FAQ for Microsoft Copilot](https://support.microsoft.com/en-us/microsoft-copilot/privacy-faq-for-microsoft-copilot)

### 2026-07-07: 初版執筆
- **内容**: Gemini・Claude・Microsoft Copilot(個人向け)の学習利用オプトアウトとカスタム指示の設定場所・既定値を整理し、ChatGPTを含む4ツール横断の比較表、コピペ用のカスタム指示例、Anthropicの2026年7月7日発効の安全レビュー例外条項などの最新動向をまとめた
- **出典**: [Google Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en)、[Google Gemini Apps ヘルプ: カスタム指示でGeminiの回答をカスタマイズする](https://support.google.com/gemini/answer/16598625?hl=ja)、[Google Workspace ヘルプ: Generative AI in Google Workspace Privacy Hub](https://knowledge.workspace.google.com/admin/generative-ai/generative-ai-in-google-workspace-privacy-hub)、[Anthropic Privacy Center: How do I change my model improvement privacy settings?](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings)、[Anthropic Privacy Center: Updates to our Privacy Policy](https://privacy.claude.com/en/articles/10301952-updates-to-our-privacy-policy)、[techcoffeehouse.com: Anthropic Said You Could Opt Out of Claude's Training Data. Its Own Privacy Policy Says Otherwise.](https://techcoffeehouse.com/2026/06/09/claude-training-data-opt-out-carve-out/)、[Claude Help Center: Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features)、[Microsoft Support: Privacy FAQ for Microsoft Copilot](https://support.microsoft.com/en-us/microsoft-copilot/privacy-faq-for-microsoft-copilot)、[Microsoft Support: Microsoft Copilot privacy controls](https://support.microsoft.com/en-us/microsoft-copilot/microsoft-copilot-privacy-controls)、[Microsoft Learn: Enterprise data protection in Microsoft 365 Copilot and Microsoft 365 Copilot Chat](https://learn.microsoft.com/en-us/microsoft-365/copilot/enterprise-data-protection)、[Microsoft Support: Customize how Microsoft 365 Copilot responds to you](https://support.microsoft.com/en-us/microsoft-365-copilot/customize-how-microsoft-365-copilot-responds-to-you)
