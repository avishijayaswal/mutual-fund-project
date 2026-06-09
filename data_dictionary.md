# Data Dictionary

This document describes all datasets used in the Mutual Fund Analytics project, including column names, data types, business definitions, and source files.

---

# Dataset: 02_nav_history_cleaned.csv

| Column    | Data Type | Business Definition                                   | Source             |
| --------- | --------- | ----------------------------------------------------- | ------------------ |
| amfi_code | INTEGER   | Unique identifier assigned to each mutual fund scheme | 02_nav_history.csv |
| date      | DATE      | Date on which NAV was recorded                        | 02_nav_history.csv |
| nav       | REAL      | Net Asset Value of the mutual fund on the given date  | 02_nav_history.csv |

---

# Dataset: 03_aum_by_fund_house_cleaned.csv

| Column         | Data Type | Business Definition                                           | Source                   |
| -------------- | --------- | ------------------------------------------------------------- | ------------------------ |
| date           | DATE      | Reporting date for AUM statistics                             | 03_aum_by_fund_house.csv |
| fund_house     | TEXT      | Name of the Asset Management Company (AMC)                    | 03_aum_by_fund_house.csv |
| aum_lakh_crore | REAL      | Assets Under Management expressed in lakh crore               | 03_aum_by_fund_house.csv |
| aum_crore      | INTEGER   | Assets Under Management expressed in crore                    | 03_aum_by_fund_house.csv |
| num_schemes    | INTEGER   | Total number of mutual fund schemes managed by the fund house | 03_aum_by_fund_house.csv |

---

# Dataset: 07_scheme_performance_cleaned.csv

| Column             | Data Type | Business Definition                             | Source                    |
| ------------------ | --------- | ----------------------------------------------- | ------------------------- |
| amfi_code          | INTEGER   | Unique mutual fund scheme identifier            | 07_scheme_performance.csv |
| scheme_name        | TEXT      | Name of the mutual fund scheme                  | 07_scheme_performance.csv |
| fund_house         | TEXT      | Asset Management Company managing the scheme    | 07_scheme_performance.csv |
| category           | TEXT      | Mutual fund category                            | 07_scheme_performance.csv |
| plan               | TEXT      | Plan type (Regular/Direct)                      | 07_scheme_performance.csv |
| return_1yr_pct     | REAL      | Annual return over the last 1 year (%)          | 07_scheme_performance.csv |
| return_3yr_pct     | REAL      | Annualized return over the last 3 years (%)     | 07_scheme_performance.csv |
| return_5yr_pct     | REAL      | Annualized return over the last 5 years (%)     | 07_scheme_performance.csv |
| benchmark_3yr_pct  | REAL      | Benchmark return over 3 years (%)               | 07_scheme_performance.csv |
| alpha              | REAL      | Alpha indicating excess return over benchmark   | 07_scheme_performance.csv |
| beta               | REAL      | Beta measuring volatility relative to benchmark | 07_scheme_performance.csv |
| sharpe_ratio       | REAL      | Risk-adjusted return using Sharpe Ratio         | 07_scheme_performance.csv |
| sortino_ratio      | REAL      | Downside risk-adjusted return measure           | 07_scheme_performance.csv |
| std_dev_ann_pct    | REAL      | Annualized standard deviation of returns        | 07_scheme_performance.csv |
| max_drawdown_pct   | REAL      | Maximum observed decline from peak (%)          | 07_scheme_performance.csv |
| aum_crore          | INTEGER   | Assets Under Management in crore                | 07_scheme_performance.csv |
| expense_ratio_pct  | REAL      | Annual expense ratio charged by the fund (%)    | 07_scheme_performance.csv |
| morningstar_rating | INTEGER   | Morningstar fund rating                         | 07_scheme_performance.csv |
| risk_grade         | TEXT      | Overall risk classification of the fund         | 07_scheme_performance.csv |

---

# Dataset: 08_investor_transactions_cleaned.csv

| Column             | Data Type | Business Definition                             | Source                       |
| ------------------ | --------- | ----------------------------------------------- | ---------------------------- |
| investor_id        | TEXT      | Unique identifier for each investor             | 08_investor_transactions.csv |
| transaction_date   | DATE      | Date of investment transaction                  | 08_investor_transactions.csv |
| amfi_code          | INTEGER   | Mutual fund scheme identifier                   | 08_investor_transactions.csv |
| transaction_type   | TEXT      | Type of transaction (SIP, Lumpsum, Redemption)  | 08_investor_transactions.csv |
| amount_inr         | REAL      | Transaction amount in Indian Rupees             | 08_investor_transactions.csv |
| state              | TEXT      | State of the investor                           | 08_investor_transactions.csv |
| city               | TEXT      | City of the investor                            | 08_investor_transactions.csv |
| city_tier          | TEXT      | Classification of city (Tier 1, Tier 2, Tier 3) | 08_investor_transactions.csv |
| age_group          | TEXT      | Investor age category                           | 08_investor_transactions.csv |
| gender             | TEXT      | Investor gender                                 | 08_investor_transactions.csv |
| annual_income_lakh | REAL      | Annual income of investor in lakh rupees        | 08_investor_transactions.csv |
| payment_mode       | TEXT      | Mode of payment used for transaction            | 08_investor_transactions.csv |
| kyc_status         | TEXT      | Know Your Customer (KYC) verification status    | 08_investor_transactions.csv |
