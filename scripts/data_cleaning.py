import pandas as pd

files = {
    "01_fund_master.csv": "clean_fund_master.csv",
    "02_nav_history.csv": "clean_nav.csv",
    "03_aum_by_fund_house.csv": "clean_aum.csv",
    "04_monthly_sip_inflows.csv": "clean_sip_inflows.csv",
    "05_category_inflows.csv": "clean_category_inflows.csv",
    "06_industry_folio_count.csv": "clean_folio_count.csv",
    "07_scheme_performance.csv": "clean_performance.csv",
    "08_investor_transactions.csv": "clean_transactions.csv",
    "09_portfolio_holdings.csv": "clean_holdings.csv",
    "10_benchmark_indices.csv": "clean_benchmark.csv"
}

for raw_file, clean_file in files.items():
    try:
        df = pd.read_csv("data/raw/" + raw_file)

        df.drop_duplicates(inplace=True)

        df.columns = df.columns.str.lower().str.strip()

        df.to_csv("data/processed/" + clean_file, index=False)

        print(clean_file, "created")

    except Exception as e:
        print(raw_file, "ERROR:", e)