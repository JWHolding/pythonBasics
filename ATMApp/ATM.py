"""An example ATM application.

By Jacob JWHolding
10.11.17
"""

from ATMFunction import displayMenu, clearScreen
from account import Account

acc1 = Account(100, "Jacob")
acc2 = Account(100, "Gareth")
acc3 = Account(100, "Elliot")
acc4 = Account(100, "Tadas")

ID = int(input("Please Insert your ID: "))
clearScreen()
displayMenu()

print("Hello %s. Your Current Balance is: %0.2f" % (acc1.getName(),
                                                    float(acc1.getBalance())))
