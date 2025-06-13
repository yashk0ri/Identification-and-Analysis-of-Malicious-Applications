import tkinter  as tk 
from tkinter import * 
from PIL import Image # For face recognition we will the the LBPH Face Recognizer 
from PIL import Image , ImageTk  

root = tk.Tk()
root.configure(background="seashell2")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("GUI_main")
img = Image.open("E:/2024-2025 New Code/Malicious Detection/100%_code_malicious_detection/logo.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)
#------------------Frame----------------------



#-------function------------------------

def reg():
    
##### tkinter window ######
    
    print("reg")
    from subprocess import call
    call(["python", "registration.py"])   



def login():
    
##### tkinter window ######
    
    print("log")
    from subprocess import call
    call(["python", "login.py"])   
    


def window():
    root.destroy()

#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('m1.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)


lbl = tk.Label(root, text="Malicious Application Detection", font=('times', 30,' bold '), height=1, width=65,bg="#000000",fg="#FFFFFF")
lbl.place(x=0, y=0)


button1 = tk.Button(root, text='Sign-In',command=login,width=15,height=1,bd=5,font=('times', 18, ' bold '),bg='#0000FF',fg='#FFFFFF')
button1.place(x=1100,y=50)
button2 = tk.Button(root, text='Sign-Up',command=reg,width=15,height=1,bd=5,font=('times', 18, ' bold '),bg='#056608',fg='#FFFFFF')
button2.place(x=1100,y=100)
exit = tk.Button(root, text="Logout", command=window, width=15, height=1, bd=5,font=('times', 18, ' bold '),bg="#FF0000",fg="#FFFFFF")
exit.place(x=1100, y=150)

root.mainloop()
