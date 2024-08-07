import datetime


class Person:
    def __init__(self, name, dob, city):
        self.name = name
        self.dob = dob
        self.city = city

    def getname(self):
        return self.name

    def getdob(self):
        D = datetime.datetime.now()
        Y = D.year
        return Y - self.dob

    def getcity(self):
        return self.city


P = Person("mansi", 2004,  "barwani")
print("Name=", P.getname(), "Age=", P.getdob(), "getcity=", P.getcity())
