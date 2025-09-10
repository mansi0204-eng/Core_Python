class Account:

    def __init__(self, acc_name, acc_number):
        self.acc_name=acc_name
        self.acc_number=acc_number
        self.balance=5000

    # def set_name(self,acc_name):
    #     self.acc_name=acc_name

    def get_name(self):
        return self.acc_name

    # def set_number(self,acc_number):
    #     self.acc_number = acc_number

    def get_number(self):
        return self.acc_number

    def set_balance(self,balance):
        self.balance=balance

    def get_balance(self):
        return self.balance

    def set_deposit(self, deposit):
        self.deposit=deposit

    def get_deposit(self):
        return self.deposit

    def set_withdraw(self, withdraw):
        self.withdraw=withdraw

    def get_withdraw(self):
        return self.withdraw

    def test_deposit(self):
        self.balance=self.balance+self.deposit
        return self.balance

    def test_withdraw(self):
        self.balance=self.balance-self.withdraw
        return self.balance

a=Account('mansi', 201)
# a.set_name('mansi')
# a.set_number(201)
a.set_deposit(2000)
a.set_withdraw(1000)

print("Account Number:",a.get_number())
print("Account holder name:",a.get_name())
print("Account balance Before deposit",a.get_balance())
print("Account balance after deposit",a.test_deposit())
print("Account balance after withdraw",a.test_withdraw())




