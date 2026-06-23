import os
import pandas as pd

# -------------------------------
# Path to raw data folder
# -------------------------------
DATA_FOLDER = "data/raw"

# List of expected CSV files
csv_files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 80)
print("BLUESTOCK FINTECH - DATA INGESTION")
print("=" * 80)

datasets = {}

for file in csv_files:
    file_path = os.path.join(DATA_FOLDER, file)

    print("\n" + "=" * 80)
    print(f"Dataset: {file}")
    print("=" * 80)

    if not os.path.exists(file_path):
        print("❌ File not found!")
        continue

    try:
        df = pd.read_csv(file_path)

        datasets[file] = df

        print("\nShape:")
        print(df.shape)

        print("\nColumns:")
        print(df.columns.tolist())

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except Exception as e:
        print(f"Error reading {file}")
        print(e)

print("\n")
print("=" * 80)
print("DATA INGESTION COMPLETED")
print("=" * 80)