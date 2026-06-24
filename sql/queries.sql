-- ===========================================================
-- BLUESTOCK MUTUAL FUND ANALYTICS PLATFORM
-- Day 2 - Analytical SQL Queries
-- ===========================================================


-- ===========================================================
-- QUERY 1
-- Top 5 Funds by Assets Under Management (AUM)
-- ===========================================================

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;



-- ===========================================================
-- QUERY 2
-- Average NAV Per Month
-- ===========================================================

SELECT
    strftime('%Y-%m', date) AS Month,
    ROUND(AVG(nav),2) AS Average_NAV
FROM fact_nav
GROUP BY Month
ORDER BY Month;



-- ===========================================================
-- QUERY 3
-- SIP Year-wise Growth
-- ===========================================================

SELECT
    strftime('%Y', transaction_date) AS Year,
    COUNT(*) AS SIP_Transactions,
    ROUND(SUM(amount_inr),2) AS Total_SIP_Amount
FROM fact_transactions
WHERE transaction_type='Sip'
GROUP BY Year
ORDER BY Year;



-- ===========================================================
-- QUERY 4
-- Transactions by State
-- ===========================================================

SELECT
    state,
    COUNT(*) AS Total_Transactions,
    ROUND(SUM(amount_inr),2) AS Total_Investment
FROM fact_transactions
GROUP BY state
ORDER BY Total_Transactions DESC;



-- ===========================================================
-- QUERY 5
-- Funds Having Expense Ratio Less Than 1%
-- ===========================================================

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;



-- ===========================================================
-- QUERY 6
-- Top 10 Funds by 1-Year Return
-- ===========================================================

SELECT
    scheme_name,
    fund_house,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;



-- ===========================================================
-- QUERY 7
-- Average Investment Amount by City Tier
-- ===========================================================

SELECT
    city_tier,
    ROUND(AVG(amount_inr),2) AS Average_Investment
FROM fact_transactions
GROUP BY city_tier;



-- ===========================================================
-- QUERY 8
-- Most Used Payment Modes
-- ===========================================================

SELECT
    payment_mode,
    COUNT(*) AS Total_Transactions
FROM fact_transactions
GROUP BY payment_mode
ORDER BY Total_Transactions DESC;



-- ===========================================================
-- QUERY 9
-- Gender-wise Investment Summary
-- ===========================================================

SELECT
    gender,
    COUNT(*) AS Total_Investors,
    ROUND(SUM(amount_inr),2) AS Total_Investment,
    ROUND(AVG(amount_inr),2) AS Average_Investment
FROM fact_transactions
GROUP BY gender;



-- ===========================================================
-- QUERY 10
-- Average Expense Ratio by Fund House
-- ===========================================================

SELECT
    fund_house,
    ROUND(AVG(expense_ratio_pct),2) AS Average_Expense_Ratio
FROM fact_performance
GROUP BY fund_house
ORDER BY Average_Expense_Ratio;



-- ===========================================================
-- BONUS QUERY 11
-- Highest Average 3-Year Return by Fund House
-- ===========================================================

SELECT
    fund_house,
    ROUND(AVG(return_3yr_pct),2) AS Avg_3Y_Return
FROM fact_performance
GROUP BY fund_house
ORDER BY Avg_3Y_Return DESC;



-- ===========================================================
-- BONUS QUERY 12
-- Average Transaction Amount by Payment Mode
-- ===========================================================

SELECT
    payment_mode,
    ROUND(AVG(amount_inr),2) AS Average_Transaction
FROM fact_transactions
GROUP BY payment_mode
ORDER BY Average_Transaction DESC;



-- ===========================================================
-- BONUS QUERY 13
-- Top 10 Cities by Investment Amount
-- ===========================================================

SELECT
    city,
    ROUND(SUM(amount_inr),2) AS Total_Investment
FROM fact_transactions
GROUP BY city
ORDER BY Total_Investment DESC
LIMIT 10;



-- ===========================================================
-- BONUS QUERY 14
-- Count of Investors by KYC Status
-- ===========================================================

SELECT
    kyc_status,
    COUNT(*) AS Investors
FROM fact_transactions
GROUP BY kyc_status;



-- ===========================================================
-- BONUS QUERY 15
-- Average NAV for Each Mutual Fund
-- ===========================================================

SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS Average_NAV
FROM fact_nav
GROUP BY amfi_code
ORDER BY Average_NAV DESC;