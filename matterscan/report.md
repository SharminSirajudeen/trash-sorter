# MatterScan — What's It Made Of, and Where Does It Go?
### One app, two modes: e-waste triage and plastic-code sorting

**Author:** [Your Name]
**Event:** EDGE — Employability Development & Growth through Education · Level Expo, 3–4 Dec 2026
**Theme:** Reusability · Sustainability · Technology for resource-efficient solutions

> Placeholders in `[ ]` are for you to complete. Fill Results from your own
> testing — no invented numbers.

---

## Abstract

Two everyday sorting problems send recoverable material to landfill. First,
**e-waste** — the fastest-growing waste stream — is often binned with household
rubbish, even though it contains hazards (lithium batteries) and valuable,
recoverable metals (gold, copper, rare earths). Second, **plastic confusion** —
the resin code stamped on packaging is tiny and poorly understood, so recyclable
plastics get thrown away and non-recyclables contaminate recycling. **MatterScan**
answers one question — *what is this made of, and where does it go?* — in two
modes. In **Electronics** mode a camera and a neural network identify a device and
flag it as e-waste with specific, baked guidance (hazard, recoverable materials,
disposal route). In **Plastics** mode a reliable tap pad of resin codes 1–7 returns
accurate recyclability information. The app runs entirely in the browser, works
offline after first load, and is fully usable with no trained model and no API key
— so the live demo is dependable.

---

## Objectives

1. Identify an electronic device from a live camera feed and flag it as e-waste.
2. Show *why it matters*: the hazard, the recoverable materials, and the correct
   disposal route.
3. Give trustworthy plastic-recyclability information for resin codes 1–7.
4. Make it **instant and unmistakable** with a colour-flooded verdict.
5. Track a live "booth impact" tally for the presentation.
6. Run **on-device and offline**, and stay fully demoable with **no model and no
   key**.

## Problem and EDGE fit

- **Reusability / urban mining** — e-waste is a source of recoverable gold,
  copper and rare metals. Getting devices to the right place keeps those materials
  in use instead of mined afresh. MatterScan makes the recoverable content vivid.
- **Sustainability** — correct plastic sorting cuts both landfill and the
  contamination that spoils whole recycling batches; correct e-waste handling
  avoids battery fires and toxic leachate.
- **Resource-efficient technology** — it runs in a browser on a phone people
  already own; no server, no install.

## Methodology — two modes, two deliberate strategies

MatterScan treats the two problems differently *on purpose*, because they have
different reliability characteristics.

### Electronics — computer vision
MobileNet (a convolutional neural network trained on millions of photos)
identifies the device on screen. A rule flags anything electronic as **e-waste**
and shows baked, device-specific guidance: the hazard, a short list of recoverable
materials shown as labelled chips ("urban mining" made concrete), and the correct
disposal route. Non-electronic items are named and the user is pointed to Plastics
mode. A verdict only changes after a reading holds for **two consecutive frames**
(flicker smoothing). Optionally, a Teachable Machine model trained on the student's
own devices can replace MobileNet.

### Plastics — tap-first, by design
The resin stamp inside the ♻ triangle is only about **2–3 mm** and is unreliable to
read from a webcam. Rather than pretend otherwise, MatterScan is **tap-first**: the
user taps the number (1–7) and gets accurate, baked data every time — abbreviation
(PET, HDPE, …), common examples, a colour-coded recyclability status (green widely
/ amber sometimes / red rarely), what it becomes when recycled, and a handling tip.
This is a deliberate reliability choice: a confident wrong answer is worse than a
reliable tap. Optionally, a Teachable Machine model trained on the seven symbols
(classes named 1–7) can auto-highlight the code when the camera is on.

### Why the optional models work with so little data — transfer learning
Both optional models use **transfer learning**: they reuse MobileNet's already-
learned understanding of images and only re-train the final layer for the new
classes (the student's devices, or the seven resin symbols). Because the general
visual learning is already done, roughly **30–50 photos per class** is enough.

### Baked vs optional-live AI
All guidance — the per-device e-waste advice and the full seven-code plastic table
— is **AI-authored knowledge frozen into the app**. It works offline and never
fails. An **optional** live mode (off by default) can call an OpenAI-compatible API
for open-ended advice on the exact item; any failure falls back silently to the
baked content, so the demo never depends on it.

## Technologies used

| Technology | Role | Why chosen |
|---|---|---|
| **TensorFlow.js** | Runs the neural network in the browser | On-device, no server, nothing uploaded |
| **MobileNet** | Identifies devices in Electronics mode | Small and fast enough for a phone |
| **Teachable Machine** | Optional custom models (devices; resin codes) | Transfer learning, no coding |
| **HTML / CSS / vanilla JS** | The whole app, one file | No build step; static hosting |
| **Optional OpenAI-compatible API** | Optional live advice | Off by default; demo independent of it |

## How to run

1. **Locally:** open `index.html` in a modern browser; allow the camera for
   Electronics mode. First load fetches the models over the internet (~14 MB),
   then caches them.
2. **Hosted:** publish to GitHub Pages (see `README.md`).
3. **No model, no key:** Plastics mode works entirely by tapping; Electronics mode
   uses the default MobileNet — no training required.

## Results

> Fill from your own testing.

**Electronics** — test 6–8 devices in good light; record what MobileNet named it,
whether it was flagged as e-waste, and the confidence.

| Device | Named as | Flagged e-waste? | Confidence | Notes |
|---|---|---|---|---|
| Phone | [ ] | [ ] | [ ]% | [ ] |
| Mouse | [ ] | [ ] | [ ]% | [ ] |
| Keyboard | [ ] | [ ] | [ ]% | [ ] |
| Headphones | [ ] | [ ] | [ ]% | [ ] |
| Remote | [ ] | [ ] | [ ]% | [ ] |

**Plastics** — confirm each tapped code shows the correct abbreviation and
recyclability. (This is fixed baked data, so it will be consistent.)

## Limitations (honest)

- **Look-alikes** fool vision models — an object recogniser can misname an unusual
  device or miss one it hasn't seen.
- **MobileNet's vocabulary is fixed** — some devices aren't in it and fall back to
  generic e-waste guidance (still correct in direction).
- **Recycling rules vary by locality** — the plastic recyclability shown is the
  general picture; the correct bin can differ by council/region.
- The resin code must be read by a human (or a trained model); MatterScan does not
  claim to read the 2–3 mm stamp reliably from a webcam — that's why it's tap-first.
- MatterScan is a **guide**, not an official waste authority.

## Conclusion

MatterScan shows that matching the *method* to the *problem* beats forcing one
approach everywhere: vision where it's reliable (recognising a device), a tap-first
lookup where vision isn't (a 2–3 mm resin stamp). It makes two invisible things
visible — the recoverable materials inside e-waste, and the real recyclability of a
plastic — and keeps a live impact count for the booth. It runs on a phone, offline,
from a single link, and is fully demoable with nothing trained and no API key.

**Future work:** broaden the device vocabulary with a custom model; add local-rule
presets for plastics by region; and let the booth share a combined diverted-from-
landfill total across the day.

## References

> Format to your institution's required style.

1. Howard, A. G. *et al.* (2017). *MobileNets.* arXiv:1704.04861.
2. Sandler, M. *et al.* (2018). *MobileNetV2.* arXiv:1801.04381.
3. TensorFlow.js. https://www.tensorflow.org/js
4. Google Teachable Machine. https://teachablemachine.withgoogle.com
5. Forti, V. *et al.* (2020). *The Global E-waste Monitor 2020.* UNU/UNITAR & ITU.
6. Society of the Plastics Industry — resin identification codes (1–7).

---

## Q&A prep — likely examiner questions

**1. Why two modes instead of one?**
Because the two problems have different reliability. A device is big and
distinctive — vision works. A resin code is a 2–3 mm stamp — vision is unreliable,
so I made plastics tap-first for accuracy.

**2. Why tap-first for plastics — isn't camera more impressive?**
A confident wrong answer is worse than a reliable one, especially in a live demo.
Tapping the number gives correct data every time; the camera is an optional extra
if you train a model on the symbols.

**3. How does it know a device is e-waste?**
MobileNet names the device; a rule flags anything electronic as e-waste and shows
baked guidance for it. Non-electronic items are sent to Plastics mode.

**4. What is transfer learning?** ⭐
Reusing a network that already understands images and only re-training its last
layer for new classes. It's why the optional models need only ~30–50 photos per
class instead of hundreds of thousands.

**5. Where does the materials list come from?**
It's baked, AI-authored knowledge per device — the battery, the circuit board with
gold and copper, the plastics — to make the "urban mining" point concrete.

**6. Is anything uploaded?**
No. Recognition runs on-device in the browser. The optional live-advice feature is
off unless someone adds their own API key.

**7. What if it misidentifies a device?**
Look-alikes can fool any vision model. If it's electronic but unrecognised, it
falls back to generic e-waste guidance, which is still the right direction. I'm
honest about this limit.

**8. Do the plastic rules apply everywhere?**
The recyclability shown is the general picture; local rules vary, so I present it
as guidance and say so on screen.

**9. Why does it need the internet at first?**
Only to download the models once (~14 MB); then it caches and runs offline.

**10. What's the booth-impact number?**
A running count of items scanned and items correctly diverted from landfill (any
e-waste, or a recyclable plastic). It's a presentation aid, clearly labelled.

**11. Is the live-AI feature required?**
No — off by default, constrained to recycling advice, silent fallback on any error.
The demo never depends on it.

---

## 60-second demo script

1. **(0–10s)** "E-waste is the fastest-growing waste stream, and plastic codes
   confuse everyone. MatterScan handles both." Show the two-mode toggle.
2. **(10–30s)** Electronics: point at a phone → screen floods **red**, "E-WASTE",
   hazard badge (lithium battery), and chips showing the gold, copper and battery
   inside — "this is urban mining." Point at a mouse → still e-waste, its own guidance.
3. **(30–45s)** Switch to Plastics: tap **1** → green, "PET, widely recycled,
   becomes new bottles and fleece." Tap **6** → red, "PS, rarely recycled." "The
   stamp is 2 mm, so tapping is the reliable choice — that's a deliberate decision."
4. **(45–60s)** Point at the booth tally growing: "Every correct call is one item
   kept out of landfill. It runs on the phone, offline, from one link." End on the
   number.
