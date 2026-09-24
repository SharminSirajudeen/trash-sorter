# Built-in demo freshness model — NOT the student's own model

FreshEye loads this automatically so the app can judge freshness itself instead of
asking the user. It is a **pre-built baseline**, not part of the graded work: it was
trained by Claude Code on a public dataset, not by the student.

**For the project marks, train your own model** (see `../README.md`). Yours is the
defensible one — your items, your lighting, and an honest answer when an examiner
asks "did you train this?". A model you load in Settings always overrides this one,
and the badge at the top says which is active:

- `Freshness: your model` — your trained model (what you want on demo day)
- `Freshness: built-in demo model` — this file
- `Freshness: manual` — no model; you tap the buttons

## What it covers

Nine fruits **and vegetables**, each in fresh and rotten form:

🍎 apple · 🍌 banana · 🍊 orange · 🥒 cucumber · 🍅 tomato · 🥔 potato ·
🫑 capsicum · 🌿 okra · 🥬 bitter gourd

Plus a third class, **`notproduce`**, so the app refuses things that aren't fruit or
vegetables instead of confidently calling a bottle "fresh". When the model is at
least 50% sure an item isn't produce, FreshEye shows **"Not produce"**, gives no
freshness verdict, and won't let you log it.

Trained on 7,537 images: 2,700 fresh + 2,700 spoiled (300 from each of the 18
produce folders, so no single item dominates) and 2,137 non-produce images from
[TrashNet](https://github.com/garythung/trashnet) — bottles, cans, paper, glass and
general packaging.

**Accuracy:** 98.3% overall — fresh 97.9%, spoiled 97.6%, notproduce **99.7%**.
A 75-image re-check through the actual Teachable Machine loader scored 75/75, but
that sample is small; trust the 98.3%.

### What the guard does *not* cover

The non-produce class is **packaging and household objects**. It does **not**
include hands, faces, clothing or empty rooms, so pointing the camera at your hand
may still get a freshness verdict. Widening it needs non-produce images of those
things. Say this plainly if asked — it's a data limitation, not a bug.

## Honest limits

- **The model itself is binary: `fresh` or `spoiled`** — the source data has no
  "partly gone" category. The app still produces the amber **"Use soon"** state by
  reading the model's *uncertainty* rather than a trained class: the model outputs a
  probability, and when that probability sits near the decision boundary (30–70%
  spoiled) the item is between states, so FreshEye shows "Use soon" and displays
  `borderline — model is torn (NN% spoiled)`. Outside that band it commits to fresh
  or spoiled.
  This is a **deliberate heuristic, not a trained class** — say so if asked. It is a
  good Q&A point: it shows the model returns probabilities, not certainties, and that
  a threshold turns those into decisions. A model trained with its own `spoiling`
  class is detected automatically and used directly, skipping the band entirely.
  The thresholds are `SPOILING_LO` / `SPOILING_HI` in `index.html` if you want to
  widen or narrow the amber zone.
- **Only those nine items.** No leafy greens, no berries, no bread. An unseen fruit
  or vegetable is still forced into fresh-or-spoiled, so it can be confidently wrong
  there. (Clearly non-produce objects are caught by the `notproduce` class above.)
- **Real-world accuracy will be lower** than the figures above. Those are measured on
  held-out images from the same datasets; your own produce, lighting and backgrounds
  are harder.
- **Architecture:** MobileNetV2 feature extractor (frozen, ImageNet weights) + a small
  trained head — transfer learning, the same technique Teachable Machine uses.
  Exported in Teachable Machine format so the app loads it with no special code.

## Reproducing it

Dataset (~3 GB, not committed — far too large for a Git repo):

```bash
curl -L -o freshness_fruit.zip \
  https://huggingface.co/datasets/Densu341/Fresh-rotten-fruit/resolve/main/freshness_fruit.zip
unzip freshness_fruit.zip          # -> dataset/Train/{fresh,rotten}<item>/
```

Public Hugging Face mirror, no login required. `train_fresh.py` next to this file is
the exact script used: it samples 300 images per folder, extracts MobileNetV2
embeddings, trains a small head, and exports in Teachable Machine format.

A smaller 3-fruit alternative (apple/banana/orange only) is at
https://github.com/Bangkit-JKT2-D/fruits-fresh-rotten-classification
