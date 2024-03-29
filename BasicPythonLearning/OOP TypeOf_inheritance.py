#MultiLEVEL iNHERITANCE
'''
class A:
    def display1(self):
        print("I am inside A class")

class B(A):
    def display2(self):
        print("I am inside B class")

class C(B):
    def display3(self):
        print("I am inside C class")

ob1 = C()
ob1.display1()
ob1.display2()
ob1.display3()
'''
#Multiple inheritance

class A:
    def display(self):
        print("I am inside A class")
class B:
    def display(self):
        print("I am inside B class")
class C(A,B):
    def display(self):
        print("I am inside C class")

ob1 = C()
ob1.display()
