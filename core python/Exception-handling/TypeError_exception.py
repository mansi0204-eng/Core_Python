try:
    result = "abc" + 10
    print(result)# string + number allowed nahi hai
except TypeError as e:
    print("Type mismatch:", e)
