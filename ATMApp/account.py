"""Accounts class."""


class Account:
    """A class to hold Bank accounts."""

    numCreated = 0

    def __init__(self, initial, fname, cpin):
        """Account Constructor."""
        self.__balance = initial
        self.__name = fname
        self.__pin = cpin
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

    def getPin(self):
        """Return the pin for Account."""
        return self.__pin
