taskList = [23 , "Jane", ["Lesson 23" , 560 , {"currency":"KES"}] , 987 , (76 , "John")]

# 1. Determine the type  of variable in taskList using an inbuilt function
print(type(taskList))

# 2. Print KES from taskList
print(taskList[2][2]["currency"])

# 3. Print 560
print(taskList[2][1])

# 4. Use a function to determine the length of taskList
print(len(taskList))

# 5. change 987 to 789 without using assignment or an inbuilt function
print(str(taskList[3])[::-1])


# 6. change the name john to jane
#N/A