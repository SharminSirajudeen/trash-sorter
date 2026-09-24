# SortRight — Q&A Cheat Sheet

The goal is to **understand and defend**, not recite. Each concept below has a
plain explanation, a one-sentence version you can say out loud, and the likely
follow-up question with a good answer.

---

## The 30-second pitch (memorise this)

> "SortRight uses a camera and a neural network to tell you which recycling bin
> an item belongs in. You hold up a bottle or a can, and it instantly shows the
> right bin and colour. It runs entirely in the browser on your phone — nothing
> is uploaded — and I trained it on real waste photos so it's a genuine trash
> classifier, not just a lookup table."

---

## Core concepts

### 1. Convolutional Neural Network (CNN)
**Plain:** A program that learns to recognise images from lots of examples,
instead of following fixed rules someone wrote. It builds understanding in
layers — edges, then shapes, then whole objects.
**Say it:** "It's a network that learned what objects look like from thousands
of example photos, rather than me writing rules for every item."
**Likely follow-up — "Why a CNN and not just rules?"**
Because you can't write a rule that describes what a bottle *looks like* in every
angle and lighting. A CNN learns that from examples; that's why it generalises.

### 2. Transfer learning ⭐ (your strongest point)
**Plain:** Instead of training a network from scratch — which needs hundreds of
thousands of images — you start from one that already understands images in
general, and only re-teach its final layer to tell *your* categories apart.
**Say it:** "I didn't train from zero. Teachable Machine takes MobileNet, which
already knows what images look like, and just re-trains the last layer on my
waste photos. That's why 30–50 images per class is enough."
**Likely follow-up — "Why is so little data enough?"**
Because the hard part — learning general visual features like edges, textures,
shapes — is already done by the pre-trained network. I'm only teaching it the
final distinction between my specific bins, which is a much smaller job.

### 3. On-device inference
**Plain:** "Inference" is using a trained model to make a prediction. Here it all
happens on the phone/laptop itself, in the browser — nothing is sent to a server.
**Say it:** "All the processing runs on the device. No image ever leaves the
phone, so it's private and it works offline once loaded."
**Likely follow-up — "What are the advantages?"**
Privacy (no uploads), no server cost, and it keeps working without internet
after the first load.

### 4. Confidence score
**Plain:** The model outputs a probability, not a certainty — how sure it is.
**Say it:** "The percentage is how confident the model is. When it's low, I show
a 'move closer or add light' message instead of guessing."
**Likely follow-up — "What if it's wrong?"**
That's why I show confidence and handle low-confidence frames honestly, and why
training on my own real items reduces mistakes.

### 5. The two modes (know the difference cold)
- **General mode:** MobileNet recognises the *object* (e.g. "water bottle"), then
  a **rule** maps object → bin. It's a recogniser *plus* a rule.
- **Trash mode:** my own trained model outputs the *bin* directly — no rule
  needed. It's a true trash classifier.
**Say it:** "General mode names the object and looks up the bin. My trained model
skips that step — its output *is* the bin, because I trained it on waste."

---

## Technology — one line each

- **TensorFlow.js** — runs the neural network in the browser using the device's
  GPU. "It's what lets a neural network run in a web page with no install."
- **MobileNet** — a small, fast CNN. "Chosen because it's light enough to run
  smoothly on a phone, unlike big models."
- **Teachable Machine** — Google's free tool to train a model with no code, using
  transfer learning.
- **HTML/CSS/JavaScript** — one file, opens in any browser.

---

## Design decisions — and why (examiners love "why")

- **Runs in a browser, not an installed app** → anyone can use it from a link, on
  any device. Lower barrier, wider reach.
- **Colour-coded results** → mirrors real recycling-bin colours, so the answer is
  intuitive, not just text.
- **Reading-stability smoothing** → the bin only changes after a result holds
  steady, so it doesn't flicker during a live demo.
- **Rear camera by default on phones, not mirrored** → matches how you'd actually
  hold it up to an item.

---

## Limitations — say these *before* you're asked

Volunteering the limits makes you look like you understand the technology, not
like you're hiding flaws.

- "It only recognises what it was trained on."
- "Visual look-alikes can fool it — a glass and a plastic bottle look similar."
- "Poor lighting lowers accuracy."
- "It can't tell apart materials that look identical, like some plastic types."
- **Then add:** "These are the known limits of any vision model. Training on my
  own real items, in real lighting, is what narrows them — which is exactly why
  I built the custom-model mode."

---

## Hard questions you might get — and answers

**"Did you build the neural network yourself?"**
"I used MobileNet as the base — training an image network from scratch needs
huge datasets and compute. My contribution is the application, the object-to-bin
logic, and a custom model I trained on real waste photos using transfer learning."

**"Is this actually machine learning, or just if-statements?"**
"The recognition is real machine learning — a CNN. In general mode there's a
small rule that maps the recognised object to a bin. In trash mode, the model I
trained outputs the bin directly, so there's no rule at all."

**"What happens with something it's never seen?"**
"It'll pick the closest class and probably show low confidence. If nothing
matches well it falls back to General Waste. That's the honest behaviour of a
classifier — and why I show the confidence score."

**"How would you improve it?"**
"Train on more real items and lighting, add a background class so empty frames
don't misfire, distinguish plastic types where the resin code is visible, and
log how many items get sorted at the expo to measure real impact."

**"Why does it need internet at first?"**
"Only to download the model the first time — about 14MB. After that the browser
caches it and it runs offline. All the actual recognition is on-device; the
internet is just for the initial download."

---

## Demo checklist (day of)

- [ ] Device charged; camera permission already granted once.
- [ ] Trash model loaded and confirmed (badge says "your trash model").
- [ ] Tested offline the night before on this exact device.
- [ ] A small kit of clean demo items (bottle, can, box, fruit, glass, old cable).
- [ ] Good light on the demo spot; plain-ish background.
- [ ] Know your one-liner for each concept above.
