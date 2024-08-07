a = int(input("Enter First Numer:"))
b = int(input("Enter Second Number:"))


def math_operation(x=a, y=b):
    sum = x + y
    print("Addition of two given number is=", sum)
    multiply = x * y
    print("multiplication of two given number is=", multiply)
    division = x / y
    print("division of two given number is=", division)
    subtraction = x - y
    print("subtraction of two given number is=", subtraction)
    return sum, multiply, division, subtraction
