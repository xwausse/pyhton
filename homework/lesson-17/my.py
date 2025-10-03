import pandas as pd
import numpy as np

# DataFrame yaratamiz
data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# 1. Columnlarni rename qilish
df = df.rename(columns=lambda x: x.lower().replace(" ", "_"))
print("Renamed DataFrame:\n", df, "\n")

# 2. Birinchi 3 qatorni chiqarish
print("First 3 rows:\n", df.head(3), "\n")

# 3. Mean age
print("Mean age:", df['age'].mean(), "\n")

# 4. Name va City columnlarni chiqarish
print("Name and City:\n", df[['first_name', 'city']], "\n")

# 5. Yangi Salary column qo‘shamiz (tasodifiy qiymatlar bilan)
df['salary'] = np.random.randint(4000, 8000, size=len(df))
print("DataFrame with Salary:\n", df, "\n")

# 6. Summary statistics
print("Summary statistics:\n", df.describe(include='all'))
# DataFrame yaratamiz
sales_and_expenses = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
})

print("Sales and Expenses Data:\n", sales_and_expenses, "\n")

# 1. Maximum
print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max(), "\n")

# 2. Minimum
print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min(), "\n")

# 3. Average
print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())
# DataFrame yaratamiz
expenses = pd.DataFrame({
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
})

print("Original Expenses Data:\n", expenses, "\n")

# Category ni index qilib qo‘yish
expenses = expenses.set_index('Category')
print("With Category as Index:\n", expenses, "\n")

# 1. Max expense for each category
print("Max expense for each category:\n", expenses.max(axis=1), "\n")

# 2. Min expense for each category
print("Min expense for each category:\n", expenses.min(axis=1), "\n")

# 3. Average expense for each category
print("Average expense for each category:\n", expenses.mean(axis=1))
