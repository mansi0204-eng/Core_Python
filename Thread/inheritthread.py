import threading


class Hii(threading.Thread):
    def run(self):
        for i in range(5):
            print("hii", i)


t1 = Hii()
t1.start()
