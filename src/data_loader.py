import pandas as pd
from pathlib import Path


def load_data(file_path: str) -> pd.DataFrame:
    try:
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")

        df = pd.read_csv(
            path,
            sep="|",
            low_memory=False
        )

        # clean column names
        df.columns = df.columns.str.strip()

        print(f"[SUCCESS] Loaded: {df.shape}")
        print("Columns:", df.columns.tolist())

        return df

    except Exception as e:
        print(f"[ERROR] {e}")
        raise


def add_derived_metrics(df):
    """
    Add Loss Ratio and Margin columns.
    """
    required_cols = ["TotalClaims", "TotalPremium"]

    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df = df.copy()

    df["LossRatio"] = df["TotalClaims"] / df["TotalPremium"].replace(0, pd.NA)
    df["Margin"] = df["TotalPremium"] - df["TotalClaims"]

    return df
