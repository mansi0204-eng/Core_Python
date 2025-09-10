def char_read_wrte():
    with open("D:/char.txt", "w") as f:
        text = input("Enter your text")
        for ch in text:
            f.write(ch)


    with open("D:/char.txt", "r") as f:
        ch = f.read(1)
        while ch:
            print(ch, end=" ")
            ch = f.read(1)


char_read_wrte()
