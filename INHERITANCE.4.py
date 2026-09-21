class A:
    def show_A(self):
        print("This is class A")


class B:
    def show_B(self):
        print("This is class B")


class C(A, B):
    def show_C(self):
        print("This is class C")


obj = C()

obj.show_A()
obj.show_B()
obj.show_C()