---
title: AIエージェントとは何か(自律型AIの基礎)
part: 11
chapter: 第1章 AI市場の動向
tags: [AIエージェント, 自律型AI, MCP, AIトレンド]
created: 2026-07-05
updated: 2026-07-05
---

# AIエージェントとは何か(自律型AIの基礎)

## これは何か

ChatGPT・Claude・Gemini・Copilotのどの発表を見ても「AIエージェント」という言葉が必ず出てくるが、普通のチャットとどう違うのか曖昧なまま「なんとなくすごいもの」として受け止めている人が多い。結論から言うと、AIエージェントとは「目標だけを与えると、AI自身が手順を考え、Webブラウザや業務アプリなどの道具を実際に操作しながら、複数ステップの作業を最後までやり遂げるAI」のことである。1問1答で終わるチャットと違い、「作業を代行してくれる」点が本質的な違いになる。

## 仕組み・背景

通常のチャットAI(ChatGPTやClaudeでの対話など)は、こちらが1ステップずつ指示を出し、返ってきた文章を人間がコピーして次の作業に使う、という「人間が都度ハンドルを握る」使い方が基本になる。これに対してAIエージェントは、次の3つの能力を組み合わせることで「ハンドルをAIに預ける」動き方をする。

- **計画立案**: 与えられた目標(例:「競合3社の価格を調べて表にして」)を、AI自身が「サイトAを開く→価格を読み取る→サイトBも同様に→表にまとめる」といった複数ステップに分解する。
- **ツール利用(Tool Use)**: 文章を生成するだけでなく、Webブラウザの操作、ファイルの読み書き、社内システムのAPI呼び出しなど、外部の「道具」を実際に動かす。ChatGPTの「エージェントモード」やClaudeの「Computer Use(コンピュータ操作)」は、AIにマウス操作やキーボード入力に近い形でアプリを操作させる機能である。
- **自己点検と繰り返し**: 実行結果を自分で確認し、うまくいっていなければやり方を変えて再試行する。すべてを自動で終わらせるものもあれば、リスクの高い操作(送金、メール送信、注文確定など)の直前で必ず人間の承認を求める「human-in-the-loop(人間を判断ループに挟む)」設計のものもある。

この仕組みを陰で支えているのが**MCP(Model Context Protocol)**という規格である。MCPは、AIが社内のSlack・Google Drive・CRM・データベースなど外部のツールやデータに接続するための共通規格で、Anthropicが2024年11月に公開した。よく「AIにとってのコンセント」に例えられ、対応するツール側さえあれば、AIは個別の連携開発なしにそのツールを操作できるようになる。2026年5月時点でMCP対応の外部ツール(MCPサーバー)は1万4千件を超えており、OpenAI・Anthropic・Googleの主要3社がそろって採用したことで、事実上の業界標準になりつつある([JAPAN AI ラボ](https://japan-ai.co.jp/media/6154/))。非エンジニアの読者が自分でMCPを構築する必要は基本的にないが、「このツールはMCP対応」と聞いたら「AIエージェントから直接操作できる範囲が広いツール」と読み替えれば十分である。

## 使いどころ・使い分け

「AI」「エージェント」「RPA」は混同されやすいが、目的とする自動化の性質が異なる。

| 項目 | 通常のチャットAI | AIエージェント | RPA(ロボティック・プロセス・オートメーション) |
|---|---|---|---|
| 与えるもの | 具体的な指示(1問ずつ) | 目標・ゴール | あらかじめ決めた操作手順(シナリオ) |
| 得意な作業 | 文章作成、要約、壁打ち、単発の質問への回答 | 複数ステップにまたがる非定型の調べもの・作業代行 | 画面操作が変わらない大量の定型反復作業 |
| 判断の柔軟性 | 高い(ただし実行はしない) | 高い(状況に応じて手順を変える) | 低い(決めた手順以外は動けない) |
| 例外への対応 | 人間が都度指示を変える | ある程度は自分で軌道修正する | 画面が変わると止まる・エラーになる |
| 向く業務例 | 提案文のドラフト作成、アイデア出し | 「競合サイトを調べて比較表を作る」「複数ファイルから情報を集めて資料化する」 | 「毎日決まった時刻に決まった帳票をダウンロードして基幹システムに転記する」 |

判断の目安はシンプルで、**「手順が毎回同じで変わらない定型作業」ならRPA、「毎回状況が変わり人が考えながら進める非定型作業」ならAIエージェント、「1回のやり取りで完結する相談・作成作業」ならチャットAI**、で仕分けるとよい。2026年時点の実務トレンドとしては、この3つを対立させず、AIエージェントが司令塔になってRPAロボットや既存ツールを呼び出す「ハイブリッド自動化」も広がり始めている([Persol Business Process Design](https://www.persol-bd.co.jp/service/salesmarketing/s-smkt/column/ai-agent/agent-rpa-difference/))。

## 実務での使い方

2026年7月時点で、ビジネスパーソンが実際に触れられる代表的なAIエージェント機能は以下の通り。

| 提供元 | 製品・機能名 | できること | 料金の目安 |
|---|---|---|---|
| OpenAI | ChatGPT「エージェントモード」(ブラウザ版・アプリ版「ChatGPT Atlas」) | サンドボックス化された仮想PC上でWeb閲覧・フォーム入力・複数サイトの調査などを自律実行。実行前後に承認を求めるステップあり | Plusプラン月額$20前後(約3,000円)から利用可 |
| OpenAI | Codex | コーディング作業(機能実装・リファクタリング・PR作成)を代行するエージェント | ChatGPTの有料プランに含まれる |
| Anthropic | Claude Cowork | 目標を渡すと自分のPC・ローカルファイル・各種アプリを操作し、成果物(資料・表など)を仕上げて返す非エンジニア向けの作業代行エージェント | Proプラン月額$20前後(約3,000円)から |
| Anthropic | Computer Use / Skills | 画面操作(マウス・キーボード相当の操作)によるアプリ操作、Excel・PowerPoint・Word・PDFの定型作業向けスキル | Claude Pro以上のプランに含まれる |
| Google | Gemini Agent / Gemini Spark | ユーザーの指示のもとで24時間365日代わりに動く個人向けエージェント。重要な操作の前には確認を挟む設計([Google公式ブログ](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)) | Google AI Pro(月額¥2,900)・AI Ultra(月額¥14,500〜)などの上位プランで利用範囲が広がる |
| Microsoft | Microsoft 365 Copilot「エージェント ビルダー」/ Copilot Studio | 自然言語での説明だけで、社内データやツールに接続した業務専用エージェントをノーコードで作成できる([Microsoft Learn](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/fundamentals-get-started)) | Microsoft 365 Copilotライセンスに含まれる(別途Copilot Studioの従量課金プランもあり) |

**具体的なタスク例**: 「競合3社のWebサイトを調べて、価格プランを比較した表を作って」とAIエージェントに頼むと、AI自身が各社サイトを開いて価格ページを読み取り、情報を整理し、表形式のドキュメントとして出力するところまでを一気に行う。人間が各サイトを開いてコピー&ペーストする作業が不要になる点が、通常のチャットとの体感差になる。

**試す手順の一例(ChatGPT Atlas)**: ChatGPT AtlasまたはChatGPTアプリを開く →画面内の「エージェント」または「Agent mode」をオンにする →日本語でタスクを入力(例:上記の比較表作成)→ 実行中に確認を求められたら内容を確認して承認する →完成した表を確認・修正する。他ツールも「設定・機能メニューからエージェント機能をオンにし、目標を自然文で入力する」という操作感はおおむね共通している。

## 注意点・よくある誤解

- **「エージェント」を名乗る機能が全て同じ自律度とは限らない**: 単にツール呼び出し(検索や計算)ができるだけの機能まで「エージェント」と呼ぶ製品もある。導入検討時は「人間の承認なしにどこまで実行するのか」「失敗したときにどう気づけるのか」を具体的に確認する。
- **実行過程は完璧ではない**: エージェントは画面の誤クリック、意図しないボタン操作、UIの誤解釈などで静かに失敗することがある。特に外部への影響が残る操作(送信・注文・支払いなど)は、人間の最終確認を挟む運用を基本にする。
- **セキュリティ・権限管理が重要**: 業務データへのアクセス権を必要最小限に絞らないと、エージェント経由での情報漏えいや誤操作のリスクが高まる。悪意あるWebページの指示にエージェントが乗っ取られる「プロンプトインジェクション」といった攻撃も報告されている。高リスクな操作には必ず人による承認を挟む設計にする([DirectCloud](https://directcloud.jp/contents/aiagent/))。
- **コストは想定より膨らみやすい**: エージェントは1つの目標達成のために内部で何度も思考・ツール呼び出しを繰り返すため、通常のチャット1回のやり取りより消費するAI利用料が大きくなりやすい。
- **「導入すれば終わり」ではない**: Gartnerは、2026年末までに企業向けアプリの40%がタスク特化型AIエージェントを組み込む一方で、コスト増・効果不明確・ガバナンス不足を理由に2027年末までにエージェント関連プロジェクトの4割以上が中止に追い込まれると予測している。過度な期待を持たず、小さく試して効果を検証しながら広げる姿勢が要る([Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025))。

## 最初の一歩

すでに契約しているChatGPT・Claude・Geminiのいずれかで「エージェントモード」に類する機能を探し、1つだけ小さな複数ステップの調べもの(例:競合サービスの価格比較表作成)を任せてみる。出てきた結果を必ず自分の目で裏取りし、「どこまで任せられて、どこから人間が確認すべきか」の感覚をつかむことが最初の一歩になる。

## 関連トピック

- [AIの分類と生成AIの位置づけ](../part01-ai-llm-basics/ai-classification-and-generative-ai.md)
- [Difyとは何か](../part09-nocode-lowcode/dify-basics.md)
- [生成AIに向く業務・向かない業務の切り分け](../part10-business-practice/ai-task-suitability.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: AIエージェントの定義(チャットとの違い)、計画立案・ツール利用・自己点検という仕組み、MCPの一言解説、チャットAI/AIエージェント/RPAの比較表、ChatGPT・Claude・Gemini・Copilotの具体的なエージェント機能と料金、セキュリティ・コスト面の注意点を整理
- **出典**: [JAPAN AI ラボ「MCPとは」](https://japan-ai.co.jp/media/6154/)、[Anthropic Claude Cowork](https://www.anthropic.com/product/claude-cowork)、[Anthropic Computer Use発表](https://www.anthropic.com/news/3-5-models-and-computer-use)、[OpenAI Introducing ChatGPT Atlas](https://openai.com/index/introducing-chatgpt-atlas/)、[OpenAI Help Center(Atlasエージェントモード)](https://help.openai.com/ja-jp/articles/12628199-atlas-%E3%81%A7-ask-chatgpt-%E3%82%B5%E3%82%A4%E3%83%89%E3%83%90%E3%83%BC%E3%81%A8-chatgpt-%E3%82%A8%E3%83%BC%E3%82%B8%E3%82%A7%E3%83%B3%E3%83%88%E3%82%92%E4%BD%BF%E3%81%86)、[Google I/O 2026公式ブログ](https://blog.google/innovation-and-ai/sundar-pichai-io-2026/)、[Microsoft Learn(Copilot Studio)](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/fundamentals-get-started)、[Gartnerプレスリリース](https://www.gartner.com/en/newsroom/press-releases/2025-08-26-gartner-predicts-40-percent-of-enterprise-apps-will-feature-task-specific-ai-agents-by-2026-up-from-less-than-5-percent-in-2025)、[Persol Business Process Design](https://www.persol-bd.co.jp/service/salesmarketing/s-smkt/column/ai-agent/agent-rpa-difference/)、[DirectCloud](https://directcloud.jp/contents/aiagent/)
