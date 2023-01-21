import socket
from _thread import *
import sys

server = "10.0.65.5"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")

def ask():
    name = input("What is the player's name: ")
    print(f"Ok, {name}. \n WELCOME TO 21 DARES")
    return name


def threaded_client(conn):
    # Ask For name
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            print(reply)

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)

            conn.sendall(str.encode(reply))
        except:
            print("Begining Game")

    print("Lost connection")
    conn.close()


while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    name = conn.send(str.encode(ask()))

    start_new_thread(threaded_client, (conn,))
