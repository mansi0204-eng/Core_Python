try:
    f = open("myfile.txt", "r")   # agar file nahi hai to error aayega
except FileNotFoundError as e:
    print("File not found!",e)
