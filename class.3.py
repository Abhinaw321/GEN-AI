class Demo:
    def msg(self):
        print("bye")
    @classmethod
    def msg1(cls):
        print("hello")
    @staticmethod
    def disp():
        print("hi")
d=Demo()
#we can access insrtance method using object
d.msg()
# we can classmethod bu using object refernce as well as class name
Demo.msg1()
d.msg1()
#we can access staticmethod using class name 
Demo.disp()