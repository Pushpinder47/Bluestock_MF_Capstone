import sqlite3
import pandas as pd

conn = sqlite3.connect("mf_capstone.db")

query = """
SELECT *
FROM investor_transactions
LIMIT 10
"""

df = pd.read_sql_query(query, conn)

print(df)

conn.close()