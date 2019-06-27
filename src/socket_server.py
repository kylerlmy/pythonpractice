import socket
import sys
from time import ctime

#tcpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# tcpsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

HOST = '127.0.0.1'
PORT = 50007
BUFSIZE = 1024

s = None

for res in socket.getaddrinfo(HOST, PORT, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
    family, socktype, proto, canonname, addr = res  # 将元组tes 赋值给多个变量

    try:
        s = socket.socket(family, socktype, proto)
    except OSError as msg:
        s = None
        continue

    try:
        s.bind(addr)
        s.listen(1)
    except OSError as msg:
        s.close()
        s = None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)

conn, addr = s.accept()

with conn:
    print('Connected by', addr)
    while True:
        data = conn.recv(BUFSIZE)
        print('Received', repr(data))
        if not data:
            break
        conn.send(data)
