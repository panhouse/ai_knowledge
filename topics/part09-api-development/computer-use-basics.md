---
title: Computer Use(画面操作エージェント)の仕組みと実務の基本
part: 9
chapter: 第4章 MCP・エージェント連携
tags: [Computer Use, 画面操作, AIエージェント, Claude, OpenAI, スクリーンショット, プロンプトインジェクション]
created: 2026-08-07
updated: 2026-08-07
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

### 対応するアクション(Anthropic Claude、2026年8月時点)

| アクション | できること |
|---|---|
| screenshot | 画面を撮影する |
| left_click / right_click / double_click | 座標`[x, y]`をクリックする |
| type | テキストを入力する |
| key / hold_key | キーボードショートカットを送る |
| scroll | 指定方向・量でスクロールする |
| left_click_drag | ドラッグ操作を行う |
| wait | 一定時間待つ |
| zoom(`computer_20251124`以降) | 画面の一部を高解像度で拡大表示する(小さい文字の読み取り精度が上がる) |

OpenAIも同様の機能を`computer-use-preview`モデルとして提供しており(ブラウザ操作エージェント「Operator」の
基盤技術)、こちらは入力$3/出力$12(100万トークンあたり、2026年時点)という専用の料金体系になっている
点がAnthropicの実装(通常のモデル料金にスクリーンショットの画像トークンが加算される方式)と異なる。

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

- **画面に埋め込まれた指示に従ってしまうリスクがある(間接プロンプトインジェクション)**:
  Webページやポップアップに悪意ある指示文が書かれていると、それに従って意図しない操作をする
  可能性がある。Anthropicは自動検知の分類器を実装し、疑わしい場合に確認を求める仕組みを
  組み込んでいるが、これに頼りきらず**機密データや取り消せない操作からは隔離する**のが前提になる
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

### 2026-08-07: 初版執筆
- **内容**: Computer Useの仕組み(スクリーンショット→判断→操作→結果確認のエージェントループ)、
  Claude(Anthropic)の対応アクション一覧(screenshot・click・type・scroll・zoom等)、
  OpenAI computer-use-previewモデルの料金(入力$3/出力$12・100万トークン)との違い、
  Function Calling・MCPとの使い分け、実装に必要な要素(仮想ディスプレイ・エージェントループ・サンドボックス)、
  精度を上げる公式推奨のプロンプト技法、間接プロンプトインジェクションを含む注意点を整理
- **出典**: [Computer use tool(Claude Platform Docs)](https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool) /
  [Anthropic computer-use-demo(GitHub)](https://github.com/anthropics/anthropic-quickstarts/tree/main/computer-use-demo) /
  [computer-use-preview pricing(economize.cloud)](https://www.economize.cloud/resources/open-ai/pricing/computer-use-preview/)
