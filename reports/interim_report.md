# Interim Report: Insurance Risk Analytics

## 1. Business Understanding

AlphaCare Insurance Solutions (ACIS) aims to improve profitability and customer targeting in the South African car insurance market using data-driven decision-making.

The main business objectives are:
- Identify low-risk customer segments for competitive pricing
- Improve marketing efficiency by targeting profitable segments
- Understand key drivers of insurance claims and risk exposure
- Move from intuition-based pricing to risk-based pricing models

This project analyzes 18 months of historical insurance data (Feb 2014 – Aug 2015) to support these goals.

---

## 2. Data Understanding

The dataset contains policy-level insurance records including:
- Client demographics (Gender, Province, Language, etc.)
- Vehicle information (Make, Type, Value, etc.)
- Policy details (Premiums, Cover type, Sum insured)
- Claims data (TotalClaims, TotalPremium)

Two key business metrics are used:
- Loss Ratio = TotalClaims / TotalPremium
- Margin = TotalPremium − TotalClaims

---

## 3. Exploratory Data Analysis (EDA) Findings

### 3.1 Overall Risk Profile
- The portfolio shows a highly skewed distribution of claims.
- A small number of high-value claims significantly impact profitability.
- Loss Ratio indicates variability in profitability across segments.

---

### 3.2 Risk by Geography
- Province shows strong variation in Loss Ratio.
- Certain provinces consistently exhibit higher risk profiles.
- Geographic location is a strong predictor of insurance risk.

---

### 3.3 Risk by Vehicle Type
- Vehicle Type significantly affects claim severity and Loss Ratio.
- Some vehicle categories are consistently associated with higher claims.
- Vehicle characteristics are a key driver of risk.

---

### 3.4 Risk by Gender
- Gender shows weaker differences in Loss Ratio compared to geography and vehicle type.
- This suggests limited predictive power for pricing alone.

---

### 3.5 Temporal Trends
- Claim frequency and severity fluctuate over time.
- Some seasonal patterns are observed in monthly claims.
- Premiums are relatively stable compared to claims volatility.

---

### 3.6 Outliers & Distribution
- TotalClaims and TotalPremium are highly right-skewed.
- Significant outliers exist in claim amounts.
- These extreme values may represent rare but high-impact insurance events.
- Robust statistical methods are required for modeling.

---

### 3.7 Vehicle Makes
- Certain vehicle makes show consistently higher claim severity.
- Others are associated with lower average claims.
- Vehicle manufacturer is an important pricing feature.

---

## 4. Data Version Control (DVC) Setup

To ensure reproducibility and auditability, this project uses DVC.

### 4.1 DVC Implementation
- DVC initialized in the project using `dvc init`
- Raw dataset is tracked using `.dvc` metadata files
- Cleaned dataset version created for modeling purposes
- Data stored externally using a DVC remote storage location

### 4.2 Data Pipeline Structure
- Raw data → tracked via DVC
- Cleaned data → generated in notebook and tracked separately
- Only `.dvc` files are committed to Git, not raw datasets

### 4.3 Reproducibility
Any user can reproduce the dataset pipeline using:
- `dvc pull` to retrieve data
- `dvc repro` (if pipeline is extended)
- Git repository + DVC metadata

---

## 5. Key Insights

- Risk is primarily driven by **vehicle type and geography**
- Claims are highly skewed with extreme outliers affecting profitability
- Gender is a weak predictor of insurance risk
- Temporal variation suggests possible seasonal effects
- Certain vehicle makes significantly increase claim severity

---

## 6. Conclusion

The analysis confirms that insurance risk is not evenly distributed across customers. Instead, it is concentrated in specific vehicle categories and geographic regions.

These findings support the development of:
- Risk-based pricing models
- Targeted marketing strategies
- Segmented underwriting rules

The next phase of the project will focus on statistical hypothesis testing and predictive modeling to quantify these relationships further.
