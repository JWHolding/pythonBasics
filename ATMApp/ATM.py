"""An example ATM application.

By Jacob JWHolding
10.11.17
"""

from ATMFunction import displayMenu, clearScreen, getAccount, delay

acc = None


while True:
    clearScreen()
    ID = int(input("Please Insert your ID: "))
    acc = getAccount(ID)
    menu = {"1": acc.getBalance,
            "2": acc.withdraw,
            "3": acc.deposit,
            "4": acc.changePin}
    attempts = int(0)
    while attempts < 4:
        clearScreen()
        if acc.checkPin():
            attempts = 0
            while True:
                uin = str(displayMenu())
                if uin.isdigit() and int(uin) <= len(menu):
                    run = menu[uin]
                    run()
                elif uin.upper() == "Q":
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
