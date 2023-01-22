import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = '10.0.65.8'
port = 12345
s.bind((host, port))

s.listen(1)

client, address = s.accept()

client.sendall(str.encode("Kanav says hi"))