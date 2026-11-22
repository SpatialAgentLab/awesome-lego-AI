# Contributing

Add useful LEGO / interlocking-brick AI resources with primary-source evidence.

1. Edit `data/resources.json`. Use a stable lowercase ID and one main category; attach paper, code, data and video links to the same project.
2. Write short original descriptions in English and Chinese. Include the first-publication year and verified venue where available. Distinguish preprints from accepted papers.
3. Link the author's repository, not an arbitrary fork. Record renamed projects as aliases instead of duplicate entries.
4. For datasets, specify modality, reported scale, source version and access conditions. Do not equate a paper's promise to release data with an available download.
5. Mark unresolved links and repository limitations in `notes`. Use the date you actually reviewed the source in `checked`.
6. For videos, distinguish research demos, talks and source channels. Do not describe a public channel as an openly licensed training corpus.
7. Add a verified citation to `papers.bib` for new papers. Keep the citation key equal to the resource ID.
8. Regenerate and check the files:

```bash
python3 scripts/render.py
python3 scripts/validate.py
```

Optional network audit:

```bash
python3 scripts/check_links.py
```

`README.md`, `README.zh-CN.md` and `docs/DATASETS.md` are generated; edit the catalog or renderer rather than making changes that the next render would overwrite. The network audit records HTTP observations, not scientific verification or permission to reuse material.

New contributions should improve coverage of spatial reasoning, procedural understanding, buildable generation, perception, assembly planning, physics or real robot execution. General LEGO resources are useful when they directly support those workflows. Please avoid unrelated AI methods that merely use “LEGO” as an acronym.
