---
title: AIエージェントとは何か
part: 11
chapter: 第1章 AI市場の動向
tags: [AIエージェント, 自律型AI, エージェントモード]
created: 2026-07-05
updated: 2026-07-05
---

# AIエージェントとは何か

## これは何か

「AIエージェント」とは、ゴール(達成したい目的)だけを与えれば、そこに至るまでの
手順を自分で計画し、Webブラウザやコード実行環境、社内システムといった**外部のツールを
実際に操作しながら複数ステップを自律的にこなすAI**のことである。

これまでのチャットボットは「1回質問して1回答えが返ってくる」で完結していたため、
複数ステップにまたがる調査・予約・データ入力のような作業は、結局そのつど人間が
チャットとブラウザ・Excel・業務システムの間を行き来して橋渡しする必要があった。
AIエージェントは、この「橋渡し」の部分自体をAIに任せられる点が最大の違いであり、
使いこなせれば「調べて→まとめて→実行する」までを一気通貫で委任できるようになる。

なお、Part 11では「AIエージェント」を個別の一製品名としてではなく、
**チャットボットの次に来た製品カテゴリの名称**として扱う。具体的な製品(ChatGPT の
Agent、Claude の Agent SDK など)は年単位で名前も仕様も変わるため、まずこのページで
カテゴリとしての本質を押さえ、個別ツールの詳細は今後Part 11に追加していく各論ページに
譲る構成にしている。

## 仕組み・背景

AIエージェントの内部では、多くの場合「観察(Observe)→推論(Reason)→行動
(Act)→評価(Evaluate)」というループが回っている。LLM(大規模言語モデル)が
現在の状況を見て次に何をすべきか考え、ツールを1つ呼び出し、その結果をまた読み込んで
「目的を達成できたか」を判断し、達成できていなければ次の一手を考える、という
サイクルをタスクが完了するまで繰り返す仕組みである。

この仕組みを支える主な技術要素は次の3つ。

- **ツール操作(Tool use)**: Webブラウザの操作、ファイルの読み書き、社内システムへの
  API呼び出しなど、テキスト生成以外の「実行環境」をAIに与える機能。技術的には
  「Function Calling(関数呼び出し)」と呼ばれる仕組みが基盤になっていることが多い
  (詳細は関連トピックの Function Calling の解説ページを参照)。
- **プランニング(計画立案)**: 大きなゴールを、実行可能な小さなステップに分解する能力。
- **メモリ(記憶)**: セッションをまたいで過去の作業内容や好みを覚えておき、
  次回以降の指示を簡略化できる仕組み(すべてのエージェントが持つわけではない)。

2025年後半から2026年にかけて、この構成を採用した製品が主要ベンダーから相次いで
投入された。代表例は以下の通り(いずれも仕様は流動的なので、利用時は各社の
最新情報を確認すること)。

- **ブラウザ/コンピュータ操作型エージェント**: 画面を見ながらクリック・入力を行い、
  Web上の作業を代行するタイプ。OpenAIの「ChatGPT agent」は、視覚的ブラウザ・
  テキストブラウザ・ターミナル・API呼び出しを組み合わせ、旅行の比較予約や
  資料作成などを自律的にこなす([OpenAI公式](https://openai.com/index/introducing-chatgpt-agent/))。
  Googleは研究プロトタイプだった「Project Mariner」を2026年5月に発展的終了とし、
  その技術は「Gemini Agent」やChromeのブラウザ自動操作機能に統合された
  ([Android Headlines](https://www.androidheadlines.com/2026/05/google-shuts-down-project-mariner-ai-agent.html))。
  Anthropicも「computer use」機能により、Claudeがアプリの起動やブラウザ操作、
  開発ツールの実行を自律的に行えるようにしている
  ([Totalum Blog](https://www.totalum.app/blog/claude-agent-sdk-totalum-2026))。
- **コーディングエージェント**: ソフトウェア開発タスクを計画・実装・テスト・
  デプロイまで自律的に進めるタイプ。Cognition社の「Devin」は自律的にコードを書き、
  デバッグし、本番環境へのデプロイまで行う商用エージェントとして企業導入が進んでいる
  ([IBM](https://www.ibm.com/think/news/goldman-sachs-first-ai-employee-devin))。
  Anthropicの「Claude Agent SDK」(旧Claude Code SDK)は、開発者が自社の業務に
  組み込める汎用エージェント基盤で、サブエージェントへのタスク委任や
  人間による承認ステップ(human-in-the-loop)の組み込みにも対応する
  ([Anthropic公式ブログ](https://claude.com/blog/building-agents-with-the-claude-agent-sdk))。
- **業務ワークフロー型エージェント**: 特定の業務プロセスに組み込み、トリガーを
  検知して能動的に動くタイプ。Microsoftの「Copilot Studio」は、あらかじめ定義した
  トリガー・指示・ガードレール(制約条件)に基づき、ユーザーの指示を待たずに
  タスクを実行する自律エージェントの構築基盤を提供している
  ([Microsoft Copilot Blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/))。
- **汎用オートノマスエージェント**: 単一ベンダーのチャットアプリに閉じず、
  クラウド環境上で目的達成までの作業一式(調査・比較・資料作成など)を
  代行するタイプ。中国発のスタートアップ Butterfly Effect が開発した「Manus」が
  代表例で、「上位のAIエージェントプラットフォームを比較してスプレッドシートに
  まとめて」のような大きな依頼を、Webブラウジングとコード実行を組み合わせて
  1つの成果物に仕上げる([Wikipedia](https://en.wikipedia.org/wiki/Manus_(AI_agent))、
  [SSOJet](https://ssojet.com/blog/what-is-manus-ai-agent-explained))。

### 普通のチャットボットとの違い

| 観点 | 普通のチャットボット | AIエージェント |
|---|---|---|
| 実行主体 | 人間が都度指示し、AIは回答を返すだけ | AIが目的達成に向けて自ら次の一手を決める |
| 複数ステップの自律実行 | 基本は1問1答(1ターン完結) | 数十ステップにわたる作業を人手を介さず連続実行 |
| 外部ツール操作 | 原則なし(テキスト生成が中心) | Webブラウザ・ファイル・API・業務システムなどを実際に操作 |
| 典型的なユースケース | 文章作成、要約、質問への回答、壁打ち | 複数サイト比較しての予約、調査から報告書作成までの自動化、コードの自律実装、定型業務の巡回・実行 |

## 使いどころ・使い分け

すべての作業をエージェント化すべきではない。判断軸は「ステップ数」「外部実行の
必要性」「間違った場合の被害の大きさ」の3つで考えるとよい。

- **単発のチャット/プロンプトで十分な場合**
  - 1回のやり取りで結果が完結する(文章の下書き、要約、アイデア出し、質問への回答)
  - 参照する情報が手元のテキストや添付ファイルだけで完結する
  - 結果をその場で人間が確認し、すぐ手直しできる
- **エージェントを使う価値がある場合**
  - 複数のサイト・システムをまたいで情報を集めて突き合わせる必要がある
    (例:競合の価格調査、複数ツールの比較検討)
  - 「調べる→まとめる→ドラフトを作る」のように工程が3段階以上に分かれる
  - 定型だが手間のかかる業務を繰り返し発生させたい(定期モニタリング+下書き作成など)
  - コーディングのように、実装→実行→エラー修正のループが本質的に多ステップである

一方で、ステップ数が多いほど「途中の1ステップの誤り」が最終成果物に伝播するリスクも
増える。特に、送金・契約締結・顧客への一斉送信・本番環境への変更のように
**取り消しが難しい行動**が含まれる場合は、後述の注意点にある人間の承認ステップを
必ず挟むこと。逆に言えば、「後から簡単に修正・破棄できる」タスクほどエージェントに
任せやすい。

## 実務での使い方

現時点(2026年7月)で、追加のセットアップなしに試せる代表的な入口は以下の通り。
提供状況・名称・料金プランは変わりやすいため、実際に使う際は各社の最新ページを
確認してほしい。

- **ChatGPT**: 入力欄下のツール選択(ツールドロップダウン)から「エージェントモード
  (agent mode)」を選ぶと、Pro/Plus/Teamプランで利用できる。旅行の比較予約、
  スクリーンショットやダッシュボードからのプレゼン資料作成、予定の調整といった
  業務を代行できる([OpenAI公式](https://openai.com/index/introducing-chatgpt-agent/))。
- **Gemini**: 「Gemini Agent」機能や、Chromeに搭載された自動ブラウジング機能から
  Web上の作業を委任できる([Android Headlines](https://www.androidheadlines.com/2026/05/google-shuts-down-project-mariner-ai-agent.html))。
- **Claude**: 開発者向けには「Claude Agent SDK」で自社ワークフローに組み込める。
  ビジネスパーソン向けの入口としては、Claude Codeのような自律型コーディング
  エージェントが、要件を渡すだけで実装からテストまで進める例が広がっている
  ([Anthropic公式](https://www.anthropic.com/product/claude-code))。
- **Microsoft 365 Copilot / Copilot Studio**: ノーコードで、トリガー・指示・
  ガードレールを設定し、社内の定型業務(メール監視、レポート下書きなど)を
  自律的にこなすエージェントを作成できる
  ([Microsoft Copilot Blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/6-core-capabilities-to-scale-agent-adoption-in-2026/))。

### 業務シナリオの例:競合調査レポートの自動作成

1. 「主要な競合5社の直近の価格改定と新機能をWebで調べ、比較表と3行サマリー付きの
   レポートをスプレッドシートにまとめて」とエージェントに依頼する。
2. エージェントが各社サイト・プレスリリースを自律的に巡回し、情報を収集する。
3. 途中、有料資料のダウンロードやアカウント登録が必要な場面では、エージェントが
   処理を一時停止し、人間に許可を求める(多くの製品は「重要な行動の前には確認を取る」
   設計になっている)。
4. 収集結果を基に比較表・要約をまとめたファイルを作成し、人間が最終レビューをして
   社内共有する。

この一連の流れは、チャットボットに1問ずつ聞いて回るより圧倒的に速いが、
最終レビューの工程は省略しないことが重要である。

## 注意点・よくある誤解

- **エージェントは実際に「行動」する。取り消しにくい操作には要注意**:
  文章を書くだけのAIと異なり、エージェントはメール送信・購入・ファイル削除・
  コードのデプロイなど、現実の結果を伴う操作を行える。FINRA(米国金融取引業規制機構)の
  2026年報告書も、エージェントの「自律性(人間の検証なしに行動する)」
  「スコープクリープ(想定より広い権限で動いてしまう)」「監査可能性の低さ
  (多段階の推論過程を後から追いにくい)」を主要リスクとして挙げている。
  重要な行動の前に人間の承認を必須にする「human-in-the-loop」の設計や、
  エージェントに与える権限を業務に必要な最小限に絞る「スコープ設計」、
  行動ログを残す「監査証跡」の3点はセットで検討すること(情報漏えいの観点は
  関連トピックの情報漏えい対策ページも参照)。
- **「エージェント」は誇張されやすいマーケティング用語でもある**:
  調査会社Gartnerは、実質的な自律性を持たないRPA(定型作業の自動化)や
  チャットボットを「エージェント」と呼び替えて売る現象を「agent washing」と
  名付けており、「エージェント」を名乗る製品のうち本当に自律的といえるものは
  ごく一部にとどまると指摘している。「エージェント搭載」を謳う製品を検討する際は、
  実際に何ステップまで人手なしで完結できるのか、どの操作の前に人間の確認が
  入るのかを必ず確認すること。
- **多段階の分だけコストと待ち時間が増える**:
  1回のプロンプトで完結するチャット利用と比べ、エージェントは内部で何十回もの
  推論・ツール呼び出しを繰り返すため、消費するトークン量(処理量に応じた課金単位)や
  完了までの時間(数分〜数十分かかることも珍しくない)が大きくなりやすい。
  「本当に複数ステップの自律実行が必要なタスクか」を見極め、単発のプロンプトで
  済むものにまでエージェントを使わないことがコスト管理上も重要である。

## 最初の一歩

普段使っているチャットボット(ChatGPT・Gemini・Claudeなど)で、
「エージェント」を名乗る機能があるか設定・ツールメニューを確認し、
取り消しが容易な小さな調べ物タスク(例: 「〇〇について3サイト調べて比較表を作って」)
を1つだけ試して、単発のチャットとの違いを体感してみる。

## 関連トピック

- [Function Calling(関数呼び出し)の基本](../part08-api-development/function-calling-basics.md)
- [情報漏えい対策](../part03-risk-security/information-leakage-prevention.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: Part 11の初回ページとして、AIエージェントの定義・チャットボットとの違い・
  代表的な製品カテゴリ(ブラウザ操作型、コーディング型、業務ワークフロー型、汎用型)・
  ビジネス活用シーン・自律性に伴うガバナンス上の留意点を整理した。
- **出典**: [Introducing ChatGPT agent(OpenAI)](https://openai.com/index/introducing-chatgpt-agent/), [Google shuts down Project Mariner(Android Headlines)](https://www.androidheadlines.com/2026/05/google-shuts-down-project-mariner-ai-agent.html), [Claude Agent SDK in 2026(Totalum)](https://www.totalum.app/blog/claude-agent-sdk-totalum-2026), [Building agents with the Claude Agent SDK(Anthropic)](https://claude.com/blog/building-agents-with-the-claude-agent-sdk), [Claude Code(Anthropic)](https://www.anthropic.com/product/claude-code), [Meet Devin, the AI Software Engineer(IBM)](https://www.ibm.com/think/news/goldman-sachs-first-ai-employee-devin), [Copilot Studio 2026年5月アップデート(Microsoft)](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/new-and-improved-computer-using-agents-a-new-workflows-experience-and-real-time-voice-experiences/), [6 core capabilities to scale agent adoption in 2026(Microsoft)](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/6-core-capabilities-to-scale-agent-adoption-in-2026/), [Manus (AI agent)(Wikipedia)](https://en.wikipedia.org/wiki/Manus_(AI_agent)), [What Is Manus AI?(SSOJet)](https://ssojet.com/blog/what-is-manus-ai-agent-explained), [Agent Washing: The Definition(Digital Applied)](https://www.digitalapplied.com/blog/agent-washing-definition-buyers-scorecard-2026), [Gartner Warns of Agent Washing Risks(Gartner)](https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-warns-of-agent-washing-risks-in-supply-chain-planning-technology-market), [AI Agent Governance and Compliance in 2026(Zylos Research)](https://zylos.ai/research/2026-05-01-ai-agent-governance-compliance-2026/)
