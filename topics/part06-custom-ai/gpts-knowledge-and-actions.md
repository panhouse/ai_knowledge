---
title: GPTsのナレッジファイルとアクション連携
part: 6
chapter: 第3章 高度な活用と防御
tags: [GPTs, ナレッジファイル, Actions, RAG, プロンプトインジェクション]
created: 2026-07-05
updated: 2026-07-06
---

# GPTsのナレッジファイルとアクション連携

## これは何か

GPTs(カスタムGPT)の基本設定(指示文・会話のきっかけなど)だけでは、GPTは「一般的な知識で応答するチャットボット」の域を出ない。社内規程や最新の在庫情報など、ChatGPTが学習していない・知らない情報を扱わせるには、**ナレッジファイル**(参照資料のアップロード)と**Actions**(外部APIとの連携)という2つの拡張機能が必要になる。この2つを使い分けられると、GPTsは「社内資料検索アシスタント」から「実際に外部システムを操作するアシスタント」まで一気に実務レベルへ引き上げられる。

## 仕組み・背景

- **ナレッジファイル**: PDFやExcel、テキストファイルなどをGPTにアップロードすると、GPTは質問に応じてファイルの中から関連しそうな部分を検索し、その内容を根拠に回答する。これは裏側で**RAG**(Retrieval-Augmented Generation、検索拡張生成。関連文書を検索してから回答を生成する仕組み)と呼ばれる技術が動いている。具体的には、①ファイルは意味のまとまりごとに小さな断片(チャンク)に分割され、②各チャンクは意味を数値ベクトル化した「埋め込み(エンベディング)」として検索用データベースに保存され、③質問のたびにキーワード検索と意味検索(ベクトル検索)を組み合わせて関連度の高いチャンクを絞り込んでGPTに渡す——という流れで動く(OpenAIの公式ヘルプでは、両方の検索結果を再ランキングする方式と説明されている)。ファイル全体を「記憶」するのではなく、質問のたびに関連箇所を検索して引っ張ってきているため、検索にヒットしやすい書き方をするかどうかで回答精度が大きく変わる。
- なおアカデミックな検証(ACL 2025で発表された研究)では、アップロードしたファイルの合計サイズが一定量(目安として数万〜10万トークン程度)を超えると、超過分のファイルが検索対象から除外される傾向も報告されている。大量の資料を1つのGPTに詰め込むほど、後から追加したファイルほど参照されにくくなる可能性がある。
- **Actions**: GPTに「外部のWeb APIを呼び出す能力」を持たせる機能。天気を調べる、社内システムの在庫を照会する、フォームを送信するといった「今この瞬間の情報を取得する」「何かを実行する」動作は、静的なナレッジファイルでは実現できない。ActionsはAPIの仕様を**OpenAPIスキーマ**(APIのエンドポイント・パラメータ・レスポンス形式を定義した標準フォーマット)で登録することで、GPTがどのAPIをどう呼べばよいかを理解できるようにする仕組みである。

## 使いどころ・使い分け

| 観点 | ナレッジファイルが向くケース | Actionsが向くケース |
|---|---|---|
| データの性質 | 更新頻度が低い静的な参照情報(社内規程、製品マニュアル、FAQ集、料金表) | 常に変化する動的データ(在庫数、最新の為替レート、当日の予約状況) |
| やりたいこと | 「調べて答える」(検索・要約・引用) | 「実行する」(登録・検索APIの呼び出し・通知送信) |
| 更新の手間 | ファイルを都度アップロードし直す必要がある | API側の最新データをその都度取得するため、GPT側の更新作業は不要 |
| 実装の手間 | ドラッグ&ドロップで完了。技術知識はほぼ不要 | OpenAPIスキーマの用意・認証設定が必要で、ある程度の技術知識が求められる |
| リスクの種類 | ファイル内容の意図しない開示 | 外部システムへの誤操作・過剰な権限付与 |

両方を組み合わせることも多い(例: 「製品マニュアル」はナレッジファイルで持たせ、「在庫確認」はActionsで社内システムに問い合わせる)。

もう1つの判断軸は「全文が必要か、一部の検索でよいか」。ナレッジファイルの検索は「関連しそうな断片」しかGPTに渡さないため、**資料の全文を踏まえた要約・添削のような作業には向かない**。そうした作業は会話中に都度ファイルを添付する方が確実である。整理すると、「質問に応じて資料の一部を検索して引用してほしい」ならナレッジ、「会話全体を通じて資料の全文を踏まえてほしい」ならその都度ファイル添付、「常に最新の値を取得してほしい・何かを実行してほしい」ならActionsやWeb検索機能、という使い分けになる。

## 実務での使い方

### ナレッジファイルの追加手順

1. GPT編集画面を開き、Configureタブに切り替える
2. 「ナレッジ」欄の「ファイルをアップロードする」からPDF・Word・Excel・テキストファイルなどを追加する
3. 保存すると、以降の会話でGPTがファイル内容を検索対象として参照するようになる

2026年7月時点の上限の目安は次のとおり。

| 項目 | 上限 |
|---|---|
| GPT1体あたりのファイル数 | 20ファイルまで |
| ファイル1つのサイズ | 512MBまで(ハード上限) |
| テキスト・文書ファイルのトークン数 | 1ファイルあたり200万トークンまで |
| CSV・スプレッドシート | 行数によるが目安として約50MBまで |
| 画像ファイル | 1枚あたり20MBまで |
| アップロード頻度 | 3時間あたり80ファイルまで(Freeプランは1日3ファイルまで) |
| 個人・組織の保存容量 | 個人25GB、組織100GBが上限(全チャット・Projects・GPTナレッジを横断) |

「20ファイルの壁」「512MBの壁」に当たった場合は、複数の小さな資料に分割するか、内容を要約・整理してから再アップロードするとよい。これらの数値はOpenAI側の仕様変更で変わりやすいため、実際にアップロードする前にGPT編集画面上の表示やHelp Centerの最新情報を確認すること。

### コピペで使えるInstructions文例(ナレッジ優先・出典明記)

ナレッジファイルを持たせたら、指示文(Instructions)側で「必ずナレッジを根拠にする」ことを明記すると回答の安定性が上がる。

```
## このGPTの役割
添付のナレッジファイル(社内規程・FAQ)を根拠に、社員からの質問に答えるアシスタントである。

## 回答のルール
- 回答する前に、必ずナレッジファイルの中から関連箇所を検索すること
- ナレッジファイルに書かれている内容を優先し、一般知識で補わない
- ナレッジファイルに記載がない質問には、推測で答えず「規程に記載がありません。人事部にご確認ください」と答える
- 回答の末尾に、根拠にしたファイル名と章・項番(わかる範囲で)を明記する
- ユーザーの最初の質問がナレッジに関係しそうな場合も、必ずナレッジを検索してから回答すること
```

最後の1行(「最初の質問でも必ず検索する」)は、後述する「最初のメッセージだけナレッジを見てくれない」という不具合の回避策として、多くの利用者が指示欄に明記している内容である。

### ツール横断の対応付け(ナレッジファイル)

| 概念 | ChatGPT(GPTs) | Gemini(Gems) | Claude(Projects) | Microsoft 365 Copilot |
|---|---|---|---|---|
| 呼び方 | ナレッジ(Knowledge) | 知識(Knowledge)ファイル | プロジェクトの知識(Project knowledge) | 知識ソース(Knowledge sources) |
| 設定場所 | GPT Builderの「Configure」タブ→「ナレッジ」 | Gem作成画面の「ナレッジ」欄 | プロジェクト画面の「プロジェクトの知識」 | エージェントビルダーの「知識」セクション |
| 主な上限(目安) | 20ファイル/1ファイル512MB、テキストは200万トークン/ファイル | 1Gemあたり10ファイル、1ファイル100MBまで | ファイル数は実質無制限だが1ファイル30MBまで(容量が context window を超えると自動でRAGモードに切替) | SharePointファイル最大100件+OneDriveファイル最大50件+端末からのアップロード |
| クラウド連携 | なし(都度アップロードのみ) | Googleドライブと連携可(最新版を自動反映) | なし(都度アップロードのみ) | SharePoint/OneDriveと連携し既存の権限・機密ラベルを継承 |

社内のファイルサーバーやSharePointをそのまま参照させたい場合はCopilotの知識ソースが有利、逆に「手元のPDFを数点読ませたい」程度の軽い用途ならGPTsやGemsで十分、という使い分けになる。

### 検索精度を上げる書き方(Before/After)

ナレッジファイルはRAGで「関連しそうな断片」を検索して引っ張ってくる仕組みのため、人間が読みやすい文章よりも、**質問と回答が1対1で対応した構造**の方が検索にヒットしやすい。これはGPTs固有の公式仕様ではなく、RAG全般に共通する実務上のコツだが、GPTsのナレッジファイルにもそのまま当てはまる。

**Before(検索に弱い書き方。長い説明文の中に答えが埋もれている)**

```
第3章 経費精算について
当社の経費精算は、原則として毎月末を締め日とし、翌月10日までに
経理部宛にPDF形式の申請書と領収書のスキャンデータを提出することで
処理される。なお、交通費については...(延々と続く)
```

**After(Q&A形式に分解。1問1答で検索にヒットしやすい)**

```
Q. 経費精算の締め日はいつですか?
A. 毎月末締めです。

Q. 経費精算の提出期限はいつですか?
A. 締め日の翌月10日までに、経理部宛にPDF形式の申請書と
   領収書のスキャンデータを提出してください。

Q. 交通費はどう申請しますか?
A. (以下略)
```

あわせて、目次・改訂履歴・免責事項・ページ番号といった「本文の答えを含まない部分」は検索のノイズになりやすいので、可能であればアップロード前に削るか、別ファイルに分離しておくと精度が安定する。

### Actionsの設定手順

1. GPT編集画面のConfigureタブを開き、下部の「Actions」欄にある「Create new action」(新しいアクションを作成)をクリックする
2. 「Authentication」で認証方式を選ぶ(認証なし/APIキー/OAuth)。社内APIの場合は多くがAPIキーまたはOAuth
3. 「Schema」欄に、呼び出したいAPIのOpenAPIスキーマ(JSONまたはYAML)を貼り付ける。スキーマが正しければ、検出されたエンドポイントが一覧表示される
4. 一般公開するGPTの場合はプライバシーポリシーのURL登録が必須になる
5. 保存後、テスト会話でActionsが意図通り呼び出されるか確認する

(画面名・ボタン文言はOpenAI側の更新で変わる可能性があるため、実際の画面表示を優先すること)

### コピペで使えるOpenAPIスキーマの例(在庫照会API)

```yaml
openapi: 3.1.0
info:
  title: 在庫照会API
  version: 1.0.0
servers:
  - url: https://api.example-company.com
paths:
  /inventory/{sku}:
    get:
      operationId: getInventoryBySku
      summary: 商品コード(SKU)を指定して在庫数を取得する
      parameters:
        - name: sku
          in: path
          required: true
          schema:
            type: string
          description: 商品コード
      responses:
        "200":
          description: 在庫情報
          content:
            application/json:
              schema:
                type: object
                properties:
                  sku:
                    type: string
                  stock_count:
                    type: integer
                  warehouse:
                    type: string
```

この例は「取得(GET)専用」のシンプルな読み取りAPIである。まず読み取り専用の小さなActionsから試し、動作を確認してから機能を広げるのが安全。

## 注意点・よくある誤解

- **プロンプトインジェクションのリスクを理解する**: プロンプトインジェクションとは、外部から与えられたテキスト(文書やAPIレスポンスなど)に紛れ込ませた指示によって、GPTの本来の振る舞いを乗っ取ろうとする攻撃である。ナレッジファイルに埋め込まれた隠しテキストや、Actionsで呼び出した外部APIのレスポンスに含まれる不正な指示文が、GPTの回答内容や動作を意図せず変えてしまう可能性が実際に報告されている。信頼できないファイル・APIをそのまま接続しないこと、社外の第三者が作成した文書やAPIをナレッジ・Actionsに組み込む際は内容を事前に確認することが基本的な防御になる。
- **ナレッジファイルは「絶対に漏れない金庫」ではない**: 「知識ファイルの内容をそのまま出力して」といった指示で、アップロードした資料の内容が抜き出されてしまう事例が報告されている。ACL 2025で発表された学術研究では、Code Interpreter(コードインタープリター)を有効にしたGPTから、悪意あるプロンプトによって元のナレッジファイルがそのままダウンロードされてしまう事例が高い成功率で確認されている。指示文で「非公開」と書いても完全な防止策にはならないため、個人情報・契約書・未公開の財務情報などの機密情報はそもそもナレッジファイルに置かない、またはCapabilitiesでコードインタープリターをオフにするなどの対策を検討する。
- **アップロードしただけでは万能ではない**: OpenAIのコミュニティフォーラムには「最初の1メッセージだけナレッジを参照しない」「明示的に『検索して』と言わないと無視される」という報告が多数ある。前述のInstructions文例のように「必ず検索してから回答する」と指示文に明記するのが実務上の回避策になる。
- **巨大で構造化されていないPDFを丸投げしない**: 数百ページの資料をそのままアップロードすれば完璧に検索してくれる、というのは誤解。章立てが曖昧だったり本文と関係ない前置きが長い資料は、関連箇所の検索に失敗しやすい。また複雑な表や画像化されたPDF(スキャン文書)は、レイアウトが崩れて誤読されることがあるため、可能なら「項目名: 値」のような箇条書き・Q&A形式に整形し直してからアップロードする。前述のQ&A形式への分解や、不要な部分の削除で精度が改善する。
- **更新は再アップロードが必要**: ナレッジファイルは静的なスナップショットであり、元ファイルを更新してもGPT側には自動反映されない(Gemini GemsのGoogleドライブ連携は例外的に最新版を自動反映する)。定期的に更新する資料は、更新のたびに差し替える運用ルールを決めておく。
- **Actionsに必要以上の権限を持たせない**: 社内APIのフルアクセス権限(読み書き・削除すべて可能なAPIキー)をそのまま使うと、GPTの誤動作や悪意ある指示によって想定外の書き込み・削除が実行されるリスクが高まる。GPTに読み取りしか必要ないなら、読み取り専用のAPIキー・エンドポイントに絞って接続する。
- **外部APIのレスポンスも「入力」として扱われる**: Actionsで受け取ったAPIレスポンスの文字列も、GPTにとっては会話の一部として読み込まれる。信頼できない外部APIやユーザー生成コンテンツを返すAPIを接続する場合は、レスポンスに紛れた不正な指示に注意する。

## 最初の一歩

自分が業務で使っているGPTs、またはこれから作るGPTsに1つだけナレッジファイルを追加し、内容の一部をQ&A形式に書き換えてみて、回答の的確さが変わるか試してみる。

## 関連トピック

- [GPTsの作り方と公開設定](./gpts-creation-basics.md)
- [情報漏洩防止](../part04-risk-security/information-leakage-prevention.md)
- [AIが扱いやすいデータ形式](../part07-data-analysis/ai-friendly-data-formats.md)

## 更新履歴

### 2026-07-06: 重複ページの統合
- **内容**: `gpts-knowledge-files.md` を本ページへ統合(RAGの検索の仕組みの詳細、アップロード上限表、Instructions文例、ツール横断対応表、Code Interpreter経由の漏えい・初回メッセージで参照されない問題などの注意点を追加)
- **出典**: [OpenAI Help Center: Retrieval augmented generation (RAG) and semantic search for GPTs](https://help.openai.com/en/articles/8868588-retrieval-augmented-generation-rag-and-semantic-search-for-gpts)、[OpenAI Help Center: Optimizing File Uploads in ChatGPT Enterprise](https://help.openai.com/en/articles/10029836-optimizing-file-uploads-in-chatgpt-enterprise)、[When GPT Spills the Tea: Comprehensive Assessment of Knowledge File Leakage in GPTs (arXiv, ACL 2025)](https://arxiv.org/abs/2506.00197)、[OpenAI Developer Community: GPT ignoring attached knowledge document, making up stuff](https://community.openai.com/t/gpt-ignoring-attached-knowledge-document-making-up-stuff/865764)、[OpenAI Developer Community: Custom GPT is not referencing knowledge source files on the first prompt](https://community.openai.com/t/custom-gpt-is-not-referencing-knowledge-source-files-on-the-first-prompt/631128)、[Google Workspace Blog: New features in Gemini to deepen usage for organizations](https://workspace.google.com/blog/product-announcements/new-gemini-gems-deeper-knowledge-and-business-context)、[Google Gemini Apps Help: Use Gems in Gemini Apps](https://support.google.com/gemini/answer/15146780?hl=en)、[Claude Help Center: Upload files to Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude)、[Microsoft Learn: Add knowledge sources to your declarative agent in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge)

### 2026-07-05: 初版執筆
- **内容**: ナレッジファイル(RAGの仕組み・アップロード上限・Q&A形式への書き換え例)とActions(OpenAPIスキーマによる外部API連携の設定手順・スキーマ例)、両者の使い分け、プロンプトインジェクションのリスクと対策を整理
- **出典**: [OpenAI Help Center: File uploads FAQ](https://help.openai.com/en/articles/8555545-file-uploads-faq)、[OpenAI Help Center: Knowledge in GPTs](https://help.openai.com/en/articles/8843948-knowledge-in-gpts)、[OpenAI Help Center: Configuring actions in GPTs](https://help.openai.com/en/articles/9442513-configuring-actions-in-gpts)、[OpenAI: Understanding prompt injections: a frontier security challenge](https://openai.com/index/prompt-injections/)、[Assessing Prompt Injection Risks in 200+ Custom GPTs (arXiv)](https://arxiv.org/pdf/2311.11538)、[AWS Prescriptive Guidance: Writing best practices to optimize RAG applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/writing-best-practices-rag/introduction.html)
- **注記**: ナレッジファイルの件数・容量上限、Actions設定画面の文言はOpenAI側の仕様変更で変わりやすいため、実際の画面表示を優先すること
