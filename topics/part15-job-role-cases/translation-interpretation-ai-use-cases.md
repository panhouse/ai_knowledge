---
title: 翻訳・通訳担当における生成AI活用事例
part: 15
chapter: 第15章 翻訳・通訳
tags: [翻訳, 通訳, DeepL, ポストエディット, MTPE, 字幕翻訳, 吹き替え, リアルタイム翻訳, 用語集]
created: 2026-07-17
updated: 2026-08-12
---

# 翻訳・通訳担当における生成AI活用事例

## これは何か

翻訳・通訳担当の仕事は、契約書や製品マニュアルのような「一言一句の正確性が問われる文書翻訳」から、会議の同時通訳、動画の字幕・吹き替えまで幅が広い。生成AIの登場で「DeepLのような専用の機械翻訳(MT: Machine Translation)を使うべきか、ChatGPT/Gemini/Claudeのような汎用LLMに翻訳させるべきか、それとも人間の通訳者を呼ぶべきか」という選択肢が増え、かえって迷いやすくなっている。本ページは、[生成AIによる文章作成・編集の実務活用](../part12-business-practice/ai-writing-and-editing.md)で扱った「翻訳・多言語化」の一般論をさらに掘り下げ、翻訳・通訳を主業務とする担当者向けに、ツールの使い分け・用語集(グロッサリー)によるブレ防止・ポストエディット(機械翻訳の人手修正)の進め方・リアルタイム通訳支援・字幕/吹き替え制作・機密文書の取り扱いまでを整理する。

## 仕組み・背景

翻訳AIには大きく2つの系統があり、得意分野が異なる。

1. **専用の機械翻訳(MT)エンジン**: DeepLやGoogle翻訳のように、翻訳専用に学習されたニューラル機械翻訳モデル。文法的な正確さと訳文の安定性(同じ入力なら毎回ほぼ同じ訳が出る一貫性)に強みがあり、特に英語・ドイツ語・フランス語・スペイン語など欧州言語間の翻訳精度が高い。
2. **汎用LLM(ChatGPT・Gemini・Claude等)**: 翻訳専用ではないが、プロンプトで「読み手」「トーン」「専門分野の用語遣い」を細かく指示できる柔軟性が強み。日本語・中国語・韓国語などアジア言語や、文脈・トーンの調整が必要な文書(マーケティング文書、社内向けの砕けた文章)で評価が高い。2026年時点の各種ベンチマーク比較でも、一般的なビジネス・技術文書であれば人間の翻訳者に匹敵する90〜95%程度の精度水準に達しているとされる一方、勝敗は言語ペアとコンテンツの性質次第という結論が多い([intlpull](https://intlpull.com/blog/machine-translation-accuracy-2026-benchmark)、[sintra.ai](https://sintra.ai/blog/deepl-vs-chatgpt))。

もう一つの背景が、**ポストエディット(PEMT: Post-Editing Machine Translation、MTPEとも呼ばれる)**という考え方の普及である。これは「機械翻訳の訳文をそのまま使う」のでも「ゼロから人間が翻訳する」のでもなく、機械翻訳の訳文をプロの翻訳者・担当者が確認・修正して仕上げる工程を指す。修正の深さによって、誤訳や訳抜けがないかだけを最低限チェックする「ライトエディット」と、人手翻訳とほぼ同等の品質に仕上げる「フルエディット」に分かれ、文書の重要度に応じて使い分けるのが実務の基本になっている([日本翻訳センター](https://www.jtc.co.jp/post-editing/)、[Phrase](https://phrase.com/blog/posts/machine-translation-post-editing/))。

リアルタイム音声翻訳(同時通訳のAI版)も2025〜2026年にかけて急速に進化した。従来は「音声認識→テキスト翻訳→音声合成」の3段階を経由するため遅延と機械的な声が課題だったが、音声を直接処理する「音声ネイティブ」なモデルが登場し、話者本来の抑揚・間・感情表現をある程度保ったまま翻訳音声を生成できるようになっている(詳細は[主要AIチャットツールの音声対話機能比較](../part03-ai-chat-tools/ai-chat-tools-voice-comparison.md)を参照)。2026年3月に北京の中関村フォーラムで54言語・1秒未満の遅延を実現したAR+AI同時通訳システムが導入されるなど、大規模国際会議での実用化も進んでいるが、業界の共通見解は「AIが翻訳の大部分を担い、人間の通訳者は高度な判断や文化的配慮が必要な場面で監督・介入する」という協働モデルが標準になりつつあるという点である([Timekettle](https://www.prnewswire.com/news-releases/timekettle-introduces-x1-meeting-interpreter-hub-bringing-real-time-ai-translation-to-global-meetings-of-up-to-50-participants-302805394.html))。

翻訳者・通訳者という職業自体も、AIによる下訳を前提に「ゼロから翻訳する人」から「AIの訳文を確認・修正するポストエディター」へと役割が変化している。厚生労働省の職業別求人動向では「翻訳者・通訳者」の求人倍率が2019年の約2.0倍から2023年に2.6倍まで上昇しており、需要自体が縮小しているわけではなく、業務の内容がポストエディット中心にシフトしていると見るのが実務的な理解になる([通訳翻訳ジャーナル](https://tsuhon.jp/professional/career/trend1/)、[クリムゾン・ジャパン](https://www.crimsonjapan.co.jp/blog/will-translators-disappear-in-the-future/))。

## 使いどころ・使い分け

### 文書翻訳: DeepL vs 汎用LLM vs 人間翻訳者

| 状況 | 向くツール・担当 | 理由 |
|---|---|---|
| 欧州言語間(英⇔独仏西等)の定型文書・レイアウト保持が必要な文書 | DeepL(Pro) | 訳文の一貫性・文書フォーマット保持機能に強み。用語集機能で表記ゆれも防げる |
| 日本語⇔英語・中国語・韓国語で、トーンや読み手を細かく調整したい文章 | 汎用LLM(ChatGPT/Gemini/Claude) | プロンプトで「読み手」「敬語レベル」「専門分野」を都度指定でき、文脈依存の訳し分けに強い |
| マーケティング文書・キャッチコピーなど「意訳・トランスクリエーション」が必要なもの | 汎用LLM+人によるレビュー | 直訳では成立たない訴求表現の言い換えは、AIに複数案を出させて人が選ぶ使い方が向く |
| 契約書・特許明細書・規制対応文書など一言一句の重みが大きい文書 | 機械翻訳(下訳)+プロ翻訳者によるフルエディット、または専門の翻訳会社 | 誤訳が法的リスク・事業リスクに直結するため、AI単独では完結させない |
| 社内向けの参考訳・大意把握(意思決定に使わない読み物) | 機械翻訳・汎用LLMそのまま、または軽いライトエディット | 誤りがあっても実害が小さく、スピード優先でよい |

判断の軸は、広報・PR職や法務職のページと同様に「間違っていても後で人が直せるか」「訳文が対外的・法的な重みを持つか」の2点。実務では「DeepL/Google翻訳で下訳→重要文書は人(プロ翻訳者)がポストエディット、社内資料はチャットAIでそのまま」という2段構えのすみ分けが定着しつつある([eesel AI](https://www.eesel.ai/blog/deepl))。

### リアルタイム通訳支援: どこまでAIに任せられるか

| シーン | AIの向き・不向き | 人の通訳者が必要な理由 |
|---|---|---|
| 社内の多言語定例会議(字幕表示のみでよい) | 向く(Zoom/Teams/Google MeetのAI字幕翻訳で十分なことが多い) | 誤訳があっても発言者が言い直せる、実害が小さい |
| 対面での多言語ミーティング・工場見学・展示会ブース対応 | 向く(Timekettleのようなウェアラブル型AI通訳デバイスが実用段階) | ソフトウェアの画面共有が不要な現場作業でも使える。2026年6月発表の「Timekettle X1 Meeting Interpreter Hub」は最大50人参加の会議で52言語・106アクセントに対応([PR Newswire](https://www.prnewswire.com/news-releases/timekettle-introduces-x1-meeting-interpreter-hub-bringing-real-time-ai-translation-to-global-meetings-of-up-to-50-participants-302805394.html)) |
| 一対一の簡単な海外出張先での会話・現地スタッフとのやり取り | 向く(スマホのChatGPT音声モード・Gemini翻訳アプリで代替可) | 定型的なやり取りなら精度・速度とも実用レベル |
| 顧客との商談・価格交渉・契約条件のすり合わせ | 限定的(AI字幕は「補助」、要点は人が確認) | ニュアンス・駆け引き・沈黙の意味など、機械翻訳では拾えない文脈が多い |
| 記者会見・株主総会・国際会議などの公式通訳 | 向かない(プロの通訳者が必須) | 誤訳が公式記録・報道として残り、訂正が効かない。話者の意図を汲んだ要約・省略の判断が必要 |
| 医療通訳・法廷通訳など専門性・責任が極めて重い場面 | 向かない | 誤訳が人命・権利に関わる。有資格の専門通訳者を必ず起用する |

AIのリアルタイム翻訳は「あった方が便利な補助輪」であり、「誤訳が許されない場面での代替」ではない、という線引きが実務での基本方針になる。

## 実務での使い方

### 1. DeepLで用語集(グロッサリー)を作り、表記ゆれを防ぐ

DeepL Pro・DeepL APIには「用語集(グロッサリー)」機能があり、社名・製品名・業界固有の専門用語について「この単語は必ずこう訳す」というルールを事前登録できる。単純な検索置換ではなく、訳文の文法(格変化・活用など)に合わせて自然に組み込まれる点が特徴([DeepLヘルプセンター](https://support.deepl.com/hc/en-us/articles/360021634540-About-the-glossary))。

画面の場所: DeepL Web版右上のアカウントメニュー→「用語集」→「+新規用語集」から、原語・訳語のペアをCSVまたは手入力で登録。API利用時は`glossary_id`パラメータで指定する。用語集はDeepL Pro・DeepL APIいずれでも作成可能(1アカウントあたり最大1,000件、1件あたり最大10MBまで)。なお2026年7月時点でDeepL APIの旧プラン(API Free/API Pro)は新規契約を終了し、新規契約は無料の「Developer」(月100万文字まで)または「Growth」(月26ドル〜)に一本化されている点に注意([eesel AI](https://www.eesel.ai/blog/deepl-pricing))。

```
【用語集の登録例(製品マニュアル向け)】
原語(日本語) → 訳語(英語)
「株式会社◯◯」 → "XX Corporation"(「Co., Ltd.」は使わない)
「お客様相談窓口」 → "Customer Support Center"(「Consultation Desk」と訳さない)
「初期設定」 → "initial setup"(「default setting」と訳し分けない)
```

### 2. 汎用LLMで「読み手・トーン・専門分野」を指定した翻訳を依頼する

DeepLのような専用MTにはない強みが、プロンプトでの細かい指示。特に契約書以外の一般文書・メール・社内資料はこちらが有利なことが多い。

```
以下の日本語の文章を英語に翻訳してください。

## 読み手
[例: 海外拠点の非日本語ネイティブの同僚、技術的な前提知識は中級レベル]

## トーン・文体
[例: ビジネスメールとして自然な丁寧さ。直訳調にせず、日本語特有の
婉曲表現(「ご検討いただければ幸いです」等)は、英語として自然な言い回しに置き換える]

## 用語の扱い
- 社内特有の略語(例: ○○)は初出時に一言説明を加える
- 専門用語(例: [業界用語をここに列挙])は下記の対訳を優先して使う
  [用語対訳リストを貼り付け]

## 出力形式
訳文のみを出力し、直訳では意味が変わってしまい意訳した箇所があれば、
末尾に「訳注」として1〜2行で説明を添える

【原文】
(ここに翻訳したい文章を貼り付け)
```

「訳注として意訳箇所を説明させる」指示を入れておくと、訳者・レビュアーが後から「どこを意訳したか」を素早く確認でき、ポストエディットの時間を圧縮できる。

### 3. ポストエディット(PEMT)の進め方: ライトエディットとフルエディットの使い分け

機械翻訳(DeepLでも汎用LLMでも)の訳文をそのまま出さず、文書の重要度に応じて2段階のチェックを行う。

- **ライトエディット**: 誤訳・訳抜け・重大な文法ミスの有無だけを確認する軽いチェック。社内資料・参考訳向け
- **フルエディット**: 訳文のトーン・文体・専門用語の統一まで人手翻訳と同等の水準に仕上げるチェック。対外文書・契約関連文書向け

汎用LLMをポストエディットの補助に使う場合、以下のようなセルフチェックのプロンプトが有効。

```
以下は原文とその機械翻訳の訳文です。
1. 誤訳・訳抜け・数値や固有名詞の取り違えがないか原文と突き合わせて指摘
2. 不自然な直訳表現(原語の語順・言い回しをそのまま引きずっている箇所)を指摘
3. 用語集([用語集の内容を貼り付け])と異なる訳語を使っている箇所を指摘
4. 修正案を「原文の該当箇所」「現状の訳」「修正案」の3列で一覧表示

【原文】(貼り付け)
【機械翻訳の訳文】(貼り付け)
```

出てきた指摘はあくまで「レビューの叩き台」であり、最終判断は人(翻訳担当者)が行う。AI自身の指摘にも誤りが混ざりうるため、鵜呑みにしない。

### 4. リアルタイム会議翻訳: Zoom / Teams / Google Meetの設定場所

| ツール | 機能名 | 画面の場所 | 2026年8月時点の状況 |
|---|---|---|---|
| Zoom | AI Companionのリアルタイム字幕翻訳/音声翻訳(ベータ) | 会議中の「字幕」ボタン→「翻訳された字幕」→翻訳先言語を選択 | 字幕翻訳は46言語に対応。音声そのものをAI音声で翻訳する「Voice Translator」は2026年4月にベータ提供開始し、8月時点も英語・中国語・日本語・スペイン語・フランス語の5言語のまま(米国アカウントの有料プラン向け)。アラビア語は2026年第4四半期に追加予定、ドイツ語・イタリア語・ポルトガル語も追って追加予定([The National](https://www.thenationalnews.com/future/technology/2026/07/24/zoom-launches-live-voice-translation-with-arabic-coming-in-late-2026/))。話者が長く話し続けると訳出が話者の発話終了後にずれ込むという制約は変わらず残る([Slator](https://slator.com/zoom-brings-ai-live-speech-translation-in-house/)) |
| Microsoft Teams | ライブ翻訳字幕(Live Translated Captions) | 会議中の「その他の操作」→「字幕の言語を変更」→翻訳先言語を選択 | 約40の音声言語を約100の字幕言語に翻訳。参加者ごとに個別の言語を選べる。Teams Premium(月額10ドル程度のアドオン)またはMicrosoft 365 E5が必要で、主催者がライセンスを持っていれば参加者は無料で使える場合がある([Microsoftサポート](https://support.microsoft.com/en-us/teams/meetings/use-live-captions-in-microsoft-teams-meetings)) |
| Google Meet | Gemini 3.5 Live Translateの音声翻訳 | Google翻訳アプリのライブ翻訳機能、Meet内のGemini連携 | 2026年6月に発表された「Gemini 3.5 Live Translate」は、話者の声色・抑揚を保ったまま数秒の遅延でほぼ同時通訳に近い音声翻訳を実現。8月時点でGoogle Meetへの展開は法人向けの非公開プレビュー段階で、2026年後半に70言語以上・2,000以上の言語ペアへ段階的に一般提供を拡大する計画([ITmedia](https://www.itmedia.co.jp/news/articles/2606/10/news060.html)、[Impress Watch](https://www.watch.impress.co.jp/docs/news/2115950.html)) |
| DeepL Voice for Meetings | 専用の会議向けリアルタイム音声翻訳 | Teams/Zoom/Google Meetに参加者として招待、各自が自分の言語で発話・聴取 | 法人向け(50ライセンスからの契約が前提)。会議データは一時的にメモリ上で処理され、通話終了後に削除される設計([DeepL](https://www.deepl.com/ja/products/voice/deepl-voice-for-meetings)、[一創](https://www.issoh.co.jp/tech/details/11652/)) |
| Timekettle X1 Meeting Interpreter Hub | ウェアラブル型AI通訳デバイス(ハードウェア) | 会議室に専用ハブを設置し、参加者が各自のスマホ/イヤホンで接続 | 2026年6月発表。最大50人が参加する会議で52言語・106アクセントに対応し、対面・ハイブリッド双方の多言語会議に使える([PR Newswire](https://www.prnewswire.com/news-releases/timekettle-introduces-x1-meeting-interpreter-hub-bringing-real-time-ai-translation-to-global-meetings-of-up-to-50-participants-302805394.html)) |

一対一の簡単な会話であれば、ChatGPTのAdvanced Voice Modeに「あなたは同時通訳者です。日本語を聞いたら英語に、英語を聞いたら英語以外の発言は一切せず翻訳のみ行ってください」と役割指定するだけでも実用的に使える(詳細は[主要AIチャットツールの音声対話機能比較](../part03-ai-chat-tools/ai-chat-tools-voice-comparison.md)を参照)。

### 5. 字幕・吹き替え(動画翻訳)のツール比較

研修動画・製品紹介動画・ウェビナー録画などを多言語展開する場合、専用の動画翻訳AIが実務的。

| ツール | 特徴 | 料金の目安(2026年8月時点) |
|---|---|---|
| HeyGen(Video Translate) | 175以上の言語・方言に対応し、話者の口の動きに合わせるリップシンクの精度が高い | 無料プランは月3本まで(1本3分以内)。有料プランは月額$24〜(上位プランは1シートあたり月$39〜)([HeyGen比較記事](https://www.heygen.com/blog/heygen-vs-elevenlabs-vs-rask-ai-vs-dubverse)) |
| ElevenLabs Dubbing(Dubbing v2) | 話者本来のトーン・間・感情表現を保持した吹き替え音声の自然さに強み | 月額$22〜、または1分あたり0.18ドル程度の従量課金([プレスリリース](https://prtimes.jp/main/html/rd/p/000000045.000160611.html)) |
| Rask AI | 130以上の言語に対応、複数話者の識別・話者分離に強み | 基本翻訳は月額$19〜、リップシンクを含むプランは月額$50〜120程度 |
| mimidub(Titan Intelligence、国内サービス) | 話者本人の声質・話し方の癖・感情表現までを再現する動画吹き替えAI。2026年5月に約200言語対応で正式リリース | 従来の吹き替え制作に比べてコストを最大90%削減、監修込みで最短3日納品と案内([ASCII STARTUP](https://ascii.jp/elem/000/004/403/4403603/)、[AI Watch](https://ai.watch.impress.co.jp/docs/news/2109555.html)) |

いずれも字幕・音声のドラフトを高速に作れる点が価値だが、専門用語・固有名詞・自社製品名の訳し分けは人によるチェックが必須([bibigpt](https://bibigpt.co/en/blog/posts/ai-video-dubbing-translation-tools-2026-guide))。mimidubのように話者本人の声を再現するサービスを使う場合は、話者(タレント・声優等)本人からの利用許諾を得て権利処理を行うことが前提になる。

### 料金の目安(2026年8月時点)

| ツール | 主なプラン | 目安料金 |
|---|---|---|
| DeepL Pro(文書翻訳) | Starter/Advanced/Ultimate | 月1,200円/3,800円/7,500円程度(いずれも個人向け、年払い時) |
| DeepL API | Developer/Growth | Developerは無料(月100万文字まで)、Growthは月26ドル〜(年間1,200万文字まで、超過分は100万文字あたり27.5ドル)。旧プランのAPI Free/API Proは新規契約終了([eesel AI](https://www.eesel.ai/blog/deepl-pricing)) |
| DeepL Voice for Meetings | 法人向け(要問い合わせ) | 50ライセンスからの契約が前提、用途・翻訳量に応じた個別見積もり |
| Timekettle X1 Meeting Interpreter Hub | 法人向けハードウェア | デバイス購入+ライセンスの組み合わせ、要問い合わせ |
| ChatGPT/Gemini/Claude(翻訳・通訳補助として利用) | Plus/Pro等の既存契約枠内 | 追加コストなしで翻訳・通訳補助に流用可能なことが多い |

## 注意点・よくある誤解

- **契約書・NDA対象文書を無料版・個人契約の生成AIに貼らない**: 契約書には取引条件・当事者名など秘密性の高い情報が含まれる。無料版・個人向けプランには法人向けのNDAやデータ処理契約(DPA)が結ばれていないことが多く、入力内容が学習に使われるリスクもゼロではない。法人契約でオプトアウト設定(学習に使わない設定)が確認できているツール、またはDeepL Proのように一時処理・非保存を明記しているサービスに限定する(詳細は[生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md))。
- **公式通訳・法廷通訳・医療通訳をAIで代替しない**: リアルタイムAI翻訳は「あれば助かる補助」であり、誤訳が許されない公式記録・法的手続き・医療現場では有資格の専門通訳者を必ず起用する。
- **機械翻訳は「一貫性」に弱点がある**: 同じ用語でも文脈によって訳語が変わってしまうことがあるため、繰り返し登場する専門用語・製品名は必ず用語集(グロッサリー)に登録し、都度の指示に頼らない仕組みにしておく。
- **音声翻訳には数秒の遅延がある**: Zoom Voice Translator・Gemini Live Translateなどのリアルタイム音声翻訳は、話者の発話が長く続くと訳出が遅れて追いつかなくなることがある。商談・交渉など間合いが重要な場面では、話者が短く区切って話す運用ルールを事前に共有しておくとよい。
- **AIの訳文は「対外発信可能な完成品」ではない**: 字幕・吹き替え・公開文書に使う訳文は、必ず人(できればネイティブスピーカーまたはプロ翻訳者)が通しでチェックしてから公開する。特に固有名詞・数値・法令名の誤りは、[ハルシネーションの仕組みと対策](../part04-risk-security/hallucination-and-countermeasures.md)で扱う「もっともらしい誤り」がそのまま対外的な誤情報になるリスクが高い領域である。
- **逆翻訳(バックトランスレーション)でのセルフチェックが有効**: 訳文を再度元の言語に翻訳させ、原文と意味がずれていないかを確認する手法は、契約書・規制文書のような重要文書のセルフチェックとして手軽に使える。
- **翻訳者は「ゼロから訳す力」より「AIの訳文を見抜く力」の比重が増している**: 求人動向が示すように翻訳・通訳の需要自体は縮小していないが、業務の中身はポストエディット(誤訳・不自然な直訳・用語集からのズレを見抜いて直す仕事)に重心が移っている。キャリア形成の観点では、専門分野の知識・用語集の運用力・AIの出力を素早く検証するレビュー力が、これまで以上に評価される力になる。

## 最初の一歩

自社でよく使う専門用語・製品名を10〜20個選び、DeepLの用語集(または汎用LLMへの指示文の定型テンプレート)に登録するところから始める。あわせて、次回の多言語会議でZoom/Teams/Google Meetいずれかのリアルタイム字幕翻訳を試しに有効化してみる。

## 関連トピック

- [生成AIによる文章作成・編集の実務活用](../part12-business-practice/ai-writing-and-editing.md)
- [主要AIチャットツールの音声対話機能比較(Advanced Voice Mode・Gemini Live等)](../part03-ai-chat-tools/ai-chat-tools-voice-comparison.md)
- [広報・PR職における生成AI活用事例](./pr-communications-ai-use-cases.md)
- [法務職における生成AI活用事例](./legal-ai-use-cases.md)
- [生成AI利用における情報漏洩対策](../part04-risk-security/information-leakage-prevention.md)
- [ハルシネーションの仕組みと対策](../part04-risk-security/hallucination-and-countermeasures.md)

## 更新履歴

### 2026-08-12: 2026年8月時点に最新化(リアルタイム通訳・字幕吹き替え・DeepL料金体系を更新)
- **内容**: (1)DeepL APIの旧プラン(API Free/API Pro)の新規契約終了とDeveloper/Growthプランへの一本化、DeepL Proの料金を最新値に更新。(2)リアルタイム通訳の最新動向として、中関村フォーラムのAR+AI同時通訳システム(54言語・1秒未満遅延)、Timekettle X1 Meeting Interpreter Hub(52言語・最大50人会議)を追加し、「AIが翻訳の大部分を担い人間が高度判断で介入する」協働モデルが業界標準化している点を明記。Zoom Voice Translator・Gemini 3.5 Live Translateの2026年8月時点の対応状況(言語数・展開フェーズ)を更新。(3)字幕・吹き替えAIに国内サービス「mimidub」(200言語対応、声質・感情再現、コスト最大90%削減)を追加し、他社(HeyGen/ElevenLabs/Rask AI)の料金も最新化。(4)厚労省の求人動向等を踏まえ、翻訳者の役割がポストエディター中心にシフトしている業界動向を「仕組み・背景」「注意点」に追記
- **出典**: [eesel AI: DeepL pricing in 2026](https://www.eesel.ai/blog/deepl-pricing)、[PR Newswire: Timekettle X1 Meeting Interpreter Hub](https://www.prnewswire.com/news-releases/timekettle-introduces-x1-meeting-interpreter-hub-bringing-real-time-ai-translation-to-global-meetings-of-up-to-50-participants-302805394.html)、[The National: Zoom launches live voice translation, with Arabic coming in late 2026](https://www.thenationalnews.com/future/technology/2026/07/24/zoom-launches-live-voice-translation-with-arabic-coming-in-late-2026/)、[ASCII STARTUP: mimidub 200言語対応で正式リリース](https://ascii.jp/elem/000/004/403/4403603/)、[AI Watch: mimidub対応言語拡大・正式リリース](https://ai.watch.impress.co.jp/docs/news/2109555.html)、[HeyGen: HeyGen vs ElevenLabs vs Rask AI vs Dubverse](https://www.heygen.com/blog/heygen-vs-elevenlabs-vs-rask-ai-vs-dubverse)、[通訳翻訳ジャーナル: 翻訳の仕事は増えた?減った?需要分析と予測](https://tsuhon.jp/professional/career/trend1/)、[クリムゾン・ジャパン: 翻訳家は将来いなくなる?](https://www.crimsonjapan.co.jp/blog/will-translators-disappear-in-the-future/)

### 2026-07-17: 初版執筆
- **内容**: 翻訳・通訳担当における生成AI活用として、DeepLと汎用LLM(ChatGPT/Gemini/Claude)・人間の翻訳者/通訳者の使い分け、DeepL用語集(グロッサリー)の設定手順、ポストエディット(PEMT/MTPE)のライト/フルエディット、Zoom/Teams/Google MeetのリアルタイムAI通訳機能の画面の場所と2026年時点の対応言語・料金、字幕・吹き替え(HeyGen/ElevenLabs Dubbing/Rask AI)の比較、契約書等の機密文書をAIに入力するリスクをコピペ用プロンプト例つきで整理
- **出典**: [intlpull: Machine Translation Accuracy 2026 Benchmark](https://intlpull.com/blog/machine-translation-accuracy-2026-benchmark)、[sintra.ai: DeepL vs ChatGPT](https://sintra.ai/blog/deepl-vs-chatgpt)、[eesel AI: An honest review of DeepL for business use](https://www.eesel.ai/blog/deepl)、[eesel AI: DeepL pricing in 2026](https://www.eesel.ai/blog/deepl-pricing)、[日本翻訳センター: ポストエディット](https://www.jtc.co.jp/post-editing/)、[Phrase: 機械翻訳ポストエディット(MTPE)](https://phrase.com/blog/posts/machine-translation-post-editing/)、[DeepLヘルプセンター: About the glossary](https://support.deepl.com/hc/en-us/articles/360021634540-About-the-glossary)、[Slator: Zoom Brings AI Live Speech Translation In-House](https://slator.com/zoom-brings-ai-live-speech-translation-in-house/)、[Microsoftサポート: Use live captions in Microsoft Teams meetings](https://support.microsoft.com/en-us/teams/meetings/use-live-captions-in-microsoft-teams-meetings)、[ITmedia: Gemini 3.5 Live Translate発表](https://www.itmedia.co.jp/news/articles/2606/10/news060.html)、[Impress Watch: "ほぼ同時"翻訳を実現 Gemini 3.5 Live Translate](https://www.watch.impress.co.jp/docs/news/2115950.html)、[DeepL: DeepL Voice for Meetings](https://www.deepl.com/ja/products/voice/deepl-voice-for-meetings)、[一創: DeepL Voiceの料金と2製品の違い](https://www.issoh.co.jp/tech/details/11652/)、[bibigpt: AI Video Dubbing & Translation Tools 2026](https://bibigpt.co/en/blog/posts/ai-video-dubbing-translation-tools-2026-guide)、[PR TIMES: ElevenLabs Dubbing v2発表](https://prtimes.jp/main/html/rd/p/000000045.000160611.html)、[kh-lawyer.com: 生成AIに機密情報を入力するとNDA違反になる?](https://kh-lawyer.com/2026/04/01/ai-nda-1/)
