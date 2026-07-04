---
title: Claude(Anthropic)
part: 7
chapter: その他のLLM
tags: [Anthropic, Claude, LLM, エージェント]
created: 2026-07-04
updated: 2026-07-04
---

# Claude(Anthropic)

## 概要

Anthropicが提供するLLMファミリー。2026年6月30日に発表された Claude Sonnet 5 は、
多段のエージェントタスクで Sonnet 4.6 を大きく上回り、多くの実務タスクで上位モデル
Opus 4.8 に迫る性能とされる。7月1日から Free / Pro プランのデフォルトモデルになった。

API価格は導入価格で入力$2/出力$10(100万トークンあたり、2026年8月31日まで)、
以降は入力$3/出力$15。「準フロンティア級の性能を低価格で」という位置づけで、
エージェント用途のコスト構造を変えつつある。

## 更新履歴

### 2026-07-04: Claude Sonnet 5がFree/Proプランのデフォルトモデルに
- **内容**: Anthropicが6月30日にClaude Sonnet 5を発表し、7月1日からFree/Proプランのデフォルトモデルにした。エージェントタスクの性能向上が主眼で、多くのタスクでOpus 4.8に迫る。API導入価格は入力$2/出力$10(8月31日まで、以降$3/$15)
- **なぜ重要か**: 準フロンティア級モデルが無料プランでも使える水準になり、エージェント運用のコスト試算前提が下がる。API利用時はモデル指定を `claude-sonnet-5` へ更新が必要
- **出典**: [Anthropic](https://www.anthropic.com/news/claude-sonnet-5), [MacRumors](https://www.macrumors.com/2026/06/30/anthropic-claude-sonnet-5/)
