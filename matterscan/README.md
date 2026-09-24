# MatterScan — What's it made of, where does it go?

One single-file web app, two modes, answering a materials question:

- **Electronics** — point the camera at a device; MobileNet recognises it and flags
  it as **e-waste**, with the hazard, the recoverable materials (battery, gold &
  copper board, metals), and the correct disposal route.
- **Plastics** — tap the resin code 1–7 stamped on the item and get accurate
  recyclability info: abbreviation, examples, whether it's widely / sometimes /
  rarely recycled, what it becomes, and a handling tip.

Everything runs in the browser (TensorFlow.js), works offline after first load, and
needs no server. Built for the EDGE sustainability expo.

## Why two modes work differently

A device is large and distinctive, so **camera vision** is reliable. A resin code
is a ~2–3 mm stamp, so reading it from a webcam is **not** reliable — MatterScan is
**tap-first** for plastics on purpose: a reliable tap beats a confident wrong guess.

## Run it locally

1. Open `index.html` in a modern browser (Chrome recommended).
2. For Electronics mode, allow the camera. First load fetches the models over the
   internet (~14 MB), then caches them.
3. **No training or key needed:** Plastics mode works entirely by tapping;
   Electronics mode uses the default MobileNet.

> The ML libraries load from a CDN at runtime **by design** — that external fetch
> is expected and correct; don't bundle or vendor it. You'll only see a load error
> if you're offline before the models have cached.

## Optional: train your own models (transfer learning, ~20 min each, free)

Both are optional — the app is fully usable without them.

**Devices (Electronics mode):**
1. [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com) →
   **Image Project** → **Standard image model**.
2. One class per device you want to recognise; 30–50 varied photos each.
3. **Train** → **Export → Tensorflow.js → Upload (shareable link)**; copy the URL.
4. In MatterScan → Settings → paste under "your own device model" → **Use**.

**Resin codes (Plastics mode):**
1. Same steps, but make **seven classes named exactly `1`–`7`**, each with photos of
   that resin symbol.
2. Paste the link under "your own code model". With the camera on, the matching code
   is auto-highlighted.

Both use **transfer learning** — reusing MobileNet's image knowledge and only
learning your classes — which is why ~30–50 photos per class is enough.

## Optional: live answers (off by default)

In Settings you can paste an OpenAI-compatible API key to enable an "Ask about this
item" button for open-ended disposal/upcycling advice. It's off unless you add a
key, the key is stored only in this browser and sent only to the endpoint you set
(never logged), there's a 10-second timeout, and any error falls back silently to
the built-in guidance. **The demo does not depend on it.**

## Publish to GitHub Pages

1. Create a new **public** repo and upload `index.html` (and `report.md` /
   `README.md`).
2. Repo **Settings → Pages** → Source: **Deploy from a branch** → Branch: **main**
   / **/(root)** → **Save**.
3. Wait ~1 minute, then open `https://<your-username>.github.io/<repo-name>/`.

Open the link once on wifi before the expo so the models cache for offline use.

## Colour theme

- **Shell:** graphite/steel dark base (`#0f1216` / `#171c22`) with a cyan accent
  (`#22b8cf`) — an "industrial / urban-mining" feel that makes the colour flood pop.
- **Electronics verdicts:** amber (`#f0a92f`) for standard e-waste, red (`#e5533c`)
  for high-hazard items (lithium batteries: phones, laptops, cameras, wireless
  headphones).
- **Plastics verdicts:** green (`#35b36a`) widely recycled, amber (`#e6a12e`)
  sometimes, red (`#d3503a`) rarely.

## Files

- `index.html` — the whole app (no build step, no dependencies to install).
- `report.md` — project report with Q&A prep and a 60-second demo script.
- `README.md` — this file.
