# Clinical AI Competency Tracker

> [!info] Purpose
> This is the project's competency gate tracker. Progress is based on demonstrated ability rather than elapsed time, chapter count, or completion of a reading list.

## Status Key

- ☐ Not demonstrated
- ==☑ Partially demonstrated / needs prompting==
- ☑ Demonstrated independently
- ↻ Reassess later if the skill is not used for a prolonged period

---

# Gate 1 — Clinical Dataset Inspection

## Competency

I can independently inspect a clinical CSV/dataset and identify:

- variable names and types;
- categorical vs numerical variables;
- distributions;
- obvious errors/outliers;
- missingness;
- units/coding issues;
- basic structural problems in the dataset.

### Evidence

- [ ] Load the dataset independently.
- [ ] Inspect dimensions and variables.
- [ ] Identify variable types.
- [ ] Summarize missingness.
- [ ] Inspect distributions with appropriate summaries/plots.
- [ ] Identify at least one plausible data-quality issue and explain why it matters.

**Status:** ☐

**Evidence / link to work:**


---

# Gate 2 — Diagnostic Accuracy

## Competency

I can calculate and interpret:

- sensitivity;
- specificity;
- PPV;
- NPV;
- LR+;
- LR−.

### Evidence

- [ ] Construct a 2×2 table correctly.
- [ ] Calculate the measures manually.
- [ ] Recalculate them in Python.
- [ ] Explain what each measure conditions on.
- [ ] Explain the effect of disease prevalence on PPV/NPV.
- [ ] Explain clinically what LR+ and LR− do.

**Status:** ☐

**Evidence / link to work:**


---

# Gate 3 — Discrimination vs Calibration

## Competency

I can explain the difference between model discrimination and calibration without relying on ML jargon.

### Evidence

- [ ] Define discrimination.
- [ ] Define calibration.
- [ ] Explain what AUC/ROC-type measures assess.
- [ ] Explain what calibration assesses.
- [ ] Give an example where two models can have similar discrimination but different calibration.
- [ ] Explain why both matter in clinical prediction.

**Status:** ☐

**Evidence / link to work:**


---

# Gate 4 — Training, Validation and Test Data

## Competency

I can explain the purpose and distinction of training, validation and test data and identify which stage is being used in a modelling workflow.

### Evidence

- [ ] Explain the role of training data.
- [ ] Explain the role of validation data/resampling.
- [ ] Explain the role of a final test set.
- [ ] Explain why test-set information must not influence model development.
- [ ] Explain how preprocessing can accidentally leak information.

**Status:** ☐

**Evidence / link to work:**


---

# Gate 5 — Overfitting and Leakage

## Competency

I can identify overfitting and data leakage in a clinical prediction workflow.

### Evidence

- [ ] Give a plain-language definition of overfitting.
- [ ] Give a plain-language definition of leakage.
- [ ] Identify at least three possible leakage mechanisms.
- [ ] Distinguish leakage from ordinary poor model performance.
- [ ] Explain why apparent test performance can become misleading.
- [ ] Detect leakage in a provided workflow or code example.

**Status:** ☐

**Evidence / link to work:**


---

# Gate 6 — Test-Set Provenance

## Competency

I can interrogate where a reported test set came from and whether it provides a credible estimate of generalization.

### Evidence

- [ ] Identify the source population.
- [ ] Identify the sampling/recruitment process.
- [ ] Determine whether the test data are truly independent.
- [ ] Check whether preprocessing/model selection used test information.
- [ ] Compare the test population with the intended-use population.
- [ ] Identify threats to transportability/generalizability.

**Status:** ☐

**Evidence / link to work:**


---

# Gate 7 — Basic Clinical Prediction Model

## Competency

I can build and evaluate a basic prediction model using an appropriate workflow.

### Evidence

- [ ] Define the clinical question before modelling.
- [ ] Define prediction time.
- [ ] Define outcome.
- [ ] Define predictors.
- [ ] Inspect missingness and data quality.
- [ ] Pre-specify a validation strategy.
- [ ] Fit a basic model.
- [ ] Estimate performance appropriately.
- [ ] Assess discrimination.
- [ ] Assess calibration.
- [ ] Interpret the model clinically.
- [ ] Identify major limitations.

**Status:** ☐

**Evidence / link to work:**


---

# Gate 8 — Explain Limitations to Another Doctor

## Competency

I can explain a clinical AI/prediction result to another doctor without using ML terminology to hide uncertainty.

### Evidence

- [ ] Explain the clinical question.
- [ ] Explain what the model predicts.
- [ ] Describe the population in which it was evaluated.
- [ ] Explain its main performance measures.
- [ ] Explain uncertainty and important limitations.
- [ ] Explain major risks of bias/leakage/overfitting where relevant.
- [ ] Explain whether the evidence supports use in a different setting.
- [ ] Avoid overstating causality or clinical usefulness.

**Status:** ☐

**Evidence / link to work:**


---

# Overall Progress

| Gate | Status |
|---|---|
| 1. Dataset inspection | ☐ |
| 2. Diagnostic accuracy | ☐ |
| 3. Discrimination vs calibration | ☐ |
| 4. Train/validation/test | ☐ |
| 5. Overfitting/leakage | ☐ |
| 6. Test-set provenance | ☐ |
| 7. Basic prediction model | ☐ |
| 8. Explain limitations clinically | ☐ |

## Advancement Rule

> **Do not advance simply because a week, chapter, book section, or course module is finished. Advance when the relevant competency has been demonstrated.**

For each gate, evidence should preferably include:

1. **Coding evidence**
2. **Interpretation evidence**
3. **Critical-appraisal evidence**

---

# Reassessment

A competency can be marked as demonstrated and still be revisited.

Use reassessment when:

- the concept becomes relevant in a new context;
- a more difficult dataset exposes a weakness;
- new methodology changes the preferred approach;
- the skill has not been used for a long period.
