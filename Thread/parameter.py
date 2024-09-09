import threading


def hello(name):
    print("hello", name)


t1 = threading.Thread(target=hello("mansi"))
t1.start()
