
# Here, If you have call 'super' then
# it will first call init of super class then call init of subclass


class A:  # class A

    def __init__(self):
        print("init of class A ")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):  # class B

    def __init__(self):
        super().__init__()
        print("init of class B")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


a1 = B()  # Object a1

a1.feature3()
a1.feature4()
