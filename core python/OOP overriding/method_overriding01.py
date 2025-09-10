class Shape:

    def area(self):
        print("This is shape class area method ")

class Rectangle(Shape):

    def area(self):
        print("This is Rectangle class area method")

s=Shape()
s.area()

r=Rectangle()
r.area()

shape:Shape=Rectangle()
shape.area()