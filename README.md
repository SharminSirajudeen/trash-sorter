# SortRight — Smart Waste Sorter

Live in-browser waste classifier for the EDGE sustainability expo. Point a
phone or webcam at an item; it recognises the object with MobileNet (TensorFlow.js,
running entirely on-device) and shows the correct recycling bin.

## Publish it (GitHub Pages, ~3 min)
1. Create a new **public** repo.
2. Upload `index.html` (this folder).
3. Repo **Settings → Pages** → Source: **Deploy from a branch** → Branch: **main** / **/(root)** → Save.
4. Wait ~1 min, then open `https://<your-username>.github.io/<repo-name>`.

First load needs internet to fetch the model (~14MB); it caches after that.
Open the link once on known wifi before the expo so it's ready offline.
