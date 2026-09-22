from abc import ABC,abstractmethod
class Demo(ABC):
    @abstractmethod #predefined like save(), fetchall(), findbyID
    def show():
        pass 
class Test(Demo):
    def show(self):
        print("Hello")
t = Test()
t.show()