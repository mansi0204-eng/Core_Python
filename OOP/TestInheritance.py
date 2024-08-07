class shape:

    def parent(self, color):
        self.color = color

    def getcolor(self):
        return self.color


class rectangle(shape):

    def area(self, length, width):
        self.length = length
        self.width = width

    def getarea(self):
        return self.length * self.width


obj = rectangle()
obj.parent("black")
obj.area(10, 20)
print("Rectangle color=", obj.getcolor(), "\narea=", obj.getarea())


class circle(shape):

    def area(self, radius):
        self.radius = radius
        self.PI = 22 / 7

    def getarea(self):
        return self.PI * self.radius ** 2


obj = circle()
obj.parent("red")
obj.area(10)
print("circle color=", obj.getcolor(), "\narea=", obj.getarea())


class Triangle(shape):

    def area(self, base, height):
        self.base = base
        self.height = height

    def getarea(self):
        return self.base * self.height


obj = Triangle()
obj.parent("white")
obj.area(10, 20)
print("Triangle color=", obj.getcolor(), "\narea=", obj.getarea())
