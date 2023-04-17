import pyqrcode
from pyqrcode import create
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from PIL import Image 
import PIL 
import os
from tkinter import filedialog

home_directory = os.path.expanduser( '~' )
print( home_directory )
  

  
  
#_______________________________________
def simple_qr_code():
 global user_location
 global file_locate
 def file_location():
  global file_locate
  global user_location
 
  file_locate=filedialog.askdirectory(initialdir=os.getcwd())
  user_location.configure(state=NORMAL)
  user_location.delete(0,1000)
  user_location.insert(0,file_locate)
  user_location.configure(state=DISABLED)
 
 
 
 
 window2 = tk.Tk()
 window2.resizable(0,0)
 window2.geometry("800x500+400+100")   
 window2.title("AOU_QRCODE_GENERATOR")  
 window2.iconbitmap('app-photos/qr.ico')
 window2.attributes('-topmost', True)
 #main compononts....
 user_link1=tk.Entry(window2,font=("Arial",15,"bold"),bg='white',width=45)
 user_link1.place(x=140,y=60)
 user_link2=tk.Entry(window2,font=("Arial",15,"bold"),bg='white',width=45)
 user_link2.place(x=140,y=140)
 user_location=tk.Entry(window2,font=("Arial",15,"bold"),bg='white',width=45)
 user_location.place(x=140,y=100)
 user_location.configure(state=DISABLED)
 button1=tk.Button(window2,font=("Arial",10,"bold"),height=1,width=18,text='Make Qr_Code',fg="white",background="#0F115B",bd=0,activebackground="#0F115B",command=lambda:my_generate_2())
 button1.place(x=645,y=60)
 button2=tk.Button(window2,font=("Arial",10,"bold"),height=1,width=18,text='Clear',fg="white",background="red",activebackground="red",bd=0,command=lambda:clear())
 button2.place(x=645,y=140)
 button3=tk.Button(window2,font=("Arial",10,"bold"),height=1,width=18,text='location',fg="white",background="green",activebackground="green",bd=0,command=lambda:file_location())
 button3.place(x=645,y=100)
 Label0=tk.Label(window2,text='LINK HERE:',fg="black",font=("Bakbak One",15,"bold"))
 Label0.place(x=0,y=60)
 Label1=tk.Label(window2,text='QR-NAME:',fg="black",font=("Bakbak One",15,"bold"))
 Label1.place(x=0,y=140)
 Label2=tk.Label(window2,text='LOCATION:',fg="black",font=("Bakbak One",15,"bold"))
 Label2.place(x=0,y=100)
 Label3=tk.Label(window2)
 Label3.place(x=280,y=170)
 Frame(window2,width=800,height=50,bg="black").place(x=0,y=450)
 Frame(window2,width=800,height=50,bg="black").place(x=0,y=0)
 Label(window2,text="QR-CODE-GENERATOR",fg="white",bg="black",font=("Amiri",20,"bold")).place(x=245,y=10)
 Frame(window2,width=800,height=50,bg="#0F115B").place(x=0,y=700)
 Label(window2,text="Copyright © 'RAMADAN' 2023 All Rights Reserved.",fg="white",bg="black",font=("Bakbak One",10,"bold")).place(x=270,y=450)
#_______________________________________
 def my_generate_2():
    global file_locate
    global my_img
    link="https:"
    if link not in user_link1.get():
      messagebox.showinfo("ENTER LINK","PLEASE INPUT CORRECT LINK...",parent=window2)
    elif user_link2.get()=="":
      messagebox.showinfo("ENTER NAME","PLEASE INPUT QR-CODE NAME...",parent=window2)
    elif user_location.get()=="":
      messagebox.showinfo("ENTER NAME","PLEASE INPUT YOUR LOCATION TO SAVE...",parent=window2)
    else:
     try:
      my_qr = pyqrcode.create(f"{user_link1.get()}") 
      my_qr.png('main-qrcode/test.png', scale=5, module_color=[0, 0, 0, 128], background=[0xff, 0xcc, 0xcc])
      my_qr = my_qr.xbm(scale=5)
      my_img=tk.BitmapImage(data=my_qr)
      Label3.config(image=my_img)
      img = Image.open(f"main-qrcode\\test.png") 
      img = img .save(f"{file_locate}//{user_link2.get().upper()}-QR-CODE.png")
      messagebox.showinfo("QR-CODE","QR-CODE CREATED SUCCESSFULLY..",parent=window2)
     except:
       messagebox.showerror("ERROR","1)WRONG FILE LOCATION")
 def clear():
   clear1=user_link1.delete(0,100) 
   clear2=user_link2.delete(0,100)
   clear3=user_location.delete(0,100)
   Label3.config(text="QR-CODE-AHMED RAMADAN.",font=("Bakbak One",25,"bold"))
   return clear1 ,clear2 ,clear3
 window2.mainloop()
simple_qr_code()
