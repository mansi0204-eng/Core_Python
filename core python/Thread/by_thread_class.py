import threading
from threading import *

class Hi(Thread):
     def __init__(self,name):
         super().__init__()
         self.name=name

     def run(self):
         for i in range(1,4):
             print("hi=",self.name,i)

t1=Hi('mansi')
t2=Hi('yash')

t1.start()
t2.start()