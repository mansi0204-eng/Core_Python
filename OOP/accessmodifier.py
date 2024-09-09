class Person:
    Name = "Mansi Kumawat"  # Public
    _Code = "Mk002"  # Protected
    __City = "Barwani"  # Private


P = Person()
print("Name", P.Name, "\nCode", P._Code, "\nCity", P._Person__City)
