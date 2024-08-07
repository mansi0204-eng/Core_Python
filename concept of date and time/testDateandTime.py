import datetime

a = datetime.datetime.now()
# print(a.year)
# b = datetime.datetime(2022, 9, 12)
# print(b)
# print(a.month,"-",a.day,"-",a.year)
print(a.strftime("%X"))