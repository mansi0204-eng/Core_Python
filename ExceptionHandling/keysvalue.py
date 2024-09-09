my_dict = {'name': "mansi", 'age': 20, }
e = input("Enter value to search")
f = input("Enter key to search")
try:
    if e.isdigit():  # will check if the value entered by user is number if it is than
        e = int(e)  # it will change the number into integer datatype
    if f.isdigit():
        f = int(f)

    if e in my_dict.values():
        print("value is present")

    else:
        print("value not found")

    if f in my_dict.keys():
        print("Key is present")

    else:
        print("Key not found")
except Exception as ex:
    print(ex)

