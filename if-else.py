if True:
    print("True")

marks = input("What is your KCPE marks: ")
marks = eval(marks)

if marks >= 350 and marks <= 500:
    print("congratulations you are admitted")
else:
    print("Sorry, Try again")



marks = input("What is your KCPE marks: ")
marks = eval(marks)
if marks < 0 or marks>500:
    print("Your marks are unrealistic")
else:
    if marks >= 350 and marks <= 500:
        print("congratulations you are admitted")
    else:
        print("Sorry, Try again")


#  read on if-elif-else conditions

avg_marks = int(input("Average marks:"))
if avg_marks > 70 and avg_marks <= 100:
    print("A")
elif avg_marks >= 60:
    print("B")
elif avg_marks >= 50:
    print("C")
elif avg_marks >= 40:
    print("D")
else:
    print("F")

# leap year
N = 4
name = input("Year of birth")
name = eval("name")
year = input("Enter the year")
year = eval(year)
if year <=0:
    print("Invalid")
else:
    if year%N=0:
        print("leap year")
    else:
    print("Not a leap year")
