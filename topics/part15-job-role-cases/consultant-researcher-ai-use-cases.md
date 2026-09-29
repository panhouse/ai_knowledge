---
title: コンサルタント・リサーチャー職における生成AI活用事例
part: 15
chapter: 第16章 コンサルタント・リサーチャー
tags: [コンサルティング, リサーチ, Deep Research, NDA, 機密情報, McKinsey, BCG]
created: 2026-08-06
updated: 2026-09-29
---

# コンサルタント・リサーチャー職における生成AI活用事例

## これは何か

経営コンサルタント・調査会社のリサーチャー・独立系のアナリストといった「調査・分析した結果を、対価をもらって他社(クライアント)に納品する」仕事は、[企画職における生成AI活用](planning-ai-use-cases.md)(第5章、成果物は社内向け)と似た作業をしながらも、性質が大きく異なる。成果物が社外に出る以上、「その数字は本当に正しいか」を自分で説明できる状態(根拠の追跡可能性)と、「他社の機密情報を正しく扱えているか」(NDA・守秘義務)の2点が、社内向け企画職以上にシビアに問われる。本ページは、大手コンサルティングファームが実際にどう生成AIを使っているかの実例を交えつつ、リサーチ〜成果物作成の各フェーズでのAI活用と、この職種特有のリスク管理を整理する。

## 仕組み・背景

コンサル・リサーチ業務の生成AI活用は、大きく3つの場面に分かれる。

1. **仮説構築(イシューツリー・MECE分解)**: 論点を「重複なく漏れなく(MECE)」分解し、検証可能な粒度まで落とし込む段階。AIを壁打ち相手にすると、1人では気づきにくい切り口の抜け漏れをその場で指摘させられる。
2. **Deep Researchによる文献・市場調査**: 2025年にOpenAIが「Deep Research」機能をChatGPTに追加して以降、「質問を投げると自律的に複数の情報源を巡回し、統合したレポートを返す」使い方が普及した。実例では1回の実行で10分超・100回以上の検索・20件以上の情報源を経由して、1万字規模のレポートが生成されたケースも報告されている([出典](https://www.businessinsider.jp/article/2505-generative-ai-deep-research-comparison/))。Perplexityは出典リンクの明示と検索速度、Geminiは表形式への整理力に強みがあるとされ、用途によって使い分ける実務者が多い。
3. **インタビュー分析・成果物のドラフト作成**: 定性インタビューの文字起こしを「切片化→グルーピング→抽象化」の順にAIへ処理させて示唆を抽出する使い方や、スライド構成・本文のたたき台を作らせる使い方が広がっている。

大手ファームはこれを汎用チャットツールに任せきりにせず、社内ナレッジと連携した専用ツールに仕立てている。McKinseyは2023年に社内ツール「**Lilli**」を公開し、40以上のナレッジソース・10万件超の社内文書を集約、案件のリサーチから実行計画のドラフトまでほぼ全工程を横断的に支援する体制を敷いている([出典](https://www.mckinsey.com/about-us/new-at-mckinsey-blog/meet-lilli-our-generative-ai-tool))。BCGは資料自動生成ツール「Deckster」(2024年3月展開、GPT-4o搭載、承認済み800〜900種のテンプレートから生成)を導入済みで、展開後45万回以上使われている([出典](https://yourstory.com/2025/06/consulting-firms-ai-tools-mckinsey-bcg-deloitte-2025))。Bainは「Sage」という独自ナレッジベース連携ツールでリサーチ・初期プレゼン作成を支援している。国内では野村総合研究所(NRI)がコンサルティング部門の生成AI利用率が8割を超えると公表しており(2025年時点)、2025年11月にAnthropicの国内初認定リセラーとなるなど提携を強化している([出典](https://www.nri.com/jp/news/newsrelease/20251125_1.html))。

## 使いどころ・使い分け

### 案件フェーズ別のAI活用マップ

| フェーズ | 主なタスク | AIの向き・不向き | 主に使う機能 |
|---|---|---|---|
| 仮説構築 | イシューツリー分解、論点のMECE整理 | 向く(視点の網羅性チェック・壁打ち) | 通常のチャット(対話形式) |
| 一次調査 | 文献・市場調査、競合動向の収集 | 向く(情報源の巡回・統合)。数値の正確性は要検証 | Deep Research系機能(ChatGPT/Gemini/Perplexity/Genspark) |
| 定性分析 | インタビュー・アンケート自由記述の統合 | 向く(切片化・グルーピング・示唆抽出) | 通常のチャット(長文コンテキスト) |
| 定量分析 | データの前処理・集計・グラフ化のたたき台 | 向く(たたき台作成)。分析結果の解釈は人が担う | [チャットAIによるデータ分析](../part07-data-analysis/chatgpt-advanced-data-analysis.md) |
| 成果物作成 | スライド構成案、レポート本文のドラフト | 向く(型に沿った文章化・構成案) | [プレゼン資料・ドキュメント作成](../part12-business-practice/ai-presentation-and-document-creation.md) |
| 納品前チェック | 数値・固有名詞・引用のファクトチェック | **不向き(AI単体での自己検証は限界がある)** | 一次情報での人手確認が必須 |

### Part 15 第5章(企画・PdM・データアナリスト)との境界線

同じ「調査して資料を作る」仕事に見えても、境界は明確に引ける。

| | 第5章(企画・PdM・データアナリスト) | 本ページ(コンサル・リサーチャー) |
|---|---|---|
| 成果物の宛先 | **自社内**(上長・経営会議) | **他社(クライアント)** |
| 情報漏洩の主な対象 | 自社の営業秘密 | **複数クライアントの機密情報**(クライアントAの情報をクライアントBの案件に流用してはならない) |
| 契約上の制約 | 社内規程のみ | **NDA(秘密保持契約)**に基づく目的外利用・第三者開示の禁止 |
| 数字の説明責任 | 社内で完結(訂正が効きやすい) | **対価を得て納品**するため、根拠の追跡可能性がプロフェッショナル責任として問われる |

このため本ページでは、企画職ページでは扱わない「NDA・クライアント機密情報」の論点を独立して扱う。

## 実務での使い方

### プロンプト例1: イシューツリーでの仮説構造化

まだ論点が整理されていない段階で、検証可能な粒度まで論点を分解したいときに使う。

```
あなたは戦略コンサルタントです。以下のテーマについて、MECE(重複なく漏れなく)を
意識したイシューツリーを3階層で作成してください。

## テーマ
[例: 中堅製造業A社の海外展開が伸び悩んでいる原因を特定したい]

## 出力条件
- 第1階層は3〜4個の大論点に分解する
- 各末端の論点は「Yes/Noで検証可能」または「定量的に測定可能」な形にする
- 各末端の論点について、検証に必要なデータソース・調査方法の案を1行で添える
- この段階では結論や仮の答えは出さず、論点の構造化のみに集中する
```

出てきたツリーに対して「この枝は本当に独立しているか」「経営層が一番知りたい枝はどれか」と聞き返し、対話を重ねて絞り込むと、1回の出力を鵜呑みにするよりも精度が上がる。

### プロンプト例2: Deep Researchでの市場調査(出典明記を必須にする)

```
以下のテーマについて、Deep Research機能を使って調査し、レポートにまとめてください。

## テーマ
[例: 国内中小製造業向けSaaS市場の規模推移と主要プレイヤーの動向]

## 調べてほしい項目
1. 市場規模の推移(過去3年分)と、算出根拠・発表元
2. 主要プレイヤー5社程度の料金・機能・ターゲット層の比較
3. 直近1年の規制・業界動向のうち、意思決定に影響しそうなもの

## 出力条件
- すべての数値・固有名詞に出典URLと発表年を明記する
- 出典が確認できない・推定に留まる数値は「推定」「未確認」と明記する
- 前提の異なる複数のデータが見つかった場合は、両方を提示し違いを説明する
- 3年以上前の古い数値は参考情報として区別する
```

Perplexityは出典リンクの提示が速く一次情報の当たりを付けやすい、Geminiは表形式への整理に強い、ChatGPTは長文レポートとしての統合力が高い、といった傾向があるとされ、「Perplexityで一次情報を集めてからChatGPTで統合する」といった併用も実務では行われている。

### プロンプト例3: インタビュー・自由記述の統合分析

```
以下は顧客インタビュー(全8件)の文字起こしです。次の手順で分析してください。

1. 発言を意味のまとまりごとに切片化する
2. 切片をテーマごとにグルーピングする(グループ名を付ける)
3. 各グループを抽象化し、「示唆」として3〜5個にまとめる
4. 示唆ごとに、根拠となった発言を1〜2件、匿名化した形で引用する

【文字起こしデータ】
(貼り付け)
```

「切片化→グルーピング→抽象化」の3段階を明示的に指示すると、一度に要約させるよりも根拠と示唆のつながりが追いやすくなる。

### 成果物作成: 構成案→肉付けの2段階

企画書と同様、コンサルの成果物もAIにいきなり本文を書かせず、まず章立て(骨子)を確認してから肉付けする2段階アプローチが手戻りを減らす(詳細は[企画職における生成AI活用](planning-ai-use-cases.md)の「企画書・事業計画書への落とし込み」と同じ考え方)。スライド化の実務は[生成AIによるプレゼン資料・ドキュメント作成の実務活用](../part12-business-practice/ai-presentation-and-document-creation.md)を参照。

### ツール横断の対応表

| やりたいこと | 主に使うツール |
|---|---|
| 自律調査・市場レポート作成 | ChatGPT Deep Research、Gemini Deep Research、Perplexity、Genspark |
| 社内ナレッジと連携した調査支援 | McKinsey「Lilli」、Bain「Sage」など各社独自ツール(社外では利用不可) |
| スライド・資料の自動生成 | BCG「Deckster」など各社独自ツール、汎用ツールでは[プレゼン資料・ドキュメント作成](../part12-business-practice/ai-presentation-and-document-creation.md)を参照 |
| 定量分析のたたき台 | ChatGPT/Gemini/Claudeの[データ分析機能](../part07-data-analysis/chatgpt-advanced-data-analysis.md) |
| 機密性の高いクライアント情報の入力 | 法人向けEnterprise/Teamプラン(学習非利用がデフォルト)。個人向け無料プランは不可 |

## 導入事例カタログ

ここまでは職種横断で使える汎用的なプロンプト例を紹介した。以下は
`templates/case-card.md` の書式による実名組織の事例である。大手コンサルティングファームが
「自社の知識検索」「全社員へのチャットAI配備」「社内問い合わせ対応」にどう組み込んだかと、
コンサルタントの成果物の質に与える影響を測った第三者の実験結果を収録する。

### McKinsey & Company(戦略コンサルティング大手) — 対象業務: 社内ナレッジ検索・議論の壁打ち
- **導入形態**: 内製(自社開発の生成AIプラットフォーム「Lilli」)
- **段階**: 全社展開(2023年8月時点で約7,000人が利用可能、2023年秋までに全社員へ拡大予定と報道)
- **やったこと**: 自社の知識資産(40超の情報源・10万件超の文書)を検索・要約する機能と、外部情報を対象にしたチャット機能の2つのモードを持つ。質問に対し関連情報を5〜7件特定して要点を要約し、リンクと該当分野の専門家を提示する。会議・プレゼン前の壁打ち相手としても使われる
- **効果**: 数値公表なし(2023年8月時点の報道では、定量的な効率化指標は示されていない。CTOのコメントは「生産性の新しい水準」という定性的なもの)
- **学べること**: 社外の汎用AIに機密を渡さず「自社の過去資産を引く」検索型から始め、出典リンクと専門家の紹介まで返す設計にすると、ハルシネーションと属人化の両方に対処しやすい
- **出典**: [CIO Dive: McKinsey rolls out generative AI tool 'Lilli' to 7K employees(2023-08-17)](https://www.ciodive.com/news/McKinsey-generative-AI-Lilli-platform-internal-employees/691231/) / 最終確認日: 2026-09-29

### PwC(会計・コンサルティング大手) — 対象業務: 全社員向けチャットAIの配備と業務別カスタムGPT開発
- **導入形態**: 専用SaaS導入(ChatGPT Enterprise)
- **段階**: 全社展開(米英を中心に10万人超への配備を2024年5月に報道)
- **やったこと**: ChatGPT Enterpriseを10万人超の社員に展開し、あわせてOpenAIの法人向け再販パートナーにもなった。社内で3,000件超のAI活用ユースケースを洗い出し、税務申告書のレビュー、提案書の回答作成、ソフトウェア開発者の支援などのカスタムGPTを開発中と報じられた
- **効果**: 洗い出したユースケースの約4割に対応済み、生成AIが米国の主要顧客上位1,000社のうち950社の案件に関与(2024年5月時点、CIO Diveの報道による。PwC自身の業務時間削減などの数値は公表なし)
- **学べること**: 「全員にツールを配る」だけでなく、先にユースケースを棚卸ししてカスタムGPTに落とし込む二段構えで展開している。棚卸しの件数と対応率を進捗指標にする方法は自社でも真似しやすい
- **出典**: [CIO Dive: PwC plans ChatGPT Enterprise rollout to 100K employees(2024-05-29)](https://www.ciodive.com/news/pwc-chatgpt-enterprise-openai-partnership/717432/)、[TechCrunch: OpenAI signs on 100K PwC workers to its ChatGPT Enterprise tier(2024-05-29)](https://techcrunch.com/2024/05/29/openai-signs-on-100k-pwc-workers-to-its-chatgpt-enterprise-tier-as-the-consultant-becomes-its-first-resale-partner) / 最終確認日: 2026-09-29

### Boston Consulting Group(戦略コンサルティング大手)× ハーバード・ビジネス・スクール等 — 対象業務: コンサルティング業務全般(実験)
- **導入形態**: 汎用チャットAI活用(GPT-4を使った統制実験)
- **段階**: PoC(BCGのコンサルタント758人が参加した野外実験。本番導入後の数値ではない)
- **やったこと**: BCGのコンサルタント758人を、AIなし・AIあり(GPT-4)などの群に分け、現実的なコンサルティング課題18件を解かせて生産性と品質を比べた
- **効果**: AIを使った群は平均で12.2%多くのタスクを完了し、25.1%速く完了、成果物の品質評価が高かった参加者が約40%(2023年秋の研究発表。公表主体は研究者=第三者)。一方、AIが苦手な範囲の課題では、AIを使った群の正答率がAIなしより19ポイント低かったと報道されている
- **学べること**: AIが得意な範囲では明確に速く・質が上がるが、範囲外の課題ではAIの説得力のある誤答に引きずられる。自分の業務のどのタスクが「AIの得意範囲内」かを事前に見極める運用ルールが要る
- **出典**: [The Harvard Crimson: Harvard Business School Partners with BCG on AI Productivity Study(2023-10-13)](https://www.thecrimson.com/article/2023/10/13/jagged-edge-ai-bcg/) / 最終確認日: 2026-09-29

### アクセンチュア(日本法人・総合コンサルティング) — 対象業務: 社内の人事・法務・調達・総務・経費・契約などの問い合わせ対応
- **導入形態**: 内製(社内チャットボット「Randy-san」を2023年4月にGPTエンジンへ移行)
- **段階**: 全社展開(2017年9月に導入、生成AI化は2023年4月)
- **やったこと**: 人事・法務・調達・総務・経費申請・契約などの社内問い合わせに答えるチャットボットの回答エンジンを生成AI(GPT)に切り替え、社員の質問対応と回答者側の負荷を同時に下げた
- **効果**: 月間アクティブユーザー1万1,000人超、月約7万件の問い合わせに対応、社員と回答者の両方で年間約20万時間の工数削減(2024年4月時点、自社公表の採用ブログ)
- **学べること**: コンサルタント本人の分析業務だけでなく、バックオフィスへの問い合わせという「質問する側・答える側の両方の時間」を減らす使い方は、コンサル以外の専門職組織にも転用しやすい
- **出典**: [アクセンチュア: 仕事の進め方を一新！生成AIを社員のパートナーに(採用ブログ)](https://www.accenture.com/jp-ja/blogs/japan-careers-blog/gen-ai) / 最終確認日: 2026-09-29

### 事例から見える傾向

- **数値の性質が事例ごとに違う**: McKinsey・PwCは規模や利用状況の指標のみで、時間削減の実測値は公表されていない。BCGは実験結果、アクセンチュアは自社公表の実績値。記事などで引用するときは「実験」「導入実績」「利用状況」を混ぜない
- **機密を扱う職種は「自社閉じ」か「法人契約」が前提**: McKinseyは自社基盤、PwCは法人向けEnterpriseプランと、いずれも汎用の無料チャットAIにクライアント情報を入れる形にはしていない

## 注意点・よくある誤解

- **クライアント情報の入力はNDA違反になり得る**: NDA(秘密保持契約)は目的外利用・第三者開示の禁止を定めており、クライアントから受け取った資料をそのまま生成AIに入力する行為が、この禁止事項に抵触し契約違反となるリスクが法律専門家から指摘されている([出典](https://storialaw.jp/blog/13047))。入力前に「このクライアントとの契約でAI利用が許可されているか」を必ず確認する。
- **「Enterprise/Team」と「無料・個人向け」の違いを正しく理解する**: 法人向け有料プラン(ChatGPT Enterprise、Claude Enterprise等)はNDA・データ処理契約が組み込まれ、学習への非利用がデフォルト設定になっている。ただし「Team」プランは名称に反して学習オプトインがデフォルトになっているケースもあり、契約内容を個別に確認しないままクライアント情報を扱うと学習データへの流出リスクが残る([出典](https://sonomos.ai/blog/chatgpt-vs-claude-confidential-work-2026/))。高機密案件では、入力データを一切保持しない「Zero Data Retention」設定の利用可否も確認する。
- **クライアントをまたいだ情報の混同(チャイニーズウォール)に注意**: 同じAIツールで複数クライアントの案件を並行して扱う場合、あるクライアントの機密情報が別クライアントとの会話・プロジェクト設定に紛れ込まないよう、ツールのプロジェクト分離機能を使い、案件ごとにワークスペースを分ける。
- **数値のハルシネーションは成果物の信頼を丸ごと壊す**: 対価を得て納品する成果物に、AIが作文した市場規模やもっともらしい統計値が無検証で混入すると、発覚した際の信頼失墜は社内資料の比ではない。McKinseyのLilliが「引用元を明示する」設計を採る([出典](https://www.mckinsey.com/about-us/new-at-mckinsey-blog/meet-lilli-our-generative-ai-tool))ように、重要な数字・固有名詞・法令の引用は必ず一次情報(官公庁統計、企業IR、業界団体データ)で自分の目で確認してから納品する。
- **AI活用が「品質向上」に直結するとは限らない**: 市場調査業界の調査では、サプライヤー側(調査会社)の67%がクライアント成果物に生成AIを直接組み込んでいる一方、発注側であるブランドのリサーチャーのAI満足度はわずか13%にとどまるという結果が報告されている([出典](https://www.greenbook.org/insights/grit/smarter-insights-faster-pace-ais-breakthrough-in-market-research))。効率化と品質担保は別軸で管理する必要がある。

## 最初の一歩

直近の案件で抱えている論点を1つ選び、プロンプト例1のイシューツリーテンプレートで分解してみる。出てきた枝の1つについて「この枝を検証するには何のデータが必要か」とAIに聞き返し、Deep Research系機能での一次調査に進めるかを判断する。

## 関連トピック

- [企画職における生成AI活用](planning-ai-use-cases.md)
- [データアナリスト/BIアナリスト職における生成AI活用事例](data-analyst-ai-use-cases.md)
- [生成AIによる情報収集・リサーチの実務活用(Deep Research機能)](../part12-business-practice/ai-research-and-information-gathering.md)
- [ハルシネーションとは何か・対策](../part04-risk-security/hallucination-and-countermeasures.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-09-29: 導入事例カタログを新設し、4件の実名事例を追加
- **内容**: `templates/case-card.md` の書式で「導入事例カタログ」節を新設し、McKinsey(Lilli、数値公表なし)、PwC(ChatGPT Enterprise 10万人超配備)、BCG×HBSの生産性実験(12.2%多く・25.1%速く、範囲外課題では正答率19ポイント低下)、アクセンチュア(社内問い合わせボットの生成AI化、年約20万時間削減)の4件を追加
- **出典**: [CIO Dive: McKinsey Lilli](https://www.ciodive.com/news/McKinsey-generative-AI-Lilli-platform-internal-employees/691231/)、[CIO Dive: PwC](https://www.ciodive.com/news/pwc-chatgpt-enterprise-openai-partnership/717432/)、[TechCrunch: PwC](https://techcrunch.com/2024/05/29/openai-signs-on-100k-pwc-workers-to-its-chatgpt-enterprise-tier-as-the-consultant-becomes-its-first-resale-partner)、[The Harvard Crimson: BCG研究](https://www.thecrimson.com/article/2023/10/13/jagged-edge-ai-bcg/)、[アクセンチュア採用ブログ](https://www.accenture.com/jp-ja/blogs/japan-careers-blog/gen-ai)

### 2026-08-06: 初版執筆
- **内容**: コンサルタント・リサーチャー職(クライアント納品前提)における生成AI活用として、イシューツリーでの仮説構造化、Deep Researchでの市場調査、インタビュー分析、成果物作成のプロンプト例を整理。McKinsey「Lilli」・BCG「Deckster」・Bain「Sage」など大手ファームの内製ツール事例、NRIの国内動向、NDA・クライアント機密情報の取り扱いや「Enterprise/Team」プランの違いといったこの職種特有のリスクを、Part 15第5章(企画・PdM・データアナリスト)との境界線とともに整理
- **出典**: [McKinsey: Meet Lilli, our generative AI tool](https://www.mckinsey.com/about-us/new-at-mckinsey-blog/meet-lilli-our-generative-ai-tool)、[YourStory: How consulting firms are deploying AI tools](https://yourstory.com/2025/06/consulting-firms-ai-tools-mckinsey-bcg-deloitte-2025)、[NRI: Anthropic国内初認定リセラーに選定](https://www.nri.com/jp/news/newsrelease/20251125_1.html)、[Business Insider Japan: 生成AIのDeep Research機能比較](https://www.businessinsider.jp/article/2505-generative-ai-deep-research-comparison/)、[STORIA法律事務所: NDAと生成AI利用](https://storialaw.jp/blog/13047)、[Sonomos: ChatGPT vs Claude for confidential work](https://sonomos.ai/blog/chatgpt-vs-claude-confidential-work-2026/)、[Greenbook GRIT 2025 Insights Practice Report](https://www.greenbook.org/insights/grit/smarter-insights-faster-pace-ais-breakthrough-in-market-research)
