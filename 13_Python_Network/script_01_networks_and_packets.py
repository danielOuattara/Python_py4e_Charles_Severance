import socket

# print(help(socket))

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(my_sock)
my_sock.connect(("data.pr4e.org", 80))
