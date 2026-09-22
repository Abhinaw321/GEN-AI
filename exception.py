from abc import ABC, abstractmethod
class InsufficientBalanceError(Exception):
    pass

class BankAccount(ABC):

    def __init__(self, name, account_no, balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance

    def deposit(self, amt):
        if amt < 0:
            print("Please enter a valid amount")
        else:
            self.balance = self.balance + amt
            print("After Deposit Balance is:", self.balance)

    @abstractmethod
    def withdraw(self, amt):
        pass

    def show_details(self):
        print("Customer Name:", self.name)
        print("Your Balance is:", self.balance)
        print("Your Account Number is:", self.account_no)

class Customer(BankAccount):

    def withdraw(self, amt):
        if amt > self.balance:
            raise InsufficientBalanceError("Insufficient Balance")
        else:
            self.balance = self.balance - amt
            print("After Withdraw Balance is:", self.balance)

try:
    c = Customer("Abhinaw", 12345, 5000)

    c.show_details()

    c.deposit(2000)

    c.withdraw(3000)

    c.show_details()

except InsufficientBalanceError as e:
    print("Error:", e)