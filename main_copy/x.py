import socket
from _thread import *
import sys

server = '10.0.65.5'
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port)) # Assigns ip address to socket
except socket.error as e:
    str(e)

s.listen(3)
print("Waiting for a connection, Server Started")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    name = conn.recv(2048)
    print(name)
    conn.send(str.encode("Hi, {name}"))

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))