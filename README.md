# Insurance Risk Analytics Project

## Overview
This project analyzes insurance policy data to identify risk patterns, profitability trends, and customer behavior using:
- Exploratory Data Analysis (EDA)
- Statistical hypothesis testing
- Predictive modeling
- Data Version Control (DVC) for reproducibility and auditability

The goal is to support risk-based pricing and marketing optimization in an insurance context.

---

## Project Structure

insurance-risk-analytics/
│
├── data/
│   └── MachineLearningRating_v3/
│       ├── MachineLearningRating_v3.txt
│       ├── MachineLearningRating_v3.txt.dvc
│       ├── cleaned_insurance_data.csv
│       └── cleaned_insurance_data.csv.dvc
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
├── .github/workflows/ci.yml
├── dvc.yaml
├── requirements.txt
├── .gitignore
└── README.md

---

## Setup Instructions

### Clone repository
git clone <repo-url>
cd insurance-risk-analytics

### Create virtual environment
python -m venv venv

Windows:
venv\Scripts\activate

Mac/Linux:
source venv/bin/activate

### Install dependencies
pip install -r requirements.txt

### Run Jupyter Notebook
python -m notebook

---

## Data Version Control (DVC)

pip install dvc

dvc init

dvc add data/MachineLearningRating_v3/MachineLearningRating_v3.txt

dvc add data/cleaned_insurance_data.csv

dvc push

dvc pull

---

## Running the Project

1. 01_eda.ipynb
2. 02_hypothesis_testing.ipynb
3. 03_modeling.ipynb

---

## Running Tests

pytest

---

## Running Lint Checks

flake8 src tests

---

## CI Pipeline

GitHub Actions runs:
- pytest
- flake8

on push and pull request to:
- main
- task-1
- task-2
- task-3
- task-4

---

## Key Features

- Loss Ratio & Margin analysis
- Risk segmentation (Province, Vehicle Type, Gender)
- Temporal claim trends
- Outlier detection
- DVC-based dataset versioning
- Reproducible ML pipeline

---

## Business Objective

Help AlphaCare Insurance Solutions:
- Identify low-risk customers
- Improve pricing strategy
- Optimize marketing spend
- Build predictive risk models