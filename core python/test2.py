class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

    def __repr__(self):
        return f"Employee:('{self.name}', {self.salary})"

    def __add__(self, other):
        return self.salary + other.salary


e1 = Employee("Mansi", 5000)
e2 = Employee("Nikhil", 6000)

print(e1)           # __str__
print(repr(e1))     # __repr__
print(e1 + e2)      # __add__
