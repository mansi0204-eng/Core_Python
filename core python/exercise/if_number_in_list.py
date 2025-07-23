list=[50,565,58,65,55]
number=5
count=0

for i in list:
    if i==number:
        count+=1
if count!=0:
    print("number exist")
else:
    print("number does not exist")