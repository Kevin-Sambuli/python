"""TASK 1:"""

""" practice question
We should create a function that ‘findsgrade’ by taking in marks of each subject as parameters
calculating total from the parameters(subjects) passed calculating the average from the total
using if statement to find grade what if I want to get total marks! and average?"""

# def findsGrade (math, eng , kisw ,chem, bio):
#     total_marks= (int(math) + int(eng) + int(kisw) + int(chem) + int(bio))
#     print("total_makrs =",total_marks)
#     avg_marks= (total_marks / 5)
#     print("avg_marks =", avg_marks)
#     if avg_marks > 75 and avg_marks <= 100:
#         print("grade =","A")
#     elif avg_marks >= 65:
#         print("grade =","B")
#     elif avg_marks >= 55:
#         print("grade =","C")
#     elif avg_marks >= 45:
#         print("grade =","D")
#     else:
#         print("grade =","F")
#
# # findsGrade(80,66,67,77,88)
#
"""practice question 2
# # Write a function called sum_digits that is given an integer num and returns the sum of the digits of num."""
# integer = input("Enter any two digit number:")
# def sum_integer(p):
#     digit_one = int(p[0])
#     digit_two = int(p[1])
#     print(digit_one + digit_two)
# sum_integer(integer)



"""practice two
Write a program which accepts a string as input to print "Yes" if the string is "yes", "YES" or "Yes", otherwise print "No"."""
# typed_input =input("enter the keyword 'yes':")
# def capitalise_y(a):
#     if a == "YES":
#         print("Yes")
#     elif a == "yes":
#         print("Yes")
#     elif a == "Yes":
#         print("Yes")
#     else:
#         print("No")
# capitalise_y(typed_input)
#
"""TASK
 Implement a function that takes as input three variables, and returns the largest of the three.Do this without
 using the Python max()function!The goal of this exercise is to think about some internal that Python normally
takes care of for us."""
# def largestNo(a,b,c):
#     if a > b and a > c:
#         largest = a
#         print("largest number is {} ".format(largest))
#     elif b > a and b > c:
#         largest = b
#         print("largest number is {} ".format(largest))
#     elif c > a and c > b:
#         largest = c
#         print("largest number is {} ".format(largest))
#
# largestNo(867,454,200)
# largestNo(180,4660,6784)
# largestNo(123,430,20)
# largestNo(180,98,20)



"""TASK 3:
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
makes a new list of only the first and last elements of the given list. For practice,
write this code inside a function"""
# def index():
#     a=[12,34,56,67,78,23,56,78,90]
#     print(a)
#     print([a[0] , a[-1]])
# index()


""" TASK 4:
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd number react differently when divided by 2?"""
# number = input("enter value:")
# number = int(number)
# def oddOrEven(a):
#     if a % 2 == 0:
#         print("its an even number")
#     else:
#         print("its an odd number")
# oddOrOdd(number)

"""Extras:
If the number is a multiple of 4, print out a different message."""



"""TASK 5"""
# # With a given tuple (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), write a program to print
# # the first half values in one line and the last half values in one line.
def arrange():
    a =(1, 2 , 3, 4, 5, 6, 7, 8, 9, 10,6,8)
    a =list(a)
    print(len(a))
    print(len(a)/2)
    print(a[0:5])
    print(a[5:10])
arrange()

"""example two"""
# def halves():
#     a = []
#     num = int(input("Enter contents of your tuple:"))
#     for i in range(0, num):
#         element = int(input())



""" Practice questions : PART C
Create a function that takes a name and returns a greeting"""
# def hello():
#     a = input("Enter your name:")
#     print("hello " + a + "!")
# hello()

""" Write a function that takes the base and height of a triangle and return its area."""
# def area(b , h):
#     area = (0.5 * b * h)
#     print("area =" ,area)
# area(3,4)

"""Create a function that finds the maximum range of a triangles third edge"""







"""Create a function that takes a list and returns the first element."""
def get_first_value():
    a = []
    num = int(input("Enter contents of your list: "))
    for i in range(0, num):
        element = int(input())
        a.append(element)
        b = list(i for i in a)
    print(b)

"""solution two"""
# def get_first_value():
#     a =(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
#     print(a[0])
# get_first_value()


"""You've got chickens (2 legs), cows (4 legs) and pigs (4 legs) on your farm.
Return the total number of legs on your farm. (CREATE A FUNCTION)"""
# def legs(ch,co,pi):
#     chicken = ch * 2
#     cow = co * 4
#     pig = pi * 4
#     total_legs = (chicken + cow + pig)
#     print("total number of legs are",total_legs)
# legs(2,4,5)

