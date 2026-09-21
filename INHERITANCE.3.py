class A:
    def show_A(self):
        print("This is class A")
class B(A):
    def show_B(self):
        print("This is class B")
class C(A):
    def show_C(self):
        print("This is class C")
obj1 = B()
obj1.show_A()
obj1.show_B()
obj2 = C()
obj2.show_A()
obj2.show_C()