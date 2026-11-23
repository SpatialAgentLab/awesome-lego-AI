# LEGO 功能设计 Agent 精简资源

[返回完整清单](../README.zh-CN.md) · 核对日期：2026-11-23

**研究问题：AI 能否使用设计软件，构建满足功能要求的 LEGO 零件系统，并验证它能装起来、能按要求工作？**

只保留 8 项直接相关的论文／工具，以及 2 项模型与视频素材。优先看 **LDraw Nova、LDraw Mecha、Computational LEGO Technic Design 和 BrickBench**。现有资源已经覆盖部分设计与检查流程；值得进一步研究的是功能需求、软件操作、装配可行性与独立功能测试之间的联系。

## 数据与 Benchmark 先看这些

| 入口 | 公开内容 | 用途与边界 |
| --- | --- | --- |
| [BrickBench 任务与评测器](https://github.com/kulits/BrickAgent) | Model、Set、Alt-Build 各 100 个任务，共 300 个；题目、库存约束、评测脚本 | 可作 LEGO 工具使用 Agent 的评测起点；现有评测不等于传动比、力矩或运动范围测试。 |
| [Nova 机构案例](https://github.com/anteloc/ldraw-nova/tree/master/examples/mechanism-atlas) | 机构搭建参考与案例；仓库另有 JSON 计划、生成脚本和 MPD 示例 | 适合构造操作与修正任务；不应直接当作带统一划分的训练轨迹集。 |
| [Mecha 保存的案例](https://github.com/anteloc/ldraw-mecha/blob/master/examples/README.md) | 传动、转向、发动机、悬挂等案例的计划、模型、检查记录与 Blender 资产 | 适合机构理解与运动检查；部分资产需 Git LFS。案例不是独立留出 benchmark。 |
| [ComputeTechnic 数据目录](https://github.com/xuhaocuhk/ComputeTechnic/tree/main/LEGO_Technic_data) | 论文代码配套案例／实验目录，包括风扇、升降机构、机械臂等命名目录 | 可研究零件结构与连接表示；不能把目录数当有效训练样本数，统一训练划分与功能标签需另行整理。 |
| [Technic 仿真测试样例](https://github.com/yoff/LegoTechnicSimulation/blob/main/tests/fixtures/README.md) | 摩擦销、无摩擦销、电机、齿轮啮合等最小 LDraw 模型及预期结果 | 适合验证器单元任务；例如 8 齿／24 齿啮合检测。属于工程测试样例，不是大规模数据集。 |

这批资源中，尚未确认有完整覆盖“功能需求 → 软件操作轨迹 → 修改 → 装配验证 → 功能实测”的统一公开训练集。可从上述案例构建任务，但应按原始套装／机构家族划分训练与测试，避免仅换颜色或视角造成重复。公开文件的复用仍以各仓库及上游模型许可为准。

## 八项核心资源

| 资源 | 为什么与本题直接相关 | 获取与验证边界 |
| --- | --- | --- |
| **1. LDraw Nova** — 社区 Agent 工具 | Agent 检索真实零件、编写 JSON 计划、构建 MPD、渲染并修改；Technic 机制约束与 trace 检查涉及输入锁死、齿轮间距、轴支撑等。 | [代码／演示](https://github.com/anteloc/ldraw-nova) · [机构工作流](https://github.com/anteloc/ldraw-nova/blob/master/docs/agent/guides/mechanisms.md) · [验证范围](https://github.com/anteloc/ldraw-nova/blob/master/docs/agent/reference/validation.md)。代码标注 AGPL-3.0；通过检查不保证真实可装配，不证明插入路径、强度或制造配合。 |
| **2. LDraw Mecha** — 社区 Agent 工具 | 从已有 MPD 推断机构，生成运动计划和 Blender rig；有传动比、杆长、闭环及采样姿态检查。非常贴近“Agent 理解乐高机构并验证运动”。 | [代码／HOWTO 视频](https://github.com/anteloc/ldraw-mecha) · [验证文档](https://github.com/anteloc/ldraw-mecha/blob/master/docs/validation.md)。代码标注 AGPL-3.0；README 明确没有完整物理模拟，不考虑重力、受力、重量和惯性。 |
| **3. Computational LEGO Technic Design** — SIGGRAPH Asia 2019 | 从草图及可选运动标注生成 Technic 结构，建模连接关系，并分析平衡、应力与可装配性。是功能性 LEGO 设计必须对照的先行工作。 | [论文／补充／视频](https://xuhaocuhk.github.io/projects/compute_technic/index.html) · [代码与案例](https://github.com/xuhaocuhk/ComputeTechnic) · [草图 UI](https://github.com/edward1997104/ComputeTechSketchUI)。输入主要是草图与运动标注，不是自然语言软件 Agent；代码和模型复用许可需逐项核对。 |
| **4. BrickBench / BrickAgent** — 2026 | 提供编码 Agent 的零件查询、精确连接、建模、查看和检查接口；有受限零件库存任务和可复用评测脚本。 | [论文](https://arxiv.org/abs/2610.12452) · [代码／任务](https://github.com/kulits/BrickAgent)。检查碰撞、连接、库存和稳定性；其稳定性模拟将每个连接分量视为刚体，不能直接验证内部齿轮运动。 |
| **5. LegoTechnicSimulation** — 社区原型 | 将 LDraw Technic 模型解析为刚体、关节、电机与齿轮关系，输出 Blender 动画或 MuJoCo MJCF。是搭建功能验证原型的候选。 | [代码／案例／限制](https://github.com/yoff/LegoTechnicSimulation)。特殊连接件识别有限；MuJoCo 碰撞使用凸包，齿轮以约束关系耦合，不等于齿面接触与真实受力已验证；复用许可待确认。 |
| **6. LDCad 脚本接口** — 乐高设计软件 | 提供模型编辑、子模型、选择、宏和动画接口，可用于研究 Agent 在实际 LEGO 编辑器中的操作。 | [官方 API](https://www.melkert.net/LDCad/docs/scriptAPI2) · [脚本示例](https://www.melkert.net/LDCad/docs/scriptExamples) · [齿轮动画教程](https://www.youtube.com/watch?v=BezWmMlbejQ)。上述 API 页面对应 1.7 Alpha；官方平台为 Windows／Linux。脚本动画不是物理可行性证明。 |
| **7. Make it Walk: Computational Design of LEGO Walkers** — 2026 预印本 | 按目标步态与外观联合设计机构和控制，并展示实物行走；适合作为“功能目标如何定义和检验”的参考。 | [论文](https://arxiv.org/abs/2610.29505)。方案包含 **3D 打印非圆齿轮**，不是纯标准 LEGO 零件方案；本轮未确认独立代码／数据下载。 |
| **8. BrickSim** — 2026 | 针对咬合积木装配与操作的物理模拟，提供装配、遥操作和记录／回放示例，可承接“能否装起来”的执行研究。 | [代码／视频](https://github.com/intelligent-control-lab/BrickSim) · [论文](https://arxiv.org/abs/2603.16853)。当前安装要求 x86-64 Linux 与兼容 NVIDIA 环境；不能据此假定已支持 Technic 全部齿轮、轴及关节功能。 |

## 两项补充素材

**9. LDraw 零件库与 OMR。** [格式规范](https://www.ldraw.org/article/218.html)定义零件引用、位姿和步骤等表示；[零件库／OMR](https://library.ldraw.org/omr)提供 LEGO 套装数字模型，可筛选 Technic 作为机构分析和任务构建的原始素材。模型文件本身不保证含功能目标、关节真值或经验证的装配轨迹。

**10. Brick Experiment Channel 的 20 种机械原理演示。** [原作者视频](https://www.youtube.com/watch?v=M1-YeqGynlw)包含齿轮传动、曲柄滑块、齿条齿轮、蜗杆等实物 LEGO 机构，可用来定义任务家族和观察真实行为。它是视频素材，不是已授权再分发的标注训练集。

## 建议的最小研究起点

先做一个“给定标准 LEGO 零件库存、目标传动比和空间限制”的任务族：借鉴 **Nova／BrickAgent** 的设计接口，参考 **ComputeTechnic** 的连接建模，用 **Mecha／TechnicSimulation** 研究运动检查，再用独立计算与实物样例校验。工具之间的格式、零件覆盖与约束语义需要适配，不能直接视为现成流水线。

记录需求、操作、模型版本、检查结果与修改；分别报告 **几何连接合法性、装配路径可行性、运动学功能、动力学／实物结果**。如果传动比已经写成仿真约束，读回同一个比例不能独立证明齿轮设计正确。GUI 操作与 Python／CLI 操作也应作为不同实验设置报告。

**与现有工作的关系：** Nova／Mecha 已经覆盖部分 Agent 设计、机构检查和运动工作流；研究差异需要落在新的功能任务、过程数据、泛化评测与独立验证上。这里的候选工具按公开源码／文档筛选，尚未完成本地运行复现。
