try:
    number=int(input("Enter you number:"))

    if number>10:
        raise Exception("Invalid Number")

except Exception as e:
    print("exception:",e)
print("after")