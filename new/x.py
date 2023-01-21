import tkinter as tk

def increment(num):
    global count
    count += num
    update_count()

def update_count():
    label.config(text="Count: "+str(count))

root = tk.Tk()
count = 0

label = tk.Label(root, text="Count: 0")
label.pack()

button1 = tk.Button(root, text="Increment 1", command=lambda: increment(1))
button1.pack()

button2 = tk.Button(root, text="Increment 2", command=lambda: increment(2))
button2.pack()

button3 = tk.Button(root, text="Increment 3", command=lambda: increment(3))
button3.pack()

root.mainloop()
