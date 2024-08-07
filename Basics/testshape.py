class shape:

    def __init__(self, color):
        self.color = color

    def getcolor(self):
        return self.color


class Rectangle(shape):

    def __init__(self, length, width, color):
        super().__init__(color)
        self.length = length
        self.width = width

    def getarea(self):
        return self.length * self.width


class Circle(shape):

    def __init__(self, radius, color):
        super().__init__(color)
        self.radius = radius
        self.PI = 22 / 7

    def getarea(self):
        return self.PI * self.radius ** 2


class Triangle(shape):

    def __init__(self, base, height, color):
        super().__init__(color)
        self.base = base
        self.height = height

    def getarea(self):
        return self.base * self.height


R = Rectangle(20, 30, "red")
print("Area of Rectangle", R.getarea(), "\nColor of Rectangle", R.getcolor())

C = Circle(2, "Blue")
print("Area of Circle", C.getarea(), "\nColor of Circle", C.getcolor())

T = Triangle(25, 12, "Black")
print("Area of Triangle", T.getarea(), "\nColor of Triangle", T.getcolor())
