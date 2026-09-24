# SortRight — Smart Waste Sorter

Live in-browser waste classifier for the EDGE sustainability expo. Point a
phone or webcam at an item; it recognises the object and shows the correct
recycling bin. Everything runs on-device (TensorFlow.js) — nothing is sent to a server.

## Two modes
- **General (default):** MobileNet names the object (e.g. "water bottle") and a
  rule maps that name to a bin.
- **Your trash model (recommended):** a Teachable Machine model you train on real
  waste photos. Each class it predicts *is* a bin, so there's no guessing step.
  The badge next to the title shows which model is active.

## Train your own trash model (~20 min, free)
1. Go to [teachablemachine.withgoogle.com](https://teachablemachine.withgoogle.com) →
   New Project → **Standard image model**.
2. Make one class per bin and name them exactly:
   `plastic`, `paper`, `metal`, `glass`, `organic`, `ewaste`, `trash`
   (skip any you don't need). Anything unrecognised goes to General Waste.
3. Add 30–50 webcam photos per class: different angles, lighting, and backgrounds.
4. Click **Train Model**, then **Export Model → Upload (shareable link)** and copy the URL.
5. In the app, open **Use your own trash-trained model**, paste the link, and
   press **Use my model**.

The link is saved on that device, so the model reloads automatically next time.
Press **Back to general** to return to MobileNet.

## Publish it (GitHub Pages, ~3 min)
1. Create a new **public** repo.
2. Upload `index.html` (this folder).
3. Repo **Settings → Pages** → Source: **Deploy from a branch** → Branch: **main** / **/(root)** → Save.
4. Wait ~1 min, then open `https://<your-username>.github.io/<repo-name>`.

First load needs internet to fetch the models (~14MB for MobileNet, plus your
custom model if you use one); they cache after that. Open the link once on known
wifi before the expo, with your trash model loaded, so it's ready offline.
