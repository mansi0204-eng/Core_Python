def readfile():

    file=open("D:/test.txt","r")
    text=file.read()
    print(text)
    file.close()

readfile()