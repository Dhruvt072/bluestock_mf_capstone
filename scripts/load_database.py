import os
import sqlite3
import pandas as pd

from sqlalchemy import create_engine

print("=" * 70)
print("LOADING CLEANED DATA INTO SQLITE DATABASE")
print("=" * 70)

# ====================================================
# Create Database
# ====================================================

db_path = "data/processed/bluestock.db"

engine = create_engine(
    f"sqlite:///{db_path}"
)

print("\nDatabase Created Successfully!")

# ====================================================
# Read Cleaned Files
# ====================================================

nav = pd.read_csv(
    "data/processed/nav_history_clean.csv"
)

transactions = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

performance = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

aum = pd.read_csv(
    "data/raw/03_aum_by_fund_house.csv"
)

print("\nDatasets Loaded Successfully!")

# ====================================================
# Load into SQLite
# ====================================================

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("\nTables Loaded Successfully!")

# ====================================================
# Verify Row Counts
# ====================================================

connection = sqlite3.connect(db_path)

tables = [
    "dim_fund",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum"
]

print("\n")
print("=" * 70)
print("ROW COUNT VERIFICATION")
print("=" * 70)

for table in tables:

    count = pd.read_sql(
        f"SELECT COUNT(*) AS rows FROM {table}",
        connection
    )

    print(f"{table:<25} {count.iloc[0,0]}")

connection.close()

print("\nDatabase Loading Complete!")