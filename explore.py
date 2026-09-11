import pandas as pd

df = pd.read_csv("raw/online_food_delivery_clean.csv")

print("=== NUMERIC COLUMNS ===")
print(df.describe())
print()

print("=== CATEGORICAL COLUMNS ===")
for col in ["Gender", "Marital Status", "Occupation", "Monthly Income",
            "Educational Qualifications", "Customer Type", "Output", "Feedback"]:
    print(f"\n{col}:")
    print(df[col].value_counts())