# Insurance Risk Analytics Project

## Overview
This project analyzes insurance policy data to identify risk patterns, profitability trends, and customer behavior using exploratory data analysis (EDA), hypothesis testing, and predictive modeling.

---

## Project Structure

```text
insurance-risk-analytics/
│
├── data/
│   └── MachineLearningRating_v3/
│       └── MachineLearningRating_v3.txt
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_hypothesis_testing.ipynb
│   └── 03_modeling.ipynb
│
├── src/
│   ├── data_loader.py
│   └── eda_utils.py
│
├── tests/
│   └── test_data_loader.py
│
├── requirements.txt
├── .github/workflows/ci.yml
└── README.md
```

---

## Setup Instructions

### 1. Clone repository

```bash
git clone <repo-url>
cd insurance-risk-analytics
```

---

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Launch Jupyter Notebook

```bash
python -m notebook
```

---

## Running the Project

Open notebooks in order:

1. `01_eda.ipynb`
2. `02_hypothesis_testing.ipynb`
3. `03_modeling.ipynb`

---

## Running Tests

```bash
pytest
```

---

## Running Lint Checks

```bash
flake8
```

---

## CI Pipeline

GitHub Actions automatically runs:

- tests
- lint checks

on every push and pull request.