"""
Bluestock Mutual Fund Analytics - Master Pipeline

This script runs the complete workflow:
1. Fetch live NAV data (ETL ingestion)
2. Run data validation / profiling
3. Generate mutual fund recommendations

This acts as the single entry point for the entire project.
"""

from scripts.data_ingestion import fetch_nav_data
from scripts.recommender import recommend_funds

import os


def main():
    """
    Executes the full analytics pipeline in sequence.
    """

    print("\n" + "=" * 60)
    print(" BLUESTOCK MUTUAL FUND ANALYTICS PIPELINE STARTED")
    print("=" * 60)

    # -------------------------------
    # STEP 1: NAV DATA INGESTION
    # -------------------------------
    print("\n Step 1: Fetching Live NAV Data...")

    schemes = {
        "hdfc_top100": 125497,
        "sbi_bluechip": 119551,
        "icici_bluechip": 120503,
        "nippon_large_cap": 118632,
        "axis_bluechip": 119092,
        "kotak_bluechip": 120841
    }

    fetch_nav_data(schemes, "data/raw")

    print(" NAV data ingestion completed")

    # -------------------------------
    # STEP 2: DATA PROFILING (OPTIONAL)
    # -------------------------------
    print("\n Step 2: Running Data Profiling...")

    try:
        summary = profile_datasets("data/raw")
        print("Data profiling completed")

    except Exception as e:
        print("⚠ Profiling skipped or failed:", e)

    # -------------------------------
    # STEP 3: RECOMMENDATION ENGINE
    # -------------------------------
    print("\nStep 3: Generating Fund Recommendations...")

    risk = input("Enter Risk Appetite (Low / Moderate / High): ")

    result = recommend_funds(risk)

    if result is None:
        print("\nNo funds found for this risk category.")
    else:
        print("\nTop Recommended Funds:\n")
        print(result.to_string(index=False))

    # -------------------------------
    # PIPELINE END
    # -------------------------------
    print("\n" + "=" * 60)
    print("PIPELINE EXECUTION COMPLETED SUCCESSFULLY")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()