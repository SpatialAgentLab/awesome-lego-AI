# 🧱 Awesome LEGO AI

[English](README.md) | [简体中文](README.zh-CN.md)

A curated research list for **LEGO / interlocking bricks × AI**: spatial and temporal reasoning, visual manuals, 3D generation, assembly planning, and robot execution.

Last curated: **2026-11-22**. **54 unique entries**, including **30 papers** and **22 data / benchmark entries**. A project may provide several artifact types; these counts overlap.

We prioritize original papers, author project pages, official repositories and dataset records. Years generally indicate the first preprint, with publication venues listed separately. Descriptions are original summaries. Link review does not imply successful reproduction or complete dataset download.

**Start here:** [Dataset matrix](docs/DATASETS.md) · [Chinese research guide](docs/RESEARCH_GUIDE.zh-CN.md) · [BibTeX](papers.bib) · [Machine-readable catalog](data/resources.json) · [Verification notes](docs/VERIFICATION.md)

## Start here

| Goal | Suggested reading |
| --- | --- |
| Multimodal spatial / temporal reasoning | [LEGO-Puzzles](#lego-puzzles) → [TPRU](#tpru) → [Brick-Composer](#brick-composer) |
| Text-to-buildable design | [BrickGPT](#brickgpt) → [BrickNet](#bricknet) → [BrickBench](#brickbench) / [BrickWright](#brickwright) / [DailyBrick](#dailybrick) |
| Manuals, actions and correction | [MEPNet](#mepnet) → [SCANet](#scanet) → [InstructioNet](#instructionet) |
| 3D reconstruction | [MobileBrick](#mobilebrick) → [BrickFlow](#brickflow) |
| Real robots | [StableLego](#stablelego) → [BrickSim](#bricksim) → [WorkBenchMark](#workbenchmark) |

## Contents

- [Spatial and procedural reasoning](#reasoning)
- [Generative design and brickification](#generation)
- [Manual understanding and assembly planning](#assembly)
- [Robotics, physics and simulation](#robotics)
- [Recognition and 3D reconstruction](#perception)
- [Additional data sources](#data)
- [CAD, rendering and evaluation tools](#tools)
- [Talks and video sources](#videos)
- [Applications](#applications)
- [Related lists](#community)
- [Research demo videos](#research-videos)

[Contributing](CONTRIBUTING.md) · [Publishing to GitHub](docs/PUBLISHING.md)

<a id="reasoning"></a>

## Spatial and procedural reasoning

<a id="lego-puzzles"></a>

### LEGO-Puzzles: How Good Are MLLMs at Multi-Step Spatial Reasoning?

*2025 · arXiv; revised 2026*

Tests spatial understanding and multi-step assembly planning. A natural starting evaluation for MLLMs.

[Paper](https://arxiv.org/abs/2503.19990) · [Code](https://github.com/Tangkexian/LEGO-Puzzles) · [Data](https://huggingface.co/datasets/KexianTang/LEGO-Puzzles) · [Project](https://tangkexian.github.io/LEGO-Puzzles/)

<a id="tpru"></a>

### TPRU: Advancing Temporal and Procedural Understanding in Large Multimodal Models

*2026 · ICLR 2026*

Multi-domain temporal reasoning with a LEGO assembly subset; studies ordering, next-frame prediction and previous-frame review.

[Paper](https://arxiv.org/abs/2602.18884) · [Code](https://github.com/Stephen-gzk/TPRU) · [Data](https://huggingface.co/datasets/Stephengzk/TPRU-25k) · [Test](https://huggingface.co/datasets/Stephengzk/TPRU-test)

> The 24,750 training examples are the full multi-domain set, not 24,750 LEGO examples.

<a id="co-builder"></a>

### LEGO Co-builder: Exploring Fine-Grained Vision-Language Modeling for Multimodal LEGO Assembly Assistants

*2025 · arXiv; revised 2026*

Studies fine-grained instruction following and state recognition in stepwise LEGO scenes.

[Paper](https://arxiv.org/abs/2507.05515) · [Code](https://github.com/peterhuang-coding/LEGO-Co-builder)

> Author-linked repository exists, but its README is minimal; dataset packaging and reproduction steps need clarification.

<a id="brick-composer"></a>

### Brick-Composer: Using MLLMs for Assembly with Diverse Bricks

*2026 · arXiv*

BC-Bench separates brick selection from pose prediction; training combines human designs, simulator feedback and synthetic trajectories.

[Paper](https://arxiv.org/abs/2606.05445) · [Code](https://github.com/Lumos-Jiateng/Brick-Composer) · [Project](https://lumos-jiateng.github.io/Brick-Composer/) · [Data](https://huggingface.co/datasets/Lumos-Jiateng/brick_synthetic) · [Design data](https://huggingface.co/datasets/Lumos-Jiateng/bricklink_lego_design)

> Repository title: “MLLMs Construct Everything from Building Blocks”; this is the same project, not a second paper.

<a id="brickbench"></a>

### BrickBench: Evaluating Agentic Brick Design

*2026 · arXiv*

Evaluates text-guided coding agents under model, full-set and fixed-inventory building constraints.

[Paper](https://arxiv.org/abs/2610.12452) · [Project](https://brickben.ch/) · [Code](https://github.com/kulits/BrickAgent) · [Data](https://huggingface.co/datasets/kulits/BrickBench-Runs) · [Gallery](https://gallery.brickben.ch/)

<a id="generation"></a>

## Generative design and brickification

<a id="dailybrick"></a>

### DailyBrick: Language-Guided Synthesis of Brick Assembly Instructions

*2026 · arXiv*

An agentic pipeline generates a brick model and executable stepwise assembly instructions, with review and repair.

[Paper](https://arxiv.org/abs/2611.22132) · [Project](https://spatialagentlab.github.io/DailyBrick.github.io/) · [Video](https://spatialagentlab.github.io/DailyBrick.github.io/assets/dailybrick-demo.mp4)

> SpatialAgentLab project. The public website repository is not a verified implementation or dataset release.

<a id="brickwright"></a>

### BrickWright: Agentic Creation of Physically Feasible Brick Builds

*2026 · arXiv*

Equips pretrained agents with the BrickLayer assembly API and a physical-feasibility validator.

[Paper](https://arxiv.org/abs/2610.31651) · [Project](https://avalovelace1.github.io/brickwright/) · [Code](https://github.com/AvaLovelace1/brickwright)

> Its validator-defined feasibility should not be equated with proof of arbitrary real-robot executability.

<a id="bricknet"></a>

### BrickNet: Graph-Backed Generative Brick Assembly

*2026 · CVPR 2026*

Generates assemblies using connectivity-based representations over diverse real part types.

[Paper](https://arxiv.org/abs/2604.22984) · [Project](https://kulits.github.io/BrickNet/) · [Code](https://github.com/kulits/BrickNet) · [Data request](https://forms.gle/dm4eYSa5gh4DqzRT6) · [Data documentation](https://github.com/kulits/BrickNet/blob/master/DATA.md)

<a id="brickgpt"></a>

### Generating Physically Stable and Buildable Brick Structures from Text (BrickGPT / LegoGPT)

*2025 · ICCV 2025*

Autoregressive text-to-brick generation with validity checks and physics-aware rollback.

[Paper](https://arxiv.org/abs/2505.05469) · [Project](https://avalovelace1.github.io/BrickGPT/) · [Code](https://github.com/AvaLovelace1/BrickGPT) · [Data](https://huggingface.co/datasets/AvaLovelace/StableText2Brick) · [Video page](https://avalovelace1.github.io/BrickGPT/)

> LegoGPT / StableText2Lego are earlier names of BrickGPT / StableText2Brick; do not double-count them.

<a id="treesba"></a>

### TreeSBA: Tree-Transformer for Self-Supervised Sequential Brick Assembly

*2024 · ECCV 2024*

Uses a tree representation and silhouette self-supervision to infer assembly sequences from multiview images.

[Paper](https://arxiv.org/abs/2407.15648) · [Project](https://dreamguo.github.io/projects/TreeSBA/) · [Code](https://github.com/dreamguo/TreeSBA) · [Video](https://dreamguo.github.io/projects/TreeSBA/resources/Assembly_Airplane.mp4)

<a id="brick-by-brick"></a>

### Brick-by-Brick: Combinatorial Construction with Deep Reinforcement Learning

*2021 · NeurIPS 2021*

Learns sequential brick placement from target images while filtering invalid actions.

[Paper](https://arxiv.org/abs/2110.15481) · [Code](https://github.com/POSTECH-CVLab/Brick-by-Brick)

<a id="image2lego"></a>

### Image2Lego: Customized LEGO Set Generation from Images

*2021 · arXiv*

Reconstructs a voxel representation from an image, then converts it into a brick layout and instructions.

[Paper](https://arxiv.org/abs/2108.08477)

<a id="graph-lego"></a>

### Building LEGO Using Deep Generative Models of Graphs

*2020 · NeurIPS 2020 ML4Eng workshop*

An early graph-generative approach to learning brick structures from human designs.

[Paper](https://arxiv.org/abs/2012.11543)

<a id="combinatorial3d"></a>

### Combinatorial 3D Shape Generation via Sequential Assembly

*2020 · NeurIPS 2020 ML4Eng workshop*

Uses Bayesian optimization to choose sequential placements under geometric and stability objectives.

[Paper](https://arxiv.org/abs/2004.07414) · [Code](https://github.com/POSTECH-CVLab/Combinatorial-3D-Shape-Generation)

<a id="legolization"></a>

### Legolization: Optimizing LEGO Designs

*2015 · ACM TOG / SIGGRAPH Asia 2015*

Optimizes brick layouts using force-based stability analysis; foundational geometry-to-brick work.

[Paper](https://www.cs.columbia.edu/~yonghao/siga15/luo-Legolization.pdf) · [Video](https://www.youtube.com/watch?v=Uv5gpqlkpis)

<a id="assembly"></a>

## Manual understanding and assembly planning

<a id="mepnet"></a>

### Translating a Visual LEGO Manual to a Machine-Executable Plan (MEPNet)

*2022 · ECCV 2022*

Recovers component poses and assembly steps from illustrated manuals.

[Paper](https://arxiv.org/abs/2207.12572) · [Project](https://cs.stanford.edu/~rcwang/projects/lego_manual/) · [Code](https://github.com/Relento/lego_release) · [Data instructions](https://github.com/Relento/lego_release#evaluation) · [Video](https://cs.stanford.edu/~rcwang/projects/lego_manual/resources/video.mp4)

<a id="break-make"></a>

### Break and Make: Interactive Structural Understanding Using LEGO Bricks

*2022 · ECCV 2022*

Introduces LTRON: inspect and disassemble a structure, then reconstruct it through low-level actions.

[Paper](https://arxiv.org/abs/2207.13738) · [Code / simulator](https://github.com/aaronwalsman/ltron) · [Training](https://github.com/aaronwalsman/ltron-torch)

> Use the paper-specific release; the master README warns about unstable development and non-public dependencies.

<a id="instructionet"></a>

### Learning to Build by Building Your Own Instructions (InstructioNet)

*2024 · ECCV 2024*

Stores visual instructions during disassembly to support longer-horizon reconstruction.

[Paper](https://arxiv.org/abs/2410.01111) · [Environment / data](https://github.com/aaronwalsman/ltron/tree/v1.1.0) · [Training](https://github.com/aaronwalsman/ltron-torch/tree/eccv-24)

<a id="scanet"></a>

### SCANet: Correcting LEGO Assembly Errors with Self-Correct Assembly Network

*2024 · IROS 2024*

Detects incorrect components and predicts assembly corrections from manual images.

[Paper](https://arxiv.org/abs/2403.18195) · [Data instructions](https://github.com/kaichen-z/SCANet-Supp) · [Video](https://github.com/kaichen-z/SCANet-Supp/blob/master/assets/Final_2.mp4)

> The former project website returned 404; use the official supplement repository and video. Its README Code link points to an MP4, so it is not counted as a verified implementation.

<a id="graph-asp"></a>

### Planning Assembly Sequence with Graph Transformer

*2022 · arXiv*

Represents LEGO assemblies as heterogeneous graphs and predicts construction order.

[Paper](https://arxiv.org/abs/2210.05236)

<a id="physics-asp"></a>

### Physics-Aware Combinatorial Assembly Sequence Planning using Data-free Action Masking

*2024 · IEEE RA-L 2025*

Reinforcement learning with online physical action masks for executable construction plans.

[Paper](https://arxiv.org/abs/2408.10162) · [Code](https://github.com/intelligent-control-lab/PhysicsAwareCombinatorialASP)

<a id="robotics"></a>

## Robotics, physics and simulation

<a id="stablelego"></a>

### StableLego: Stability Analysis of Block Stacking Assembly

*2024 · IEEE RA-L 2024*

Analyzes force balance and structural stability; useful for evaluating generated designs.

[Paper](https://arxiv.org/abs/2402.10711) · [Code / data](https://github.com/intelligent-control-lab/StableLego)

> The implementation uses Gurobi; code availability alone does not guarantee a ready-to-run environment.

<a id="workbenchmark"></a>

### WorkBenchMark: A LEGO-Based Assembly Benchmark with an Assembly-by-Disassembly Baseline for the Smart Manufacturing League

*2026 · RoboCup Symposium 2026*

A Duplo assembly benchmark connecting perception, symbolic planning and manipulation.

[Paper](https://arxiv.org/abs/2606.19358) · [Project](https://workbenchmark.github.io/) · [Data](https://github.com/WorkBenchMark/dataset) · [Video](https://workbenchmark.github.io/static/videos/demo.mp4)

<a id="bricksim"></a>

### BrickSim: A Physics-Based Simulator for Manipulating Interlocking Brick Assemblies

*2026 · arXiv*

Simulates interlocking brick manipulation; a useful environment for assembly, disassembly and teleoperation.

[Paper](https://arxiv.org/abs/2603.16853) · [Code](https://github.com/intelligent-control-lab/BrickSim) · [Project](https://intelligent-control-lab.github.io/BrickSim/) · [Video](https://www.youtube.com/watch?v=VGuHfz4yxLU)

> Current upstream quickstart targets x86-64 Linux and NVIDIA / Isaac Sim. No local simulator installation was attempted.

<a id="apex-mr"></a>

### APEX-MR: Multi-Robot Asynchronous Planning and Execution for Cooperative Assembly

*2025 · RSS 2025*

Coordinates multiple robots asynchronously for cooperative assembly.

[Paper](https://arxiv.org/abs/2503.15836) · [Project / video](https://intelligent-control-lab.github.io/APEX-MR/)

<a id="eye-in-finger"></a>

### Eye-in-Finger: Smart Fingers for Delicate Assembly and Disassembly of LEGO

*2025 · IROS 2025*

Studies sensor-equipped fingers for precise brick insertion and removal.

[Paper](https://arxiv.org/abs/2503.06848) · [Lab / video](https://icontrol.ri.cmu.edu/research/lego.html)

<a id="human-demonstration"></a>

### Robotic LEGO Assembly and Disassembly from Human Demonstration

*2023 · arXiv*

Learns assembly and disassembly from demonstrations and validates execution using a digital twin.

[Paper](https://arxiv.org/abs/2305.15667) · [Lab / video](https://icontrol.ri.cmu.edu/research/lego.html)

<a id="perception"></a>

## Recognition and 3D reconstruction

<a id="mobilebrick"></a>

### MobileBrick: Building LEGO for 3D Reconstruction on Mobile Devices

*2023 · CVPR 2023*

Mobile RGB-D observations paired with precise geometry for fine-scale reconstruction.

[Paper](https://arxiv.org/abs/2303.01932) · [Code / data](https://github.com/ActiveVisionLab/MobileBrick) · [Project](https://code.active.vision/MobileBrick/)

<a id="brickflow"></a>

### BrickFlow: Connectivity-Guided Brick Reconstruction

*2026 · NeurIPS 2026*

Infers part poses from an image and a given part inventory using SE(3) flow and connectivity guidance.

[Paper](https://arxiv.org/abs/2611.17321) · [Project](https://kulits.github.io/BrickFlow/) · [Code](https://github.com/kulits/BrickFlow) · [Data](https://huggingface.co/datasets/kulits/BrickFlow) · [Models](https://huggingface.co/kulits/BrickFlow)

<a id="photos-renders"></a>

### Photos and rendered images of LEGO bricks

*2023 · Scientific Data*

A data descriptor for real and synthetic part images, with part identity and category labels.

[Paper](https://www.nature.com/articles/s41597-023-02682-2) · [Full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC10657460/)

<a id="data"></a>

## Additional data sources

<a id="b200c"></a>

### B200C LEGO Classification Dataset

*2021*

Synthetic part-classification images with randomized context, lighting and occlusions.

[Code / documentation](https://github.com/korra-pickell/LEGO-Classification-Dataset) · [Data](https://www.kaggle.com/datasets/ronanpickell/b200c-lego-classification-dataset)

> The author repository documents the dataset, but the Kaggle URL returned 404 to HEAD and only a script-rendered shell in the web reader; download availability remains unresolved.

<a id="conveyor"></a>

### Video of LEGO bricks on conveyor belt

*2022*

Real conveyor-belt videos for part recognition and sorting research.

[Data](https://mostwiedzy.pl/en/open-research-data-series/video-of-lego-bricks-on-conveyor-belt,202011132226557715481-0/catalog) · [Descriptor](https://mostwiedzy.pl/pl/publication/download/1/video-of-lego-bricks-on-conveyor-belt-dataset-series_71732.pdf)

> Automated access met an anti-bot page during this review; download availability was not confirmed.

<a id="lego-video-archive"></a>

### Lego Project Data Archive

*2020*

Research archive of collaborative LEGO puzzle activity with audiovisual and 360-degree material.

[Data record](https://vbn.aau.dk/en/datasets/lego-project-data-archive/)

<a id="ldraw-omr"></a>

### LDraw Official Model Repository (OMR)

Community reconstructions of LEGO sets in an interoperable CAD format.

[Models](https://library.ldraw.org/omr)

<a id="rebrickable"></a>

### Rebrickable downloads and API

Structured part, color, set and inventory metadata for joining CAD, manuals and video set IDs.

[Downloads](https://rebrickable.com/downloads/) · [API](https://rebrickable.com/api/)

> Automated browser access was blocked during review; download endpoints and current terms need a manual check.

<a id="lego-instructions"></a>

### LEGO official building instructions

Set-number lookup for original instruction booklets and step references.

[Instructions](https://www.lego.com/en-us/service/building-instructions)

<a id="tools"></a>

## CAD, rendering and evaluation tools

<a id="ldraw"></a>

### LDraw parts library and file format

Core geometry and interchange format for digital brick pipelines.

[Website](https://www.ldraw.org/) · [Library](https://library.ldraw.org/)

<a id="leocad"></a>

### LeoCAD

Open-source LDraw-compatible editor for creating and inspecting brick models.

[Website](https://www.leocad.org/) · [Code](https://github.com/leozide/leocad)

<a id="studio"></a>

### BrickLink Studio

Desktop brick-design tool and instruction authoring ecosystem.

[Website](https://www.bricklink.com/v3/studio/download.page)

> The site redirected to a maintenance notice on 2026-11-22. Recheck before installation.

<a id="lpub3d"></a>

### LPub3D

Creates LEGO-style digital building instructions from LDraw models.

[Code](https://github.com/trevorsandy/lpub3d)

<a id="importldraw"></a>

### ImportLDraw for Blender

Imports LDraw parts and models into Blender for rendering.

[Code](https://github.com/TobyLobster/ImportLDraw)

> Check supported Blender versions before building a rendering pipeline.

<a id="bricknet-render"></a>

### BrickNet-Render

*2026*

Converts LDraw assemblies into Blender scenes for batch rendering.

[Code](https://github.com/kulits/BrickNet-Render)

<a id="brick-renderer"></a>

### BrickRenderer

Renders realistic training images of individual LDraw pieces.

[Code](https://github.com/spencerhhubert/brick-renderer)

<a id="lego-training-renderer"></a>

### LegoTrainingRenderer

Blender/Python utilities for RGB renders, masks and normals of LEGO structures.

[Code](https://github.com/WHSnyder/LegoTrainingRenderer)

<a id="vlmevalkit"></a>

### VLMEvalKit LEGO-Puzzles integration

A common evaluation harness; LEGO-Puzzles documents its LEGO dataset entry.

[Code](https://github.com/open-compass/VLMEvalKit) · [Integration reference](https://github.com/Tangkexian/LEGO-Puzzles)

<a id="videos"></a>

## Talks and video sources

<a id="europython"></a>

### Classifying LEGO Bricks with Machine Learning — Piotr Rybak

*2022*

EuroPython talk covering dataset construction, classification, detection and metric learning.

[Video](https://www.youtube.com/watch?v=bzyG4Wf1Nkc)

<a id="west-sorter"></a>

### The WORLD’S FIRST Universal LEGO Sorting Machine — Daniel West

*2019*

Creator demonstration of an AI-based part sorter.

[Video](https://www.youtube.com/watch?v=04JkdHEX3Yk)

<a id="west-ai"></a>

### LEGO Sorter AI: How Does It Work? — Daniel West

*2019*

Creator explanation of the visual-recognition pipeline behind the sorter.

[Video](https://www.youtube.com/watch?v=-UGl0ZOCgwQ)

<a id="austrianbrickfan"></a>

### AustrianBrickFan

Speed-build channel: a candidate source for studying visual construction sequences, after checking each video.

[Channel](https://www.youtube.com/channel/UCuk26DMu7ewAkC-ntx7esiA)

> A viewing/source-discovery link, not a pre-cleared training dataset. Speedups and edits can hide actions.

<a id="applications"></a>

## Applications

<a id="brickognize"></a>

### Brickognize

Visual part identification application; the author talk provides technical context.

[App](https://brickognize.com/) · [Author talk](https://www.youtube.com/watch?v=bzyG4Wf1Nkc)

> JavaScript application; included as a product reference, not an open model release.

<a id="brickit"></a>

### Brickit

Scans a pile of bricks and proposes builds using the observed inventory.

[App](https://brickit.app/)

> Product reference; no public training-data release is asserted.

<a id="community"></a>

## Related lists

<a id="awesome-ml"></a>

### Awesome LEGO Machine Learning

The inspiration for this list, especially its recognition, sorting and rendering coverage.

[List](https://github.com/360er0/awesome-lego-machine-learning)

<a id="awesome-general"></a>

### Awesome LEGO

A broader community index covering the LEGO software and hobby ecosystem.

[List](https://github.com/ad-si/awesome-lego)

<a id="awesome-robot"></a>

### Awesome Brick Assembly Robot Creativity

A complementary research list focused on brick assembly and robotic creativity.

[List](https://github.com/intelligent-control-lab/Awesome-Brick-Assembly-Robot-Creativity)

<a id="research-videos"></a>

## Research demo videos

Author demonstrations, distinguishing direct videos from pages containing embedded media.

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

## Curation and reuse

The core scope is actual bricks, their geometry and the construction process. Unrelated methods merely named LEGO are excluded. Multi-domain resources such as TPRU are explicitly identified.

Public video viewing is not a grant of bulk-download, training or redistribution rights. Papers, software, datasets and CAD assets can carry different licenses; consult the original release. This repository contains links and original descriptions only.

Inspired by and with thanks to [360er0/awesome-lego-machine-learning](https://github.com/360er0/awesome-lego-machine-learning). See [Contributing](CONTRIBUTING.md) for additions and corrections.

LEGO® is a trademark of the LEGO Group. This independent research index is not affiliated with or endorsed by the LEGO Group.
