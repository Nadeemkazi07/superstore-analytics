import pandas as pd
import matplotlib.pyplot as plt


# LOAD CLEANED DATASET

file_path = "data/indian_retail_sales_cleaned.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 60)


# CREATE VISUALIZATION FOLDER

import os

os.makedirs("visualizations", exist_ok=True)

#SALES BY CATEGORY

category_sales = (df.groupby("Category")["Sales_INR"].sum().sort_values(ascending=False))

print("\n--- SALES BY CATEGORY ---")
print(category_sales)


plt.figure(figsize=(10, 6))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visualizations/01_sales_by_category.png")
plt.show()

# PROFIT BY CATEGORY

category_profit = (df.groupby("Category")["Profit_INR"].sum().sort_values(ascending=False))

print("\n--- PROFIT BY CATEGORY ---")
print(category_profit)
plt.figure(figsize=(10, 6))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit (INR)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visualizations/02_profit_by_category.png")
plt.show()

#  MONTHLY SALES TREND

monthly_sales = (df.groupby(["Month", "Month_Name"])["Sales_INR"].sum().reset_index().sort_values("Month"))

print("\n--- MONTHLY SALES ---")
print(monthly_sales)
plt.figure(figsize=(12, 6))
plt.plot(monthly_sales["Month_Name"],monthly_sales["Sales_INR"],marker="o")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/03_monthly_sales_trend.png")
plt.show()

# MONTHLY PROFIT TREND

monthly_profit = (df.groupby(["Month", "Month_Name"])["Profit_INR"].sum().reset_index().sort_values("Month"))

print("\n--- MONTHLY PROFIT ---")
print(monthly_profit)
plt.figure(figsize=(12, 6))
plt.plot(monthly_profit["Month_Name"],monthly_profit["Profit_INR"],marker="o")
plt.title("Monthly Profit Trend")
plt.xlabel("Month")
plt.ylabel("Profit (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/04_monthly_profit_trend.png")
plt.show()


#SALES BY STATE

state_sales = (df.groupby("State")["Sales_INR"].sum().sort_values(ascending=False))

print("\n--- SALES BY STATE ---")
print(state_sales)
plt.figure(figsize=(12, 6))
state_sales.plot(kind="bar")
plt.title("Sales by State")
plt.xlabel("State")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/05_sales_by_state.png")
plt.show()

# PROFIT BY STATE

state_profit = (df.groupby("State")["Profit_INR"].sum().sort_values(ascending=False))

print("\n--- PROFIT BY STATE ---")
print(state_profit)

plt.figure(figsize=(12, 6))
state_profit.plot(kind="bar")
plt.title("Profit by State")
plt.xlabel("State")
plt.ylabel("Profit (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visualizations/06_profit_by_state.png")
plt.show()

#  TOP 10 PRODUCTS BY SALES

top_products = (df.groupby("Product_Name")["Sales_INR"].sum().sort_values(ascending=False).head(10))

print("\n--- TOP 10 PRODUCTS BY SALES ---")
print(top_products)

plt.figure(figsize=(12, 6))
top_products.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Sales")
plt.xlabel("Sales (INR)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("visualizations/07_top_10_products_sales.png")
plt.show()

#TOP 10 PRODUCTS BY PROFIT

top_profit_products = (df.groupby("Product_Name")["Profit_INR"].sum().sort_values(ascending=False).head(10))

print("\n--- TOP 10 PRODUCTS BY PROFIT ---")
print(top_profit_products)

plt.figure(figsize=(12, 6))
top_profit_products.sort_values().plot(kind="barh")
plt.title("Top 10 Products by Profit")
plt.xlabel("Profit (INR)")
plt.ylabel("Product")
plt.tight_layout()
plt.savefig("visualizations/08_top_10_products_profit.png")
plt.show()

#CUSTOMER TYPE SALES

customer_sales = (df.groupby("Customer_Type")["Sales_INR"].sum().sort_values(ascending=False))

print("\n--- SALES BY CUSTOMER TYPE ---")
print(customer_sales)

plt.figure(figsize=(8, 6))
customer_sales.plot(kind="bar")
plt.title("Sales by Customer Type")
plt.xlabel("Customer Type")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visualizations/09_sales_by_customer_type.png")
plt.show()

# PAYMENT METHOD ANALYSIS

payment_sales = (df.groupby("Payment_Method")["Sales_INR"].sum().sort_values(ascending=False))

print("\n--- SALES BY PAYMENT METHOD ---")
print(payment_sales)

plt.figure(figsize=(10, 6))
payment_sales.plot(kind="bar")
plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Sales (INR)")
plt.xticks(rotation=30)
plt.tight_layout()

# PROFIT MARGIN BY CATEGORY

category_margin = (df.groupby("Category").agg(Sales=("Sales_INR", "sum"),Profit=("Profit_INR", "sum")))

category_margin["Profit_Margin_Pct"] = (category_margin["Profit"] /category_margin["Sales"]) * 100

category_margin = category_margin.sort_values("Profit_Margin_Pct",ascending=False)

print("\n--- PROFIT MARGIN BY CATEGORY ---")
print(category_margin)

plt.figure(figsize=(10, 6))
category_margin["Profit_Margin_Pct"].plot(kind="bar")
plt.title("Profit Margin by Category")
plt.xlabel("Category")
plt.ylabel("Profit Margin (%)")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visualizations/11_profit_margin_by_category.png")
plt.show()

# DISCOUNT VS PROFIT

print("\n--- DISCOUNT VS PROFIT CORRELATION ---")

discount_profit_corr = df[["Discount_Pct", "Profit_INR"]].corr().iloc[0, 1]

print("Correlation between Discount and Profit:",round(discount_profit_corr, 3))

plt.figure(figsize=(10, 6))
plt.scatter(df["Discount_Pct"] * 100,df["Profit_INR"])
plt.title("Discount vs Profit")
plt.xlabel("Discount (%)")
plt.ylabel("Profit (INR)")
plt.tight_layout()
plt.savefig("visualizations/12_discount_vs_profit.png")
plt.show()

#PROFIT BY DISCOUNT LEVEL

discount_profit = (df.groupby("Discount_Pct")["Profit_INR"].mean())
print("\n--- AVERAGE PROFIT BY DISCOUNT ---")
print(discount_profit)

plt.figure(figsize=(10, 6))
discount_profit.plot(kind="bar")
plt.title("Average Profit by Discount Level")
plt.xlabel("Discount")
plt.ylabel("Average Profit (INR)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visualizations/13_average_profit_by_discount.png")
plt.show()

#  LOSS-MAKING ORDERS

loss_orders = df[df["Profit_INR"] < 0].sort_values("Profit_INR")
print("\n--- LOSS-MAKING ORDERS ---")
print(loss_orders[["Order_ID","Product_Name", "Category","State","Quantity","Discount_Pct","Sales_INR","Profit_INR"]])
        
#  RETURN ANALYSIS

return_counts = df["Returned"].value_counts()
print("\n--- RETURN ANALYSIS ---")
print(return_counts)

return_rate = (df["Returned"].eq("Yes").mean()) * 100

print(f"Return Rate: {return_rate:.2f}%")

plt.figure(figsize=(7, 6))
return_counts.plot(kind="bar")
plt.title("Returned vs Non-Returned Orders")
plt.xlabel("Return Status")
plt.ylabel("Number of Orders")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visualizations/14_return_analysis.png")
plt.show()

#  RETURN REASONS

return_reasons = (df[df["Returned"] == "Yes"]["Return_Reason"].value_counts())

print("\n--- RETURN REASONS ---")
print(return_reasons)
plt.figure(figsize=(10, 6))
return_reasons.plot(kind="bar")
plt.title("Reasons for Product Returns")
plt.xlabel("Return Reason")
plt.ylabel("Number of Returns")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("visualizations/15_return_reasons.png")
plt.show()

#  DELIVERY DAYS VS RATING

delivery_rating = (df.groupby("Delivery_Days")["Customer_Rating"].mean())
print("\n--- DELIVERY DAYS VS CUSTOMER RATING ---")
print(delivery_rating)

plt.figure(figsize=(10, 6))

delivery_rating.plot(kind="line",marker="o")

plt.title("Delivery Days vs Customer Rating")
plt.xlabel("Delivery Days")
plt.ylabel("Average Customer Rating")
plt.tight_layout()
plt.savefig("visualizations/16_delivery_vs_rating.png")
plt.show()

#  DELIVERY DAYS VS RETURN RATE

delivery_return = (df.groupby("Delivery_Days")["Returned"].apply(lambda x: (x == "Yes").mean() * 100))

print("\n--- DELIVERY DAYS VS RETURN RATE ---")
print(delivery_return)
plt.figure(figsize=(10, 6))

delivery_return.plot(kind="line",marker="o")
plt.title("Delivery Days vs Return Rate")
plt.xlabel("Delivery Days")
plt.ylabel("Return Rate (%)")
plt.tight_layout()
plt.savefig("visualizations/17_delivery_vs_return_rate.png")
plt.show()

