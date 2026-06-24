import sqlite3
import pandas as pd

conn = sqlite3.connect("mf_capstone.db")

nav = pd.read_csv("data/processed/clean_nav.csv")
transactions = pd.read_csv("data/processed/clean_transactions.csv")

nav.to_sql("nav_history", conn, if_exists="replace", index=False)
transactions.to_sql("investor_transactions", conn, if_exists="replace", index=False)

print("Database created successfully")

conn.close()