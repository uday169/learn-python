# Operator Overloading


class Student:
    def __init__(self, a, b):
        self.a = a
        self.b = b

        # adding two objects

    def __add__(self, other):
        r1 = self.a + other.a
        r2 = self.b + other.b
        r3 = Student(r1, r2)
        return r3

    def __gt__(self, other):


    def __str__(self):
        return '{} {} '.format(self.a , self.b)


ob1 = Student(1, 5)
ob2 = Student(2, 6)

print(ob1 + ob2)