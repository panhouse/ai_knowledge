---
title: カスタマーサポート職における生成AI活用事例
part: 15
chapter: 第4章 カスタマーサポート・カスタマーサクセス
tags: [カスタマーサポート, コールセンター, RAG, チャットボット, エージェントアシスト, ハルシネーション, CRM]
created: 2026-07-06
updated: 2026-08-08
---

# カスタマーサポート職における生成AI活用事例

## これは何か

カスタマーサポート・コールセンター・ヘルプデスクは、問い合わせ対応という「大量・反復・定型」の業務が多く、生成AIの効果が最も出やすい職種の一つとされる。マッキンゼーも生成AIのインパクトが特に大きい領域として「顧客対応」を挙げている。一方で、AIが顧客に直接誤った回答をしてしまうと企業の信用問題に直結するため、どの工程をAIに任せ、どこに人間の確認を残すかの設計が他の職種以上に重要になる。本ページでは、一次対応チャットボットからオペレーター支援、通話要約、感情分析、翻訳、応対品質レビューまで、カスタマーサポート特有の活用場面を具体的なツール名・プロンプト例とともに整理する。

## 仕組み・背景

カスタマーサポートでの生成AI活用は、大きく3つの技術要素の組み合わせで成り立っている。

1. **RAG(検索拡張生成)**: 社内のFAQ・マニュアル・過去の対応履歴を検索し、その内容をもとにAIが回答文を生成する仕組み。自社データにない内容を答えにくくすることで、ハルシネーション(もっともらしい誤情報の生成)のリスクを抑える。詳細は [RAG(検索拡張生成)の基本](../part07-data-analysis/rag-basics.md) を参照。
2. **音声認識・自然言語処理**: 通話をテキスト化し、要約・感情分析・キーワード抽出にかける技術。コールセンターの通話要約や感情分析AIの基盤になっている。
3. **エージェント型AI(AIエージェント)**: 単に回答文を生成するだけでなく、注文状況の照会・返金処理・チケットの起票など、外部システムと連携して手続きまで代行する仕組み。Salesforce Agentforce、Fin(旧Intercom)のFin AI Agentなどがこの方向に進化している。

これらは互いに独立ではなく、「一次対応はAIエージェントが完結」「解決できない場合は人間に引き継ぎ、その際にAIが要約と感情スコアを添えて渡す」という形で連携させるのが2026年時点の主流構成になっている。

もう一つの構造変化として、主要ベンダーの課金モデルが2026年に入って軒並み「アウトカム課金(成果報酬型)」へ移行した点がある。会話数や利用時間ではなく「実際に解決できた件数」に対して課金する方式で、Zendesk・Fin(旧Intercom)・Salesforce Agentforceの3社が2026年に相次いでこの方向に舵を切った。裏を返すと、導入企業にとっては「解決率が低いほど費用対効果が悪化する」という新しいコスト構造になっており、契約前に自社データでの解決率検証が以前にも増して重要になっている。

## 使いどころ・使い分け

代表的な6つの活用場面と、全自動化の可否の目安は以下の通り。

| 活用場面 | 何をするか | 全自動化 vs 人間介在 |
|---|---|---|
| 一次対応チャットボット(RAGベース) | FAQ・マニュアルを検索し、定型的な質問に自動回答 | 定型・低リスクな質問(営業時間、送料、パスワード再発行など)は全自動化しやすい。返金・解約・契約変更など個別事情が絡む質問は人間に引き継ぐ設計にする |
| エージェントアシスト(オペレーター支援) | 通話・チャット中にAIが回答候補や関連マニュアルをリアルタイム提示 | 常に人間が最終確認・送信するHuman-in-the-Loop(人間が最終確認・介在する業務設計)が前提。ただし2026年は「AIが有人のように通話応対する」完全自動化型も登場し始めている |
| 通話・チャット要約とCRM入力 | 対応内容をAIが要約し、CRM(顧客管理システム)の所定項目に自動反映 | 要約の生成は自動化してよいが、公式記録として使う前に軽く目視確認するのが望ましい |
| 感情分析・エスカレーション判定 | 音声・テキストから怒り・不満などの感情スコアを算出し、悪化時に上長へアラート | 判定はAI、対応判断とエスカレーション実行は人間 |
| 多言語対応の下書き | 問い合わせ内容を翻訳し、多言語での返信文をAIが下書き | 下書きは自動化、送信前の最終確認は人間(特に規約・法律に関わる内容) |
| 応対品質レビュー・コーチング支援 | 過去の通話・チャットログをAIが評価し、改善点をフィードバック | 評価はAI支援、人事評価への反映は人間が行う |

判断の軸はシンプルで、「間違えたときの被害が『言い直せば済む』レベルか、『返金・解約・法的トラブルに発展する』レベルか」で全自動化の可否を分けるとよい。

## 実務での使い方

### 1. 一次対応チャットボット(RAGでFAQボットを構築する)

自社のFAQ・マニュアルPDFを取り込み、ノーコードでRAGチャットボットを作れるツールとして、国内では [Dify](../part10-nocode-lowcode/dify-rag-implementation.md) のような自前構築プラットフォームや、PKSHA AIヘルプデスク(旧PKSHA Chatbot、ゼロFAQからでも生成AIがFAQ生成を支援する方式が特徴)、カラクリ(KARAKURI)、Helpfeelなどの専業SaaSがある。AWSのオープンソース「Generative AI Use Cases(GenU)」とAmazon Bedrockを組み合わせて社内専用RAGチャットを構築し、問い合わせ対応工数を7割削減した保守業界の事例も報告されている。自治体でも、東京都港区がLINE公式アカウント上で生成AIを活用したチャットボットの本格運用を開始するなど、公共分野への広がりも見られる。

LINE公式アカウントは有料オプション「チャットPro」(月額3,000円・税別)で「AIチャットボット(β)」を提供しており、事前にアップロードしたPDF・画像から生成AIがQ&Aを自動生成し、その中から最適な回答を選んで返信する方式を採る(2026年8月時点もβ版のまま)。自由生成ではなく登録済みQ&Aからの選択方式にすることで、ハルシネーションのリスクを抑えている点が実務上のポイント。

**コピペで使えるRAG回答生成プロンプト例**(Dify・社内GPT等のシステムプロンプトに設定)

```
あなたは〇〇株式会社のカスタマーサポート担当AIです。
以下のルールを厳守して回答してください。

## 回答ルール
- 必ず「参照ドキュメント」に記載されている内容のみを根拠に回答する
- 参照ドキュメントに答えがない場合は、絶対に推測で答えず
  「担当者にお繋ぎしますので少々お待ちください」と回答する
- 返金・解約・契約変更・法律相談に関する質問は、
  金額や可否を断定せず必ず有人対応に引き継ぐ
- 語尾は丁寧語で統一し、絵文字は使わない
- 回答は3文以内で簡潔にまとめる

## 参照ドキュメント
{{FAQ・マニュアルの検索結果がここに挿入される}}

## 顧客からの質問
{{顧客の入力}}
```

### 2. エージェントアシスト(オペレーター支援)・自動応対エージェント

代表的な製品と機能は以下の通り(2026年8月時点)。

| 製品 | 提供元 | 主な機能 | 料金の目安 |
|---|---|---|---|
| Zendesk Copilot / AI agents | Zendesk | Copilotがオペレーター向けに返信案を下書き、関連マクロを提示。AI Agentは関連システム(Shopify、Jira、Slack等)への後続処理も自動実行 | Support Team 19ドル/エージェント/月〜、Suite Team 55ドル/エージェント/月・Suite Professional 115ドル/エージェント/月。旧Advanced AIアドオン(50ドル/月)は2026年5月にSuite/Supportプランへ順次統合されたが、AI Agentの自動解決は解決(Verified Resolution)1件あたり1.2〜1.5ドル程度の従量課金が別途かかる |
| Fin AI Agent | Fin(2026年5月に運営会社がIntercomから改称、プロダクト名は引き続き「Intercom」。同年6月にSalesforceが約36億ドルで買収に合意、クローズは同社2027会計年度第4四半期を予定) | 自社ナレッジベース・ポリシーを学習し、メール・チャット・API・WhatsApp・音声等で自動応対。既存のZendesk・Salesforce・HubSpot等のヘルプデスク上でも単独稼働可能(Fin for platforms) | 解決(Resolution)1件0.99ドル、月最低50件〜(最低月額49.5ドル相当)。Intercom本体契約なしの単独利用でも同一料金体系 |
| Agentforce for Service / Agentforce Help Agent | Salesforce | 生成AIエージェントが定型対応を自動化し、複雑な案件のみ人間に引き継ぐ。2026年6月に発表・同年7月にGAした「Agentforce Help Agent」は音声・Web・ポータル・メッセージングを横断するパッケージ型エージェント | 従来型は会話単位課金(1会話2ドル)またはFlex Credits(アクション単位0.10ドル、10万クレジット500ドル)、ユーザー単位アドオン125ドル/ユーザー/月〜。Help Agentは「解決できた場合のみ1件2ドル」の完全成果報酬型(顧客が有人対応を希望・低評価・離脱した場合は無料) |

Fin AI Agentは「平均67%の会話を解決」と謳われる一方、実際の顧客事例ベースでは解決率42〜50%程度という報告もあり、公称値と実運用値には差があることを踏まえて費用試算をするのが実務上のコツ。なお、Fin(旧Intercom)はSalesforceによる買収合意が2026年6月に発表されたものの2026年8月時点ではクローズ前であり、料金体系自体には変更がない。長期契約を検討する場合は、買収完了後の価格改定・製品統合の可能性を見込んでおくとよい。

日本語コールセンターでは、通話をリアルタイムでテキスト化しFAQ・マニュアルを自動検索する音声認識×生成AIの組み合わせが普及している。アドバンスト・メディアの「AmiVoice Communication Suite」は複数のAIエージェントが同時にオペレーターをリアルタイム支援する機能を追加しており、ベルシステム24ホールディングスはAIが有人オペレーターのように通話応対まで行う「Hybrid Operation Loop(HOL)」を2026年にサービス開始すると発表するなど、支援型から自動応対型への移行も進んでいる。

### 3. 通話・チャット要約とCRM入力

音声認識と生成AIを組み合わせ、通話終了後にAIが自動で要約を作成し、CRMの所定フィールドに転記する仕組みが普及しつつある。これによりACW(After Call Work、通話後の後処理時間)を短縮できる。MiiTel(トーク解析AI)やIVRyなどの国内ツールがこの用途で使われている。

**コピペで使える通話要約→CRM入力プロンプト例**

```
以下は顧客対応の通話ログ(音声認識テキスト)です。
下記のCRM入力フォーマットに沿って要約してください。
記載のない項目は「情報なし」と明記し、推測で埋めないこと。

## CRM入力フォーマット
- 顧客名:
- 問い合わせカテゴリ(製品不具合/請求/解約/その他):
- 要件の要約(3行以内):
- 対応内容:
- 対応結果(解決/未解決/エスカレーション):
- 次のアクション・フォロー予定:
- 顧客の感情トーン(平常/不満/強い不満):

## 通話ログ
{{音声認識テキストがここに入る}}
```

### 4. 感情分析・エスカレーション判定

音声のトーン・話速・言葉遣いから感情スコアを算出し、スコアが一定値を下回るとリアルタイムで管理者にアラートを送る仕組み。通信業界などで、通話中の感情スコア低下を検知して自動的に上長へエスカレーションする運用事例が報告されている。感情分析を導入したコールセンターで顧客満足度が向上したとする調査結果も紹介されている。

### 5. 多言語対応の下書き

インバウンド対応や海外拠点向けサポートでは、AIによる翻訳と返信文の下書き生成が有効。Zendesk・Fin(旧Intercom)など主要SaaSは多言語自動翻訳機能を標準搭載している。

**コピペで使える多言語返信下書きプロンプト例**

```
あなたは〇〇株式会社のカスタマーサポート担当です。
以下の顧客からの問い合わせ(原文言語不明)を読み、
1. 何語で書かれているかを判定
2. 日本語に翻訳した要約
3. 顧客と同じ言語での返信文の下書き(丁寧・簡潔・絵文字なし)
の3点をこの順で出力してください。返信文には、参照FAQにない断定的な
金額・期日は書かないこと。

## 参照FAQ
{{FAQ抜粋}}

## 顧客からの問い合わせ
{{原文}}
```

### 6. 応対品質レビュー・コーチング支援

過去の通話ログやチャットログをAIに読ませ、応対品質のチェックリスト(挨拶・傾聴・提案内容など)に沿ってスコアリングし、改善点をフィードバックさせる使い方。個人の人事評価に直結させる場合は、AIのスコアを一次情報としつつ最終判断は人間が行う運用にするのが無難。

## 注意点・よくある誤解

- **ハルシネーションによる誤回答は「言い直せば済まない」レベルの実害を招く**: Air Canadaのチャットボットが忌引き割引の規定を誤って案内し、裁判所(仲裁機関)が実際に賠償を命じた事例や、DPDのチャットボットがジェイルブレイク(AIに制約を破らせる入力)によって自社を罵倒する発言をしてしまった事例など、顧客対応でのAIの誤回答・逸脱は実際に企業の信用と費用の両面で損害を発生させている。返金額・解約可否・法的な可否など「金額や権利に関わる断定」はRAGでも完全には防げないため、システムプロンプトで明示的に人間へのエスカレーションを指示するのが実務上の防御策になる
- **「回答を根拠に紐づける(グラウンディング)」だけでハルシネーションはゼロにならない**: 回答を検索結果・ナレッジベースに紐づける「ソースグラウンディング型RAG」は、ハルシネーションを何もしない場合と比べて6〜7割程度減らせるとされるが、ゼロにはならない。ナレッジベース自体に重複・矛盾・古い情報が残っていると誤回答の温床になるため、「情報源ごとに担当者・更新頻度・承認プロセスを決めて定期的に棚卸しする」運用まで含めて設計する必要がある
- **「解決率」は公称値と実運用値が乖離しやすい**: ベンダーが提示する解決率は好条件下の数値であることが多く、実際の自社データで検証してから予算化する。2026年は主要ベンダーが軒並み「解決できた分だけ課金」のアウトカム課金へ移行したため、見かけの単価だけでなく「自社データでの想定解決率×単価」で総コストを試算することが以前より重要になっている
- **Q&A方式とフリー生成方式は精度もリスクも異なる**: LINE公式アカウントのAIチャットボットのように、登録済みQ&Aから選択する方式はハルシネーションのリスクが低い一方、想定外の質問には答えられない。自由記述型のRAGチャットボットは柔軟だが、検索対象データの整備(誤字脱字のない一問一答形式にするなど)を怠ると誤回答が増える
- **感情分析・要約の自動化は「記録の代替」であって「判断の代替」ではない**: エスカレーション実行やクレーム対応方針の決定はAIに任せきりにせず、人間が最終判断する設計にする
- **買収・社名変更に伴うベンダーリスクにも注意する**: Intercomは2026年5月にFinへ社名変更し、同年6月にはSalesforceによる買収合意も発表された。長期契約を結ぶ前に、買収・統合が完了した後の価格改定や既存契約の扱いについてベンダーに確認しておくと安心
- **導入して終わりにしない**: 生成AIは対応そのものを効率化しても、問い合わせの根本原因(製品・サービスの分かりにくさ)を解決するわけではない。要約・感情分析のログを商品改善やFAQ改訂にフィードバックする運用まで設計してはじめて投資対効果が出る

## 最初の一歩

自社のFAQページやマニュアルの中から「よくある質問トップ10」を1つのテキストファイルにまとめ、ChatGPTやDifyに読み込ませて、上記のRAG回答生成プロンプト例をそのまま試し、想定通りの回答が返るか・答えられない質問をどう扱うかを確認してみる。

## 関連トピック

- [RAG(検索拡張生成)の基本](../part07-data-analysis/rag-basics.md)
- [ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)
- [生成AIに向く業務・向かない業務の切り分け](../part12-business-practice/ai-task-suitability.md)

## 更新履歴

### 2026-08-08: 主要ベンダーの料金体系・買収動向を最新化
- **内容**: Zendesk(Advanced AIアドオンのSuite/Support統合完了、解決1件1.2〜1.5ドルへの実勢価格更新)、Intercom→Fin社名変更とSalesforceによる約36億ドルでの買収合意(2026年6月)、Salesforce Agentforce Help Agentの成果報酬型新料金(解決できた場合のみ1件2ドル)を反映。日本のコールセンター向けエージェントアシストの最新事例(AmiVoice Communication Suite、ベルシステム24のHybrid Operation Loop)、港区のLINE公式アカウント生成AIチャットボット本格運用、LINEチャットProの料金(月額3,000円)を追記。ハルシネーション対策の節に「ソースグラウンディングでも6〜7割減にとどまる」「アウトカム課金移行に伴うコスト試算の重要性」「ベンダーの買収・社名変更リスク」を追加
- **出典**: [eesel AI: Zendesk AI agents pricing (2026)](https://www.eesel.ai/blog/a-complete-guide-to-zendesk-ai-agents-setup-costs-and-best-practices)、[Voiceflow: Zendesk Pricing 2026](https://www.voiceflow.com/blog/zendesk-pricing)、[Salesforce Ben: Salesforce Acquires Fin (Formerly Intercom)](https://www.salesforceben.com/salesforce-acquires-fin-formerly-intercom-adding-30k-ai-customers/)、[Trending Topics: Salesforce to Acquire Fin.ai for $3.6 Billion](https://www.trendingtopics.eu/salesforce-to-acquire-fin-ai-formerly-intercom-for-3-6-billion/)、[getmacha: Intercom Fin AI Agent Pricing (2026)](https://www.getmacha.com/blog/intercom-fin-ai-agent-complete-guide)、[SiliconANGLE: Salesforce launches Help Agent](https://siliconangle.com/2026/06/25/salesforce-launches-help-agent-simplify-ai-customer-service-deployment/)、[Salesforce Ben: Huge Agentforce Pricing Shift](https://www.salesforceben.com/huge-agentforce-pricing-shift-salesforce-introduces-pay-per-resolution/)、[アドバンスト・メディア: AmiVoice Communication Suite 新機能](https://www.advanced-media.co.jp/newsrelease/12140-2/)、[三井情報: コンタクトセンター業務に生成AIは使える?](https://www.mki.co.jp/lp/genesyscloud/blog/generative-ai-for-call-center-agent-assist.html)、[港区: LINE公式アカウントに生成AIを活用したチャットボットの本格運用を開始](https://www.city.minato.tokyo.jp/dejitarukaikakutan/line-chatbot-release.html)、[LINEステップ: LINE公式アカウントの「AIチャットボット(β)」とは](https://linestep.jp/2026/02/07/loa-ai-chatbot/)、[knowmax: Why RAG Is the Fix for AI Hallucinations](https://knowmax.ai/blog/rag-in-customer-service/)、[PKSHA Technology: AGSグループが「PKSHA AI ヘルプデスク」を導入](https://www.pkshatech.com/news/20260203/)

### 2026-07-06: 初版執筆
- **内容**: カスタマーサポート職における生成AI活用を、一次対応チャットボット(RAG)、エージェントアシスト、通話・チャット要約とCRM入力、感情分析・エスカレーション、多言語対応、応対品質レビューの6場面に整理。Zendesk/Intercom(Fin)/Salesforce Agentforceの機能・料金比較表と、Air Canada・DPDのハルシネーション事例を含む注意点、コピペ用プロンプト3種を記載
- **出典**: [DevelopersIO: Zendesk AIエージェント機能アップデート](https://dev.classmethod.jp/articles/zendesk-update-202405-ai-agent/)、[eesel AI: Zendesk AI agents setup, costs, and best practices (2026)](https://www.eesel.ai/blog/a-complete-guide-to-zendesk-ai-agents-setup-costs-and-best-practices)、[Gleap: Intercom Fin AI Pricing Explained 2026](https://www.gleap.io/blog/intercom-fin-ai-pricing-2026)、[Intercom Help: Fin AI Agent outcomes](https://www.intercom.com/help/en/articles/8205718-fin-ai-agent-outcomes)、[Salesforce: Agentforce for Serviceの価格](https://www.salesforce.com/jp/service/ai/agentforce-for-service-pricing/)、[eesel AI: Is Salesforce Agentforce worth the cost? (2026)](https://www.eesel.ai/blog/is-salesforce-agentforce-worth-the-cost)、[LINEヤフー: LINE公式アカウントのAIチャットボット(β)](https://www.lycbiz.com/jp/news/line-official-account/20251113/)、[はてなベース: 生成AIがカスタマーサポートを新時代へ導く](https://hatenabase.jp/blog/%E7%94%9F%E6%88%90ai%E3%81%8C%E3%82%AB%E3%82%B9%E3%82%BF%E3%83%9E%E3%83%BC%E3%82%B5%E3%83%9D%E3%83%BC%E3%83%88%E3%82%92%E6%96%B0%E6%99%82%E4%BB%A3%E3%81%B8%E5%B0%8E%E3%81%8F%EF%BC%9A-%E5%9B%BD/)、[StepAI: コールセンターの感情分析とは](https://www.stepai.co.jp/blog/%E3%82%B3%E3%83%BC%E3%83%AB%E3%82%BB%E3%83%B3%E3%82%BF%E3%83%BC%E3%81%AE%E6%84%9F%E6%83%85%E5%88%86%E6%9E%90%E3%81%A8%E3%81%AF%E9%A1%A7%E5%AE%A2%E6%BA%80%E8%B6%B3%E5%BA%A6%E5%90%91%E4%B8%8A%E3%81%A8%E3%82%AA%E3%83%9A%E3%83%AC%E3%83%BC%E3%82%BF%E3%83%BC%E6%94%AF%E6%8F%B4%E3%82%92%E5%AE%9F%E7%8F%BE%E3%81%99%E3%82%8Bai%E9%9F%B3%E5%A3%B0%E6%84%9F%E6%83%85%E8%AA%8D%E8%AD%98%E6%8A%80%E8%A1%93)、[Forbes: What Air Canada Lost In 'Remarkable' Lying AI Chatbot Case](https://www.forbes.com/sites/marisagarcia/2024/02/19/what-air-canada-lost-in-remarkable-lying-ai-chatbot-case/)、[CX Quest: AI Hallucinations in Customer Support](https://cxquest.com/ai-hallucinations-in-customer-support-risks-causes-prevention/)
</content>
