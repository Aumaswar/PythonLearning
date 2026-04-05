# User name followed by good afternoon message

name = input("Enter your name: ")
date = ("28-03-2026")
print(f"Good afternoon {name}")

# Replacing chars

# Given template
letter = '''
Dear <|Name|>
You are selected!
<|Date|>
'''
NewLetter = letter.replace("<|Name|>" , name)
NewLetter = NewLetter.replace("<|Date|>" , date)

print(NewLetter)

# Check for double spaces
a = "  Aum aswar"
DoubleSpace = a.find("  ")

if(DoubleSpace != -1):
    a = a.replace("  ", " ")
    print(a)
else:
    print("No double space found")