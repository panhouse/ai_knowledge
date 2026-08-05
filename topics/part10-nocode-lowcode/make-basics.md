---
title: "Makeの基本"
part: 10
chapter: 第3章 自動化・連携ツール
tags: [Make, ワークフロー自動化, ノーコード, iPaaS]
created: 2026-07-06
updated: 2026-08-03
---

# Makeの基本

## これは何か

「フォームの回答をAIで自動分類してスプレッドシートに記録したい」「複数のSaaS(クラウドサービス)をつないで、その間にAIの判断を1ステップ挟みたい」——プログラミングなしでこれを実現したい場合の代表的な選択肢がMake(メイク、旧Integromat〈インテグロマット〉)である。フローチャートのような画面上に「モジュール」と呼ばれる処理ブロックを並べて線でつなぎ、Gmail・Slack・Googleスプレッドシート・OpenAI・Anthropic・Google Geminiなど3,000以上のアプリ・サービスを連携させる、クラウド専業のiPaaS(Integration Platform as a Service、複数のクラウドサービスをつなぐ統合基盤)ツールである。[n8n](./n8n-basics.md)と同じ「AIも1ステップとして使える汎用の業務自動化ツール」というカテゴリだが、Makeはセルフホスト(自社サーバーでの運用)ができないクラウド専業で、GUI(操作画面)の分かりやすさを重視した設計になっている点が異なる。

## 仕組み・背景

Makeでは1つの自動化の単位を「シナリオ(Scenario)」と呼ぶ。シナリオは「トリガー(処理の起点。例: フォーム送信、新着メール受信、スケジュール実行)」から始まり、その後に続く「モジュール(実際の処理。例: AIに要約させる、スプレッドシートに書き込む、Slackに投稿する)」を線でつないで実行順序を定義する。1つのモジュールが1つの処理ステップに対応し、この「モジュールを積み木のように並べる」感覚の分かりやすさが、Makeが非エンジニアに支持されてきた理由になっている。

### Integromatからのリブランドという成り立ち

Makeはチェコ発のスタートアップ「Integromat」が前身で、2012年にサービスを開始した。2020年にプロセスマイニング(業務プロセスの可視化・分析)大手のCelonis(セロニス)に買収され、2022年2月に「Make」へ正式にリブランドしている。n8n(2019年創業・OSSのSustainable Use License)やZapier(2011年創業・非公開の商用SaaS)とは異なり、Makeは「老舗のワークフロー自動化ツールが、大手企業の傘下でブランドと機能を刷新した」という成り立ちを持つ。ソースコードは非公開で、n8nのようなセルフホストの選択肢は提供されていない。

### AI関連の仕組み

MakeにはOpenAI・Anthropic(Claude)・Google Gemini・Azure OpenAIなど主要LLM(大規模言語モデル)ベンダーそれぞれの公式モジュールが用意されており、シナリオの中に「Anthropicモジュールでテキストを分類する」「OpenAIモジュールで文章を要約する」といった形でAI処理を1ステップとして組み込める。

単発のAI呼び出しに加えて、2025年4月に自律的にツールを選び複数ステップを判断させられる「Make AI Agents」機能が発表された後、2026年2月2日には作り直された新版「Make AI Agent(New)」がオープンベータで公開されている。従来のシナリオと同じキャンバス上でエージェントを組み立てられる点が刷新の核で、AIがどのツールをどう選んで実行したかを画面上で追いながら組み立て・修正でき、完成したエージェントは複数のワークフロー・チームをまたいで共有できる。AIの頭脳部分にあたる「AIプロバイダー」は、無料プランを含む全プランで使えるMake組み込みのAIプロバイダーと、OpenAI・Anthropic・Google Geminiなど自分のAPIキーで接続する「カスタムAIプロバイダー」の2種類があり、後者は有料プランでのみ選択できる。ただし現時点(2026年8月)でも日本の実務利用の主流は、n8nの「AI Agentノード」のような自律型エージェントよりも、シナリオの1ステップとしてAIモジュールを組み込む使い方であり、Make AI Agent(New)自体もオープンベータ(機能・料金は変更の可能性あり)という位置づけである。

## 使いどころ・使い分け

| やりたいこと | 向いているツール |
|---|---|
| プログラミング知識がないメンバーが直感的に自動化を組みたい | Make・Zapier(GUIがシンプルで学習コストが低い) |
| 複数のSaaS・DB・社内システムをつなぎ、AIをその中の1ステップとして使いたい | Make・[n8n](./n8n-basics.md) |
| AIチャットボット・社内RAG検索アプリなど「AI利用そのもの」が主目的 | [Dify](./dify-basics.md)(RAG・プロンプト管理・チャットUIが標準装備) |
| セキュリティ・データ主権を重視し自社サーバーで運用したい | n8n(セルフホスト無料。Make・Zapierはクラウド専用) |
| 複雑な条件分岐やコードによる細かいデータ加工が必要 | n8n(Codeノードで直接JavaScript/Pythonを実行できる) |
| シナリオの見た目・操作感の分かりやすさを最優先したい | Make(モジュールを積み木のようにつなぐUIで、非エンジニアへの説明がしやすい) |

比較表([n8nの基本](./n8n-basics.md)の比較表と対応。2026年8月時点の目安。料金・仕様は変更されやすいため各公式サイトで最終確認すること)

| 項目 | Make | n8n | Dify | Zapier |
|---|---|---|---|---|
| 主な用途 | 汎用ワークフロー自動化 | 汎用ワークフロー自動化(AIは機能の1つ) | AIチャットボット/RAGアプリ構築 | 汎用ワークフロー自動化 |
| AI機能 | OpenAI/Anthropic/Gemini等の公式モジュール、Make AI Agent(New)(自律型、2026年2月にオープンベータ公開) | AI Agentノード、主要LLM全対応、LangChain統合 | LLM呼び出しが中核機能、RAGが標準搭載 | AI Copilotによる作成支援、AI系アクションあり |
| セルフホスト | 不可(クラウド専用) | 可(無料、要インフラ管理) | 可(無料、要インフラ管理) | 不可(クラウド専用) |
| 料金モデル | クレジット(旧オペレーション)課金。標準モジュール実行1回=1クレジットが基本 | セルフホスト無料/クラウドは実行(ワークフロー1回の実行)課金 | セルフホスト無料/クラウドはメンバー数・アプリ数等で段階課金 | タスク(1ステップ実行)課金 |
| 学習コストの目安 | 低〜中(GUIが直感的) | 中〜高(ノードの概念・データ構造の理解が必要) | 中(AI特化のため機能は絞られている) | 低(非エンジニア向けに設計) |

「AIの生成・判断が主目的ならDify、業務システム間の連携が主目的でAIはその一部ならMake/n8n、その中でも操作の分かりやすさを優先するならMake、柔軟性・セルフホスト可否を優先するならn8n」という整理が実務上の目安になる。MakeとZapierも近い競合関係にあり、一般にZapierの方が連携アプリ数・ブランド認知度で先行し、Makeはより複雑な分岐・データ加工を視覚的に組みやすい代わりに画面の情報量がやや多い、という違いがある。

## 実務での使い方

### シナリオ作成の基本手順(画面の場所)

1. make.comでサインアップ後、左メニューの「Scenarios(シナリオ)」→右上の「Create a new scenario(新しいシナリオを作成)」をクリックする
2. 空のキャンバスの中央にある「+」をクリックし、検索窓にアプリ名(例: 「Google Forms」「Anthropic」)を入力してトリガー/アクションのモジュールを選ぶ
3. 各モジュールをクリックすると設定パネルが右側(または画面下)に開き、そこで対象サービスのアカウント接続(Connection)とパラメータを設定する
4. モジュール同士を線でつなぎ、必要に応じて「Router(ルーター)」で条件分岐を追加する
5. 画面下部の再生アイコン「Run once(1回だけ実行)」でテスト実行し、各モジュールの入出力を確認する
6. 問題なければ画面左下のトグルスイッチをON(緑)にしてシナリオを有効化し、常時稼働させる

### 料金プラン(2026年8月時点の目安。最新情報は make.com/pricing で必ず確認)

2025年8月27日付で、Makeは課金単位を「オペレーション(Operations)」から「クレジット(Credits)」に変更した。標準モジュール(AI以外の連携アプリ)は実行1回=1クレジットのままだが、AIモジュールやコード実行(Make内でのJavaScript/Python実行)は機能・モデル・トークン量に応じてクレジット消費が変動する仕組みになっている点が変更点である。この体系は2026年8月時点でも継続している。

| プラン | 料金(年払い時の月額目安) | クレジット/月の目安 | 主な特徴 |
|---|---|---|---|
| Free | 無料 | 1,000クレジット | アクティブシナリオ2本まで、実行間隔は最短15分、1回の実行時間は最大5分 |
| Core | 約$9/月 | 10,000クレジット〜 | 有料プランの入門。無制限のアクティブシナリオ、実行間隔は最短1分、Make APIへのアクセス |
| Pro | 約$16/月 | 10,000クレジット〜(上位) | Coreの機能に加え、実行ログの全文検索、カスタム変数、優先実行(混雑時も実行が詰まりにくい) |
| Teams | 約$29/月 | プランに応じて拡大 | Proの機能に加え、チームロール、シナリオテンプレートの作成・共有など複数人での運用機能 |
| Enterprise | 個別見積り | 要相談 | SSO、SCIM、監査ログ、SLA付きサポート、専用インフラ |

年払いだと月払いよりおおむね15〜17%程度安くなる。クレジット数は10,000→20,000→40,000…という形でプラン内でも段階的に増量できる(上位クレジット枠ほど料金は上がる)。

### Make AI Agent(New)のクレジット消費(2026年2月公開のオープンベータ機能)

Make AI Agent(New)を使う場合、クレジットの消費ルールが通常のモジュールと異なる。Make組み込みのAIプロバイダーを使う場合は「エージェントの実行: 1操作=1クレジット+AIトークン量に応じた追加クレジット」「チャット: 1操作分+呼び出したツールの操作分+AIトークン量に応じた追加クレジット」「ナレッジ(PDF/DOCXの読み込み): 1操作分+1ページあたり10トークン相当」という組み合わせでクレジットが減る。一方、OpenAIやAnthropic Claudeなど自分のAPIキーで接続する「カスタムAIプロバイダー」を選んだ場合は、Make側のクレジット消費は1操作=1クレジットのみで、AIモデルの利用料はLLMベンダー側に別途発生する。クレジット消費を予測しやすくしたい場合はカスタムAIプロバイダー接続の方が見積りやすい。

### AI活用の実装例:フォーム回答をAIで分類してスプレッドシートに記録

構成は「Google Forms(トリガー)→ Anthropic(または OpenAI/Gemini)モジュールで分類 → Google スプレッドシートに書き込み」という3ステップ。

1. **Google Formsモジュール**: 「Watch Responses(新しい回答を監視)」をトリガーに設定する
2. **Anthropicモジュール(Create a Message等)のプロンプト例(コピペ可)**
   ```
   以下の問い合わせ内容を読み、次の3カテゴリのいずれか1語だけで分類してください。
   カテゴリ: 「見積依頼」「クレーム」「その他」

   問い合わせ内容:
   {{フォームの回答本文}}
   ```
3. **Google スプレッドシートモジュール(Add a Row)**: 「回答日時」「回答者名」「分類結果(前段のAnthropicモジュールの出力)」を列にマッピングして1行追加する

同様の構成で、Slackへの通知・Notionへの記録・Gmailへの自動返信下書きなど、後段のモジュールを差し替えるだけで応用が利く。

## 注意点・よくある誤解

- **クレジット課金は「実行回数」ではなく「処理の重さ」で増減する**: 標準モジュールは実行1回=1クレジットが目安だが、AIモジュールやMake AI Agentはモデルやトークン量に応じてクレジット消費が変動する。n8n(ワークフロー実行単位)・Zapier(タスク単位)とは課金の考え方が異なるため、単純な「月◯回使うから◯円」という見積りは誤りやすい
- **Make AI Agent(New)はオープンベータであることを踏まえて使う**: 2026年2月に公開された現行版のMake AI Agentは、Make公式も「機能・料金は変更される可能性がある」と明示しているベータ機能。本番の基幹業務にいきなり組み込むより、まずは限定的な用途で試し、仕様変更を前提に運用するのが安全
- **無料プランは検証用と割り切る**: 1,000クレジット/月、アクティブシナリオ2本まで、実行間隔は最短15分という制限があり、フォーム送信のたびに動くような業務利用ではすぐに枯渇する。まずは有料プランに上げる前提でPoC(概念実証)に使うのが現実的
- **日本語サポート・ドキュメントは発展途上**: 管理画面自体は日本語表示に対応しつつあるが、公式ドキュメントやサポート窓口は基本的に英語が中心。ブラウザの翻訳機能や、問い合わせ文面をAIに作らせるといった工夫が実務では有効
- **シナリオが複雑化すると見通しが悪くなる**: モジュール数・分岐が増えるほど画面が縦横に広がり全体像を追いにくくなる。処理のまとまりごとに「サブシナリオ(他のシナリオから呼び出す部品)」に分割し、モジュールに分かりやすい名前を付けておくと保守しやすい
- **APIキー等の認証情報はConnection機能で一元管理する**: AnthropicやSlackのAPIキーをモジュールの設定に直書きせず、Makeの「Connections」機能で管理し、複数モジュールから参照する形にすることで、シナリオを共有・複製した際の漏洩リスクを避けられる

## 最初の一歩

make.comで無料アカウントを作成し、「Google Forms(またはGmail)→ AIモジュールで分類・要約 → スプレッドシートに記録」という3ステップのシナリオを1つ組んで、「Run once」で実際に動かしてみる。

## 関連トピック

- [n8nの基本](./n8n-basics.md)
- [Difyとは何か](./dify-basics.md)

## 更新履歴

### 2026-08-03: 「仕組み・背景」「実務での使い方」「注意点」の節を最新化
- **内容**: 2026年2月2日にオープンベータ公開された新版「Make AI Agent(New)」の概要(キャンバス上での構築、AI判断の可視化、チーム間共有、Make組み込み/カスタムAIプロバイダーの使い分け)を追記。Make AI Agentのクレジット消費ルール(エージェント実行・チャット・ナレッジ読み込みそれぞれの計算方法、カスタムAIプロバイダー利用時は1操作=1クレジットのみ)を新設。料金プランの各段の機能差分(Core/Pro/Teamsの積み上げ内容)と年払い割引率を明確化。ベータ機能である点を注意点に追加
- **出典**: [Introduction to Make AI Agents (New) (Make Help Center)](https://help.make.com/introduction-to-make-ai-agents-new)、[Make AI Agents app (Make Help Center)](https://help.make.com/make-ai-agents-app)、[Announcing the next generation of Make AI Agents (Make公式ブログ)](https://www.make.com/en/blog/announcing-next-generation-make-ai-agents)、[Make AI Agents 製品ページ (Make公式)](https://www.make.com/en/ai-agents)、[Credit usage for AI agents (Make Help Center)](https://help.make.com/credit-usage-for-ai-agents)、[Credits (Make Help Center)](https://help.make.com/credits)、[Step 1. Set up the AI agent (Make Help Center)](https://help.make.com/step-1-set-up-the-ai-agent)、[Make.com Pricing: Plans, Costs, and Is It Worth It in 2026? (Lindy)](https://www.lindy.ai/blog/make-com-pricing)、[Make.com pricing: Is it worth it? [2026] (Zapier)](https://zapier.com/blog/make-com-pricing/)、[Make.com Free Plan 2026: Limits, Use Cases, and When to Upgrade (Use Apify)](https://use-apify.com/blog/make-com-free-plan-limits)
- **注記**: 料金プランの金額・クレジット数自体は2026年7月時点から変更なしと複数の第三者メディアで確認できたため据え置き。Make AI Agent(New)はオープンベータのため、機能・料金は今後変更される可能性がある

### 2026-07-06: 初版執筆
- **内容**: Make(旧Integromat)の概要(シナリオ・モジュールという基本単位、AIモジュールとMake AI Agents、Integromatからのリブランド経緯)、n8n/Dify/Zapierとの比較表、シナリオ作成の画面操作手順、2025年8月のオペレーション→クレジット課金への変更、料金プラン、フォーム回答のAI分類→スプレッドシート記録の実装例を整理
- **出典**: [Make Pricing公式](https://www.make.com/en/pricing)、[Make.com Pricing 2026 (trackstack)](https://trackstack.tech/en/make-com-pricing-2026/)、[Make.com Free Plan 2026 (Use Apify)](https://use-apify.com/blog/make-com-free-plan-limits)、[Introducing Credits: A New System Of Billing (Make Community)](https://community.make.com/t/introducing-credits-a-new-system-of-billing/89480)、[Make.com Credits: What Changed in 2025 (4Spot Consulting)](https://4spotconsulting.com/make-com-changing-pricing-structure-what-you-need-to-know/)、[Integromat evolves to Make (Make公式)](https://www.make.com/en/integromat-evolves-to-make)、[Make announces Make AI Agents (Make公式プレスリリース)](https://www.make.com/en/make-ai-agents-press-release)、[Announcing the next generation of Make AI Agents (Make公式ブログ)](https://www.make.com/en/blog/announcing-next-generation-make-ai-agents)、[Anthropic Claude Integration (Make公式)](https://www.make.com/en/integrations/anthropic-claude)、[Create your first scenario (Make Help Center)](https://help.make.com/create-your-first-scenario)
- **注記**: 料金プラン名・金額・クレジット数は第三者メディアの記載をもとにした2026年7月時点の目安(公式pricingページはアクセス制限のため直接確認できず)。掲載・記事化前に make.com/pricing で最終確認を推奨
