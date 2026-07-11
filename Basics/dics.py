# Dictionary Practice File

# Creating a dictionary

student = {
    "name": "Aum",
    "age": 20,
    "course": "CSE"
}

print(student)

print("\n")


# Accessing values

print(student["name"])
print(student.get("age"))

print("\n")


# Adding new values

student["college"] = "Parul University"
student["city"] = "Vadodara"

print(student)

print("\n")


# Updating values

student["age"] = 21

print(student)

print("\n")


# Removing values

student.pop("city")

print(student)

print("\n")


# Dictionary length

print(len(student))

print("\n")


# Looping through dictionary

for key in student:
    print(key, ":", student[key])

print("\n")


# Using items()

for key, value in student.items():
    print(key, value)

print("\n")


# Using keys()

for key in student.keys():
    print(key)

print("\n")


# Using values()

for value in student.values():
    print(value)

print("\n")


# Copying dictionary

student_copy = student.copy()

print(student_copy)

print("\n")


# Nested dictionary

students = {
    "student1": {
        "name": "Aum",
        "marks": 90
    },

    "student2": {
        "name": "Raj",
        "marks": 80
    }
}

print(students)

print(students["student1"]["name"])

print("\n")


# Dictionary comprehension

squares = {x: x * x for x in range(1, 6)}

print(squares)

print("\n")


# Frequency counter

numbers = [1, 2, 2, 3, 1, 4, 2]

frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print(frequency)

print("\n")


# Shopping cart example

cart = {
    "Milk": 30,
    "Bread": 40,
    "Paneer": 120
}

total = 0

for item, price in cart.items():
    print(item, "=", price)
    total += price

print("Total =", total)

print("\n")


# User input dictionary

person = {}

name = input("Enter your name: ")
age = int(input("Enter your age: "))

person["name"] = name
person["age"] = age

print(person)

print("\n")


# Using update()

person.update({
    "city": "Vadodara",
    "course": "Python"
})

print(person)

print("\n")


# Using clear()

temp = {
    "a": 1,
    "b": 2
}

temp.clear()

print(temp)