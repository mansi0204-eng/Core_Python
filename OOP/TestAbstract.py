from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b


    def area(self):
        return self.l * self.b


R = Rectangle(10, 20)
print("area=", R.area())

