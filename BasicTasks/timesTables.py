"""Script for doing times tables.

Insert the incrementer and max value.
"""

mult = int(input("Which times tables do you want?:"))
maxi = int(input("How many increments do you want?:"))

for i in range(1, maxi+1):
    print(i, "x", mult, "=", mult*i)
