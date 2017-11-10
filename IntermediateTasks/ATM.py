"""An example ATM application.

By Jacob JWHolding
10.11.17
"""

import os
from ATMFunction import displayMenu

ID = int(input("Please Insert your ID: "))

if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')
displayMenu()
