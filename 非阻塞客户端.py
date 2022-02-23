import socket

client = socket.socket()
client.connect(('127.0.0.1',8889))

while True:
    data = input('输入数据:')
    if data:
        client.send(data.encode())
        recv_data = client.recv(1024)
        print(recv_data.decode())
    else:
        break

client.close()
