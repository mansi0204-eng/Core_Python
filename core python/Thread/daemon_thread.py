import threading
from time import sleep

def first_thread(name):
    for i in range(1,11):
        sleep(3)
        print(name,"=",i)

def second_thread(name):
    for i in range(1,11):
        sleep(1)
        print(name,"=",i)

t1=threading.Thread(target=first_thread,args=('daemon',), daemon=True)
t2=threading.Thread(target=second_thread,args=('yash',))
t1.start()
t2.start()
