# Clinical AI Working Principles

> [!info] Purpose
> Keep these principles in mind throughout the Clinical AI Foundations project. They are the project's operating rules for learning, analysis, interpretation, and appraisal.

## 1. Doctor first

The goal is:

> **Doctor who understands computational medicine**

not:

> software engineer who happens to know medicine.

Learn technical material to the depth required to understand, analyse, reproduce, critique, and communicate clinical computational work.

---

## 2. Statistics before machine learning

Do not use machine-learning terminology to compensate for weak statistical understanding.

Before interpreting a model, understand:

- the outcome;
- the population;
- the study/design;
- uncertainty;
- assumptions;
- validation;
- the meaning of the performance metric.

---

## 3. Design before analysis

Before analysing a clinical dataset, define:

```text
Population
↓
Clinical question
↓
Prediction/measurement time
↓
Outcome
↓
Predictors/exposures
↓
Analysis strategy
```

Do not choose the analysis because it gives the nicest result after looking at the data.

---

## 4. Association ≠ prediction ≠ causation

Keep these questions separate:

### Association
Is X statistically related to Y?

### Prediction
Can information available at time T help predict Y?

### Causation
Would changing X alter Y?

A variable can be useful for prediction without being causal.

---

## 5. Statistical performance ≠ clinical usefulness

A model can perform well statistically without providing clinically useful decisions.

Whenever relevant, ask:

- What decision is being made?
- At what threshold?
- What are the consequences of false positives and false negatives?
- Does using the model improve decisions?

---

## 6. Discrimination ≠ calibration

### Discrimination
Can the model distinguish higher-risk from lower-risk individuals?

### Calibration
Do predicted risks correspond reasonably to observed risks?

Always distinguish the two.

---

## 7. Development ≠ validation

A model that fits its development dataset well has not necessarily demonstrated useful performance elsewhere.

Ask:

- Was performance estimated on data used for development?
- Was there internal validation?
- Was there external validation?
- How independent was the evaluation data?

---

## 8. Watch for overfitting

A model can learn patterns that are specific to the development data rather than patterns that generalize.

Warning signs include:

- excessive model complexity;
- too many predictors relative to available information;
- repeated tuning against the same evaluation data;
- large development/evaluation performance differences.

---

## 9. Watch for leakage

Always ask:

> **Would this information have been available at the exact moment the prediction was supposed to be made?**

Check for:

- future information;
- outcome-derived variables;
- inappropriate preprocessing;
- test-set driven feature selection;
- duplicates across datasets;
- information shared across related observations.

---

## 10. Reproducibility matters

Prefer analysis that another person can understand and reproduce.

Record:

- source data;
- preprocessing;
- code;
- package versions;
- random seeds where relevant;
- validation method;
- performance metrics;
- interpretation.

A result that cannot be reproduced deserves extra skepticism.

---

## 11. Interpret uncertainty

Never treat an estimate as a fact without considering uncertainty.

For important results ask:

- What is the estimate?
- What is the uncertainty?
- How wide is the interval?
- How many observations/events support it?
- Would a clinically important alternative value still be compatible with the data?

---

## 12. Statistical significance is not clinical importance

A small effect can be statistically convincing in a large dataset.

A clinically meaningful effect can be estimated imprecisely in a small dataset.

Always examine the effect estimate and its uncertainty, not just the p-value.

---

## 13. Generalizability is a separate question

Ask whether the population used to develop or evaluate a model resembles the population in which it is intended to be used.

Consider:

- setting;
- geography;
- time period;
- disease spectrum;
- prevalence;
- measurement processes;
- treatment patterns;
- patient characteristics.

---

## 14. Do not chase the highest metric

A higher AUC, accuracy, or other metric is not automatically a better clinical model.

The relevant question is:

> **Is this analysis appropriate, valid, interpretable, well-validated, and clinically useful for the intended purpose?**

---

## 15. Reproduce important results

Do not be satisfied with recognising an answer.

For important concepts and analyses:

```text
Understand
↓
Implement
↓
Interpret
↓
Critique
↓
Reproduce
```

---

## 16. Ask what the dataset actually represents

Before trusting a dataset, ask:

- Who was included?
- Who was excluded?
- Why?
- How were variables measured?
- How was the outcome defined?
- When were measurements made?
- What population does this actually represent?

The dataset is not automatically equivalent to the clinical population you care about.

---

## 17. Keep clinical interpretation attached to computational output

For every important numerical result, write a plain-language interpretation.

Example:

```text
Model output:
AUROC = ...

Clinical interpretation:
This indicates how well the model separates patients with higher
observed risk from those with lower observed risk in the evaluated
population. It does not by itself establish good calibration or
clinical usefulness.
```

The exact interpretation should always depend on the metric, design, population, and context.

---

# Final Rule

> **Understand the clinical question first. Understand the data second. Choose the method third. Interpret the result fourth. Critique it fifth.**

Never reverse that order simply because a model or software package makes the final step easy.
