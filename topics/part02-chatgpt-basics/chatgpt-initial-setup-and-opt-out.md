---
title: ChatGPTの初期設定とデータ利用(学習)オプトアウト
part: 2
chapter: 第2章 基本操作
tags: [ChatGPT基礎, 初期設定, プライバシー]
created: 2026-07-05
updated: 2026-07-05
---

# ChatGPTの初期設定とデータ利用(学習)オプトアウト

## これは何か

ChatGPTは会員登録すればすぐ使い始められるが、業務利用の前に必ず確認すべき設定が2つある。1つは自分の答え方の好みを毎回入力し直さずに済む「パーソナライズ設定」、もう1つは自分が入力した内容(プロンプトや添付ファイル)がOpenAIのモデル学習に使われるのを防ぐ「データ利用オプトアウト」だ。特に後者は、個人向け(Free/Plus/Pro)と法人向け(Business/Enterprise)でデフォルトの挙動が逆になっているため、初期設定を確認しないまま機密情報を入力すると、意図せずモデル学習用データとして使われてしまうリスクがある。

## 仕組み・背景

ChatGPTは既定で、ユーザーが入力した会話(プロンプト・アップロードした画像やファイルへの応答)を「モデルの改善」に使うかどうかを選べる仕組みを持っている。この設定はOpenAIのヘルプセンターでは「Data controls(データ管理)」と呼ばれ、中でも学習利用の可否を切り替えるトグルが「Improve the model for everyone(モデルの改善に協力する)」だ。

このトグルがONだと、新しい会話がモデルの学習データとして使われる可能性がある。OFFにすると、それ以降に始めた新しい会話は学習に使われなくなる。ただし、OFFにした時点で過去の会話が学習データから遡って取り除かれるわけではない点に注意([OpenAI公式: Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq))。

デフォルトの挙動はプランによって正反対になっている。

- **個人向け(Free・Go・Plus・Pro)**: デフォルトで学習利用がON。自分でオプトアウトしない限り、入力内容がモデル改善に使われる可能性がある
- **法人向け(Business・Enterprise・Edu、およびAPI)**: デフォルトで学習利用がOFF。ワークスペースのデータは既定で学習に使われず、追加の設定操作は不要([OpenAI公式: Business data privacy](https://openai.com/business-data/))

つまり「Businessに切り替えれば自動的に安全になる」が正しく、「個人向けプランは自分で毎回オプトアウトを確認する必要がある」というのが実務上の理解になる。

## 使いどころ・使い分け

| 状況 | 推奨プラン・設定 |
|---|---|
| 個人の学習・雑務など、機密情報を入力しない | Free/Plus のままでよい。学習利用ONでも実害は小さい |
| 個人事業主や副業で顧客情報・契約内容など機密を扱う | Plus/ProでData Controlsを必ずオプトアウトに設定 |
| 数名〜中規模チームで会社の情報(議事録、社内資料、顧客データ)を扱う | Businessに移行(デフォルトで学習利用OFF、SSOも利用可) |
| 大規模組織で、部署ごとにデータ保存地域や監査ログの要件がある | Enterpriseを検討(データレジデンシー、SCIM、RBACに対応) |
| とにかく今すぐ個人プランで機密情報を1回だけ扱いたい | 「一時チャット(Temporary Chat)」を使う。履歴に残らず学習にも使われない |

判断基準はシンプルで、「その会話に会社名・顧客名・未公開の数値・個人情報が含まれるか」で分ける。含まれるなら、個人向けプランではオプトアウト設定を確認するか、法人向けプランへの移行を検討する。

## 実務での使い方

### 1. 最初にやるべき初期設定(共通)

1. [chat.openai.com](https://chatgpt.com) または ChatGPTアプリでログイン
2. 画面右上(PC版)または左下(旧レイアウト)の**アカウントアイコン**をクリック
3. 「**設定**」→「**パーソナライズ**」を開く
4. 「**カスタム指示**」に、回答してほしいスタイル・注意事項を記入する。例:

   ```
   ## 私について
   食品メーカーのマーケティング部で働いています。BtoB向けの提案資料作成が主な業務です。

   ## 回答のスタイル
   - 結論を先に、その後に理由を箇条書きで
   - 断定できない場合は「要確認」と明示する
   - 社内文書のトーンに合わせて、絵文字は使わない
   ```

5. 自動保存されるので「×」で閉じる。**設定は新しく開いたチャットから反映される**(既存チャットには遡って反映されない)ので、設定後は必ず新規チャットで確認する

法人向け(Business/Enterprise)を契約している場合は、管理者が事前にワークスペースを作成し、メンバーをメールまたはCSVインポートで招待する。招待を受けたら、届いたメールのリンクからワークスペースに参加する。ワークスペース内の設定は、チャット画面左下のワークスペース名をクリック→「Workspace settings」から管理者が一元管理する([OpenAI公式: Managing your ChatGPT Business workspace](https://help.openai.com/ja-jp/articles/8798577-how-to-manage-your-chatgpt-business-workspace))。

### 2. データ利用(学習)オプトアウトの設定手順

**個人向け(Free/Plus/Pro)の場合**

1. アカウントアイコン→「**設定**」→「**データ管理(Data controls)**」を開く
2. 「**Improve the model for everyone(モデルの改善に協力する)**」のトグルをOFFにする
3. OFFにした時点より後に開始した会話が学習対象から除外される(既存の会話は遡って除外されない)

同じ画面から、次の関連設定も確認しておくとよい。

- **Temporary chat(一時チャット)**: 新規チャット画面で有効にすると、その会話は履歴に残らず、学習にも使われない。1回限りの機密情報の入力に向く
- **Delete chat history / Delete all chats**: 保存済みの会話をまとめて削除する

**法人向け(Business/Enterprise)の場合**

- ワークスペース全体でデフォルトが「学習利用OFF」のため、メンバー個人が上記トグルを操作する必要は基本的にない
- Business/Enterpriseでは、管理者が「Workspace settings」の中でメンバーによる会話共有(GPTsの共有範囲など)を制御できるが、学習利用自体はワークスペース単位で既定OFFに固定されている([OpenAI公式: Enterprise privacy at OpenAI](https://openai.com/enterprise-privacy/))
- 個人のFree/Plusアカウントを業務用に併用している社員がいる場合、そのアカウントは個人向けの既定(学習利用ON)のままなので、会社として利用ルールを明示し、Business/Enterpriseへの一本化を進めるのが望ましい

### 3. ツール横断の対応付け(学習オプトアウト設定の場所)

| ツール | 学習オプトアウトの名称 | 設定場所 | 法人向けプランのデフォルト |
|---|---|---|---|
| ChatGPT | Improve the model for everyone | 設定→データ管理(Data controls) | Business/Enterpriseは既定でOFF(オプトアウト不要) |
| Google Gemini | Gemini Apps Activity(アクティビティの保存) | Gemini Apps アクティビティ管理ページ(Googleアカウントの「マイアクティビティ」経由) | Google Workspace版はエンドユーザーライセンス契約上、原則学習に利用されない |
| Claude(Anthropic) | Improve Claude for everyone(モデル改善への協力) | Claude.ai→設定→プライバシー | Team/Enterpriseは既定でOFF(オプトアウト不要) |
| Microsoft Copilot | 会話アクティビティのトレーニング / Enterprise Data Protection(EDP) | 個人向け: copilot.com→プロフィール→プライバシー。法人向け: Entra IDでサインインすると自動的にEDPが適用され追加設定不要 | Microsoft 365 Copilot(Entra ID利用)は既定で学習利用なし |

共通する構図は「個人向け無料/単体プランは既定でON(要オプトアウト操作)、法人向け・組織向けは既定でOFF(操作不要)」という点で、ChatGPT・Claude・Copilotで揃っている。Geminiは仕組みがやや異なり、「アクティビティの保存」自体をOFFにしないと学習対象から外れないため、他社より一手間多い。

## 注意点・よくある誤解

- **オプトアウトしても即座にデータが消えるわけではない**: OpenAIは不正利用の監視や法令対応のため、オプトアウト後も最大30日程度はサーバー上にデータを保持する。「オプトアウト=即時完全削除」ではない([OpenAI公式: Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq))
- **オプトアウトは遡及しない**: トグルをOFFにしても、それ以前の会話が学習データから取り除かれるわけではない。契約直後にまずオプトアウトしておくことが重要
- **「履歴を残す」と「学習に使わせない」は別の設定**: 履歴(チャット履歴)をONのままでも学習利用だけをOFFにできる。逆に履歴を完全に消したい場合は「一時チャット」または個別の会話削除を使う
- **無料プランは地域によって選択肢が制限される場合がある**: EU/EEA地域ではAI Act対応のためMemory機能などが一部制限されており、個人向けプランの設定項目の見え方が地域で異なることがある。会社として利用する場合は、契約プランのヘルプページで自社の地域における最新の挙動を確認する
- **社員が個人向けの無料/Plusアカウントを業務に使ってしまうケースに注意**: 会社としてBusiness/Enterpriseを契約していても、社員が個人アカウントで同じ作業をしてしまうと学習利用ONのまま機密情報を入力するリスクが残る。利用ルールの周知とアカウントの統一が重要
- **オプトアウトはセキュリティ対策の一部にすぎない**: 学習利用を止めても、OpenAI側のサーバーにデータが保存される点(前述の保持期間)や、入力ミスによる情報漏洩(誤って別の会話に貼り付けるなど)は別途対策が必要。詳細は[生成AI利用における情報漏洩対策](../part03-risk-security/information-leakage-prevention.md)を参照

## 最初の一歩

今すぐ自分のChatGPTの「設定→データ管理」を開き、「Improve the model for everyone」がONになっていないか確認する。ONであれば、業務で機密情報を入力する前にOFFに切り替える。

## 関連トピック

- [ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)
- [生成AI利用における情報漏洩対策](../part03-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: ChatGPTの初期設定(パーソナライズ、ワークスペース参加)手順と、データ利用(学習)オプトアウトの個人向け/法人向けデフォルトの違い、設定手順、Gemini/Claude/Copilotとの対応付けを整理
- **出典**: [OpenAI公式: Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq)、[OpenAI公式: How do I turn off model training](https://help.openai.com/en/articles/8983082-how-do-i-turn-off-model-training-to-stop-openai-training-models-on-my-conversations)、[OpenAI公式: What if I want to keep my history on but disable model training?](https://help.openai.com/en/articles/8983130-what-if-i-want-to-keep-my-history-on-but-disable-model-training)、[OpenAI公式: Business data privacy, security, and compliance](https://openai.com/business-data/)、[OpenAI公式: Enterprise privacy at OpenAI](https://openai.com/enterprise-privacy/)、[OpenAI公式: Managing your ChatGPT Business workspace](https://help.openai.com/ja-jp/articles/8798577-how-to-manage-your-chatgpt-business-workspace)、[Anthropic Privacy Center: How do I change my model improvement privacy settings?](https://privacy.claude.com/en/articles/12109829-how-do-i-change-my-model-improvement-privacy-settings)、[Microsoft Learn: Data, Privacy, and Security for Microsoft 365 Copilot](https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-privacy)、[Microsoft サポート: プライバシー制御のMicrosoft Copilot](https://support.microsoft.com/ja-jp/topic/%E3%83%97%E3%83%A9%E3%82%A4%E3%83%90%E3%82%B7%E3%83%BC%E5%88%B6%E5%BE%A1%E3%81%AEmicrosoft-copilot-8e479f27-6eb6-48c5-8d6a-c134062e2be6)、[Google Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en)
