class Automobile:
    def __init__(self, color, speed, make):
        self.color = color
        self.speed = speed
        self.make = make

    def getcolor(self):
        return self.color

    def getspeed(self):
        return self.speed

    def getmake(self):
        return self.make

    def gear(self):
        if (self.speed <= 20):
            return 1
        if (20 < self.speed >= 40):
            return 2
        if (40 < self.speed >= 60):
            return 3
        if (60 < self.speed >= 80):
            return 4
        if (self.speed > 80):
            return 5


B = Automobile("red", 60, "SUV")
print("color", B.getcolor(), "\nSpeed", B.getspeed(), "\nmake", B.getmake(), "\ngear", B.gear())
