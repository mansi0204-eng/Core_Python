import datetime
dob=datetime.date(2004,4,2)
today=datetime.date.today()

age=today.year - dob.year

if(today.month, today.day)<(dob.month, dob.day):
    age -=1

print("your age is=",age)