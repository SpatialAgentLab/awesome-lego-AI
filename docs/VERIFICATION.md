# Verification / 核验说明

Review date: **2026-11-22**.

## What was reviewed

- The two seed papers, their author repositories and available dataset links.
- Primary paper abstracts, project descriptions, repository READMEs and data records for the added research entries.
- Renamed projects and overlapping assets: LegoGPT / BrickGPT and StableText2Lego / StableText2Brick are each treated as one project / dataset family.
- Dataset scope: TPRU's reported total is multi-domain; MobileBrick concerns reconstruction; conveyor videos concern sorting; public channels are source leads rather than released training datasets.
- Local Markdown links, anchors, duplicate resource IDs, citation coverage and consistency between the JSON catalog and generated READMEs.

The linked primary pages are the evidence for each entry. The original awesome list provided discovery leads and organizational inspiration; descriptions here were rewritten and research facts checked against original sources where available. Access restrictions and sparse documentation are explicitly recorded rather than silently treated as confirmation.

## What the network report means

[data/link-check.json](../data/link-check.json) records the exact URL, final URL, HTTP status, curl error and check time. It is an automated **HEAD** audit. It does not establish that a 200 response is the intended page: maintenance pages, login pages and bot challenges can also return 200.

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
