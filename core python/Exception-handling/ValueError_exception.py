try:
    num = int(input("Enter a number: "))  # yaha agar 'abc' daloge to error aayega
    print("You entered:", num)
except ValueError as e:
    print("Invalid input! Please enter a number.",e)
