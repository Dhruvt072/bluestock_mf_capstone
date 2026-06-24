
import pandas as pd
import os

# ==========================================
# Load Dataset
# ==========================================

file_path = "data/raw/07_scheme_performance.csv"

df = pd.read_csv(file_path)

print("=" * 70)
print("SCHEME PERFORMANCE CLEANING")
print("=" * 70)

print("\nOriginal Shape:")
print(df.shape)

# ==========================================
# Convert Return Columns to Numeric
# ==========================================

return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "expense_ratio_pct"
]

print("\nChecking Numeric Columns...")

for column in return_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# ==========================================
# Missing Numeric Values
# ==========================================

print("\nMissing Values After Conversion:")

for column in return_columns:
    missing = df[column].isna().sum()
    print(f"{column:<25} : {missing}")

# ==========================================
# Validate Expense Ratio
# ==========================================

print("\nChecking Expense Ratio...")

invalid_expense = (
    (df["expense_ratio_pct"] < 0.1) |
    (df["expense_ratio_pct"] > 2.5)
)

print("Invalid Expense Ratios:", invalid_expense.sum())

# ==========================================
# Flag Return Anomalies
# ==========================================

print("\nChecking Return Anomalies...")

anomaly = (
    (df["return_1yr_pct"] < -100) |
    (df["return_1yr_pct"] > 100)
)

print("1-Year Return Anomalies:", anomaly.sum())

# ==========================================
# Remove Duplicate Rows
# ==========================================

duplicates = df.duplicated().sum()

print("\nDuplicate Rows:", duplicates)

df = df.drop_duplicates()

# ==========================================
# Save Clean Dataset
# ==========================================

output_folder = "data/processed"

os.makedirs(output_folder, exist_ok=True)

output_file = os.path.join(
    output_folder,
    "scheme_performance_clean.csv"
)

df.to_csv(output_file, index=False)

print("\nFinal Shape:")
print(df.shape)

print("\nClean dataset saved successfully!")

print(output_file)