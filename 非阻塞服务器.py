import socket

server = socket.socket()        #创建套接字
server.setblocking(False)       #把套接字设置为非阻塞
server.bind(('0.0.0.0', 8001))  #绑定IP和端口
server.listen(5)                #监听端口


all_connection = []             #保存已经连接的客户
while True:
    #只管连接的事情
    try:
        conn, addr = server.accept()    # 建立连接，没有就抛出异常
        conn.setblocking(False)         #设置非阻塞
        print('用户连接:', addr)
        all_connection.append(conn)
    except Exception as e:
        pass


    #处理已经连接用户的消息
    handle = all_connection.copy()  #完全拷贝了列表
    for connection in handle:
        try:
            recv_data = connection.recv(1024)
            if recv_data:
                print(recv_data.decode())
                connection.send(recv_data)
            else:                               #客户端消息处理完了，已经断开了连接
                print('断开连接', connection)
                connection.close()
                all_connection.remove(connection)       #从客户列表里移除断开连接的客户
        except Exception as e:
            pass
