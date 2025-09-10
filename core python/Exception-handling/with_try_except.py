print("before")
a=10
b=0
print("mid")
try:
    c=a/b
    print("division:",c)
except ZeroDivisionError as e:
    print("number cannot be divided by Zero")
print("after")