# If you create object of subclass it will first
# try to find init of subclass if it not found then it will call init of super class

# Here, It find the init of subclass because the init available in subclass


class A:  # class A

    def __init__(self):
        print("init of class A ")

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B(A):  # class B

    def __init__(self):
        print("init of class B")

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


a1 = B()  # Object a1

a1.feature3()
a1.feature4()
