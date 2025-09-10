class Account:

    def __init__(self, name):
        self.name=name
        self.balance=0

    def deposit(self,amt):
        if amt>0:
            self.balance+=amt
            print("Deposited:",amt)
        else:
            print("Amount cannot me negative")

    def withdraw(self,amt):
        if amt>0:
            if amt<=self.balance:
                self.balance-=amt
                print("withdrawn:",amt)
            else:
                print("Balance is not enough")

    def show_balance(self):
        print("Account Balance:",self.balance)

def main():

    name=input("Enter your name")
    acc=Account(name)

    while True:
        print("\n1. Deposit \n2. Withdraw \n3. check balance \n4. exit")
        ch=input("choose option:")

        if ch=='1':
            amt=float(input("Amount to deposit"))
            acc.deposit(amt)
        elif ch=='2':
            amt=float(input("Amount to withdraw"))
            acc.withdraw(amt)
        elif ch=='3':
            acc.show_balance()
        elif ch=='4':
            print("Bye!")
            break
        else:
            print("Invalid option. Try again")

if __name__=="__main__":
    main()















