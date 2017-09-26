import sys

while 1:
    num = int(input("Please insert a whole number. (0000 to exit):"))
    if num % 2:
        print(num, "Is Odd")
    elif num == 0000:
        sys.exit()
    else:
        print(num, "Is Even")
