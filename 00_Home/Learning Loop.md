# Clinical AI Learning Loop

> [!info] Purpose
> Use this loop for important concepts throughout the Clinical AI Foundations project. The aim is to connect conceptual understanding, computation, clinical reasoning, and critical appraisal rather than learning each subject in isolation.

## Core Loop

```text
CONCEPT
   ↓
CODE
   ↓
CLINICAL EXAMPLE
   ↓
INTERPRETATION
   ↓
CRITIQUE
   ↓
REPRODUCTION
```

## 1. Concept

Understand the idea before relying on code.

Answer:

- What problem does this concept solve?
- What is the intuitive/plain-language meaning?
- What is the mathematical/statistical meaning?
- What assumptions or conditions matter?
- How does it relate to concepts I already know?

For important concepts, use three layers:

### Intuitive layer
Explain it in ordinary language.

### Mathematical/statistical layer
State the formal definition, equation, probability model, or statistical interpretation.

### Computational layer
Show how the concept is implemented in Python.

---

## 2. Code

Implement the concept yourself.

Prefer:

- readable Python;
- small functions;
- explicit variable names;
- reproducible examples;
- comments/docstrings where they genuinely help.

Do not treat library output as understanding.

Ask:

> Could I modify this code without being shown exactly what to change?

---

## 3. Clinical Example

Connect the concept to a clinically meaningful situation.

Define:

- population;
- clinical question;
- variables;
- outcome;
- relevant time point;
- assumptions.

Avoid creating artificial clinical examples merely to force a connection. Use a clinical example when it genuinely improves understanding.

---

## 4. Interpretation

Explain the result in plain clinical/statistical language.

For numerical output, always ask:

- What was estimated or calculated?
- In what population?
- What does the value mean?
- How precise is it?
- What assumptions were involved?
- What would a clinician conclude from it?
- What should a clinician **not** conclude from it?

> [!important]
> Never present statistical output without interpretation.

---

## 5. Critique

Interrogate the analysis.

Consider:

### Design
- Is the study/design appropriate for the question?
- What is the population?
- How were participants/data selected?

### Measurement
- Are variables measured appropriately?
- Could there be misclassification or measurement error?

### Statistical assumptions
- Are the assumptions plausible?
- Was the chosen method appropriate?

### Bias and confounding
- Selection bias?
- Information/measurement bias?
- Confounding?
- Spectrum effects?

### Prediction-specific issues
- Leakage?
- Overfitting?
- Inappropriate preprocessing?
- Validation problems?
- Poor calibration?
- Limited transportability?
- Subgroup performance?

### Clinical meaning
- Is the effect/performance clinically important?
- Is statistical performance being confused with clinical usefulness?

---

## 6. Reproduction

Reproduce the result independently.

Possible levels:

### Level 1 — Calculation
Recalculate the result from the raw inputs.

### Level 2 — Code
Reimplement the analysis in Python.

### Level 3 — Paper reproduction
Reproduce an analysis from a published study or provided dataset.

### Level 4 — Independent extension
Change one reasonable element and predict what should happen before running the code.

The goal is not merely to obtain the same number. The goal is to understand why the number was obtained.

---

# Completion Check

For an important topic, ask:

- [ ] Can I explain it simply?
- [ ] Can I state the formal/statistical meaning?
- [ ] Can I write or modify the relevant Python?
- [ ] Can I connect it to a clinical example?
- [ ] Can I interpret the output clinically?
- [ ] Can I identify assumptions and limitations?
- [ ] Can I reproduce the result independently?

> [!tip] Advancement rule
> Move forward when the competency is demonstrated, not merely when the chapter or week has been completed.
