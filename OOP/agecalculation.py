import datetime


class person:
    def __init__(self, name, dob, address):
        self.name = name
        self.dob = dob
        self.address = address

    def getname(self):
        return self.name

    def getdob(self):
        D = datetime.datetime.now()
        Y = D.year
        return Y - self.dob

    def getaddress(self):
        return self.address


P = person("mansi", 2004, "nisarpur")
print("Name", P.getname(), "age", P.getdob(), "address", P.getaddress())
