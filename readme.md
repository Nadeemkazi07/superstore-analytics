# Indian Retail Sales Analytics

## Project Overview

Indian Retail Sales Analytics is a mini data analytics project created to analyze retail sales data from an Indian business perspective.

The project uses a 500-record retail sales dataset and covers the complete data analyst workflow:

- Data Understanding
- Data Cleaning
- Exploratory Data Analysis (EDA)
- SQL Analysis
- Business KPI Analysis
- Power BI Dashboard
- Streamlit Dashboard
- Business Insights

The main objective is to understand sales performance, profitability, customer behavior, product performance, discounts, returns, and delivery performance.

---

## Dataset

The dataset contains 500 retail sales records and 30 columns.

### Dataset Size

- Rows: 500
- Columns: 30
- Customers: 168
- Products: 20
- States: 10
- Categories: 5
- Sub-Categories: 14

### Main Columns

- Order_ID
- Order_Date
- Ship_Date
- Ship_Mode
- Customer_ID
- Customer_Name
- Customer_Type
- State
- City
- Country
- Product_ID
- Category
- Sub_Category
- Product_Name
- Unit_Price_INR
- Quantity
- Discount_Pct
- Sales_INR
- Cost_INR
- Profit_INR
- Payment_Method
- Delivery_Days
- Customer_Rating
- Returned
- Return_Reason
- Year
- Month
- Month_Name
- Quarter
- Profit_Margin_Pct

---

# 1. Data Understanding

The first stage of the project was understanding the dataset structure.

The following checks were performed:

- Dataset shape
- Column names
- Data types
- Missing values
- Duplicate records
- Statistical summary
- Unique values
- Category distribution
- Sub-category distribution
- Customer type distribution
- State distribution
- Payment method distribution
- Shipping mode distribution
- Return status
- Business KPIs

### Dataset Quality

- Total Records: 500
- Duplicate Records: 0
- Missing Values Before Cleaning: Return_Reason contained 459 "Not Applicable" values
- Missing Values After Cleaning: 0
- Invalid Customer Ratings: 0
- Invalid Discounts: 0
- Invalid Quantities: 0
- Invalid Sales Records: 0
- Invalid Cost Records: 0
- Inconsistent Delivery Days: 0

---

# 2. Data Cleaning

Python and Pandas were used for data cleaning.

The following tasks were performed:

- Loaded the CSV dataset
- Converted Order_Date to datetime
- Converted Ship_Date to datetime
- Checked duplicate records
- Checked missing values
- Standardized Return_Reason
- Checked customer ratings
- Checked discount values
- Checked quantity values
- Checked sales and cost values
- Checked delivery days
- Identified loss-making orders
- Saved the cleaned dataset

### Cleaning Results

- Rows: 500
- Columns: 30
- Missing Values: 0
- Duplicate Records: 0
- Loss-making Orders: 11
- Total Loss: ₹31,965.39

The cleaned dataset was saved as:

`indian_retail_sales_cleaned.csv`

---

# 3. Exploratory Data Analysis

EDA was performed using Python and Pandas.

The analysis focused on sales, profit, products, customers, states, discounts, returns, and delivery performance.

---

## Business KPIs

| KPI | Value |
|---|---:|
| Total Sales | ₹21,610,887.56 |
| Total Profit | ₹3,376,226.49 |
| Total Orders | 500 |
| Total Customers | 168 |
| Total Units Sold | 1,034 |
| Profit Margin | 15.62% |
| Average Order Value | ₹43,221.78 |
| Return Rate | 8.20% |

---

# 4. Sales by Category

| Category | Sales |
|---|---:|
| Electronics | ₹16,851,417.79 |
| Home Appliances | ₹3,658,896.24 |
| Home & Furniture | ₹766,971.06 |
| Fashion | ₹271,564.91 |
| Beauty & Personal Care | ₹62,037.56 |

Electronics generated the highest sales and was the main revenue-generating category.

---

# 5. Profit by Category

| Category | Profit |
|---|---:|
| Electronics | ₹2,510,923.86 |
| Home Appliances | ₹565,344.41 |
| Home & Furniture | ₹178,175.46 |
| Fashion | ₹97,129.95 |
| Beauty & Personal Care | ₹24,652.81 |

Electronics generated the highest total profit.

---

# 6. Profit Margin by Category

| Category | Profit Margin |
|---|---:|
| Beauty & Personal Care | 39.74% |
| Fashion | 35.77% |
| Home & Furniture | 23.23% |
| Home Appliances | 15.45% |
| Electronics | 14.90% |

An important finding is that Electronics generates the highest revenue but has the lowest profit margin among the categories.

Beauty & Personal Care has the highest profit margin despite having the lowest sales.

---

# 7. Sales by State

| State | Sales |
|---|---:|
| Karnataka | ₹3,389,294.62 |
| Maharashtra | ₹3,016,193.72 |
| Kerala | ₹2,825,812.70 |
| Uttar Pradesh | ₹2,425,083.00 |
| Tamil Nadu | ₹2,343,914.60 |
| Telangana | ₹1,993,901.94 |
| West Bengal | ₹1,881,264.29 |
| Delhi | ₹1,827,003.68 |
| Rajasthan | ₹1,093,445.64 |
| Gujarat | ₹814,973.37 |

Karnataka generated the highest sales among the states.

---

# 8. Top Products by Sales

The top products by sales were:

1. HP 15s Laptop
2. Samsung Galaxy S24
3. Apple iPhone 15
4. Lenovo IdeaPad Slim 3
5. Samsung 7kg Washing Machine
6. Samsung 43-inch Smart TV
7. OnePlus Nord CE 4
8. Sony WH-1000XM5 Headphones
9. LG 260L Refrigerator
10. Philips Air Fryer

HP 15s Laptop generated the highest sales.

---

# 9. Top Products by Profit

The top products by profit were:

1. Samsung Galaxy S24
2. HP 15s Laptop
3. Apple iPhone 15
4. Lenovo IdeaPad Slim 3
5. Samsung 7kg Washing Machine
6. OnePlus Nord CE 4
7. Samsung 43-inch Smart TV
8. Sony WH-1000XM5 Headphones
9. LG 260L Refrigerator
10. Philips Air Fryer

Samsung Galaxy S24 generated the highest profit.

---

# 10. Customer Analysis

### Sales by Customer Type

| Customer Type | Sales |
|---|---:|
| Consumer | ₹12,224,456.03 |
| Corporate | ₹5,064,389.92 |
| Small Business | ₹4,322,041.61 |

Consumer customers contributed the highest sales.

---

# 11. Payment Method Analysis

| Payment Method | Sales |
|---|---:|
| UPI | ₹8,436,314.14 |
| Cash on Delivery | ₹4,619,984.37 |
| Credit Card | ₹3,629,492.72 |
| Debit Card | ₹3,124,196.59 |
| Net Banking | ₹967,422.58 |
| Wallet | ₹833,477.16 |

UPI was the most commonly used and highest-revenue payment method.

This shows the importance of digital payment methods in Indian retail.

---

# 12. Monthly Sales Analysis

Monthly sales were analyzed to understand changes in revenue throughout the year.

| Month | Sales |
|---|---:|
| January | ₹2,250,604.04 |
| February | ₹1,119,279.27 |
| March | ₹2,459,331.41 |
| April | ₹1,298,057.77 |
| May | ₹1,804,832.16 |
| June | ₹952,589.27 |
| July | ₹2,250,799.05 |
| August | ₹2,102,075.62 |
| September | ₹1,635,771.47 |
| October | ₹1,758,012.19 |
| November | ₹2,437,535.82 |
| December | ₹1,541,999.49 |

March had the highest monthly sales.

June had the lowest monthly sales.

---

# 13. Discount vs Profit Analysis

The correlation between discount and profit was:

**-0.31**

This indicates a moderate negative relationship between discount and profit.

As discounts increase, profit tends to decrease.

### Average Profit by Discount

| Discount | Average Profit |
|---|---:|
| 0% | ₹11,155.53 |
| 5% | ₹7,152.65 |
| 10% | ₹7,888.82 |
| 15% | ₹3,805.68 |
| 20% | ₹1,090.36 |
| 25% | -₹448.06 |

At a 25% discount, the average profit became negative.

This suggests that high discounts should be carefully controlled.

---

# 14. Loss-Making Orders

There were:

**11 loss-making orders**

Total loss:

**₹31,965.39**

Most loss-making orders were associated with higher discount levels, particularly 20% and 25%.

This supports the finding that excessive discounting can negatively affect profitability.

---

# 15. Return Analysis

### Return Status

| Status | Orders |
|---|---:|
| No | 459 |
| Yes | 41 |

Return Rate:

**8.20%**

### Return Reasons

| Return Reason | Orders |
|---|---:|
| Wrong Product | 12 |
| Size/Fit Issue | 10 |
| Damaged Product | 8 |
| Late Delivery | 8 |
| Changed Mind | 3 |

Wrong Product was the most common return reason.

---

# 16. Delivery and Customer Rating

Average customer ratings were analyzed based on delivery days.

The results showed that customer ratings generally decreased as delivery time increased.

For example:

- 1 day: 4.28 average rating
- 2 days: 4.30 average rating
- 3 days: 4.17 average rating
- 4 days: 4.00 average rating
- 5 days: 4.00 average rating
- 6 days: 3.77 average rating
- 7 days: 3.76 average rating

This suggests that faster delivery can contribute to better customer satisfaction.

---

# 17. SQL Analysis

MySQL was used to perform business-oriented SQL analysis.

The SQL analysis includes:

- Total sales
- Total profit
- Total orders
- Total customers
- Sales by category
- Profit by category
- Sales by state
- Sales by customer type
- Sales by payment method
- Top products
- Monthly sales
- Loss-making orders
- Return analysis

SQL file:

`sql/indian_retail_analysis.sql`

---

# 18. Power BI Dashboard

Power BI was used to create an interactive dashboard for business reporting.

The dashboard includes:

- Total Sales
- Total Profit
- Total Orders
- Total Customers
- Total Units
- Profit Margin
- Monthly Sales Trend
- Sales by Category
- Profit by Category
- Top Products
- State-level analysis
- Customer analysis

Power BI file:

`Power bi/Indian_Retail_Sales_Analytics.pbix`

---

# 19. Streamlit Dashboard

A Streamlit dashboard was also created to provide an interactive web-based view of the analysis.

The Streamlit application includes:

- Project title
- Business KPIs
- Dataset overview
- Customer information
- Product information
- Dataset preview
- Sales and business analysis

Streamlit application:

`Streamlit/app.py`

The dashboard was created using Python, Pandas, and Streamlit.

---

# 20. Tools and Technologies

### Programming

- Python
- Pandas
- Matplotlib

### Database

- MySQL
- MySQL Workbench

### Visualization

- Power BI
- Streamlit
- Matplotlib

### Development

- Visual Studio Code
- Python Virtual Environment
- Git / GitHub

---

# 21. Project Structure

```text
superstore-Analytics/
│
├── data/
│   ├── indian_retail_sales_cleaned.csv
│   └── superstore-sales.csv
│
├── Power bi/
│   └── Indian_Retail_Sales_Analytics.pbix
│
├── python/
│   ├── data_cleaning.py
│   ├── data_understanding.py
│   └── eda.py
│
├── sql/
│   └── indian_retail_analysis.sql
│
├── Streamlit/
│   └── app.py
│
├── visualizations/
│
├── README.md
└── .gitignore