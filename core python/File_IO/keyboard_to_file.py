def keyboardtofile():

    file=open("D:/test.txt","w")
    text=input("Enter your message:")

    while text!="quit":
        file.write(text)
        file.write("\n")
        text=input("")
    file.close()

keyboardtofile()