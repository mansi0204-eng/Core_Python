class BankAccount:
    def __init__(self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amt):
        if amt > 0:
            self.balance += amt
            print("Deposited:", amt)
        else:
            print("Amount must be positive.")

    def withdraw(self, amt):
        if amt > 0:
            if amt <= self.balance:
                self.balance -= amt
                print("Withdrawn:", amt)
            else:
                print("Not enough balance.")

    def show_balance(self):
        print("Balance:", self.balance)


def main():
    name = input("Enter your name: ")
    acc = BankAccount(name)

    while True:
        print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
        ch = input("Choose option: ")

        if ch == '1':
            amt = float(input("Amount to deposit: "))
            acc.deposit(amt)
        elif ch == '2':
            amt = float(input("Amount to withdraw: "))
            acc.withdraw(amt)
        elif ch == '3':
            acc.show_balance()
        elif ch == '4':
            print("Bye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()