"""Funtions for the ATM App."""
from account import Account

accs = [Account(100, "Jacob", "0000"),
        Account(100, "Gareth", "0000"),
        Account(100, "Elliot", "0000"),
        Account(100, "Tadas", "0000"),
        Account(100, "Shafeeq", "0000")]


def displayMenu():
    """Print out ATM Menu."""
    print("Welcome To QA Bank")
    print("------------------------------")
    print("Press 1 to see Current Balance")
    print("Press 2 to withdraw Money")
    print("Press 3 to Deposit Money")
    print("q to quit")
    selection = str(input("Selection: "))
    return selection


def clearScreen():
    """Clear the screen. OS detection included."""
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def delay(amt):
    """Provide a short delay. Seconds."""
    import time
    time.sleep(amt)


def getAccount(uid):
    """Return the account object for user."""
    for i in range(0, len(accs)):
        if int(uid) == accs[i].getId():
            print(accs[i])
            return accs[i]
