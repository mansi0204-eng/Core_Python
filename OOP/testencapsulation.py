class Person:
    def setName(self, Name):
        self.Name = Name

    def getName(self):
        return self.Name

    def setCity(self, City):
        self.City = City

    def getCity(self):
        return self.City


P = Person()
P.setName("mansi")
P.setCity("Nisarpur")

print(P.getName())
print(P.getCity())
