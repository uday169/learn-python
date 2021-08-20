# example of Inner Class

# Outer Class
class Student:

    def __init__(self,name,roll_no):
         self.name = name
         self.roll_no = roll_no
         self.lap = self.Laptop()

    def show(self):
         print(self.name, self.roll_no)
         self.lap.show()

    # Inner class
    class Laptop:

        def __init__(self):
             self.brand = 'Dell'
             self.cpu = 'i7'
             self.ram = '8gb'

        def show(self):
             print(self.brand, self.cpu, self.ram)


s1 = Student('Uday',12)
s2 = Student('pratap', 23)

s1.show()