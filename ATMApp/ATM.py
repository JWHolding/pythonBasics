"""An example ATM application.

By Jacob JWHolding
10.11.17
"""

from ATMFunction import displayMenu, clearScreen, getAccount, delay


while True:
    clearScreen()
    ID = int(input("Please Insert your ID: "))
    acc = getAccount(ID)
    attempts = int(0)
    while attempts < 4:
        clearScreen()
        if acc.checkPin():
            attempts = 0
            while True:
                uin = str(displayMenu())
                if uin == "1":
                    print("Hello %s. Your Current Balance is: £%0.2f"
                          % (acc.getName(), float(acc.getBalance())))
                    delay(2)
                    clearScreen()
                elif uin == "2":
                    acc.withdraw()
                    delay(0.5)
                    clearScreen()
                elif uin == "3":
                    acc.deposit()
                    delay(0.5)
                    clearScreen()
                elif uin == "4":
                    acc.changePin()
                elif uin == "Q" or uin == "q":
                    print("Goodbye!")
                    delay(0.5)
                    attempts = 5
                    break
                else:
                    clearScreen()
                    print("Invalid option, try again.")
                    continue
        else:
            attempts = attempts + 1
    if attempts == 4:
        print("Too many incorrect attempts")
        input("press any key to continue...")
