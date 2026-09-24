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

Trained on 5,400 images — **300 from every one of the 18 folders**, so each item
carries equal weight and no single fruit dominates.

## Honest limits

- **Binary: `fresh` or `spoiled`.** There is no `spoiling` class, because the source
  data has no "partly gone" category. The app's amber **"Use soon"** state is
  therefore only reachable by tapping it, or by training your own 3-class model with
  `fresh` / `spoiling` / `spoiled`.
- **Only those nine items.** No leafy greens, no berries, no bread. Anything outside
  the list still gets forced into fresh-or-spoiled — a binary classifier has nowhere
  else to put it — so it can be confidently wrong on an unseen item.
- **Accuracy:** 97.4% on a held-out split (fresh 97.5%, spoiled 97.3%). A 60-image
  re-check through the actual Teachable Machine loader in a browser scored 60/60,
  but that sample is small — trust the 97.4%. Real-world accuracy on your own
  produce, lighting and background will be lower.
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
