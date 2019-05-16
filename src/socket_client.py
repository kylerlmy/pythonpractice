import socket
import sys

HOST=None
PORT=50007

s=None

for res in socket.getaddrinfo(HOST,PORT,socket.AF_UNSPEC,socket.SOCK_STREAM):
    fimaly,socktype,proto,canonname,sa=res

    try:
        s=socket.socket(fimaly,socktype,proto)
    except OSError as msg:
        s=None
        continue
    
    try:
        s.connect(sa)
        continue
    except OSError as msg:
        s.close()
        s=None
        continue
    break
if s is None:
    print('could not open socket')
    sys.exit(1)
with s:
    s.sendall(b'Hello,world')
    data=s.recv(1024)
print('Received',repr(data))