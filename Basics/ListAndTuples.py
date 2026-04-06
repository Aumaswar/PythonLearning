# Lists

# Lisits can store any type of data
friends = ["Aum","Saman",700]

print(friends[0])

# LIST ARE MUTABLE UNLIKE STRINGS
friends[0] = "Goku"

print(friends[0])

# Can be sliced just as strings

print(friends[-3:-1])

# Add values at the end of the list

friends.append("Aum")

print(friends)

# Sorting the list

number = [3312,123,456,243,23445]

print(number)
number.sort()

# Revering the string
number.reverse()
print(number)

# Inserting a new value
number.insert(2,"Homelander")
print(number)

# Poping an element
print(number.pop(2))


# Removing an element
number.remove(3312)
print(number)


tup = (1,2,3,5,6,7,10)
print(tup.count(5))
print(tup.index(5))

print(min(tup))
print(max(tup))

print(sum(tup))