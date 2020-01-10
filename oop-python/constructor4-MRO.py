
# Here, whenever have multiple inheritance ,
# then child class inherit the left side class first....
# Method Resolution Order(M.R.O)
# To represent super class we use super method


class A:  # class A

    def __init__(self):
        print("init of class A ")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B:  # class B

    def __init__(self):
        super().__init__()
        print("init of class B")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(A,B):
    def __init__(self):
        super().__init__() # super method
        print("init of class C")


a1 = C()  # Object a1

a1.feature3()
a1.feature4()
