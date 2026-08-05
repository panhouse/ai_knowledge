---
title: "量子化(モデル軽量化)の基本"
part: 8
chapter: 第4章 ローカル・オープンモデル
tags: [量子化, GGUF, Ollama, ローカルLLM, オープンウェイト, AWQ, MXFP4]
created: 2026-07-07
updated: 2026-08-02
---

# 量子化(モデル軽量化)の基本

## これは何か

「量子化(Quantization)」とは、AIモデルの重み(パラメータの数値)を表現する精度を落とすことで、モデルのファイルサイズと必要メモリを大幅に圧縮する技術である。[ローカルLLMの基本](local-llm-basics.md)で触れた「7Bモデルなら8GB前後で動く」という目安は、実際には量子化された(軽量化された)モデルを前提にした数字であり、量子化を知らないと「なぜ同じ7Bモデルなのにファイルサイズが2倍・4倍も違うバージョンが複数あるのか」が分からず、Hugging FaceやOllamaでのモデル選びで迷うことになる。本ページでは、量子化の仕組み・主要な方式・実務での選び方を整理する。

## 仕組み・背景

### 「精度を落として容量を圧縮する」とは具体的に何か

学習済みのAIモデルの重みは、通常16ビット(FP16/BF16)という精度の数値で保存されている。量子化は、この数値をより少ないビット数(8ビット・4ビット・場合によっては3ビット以下)で近似的に表現し直す処理である。ビット数が半分になれば、単純計算でファイルサイズ・必要メモリもおよそ半分になる。目安として、7Bモデル(70億パラメータ)はFP16では約14GBだが、8ビット(INT8)では約7GB、4ビット(INT4相当)では約4〜4.5GBまで圧縮される。

精度を落とす以上、モデルの出力品質はわずかに劣化する。ただし劣化の度合いは一様ではなく、どのビット数・どの方式を選ぶかによって「ほぼ無劣化」から「明らかに品質が落ちる」まで大きな差が出る。

### 主要な量子化方式

| 方式 | 特徴 | 向いている環境 |
|---|---|---|
| **GGUF** | [llama.cpp](https://github.com/ggml-org/llama.cpp)プロジェクトが確立した形式。CPU・GPU・Apple Silicon(Mac)を問わず動く汎用性が最大の強み。OllamaやLM Studioが標準採用 | 個人PC・社内PCでのローカル運用全般 |
| **AWQ** | 「重みの重要度は均等ではない」という発想で、影響の大きい一部の重み(チャネル)を活性化パターンから特定して保護してから量子化する。2026年時点でGPU向け4ビット量子化の事実上のデフォルトになっており、vLLM・TGIなど主要な推論エンジンとの相性もよい | GPU中心のサーバー運用、精度重視 |
| **GPTQ** | 重みを1列ずつ調整しながら誤差(二乗誤差)を最小化する量子化手法。先行して普及したが、誤差が後の列に蓄積しやすく、コード生成など多段階の推論タスクでAWQより劣化しやすい傾向が確認されており、新しいモデルではAWQに置き換わりつつある | GPU中心のサーバー運用(旧世代モデル・過去資産の流用) |
| **EXL2 / EXL3** | ExLlamaV2/V3プロジェクトの独自形式。2〜8ビットの間で0.1刻みの微妙なビット幅を指定でき、限られたVRAMに収まる最大品質を追い込みやすい。EXL3はQTIP系のトレリス符号化を採用し同ビット幅でのAWQ・GPTQに匹敵する品質を狙う | GPU中心・VRAM上限がシビアな個人運用 |
| **MXFP4 / NVFP4(ネイティブFP4)** | 4ビット浮動小数点をブロック単位で共有指数を持たせて表現する規格(OCP・Microscaling Formats)。AMD・NVIDIA・Microsoft・Meta・OpenAIなど業界横断で標準化されており、後から量子化するのではなく学習時点からこの形式で重みを持つ「ネイティブ量子化」モデルが増えている(代表例: OpenAIのgpt-oss) | 対応GPU(Blackwell世代等)、対応モデルをそのまま使う場合 |
| **bitsandbytes(NF4等)** | Hugging Face Transformersと連携したその場限りの量子化。ファインチューニング(QLoRA等)との組み合わせでよく使われる | 開発者による研究・追加学習 |

ローカルLLMを画面操作で試すビジネスパーソンが実際に目にするのはほぼ「GGUF」であり、Ollama・LM StudioのモデルカードにあるQ4・Q8といった表記もGGUFの量子化レベルを指す。GPU運用を前提とした社内システムを検討する場合は、AWQ版が用意されていればまずそちらを優先し、GPTQ版しかない場合のみそれを使う、という判断で困らない。

### GGUFの量子化レベル表記の読み方

GGUF形式のファイル名には`Q4_K_M`のような表記が付く。数字がビット数、末尾のアルファベットが精度配分の方式を示す。

| 表記 | ビット数の目安 | 品質・容量のバランス |
|---|---|---|
| Q8_0 | 8ビット | FP16とほぼ同等の品質(劣化0.1〜0.5%程度)。容量はFP16の約半分 |
| Q6_K | 6ビット | ほぼ無劣化に近い品質を保ちつつ、さらに圧縮 |
| Q5_K_M | 5ビット | 品質とサイズのバランスが良く、Q4より高品質 |
| **Q4_K_M** | 4ビット | 「スイートスポット」と呼ばれる標準的な選択。7Bモデルで容量はFP16比70%減、品質劣化は1〜3%程度に収まることが多い |
| Q3_K以下 | 3ビット以下 | 容量は大きく減るが、品質劣化が目に見えて分かるレベルになりやすい |

`K`は「重要な層(埋め込み層・出力層等)は高ビット、それ以外の層は低ビット」という混合精度を使うことを意味し、`_M`(Medium)・`_S`(Small)・`_L`(Large)は同じビット数の中でのバランス違いを表す。単純な`Q4_0`のような旧世代の表記より、`Q4_K_M`のような「Kクオンツ」表記の方が同じビット数でも品質が高い傾向にある。

### IQ量子化(importance matrix、imatrix)という選択肢

Q4_K_M等の「Kクオンツ」より新しい世代として、`IQ4_XS`・`IQ3_XXS`・`IQ2_S`のような「IQ」で始まる表記のファイルも配布されている。これは「imatrix(importance matrix、重要度行列)」と呼ばれる、実際の文章データを流して各重みの影響度を事前に測定した情報をもとに、影響の大きい重みを優先的に高精度で保持する方式である。効果が大きいのは4ビット以下(特に3ビット以下)の強い圧縮域で、同じサイズならKクオンツよりIQ量子化の方が品質が高いことが多い。逆に6ビット以上ではKクオンツとの差はほぼ気にしなくてよい。Hugging Faceでは`bartowski`等の配布者がQ系とIQ系の両方を並行して公開していることが多く、「容量を切り詰めたいが品質もできるだけ残したい」場合はIQ表記のファイルを優先して探すとよい。

### PTQ(学習後量子化)とQAT(量子化を意識した学習)

量子化には、いつ適用するかで2つのアプローチがある。

- **PTQ(Post-Training Quantization、学習後量子化)**: 学習が終わったモデルに、追加学習なしで量子化を適用する方式。手軽で計算コストが低く、GGUF・GPTQ・AWQなどローカルLLMで配布されているモデルのほとんどはこの方式。ただし4ビット以下など強い圧縮では品質劣化が目立ちやすい
- **QAT(Quantization-Aware Training、量子化対応学習)**: 学習の過程であらかじめ量子化による誤差を模擬し、モデル自身がその誤差を補正できるように訓練する方式。追加の学習コストがかかる分、同じビット数でもPTQより高品質になりやすい。モデル提供元(Google・Metaなど)が公式に「QAT版」を配布している場合、通常版より優先して選ぶ価値がある
- **ネイティブ量子化(学習時点から低ビットで持つ)**: PTQ・QATが「フルサイズで学習してから圧縮する」のに対し、OpenAIのgpt-oss(120b/20b)のように、MoE(専門家混合)層の重みを最初からMXFP4形式(4.25ビット相当)で保持するモデルも登場している。この場合「量子化版・非量子化版」という区別自体がなく、配布されているファイルがそのまま最適な状態なので、追加の量子化やビット数選びに悩む必要がない

## 使いどころ・使い分け

量子化のレベル選びは「品質」と「動かせるかどうか(メモリ・速度)」のトレードオフである。

| 状況 | 推奨レベルの目安 |
|---|---|
| まず動かして試したい・PCスペックに余裕がない | Q4_K_M(標準的な選択。多くのツールの既定値) |
| 品質を優先したいが容量も抑えたい | Q5_K_M・Q6_K |
| 精度が重要な業務(要約の正確性を細かく検証する等)でVRAMに余裕がある | Q8_0(実質ロスレスに近い) |
| メモリが極端に少ない環境(古いPC・小型端末) | Q3_K以下、またはIQ3系(imatrix)で品質劣化を抑えつつ圧縮 |
| 数式・コード生成・複雑な推論タスク | 4ビット以下は品質劣化が特に目立ちやすいため、可能な限りQ6_K以上を検討 |
| モデルが最初からMXFP4等のネイティブ低ビット形式で配布されている(gpt-oss等) | 追加の量子化は不要。配布されているファイルをそのまま使う |

判断に迷う場合の考え方は次のとおり。

- **「動かない」より「多少品質が落ちる」方がまし**なので、まずはQ4_K_Mで試し、実用に足りるか確認する
- 要約・下書き・社内文書検索など「多少の粗さが許容される」用途はQ4系で十分なことが多い
- 契約書レビューや専門知識を要する用途など「間違いが困る」用途は、可能な限りQ6_K以上、あるいは量子化前提を諦めてクラウドAPIを検討する

## 実務での使い方

### Ollamaでの選び方

Ollamaでモデル名だけを指定すると(例: `ollama run llama3.2`)既定の量子化レベル(多くはQ4_K_M相当)が自動で選ばれる。別のレベルを試したい場合は、モデル名の後ろにタグを付けて指定する(コピペ可)。

```bash
# 標準(バランス重視、まずはこれで試す)
ollama run llama3.2:8b-instruct-q4_K_M

# 品質重視(VRAM・メモリに余裕がある場合)
ollama run llama3.2:8b-instruct-q8_0
```

`ollama list`で現在ダウンロード済みのモデルとサイズを確認できるため、複数の量子化レベルを試して容量・応答速度・品質の感触を比較するとよい。

### Hugging Face・LM Studioでの選び方

Hugging Faceでモデルを検索すると、`bartowski`や`unsloth`といった量子化配布者が公開している「モデル名-GGUF」というリポジトリが見つかることが多い。ファイル一覧に`model-Q4_K_M.gguf`のように量子化レベル別のファイルが並んでおり、必要なレベルのファイルだけをダウンロードすればよい。LM Studioの「Discover」タブでも、同じモデルの複数の量子化バージョンが一覧表示され、それぞれの推定メモリ使用量が表示されるため、自分のPCで動くレベルを選びやすい。

### 量子化版と非量子化版の見分け方(コピペで使える確認ポイント)

モデルを選ぶ際、次の点を確認すると失敗が減る。

1. モデルカードに「Quantized by」「GGUF」「量子化」といった記載があるか
2. ファイルサイズがパラメータ数から想定される非圧縮サイズ(パラメータ数×2バイト、FP16の場合)より明らかに小さいか
3. 量子化レベルの表記(Q4/Q5/Q6/Q8等)がファイル名やタグに含まれているか

## 注意点・よくある誤解

- **「量子化=劣化するだけ」ではない**: Q8_0やQ6_Kなど高ビットの量子化は、実用上ほぼ無視できる品質差でファイルサイズを大きく減らせる。「量子化=品質が落ちるから避けるべき」という判断は早計で、まずどのレベルかを確認すべき
- **数式・コード・複雑な推論では劣化が目立ちやすい**: 4ビット以下の量子化は要約や雑談レベルのタスクでは気づきにくいが、正確な計算・厳密なコード生成・多段階の推論では誤りが増えやすい。用途に応じてレベルを上げることを検討する
- **同じビット数でも方式によって品質が違う**: 「4ビットだから同じ」ではなく、AWQはGPTQより同じ4ビットで精度劣化が少ない傾向があり2026年時点ではGPU向け4ビット量子化の主流はAWQに移っている、GGUFでも`K`クオンツより`IQ`系(imatrix)の方が低ビット域で高品質、といった方式間の差がある。ビット数だけでなく方式名も確認する
- **量子化モデル同士を安易に混在・合成しない**: 異なる量子化レベルのモデルをマージ(統合)したり、量子化済みモデルにさらにファインチューニングを重ねたりすると、想定外の品質劣化が起きることがある。追加学習を前提にする場合はQATやQLoRAなど専用の手法を検討する
- **ベンチマークの数字は目安に過ぎない**: 「品質劣化1%」等の数値は特定のベンチマークでの平均値であり、自社の実際の業務内容での劣化度合いとは異なる場合がある。導入前に自社の代表的なタスクで簡単な比較検証を行うのが望ましい

## 最初の一歩

Ollamaで既にモデルを試したことがあれば、`ollama list`で現在使っているモデルの量子化レベル(タグ名)を確認し、Q4系であればQ8_0版も試して、応答品質と速度の違いを実際に比較してみる。

## 関連トピック

- [ローカルLLMの基本(自社PC・サーバーで動かす生成AI)](local-llm-basics.md)
- [モデルの種類と選び方(マルチモーダル・パラメータ数・SLM・VLM)](../part02-llm-basics/model-types-and-selection-basics.md)

## 更新履歴

### 2026-08-02: 方式比較・GGUF量子化レベルの節を最新化
- **内容**: 主要な量子化方式の表にEXL2/EXL3、MXFP4/NVFP4(ネイティブFP4)を追加し、2026年時点でGPU向け4ビット量子化の主流がGPTQからAWQに移っている旨を明記。GGUFのIQ量子化(importance matrix、imatrix)を新設の節で解説し、低ビット域でKクオンツより高品質になりやすい点を追記。PTQ/QATに加え「ネイティブ量子化」(gpt-oss等が学習時点からMXFP4で重みを持つ方式)を追加し、使いどころ表・注意点にも反映
- **出典**: [InsiderLLM: FP4 Just Landed in llama.cpp - NVFP4 vs MXFP4 Explained (2026)](https://insiderllm.com/guides/fp4-inference-llamacpp-nvfp4-mxfp4/)、[theaiengineer: GPTQ vs AWQ vs GGUF: Which 4-Bit to Pick in 2026](https://theaiengineer.substack.com/p/quantization-in-practice-gptq-vs)、[GIGAGPU: AWQ vs GPTQ vs GGUF vs EXL2: 2026 Guide](https://gigagpu.com/awq-vs-gptq-vs-gguf-vs-exl2-2026/)、[turboderp-org/exllamav3(GitHub)](https://github.com/turboderp-org/exllamav3/blob/master/doc/exl3.md)、[kaitchup: Choosing a GGUF Model - K-Quants, I-Quants and Legacy Quants](https://kaitchup.substack.com/p/choosing-a-gguf-model-k-quants-i)、[centron.de: OpenAI gpt-oss Explained - Architecture, MXFP4 Quantization](https://www.centron.de/en/tutorial/openai-gpt-oss-explained-architecture-mxfp4-quantization-120b-20b-models/)、[Hugging Face Transformers Docs: MXFP4](https://huggingface.co/docs/transformers/en/quantization/mxfp4)

### 2026-07-07: 初版執筆
- **内容**: 量子化の仕組み(精度を落として容量を圧縮する処理)、GGUF/GPTQ/AWQ/bitsandbytesの方式比較、GGUFのQ4_K_M等の表記の読み方、PTQとQATの違い、用途別の量子化レベル選定基準、Ollama/Hugging Face/LM Studioでの実際の選び方、よくある誤解を整理
- **出典**: [PromptQuorum: Q4_K_M vs Q4_0 vs Q8_0 LLM量子化を解説(2026)](https://www.promptquorum.com/ja/local-llms/llm-quantization-explained)、[Sesame Disk: Quantization Techniques for AI Inference in 2026](https://sesamedisk.com/quantization-techniques-ai-inference-2026/)、[VRLA Tech: LLM Quantization Explained: INT4, INT8, FP8, AWQ, and GPTQ in 2026](https://vrlatech.com/llm-quantization-explained-int4-int8-fp8-awq-and-gptq-in-2026/)、[ML Journey: Ollama Quantization Explained: Q4 vs Q5 vs Q8 and How to Choose](https://mljourney.com/ollama-quantization-explained-q4-vs-q5-vs-q8-and-how-to-choose/)、[GitHub ggml-org/llama.cpp Discussion #2094: Difference in different quantization methods](https://github.com/ggml-org/llama.cpp/discussions/2094)、[KnowledgeFlow: 学習後量子化(PTQ)と量子化意識学習(QAT)によるAIモデル性能比較](https://media.tcdigital.jp/ai-knowledge-flow/keywords/ptq-qat-ai/)
