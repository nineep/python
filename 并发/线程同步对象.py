import threading, time

class Boss(threading.Thread):

    def run(self):
        print('BOSS: 今晚大家加班')
        print(event.isSet())
        event.set()
        time.sleep(5)

        print('BOSS: 22点下班')
        print(event.isSet())
        event.set()


class Worker(threading.Thread):
    def run(self):
        event.wait()
        print('worker: 哎')
        time.sleep(1)
        event.clear()

        event.wait()
        print('worker: oh')

if __name__ == '__main__':
    event=threading.Event()

    threads=[]
    for i in range(5):
        threads.append(Worker())
    threads.append(Boss())
    print(threads)

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print('ending...')
