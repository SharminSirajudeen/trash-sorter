# Training Your Own Trash Model — Step by Step

This is the part that earns the marks: a model **you** trained on **real waste
photos**, so SortRight becomes a true trash classifier instead of a general
object recogniser. It takes about 20 minutes and needs no coding.

> You will do this in a web browser (Chrome works best), signed into a Google
> account. Have your items ready: a few examples for each bin you want to
> support.

---

## Before you start: the class names matter

SortRight maps your model's class names straight to bins. **Name your classes
exactly like this** (all lowercase, no spaces), and skip any bin you don't need:

| Class name to type | Bin it maps to |
|---|---|
| `plastic` | Plastic |
| `paper` | Paper & Card |
| `metal` | Metal |
| `glass` | Glass |
| `organic` | Organic / Compost |
| `ewaste` | E-waste |
| `trash` | General Waste |

If a photo doesn't match any class well, the app falls back to **General
Waste**, so it always gives an answer.

**Tip — add a `nothing` / background class.** Make one extra class called
`trash` (or `nothing`) and give it photos of your empty hand, the table, and the
background with no item. This stops the model from confidently "recognising" an
empty frame as a bin, which looks much more polished in a live demo.

---

## Step 1 — Open Teachable Machine

Go to **https://teachablemachine.withgoogle.com** → **Get Started** →
**Image Project** → **Standard image model**.

## Step 2 — Create one class per bin

- Rename "Class 1" to `plastic`, "Class 2" to `paper`, and so on — using the
  exact names from the table above.
- Click **Add a class** for each additional bin you want.
- Only include bins you actually have items for. A model with `plastic`,
  `paper`, `metal`, `glass`, and `trash` is perfectly good if that's what you
  have.

## Step 3 — Add photos to each class (the important step)

For **each** class, click **Webcam** and hold the item up while it records, or
upload photos. Aim for **30–50 images per class**, and make them varied:

- **Different angles** — turn the item as it records.
- **Different distances** — close and a bit further back.
- **Different lighting** — near a window, under room light.
- **Different backgrounds** — not always the same tabletop.
- **Different examples** — two or three different bottles, not just one.

Variety is what makes the model robust. Fifty near-identical photos are worth
less than thirty varied ones.

## Step 4 — Train

Click **Train Model**. Leave the browser tab open and in the foreground while it
trains (it takes under a minute for this size). Do not switch tabs during
training.

## Step 5 — Test it right there

Use the **Preview** panel on the right to hold up items and check it. If a class
is weak (keeps getting confused), go back and add more varied photos to that
class, then train again. A few iterations here pay off.

## Step 6 — Export and get the link

1. Click **Export Model** (top right of the Preview panel).
2. Choose the **Tensorflow.js** tab.
3. Select **Upload (shareable link)**.
4. Click **Upload my model** and wait for it to finish.
5. **Copy the shareable link** it gives you. It looks like:
   `https://teachablemachine.withgoogle.com/models/XXXXXXXX/`

## Step 7 — Use it in SortRight

1. Open SortRight (the live link, or `index.html`).
2. Open the section **"Use your own trash-trained model"**.
3. Paste your link into the box and press **Use my model**.
4. The badge at the top should change to **Model: your trash model**, and the
   status line confirms how many classes loaded.
5. Turn on the camera and test with real items.

SortRight remembers your link on that device, so next time it loads your model
automatically. Press **Back to general** to switch back to MobileNet.

---

## Before the expo — make it work offline

The first time the page loads, it fetches the model over the internet; after
that the browser caches it. To be safe on the day:

1. On known wifi, open SortRight and load your trash model.
2. Turn the camera on once so everything is fetched.
3. Then test with wifi **off** — reload and confirm it still runs.

Do this the night before, on the actual device you'll demo with.

---

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| "Couldn't load that model" | Link isn't the uploaded shareable link, or it's an audio/pose model | Re-export as **Standard image model → Tensorflow.js → Upload (shareable link)** and copy the full URL |
| Badge still says "general" | The model didn't finish loading | Check the status line for an error; confirm you pressed **Use my model** |
| Camera button greyed out | The general model hasn't finished downloading yet | Wait a few seconds on first load; it enables once ready |
| Everything reads as one bin | Not enough variety, or a class is over-represented | Add more varied photos to the weak classes and re-train |
| Confident wrong answer on empty frame | No background class | Add a `trash`/`nothing` class with empty-scene photos and re-train |
