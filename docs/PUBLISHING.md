# Publish to SpatialAgentLab later

This repository is prepared locally as `awesome-lego-AI`. No remote repository is created by the preparation workflow, and no push is required for reviewing its contents.

权限开通后，在 GitHub 的 **SpatialAgentLab** 组织内创建空仓库 `awesome-lego-AI`。不要自动添加 README、License 或 `.gitignore`，以免与本地初始提交冲突。

Suggested description:

> Curated LEGO × AI resources: spatial reasoning, procedural understanding, generative design, datasets, simulation, and robotic assembly.

Suggested topics: `awesome-list`, `lego`, `spatial-reasoning`, `multimodal-learning`, `robotics`, `assembly-planning`, `3d-generation`, `datasets`.

在本地仓库目录运行：

```bash
python3 scripts/validate.py
git status
git remote add origin git@github.com:SpatialAgentLab/awesome-lego-AI.git
git push -u origin main
```

如果已经设置 `origin`，先用 `git remote -v` 核对目标；确认是本组织目标仓库后再推送。若尚无本地提交，先使用自己的 Git 身份提交：

```bash
git add .
git commit -m "Add curated LEGO AI research resources"
```

不需要额外的网站部署。GitHub 会直接呈现英文 README，首页提供中文版、数据表、阅读路线和 BibTeX 链接。
