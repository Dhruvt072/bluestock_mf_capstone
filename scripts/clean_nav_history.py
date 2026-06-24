import pandas as pd
import os

# ==========================================
# Load Dataset
# ==========================================
file_path = "data/raw/02_nav_history.csv"
df = pd.read_csv(file_path)

print(df.head())
print("\nColumn Names:")
print(df.columns.tolist())


print("=" * 60)
print("NAV HISTORY CLEANING")
print("=" * 60)

print("\nOriginal Shape:")
print(df.shape)

# ==========================================
# Convert Date Column
# ==========================================

print("\nConverting Date Column...")

df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)
# ==========================================
# Check Invalid Dates
# ==========================================

invalid_dates = df["date"].isnull().sum()

print("Invalid Dates:", invalid_dates)

# ==========================================
# Remove Duplicate Records
# ==========================================

duplicates = df.duplicated().sum()

print("Duplicate Rows:", duplicates)

df = df.drop_duplicates()

# ==========================================
# Sort Dataset
# ==========================================

print("\nSorting Data...")

df = df.sort_values(
    by=["amfi_code", "date"]
)

# ==========================================
# Convert NAV to Numeric
# ==========================================

df["nav"] = pd.to_numeric(
    df["nav"],
    errors="coerce"
)

# ==========================================
# Forward Fill Missing NAV
# ==========================================

print("\nForward Filling Missing NAV...")

df["nav"] = (
    df.groupby("amfi_code")["nav"]
      .ffill()
)

# ==========================================
# Remove Remaining Missing NAV
# ==========================================

missing_nav = df["nav"].isnull().sum()

print("Remaining Missing NAV:", missing_nav)

df = df.dropna(subset=["nav"])

# ==========================================
# Validate NAV
# ==========================================

invalid_nav = (df["nav"] <= 0).sum()

print("Invalid NAV Values:", invalid_nav)

df = df[df["nav"] > 0]

# ==========================================
# Final Shape
# ==========================================

print("\nFinal Shape:")
print(df.shape)

# ==========================================
# Save Clean Dataset
# ==========================================

output_folder = "data/processed"

os.makedirs(output_folder, exist_ok=True)

output_path = os.path.join(
    output_folder,
    "nav_history_clean.csv"
)

df.to_csv(
    output_path,
    index=False
)

print("\nClean dataset saved successfully!")

print(output_path)