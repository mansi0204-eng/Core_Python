number=14541
n=number
rem=0
sum=0

while n>0:
    rem=n%10
    sum=(sum*10)+rem
    n=n//10
if sum==number:
    print(number,"is an palindrome number")
else:
    print(number,"is not an palindrome number")