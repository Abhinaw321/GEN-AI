class Student:
    college = "CGC University"     # Class variable

    def __init__(self, name, age):
        self.name = name            # Instance variable
        self.age = age              # Instance variable
    def show(self):
        course = "B.Tech CSE"       # Local variable
        print(self.name)
        print(self.age)
        print(Student.college)
        print(course)
s1 = Student("Abhinaw", 20)
s2 = Student("Rahul", 21)
s1.show()
s2.show()