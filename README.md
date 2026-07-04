# ai_knowledge

毎朝のルーティン(Claude Codeのるーちん機能)で生成AIに関する知識をWeb検索で収集し、
体系化されたトピックページに蓄積していくナレッジベースです。

## 読み方

- **今朝の更新を知りたい** → [UPDATES.md](UPDATES.md) を見る(新しい日付が上)
- **テーマごとに深掘りしたい** → 下の目次から各パートの `_index.md` へ
- **運用ルールを確認・変更したい** → [CLAUDE.md](CLAUDE.md)

## 知識体系(目次)

| Part | テーマ | 主な内容 |
|------|--------|----------|
| [Part 1](topics/part01-ai-llm-basics/_index.md) | AI・LLM基礎 | AIの全体像と歴史、LLMの基礎、LLMの特性と注意点 |
| [Part 2](topics/part02-chatgpt-basics/_index.md) | ChatGPT基礎 | 概要・プラン比較、基本操作、主要機能 |
| [Part 3](topics/part03-risk-security/_index.md) | リスク管理・セキュリティ | 情報漏洩対策、ハルシネーション対策、著作権・法的リスク |
| [Part 4](topics/part04-prompt-engineering/_index.md) | プロンプトエンジニアリング | 基本原則、入門〜応用手法、ベストプラクティス |
| [Part 5](topics/part05-gpts-customization/_index.md) | GPTs・カスタマイズ | GPTsの基礎、高度な活用 |
| [Part 6](topics/part06-data-analysis/_index.md) | データ活用・分析 | データ形式、ChatGPTによる分析、RAG |
| [Part 7](topics/part07-other-llm-tools/_index.md) | 他の主要LLM・AIツール | Gemini、Claude、Copilot、検索特化型AIなど |
| [Part 8](topics/part08-api-development/_index.md) | API・開発連携 | OpenAI API、Function Calling、GAS連携、MCP |
| [Part 9](topics/part09-nocode-lowcode/_index.md) | ノーコード・ローコード開発 | Dify、n8n、Make、AIエージェント |
| [Part 10](topics/part10-business-practice/_index.md) | 業務活用・実践 | 業務切り分け、文章作成、資料作成、リサーチ |
| [Part 11](topics/part11-ai-trends/_index.md) | AI動向・将来展望 | AI市場の動向、AGI、AI時代の働き方 |
| [Part 12](topics/part12-uncategorized/_index.md) | 未分類 | 上記の体系に収まらない情報を一旦集約する場所 |

## 仕組み

1. 毎朝ルーティンがWeb検索で生成AI関連の新情報を収集
2. 上記の知識体系(Part 1〜11)に分類し、トピックページを新規作成または追記
3. 体系に外れる情報は Part 12 に一旦集約
4. 更新内容を [UPDATES.md](UPDATES.md) に記録して main に直接コミット

詳細な運用ルールは [CLAUDE.md](CLAUDE.md) を参照。
