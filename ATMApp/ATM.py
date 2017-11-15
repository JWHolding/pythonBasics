"""An example ATM application.

By Jacob JWHolding
10.11.17
"""

import getpass
from ATMFunction import displayMenu, clearScreen
from account import Account

acc1 = Account(100, "Jacob", 1234)
acc2 = Account(100, "Gareth", 123)
acc3 = Account(100, "Elliot", 123)
acc4 = Account(100, "Tadas", 123)

while True:
    clearScreen()
    name = str(input("Please Insert your Name: "))
    clearScreen()
    pin = getpass.getpass()
    clearScreen()
    count = int(0)
    while True:
        uin = str(displayMenu())
        if uin == "1":
            print("Hello %s. Your Current Balance is: %0.2f"
                  % (acc1.getName(), float(acc1.getBalance())))
            input("Press any key to continue...")
            clearScreen()
        elif uin == "2":
            acc1.withdraw(int(input("How much would you like to Withdraw: ")))
            input("Press any key to continue...")
            clearScreen()
        elif uin == "3":
            acc1.deposit(int(input("How much would you like to Deposit: ")))
            input("Press any key to continue...")
            clearScreen()
        elif uin == "Q" or uin == "q":
            break
        else:
            clearScreen()
            print("Invalid option, try again.")
            continue
