# # FUNCTIONS
# # def functionName(p):
# #     "statement"
#
# # example one
# def hello():
#     print("Hello world")
#     print("Sambuli")
# hello()
#
# # example two
# def addTwoNumbers(a, b):
#     summ=a +b
#     print(summ)
#
# addTwoNumbers(10, 10)
# addTwoNumbers(20, 30)
# addTwoNumbers(40, 90)
# addTwoNumbers("Kevin"," Sambuli")
#
# # example three
# def subtractTwoNumbers(a, b):
#     subtract=a -b
#     print(subtract)
#
# subtractTwoNumbers(10, 10)
# subtractTwoNumbers(20, 30)
# subtractTwoNumbers(150, 90)
#
# # example four
# def multiplyTwoNumbers(a, b):
#     multiply=a *b
#     print(multiply)
#
# multiplyTwoNumbers(10, 10)
# multiplyTwoNumbers(20, 30)
# multiplyTwoNumbers(150, 90)

# example five if statement
def int(a):
    if a > 100:
        print("True")
    else:
        print("False")

int(100)

#  example six if a number is divisible by 2
def divBy2(N):
    if N % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

divBy2(20)

# kevin
def caps(name):
    print(name.title())
caps("kevin")

def upperCaseFirstName(name):
    index1 =name[0].upper()
    fullname =index1 + name[1:]
    print(fullname)

#  replacing morning with afternoon
def name(aName):
    print(aName.replace("Morning", "Afternoon"))

name("Good Morning")


def add2No(a,b):
    return a +b
# use return if you want to store the value in a new variable
x = add2No(10,10)
print(x)
# or
print(add2No(10,100))


def computeAndPrint(x, y):
    val = x**4/4.0 - x**3/3.0 - 3 * x * x + y
    print("You called computeAndPrint("+str(x)+","+str(y)+")")
    return val
    print(computeAndPrint(6,5))
    
    

