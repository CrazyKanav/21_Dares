import socket
import tkinter as tk
from tkinter import *

# Create a socket object
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Connect to the server
# host = '10.0.65.5'
# port = 12345
# s.connect((host, port))

print('Connected to the server')

def get_name():
    name = name_entry.get()
    name_label.config(text=f"Hello, {name}!")
    dare_label.config(text="Dare 1: Sing a song in public.")
    dare_number = 1


def get_name():
    name = name_entry.get()
    name_label.config(text=f"Hello, {name}!")
    dare_label.config(text="Dare 1: Sing a song in public.")
    dare_number = 1

def next_dare():
    global dare_number
    dare_number += 1
    dare_label.config(text=f"Dare {dare_number}: Eat a spoonful of hot sauce.")

root = tk.Tk()
root.title("21 Dares")

name_label = tk.Label(root, text="What is your name?")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

get_name_button = tk.Button(root, text="Submit", command=get_name)
get_name_button.pack()

dare_label = tk.Label(root, text="")
dare_label.pack()

next_dare_button = tk.Button(root, text="Next Dare", command=next_dare)
next_dare_button.pack()

root.mainloop()

# Close the socket
s.close()
