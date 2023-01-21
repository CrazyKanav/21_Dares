import socket
from tkinter import *

def on_select(v):
    s.sendall(v.get().encode())
    
def on_submit():
    global current_dare
    current_dare = dare_var.get()
    dare_var.set("")
    dare_label.config(text="Dare: "+current_dare)
    
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
host = '127.0.0.1'
port = 12345
s.connect((host, port))

print('Connected to the server')

root = Tk()
root.geometry("300x200")

dare_var = StringVar()
dare_var.set("")
dare_label = Label(root, text="Dare:")
dare_label.pack()

completed_var = StringVar()
completed_var.set("completed")
completed_rb = Radiobutton(root, text="Completed", variable=completed_var, value="completed", command=lambda: on_select(completed_var))
completed_rb.pack()

failed_var = StringVar()
failed_var.set("failed")
failed_rb = Radiobutton(root, text="Failed", variable=failed_var, value="failed", command=lambda: on_select(failed_var))
failed_rb.pack()

submit_button = Button(root, text="Submit", command=on_submit)
submit_button.pack()

score_label = Label(root, text="Score: 0")
score_label.pack()

current_dare = ""
score = 0

while True:
    dare = s.recv(1024).decode()
    if dare == "Your final score is":
        break
    current_dare = dare
    dare_label.config
