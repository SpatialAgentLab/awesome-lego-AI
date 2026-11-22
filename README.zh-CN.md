# 🧱 Awesome LEGO AI

[English](README.md) | [简体中文](README.zh-CN.md)

面向 **LEGO / 咬合积木 × AI** 的研究资源清单：从空间与时序推理，到说明书理解、三维生成、装配规划和机器人执行。

最近整理：**2026-11-22**。共 **64 个独立条目**，其中 **35 篇论文**、**29 个数据／基准条目**。同一项目可同时提供论文、数据、代码和视频，不重复计为独立项目。

优先收录原论文、作者项目页、官方代码和数据入口。年份优先采用首个预印本年份，正式发表信息另列；摘要为本清单重新撰写。链接核对不等于代码复现或数据完整下载。

**从这里开始：** [训练数据与 Benchmark](#datasets-benchmarks) · [中文阅读路线与研究切入点](docs/RESEARCH_GUIDE.zh-CN.md) · [BibTeX](papers.bib) · [机器可读目录](data/resources.json) · [核验说明](docs/VERIFICATION.md)

<a id="datasets-benchmarks"></a>

## 训练数据与 Benchmark

**数据优先：以下在正文汇总全部 29 个数据／基准条目，提供任务、规模、获取状态和原始入口。** 数据与配套测试集、独立 benchmark、原始素材分别列出；部分项目同时支持训练与评测。

**本轮更新（2026-11-22）：** 新增 [BrickVision（11 月）](#brickvision)、[LMBuild（10 月）](#lmbuild)、[PIXIE](#pixie)、[仿真装配示范](#lego-flat200)、[YUBI（受限访问）](#yubi-umi-arena)、[OMR 整合包](#omr-rebrickable) 和 [BrickAGI（社区）](#brickagi)；补全 [BrickFlow / ProcBrick](#brickflow) 的 1 亿结构预训练集、100 万微调渲染图与评测划分。表格末尾另列尚未确认下载的数据线索，不计入上述数据条目。

**按任务定位：** 空间推理看 [LEGO-Puzzles](#lego-puzzles)；时序理解看 [TPRU 的 LEGO 子集](#tpru)；文本到结构看 [StableText2Brick](#brickgpt) / [BrickNet](#bricknet)；说明书与纠错看 [MEPNet](#mepnet) / [LEGO-ECA](#scanet)；生成评测看 [BrickBench](#brickbench)。

规模沿用原始发布记录，不代表本地下载核验后的可用训练量，也不能跨条目直接相加。**TPRU 的 24,750 条是多领域训练总量，并非 LEGO 子集大小。** 更完整的选用、划分与许可注意事项见 [数据子文档](docs/DATASETS.md)。

### 训练数据与配套评测集

| 数据／基准 | 模态与任务 | 报告规模 | 获取状态 | 数据／原始入口 |
| --- | --- | --- | --- | --- |
| [BrickFlow / ProcBrick](#brickflow) | Procedural assemblies + image-conditioned reconstruction data | 100M pretraining trees (100 parts each); 1M finetuning renders; 9,900 validation renders | Hugging Face 文件公开（MIT）；额外的 512 模型 BrickNet 评测集需另行申请 BrickNet。 | [Code](https://github.com/kulits/BrickFlow) · [Data](https://huggingface.co/datasets/kulits/BrickFlow) · [Models](https://huggingface.co/kulits/BrickFlow) · [Data generator](https://github.com/kulits/ProcBrick) |
| [LEGO flat final-goal 200](#lego-flat200) | Simulation video + robot states / actions + goal image / text | 200 episodes (100 teleoperation + 100 correction); 79,956 frames at 20 Hz | Parquet／MP4 文件公开；meta/info.json 已确认规模与仅训练划分。许可仍需澄清。 | [Data](https://huggingface.co/datasets/ajaysri/lego_flat_final_goal_200_v1) · [Data metadata](https://huggingface.co/datasets/ajaysri/lego_flat_final_goal_200_v1/blob/main/meta/info.json) |
| [YUBI UMI Arena — includes LEGO subset](#yubi-umi-arena) | Real robot RGB + states + actions; LeRobot v3 | Initial release: 336,543 primitive-action episodes / 579.9 h across tasks | 人工审核、仅限竞赛用途；只有训练划分，全量约 2.7 TB；需按任务元数据筛选 LEGO。 | [Data / terms](https://huggingface.co/datasets/airoa-org/yubi-corl2026-umi-arena) |
| [TPRU-25k / TPRU-test](#tpru) | Frame sequences + temporal QA | 24,750 training examples across domains | Hugging Face；论文注明 LEGO 源材料为 Arvin Bricks 的 36 个定格动画视频。 | [Code](https://github.com/Stephen-gzk/TPRU) · [Data](https://huggingface.co/datasets/Stephengzk/TPRU-25k) · [Test](https://huggingface.co/datasets/Stephengzk/TPRU-test) |
| [StableText2Brick (formerly StableText2Lego)](#brickgpt) | Brick sequences + text captions | Over 47,000 structures / over 28,000 unique objects | Hugging Face；官方代码仓库提供模型和生成流程入口。 | [Code](https://github.com/AvaLovelace1/BrickGPT) · [Data](https://huggingface.co/datasets/AvaLovelace/StableText2Brick) |
| [BrickNet](#bricknet) | LDraw-derived graphs + build paths + captions | Paper: over 100,000 human-designed objects / scenes | 数据需要通过表单申请；代码和部分零件资产公开。 | [Code](https://github.com/kulits/BrickNet) · [Data request](https://forms.gle/dm4eYSa5gh4DqzRT6) · [Data documentation](https://github.com/kulits/BrickNet/blob/master/DATA.md) |
| [MEPNet LEGO manual datasets](#mepnet) | Manual images + 3D parts / poses | Three LEGO manual datasets; see paper | 仓库链接 SharePoint 上的训练、验证与评测数据；本次未下载完整压缩包。 | [Code](https://github.com/Relento/lego_release) · [Data instructions](https://github.com/Relento/lego_release#evaluation) |
| [LEGO-ECA](#scanet) | Manual images + erroneous assemblies / corrections | 1,429 manuals; approximately 120,000 incorrect examples | 官方补充仓库提供 Google Drive / 百度网盘；本次未下载完整数据。 | [Data instructions](https://github.com/kaichen-z/SCANet-Supp) |
| [MobileBrick](#mobilebrick) | RGB-D + camera poses + masks + ground-truth mesh | 153 sequences: 135 training + 18 evaluation | 通过官方项目页／仓库下载；这是重建数据，并非装配动作语料。 | [Code / data](https://github.com/ActiveVisionLab/MobileBrick) |
| [StableLego](#stablelego) | Voxel grids + assembly JSON + stability scores | See upstream release | 官方仓库提供下载入口，包含稳定与不稳定结构样本。 | [Code / data](https://github.com/intelligent-control-lab/StableLego) |
| [Combinatorial 3D Shape Dataset](#combinatorial3d) | Primitive structures + generation scripts | See repository dataset directory | 仓库内包含数据目录与生成脚本。 | [Code](https://github.com/POSTECH-CVLab/Combinatorial-3D-Shape-Generation) |
| [Photos and rendered images of LEGO bricks](#photos-renders) | Real photos + renders + part labels / detection subsets | Approximately 155,000 photos + 1.5 million renders across the collection | 按论文中各子数据集 DOI 获取；Most Wiedzy 可能需要浏览器验证。 | [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10657460/) |
| [B200C](#b200c) | Synthetic RGB part images | 800,000 images / 200 classes / 64×64 | 作者提供 Kaggle 链接；当前能否下载尚未确认。 | [Data](https://www.kaggle.com/datasets/ronanpickell/b200c-lego-classification-dataset) |

### Benchmark 与交互任务环境

| 数据／基准 | 模态与任务 | 报告规模 | 获取状态 | 数据／原始入口 |
| --- | --- | --- | --- | --- |
| [BrickVision](#brickvision) | Brick images + pointing / counting labels | 1,000 test items: 4 tasks × 250 | Hugging Face 文件与评测器公开；代码含场景生成器。使用同类生成任务训练的结果需单列。 | [Code](https://github.com/elorian-ai/why-grounding) · [Data](https://huggingface.co/datasets/elorian-ai/BrickVision) |
| [LMBuild Core / Full — LEGO subset](#lmbuild) | Text + images + CAD assemblies / joints / evaluation | Core: 200 total / 55 LEGO; Full: 2,549 total / 938 LEGO | Hugging Face 数据与下载脚本公开；属于混合领域评测，不是独立的全 LEGO 训练语料。 | [Code](https://github.com/Lumos-Jiateng/LMBuild) · [Data](https://huggingface.co/datasets/Lumos-Jiateng/LMBuild) |
| [PIXIE Assembly](#pixie) | RGB + 6DoF poses + assembly defects | 4 model folders / 695 input-image files counted in repository | 公开、仅测试（不可训练／调参）；统计排除了标定图与网站展示图。 | [Data / protocol](https://github.com/ZEISS/PIXIE-dataset) · [Data files](https://github.com/ZEISS/PIXIE-dataset/tree/main/dataset) |
| [LEGO-Puzzles](#lego-puzzles) | Images + VQA / planning | Elementary: 1,100 questions / 11 tasks; Planning: see paper version | Hugging Face；下载版本须与所采用论文版本对应。 | [Code](https://github.com/Tangkexian/LEGO-Puzzles) · [Data](https://huggingface.co/datasets/KexianTang/LEGO-Puzzles) |
| [BC-Bench / Brick-Composer assets](#brick-composer) | Manual renders + brick selection + 6-DoF pose / trajectories | See release splits; designer supervision covers 102 human-designed objects | 官方仓库提供 Hugging Face 入口；需单独确认 benchmark 的划分。 | [Code](https://github.com/Lumos-Jiateng/Brick-Composer) · [Data](https://huggingface.co/datasets/Lumos-Jiateng/brick_synthetic) · [Design data](https://huggingface.co/datasets/Lumos-Jiateng/bricklink_lego_design) |
| [BrickBench prompts / runs](#brickbench) | Text prompts + generated assemblies / agent runs | 300 prompts across 3 settings | 题目在 BrickAgent 仓库；运行产物在 Hugging Face。 | [Code](https://github.com/kulits/BrickAgent) · [Data](https://huggingface.co/datasets/kulits/BrickBench-Runs) |
| [WorkBenchMark](#workbenchmark) | YAML task specifications + hidden ground truth | 400 tasks / 4 difficulty tiers | 任务文件已公开；ground_truth 仅供评测，不能作为求解器输入。 | [Data](https://github.com/WorkBenchMark/dataset) |
| [LTRON / Break and Make](#break-make) | LDraw models + interactive assembly environment | Complex models with over 1,000 distinct brick shapes in the paper | 通过 LTRON 获取资产；固定与论文对应的版本。 | [Code / simulator](https://github.com/aaronwalsman/ltron) · [Training](https://github.com/aaronwalsman/ltron-torch) |
| [LTRON procedural vehicles](#instructionet) | Procedural models + assembly / disassembly episodes | Average 31 bricks; over 100 disassembly/reassembly actions | 使用 LTRON v1.1.0 与 eccv-24 训练分支。 | [Environment / data](https://github.com/aaronwalsman/ltron/tree/v1.1.0) |
| [BrickAGI v1.5](#brickagi) | Text design tasks + parts / placements + structural checks | 37 public tasks / 7 difficulty tiers, per upstream index | 社区开卷任务／答案及留出集生成器；需固定协议和验证器版本。 | [Code / data](https://github.com/withtally/brickagi) · [Data task index](https://github.com/withtally/brickagi/blob/main/brickagi/tasks/INDEX.md) |

### 构建数据集的原始素材

| 数据／基准 | 模态与任务 | 报告规模 | 获取状态 | 数据／原始入口 |
| --- | --- | --- | --- | --- |
| [sets_lego_omr_full](#omr-rebrickable) | MPD structure text + set metadata | Approximately 1,367 sets, as reported by the curator | Hugging Face 提供 JSONL 文件；属于社区打包，与上游数据重叠。 | [Data](https://huggingface.co/datasets/DylanRiden/sets_lego_omr_full) |
| [Conveyor-belt videos](#conveyor) | Real video | Multiple dataset records; see catalog | 机构目录，可能需要浏览器验证。 | [Data](https://mostwiedzy.pl/en/open-research-data-series/video-of-lego-bricks-on-conveyor-belt,202011132226557715481-0/catalog) |
| [Lego Project Data Archive](#lego-video-archive) | Audio + video + ancillary material | See archive records | 大学记录链接 Zenodo；用于交互研究，不提供逐砖位姿标注的保证。 | [Data record](https://vbn.aau.dk/en/datasets/lego-project-data-archive/) |
| [LDraw OMR](#ldraw-omr) | LDR / MPD models | Growing community catalog | 按模型记录和文件条款使用；模型不自动等于已验证动作轨迹。 | [Models](https://library.ldraw.org/omr) |
| [Official building instructions](#lego-instructions) | PDF manuals | Continuously updated | 官方检索入口；公开阅读与再分发／训练授权应分开确认。 | [Instructions](https://www.lego.com/en-us/service/building-instructions) |
| [Rebrickable catalog](#rebrickable) | Tabular metadata / API | Continuously updated | 目录／API，并非带标注的视觉数据集。 | [Downloads](https://rebrickable.com/downloads/) · [API](https://rebrickable.com/api/) |

### 待确认数据发布：论文已公开

以下规模为论文报告；尚未确认完整数据下载，不能当作已取得的训练集。

| 项目 | 报告规模 | 发布状态 |
| --- | --- | --- |
| [JARVIS / JARVIS-v1](#jarvis) | 236,679 training tasks / 8,987 scenes; 50 evaluation tasks | 论文描述了语料规模；公开下载尚未确认。 |
| [LegoVerse / LegoACE](#legoace) | >55,000 models / 9,314 brick types (paper report) | 代码与权重已有入口；完整语料下载未确认。 |
| [BrickAnything training data](#brickanything) | No separately verified release size | 有推理代码与权重；独立训练数据发布未确认。 |

## 快速选读

| 目标 | 建议起点 |
| --- | --- |
| 多模态空间／时序推理 | [LEGO-Puzzles](#lego-puzzles) → [TPRU](#tpru) → [Brick-Composer](#brick-composer) |
| 文本到可搭建模型 | [BrickGPT](#brickgpt) → [BrickNet](#bricknet) → [BrickBench](#brickbench) / [BrickWright](#brickwright) / [DailyBrick](#dailybrick) |
| 说明书到动作与纠错 | [MEPNet](#mepnet) → [SCANet](#scanet) → [InstructioNet](#instructionet) |
| 三维重建 | [MobileBrick](#mobilebrick) → [BrickFlow](#brickflow) |
| 真实机器人 | [StableLego](#stablelego) → [BrickSim](#bricksim) → [WorkBenchMark](#workbenchmark) |

## 目录

- [训练数据与 Benchmark](#datasets-benchmarks)
- [空间与过程推理](#reasoning)
- [生成式设计与积木化](#generation)
- [说明书理解与装配规划](#assembly)
- [机器人、物理与仿真](#robotics)
- [识别与三维重建](#perception)
- [其他数据来源](#data)
- [CAD、渲染与评测工具](#tools)
- [演讲与视频来源](#videos)
- [应用](#applications)
- [相关清单](#community)
- [论文演示视频速查](#research-videos)

[Contributing](CONTRIBUTING.md) · [Publishing to GitHub](docs/PUBLISHING.md)

<a id="reasoning"></a>

## 空间与过程推理

<a id="brickvision"></a>

### BrickVision / Where and Why is Grounded Reasoning Useful?

*2026 · arXiv; November 2026*

通过局部图匹配、计数、重复结构识别和无配对结构搜索，评测积木场景中的细粒度视觉定位；包含程序化渲染、风格化图像和几何标签。

[Paper](https://arxiv.org/abs/2611.08485) · [Project](https://elorian.ai/blog/why-grounding) · [Code](https://github.com/elorian-ai/why-grounding) · [Data](https://huggingface.co/datasets/elorian-ai/BrickVision) · [Related training / outputs](https://huggingface.co/datasets/elorian-ai/why-grounding)

> 已逐个统计四份测试 JSONL，各 250 条。配套 SFT/RL 发布也包含非 LEGO 任务，不能全部计为 LEGO 训练数据。数据卡标注 CC BY 4.0。

<a id="lego-puzzles"></a>

### LEGO-Puzzles: How Good Are MLLMs at Multi-Step Spatial Reasoning?

*2025 · arXiv; revised 2026*

评测空间理解与多步搭建规划，适合作为多模态模型的起点评测。

[Paper](https://arxiv.org/abs/2503.19990) · [Code](https://github.com/Tangkexian/LEGO-Puzzles) · [Data](https://huggingface.co/datasets/KexianTang/LEGO-Puzzles) · [Project](https://tangkexian.github.io/LEGO-Puzzles/)

<a id="tpru"></a>

### TPRU: Advancing Temporal and Procedural Understanding in Large Multimodal Models

*2026 · ICLR 2026*

包含 LEGO 装配子集的多领域时序推理工作，覆盖排序、下一帧预测与前序帧回溯。

[Paper](https://arxiv.org/abs/2602.18884) · [Code](https://github.com/Stephen-gzk/TPRU) · [Data](https://huggingface.co/datasets/Stephengzk/TPRU-25k) · [Test](https://huggingface.co/datasets/Stephengzk/TPRU-test)

> 24,750 是多领域训练集总量，不是 LEGO 子集大小。

<a id="co-builder"></a>

### LEGO Co-builder: Exploring Fine-Grained Vision-Language Modeling for Multimodal LEGO Assembly Assistants

*2025 · arXiv; revised 2026*

研究分步 LEGO 场景中的细粒度指令遵循与状态识别。

[Paper](https://arxiv.org/abs/2507.05515) · [Code](https://github.com/peterhuang-coding/LEGO-Co-builder)

> 作者链接的仓库存在，但 README 很简略；数据打包方式和复现步骤仍需核实。

<a id="brick-composer"></a>

### Brick-Composer: Using MLLMs for Assembly with Diverse Bricks

*2026 · arXiv*

BC-Bench 将选砖与位姿预测分开评测，结合人类设计、仿真反馈和合成轨迹训练。

[Paper](https://arxiv.org/abs/2606.05445) · [Code](https://github.com/Lumos-Jiateng/Brick-Composer) · [Project](https://lumos-jiateng.github.io/Brick-Composer/) · [Data](https://huggingface.co/datasets/Lumos-Jiateng/brick_synthetic) · [Design data](https://huggingface.co/datasets/Lumos-Jiateng/bricklink_lego_design)

> 仓库使用标题“MLLMs Construct Everything from Building Blocks”，与此条为同一项目。

<a id="brickbench"></a>

### BrickBench: Evaluating Agentic Brick Design

*2026 · arXiv*

评测文本驱动的编程智能体，覆盖小模型、整套搭建与限定零件库存。

[Paper](https://arxiv.org/abs/2610.12452) · [Project](https://brickben.ch/) · [Code](https://github.com/kulits/BrickAgent) · [Data](https://huggingface.co/datasets/kulits/BrickBench-Runs) · [Gallery](https://gallery.brickben.ch/)

<a id="generation"></a>

## 生成式设计与积木化

<a id="lmbuild"></a>

### LMBuild: Evaluating LLM Agents for Generating Buildable and Functional Structures

*2026 · arXiv; October 2026*

评测智能体生成零件、关节、材料和装配顺序的能力，覆盖结构、功能、设计与实现；包含 LEGO 与其他 CAD 领域。

[Paper](https://arxiv.org/abs/2610.04292) · [Project](https://lumos-jiateng.github.io/LMBuild/) · [Code](https://github.com/Lumos-Jiateng/LMBuild) · [Data](https://huggingface.co/datasets/Lumos-Jiateng/LMBuild)

> 作者来源表给出 Core 中 55 个 LEGO 任务（50 BrickComposer + 5 BrickNet），Full 中 938 个（50 + 888）；与上游语料重叠。数据采用 CC BY-NC-SA 4.0，并保留逐对象来源条款。

<a id="brickagi"></a>

### BrickAGI — community brick-design benchmark

*2026 · Community benchmark; v1.5 June 2026*

提供设计题、参考放置结果与有明确覆盖范围的结构验证器，区分直接生成放置与提示连接规则两种协议。

[Code / data](https://github.com/withtally/brickagi) · [Data task index](https://github.com/withtally/brickagi/blob/main/brickagi/tasks/INDEX.md)

> 社区 benchmark，非同行评审论文。公开任务与答案属于开卷设置；未见任务评测应使用其留出集生成器。验证器不覆盖咬合力、插入顺序和负载稳定性。

<a id="legoace"></a>

### LegoACE: Autoregressive Construction Engine for Expressive LEGO Assemblies

*2025 · SIGGRAPH Asia 2025*

从文本或法线图生成装配结构，并报告覆盖大量零件类型的 LegoVerse 语料。

[Paper](https://doi.org/10.1145/3757377.3763881) · [Project](https://xh38.github.io/LegoACE/) · [Code](https://github.com/VAST-AI-Research/LegoACE) · [Models](https://huggingface.co/VAST-AI/LegoACE)

> 官方仓库给出数据格式、训练步骤和权重入口，但尚未确认完整 LegoVerse 数据集下载。

<a id="brickanything"></a>

### BrickAnything: Geometry-Conditioned Buildable Brick Generation with Structure-Aware Tokenization

*2026 · arXiv; repository labels NeurIPS 2026*

以点云或网格为条件生成积木，结合连接关系树编码、偏好优化和结构回退。

[Paper](https://arxiv.org/abs/2605.26182) · [Code](https://github.com/xjtunzy/BrickAnything) · [Models](https://huggingface.co/niels-peter/BrickAnything)

> 官方 README 提供推理和权重下载；未确认单独发布的作者训练数据归档。稳定性分析依赖 Gurobi。

<a id="dailybrick"></a>

### DailyBrick: Language-Guided Synthesis of Brick Assembly Instructions

*2026 · arXiv*

通过智能体流程生成积木模型与可执行的逐砖说明书，并进行审查和修复。

[Paper](https://arxiv.org/abs/2611.22132) · [Project](https://spatialagentlab.github.io/DailyBrick.github.io/) · [Video](https://spatialagentlab.github.io/DailyBrick.github.io/assets/dailybrick-demo.mp4)

> SpatialAgentLab 项目；公开项目网页仓库不等于算法代码或数据已发布。

<a id="brickwright"></a>

### BrickWright: Agentic Creation of Physically Feasible Brick Builds

*2026 · arXiv*

为预训练智能体提供 BrickLayer 搭建 API 与物理可行性检查器。

[Paper](https://arxiv.org/abs/2610.31651) · [Project](https://avalovelace1.github.io/brickwright/) · [Code](https://github.com/AvaLovelace1/brickwright)

> 检查器定义的物理可行性不能直接等同于任意真实机器人都可执行。

<a id="bricknet"></a>

### BrickNet: Graph-Backed Generative Brick Assembly

*2026 · CVPR 2026*

采用基于连接关系的表示，生成包含多种真实零件类型的积木结构。

[Paper](https://arxiv.org/abs/2604.22984) · [Project](https://kulits.github.io/BrickNet/) · [Code](https://github.com/kulits/BrickNet) · [Data request](https://forms.gle/dm4eYSa5gh4DqzRT6) · [Data documentation](https://github.com/kulits/BrickNet/blob/master/DATA.md)

<a id="brickgpt"></a>

### Generating Physically Stable and Buildable Brick Structures from Text (BrickGPT / LegoGPT)

*2025 · ICCV 2025*

通过自回归模型、合法性检查和物理约束回退，实现文本到积木结构生成。

[Paper](https://arxiv.org/abs/2505.05469) · [Project](https://avalovelace1.github.io/BrickGPT/) · [Code](https://github.com/AvaLovelace1/BrickGPT) · [Data](https://huggingface.co/datasets/AvaLovelace/StableText2Brick) · [Video page](https://avalovelace1.github.io/BrickGPT/)

> LegoGPT / StableText2Lego 是 BrickGPT / StableText2Brick 的早期名称，不重复计数。

<a id="treesba"></a>

### TreeSBA: Tree-Transformer for Self-Supervised Sequential Brick Assembly

*2024 · ECCV 2024*

利用树表示与轮廓自监督，从多视角图像预测搭建序列。

[Paper](https://arxiv.org/abs/2407.15648) · [Project](https://dreamguo.github.io/projects/TreeSBA/) · [Code](https://github.com/dreamguo/TreeSBA) · [Video](https://dreamguo.github.io/projects/TreeSBA/resources/Assembly_Airplane.mp4)

<a id="brick-by-brick"></a>

### Brick-by-Brick: Combinatorial Construction with Deep Reinforcement Learning

*2021 · NeurIPS 2021*

从目标图像学习逐砖放置，并筛除非法动作。

[Paper](https://arxiv.org/abs/2110.15481) · [Code](https://github.com/POSTECH-CVLab/Brick-by-Brick)

<a id="image2lego"></a>

### Image2Lego: Customized LEGO Set Generation from Images

*2021 · arXiv*

从图像预测体素表示，再转换为积木布局与搭建说明。

[Paper](https://arxiv.org/abs/2108.08477)

<a id="graph-lego"></a>

### Building LEGO Using Deep Generative Models of Graphs

*2020 · NeurIPS 2020 ML4Eng workshop*

从人类设计中学习积木结构的早期图生成模型。

[Paper](https://arxiv.org/abs/2012.11543)

<a id="combinatorial3d"></a>

### Combinatorial 3D Shape Generation via Sequential Assembly

*2020 · NeurIPS 2020 ML4Eng workshop*

利用贝叶斯优化，在几何和稳定性目标下选择顺序放置动作。

[Paper](https://arxiv.org/abs/2004.07414) · [Code](https://github.com/POSTECH-CVLab/Combinatorial-3D-Shape-Generation)

<a id="legolization"></a>

### Legolization: Optimizing LEGO Designs

*2015 · ACM TOG / SIGGRAPH Asia 2015*

使用基于受力的稳定性分析优化积木布局，是几何模型转积木的重要早期工作。

[Paper](https://www.cs.columbia.edu/~yonghao/siga15/luo-Legolization.pdf) · [Video](https://www.youtube.com/watch?v=Uv5gpqlkpis)

<a id="assembly"></a>

## 说明书理解与装配规划

<a id="mepnet"></a>

### Translating a Visual LEGO Manual to a Machine-Executable Plan (MEPNet)

*2022 · ECCV 2022*

从图解说明书恢复零件位姿与装配步骤。

[Paper](https://arxiv.org/abs/2207.12572) · [Project](https://cs.stanford.edu/~rcwang/projects/lego_manual/) · [Code](https://github.com/Relento/lego_release) · [Data instructions](https://github.com/Relento/lego_release#evaluation) · [Video](https://cs.stanford.edu/~rcwang/projects/lego_manual/resources/video.mp4)

<a id="break-make"></a>

### Break and Make: Interactive Structural Understanding Using LEGO Bricks

*2022 · ECCV 2022*

提出 LTRON：先观察并拆解结构，再使用低层动作重建。

[Paper](https://arxiv.org/abs/2207.13738) · [Code / simulator](https://github.com/aaronwalsman/ltron) · [Training](https://github.com/aaronwalsman/ltron-torch)

> 复现应使用对应论文版本；master 的 README 提醒开发版不稳定且存在非公开依赖。

<a id="instructionet"></a>

### Learning to Build by Building Your Own Instructions (InstructioNet)

*2024 · ECCV 2024*

在拆解时保存视觉说明书，支持更长序列的重建。

[Paper](https://arxiv.org/abs/2410.01111) · [Environment / data](https://github.com/aaronwalsman/ltron/tree/v1.1.0) · [Training](https://github.com/aaronwalsman/ltron-torch/tree/eccv-24)

<a id="scanet"></a>

### SCANet: Correcting LEGO Assembly Errors with Self-Correct Assembly Network

*2024 · IROS 2024*

依据说明书图像检测错装零件并预测修正。

[Paper](https://arxiv.org/abs/2403.18195) · [Data instructions](https://github.com/kaichen-z/SCANet-Supp) · [Video](https://github.com/kaichen-z/SCANet-Supp/blob/master/assets/Final_2.mp4)

> 旧项目网站返回 404，改用官方补充仓库和演示视频。其 README 的 Code 链接实际指向 MP4，因此不标记为已核实的算法实现。

<a id="graph-asp"></a>

### Planning Assembly Sequence with Graph Transformer

*2022 · arXiv*

将 LEGO 装配表示为异构图并预测搭建顺序。

[Paper](https://arxiv.org/abs/2210.05236)

<a id="physics-asp"></a>

### Physics-Aware Combinatorial Assembly Sequence Planning using Data-free Action Masking

*2024 · IEEE RA-L 2025*

利用在线物理动作掩码约束强化学习，规划可执行搭建序列。

[Paper](https://arxiv.org/abs/2408.10162) · [Code](https://github.com/intelligent-control-lab/PhysicsAwareCombinatorialASP)

<a id="robotics"></a>

## 机器人、物理与仿真

<a id="yubi-umi-arena"></a>

### YUBI — The UMI Arena @ CoRL 2026

*2026 · CoRL 2026 workshop competition data*

真实双臂操作记录包含 LEGO 拼装／拆解和其他任务；LeRobot v3 数据提供三视角图像、机器人状态、动作与任务层级。

[Data / terms](https://huggingface.co/datasets/airoa-org/yubi-corl2026-umi-arena) · [Project](https://umi-arena.airoa.io/)

> 限通过审核并提交 NDA／保密承诺的竞赛参与者使用，不是通用开放研究语料。规模为所有任务总量，LEGO 子集大小尚未核实；本次未申请访问。

<a id="lego-flat200"></a>

### LEGO flat final-goal demonstrations (community release)

*2026 · Hugging Face; September 2026*

仿真 UR5/WSG50 示范将机器人观测与动作配对到完整搭建目标图或文本，包含遥操作与纠正轨迹。

[Data](https://huggingface.co/datasets/ajaysri/lego_flat_final_goal_200_v1) · [Data metadata](https://huggingface.co/datasets/ajaysri/lego_flat_final_goal_200_v1/blob/main/meta/info.json)

> 社区训练数据，不是标准化 benchmark；没有留出测试集，所核对数据卡未明确复用许可。inspection 浏览表不能重复计入训练量。

<a id="jarvis"></a>

### JARVIS: From Visual Manuals to Autonomous Robotic Assembly

*2026 · arXiv; October 2026*

研究仿真中的视觉说明书引导机器人装配，报告大规模任务语料与 50 任务交互评测集。

[Paper](https://arxiv.org/abs/2610.27618) · [Dataset description](https://arxiv.org/html/2610.27618v1)

> 本次未确认作者发布的数据下载入口。论文提供目标积木位姿与装配状态，不代表每个任务都有底层机器人示范轨迹。

<a id="stablelego"></a>

### StableLego: Stability Analysis of Block Stacking Assembly

*2024 · IEEE RA-L 2024*

分析受力平衡与结构稳定性，可用于检查生成的搭建方案。

[Paper](https://arxiv.org/abs/2402.10711) · [Code / data](https://github.com/intelligent-control-lab/StableLego)

> 实现依赖 Gurobi；有代码不代表环境可直接运行。

<a id="workbenchmark"></a>

### WorkBenchMark: A LEGO-Based Assembly Benchmark with an Assembly-by-Disassembly Baseline for the Smart Manufacturing League

*2026 · RoboCup Symposium 2026*

连接感知、符号规划与操作的 Duplo 装配基准。

[Paper](https://arxiv.org/abs/2606.19358) · [Project](https://workbenchmark.github.io/) · [Data](https://github.com/WorkBenchMark/dataset) · [Video](https://workbenchmark.github.io/static/videos/demo.mp4)

<a id="bricksim"></a>

### BrickSim: A Physics-Based Simulator for Manipulating Interlocking Brick Assemblies

*2026 · arXiv*

仿真咬合积木的操作，可用于装配、拆卸与遥操作研究。

[Paper](https://arxiv.org/abs/2603.16853) · [Code](https://github.com/intelligent-control-lab/BrickSim) · [Project](https://intelligent-control-lab.github.io/BrickSim/) · [Video](https://www.youtube.com/watch?v=VGuHfz4yxLU)

> 当前官方快速入门面向 x86-64 Linux 与 NVIDIA / Isaac Sim；本次没有在本机安装仿真器。

<a id="apex-mr"></a>

### APEX-MR: Multi-Robot Asynchronous Planning and Execution for Cooperative Assembly

*2025 · RSS 2025*

通过异步规划与执行协调多个机器人协作装配。

[Paper](https://arxiv.org/abs/2503.15836) · [Project / video](https://intelligent-control-lab.github.io/APEX-MR/)

<a id="eye-in-finger"></a>

### Eye-in-Finger: Smart Fingers for Delicate Assembly and Disassembly of LEGO

*2025 · IROS 2025*

研究面向精密积木插接与拆卸的传感手指。

[Paper](https://arxiv.org/abs/2503.06848) · [Lab / video](https://icontrol.ri.cmu.edu/research/lego.html)

<a id="human-demonstration"></a>

### Robotic LEGO Assembly and Disassembly from Human Demonstration

*2023 · arXiv*

从人类演示学习装配与拆卸，并用数字孪生验证执行。

[Paper](https://arxiv.org/abs/2305.15667) · [Lab / video](https://icontrol.ri.cmu.edu/research/lego.html)

<a id="perception"></a>

## 识别与三维重建

<a id="pixie"></a>

### PIXIE Assembly Dataset

*2026 · Dataset release*

使用有装配缺陷、颜色变化与杂乱背景的 LEGO 物体评测零样本 6DoF 位姿估计，提供 RGB、相机标定、目标几何与装配状态标签。

[Data / protocol](https://github.com/ZEISS/PIXIE-dataset) · [Data files](https://github.com/ZEISS/PIXIE-dataset/tree/main/dataset)

> 仅测试：不可用这些图像训练或调参；推理只能使用完整装配的目标模型，不能输入缺陷状态几何或真值。未提供评测脚本。许可为 CC BY 4.0。

<a id="mobilebrick"></a>

### MobileBrick: Building LEGO for 3D Reconstruction on Mobile Devices

*2023 · CVPR 2023*

移动设备 RGB-D 观测与精确几何配对，用于精细三维重建。

[Paper](https://arxiv.org/abs/2303.01932) · [Code / data](https://github.com/ActiveVisionLab/MobileBrick) · [Project](https://code.active.vision/MobileBrick/)

<a id="brickflow"></a>

### BrickFlow: Connectivity-Guided Brick Reconstruction

*2026 · NeurIPS 2026 (author release)*

给定图像与零件集合，利用 SE(3) 流模型和连接引导推断零件位姿。

[Paper](https://arxiv.org/abs/2611.17321) · [Project](https://kulits.github.io/BrickFlow/) · [Code](https://github.com/kulits/BrickFlow) · [Data](https://huggingface.co/datasets/kulits/BrickFlow) · [Models](https://huggingface.co/kulits/BrickFlow) · [Data generator](https://github.com/kulits/ProcBrick)

> ProcBrick 树是合成结构，不是人工设计模型或真实机器人示范。已核对预训练、图像条件微调和验证目录；未完整下载语料。

<a id="photos-renders"></a>

### Photos and rendered images of LEGO bricks

*2023 · Scientific Data*

记录真实照片和合成零件图像的数据论文，包含零件身份与类别标签。

[Paper](https://www.nature.com/articles/s41597-023-02682-2) · [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10657460/)

<a id="data"></a>

## 其他数据来源

<a id="omr-rebrickable"></a>

### LEGO OMR + Rebrickable JSONL (community packaging)

*2026 · Hugging Face; January 2026*

将完整 LDraw MPD 文本与套装元数据打包，便于结构生成实验；是本清单已有 OMR 与 Rebrickable 来源的社区整合版。

[Data](https://huggingface.co/datasets/DylanRiden/sets_lego_omr_full)

> 不能算作 OMR 之外新增的独立模型。数据卡将打包产物标为 Apache-2.0，但仍须核对原模型和元数据条款；未确认已验证装配轨迹或固定测试集。

<a id="b200c"></a>

### B200C LEGO Classification Dataset

*2021*

带随机场景、光照和遮挡的合成零件分类图像。

[Code / documentation](https://github.com/korra-pickell/LEGO-Classification-Dataset) · [Data](https://www.kaggle.com/datasets/ronanpickell/b200c-lego-classification-dataset)

> 作者仓库记录了该数据集，但 Kaggle 入口对 HEAD 返回 404，网页读取仅得到脚本页面；当前下载可用性尚未确认。

<a id="conveyor"></a>

### Video of LEGO bricks on conveyor belt

*2022*

用于零件识别与分拣研究的真实传送带视频。

[Data](https://mostwiedzy.pl/en/open-research-data-series/video-of-lego-bricks-on-conveyor-belt,202011132226557715481-0/catalog) · [Descriptor](https://mostwiedzy.pl/pl/publication/download/1/video-of-lego-bricks-on-conveyor-belt-dataset-series_71732.pdf)

> 本次自动访问遇到反爬页面，未确认能否完成数据下载。

<a id="lego-video-archive"></a>

### Lego Project Data Archive

*2020*

协作 LEGO 拼图活动的研究档案，包含音视频与 360 度材料。

[Data record](https://vbn.aau.dk/en/datasets/lego-project-data-archive/)

<a id="ldraw-omr"></a>

### LDraw Official Model Repository (OMR)

以通用 CAD 格式发布的社区 LEGO 套装重建模型。

[Models](https://library.ldraw.org/omr)

<a id="rebrickable"></a>

### Rebrickable downloads and API

提供零件、颜色、套装和库存元数据，可连接 CAD、说明书与视频套装编号。

[Downloads](https://rebrickable.com/downloads/) · [API](https://rebrickable.com/api/)

> 本次自动浏览访问受阻，具体下载入口和当前条款需人工核对。

<a id="lego-instructions"></a>

### LEGO official building instructions

按套装编号查找原版说明书和步骤参考。

[Instructions](https://www.lego.com/en-us/service/building-instructions)

<a id="tools"></a>

## CAD、渲染与评测工具

<a id="ldraw"></a>

### LDraw parts library and file format

数字积木流程的基础零件几何库与交换格式。

[Website](https://www.ldraw.org/) · [Library](https://library.ldraw.org/)

<a id="leocad"></a>

### LeoCAD

开源且兼容 LDraw 的积木模型编辑与检查工具。

[Website](https://www.leocad.org/) · [Code](https://github.com/leozide/leocad)

<a id="studio"></a>

### BrickLink Studio

桌面积木设计工具与说明书制作生态。

[Website](https://www.bricklink.com/v3/studio/download.page)

> 2026-11-22 访问跳转到维护公告，安装前需重新确认。

<a id="lpub3d"></a>

### LPub3D

基于 LDraw 模型制作 LEGO 风格数字搭建说明书。

[Code](https://github.com/trevorsandy/lpub3d)

<a id="importldraw"></a>

### ImportLDraw for Blender

将 LDraw 零件和模型导入 Blender 进行渲染。

[Code](https://github.com/TobyLobster/ImportLDraw)

> 搭建渲染流水线前先核对兼容的 Blender 版本。

<a id="bricknet-render"></a>

### BrickNet-Render

*2026*

将 LDraw 装配模型转换为 Blender 场景，用于批量渲染。

[Code](https://github.com/kulits/BrickNet-Render)

<a id="brick-renderer"></a>

### BrickRenderer

为 LDraw 零件渲染较真实的训练图像。

[Code](https://github.com/spencerhhubert/brick-renderer)

<a id="lego-training-renderer"></a>

### LegoTrainingRenderer

生成 LEGO 结构 RGB 图像、掩码和法线的 Blender／Python 工具。

[Code](https://github.com/WHSnyder/LegoTrainingRenderer)

<a id="vlmevalkit"></a>

### VLMEvalKit LEGO-Puzzles integration

通用多模态评测框架，LEGO-Puzzles 官方文档给出了 LEGO 数据集入口。

[Code](https://github.com/open-compass/VLMEvalKit) · [Integration reference](https://github.com/Tangkexian/LEGO-Puzzles)

<a id="videos"></a>

## 演讲与视频来源

<a id="europython"></a>

### Classifying LEGO Bricks with Machine Learning — Piotr Rybak

*2022*

EuroPython 演讲，涵盖数据构建、分类、检测与度量学习。

[Video](https://www.youtube.com/watch?v=bzyG4Wf1Nkc)

<a id="west-sorter"></a>

### The WORLD’S FIRST Universal LEGO Sorting Machine — Daniel West

*2019*

创作者展示基于 AI 的积木零件分拣机。

[Video](https://www.youtube.com/watch?v=04JkdHEX3Yk)

<a id="west-ai"></a>

### LEGO Sorter AI: How Does It Work? — Daniel West

*2019*

创作者解释分拣机背后的视觉识别流程。

[Video](https://www.youtube.com/watch?v=-UGl0ZOCgwQ)

<a id="austrianbrickfan"></a>

### AustrianBrickFan

搭建速录频道，可逐条筛选用于研究视觉搭建序列的视频。

[Channel](https://www.youtube.com/channel/UCuk26DMu7ewAkC-ntx7esiA)

> 用于观看和发现视频来源，不是已授权训练数据集；加速与剪辑可能隐藏动作。

<a id="applications"></a>

## 应用

<a id="brickognize"></a>

### Brickognize

视觉零件识别应用，作者演讲提供技术背景。

[App](https://brickognize.com/) · [Author talk](https://www.youtube.com/watch?v=bzyG4Wf1Nkc)

> JavaScript 应用；作为产品参考收录，不标作开放模型。

<a id="brickit"></a>

### Brickit

扫描散落积木，并依据识别出的库存推荐搭建方案。

[App](https://brickit.app/)

> 产品参考，不据此声称其训练数据已公开。

<a id="community"></a>

## 相关清单

<a id="awesome-ml"></a>

### Awesome LEGO Machine Learning

本仓库的结构参考，尤其是零件识别、分拣与渲染部分。

[List](https://github.com/360er0/awesome-lego-machine-learning)

<a id="awesome-general"></a>

### Awesome LEGO

覆盖 LEGO 软件与爱好者生态的综合社区索引。

[List](https://github.com/ad-si/awesome-lego)

<a id="awesome-robot"></a>

### Awesome Brick Assembly Robot Creativity

聚焦积木装配与机器人创造力的补充研究清单。

[List](https://github.com/intelligent-control-lab/Awesome-Brick-Assembly-Robot-Creativity)

<a id="research-videos"></a>

## 论文演示视频速查

以下为作者项目的演示入口；项目页中的嵌入视频与单独视频文件均已区分。

| Project | Video / demo |
| --- | --- |
| [DailyBrick: Language-Guided Synthesis of Brick Assembly Instructions](#dailybrick) | [Video](https://spatialagentlab.github.io/DailyBrick.github.io/assets/dailybrick-demo.mp4) |
| [Generating Physically Stable and Buildable Brick Structures from Text (BrickGPT / LegoGPT)](#brickgpt) | [Video page](https://avalovelace1.github.io/BrickGPT/) |
| [TreeSBA: Tree-Transformer for Self-Supervised Sequential Brick Assembly](#treesba) | [Video](https://dreamguo.github.io/projects/TreeSBA/resources/Assembly_Airplane.mp4) |
| [Legolization: Optimizing LEGO Designs](#legolization) | [Video](https://www.youtube.com/watch?v=Uv5gpqlkpis) |
| [Translating a Visual LEGO Manual to a Machine-Executable Plan (MEPNet)](#mepnet) | [Video](https://cs.stanford.edu/~rcwang/projects/lego_manual/resources/video.mp4) |
| [SCANet: Correcting LEGO Assembly Errors with Self-Correct Assembly Network](#scanet) | [Video](https://github.com/kaichen-z/SCANet-Supp/blob/master/assets/Final_2.mp4) |
| [WorkBenchMark: A LEGO-Based Assembly Benchmark with an Assembly-by-Disassembly Baseline for the Smart Manufacturing League](#workbenchmark) | [Video](https://workbenchmark.github.io/static/videos/demo.mp4) |
| [BrickSim: A Physics-Based Simulator for Manipulating Interlocking Brick Assemblies](#bricksim) | [Video](https://www.youtube.com/watch?v=VGuHfz4yxLU) |
| [APEX-MR: Multi-Robot Asynchronous Planning and Execution for Cooperative Assembly](#apex-mr) | [Project / video](https://intelligent-control-lab.github.io/APEX-MR/) |
| [Eye-in-Finger: Smart Fingers for Delicate Assembly and Disassembly of LEGO](#eye-in-finger) | [Lab / video](https://icontrol.ri.cmu.edu/research/lego.html) |
| [Robotic LEGO Assembly and Disassembly from Human Demonstration](#human-demonstration) | [Lab / video](https://icontrol.ri.cmu.edu/research/lego.html) |

## 收录与复用

本清单关注真实积木、结构和搭建过程；仅名称含 LEGO、但与积木无关的方法不作为核心资源。TPRU 属于包含 LEGO 子集的多领域数据，已明确标注。

视频可观看不等于可批量下载、训练或再分发；论文、代码、数据、CAD 零件库可能有不同许可，具体以原始发布页为准。本仓库仅提供索引和原创摘要。

结构参考并致谢 [360er0/awesome-lego-machine-learning](https://github.com/360er0/awesome-lego-machine-learning)。欢迎按 [贡献指南](CONTRIBUTING.md) 补充条目或修复链接。

LEGO® 是 LEGO Group 的商标。本清单为独立研究资源索引，与 LEGO Group 无隶属或背书关系。
