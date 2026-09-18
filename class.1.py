class Test:
    def __init__(self):
        #instance variable
        self.a=10
        self.b=20
t=Test()
print(t.a)
print(t.__dict__) #is a keyword which is used to access class altr

class Test:
    def __init__(self):
        #instance variable
        self.a=10
        self.b=20
        #instance method can access instance variable
    def add(self):
            print(self.a+self.b)
t=Test()
t.add()

class User:
    def __init__(self,name,password):
        self.name= name
        self.password= password
    def login(self):
        if self.name="Techlive" and password=123:
            print("valid one")
        else:
            print("Invalid User")
name = input("enter name:")
u= user(new.passwords)
u.login()