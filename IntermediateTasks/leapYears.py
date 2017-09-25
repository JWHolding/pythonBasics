#!/usr/bin/python

import sys
days = {0 : 'Sunday', 1 : 'Monday', 2 : 'Tuesday', 3 : 'Wednesday', 4 : 'Thursday', 5 : 'Friday', 6 : 'Saturday'}
while(1):
    d = int(input("Insert Day: "))
    m = int(input("Insert Month: "))
    y = int(input("Insert Year: "))

#split into d m y ???

    if y == 0000:
        print("Goodbye!")
        sys.exit(0)
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        print("The year", y, "is a leap year!")
        if m ==1 or m == 2:
            d -= 2
            m += 12
            z=(1+d+(m*2)+(3*(m+1)/5)+y+y/4-y/100+y/400) % 7
            print(days[z])
        else:
            z=(1+d+(m*2)+(3*(m+1)/5)+y+y/4-y/100+y/400) % 7
            print(days[z])
    else:
        print("The year", y, "is NOT a leap year!")
        if m == 1 or m == 2:
            d-=1
            z=(1+d+(m*2)+(3*(m+1)/5)+y+y/4-y/100+y/400) % 7
            print(days[z])
        else:
            z=(1+d+(m*2)+(3*(m+1)/5)+y+y/4-y/100+y/400) % 7
            print(days[z])
