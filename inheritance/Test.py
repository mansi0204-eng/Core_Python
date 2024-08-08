# # # class car:
# # #     def __init__(self, make, model, year):
# # #         self.make = make
# # #         self.model = model
# # #         self.year = year
# # #
# # #     def getmake(self):
# # #         return self.make
# # #
# # #     def getmodel(self):
# # #         return self.model
# # #
# # #     def getyear(self):
# # #         return self.year
# # #
# # #
# # # obj = car("BMW", 2004, 2024)
# # # print("Car:", obj.getmake(), "\nModel:", obj.getmodel(), "\nYear:", obj.getyear())
# # #
# # #
# # class Mobile:
# #     def __init__(self, maH, percent):
# #         self.maH = maH
# #         self.percent = percent
# #
# #     def getmah(self):
# #         return self.maH
# #
# #     def getpercent(self):
# #         return self.percent
# #
# #
# # class Battery(Mobile):
# #     def battery(self, maH, percent):
# #         super().battery(maH)
# #         super().battery(percent)
# #
# # obj = Battery(5000, 60)
# # print("Battery maH:", obj.getmah(), "\nBattery %", obj.getpercent())
#
#
# class Bank:
#     def Bankbalance(self, Totalbalance, accountN0):
#         self.Totalbalance = Totalbalance
#         self.accountNo = accountN0
#
#     def Deposit(self, depositamount):
#         self.depositamount = depositamount
#
#     def withdraw(self, withdraw):
#         self.withdraw = withdraw
#
#     def gettotal(self):
#         return self.Totalbalance
#
#     def getaccount(self):
#         return self.accountNo
#
#     def getde(self):
#         return self.depositamount
#
#     def getdeposit(self):
#         return self.Totalbalance + self.depositamount
#
#     def getwithdraw(self):
#         return self.withdraw
#
#     def getw(self):
#         return self.Totalbalance - self.withdraw
#
#
# B= Bank()
# B.Bankbalance(5000, "AC505")
# print("Account NO:",B.getaccount(),"\nOpening balance",B.gettotal() )
# B.Deposit(2000)
# print("Deposit Amount",B.getde(),"\nTotal Balance",B.getdeposit())
# B.withdraw(2000)
# print("Withdrawal Amount",B.getwithdraw(),"\nTotal Balance",B.getw())


class A:
    def show(self):
        print("hello guys")


class B:
    def show(self):
        print("he guys")


class C(A, B):
    def New(self):
        print("hello")


# Create an instance of class C
c = C()
b = B()
b.show()

# Call methods on the instance
c.New()
c.show()
c.show()
