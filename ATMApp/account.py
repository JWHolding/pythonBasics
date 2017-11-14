"""Accounts class."""


class Account:
    """A class to hold Bank accounts."""

    numCreated = 0

    def __init__(self, initial, fname, pin):
        """Account Constructor."""
        self.__balance = initial
        self.__name = fname
        self.__pin = pin
        Account.numCreated += 1

    def deposit(self, amt):
        """Deposit Method for Account."""
        self.__balance = self.__balance + amt

    def withdraw(self, amt):
        """Withdraw method for Account."""
        self.__balance = self.__balance - amt

    def getBalance(self):
        """Balance getter for Account."""
        return self.__balance

    def getName(self):
        """Name getter for Account."""
        return self.__name

    def checkPin(self, upin):
        """Method for checking if user inputted string matches stored pin."""
        return bool(upin == self.__pin)
