
# String data types

# literal assignment
first = "Cristian"
last = "Danu"

# print()
# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))
# print()

# constructor function

# pizza = str("Pepperoni")
# print()
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))
# print()


# Concatenation
# fullname = first + " " + last
# print(fullname)
# fullname += "!"
# print(fullname)

# Casting a number to a string
# decade = str(1980)
# print(type(decade))
# print(decade)

# statement = "I like rock music from the " + decade + "s."
# print(statement)

# Multiple lines

multiline = """
Hey, how are you?                       
                                                
I was just checking in.
                          All good?
"""

print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                      "
multiline = "              " + multiline
print(len(multiline))

print()

print(len(multiline.strip())) #removes ALL white space
print(len(multiline.lstrip())) # removes space from the left side
print(len(multiline.rstrip())) # removes space from the right side

print()

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Tea".ljust(16, ".") + "$0.5".rjust(4))
print("Water".ljust(16, ".") + "$0.7".rjust(4))
print("Soda".ljust(16, ".") + "$0.3".rjust(4))
print("Popsi".ljust(16, ".") + "$2".rjust(4))
print("Coca-Cola".ljust(16, ".") + "$2".rjust(4))
print()

# string index values
print(first[1])
print(first[-1])
print(first[1:-1]) #the value we put at the end of the range will not be part of the output
print(first[1:]) # NOT providing the last value - leaving the space empty - will return all the characters until the end

# Some methods return boolean data
print(first.startswith("C"))
print(first.endswith("Z"))
print(first.endswith("N"))

print()

#Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))
print()


# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
print()

# float types
gpa = 3.28
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))
print()

# complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
print()

# built-in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))

import math

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))   # rounds UP to the nearest integer
print(math.floor(gpa))   # rounds doun to the nearest integer

# Casting a string to a number
zipcode = "10001"
zipcode_value = int(zipcode)

print(type(zipcode))
print(type(zipcode_value))


# Error if you attempt to cast incorrect data
# zipcode_value2 = int("New York")   # ValueError: invalid literal
