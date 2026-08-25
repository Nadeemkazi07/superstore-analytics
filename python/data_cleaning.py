import pandas as pd

#LOAD DATASET

file_path = "data/superstore-sales.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("DATA CLEANING")
print("=" * 60)

#  CHECK ORIGINAL DATA

print("\n--- ORIGINAL DATA ---")

print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

#  CONVERT DATE COLUMNS

df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

print("\n--- DATE CONVERSION ---")

print("Order_Date:", df["Order_Date"].dtype)
print("Ship_Date:", df["Ship_Date"].dtype)

# HANDLE RETURN REASON

df["Return_Reason"] = df["Return_Reason"].fillna("Not Applicable")

print("\n--- RETURN REASON ---")
print(df["Return_Reason"].value_counts())

#CHECK DUPLICATES

duplicate_count = df.duplicated().sum()
print("\n--- DUPLICATES ---")

print("Duplicate rows:", duplicate_count)


if duplicate_count > 0:
    df = df.drop_duplicates()

    print("Duplicates removed.")

else:
    print("No duplicates found.")

# CHECK MISSING VALUES

print("\n--- MISSING VALUES AFTER CLEANING ---")

print(df.isnull().sum())

# CHECK NEGATIVE VALUES

print("\n--- NEGATIVE PROFIT ORDERS ---")

negative_profit = df[df["Profit_INR"] < 0]
print("Number of loss-making orders:", len(negative_profit))
print("Total loss:", negative_profit["Profit_INR"].sum())

# CHECK INVALID RATINGS

print("\n--- CUSTOMER RATING CHECK ---")

invalid_ratings = df[(df["Customer_Rating"] < 1) |(df["Customer_Rating"] > 5)]
print("Invalid ratings:", len(invalid_ratings))

# CHECK DISCOUNT VALUES

print("\n--- DISCOUNT CHECK ---")

invalid_discount = df[(df["Discount_Pct"] < 0) |(df["Discount_Pct"] > 1)]

print("Invalid discount values:", len(invalid_discount))


#  CHECK QUANTITY


print("\n--- QUANTITY CHECK ---")

invalid_quantity = df[df["Quantity"] <= 0]
print("Invalid quantity records:", len(invalid_quantity))

# CHECK SALES / COST / PROFIT LOGIC

print("\n--- FINANCIAL DATA CHECK ---")

invalid_sales = df[df["Sales_INR"] <= 0]
invalid_cost = df[df["Cost_INR"] <= 0]
print("Invalid sales records:", len(invalid_sales))
print("Invalid cost records:", len(invalid_cost))

#  CREATE DELIVERY DAYS CHECK

calculated_delivery_days = (df["Ship_Date"] - df["Order_Date"]).dt.days

delivery_difference = (calculated_delivery_days != df["Delivery_Days"])

print("\n--- DELIVERY DAYS CHECK ---")

print("Records with inconsistent delivery days:",delivery_difference.sum())

# CREATE PROFIT MARGIN

df["Profit_Margin_Pct"] = (df["Profit_INR"] / df["Sales_INR"]) * 100
df["Profit_Margin_Pct"] = df["Profit_Margin_Pct"].round(2)

# CREATE DATE ATTRIBUTES

df["Year"] = df["Order_Date"].dt.year
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.strftime("%B")
df["Quarter"] = "Q" + df["Order_Date"].dt.quarter.astype(str)

# SAVE CLEAN DATASET

output_file = "data/indian_retail_sales_cleaned.csv"

df.to_csv(output_file,index=False)

# FINAL CHECK

print("\n--- FINAL DATASET ---")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])
print("Missing values:", df.isnull().sum())
print("Duplicates:", df.duplicated().sum())
print("\nCleaned dataset saved to:")
print(output_file)
print("\n" + "=" * 60)
print("DATA CLEANING COMPLETED")
print("=" * 60)