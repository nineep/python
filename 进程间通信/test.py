# dic = {'k1': 123, 'k2':123, 'k3':123}
# # print(dic.items())
# for i, v in enumerate(dic.items(), 1):
#     print(i, v[0], v[1])
#
# for i, v in enumerate(dic, 1):
#     print(i, v, dic[v])


# # 1 1 2 3 5 8
#
# def fib(num):
#     a = b = 1
#     l = [1]
#     while b < num:
#         a, b = b, a+b
#
#         print(a)
#         l.append(a)
#     print(l)
# fib(100)


# class Mytype(type):
#     def __init__(self, what, bases=None, dict=None):
#         print(what, bases, dict)
#
#     def __call__(self, *args, **kwargs):
#         print('调用Mytype __call__')
#         obj = object.__new__(self)
#         self.__init__(obj, *args, **kwargs)
#         return obj
#
# class Room(metaclass=Mytype):
#     def __init__(self, name):
#         self.name = name
#
# r1 = Room('test')
# print(r1.__dict__)


# #使用__slots__节省内存
#
# class Myclass(object):
#     def __init__(self, name, identifier):
#         self.name = name
#         self.identifier = identifier
#         self.set_up()

'''
物理层：光缆、双绞线、无线电波
数据链路层: ethernet协议，mac地址（硬件地址），广播
网络层：ip协议、ip地址逻辑地址寻址
传输层：TCP，UDP协议，协议端口号，流控，差错校验
会话层：建立、管理、终止会话
表示层：数据的表示、安全、压缩
应用层：网络服务于最终用户的一个接口，http,ftp,smtp等协议
'''

# import socket
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.bind(('127.0.0.1', 8080))
# phone.listen(10)
# conn, addr = phone.accept()
# data=conn.recv(1024)
# conn.send(data)
# conn.close()
# phone.close()
#
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.connect(('127.0.0.1', 8080))
# phone.send(data.encode('utf-8'))
# phone.recv(1024)
# phone.close

#
# from socket import *
#
# ip_port = ('127.0.0.1', 8080)
#
# udp_server = socket(AF_INET, SOCK_DGRAM)
# udp_server.bind(ip_port)
#
# while True:
#     data, addr = udp_server.recvfrom(buffer_size)
#     print(data)
#
#     udp_server.sendto(data, addr)

# import socket
# import select
# sk = socket.socket()
# sk.bind(('127.0.0.1', 9904))
# sk.listen(5)
#
# while True:
#     r, w, e = select.select([sk,], [], [], 5)
#     for i in r:
#         conn, add = i.accept()
#         print(conn)
#         print('hello')
#
#     print('>>>')

import socket
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 8080))
    sock.listen(5)

    while True:
        connection, address = sock.accept()
        buf = connection.recv(1024)
        f = open('test.html', 'rb')
        data = f.read()
        connection.sendall(bytes('HTTP/1.1 201 OK\r\n\r\n', 'utf-8'))
        connection.sendall(data)
        connection.close()

if __name__ == '__main__':
    main()