import pandas as pd


# Employee Dataset

data = {
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Name": ["Aum", "Raj", "Priya", "Neha", "Karan", "Simran"],
    "Department": ["IT", "HR", "IT", "Finance", "HR", "IT"],
    "Age": [20, 21, 22, 19, 23, 24],
    "Salary": [50000, 30000, 70000, 25000, 45000, 80000],
    "Experience": [1, 2, 3, 1, 4, 5]
}

df = pd.DataFrame(data)

print("Employee Data:")
print(df)

print("\n")


# Display top rows

print("First 3 Rows:")
print(df.head(3))

print("\n")


# Display bottom rows

print("Last 2 Rows:")
print(df.tail(2))

print("\n")


# Random sample

print("Random Sample:")
print(df.sample(2))

print("\n")


# DataFrame summary

print("DataFrame Info:")
print(df.info())

print("\n")


# Statistical summary

print("Statistics:")
print(df.describe())

print("\n")


# Selecting columns

print("Names:")
print(df["Name"])

print("\n")


# Multiple columns

print("Name and Salary:")
print(df[["Name", "Salary"]])

print("\n")


# Filtering by condition

print("Employees with salary above 50000:")
print(df[df["Salary"] > 50000])

print("\n")


# Multiple conditions

print("IT Employees earning above 60000:")
print(df[(df["Department"] == "IT") & (df["Salary"] > 60000)])

print("\n")


# isin()

print("Employees from IT and HR:")
print(df[df["Department"].isin(["IT", "HR"])])

print("\n")


# Sorting values

print("Sorted by Experience:")
print(df.sort_values(by="Experience"))

print("\n")


# Sorting descending

print("Highest Salary First:")
print(df.sort_values(by="Salary", ascending=False))

print("\n")


# Creating new columns

df["Bonus"] = df["Salary"] * 0.10
df["Total Salary"] = df["Salary"] + df["Bonus"]

print("After Adding Columns:")
print(df)

print("\n")


# Using apply()

df["Salary Category"] = df["Salary"].apply(
    lambda x: "High" if x > 50000 else "Low"
)

print("Salary Category:")
print(df)

print("\n")


# Groupby operations

print("Average Salary by Department:")
print(df.groupby("Department")["Salary"].mean())

print("\n")


print("Maximum Salary by Department:")
print(df.groupby("Department")["Salary"].max())

print("\n")


# Counting department employees

print("Department Counts:")
print(df["Department"].value_counts())

print("\n")


# Indexing

df.set_index("Employee_ID", inplace=True)

print("After Setting Index:")
print(df)

print("\n")


# Reset index

df.reset_index(inplace=True)

print("After Resetting Index:")
print(df)

print("\n")


# Null values

df.loc[1, "Salary"] = None

print("Added Missing Value:")
print(df)

print("\n")


# Detect missing values

print("Missing Values:")
print(df.isnull())

print("\n")


# Fill missing values

df["Salary"].fillna(df["Salary"].mean(), inplace=True)

print("After Filling Missing Salary:")
print(df)

print("\n")


# Duplicate rows

duplicate_df = pd.concat([df, df])

print("Duplicate Data:")
print(duplicate_df)

print("\n")


# Remove duplicates

duplicate_df.drop_duplicates(inplace=True)

print("After Removing Duplicates:")
print(duplicate_df)

print("\n")


# Exporting files

duplicate_df.to_csv("employees_cleaned.csv", index=False)

print("CSV File Exported")

print("\n")


# Reading exported file

new_df = pd.read_csv("employees_cleaned.csv")

print("Reading Exported CSV:")
print(new_df)

print("\n")


# Correlation

print("Correlation Matrix:")
print(new_df.corr(numeric_only=True))

print("\n")


# Query method

print("Employees older than 21:")
print(new_df.query("Age > 21"))

print("\n")


# Final summary

print("Final Data Summary:")
print(new_df.describe())