"""Funtions for the ATM App."""


def displayMenu():
    """Print out ATM Menu."""
    print("Hello World")


def clearScreen():
    """Clear the screen. OS detection included."""
    import os
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
