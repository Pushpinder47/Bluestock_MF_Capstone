CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT
);

CREATE TABLE fact_nav (
    amfi_code INTEGER,
    nav_date TEXT,
    nav REAL
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    amfi_code INTEGER,
    transaction_date TEXT,
    amount REAL,
    transaction_type TEXT
);

CREATE TABLE fact_performance (
    amfi_code INTEGER,
    return_1yr REAL,
    sharpe REAL,
    alpha REAL,
    beta REAL
);