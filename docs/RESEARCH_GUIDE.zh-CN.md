# LEGO × AI 阅读路线与研究切入点

[返回清单](../README.zh-CN.md) · [数据对照表](DATASETS.md)

以下“建议”是基于本次资料整理的研究判断，不是论文已经验证的结论，也不构成“尚无人研究”的新颖性声明。

## 先把目标分清楚

| 研究目标 | 输入 → 输出 | 重点看什么 |
| --- | --- | --- |
| 空间／时序理解 | 多视角或状态序列 → 答案、排序、下一步 | 模型是否理解状态变化与装配依赖 |
| 说明书理解 | 说明书 + 当前状态 → 零件与位姿 | 二维图解到三维动作的对齐 |
| 可搭建生成 | 文字／图片 + 零件约束 → 结构与搭建程序 | 语义、连接、碰撞、稳定性、库存 |
| 交互规划 | 观察 + 可执行动作 → 探索、拆解与重建 | 主动观察、记忆、长序列与错误恢复 |
| 真实执行 | 规划 + 机器人状态 → 抓取、插接、拆卸 | 接触、容差、可达性与闭环纠错 |

## 推荐的第一轮阅读

1. **先明确评测对象。** 读 [LEGO-Puzzles](https://arxiv.org/abs/2503.19990)，再读 [TPRU](https://arxiv.org/abs/2602.18884)。前者提供 LEGO 空间推理任务，后者把 LEGO 装配放入多领域时序训练。复现时记录论文版本、题目版本和提示词，避免混用旧版与更新版结果。
2. **把答案落到动作。** 读 [MEPNet](https://arxiv.org/abs/2207.12572)、[SCANet](https://arxiv.org/abs/2403.18195) 与 [Brick-Composer](https://arxiv.org/abs/2606.05445)。重点比较“选对零件”“位姿正确”“这一步成功”和“完整模型成功”的区别。
3. **理解结构表示。** 比较 [BrickGPT](https://avalovelace1.github.io/BrickGPT/) 的序列生成与 [BrickNet](https://kulits.github.io/BrickNet/) 的连接关系表示；再看 [BrickBench](https://brickben.ch/)、[BrickWright](https://avalovelace1.github.io/brickwright/) 和 [DailyBrick](https://arxiv.org/abs/2611.22132) 如何让智能体使用工具生成和检查搭建方案。
4. **最后接入物理与机器人。** 用 [StableLego](https://github.com/intelligent-control-lab/StableLego) 理解结构检查，用 [BrickSim](https://github.com/intelligent-control-lab/BrickSim) 和 [WorkBenchMark](https://workbenchmark.github.io/) 理解仿真和执行评测的接口需求。

## 建议优先探索的三条线

### 1. 视频／说明书／三维状态的统一过程表示

**假设：** 如果让帧序列、说明书步骤和结构状态共享显式表示，模型可能更容易学会过程推理，而不是依赖相邻图像相似度。

建议先用 TPRU 的 LEGO 子集和可控合成搭建序列做小规模实验。为每步记录新增零件、局部位姿、连接对象与前置条件；再设计跳步、重复、旋转错误和遮挡干扰。真实视频中的三维标注成本需要单独估算，不能假设现有资源已提供全部对齐标签。

评测保留排序、下一步与回溯，同时加入跨视角一致性和执行后状态检查。训练／测试按完整模型或源视频划分。

### 2. 长序列装配中的发现错误与恢复

**假设：** 针对失败状态训练或提供可检验反馈，可能改善长期装配成功率；这一点需要与单纯增加生成预算的基线比较。

起点可选 LEGO-ECA、MEPNet 或 LTRON。对照一次性规划、逐步重规划、带检查器的局部修复。报告完整任务成功率、错误发现率、恢复所需步骤和工具调用开销，避免只报逐步准确率。

### 3. 限定库存下的结构生成与可执行说明书

**假设：** 将库存、物理检查和中间步骤约束纳入生成流程，可能产生更实用的搭建输出。

以 BrickBench 的限定库存设置作为参考，比较结构生成模型与使用搭建 API 的智能体。把语义一致性、零件使用、结构检查与每步可执行性分开评估。机器人验证可从少量固定几何的真实搭建开始，逐步增加复杂度。

## 数据获取顺序建议

本轮补查后，可按研究目标加入以下资源（具体规模和获取状态见 [正文数据节](../README.zh-CN.md#datasets-benchmarks)）：

- **MLLM 视觉评测：** 加入 [BrickVision](https://huggingface.co/datasets/elorian-ai/BrickVision) 的定位、计数与结构比较任务，补充 LEGO-Puzzles；同类生成题训练与零样本结果分别报告。
- **大规模结构训练：** 查看 [BrickFlow / ProcBrick](https://huggingface.co/datasets/kulits/BrickFlow) 的结构预训练与图像条件微调划分。先验证小规模读取和表示转换，再确定完整下载需求。
- **结构功能评测：** 使用 [LMBuild](https://huggingface.co/datasets/Lumos-Jiateng/LMBuild) 的 LEGO 子集，按来源检查与 BrickNet / BrickComposer 训练数据的重叠。
- **装配缺陷感知：** [PIXIE](https://github.com/ZEISS/PIXIE-dataset) 适合作为零样本位姿评测集，不用于训练或调参。
- **机器人动作训练：** [LEGO flat final-goal 200](https://huggingface.co/datasets/ajaysri/lego_flat_final_goal_200_v1) 是小规模仿真示范线索，复用前需澄清许可；[YUBI](https://huggingface.co/datasets/airoa-org/yubi-corl2026-umi-arena) 受竞赛访问与用途限制，不作为默认开放语料。

| 阶段 | 先获取什么 | 应产出的最小结果 |
| --- | --- | --- |
| 起步 | LEGO-Puzzles、TPRU 的小样本及任务定义 | 可复跑的评测清单和数据划分记录 |
| 对齐 | MEPNet / LEGO-ECA 或 Brick-Composer 发布数据 | 单步选砖、位姿或纠错基线 |
| 生成 | StableText2Brick；同时申请 BrickNet | 一份含失败类型的生成评测报告 |
| 执行 | LTRON 或 BrickSim + WorkBenchMark | 仿真中有状态记录的短序列任务 |

此顺序是工作安排建议，不是对下载体积或复现难度的保证。BrickNet 的申请等待可与其他实验并行。

## 视频怎么用

- **研究演示：** 首页的演示表适合快速了解输入、输出和执行效果，不能直接当训练集规模证据。
- **原始搭建视频：** TPRU 提到 Arvin Bricks；本次没有查到可靠的频道规范链接和 36 条视频清单，因此未猜测 URL。AustrianBrickFan 提供另一类可人工筛选的搭建速录来源。
- **标注重点：** 套装编号、真实步骤、重复／跳过动作、镜头切换、遮挡、播放加速、视频与说明书的对应关系。
- **采集记录：** 每条记录作者、URL、获取方式、许可依据和划分归属；如果训练集同时使用视频和说明书，按套装分组检查泄漏。

## 收录边界

这个清单覆盖与真实 LEGO / 咬合积木有关的研究和基础工具。名称含 LEGO 但实际是通用网络模块、知识图谱或其他领域缩写的论文，没有因为名字相同而收录。普通的乐高风格图片生成与具有零件、连接和搭建约束的结构生成也应分开评测。
