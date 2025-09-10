class Employee:
    'I am Employee'

    def __init__(self, salary):
        self.salary=salary

    def set_salary(self,salary):
        self.salary=salary

    def get_salary(self):
        return self.salary

emp=Employee(2000)
print("object stored location  in memory",emp)
print("object memory id",id(emp))
print(emp.__doc__)

print("object memory location",str(emp))
print("salary",emp.get_salary())

