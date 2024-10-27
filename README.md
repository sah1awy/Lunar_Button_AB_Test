# A/B Testing Case Study Using Python

This Python script simulates an A/B test, a common technique in statistics and data science for comparing two versions of a variable. The objective is to identify which version performs better, providing a practical example of A/B testing.

---

## 1. Simulating Click Data for A/B Testing

### Objective
Simulate click data for an experimental group (`exp`) and a control group (`con`).

### Method
- **Data Generation**: Utilizes `numpy` and `pandas` libraries to create random binary click data (`1` = click, `0` = no click).
- **Datasets Created**: `df_exp` for the experimental group and `df_con` for the control group.
- **Sample Size and Click Probability**: Each group has `1000` samples, with click probabilities set to `0.5` for `exp` and `0.2` for `con`.
- **Merged Data**: Combines `df_exp` and `df_con` into a single DataFrame, `df_ab_test`, for analysis.

<p align="center">
  <img src="https://github.com/sah1awy/Lunar_Button_AB_Test/blob/main/assets/Count.png" alt="Data simulation for A/B testing">
</p>

---

## 2. Statistical Significance in A/B Testing

### Objective
Assess if the difference in click rates between the experimental and control groups is statistically significant.

### Method
- **Click Totals and Probabilities**: Calculates total clicks (`X_con`, `X_exp`) and click probabilities (`p_con_hat`, `p_exp_hat`) for each group.
- **Pooled Probability**: Computes a pooled click probability (`p_pooled_hat`) and pooled variance.
- **Standard Error**: Calculates the standard error (`SE`) to measure the precision of click probability estimates.
- **Two-Sample Z-Test**: Conducts a Z-test by calculating:
  - Test statistic (`Test_stat`)
  - Critical value (`Z_crit`)
  - P-value
- **Confidence Interval**: Determines a confidence interval (`CI`) to estimate the true difference in click probabilities.

---

## Application as a Case Study

### Scenario
A website tests two webpage designs to find which version drives higher user engagement, measured by clicks.

### Process
1. The `exp` group views the new webpage design, while the `con` group sees the original design.
2. User interactions are simulated to calculate click-through rates for each group.
3. A statistical analysis is performed to determine if the new design significantly improves engagement.

---

## Conclusion

### Findings
This script provides statistical evidence to indicate whether the experimental design (new webpage) leads to a higher click rate than the control (original webpage).

<p align="center">
  <img src="https://github.com/sah1awy/Lunar_Button_AB_Test/blob/main/assets/Test2.png" alt="A/B Testing Results">
</p>

### Decision Making
Based on the p-value and confidence interval, decisions are made regarding the potential implementation of the new design across the website.

---

*This case study demonstrates how A/B testing can be effectively used in digital marketing, website optimization, and user experience research to support data-driven decision-making.*
