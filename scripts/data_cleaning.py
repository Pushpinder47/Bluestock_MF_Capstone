import pandas as pd

# Clean NAV History
nav = pd.read_csv("data/raw/02_nav_history.csv")

nav.drop_duplicates(inplace=True)

nav.columns = nav.columns.str.lower().str.strip()

nav.to_csv("data/processed/clean_nav.csv", index=False)

print("clean_nav.csv created")


# Clean Investor Transactions
transactions = pd.read_csv("data/raw/08_investor_transactions.csv")

transactions.drop_duplicates(inplace=True)

transactions.columns = transactions.columns.str.lower().str.strip()

transactions.to_csv("data/processed/clean_transactions.csv", index=False)

print("clean_transactions.csv created")


# Clean Scheme Performance
performance = pd.read_csv("data/raw/07_scheme_performance.csv")

performance.drop_duplicates(inplace=True)

performance.columns = performance.columns.str.lower().str.strip()

performance.to_csv("data/processed/clean_performance.csv", index=False)

print("clean_performance.csv created")