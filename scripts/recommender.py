"""
Mutual Fund Recommendation Engine

This module recommends top mutual funds based on investor risk appetite.
It filters funds using risk grade and ranks them using Sharpe Ratio.
"""

from pathlib import Path
import pandas as pd


# -------------------------------
# Load dataset
# -------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
FILE_PATH = BASE_DIR / "data" / "processed" / "07_scheme_performance_cleaned.csv"

performance = pd.read_csv(FILE_PATH)


# -------------------------------
# Recommendation Function
# -------------------------------
def recommend_funds(risk_appetite: str, top_n: int = 3):
    """
    Recommends top mutual funds based on risk appetite and Sharpe Ratio.

    Parameters:
        risk_appetite (str): Investor risk level (Low / Moderate / High)
        top_n (int): Number of funds to recommend (default = 3)

    Returns:
        DataFrame: Top recommended funds sorted by Sharpe Ratio
    """

    risk_appetite = risk_appetite.strip().title()

    if "risk_grade" not in performance.columns:
        raise ValueError("Column 'risk_grade' not found in dataset.")

    filtered = performance[
        performance["risk_grade"].astype(str).str.strip().str.title() == risk_appetite
    ]

    if filtered.empty:
        return None

    recommendations = (
        filtered.sort_values("sharpe_ratio", ascending=False)
        .head(top_n)
        [["scheme_name", "risk_grade", "sharpe_ratio"]]
    )

    return recommendations


# -------------------------------
# Main execution block
# -------------------------------
if __name__ == "__main__":

    risk = input("Enter Risk Appetite (Low / Moderate / High): ")

    result = recommend_funds(risk)

    if result is None:
        print("\nNo funds found for this risk category.")
    else:
        print("\nTop Recommended Funds:\n")
        print(result.to_string(index=False))