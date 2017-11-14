"""Accounts class."""
import hashlib


class Account:
    """A class to hold Bank accounts."""

    numCreated = 0

    def __init__(self, initial, fname, pin):
        """Account Constructor."""
        self.__balance = initial
        self.__name = fname
        self.__pin = hashlib.sha512(pin.encode()).hexdigest()
        self.__id = Account.numCreated + 1
        Account.numCreated += 1

    def deposit(self):
        """Deposit Method for Account."""
        amt = int(input("How much would you like to Deposit: "))
        self.__balance = self.__balance + amt

    def withdraw(self):
        """Withdraw method for Account."""
        amt = int(input("How much would you like to Withdraw: "))
        self.__balance = self.__balance - amt

    def getBalance(self):
        """Balance getter for Account."""
        return self.__balance

    def getName(self):
        """Name getter for Account."""
        return self.__name

    def checkPin(self, upin):
        """Method for checking if user inputted string matches stored pin."""
        return bool(hashlib.sha512(upin.encode()).hexdigest() == self.__pin)

    def changePin(self):
        """Method that allows user to change their pin."""
        pin = input("insert new pin: ")
        self.__pin = hashlib.sha512(pin.encode()).hexdigest()
