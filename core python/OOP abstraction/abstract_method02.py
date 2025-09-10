from abc import ABC, abstractmethod


class Shape(ABC):

    def execute(self):
        self.area()

    def area(self):
        pass


class Rectangle(Shape):

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        rectangle_area = self.width * self.length
        print("Rectangle Area:", rectangle_area)
        return rectangle_area


r = Rectangle(10, 5)
r.execute()
