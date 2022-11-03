""" A simple web browser """

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

my_sock.close()
