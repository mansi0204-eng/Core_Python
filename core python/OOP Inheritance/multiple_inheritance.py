class Addition:

    def sum(self, a, b):
        return a + b


class Multiplication:

    def multiply(self, a, b):
        return a * b


class Derived(Addition, Multiplication):
    def divide(self,a,b):
        return a/b

derived_obj=Derived()
print("Division=",derived_obj.divide(10,2))
print("Multiplication=",derived_obj.multiply(5,2))
print("Addition=",derived_obj.sum(452,56))