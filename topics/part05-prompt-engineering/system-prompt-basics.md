---
title: システムプロンプトの役割と書き方
part: 5
chapter: 第1章 基本原則
tags: [システムプロンプト, カスタム指示, System Prompt, API, カスタムAI]
created: 2026-07-06
updated: 2026-08-15
---

# システムプロンプトの役割と書き方

## これは何か

毎回のやり取りで「あなたは経験豊富な広報担当者として」「敬語で」「300文字以内で」と同じ前置きを打っていないだろうか。**システムプロンプト**とは、そうした「毎回書くべき前提条件」をAIの裏側にあらかじめ登録しておき、以後のすべての会話に自動的に効かせ続ける「土台の指示」のことである。ユーザーが毎回入力する会話文(以下「通常プロンプト」と呼ぶ)とは別のレイヤーにあり、会話中に何を尋ねても常に裏側で参照される点が最大の特徴である。

この概念を知っておく価値は3つある。

1. **毎回同じ指示を書く手間がなくなる**: 役割・トーン・出力形式などを一度登録すれば、以後は本題だけを入力すればよい
2. **AIの「人格」や制約を固定化できる**: 「機密情報は外に出さない」「特定の話題には答えない」といったルールを会話ごとの言い忘れなく徹底できる
3. **社内向けカスタムAI・チャットボット構築の土台になる**: GPTsやDifyのチャットボットなど「誰かに配布するAI」は、配布先の人が触れない裏側にシステムプロンプトを埋め込むことで動作を規定している

開発者がAPIを使ってアプリやチャットボットを作る際の「`system`ロール・パラメータ」と、ChatGPTの「カスタム指示」やClaude Projectsの「指示」のようなチャット画面上の機能は、名前も操作方法も異なるが**技術的には同じ概念の異なる実装**である。両者とも「ユーザーが入力する通常プロンプトより優先度の高い、裏側の指示」をモデルに渡している点で一致する。この対応関係を知っていると、「ChatGPTのカスタム指示で効いていた設定を、API経由の自社ツールでも再現するには`system`パラメータに同じ文面を入れればよい」といった橋渡しができるようになる。

## 仕組み・背景

### 通常プロンプトとの違い

| | 通常プロンプト(ユーザープロンプト) | システムプロンプト |
|---|---|---|
| 入力するタイミング | 会話のたびに毎回 | 事前に1回(以後は自動適用) |
| 効く範囲 | その発言・その返答のみ | 会話全体(すべてのやり取り) |
| 優先度 | システムプロンプトの制約内で処理される | 通常プロンプトより優先度が高い(モデルが指示の衝突時に参照する土台) |
| 主な内容 | 「今回やってほしいこと」(タスク) | 「ずっと守ってほしいこと」(役割・トーン・制約・出力形式) |
| 実装例 | チャット画面への入力文、APIの`user`ロール | カスタム指示、Project指示、Gem指示、APIの`system`ロール/パラメータ |

[プロンプトの基本構成要素](prompt-basic-structure.md)で扱った「役割・タスク・出力形式」といった要素そのものは同じだが、システムプロンプトはこれらを**都度書くのではなく、事前に固定化して裏側に置く**という点が異なる。いわば、通常プロンプトが「その場で渡す指示書」、システムプロンプトが「あらかじめ配っておく行動規範・マニュアル」に相当する。

### 開発者向けAPIでの実装(2026年8月時点)

API(開発者がプログラムからAIモデルを呼び出す際の窓口)では、システムプロンプトは各社で少しずつ異なる名前・仕組みで実装されている。

| 提供元 | API | 実装方法 | 補足 |
|---|---|---|---|
| OpenAI | Chat Completions API | `messages`配列内の`role: "developer"`(o1以降の全モデルの標準ロール。`system`は旧世代モデル向けの後方互換として残るのみで非推奨) | 2025年に`system`から`developer`への呼称移行が完了しており、2026年7月時点で新規に実装するならGPT-4o等の旧世代を除き`developer`を使うのが基本 |
| OpenAI | Responses API(推奨の新方式) | トップレベルの`instructions`パラメータ、または`role: "developer"`のメッセージ | `input`配列とは別枠。優先度は`input`内の指示より高いが、`previous_response_id`で会話を継続する場合、前ターンの`instructions`は自動的に持ち越されないため、安定した指示は毎回再送する必要がある。なお同社の旧「Assistants API」(会話・ファイル管理を丸ごと担っていたAPI)は2026年8月26日に廃止予定(本稿執筆時点で残り2週間を切っている)で、`/v1/assistants`・`/v1/threads`等のエンドポイントは廃止後リクエストが失敗するようになる。Responses APIへの移行が必須である |
| Anthropic(Claude) | Messages API | トップレベルの`system`パラメータ(文字列または配列) | `messages`配列の中の1要素ではなく、独立したフィールド。そのため「systemメッセージを会話の先頭に置く」という発想自体がなく、常に別枠で渡す。プロンプトキャッシュ(同じ入力を再利用してコスト・速度を最適化する仕組み)のキャッシュポイントもここに置ける |
| Google(Gemini) | Gemini API | `systemInstruction`パラメータ(`role`と`parts`を持つオブジェクト) | モデルインスタンス生成時、またはリクエストごとに指定。Gemini全モデルで利用可能 |

3社に共通するのは、「システムプロンプト用の指示は、ユーザーの発言とは別の入力枠に分離されており、モデル内部で優先的に扱われる」という設計思想である。自社でAIチャットボットやカスタムAIをAPI経由で作る場合、この専用枠に固定の役割・ルールを入れ、ユーザーの発言は毎回変わる`user`枠に入れる、という分担が基本形になる。

## 使いどころ・使い分け

| 状況 | 使うべきもの |
|---|---|
| 単発の質問・その場限りの依頼 | 通常プロンプト(そのつど[基本構成要素](prompt-basic-structure.md)を書く) |
| 同じ役割・トーン・出力形式で何度もやり取りする | システムプロンプト(カスタム指示・Project指示など)で固定化 |
| 特定の業務用途に絞ったAIを社内配布したい | システムプロンプト前提のカスタムAI([GPTsの作り方](../part06-custom-ai/gpts-creation-basics.md)など)を作る |
| プロジェクト・案件単位で参照資料やルールが変わる | ChatGPTの「プロジェクトの指示」やClaude Projectsのように、プロジェクトスコープのシステムプロンプトを使う(個人全体のカスタム指示とは別枠で設定できる) |
| 自社システムからAPIを叩いて自動応答させたい | APIの`system`ロール/パラメータに固定指示を渡す設計にする |

判断の軸は単純で、「この指示は今回だけ効けばよいか、それとも今後ずっと効いてほしいか」で決める。「今後ずっと」に該当する指示が会話の中で何度も繰り返されている場合、それはシステムプロンプト化すべきサインである。

## 実務での使い方

### ツール横断の対応表(2026年8月時点、設定場所まで)

| ツール | 機能名 | 設定場所 |
|---|---|---|
| ChatGPT(個人の全チャット共通) | カスタム指示 | 左下のアカウントアイコン→「パーソナライズ」→「カスタム指示」。「自分について」「回答方法」の2欄に各1,500文字まで登録可。別欄の「基本のスタイル」(Professional・Friendly等のプリセット+温かみ・熱量のスライダー)は口調だけを変える機能で、カスタム指示とは別枠 |
| ChatGPT(プロジェクト単位) | プロジェクトの指示 | 対象プロジェクトを開く→プロジェクト名の右にある設定アイコン(歯車、または「…」の3点メニュー)→「Instructions(指示)」。そのプロジェクト内の会話にのみ適用され、グローバルなカスタム指示より優先される |
| Claude | プロジェクトの指示(Project instructions) | 左サイドバーの「Projects」からプロジェクトを作成・選択→「Set project instructions」(既存プロジェクトでは設定アイコンから開く)→保存。ナレッジ(参照資料、1ファイル30MBまで)の追加も同じプロジェクト画面から行う |
| Gemini(役割特化のカスタムボット) | Gem(カスタムGem)の指示 | gemini.google.com→左メニュー「Gemを表示」→「Gemを作成」(旧称「Gemマネージャー」の「+新しいGem」)→名前と指示欄に役割・ルールを入力→右側のプレビューで動作確認→保存。ナレッジ(アップロードファイル・Google Drive)や既定で起動するツール(Deep Research・Canvas等)の紐付けも同画面。2026年のアップデートでGemの作成・利用は無料プランを含む全ユーザーに開放されている |
| Gemini(アプリ全体の恒常設定) | 「Geminiへのカスタム指示」(パーソナル インテリジェンス) | メニューアイコン→「設定とヘルプ」→「パーソナル インテリジェンス」→「Geminiへのカスタム指示」。**個人のGoogleアカウント限定**の機能で、職場・学校・管理対象アカウントでは利用できない点に注意 |
| Microsoft Copilot(無料版・全チャット共通) | カスタム指示 | チャット画面右上の「…」→「設定」→「個人用設定」→カスタム指示のトグルをオン→「指示の編集」 |
| Microsoft 365 Copilot(業務用エージェント) | エージェント ビルダーの「指示」 | Microsoft 365 Copilotアプリ左ペイン「エージェント」→「+新しいエージェント」→「構成」タブの「指示」欄。より本格的な配布・外部連携が必要ならCopilot Studio(copilotstudio.microsoft.com)の同名の欄を使う |
| Dify(ノーコード開発ツール) | LLMブロックの「SYSTEM」プロンプト欄 | アプリのワークフロー編集画面→LLMブロックを選択→プロンプト設定で「SYSTEM」を選び入力(「USER」欄とは別枠) |
| OpenAI API / Anthropic API / Gemini API | `developer`ロール(旧`system`)・`system`パラメータ・`systemInstruction` | プログラムから各APIを呼び出す際にパラメータとして指定(上表参照) |

Gemini・Copilotはそれぞれ「役割特化の専用ボットを作る仕組み」(Gem、エージェントビルダー)と「アプリ全体に効く恒常設定」(Geminiへのカスタム指示、Copilotのカスタム指示)の2階建てになっている点に注意。前者は[Gem(Geminiのカスタムボット機能)の基本](../part06-custom-ai/gemini-gem-feature.md)・[Microsoft Copilot Studioによるカスタムエージェント作成の基本](../part06-custom-ai/copilot-agent-builder-basics.md)、後者は本ページの表がそれぞれ対応する。

### 良いシステムプロンプトを書くコツ

1. **役割を固定する**: 「あなたは◯◯社のカスタマーサポート担当です」のように、AIに一貫して名乗らせたい立場を明記する
2. **トーン・文体を明文化する**: 「です・ます調」「絵文字は使わない」など、毎回言わなくても守ってほしい文体ルールを書く
3. **出力形式を固定する**: 「回答は必ず結論→理由→次のアクションの順」のように、構造をテンプレート化する
4. **禁止事項・対応範囲を明記する**: 「料金に関する質問には答えず、営業担当への連絡を案内する」のように、やってほしくないことも具体的に書く
5. **見出し(Markdown)や`<タグ>`(XML)で構造化する**: 項目が増えるほど、`##`見出しで意味のまとまりを分けるか、`<role>`「役割」・`<context>`「文脈」・`<constraints>`「制約」・`<output_format>`「出力形式」のようなXMLタグで区切った方がAIが指示を読み取りやすい。Anthropicの公式プロンプトエンジニアリングガイドも、指示・文脈・例示・入力を別々のタグで囲むと解釈のブレが減ると明言している。Markdown見出しは人間にも読みやすく汎用性が高い一方、XMLタグは「指示」「例示」「入力データ」のように性質の異なる情報を厳密に分離したい場合に効果を発揮する。どちらか一方に決めうちせず、プロンプトが長く要素が混在するほどタグ分けを厚くするとよい
6. **例示(few-shot)を入れる**: 期待する出力の型・トーンを言葉で説明するより、3〜5個程度の具体例を`<example>`タグ等で示す方が安定する。例は「実際のユースケースに近いこと」「境界的なケースを含め多様であること」を意識すると、AIが変な共通点を学習してしまう事故を防げる
7. **粒度は「ちょうどよい高さ」にする**: 細かすぎる手順を逐一書くと例外に対応できず脆くなり、逆に抽象的すぎると具体的な行動に落とし込めない。まず要点だけで運用し、実際のやり取りで外れた挙動が出た箇所だけ加筆していく

### コピペで使えるシステムプロンプトの雛形

ChatGPTのカスタム指示・Claude Projectsの指示・Gemの指示・APIの`system`パラメータのいずれにも、以下の骨格をそのまま使い回せる。

```
## 私について
- 職種・立場: [例: 中小製造業の営業企画担当]
- 目的: [例: 見積書のドラフト作成と、顧客への提案文面の作成を効率化したい]
- 知識レベル: [例: AI・専門用語には詳しくない前提で説明してほしい]

## 会社について
- 会社名・事業内容: [例: 産業用センサーの製造・販売を行う従業員80名のメーカー]
- 想定する顧客・読み手: [例: 取引先の購買担当者、社内の上司]
- 社内で使ってはいけない表現・NGワード: [例: 「業界最速」「絶対」など誇大な言い回し]

## 回答のルール
- トーン: [例: 丁寧だが堅すぎない、ビジネスメールで使える敬語]
- 出力形式: [例: 結論を先に1行、その後に理由や補足を箇条書き3点以内]
- 分量: [例: 特に指定がない限り400字以内]
- 不確かな情報: [例: 断定できない場合は「要確認」と明記し、勝手に数値を作らない]
- 対応してほしくない依頼: [例: 契約書の最終判断や法的助言は行わず、専門家への確認を促す]
```

各項目の`[ ]`を自分の状況に置き換えて登録するだけで、以後は「見積書のドラフトを作って」のような本題だけを入力すれば、毎回同じ前提条件が自動的に効くようになる。

## 注意点・よくある誤解

- **システムプロンプトは「絶対のルール」ではない**: モデルは通常プロンプトより優先して扱う設計だが、ユーザー(あるいは悪意ある第三者が仕込んだ外部コンテンツ)からの巧妙な誘導によって指示が上書きされてしまうことがある。「システムプロンプトに書いておけば安全」という過信は禁物で、機密情報の保護や不正操作の防止を狙うなら、システムプロンプトの工夫だけに頼らず、外部からの入力を検証する・出力側でチェックするといった多層的な対策が必要になる。攻撃の仕組みと具体的な対策は[プロンプトインジェクションとは何か](../part04-risk-security/prompt-injection-basics.md)で詳しく扱っている
- **長く書けば効くわけではない**: 情報を詰め込みすぎると、AIがどの指示を優先すべきか判断しづらくなり、逆に守られない項目が増える。まずは要点だけで運用し、実際に外れた挙動が出た部分だけ加筆する方が効率的
- **個人のカスタム指示とプロジェクト単位の指示は別枠で管理される**: ChatGPTやClaudeでは、個人アカウント全体に効く設定と、特定プロジェクト・Gem内だけに効く設定が独立している。どちらに書いたか忘れて「なぜ設定した指示が効かないのか」と混乱しやすいので、用途に応じて登録場所を意識する
- **Geminiの「アプリ全体のカスタム指示」は個人アカウント限定**: 「Geminiへのカスタム指示」(パーソナル インテリジェンス)は、会社・学校の管理対象Googleアカウントでは利用できない。業務用アカウントで同等のことをしたい場合は、Gemの指示欄か、法人向けのGoogle Workspace with Geminiの設定を使う必要がある
- **APIは`system`ロールから`developer`ロールへの移行が進んでいる**: OpenAIのAPIでは、o1以降の新しいモデルは`developer`ロールが標準になっており、`system`ロールは旧世代モデル向けの後方互換としてのみ残っている。自社で新規開発する際は、利用モデルの公式ドキュメントで現在の推奨ロールを確認する

## 最初の一歩

自分がAIに毎回打っている「決まり文句」の前置き(役割・トーン・文字数など)を1つ思い出し、使っているツールのカスタム指示・Project指示・Gem指示のいずれかにそのまま登録してみて、次回から本題だけで済むかを確認する。

## 関連トピック

- [プロンプトの基本構成要素](prompt-basic-structure.md)
- [プロンプトテンプレート化(変数管理・再利用のコツ)](prompt-templating.md)
- [プロンプトインジェクションとは何か(仕組みと対策)](../part04-risk-security/prompt-injection-basics.md)
- [ChatGPTの初期設定とカスタム指示の書き方](../part03-ai-chat-tools/chatgpt-custom-instructions.md)
- [ChatGPTの「プロジェクト」機能](../part03-ai-chat-tools/chatgpt-projects-feature.md)
- [Claude(Anthropic)の「プロジェクト」機能の基本](../part06-custom-ai/claude-projects-basics.md)
- [Gem(Geminiのカスタムボット機能)の基本](../part06-custom-ai/gemini-gem-feature.md)
- [Microsoft Copilot Studioによるカスタムエージェント作成の基本](../part06-custom-ai/copilot-agent-builder-basics.md)
- [GPTsの作り方と公開設定](../part06-custom-ai/gpts-creation-basics.md)

## 更新履歴

### 2026-08-15: 書き方のコツにXMLタグ構造化・few-shot例示を追加、Gemini GemとAssistants API廃止の記述を更新
- **内容**: Anthropic公式のプロンプトエンジニアリングガイドを確認し、「良いシステムプロンプトを書くコツ」にMarkdown見出しと並ぶ構造化手法として`<role>`・`<context>`・`<constraints>`等のXMLタグ、および3〜5個の具体例(few-shot)を追加する項目を新設した。Gemini Gemは2026年のアップデートで作成・利用が無料プランにも開放されたこと、作成画面が「Gemを表示」→「Gemを作成」に簡略化されたことを反映。OpenAI Assistants APIの廃止(2026年8月26日予定)が本稿執筆時点で目前に迫っている旨を明記した。その他のツール横断対応表(ChatGPT・Claude Projects・Copilotエージェントビルダー)は現行の画面遷移と一致することをWeb検索で再確認済み
- **出典**: [Claude Docs: Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)、[Claude Docs: Use XML tags to structure your prompts](https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/use-xml-tags)、[Google Gemini アプリ ヘルプ: Gem を使用する](https://support.google.com/gemini/answer/15146780?hl=ja)、[Google Gemini アプリ ヘルプ: カスタム Gem 作成のヒント](https://support.google.com/gemini/answer/15235603?hl=ja)、[OpenAI Developer Community: Assistants API beta deprecation — August 26, 2026 sunset](https://community.openai.com/t/assistants-api-beta-deprecation-august-26-2026-sunset/1354666)、[OpenAI API: Deprecations](https://developers.openai.com/api/docs/deprecations)

### 2026-07-21: ツール横断の対応表とAPI実装の記述を最新化
- **内容**: ChatGPT・Claude・Gemini・Microsoft Copilotの設定場所を、各ツールの詳細ページ(2026-07-06執筆)と最新のWeb検索で再確認し、正確な画面遷移に更新。特にGeminiは「Gem(役割特化ボット)」と「Geminiへのカスタム指示(パーソナル インテリジェンス、個人アカウント限定)」、Copilotは「無料版のカスタム指示」と「M365 Copilotのエージェントビルダー」がそれぞれ別機能であることを明記。OpenAI APIは`system`ロールから`developer`ロールへの移行が完了している点、Assistants APIが2026年8月26日に廃止予定である点を追記し、関連トピックにツール別の詳細ページへのリンクを追加した
- **出典**: [Google Gemini アプリ ヘルプ: カスタム指示で Gemini の回答をカスタマイズする](https://support.google.com/gemini/answer/16598625?hl=ja)、[Microsoft Learn: Microsoft 365 Copilotでエージェント ビルダーを使用してエージェントをビルドする](https://learn.microsoft.com/ja-jp/microsoft-365/copilot/extensibility/agent-builder-build-agents)、[Qiita: Microsoft 365無償版のCopilot Chatガイド(38)カスタム指示の使い方](https://qiita.com/Shinyas77/items/1b85ea7545d9f020ad5e)、[Dify Docs: LLM node](https://docs.dify.ai/en/guides/workflow/node/llm)、[Aurelio AI: OpenAI Developer Role](https://www.aurelio.ai/reference/openai-developer-role)、[Zoho Help: Deprecation Notice - OpenAI Assistants API will be shut down on August 26, 2026](https://help.zoho.com/portal/hi/community/topic/deprecation-notice-openai-assistants-api-will-be-shut-down-on-august-26-2026?page=54)

### 2026-07-06: 初版執筆
- **内容**: システムプロンプトと通常プロンプトの違い、OpenAI/Anthropic/GeminiのAPIにおける実装方式の比較、ChatGPT・Claude・Gemini・Copilot・Difyでの設定場所、良い書き方のコツとコピペ用テンプレート、プロンプトインジェクションとの関係(過信への注意)をまとめた
- **出典**: [OpenAI Developer Community: System and Developer Roles in messages and Instructions in Responses.Create?](https://community.openai.com/t/system-and-developer-roles-in-messages-and-instructions-in-responses-create/1370516)、[OpenAI Text generation Guide](https://platform.openai.com/docs/guides/text)、[Anthropic Claude Platform Docs: Using the Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)、[Anthropic Prompting best practices](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices)、[Google AI for Developers: Generating content](https://ai.google.dev/api/generate-content)、[OpenAI Help Center: ChatGPT カスタム指示](https://help.openai.com/ja-jp/articles/8096356-chatgpt-custom-instructions)、[Microsoft Learn: エージェントの指示を記述する](https://learn.microsoft.com/ja-jp/microsoft-copilot-studio/authoring-instructions)、[Claude Help Center: How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects)
