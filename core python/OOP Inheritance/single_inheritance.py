class Shape:

    def __init__(self):
        self.color = ''
        self.borderWidth = 0

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_borderWidth(self, borderWidth):
        self.borderWidth = borderWidth

    def get_borderWidth(self):
        return self.borderWidth


class Rectangle(Shape):

    def __init__(self):
        self.length = 0
        self.width = 0

    def set_length(self, length):
        self.length = length

    def get_length(self):
        return self.length

    def set_width(self, width):
        self.width = width

    def get_width(self):
        return self.width

r=Rectangle()
r.set_length(5)
r.set_borderWidth(50)
r.set_width(10)
r.set_color('red')

print("color:",r.get_color())
print("borderWidth]:",r.get_borderWidth())
print("width:",r.get_width())
print("length:",r.get_length())
