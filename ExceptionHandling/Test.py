# a = 20
# b = 0
#
# try:
#     c = a % b
#     print(c)
# except ArithmeticError:
#     print("it's an Arithmetic error")
# finally:
#     print("hello")


# try:
#     d=int(input("Enter Value"))
#     a = '10'
#     b = '2'
#     c = a/b
#     print(c)
#     print(d)
# except TypeError as t:
#     print("Type Error")
# except ValueError as v:
#     print("Value Error")
# except ModuleNotFoundError as m:
#     print("Module Error")
#
# try:
#     a = int(input("Enter your first Number:"))
#     b = int(input("Enter your Second Number:"))
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print("Can't divide by zero")
# except ValueError:
#     print("Enter Integer value only")

list=[0,1,2,3,4]
try:
    print(list[9])
except Exception as e:
    print(e)