list=[25,56,45,48,45,66,52]
highest=0
second_highest=0

for num in list:
    if num>highest:
        second_highest=highest
        highest=num
    elif num>second_highest and num!=highest:
        second_highest=num
print("highest",highest)
print("second highest",second_highest)

