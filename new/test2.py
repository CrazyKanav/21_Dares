import tkinter as tk
from tkinter import *
import time 
from PIL import Image, ImageTk
import cv2

root3 = Tk()
root3.title("21 Dares")
canvas3 = Canvas(root3, height=500, width=795)
video_label = tk.Label(root3)
video_label.pack()

# Create a label for the caption
caption_label = tk.Label(root3, text="Doing a dare...")
caption_label.pack()

# Create a button to stop the video recording
stop_button = tk.Button(root3, text="Stop Recording", command=root3.destroy)
stop_button.pack()

# Start the video capture
cap = cv2.VideoCapture(0)
cap.set(3, 700)
cap.set(4, 420)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))

def update_frame():
    # Read the current frame from the video capture
    ret, frame = cap.read()
    out.write(frame)
    # Convert the frame to a PhotoImage object
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame)
    frame = ImageTk.PhotoImage(frame)

    # Update the video label with the current frame
    video_label.config(image=frame)
    video_label.image = frame

    # Schedule the next frame update
    root3.after(30, update_frame)

# Start updating the frame
update_frame()


dare_txt_lb=tk.Label(root3,font=('Arial',20),fg='black',text="What dare do you want to give?").place(x=30, y=190)

dare_txt=Entry(root3,fg='black',bg='palegreen1',font=('Arial',20)).place(x=50, y=230)
lb_done = tk.Label(root3,text="Did you do the dare?",font=('Arial',20),foreground='sea green')
lb_done.pack()
bt_done = tk.Button(root3,text="Yes",font=('Calibri',25),foreground='black',background="lemon chiffon")
bt_done.pack()

root3.mainloop()