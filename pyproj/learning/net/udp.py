# -*- coding: utf-8 -*-

import socket



def server_udp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)# SOCK_DGRAM指定了这个Socket的类型是UDP
    s.bind('127.0.0.1',9999)
    print('Bind UDP on 9999...')
    while True:
        # 接收数据:
        data, addr = s.recvfrom(1024) # 返回数据和客户端的地址与端口
        print('Received from %s:%s.' % addr)
        s.sendto(b'Hello, %s!' % data, addr)


def client_udp():
    # 客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    for data in [b'Michael', b'Tracy', b'Sarah']:
        # 发送数据:
        s.sendto(data, ('127.0.0.1', 9999))
        # 接收数据:
        print(s.recv(1024).decode('utf-8'))
    s.close()

