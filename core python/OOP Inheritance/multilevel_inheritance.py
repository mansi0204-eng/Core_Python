class Student:

    def getname(self):
        self.name=input("Name:")
        self.Class=input("Class:")

class Test(Student):

    def gemarks(self):
        print("Enter your marks")
        self.physics=int(input("Physics:"))
        self.Chemistry = int(input("Chemistry:"))
        self.Maths = int(input("Maths:"))

class Display(Test):

    def result(self):
        print("Name:",self.name)
        print("class:",self.Class)
        Total_marks=self.physics + self.Chemistry + self.Maths
        print("Total Marks",Total_marks)
d=Display()
d.getname()
d.gemarks()
d.result()