# FreshEye — See What's Still Good
### A camera app that checks food freshness to cut household food waste

**Author:** [Your Name]
**Event:** EDGE — Employability Development & Growth through Education · Level Expo, 3–4 Dec 2026
**Theme:** Reusability · Sustainability · Technology for resource-efficient solutions

> Placeholders in `[ ]` are for you to complete. The Results section must be
> filled from your own testing — do not use invented numbers.

---

## Abstract

Roughly a third of all food produced is thrown away, and food waste is one of
the largest single contributors to global greenhouse-gas emissions. A lot of
that waste is avoidable: food gets binned simply because no one was sure whether
it was still good, or knew what to do with it before it turned. **FreshEye**
tackles that moment. It is a web app that uses a phone or laptop camera to
identify a piece of fruit or vegetable, show at a glance whether it is **fresh**,
**use soon**, or **spoiled** — flooding the screen with green, amber or red — and
then suggest a concrete way to use it up plus a storage tip. It also keeps a
running, clearly-labelled estimate of the food and CO₂e the user has saved. The
whole app runs in the browser with nothing uploaded, works offline after the
first load, and is fully usable with a simple manual freshness control before any
machine-learning model is trained — so it is dependable for a live demo.

---

## Objectives

1. Identify a produce item from a live camera feed.
2. Communicate its freshness **instantly and unmistakably** through colour, so
   the answer reads across a room.
3. Turn that into action: a short, practical "use it up" idea and a storage tip.
4. Make the value tangible with a live, honestly-estimated impact tally.
5. Run entirely **on-device**, offline-capable, installable from a single link.
6. Guarantee a **reliable demo**: fully functional with a manual freshness
   fallback, before any custom model exists.

## Problem and EDGE fit

Food waste wastes everything that went into growing, transporting and storing the
food — water, energy, land — and then emits methane as it rots in landfill. The
avoidable part is often a knowledge gap at home: *is this still okay, and what do
I do with it?* FreshEye closes that gap in a second.

- **Reusability** — it helps people actually *use* food they already have instead
  of discarding it, and suggests ways to rescue items that are on the turn.
- **Sustainability** — less food waste means fewer emissions and less pressure on
  the resources behind food production.
- **Resource-efficient technology** — it runs on hardware people already own, in a
  browser, with no server and no install. The computation is light enough for a
  phone.

## Methodology — the pipeline

Every camera frame goes through three stages, all on the device:

1. **Identify** — MobileNet (a convolutional neural network trained on millions
   of photos) names the produce, e.g. "banana", with a confidence score.
2. **Judge freshness** — freshness *cannot* come from MobileNet: a banana is
   classed as a banana whether it is ripe or rotten. So the freshness verdict
   comes from one of two sources:
   - **Primary — a custom Teachable Machine model**, trained on
     fresh/spoiling/spoiled photos, whose prediction drives the verdict.
   - **Fallback — a manual control**: three large buttons (Fresh / Use soon /
     Spoiled). The app is completely usable this way with no model at all.
3. **Advise** — the item and its freshness state are matched to a built-in rescue
   idea and storage tip (e.g. an overripe banana → "mash into banana bread";
   wilting spinach → "blend into soup").

To keep the display steady during a live demo, a verdict only changes after a
reading has held for **two consecutive frames** (flicker smoothing).

### Why a separate freshness model — transfer learning, simply

Training an image network from scratch needs hundreds of thousands of photos.
The custom freshness model avoids that using **transfer learning**: Teachable
Machine starts from a network that has *already* learned general image features
(edges, textures, shapes) and only re-teaches the final layer to tell *fresh*,
*spoiling* and *spoiled* apart. Because the hard, general learning is already
done, roughly **30–50 photos per class** is enough. This is the single most
important concept to be able to explain.

## Technologies used

| Technology | Role | Why chosen |
|---|---|---|
| **TensorFlow.js** | Runs the neural networks in the browser on the device's GPU | No install, no server, nothing uploaded |
| **MobileNet** | Identifies the produce | Small and fast enough for a phone browser |
| **Teachable Machine** | Trains the custom freshness model (transfer learning) | No coding; few images needed |
| **HTML / CSS / vanilla JS** | The whole application, one file | No build step, hosts as a static file anywhere |
| **Optional: an OpenAI-compatible API** | Optional live "fresh idea" generation | Off by default; the app never depends on it |

## How to run

1. **Locally:** open `index.html` in a modern browser (Chrome recommended). Allow
   the camera when asked. The first load fetches the models over the internet
   (~14 MB) and then caches them.
2. **Hosted:** publish `index.html` to GitHub Pages (see `README.md`) and open the
   live URL on a phone.
3. **Without any model or key:** turn on the camera (or not) and use the three
   manual freshness buttons — the full pipeline (advice, colour, impact tally)
   works immediately.

## Results

> Fill this in from your own testing. Do not invent figures.

Test 5–6 items per freshness state in good light. For each, record the produce
FreshEye named, the verdict source (model or manual), whether the verdict was
sensible, and the confidence shown.

| Item | Named as | Freshness (source) | Sensible? | Notes |
|---|---|---|---|---|
| Ripe banana | [ ] | [ ] | [ ] | [ ] |
| Overripe banana | [ ] | [ ] | [ ] | [ ] |
| Fresh apple | [ ] | [ ] | [ ] | [ ] |
| Wrinkled apple | [ ] | [ ] | [ ] | [ ] |
| Fresh tomato | [ ] | [ ] | [ ] | [ ] |
| Soft tomato | [ ] | [ ] | [ ] | [ ] |

Report: how reliably produce was identified, how well the freshness model (if
trained) matched your own judgement, and which items were hardest.

## Limitations (state these honestly)

- **Freshness is genuinely hard from a photo.** Surface look doesn't always match
  internal state; a smooth skin can hide a spoiled interior.
- **MobileNet only knows common produce**, and some items (e.g. tomato, potato)
  aren't in its vocabulary — it may mislabel them. Freshness and advice still
  work via the manual control.
- **Lighting and background** affect both identification and any freshness model.
- **The freshness model only knows what it was trained on** — train it on your own
  items, in realistic lighting, to make it reliable.
- FreshEye is a **guide, not a food-safety authority**. When in doubt, use normal
  judgement (smell, texture) and don't eat anything questionable.

## Impact estimate — and its source

FreshEye shows a running estimate, clearly labelled as an estimate, never as an
exact measurement:

- **Food saved** = items you logged as *rescued* (Fresh or Use soon) × an assumed
  **~0.15 kg per item** (a rough average weight for a piece of produce — this is
  an assumption, not a measured figure).
- **CO₂e avoided** = food saved × **~2.5 kg CO₂e per kg of food**, an approximate
  average carbon footprint across mixed foods.

The ~2.5 kg CO₂e/kg figure is an illustrative average; real values vary widely by
food type (from well under 1 for many vegetables to far more for meat and dairy).
It is drawn from published food-emissions research and should be cited as such,
with its uncertainty acknowledged:

- Poore, J. & Nemecek, T. (2018). *Reducing food's environmental impacts through
  producers and consumers.* Science, 360(6392), 987–992.
- WRAP (UK). *Food surplus and waste — emissions and reduction guidance.*
  https://www.wrap.ngo

Always present the tally as "estimated" and be ready to explain both assumptions.

## Conclusion

FreshEye shows that a small, well-scoped tool can make a real dent in an everyday
sustainability problem using only free technology and hardware people already
own. Its design deliberately separates the two questions — *what is this?*
(MobileNet) and *is it still good?* (a trained freshness model, or a human tap) —
which keeps it honest about what a camera can and cannot know. The manual
fallback guarantees a working demo, while the custom-model path demonstrates
transfer learning and a genuine freshness classifier. The live impact tally turns
an abstract benefit into a number an audience can watch grow.

**Future work:** broaden the produce vocabulary; train the freshness model on more
items and lighting; add per-item shelf-life bands; and let users share an
anonymised total impact across a class or event.

## References

> Format to your institution's required style before submitting.

1. Howard, A. G. *et al.* (2017). *MobileNets: Efficient CNNs for Mobile Vision
   Applications.* arXiv:1704.04861.
2. Sandler, M. *et al.* (2018). *MobileNetV2: Inverted Residuals and Linear
   Bottlenecks.* arXiv:1801.04381.
3. TensorFlow.js. https://www.tensorflow.org/js
4. Google Teachable Machine. https://teachablemachine.withgoogle.com
5. Poore, J. & Nemecek, T. (2018). *Reducing food's environmental impacts through
   producers and consumers.* Science, 360(6392), 987–992.
6. WRAP. *Food waste reduction resources.* https://www.wrap.ngo

---

## Q&A prep — likely examiner questions

**1. How does it know if food is fresh?**
Freshness doesn't come from the object recogniser — a banana is a banana ripe or
rotten. It comes from either a freshness model I trained on fresh/spoiling/spoiled
photos, or from the manual buttons. I separated "what is it" from "is it good".

**2. What is transfer learning, and why does it matter here?** ⭐
It's reusing a network that already understands images and only re-training its
final layer for my three freshness classes. The general visual learning is
already done, so I only need ~30–50 photos per class instead of hundreds of
thousands. It's why a first-year can train a working model in 20 minutes.

**3. Did you build the neural network yourself?**
I used MobileNet as the base — training from scratch needs huge datasets and
compute. My work is the app, the identify→judge→advise pipeline, the built-in
rescue knowledge, the impact model, and a freshness model I trained with transfer
learning.

**4. Is this real machine learning or just if-statements?**
The recognition is a real convolutional neural network. The advice step is a
lookup from item + freshness to a tip — that part is deliberately simple and
offline so the demo never fails.

**5. Where does the CO₂ number come from? Is it exact?**
No — it's clearly labelled an estimate: rescued items × ~0.15 kg each × ~2.5 kg
CO₂e per kg, an average food footprint from published research (Poore & Nemecek,
2018). Real values vary a lot by food; I present it as illustrative, not exact.

**6. Does my data or image get uploaded?**
No. All recognition runs on the device in the browser. Nothing is sent anywhere.
The optional "live idea" feature is off by default and only runs if someone adds
their own API key.

**7. What if it can't identify the item?**
Some produce isn't in MobileNet's vocabulary. Freshness and advice still work via
the manual buttons and a generic per-state tip, so the app is always usable.

**8. Why does it need the internet at first?**
Only to download the models once (~14 MB). After that the browser caches them and
it runs offline. All the actual work is on-device.

**9. How is this different from just looking at the food?**
It makes the call instant and consistent, gives a concrete rescue action most
people wouldn't think of, and — for the expo — turns saved food into a visible,
growing impact number.

**10. What are its limits?**
Freshness from a photo is genuinely hard, lighting matters, and it only knows what
it was trained on. It's a helpful guide, not a food-safety authority — I'm upfront
about that.

**11. Is the live-AI feature required?**
No. It's an optional extra, off by default, with a constrained prompt so it only
answers about using up food. Any error or timeout silently falls back to the
built-in tip. The demo never depends on it.

---

## 60-second demo script

1. **(0–10s)** "A third of food is wasted, and a lot of it is avoidable — people
   just aren't sure if it's still good. This is FreshEye." Hold up the phone.
2. **(10–30s)** Point at a fresh item → screen floods **green**, "Fresh — good for
   a few days", with a storage tip. Point at an overripe banana → **amber**, "Use
   soon — mash into banana bread."
3. **(30–45s)** "Freshness can't come from the object recogniser, so I trained my
   own model on fresh and spoiled photos using transfer learning — that's why 30
   to 50 photos per class is enough." Tap **Log this item** a few times.
4. **(45–60s)** Point at the impact tally: "Every rescued item adds to an estimated
   food-and-CO₂ saving. It runs entirely on the phone, offline, from a single
   link — no app, no server." End on the growing number.
