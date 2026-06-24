import pandas as pd
import os

# ==========================================
# Load Dataset
# ==========================================

file_path = "data/raw/08_investor_transactions.csv"

df = pd.read_csv(file_path)

print("=" * 70)
print("INVESTOR TRANSACTIONS CLEANING")
print("=" * 70)

print("\nOriginal Shape:")
print(df.shape)

# ==========================================
# Convert Date Column
# ==========================================

print("\nConverting transaction_date...")

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

invalid_dates = df["transaction_date"].isna().sum()

print("Invalid Dates:", invalid_dates)

# ==========================================
# Standardize Transaction Type
# ==========================================

print("\nStandardizing Transaction Types...")

df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

valid_transactions = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

invalid_transaction = ~df["transaction_type"].isin(valid_transactions)

print(
    "Invalid Transaction Types:",
    invalid_transaction.sum()
)

# ==========================================
# Validate Amount
# ==========================================

print("\nChecking Amount...")

invalid_amount = (df["amount_inr"] <= 0).sum()

print("Invalid Amounts:", invalid_amount)

df = df[df["amount_inr"] > 0]

# ==========================================
# Validate KYC Status
# ==========================================

print("\nChecking KYC Status...")

df["kyc_status"] = (
    df["kyc_status"]
    .str.strip()
    .str.title()
)

valid_kyc = [
    "Verified",
    "Pending"
]

invalid_kyc = ~df["kyc_status"].isin(valid_kyc)

print(
    "Invalid KYC Records:",
    invalid_kyc.sum()
)

# ==========================================
# Remove Duplicate Rows
# ==========================================

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# ==========================================
# Sort Data
# ==========================================

df = df.sort_values(
    by=[
        "transaction_date",
        "investor_id"
    ]
)

# ==========================================
# Save Clean Dataset
# ==========================================

output_folder = "data/processed"

os.makedirs(
    output_folder,
    exist_ok=True
)

output_file = os.path.join(
    output_folder,
    "investor_transactions_clean.csv"
)

df.to_csv(
    output_file,
    index=False
)

print("\nFinal Shape:")
print(df.shape)

print("\nClean dataset saved successfully!")

print(output_file)