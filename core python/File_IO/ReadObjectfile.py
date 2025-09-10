import pickle
from WriteObjectFile import Employee

with open("D:/employee.txt","rb") as file:
    emp=pickle.load(file)
    print("Employee information after unpickling")
    emp.display()