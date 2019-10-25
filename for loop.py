# a for loop loops over a given range the i in the
# below represents each individual member of that range
# in rangen the las value is excluded
for i in range(100):
    print(i)

for num in range (5,10):
    print(num)

for num in range (5,10,2):
    print(num)

house = {"utensils": ["spoon","plate","cup","fork"], "clothes":["jacket"," jumper","sweater","trouser"]}
for each in house:
    print(house[each])

students = ["Ali","Kassim","Andrew","Eugene"]
for every in students:
    every += " Kamau"
    print(every)

subjects =[23,45,67,89,56]
total = 0
# for each in subjects:
#     total += each
#     print(total)

#1. write a program that prints your name 100 times using while and for loop
# while loop
a = 0
while a < 100:
    print("Kevin Sambuli")
    a +=1

# for loop
a = 0
for a in range(100):
# 2.write a program that outputs 100 lines numbered 1-100 each with your name on it
# for loop
a=0
for a in range(1,101):
    print("{} Kevin Sambuli".format(i))

# while loop
number = 100
i = 1
while i <= 100:
    print("{} Kevin Sambuli".format(i))
    i +=1

# 3. write a program that uses a for loop prints the numbers 8,11,14,17,20.....86,89
# for loop
for num in range (8,90,3):
    print(num)

# while loop
a = 8
while(8 <= a < 90):
    print(a)
    a+=3
# 4.write a program that prints the first 20 numbers and their squares and their cubes
# use both a for loop and a while loop
# 1...1....1
# 2...4....8
# while loop
a=0
for a in range (1,20):
    a +=1
    print(a,a**2,a**3)
    a +=1

for b in range(1,21):
    sq = b**2
    cb = b**3
    print("{}.{}.{}".format(b,sq,cb))

