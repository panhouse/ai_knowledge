---
title: AIクローラーとコンテンツ権利
part: 3
chapter: 著作権・法的リスク
tags: [Cloudflare, クローラー, 著作権, パブリッシャー, スクレイピング]
created: 2026-07-04
updated: 2026-07-04
---

# AIクローラーとコンテンツ権利

## 概要

AI企業によるWebコンテンツのクロール(モデル学習・AI回答生成・エージェント利用)と、
コンテンツ提供者(パブリッシャー)の権利・広告収益の対立が、生成AIをめぐる主要な
法務・ビジネス論点になっている。

転機となったのがCloudflareの方針転換で、2026年9月15日から、検索・AI回答・学習を
混合する「用途混合クローラー」を広告掲載ページからデフォルトで遮断する。AI企業は
クローラーの用途分離(学習用・検索用・エージェント用)の申告を迫られ、コンテンツ側は
「ブロックするか、対価を取るか」を選べる構造(Pay Per Use)へ移行しつつある。

## 更新履歴

### 2026-07-04: Cloudflareが用途混合AIクローラーを9月15日からデフォルトブロックへ
- **内容**: Cloudflareが7月1日、検索・AI回答・モデル学習を混合するクローラーを広告掲載ページからデフォルトで遮断する方針を発表(2026年9月15日開始)。合わせてPay Per Crawlを「Pay Per Use」モデルに拡張し、コンテンツがAIの回答に使われた時点で対価が発生する仕組みを導入する
- **なぜ重要か**: AI企業はクローラーの用途分離を、サイト運営者はブロック/課金の方針決定を迫られる。外部サイトのスクレイピングに依存するRAGパイプラインやAIエージェントは、9月までに取得手段の見直しが必要になる可能性がある
- **出典**: [TechCrunch](https://techcrunch.com/2026/07/01/cloudflares-new-policy-pushes-ai-companies-to-pay-for-publishers-content/), [The AI Insider](https://theaiinsider.tech/2026/07/02/cloudflare-sets-september-deadline-to-force-ai-crawlers-apart-from-search-bots/)
