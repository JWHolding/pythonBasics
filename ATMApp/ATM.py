"""An example ATM application.

By Jacob JWHolding
10.11.17
"""

import getpass
import time
from account import Account
from ATMFunction import displayMenu, clearScreen

acc1 = Account(100, "Jacob", "0000")
acc2 = Account(100, "Gareth", "0000")
acc3 = Account(100, "Elliot", "0000")
acc4 = Account(100, "Tadas", "0000")
acc5 = Account(100, "Shafeeq", "0000")

while True:
    clearScreen()
    ID = int(input("Please Insert your ID: "))
    attempts = int(0)
    while attempts < 4:
        clearScreen()
        pin = getpass.getpass()
        clearScreen()
        if acc1.checkPin(pin):
            attempts = 0
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
                    print("Goodbye!")
                    time.sleep(0.5)
                    attempts = 4
                    break
                else:
                    clearScreen()
                    print("Invalid option, try again.")
                    continue
        else:
            attempts = attempts + 1
    if attempts < 4:
        print("Too many incorrect attempts")
        input("press any key to continue...")
