# SortRight — A Smart Waste Sorter
### Using On-Device Machine Vision to Guide Correct Recycling

**Author:** [Your Name]
**Event / Course:** EDGE — Employability Development & Growth through Education · Level Expo, 3–4 Dec 2026
**Theme:** Reusability · Sustainability · Resource-efficient technology

> How to use this document: everything between square brackets `[ ]` is a
> placeholder for you to fill in — your name, your own test results, your
> screenshots. Do **not** submit invented accuracy numbers; run the test
> described in Section 6 on your own items and record what you actually see.

---

## Abstract

Most people want to recycle correctly but hesitate at the bin because they are
not sure which stream an item belongs to. That single moment of doubt is a
major source of contamination: recyclables end up in landfill, and landfill
waste ends up in recycling. **SortRight** removes the doubt. It is a web
application that uses a camera and a neural network to recognise an everyday
object and instantly tell the user which bin it belongs in — Plastic, Paper,
Metal, Glass, Organic, E-waste, or General Waste — colour-coding the screen to
match. The entire system runs inside the web browser on a phone or laptop, with
no app to install and no data sent to any server. This report describes the
problem, the two-stage recognition pipeline, the machine-learning concepts
behind it (convolutional neural networks and transfer learning), the design
decisions, the honest limitations of the approach, and how the project maps
directly onto the EDGE themes of reusability, sustainability, and
resource-efficient technology.

---

## 1. Introduction and Problem Statement

Recycling only works when items are sorted correctly. When the wrong item goes
in a bin — a greasy pizza box in paper recycling, a glass bottle in with
plastics — it can contaminate the whole batch, and contaminated batches are
often sent to landfill. The barrier is not that people don't care; it is that
they don't *know*, and there is no help available at the exact second they are
holding the item over the bin.

SortRight addresses that specific moment. It answers one question — *"which bin
does this go in?"* — in a fraction of a second, visually and without any
typing, reading of labels, or prior knowledge. By making correct sorting
instant and obvious, it aims to reduce contamination and divert recyclable
material away from landfill.

## 2. Objectives

1. Build a tool that identifies a physical waste item from a live camera feed
   and names the correct disposal bin.
2. Make the result **immediate and intuitive** — colour-coded to match how real
   recycling bins are labelled — so it needs no explanation.
3. Run entirely **on the user's own device** in a browser, so it requires no
   installation, no server, and no dedicated hardware.
4. Support a **custom, waste-specific model** the user can train themselves, so
   the system is a genuine trash classifier rather than a general object
   recogniser with a lookup table.
5. Be **honest about its limits**, so the tool teaches good judgement rather
   than blind trust.

## 3. Background: the machine-learning concepts

These are the ideas an examiner will expect the author to explain. They are
stated here in plain terms, with the reason each one matters to this project.

**Neural network / Convolutional Neural Network (CNN).** A CNN is a program
that *learns* to recognise images from many examples, rather than being given
fixed hand-written rules. It looks for visual patterns — edges, then shapes,
then whole objects — building them up layer by layer. CNNs are the standard
technology behind modern image recognition, which is why this project uses one.

**Transfer learning.** Training a CNN from scratch normally needs hundreds of
thousands of images. Transfer learning avoids that: it starts from a network
that has *already* learned what images look like in general (from millions of
photos), and only re-teaches the final decision layer to tell the new,
project-specific categories apart. This is the reason a custom model can be
trained on just 30–50 photos per bin. Being able to explain *why* so few images
are enough is one of the strongest points the author can make.

**On-device inference.** "Inference" means using a trained model to make a
prediction. In this project all inference happens on the phone or laptop itself,
using the device's own processor/GPU through the browser. Nothing is uploaded.
The consequences are real and worth stating: **privacy** (no images leave the
device) and **offline capability** (it keeps working once the model has loaded).

**Confidence score.** The model does not output a certainty; it outputs a
*probability* — how sure it is. SortRight shows this percentage and, when it is
low, displays a "move closer / add light" prompt instead of pretending to be
sure. This honesty is a design feature, not a weakness.

## 4. System Design and Pipeline

Every time SortRight looks at a frame from the camera, it runs four stages:

1. **Capture** — grab a still frame from the live camera feed.
2. **Recognise** — pass that frame to a neural network, which outputs *what the
   object is* together with a confidence score.
3. **Map to a bin** — convert the recognised object into the correct waste
   stream.
4. **Display** — flood the panel with that bin's colour and show the disposal
   instruction and confidence.

This loop repeats a few times per second, so the experience feels live. To stop
the display flickering between bins during a demo, the shown result only changes
after a new bin has won on consecutive readings — a small **reading-stability
smoothing** step.

### 4.1 The two modes

The application can run on two different "brains", and understanding the
difference between them is central to the project.

**General mode (works instantly).** Uses **MobileNet**, a neural network Google
trained on roughly 1.2 million photos to recognise about 1,000 everyday
objects. MobileNet knows "water bottle" and "banana", but it does not know the
concept "recyclable". A small **mapping rule** bridges that gap: *banana →
Organic*, *water bottle → Plastic*, and so on. In this mode the system is a
*general object recogniser plus a rule* — Stage 3 above does real work.

**Trash mode (the real project).** The author trains their own model on actual
waste photos using **Google Teachable Machine**, then pastes its link into the
app. Now the model's output *is* the bin — if it says "plastic", that is the
answer, and the mapping rule is no longer needed. In this mode the system is a
genuine *trash classifier*. This is the stronger result and the recommended
configuration for the demo and the marks.

### 4.2 Why each technology was chosen

| Technology | Role | Why this one |
|---|---|---|
| **TensorFlow.js** | Runs the neural network inside the browser using the device's GPU | No install, no server; everything stays on-device |
| **MobileNet** | The recognition network (general mode) and the base for transfer learning | Small and fast enough to run smoothly in a phone browser, unlike heavier models |
| **Teachable Machine** | Lets the author train a custom waste model | Uses transfer learning; needs no coding and only a few dozen images per class |
| **Plain HTML/CSS/JavaScript** | The whole application | One file, opens in any modern browser from a single link |

## 5. Methodology (how it was built and used)

1. **Interface first.** A single HTML page presents a camera view and a result
   panel. The seven bins and their colours are defined once and drive both the
   on-screen legend and the live result, so the colour coding is consistent.
2. **General mode wired up.** MobileNet is loaded through TensorFlow.js. On each
   loop the current video frame is classified; the top label is passed through
   the mapping rule to pick a bin.
3. **Trash mode added.** The page accepts a Teachable Machine model link. When
   provided, predictions come from that model instead, and its class name is
   taken directly as the bin. The link is remembered on the device so the model
   reloads automatically next time.
4. **Robustness for a live demo.** Reading-stability smoothing prevents flicker;
   a low-confidence prompt handles uncertain frames; the rear camera is used by
   default on phones (and not mirrored), with a flip control for the front
   camera.
5. **Training the custom model.** See the separate **Training Guide**. In short:
   create a Standard image project in Teachable Machine, make one class per bin
   named exactly `plastic, paper, metal, glass, organic, ewaste, trash`, add
   30–50 varied webcam photos to each, train, export as an uploaded shareable
   link, and paste that link into the app.

## 6. Results

> Fill this section from your own testing — do not use invented numbers.

**How to gather results.** Pick 5–6 real items for each bin (a mix of easy and
tricky ones). For each item, point the camera at it in good light and record:
the bin SortRight chose, whether it was correct, and the confidence shown.
Repeat in both modes if you have trained a custom model.

**Suggested results table (fill in):**

| Item | True bin | Bin shown (General) | Bin shown (Trash) | Confidence | Correct? |
|---|---|---|---|---|---|
| Plastic water bottle | Plastic | [ ] | [ ] | [ ]% | [ ] |
| Aluminium can | Metal | [ ] | [ ] | [ ]% | [ ] |
| Banana | Organic | [ ] | [ ] | [ ]% | [ ] |
| Cardboard box | Paper | [ ] | [ ] | [ ]% | [ ] |
| Glass bottle | Glass | [ ] | [ ] | [ ]% | [ ] |
| Old phone/charger | E-waste | [ ] | [ ] | [ ]% | [ ] |

**What to report from this:** the proportion correct in each mode, which items
were confused and why (usually visual look-alikes), and how much the custom
(Trash) model improved on the general model for your own items. A typical,
honest finding is that the custom model is noticeably more reliable on the
specific items it was trained on, which is exactly what transfer learning
predicts.

## 7. Limitations (state these before an examiner asks)

- **It only recognises what it was trained on.** An unseen item type will be
  guessed, not known.
- **Visual look-alikes fool it** — a clear glass bottle and a clear plastic
  bottle can look almost identical to a camera.
- **Poor lighting lowers accuracy** and confidence.
- **Confusable materials aren't distinguished** — for example different plastic
  types that look the same.

These are not bugs; they are the known boundaries of any computer-vision model.
The way to narrow them is exactly what this project does in Trash mode: train on
your own real items, in the lighting and against the backgrounds where the tool
will actually be used.

## 8. Conclusion

SortRight shows that a genuinely useful, privacy-respecting recycling aid can be
built with free tools and run on hardware people already own. It turns an
uncertain moment at the bin into an instant, colour-coded answer. The two-mode
design also makes it a good teaching artefact: general mode demonstrates object
recognition plus a rule, while trash mode — a model the author trains themselves
— demonstrates transfer learning and a true image classifier. The honest
handling of confidence and limitations means the tool encourages good judgement
rather than blind trust.

**Future work:** train the custom model on a wider range of real items and
lighting; distinguish plastic types (e.g. by resin code where visible); add a
short on-screen tip for contamination (e.g. "empty and rinse first"); and log
anonymous counts of items sorted to measure impact at the expo.

## 9. How SortRight fits the EDGE theme

- **Reusability** — it actively promotes recycling and reuse by getting more of
  the right material into the right stream.
- **Sustainability** — correct sorting reduces contamination and diverts
  recyclable material away from landfill.
- **Resource-efficient technology** — it runs in a browser on phones and laptops
  people already own, needing no dedicated device, no installation, and no
  server. The computation is efficient enough for a mobile browser.

Each of the three theme words therefore maps to a concrete property of the
project, not just an aspiration.

## 10. References

> Verify each link and format to your institution's required referencing style
> (e.g. Harvard, IEEE) before submitting.

1. Howard, A. G. *et al.* (2017). *MobileNets: Efficient Convolutional Neural
   Networks for Mobile Vision Applications.* arXiv:1704.04861.
2. Sandler, M. *et al.* (2018). *MobileNetV2: Inverted Residuals and Linear
   Bottlenecks.* arXiv:1801.04381.
3. TensorFlow.js — *Machine learning for JavaScript developers.*
   https://www.tensorflow.org/js
4. Google Teachable Machine. https://teachablemachine.withgoogle.com
5. Pan, S. J. and Yang, Q. (2010). *A Survey on Transfer Learning.* IEEE
   Transactions on Knowledge and Data Engineering, 22(10), 1345–1359.

---

## Appendix A — Glossary (one-line definitions)

- **CNN:** a network that learns visual patterns from example images.
- **Transfer learning:** reusing a pre-trained network and re-teaching only its
  final layer for new categories.
- **Inference:** using a trained model to make a prediction.
- **On-device:** all processing happens on the phone/laptop; nothing is uploaded.
- **Confidence:** the model's own probability that its answer is right.
