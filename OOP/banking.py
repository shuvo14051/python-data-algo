from abc import  abstractmethod, ABCMeta
from random import  randint

"""
from 9:25
"""
class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self):
        return 0
    @abstractmethod
    def authenticate(self):
        return 0
    @abstractmethod
    def withdraw(self):
        return 0
    @abstractmethod
    def deposit(self):
        return 0
    @abstractmethod
    def displayBalance(self):
        return 0


class SavingsAccount:

    def __init__(self):
        self.savingsAccount = {}

    def createAccount(self, name, initialDeposit):
        self.accountNumber = randint(10000,999999)
        self.savingsAccount [self.accountNumber] = [name, initialDeposit]

    def authenticate(self, name, accountNumber):
        if accountNumber in self.savingsAccount.keys():
            if self.savingsAccount[accountNumber][0] == name:
                print("Authentication succesfull")
                self.accountNumber = accountNumber
                return True
            else:
                print("Authentication failed")
                return False
        else:
            print("Authentication failed")
            return False

    def withdraw(self, withdrawalAmount):
        pass

    def deposit(self, depositAmount):
        pass

    def displayBalance(self):
        pass