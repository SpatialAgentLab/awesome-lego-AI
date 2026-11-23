#!/usr/bin/env python3
"""Render the bilingual catalog from data/resources.json (Python standard library)."""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = json.loads((ROOT / 'data/resources.json').read_text())
RESOURCES = CATALOG['resources']
CATEGORIES = [
    ('reasoning', 'Spatial and procedural reasoning', '空间与过程推理'),
    ('generation', 'Generative design and brickification', '生成式设计与积木化'),
    ('assembly', 'Manual understanding and assembly planning', '说明书理解与装配规划'),
    ('robotics', 'Robotics, physics and simulation', '机器人、物理与仿真'),
    ('perception', 'Recognition and 3D reconstruction', '识别与三维重建'),
    ('data', 'Additional data sources', '其他数据来源'),
    ('tools', 'CAD, rendering and evaluation tools', 'CAD、渲染与评测工具'),
    ('videos', 'Talks and video sources', '演讲与视频来源'),
    ('applications', 'Applications', '应用'),
    ('community', 'Related lists', '相关清单'),
]


def links(r):
    return ' · '.join(f'[{label}]({url})' for label, url in r['links'].items())


def dataset_overview(lang):
    """Put all cataloged data resources in the README, with direct access links."""
    zh = lang == 'zh'
    groups = [
        ('Training datasets and paired evaluation splits', '训练数据与配套评测集',
         ('brickflow', 'lego-flat200', 'yubi-umi-arena', 'tpru', 'brickgpt',
          'bricknet', 'mepnet', 'scanet', 'mobilebrick', 'stablelego',
          'combinatorial3d', 'photos-renders', 'b200c')),
        ('Benchmarks and interactive task environments', 'Benchmark 与交互任务环境',
         ('brickvision', 'lmbuild', 'pixie', 'lego-puzzles', 'brick-composer',
          'brickbench', 'workbenchmark', 'break-make', 'instructionet', 'brickagi')),
        ('Source material for building datasets', '构建数据集的原始素材',
         ('omr-rebrickable', 'conveyor', 'lego-video-archive', 'ldraw-omr',
          'lego-instructions', 'rebrickable')),
    ]
    by_id = {r['id']: r for r in RESOURCES if 'dataset' in r}
    grouped = [key for _, _, keys in groups for key in keys]
    if len(grouped) != len(set(grouped)) or set(grouped) != set(by_id):
        raise ValueError('README data groups must cover every dataset exactly once')
    lines = ['<a id="datasets-benchmarks"></a>', '',
             '## ' + ('训练数据与 Benchmark' if zh else 'Training datasets and benchmarks'), '']
    if zh:
        lines += [
            f'**数据优先：以下在正文汇总全部 {len(by_id)} 个数据／基准条目，提供任务、规模、获取状态和原始入口。** 数据与配套测试集、独立 benchmark、原始素材分别列出；部分项目同时支持训练与评测。', '',
            '**本轮更新（2026-11-22）：** 新增 [BrickVision（11 月）](#brickvision)、[LMBuild（10 月）](#lmbuild)、[PIXIE](#pixie)、[仿真装配示范](#lego-flat200)、[YUBI（受限访问）](#yubi-umi-arena)、[OMR 整合包](#omr-rebrickable) 和 [BrickAGI（社区）](#brickagi)；补全 [BrickFlow / ProcBrick](#brickflow) 的 1 亿结构预训练集、100 万微调渲染图与评测划分。表格末尾另列尚未确认下载的数据线索，不计入上述数据条目。', '',
            '**按任务定位：** 空间推理看 [LEGO-Puzzles](#lego-puzzles)；时序理解看 [TPRU 的 LEGO 子集](#tpru)；文本到结构看 [StableText2Brick](#brickgpt) / [BrickNet](#bricknet)；说明书与纠错看 [MEPNet](#mepnet) / [LEGO-ECA](#scanet)；生成评测看 [BrickBench](#brickbench)。', '',
            '规模沿用原始发布记录，不代表本地下载核验后的可用训练量，也不能跨条目直接相加。**TPRU 的 24,750 条是多领域训练总量，并非 LEGO 子集大小。** 更完整的选用、划分与许可注意事项见 [数据子文档](docs/DATASETS.md)。', '',
        ]
    else:
        lines += [
            f'**Data first: all {len(by_id)} data / benchmark entries are listed here with tasks, reported scale, access status and source links.** Datasets with paired evaluation splits, standalone benchmarks and source material are grouped separately; some projects support both training and evaluation.', '',
            '**Update (2026-11-22):** added [BrickVision (November)](#brickvision), [LMBuild (October)](#lmbuild), [PIXIE](#pixie), [simulated assembly demonstrations](#lego-flat200), [YUBI (restricted)](#yubi-umi-arena), [OMR packaging](#omr-rebrickable) and [BrickAGI (community)](#brickagi). Expanded [BrickFlow / ProcBrick](#brickflow) with its 100M-tree pretraining corpus, 1M finetuning renders and evaluation splits. Unconfirmed dataset releases are listed separately below and excluded from the data-entry count.', '',
            '**Find data by task:** [LEGO-Puzzles](#lego-puzzles) for spatial reasoning; the [LEGO subset of TPRU](#tpru) for temporal understanding; [StableText2Brick](#brickgpt) / [BrickNet](#bricknet) for text-to-structure; [MEPNet](#mepnet) / [LEGO-ECA](#scanet) for manuals and correction; [BrickBench](#brickbench) for generation evaluation.', '',
            'Counts come from the source releases, not verified local downloads, and should not be summed across entries. **TPRU contains 24,750 training examples across domains; this is not the size of its LEGO subset.** See the [dataset companion](docs/DATASETS.md) for selection, split and licensing notes.', '',
        ]
    for en, cn, keys in groups:
        lines += [f'### {cn if zh else en}', '']
        if zh:
            lines += ['| 数据／基准 | 模态与任务 | 报告规模 | 获取状态 | 数据／原始入口 |']
        else:
            lines += ['| Dataset / benchmark | Modality / task | Reported scale | Access status | Data / source |']
        lines += ['| --- | --- | --- | --- | --- |']
        for key in keys:
            r = by_id[key]
            d = r['dataset']
            sources = {k: v for k, v in r['links'].items()
                       if 'data' in k.lower() or k in ('Test', 'Models', 'Downloads', 'API', 'Instructions', 'Code')}
            if not sources:
                sources = {k: v for k, v in r['links'].items()
                           if k in ('Code', 'Code / simulator', 'Training', 'Full text')}
            source_links = ' · '.join(f'[{k}]({v})' for k, v in sources.items())
            lines.append(f'| [{d["name"]}](#{key}) | {d["modality"]} | {d["scale"]} | {d["access_zh" if zh else "access_en"]} | {source_links} |')
        lines += ['']
    lines += data_watchlist(lang)
    return lines


def data_watchlist(lang, prefix=''):
    zh = lang == 'zh'
    lines = ['### ' + ('待确认数据发布：论文已公开' if zh else 'Dataset release watchlist: papers available'), '',
             ('以下规模为论文报告；尚未确认完整数据下载，不能当作已取得的训练集。' if zh else
              'Reported corpus sizes are paper claims; full dataset downloads have not been confirmed.'), '',
             ('| 项目 | 报告规模 | 发布状态 |' if zh else '| Project | Reported scale | Release status |'),
             '| --- | --- | --- |']
    for r in RESOURCES:
        if 'data_watch' in r:
            d = r['data_watch']
            lines.append(f'| [{d["name"]}]({prefix}#{r["id"]}) | {d["scale"]} | {d[lang]} |')
    return lines + ['']


def readme(lang):
    zh = lang == 'zh'
    n_papers = sum('Paper' in r['links'] for r in RESOURCES)
    n_data = sum('dataset' in r for r in RESOURCES)
    lines = ['# 🧱 Awesome LEGO AI', '', '[English](README.md) | [简体中文](README.zh-CN.md)', '']
    if zh:
        lines += [
            '面向 **LEGO / 咬合积木 × AI** 的研究资源清单：从空间与时序推理，到说明书理解、三维生成、装配规划和机器人执行。', '',
            '**专题精简版：** [LEGO 功能设计 Agent：10 项直接相关资源](docs/FOCUSED_LEGO_DESIGN.zh-CN.md) — 功能需求、软件建模、装配与功能验证；含数据和 benchmark 入口。', '',
            f'主目录最近整理：**{CATALOG["updated"]}**。共 **{len(RESOURCES)} 个独立条目**，其中 **{n_papers} 篇论文**、**{n_data} 个数据／基准条目**。同一项目可同时提供论文、数据、代码和视频，不重复计为独立项目；专题补充资源另列。', '',
            '优先收录原论文、作者项目页、官方代码和数据入口。年份优先采用首个预印本年份，正式发表信息另列；摘要为本清单重新撰写。链接核对不等于代码复现或数据完整下载。', '',
            '**从这里开始：** [训练数据与 Benchmark](#datasets-benchmarks) · [中文阅读路线与研究切入点](docs/RESEARCH_GUIDE.zh-CN.md) · [BibTeX](papers.bib) · [机器可读目录](data/resources.json) · [核验说明](docs/VERIFICATION.md)', '',
            '## 快速选读', '',
            '| 目标 | 建议起点 |', '| --- | --- |',
            '| 多模态空间／时序推理 | [LEGO-Puzzles](#lego-puzzles) → [TPRU](#tpru) → [Brick-Composer](#brick-composer) |',
            '| 文本到可搭建模型 | [BrickGPT](#brickgpt) → [BrickNet](#bricknet) → [BrickBench](#brickbench) / [BrickWright](#brickwright) / [DailyBrick](#dailybrick) |',
            '| 说明书到动作与纠错 | [MEPNet](#mepnet) → [SCANet](#scanet) → [InstructioNet](#instructionet) |',
            '| 三维重建 | [MobileBrick](#mobilebrick) → [BrickFlow](#brickflow) |',
            '| 真实机器人 | [StableLego](#stablelego) → [BrickSim](#bricksim) → [WorkBenchMark](#workbenchmark) |', '',
            '## 目录', '',
        ]
    else:
        lines += [
            'A curated research list for **LEGO / interlocking bricks × AI**: spatial and temporal reasoning, visual manuals, 3D generation, assembly planning, and robot execution.', '',
            '**Focused shortlist (Chinese):** [10 resources for functional LEGO design agents](docs/FOCUSED_LEGO_DESIGN.zh-CN.md) — requirements, software-based modeling, assembly and functional verification, with data and benchmark links.', '',
            f'Main catalog last curated: **{CATALOG["updated"]}**. **{len(RESOURCES)} unique entries**, including **{n_papers} papers** and **{n_data} data / benchmark entries**. A project may provide several artifact types; these counts overlap. Additional shortlist resources are listed separately.', '',
            'We prioritize original papers, author project pages, official repositories and dataset records. Years generally indicate the first preprint, with publication venues listed separately. Descriptions are original summaries. Link review does not imply successful reproduction or complete dataset download.', '',
            '**Start here:** [Training datasets and benchmarks](#datasets-benchmarks) · [Chinese research guide](docs/RESEARCH_GUIDE.zh-CN.md) · [BibTeX](papers.bib) · [Machine-readable catalog](data/resources.json) · [Verification notes](docs/VERIFICATION.md)', '',
            '## Start here', '',
            '| Goal | Suggested reading |', '| --- | --- |',
            '| Multimodal spatial / temporal reasoning | [LEGO-Puzzles](#lego-puzzles) → [TPRU](#tpru) → [Brick-Composer](#brick-composer) |',
            '| Text-to-buildable design | [BrickGPT](#brickgpt) → [BrickNet](#bricknet) → [BrickBench](#brickbench) / [BrickWright](#brickwright) / [DailyBrick](#dailybrick) |',
            '| Manuals, actions and correction | [MEPNet](#mepnet) → [SCANet](#scanet) → [InstructioNet](#instructionet) |',
            '| 3D reconstruction | [MobileBrick](#mobilebrick) → [BrickFlow](#brickflow) |',
            '| Real robots | [StableLego](#stablelego) → [BrickSim](#bricksim) → [WorkBenchMark](#workbenchmark) |', '',
            '## Contents', '',
        ]
    overview_index = lines.index('## 快速选读' if zh else '## Start here')
    lines[overview_index:overview_index] = dataset_overview(lang)
    lines.append('- [' + ('训练数据与 Benchmark' if zh else 'Training datasets and benchmarks') + '](#datasets-benchmarks)')
    for key, en, cn in CATEGORIES:
        lines.append(f'- [{cn if zh else en}](#{key})')
    lines += [f'- [{"论文演示视频速查" if zh else "Research demo videos"}](#research-videos)', '',
              '[Contributing](CONTRIBUTING.md) · [Publishing to GitHub](docs/PUBLISHING.md)', '']
    for key, en, cn in CATEGORIES:
        lines += [f'<a id="{key}"></a>', '', f'## {cn if zh else en}', '']
        for r in (r for r in RESOURCES if r['category'] == key):
            meta = ' · '.join(str(x) for x in (r['year'], r['venue']) if x)
            lines += [f'<a id="{r["id"]}"></a>', '', f'### {r["title"]}', '']
            if meta:
                lines += [f'*{meta}*', '']
            lines += [r['description'][lang], '', links(r), '']
            if r['notes'][lang]:
                lines += [f'> {r["notes"][lang]}', '']
    lines += ['<a id="research-videos"></a>', '', f'## {"论文演示视频速查" if zh else "Research demo videos"}', '']
    lines += [('以下为作者项目的演示入口；项目页中的嵌入视频与单独视频文件均已区分。' if zh else
               'Author demonstrations, distinguishing direct videos from pages containing embedded media.'), '',
              '| Project | Video / demo |', '| --- | --- |']
    for r in RESOURCES:
        if r['category'] in ('videos', 'applications'):
            continue
        media = {k: v for k, v in r['links'].items() if 'video' in k.lower()}
        if media:
            lines.append(f'| [{r["title"]}](#{r["id"]}) | ' + ' · '.join(f'[{k}]({v})' for k, v in media.items()) + ' |')
    lines += ['', '## ' + ('收录与复用' if zh else 'Curation and reuse'), '']
    if zh:
        lines += ['本清单关注真实积木、结构和搭建过程；仅名称含 LEGO、但与积木无关的方法不作为核心资源。TPRU 属于包含 LEGO 子集的多领域数据，已明确标注。', '',
                  '视频可观看不等于可批量下载、训练或再分发；论文、代码、数据、CAD 零件库可能有不同许可，具体以原始发布页为准。本仓库仅提供索引和原创摘要。', '',
                  '结构参考并致谢 [360er0/awesome-lego-machine-learning](https://github.com/360er0/awesome-lego-machine-learning)。欢迎按 [贡献指南](CONTRIBUTING.md) 补充条目或修复链接。', '',
                  'LEGO® 是 LEGO Group 的商标。本清单为独立研究资源索引，与 LEGO Group 无隶属或背书关系。']
    else:
        lines += ['The core scope is actual bricks, their geometry and the construction process. Unrelated methods merely named LEGO are excluded. Multi-domain resources such as TPRU are explicitly identified.', '',
                  'Public video viewing is not a grant of bulk-download, training or redistribution rights. Papers, software, datasets and CAD assets can carry different licenses; consult the original release. This repository contains links and original descriptions only.', '',
                  'Inspired by and with thanks to [360er0/awesome-lego-machine-learning](https://github.com/360er0/awesome-lego-machine-learning). See [Contributing](CONTRIBUTING.md) for additions and corrections.', '',
                  'LEGO® is a trademark of the LEGO Group. This independent research index is not affiliated with or endorsed by the LEGO Group.']
    return '\n'.join(lines) + '\n'


def datasets():
    lines = ['# Dataset matrix / 数据对照表', '', '[Back to list](../README.md) · [返回中文版](../README.zh-CN.md)', '',
             f'Curated {CATALOG["updated"]}. Counts refer to the named source version, not verified local downloads.', '',
             '数据、基准、原始目录分别说明。`规模` 不代表可直接用于训练的独立样本量；不同条目可能共享原模型或视频，不能简单相加。', '',
             '| Resource | Modality | Reported scale | Access / 获取状态 |', '| --- | --- | --- | --- |']
    for r in RESOURCES:
        if 'dataset' not in r:
            continue
        d = r['dataset']
        lines.append(f'| [{d["name"]}](../README.md#{r["id"]}) | {d["modality"]} | {d["scale"]} | {d["access_en"]}<br>{d["access_zh"]} |')
    lines += [''] + data_watchlist('en', '../README.md')
    lines += ['', '## Choosing data / 如何选用', '',
              '- **Fine-grained grounding / counting:** BrickVision (1,000 test items); its scene generator supports separate synthetic training experiments.',
              '- **Functional assembly:** LMBuild has 55 LEGO tasks in Core and 938 in Full; do not treat its mixed-CAD total as LEGO-only.',
              '- **Assembly-defect pose evaluation:** PIXIE is test-only. Do not train or tune on its images.',
              '- **Robot demonstrations:** LEGO flat final-goal 200 is simulated and train-only, with license clarification needed. YUBI contains real LEGO tasks but is restricted to approved competition use.',
              '- **Spatial / temporal QA:** LEGO-Puzzles; the LEGO subset of TPRU. Keep the multi-domain totals separate.',
              '- **Manual-to-action / correction:** MEPNet, LEGO-ECA and BC-Bench assets.',
              '- **Text-to-structure:** StableText2Brick, BrickNet (request access), and BrickBench prompts / runs.',
              '- **Image-to-structure:** MobileBrick for geometry reconstruction; BrickFlow for part-pose assembly.',
              '- **Interaction / robotics:** LTRON and WorkBenchMark; BrickSim supplies a simulator rather than a generic labeled video corpus.',
              '- **Recognition:** B200C and the photos/renders collection; conveyor videos offer real motion but not assembly sequences.', '',
              '## Practical notes / 实验前检查', '',
              '1. 保存原始数据版本、下载日期和许可文本；代码仓库许可不自动覆盖外链数据。此表没有把未核实的许可标作“可商用”。',
              '2. 训练／测试优先按套装、完整模型或源视频划分，避免相邻步骤和不同渲染视角跨集合泄漏。',
              '3. 统一零件 ID、颜色、坐标轴、长度单位和旋转约定；保留原始 ID 到规范 ID 的映射。',
              '4. 区分最终结构合法、每步可搭建、机器人可达、真实执行成功。只检查碰撞不能替代全部指标。',
              '5. 视频来源应记录作者、原 URL、套装编号、剪辑／加速、许可和标注状态；不要从频道总视频数推算可用训练规模。', '',
              '## Known access limitations / 已知限制', '',
              '- BrickNet: the full dataset uses an author request form. The public CAD assets are a separate download.',
              '- YUBI: manual approval, competition registration and confidentiality terms; not general-purpose open training data. Its published hours/episodes include non-LEGO tasks.',
              '- JARVIS, LegoVerse/LegoACE and BrickAnything: tracked as data-release leads, not confirmed downloadable training corpora.',
              '- Community releases: LEGO flat final-goal 200 has no held-out split or explicit license in the reviewed card; OMR packaging overlaps its upstream models; BrickAGI public tasks/solutions are open-book.',
              '- LEGO Co-builder: an author-linked repository was found, but packaging and reproducibility remain unclear; not counted as a confirmed downloadable dataset here.',
              '- Arvin Bricks: TPRU identifies this source, but this review did not resolve a reliable canonical channel URL or the 36-video manifest. No channel URL is guessed.',
              '- Most Wiedzy / Rebrickable: automated access was restricted. Use the original catalog / paper links and check through a normal browser.',
              '- Remote archives and model weights were not downloaded or executed in this curation task.', '']
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true', help='Fail if generated files are stale')
    args = parser.parse_args()
    outputs = {'README.md': readme('en'), 'README.zh-CN.md': readme('zh'), 'docs/DATASETS.md': datasets()}
    stale = []
    for name, content in outputs.items():
        path = ROOT / name
        if args.check:
            if not path.exists() or path.read_text() != content:
                stale.append(name)
        else:
            path.write_text(content)
    if stale:
        raise SystemExit('Stale generated files: ' + ', '.join(stale))
    print('Generated content is current.' if args.check else 'Rendered bilingual catalog and dataset matrix.')


if __name__ == '__main__':
    main()
