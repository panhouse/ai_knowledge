---
title: 法律事務所・弁護士法人における生成AI活用事例
part: 14
chapter: 第11章 士業・専門サービス
tags: [法律事務所, 弁護士法人, 契約書レビュー, リーガルテック, Harvey, LegalOn, MNTSQ, 弁護士法72条, 生成AI活用事例]
created: 2026-09-15
updated: 2026-09-15
---

# 法律事務所・弁護士法人における生成AI活用事例

## これは何か

本ページで扱うのは、**法律事務所・弁護士法人という「事業体」が組織としてどう生成AIを導入・運用しているか**という事例である。契約書レビューAI・LegalOn/Harveyといった個別ツールの機能自体は[士業・専門サービスにおける生成AI活用事例](professional-services-ai-use-cases.md)で概観済みのため、本ページはその一段深く、①事務所全体としてのAI導入方針・ガバナンス体制の作り方、②大手事務所が自らの専門知見を「プレイブック」としてリーガルテック企業と共同開発・製品化する新しい収益モデル、③訴訟支援・証拠開示(ディスカバリー)・判例調査といった契約書レビュー以外の業務領域、④弁護士法72条(非弁行為の禁止)という業種特有の法的制約、⑤AIが生成した架空の判例引用(ハルシネーション)による懲戒・制裁事例、を整理する事例カタログである。個々の企業の法務担当者がAIをどう使うかは[法務職における生成AI活用事例](../part15-job-role-cases/legal-ai-use-cases.md)に譲り、本ページは「依頼者に法的サービスを提供する側」である法律事務所・弁護士法人の経営・運用の視点で書く。

## 仕組み・背景

法律事務所向けの生成AI活用は、2023〜2024年の「契約書レビューAIを個別に試す」段階から、2025〜2026年にかけて「事務所全体のAI基本方針を策定し、リーガルテック企業と組んで自らの専門知見を製品化する」段階へと進んでいる。背景には次の3つの構造要因がある。

1. **契約書レビューAIの法的地位が明確化された**: 法務省大臣官房司法法制部が2023年8月1日に公表した「AI等を用いた契約書等関連業務支援サービスの提供と弁護士法第72条との関係についてのガイドライン」により、契約書の条文ごとにチェックリストに基づく一般的な説明・修正例を表示する機能は、弁護士法72条が禁じる「鑑定」等の法律事務にあたらないことが明確になった。これにより、LegalOn Technologies「LegalForce」などの契約書レビューAIは適法性への懸念を大きく減らし、法律事務所・企業法務部の双方で導入が加速した([LegalOn Technologies公式](https://legalontech.jp/6611/))。
2. **AI・契約ナレッジを掛け合わせた「AI Agent」型製品への移行**: 契約書レビューAIは、条文単位のチェックから、複数の書類・過去の契約データベースを横断して判断を支援する「AIエージェント」型の製品へ進化している。MNTSQは2025年10月、契約書の論点を自動で整理・構造化する「MNTSQ AI契約アシスタント」をリリースし、全サービスへの「MNTSQ AI Agent」実装を開始した([MNTSQ公式](https://mntsq.co.jp/news/release/mntsq-ai-agent-2025))。
3. **大手法律事務所が「知見の製品化」に動き始めた**: 従来、法律事務所はリーガルテックの「利用者」だった。2024〜2025年にかけて、大手事務所が自らの審査基準・ひな形をリーガルテック企業と共同で製品化し、収益源とする動きが顕在化している(詳細は後述)。これは会計事務所業界でみられる「基幹システムベンダーがAIエージェントを標準搭載する」動き([会計事務所・税理士法人における生成AI活用事例](accounting-tax-firm-industry-ai-use-cases.md)参照)とは逆方向で、法律事務所側が能動的にリーガルテック企業と組んで市場に出るという特徴がある。

あわせて、日本弁護士連合会(日弁連)が2025年9月にAI戦略ワーキンググループ名で「弁護士業務における生成AIの利活用等に関する注意事項〜適切な利活用に向けた5つのポイント」を公表するなど、業界団体によるルール整備も同時期に進んだ(詳細は後述)。

## 使いどころ・使い分け

法律事務所の業務領域ごとに、生成AI活用の向き・不向きと成熟度を整理すると次のようになる。

| 業務領域 | AIの向き・不向き | 理由・成熟度(2026年9月時点) |
|---|---|---|
| 契約書レビュー(国内契約・定型) | 向く(実用段階) | LegalForce・GVA assist・MNTSQ・BoostDraftなど、弁護士監修プレイブックを搭載した専用AIが多数あり、大手事務所も監修者として関与 |
| 契約書レビュー(英文・クロスボーダー) | 向く(実用段階、ただし要検証) | Harveyなど法務特化AIが対応。ただし準拠法・言語が混在する契約は誤読リスクが上がるため人によるダブルチェックが必須 |
| 判例・法令調査 | 条件付きで向く | 海外ではWestlaw Edge・Lexis+ AIのように判例データベースに根ざしたAI調査ツールが普及。汎用チャットAIでの判例調査は[ハルシネーション](../part04-risk-security/hallucination-and-countermeasures.md)による架空判例引用のリスクが高く、原典を必ず自分で確認する運用が前提 |
| デューデリジェンス(DD)・訴訟資料の一次レビュー | 向く(実用段階) | 大量の書類から論点・リスクを抽出する一次処理は生成AIの得意領域。Harveyの海外導入事例では週数時間〜10時間規模の作業時間削減が報告されている |
| 証拠開示(e-ディスカバリー) | 向く(海外訴訟中心に急速進展) | Relativity・Everlawなど大手eディスカバリー基盤が2026年に生成AIレビュー機能を標準機能化・無償化する動きがあり、大量文書の一次選別が高速化 |
| 訴訟書面のドラフト・引用チェック | 条件付きで向く | 下書き作成には有効だが、AIが生成した判例引用は必ず実在確認が必要。米国では2026年に入っても架空判例引用による懲戒処分が相次いでいる(後述) |
| 事務所の経営方針・料金体系・弁護士の最終判断 | 不向き | 依頼者との信頼関係・弁護士としての善管注意義務に関わる意思決定はAIが代替できない領域 |
| 一般人からの法律相談への直接回答(非弁行為に該当しうる業務) | 不向き(弁護士法72条の制約) | AIが個別事案について法的な鑑定・代理を行うことは弁護士法72条に抵触しうる。契約書レビューAIが適法とされているのは「一般的な説明・チェックリストに基づく指摘」にとどまる範囲であるため |

**判断の軸**: 「大量の文書を横断的に処理する定型業務」ほどAIエージェントへの置き換えが進み、「個別事案の法的評価・最終責任」に関わる業務ほど弁護士本人が判断を握り続ける、という構図は会計・コンサルなど他の専門サービス業とも共通する。法律事務所に固有なのは、この境界線が弁護士法72条という明文の法律で引かれている点である。

## 実務での使い方

### 1. 大手法律事務所の全社導入方針・ガバナンス体制

- **西村あさひ法律事務所・外国法共同事業**: 2025年を「AI元年」と位置づけ、全弁護士・全所員にAI活用環境を提供開始した。特定のAIベンダーに依存せず、用途に応じて最適なAIを選べる「ベスト・オブ・ブリード」方針を採用し、基本的な考え方を示す「AI基本方針」を策定したうえで実効性あるガバナンス体制・情報管理体制を整備している。情報検索の効率化、文書要約の迅速化、クライアント向け報告資料のたたき台作成などで成果を積み上げているとする([西村あさひ法律事務所公式](https://www.nishimura.com/ja/responsible-ai))。
- **森・濱田松本法律事務所**: 法務特化の生成AI企業Harveyとアジアで初めての独占パートナーシップを締結し、オープンエンドAPIの独占アクセス権を獲得。国内外の拠点で全面的に生成AIシステムを導入し、契約書チェックなどの業務効率化を進めている。これとは別に、自事務所が監修した法務ひな形・解説記事をLegalOn Technologiesの「LegalOn Cloud」上の「MORI HAMADAライブラリー」として提供しており、シンガポール法・タイ法のひな形も追加するなどアジア展開も進めている([Law.asia](https://law.asia/ja/mori-hamada-inks-exclusive-ai-partnership/)、[日本経済新聞](https://www.nikkei.com/article/DGXZQOTG2249G0S4A720C2000000/)、[LegalOn Technologies公式](https://legalontech.jp/9188/))。
- **長島・大野・常松法律事務所**: MNTSQと共同で審査基準書(プレイブック)を開発し、2025年10月にリリースされた「MNTSQ AI契約アシスタント」に標準搭載されている。導入企業は初日から自己解決とエスカレーション支援が可能になり、審査基準の統一・ガバナンス強化につながるとされる。三菱電機・電通総研などがこのプレイブックを採用している([MNTSQ公式](https://mntsq.co.jp/news/release/mntsq-ai-agent-2025)、[businessandlaw.jp](https://businessandlaw.jp/articles/lawyersguide2026-scope01/))。

**読み方のコツ**: いずれの事例も「AIツールを社内利用するだけ」にとどまらず、①事務所単位の基本方針・ガバナンス体制を先に整備する、②自事務所の審査基準・ひな形という無形資産をリーガルテック企業と組んで製品化し、対外的な収益源・ブランディングに変える、という2段階で動いている点が共通する。特に②は、士業事務所が「AIの利用者」から「AIベンダーの共同開発パートナー」へ立場を広げる動きとして、他の専門サービス業にも応用できる視点である。

### 2. 契約書レビューAIの主要製品比較(国内・2026年9月時点)

| 製品 | 提供元 | 特徴 | 監修・提携関係 |
|---|---|---|---|
| LegalForce / LegalOn Cloud | LegalOn Technologies | 条文ごとのリスク自動検知、2,000件以上のひな形、弁護士作成の定型プロンプトを呼び出す「Prompt Workflows」を提供(詳細は[士業・専門サービスにおける生成AI活用事例](professional-services-ai-use-cases.md)) | 森・濱田松本法律事務所監修の「MORI HAMADAライブラリー」を搭載 |
| MNTSQ AI契約アシスタント | MNTSQ | 契約書の論点を自動整理・構造化する「AI Agent」型。プレイブックを標準搭載 | 長島・大野・常松法律事務所監修のプレイブックを標準搭載 |
| GVA assist | GVA TECH | 法務案件の依頼受付から契約審査・管理までを一元化する法務オートメーション「OLGA」の一部として提供 | GVA法律事務所グループが自らプロンプト活用セミナーを実施するなど、開発元と法律事務所が同一グループ内 |
| BoostDraft | BoostDraft | Word上で動作する契約書ドラフト支援AI。国内外の大手事務所・企業法務部での採用が進む | - |

**自事務所・自社への応用ヒント**: どの製品も「弁護士監修のプレイブック(審査基準集)を標準搭載している」点が競争軸になっている。自社が契約書レビューAIを選定する際は、機能の見た目だけでなく「どの事務所・どの水準の審査基準が搭載されているか」を確認するのが実務上の近道になる。

### 3. 海外大手法律事務所のAI導入(比較の視点として)

海外の大手法律事務所(Magic Circle・米国大手事務所)は、Harvey・CoCounselなど法務特化AIの導入で先行している。詳細な導入企業・削減時間の実例は[士業・専門サービスにおける生成AI活用事例](professional-services-ai-use-cases.md)を参照されたいが、本ページで補足すべきは訴訟実務に直結する**証拠開示(e-ディスカバリー)**の動きである。大量の電子文書から関連証拠を選別するeディスカバリー分野では、大手基盤のRelativityが2026年初めから生成AIレビュー機能「aiR for Review」「aiR for Privilege」を標準パッケージに無償で組み込み、競合のEverlawも追随して自社の生成AI機能を無償化した。Everlawはさらに Thomson Reuters CoCounsel・Harvey・Google Cloud Gemini Enterprise for Legal・Microsoft 365 Copilotとの連携も発表しており、訴訟実務の一次書類レビューが急速にコモディティ化している([ILS](https://www.ilsteam.com/relativity-and-everlaws-landmark-free-gen-ai-announcements-level-the-playing-field/)、[LawNext](https://www.lawnext.com/2026/09/iltacon-news-round-up-part-1-e-discovery-disco-everlaw-nuix-relativity-reveal.html))。

判例・法令調査の分野では、米国ではWestlaw Edge・Lexis+ AIが2026年時点でそれぞれ月額100〜400ドル程度(AI機能込みの構成では月額300〜500ドル程度)という価格帯で提供されており、法律事務所が判例調査業務にAIを組み込む際の代表的な選択肢になっている([vaquill.ai「Legal AI Pricing Benchmark」](https://www.vaquill.ai/blog/legal-ai-pricing-benchmark))。米国法曹協会(ABA)の調査では、法律事務所・企業法務部門の37%が2026年に生成AIを日常の法律業務プロセスへ組み込む計画があると報告されている([ABA Law Practice Magazine](https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/8am-legal-industry-report/))。

### 4. コピペで使える実例: 契約書レビュー前の一次チェックプロンプト

契約書レビューAIを導入していない小規模事務所・法務部門でも、汎用チャットAI(ChatGPT/Claude/Gemini等)に契約書の下書きレビューを手伝わせる際のプロンプト例。**あくまで弁護士による最終確認前の一次チェック用であり、機密情報の入力可否は事前に事務所のルールを確認すること。**

```
あなたは契約書レビューを補助するアシスタントです。以下の契約書(業務委託契約書)について、
条文ごとに次の観点でチェックし、表形式で出力してください。

1. 条文番号・見出し
2. リスクの種類(例: 一方に不利な解除条件、損害賠償の上限がない、
   秘密保持期間が不明確 など)
3. リスクの度合い(高/中/低)
4. 修正の方向性(具体的な代替文言までは提案せず、論点の指摘にとどめること)

注意:
- 法的な結論やアドバイスを断定的に述べず、「弁護士の確認が必要な論点」として提示すること
- 判例・法令を引用する場合は、実在するものか自信がない場合は
  「要検証」と明記すること(存在しない条文・判例を作らないこと)

[ここに契約書の本文を貼り付け]
```

### 5. ツール横断の対応付け

| 概念 | 契約書レビューAI(国内) | 汎用AIチャット | 海外法務特化AI |
|---|---|---|---|
| 審査基準・プレイブック | LegalForce/MNTSQ等の「プレイブック」機能 | カスタムプロジェクトの指示欄にチェックリストを記述 | Harvey/CoCounselの「プレイブック」「ナレッジベース」機能 |
| 過去の契約・ひな形検索 | 各製品のひな形データベース・条文検索機能 | [RAG(検索拡張生成)](../part07-data-analysis/rag-basics.md)を組んだ社内検索 | 各社のナレッジ連携機能 |
| 判例・法令の調査 | (国内専用の判例調査AIは発展途上) | 出典確認必須、原典リンクをたどる運用が前提 | Westlaw Edge / Lexis+ AI |

## 注意点・よくある誤解

- **弁護士法72条(非弁行為の禁止)は依然として境界線である**: 法務省の2023年8月ガイドラインが明確にしたのは、チェックリストに基づく一般的な説明・修正例の提示は弁護士法72条の「鑑定」等にあたらないという点であり、AIが個別事案について法的な結論を出して代理・交渉まで行えば非弁行為に該当しうる。契約書レビューAIの利用範囲を「一般的な指摘」にとどめ、個別の法的助言・交渉代理はAIに行わせない設計を維持する必要がある([LegalOn Technologies公式](https://legalontech.jp/6611/))
- **架空の判例引用は米国で現に懲戒・制裁を招いている**: 2026年に入ってからも、AIが生成した実在しない判例をそのまま訴訟書面に引用し、裁判所から制裁金や懲戒処分を受ける事例が相次いでいる。ある離婚訴訟の控訴審では、提出された63件の引用のうち57件に不備があり、20件が実在しない判例だったとして、担当弁護士が2026年4月にネブラスカ州最高裁判所から業務停止処分を受けた。第6巡回区控訴裁判所も、24件を超える架空の引用を含む書面を提出した弁護士を制裁している。米国では2026年第1四半期だけでAI関連の書面提出に対する制裁金が14万5,000ドルを超えたとする分析もある([Scientific American](https://www.scientificamerican.com/article/why-lawyers-keep-citing-fake-cases-invented-by-ai/)、[Sixth Circuit Appellate Blog](https://www.sixthcircuitappellateblog.com/recent-cases/sixth-circuit-sanctions-attorneys-for-fake-citations-what-does-this-mean-for-use-of-ai/)、[vaquill.ai](https://www.vaquill.ai/blog/ai-hallucination-sanctions-tracker)、[GC.ai](https://gc.ai/blog/ai-hallucination-legal-cases))。日本でも法律・判例分野の[ハルシネーション](../part04-risk-security/hallucination-and-countermeasures.md)対策として、AIが提示した条文・判例は必ず原典(判例データベース・官報等)で実在確認する運用を徹底する必要がある
- **日弁連の「注意事項」は公式見解ではなく免責にもならない**: 日弁連AI戦略ワーキンググループが2025年9月に公表した「弁護士業務における生成AIの利活用等に関する注意事項」は、①入力した情報がAIの学習に利用され第三者への出力に反映されるおそれがあるため営業秘密・非公開情報の入力を避けること、②AIの生成物の正確性は保証されておらず弁護士自身が確認する責任を負うこと、③AIサービスの利用規約・商用利用可否が頻繁に変わるため最新の条件を都度確認すること、を主なポイントとして挙げている。一方で「日弁連としての公式見解を示すものではない」と明記されており、ガイドラインに沿って利用していてもAIが生成した誤った判例・条文を成果物に載せた責任は弁護士本人に残る点は、会計士・弁理士など他の士業団体のガイドラインと共通する構図である
- **依頼者の機密情報・秘匿特権(プリビレッジ)の扱いに特に注意する**: 法律事務所が扱う情報は契約交渉の内幕・M&A情報・訴訟戦略など極めて機微な内容が多く、[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)を徹底したうえで、学習データに利用されない設定・法務特化型AIの利用を検討する必要がある。海外の法律事務所がHarveyのような法務特化AIを選ぶ理由の一つも、汎用AIより秘匿特権への配慮を明示している点にある
- **「知見の製品化」は大手事務所に有利な構図になりやすい**: 森・濱田松本法律事務所や長島・大野・常松法律事務所の事例は、豊富な案件データベースと交渉力を持つ大手事務所だからこそ実現できるモデルである。中小規模の事務所は、自らプレイブックを製品化するより、こうした大手監修のひな形・プレイブックが搭載された既製の契約書レビューAI(LegalForce等)を利用する側に回る方が現実的な選択肢になる

## 最初の一歩

自事務所(または自社法務部)が依頼者向け・社内向けに使っている契約書ひな形・チェックリストを1つ選び、それが自事務所のAI活用方針(入力してよい情報の範囲、AIの生成物を誰がどう確認するか)のもとで、汎用AIチャットや契約書レビューAIの一次チェックに使える状態になっているかを確認することから始めるとよい。

## 関連トピック

- [士業・専門サービスにおける生成AI活用事例](professional-services-ai-use-cases.md)
- [会計事務所・税理士法人における生成AI活用事例](accounting-tax-firm-industry-ai-use-cases.md)
- [法務職における生成AI活用事例](../part15-job-role-cases/legal-ai-use-cases.md)
- [ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-09-15: 初版執筆
- **内容**: 法律事務所・弁護士法人という事業体単位での生成AI活用事例として、西村あさひ法律事務所(AI基本方針・ベスト・オブ・ブリード)、森・濱田松本法律事務所(Harveyとのアジア初独占提携、LegalOn Cloud「MORI HAMADAライブラリー」)、長島・大野・常松法律事務所(MNTSQ AI契約アシスタントのプレイブック監修)といった大手事務所の「知見の製品化」事例、国内契約書レビューAI各製品(LegalForce/MNTSQ/GVA assist/BoostDraft)の比較、海外のeディスカバリー(Relativity/Everlaw)・判例調査AI(Westlaw Edge/Lexis+ AI)の動向、弁護士法72条をめぐる2023年法務省ガイドライン、日弁連の2025年9月「生成AI利活用に関する注意事項」、米国での架空判例引用による懲戒・制裁事例を整理した
- **出典**: [法律事務所・法務部門のための生成AI導入完全ガイド2026(renue)](https://renue.co.jp/posts/legal-law-firm-generative-ai-15-use-cases-2026)、[LegalOn Technologies「弁護士法72条ガイドライン公表について」](https://legalontech.jp/6611/)、[MNTSQ「MNTSQ AI Agent実装開始」プレスリリース](https://mntsq.co.jp/news/release/mntsq-ai-agent-2025)、[MNTSQ「AI契約アシスタント受注開始」プレスリリース](https://mntsq.co.jp/news/release/aikeiyakuasst)、[西村あさひ法律事務所「責任あるAI活用への取り組み」](https://www.nishimura.com/ja/responsible-ai)、[Law.asia「森・濱田松本、Harveyとアジア初の独占パートナーシップ締結」](https://law.asia/ja/mori-hamada-inks-exclusive-ai-partnership/)、[日本経済新聞「森・浜田松本法律事務所、アメリカの生成AI企業と提携」](https://www.nikkei.com/article/DGXZQOTG2249G0S4A720C2000000/)、[LegalOn Technologies「MORI HAMADAライブラリーにアジア法ひな形を搭載」](https://legalontech.jp/9188/)、[businessandlaw.jp「生成AIが切り拓く"攻め"の法務戦略と未来像」](https://businessandlaw.jp/articles/lawyersguide2026-scope01/)、[ILS「Relativity and Everlaw's Landmark Free Gen AI Announcements」](https://www.ilsteam.com/relativity-and-everlaws-landmark-free-gen-ai-announcements-level-the-playing-field/)、[LawNext「ILTACON News Round-Up: E-Discovery」](https://www.lawnext.com/2026/09/iltacon-news-round-up-part-1-e-discovery-disco-everlaw-nuix-relativity-reveal.html)、[vaquill.ai「Legal AI Pricing Benchmark 2026」](https://www.vaquill.ai/blog/legal-ai-pricing-benchmark)、[ABA Law Practice Magazine「8am Legal Industry Report」](https://www.americanbar.org/groups/law_practice/resources/law-practice-magazine/2026/march-april-2026/8am-legal-industry-report/)、[Scientific American「Why Lawyers Keep Citing Fake Cases Invented by AI」](https://www.scientificamerican.com/article/why-lawyers-keep-citing-fake-cases-invented-by-ai/)、[Sixth Circuit Appellate Blog「Sixth Circuit Sanctions Attorneys for Fake Citations」](https://www.sixthcircuitappellateblog.com/recent-cases/sixth-circuit-sanctions-attorneys-for-fake-citations-what-does-this-mean-for-use-of-ai/)、[vaquill.ai「AI Hallucination Sanctions Tracker」](https://www.vaquill.ai/blog/ai-hallucination-sanctions-tracker)、[GC.ai「AI Hallucination Legal Cases: A Sanctions Tracker」](https://gc.ai/blog/ai-hallucination-legal-cases)、[GVA Professional Group「弁護士業務における生成AIの利活用等に関する注意事項セミナー」](https://olga-legal.com/13865/)
