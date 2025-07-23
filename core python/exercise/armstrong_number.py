number=153
n=number
sum=0
rem=0


while n>0:
    rem=n%10
    sum=sum+(rem*rem*rem)
    n=n//10

if sum==number:
    print("armstrong number")
else:
    print("not armstrong number")

