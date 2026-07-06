---
title: ChatGPTのメモリ(Memory)機能
part: 3
chapter: 第3章 記憶・文脈の管理
tags: [ChatGPT, メモリ機能, カスタム指示, パーソナライズ]
created: 2026-07-06
updated: 2026-07-06
---

# ChatGPTのメモリ(Memory)機能

## これは何か

メモリ(Memory)とは、ChatGPTが会話の中で得た自分に関する情報(職種、好み、進行中のプロジェクトなど)を自動的に覚えておき、以降の**別の新しいチャットでも**踏まえて答えてくれる機能である。これがないと、新しいチャットを開くたびに「私は営業職で」「関西弁は使わないで」といった自己紹介を毎回やり直すことになる。メモリを使いこなせば、この前置きの手間が減り、回答が自分の状況に沿ったものになっていく。

ただし「メモリ」「チャット履歴」「カスタム指示」は名前も画面も紛らわしいが別物であり、これを混同すると「なぜ前に話したことを覚えていないのか」「なぜ設定した通りに答えないのか」という誤解につながる。決定的な違いは能動性で、カスタム指示は自分で書いて登録する固定の設定、メモリは会話の中でChatGPTが勝手に判断して蓄積する動的な記憶である。本ページはメモリに絞って、仕組み・確認方法・削除方法・業務での使いどころを整理する。

## 仕組み・背景

ChatGPTのパーソナライズ設定には、性質の異なる複数の仕組みが存在する。

| 仕組み | 何を覚えるか | 更新のされ方 |
|---|---|---|
| カスタム指示(Custom Instructions) | 自分で書いた属性・回答スタイルの固定文 | 自分で編集しない限り変わらない |
| メモリ(保存されたメモリ) | 会話の中でChatGPTが「覚えておくと便利」と判断した事実の断片(名前、役職、好み、食事制限など) | 会話のたびに自動で追加・更新される。明示的に「覚えておいて」と頼んだ場合も、話の流れから拾われる場合もある |
| チャット履歴を参照 | 過去の会話全体の文脈・傾向(個々の「メモリ」に切り出されていない情報も含む) | 保存されたメモリと連動してオン/オフされる |

設定画面では「保存されたメモリを参照する」と「チャット履歴を参照する」という2つのトグルが並んでいるが、前者をオフにすると後者も自動的にオフになる(逆に前者をオンにすると後者も自動でオンになる)、という連動関係がある点に注意([OpenAI Help Center](https://help.openai.com/en/articles/11146739-how-does-reference-saved-memories-work))。

2026年時点ではこれに加えて「Dreaming」と呼ばれるバックグラウンド処理が組み込まれている。Dreamingは、ユーザーが操作していない間に過去の会話全体を非同期で読み返し、要点を統合した記憶の状態を作り直す仕組みで、たとえば「7月にシンガポール出張予定」という記憶を、出張が終わった後には「7月にシンガポールに出張した」という過去形に自動更新するといった処理を行う([OpenAI: Dreaming](https://openai.com/index/chatgpt-memory-dreaming/))。覚えた内容そのものは「保存されたメモリ」の一覧として文章化されており、ユーザーはそれを一件ずつ読んで削除できる。つまりメモリはブラックボックスではなく、中身を確認・編集できる「あなたに関するメモ帳」のようなものだと捉えるとよい。

記憶の深さはプランによって差がある。無料プランは直近の会話から短期的な連続性を持たせる軽量版にとどまるのに対し、Plus・Proは長期にわたってユーザー像を理解する本格的なメモリが使え、さらに保存上限に近づくと重要度の低い記憶を自動的に整理する「自動メモリ管理(Automatic Memory Management)」が使える(この管理機能と詳細な一覧編集はWeb版のPlus・Proでのみ利用可能)。Business/Enterprise/Eduのワークスペースでは、個人向けとは別に管理者がワークスペース単位でメモリ機能自体をオン/オフする権限を持ち、オフにした場合はそのワークスペースに属するメンバー全員の保存済みメモリが削除される([Memory FAQ (Business Version) | OpenAI Help Center](https://help.openai.com/en/articles/9295112-memory-faq-business-version))。会社アカウントで「前に話したことを覚えていない」場合は、機能が壊れているのではなく管理者側の設定が原因であることが多い。

さらに、欧州経済領域(EEA)・英国・スイス・ノルウェー・アイスランド・リヒテンシュタインでは、GDPR(EU一般データ保護規則)のデータ最小化原則への対応として、メモリ機能は既定でオフになっており、使いたい場合はユーザー自身が明示的にオンにする必要がある([OpenAI Developer Community](https://community.openai.com/t/so-openai-s-solution-to-the-eu-s-privacy-laws-is-to-lock-us-out-entirely/1230166))。海外拠点のメンバーと同じ設定になっているはずと思い込まないこと。

## 使いどころ・使い分け

| 使う場面 | 向いている仕組み |
|---|---|
| 毎回のチャットで前提として確実に効かせたい固定ルール(口調、フォーマット、絶対条件) | カスタム指示(自分で書くので内容が確定し抜け漏れがない) |
| 会話の流れの中で自然に蓄積してよい、緩やかな個人情報(好み・立場・継続プロジェクトの状況) | メモリ |
| 他人に配布・引き継ぎできるテンプレートとして前提条件を残したい | カスタム指示(社内の他メンバーにコピペで配れる) |
| 特定の案件・資料だけに紐づく前提(その案件のときだけ使う指示や参照ファイル) | プロジェクト機能(個別の指示・ナレッジ) |
| 機密情報を扱う相談、他人と共有する画面で使う一時的な質問 | メモリを使わない「一時チャット(Temporary Chat)」 |

判断の目安はシンプルで、「毎回必ず効かせたい・自分で管理したい」ならカスタム指示に書き、「会話の中で自然に蓄積されればよい細かい話」はメモリに任せる。両者は併用され、回答生成時には両方が加味される([ChatGPTの初期設定とカスタム指示の書き方](chatgpt-custom-instructions.md)も参照)。メモリは「いつ何が保存されるか」を利用者が完全にはコントロールできないため、重要な前提を確実に効かせたい場面ではメモリだけに頼らない方がよい。

一時チャットでは、メモリの参照も新規作成も行われない(既存のメモリの内容が反映されず、その会話内容がメモリに追加されることもない)。ただし有効にしているカスタム指示自体は一時チャットにも適用される点に注意。社外秘の話題や共有端末での利用時はここを使うと安全側に倒せる([一時チャット FAQ | OpenAI Help Center](https://help.openai.com/ja-jp/articles/8914046-temporary-chat-faq))。

## 実務での使い方

### 設定画面の場所(2026年7月時点)

**PC版Web(chatgpt.com)**

1. 画面左下の自分のアカウントアイコン(または名前)をクリック
2. 「設定」を選択
3. 左メニューの「パーソナライズ」を開く
4. 「メモリ」の項目にある「メモリを管理」(Manage memory)をクリックすると、保存されているメモリの一覧が表示される
5. 各メモリの右側の「…」(三点メニュー)から「削除(Delete)」を選ぶと個別削除、検索欄の横の「…」から「すべて削除(Delete all)」を選ぶと一括削除ができる
6. 同じ「パーソナライズ」画面で「保存されたメモリを参照する」のトグルをオフにすると、メモリの参照自体を停止できる(既存の記憶は残ったまま、一時停止する形)

**スマートフォンアプリ**

「設定→パーソナライズ」から同様の項目にアクセスできるが、個別編集や自動メモリ管理などフルの管理機能はPC版Webの方が充実している。

### コピペで使える活用例

チャット欄にそのまま入力して試せる依頼文。

```
これから話す内容を覚えておいてください。
私は中堅メーカーの人事部で採用広報を担当しています。
回答は「ですます調」、専門用語には必ず一言説明を付けてください。
```

```
今後、資料のたたき台を作るときは
「結論→理由→具体例」の順番で書くようにしてください。覚えておいて。
```

```
〇〇プロジェクトの件は先週終了したので、その内容は忘れてください。
```

```
私について何を覚えているか教えてください。
```

明示的に「覚えておいて」と頼む例に加えて、頼まなくても会話の中で自然に語った内容(役職、好み、繰り返し出てくるプロジェクト名など)がメモリに拾われることもある。

### 他ツールとの対応関係

| 概念 | ChatGPT | Claude | Gemini | Microsoft Copilot |
|---|---|---|---|---|
| 自動で蓄積される長期記憶 | メモリ(保存されたメモリ+チャット履歴を参照+Dreamingによる統合) | メモリ(2026年3月に無料プランを含む全プランへ展開) | パーソナルコンテキスト/「Memories」設定(既定でオン) | Microsoft 365 Copilotの「メモリ」(2026年後半に一般提供予定、順次展開中) |
| 確認・管理画面 | 設定→パーソナライズ→メモリを管理 | 設定→Capabilities→「View and edit memory」 | Geminiアプリの設定内「Memories」(gemini.google.com/personal-context、Web版が最も充実) | プロフィールアイコン→設定→メモリ |
| 一時停止・リセット | オフにする(既存メモリは保持)/個別削除・全削除 | Pause memory(一時停止、記憶は保持)/Reset memory(完全削除、取り消し不可) | 個別項目の削除 | 順次整備中(2026年7月時点で機能は発展途上) |
| 記憶を残したくないときの機能 | 一時的なチャット(Temporary Chat) | シークレットモード(incognito) | シークレットモード相当の設定 | プライベートセッション相当の設定(順次整備中) |
| 自分で書く固定指示との関係 | カスタム指示と併用 | Projectsのカスタム指示と併用 | Gemの「カスタム指示」と併用 | エージェントごとの指示と併用 |

Claudeのメモリは2026年3月に無料・Proを含む全ユーザーへ展開され、明示的な指示がなくても好みや進行中の作業を自動記録するようになった([Claude Help Center](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context))。Geminiの保存済み情報は2024年11月にGemini Advanced向けに先行導入された後、無料ユーザーにも展開されている([9to5Google](https://9to5google.com/2024/11/19/gemini-remember-saved-info/))。3社(4ツール)とも「自動で覚える長期記憶」と「自分で書く固定指示」を分けて持つ設計は共通している。

## 注意点・よくある誤解

- **メモリは会話をまたいで“漏れる”前提で使う**: いったんメモリに保存された情報は、その後に開く全く無関係な新規チャットにも自動的に読み込まれる可能性がある。取引先名・未公表の人事情報・具体的な契約金額といった社外秘の内容は、雑談の中でうっかり触れただけでも記憶されてしまうことがあるため、機密情報を含む相談は一時チャットで行う
- **メモリ≠チャット履歴の全文保存**: メモリは会話全部を丸ごと保存しているわけではなく、要点を抜き出した短い記述の集合体。詳細な過去のやり取りそのものを参照したい場合は、該当のチャットを検索する方が確実
- **メモリを消してもチャット自体は消えない、チャットを消してもメモリは自動では消えない**: メモリの削除・オフとチャット履歴の削除は別の操作である。チャットを削除しても、そこから生成されたメモリが残る場合がある([Memory FAQ | OpenAI Help Center](https://help.openai.com/en/articles/8590148-memory-faq))
- **メモリを再度オンにすると、履歴に残っている古い会話から新しいメモリが再生成されることがある**: 一度削除しても「もう二度と思い出さない」という保証にはならない
- **地域によって既定値が異なる**: EEA・英国・スイスなどではGDPR対応のためメモリが既定でオフになっている。海外拠点のメンバーと同じ設定だと思い込まない
- **メモリが古くなると回答がずれる**: 異動・担当変更・方針転換があった後は、古いメモリが前提として残り続け、実態と合わない回答が出ることがある。定期的にメモリ一覧を見直し、不要になった項目は削除する
- **法人プランでは管理者の設定次第で挙動が変わる**: Business/Enterprise/Eduでは管理者がワークスペース単位でメモリを無効化でき、その場合メンバー個人の設定に関わらず記憶が失われる。会社アカウントで挙動が想定と違う場合はIT管理者に有効化状況を確認する

## 最初の一歩

「設定→パーソナライズ→メモリを管理」を開き、これまでに保存されているメモリの一覧に目を通して、業務上の機密情報や実態と合わなくなった項目(古い部署名など)がないか確認し、あれば1つ削除してみる。

## 関連トピック

- [ChatGPTの初期設定とカスタム指示の書き方](chatgpt-custom-instructions.md)
- [ChatGPTの「プロジェクト」機能](chatgpt-projects-feature.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-07-06: 初版執筆
- **内容**: メモリ機能の仕組み(保存されたメモリ/チャット履歴を参照の連動、Dreamingによる記憶の統合)、カスタム指示・プロジェクトとの使い分け、設定画面での確認・削除手順、コピペで使える活用例、Free/Plus/Pro/Business・EnterpriseでのメモリとAutomatic Memory Managementの違い、EEA/英国/スイスでの既定オフ(GDPR対応)、Claude・Gemini・Microsoft Copilotとの対応表、プライバシー上の注意点を整理
- **出典**: [Memory FAQ | OpenAI Help Center](https://help.openai.com/en/articles/8590148-memory-faq), [How does "Reference saved memories" work? | OpenAI Help Center](https://help.openai.com/en/articles/11146739-how-does-reference-saved-memories-work), [Memory FAQ (Business Version) | OpenAI Help Center](https://help.openai.com/en/articles/9295112-memory-faq-business-version), [一時チャット FAQ | OpenAI Help Center](https://help.openai.com/ja-jp/articles/8914046-temporary-chat-faq), [OpenAI: Memory and new controls for ChatGPT](https://openai.com/index/memory-and-new-controls-for-chatgpt/), [OpenAI: Dreaming - Better memory for a more helpful ChatGPT](https://openai.com/index/chatgpt-memory-dreaming/), [OpenAI Developer Community: So OpenAI's solution to the EU's privacy laws is... to lock us out entirely?](https://community.openai.com/t/so-openai-s-solution-to-the-eu-s-privacy-laws-is-to-lock-us-out-entirely/1230166), [Use Claude's chat search and memory to build on previous context | Claude Help Center](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context), [You can now ask Gemini to remember your preferences with memory feature | 9to5Google](https://9to5google.com/2024/11/19/gemini-remember-saved-info/), [Gemini launches new personalisation features in the UK | Google](https://blog.google/company-news/inside-google/around-the-globe/google-europe/united-kingdom/gemini-launches-new-personalisation-features-in-the-uk/), [Introducing Copilot Memory | Microsoft Community Hub](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-copilot-memory-a-more-productive-and-personalized-ai-for-the-way-you/4432059)
