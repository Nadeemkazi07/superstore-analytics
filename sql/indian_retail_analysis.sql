CREATE database indian_retail_analytics;

USE indian_retail_analytics;

SELECT COUNT(*) AS total_records
FROM sales;

SELECT *
FROM sales
LIMIT 10;
SELECT 
    SUM(Sales_INR) AS Total_Sales,
    SUM(Profit_INR) AS Total_Profit,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Total_Customers,
    SUM(Quantity) AS Total_Units
FROM sales;

SELECT
    ROUND(SUM(Sales_INR), 2) AS Total_Sales,
    ROUND(SUM(Profit_INR), 2) AS Total_Profit,
    ROUND(
        (SUM(Profit_INR) / SUM(Sales_INR)) * 100,
        2
    ) AS Profit_Margin_Pct,
    ROUND(
        SUM(Sales_INR) / COUNT(DISTINCT Order_ID),
        2
    ) AS Average_Order_Value
FROM sales;

SELECT
    Category,
    ROUND(SUM(Sales_INR), 2) AS Total_Sales,
    ROUND(SUM(Profit_INR), 2) AS Total_Profit,
    ROUND(
        (SUM(Profit_INR) / SUM(Sales_INR)) * 100,
        2
    ) AS Profit_Margin_Pct
FROM sales
GROUP BY Category
ORDER BY Total_Sales DESC;

SELECT
    State,
    ROUND(SUM(Sales_INR), 2) AS Total_Sales,
    ROUND(SUM(Profit_INR), 2) AS Total_Profit,
    ROUND(
        (SUM(Profit_INR) / SUM(Sales_INR)) * 100,
        2
    ) AS Profit_Margin_Pct
FROM sales
GROUP BY State
ORDER BY Total_Sales DESC;

SELECT
    Product_Name,
    ROUND(SUM(Sales_INR), 2) AS Total_Sales,
    ROUND(SUM(Profit_INR), 2) AS Total_Profit
FROM sales
GROUP BY Product_Name
ORDER BY Total_Sales DESC
LIMIT 10;
SELECT
    Product_Name,
    ROUND(SUM(Profit_INR), 2) AS Total_Profit,
    ROUND(SUM(Sales_INR), 2) AS Total_Sales
FROM sales
GROUP BY Product_Name
ORDER BY Total_Profit DESC
LIMIT 10;

SELECT
    Customer_Type,
    COUNT(DISTINCT Order_ID) AS Total_Orders,
    COUNT(DISTINCT Customer_ID) AS Total_Customers,
    ROUND(SUM(Sales_INR), 2) AS Total_Sales,
    ROUND(SUM(Profit_INR), 2) AS Total_Profit
FROM sales
GROUP BY Customer_Type
ORDER BY Total_Sales DESC;

SELECT
    Payment_Method,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Sales_INR), 2) AS Total_Sales,
    ROUND(SUM(Profit_INR), 2) AS Total_Profit
FROM sales
GROUP BY Payment_Method
ORDER BY Total_Sales DESC;

SELECT
    Returned,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Sales_INR), 2) AS Total_Sales,
    ROUND(SUM(Profit_INR), 2) AS Total_Profit
FROM sales
GROUP BY Returned
ORDER BY Total_Orders DESC;

SELECT
    Return_Reason,
    COUNT(*) AS Return_Count
FROM sales
WHERE Returned = 'Yes'
GROUP BY Return_Reason
ORDER BY Return_Count DESC;

SELECT
    Discount_Pct,
    COUNT(*) AS Total_Orders,
    ROUND(SUM(Sales_INR), 2) AS Total_Sales,
    ROUND(SUM(Profit_INR), 2) AS Total_Profit,
    ROUND(AVG(Profit_INR), 2) AS Average_Profit
FROM sales
GROUP BY Discount_Pct
ORDER BY Discount_Pct;

SELECT
    Order_ID,
    Product_Name,
    Category,
    State,
    Quantity,
    Discount_Pct,
    ROUND(Sales_INR, 2) AS Sales,
    ROUND(Profit_INR, 2) AS Profit
FROM sales
WHERE Profit_INR < 0
ORDER BY Profit_INR ASC;

SELECT
    Product_Name,
    COUNT(*) AS Loss_Order_Count,
    ROUND(SUM(Profit_INR), 2) AS Total_Loss
FROM sales
WHERE Profit_INR < 0
GROUP BY Product_Name
ORDER BY Total_Loss ASC;

SELECT
    Delivery_Days,
    COUNT(*) AS Total_Orders,
    ROUND(AVG(Customer_Rating), 2) AS Average_Rating,
    ROUND(
        AVG(
            CASE
                WHEN Returned = 'Yes' THEN 1
                ELSE 0
            END
        ) * 100,
        2
    ) AS Return_Rate_Pct
FROM sales
GROUP BY Delivery_Days
ORDER BY Delivery_Days;

SELECT
    Order_ID,
    Product_Name,
    Category,
    Discount_Pct,
    ROUND(Sales_INR, 2) AS Sales,
    ROUND(Profit_INR, 2) AS Profit
FROM sales
WHERE Discount_Pct >= 0.20
ORDER BY Profit_INR ASC;

WITH product_sales AS (
    SELECT
        Category,
        Product_Name,
        SUM(Sales_INR) AS Total_Sales
    FROM sales
    GROUP BY Category, Product_Name
),

ranked_products AS (
    SELECT
        Category,
        Product_Name,
        ROUND(Total_Sales, 2) AS Total_Sales,
        RANK() OVER (
            PARTITION BY Category
            ORDER BY Total_Sales DESC
        ) AS Product_Rank
    FROM product_sales
)

SELECT
    Category,
    Product_Name,
    Total_Sales,
    Product_Rank
FROM ranked_products
WHERE Product_Rank <= 3
ORDER BY Category, Product_Rank;

SELECT
    Product_Name,
    ROUND(SUM(Sales_INR), 2) AS Total_Sales,
    ROUND(SUM(Profit_INR), 2) AS Total_Profit
FROM sales
GROUP BY Product_Name
HAVING SUM(Sales_INR) > (
    SELECT AVG(product_sales)
    FROM (
        SELECT SUM(Sales_INR) AS product_sales
        FROM sales
        GROUP BY Product_Name
    ) AS product_summary
)
ORDER BY Total_Sales DESC;