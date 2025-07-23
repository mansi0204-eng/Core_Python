list=[69,54,20,50,85]

for i in range(0, len(list)):
    for j in range(i+1, len(list)):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
    print(list[i], end=" ")