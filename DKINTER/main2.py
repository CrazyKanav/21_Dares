import tkinter as tk
from tkinter import *
root = Tk()
root.title("21 Dares")
root.geometry("800x600")
w= root.winfo_screenwidth()               
h= root.winfo_screenheight()  
C = tk.Canvas(root, height=w, width=h)
arc = C.create_rectangle(100,50,340,210)

C.pack()
root.mainloop()