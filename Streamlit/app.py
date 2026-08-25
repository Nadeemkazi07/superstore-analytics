import streamlit as st
import pandas as pd
from pathlib import Path


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Indian Retail Sales Dashboard",
    page_icon="🛒",
    layout="wide"
)


# --------------------------------------------------
# LOAD DATASET
# --------------------------------------------------

file_path = Path("data") / "indian_retail_sales_cleaned.csv"

df = pd.read_csv(file_path)


# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("🛒 Indian Retail Sales Analysis")

st.write(
    "Interactive dashboard for analysing sales, profit, "
    "customers, products and returns."
)


# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Dashboard Filters")

category_list = ["All"] + sorted(df["Category"].unique().tolist())

selected_category = st.sidebar.selectbox(
    "Select Category",
    category_list
)

state_list = ["All"] + sorted(df["State"].unique().tolist())

selected_state = st.sidebar.selectbox(
    "Select State",
    state_list
)


# --------------------------------------------------
# APPLY FILTERS
# --------------------------------------------------

filtered_df = df.copy()

if selected_category != "All":
    filtered_df = filtered_df[
        filtered_df["Category"] == selected_category
    ]

if selected_state != "All":
    filtered_df = filtered_df[
        filtered_df["State"] == selected_state
    ]


# --------------------------------------------------
# KPI CALCULATIONS
# --------------------------------------------------

total_sales = filtered_df["Sales_INR"].sum()

total_profit = filtered_df["Profit_INR"].sum()

total_orders = filtered_df["Order_ID"].nunique()

total_customers = filtered_df["Customer_ID"].nunique()

total_units = filtered_df["Quantity"].sum()

profit_margin = (
    total_profit / total_sales * 100
    if total_sales != 0
    else 0
)


# --------------------------------------------------
# KPI DISPLAY
# --------------------------------------------------

st.subheader("Business KPIs")

col1, col2, col3, col4, col5, col6 = st.columns(6)

with col1:
    st.metric(
        "Total Sales",
        f"₹{total_sales:,.2f}"
    )

with col2:
    st.metric(
        "Total Profit",
        f"₹{total_profit:,.2f}"
    )

with col3:
    st.metric(
        "Orders",
        f"{total_orders:,}"
    )

with col4:
    st.metric(
        "Customers",
        f"{total_customers:,}"
    )

with col5:
    st.metric(
        "Units Sold",
        f"{total_units:,}"
    )

with col6:
    st.metric(
        "Profit Margin",
        f"{profit_margin:.2f}%"
    )


st.divider()


# --------------------------------------------------
# SALES TREND
# --------------------------------------------------

st.subheader("Monthly Sales Trend")

monthly_sales = (
    filtered_df
    .groupby(["Month", "Month_Name"])["Sales_INR"]
    .sum()
    .reset_index()
    .sort_values("Month")
)

monthly_sales = monthly_sales.set_index("Month_Name")

st.line_chart(
    monthly_sales["Sales_INR"]
)


# --------------------------------------------------
# CATEGORY ANALYSIS
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("Sales by Category")

    category_sales = (
        filtered_df
        .groupby("Category")["Sales_INR"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(category_sales)


with col2:

    st.subheader("Profit by Category")

    category_profit = (
        filtered_df
        .groupby("Category")["Profit_INR"]
        .sum()
        .sort_values(ascending=False)
    )

    st.bar_chart(category_profit)


# --------------------------------------------------
# STATE ANALYSIS
# --------------------------------------------------

st.subheader("Sales by State")

state_sales = (
    filtered_df
    .groupby("State")["Sales_INR"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(state_sales)


# --------------------------------------------------
# TOP PRODUCTS
# --------------------------------------------------

col1, col2 = st.columns(2)


with col1:

    st.subheader("Top 10 Products by Sales")

    top_products_sales = (
        filtered_df
        .groupby("Product_Name")["Sales_INR"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .sort_values()
    )

    st.bar_chart(top_products_sales)


with col2:

    st.subheader("Top 10 Products by Profit")

    top_products_profit = (
        filtered_df
        .groupby("Product_Name")["Profit_INR"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .sort_values()
    )

    st.bar_chart(top_products_profit)


# --------------------------------------------------
# CUSTOMER ANALYSIS
# --------------------------------------------------

st.subheader("Sales by Customer Type")

customer_sales = (
    filtered_df
    .groupby("Customer_Type")["Sales_INR"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(customer_sales)


# --------------------------------------------------
# PAYMENT METHOD
# --------------------------------------------------

st.subheader("Sales by Payment Method")

payment_sales = (
    filtered_df
    .groupby("Payment_Method")["Sales_INR"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(payment_sales)


# --------------------------------------------------
# RETURN ANALYSIS
# --------------------------------------------------

st.subheader("Return Analysis")

return_count = filtered_df["Returned"].value_counts()

col1, col2 = st.columns(2)

with col1:

    st.write("Return Status")

    st.bar_chart(return_count)


with col2:

    returned_orders = (
        filtered_df["Returned"] == "Yes"
    ).sum()

    return_rate = (
        returned_orders / len(filtered_df) * 100
        if len(filtered_df) > 0
        else 0
    )

    st.metric(
        "Return Rate",
        f"{return_rate:.2f}%"
    )


# --------------------------------------------------
# PROFIT MARGIN BY CATEGORY
# --------------------------------------------------

st.subheader("Profit Margin by Category")

margin_data = (
    filtered_df
    .groupby("Category")
    .agg(
        Sales=("Sales_INR", "sum"),
        Profit=("Profit_INR", "sum")
    )
)

margin_data["Profit_Margin_Pct"] = (
    margin_data["Profit"] /
    margin_data["Sales"] * 100
)

margin_data = margin_data.sort_values(
    "Profit_Margin_Pct",
    ascending=False
)

st.dataframe(
    margin_data.round(2),
    use_container_width=True
)


# --------------------------------------------------
# DATA PREVIEW
# --------------------------------------------------

st.subheader("Dataset Preview")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)


# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.caption(
    "Indian Retail Sales Analytics | Python • Pandas • Streamlit • SQL • Power BI"
)