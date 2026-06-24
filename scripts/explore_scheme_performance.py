import pandas as pd

file_path = "data/raw/07_scheme_performance.csv"

df = pd.read_csv(file_path)

print("=" * 70)
print("SCHEME PERFORMANCE EXPLORATION")
print("=" * 70)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nFirst 10 Rows:")
print(df.head(10))

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())