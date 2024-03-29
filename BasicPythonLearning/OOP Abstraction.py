from  abc import ABC,abstractmethod  #input Abstrac method

class Shape(ABC):   #declear abstrac class by ABC(Abstrac BAse CLass)
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    @abstractmethod      #d3clear Abstrac Method
    def area(self):
        pass

class Triangle(Shape):
    def area(self):
        area = 0.5 * self.dim1 * self.dim2
        print("Ares of Triangle : ", area)


class Rectangle(Shape):
    def area(self):
        area =  self.dim1 * self.dim2
        print("Ares of Rectangle : ", area)


t1 = Triangle(20,30)
t1.area()

r1 = Rectangle(20,30)
r1.area()