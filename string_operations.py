# concatenating strings
firstName = "Kevin"
last_name = " Sambuli"
firstName = " Amuhaya"
full_name = firstName + last_name
print(full_name)

# concatenating using format
full_name = "{}{}".format(firstName,last_name)
print(full_name)

#string operations
print(firstName.upper(),last_name)# a comma creates a space between  two words or strings
print("54 + 36 =", 54 + 36)


firstName = "kevin"
last_name = " sambuli"
firstName = "amuhaya"



#printing the first name us capital capitalisation
full_name = "{}{}".format(firstName,last_name)
email = "dear {} regards {}"
print(full_name.capitalize())
print(full_name.title())

#count
print(full_name.lower().count("a")) # python is case sensitive
print(firstName.split("a"))

# string slicing
# [] indexing 0 position left of the colon signifies the starting element then
# right signifies the ending position but that position is excluded
print(firstName[0])
print(firstName[0:])
print(firstName[1:])
print(firstName[2:])
print(firstName[3:])
print(firstName[-3:])
print(firstName[2:0])
print(firstName[1:-2])
print(firstName[0:0])
# it inverts the name to start from the end
print(firstName[::-1])

#Length
len(firstName)
