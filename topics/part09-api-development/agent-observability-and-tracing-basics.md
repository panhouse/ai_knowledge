---
title: AIエージェントの可観測性・トレーシングの基本(LangSmith・Langfuse等)
part: 9
chapter: 第4章 MCP・エージェント連携
tags: [可観測性, トレーシング, LangSmith, Langfuse, LLMOps, デバッグ]
created: 2026-09-03
updated: 2026-09-03
---

# AIエージェントの可観測性・トレーシングの基本(LangSmith・Langfuse等)

## これは何か

AIエージェントを本番運用に乗せると、必ず「なぜこの回答になったのか」「なぜ急に遅くなったのか」「今月のAPI費用が想定の3倍になったのはどのステップが原因か」がわからなくなる場面に突き当たる。エージェントは1回のプロンプトで完結せず、計画→ツール呼び出し→結果確認→再計画…という複数ステップを自律的に繰り返すため、単なるアプリケーションログでは途中経過を追いきれない。可観測性(オブザーバビリティ、observability)・トレーシング(tracing)ツールは、この「エージェントが内部で何をしたか」を1ステップずつ記録・可視化し、デバッグ・コスト管理・品質監視を可能にする仕組みである。LangSmith・Langfuse・Helicone・Arize Phoenix・W&B Weave・Datadog LLM Observabilityなどが代表的なツールで、開発中のデバッグから本番運用後の継続監視まで一貫して使われる。

本ページは、これらツールが記録する「トレース」「スパン」といった基本概念、何を監視すべきか、主要ツールの比較と選び方を扱う。エージェントを自作する際の設計・実装そのもの(LangGraph・OpenAI Agents SDK等のフレームワーク)は別トピックの範囲であり、本ページは「動いているエージェントを観測・デバッグする」側に焦点を当てる。

## 仕組み・背景

### なぜ従来のAPM(アプリケーション監視)では足りないのか

Webサーバーやアプリの監視(APM、Application Performance Monitoring)は、「このAPIは200ミリ秒で返ったか」「エラー率は何%か」のように、入出力が決まった処理を対象にしてきた。LLMエージェントの監視が別分野として発達したのは、次の3点が従来の監視と質的に異なるためである。

- **出力が非決定的**: 同じ入力を与えても、モデルの出力は毎回変わりうる。「正解/不正解」の二値ではなく、出力の「質」を継続的に評価する仕組みが要る
- **1回のリクエストが多段の処理に分解される**: エージェントは計画→ツール呼び出し→検索→再計画のように複数ステップを踏む。1つのAPI呼び出しにつき8〜15個、エージェントのループが絡むと1回のユーザー対話で40〜75個ものスパン(後述)が生成されることも珍しくない
- **コストとトークン消費が可変**: 呼び出すモデル・生成トークン数・ツール呼び出し回数によって1回あたりのコストが変動するため、「このユーザーのこの操作にいくらかかったか」を追跡する仕組みが必要になる

### トレース(Trace)とスパン(Span)

可観測性ツールに共通する基本単位は次の2つ。

- **トレース(Trace)**: エージェントへの1回のリクエストから応答完了までの「一連の流れ全体」。ユーザーの1つの質問・1回のタスク実行に対応する
- **スパン(Span)**: トレースの中の「1つのステップ」。LLM呼び出し1回、ツール実行1回、検索(リトリーバル)1回などがそれぞれ1スパンとして記録される。スパンは入れ子(親子関係)になり、「計画スパンの中でツール呼び出しスパンが3つ動いた」といった構造がツリー表示される

これに加えて、記録したトレースに対して「この回答は事実に基づいているか」「有害な内容を含んでいないか」などをLLM自身に採点させる**評価(Evaluation)スコア**を後付けで紐づけられるのが主要ツールの共通機能になっている(LLM自身を採点者に使う手法は「LLM-as-a-Judge」と呼ばれる)。

### OpenTelemetry(OTel)への収斂

2026年時点の大きな流れとして、トレース記録の形式が**OpenTelemetry(OTel、業界標準の分散トレーシング規格)**に収斂しつつある。LangSmith・Langfuse・Arize Phoenix・Datadog LLM Observabilityはいずれも OTel 形式でのデータ取り込みに対応しており、アプリ側に一度計装コード(instrumentation、監視用のコードを埋め込むこと)を入れておけば、送り先のツールを後から差し替えやすくなっている。ベンダーロックインを避けたいなら、OTel対応を選定基準に入れるとよい。

## 使いどころ・使い分け

| 状況 | 向いている選択 |
|---|---|
| LangChain/LangGraphで開発している | LangSmith(ほぼ設定不要でインテグレーションできる) |
| 社内にデータを置きたい、コンプライアンス上SaaSにログを出せない | Langfuse(セルフホスト)または Arize Phoenix(セルフホスト) |
| まずは無料で1つのエージェントを可視化したいだけ | Langfuse Hobby プラン、または LangSmith Developer プラン(いずれも無料枠あり) |
| 既にDatadogで自社インフラを監視しており、その延長でLLM呼び出しも見たい | Datadog LLM Observability(既存ダッシュボードに統合できる) |
| MLOps基盤としてW&Bをすでに使っている(モデル学習の実験管理など) | W&B Weave(同じエコシステムで完結) |
| とにかく安く・軽く、コスト(トークン単価)の可視化だけしたい | Helicone(プロキシ型で導入が容易。ただし2026年3月のMintlifyによる買収後はメンテナンスモードに移行しており、今後の機能追加は限定的と見ておく) |
| 特定フレームワークに依存せず、ツールをいつでも差し替えたい | OpenTelemetry対応のツール(Langfuse・Arize Phoenix・Datadog等)を選び、計装をOTel準拠にしておく |

判断基準は大きく3つ。(1) 既に使っている開発フレームワーク・監視基盤との親和性、(2) データを外部SaaSに出せるか(セルフホスト要否)、(3) 想定するトレース量に対してコストが見合うか。小規模なPoC段階では無料枠のあるツールで十分なことが多く、本番でトレース量が増えてから有料プランやセルフホストへの移行を検討するのが実務的な順序になる。

## 実務での使い方

### 主要ツールの比較(2026年9月時点)

| ツール | 提供元 | セルフホスト | 料金の目安 | 相性がよい環境 |
|---|---|---|---|---|
| LangSmith | LangChain社 | 不可(SaaSが基本、Enterpriseで専用環境の相談可) | 無料(月5,000トレース、14日保持)/ Plus $39/席/月(月1万トレース込み、超過は1,000トレースあたり$2.50〜)/ Enterpriseは要問合せ | LangChain・LangGraphでの開発。ほぼ設定不要で連携できる |
| Langfuse | Langfuse GmbH | 可(2025年6月からトレース・評価・プロンプト管理を含むコア機能が全てMITライセンスでOSS化) | セルフホストは無料(インフラ費用は別途)/ クラウドはHobby無料(月5万ユニット・2ユーザー)、Core $29/月、Pro $199/月、Enterprise $2,499/月 | 自社インフラにログを置きたい・特定フレームワークに縛られたくない場合。OTel対応 |
| Helicone | Helicone(2026年3月にMintlifyが買収) | 可(Apache-2.0) | 無料枠あり、有料は$79/月〜 | 手軽にプロキシ経由でコスト・レイテンシを可視化したい場合。買収後はメンテナンスモードで新機能追加は限定的 |
| Arize Phoenix / Arize AX | Arize AI | Phoenix(OSS版)は可(Elastic License 2.0)/ AX(クラウド版)はSaaS | Phoenixは無料(自社インフラ費用は別)/ AXは無料枠(月2.5万スパン)、Pro $50/月〜、Enterpriseは要問合せ(中央値で年間$60,000程度という調査もある) | 評価(Evaluation)機能を重視する場合、MLの実験管理も含めて一体運用したい場合 |
| W&B Weave | Weights & Biases | 不可(SaaS) | 個人・小規模チーム向け無料枠あり、チーム/Enterpriseは要問合せ(トレース取り込みは$0.10/MBという報告あり) | 既にW&Bでモデル学習・実験管理をしている組織 |
| Datadog LLM Observability | Datadog | 不可(SaaS、既存Datadog契約に追加) | 無料枠(月4万LLMスパン)、超過分はスパン課金(ツール呼び出し・埋め込み等の非LLMスパンは無課金) | 既存のインフラ監視(APM)をDatadogで行っており、LLM呼び出しも同じダッシュボードで見たい場合 |

料金は変動が速いため、契約前に必ず各社公式サイトで最新情報を確認すること。

### 導入の基本手順(Langfuseの例)

1. Langfuse Cloud(https://cloud.langfuse.com )でアカウントを作成するか、Docker Composeでセルフホスト環境を構築する
2. プロジェクトを作成し、発行された `Public Key` / `Secret Key` を控える
3. アプリのコードに計装ライブラリ(Python: `langfuse`パッケージ、JS/TS: `langfuse` SDK)を追加し、LLM呼び出し・ツール呼び出しの前後を `@observe` デコレータ等でラップする
4. アプリを実行すると、Langfuseのダッシュボードにトレースがリアルタイムで表示される。ツリー表示で各スパンの入出力・レイテンシ・トークン数・コストを確認できる

### コピペで使える最小コード例(Python、Langfuse)

```python
from langfuse import observe

@observe()  # この関数の呼び出し1回が1つのスパンとして記録される
def call_llm(prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content

@observe()  # ここが1つのトレース(エージェントの1回の実行全体)になる
def run_agent(user_goal: str) -> str:
    plan = call_llm(f"次のゴールを達成する手順を考えて: {user_goal}")
    result = call_llm(f"次の手順を実行して: {plan}")
    return result
```

`@observe()` を付けるだけで、関数のネスト構造がそのままトレースの親子関係(スパンのツリー)としてダッシュボードに反映される。LangSmithも同様に `@traceable` デコレータ、OpenAI Agents SDKは組み込みのトレーシング機能を持つなど、主要ツール・フレームワークはいずれも「関数やステップに印を付けるだけ」で計装できる設計になっている。

### 本番運用で見るべき指標

- **レイテンシ**: エージェント全体の応答時間、およびボトルネックになっているステップ(スパン)
- **コスト**: 1回の実行あたりのトークン消費・API費用。ユーザー単位・機能単位で集計できると予算管理がしやすい
- **ツール呼び出しの成功/失敗率**: どのツール呼び出しが失敗し、リトライや代替手段に切り替わっているか
- **出力品質(LLM-as-a-Judge等での自動採点)**: ハルシネーション(もっともらしい誤情報)の有無、有害性、フォーマット遵守などをサンプリングで自動採点し、品質の劣化(ドリフト)を継続的に検知する
- **異常検知**: 特定バージョンのプロンプト・モデル更新後にエラー率やコストが急変していないか

## 注意点・よくある誤解

- **トレースにも個人情報・機密情報が乗る**: トレースにはプロンプトの全文・LLMの応答・ツールの実行結果がそのまま記録されるため、顧客の個人情報や社外秘の情報を含む場合がある。SaaS型ツールを使う場合は、契約プランのデータ取り扱い方針(保持期間、学習利用の有無)を確認し、必要ならマスキング(機微情報を隠す処理)を計装コード側で行う
- **セルフホストは「無料」ではなく「インフラ費用+運用工数」に置き換わる**: LangfuseやPhoenixのコア機能自体は無料でも、Langfuseのセルフホストには PostgreSQL・ClickHouse・Redis・S3互換ストレージなど複数のミドルウェアの運用が必要になり、中規模構成で月$3,000〜4,000程度のインフラ・運用コストがかかったという試算もある。「ライセンス費用がかからない」と「運用コストがゼロ」は別問題として比較する
- **スパン数の見積もりを誤ると想定外の課金になる**: エージェントのループ処理は1回のユーザー対話で数十スパンを生成しうる。スパン課金・トレース課金のツールを使う場合は、PoC段階の想定より本番の実トラフィックでスパン数が桁違いに増えることを見込んで料金プランを選ぶ
- **LLM-as-a-Judge(AIによる自動採点)を過信しない**: 出力品質の自動採点はサンプリングと継続監視には有効だが、採点自体もLLMが行うため誤判定はありうる。重要な品質基準については、人手によるサンプルレビューを定期的に組み合わせる
- **買収・事業統合による将来性の変化に注意**: HeliconeはMintlifyによる買収(2026年3月)後にメンテナンスモードへ移行しており、この分野はベンダーの統廃合が起きやすい。長期利用を前提にする場合は、OpenTelemetry対応など「ツールを乗り換えやすい計装」にしておくとリスクを下げられる
- **「トレースを取っただけ」では改善につながらない**: 可視化はデバッグの出発点にすぎない。異常が起きたときにアラートが飛ぶ設定、コストの週次レビュー、品質スコアの継続的なモニタリングまで運用に組み込んで初めて効果が出る

## 最初の一歩

今すでに社内で動いているエージェント(自作のもの、またはLangChain/LangGraphで組んだPoC)が1つでもあれば、LangfuseかLangSmithの無料枠に登録し、その中の1つの関数呼び出しに `@observe`(または`@traceable`)を付けて、ダッシュボードにトレースが表示される様子を今週中に確認してみるとよい。

## 関連トピック

- [MCP(Model Context Protocol)の基本](mcp-basics.md)
- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [AIエージェントとは何か](../part11-ai-agents/ai-agent-basics.md)
- [AIエージェント運用のガバナンス設計(権限ポリシー・監査ログ・コスト管理)](../part11-ai-agents/ai-agent-governance-basics.md)
- [AIエージェント導入PoCの評価指標・進め方の基本](../part11-ai-agents/ai-agent-poc-evaluation-basics.md)

## 更新履歴

### 2026-09-03: 初版執筆
- **内容**: AIエージェント可観測性・トレーシングの基本概念(トレース/スパン/評価スコア)、従来のAPMとの違い、OpenTelemetryへの収斂、LangSmith・Langfuse・Helicone・Arize Phoenix・W&B Weave・Datadog LLM Observabilityの比較表(セルフホスト可否・料金・相性)、Langfuseでの導入手順とコード例、本番で見るべき指標、セルフホストのコスト・機微情報・ベンダー統廃合リスクなどの注意点を整理
- **出典**: [Inference.net: LangSmith Pricing Explained (2026)](https://inference.net/content/langsmith-pricing/), [Langfuse: Self-Hosted Pricing](https://langfuse.com/pricing-self-host), [dev.to: Langfuse Pricing Teardown 2026](https://dev.to/beton/langfuse-pricing-teardown-2026-2pi9), [The Rundown AI: Helicone — LLM Observability, Pricing & Alternatives](https://www.therundown.ai/tools/helicone), [enterprisedna.co: Helicone — Open Source](https://enterprisedna.co/directories/open-source/helicone/), [costbench.com: Arize Phoenix Pricing 2026](https://costbench.com/software/ai-observability/arize-phoenix/), [Langfuse: Arize AX Alternative? Langfuse vs. Arize AI and Arize Phoenix](https://langfuse.com/resources/engineering/best-phoenix-arize-alternatives), [qaskills.sh: W&B Weave LLM Evaluation & Tracing Guide 2026](https://qaskills.sh/blog/weave-llm-evaluation-tracing-guide-2026), [Datadog Docs: LLM Observability Cost](https://docs.datadoghq.com/llm_observability/monitoring/cost/), [buildmvpfast.com: Datadog AI Agent Monitoring](https://www.buildmvpfast.com/blog/datadog-ai-agent-monitoring-production-observability-2026), [Qiita: Langfuse vs LangSmith vs Helicone — LLM観測・デバッグツール比較【2026年版】](https://qiita.com/agdexai/items/f07b502d096c8f12d273)
