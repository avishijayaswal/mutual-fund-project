"""
Live NAV Data Ingestion Module

This module fetches mutual fund NAV data from the MFAPI service
and stores it as CSV files in the raw data directory.
"""

import requests
import pandas as pd
from pathlib import Path


# -------------------------------
# NAV Fetch Function
# -------------------------------
def fetch_nav_data(schemes: dict, output_folder: str):
    """
    Fetches NAV data for multiple mutual fund schemes and saves them as CSV.

    Parameters:
        schemes (dict): Dictionary mapping scheme names to AMFI codes
        output_folder (str): Directory where CSV files will be saved

    Returns:
        dict: Status report of successful and failed downloads
    """

    output_path = Path(output_folder)
    output_path.mkdir(parents=True, exist_ok=True)

    status_report = {
        "success": [],
        "failed": []
    }

    for name, code in schemes.items():

        try:
            url = f"https://api.mfapi.in/mf/{code}"
            response = requests.get(url, timeout=10)

            if response.status_code != 200:
                raise Exception(f"HTTP {response.status_code}")

            data = response.json()

            if "data" not in data:
                raise Exception("Invalid API response format")

            nav_df = pd.DataFrame(data["data"])

            file_path = output_path / f"{name}_nav.csv"
            nav_df.to_csv(file_path, index=False)

            print(f"Saved: {file_path.name}")
            status_report["success"].append(name)

        except Exception as e:
            print(f"Failed to fetch {name}: {e}")
            status_report["failed"].append(name)

    return status_report


# -------------------------------
# Main Execution Block
# -------------------------------
if __name__ == "__main__":

    schemes = {
        "hdfc_top100": 125497,
        "sbi_bluechip": 119551,
        "icici_bluechip": 120503,
        "nippon_large_cap": 118632,
        "axis_bluechip": 119092,
        "kotak_bluechip": 120841
    }

    result = fetch_nav_data(schemes, "data/raw")

    print("\nDownload Summary:")
    print(result)