import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def missing_values_report(df: pd.DataFrame) -> pd.DataFrame:
    """Return missing value summary."""
    try:
        missing = df.isnull().sum()
        percent = (missing / len(df)) * 100

        report = pd.DataFrame(
            {
                "Missing Values": missing,
                "Percentage": percent,
            }
        ).sort_values(by="Percentage", ascending=False)

        return report

    except Exception as e:
        print(f"[ERROR] Missing value report failed: {e}")
        raise


def plot_histogram(df, col):
    """Plot histogram for a numeric column."""
    try:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col].dropna(), bins=50, kde=True)
        plt.title(f"Distribution of {col}")
        plt.show()

    except Exception as e:
        print(f"[ERROR] Histogram failed for {col}: {e}")


def plot_box(df, col):
    """Plot boxplot for a numeric column."""
    try:
        plt.figure(figsize=(6, 3))
        sns.boxplot(x=df[col])
        plt.title(f"Boxplot of {col}")
        plt.show()

    except Exception as e:
        print(f"[ERROR] Boxplot failed for {col}: {e}")


def loss_ratio(df):
    """Calculate loss ratio."""
    try:
        df = df.copy()
        df["LossRatio"] = (
            df["TotalClaims"] /
            df["TotalPremium"].replace(0, np.nan)
        )
        return df

    except Exception as e:
        print(f"[ERROR] Loss ratio calculation failed: {e}")
        raise


def plot_categorical_count(
    df: pd.DataFrame,
    col: str,
    top_n: int = 10
):
    """Plot frequency distribution of a categorical column."""
    try:
        plt.figure(figsize=(10, 4))

        df[col].value_counts().head(top_n).plot(kind="bar")

        plt.title(f"Top {top_n} categories in {col}")
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

    except Exception as e:
        print(
            f"[ERROR] Categorical count plot failed for {col}: {e}"
        )


def plot_category_vs_target(
    df: pd.DataFrame,
    category_col: str,
    target_col: str = "LossRatio",
    top_n: int = 10,
):
    """Compare average numeric target across categories."""
    try:
        plt.figure(figsize=(10, 4))

        grouped = (
            df.groupby(category_col)[target_col]
            .mean()
            .sort_values(ascending=False)
            .head(top_n)
        )

        grouped.plot(kind="bar")

        plt.title(f"{target_col} by {category_col}")
        plt.ylabel(f"Average {target_col}")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

    except Exception as e:
        print(
            f"[ERROR] Category vs target plot failed "
            f"for {category_col}: {e}"
        )


def plot_proportion_table(df: pd.DataFrame, col: str):
    """Show percentage distribution of categorical values."""
    try:
        plt.figure(figsize=(8, 4))

        (
            df[col].value_counts(normalize=True) * 100
        ).head(10).plot(kind="bar")

        plt.title(f"Percentage distribution of {col}")
        plt.ylabel("Percentage (%)")
        plt.xticks(rotation=45)
        plt.tight_layout()

        plt.show()

    except Exception as e:
        print(f"[ERROR] Proportion plot failed for {col}: {e}")


def plot_correlation_heatmap(
    df: pd.DataFrame,
    cols=None
):
    """Plot correlation heatmap for numeric features."""
    try:
        plt.figure(figsize=(10, 6))

        if cols is None:
            corr = df.select_dtypes(include=[np.number]).corr()
        else:
            corr = df[cols].corr()

        sns.heatmap(
            corr,
            annot=False,
            cmap="coolwarm",
            linewidths=0.5,
        )

        plt.title("Correlation Heatmap")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"[ERROR] Correlation heatmap failed: {e}")


def plot_premium_vs_claims(df):
    """Scatter plot of Total Premium vs Total Claims."""
    try:
        plt.figure(figsize=(8, 5))

        sns.scatterplot(
            data=df,
            x="TotalPremium",
            y="TotalClaims",
            alpha=0.4,
        )

        plt.title("Total Premium vs Total Claims")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"[ERROR] Scatter plot failed: {e}")
