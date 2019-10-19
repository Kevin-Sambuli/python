"""VARIABLES."""
# variables are temporary memory storage locations for reference
#this memory is normally primary memory(RAM)
x = 35
y = 25
z = x + y
print(z)

"""Data types"""

# integer
# integer is a datatype that holds whole numbers
b=100
c=1000
number_of_students = 45
math = 75
type_of_math = type(math)
print(type_of_math)


# float
opening_balance = 100.0
print(type(opening_balance))

# boolean
# used when we want to execute some conditions
g = True
h = False

# strings
# any character is a string
name = 'Kevin Sambuli Amuhaya'
national_id = "33168609"

print(type(name))
national_id = int(national_id) # type casting-converting from one data type to another data type
print(national_id)


# contactinating
firstName = "Kevin"
last_name = " Sambuli"
firstName = "Amuhaya"
full_name = firstName + last_name
print(full_name)
print(firstName.upper(),last_name)
print("54 + 36 =", 54 + 36)


firstName = "kevin"
last_name = " sambuli"
firstName = "amuhaya"
full_name = firstName + last_name
print(full_name)

#printing the first name us capital capitalisation
print(firstName.upper(),last_name)
print("54 + 36 =", 54 + 36)
print(firstName.capitalize())
print(full_name.title())
print(firstName.count("a"))
print(firstName.split("a"))

#Slice strings [] indexing 0 position 1
print(firstName[0:])
print(firstName[1:])
print(firstName[2:])
print(firstName[3:])
print(firstName[-3:])
print(firstName[2:0])
print(firstName[0:0])

#Length
len(firstName)

#DATA STRUCTURES