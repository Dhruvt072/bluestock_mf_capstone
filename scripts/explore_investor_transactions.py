import pandas as pd

# ===========================
# Load Dataset
# ===========================

file_path = "data/raw/08_investor_transactions.csv"

df = pd.read_csv(file_path)

print("=" * 70)
print("INVESTOR TRANSACTIONS DATA EXPLORATION")
print("=" * 70)

print("\nShape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 10 Rows:")
print(df.head(10))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

print("\nUnique Transaction Types:")
print(df["transaction_type"].unique())

print("\nUnique KYC Status:")
print(df["kyc_status"].unique())