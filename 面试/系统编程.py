#进程
"""
程序运行在操作系统上的一个实例，称为进程
进程需要相应系统资源：内存，时间片，pid
"""
import os
from multiprocessing import Process
import time

def pro_func(name, age, **kwargs):
    for i in range(5):
        print('子进程在运行中，name=%s, age=%d, pid=%d' % (name, age, os.getpid()))
        print(kwargs)
        time.sleep(0.2)

if __name__ == '__main__':
    #创建Process实例
    p = Process(target=pro_func, args=('小明', 19), kwargs={'m': 20})
    p.start()
    time.sleep(1)
    p.terminate()
    p.join()

# 注意： 进程间不共享全局变量
# 进程间通信Queue
from multiprocessing import Process, Queue
import os, time, random
# 写数据进程执行的代码
def write(q):
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print("Get %s from queue" % value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':
    #父进程创建Queue实例，并传给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #启动子进程pw，写入
    pw.start()
    #等待pw结束
    pw.join()
    #启动子进程pr， 读取
    pr.start()
    pr.join()
    #pr进程里是死循环，无法等待其结束，只能强行终止
    print('写读完成')


# # 进程池Pool
# from multiprocessing import Pool
# import os, time, random
#
# def worker(msg):
#     t_start = time.time()
#     print('%s 开始执行， 进程号为%d' % (msg, os.getpid()))
#     # random.random()随机生成0-1之间的浮点数
#     time.sleep(random.random()*2)
#     t_stop = time.time()
#     print(msg, '执行完毕，耗时%0.2f' % (t_stop-t_start))
#
# # 定义一个进程池，最大进程数为3
# po = Pool(3)
# for i in range(0, 10):
#     po.apply_async(worker, (i,))
# print('----start')
# po.close()
# po.join()
# print('------end')


# 进程池中使用Queue
# 如果要使用Pool创建进程， 就需要使用multiprocessing.Manager()中的Queue()
# 而不是multiprocessing.Queue(), 否则会得到如下错误：
# RuntimeError： Queue objects should only be shared between processs through inheritance
from multiprocessing import Manager, Pool
import os, time, random
def reader(q):
    print('reader 启动（%s), 父进程为（%s)' % (os.getpid(), os.getpid()))
    for i in range(q.size()):
        print('reader 从Queue获取到消息：%s' % q.get(True))

def writer(q):
    print("writer 启动（%s),父进程为(%s)"%(os.getpid(),os.getpid()))
    for i in "itcast":
        q.put(i)

if __name__ == '__main__':
    print('(%s) start' % os.getpid())
    q = Manager().Queue()
    po = Pool()
    po.apply_async(writer, (q,))
    time.sleep(1)
    po.apply_async(reader, (q,))
    po.close()
    po.join()
    print('%s End' % os.getpid())


# 进程，线程，协程 理解
"""
进程：系统资源分配的最小单位，拥有自己独立的内存空间，进程数据不共享，开销大
线程：cpu调度执行的最小单位，也就执行路径， 不能独立存在，依赖进程存在，一个进程至少有一个线程，叫主线程
        多个线程共享内存（数据共享，共享全局变量），从而极大提高了程序的运行效率
协程：是一种用户态轻量级线程，协程调度完全由用户控制。协程拥有自己的寄存器上下文和栈。协程调度时，将寄存器上下文和栈保存到其他地方，
        在切回来的时候， 恢复先前保存的寄存器上下文和栈，直接操作中栈则基本没有内核切换的开销，可以不加锁访问全局变量，所以上下文访问非常快
        
"""

# 异步使用场景
"""
1.不涉及共享资源，或对共享资源只读，即非互斥操作
2.没有时序上的严格关系
3.不需要原子操作，或可以通过其他方式控制原子性
4.常用于IO操作等耗时操作，因为比较影响客户体验和使用性能
5.不影响主线程逻辑
"""


# 多线程共同操作同一个数据互斥锁同步
import threading, time
class MyThread(threading.Thread):
    def run(self):
        global num
        time.sleep(1)

        if mutex.acquire(1):
            num += 1
            msg = self.name + 'set num to' + str(num)
            print(msg)
            mutex.release()
num = 0
mutex = threading.Lock()
def test():
    for i in range(5):
        t = MyThread()
        t.start()

test()
