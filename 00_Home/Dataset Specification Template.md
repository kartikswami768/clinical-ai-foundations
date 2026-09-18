# Clinical Dataset Specification

> [!info] Purpose
> Complete this document **before modelling**. The goal is to define the clinical prediction problem and analysis plan before looking for the method that produces the most attractive performance.

---

# 1. Dataset Identification

**Dataset name:**

**Source:**

**Version / date accessed:**

**Dataset documentation:**

**Original study / publication, if applicable:**

**Educational / research / clinical purpose:**

> [!warning]
> Educational datasets should not automatically be treated as valid clinical tools.

---

# 2. Clinical Question

## Primary question

> What clinically meaningful outcome are we trying to predict or estimate?

**Question:**


## Decision context

What clinical situation would this information be used in?


---

# 3. Target Population

**Population of interest:**


**Inclusion criteria:**


**Exclusion criteria:**


**Recruitment / sampling method:**


**Setting:**


**Geographic population:**


**Time period:**


---

# 4. Prediction Time

> [!important]
> Define the exact point at which the prediction is supposed to be made.

**Prediction time:**


## Information available at prediction time

- 
- 
- 

## Information that becomes available only later

- 
- 
- 

> [!danger] Leakage check
> Any variable that would not have been available at the prediction time may create information leakage if used as a predictor.

---

# 5. Outcome

**Outcome name:**


**Operational definition:**


**Outcome type:**

- [ ] Binary
- [ ] Multicategory
- [ ] Continuous
- [ ] Time-to-event
- [ ] Other

**Outcome measurement method:**


**Outcome ascertainment / reference standard:**


**Prediction horizon:**


**Potential outcome misclassification:**


---

# 6. Predictors

| Predictor | Meaning | Type | Unit/coding | Available at prediction time? | Missing? |
|---|---|---|---|---|---|
| | | | | | |
| | | | | | |
| | | | | | |

## Predictor selection rationale

Why are these predictors included?


Were predictors specified before modelling?


---

# 7. Coding and Units

## Continuous variables

Document the original units and any transformations.

| Variable | Original unit | Analysis unit | Transformation |
|---|---|---|---|
| | | | |
| | | | |

## Categorical variables

| Variable | Original coding | Analysis coding | Reference category |
|---|---|---|---|
| | | | |
| | | | |

---

# 8. Missing Data

## Missingness summary

| Variable | Missing n | Missing % | Pattern / notes |
|---|---:|---:|---|
| | | | |
| | | | |

## Missingness mechanism considerations

- [ ] MCAR considered
- [ ] MAR considered
- [ ] MNAR considered
- [ ] Mechanism uncertain

## Planned handling

- [ ] Complete-case analysis
- [ ] Single imputation
- [ ] Multiple imputation
- [ ] Missing-category approach
- [ ] Model-based handling
- [ ] Other

**Rationale:**


> [!warning]
> Missing-data handling must be considered as part of the analysis rather than treated as an unimportant cleaning step.

---

# 9. Data Quality

Check:

- [ ] Duplicate observations
- [ ] Impossible values
- [ ] Implausible values
- [ ] Unit inconsistencies
- [ ] Coding inconsistencies
- [ ] Date/time problems
- [ ] Data-entry errors
- [ ] Outliers
- [ ] Measurement problems
- [ ] Inconsistent repeated measurements

## Data-quality findings


---

# 10. Preprocessing

Document every transformation that occurs before modelling.

| Step | Purpose | Applied to | When fitted/estimated? |
|---|---|---|---|
| | | | |
| | | | |

Examples:

- scaling;
- normalization;
- transformations;
- encoding;
- imputation;
- feature construction;
- feature selection.

> [!danger] Leakage rule
> Any preprocessing step that learns information from the data must be fitted using the appropriate training data and then applied to held-out data.

---

# 11. Validation Strategy

**Primary validation strategy:**


Examples:

- hold-out validation;
- k-fold cross-validation;
- bootstrap;
- temporal validation;
- geographic validation;
- external validation.

## Data partitioning

**Training set:**


**Validation/resampling set:**


**Test set:**


## Independence

Explain why the evaluation data are independent of model development.


---

# 12. Performance Metrics

Select metrics **before** looking at the results.

## Discrimination

- [ ] AUROC
- [ ] AUPRC
- [ ] C-statistic
- [ ] Sensitivity/specificity at a prespecified threshold
- [ ] Other

## Calibration

- [ ] Calibration plot
- [ ] Calibration-in-the-large
- [ ] Calibration slope
- [ ] Brier score
- [ ] Other

## Classification measures

- [ ] PPV
- [ ] NPV
- [ ] Accuracy
- [ ] Sensitivity
- [ ] Specificity
- [ ] F1
- [ ] Other

## Clinical usefulness

- [ ] Threshold-based decision analysis
- [ ] Net benefit / decision curve analysis
- [ ] Other

**Why were these metrics selected?**


---

# 13. Uncertainty

How will uncertainty around performance estimates be quantified?

- [ ] Confidence intervals
- [ ] Bootstrap intervals
- [ ] Cross-validation variability
- [ ] Other

**Method:**


---

# 14. Overfitting Assessment

Consider:

- [ ] Number of observations
- [ ] Number of outcome events
- [ ] Number of predictors
- [ ] Model complexity
- [ ] Regularization
- [ ] Resampling/validation
- [ ] Optimism correction

**Main overfitting concerns:**


---

# 15. Leakage Audit

Before modelling, ask:

### Temporal leakage
Does any predictor contain information from after prediction time?

### Outcome leakage
Is any predictor partly derived from the outcome?

### Preprocessing leakage
Was preprocessing fitted using information from held-out data?

### Selection leakage
Were predictors selected using the test set?

### Validation leakage
Was model tuning influenced by the final evaluation set?

### Duplicate / related-patient leakage
Could the same patient, encounter, family, institution, or near-duplicate appear across development and evaluation data?

**Leakage findings:**


---

# 16. Bias and Applicability

## Selection

How was the population selected?


## Measurement

How were predictors and outcomes measured?


## Spectrum

Does the dataset represent the range of patients in intended use?


## Confounding / association issues

Are predictors being interpreted causally when the task is actually prediction?


## Applicability

Would the model/data reasonably apply to:

- [ ] A different hospital?
- [ ] A different geographic region?
- [ ] A different healthcare system?
- [ ] A different time period?
- [ ] Different patient subgroups?

**Concerns:**


---

# 17. Subgroup Performance

Pre-specified important subgroups:

- 
- 
- 

For each subgroup, consider:

- discrimination;
- calibration;
- missingness;
- sample size;
- uncertainty;
- clinical usefulness.

**Findings:**


---

# 18. Transportability / Generalizability

## Development population

Describe:


## Intended-use population

Describe:


## Important differences

- 
- 
- 

**Transportability concerns:**


---

# 19. Final Pre-Modelling Checklist

- [ ] Clinical question defined
- [ ] Population defined
- [ ] Prediction time defined
- [ ] Outcome defined
- [ ] Predictors defined
- [ ] Coding and units checked
- [ ] Missingness assessed
- [ ] Data quality assessed
- [ ] Preprocessing specified
- [ ] Leakage considered
- [ ] Validation strategy specified
- [ ] Performance metrics selected
- [ ] Uncertainty strategy specified
- [ ] Applicability considered

> [!important]
> **Only after this checklist is complete should modelling begin.**

---

# 20. Post-Analysis Interpretation

## What did the model show?


## How was performance estimated?


## What does the performance mean clinically?


## What are the main sources of uncertainty?


## What are the main threats to validity?


## Does performance generalize to the intended population?


## What should not be concluded?


---

# 21. Reproducibility

**Code location:**


**Notebook/script:**


**Environment / Python version:**


**Package versions:**


**Random seed, if applicable:**


**Data-processing steps recorded?**

- [ ] Yes
- [ ] No

**Analysis reproducible by another person?**

- [ ] Yes
- [ ] Partially
- [ ] No
