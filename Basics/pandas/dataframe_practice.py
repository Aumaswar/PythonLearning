import pandas as pd


# Creating DataFrame

data = {
    "Name": ["Aum", "Raj", "Priya", "Neha", "Karan"],
    "Age": [20, 21, 22, 19, 23],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 30000, 70000, 25000, 45000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)

print("\n")


# Selecting rows using loc

print("Row with index 2:")
print(df.loc[2])

print("\n")


# Selecting multiple rows

print("Rows 1 to 3:")
print(df.loc[1:3])

print("\n")


# Selecting specific columns

print("Name and Salary:")
print(df[["Name", "Salary"]])

print("\n")


# Filtering rows

print("Employees with salary above 40000:")
print(df[df["Salary"] > 40000])

print("\n")


# Multiple conditions

print("IT Department Employees:")
print(df[df["Department"] == "IT"])

print("\n")


# Multiple filters together

print("HR Employees with salary above 35000:")
print(df[(df["Department"] == "HR") & (df["Salary"] > 35000)])

print("\n")


# Sorting values

print("Sorted by Salary:")
print(df.sort_values(by="Salary"))

print("\n")


# Sorting descending

print("Salary High to Low:")
print(df.sort_values(by="Salary", ascending=False))

print("\n")


# Adding a new column

df["Bonus"] = df["Salary"] * 0.15

print("Added Bonus Column:")
print(df)

print("\n")


# Updating specific value

df.loc[0, "Salary"] = 60000

print("Updated Salary:")
print(df)

print("\n")


# Deleting a column

df.drop("Bonus", axis=1, inplace=True)

print("After Removing Bonus Column:")
print(df)

print("\n")


# Checking null values

print("Null Values:")
print(df.isnull())

print("\n")


# Basic statistics

print("Average Salary:")
print(df["Salary"].mean())

print("\n")

print("Highest Salary:")
print(df["Salary"].max())

print("\n")

print("Lowest Salary:")
print(df["Salary"].min())

print("\n")


# Grouping data

print("Average Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

print("\n")


# Saving to CSV

df.to_csv("employee_data.csv", index=False)

print("CSV File Saved")