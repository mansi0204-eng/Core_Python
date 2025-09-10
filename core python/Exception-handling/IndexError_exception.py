try:
    lst = [1, 2, 3]
    print(lst[5])   # index 5 exist hi nahi karta
except IndexError as e:
    print("Index out of range!",e)
