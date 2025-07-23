name="mansi"
for ch in "abcdefghijklmnopqrstuvwxyz":
    count=0
    for letter in name:
        if letter==ch:
            count+=1
    if count!=0:
        print(ch,"count=",count)
