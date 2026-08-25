import pandas as pd

#LOAD DATASET


file_path = "data/superstore-sales.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("INDIAN RETAIL SALES ANALYSIS")
print("=" * 60)

#DATASET SHAPE

print("\n--- DATASET SHAPE ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

#COLUMN NAMES

print("\n--- COLUMN NAMES ---")

for column in df.columns:print(column)



#DATA TYPES

print("\n--- DATA TYPES ---")

print(df.dtypes)

#MISSING VALUES

print("\n--- MISSING VALUES ---")
missing_values = df.isnull().sum()
print(missing_values)


#DUPLICATE RECORDS
print("\n--- DUPLICATE RECORDS ---")
duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

# STATISTICAL SUMMARY

print("\n--- STATISTICAL SUMMARY ---")
print(df.describe())

#UNIQUE VALUES

print("\n--- UNIQUE VALUES ---")

for column in df.columns:
    print(column, ":", df[column].nunique())

#CATEGORY DISTRIBUTION
print("\n--- CATEGORY DISTRIBUTION ---")
print(df["Category"].value_counts())


# SUB-CATEGORY DISTRIBUTION


print("\n--- SUB-CATEGORY DISTRIBUTION ---")

print(df["Sub_Category"].value_counts())


# 11. CUSTOMER TYPE

print("\n--- CUSTOMER TYPE ---")
print(df["Customer_Type"].value_counts())

# 12. REGION / STATE DISTRIBUTION

print("\n--- STATE DISTRIBUTION ---")
print(df["State"].value_counts())

# 13. PAYMENT METHOD

print("\n--- PAYMENT METHOD ---")
print(df["Payment_Method"].value_counts())

# SHIPPING MODE
print("\n--- SHIPPING MODE ---")
print(df["Ship_Mode"].value_counts())

#RETURN STATUS
print("\n--- RETURN STATUS ---")
print(df["Returned"].value_counts())

# BUSINESS KPIs
total_sales = df["Sales_INR"].sum()

total_profit = df["Profit_INR"].sum()

total_orders = df["Order_ID"].nunique()

total_customers = df["Customer_ID"].nunique()

total_units = df["Quantity"].sum()

profit_margin = (total_profit / total_sales) * 100

average_order_value = total_sales / total_orders

return_rate = (df["Returned"].eq("Yes").sum() / total_orders) * 100

print("\n--- BUSINESS KPIs ---")

print(f"Total Sales: ₹{total_sales:,.2f}")

print(f"Total Profit: ₹{total_profit:,.2f}")

print(f"Total Orders: {total_orders}")

print(f"Total Customers: {total_customers}")

print(f"Total Units Sold: {total_units}")

print(f"Profit Margin: {profit_margin:.2f}%")

print(f"Average Order Value: ₹{average_order_value:,.2f}")

print(f"Return Rate: {return_rate:.2f}%")



#SALES BY CATEGORY

print("\n--- SALES BY CATEGORY ---")

category_sales = (df.groupby("Category")["Sales_INR"].sum().sort_values(ascending=False))
print(category_sales)


# PROFIT BY CATEGORY


print("\n--- PROFIT BY CATEGORY ---")

category_profit = (df.groupby("Category")["Profit_INR"].sum().sort_values(ascending=False))
print(category_profit)


#SALES BY STATE

print("\n--- SALES BY STATE ---")

state_sales = (df.groupby("State")["Sales_INR"].sum().sort_values(ascending=False))
print(state_sales)

# PROFIT BY STATE

print("\n--- PROFIT BY STATE ---")
state_profit = (df.groupby("State")["Profit_INR"].sum().sort_values(ascending=False))
print(state_profit)

#TOP 10 PRODUCTS BY SALES

print("\n--- TOP 10 PRODUCTS BY SALES ---")

top_products = (df.groupby("Product_Name")["Sales_INR"].sum().sort_values(ascending=False).head(10))
print(top_products)

#TOP 10 PRODUCTS BY PROFIT

print("\n--- TOP 10 PRODUCTS BY PROFIT ---")

top_profit_products = (df.groupby("Product_Name")["Profit_INR"].sum().sort_values(ascending=False).head(10))
print(top_profit_products)


#LOWEST 10 PRODUCTS BY PROFIT


print("\n--- LOWEST 10 PRODUCTS BY PROFIT ---")

low_profit_products = (df.groupby("Product_Name")["Profit_INR"].sum().sort_values(ascending=True).head(10))
print(low_profit_products)



# MONTHLY SALES

print("\n--- MONTHLY SALES ---")

monthly_sales = (df.groupby(["Year", "Month", "Month_Name"])["Sales_INR"].sum().reset_index().sort_values(["Year", "Month"]))
print(monthly_sales)



# MONTHLY PROFIT


print("\n--- MONTHLY PROFIT ---")

monthly_profit = (df.groupby(["Year", "Month", "Month_Name"])["Profit_INR"].sum().reset_index().sort_values(["Year", "Month"]))
print(monthly_profit)

print("\n" + "=" * 60)
print("DATA UNDERSTANDING COMPLETED")
print("=" * 60)