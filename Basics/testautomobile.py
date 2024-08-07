class Automobile:

    def __init__(self, car, speed, color):
        self.car = car
        self.speed = speed
        self.color = color

    def getcar(self):
        return self.car

    def getspeed(self):
        return self.speed

    def getcolor(self):
        return self.color

    def gear(self):

        if (self.speed <= 20):
            return 1
        if (20 >self.speed >= 40):
            return 2
        if (40 < self.speed >= 60):
            return 3
        if (60 < self.speed >= 80):
            return 4
        if (self.speed > 80):
            return 5


A = Automobile("BMW", 60, "black")
print("Car:", A.getcar(), "\nSpeed:", A.getspeed(), "\nGear:", A.gear(), "\nColor", A.getcolor())
