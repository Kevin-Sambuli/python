# WHILE LOOP
# a while loop repeats an execution of its indented block until a condition is false
# a = 0
# while a < 100:
#     print("Kevin Sambuli")
#     a += 1
#     print(a)


savedPin = "8456"
tries = 3
entries = 0
current = input("Enter pin")
entries += 1
while current != savedPin and entries <tries:
    current = input("Enter pin")
    entries += 1

if current != savedPin:
    print("Access denied")
else:
    print("Access granted")