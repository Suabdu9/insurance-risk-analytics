import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    mean_squared_error, r2_score,
    accuracy_score, precision_score, recall_score, f1_score
)

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from xgboost import XGBRegressor, XGBClassifier


# ----------------------------
# CLEAN DATA (CRASH-PROOF)
# ----------------------------
def clean_data(df):
    df = df.copy()

    # convert empty strings / spaces → NaN
    df = df.replace(r"^\s*$", np.nan, regex=True)

    # strip all object columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()
        df[col] = df[col].replace("nan", np.nan)

    return df


def clean_column_types(df):
    """
    Force correct dtype separation and prevent mixed-type crashes.
    """
    df = df.copy()

    for col in df.columns:
        # Try converting to numeric
        numeric_version = pd.to_numeric(df[col], errors="coerce")

        # If MOST values become numeric → treat as numeric
        if numeric_version.notna().mean() > 0.8:
            df[col] = numeric_version
        else:
            df[col] = df[col].astype("object")

    return df


# ----------------------------
# FEATURE ENGINEERING
# ----------------------------
def feature_engineering(df):
    df = df.copy()

    df["TransactionMonth"] = pd.to_datetime(df["TransactionMonth"], errors="coerce")

    df["TransactionYear"] = df["TransactionMonth"].dt.year
    df["TransactionMonthNum"] = df["TransactionMonth"].dt.month

    if "RegistrationYear" in df.columns:
        df["VehicleAge"] = df["TransactionYear"] - df["RegistrationYear"]

    df["ClaimOccurred"] = np.where(df["TotalClaims"] > 0, 1, 0)

    return df


def enforce_sklearn_dtypes(df):
    """
    Fix dtype issues for sklearn compatibility.
    """

    df = df.copy()

    for col in df.columns:
        # convert custom 'str' dtype to proper object
        if str(df[col].dtype) == "str":
            df[col] = df[col].astype("object")

        # force datetime handling
        if "datetime" in str(df[col].dtype):
            df[col] = df[col].astype("int64", errors="ignore")

    return df


# ----------------------------
# SPLIT
# ----------------------------
def prepare_data(df, target, drop_cols=None, test_size=0.2):
    if drop_cols is None:
        drop_cols = []

    df = df.copy()

    X = df.drop(columns=[target] + drop_cols, errors="ignore")
    y = df[target]

    X = X.replace([np.inf, -np.inf], np.nan)

    preprocessor = build_preprocessor(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        random_state=42
    )

    return X_train, X_test, y_train, y_test, preprocessor


# ----------------------------
# PREPROCESSOR (SAFE)
# ----------------------------
def build_preprocessor(X):
    X = X.copy()

    # FORCE clean column separation
    numeric_features = []
    categorical_features = []

    for col in X.columns:
        if pd.api.types.is_numeric_dtype(X[col]):
            numeric_features.append(col)
        else:
            categorical_features.append(col)

    numeric_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="median"))
    ])

    categorical_transformer = Pipeline(steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        ("onehot", OneHotEncoder(handle_unknown="ignore"))
    ])

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_features),
            ("cat", categorical_transformer, categorical_features)
        ]
    )

    return preprocessor


# ----------------------------
# REGRESSION (STABLE)
# ----------------------------
def train_regression_models(X_train, X_test, y_train, y_test):

    preprocessor = build_preprocessor(X_train)

    models = {
        "Linear Regression": LinearRegression(),

        "Random Forest": RandomForestRegressor(
            n_estimators=50,
            random_state=42,
            n_jobs=1
        ),

        "XGBoost": XGBRegressor(
            n_estimators=50,
            max_depth=4,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=42,
            n_jobs=1,
            verbosity=0
        )
    }

    results = []
    fitted = {}

    for name, model in models.items():

        pipe = Pipeline([
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        pipe.fit(X_train, y_train)
        preds = pipe.predict(X_test)

        results.append({
            "Model": name,
            "RMSE": np.sqrt(mean_squared_error(y_test, preds)),
            "R2": r2_score(y_test, preds)
        })

        fitted[name] = pipe

    return pd.DataFrame(results), fitted


# ----------------------------
# CLASSIFICATION
# ----------------------------
def train_classification_models(X_train, X_test, y_train, y_test):

    preprocessor = build_preprocessor(X_train)

    models = {
        "Logistic Regression": LogisticRegression(max_iter=1000),

        "Random Forest": RandomForestClassifier(
            n_estimators=50,
            random_state=42,
            n_jobs=1
        ),

        "XGBoost": XGBClassifier(
            n_estimators=50,
            max_depth=4,
            learning_rate=0.1,
            subsample=0.8,
            colsample_bytree=0.8,
            eval_metric="logloss",
            random_state=42,
            n_jobs=1,
            verbosity=0
        )
    }

    results = []
    fitted = {}

    for name, model in models.items():

        pipe = Pipeline([
            ("preprocessor", preprocessor),
            ("model", model)
        ])

        pipe.fit(X_train, y_train)
        preds = pipe.predict(X_test)

        results.append({
            "Model": name,
            "Accuracy": accuracy_score(y_test, preds),
            "Precision": precision_score(y_test, preds, zero_division=0),
            "Recall": recall_score(y_test, preds, zero_division=0),
            "F1": f1_score(y_test, preds, zero_division=0)
        })

        fitted[name] = pipe

    return pd.DataFrame(results), fitted


# ----------------------------
# PREMIUM FORMULA
# ----------------------------
def calculate_optimized_premium(prob, severity,
                                expense_loading=500,
                                profit_margin=0.1):

    return (prob * severity + expense_loading) * (1 + profit_margin)
