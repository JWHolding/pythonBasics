import sys

while (1==1):
    num1 = input("Please enter first num:")
    if num1 == "0000" :
        sys.exit(0)
    num2 = input("Please enter second num:")
    result = int(num1) + int(num2)
    print("The Result is:", result)
