# Built-in demo freshness model — NOT the student's own model

FreshEye loads this automatically so the app can judge freshness itself instead of
asking the user. It is a **pre-built baseline**, not part of the graded work: it was
trained by Claude Code on a public dataset, not by the student.

**For the project marks, train your own model** (see `../README.md`). Yours is the
defensible one — your items, your lighting, and an answer you can give honestly when
an examiner asks "did you train this?". A model you load in Settings always
overrides this one, and the badge at the top says which is active:

- `Freshness: your model` — your trained model (what you want on demo day)
- `Freshness: built-in demo model` — this file
- `Freshness: manual` — no model; you tap the buttons

## What it is

- **Classes:** `fresh`, `spoiled` — **binary**. There is no `spoiling` class, because
  the source dataset has no "partly gone" category. The app's **"Use soon"** state is
  therefore only reachable by tapping it manually, or by training your own 3-class
  model with `fresh` / `spoiling` / `spoiled`.
- **Fruits:** apples, bananas and oranges **only**. It will be unreliable on anything
  else — a tomato or a bag of spinach is outside what it has ever seen.
- **Accuracy:** 96.9% on a held-out split during training, and 97.5% (39/40) when
  re-checked by actually loading it in the Teachable Machine loader in a browser.
  Real-world accuracy on your own fruit, lighting and background will be lower.
- **Architecture:** MobileNetV2 feature extractor (frozen, ImageNet weights) + a small
  trained head — i.e. transfer learning, the same technique Teachable Machine uses.
  Exported in Teachable Machine format so the app loads it with no special code.

## Reproducing it

Dataset (~3.7 GB, not committed — far too large for a Git repo):

```bash
git clone --depth 1 https://github.com/Bangkit-JKT2-D/fruits-fresh-rotten-classification
```

Originally from Kaggle: *"Fruits fresh and rotten for classification"* by **sriramr** —
https://www.kaggle.com/datasets/sriramr/fruits-fresh-and-rotten-for-classification
(13,599 images: apple / banana / orange, each fresh and rotten).

The training script used to produce this model is in `train_fresh.py` next to this
file. It samples 1,200 images per class, extracts MobileNetV2 embeddings, trains a
small head, and exports in Teachable Machine format.
