---
title: GPTsのナレッジファイル活用
part: 5
chapter: 第2章 高度な活用
tags: [GPTs, ナレッジファイル, カスタムGPT, RAG]
created: 2026-07-05
updated: 2026-07-05
---

# GPTsのナレッジファイル活用

## これは何か

社内マニュアル・FAQ・商品カタログなどを、質問のたびにChatGPTへコピペしているなら、その資料をGPTs(カスタムGPT)の「ナレッジ」に一度アップロードしておけば、以降はGPTが自動でその中身を参照して回答してくれる。ナレッジファイルは、GPTに「専用の参照資料」を持たせる機能であり、都度の貼り付け作業をなくし、複数人で同じ前提知識を共有できる状態にするための仕組みである。

## 仕組み・背景

ナレッジファイルの中身は、丸ごとプロンプトに流し込まれているわけではない。裏側ではRAG(Retrieval-Augmented Generation、検索拡張生成。質問に関連する情報を外部データから検索してから回答を生成させる方式)という仕組みが使われている。

1. **チャンク化(分割)**: アップロードしたファイルは、意味のまとまりごとに数百トークン程度の小さな断片(チャンク)に分割される
2. **埋め込み(エンベディング)**: 各チャンクは、意味を数値ベクトルに変換した「埋め込み」としてベクトルストア(検索用データベース)に保存される
3. **検索**: ユーザーの質問も同じ方式でベクトル化され、意味が近いチャンクをキーワード検索とベクトル検索の両方で探し出し、関連度の高いものに絞り込んでからGPTに渡す(OpenAIの公式ヘルプでは、キーワード検索と意味検索を組み合わせて再ランキングする方式と説明されている)

つまりGPTは「ファイル全体を毎回読んでいる」のではなく「質問に関連しそうな断片だけを検索して参照している」。これが、後述する「ちゃんとアップロードしたのに参照してくれない」という現象の一因になる。

なお、アカデミックな検証(ACL 2025で発表された研究)によれば、アップロードしたファイルの合計サイズが一定量(目安として数万〜10万トークン程度)を超えると、超過分のファイルは検索対象から除外される傾向があることも報告されている。大量の資料を1つのGPTに詰め込むほど、後から追加したファイルほど参照されにくくなる可能性がある。

## 使いどころ・使い分け

| ケース | ナレッジファイルが向く/向かない | 理由 |
|---|---|---|
| 社内規程・FAQ・マニュアルへの回答 | 向く | 「規程に何が書いてあるか」を検索して答える用途に最適 |
| 用語集・商品スペック表の参照 | 向く(表は簡潔なQ&A化を推奨) | 構造が単純なら検索精度が出やすい |
| 常に全文を踏まえた要約・添削をしたい | 向かない | 検索は「一部の断片」しか渡さないため、全文把握が必要な作業には不向き。会話中に都度ファイルを添付する方が確実 |
| 頻繁に更新されるデータ(在庫・最新価格) | 向かない | ナレッジは静的ファイルの再アップロードが必要。Actions(API連携)やWeb検索機能の方が適する |
| 機密性の高い契約書・個人情報を含む資料 | 慎重に | 後述の漏えいリスクがあるため、そのまま載せるかどうかは要検討 |

判断基準はシンプルで、「質問に応じて資料の一部を検索して引用してほしい」ならナレッジ、「会話全体を通じて資料の全文を踏まえてほしい」ならその都度ファイル添付、「常に最新の値を取得してほしい」ならActionsやWeb検索機能を使う。

## 実務での使い方

### アップロード手順(2026年7月時点の目安)

1. ChatGPT(Web版)にログインし、左サイドバーの「GPTを探す」→ 右上「＋作成する」でGPT Builderを開く(既存GPTの場合は編集画面を開く)
2. 「Configure」タブを選択
3. 「ナレッジ」欄の「ファイルをアップロードする」をクリックし、PDF・Word・Excel・CSV・テキストなどのファイルを選択する
4. 保存すると、以降の会話でGPTが自動的にナレッジを検索して回答に利用する

### アップロード上限(2026年7月時点)

| 項目 | 上限 |
|---|---|
| GPT1体あたりのファイル数 | 20ファイルまで |
| ファイル1つのサイズ | 512MBまで(ハード上限) |
| テキスト・文書ファイルのトークン数 | 1ファイルあたり200万トークンまで |
| CSV・スプレッドシート | 行数によるが目安として約50MBまで |
| 画像ファイル | 1枚あたり20MBまで |
| アップロード頻度 | 3時間あたり80ファイルまで(Freeプランは1日3ファイルまで) |
| 個人・組織の保存容量 | 個人25GB、組織100GBが上限 |

数字自体は個々のGPTでは意識しなくてよいことが多いが、「20ファイルの壁」「512MBの壁」に当たった場合は、複数の小さな資料に分割するか、内容を要約・整理してから再アップロードするとよい。

### コピペで使えるInstructions文例(ナレッジ優先・出典明記)

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

### ツール横断の対応付け

| 概念 | ChatGPT(GPTs) | Gemini(Gems) | Claude(Projects) | Microsoft 365 Copilot |
|---|---|---|---|---|
| 呼び方 | ナレッジ(Knowledge) | 知識(Knowledge)ファイル | プロジェクトの知識(Project knowledge) | 知識ソース(Knowledge sources) |
| 設定場所 | GPT Builderの「Configure」タブ→「ナレッジ」 | Gem作成画面の「ナレッジ」欄 | プロジェクト画面の「プロジェクトの知識」 | エージェントビルダーの「知識」セクション |
| 主な上限(目安) | 20ファイル/1ファイル512MB、テキストは200万トークン/ファイル | 1Gemあたり10ファイル、1ファイル100MBまで | ファイル数は実質無制限だが1ファイル30MBまで(容量が context window を超えると自動でRAGモードに切替) | SharePointファイル最大100件+OneDriveファイル最大50件+端末からのアップロード |
| クラウド連携 | なし(都度アップロードのみ) | Googleドライブと連携可(最新版を自動反映) | なし(都度アップロードのみ) | SharePoint/OneDriveと連携し既存の権限・機密ラベルを継承 |

社内のファイルサーバーやSharePointをそのまま参照させたい場合はCopilotの知識ソースが有利、逆に「手元のPDFを数点読ませたい」程度の軽い用途ならGPTsやGemsで十分、という使い分けになる。

## 注意点・よくある誤解

- **アップロードしただけでは万能ではない**: OpenAIのコミュニティフォーラムには「最初の1メッセージだけナレッジを参照しない」「明示的に『検索して』と言わないと無視される」という報告が多数ある。Instructionsに「必ず検索してから回答する」と明記するのが実務上の回避策になる。
- **表・図・スキャンPDFは読み取り精度が落ちやすい**: 複雑な表や画像化されたPDF(スキャン文書)は、レイアウトが崩れて誤読されることがある。可能であれば「項目名: 値」のようなQ&A形式・箇条書きに整形し直してからアップロードすると検索精度が上がる。目次・免責事項・装飾的なヘッダー/フッターなど本文以外の要素は、検索ノイズになるため事前に削っておくとよい。
- **大量のファイルを詰め込むと後半が参照されにくくなる**: 合計トークン数が一定量を超えると、超過分のファイルが検索対象から外れる傾向が研究で報告されている。1体のGPTに何十ものPDFを詰め込むより、テーマごとにGPTを分けるか、内容を要約して情報密度を上げる方が安全である。
- **ナレッジファイルは「機密扱いにできない」前提で運用する**: ACL 2025で発表された学術研究では、Code Interpreter(コードインタープリター)を有効にしたGPTから、悪意あるプロンプトによって元のナレッジファイルがそのままダウンロードされてしまう事例が高い成功率で確認されている。個人情報・契約書・未公開の財務情報などを含むファイルは、そもそもナレッジに載せない、またはCapabilitiesでコードインタープリターをオフにするなどの対策を検討する。
- **更新は再アップロードが必要**: ナレッジファイルは静的なスナップショットであり、元ファイルを更新してもGPT側には自動反映されない(Gemini GemsのGoogleドライブ連携は例外的に最新版を自動反映する)。定期的に更新する資料は、更新のたびに差し替える運用ルールを決めておく。

## 最初の一歩

自社のFAQやマニュアルの中から、社員によく聞かれる1つのトピック(例: 経費精算のルール)を選び、その部分だけをQ&A形式に整形したテキストファイルを作って、既存または新規のGPTのナレッジに追加してみる。

## 関連トピック

- [GPTsの作り方と公開設定](./gpts-creation-basics.md)
- [AIが扱いやすいデータ形式](../part06-data-analysis/ai-friendly-data-formats.md)

## 更新履歴

### 2026-07-05: 初版執筆
- **内容**: GPTsのナレッジファイル機能について、RAGによる検索の仕組み、アップロード上限、Instructions文例、他ツール(Gemini Gems・Claude Projects・Microsoft 365 Copilot)との対応、精度・セキュリティ面の注意点を整理
- **出典**: [OpenAI Help Center: File Uploads FAQ](https://help.openai.com/en/articles/8555545-file-uploads-faq), [OpenAI Help Center: Creating and editing GPTs (Knowledge in GPTs)](https://help.openai.com/en/articles/8843948-knowledge-in-gpts), [OpenAI Help Center: Retrieval augmented generation (RAG) and semantic search for GPTs](https://help.openai.com/en/articles/8868588-retrieval-augmented-generation-rag-and-semantic-search-for-gpts), [OpenAI Help Center: Optimizing File Uploads in ChatGPT Enterprise](https://help.openai.com/en/articles/10029836-optimizing-file-uploads-in-chatgpt-enterprise), [When GPT Spills the Tea: Comprehensive Assessment of Knowledge File Leakage in GPTs (arXiv, ACL 2025)](https://arxiv.org/abs/2506.00197), [OpenAI Developer Community: GPT ignoring attached knowledge document, making up stuff](https://community.openai.com/t/gpt-ignoring-attached-knowledge-document-making-up-stuff/865764), [OpenAI Developer Community: Custom GPT is not referencing knowledge source files on the first prompt](https://community.openai.com/t/custom-gpt-is-not-referencing-knowledge-source-files-on-the-first-prompt/631128), [Google Workspace Blog: New features in Gemini to deepen usage for organizations](https://workspace.google.com/blog/product-announcements/new-gemini-gems-deeper-knowledge-and-business-context), [Google Gemini Apps Help: Use Gems in Gemini Apps](https://support.google.com/gemini/answer/15146780?hl=en), [Claude Help Center: Upload files to Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude), [Microsoft Learn: Add knowledge sources to your declarative agent in Microsoft 365 Copilot](https://learn.microsoft.com/en-us/microsoft-365/copilot/extensibility/agent-builder-add-knowledge)
