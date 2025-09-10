class Shape:

    def __init__(self):
        self.__color =''

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

s=Shape()
s.set_color('red')
print('Color:',s.get_color())