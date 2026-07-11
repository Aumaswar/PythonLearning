import pandas as pd


# Creating a Series

numbers = pd.Series([10, 20, 30, 40, 50])

print("Series:")
print(numbers)

print("\n")


# Creating a DataFrame

data = {
    "Name": ["Aum", "Raj", "Priya", "Neha"],
    "Age": [20, 21, 22, 19],
    "Salary": [50000, 30000, 70000, 25000]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\n")


# Head

print("First 2 Rows:")
print(df.head(2))

print("\n")


# Tail

print("Last 2 Rows:")
print(df.tail(2))

print("\n")


# Information about DataFrame

print("Info:")
print(df.info())

print("\n")


# Description

print("Describe:")
print(df.describe())

print("\n")


# Shape

print("Shape:")
print(df.shape)

print("\n")


# Columns

print("Columns:")
print(df.columns)

print("\n")


# Selecting a Column

print("Names Column:")
print(df["Name"])

print("\n")


# Multiple Columns

print("Name and Salary:")
print(df[["Name", "Salary"]])

print("\n")


# Selecting Rows using iloc

print("First Row:")
print(df.iloc[0])

print("\n")


# Filtering Data

print("Salary Greater Than 40000:")
print(df[df["Salary"] > 40000])

print("\n")


# Mean Salary

print("Average Salary:")
print(df["Salary"].mean())

print("\n")


# Maximum Salary

print("Highest Salary:")
print(df["Salary"].max())

print("\n")


# Minimum Salary

print("Lowest Salary:")
print(df["Salary"].min())

print("\n")


# Sorting Data

print("Sorted by Salary:")
print(df.sort_values(by="Salary"))

print("\n")


# Adding a New Column

df["Bonus"] = df["Salary"] * 0.10

print("DataFrame with Bonus:")
print(df)

print("\n")


# Updating Values

df.loc[0, "Salary"] = 55000

print("Updated Salary:")
print(df)

print("\n")


# Saving to CSV

df.to_csv("employees.csv", index=False)

print("CSV File Saved")