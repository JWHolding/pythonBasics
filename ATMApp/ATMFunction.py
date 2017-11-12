"""Funtions for the ATM App."""


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
