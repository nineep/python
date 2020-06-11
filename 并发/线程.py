import threading
import time

def Hi(num):
    print("hello %s" % num)
    time.sleep(3)


if __name__ == '__main__':
    t1 = threading.Thread(target=Hi, args=(10,))
    t1.start()

    t1 = threading.Thread(target=Hi, args=(11,))
    t1.start()

    print('ending')