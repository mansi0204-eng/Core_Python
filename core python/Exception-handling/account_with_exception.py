class InsufficientFundException(Exception):
    def __init__(self, msg):
        super().__init__(msg)


class Account:
    def __init__(self):
        self.balance = 0

    def set_balance(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:",amount ,"Current Balance:", self.balance)

    def withdrawl(self, amount):
        if self.balance - amount >= 2000:
            self.balance -= amount
            print(f"Withdrew: {amount}, Remaining Balance: {self.balance}")
        else:
            raise InsufficientFundException("Insufficient balance. Minimum ₹2000 must remain in the account.")


# Example
acc = Account()
acc.set_balance(1000)

try:
    acc.deposit(1000)  # balance = 7000
    acc.withdrawl(2000)  # balance = 4000
    # will raise exception (balance would go below 2000)
except InsufficientFundException as e:
    print("exception:", e)

try:
    acc.deposit(7000)
    acc.set_balance(2000)
    acc.withdrawl(3000)
except InsufficientFundException as e:
    print("exception",e)
