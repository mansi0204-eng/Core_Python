# import pickle
#
# class Employee:
#     def __init__(self, eno, ename, city, age):
#         self.eno = eno
#         self.ename = ename
#         self.city = city
#         self.age = age
#
#
# e = Employee(1, "mansi", "barwani",20)
# f = open("C:/Users/Dell/Desktop/hello/emp.txt", "wb")
# pickle.dump(e, f)
# f.close()
#
# f = open("C:/Users/Dell/Desktop/hello/emp.txt", "rb")
# e = pickle.load(f)
# f.close()
# print(e.eno)
# print(e.ename,e.city,e.age)
# import os
# os.remove("C:/Users/Dell/Desktop/hello/expenses.txt")


# file = open("C:/Users/Dell/Desktop/hello/mansi.txt", "w")
# text="hii"
# while (text!="quit"):
#     text = input("Enter your text")
#     if (text=="quit"):
#         break
#     file.write(text)
#     file.write("\n")
# file.close()


import os
t=os.listdir("C:/Users/Dell/PycharmProjects/Corepython/Basics")
print(t)