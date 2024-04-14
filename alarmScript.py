# this is a script to trigger the alarm when the model finds the driver being drowsy
# needed to integrated into the RunModel.py file and tested
  
import tkinter as tk
import customtkinter as ctk
import torch
import numpy as np
import cv2
from PIL import Image, ImageTk
import vlc
import wave

app = tk.Tk()
app.geometry("600x600")
app.title("Drowsiness Detection Testing")
ctk.set_appearance_mode("dark")

vidFrame = tk.Frame(height=480, width=600)
vidFrame.pack()
vid = ctk.CTkLabel(vidFrame)
vid.pack()


model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp9/weights/last.pt', force_reload = True)
cap = cv2.VideoCapture(3)

def detect():
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = model(frame)
    img = np.squeeze(results.render())

    if len(results.xywh[0]) > 0:
        dconf = results.xywh[0][0][4]
        dclass = results.xywh[0][0][5]

        if dconf.item() > 0.75 and dclass.item() == 1.0:
            p = vlc.mediaPlayer(f"file:/wake_up.mp3")
            p.load()
            p.play()

            # call_playAudio.py()


    imgarr = Image.fromarray(frame)
    imgtk = ImageTk.PhotoImage(imgarr)
    vid.imgtk = imgtk
    vid.configure(image = imgtk) 
    vid.after(10, detect)

detect()
app.mainloop()
