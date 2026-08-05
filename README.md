# ai_knowledge

毎朝のルーティン(Claude CodeのRoutine機能)で、生成AIの基本知識を体系立てて
書き溜めていくナレッジベースです。ニュースを集めるのではなく、知識体系
(Part 1〜12は教科書、Part 13〜15はカタログ)のトピックを1つずつ書き上げ、常に最新に保ちます。

## 読み方

- **今朝の更新を知りたい** → [UPDATES.md](UPDATES.md) を見る(新しい日付が上)
- **テーマごとに深掘りしたい** → 下の目次から各パートの `_index.md` へ
- **運用ルールを確認・変更したい** → [CLAUDE.md](CLAUDE.md)

## 知識体系(目次)

| Part | テーマ | 主な内容 |
|------|--------|----------|
| [Part 1](topics/part01-ai-basics/_index.md) | AI基礎 | 人工知能とは、AIの歴史、機械学習・ディープラーニングの基礎、認識系AIの応用、評価の基礎 |
| [Part 2](topics/part02-llm-basics/_index.md) | LLM基礎 | LLMの仕組み、モデルの種類と選び方、特性と限界、周辺概念 |
| [Part 3](topics/part03-ai-chat-tools/_index.md) | AIチャットツールの基本 | プラン・モデルの選び方、設定とデータ保護、記憶・文脈の管理、主要機能、主要ツール各論 |
| [Part 4](topics/part04-risk-security/_index.md) | リスク管理・セキュリティ | 情報漏洩・データ管理、攻撃と防御、ハルシネーション対策、法務・ガバナンス |
| [Part 5](topics/part05-prompt-engineering/_index.md) | プロンプトエンジニアリング | 基本原則、例示と誘導、思考を引き出す手法、エージェント的手法、評価と改善 |
| [Part 6](topics/part06-custom-ai/_index.md) | カスタムAIの作成 | 設計の基礎、GPTs / Gem / Copilot Agent / Claude Projects、高度な活用と防御 |
| [Part 7](topics/part07-data-analysis/_index.md) | データ活用・分析 | データ形式、チャットAIによる分析、RAGの基礎、精度改善と基盤、画像・PDFの読み取り活用(Vision入力) |
| [Part 8](topics/part08-specialized-ai-tools/_index.md) | 特化型AIツール | 検索・リサーチ、コーディング支援、画像・動画・音声生成、ローカル・オープンモデル(OSSライセンス比較含む)、選び方、会議・議事録AI |
| [Part 9](topics/part09-api-development/_index.md) | API・開発連携 | LLM API基礎、API活用実践(リアルタイム音声API含む)、業務ツール連携、MCP・エージェント連携 |
| [Part 10](topics/part10-nocode-lowcode/_index.md) | ノーコード・ローコード開発 | Dify基礎、Difyワークフロー、自動化・連携ツール、AIエージェント構築 |
| [Part 11](topics/part11-business-practice/_index.md) | 業務活用・実践 | 導入の設計(コスト管理・予算配分含む)、文章・コミュニケーション、資料作成、リサーチ |
| [Part 12](topics/part12-ai-trends/_index.md) | AI動向・将来展望 | 技術トレンド、主要プレイヤーの動向、AGIと働き方、日本における動向 |
| [Part 13](topics/part13-industry-cases/_index.md) | 業種別 生成AI活用事例 | 製造・小売・金融・医療など業種ごとの活用事例(+未分類の受け皿) |
| [Part 14](topics/part14-job-role-cases/_index.md) | 職種別 生成AI活用事例 | 営業、マーケ・広報、CS、企画・PdM・データ分析、人事・L&D、経理・監査、法務、総務・秘書・購買、情シス・セキュリティ、R&D・QA、生産管理、クリエイティブ・翻訳 |
| [Part 15](topics/part15-japan-ai-companies/_index.md) | 国内AI企業マップ | コンサル・SIer系、基盤モデル系、業務ドメイン特化ツール系、ノーコード・エージェント基盤系、研修・人材育成系(+未分類の受け皿) |

## 仕組み

1. 毎朝9時(JST)にルーティンが知識体系の未執筆トピックから最大10件を選定
2. Web検索(日英)で裏取り・最新情報を確認しながら、教材品質のガイドページを執筆
3. 業種別の活用事例は Part 13、職種別の活用事例は Part 14、国内AI企業の一覧は Part 15 に整理
   (体系に収まらないテーマはそれぞれ末尾の「その他・未分類」へ一旦集約)
4. 1トピック = 1ブランチ = 1PR で main 向けにPRを作成し、執筆・改訂内容を [UPDATES.md](UPDATES.md) に記録(mainへ直接コミットはせず、採否はPR画面で判断)

詳細な運用ルールは [CLAUDE.md](CLAUDE.md) を参照。
