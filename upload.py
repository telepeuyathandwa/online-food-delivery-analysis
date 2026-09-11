import pandas as pd
from sqlalchemy import create_engine

# Connect through the Railway SSH tunnel
engine = create_engine(
    "postgresql://postgres:ptgvWMHxzpmHoBsOCuZYOzjlMxPAHxhG@127.0.0.1:42633/railway"
)

# Load the cleaned CSV
df = pd.read_csv("raw/online_food_delivery_clean.csv")

# Upload to Postgres
df.to_sql("food_delivery_clean", engine, if_exists="replace", index=False)

print(f"Uploaded {len(df)} rows to table 'food_delivery_clean'")