import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import cv2

root = tk.Tk()
root.title("Dare Challenge")
# Create a label for the video
video_label = tk.Label(root)
video_label.pack()

# Create a label for the caption
caption_label = tk.Label(root, text="Doing a dare...")
caption_label.pack()

# Create a button to stop the video recording
stop_button = tk.Button(root, text="Stop Recording", command=root.destroy)
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
    root.after(30, update_frame)

# Start updating the frame
update_frame()

root.mainloop()
