import pandas as pd

# Load the dataset
df = pd.read_csv("amazon.csv")

# Remove duplicates
df = df.drop_duplicates()

# Fill missing rating_count
df["rating_count"] = df["rating_count"].fillna("0")

# Clean currency and percent columns
def clean_currency(val):
    return pd.to_numeric(val.replace("₹", "").replace(",", "").strip(), errors='coerce')

df["discounted_price"] = df["discounted_price"].apply(clean_currency)
df["actual_price"] = df["actual_price"].apply(clean_currency)
df["rating_count"] = df["rating_count"].str.replace(",", "").astype(int)
df["discount_percentage"] = df["discount_percentage"].str.replace("%", "").astype(int)
df["rating"] = pd.to_numeric(df["rating"], errors='coerce')

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Save the cleaned dataset
df.to_csv("amazon_cleaned.csv", index=False)

print("✅ Cleaning complete. File saved as 'amazon_cleaned.csv'.")
