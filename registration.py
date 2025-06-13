import tkinter as tk
# from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re



window = tk.Tk()
window.geometry("700x700")
window.title("REGISTRATION FORM")
window.configure(background="#C3FDB8")
img = Image.open("E:/2024-2025 New Code/Malicious Detection/100%_code_malicious_detection/logo.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
window.iconphoto(False, photo)

Fullname = tk.StringVar()
address = tk.StringVar()
username = tk.StringVar()
Email = tk.StringVar()
Phoneno = tk.IntVar()
var = tk.IntVar()
age = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()
policeno = tk.IntVar()


# database code
db = sqlite3.connect('evaluation.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS admin_registration"
               "(Fullname TEXT, address TEXT, username TEXT, Email TEXT, Phoneno TEXT,Gender TEXT,age TEXT , password TEXT)")
db.commit()



def password_check(passwd): 
	
	SpecialSym =['$', '@', '#', '%'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 20: 
		print('length should be not be greater than 8') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 

def insert():
    fname = Fullname.get()
    addr = address.get()
    un = username.get()
    email = Email.get()
    mobile = Phoneno.get()
    gender = var.get()
    time = age.get()
    pwd = password.get()
    cnpwd = password1.get()
    with sqlite3.connect('evaluation.db') as db:
        c = db.cursor()

    # Find Existing username if any take proper action
    find_user = ('SELECT * FROM admin_registration WHERE username = ?')
    c.execute(find_user, [(username.get())])

    # else:
    #   ms.showinfo('Success!', 'Account Created Successfully !')

    # to check mail
    #regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        a = True
    else:
        a = False
    # validation
    if (fname.isdigit() or (fname == "")):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "please enter valid name")
    elif (addr == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter Address")
    elif (email == "") or (a == False):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif ((time > 100) or (time == 0)):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid age")
    elif (c.fetchall()):
        ms.showerror('Error!', 'Username Taken Try a Diffrent One.')
    elif (pwd == ""):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Please Enter valid password")
    elif (var == False):
        ms.showinfo("Message", "Please Enter gender")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "password must contain atleast 1 Uppercase letter,1 symbol,1 number")
    elif (pwd != cnpwd):
        ms.showerror("showerror", "Error")
        ms.showinfo("Message", "Password Confirm password must be same")
    else:
        conn = sqlite3.connect('evaluation.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO admin_registration(Fullname, address, username, Email, Phoneno, Gender, age , password) VALUES(?,?,?,?,?,?,?,?)',
                (fname, addr, un, email, mobile, gender, time, pwd))

            conn.commit()
            db.close()
            ms.askquestion("askquestion", "Are you sure?")
            ms.askokcancel("askokcancel", "Want to continue?")
            ms.showinfo('Success!', 'Account Created Successfully !')
            
            from subprocess import call
            call(["python", "login.py"])
            
            window.destroy()

#####################################################################################################################################################
frame = tk.LabelFrame(window,width=550, height=500, bd=5, font=('times', 14, ' bold '),bg="#C3FDB8")
frame.grid(row=0, column=0, sticky='nw')
frame.place(x=70, y=50)
        
            



l1 = tk.Label(window, text="Create Your Account Here!! ", font=("Times new roman", 25, "bold"), bg="#C3FDB8", fg="#000000")
l1.place(x=120, y=0)

# that is for label1 registration

l2 = tk.Label(frame, text="Enter Your Name:", width=16, font=("Times new roman", 15, "bold"), bg="#C3FDB8")
l2.place(x=50, y=30)
t1 = tk.Entry(frame, textvar=Fullname, width=20,bd=3, font=('', 15))
t1.place(x=250, y=30)
# that is for label 2 (full name)


l3 = tk.Label(frame, text="Enter Your Address:", width=16, font=("Times new roman", 15, "bold"), bg="#C3FDB8")
l3.place(x=50, y=70)
t2 = tk.Entry(frame, textvar=address, width=20,bd=3, font=('', 15))
t2.place(x=250, y=70)
# that is for label 3(address)


# that is for label 4(blood group)

l5 = tk.Label(frame, text="Enter Your Email-ID:", width=16, font=("Times new roman", 15, "bold"), bg="#C3FDB8")
l5.place(x=50, y=110)
t4 = tk.Entry(frame, textvar=Email, width=20,bd=3, font=('', 15))
t4.place(x=250, y=110)
# that is for email address

l6 = tk.Label(frame, text="Enter Your Phone-no:", width=16, font=("Times new roman", 15, "bold"), bg="#C3FDB8")
l6.place(x=50, y=150)
t5 = tk.Entry(frame, textvar=Phoneno, width=20,bd=3, font=('', 15))
t5.place(x=250, y=150)
# phone number
l7 = tk.Label(frame, text="Enter Your Gender:", width=16, font=("Times new roman", 15, "bold"), bg="#C3FDB8")
l7.place(x=50, y=190)
# gender
tk.Radiobutton(frame, text="Male", padx=5, width=5, bg="#C3FDB8", font=("Times new roman", 15, "bold"), variable=var, value=1).place(x=250,y=190)
tk.Radiobutton(frame, text="Female", padx=20, width=4,bg="#C3FDB8", font=("Times new roman", 15, "bold"), variable=var, value=2).place(x=350, y=190)

l8 = tk.Label(frame, text="Enter Your Age:", width=16, font=("Times new roman", 15, "bold"), bg="#C3FDB8")
l8.place(x=50, y=230)
t6 = tk.Entry(frame, textvar=age, width=20,bd=3, font=('', 15))
t6.place(x=250, y=230)

l4 = tk.Label(frame, text="Enter Your Username:", width=16, font=("Times new roman", 15, "bold"), bg="#C3FDB8")
l4.place(x=50, y=270)
t3 = tk.Entry(frame, textvar=username, width=20,bd=3, font=('', 15))
t3.place(x=250, y=270)

l9 = tk.Label(frame, text="Enetr Your Password:", width=16, font=("Times new roman", 15, "bold"), bg="#C3FDB8")
l9.place(x=50, y=310)
t9 = tk.Entry(frame, textvar=password, width=20,bd=3, font=('', 15), show="*")
t9.place(x=250, y=310)

l10 = tk.Label(frame, text="Re-Confirm Password:", width=16, font=("Times new roman", 15, "bold"), bg="#C3FDB8")
l10.place(x=50, y=350)

t10 = tk.Entry(frame, textvar=password1, width=20,bd=3, font=('', 15), show="*")
t10.place(x=250, y=350)

btn = tk.Button(frame, text="SUBMIT", bg="green",font=("times",20),fg="white", width=9, height=0, command = insert)
btn.place(x=180, y=400)

#btn = tk.Button(window, text="login", bg="#192841",font=("",20),fg="white", width=9, height=0, command=login)
#btn.place(x=350, y=600)
# tologin=tk.Button(window , text="Go To Login", bg ="dark green", fg = "white", width=15, height=2, command=login)
# tologin.place(x=330, y=600)
window.mainloop()