"""Script for doing times tables.

Calculate times tables between inputted number and 10 up to the increments
"""

mult = int(input("Which times tables do you want to start with?:"))
maxi = int(input("How many increments do you want?:"))

for x in range(mult, 10):
    print("Time Table of:", x)
    for i in range(1, maxi+1):
        print(i, "x", x, "=", x*i)
