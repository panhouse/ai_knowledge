---
title: ChatGPTのプラン比較
part: 3
chapter: 第1章 プラン・モデルの選び方
tags: [ChatGPT, 料金プラン, Plus, Pro, Business, Enterprise]
created: 2026-07-04
updated: 2026-09-04
---

# ChatGPTのプラン比較

## これは何か

ChatGPTには無料版から法人向けEnterpriseまで複数のプランがあり、使えるモデルや機能の上限が大きく異なる。「とりあえずPlusにしておけばよい」と考えて契約すると、業務利用に必要なガバナンス機能(データの学習利用オプトアウトやSSO)が個人向けプランには無いことに後から気づくことがある。自分・自社の使い方に見合ったプランを選ぶための整理をしておく。

## 仕組み・背景

2026年9月時点のChatGPTのプラン体系は、大きく個人向けと法人向けに分かれる。2026年7月9日に最新モデル世代「GPT-5.6」(愛称Sol/Terra/Luna)が投入され、2026年8月6日にOpenAIがFree・Go向けの提供内容を大きく引き上げ、さらに2026年8月10日にBusinessの座席(シート)を「Standard」「Premium」の2種類に分ける改定が発表された(一般提供は8月25日)。短期間に複数回の改定が続いており、「どのプランでどのモデルが、どれだけ使えるか」だけでなく「同じBusinessでも座席の種類でどれだけ使えるか」まで見る必要が出てきた点に注意する。

**個人向け**

| プラン | 月額の目安 | 使えるモデルの目安 | 位置づけ |
|---|---|---|---|
| Free | 無料 | GPT-5.6 Luna(性能帯としては最軽量)がデフォルト。2026年8月6日の週から、テキストチャットは回数無制限に(画像生成・ファイル添付など一部機能には引き続き上限あり) | お試し利用の域を超え、日常的なテキスト対話であれば無料でも実質使い放題になった。米国で先行導入された広告表示は、2026年6月19日から日本でも導入されている。難しい質問向けの推論モード「Think」ボタンも追加された |
| Go | 月額$8程度(日本では月額1,400円前後。2026年1月に日本を含む170カ国以上に展開) | Freeと同じくGPT-5.6 Lunaがデフォルトで、テキストチャットは無制限 | Freeより高い画像生成回数・音声モード時間・ファイル添付上限が欲しいが、Plus以上の高度機能までは不要な個人向け。広告表示の対象にもなり得る |
| Plus | 月額$20(日本では月額3,000円程度) | GPT-5.6 Sol(性能帯としては最上位。2026年8月に日常会話向けにチューニングし直された版に更新)。中程度の推論強度〈effort〉まで選択可能 | 業務でAIを日常的に使うビジネスパーソンの標準的な選択肢。最上位モデルSolに最初にアクセスできる個人向けプラン |
| Pro | 月額$100/$200の2段階(2026年4月に$100の下位ティアを新設。日本では$100ティアが月額16,800円程度) | GPT-5.6 Solに加え、$200ティアではより高い推論強度まで利用可能。$100ティアは主にCodex(コーディングエージェント)利用量をPlusの5倍確保する位置づけで、モデル自体は$200ティアと同じ | コーディングや大量利用など、Plusの上限を頻繁に超えるヘビーユーザー向け |

**法人向け**

| プラン | 月額の目安 | 使えるモデルの目安 | 位置づけ |
|---|---|---|---|
| Business(旧Team) | **Standard**座席: 1ユーザーあたり年払い$20/月払い$25程度(2026年4月に値下げ、最少2ユーザーから)。**Premium**座席(2026年8月25日〜新設): 1ユーザーあたり年払い$100/月払い$125程度 | GPT-5.6 Sol利用可能。Premium座席はStandardの5倍相当の利用枠で、高度な機能に付く「5時間ごとの利用上限」が撤廃される | 数名〜中規模チーム向け。データの学習非利用がデフォルト、SAML SSOに対応。2026年8月6日以降、含まれる利用量を超えた分はワークスペースの「クレジットプール」からの従量課金(フレキシブルプライシング)に切り替わる。同じワークスペース内でStandard/Premiumの座席を混在させ、ヘビーユーザーだけPremiumを割り当てるといった使い方ができる |
| Enterprise | 非公開・要問い合わせ。2026年の複数の第三者調査では1ユーザー月$45〜75程度(平均$60前後)、最少150ユーザー・年間契約が相場とされ、年間契約の下限は概算$108,000程度 | GPT-5.6 Solに加え、Pro同様の高い推論強度にも対応 | 大規模組織向け。SSO+SCIMによる自動プロビジョニング、データレジデンシー(データ保存地域の指定)など高度なガバナンス機能 |

なお「Team」プランは2025年8月に「Business」へ名称変更されており、古い記事や社内資料で「Team」と書かれている場合は現在のBusinessを指す。また「GPT-5.6」は数字がモデル世代、Sol/Terra/Luna が性能帯(Solが最上位、Terra・Lunaはより軽量・安価)を表す新しい命名方式で、ChatGPT上ではプラン・選択した推論強度によって実際に呼び出されるモデルが変わる。2026年8月6日の改定までは「最新世代モデルはPlus以上でしか使えない」状態だったが、改定後はFree・GoでもGPT-5.6系(Luna)に切り替わっており、この対応関係は今後も変わり得る。

## 使いどころ・使い分け

| 利用者像 | 向いているプラン |
|---|---|
| とりあえず試したい個人 | Free |
| 個人利用でPlusほどの機能は不要 | Go |
| 業務でAIを日常的に使う個人、最新モデル世代をいち早く使いたい | Plus |
| コーディングなどでPlusの上限を頻繁に超える、より高い推論強度を使いたい | Pro |
| 数名〜中規模チームで、データ非学習・SSOなど最低限のガバナンスが必要 | Business(Standard座席) |
| Business契約の中でも、コーディングや大量出力で5時間上限に頻繁に当たるヘビーユーザーが一部いる | 該当メンバーだけBusinessのPremium座席に切り替える |
| 大規模組織で、SCIM・RBAC・データレジデンシーなど高度な要件がある | Enterprise |

Deep Research(高度な調査レポート機能)や、複数手順にまたがる作業を任せる「ChatGPT Work」(後述)など一部の高度機能は上位プランほど利用回数の上限が緩和される設計になっている。個人利用でも、これらの機能を頻繁に使うならPro、たまにしか使わないならPlusで十分というのが基本的な判断軸になる。

## 実務での使い方

### 機能面の違い(2026年9月時点)

- **Deep Research**: Plusは「フル版」月10回+「軽量版」月15回(合計25回程度)、Proは月250回程度(フル版・軽量版でほぼ折半)が目安。Business・Enterpriseも概ねPlus以上の水準。上限に達すると軽量版に自動切替される。正確な回数は変動するため契約前に公式ページで確認する
- **Canvas・Projects・Tasks**: Plus以上に標準搭載
- **画像・音声・動画生成**: Plus以上で利用可能
- **ChatGPT Work(2026年7月9日〜)**: ゴールを伝えるだけで資料・スプレッドシート・スライド・簡易サイトなどの「完成品」まで仕上げる自律型エージェント。従来の「エージェントモード」やコーディング特化のCodexを統合する新しい仕組みで、長時間かかる作業を裏側で分割・実行し、途中経過の確認や方針変更もできる。Slack・Gmail・Google Drive・カレンダー・CRM・SharePoint・GitHubなど60以上の連携先(コネクタ)と組み合わせて使う。当初はPro・Business・Enterprise・Edu向けの先行公開だったが、現在はFree・Goを含む全プランで利用可能になった。ただしFree・Goでは軽量モデルTerraのみでの動作となり、Sol/Terra/Lunaを選べて利用量も多いPlus以上との差は残る
- **カスタム指示の文字数上限**: 2026年7月15日にPro・Business・Enterprise・Eduで1,500字から5,000字に拡張(Free・Goは対象外)

### 法人プラン特有の機能

- **Business**: 管理コンソールでのワークスペース管理・一括請求、SAML SSOのセルフサーブ設定、デフォルトでビジネスデータをモデル学習に利用しない設定、SOC 2 Type IIなど各種認証取得済み。2026年8月25日からは管理コンソールの「メンバー」画面で座席の種類(Standard/Premium)をユーザーごとに選べるようになり、混在運用も可能
- **Enterprise**: SSO+SCIMによる自動プロビジョニング、役割ベースアクセス制御(RBAC)、データレジデンシー(日本を含む複数リージョンから保存場所を指定可能)、ワークスペース単位の利用分析

## 注意点・よくある誤解

- **「Team」という名前のプランは現在存在しない**: 2025年8月にBusinessへ名称変更されている。過去の記事や資料の「Team」は現在のBusinessと読み替える。
- **モデル名・料金・利用回数の上限は非常に頻繁に変わる**: 2026年だけでもPro $100ティアの新設(4月)、Businessの値下げ(4月)、GPT-5.6世代への切り替え(7月)、Free・Goのテキストチャット無制限化(8月)、BusinessへのPremium座席追加(8月)と、短期間に複数回の改定が続いている。本ページの数値はあくまで執筆時点の目安であり、契約前に必ず[ChatGPT公式の料金ページ](https://chatgpt.com/pricing)で最新情報を確認すること。
- **「Business=1料金」ではなくなった**: 2026年8月25日から、Businessは1ユーザーあたり年払い$20/月払い$25程度の「Standard座席」と、その5倍の利用枠を持つ年払い$100/月払い$125程度の「Premium座席」の2種類から選ぶ形になった。契約全体を一律でPremiumにする必要はなく、同じワークスペース内で座席の種類を人によって使い分けられる。導入済みの会社では、まず現行のStandard座席で誰が利用上限に頻繁に当たっているかを確認し、対象者だけPremiumへ切り替えるのがコスト効率のよい進め方になる。
- **「無料プランは制限だらけ」という前提は8月の改定で崩れた**: 2026年7月時点ではFree・Goは旧世代(GPT-5.5系)に据え置かれていたが、8月6日の改定でGPT-5.6 Lunaに切り替わり、テキストチャットも無制限になった。ただし画像生成・ファイル添付・音声モードなど「テキスト以外」の機能には引き続き上限があり、最上位モデルSolや高い推論強度を使えるのはPlus以上のままである点は変わっていない。プラン間の差の中身は「使えるかどうか」から「どのモデル・どれだけの量を使えるか」に移りつつあるため、最新の対応表を都度確認する。
- **Enterpriseの価格は非公開**: 個別見積もりのため、ネット上に出回る金額情報(第三者による推計)は正確とは限らない。導入検討時は必ず営業窓口に問い合わせる。
- **個人向けプランと法人向けプランはガバナンス機能が別物**: PlusやProにはSSOやデータレジデンシーの指定機能がない。会社の情報を扱うならBusiness以上への移行を検討する。
- **Businessは「定額+従量課金」の要素が加わった**: 2026年8月6日以降、Businessの標準的な利用量を超えた分(高度な機能の多用など)はワークスペースのクレジットプールからの従量課金になる。座席料金だけで青天井に使い放題ではない点に注意し、利用量が多い組織は想定コストを事前に確認する。
- **広告表示の対象地域は拡大中**: Free・Go向けの広告表示は2026年6月19日から日本でも導入されている。広告を避けたい場合はPlus以上の有料プランを検討する。

## 最初の一歩

自分が使っているプランの設定画面で、現在の利用回数上限(Deep Researchの回数など)と、使えるモデルがGPT-5.6のどの性能帯(Luna/Terra/Sol)かを一度確認し、業務での利用頻度と見合っているかをチェックしてみる。

## 関連トピック

- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-09-04: Businessの座席がStandard/Premiumの2種類に分かれた点を反映
- **内容**: 2026年8月10日にOpenAIが発表し8月25日に一般提供が始まった「ChatGPT Business Premium seats」を追記。Businessは従来のStandard座席(年払い$20/月払い$25)に加え、5倍の利用枠と高度機能の5時間上限撤廃を特徴とするPremium座席(年払い$100/月払い$125)を選べるようになり、同一ワークスペース内での混在運用も可能になった。法人向け比較表・使いどころの表・法人プラン特有の機能・注意点の各セクションを更新。GPT-5.6(Sol/Terra/Luna)世代やFree/Go/Plus/Proの料金・仕様に変更は確認されず、既存記述を維持した
- **出典**: [OpenAI公式: Premium seats are coming to ChatGPT Business](https://openai.com/index/premium-seats-chatgpt-business/)、[TechTimes: ChatGPT Business Adds $125 Premium Seat for Power Users Hitting Five-Hour Cap](https://www.techtimes.com/articles/323905/20260811/chatgpt-business-adds-125-premium-seat-power-users-hitting-five-hour-cap.htm)、[PYMNTS: OpenAI Courts Business Users With Premium ChatGPT](https://www.pymnts.com/news/artificial-intelligence/2026/openai-courts-business-users-with-premium-chatgpt/)、[note(高梨洋平): ChatGPT Businessに「プレミアムシート」が登場](https://note.com/takanashi_ai/n/n8a5ff61aa407)、[AIの学校 AI Crew: ChatGPT Businessプレミアムシートとは](https://www.ai-crew-school.jp/blog/chatgpt-business-premium-seats/)
- **注記**: OpenAI公式ヘルプページ(help.openai.com)・料金ページ(chatgpt.com/pricing)には直接アクセスできず、公式ブログ記事と複数の第三者媒体(英語・日本語)のクロスチェックに基づく。正確な最新値は[公式料金ページ](https://chatgpt.com/pricing)で要確認

### 2026-08-16: Free・Goの無制限化、ChatGPT Workの全プラン展開、Enterprise価格帯の精緻化を反映
- **内容**: 2026年8月6日の改定でFree・GoがGPT-5.6 Lunaに切り替わりテキストチャットが無制限になった点(画像・ファイル等の上限は継続)、ChatGPT Workが当初のPro/Business/Enterprise/Edu先行公開からFree・Goを含む全プランへ展開された点(Free・Goは軽量モデルTerraのみ)、Businessが2026年8月6日以降クレジットプールからの従量課金(フレキシブルプライシング)に移行した点、Enterprise料金を「$40〜60程度」から「$45〜75(平均$60前後)・最少150ユーザー・年間契約下限約$108,000」に精緻化、Deep Researchの回数をPlus(フル10回+軽量15回)・Pro(月250回程度)の具体値に更新、カスタム指示の文字数上限拡張(Pro/Business/Enterprise/Edu、1,500→5,000字)を追記
- **出典**: [TechCrunch: ChatGPT brings unlimited text chats to free users](https://techcrunch.com/2026/08/06/openai-brings-unlimited-chatgpt-text-chats-to-free-users/)、[MacRumors: Free ChatGPT Users Get Unlimited Text Chats and GPT-5.6 Luna](https://www.macrumors.com/2026/08/06/chatgpt-free-unlimited-text-chats/)、[窓の杜: 無料版「ChatGPT」にも「GPT-5.6 Luna」が開放、テキストチャットは無制限へ](https://forest.watch.impress.co.jp/docs/news/2131367.html)、[Impress Watch: ChatGPT、日本で広告表示開始](https://www.watch.impress.co.jp/docs/news/2118443.html)、[Coworker AI: ChatGPT Enterprise Pricing in 2026](https://coworker.ai/blog/chatgpt-enterprise-pricing)、[cryptobriefing: OpenAI raises ChatGPT custom instructions limit to 5,000 characters](https://cryptobriefing.com/openai-chatgpt-custom-instructions-5000-characters/)
- **注記**: Deep ResearchやEnterprise料金の数値は公式ヘルプページへの直接アクセスができず、複数の第三者情報のクロスチェックに基づく目安。正確な最新値は[公式料金ページ](https://chatgpt.com/pricing)で要確認

### 2026-07-19: モデル世代交代(GPT-5.6)とChatGPT Work、日本での広告展開を反映
- **内容**: 2026年7月9日のGPT-5.6(Sol/Terra/Luna)投入に伴うプラン別モデル対応表の更新(Free/GoはGPT-5.5系に据え置き、Plus以上がGPT-5.6 Solに対応)、新エージェント「ChatGPT Work」の追加、広告表示が日本でも試験導入されたことを反映
- **出典**: [OpenAI公式: GPT-5.6](https://openai.com/index/gpt-5-6/)、[OpenAI公式: Previewing GPT-5.6 Sol](https://openai.com/index/previewing-gpt-5-6-sol/)、[OpenAI公式: ChatGPT Work](https://openai.com/chatgpt-work/)、[The Japan Times: OpenAI to introduce ads to ChatGPT in Japan](https://www.japantimes.co.jp/business/2026/06/19/companies/openai-chatgpt-advertisements/)
- **注記**: Deep Researchの月間回数や日本円建ての料金は媒体により表記の揺れがあり、複数の第三者情報のクロスチェックに基づく目安。正確な最新値は[公式料金ページ](https://chatgpt.com/pricing)で要確認

### 2026-07-04: 初版執筆
- **内容**: ChatGPTの個人向け(Free/Go/Plus/Pro)・法人向け(Business/Enterprise)プランの料金・機能差、利用者像ごとの選び方を整理
- **出典**: [OpenAI公式ブログ: Introducing ChatGPT Go](https://openai.com/index/introducing-chatgpt-go/)、[OpenAI公式ブログ: Introducing GPT-5.5](https://openai.com/index/introducing-gpt-5-5/)、[TechCrunch: ChatGPT finally offers $100/month Pro plan](https://techcrunch.com/2026/04/09/chatgpt-pro-plan-100-month-codex/)、[MacRumors: ChatGPT Now Has Ads](https://www.macrumors.com/2026/02/09/chatgpt-now-has-ads/)
- **注記**: OpenAI公式ヘルプページへの直接アクセスができなかったため、一部の利用回数上限などの数値は複数の第三者情報のクロスチェックに基づく目安。正確な最新値は[公式料金ページ](https://chatgpt.com/pricing)で要確認
