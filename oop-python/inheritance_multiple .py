# Multiple Inheritance


class A: # class A

    def feature1(self):
        print("Feature 1 working")

    def feature2(self):
        print("Feature 2 working")


class B: # class B

    def feature3(self):
        print("Feature 3 working")

    def feature4(self):
        print("Feature 4 working")


class C(A,B): # Class C inherit all the features of class A and Class B
    def feature5(self):
        print("Feature 5 working")


a1 = A() # Object a1

a1.feature1()
a1.feature2()

b1 = B() # Object b1
b1.feature3()
b1.feature4()

c1 = C() # Object c1

c1.feature1() # class C inherit the feature of class A
c1.feature2() # class C inherit the feature of class A
c1.feature3() # class C inherit the feature of class B
c1.feature4() # class C inherit the feature of class B
c1.feature5()
