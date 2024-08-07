class Math:

    def number(self, a, b):
        self.a = a
        self.b = b

    def Add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def modulus(self):
        return self.a % self.b


M = Math()
M.number(10, 20)
print("Addition of two given number is:", M.Add(), "\nSubtraction. of two given number:", M.subtract(),
      "\nDivision of two given number is:", M.division(), "\nMultiplication of two given number is:", M.multiply(),
      "\nmodulus of two given number is:", M.modulus())


class Employee:
    def empName(self, Name, City,post):
        self.Name = Name
        self.City = City
        self.post = post

    def getEmp(self):
        return self.Name, self.City, self.post


E = Employee()
E.empName("mansi", "nisarpur", "operator")
print("employe name and city:", E.getEmp())
