-- Top 5 funds by AUM
SELECT * FROM fact_aum
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Total Transactions
SELECT COUNT(*)
FROM fact_transactions;

-- Transactions by State
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Funds with Expense Ratio < 1%
SELECT *
FROM dim_fund
WHERE expense_ratio < 1;