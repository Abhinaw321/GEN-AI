class Customer:
     bname = "HDFC Bank Mohali"
     def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
     def deposit(self,amt):
        self.balance = self.balance+amt
        print("after deposit Balance is:",self.balance)
        
     def withdraw(self,amt):
        if self.balance<amt:
            print("insufficient Balance")
        else:
             self.balance = self.balance-amt
        print("after withdraw balance is:",self.balance)
name=input("enter customer name:")
c=Customer(name)   
print("welcome to",Customer.bname, "Mr.",name)

while True:
    print("d Deposit")
    print("w Withdraw")
    print("e Exit")
ch=input("enter your choice:")
if ch=='d':
    amt=int(input("enter amount to deposit:"))
    c.deposit(amt)
    print("after deposit balance is:",c.balance)
    