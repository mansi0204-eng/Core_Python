from time import sleep
from threading import *

class Account:
    balance = 0

    def get_balance(self):
        sleep(2)
        return self.balance

    def set_balance(self, amount):
        sleep(2)
        self.balance = amount

    def diposite(self, amount):
        bal = self.get_balance()
        self.set_balance(bal + amount)


class Racing(Thread):
    account: Account
    name = "no name"

    def __init__(self, account, name):
        super(Racing, self).__init__()
        self.account = account
        self.name = name

    def run(self):
        for i in range(5):
            self.account.diposite(100)
            print(self.name, self.account.get_balance())


def main_task():
    acc = Account()
    # create thread instances
    t1 = Racing(acc, "Ram")
    t2 = Racing(acc, "Shyam")

    # Start threads
    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print("Finish")


main_task()