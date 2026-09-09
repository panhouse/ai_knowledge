---
title: "ガードレール(生成AIの入出力安全対策)の基本"
part: 4
chapter: 第2章 攻撃と防御
tags: [ガードレール, コンテンツモデレーション, AI安全対策, ジェイルブレイク対策]
created: 2026-07-06
updated: 2026-09-09
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

技術的な中身は大きく2系統ある。1つは「キーワード・正規表現によるルールベースのフィルタ」で、NGワードを機械的に検出する単純な仕組み。もう1つは「分類モデル(classifier)による判定」で、文章を読んで「暴力」「性的」「自傷」「ヘイト」といったカテゴリごとに危険度スコアを出し、しきい値を超えたらブロックする方式である。OpenAIのModeration APIは後者にあたり、現行モデル`omni-moderation-latest`(2026年9月時点)はGPT-4o相当の基盤でテキスト・画像を対象に13カテゴリ(7カテゴリはテキストのみ、6カテゴリは画像も対応)を判定し、無料・低遅延(応答目安20ミリ秒程度)で提供されている。Azure AI Content Safetyも「ヘイト」「性的」「暴力」「自傷」の4カテゴリについて、それぞれ0〜7段階の深刻度(セブリティ)を返す方式で、しきい値をどこに置くかを利用側が選べる。近年はさらに、Anthropicの「Constitutional Classifiers(憲法的分類器)」のように、モデル内部の活性化パターンを読み取って怪しい会話だけを重い判定にエスカレーションする効率重視の方式や、Meta「Llama Guard」・NVIDIA「NeMo Guardrails」のように分類専用の小型AIモデルを自社システムの前段・後段に自分で組み込む方式も普及している。Llama Guardは2026年9月時点、マルチモーダル対応の大型モデル「Llama Guard 4」(12Bパラメータ)と、より軽量な「Llama Prompt Guard 2」(86Mパラメータ)を組み合わせ、まず高速な一次フィルタで大半のリクエストをさばき、怪しいものだけをLlama Guardの詳細判定に回す2段構成が実務での定番になっている。

いずれの方式も「絶対的な正解」を判定しているわけではなく、確率的なスコアにしきい値を設けているに過ぎない。しきい値を厳しくすれば誤ブロック(過検知)が増え、緩めれば見逃し(過小検知)が増えるというトレードオフが常にある。

## 使いどころ・使い分け

自社でAIチャットボットやGPTs・Gemを公開する際、どこまでガードレールを厚くすべきかは「公開範囲」と「扱う情報・話題のリスク」で判断するとよい。

| 公開するAIの性質 | 想定リスク | 最低限入れるべきガードレール |
|---|---|---|
| 社内限定・雑談やアイデア出し用 | 低い | システムプロンプトでの制約のみで足りることが多い |
| 社内向けFAQボット・社内文書検索(RAG) | 中程度 | 上記+出力フィルタ(社内文書に含まれる個人情報・機密情報が答えに漏れ出さないかのチェック) |
| 社外顧客向けに公開する窓口ボット(会社の顔になる) | 中〜高い | 上記+入力・出力両方でモデレーションAPIを通す。炎上リスクのある発言を機械的にブロック |
| 医療・金融・法律など専門領域の相談対応 | 高い | 上記+事実性チェック(ハルシネーション検知)、専門外の話題への逸脱防止(トピック制御) |
| 社内システムや機密データにアクセスするエージェント型AI | 非常に高い | 上記+PII(個人を特定できる情報)検出、送信・実行前の人間による確認ステップ、外部ツール呼び出し(MCP・エージェント間通信)経由で入り込む悪意ある指示のゲートウェイ側チェック([プロンプトインジェクションとは何か](prompt-injection-basics.md)の権限設計と合わせて検討) |

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
| Moderation API / OpenAI Guardrails(Python) | OpenAI | Moderation APIはテキスト・画像を無料・低遅延で判定できる分類API。2026年9月時点の最新モデルは`omni-moderation-latest`(GPT-4o相当の基盤)で、性的・ヘイト・暴力・自傷・違法行為など13カテゴリを100以上の言語で判定(うち6カテゴリは画像入力にも対応)。加えて「OpenAI Guardrails」というOSSライブラリ(MITライセンス)が公開されており、モデレーション・PII検出(Microsoft Presidioを内部で利用)・ジェイルブレイク検出(役割詐称・難読化・複数ターンにまたがる誘導などをLLMベースで判定)・ハルシネーション検知(自社のナレッジベースと照合)を組み合わせ、違反検知時に処理を即座に止める「トリップワイヤ」機能とともに、自分のOpenAI API利用に薄いラッパーとしてかぶせられる |
| Azure AI Content Safety | Microsoft | ヘイト・性的・暴力・自傷の4カテゴリを0〜7段階のセブリティで判定する基本機能に加え、ジェイルブレイク・間接的プロンプトインジェクションを検知する「Prompt Shields」、生成内容が根拠資料と矛盾していないかを確認する「Groundedness Detection」、個人情報検出などをそろえた総合サービス。Azure OpenAI/Foundry上のモデル呼び出しには既定で組み込まれている。2026年6月(Microsoft Build 2026)には、Azure API ManagementのAIゲートウェイ機能としてPrompt Shieldsの適用範囲がMCP(Model Context Protocol)のツール呼び出し引数・応答やエージェント間通信(A2A)のペイロードにまで拡張され、エージェント型AIが外部ツール経由で悪意ある指示を読み込むケースをゲートウェイ側で検知できるようになった。料金は標準(S0)ティアでテキスト1,000件あたり0.38米ドル程度(2026年1月時点の目安値、実際は地域・為替で変動)で、無料枠として月5,000件のテキスト・画像判定が付く |
| Llama Guard(4)/ Llama Prompt Guard(2) | Meta | Llama Guard 4は12Bパラメータのマルチモーダル対応オープンウェイトAIモデルで、テキスト・画像を対象に有害性を判定する専用の分類モデル。MLCommonsの標準有害カテゴリに準拠し、自社サーバーやNVIDIA NIM経由でホストして、自作システムの前段・後段に置く用途で使われる。2026年9月時点では、86Mパラメータの軽量モデル「Llama Prompt Guard 2」を一次フィルタとして先に通し、怪しいものだけをLlama Guardの詳細判定に回す2段構成が一般的 |
| NeMo Guardrails | NVIDIA | LLMアプリに「話してよい話題(トピック制御)」「個人情報の検出」「RAGの回答が参照資料に基づいているかの確認」「ジェイルブレイク検出」などをColang(独自の対話記述言語)のルールとして定義・組み込めるOSSのオーケストレーションツールキット。LangChainやLangGraphと連携しやすい。2026年時点ではAPIベースで呼び出せるマイクロサービス版も提供され、GPU上で1チェックあたり50ミリ秒未満という低遅延で、PIIのマスキングやダイアログの状態管理までまとめて処理できる |
| Constitutional Classifiers(憲法的分類器)/ Enterprise Frontier Safeguards | Anthropic | Claudeの入出力を監視し、あらかじめ定めた「憲法(許可される内容・禁止される内容を定めた自然言語のルール)」から合成データを作って訓練した分類器で有害なやり取りを検知する仕組み。モデル内部の活性化情報を読み取る軽量な一次判定と、怪しいものだけを重い判定に回す二段構えで、追加コストを抑えつつ精度を上げている。2026年6月のClaude Fable 5では、サイバーセキュリティ・生物/化学・モデル蒸留などリスクの高い話題を検知した会話だけを、より非力な代替モデルに振り分ける「分類器スタック」を採用。2026年9月のClaude Fable 5.1/Mythos 5.1では、この防御網が「Enterprise Frontier Safeguards(EFS)」という名称の単体機能として明示化され、誤ブロック(過検知)の低減に加え、データをAnthropicではなく顧客自身のクラウド環境に置いたままにできるゼロデータ保持契約や、不審な利用の一次レビューを顧客側で行える運用まで含む企業向けの安全策パッケージとして提供されている(2026年内はAWS・Google・Microsoft Foundry等への段階展開中) |

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
□ (エージェント型の場合)ツール呼び出し: MCP経由の外部ツールの引数・応答やエージェント間通信(A2A)にも、
  入出力フィルタと同等のチェックがゲートウェイ層でかかっているか
```

## 注意点・よくある誤解

- **「ガードレールを設定したから100%安全」ではない**: モデレーションAPIも分類モデルも確率的な判定であり、巧妙な言い回し(遠回しな表現、外国語への切り替え、文字を分割するなど)で回避される事例が継続的に報告されている。Anthropicが公表する研究でも、対策前に86%だったジェイルブレイク成功率を分類器で4.4%まで下げたと報告されているが、ゼロにはなっていない。「導入した」ことと「防げている」ことは別問題だと理解しておく。2026年7月には、AIの応答側に偽の同意メッセージを差し込む「assistant prefill」を悪用した手口(通称Sockpuppeting)が11の主要LLM横断で報告され、モデルによって突破率にばらつき(報告値でGemini 2.5 Flash 15.7%、Claude 4 Sonnet 8.3%、GPT-4o 1.4%)があることも示された。ガードレール製品を導入していても、こうした新しい回避手口が継続的に見つかる前提で運用する
- **ガードレールが「厳しすぎて」正当な業務を止めてしまう場合もある**: 2026年7月に報告されたある事例では、大量の攻撃ログをAI分析エージェントに読み込ませてインシデント調査(フォレンジック)をしようとした際、防御側であるはずのセキュリティ担当者の利用を、商用フロンティアモデルのガードレールが「攻撃的な内容」と誤認してブロックしてしまった。ガードレールは攻撃者だけでなく防御側の正当な利用も止めうる点を踏まえ、社内でこうした専門的な調査用途に使う場合は、より緩いモデレーション設定や専用の審査プロセスを用意しておくと業務が止まらない。ベンダー側もこの誤検知(過検知)を課題視しており、Anthropicは2026年9月のClaude Fable 5.1で防御網を強化しつつ誤ブロックの低減を図ったと発表しているが、「新しいバージョンだから誤検知が起きない」と過信せず、自社の実利用でブロックログを確認する運用は変わらず必要
- **エージェント型AIでは、外部ツール経由の入力もチェック対象になる**: MCP(Model Context Protocol)でつないだ外部ツールの応答や、エージェント同士が直接やり取りするA2A(agent-to-agent)通信の中に悪意ある指示が埋め込まれていると、ユーザーの入力を見張るだけの入力フィルタでは気づけない。Microsoftは2026年6月、Azure API ManagementのAIゲートウェイ機能としてPrompt Shieldsの検査対象をMCPのツール呼び出し・A2Aペイロードにまで広げており、社内でエージェント型AIを運用する場合はチャット窓口だけでなく、こうしたツール呼び出しの経路にもガードレールを及ばせる設計が必要になる
- **多層防御(defense in depth)が前提**: 上記の理由から、実務では「1つの仕組みで完全に防ぐ」のではなく、入力フィルタ・システムプロンプト・出力フィルタ・人間の確認ステップを重ねて、どれか1つが突破されても次の層で止める設計が基本になる。Azure AI Content Safetyのドキュメントも、Prompt Shields(入口)・Task Adherence(実行中)・PII検出(出口)を組み合わせる考え方を「defense in depth」と明示している。
- **しきい値のチューニングが必要**: しきい値を厳しくしすぎると業務上正当な発言まで誤ブロックし(過検知)、緩めすぎると有害な内容を見逃す(過小検知)。公開後もブロックログを確認し、誤検知が多ければしきい値やルールを調整する運用が必要になる。
- **ガードレールとジェイルブレイク対策は別物ではなく重なる**: 本ページで扱う入出力フィルタや分類モデルは、ジェイルブレイクや間接的プロンプトインジェクションに対する防御層の1つでもある。個々の攻撃手口の理解は[プロンプトインジェクションとは何か](prompt-injection-basics.md)、GPTs固有の防御指示の書き方は[GPTsにおけるプロンプトインジェクション対策](../part06-custom-ai/gpts-prompt-injection-defense.md)を参照し、本ページの内容と組み合わせて使う。
- **コスト・レイテンシも考慮する**: 専用の分類モデルや複数段階のチェックを挟むほど、応答までの時間とAPIコストが増える。すべてのAIに最重量級のガードレールを積む必要はなく、前述の「使いどころ・使い分け」の表でリスクに見合った層を選ぶ。

## 最初の一歩

自社で公開しているAIチャットボット・GPTs・Gemについて、前述の「コピペで使える設計チェックリスト」の各項目にいくつ✓が付くかを今すぐ確認する。入力フィルタ・出力フィルタのどちらもシステムプロンプトの指示文だけに頼っているなら、まずは無料で使えるOpenAI Moderation APIか、利用中のクラウドが提供するモデレーション機能(Azure AI Content Safety、Copilot Studioのコンテンツモデレーションレベルなど)を1つ追加することから始める。

## 関連トピック

- [プロンプトインジェクションとは何か(仕組みと対策)](prompt-injection-basics.md)
- [GPTsにおけるプロンプトインジェクション対策](../part06-custom-ai/gpts-prompt-injection-defense.md)

## 更新履歴

### 2026-09-09: 各社の最新アップデートを反映して全体を最新化
- **内容**: OpenAI Moderation API(`omni-moderation-latest`の13カテゴリ・低遅延)とOpenAI Guardrails Python(PII検出・ジェイルブレイク検出・ハルシネーション検知・トリップワイヤの具体的な仕組み)、Azure AI Content Safety(2026年6月Build 2026でのPrompt ShieldsのMCP・A2A対応拡張、標準ティアの料金目安)、Llama Guard 4とLlama Prompt Guard 2の2段構成、NeMo Guardrailsのマイクロサービス化とColang・低遅延の実態、Anthropicの分類器スタックおよび2026年9月のClaude Fable 5.1/Mythos 5.1で明示化された「Enterprise Frontier Safeguards」を本文・比較表に反映。エージェント型AI運用時にMCP・A2A経由の入力もチェック対象になる点を「使いどころ・使い分け」「注意点」「設計チェックリスト」に追記
- **出典**: [OpenAI: Moderation guide](https://developers.openai.com/api/docs/guides/moderation)、[OpenAI: omni-moderation-latest model](https://developers.openai.com/api/docs/models/omni-moderation-latest)、[OpenAI Guardrails Python Docs](https://openai.github.io/openai-guardrails-python/)、[DeepWiki: OpenAI Guardrails Python - Data Protection Guardrails](https://deepwiki.com/openai/openai-guardrails-python/6.2-data-protection-guardrails)、[Microsoft Learn: What's new in Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/whats-new)、[Microsoft Learn: Prompt Shields in Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection)、[InfoQ: Azure API Management Ships Unified Model API and MCP Content Safety at Build 2026](https://www.infoq.com/news/2026/06/azure-apim-ai-gateway-build/)、[Microsoft Security Blog: Securing AI agents](https://www.microsoft.com/en-us/security/blog/2026/06/30/securing-ai-agents-ai-tools-move-from-reading-acting/)、[Azure AI Content Safety Pricing](https://azure.microsoft.com/en-in/pricing/details/cognitive-services/content-safety/)、[Meta Llama Guard 4 / Prompt Guard 2 比較解説](https://www.solulab.com/llm-guardrails/)、[NVIDIA NeMo Guardrails (GitHub)](https://github.com/NVIDIA-NeMo/Guardrails)、[Spheron: NeMo Guardrails Production Deployment](https://www.spheron.network/blog/nemo-guardrails-production-deployment-llm-gpu-cloud/)、[Anthropic: Introducing Claude Fable 5.1 and Claude Mythos 5.1](https://www.anthropic.com/claude-fable-and-mythos-5-1)、[AWS: Claude Fable 5.1 is now available on AWS](https://aws.amazon.com/about-aws/whats-new/2026/09/claude-fable-5-1-aws/)、[tech-insider.org: Anthropic Claude Enterprise Frontier Safeguards Explained](https://tech-insider.org/anthropic-claude-enterprise-frontier-safeguards-2026/)

### 2026-07-28: 新しい回避手口と防御側の誤検知事例を追記
- **内容**: 2026年7月に報告された「assistant prefill」を悪用したジェイルブレイク手口(通称Sockpuppeting、11の主要LLM横断で報告)と、防御側のフォレンジック調査がガードレールに誤ってブロックされた事例を注意点に追記
- **出典**: [Trend Micro: Sockpuppeting - How a Single Line Can Bypass LLM Safety Guardrails](https://www.trendmicro.com/vinfo/us/security/news/cybercrime-and-digital-threats/sockpuppeting-how-a-single-line-can-bypass-llm-safety-guardrails)、[malware.news: The Guardrails Problem Just Played Out on Both Sides of the Same Incident](https://malware.news/t/the-guardrails-problem-just-played-out-on-both-sides-of-the-same-incident/124212)

### 2026-07-06: 初版執筆
- **内容**: ガードレールを「入力フィルタ」「システムプロンプトでの制約」「出力フィルタ」「専用の分類モデル」の4種類に整理し、公開範囲・リスクに応じた使い分けの判断基準、ChatGPT(GPTs)・Gemini・Copilot Studio・Difyの設定箇所の対応表、OpenAI Moderation API/OpenAI Guardrails・Azure AI Content Safety・Llama Guard・NeMo Guardrails・Anthropic Constitutional Classifiersといった専用製品/ライブラリの比較、多層防御(defense in depth)の考え方を整理
- **出典**: [OpenAI: Moderation guide](https://developers.openai.com/api/docs/guides/moderation)、[OpenAI: omni-moderation-latest model](https://developers.openai.com/api/docs/models/omni-moderation-latest)、[OpenAI Guardrails Python (GitHub)](https://github.com/openai/openai-guardrails-python)、[Microsoft Learn: Prompt Shields in Azure AI Content Safety](https://learn.microsoft.com/en-us/azure/ai-services/content-safety/concepts/jailbreak-detection)、[Azure AI Content Safety 製品ページ](https://azure.microsoft.com/en-us/products/ai-services/ai-content-safety)、[NVIDIA NeMo Guardrails (GitHub)](https://github.com/NVIDIA-NeMo/Guardrails)、[NVIDIA Developer: NeMo Guardrails Library](https://developer.nvidia.com/nemo-guardrails)、[Meta: Llama Guard 4 12B Model Card (GitHub)](https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard4/12B/MODEL_CARD.md)、[Anthropic: Constitutional Classifiers](https://www.anthropic.com/research/constitutional-classifiers)、[Anthropic: Next-generation Constitutional Classifiers](https://www.anthropic.com/research/next-generation-constitutional-classifiers)、[Microsoft Learn: モデルのバージョンと設定を変更する(Copilot Studio)](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/prompt-model-settings)、[Microsoft Support: Microsoft 365 Copilot Chatの有害なコンテンツ保護設定](https://learn.microsoft.com/ja-jp/copilot/microsoft-365/harmful-content-protection-copilot-chat)、[Dify Docs: Moderation Tool](https://docs.dify.ai/en/guides/application-orchestrate/app-toolkits/moderation-tool)、[Google AI for Developers: Safety settings (Gemini API)](https://ai.google.dev/gemini-api/docs/safety-settings)
