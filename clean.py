import pandas as pd

# 1. Load the data
df = pd.read_csv("raw/online_food_delivery.csv")

# 2. Show what we're starting with
print("=== BEFORE CLEANING ===")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print()

# 3. Drop the junk column
df = df.drop(columns=["Unnamed: 13"])

# 4. Strip whitespace from all text columns
for col in df.select_dtypes(include="str").columns:
    df[col] = df[col].str.strip()

# 5. Show what we have now
print("=== AFTER CLEANING ===")
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print()

# 6. Quick peek at unique values in the messy columns
print("Feedback values:", df["Feedback"].unique())
print("Output values:", df["Output"].unique())
print("Customer Type values:", df["Customer Type"].unique())

# 7. Save cleaned data
df.to_csv("raw/online_food_delivery_clean.csv", index=False)
print()
print("Saved to raw/online_food_delivery_clean.csv")