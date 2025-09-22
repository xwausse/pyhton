import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)
print(df)


df = df.rename(columns={"First Name" : "first_name" , "Age" : "age"})
print(df)

df.head()

mean_age = df["age"].mean()
print("Mean Age:", mean_age)

print(df[["first_name", "City"]])


import numpy as np
df["Salary"] = np.random.randint(3000, 7000, size=len(df))
print(df)

dsfs = df.describe()
print(dsfs)

data = {
    'Month' : ['Jan', 'Feb', 'Mar', 'Apr' ],
    'Sales' : [5000, 6000, 7500, 8000],
    'Expenses' : [3000, 3500, 4000, 4500]    
}
df = pd.DataFrame(data)
print(df)

maxim = df['Sales'].max()
expen = df['Expenses'].max()

print("Maximum Sales:", maxim)
print("Maximum Expenses:", expen)

maxim = df['Sales'].min()
expen = df['Expenses'].min()
print("minimum Sales:", maxim)
print("Minimum Expenses:", expen)

mean_sales = df['Sales'].mean()
mean_expen = df['Expenses'].mean()
print("meanimum Sales:", mean_sales)
print("meanimum Expenses:", mean_expen)

data = {
    'Category' : ['Rent','Utilities', 'Groceries', 'Entertainment'],
    'January' : [1200, 200, 300, 150],
    'February' : [1300, 220, 320, 160],
    'March' : [1400,240,330,170],
    'April' : [1500, 250, 350, 180]
}
df = pd.DataFrame(data)
print(df)

df['Max_Expense'] = df[['January','February','March','April']].max(axis=1)

print(df[['Category','Max_Expense']])

df['min_expense'] = df[['January','February','March','April']].min(axis=1)
print(df[['Category', 'min_expense']])

df['mean_expense'] = df[['January','February','March','April']].mean(axis=1)
print(df[['Category', 'mean_expense']])
