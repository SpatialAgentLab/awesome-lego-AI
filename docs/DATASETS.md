# Dataset matrix / 数据对照表

[Back to list](../README.md) · [返回中文版](../README.zh-CN.md)

Curated 2026-11-22. Counts refer to the named source version, not verified local downloads.

数据、基准、原始目录分别说明。`规模` 不代表可直接用于训练的独立样本量；不同条目可能共享原模型或视频，不能简单相加。

| Resource | Modality | Reported scale | Access / 获取状态 |
| --- | --- | --- | --- |
| [LEGO-Puzzles](../README.md#lego-puzzles) | Images + VQA / planning | Elementary: 1,100 questions / 11 tasks; Planning: see paper version | Hugging Face; match the downloaded release to the evaluated paper version.<br>Hugging Face；下载版本须与所采用论文版本对应。 |
| [TPRU-25k / TPRU-test](../README.md#tpru) | Frame sequences + temporal QA | 24,750 training examples across domains | Hugging Face; LEGO source: 36 Arvin Bricks stop-motion videos, as reported in the paper.<br>Hugging Face；论文注明 LEGO 源材料为 Arvin Bricks 的 36 个定格动画视频。 |
| [BC-Bench / Brick-Composer assets](../README.md#brick-composer) | Manual renders + brick selection + 6-DoF pose / trajectories | See release splits; designer supervision covers 102 human-designed objects | Hugging Face links in the official repository; confirm the benchmark split separately.<br>官方仓库提供 Hugging Face 入口；需单独确认 benchmark 的划分。 |
| [BrickBench prompts / runs](../README.md#brickbench) | Text prompts + generated assemblies / agent runs | 300 prompts across 3 settings | Prompts in BrickAgent; run artifacts on Hugging Face.<br>题目在 BrickAgent 仓库；运行产物在 Hugging Face。 |
| [BrickNet](../README.md#bricknet) | LDraw-derived graphs + build paths + captions | Paper: over 100,000 human-designed objects / scenes | Dataset access is gated by a request form; code and some part assets are public.<br>数据需要通过表单申请；代码和部分零件资产公开。 |
| [StableText2Brick (formerly StableText2Lego)](../README.md#brickgpt) | Brick sequences + text captions | Over 47,000 structures / over 28,000 unique objects | Hugging Face; official code links models and generation pipeline.<br>Hugging Face；官方代码仓库提供模型和生成流程入口。 |
| [Combinatorial 3D Shape Dataset](../README.md#combinatorial3d) | Primitive structures + generation scripts | See repository dataset directory | Dataset and generation scripts are included in the repository.<br>仓库内包含数据目录与生成脚本。 |
| [MEPNet LEGO manual datasets](../README.md#mepnet) | Manual images + 3D parts / poses | Three LEGO manual datasets; see paper | Repository links training, validation and evaluation archives on SharePoint; archives not downloaded here.<br>仓库链接 SharePoint 上的训练、验证与评测数据；本次未下载完整压缩包。 |
| [LTRON / Break and Make](../README.md#break-make) | LDraw models + interactive assembly environment | Complex models with over 1,000 distinct brick shapes in the paper | Install assets through LTRON; pin the release associated with the paper.<br>通过 LTRON 获取资产；固定与论文对应的版本。 |
| [LTRON procedural vehicles](../README.md#instructionet) | Procedural models + assembly / disassembly episodes | Average 31 bricks; over 100 disassembly/reassembly actions | Use LTRON v1.1.0 and the eccv-24 training branch.<br>使用 LTRON v1.1.0 与 eccv-24 训练分支。 |
| [LEGO-ECA](../README.md#scanet) | Manual images + erroneous assemblies / corrections | 1,429 manuals; approximately 120,000 incorrect examples | Official supplement repository links Google Drive / Baidu archives; not downloaded here.<br>官方补充仓库提供 Google Drive / 百度网盘；本次未下载完整数据。 |
| [StableLego](../README.md#stablelego) | Voxel grids + assembly JSON + stability scores | See upstream release | Download link in official repository; includes stable and unstable examples.<br>官方仓库提供下载入口，包含稳定与不稳定结构样本。 |
| [WorkBenchMark](../README.md#workbenchmark) | YAML task specifications + hidden ground truth | 400 tasks / 4 difficulty tiers | Task files are public; do not expose ground_truth to the solver.<br>任务文件已公开；ground_truth 仅供评测，不能作为求解器输入。 |
| [MobileBrick](../README.md#mobilebrick) | RGB-D + camera poses + masks + ground-truth mesh | 153 sequences: 135 training + 18 evaluation | Download via official project / repository; reconstruction data, not an assembly-action corpus.<br>通过官方项目页／仓库下载；这是重建数据，并非装配动作语料。 |
| [BrickFlow](../README.md#brickflow) | Procedural assemblies + image-conditioned reconstruction data | See Hugging Face release | Data and model entry points are linked by the official project.<br>官方项目链接数据与模型入口。 |
| [Photos and rendered images of LEGO bricks](../README.md#photos-renders) | Real photos + renders + part labels / detection subsets | Approximately 155,000 photos + 1.5 million renders across the collection | Follow the individual dataset DOIs in the paper; Most Wiedzy may require a normal browser challenge.<br>按论文中各子数据集 DOI 获取；Most Wiedzy 可能需要浏览器验证。 |
| [B200C](../README.md#b200c) | Synthetic RGB part images | 800,000 images / 200 classes / 64×64 | Author-linked Kaggle page; current download availability not confirmed.<br>作者提供 Kaggle 链接；当前能否下载尚未确认。 |
| [Conveyor-belt videos](../README.md#conveyor) | Real video | Multiple dataset records; see catalog | Institutional catalog; browser verification may be required.<br>机构目录，可能需要浏览器验证。 |
| [Lego Project Data Archive](../README.md#lego-video-archive) | Audio + video + ancillary material | See archive records | University record links Zenodo; designed for interaction research, not brick-pose labels.<br>大学记录链接 Zenodo；用于交互研究，不提供逐砖位姿标注的保证。 |
| [LDraw OMR](../README.md#ldraw-omr) | LDR / MPD models | Growing community catalog | Browse model records and per-file terms; models are not automatically validated action trajectories.<br>按模型记录和文件条款使用；模型不自动等于已验证动作轨迹。 |
| [Rebrickable catalog](../README.md#rebrickable) | Tabular metadata / API | Continuously updated | Catalog / API, not an annotated vision dataset.<br>目录／API，并非带标注的视觉数据集。 |
| [Official building instructions](../README.md#lego-instructions) | PDF manuals | Continuously updated | Official lookup portal; public viewing is separate from redistribution or training permission.<br>官方检索入口；公开阅读与再分发／训练授权应分开确认。 |

## Choosing data / 如何选用

- **Spatial / temporal QA:** LEGO-Puzzles; the LEGO subset of TPRU. Keep the multi-domain totals separate.
- **Manual-to-action / correction:** MEPNet, LEGO-ECA and BC-Bench assets.
- **Text-to-structure:** StableText2Brick, BrickNet (request access), and BrickBench prompts / runs.
- **Image-to-structure:** MobileBrick for geometry reconstruction; BrickFlow for part-pose assembly.
- **Interaction / robotics:** LTRON and WorkBenchMark; BrickSim supplies a simulator rather than a generic labeled video corpus.
- **Recognition:** B200C and the photos/renders collection; conveyor videos offer real motion but not assembly sequences.

## Practical notes / 实验前检查

1. 保存原始数据版本、下载日期和许可文本；代码仓库许可不自动覆盖外链数据。此表没有把未核实的许可标作“可商用”。
2. 训练／测试优先按套装、完整模型或源视频划分，避免相邻步骤和不同渲染视角跨集合泄漏。
3. 统一零件 ID、颜色、坐标轴、长度单位和旋转约定；保留原始 ID 到规范 ID 的映射。
4. 区分最终结构合法、每步可搭建、机器人可达、真实执行成功。只检查碰撞不能替代全部指标。
5. 视频来源应记录作者、原 URL、套装编号、剪辑／加速、许可和标注状态；不要从频道总视频数推算可用训练规模。

## Known access limitations / 已知限制

- BrickNet: the full dataset uses an author request form. The public CAD assets are a separate download.
- LEGO Co-builder: an author-linked repository was found, but packaging and reproducibility remain unclear; not counted as a confirmed downloadable dataset here.
- Arvin Bricks: TPRU identifies this source, but this review did not resolve a reliable canonical channel URL or the 36-video manifest. No channel URL is guessed.
- Most Wiedzy / Rebrickable: automated access was restricted. Use the original catalog / paper links and check through a normal browser.
- Remote archives and model weights were not downloaded or executed in this curation task.
