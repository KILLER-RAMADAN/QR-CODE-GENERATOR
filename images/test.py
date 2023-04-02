import pyqrcode
from pyqrcode import create
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from PIL import Image 
import PIL 
import os


home_directory = os.path.expanduser( '~' )
print( home_directory )
  
#_______________________________________
def simple_qr_code():
 window2 = tk.Tk()
 window2.resizable(0,0)
 window2.geometry("800x500+400+100")   
 window2.title("AOU_QRCODE_GENERATOR")  
 window2.iconbitmap('app-photos/qr.ico')
 window2.attributes('-topmost', True)
 #main compononts....
 user_link=tk.Entry(window2,font=("Arial",15,"bold"),bg='white',width=45)
 user_link.place(x=130,y=60)
 button1=tk.Button(window2,font=("Arial",10,"bold"),height=1,width=18,text='Make Qr_Code',fg="white",background="#0F115B",bd=0,activebackground="green",command=lambda:my_generate_2())
 button1.place(x=635,y=60)
 button2=tk.Button(window2,font=("Arial",10,"bold"),height=1,width=18,text='Clear',fg="white",background="red",activebackground="red",bd=0,command=lambda:clear())
 button2.place(x=635,y=100)
 Label0=tk.Label(window2,text='INPUT HERE:',fg="black",font=("Bakbak One",15,"bold"))
 Label0.place(x=0,y=60)
 Label3=tk.Label(window2)
 Label3.pack(side="left")
 Frame(window2,width=800,height=50,bg="black").place(x=0,y=450)
 Frame(window2,width=800,height=50,bg="black").place(x=0,y=0)
 Label(window2,text="QR-CODE-GENERATOR",fg="white",bg="black",font=("Amiri",20,"bold")).place(x=245,y=10)
 Frame(window2,width=800,height=50,bg="#0F115B").place(x=0,y=700)
 Label(window2,text="Copyright © 'RAMADAN' 2023 All Rights Reserved.",fg="white",bg="black",font=("Bakbak One",10,"bold")).place(x=270,y=450)
#_______________________________________
 def my_generate_2():
    global my_img
    if user_link.get()=="":
      messagebox.showinfo("ENTER LINK","PLEASE INPUT LINK...",parent=window2)
    else:
     my_qr = pyqrcode.create(f"{user_link.get()}") 
     my_qr.png('main-qrcode/test.png', scale=5, module_color=[0, 0, 0, 128], background=[0xff, 0xcc, 0xcc])
     my_qr = my_qr.xbm(scale=5)
     my_img=tk.BitmapImage(data=my_qr)
     Label3.config(image=my_img)
     img = Image.open(f"{home_directory}\\images\\main-qrcode\\test.png") 
     img = img .save(f"{home_directory}//images//outputs-qrcode//{user_link.get()[6:20]}-qr-code.png")
 def clear():
   clear=user_link.delete(0,100)
   return clear 
 window2.mainloop()
simple_qr_code()