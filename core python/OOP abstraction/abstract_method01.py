from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass
    def another_method(self):
        print("Another method of shape class")

class Rectangle(Shape):

    def __init__(self, length, width):
        self.length=length
        self.width=width

    def area(self):
        return self.width*self.length

r=Rectangle(10,20)
print("Area of Rectangle=",r.area())
r.another_method()

shape:Shape=Rectangle(20,5)
print("Area of Rectangle=",shape.area())
shape.another_method()