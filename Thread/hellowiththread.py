import threading



def hello():
    for i in range(15):
        print("hello", i)


def hii():
    for i in range(15):
        print("hii", i)


t1 = threading.Thread(target=hello)
t2 = threading.Thread(target=hii)
t1.start()
t2.start()
