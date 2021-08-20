# Example of instance method , class method and static method
class Student:

    school = "THis is the school"

    # instance method
    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def avg(self):
        return (self.m1 + self.m2 + self.m3)/3

    # class method
    @classmethod
    def get_school(cls):
        return cls.school

    # static method
    @staticmethod
    def info():
        print("This is the Student class Static method ")


s1 = Student(50, 26, 34)
s2 = Student(62, 36, 49)

# print the values
print(s1.avg())
print(s2.avg())
print(Student.get_school())

Student.info()

