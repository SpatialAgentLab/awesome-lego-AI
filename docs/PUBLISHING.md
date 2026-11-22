# Maintaining the GitHub repository

Public repository: [SpatialAgentLab/awesome-lego-AI](https://github.com/SpatialAgentLab/awesome-lego-AI).

默认分支为 `main`。GitHub 会直接展示英文 README，首页提供中文版、数据表、阅读路线和 BibTeX 链接，不需要额外的网站部署。

## Update the resource list

资源条目统一维护在 `data/resources.json`，然后重新生成文档并检查：

```bash
python3 scripts/render.py
python3 scripts/validate.py
git diff
```

确认内容后提交并推送：

```bash
git add data/resources.json README.md README.zh-CN.md docs/DATASETS.md
git commit -m "Update LEGO AI resources"
git push origin main
```

如果改动包含论文引用或其他文档，请将相应文件一并加入提交。贡献者没有写入权限时，请通过 fork 和 pull request 提交。

## Set up another computer

```bash
gh auth login --hostname github.com --git-protocol https --web
gh auth setup-git
gh repo clone SpatialAgentLab/awesome-lego-AI
cd awesome-lego-AI
```

推送前用 `git remote -v` 核对目标。请勿将访问令牌或登录凭证写进仓库。
