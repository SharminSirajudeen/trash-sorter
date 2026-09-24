# Pre-built demo fallback model — NOT the student's own model

This folder is a **pre-built safety net**, not part of the graded work. It is a
baseline waste classifier that **Claude Code trained on the public
[TrashNet](https://github.com/garythung/trashnet) dataset** (transfer learning on
MobileNetV2), exported in Teachable Machine format so SortRight can load it.

**For the project marks, train your own model** (see `docs/TRAINING_GUIDE.md`). Your
own model is the defensible one — you trained it, on your own items, and can explain
it. If an examiner asks "did you train this?", the answer must be about *your* model,
not this one.

## What it is

- **Classes:** `plastic`, `paper`, `metal`, `glass`, `trash` (→ General Waste).
  It has **no organic or e-waste** classes — TrashNet doesn't include them — so it's
  only a partial fallback.
- **Validated accuracy:** ~90% on a held-out split of TrashNet (verified loading in
  the Teachable Machine loader in a browser). Real-world accuracy on your own items,
  lighting and backgrounds will be lower — which is exactly why training your own
  model matters.

## How to use it (only as a backup)

If your own model or the network fails on demo day, you can fall back to this one:

1. Open SortRight and expand **"Use your own trash-trained model"**.
2. Paste this URL and press **Use my model**:
   `https://sharminsirajudeen.github.io/trash-sorter/model/`
3. Load it once on wifi beforehand so it caches for offline use.

It is **not auto-loaded** — SortRight defaults to general mode / your own model, on
purpose, so this pre-built model never silently stands in for your work.
