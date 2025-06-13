# -*- coding: utf-8 -*-
"""
Created on Fri Jan 10 10:38:40 2025

@author: DELL
"""

import tkinter  as tk 
from tkinter import * 
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
root.title("Malicious Application")
root.configure(background="#FFFFFF")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("1400x900")

img = Image.open("E:/2024-2025 New Code/Malicious Detection/100%_code_malicious_detection/logo.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)

image2 =Image.open('slide3.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)

def welcome():
    from subprocess import call
    call(["python", "GUI_main.py"])

label1=tk.Label(root, text="'Welcome To Malicious Application Detection'", font=('times', 25,' bold '), height=1, width=75,bg="#000000",fg="#FFFFFF")
label1.place(x=0, y=0)


button1 = tk.Button(root, text="Lets begin",command=welcome,width=15,height=1,bd=5,bg='#FFFFFF',fg='#004225',font=('times', 20, ' bold '),)
button1.place(x=550,y=350)

root.mainloop()