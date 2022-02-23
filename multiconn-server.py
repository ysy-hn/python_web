import selectors
import socket

sel = selectors.DefaultSelector()
lsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
lsock.bind(host,port)
lsock.listen()
print('listening on',(host,port))
lsock.setblocking(False)  # 配置 socket 为非阻塞模式，这个 socket 的调用将不在是阻塞的.
sel.register(lsock,selectors.EVENT_READ,data=None)
# sel.register() 使用 sel.select() 为你感兴趣的事件注册 socket 监控，
# 对于监听 socket，我们希望使用 selectors.EVENT_READ 读取到事件
# data 用来存储任何你 socket 中想存的数据，当 select() 返回的时候它也会返回。
# 我们将使用 data 来跟踪 socket 上发送或者接收的东西
while True:
    events = sel.select(timeout=None)
    for key, mask in events:
        if key.data is None:
            accept_wrapper(key.fileobj)
        else:
            service_connection(key, mask)

