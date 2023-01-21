import socket
from _thread import *
import sys
import os

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
    conn.send("Connected") # Converts string to binary
    reply = ""
    while True:
        try:
            data = conn.recv(2048*2)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

                conn.sendall(str.encode(reply))

        except:
            pass

    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))
