---
title: Computer Use(画面操作エージェント)の仕組みと実務の基本
part: 9
chapter: 第4章 MCP・エージェント連携
tags: [Computer Use, 画面操作, AIエージェント, Claude, OpenAI, Gemini, スクリーンショット, プロンプトインジェクション]
created: 2026-08-07
updated: 2026-09-26
---

# Computer Use(画面操作エージェント)の仕組みと実務の基本

## これは何か

Computer Use(コンピュータ操作)は、AIモデルに**画面のスクリーンショットを見せ、
マウス操作・キーボード入力を指示として返させる**ことで、人間がPCを操作するのと同じ方法で
アプリやWebサイトを自動操作させる技術である。

[Function Calling](function-calling-basics.md)がAPIの決まった入出力を呼び出す仕組みであるのに対し、
Computer Useは**API連携のない旧来のソフトウェアやWebサイトでも、画面が見えればAIに操作させられる**のが特徴。
[Claude Cowork](../part11-ai-agents/claude-cowork-basics.md)や[ChatGPTのエージェント機能](../part03-ai-chat-tools/chatgpt-agent-mode-feature.md)
のようなブラウザ・PCを操作するエージェント製品の**内部で使われている中核技術**がこれである。

## 仕組み・背景

### エージェントループ

Computer Useは次のサイクル(エージェントループ)で動く。

```
1. スクリーンショットを撮る
2. AIモデルがスクリーンショットを見て、次に何をすべきか判断する
3. AIモデルが「座標[x, y]をクリック」「テキストを入力」などの操作を指示として返す
4. アプリケーション側がその指示を実際のマウス・キーボード操作に変換して実行する
5. 実行結果(新しいスクリーンショット)を1に戻してAIモデルに渡す
```

AIモデル自身はOS・ブラウザに直接つながっておらず、**アプリケーション側が操作を仲介する**。
Anthropicの実装例では、この一連のやりとりをDockerコンテナ内の仮想ディスプレイ(Xvfb)上で行い、
AIが操作する環境を人間から隔離している([Claude Platform Docs](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool))。

### 対応するアクション(Anthropic Claude、2026年9月時点)

旧ツールバージョン`computer_20251124`は、2026年8月19日に後継の**`computer_toolset_20260801`**へ
置き換えられ、Claude API・Google Cloud上でGA(一般提供)された(Amazon Bedrockでは旧版が
ベータのまま継続利用可)。新ツールセットはアクションが17種類に拡張されている。

| アクション | できること |
|---|---|
| screenshot | 画面を撮影する |
| left_click / right_click / middle_click / double_click / triple_click | 座標`[x, y]`をクリックする |
| mouse_move / left_mouse_down / left_mouse_up / cursor_position | マウス移動・ボタン押下/解放・現在位置の取得(新ツールセットで追加) |
| type | テキストを入力する |
| key / hold_key | キーボードショートカットを送る |
| scroll | 指定方向・量でスクロールする |
| left_click_drag | ドラッグ操作を行う |
| wait | 一定時間待つ |
| zoom | 画面の一部を高解像度で拡大表示する(小さい文字の読み取り精度が上がる) |

新ツールセットに対応するモデルはClaude Opus 5.5/5/4.8、Sonnet 5、Fable 5.1/5、Mythos 5.1/5
(2026年9月時点)。課金は通常のトークン従量課金のままだが、**ツールセットを宣言するだけで
入力トークンが約4,500トークン増加**する(zoomアクションを無効化すると約410トークン分減らせる)。

OpenAIが提供していた`computer-use-preview`モデル(ブラウザ操作エージェント「Operator」の基盤技術、
入力$3/出力$12・100万トークンあたり)は**2026年7月23日に廃止**された。Operatorの機能はその後
「ChatGPT agent」に統合され、さらに2026年7月9日ローンチの新エージェント**「ChatGPT Work」**に
引き継がれている(Work内の「Computer Use」機能がユーザーのPC上でクリック・入力・ファイル操作を行う)。
単体モデルとしての公開料金は確認できず、ChatGPT側の統合レートカードに含まれる形になっている。

Googleも同様の技術を「Project Mariner」として開発していたが、2026年5月4日に単体プロダクトとしては
終了し、技術はGemini API・Gemini Agent・Chromeの自動閲覧機能に統合された。後継として
**Gemini 2.5 Computer Use**がGemini APIでパブリックプレビュー提供されており、料金は入力
$1.25/100万トークン・出力$10/100万トークン(コンテキストが20万トークンを超える場合は入力$2.50/100万トークン)。
その後継として「Gemini 3.7 Flash」でもComputer Useのプレビューが提供されている。

## 使いどころ・使い分け

### Function CallingやMCPで足りない場面で使う

| 状況 | 向く技術 |
|---|---|
| API・SDKが用意されている外部サービスを呼びたい | [Function Calling](function-calling-basics.md) |
| 複数ツールを標準化された方法で接続したい | [MCP](mcp-basics.md) |
| **API が用意されていない社内システム・レガシーな画面を操作したい** | **Computer Use** |
| ブラウザでログインが必要な複雑な操作を自動化したい | **Computer Use** |

Computer Useは「他に手段がないときの最後の選択肢」と位置づけるのが実務上の基本である。
API が使えるなら Function Calling や MCP の方が高速・低コスト・低リスクになる。

### 自分で実装するか、既製品を使うか

- **既製品のエージェント(Claude Cowork、ChatGPT Workなど)を使う**: Computer Useの仕組みを
  意識せずに済む。非エンジニアはこちらを選ぶ
- **自分でComputer Useを実装する**: 社内独自システムの自動化や、既製品にない業務フローへの
  組み込みが必要な場合。開発リソースが必要になる([Anthropic公式のリファレンス実装](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)が公開されている)

## 実務での使い方

### 実装に必要な要素

Computer Useを自分で組み込むには、最低限以下の環境を用意する。

```
1. 仮想ディスプレイ(操作対象の画面を表示する仮想環境)
2. AIとその環境をつなぐエージェントループ(アクションの実行と結果の受け渡し)
3. サンドボックス(コンテナなどでAIの操作範囲を隔離する)
```

### 精度を上げるコツ(公式ガイドより)

- **各操作の後にスクリーンショットを撮らせ、結果を確認させる**: 「操作後に必ずスクリーンショットを撮って、
  意図した状態になっているか確認してください。違っていればやり直してください」と明示すると、
  AIが「操作したはず」で先に進んでしまう事故を防げる
- **繰り返し行う操作は、成功例のスクリーンショットと操作手順をプロンプトに含める**
- **ドロップダウンやスクロールバーはクリックが苦手なことがある**: キーボードショートカットを使うよう
  促すと安定する
- **ログイン情報を渡す場合は専用のタグで囲む**(例: `<robot_credentials>`)。ただし
  ログインを伴う操作は間接プロンプトインジェクションのリスクが上がるため、慎重に検討する

## 注意点・よくある誤解

- **ベンチマーク上は人間を超えても、難度の高いタスクではまだ実用に届かない**: 定番ベンチマーク
  「OSWorld-Verified」では上位モデルが人間の基準値(72.4%)を超え80%台後半に達しているが
  (2026年時点)、より難度を上げた新ベンチマーク「OSWorld 2.0」(2026年6月公開)では、
  最上位クラスのモデル・設定でも二値の成功率が20%程度にとどまるという報告がある。
  「ベンチマークで人間超え」という見出しだけで実務の複雑な操作を任せきれると判断しないこと
- **画面に埋め込まれた指示に従ってしまうリスクがある(間接プロンプトインジェクション)**:
  Webページやポップアップに悪意ある指示文が書かれていると、それに従って意図しない操作をする
  可能性がある。OWASPの2026年のエージェントAIセキュリティ調査では、間接プロンプトインジェクション
  事例の85.2%が「これはセキュリティ更新です」といった権威を装う文言を使っていたと報告されている。
  Anthropicは自動検知の分類器を実装し、疑わしい場合に確認を求める仕組みを組み込んでいるが、
  これに頼りきらず**機密データや取り消せない操作からは隔離する**のが前提になる
  ([プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md))
- **専用の仮想マシン・コンテナで動かす**: 本番の業務端末で直接動かさず、権限を絞った
  隔離環境を使うことが公式にも強く推奨されている
- **金銭が関わる操作・同意が必要な操作は人が確認する**: 決済、利用規約への同意、
  クッキーの受け入れなど、後戻りしにくい操作の前には人間の確認を挟む設計にする
- **「見たものが正しいと思い込む」失敗が起きやすい**: AIは操作結果を確認せずに次に進むことがある。
  各ステップでの検証を明示的に指示に含める
- **Function CallingやMCPで代替できないか先に検討する**: 画面操作は遅く、UIの変更に弱く、
  トークン消費(スクリーンショットの画像)も大きい。API連携が使えるなら常にそちらを優先する

## 最初の一歩

[Anthropicの公式リファレンス実装](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo)を
Dockerで立ち上げ、「デスクトップの電卓アプリを開いて1+1を計算して」のような単純な操作を1つ試してみる。
隔離環境でどこまで安定して動くかを体感することが、実務導入の判断材料になる。

## 関連トピック

- [Function Calling(Tool Calling)の基本](function-calling-basics.md)
- [MCP(Model Context Protocol)の基本](mcp-basics.md)
- [Claude Coworkの基本](../part11-ai-agents/claude-cowork-basics.md)
- [ChatGPTのエージェント機能(旧ChatGPT Agent→ChatGPT Work)とスケジュールタスク(Tasks)](../part03-ai-chat-tools/chatgpt-agent-mode-feature.md)
- [Gemini Spark(Google)の基本](../part03-ai-chat-tools/gemini-spark-basics.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)

## 更新履歴

### 2026-09-26: 各社の最新状況を反映して最新化
- **内容**: Anthropicのcomputer useツールが`computer_20251124`から`computer_toolset_20260801`
  (2026年8月19日GA、17アクションに拡張、対応モデルをOpus 5.5/5/4.8・Sonnet 5・Fable 5.1/5・
  Mythos 5.1/5に更新、ツール宣言だけで入力トークンが約4,500増加)に変わったことを反映。
  OpenAIの`computer-use-preview`が2026年7月23日に廃止され、Operator→ChatGPT agent→
  「ChatGPT Work」のComputer Use機能へ引き継がれた経緯を追記。GoogleのProject Marinerが
  2026年5月4日に終了しGemini API・Agent・Chromeに統合されたこと、後継の
  「Gemini 2.5 Computer Use」(パブリックプレビュー、入力$1.25/出力$10・100万トークン)を追加。
  ベンチマーク(OSWorld-Verifiedでの人間超え、より難度の高いOSWorld 2.0での成功率20%程度という
  ギャップ)と、OWASPの2026年調査による間接プロンプトインジェクションの手口(権威詐称型が85.2%)を
  注意点に追加
- **出典**: [Claude Platform Docs「Computer use tool」](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool)、
  [OpenAI API Deprecations](https://developers.openai.com/api/docs/deprecations)、
  [ppc.land「OpenAI kills Atlas browser, folds it into new ChatGPT Work agent」](https://ppc.land/openai-kills-atlas-browser-folds-it-into-new-chatgpt-work-agent/)、
  [Android Headlines「Google Shuts Down Project Mariner」](https://www.androidheadlines.com/2026/05/google-shuts-down-project-mariner-ai-agent.html)、
  [byteiota「Gemini 2.5 Computer Use Is Now an API」](https://byteiota.com/gemini-2-5-computer-use-is-now-an-api-heres-how-to-build-with-it/)、
  [Steel.dev OSWorldリーダーボード](https://leaderboard.steel.dev/leaderboards/osworld/)、
  [arXiv「OSWorld 2.0」](https://arxiv.org/pdf/2606.29537)、
  [Help Net Security「Prompt injection still drives most agentic AI security failures」](https://www.helpnetsecurity.com/2026/06/11/owasp-prompt-injection-ai-security-failures/)

### 2026-08-07: 初版執筆
- **内容**: Computer Useの仕組み(スクリーンショット→判断→操作→結果確認のエージェントループ)、
  Claude(Anthropic)の対応アクション一覧(screenshot・click・type・scroll・zoom等)、
  OpenAI computer-use-previewモデルの料金(入力$3/出力$12・100万トークン)との違い、
  Function Calling・MCPとの使い分け、実装に必要な要素(仮想ディスプレイ・エージェントループ・サンドボックス)、
  精度を上げる公式推奨のプロンプト技法、間接プロンプトインジェクションを含む注意点を整理
- **出典**: [Computer use tool(Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) /
  [Anthropic computer-use-demo(GitHub)](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) /
  [computer-use-preview pricing(economize.cloud)](https://www.economize.cloud/resources/open-ai/pricing/computer-use-preview/)
