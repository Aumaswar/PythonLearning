import pandas as pd


# Reading CSV File

df = pd.read_csv("employee_data.csv")

print("CSV Data:")
print(df)

print("\n")


# Shape of DataFrame

print("Shape:")
print(df.shape)

print("\n")


# Data types

print("Data Types:")
print(df.dtypes)

print("\n")


# Unique values

print("Unique Departments:")
print(df["Department"].unique())

print("\n")


# Number of unique values

print("Number of Unique Departments:")
print(df["Department"].nunique())

print("\n")


# Value counts

print("Department Counts:")
print(df["Department"].value_counts())

print("\n")


# Renaming columns

df.rename(columns={"Salary": "Monthly Salary"}, inplace=True)

print("Renamed Column:")
print(df)

print("\n")


# Adding a tax column

df["Tax"] = df["Monthly Salary"] * 0.05

print("Added Tax Column:")
print(df)

print("\n")


# Filtering employees

high_salary = df[df["Monthly Salary"] > 40000]

print("Employees with High Salary:")
print(high_salary)

print("\n")


# Using loc

print("Using loc:")
print(df.loc[:, ["Name", "Monthly Salary"]])

print("\n")


# Using iloc

print("Using iloc:")
print(df.iloc[0:3, 0:2])

print("\n")


# Sorting by age

print("Sorted by Age:")
print(df.sort_values(by="Age"))

print("\n")


# Groupby example

print("Average Salary by Department:")
print(df.groupby("Department")["Monthly Salary"].mean())

print("\n")


# Finding highest paid employee

highest_salary = df[df["Monthly Salary"] == df["Monthly Salary"].max()]

print("Highest Paid Employee:")
print(highest_salary)

print("\n")


# Handling missing values

df.loc[2, "Age"] = None

print("Missing Value Added:")
print(df)

print("\n")


# Checking missing values

print("Null Values:")
print(df.isnull())

print("\n")


# Filling missing values

df["Age"].fillna(df["Age"].mean(), inplace=True)

print("After Filling Missing Values:")
print(df)

print("\n")


# Dropping duplicates

df = pd.concat([df, df])

print("Duplicate Rows Added:")
print(df)

print("\n")


df.drop_duplicates(inplace=True)

print("After Removing Duplicates:")
print(df)

print("\n")


# Creating another DataFrame

bonus_data = {
    "Name": ["Aum", "Raj", "Priya", "Neha", "Karan"],
    "Bonus": [5000, 2000, 7000, 1500, 4000]
}

bonus_df = pd.DataFrame(bonus_data)

print("Bonus DataFrame:")
print(bonus_df)

print("\n")


# Merging DataFrames

merged_df = pd.merge(df, bonus_df, on="Name")

print("Merged DataFrame:")
print(merged_df)

print("\n")


# Saving final data

merged_df.to_csv("final_employee_data.csv", index=False)

print("Final CSV Saved")