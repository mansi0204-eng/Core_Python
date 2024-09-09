# f = open("new.txt", "w")
# f.write("hello this my new file")
# print("done")
# # print(f.read())
# f.close()

#
# file = open("new.txt","r")
# text = file.read()
# print(text)
# file.close()


# folder = open("C:/Users/Dell/Desktop/python/mansi.txt","r")
# # folder.write(" hello")
# file=folder.read()
# print(file)
# print("task done")
# folder.close()
#


# folder = open("C:/Users/Dell/Desktop/python/test.txt","r+")
# folder.write(" hello")
# folder.seek(0)
# file=folder.read()
# print(file)
#
# folder.close()

fo = open("C:/Users/Dell/Desktop/python/mansi.txt", "r")
print("File Name:", fo.name)
print("Mode of Opening:", fo.mode)
print("Is closed:", fo.closed)
fo.close()


# file=open("C:/Users/Dell/Desktop/python/mansi.txt")
# for line in file:
#     print(line)
# file.close()
#
# with open("C:/Users/Dell/Desktop/python/mansi.txt","w") as file:
#     file.write("\ngreetings to you all")
#     file.write("hello")


# folder = open("C:/Users/Dell/Desktop/python", "r")
# file = folder.read()
# print(file)
# folder.close()
