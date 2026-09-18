class User:
    def __init__(self,name,password):
        self.name = name
        self.password = password
    def login(self):
        if self.name=="Techlive" and password==123:
            print("valid one")
        else:
            print("Invalid User")
name = input("enter name:")
password = int(input("enter a password:"))
u= User(name,password)
u.login()