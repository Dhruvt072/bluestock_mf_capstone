# Data Dictionary

## Bluestock Mutual Fund Analytics Platform

### Project

Day 2 - Data Cleaning & SQLite Database

---

# Overview

This document describes the datasets used in the Bluestock Mutual Fund Analytics Platform. It includes the column names, data types, business definitions, and data sources for each dataset.

---

# Dataset 1 : Fund Master

**Source:** `01_fund_master.csv`

| Column       | Data Type | Description                        |
| ------------ | --------- | ---------------------------------- |
| amfi_code    | Integer   | Unique AMFI scheme code            |
| scheme_name  | Text      | Name of the mutual fund scheme     |
| fund_house   | Text      | Mutual fund company                |
| category     | Text      | Fund category (Equity, Debt, etc.) |
| sub_category | Text      | Sub-category of the fund           |
| plan         | Text      | Regular or Direct plan             |
| risk_grade   | Text      | Risk level of the scheme           |

---

# Dataset 2 : NAV History

**Source:** `02_nav_history.csv`

| Column    | Data Type | Description                   |
| --------- | --------- | ----------------------------- |
| amfi_code | Integer   | AMFI scheme code              |
| date      | Date      | NAV date                      |
| nav       | Decimal   | Net Asset Value of the scheme |

---

# Dataset 3 : AUM by Fund House

**Source:** `03_aum_by_fund_house.csv`

| Column     | Data Type | Description                      |
| ---------- | --------- | -------------------------------- |
| fund_house | Text      | Mutual fund company              |
| month      | Date      | Reporting month                  |
| aum_crore  | Decimal   | Assets Under Management (Crores) |

---

# Dataset 4 : Monthly SIP Inflows

**Source:** `04_monthly_sip_inflows.csv`

| Column           | Data Type | Description               |
| ---------------- | --------- | ------------------------- |
| month            | Date      | Month                     |
| sip_inflow_crore | Decimal   | Monthly SIP inflow amount |

---

# Dataset 5 : Category Inflows

**Source:** `05_category_inflows.csv`

| Column       | Data Type | Description           |
| ------------ | --------- | --------------------- |
| category     | Text      | Mutual fund category  |
| month        | Date      | Reporting month       |
| inflow_crore | Decimal   | Monthly inflow amount |

---

# Dataset 6 : Industry Folio Count

**Source:** `06_industry_folio_count.csv`

| Column      | Data Type | Description               |
| ----------- | --------- | ------------------------- |
| month       | Date      | Reporting month           |
| folio_count | Integer   | Number of investor folios |

---

# Dataset 7 : Scheme Performance

**Source:** `07_scheme_performance.csv`

| Column             | Data Type | Description                   |
| ------------------ | --------- | ----------------------------- |
| amfi_code          | Integer   | AMFI scheme code              |
| scheme_name        | Text      | Scheme name                   |
| fund_house         | Text      | Mutual fund company           |
| category           | Text      | Fund category                 |
| plan               | Text      | Regular / Direct              |
| return_1yr_pct     | Decimal   | One-year return (%)           |
| return_3yr_pct     | Decimal   | Three-year return (%)         |
| return_5yr_pct     | Decimal   | Five-year return (%)          |
| benchmark_3yr_pct  | Decimal   | Benchmark return (%)          |
| alpha              | Decimal   | Alpha performance metric      |
| beta               | Decimal   | Beta risk metric              |
| sharpe_ratio       | Decimal   | Risk-adjusted return metric   |
| sortino_ratio      | Decimal   | Downside risk-adjusted return |
| std_dev_ann_pct    | Decimal   | Annualized standard deviation |
| max_drawdown_pct   | Decimal   | Maximum drawdown percentage   |
| aum_crore          | Decimal   | Assets Under Management       |
| expense_ratio_pct  | Decimal   | Expense ratio (%)             |
| morningstar_rating | Integer   | Morningstar rating (1–5)      |
| risk_grade         | Text      | Risk category                 |

---

# Dataset 8 : Investor Transactions

**Source:** `08_investor_transactions.csv`

| Column             | Data Type | Description                    |
| ------------------ | --------- | ------------------------------ |
| investor_id        | Text      | Unique investor ID             |
| transaction_date   | Date      | Transaction date               |
| amfi_code          | Integer   | AMFI scheme code               |
| transaction_type   | Text      | SIP, Lumpsum or Redemption     |
| amount_inr         | Decimal   | Transaction amount (₹)         |
| state              | Text      | Investor state                 |
| city               | Text      | Investor city                  |
| city_tier          | Text      | T30 or B30 city classification |
| age_group          | Text      | Investor age group             |
| gender             | Text      | Investor gender                |
| annual_income_lakh | Decimal   | Annual income (Lakhs)          |
| payment_mode       | Text      | Mode of payment                |
| kyc_status         | Text      | KYC verification status        |

---

# Dataset 9 : Portfolio Holdings

**Source:** `09_portfolio_holdings.csv`

| Column       | Data Type | Description         |
| ------------ | --------- | ------------------- |
| amfi_code    | Integer   | AMFI scheme code    |
| company_name | Text      | Company invested in |
| sector       | Text      | Industry sector     |
| holding_pct  | Decimal   | Percentage holding  |

---

# Dataset 10 : Benchmark Indices

**Source:** `10_benchmark_indices.csv`

| Column        | Data Type | Description          |
| ------------- | --------- | -------------------- |
| date          | Date      | Trading date         |
| index_name    | Text      | Benchmark index name |
| closing_value | Decimal   | Closing index value  |

---

# Data Cleaning Summary

The following preprocessing steps were completed during Day 2:

* Converted date columns to datetime format.
* Removed duplicate records.
* Standardized transaction type values.
* Validated KYC status values.
* Validated positive transaction amounts.
* Validated NAV values.
* Validated return columns as numeric.
* Checked expense ratio range (0.1%–2.5%).
* Saved cleaned datasets into the `data/processed` directory.

---

# Database

SQLite Database:

`data/processed/bluestock.db`

Tables Created:

* dim_fund
* fact_nav
* fact_transactions
* fact_performance
* fact_aum

---

# Author

Dhruv Trivedi

Bluestock Internship Project

Day 2
