# import time
# import multiprocessing
#
# def foo(q):
#     time.sleep(1)
#     print('son process', id(q))
#     q.put(123)
#     q.put('yuan')
#
# if __name__ == '__main__':
#     q = multiprocessing.Queue()
#     p = multiprocessing.Process(target=foo, args=(q,))
#     p.start()
#     print('main process', id(q))
#     print(q.get())
#     print(q.get())


# from multiprocessing import Process, Pipe
# def f(conn):
#     conn.send([12, {'name': 'yuan'}, 'hello'])
#     response = conn.recv()
#     print('response', response)
#     conn.close()
#     print('q_ID2:', id(conn))
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()
#
#     print('q_ID1:', id(child_conn))
#     p = Process(target=f, args=(child_conn,))
#     p.start()
#
#     print(parent_conn.recv())
#
#     parent_conn.send('儿子你好')
#     p.join()


from multiprocessing import Process, Manager
def f(d, l, n):
    d[n] = '1'
    d['2'] = 2
    l.append(n)

if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(5))

        p_list = []

        for i in range(10):  #启动10个子进程
            p = Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print(d)
        print(l)
