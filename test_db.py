import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("DATABASE_URL")
print("Connecting to:", url.split("@")[-1] if url else " NO URL FOUND")

conn = psycopg2.connect(url)
cur = conn.cursor()
cur.execute("SELECT version();")
print("Connected!")
print(cur.fetchone()[0])

cur.close()
conn.close()