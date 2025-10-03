import pandas as pd

# CSV dan o‘qish
sales_df = pd.read_csv("task\\sales_data.csv")

# 1. Group by Category – aggregate statistics
category_stats = sales_df.groupby("Category").agg(
    total_quantity=("Quantity", "sum"),
    avg_price=("Price", "mean"),
    max_quantity=("Quantity", "max")
).reset_index()
print("Category statistics:\n", category_stats, "\n")

# 2. Top-selling product in each category
top_products = sales_df.groupby(["Category", "Product"])["Quantity"].sum().reset_index()
top_products = top_products.sort_values(["Category", "Quantity"], ascending=[True, False])
top_products = top_products.groupby("Category").head(1)
print("Top-selling product in each category:\n", top_products, "\n")

# 3. Date with highest total sales (Quantity * Price)
sales_df["TotalSale"] = sales_df["Quantity"] * sales_df["Price"]
highest_sales_date = sales_df.groupby("Date")["TotalSale"].sum().idxmax()
print("Date with highest total sales:", highest_sales_date)
import pandas as pd

# CSV dan o‘qish
orders_df = pd.read_csv("task\\customer_orders.csv")

# 1. Customers with >= 20 orders
orders_count = orders_df.groupby("CustomerID")["OrderID"].count().reset_index()
active_customers = orders_count[orders_count["OrderID"] >= 20]
print("Customers with >= 20 orders:\n", active_customers, "\n")

# 2. Customers with avg price per unit > 120
avg_price_customers = orders_df.groupby("CustomerID")["Price"].mean().reset_index()
high_price_customers = avg_price_customers[avg_price_customers["Price"] > 120]
print("Customers avg price > 120:\n", high_price_customers, "\n")

# 3. Total quantity and price per product; filter products with total qty >= 5
product_stats = orders_df.groupby("Product").agg(
    total_quantity=("Quantity", "sum"),
    total_price=("Price", "sum")
).reset_index()
product_stats = product_stats[product_stats["total_quantity"] >= 5]
print("Product stats with total quantity >= 5:\n", product_stats, "\n")
import pandas as pd
import sqlite3

# 1. DB dan o‘qish
conn = sqlite3.connect("task\\population.db")
population_df = pd.read_sql("SELECT * FROM population", conn)
conn.close()

# 2. Salary bands fayldan o‘qish
salary_bands = pd.read_excel("task\\population salary analysis.xlsx")

# Salary bandlarni merge qilish uchun
# band faylida: MinSalary, MaxSalary, Category kabi ustunlar bo‘lishi kerak
def categorize_salary(salary, bands):
    for _, row in bands.iterrows():
        if row["MinSalary"] <= salary <= row["MaxSalary"]:
            return row["Category"]
    return "Unknown"

population_df["SalaryCategory"] = population_df["Salary"].apply(lambda x: categorize_salary(x, salary_bands))

# 3. Category bo‘yicha hisob-kitob
category_stats = population_df.groupby("SalaryCategory").agg(
    population_count=("Salary", "count"),
    avg_salary=("Salary", "mean"),
    median_salary=("Salary", "median")
).reset_index()

# Foiz hisoblash
total_pop = population_df.shape[0]
category_stats["percentage"] = (category_stats["population_count"] / total_pop) * 100
print("Salary Category Statistics:\n", category_stats, "\n")

# 4. Har bir State bo‘yicha hisob-kitob
state_category_stats = population_df.groupby(["State", "SalaryCategory"]).agg(
    population_count=("Salary", "count"),
    avg_salary=("Salary", "mean"),
    median_salary=("Salary", "median")
).reset_index()

# Har bir state ichida foiz hisoblash
state_totals = state_category_stats.groupby("State")["population_count"].transform("sum")
state_category_stats["percentage"] = (state_category_stats["population_count"] / state_totals) * 100
print("State-wise Salary Category Statistics:\n", state_category_stats)
