# Verification / 核验说明

Review date: **2026-11-22**.

## What was reviewed

- The two seed papers, their author repositories and available dataset links.
- Primary paper abstracts, project descriptions, repository READMEs and data records for the added research entries.
- Renamed projects and overlapping assets: LegoGPT / BrickGPT and StableText2Lego / StableText2Brick are each treated as one project / dataset family.
- Dataset scope: TPRU's reported total is multi-domain; MobileBrick concerns reconstruction; conveyor videos concern sorting; public channels are source leads rather than released training datasets.
- Local Markdown links, anchors, duplicate resource IDs, citation coverage and consistency between the JSON catalog and generated READMEs.

The linked primary pages are the evidence for each entry. The original awesome list provided discovery leads and organizational inspiration; descriptions here were rewritten and research facts checked against original sources where available. Access restrictions and sparse documentation are explicitly recorded rather than silently treated as confirmation.

## Expanded data search — 2026-11-22

Added seven data / benchmark entries and three paper-based release leads. The catalog now contains 64 resources, 35 papers and 29 data / benchmark records. Release leads are excluded from the data count. These are additions to this catalog, not a claim that every resource was first released in November.

| Resource | Evidence and scope |
| --- | --- |
| [BrickVision](https://huggingface.co/datasets/elorian-ai/BrickVision) | Read all four test JSONL files: 250 records each, 1,000 total. Image payloads were not downloaded. The [November paper](https://arxiv.org/abs/2611.08485) and official card identify the tasks and evaluation. |
| [BrickFlow / ProcBrick](https://huggingface.co/datasets/kulits/BrickFlow) | Updated the existing entry with source-reported 100M pretraining trees, 1M finetuning renders and 9,900 validation renders. The additional 512-model BrickNet evaluation set is separately gated. |
| [LMBuild](https://lumos-jiateng.github.io/LMBuild/) | Author source table reports 55 LEGO tasks in Core and 938 in Full, within mixed-domain totals of 200 and 2,549. Public data card and download instructions were reviewed; a local download of the core manifest timed out, so counts were not independently reproduced. |
| [PIXIE](https://github.com/ZEISS/PIXIE-dataset) | Counted four model directories and 695 input-image files in the Git tree at `86a3ca0ada507a52fa5879296fd5e4aa4d3fe9cf`, excluding calibration and website images. The official protocol is test-only; the numerical count is file inventory, not a claim of 695 unique scenes. |
| [LEGO flat final-goal 200](https://huggingface.co/datasets/ajaysri/lego_flat_final_goal_200_v1) | Read `meta/info.json`: 200 episodes, 79,956 frames, 20 Hz, train-only. Public metadata and file listing verified; no full videos downloaded. No explicit reuse license was found in the reviewed card. |
| [YUBI](https://huggingface.co/datasets/airoa-org/yubi-corl2026-umi-arena) | Card reports 579.9 hours across all tasks, including LEGO. Hub metadata confirms manual gating. Competition-only terms apply; no access request, NDA or acceptance was submitted. LEGO subset size remains unresolved. |
| [OMR + Rebrickable package](https://huggingface.co/datasets/DylanRiden/sets_lego_omr_full) | Reviewed the original curator's card and JSONL file listing. Approximately 1,367 sets is curator-reported, with overlap with OMR; package licensing does not resolve all upstream terms. |
| [BrickAGI](https://github.com/withtally/brickagi) | Reviewed the community task index and versioned protocol notes. Public tasks/solutions are open-book; structural checks have a limited proof scope and are not physical robot validation. |

[Machine-readable review evidence](../data/source-review-2026-11-22.json) records Hub revisions, small-file hashes, counts and exclusions. New paper citations were checked against arXiv metadata or the author's official BibTeX.

**Release watchlist:** [JARVIS](https://arxiv.org/abs/2610.27618) reports 236,679 training tasks and a 50-task evaluation suite, but no author-controlled data download was confirmed. [LegoACE](https://github.com/VAST-AI-Research/LegoACE) reports LegoVerse and provides training formats/model links; its full dataset download was not confirmed. [BrickAnything](https://github.com/xjtunzy/BrickAnything) provides inference/model links, with no separate training archive confirmed. These statements describe this review's findings, not proof that the authors have released nothing elsewhere.

Namesakes excluded after reading their cards: SWE-Lego / Terminal-Lego (software engineering), LegoEnv (software tool environments), `bolinlai/LEGO-Dataset` (egocentric action generation), and Bricker (RAW flicker-banding restoration).

## What the network report means

[data/link-check.json](../data/link-check.json) records the exact URL, final URL, HTTP status, curl error and check time. It is an automated **HEAD** audit. It does not establish that a 200 response is the intended page: maintenance pages, login pages and bot challenges can also return 200.

The expansion checks only newly added URLs. Those records have individual `checked_at` timestamps; `last_incremental_check` does not imply that older records were rechecked.

The catalog's `checked` field is a review date, not a claim that every linked archive was downloaded successfully. An upstream README linking a cloud archive establishes a published entry point; it does not verify the entire archive's current contents.

## Material limitations

- **BrickNet:** the main dataset is explicitly gated by an author request form. Public geometry assets and source code are separate from access to the training corpus.
- **LEGO Co-builder:** the author-linked README is minimal; no complete replication recipe or dataset manifest was established.
- **DailyBrick:** a paper, public project page and demo were found. The website repository is not presented as an algorithm implementation release.
- **Arvin Bricks:** identified in the TPRU paper, but a dependable canonical channel URL and the 36-video manifest were not resolved. No guessed URL was added.
- **BrickLink Studio:** redirected to a maintenance notice during review. The stable product URL is retained with a dated note.
- **Most Wiedzy and Rebrickable:** automated access encountered restrictions. Their existence or purpose is supported by source records, but data-download success is unresolved.
- **B200C:** the creator's repository documents the dataset; Kaggle returned 404 to HEAD and no readable page content through the web reader. A working download was not established.
- **SCANet:** the former project site returned 404. The catalog instead links the author supplement repository and its hosted demo. The supplement README's “Code” link actually leads to a video, so it is not treated as an implementation release.
- **LTRON / BrickSim:** version and environment requirements were inspected; neither simulator was installed or executed.

No model weights, full datasets, third-party PDFs or video files are mirrored in this repository. Research results are summarized as reported by their authors; this task does not independently reproduce their numerical claims.

## Refresh

```bash
python3 scripts/check_links.py
python3 scripts/validate.py
```

Review failed or redirected entries manually before deleting them. HTTP errors can reflect temporary access policy; a successful HTTP response cannot substitute for checking the actual artifact. Update the per-entry date and notes when the content has been inspected again.
