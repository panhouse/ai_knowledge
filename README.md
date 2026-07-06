# ai_knowledge

毎朝のルーティン(Claude CodeのRoutine機能)で、生成AIの基本知識を体系立てて
書き溜めていくナレッジベースです。ニュースを集めるのではなく、知識体系(Part 1〜11)の
トピックを1つずつ「教科書」として書き上げ、常に最新に保ちます。

## 読み方

- **今朝の更新を知りたい** → [UPDATES.md](UPDATES.md) を見る(新しい日付が上)
- **テーマごとに深掘りしたい** → 下の目次から各パートの `_index.md` へ
- **運用ルールを確認・変更したい** → [CLAUDE.md](CLAUDE.md)

## 知識体系(目次)

| Part | テーマ | 主な内容 |
|------|--------|----------|
| [Part 1](topics/part01-ai-llm-basics/_index.md) | AI・LLM基礎 | 全体像と歴史、LLMの仕組み、モデルの種類と選び方、特性と限界、周辺概念 |
| [Part 2](topics/part02-chatgpt-basics/_index.md) | ChatGPT基礎 | プランとモデルの選び方、初期設定とデータ保護、記憶・文脈の管理、主要機能 |
| [Part 3](topics/part03-risk-security/_index.md) | リスク管理・セキュリティ | 情報漏洩・データ管理、攻撃と防御、ハルシネーション対策、法務・ガバナンス |
| [Part 4](topics/part04-prompt-engineering/_index.md) | プロンプトエンジニアリング | 基本原則、例示と誘導、思考を引き出す手法、エージェント的手法、評価と改善 |
| [Part 5](topics/part05-gpts-customization/_index.md) | GPTs・カスタマイズ | GPTsの基礎、高度な活用、他ツールのカスタムボット |
| [Part 6](topics/part06-data-analysis/_index.md) | データ活用・分析 | データ形式、ChatGPTによる分析、RAGの基礎、精度改善と基盤 |
| [Part 7](topics/part07-other-llm-tools/_index.md) | 他の主要LLM・AIツール | Gemini系、対抗LLM、ローカル・オープンモデル、検索特化型AI、コーディング支援、画像・動画・音声生成、選び方 |
| [Part 8](topics/part08-api-development/_index.md) | API・開発連携 | OpenAI API、API活用実践、業務ツール連携、MCP・エージェント連携 |
| [Part 9](topics/part09-nocode-lowcode/_index.md) | ノーコード・ローコード開発 | Dify基礎、Difyワークフロー、自動化・連携ツール、AIエージェント構築 |
| [Part 10](topics/part10-business-practice/_index.md) | 業務活用・実践 | 導入の設計、文章・コミュニケーション、資料作成、リサーチ、職種別ユースケース |
| [Part 11](topics/part11-ai-trends/_index.md) | AI動向・将来展望 | 技術トレンド、主要プレイヤーの動向、AGIと働き方、日本における動向 |
| [Part 12](topics/part12-uncategorized/_index.md) | 業種別 生成AI活用事例 | 製造・小売・金融・医療など業種ごとの活用事例(+未分類の受け皿) |

## 仕組み

1. 毎朝ルーティンが知識体系(Part 1〜11)の未執筆トピックから10件を選定
2. Web検索(日英)で裏取り・最新情報を確認しながら、教材品質のガイドページを執筆
3. 業種別の活用事例は Part 12 に整理(体系に収まらないテーマは Part 12 末尾の「その他・未分類」へ一旦集約)
4. 執筆・改訂内容を [UPDATES.md](UPDATES.md) に記録して main に直接コミット

詳細な運用ルールは [CLAUDE.md](CLAUDE.md) を参照。
