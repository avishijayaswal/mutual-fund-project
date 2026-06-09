-- Query 1: Top 5 Fund Houses by AUM
SELECT
    fund_house,
    MAX(aum_crore) AS highest_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY highest_aum DESC
LIMIT 5;


-- Query 2: Average NAV per Month
SELECT
    strftime('%Y-%m', date) AS month,
    AVG(nav) AS average_nav
FROM fact_nav
GROUP BY month
ORDER BY month;


-- Query 3: SIP Year-wise Growth
SELECT
    strftime('%Y', transaction_date) AS year,
    COUNT(*) AS sip_transactions,
    SUM(amount_inr) AS total_sip_amount
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;


-- Query 4: Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- Query 5: Funds with Expense Ratio < 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;


-- Query 6: Total Transaction Amount
SELECT
    SUM(amount_inr) AS total_transaction_amount
FROM fact_transactions;


-- Query 7: Average 1-Year Return
SELECT
    AVG(return_1yr_pct) AS average_return_1yr
FROM fact_performance;


-- Query 8: Top 5 Funds by 5-Year Return
SELECT
    scheme_name,
    return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;


-- Query 9: Average Expense Ratio
SELECT
    AVG(expense_ratio_pct) AS average_expense_ratio
FROM fact_performance;


-- Query 10: Number of Transactions per Fund
SELECT
    amfi_code,
    COUNT(*) AS transaction_count
FROM fact_transactions
GROUP BY amfi_code
ORDER BY transaction_count DESC;