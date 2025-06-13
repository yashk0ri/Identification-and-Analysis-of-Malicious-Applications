from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
root = tk.Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Malicious Application Prediction")
root.configure(background="white")
img = Image.open("E:/2024-2025 New Code/Malicious Detection/100%_code_malicious_detection/logo.ico")  # Replace with your image path
if img.size != (32, 32):
    img = img.resize((32, 32), Image.LANCZOS)
photo = ImageTk.PhotoImage(img)
root.iconphoto(False, photo)

def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    
    
    
    
    tele_device = tk.IntVar()
    tele_subscriber = tk.IntVar()
    abort = tk.IntVar()
    sendsms = tk.IntVar()
    delete_pack = tk.IntVar()
    sms_received = tk.IntVar()
    ljava = tk.IntVar()
    phone_s= tk.IntVar()
    readsms = tk.IntVar()
    boot_comp = tk.IntVar()
    io_delete = tk.IntVar()
    chown = tk.IntVar()
    chmod = tk.IntVar()
    mount = tk.IntVar()
    apk = tk.IntVar()
    zip_file = tk.IntVar()
    dex_file= tk.IntVar()
    camera = tk.IntVar()
    access = tk.IntVar()
    package = tk.IntVar()
    battery_low = tk.IntVar()
    so_file = tk.IntVar()
    power_connec = tk.IntVar()
    load_lib = tk.IntVar()
    exe_file = tk.IntVar()
    
    #===================================================================================================================
    def Detect():
        e1=tele_device.get()
        print(e1)
        e2=tele_subscriber.get()
        print(e2)
        e3=abort.get()
        print(e3)
        #print(type(e3))
        e4=sendsms.get()
        print(e4)
        e5=delete_pack.get()
        print(e5)
        e25=phone_s.get()
        print(e5)
        e6=sms_received.get()
        print(e6)
        e7=ljava.get()
        print(e7)
        e8=readsms.get()
        print(e8)
        e9=boot_comp.get()
        print(e9)
        e10=io_delete.get()
        print(e10)
        e11=chown.get()
        print(e11)
        e12=chmod.get()
        print(e12)
        e13=mount.get()
        print(e13)
    
        e14=apk.get()
        print(e14)
        e15=zip_file.get()
        print(e15)
        e16=dex_file.get()
        print(e16)    
        e17=camera.get()
        print(e17)
        e18=access.get()
        print(e18)
        e19=package.get()
        print(e19)
        e20=battery_low.get()
        print(e20)
        
        e21=so_file.get()
        print(e21)
        e22=power_connec.get()
        print(e22)
        e23=load_lib.get()
        print(e23)
        e24=exe_file.get()
        print(e24)

        
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('malicious_MODEL.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5,e25, e6, e7, e8, e9,e10, e11, e12, e13,e14, e15, e16, e17, e18, e19, e20, e21, e22,e23, e24]])
        print(v)
        if v[0]==1:
            print("Yes")
            yes = tk.Label(root,text="Malicious Application Predicted",background="white",foreground="red",font=('times', 18, ' bold underline '),width=35)
            yes.place(x=350,y=600)
                     
        else:
            print("No")
            no = tk.Label(root, text="No Malicious Application Predicted", background="white", foreground="green",font=('times', 18, 'bold underline '),width=35)
            no.place(x=350, y=600)
            

    frame_alpr = tk.LabelFrame(root, text=" --Prediction-- ", width=1100, height=600, bd=5, font=('times', 14, ' bold '),bg="#81D8D0",fg="#FFFFFF")
    frame_alpr.grid(row=0, column=0, sticky='nw')
    frame_alpr.place(x=50, y=0) 
    
    l1=tk.Label(frame_alpr,text="Telephony Get Device ID ",bg="#81D8D0",font=('times', 16, ' bold '),width=25)
    l1.place(x=0,y=30)
    tele_device=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=tele_device)
    tele_device.place(x=310,y=30)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=30)

    l2=tk.Label(frame_alpr,text="Telephony Get Subscriber ID",bg="#81D8D0",font=('times', 16, ' bold '),width=25)
    l2.place(x=0,y=70)
    tele_subscriber=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=tele_subscriber)
    tele_subscriber.place(x=310,y=70)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=70)

    l3=tk.Label(frame_alpr,text="Abort Broadcast",bg="#81D8D0",font=('times', 16, ' bold '),width=15)
    l3.place(x=50,y=110)
    abort=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=abort)
    abort.place(x=310,y=110)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=110)
    
    l4=tk.Label(frame_alpr,text="Send SMS",bg="#81D8D0",font=('times', 16, ' bold '),width=15)
    l4.place(x=50,y=150)
    sendsms=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sendsms)
    sendsms.place(x=310,y=150)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=150) 
    
    l5=tk.Label(frame_alpr,text="Delete Packages",bg="#81D8D0",font=('times', 16, ' bold '),width=15)
    l5.place(x=50,y=190)
    delete_pack=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=delete_pack)
    delete_pack.place(x=310,y=190)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=190)

    l6=tk.Label(frame_alpr,text="Phone_State",bg="#81D8D0",font=('times', 16, ' bold '),width=15)
    l6.place(x=50,y=230)
    phone_s=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=phone_s)
    phone_s.place(x=310,y=230)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=230)

    l7=tk.Label(frame_alpr,text="SMS_Received",bg="#81D8D0",font=('times', 16, ' bold '),width=15)
    l7.place(x=50,y=270)
    sms_received=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=sms_received)
    sms_received.place(x=310,y=270)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=270)

    l8=tk.Label(frame_alpr,text="Socket Address",bg="#81D8D0",font=('times', 16, ' bold '),width=15)
    l8.place(x=50,y=310)
    ljava=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=ljava)
    ljava.place(x=310,y=310)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=310)

    l9=tk.Label(frame_alpr,text="Read_SMS",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l9.place(x=50,y=350)
    readsms=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=readsms)
    readsms.place(x=310,y=350)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=350)

    l10=tk.Label(frame_alpr,text="Boot Completed",bg="#81D8D0",font=('times',16, ' bold '),width=15)
    l10.place(x=50,y=390)
    boot_comp=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=boot_comp)
    boot_comp.place(x=310,y=390)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=390)

    l11=tk.Label(frame_alpr,text="IO.File.*delete",bg="#81D8D0",font=('times', 16, ' bold '),width=15)
    l11.place(x=50,y=430)
    io_delete=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=io_delete)
    io_delete.place(x=310,y=430)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=430)

    l12=tk.Label(frame_alpr,text="Chown",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l12.place(x=50,y=470)
    chown=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=chown)
    chown.place(x=310,y=470)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=400,y=470)
##################################################################################################################
    l13=tk.Label(frame_alpr,text="Chmod",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l13.place(x=600,y=30)
    chmod=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=chmod)
    chmod.place(x=850,y=30)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=30)

    l14=tk.Label(frame_alpr,text="Mount",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l14.place(x=600,y=70)
    mount=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=mount)
    mount.place(x=850,y=70)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=70)
    
    l15=tk.Label(frame_alpr,text=".APK",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l15.place(x=600,y=110)
    apk=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=apk)
    apk.place(x=850,y=110)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=110)
    
    l16=tk.Label(frame_alpr,text=".ZIP",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l16.place(x=600,y=150)
    zip_file=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=zip_file)
    zip_file.place(x=850,y=150)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=150)
    
    l17=tk.Label(frame_alpr,text=".DEX",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l17.place(x=600,y=190)
    dex_file=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=dex_file)
    dex_file.place(x=850,y=190)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=190)
    
    l18=tk.Label(frame_alpr,text="Camera",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l18.place(x=600,y=230)
    camera=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=camera)
    camera.place(x=850,y=230)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=230)
     
    l19=tk.Label(frame_alpr,text="Access Fine Location",bg="#81D8D0",font=('times', 16, ' bold '),width=16)
    l19.place(x=600,y=270)
    access=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=access)
    access.place(x=850,y=270)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=270)
    
    l20=tk.Label(frame_alpr,text="Install Packages",bg="#81D8D0",font=('times', 16, ' bold '),width=15)
    l20.place(x=600,y=310)
    package=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=package)
    package.place(x=850,y=310)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=310)
    
    l21=tk.Label(frame_alpr,text="Battery Low",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l21.place(x=600,y=350)
    battery_low=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=battery_low)
    battery_low.place(x=850,y=350)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=350)
    
    l22=tk.Label(frame_alpr,text=".SO",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l22.place(x=600,y=390)
    so_file=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=so_file)
    so_file.place(x=850,y=390)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=390)
    
    l23=tk.Label(frame_alpr,text="Power Connected",bg="#81D8D0",font=('times', 16, ' bold '),width=15)
    l23.place(x=600,y=430)
    power_connec=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=power_connec)
    power_connec.place(x=850,y=430)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=430)
    
    l24=tk.Label(frame_alpr,text="System Load Library",bg="#81D8D0",font=('times', 16, ' bold '),width=15)
    l24.place(x=600,y=470)
    load_lib=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=load_lib)
    load_lib.place(x=850,y=470)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=470)
    
    l25=tk.Label(frame_alpr,text=".EXE",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l25.place(x=600,y=510)
    exe_file=tk.Entry(frame_alpr,bd=2,width=5,font=("TkDefaultFont", 20),textvar=exe_file)
    exe_file.place(x=850,y=510)
    l1=tk.Label(frame_alpr,text="Value(0/1) ",bg="#81D8D0",font=('times', 16, ' bold '),width=10)
    l1.place(x=950,y=510)
    
    def window():
        root.destroy()
        
    button1 = tk.Button(root,text="Submit",command=Detect,bd=5,font=('times', 15, ' bold '),width=10,height="1",bg="#008000",fg="#FFFFFF")
    button1.place(x=1150,y=230)
    
    button5 = tk.Button(root, text="Exit", command=window,bd=5, width=10, height=1, font=('times', 15, ' bold '),bg="#FF0000",fg="#FFFFFF")
    button5.place(x=1150, y=650)
   
    root.mainloop()

Train()