# DATA STRUCTURES
# LISTS
# is a collection is a collection of more than one variable
 # python list
students = ["james","stephie","john","kevin","meshack","kiprop"]
print(students)
print(students[0].title())
# print(students[1].title())
# print(students[2].title())
# print(students[3].title())
personal = []
personal = ["kevin sambuli", "nairobi", 24 , 20000 ,"vihiga"]
#len is used to count the number of varaibles in the list
print(len(personal))
print(type(personal))

students = ["james","stephie","john","kevin","meshack","kiprop"]
print(len(students))
new_student =["andrew"]
all_students = students + new_student
print(all_students)

# appends is used to mean add to
all_students.append("linda")
print(all_students)

# clear
# all_students.clear()
# print(all_students)

# count
a = all_students.count("linda")
print(a)

# index
# it finds position
pos = all_students.index("linda")
print(pos)
print(all_students[3] , all_students[4])
print(all_students[4])

# message = "hello, hope you had a good day"

# print(students[4].title())
# print(students[5].title())

