---
title: "ガードレール(生成AIの入出力安全対策)の基本"
part: 4
chapter: 第2章 攻撃と防御
tags: [ガードレール, コンテンツモデレーション, AI安全対策, ジェイルブレイク対策]
created: 2026-07-06
updated: 2026-07-28
---

# ガードレール(生成AIの入出力安全対策)の基本

## これは何か

ガードレール(guardrail)とは、生成AIへの入力と生成AIからの出力を機械的にチェックし、有害な内容・個人情報・企業ポリシー違反・ジェイルブレイク(AIの制約を迂回する試み)らしき文言などを検知してブロックしたり、定型の返答に差し替えたりする仕組み全般を指す。社内でチャットボットやGPTs・Gemを作って社内外に公開する立場になると、「システムプロンプトに『不適切な発言はしない』と書いておけば大丈夫」という思い込みが最も危険であり、それとは別にAIの入口と出口を機械的に見張る層が必要になる。本ページでは、そのガードレールという防御の仕組みそのもの(モデレーションAPI、入出力フィルタ、専用の分類モデル・製品)を扱う。なお、AIを直接言葉で騙して制約を外させる「ジェイルブレイク」自体の手口や、第三者コンテンツ経由で乗っ取る「プロンプトインジェクション」との違いは[プロンプトインジェクションとは何か](prompt-injection-basics.md)で説明済みのため、本ページでは繰り返さない。

## 仕組み・背景

ガードレールは、置く場所によって大きく4種類に分けて考えると整理しやすい。

| 種類 | チェック対象 | 主な役割 | 代表的な実装例 |
|---|---|---|---|
| 入力フィルタ | ユーザーがAIに送った内容 | 有害な依頼・個人情報・ジェイルブレイク/インジェクションの試みをモデルに渡す前に検知 | OpenAI Moderation API(入力側)、Azure AI Content SafetyのPrompt Shields |
| システムプロンプトでの制約 | モデルの挙動そのもの | 応答してよい話題・トーン・禁止事項をあらかじめ指示文で規定する | GPTsのInstructions、Gemの「カスタム指示」、Copilot Studioの「指示」欄 |
| 出力フィルタ | モデルが生成した内容 | 有害表現・個人情報の漏洩・事実に基づかない内容(ハルシネーション)・著作物の丸ごと引用などを、利用者に届く前に検知 | OpenAI Moderation API(出力側)、Azure AI Content Safetyの出力チェック・Groundedness Detection(根拠確認) |
| 専用の分類モデル(ガードレールモデル) | 入力・出力の両方、または会話全体 | 有害性・トピック逸脱・ジェイルブレイクを、応答を生成する本体のAIとは別のAIモデルに判定させる | Meta「Llama Guard」、NVIDIA「NeMo Guardrails」、Anthropicの分類器(Constitutional Classifiers) |

技術的な中身は大きく2系統ある。1つは「キーワード・正規表現によるルールベースのフィルタ」で、NGワードを機械的に検出する単純な仕組み。もう1つは「分類モデル(classifier)による判定」で、文章を読んで「暴力」「性的」「自傷」「ヘイト」といったカテゴリごとに危険度スコアを出し、しきい値を超えたらブロックする方式である。OpenAIのModeration APIは後者にあたり、テキストと画像を対象に、暴力・自傷・性的・ヘイト・ハラスメントなど十数カテゴリを判定して無料で提供している。Azure AI Content Safetyも「ヘイト」「性的」「暴力」「自傷」の4カテゴリについて、それぞれ0〜7段階の深刻度(セブリティ)を返す方式で、しきい値をどこに置くかを利用側が選べる。近年はさらに、Anthropicの「Constitutional Classifiers(憲法的分類器)」のように、モデル内部の活性化パターンを読み取って怪しい会話だけを重い判定にエスカレーションする効率重視の方式や、Meta「Llama Guard」・NVIDIA「NeMo Guardrails」のように分類専用の小型AIモデルを自社システムの前段・後段に自分で組み込む方式も普及している。

いずれの方式も「絶対的な正解」を判定しているわけではなく、確率的なスコアにしきい値を設けているに過ぎない。しきい値を厳しくすれば誤ブロック(過検知)が増え、緩めれば見逃し(過小検知)が増えるというトレードオフが常にある。

## 使いどころ・使い分け

自社でAIチャットボットやGPTs・Gemを公開する際、どこまでガードレールを厚くすべきかは「公開範囲」と「扱う情報・話題のリスク」で判断するとよい。

| 公開するAIの性質 | 想定リスク | 最低限入れるべきガードレール |
|---|---|---|
| 社内限定・雑談やアイデア出し用 | 低い | システムプロンプトでの制約のみで足りることが多い |
| 社内向けFAQボット・社内文書検索(RAG) | 中程度 | 上記+出力フィルタ(社内文書に含まれる個人情報・機密情報が答えに漏れ出さないかのチェック) |
| 社外顧客向けに公開する窓口ボット(会社の顔になる) | 中〜高い | 上記+入力・出力両方でモデレーションAPIを通す。炎上リスクのある発言を機械的にブロック |
| 医療・金融・法律など専門領域の相談対応 | 高い | 上記+事実性チェック(ハルシネーション検知)、専門外の話題への逸脱防止(トピック制御) |
| 社内システムや機密データにアクセスするエージェント型AI | 非常に高い | 上記+PII(個人を特定できる情報)検出、送信・実行前の人間による確認ステップ([プロンプトインジェクションとは何か](prompt-injection-basics.md)の権限設計と合わせて検討) |

「厚くすればするほど良い」わけでもない点に注意する。モデレーションのしきい値を厳しくしすぎると、業務上正当な質問(たとえば医療従事者向けの症例相談)まで過剰にブロックしてしまい、ユーザー体験を損なう。公開範囲が狭く、扱う話題のリスクが低いAIにまで重厚なガードレールを積む必要はない。

## 実務での使い方

### 主要ツールでの設定場所(ツール横断の対応付け)

| 概念・機能 | ChatGPT(GPTs) | Gemini(API/Vertex AI) | Microsoft Copilot Studio | Dify |
|---|---|---|---|---|
| 入力側のブロック設定 | GPTs自体には専用UIはなく、Instructions欄で防御指示を書く。API経由で自作する場合はOpenAI Moderation API/OpenAI Guardrails(後述)を自分のシステムの前段に組み込む | APIリクエストの`safetySettings`パラメータで、ヘイト・ハラスメント・性的・危険コンテンツなど4カテゴリごとに`HarmBlockThreshold`(しきい値)を指定 | 「生成AIの調整」画面の「コンテンツモデレーションレベル」スライダー(低〜高、既定は「中」) | アプリの「オーケストレーション」画面→「機能」→「モデレーション」で、OpenAI Moderation APIまたは自作のキーワードリストを選択 |
| 出力側のブロック設定 | 上記と同様、Instructionsでの制約が中心 | 同上(入力・出力どちらの候補にも同じしきい値が適用される) | 同上のスライダーで入出力ともに一括制御 | モデレーション画面で「出力の審査」を個別にON/OFF、検知時の定型応答文を設定可能 |
| 検知時の挙動のカスタマイズ | Instructionsで「その内容にはお答えできません、とだけ返す」のように明示 | ブロック時は空の候補やエラーが返るため、アプリ側でハンドリングが必要 | ブロック時のメッセージをトピックのフローで作り込み可能 | 「プリセットの返信文」を自由に設定できる(例:「この内容はご案内できません」) |

### 専用のガードレール製品・ライブラリ

自作のAIチャットボットやAPI連携で使う場合、次のような専用の製品・OSSが選択肢になる。

| 製品・ライブラリ | 提供元 | 特徴 |
|---|---|---|
| Moderation API / OpenAI Guardrails(Python) | OpenAI | Moderation APIはテキスト・画像を無料で判定できる分類API。2026年時点の最新モデルは`omni-moderation-latest`で、性的・ヘイト・暴力・自傷・違法行為など十数カテゴリを100以上の言語で判定。加えて「OpenAI Guardrails」というOSSライブラリ(MITライセンス)が公開されており、モデレーション・PII検出・ジェイルブレイク検出・ハルシネーション検知などを組み合わせて自分のOpenAI API利用に薄いラッパーとしてかぶせられる |
| Azure AI Content Safety | Microsoft | ヘイト・性的・暴力・自傷の4カテゴリを0〜7段階のセブリティで判定する基本機能に加え、ジェイルブレイク・間接的プロンプトインジェクションを検知する「Prompt Shields」、生成内容が根拠資料と矛盾していないかを確認する「Groundedness Detection」、個人情報検出などをそろえた総合サービス。Azure OpenAI/Foundry上のモデル呼び出しには既定で組み込まれている |
| Llama Guard(4) | Meta | 12BパラメータのオープンウェイトAIモデルで、テキスト・画像を対象に有害性を判定する専用の分類モデル。MLCommonsの標準有害カテゴリに準拠し、自社サーバーやNVIDIA NIM経由でホストして、自作システムの前段・後段に置く用途で使われる |
| NeMo Guardrails | NVIDIA | LLMアプリに「話してよい話題(トピック制御)」「個人情報の検出」「RAGの回答が参照資料に基づいているかの確認」「ジェイルブレイク検出」などをルールとして定義・組み込めるOSSのオーケストレーションツールキット。LangChainやLangGraphと連携しやすい |
| Constitutional Classifiers(憲法的分類器) | Anthropic | Claudeの入出力を監視し、あらかじめ定めた「憲法(許可される内容・禁止される内容を定めた自然言語のルール)」から合成データを作って訓練した分類器で有害なやり取りを検知する仕組み。最新世代はモデル内部の活性化情報を読み取る軽量な一次判定と、怪しいものだけを重い判定に回す二段構えで、追加コストを抑えつつ精度を上げている |

### コピペで使える設計チェックリスト

自社でAIチャットボット・GPTs・Gemを公開する前に、次を1つずつ埋めていくと抜け漏れが減る。

```
□ 入力フィルタ: 有害・機密・ジェイルブレイク的な入力を検知する仕組みがあるか
  (モデレーションAPI/Prompt Shields/キーワードフィルタのいずれか)
□ システムプロンプト: 応答してよい話題・トーン・禁止事項を明記しているか
□ 出力フィルタ: 生成された回答を利用者に届ける前にチェックしているか
  (個人情報・機密情報・ハルシネーション・著作物の丸ごと引用など)
□ 検知時の挙動: ブロックされた場合に、理由を詳しく説明せず定型文で断る設計になっているか
□ ログ: 何がブロックされたかを後から確認できる記録が残るか
□ 人間の確認: 送信・決済・削除など取り消せない操作の前に承認ステップがあるか
```

## 注意点・よくある誤解

- **「ガードレールを設定したから100%安全」ではない**: モデレーションAPIも分類モデルも確率的な判定であり、巧妙な言い回し(遠回しな表現、外国語への切り替え、文字を分割するなど)で回避される事例が継続的に報告されている。Anthropicが公表する研究でも、対策前に86%だったジェイルブレイク成功率を分類器で4.4%まで下げたと報告されているが、ゼロにはなっていない。「導入した」ことと「防げている」ことは別問題だと理解しておく。2026年7月には、AIの応答側に偽の同意メッセージを差し込む「assistant prefill」を悪用した手口(通称Sockpuppeting)が11の主要LLM横断で報告され、モデルによって突破率にばらつき(報告値でGemini 2.5 Flash 15.7%、Claude 4 Sonnet 8.3%、GPT-4o 1.4%)があることも示された。ガードレール製品を導入していても、こうした新しい回避手口が継続的に見つかる前提で運用する
- **ガードレールが「厳しすぎて」正当な業務を止めてしまう場合もある**: 2026年7月に報告されたある事例では、大量の攻撃ログをAI分析エージェントに読み込ませてインシデント調査(フォレンジック)をしようとした際、防御側であるはずのセキュリティ担当者の利用を、商用フロンティアモデルのガードレールが「攻撃的な内容」と誤認してブロックしてしまった。ガードレールは攻撃者だけでなく防御側の正当な利用も止めうる点を踏まえ、社内でこうした専門的な調査用途に使う場合は、より緩いモデレーション設定や専用の審査プロセスを用意しておくと業務が止まらない
- **多層防御(defense in depth)が前提**: 上記の理由から、実務では「1つの仕組みで完全に防ぐ」のではなく、入力フィルタ・システムプロンプト・出力フィルタ・人間の確認ステップを重ねて、どれか1つが突破されても次の層で止める設計が基本になる。Azure AI Content Safetyのドキュメントも、Prompt Shields(入口)・Task Adherence(実行中)・PII検出(出口)を組み合わせる考え方を「defense in depth」と明示している。
- **しきい値のチューニングが必要**: しきい値を厳しくしすぎると業務上正当な発言まで誤ブロックし(過検知)、緩めすぎると有害な内容を見逃す(過小検知)。公開後もブロックログを確認し、誤検知が多ければしきい値やルールを調整する運用が必要になる。
- **ガードレールとジェイルブレイク対策は別物ではなく重なる**: 本ページで扱う入出力フィルタや分類モデルは、ジェイルブレイクや間接的プロンプトインジェクションに対する防御層の1つでもある。個々の攻撃手口の理解は[プロンプトインジェクションとは何か](prompt-injection-basics.md)、GPTs固有の防御指示の書き方は[GPTsにおけるプロンプトインジェクション対策](../part06-custom-ai/gpts-prompt-injection-defense.md)を参照し、本ページの内容と組み合わせて使う。
- **コスト・レイテンシも考慮する**: 専用の分類モデルや複数段階のチェックを挟むほど、応答までの時間とAPIコストが増える。すべてのAIに最重量級のガードレールを積む必要はなく、前述の「使いどころ・使い分け」の表でリスクに見合った層を選ぶ。

## 最初の一歩

自社で公開しているAIチャットボット・GPTs・Gemについて、前述の「コピペで使える設計チェックリスト」の6項目にいくつ✓が付くかを今すぐ確認する。入力フィルタ・出力フィルタのどちらもシステムプロンプトの指示文だけに頼っているなら、まずは無料で使えるOpenAI Moderation APIか、利用中のクラウドが提供するモデレーション機能(Azure AI Content Safety、Copilot Studioのコンテンツモデレーションレベルなど)を1つ追加することから始める。

## 関連トピック

- [プロンプトインジェクションとは何か(仕組みと対策)](prompt-injection-basics.md)
- [GPTsにおけるプロンプトインジェクション対策](../part06-custom-ai/gpts-prompt-injection-defense.md)

## 更新履歴

### 2026-07-28: 新しい回避手口と防御側の誤検知事例を追記
- **内容**: 2026年7月に報告された「assistant prefill」を悪用したジェイルブレイク手口(通称Sockpuppeting、11の主要LLM横断で報告)と、防御側のフォレンジック調査がガードレールに誤ってブロックされた事例を注意点に追記
- **出典**: [Trend Micro: Sockpuppeting - How a Single Line Can Bypass LLM Safety Guardrails](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/sockpuppeting-how-a-single-line-can-bypass-llm-safety-guardrails)、[malware.news: The Guardrails Problem Just Played Out on Both Sides of the Same Incident](https://malware.news/t/the-guardrails-problem-just-played-out-on-both-sides-of-the-same-incident/124212)

### 2026-07-06: 初版執筆
- **内容**: ガードレールを「入力フィルタ」「システムプロンプトでの制約」「出力フィルタ」「専用の分類モデル」の4種類に整理し、公開範囲・リスクに応じた使い分けの判断基準、ChatGPT(GPTs)・Gemini・Copilot Studio・Difyの設定箇所の対応表、OpenAI Moderation API/OpenAI Guardrails・Azure AI Content Safety・Llama Guard・NeMo Guardrails・Anthropic Constitutional Classifiersといった専用製品/ライブラリの比較、多層防御(defense in depth)の考え方を整理
- **出典**: [OpenAI: Moderation guide](https://developers.openai.com/api/docs/guides/moderation)、[OpenAI: omni-moderation-latest model](https://developers.openai.com/api/docs/models/omni-moderation-latest)、[OpenAI Guardrails Python (GitHub)](https://github.com/openai/openai-guardrails-python)、[Microsoft Learn: Prompt Shields in Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection)、[Azure AI Content Safety 製品ページ](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety)、[NVIDIA NeMo Guardrails (GitHub)](https://github.com/NVIDIA-NeMo/Guardrails)、[NVIDIA Developer: NeMo Guardrails Library](https://developer.nvidia.com/nemo-guardrails)、[Meta: Llama Guard 4 12B Model Card (GitHub)](https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard4/12B/MODEL_CARD.md)、[Anthropic: Constitutional Classifiers](https://www.anthropic.com/research/constitutional-classifiers)、[Anthropic: Next-generation Constitutional Classifiers](https://www.anthropic.com/research/next-generation-constitutional-classifiers)、[Microsoft Learn: モデルのバージョンと設定を変更する(Copilot Studio)](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/prompt-model-settings)、[Microsoft Support: Microsoft 365 Copilot Chatの有害なコンテンツ保護設定](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/harmful-content-protection-copilot-chat)、[Dify Docs: Moderation Tool](https://docs.dify.ai/en/guides/application-orchestrate/app-toolkits/moderation-tool)、[Google AI for Developers: Safety settings (Gemini API)](https://ai.google.dev/gemini-api/docs/safety-settings)
