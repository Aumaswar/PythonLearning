a = 'Aum Aswar'
b = "\nAum Aswar"
c = '''\nAum 
Aswar'''
print(a,b,c)
# a = 'My name'
# print(a)

# String slicing
FirstName = a[0:3]

print(FirstName)

LastName = a[4:9]
print(LastName)

NameFirst = a[-9:-6]
print(NameFirst)

# To skip a value

SkipValue = a[:9:3]
print(SkipValue)

# Length of a string

Len = len(a)
print(Len)

# String Functions

Aswar = a.endswith('Aswar') 
print(Aswar)

Aum = a.startswith('Aum')
print(Aum)

Caps = (a.capitalize())
print(Caps)

Strip = a.strip()

print(Strip)

Split = a.split()

print(Split)

Replace = a.replace('Aswar','Aswarr')
print(Replace)

Find = a.find('Aum')

print(Find)

AllUpperCase = a.upper()

print(AllUpperCase)