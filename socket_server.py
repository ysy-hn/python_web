import socket

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
body = '''Hello,world! <h1> from the5fire 《Django 企业开发实战》</h1>'''
response_params = [
    'HTTP/1.0 200 OK',
    'Date: Sun,27 may 2018 01 : 01 : 01 GMT '
    'Content-Type: text/plain; charset=utf-8'
    'Content-Length:{}\r\n'.format(len(body.encode())),
    body,
]
response = '\r\n'.join(response_params)

def handle_connection(conn,addr):
    print('oh,new conn',conn,addr)
    import time
    time.sleep(100)

def handle_connection(conn,addr):
    request = b""
    while EOL1 not in request and EOL2 not in request:
        request += conn.recv(1024)
    print(request)
    conn.send(response.encode())  # response转为bytes后传输
    conn.close()

def main():
    # socket AF INET 用于服务器 服务器之间的 网络通信
    # socket SOCK_STREAM 用于 TCP 流式 socket 通信
    serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置端口可复用，保证我们每次按Ctrl+C组合键之后，快速重启
    serversocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    serversocket.bind(('127.0.0.1',8000))
    serversocket.listen(5)  # 设置backlog-socket连接最大排队数量
    print('http://127.0.0.1:8000')
    try:
        while True:
            conn,address = serversocket.accept()
            handle_connection(conn,address)
    finally:
        serversocket.close()

if __name__ == '__main__':
    main()





