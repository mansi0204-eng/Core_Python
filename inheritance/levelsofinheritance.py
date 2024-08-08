# # single level inheritance
# class Parent:
#     def parent(self):
#         print("parent method call")
#
#
# class Child(Parent):
#     def child(self):
#         print("child method called")
#
#
# obj = Child()
# obj.parent()
# obj.child()
#
#
# # Multi Level Inheritance
# class Grandparent:
#
#     def grandparent(self):
#         print("Grandparent Method called")
#
#
# class Parent(Grandparent):
#
#     def parent(self):
#         print("Parent Method called")
#
#
# class Child(Parent):
#     def child(self):
#         print("child Method called")
#
#
# obj = Child()
# obj.grandparent()
# obj.parent()
# obj.child()
#
#
# # hierarchical inheritance
#
# class Parent:
#     def parent(self):
#         print("parent method called")
#
#
# class Child1(Parent):
#     def child(self):
#         print("child 1 method called")
#
#
# class Child2(Parent):
#     def child(self):
#         print("child 2 method called")
#
#
# obj1 = Child1()
# obj2 = Child2()
# obj1.child()
# obj1.parent()
# obj2.child()
# obj2.parent()

# Multiple Inheritance
class Parent1:
    def parent1(self):
        print("parent 1 method called")


class Parent2:
    def parent2(self):
        print("Parent 2 method called")


class Child(Parent1, Parent2):
    def child(self):
        print("child method called")


obj = Child()
obj.parent1()
obj.parent2()
obj.child()





