from abc import ABC, abstractmethod

class Test1(ABC):
    @abstractmethod
    def n1(self):
        pass
class Test2(ABC):
    @abstractmethod
    def n2(self):
        pass
class Test3(Test1, Test2):
    def n1(self):
        print("This is n1")
    def n2(self):
        print("This is n2")
obj = Test3()
obj.n1()
obj.n2()