---
title: Google Geminiの基本
part: 7
chapter: 第1章 Google Gemini
tags: [Gemini, Google, Gem, NotebookLM]
created: 2026-07-04
updated: 2026-07-04
---

# Google Geminiの基本

## これは何か

Google Geminiは、ChatGPTと並ぶ代表的な生成AIだが、モデルの世代(Flash/Pro等)や周辺機能(Gem、NotebookLM)の呼び方がGoogle独自で分かりにくい。ChatGPTを使い慣れた人がGeminiに触れると、「Gemって何?」「NotebookLMとどう違うの?」と戸惑いやすい。ここではGeminiのラインナップと周辺機能の関係を整理する。

## 仕組み・背景

2026年7月時点でのGeminiのモデルラインナップは、性能・速度のバランスで複数段階に分かれている。

- **Flash-Lite**: 低遅延・高頻度処理向けの最軽量モデル
- **Flash**: 汎用のワークホースモデル。コストと品質のバランス型で、無料版の既定モデルにもなっている
- **Pro**: 複雑なタスク・専門用途向けの高性能モデル。上位モードとして、並列推論を行う「Deep Think」(ブーストモード)も用意されている

画像生成については「Nano Banana」シリーズという名称で展開されており、Nano Banana 2 Lite(軽量)、Nano Banana 2(汎用)、Nano Banana Pro(高精度)という位置づけになっている。

モデルの世代交代は非常に速く、2026年に入ってからも数か月単位でアップデートが続いている。記事や社内資料に具体的なモデル名を書く場合は、必ず[Google公式のGeminiモデル一覧](https://gemini.google/)で最新の世代を確認することを推奨する。

## 使いどころ・使い分け

| 用途 | 向いているモデル・機能 |
|---|---|
| 簡単な質問・チャット | Flash(無料版の既定モデル) |
| 複雑な分析・専門的なタスク | Pro |
| 大量・高頻度の軽い処理 | Flash-Lite |
| 手元の資料だけを根拠に正確に調べたい | NotebookLM |
| 幅広い一般知識も使って発想を広げたい | Geminiアプリ本体 |

GeminiアプリとNotebookLMの使い分けが特によく混同される。**Geminiアプリは「外の世界の知識」も使う汎用AI**であるのに対し、**NotebookLMは「ユーザーが渡した資料だけ」を根拠に回答するリサーチ特化AI**という違いがある。手元の資料から正確に情報を引き出したいならNotebookLM、既存資料を踏まえつつ新しいアイデアを広げたいならGeminiアプリ、という選び方になる。

## 実務での使い方

### 個人向けプラン(2026年7月時点の目安)

| プラン | 目安 | 特徴 |
|---|---|---|
| 無料 | ¥0 | Flashが既定モデル。Deep Research月数回まで、画像生成は1日あたり上限あり |
| Google AI Plus | 月額千円未満〜(ストレージ量で複数段階) | 無料版より上位モデルの利用枠が拡大 |
| Google AI Pro | 月額数千円程度 | Deep Research・Gemini Live・Gem機能など高度機能が解放。NotebookLMの利用上限が無料版の5倍 |
| Google AI Ultra | 月額1万円台〜 | 最上位機能へのアクセス拡大 |

料金は2026年5月のGoogle I/Oで改定されたばかりで、その後も変更される可能性が高い。契約前に必ず[Google公式のプランページ](https://one.google.com/about/google-ai-plans/)で最新の金額を確認すること。

### Gem機能(ChatGPTのGPTsに相当)

Gemは「どんなトピックにも対応できる自分専用のカスタムAI」で、毎回の会話で前提説明を繰り返す手間を省ける。

作成手順の目安:
1. gemini.google.com を開き、左側メニューの「Gemを表示」をクリック
2. 「Gemを作成」を選択し、名前を付ける
3. 指示欄に、ペルソナ(役割・口調)・タスク(してほしいこと)・コンテキスト(背景情報)・出力形式を書く(「Geminiを使用」ボタンで簡単な目的文を詳しい指示文に自動リライトさせることも可能)
4. 右側のプレビューで確認しながら「保存」

作成したGemはGeminiモバイルアプリやGoogle Workspaceのサイドパネルからも呼び出せる。

### 法人向け(Google Workspace with Gemini)

個人向けプランとは別に、法人向けは「Google Workspace with Gemini」という名称で提供されている。GmailやGoogleドキュメント、スプレッドシート、Meetなど業務ツール群にGeminiが統合されており、Business Starterプランからも標準で利用できる(上位プランほど利用できる範囲が広がる)。

## 注意点・よくある誤解

- **モデル名・料金の変更頻度が非常に高い**: 2026年に入ってからプラン体系・価格が複数回改定されている。本ページの数値は目安であり、契約前に必ず公式サイトで確認すること。
- **無料版でGemが使えるかどうかは要確認**: 情報源によって「Pro以上の機能」とする説明と「無料版でも使えるが上限が低いだけ」とする説明が混在している。実際の挙動は公式ヘルプで確認するのが確実。
- **NotebookLMとGeminiアプリは統合が進んでいる**: 2026年にGeminiアプリ内に「ノートブック」機能が追加され、NotebookLMと相互に同期する仕組みが導入された。今後さらに機能の境界が変わる可能性がある。

## 最初の一歩

手元にある社内マニュアルやプロジェクト資料を1つNotebookLMに読み込ませ、内容についての質問を投げて、根拠付きで答えが返ってくる感覚を試してみる。

## 関連トピック

- [ChatGPTのプラン比較](../part02-chatgpt-basics/chatgpt-plan-comparison.md)

## 更新履歴

### 2026-07-04: 初版執筆
- **内容**: Geminiのモデルラインナップ(Flash-Lite/Flash/Pro)、個人向け・法人向けプランの概要、Gem機能の作成手順、NotebookLMとの使い分けを整理
- **出典**: [Google Blog: Gemini Omni Flash / Nano Banana 2発表](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-omni-flash-nano-banana-2-lite/)、[Google公式ヘルプ: カスタムGem作成のヒント](https://support.google.com/gemini/answer/15235603?hl=ja)、[マネーフォワード クラウド: Google Workspace with Gemini解説](https://biz.moneyforward.com/ai/basic/863/)、[アイスマイリー: GeminiとNotebookLMの違い](https://aismiley.co.jp/ai_news/gemini-notebooklm/)
- **注記**: Google公式サイトへの直接アクセスができなかったため、料金・モデル名の一部は複数の第三者情報の突き合わせに基づく目安。正確な最新値は公式サイトで要確認
