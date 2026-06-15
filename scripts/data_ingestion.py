"""
Dataset Profiling Module

This script performs basic data quality checks on all CSV files
inside a given folder. It prints dataset shape, data types,
missing values, duplicates, and preview of data.
"""
import requests
import pandas as pd
from pathlib import Path


def fetch_nav_data(schemes: dict, output_folder: str):
    """
    Fetch NAV data from MF API and save as CSV files.

    Parameters:
        schemes (dict): scheme_name → AMFI code mapping
        output_folder (str): folder to save CSV files
    """

    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    for name, code in schemes.items():

        url = f"https://api.mfapi.in/mf/{code}"
        response = requests.get(url)

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        nav_df.to_csv(
            output_path / f"{name}_nav.csv",
            index=False
        )

        print(f"Saved {name}_nav.csv")