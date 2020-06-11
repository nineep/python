import threading
import time

def music():
    print('开始music %s' % time.ctime())
    time.sleep(3)
    print('结束music %s' % time.ctime())


def game():
    print('开始game %s' % time.ctime())
    time.sleep(5)
    print('结束game %s' % time.ctime())


if __name__ == '__main__':
    t1 = threading.Thread(target=music)
    t1.start()
    t2 = threading.Thread(target=game)
    t2.start()
    t1.join() #等待t1子线程结束后，才能继续执行主线程任务，\
    # 否则主线程和t1子线程任务并发
    t2.join()  #子线程 和 主线程之间的先后顺序
    print('ending')  #主线程任务
