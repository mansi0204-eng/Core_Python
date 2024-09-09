try:
    number=int(input("Enter your Number:"))
    if number>10:
        raise Exception("Number should be less than 10")
    else:
        print(number+20)
except Exception as e:
    print(e)