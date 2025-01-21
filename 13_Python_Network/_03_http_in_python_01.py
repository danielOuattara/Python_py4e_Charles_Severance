""" A simple web browser

socket
connect
send
receive
close
"""

import socket

# print(help(socket))

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(("data.pr4e.org", 80))

req = "GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n"
req_encoded = req.encode()
my_sock.send(req_encoded)

while True:
    data = my_sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())


print('--------------------------------------------------------------')


my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(("www.dr-chuck.com", 80))

req_2 = "GET http://www.dr-chuck.com/page1.htm HTTP/1.0\r\n\r\n".encode()
my_sock.send(req_2)

while True:
    data = my_sock.recv(512)
    if len(data) < 1:
        break
    print(data.decode())
my_sock.close()
