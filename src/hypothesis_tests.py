import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency


def run_ttest(group_a, group_b):
    """
    Independent t-test for numerical comparison.
    """
    try:
        stat, p_value = ttest_ind(
            group_a.dropna(),
            group_b.dropna(),
            equal_var=False
        )
        return p_value

    except Exception as e:
        print(f"[ERROR] t-test failed: {e}")
        return None


def run_chi2_test(df, category_col, target_col):
    """
    Chi-square test for categorical comparison.
    """
    try:
        contingency = pd.crosstab(
            df[category_col],
            df[target_col]
        )

        _, p_value, _, _ = chi2_contingency(contingency)

        return p_value

    except Exception as e:
        print(f"[ERROR] Chi-square test failed: {e}")
        return None


def hypothesis_decision(p_value, alpha=0.05):
    """
    Return statistical decision.
    """
    try:
        if p_value < alpha:
            return "Reject H0"
        return "Fail to Reject H0"

    except Exception as e:
        print(f"[ERROR] Decision function failed: {e}")
        return None
