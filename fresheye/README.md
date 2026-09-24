# FreshEye — See What's Still Good

A single-file web app that uses your camera to check whether fruit and veg is
**fresh**, **use soon**, or **spoiled**, then suggests how to use it up — so food
gets eaten, not binned. It runs entirely in the browser (TensorFlow.js), works
offline after the first load, and needs no server.

Built for the EDGE sustainability expo: reusability, sustainability, and
technology for resource-efficient solutions.

## What it does

- **Identifies** the produce with MobileNet (e.g. "banana", "apple").
- **Judges freshness** from either your own trained model *or* three manual
  buttons — the app is fully usable with the manual buttons alone.
- **Colour-floods** the screen green / amber / red so the verdict reads across a
  room.
- **Advises**: a built-in rescue idea + storage tip for the item and its state.
- **Tallies impact**: a running, clearly-labelled *estimate* of food and CO₂e
  saved (see the report for the source and assumptions).

Nothing is uploaded. All recognition happens on your device.

## Run it locally

1. Open `index.html` in a modern browser (Chrome works best).
2. Allow the camera when prompted.
3. First load fetches the models over the internet (~14 MB), then caches them.

You can also use it with **no camera and no model** — just tap the freshness
buttons to see the advice, colours, and impact tally work.

> The ML libraries load from a CDN at runtime **by design**. That external fetch
> is expected and correct — do not try to bundle or vendor it. The only time
> you'll see a load error is if you're offline before the models have cached.

## Automate freshness — train your own model (~20 min, free)

Freshness can't come from MobileNet (a banana is a banana, ripe or rotten). To
automate the freshness verdict, train a small model on real photos:

1. Go to [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com)
   → **Image Project** → **Standard image model**.
2. Create three classes, named **exactly**: `fresh`, `spoiling`, `spoiled`.
3. Add **30–50 varied photos** to each — different items, angles, lighting, and
   backgrounds. (For best results, use the produce you'll actually demo.)
4. Click **Train Model**, then **Export Model → Tensorflow.js → Upload (shareable
   link)** and copy the URL.
5. In FreshEye, open **Settings & training**, paste the link, and press **Use
   model**. The badge changes to "Freshness: your model".

This uses **transfer learning** — it reuses MobileNet's general image knowledge
and only learns your three classes, which is why so few photos are enough.

## Optional: live rescue ideas (off by default)

FreshEye ships with built-in offline tips that always work. Optionally, in
Settings, you can paste an OpenAI-compatible API key to enable a "Fresh idea"
button that writes a tip for the exact item. Details:

- Off unless you add a key. **The demo does not depend on it.**
- Your key is stored **only in this browser** and is sent only to the endpoint you
  set. It is never committed or logged.
- 10-second timeout; any error falls back silently to the built-in tip.
- The request uses a constrained prompt so the model only answers about using up
  food.

## Publish to GitHub Pages

1. Create a new **public** repo and upload `index.html` (and this `README.md` /
   `report.md`).
2. Repo **Settings → Pages** → Source: **Deploy from a branch** → Branch: **main**
   / **/(root)** → **Save**.
3. Wait ~1 minute, then open `https://<your-username>.github.io/<repo-name>/`.

Open the link once on wifi (with your model loaded, if you trained one) so
everything caches before offline use at the expo.

## Files

- `index.html` — the whole app (no build step, no dependencies to install).
- `report.md` — project report with Q&A prep and a 60-second demo script.
- `README.md` — this file.
