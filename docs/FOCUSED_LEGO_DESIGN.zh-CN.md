# LEGO 功能设计 Agent 研究指南

[English](FOCUSED_LEGO_DESIGN.md) · [返回完整清单](../README.zh-CN.md)
资料核对日期：**2026-11-23** · 20 项重点资源，另附 1 项观察名单

**研究问题：AI 能否使用设计软件，构建满足功能要求的 LEGO 零件系统，并验证它能装起来、能按要求工作？**

例如，我们给 AI 一盒 Technic 零件，要求：“输入轴转三圈，输出轴反向转一圈；整个机构不能超过指定尺寸。”AI 需要选齿轮、放轴、搭支撑，在软件里检查并修改，最后交付模型、装配步骤和功能测试结果。这里的 Agent，就是能连续调用工具、查看反馈、修改设计的 AI。

这份指南围绕 **LEGO，尤其是 Technic 的齿轮、轴、梁、销和连杆机构**。功能要能测量，例如转动方向、转速比例、升降距离或末端轨迹。只涉及外观生成、通用 CAD 或家具装配的资源不作为本专题重点。

第一次阅读，建议先看六项：[Nova](#nova)（AI 怎么搭）、[Mecha](#mecha)（机构怎么动）、[BrickWright](#brickwright)（怎么用检查反馈改错）、[BrickBench](#brickbench)（怎么评测 Agent）、[ComputeTechnic](#computetechnic)（已有的 Technic 自动设计）、[ReLink](#relink)（按目标运动反推连杆设计）。

导航：[数据与 benchmark](#data) · [Agent](#agents) · [机构设计](#mechanisms) · [设计软件](#editors) · [验证与实测](#verification) · [零件与素材](#assets) · [研究起点](#roadmap)

## 先分清：什么叫“设计成功”？

| 层次 | 通俗解释 | 不能据此直接得出的结论 |
| --- | --- | --- |
| 几何与连接正确 | 零件没有明显穿透，连接位置和类型正确。 | 最终位置合法，不代表零件有路径插进去。 |
| 能装起来 | 存在合理顺序，轴、销和梁能逐步装到位。 | 人能装，不代表指定机器人也能装。 |
| 运动符合要求 | 输入转动后，输出方向、比例、行程或轨迹正确；这叫运动学。 | 动画能动，不代表电机带得动或带负载不卡住。 |
| 受力或实物测试通过 | 考虑摩擦、重力、负载等，或者实际搭起来测试；这涉及动力学和实物验证。 | 一个样例成功，不代表换库存、尺寸或负载仍然成功。 |

这四类结果应分开报告。现有工具各自覆盖其中一部分；下文的“适合怎么用”是研究建议，不代表工具已经实现完整流程。

<a id="data"></a>
## 数据最重要：哪些拿来就能用，哪些还需要整理？

**训练集**是给模型学习的例子；**benchmark**是一套用来考试的任务和评分规则；**生成器**是能继续造例子的程序；**素材库**则提供零件、模型或视频，通常还没有我们需要的功能标签。它们不能混为一谈。

| 资源入口 | 当前能拿到什么 | 对本研究的价值与限制 |
| --- | --- | --- |
| [BrickBench / BrickAgent](https://github.com/kulits/BrickAgent) | Model、Set、Alt-Build 各 100 个任务，共 300 个；环境和评测代码。 | 可先评测 Agent 使用 LEGO 工具的能力；需另加齿轮、连杆等功能题与评分。 |
| [Nova 机构案例](https://github.com/anteloc/ldraw-nova/tree/master/examples/mechanism-atlas) | 机构案例和设计参考；仓库另有构建计划与脚本。 | 可整理成“搭建—检查—修正”任务；不是已经划好训练／测试集的操作轨迹数据。 |
| [Mecha 案例档案](https://github.com/anteloc/ldraw-mecha/blob/master/examples/README.md) | 传动、转向、发动机、悬挂等模型、计划、检查记录与 Blender 资产。 | 适合从现成机构提取运动理解题；部分资产需 Git LFS，不等于独立 benchmark。 |
| [ComputeTechnic 案例](https://github.com/xuhaocuhk/ComputeTechnic/tree/main/LEGO_Technic_data) | 配套案例目录，包括风扇、升降机构、机械臂等。 | 适合研究零件和连接表示；需要整理功能描述、有效样本和划分，不能把目录数当样本数。 |
| [ReLink 目标曲线](https://github.com/ETHZ-EDAC/ReLink/tree/main/assets/curves) | 7 个 `.npy` 曲线文件；仓库提供机构生成与优化代码。 | 很适合做“让末端沿这条线移动”的任务。运行生成器后才能得到更多机构，不应称为已下载的大规模训练集。 |
| [TechnicSimulation 最小测试模型](https://github.com/yoff/LegoTechnicSimulation/blob/main/tests/fixtures/README.md) | 摩擦销、无摩擦销、齿轮、电机等小模型及预期结果。 | 适合先检验验证器是否认对连接和运动；规模属于工程测试样例。 |
| [LDCad Shadow Library](https://github.com/RolandMelkert/LDCadShadowLibrary) | 部分零件的吸附／连接位置等元数据。 | 可以减少手工标连接点的工作；覆盖不完整，也没有完整受力参数。 |
| [LDraw OMR](https://library.ldraw.org/omr) | 社区整理的官方套装数字模型。 | 可筛选 Technic 模型作原始素材；通常还需补关节、功能目标和测试标签。 |
| [Philo 电机测量](https://www.philohome.com/motors/motorcomp.htm) / [BEC 零件测量](https://brickexperimentchannel.wordpress.com/2023/11/15/characteristics-of-lego-parts/) | 电机或零件的实测表格、曲线和实验说明。 | 可辅助设定合理负载与性能范围；需要人工整理并保留测量条件，不是现成训练集。 |

**目前核对的资源中，尚未确认一个完整覆盖“功能需求 → 软件操作 → 失败与修改 → 装配验证 → 功能实测”的统一公开数据集。** 这是值得做数据工作的地方，但不能仅凭这轮检索宣称不存在其他数据集。

整理数据时，保留原始来源、许可、零件版本和机构家族。建议按原套装、机构结构或家族划分训练与测试，而不是把同一个机构换颜色、换视角后分到两边。代码许可证也不自动覆盖上游模型、零件库和视频。

<a id="agents"></a>
## 一、让 AI 在软件里搭建、检查、修改

<a id="nova"></a>
### 1. LDraw Nova — 很贴近“会用工具的 LEGO 设计助手”

**是什么：** 面向 Agent 的 LEGO 建模工具，支持查真实零件、写设计计划、生成 LDraw 模型、渲染和修改。LDraw 是 LEGO 数字模型常用格式；MPD 可以把多个子模型放在一个文件里。

**适合怎么用：** 作为设计端候选，让 AI 从功能要求开始搭机构；参考其 Technic 检查，研究 AI 能否根据齿轮间距、轴支撑或输入锁死等反馈改错。

**能拿到什么：** 代码、Agent 工作流说明、机构案例。**边界：** 检查通过不证明所有零件都有插入路径，也不证明强度和真实配合可靠；需阅读具体检查覆盖范围。代码标注 AGPL-3.0。

[代码](https://github.com/anteloc/ldraw-nova) · [机构工作流](https://github.com/anteloc/ldraw-nova/blob/master/docs/agent/guides/mechanisms.md) · [验证范围](https://github.com/anteloc/ldraw-nova/blob/master/docs/agent/reference/validation.md)

<a id="mecha"></a>
### 2. LDraw Mecha — 把静态 LEGO 模型变成可检查的运动机构

**是什么：** 从已有 MPD 模型推断机构，生成运动计划和 Blender 动画控制结构，并检查传动比、杆长、闭环和采样姿态。

**适合怎么用：** 用来研究“AI 是否看懂这套零件怎么动”，以及设计修改前后的运动是否符合目标。它与 Nova 都值得优先读代码，因为已有工作与本课题相当接近。

**能拿到什么：** 代码、教程视频、保存的机构案例和检查记录。**边界：** 它没有完整的受力物理模拟；动画不能代替重力、惯性、摩擦和负载测试。部分案例资产需 Git LFS；代码标注 AGPL-3.0。

[代码与教程](https://github.com/anteloc/ldraw-mecha) · [验证说明](https://github.com/anteloc/ldraw-mecha/blob/master/docs/validation.md) · [案例说明](https://github.com/anteloc/ldraw-mecha/blob/master/examples/README.md)

<a id="brickwright"></a>
### 3. BrickWright / BrickLayer — 让 AI 边写搭建代码边检查

**是什么：** 2026 年工作。AI 用 Python 的 BrickLayer 工具搭建 LEGO，并接收真实零件、碰撞、悬空和连接等检查反馈。

**适合怎么用：** 参考其“写代码—检查—修改”过程，比较有反馈和没有反馈时 AI 的表现；也可作为设计工具候选。

**能拿到什么：** 论文、Agent 代码、BrickLayer SDK 和 LDraw 导出功能。**边界：** 这里的结构合法性不等于齿轮能传动、机构能承载。接入 Technic 功能任务前，要先核对零件和连接覆盖。SDK 及上游零件数据的许可需要分别处理。

[论文](https://arxiv.org/abs/2610.31651) · [代码](https://github.com/AvaLovelace1/brickwright) · [BrickLayer SDK](https://github.com/AvaLovelace1/brickwright/tree/main/packages/bricklayer)

<a id="brickbench"></a>
### 4. BrickBench / BrickAgent — 可复用的 LEGO Agent 考试框架

**是什么：** 2026 年的文本条件 LEGO 设计 benchmark，配有让编码 Agent 查零件、连接、建模、查看和验证的环境。

**适合怎么用：** 学习怎样把“给定要求和零件库存，交付模型”定义成可重复的任务；以其任务和评测组织方式为参考，增加功能性 Technic 题目。

**能拿到什么：** 论文、300 个任务、环境和评测代码。**边界：** 碰撞、库存、连接和稳定性分数不能直接充当机械功能分数；其稳定性检查将连接分量当作刚体，不能据此判断内部齿轮是否正常转动。

[论文](https://arxiv.org/abs/2610.12452) · [项目](https://brickben.ch/) · [代码与任务](https://github.com/kulits/BrickAgent)

<a id="mechanisms"></a>
## 二、根据“要怎么动”，反过来设计机构

<a id="computetechnic"></a>
### 5. Computational LEGO Technic Design — 必须对照的先行工作

**是什么：** SIGGRAPH Asia 2019 工作。从草图及可选运动标注出发，生成 Technic 结构，并考虑连接、平衡、应力和装配问题。

**适合怎么用：** 学习如何把梁、销、轴等变成计算机能处理的结构，也帮助确定我们的新贡献：已有工作已经研究了功能性 Technic 自动设计。

**能拿到什么：** 论文、补充材料、演示视频、代码和案例，还有独立的草图界面仓库。**边界：** 输入主要是草图和运动标注，不是自然语言驱动的软件 Agent。复用前需逐项确认代码和案例许可。

[论文／视频／补充材料](https://xuhaocuhk.github.io/projects/compute_technic/index.html) · [代码](https://github.com/xuhaocuhk/ComputeTechnic) · [草图界面](https://github.com/edward1997104/ComputeTechSketchUI)

<a id="relink"></a>
### 6. ReLink — 给定一些梁和销，让它设计出指定轨迹

**是什么：** 2025 年提交、2026 年修订的工作。把零件抽象成 Technic 类梁和销，在有限库存下生成平面连杆机构，或寻找末端运动最接近目标曲线的设计。

**适合怎么用：** 特别适合构造第二类功能任务：“给你这些零件，让这个点走出指定轨迹。”其搜索和优化方法还可作为非大模型基线，用来判断 Agent 是否真的带来改进。

**能拿到什么：** 论文、MIT 代码、界面、运动学求解器、生成与优化程序、7 条目标曲线。**边界：** 平面抽象还需落实为真实 LEGO 的厚度、连接和装配；路径吻合不代表承载能力已经验证。

[论文](https://arxiv.org/abs/2506.19657) · [代码与演示](https://github.com/ETHZ-EDAC/ReLink) · [目标曲线](https://github.com/ETHZ-EDAC/ReLink/tree/main/assets/curves)

<a id="walkers"></a>
### 7. Make it Walk: Computational Design of LEGO Walkers — 用“能走”来定义成功

**是什么：** 2026 年预印本，围绕目标步态和外观设计 LEGO 行走机构与控制，并展示实物行走。

**适合怎么用：** 参考如何从“长得像一个机器人”进到“它实际按要求移动”，尤其是功能目标、机构设计与实物结果之间的关系。

**能拿到什么：** 论文；本轮未确认独立代码或数据下载入口。**边界：** 方案包含 3D 打印非圆齿轮。如果研究限定“只用标准 LEGO 零件”，应将这类定制零件方案单独比较。

[论文](https://arxiv.org/abs/2610.29505)

<a id="classic-synthesis"></a>
### 8. Conceptual Synthesis of Mechanisms from Qualitative Specifications of Behaviour — 早期的“从功能到 LEGO 机构”

**是什么：** 1992 年研究，把运动要求分解并组合成机构，在 Technic LEGO 场景中展示设计方法，包括步行机构。

**适合怎么用：** 帮助梳理功能描述、机构组合和几何约束之间的关系。它也提醒我们：不能把“从功能要求自动设计 LEGO”本身当作全新的问题。

**能拿到什么：** 作者页面与论文 PDF。**边界：** 这是方法和历史背景参考；本轮未确认可直接运行的现代代码或数据集。

[作者页面](https://www3.cs.stonybrook.edu/~stoller/synthesis.html) · [论文 PDF](https://www3.cs.stonybrook.edu/~stoller/papers/synthesis-of-mechanisms.pdf)

<a id="editors"></a>
## 三、实际的 LEGO 设计软件：AI 可以在哪操作？

<a id="ldcad"></a>
### 9. LDCad — 有脚本接口的 LEGO 编辑器

**是什么：** LEGO 模型编辑软件，提供模型、子模型、宏和动画相关的脚本能力。

**适合怎么用：** 如果研究重点是“AI 使用实际设计软件”，可探索让 Agent 调用脚本或宏，在软件里编辑并观察机构。

**能拿到什么：** 软件、API 文档、脚本示例和齿轮动画教程。**边界：** 这里链接的 API 文档对应 1.7 Alpha；官方平台是 Windows／Linux。动画脚本不自动提供物理正确性，版本也需固定。

[软件功能](https://www.melkert.net/LDCad/features) · [API](https://www.melkert.net/LDCad/docs/scriptAPI2) · [脚本示例](https://www.melkert.net/LDCad/docs/scriptExamples) · [齿轮动画视频](https://www.youtube.com/watch?v=BezWmMlbejQ)

<a id="studio"></a>
### 10. BrickLink Studio — 适合人工复核和图形界面操作

**是什么：** LEGO 数字搭建软件，带碰撞和稳定性检查等功能。

**适合怎么用：** 人工检查生成模型；如果要研究鼠标、键盘式 Agent，也可把它作为图形界面任务环境候选。

**能拿到什么：** 软件和官方帮助文档。**边界：** 官方文档说明碰撞检查对复杂或非刚性零件有限制，稳定性检查也偏保守。它们不是机械功能的最终裁判；本轮未确认通用、受官方支持的自动化编辑 API。

[软件](https://store.bricklink.com/v2/build/studio.page) · [碰撞检查](https://studiohelp.bricklink.com/hc/en-us/articles/5412820155927-Collision) · [稳定性检查](https://studiohelp.bricklink.com/hc/en-us/articles/6501498505111-Stability-check)

<a id="leocad"></a>
### 11. LeoCAD — 开源模型查看、编辑与渲染入口

**是什么：** 支持 LDraw 的开源 LEGO 编辑器，可在 Windows、macOS 和 Linux 使用。

**适合怎么用：** 查看 Agent 输出的模型，或用命令行批量导出图像，给 AI 提供“自己搭出来是什么样”的视觉反馈。

**能拿到什么：** 软件、源码入口和命令行文档。**边界：** 命令行渲染／导出不等于完整的远程编辑 API；它也不是机构物理仿真器。

[官网与代码入口](https://www.leocad.org/) · [命令行文档](https://www.leocad.org/docs/cli.html)

<a id="verification"></a>
## 四、验证能否装起来、能否工作

<a id="technic-sim"></a>
### 12. LegoTechnicSimulation — 从 Technic 模型生成运动／仿真表示

**是什么：** 社区原型，把 LDraw 零件连接解析为刚体、关节、电机和齿轮关系，生成 Blender 动画或 MuJoCo 模型。

**适合怎么用：** 从小齿轮组和销连接样例开始，评估能否作为功能验证器的一部分。

**能拿到什么：** 代码、测试模型、转换与运行说明。**边界：** 特殊连接覆盖有限；凸包碰撞会简化几何；齿轮通过约束耦合，不等于模拟了真实齿面接触。不能把预先写入的传动比读回来，就当成独立验证。复用许可需确认。

[代码与限制](https://github.com/yoff/LegoTechnicSimulation) · [测试样例](https://github.com/yoff/LegoTechnicSimulation/blob/main/tests/fixtures/README.md)

<a id="bricksim"></a>
### 13. BrickSim — 更偏向“机器人怎样把积木装上”

**是什么：** 2026 年针对咬合积木装配和操作的物理模拟工作，提供装配、遥操作和记录／回放示例。

**适合怎么用：** 如果后续要让机器人执行装配，可参考其接触建模、操作环境和演示数据采集方式。

**能拿到什么：** 论文、代码、视频与示例。**边界：** 当前安装面向 x86-64 Linux 和兼容 NVIDIA 环境；不能假定已经支持所有 Technic 齿轮、轴和连接功能。它与“设计满足运动要求的机构”是相邻环节。

[论文](https://arxiv.org/abs/2603.16853) · [代码／视频](https://github.com/intelligent-control-lab/BrickSim)

<a id="sariel"></a>
### 14. Sariel 齿轮工具 — 快速核对齿轮比例

**是什么：** LEGO Technic 作者提供的齿轮比例计算器和参考表。

**适合怎么用：** 生成和人工核对简单齿轮传动题，例如给定齿数后算输出速度比例；也可以辅助设计错误案例。

**能拿到什么：** 网页工具和齿轮比 PDF 表。**边界：** 齿数比例算对，不代表两枚齿轮能在指定位置正确啮合，更不说明效率、负载和支撑都合格。任务中应明确比例定义及转动方向。

[计算器](https://gears.sariel.pl/) · [齿轮比参考表](https://sariel.pl/down/gear-ratios-table.pdf)

<a id="pybricks"></a>
### 15. Pybricks — 让实物电机按要求转，并记录结果

**是什么：** 用 Python 控制兼容 LEGO 硬件的工具；电机接口可控制运动，读取角度、速度，以及部分状态和估计值。

**适合怎么用：** 搭好机构后，让输入电机按规定转动，再用独立测量检查输出轴方向、速度或机构行程。

**能拿到什么：** 软件、文档与示例。**边界：** `load()` 是估计负载，不是独立力矩传感器；`gears` 参数会按填写的齿轮比换算读数。不能用这一换算后的读数证明实际齿轮比正确，输出端需要独立测量。它不是仿真器或训练数据集。

[项目](https://pybricks.com/) · [电机控制与测量文档](https://docs.pybricks.com/en/stable/pupdevices/motor.html)

<a id="assets"></a>
## 五、零件、连接、模型与实物参考

<a id="ldraw"></a>
### 16. LDraw 零件库与格式 — 让设计落到真实零件编号

**是什么：** LEGO 零件的数字几何及模型文件格式，可表达零件引用、位置、方向和步骤等信息。

**适合怎么用：** 作为零件编号、模型交换和渲染的基础，避免只生成无法对应真实零件的形状。

**能拿到什么：** 零件文件、格式规范和更新。**边界：** 几何文件通常不直接给出摩擦、承载、关节类型或插入路径；这些需要补充数据。固定零件库版本有助于复现。

[格式规范](https://www.ldraw.org/article/218.html) · [零件库更新](https://library.ldraw.org/updates)

<a id="shadow"></a>
### 17. LDCad Shadow Library — 补上“这个零件哪里能连接”

**是什么：** 为 LDraw 零件补充吸附、连接位置和镜像等信息的文件库；文件与相应零件对应。

**适合怎么用：** 建立可连接位置和连接候选，减少仅靠三角网格猜孔、轴和销的工作。

**能拿到什么：** 元数据文件、格式说明，仓库标注 CC BY-SA 4.0。**边界：** 并非所有零件都有完整数据；能吸附不证明真实的摩擦、轴向固定或力矩传递可靠。

[元数据仓库](https://github.com/RolandMelkert/LDCadShadowLibrary) · [格式说明](https://www.melkert.net/LDCad/tech/shadowLib)

<a id="omr"></a>
### 18. LDraw OMR — 从已有 Technic 套装提取机构案例

**是什么：** 社区维护的官方套装数字模型库。

**适合怎么用：** 筛选传动、转向、悬挂和升降相关模型，再人工标注输入、输出、连接和预期功能；也可设计“删掉一个关键零件，请修复”的题目。

**能拿到什么：** 可下载模型。**边界：** “官方套装”指模型对应的套装，不代表每个数字模型都经过 LEGO 官方工程认证。模型也不是现成的功能标注训练集；需检查完整性、许可及跨集合重复。

[模型库](https://library.ldraw.org/omr)

<a id="philo"></a>
### 19. Philo 电机测量 — 避免设计一个理论能转、实际带不动的机构

**是什么：** LEGO 电机的实测比较资料，包括速度、力矩、电流等信息及测试条件。

**适合怎么用：** 为实物实验选择电机、设定初始负载范围；将整理后的测量数据用于校准假设。

**能拿到什么：** 图表、实验说明与技术文章。**边界：** 数值与电源、工况、型号和测量方法相关，不能直接当成所有电机的统一参数。需要保留来源和条件，关键结果仍应在自己的装置上测量。

[电机比较与测量](https://www.philohome.com/motors/motorcomp.htm) · [技术文章](https://www.philohome.com/tech.htm)

<a id="bec"></a>
### 20. Brick Experiment Channel — 实物机械原理视频与测量

**是什么：** 用 LEGO 展示和测试机械原理的作者资源，包括多种机构组合演示，以及零件和电机测量。

**适合怎么用：** 初学者先通过视频理解齿轮、曲柄滑块、齿条等机构；研究时把这些例子改写成有明确输入、输出和通过条件的任务。

**能拿到什么：** 原作者视频、文章与测量结果。**边界：** 视频不是带标注和统一划分的数据集；文章可能涉及兼容零件，应区分零件来源。公开观看不等于可以重新分发视频作训练数据。

[20 种机械原理演示](https://www.youtube.com/watch?v=M1-YeqGynlw) · [零件特性实测](https://brickexperimentchannel.wordpress.com/2023/11/15/characteristics-of-lego-parts/)

## 观察名单：有价值，但先不要按可用工具安排实验

[GrafXP/TechnicsSimulator](https://github.com/GrafXP/TechnicsSimulator) 提供 Technic 仿真方向的设计材料和模型资产。核对时 README 明确处于研究／设计阶段，尚无可运行应用；也未确认整体软件许可。因此只列入观察名单，不计入上述 20 项，不把计划中的能力当成已实现功能。

<a id="roadmap"></a>
## 接下来怎么做研究：先完成一个小而完整的实验

以下是**建议的新实验设计**，不是上述项目已经提供的 benchmark。

### 第一步：先做齿轮传动，再扩到连杆轨迹

第一组任务可以固定为：给定标准 LEGO 零件库存、空间限制和输入／输出轴位置，要求达到指定方向和速度比例。例如明确规定 **输出角速度 / 输入角速度 = −1/3**，负号表示反向。AI 除了选对齿轮，还要处理轴、支撑和连接。

先人工搭出少量正确答案，并制作几类错误样例：齿轮位置不对、轴没有有效支撑、连接不足、转动方向错误或装配路径被挡住。用它们检验验证器，允许验证器对不支持的情况返回“未知”。验证器如果连这些都分不清，就不宜直接给 Agent 打分。

第二组再引入 ReLink 类任务：给定梁、销和目标轨迹，让末端尽量沿曲线运动。这样可以逐步从简单的比例要求，进入更复杂的机构设计。

### 第二步：选一个设计环境，完整记录修改过程

先从 Nova、BrickAgent 或 BrickLayer 中选一个，跑通“读要求 → 查零件 → 搭建 → 检查 → 修改 → 导出”。不必一开始接通所有工具；格式、坐标单位、零件编号和连接语义都可能需要适配。

在相同模型、任务和工具调用预算下，比较三种设置：**不给检查反馈、只给几何连接反馈、再加功能反馈**。同时加入规则／搜索方法作为基线。若让 Agent 操作鼠标和键盘，应作为 GUI 设置；写 Python 或调用命令行则另列，不把它们混成同一种软件使用能力。

### 第三步：功能验证需要独立证据

不能在仿真里写入“传动比是 1:3”，再读取这个约束，声称证明设计达到了 1:3。应从实际零件及连接推导运动关系，再用独立实现或实物测量交叉核对。

装配评估检查顺序和插入空间；运动评估测方向、比例、行程或轨迹；实物评估再记录电机、输入速度、负载和卡住等情况。可用 Pybricks 控制输入，用额外传感器或视频测量输出。给出哪些测试通过、哪些未测或不支持。

### 从第一天就保存的数据

| 记录内容 | 为什么要保存 |
| --- | --- |
| 功能要求、库存、尺寸限制、输入／输出定义、软件和零件库版本 | 让别人能重做同一道题。 |
| 每次工具调用、模型版本和视图 | 研究 AI 怎样设计，而不只看最后文件。 |
| 检查结果、失败原因和修改 | 分析反馈是否真的帮助修复；形成后续训练素材。 |
| 装配步骤、独立功能测试、实物条件和结果 | 区分模型看起来正确、能装和能工作。 |
| 来源、许可、原套装／机构家族、训练测试归属 | 支持合法复用，并减少重复案例造成的评测泄漏。 |

建议分别报告连接合法率、装配成功率、功能成功率、三者同时成功率、修复次数和工具成本。用人工核对的正反例检查验证器的误判；再测试未见过的库存、尺寸与机构家族，判断能力能否泛化。

### 怎样形成自己的研究重点？

[Awesome Brick Assembly & Robot Creativity](https://github.com/intelligent-control-lab/Awesome-Brick-Assembly-Robot-Creativity) 已包含设计、装配和机器人相关工作；Nova、Mecha 等也已覆盖部分 Agent 设计与验证流程。因此，“AI 设计 LEGO”这个大方向本身不足以说明差异。

更明确的研究重点可以是：**面向标准 LEGO Technic 零件的可测量功能任务，记录 Agent 使用设计工具和修复错误的全过程，并用独立装配／功能证据评测。** 最终新意要落实到具体数据、任务、方法或可靠性结果，并继续对照最新论文。

本指南核对了公开论文、源码说明和官方文档；尚未完成这些工具的本地运行复现，也没有下载或重建完整训练数据。
