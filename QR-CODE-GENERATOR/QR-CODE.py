import pyqrcode
from pyqrcode import create
import tkinter as tk
from tkinter import * 
from tkinter import messagebox
from PIL import Image ,ImageTk
import PIL 
import os
from tkinter import filedialog
import smtplib
from email.message import EmailMessage
import imghdr

home_directory = os.path.expanduser( '~' )
print( home_directory )
#_______________________________________
def simple_qr_code():
 global user_location
 global file_locate
 global send_qrcode
 
 
 def file_location():
  global file_locate
  global user_location
 
  file_locate=filedialog.askdirectory(initialdir=os.getcwd())
  user_location.configure(state=NORMAL)
  user_location.delete(0,1000)
  user_location.insert(0,file_locate)
  user_location.configure(state=DISABLED)
 def pass_enter(e):
    send_qrcode_entry.delete(0,"end")
 def pass_leave(e):
    if send_qrcode_entry.get()=="":
        send_qrcode_entry.insert(0,"Enter MAIL")   
      
        
 def send_qrcode_to_gmail():
  basic="Enter Email"
  basic_email="gmail.com"
  if basic in send_qrcode_entry.get():
    messagebox.showinfo("Error","Enter Mail....")
  elif basic_email not in send_qrcode_entry.get():
    messagebox.showinfo("Error","Enter Cotrrect Mail....")
  elif  send_qrcode_entry.get()=="":
    messagebox.showinfo("Error","Enter Mail To Send Qr-code....")
  else:
   try:
    user="sendqrcodetest@gmail.com"
    password="aznldnjsvjanilxs"
    msg=EmailMessage()
    msg["Subject"]="Welcome We all happy to use our program"
    msg["To"]=send_qrcode_entry.get()
    msg['From']=user
    msg.set_content("Scan Qr-Code or Save it")
    with open(f"{user_location.get()}//{get_name.get()}.png","rb") as f:
     file_data=f.read()
     file_name=get_name.get()
     file_type=imghdr.what(f.name)
    msg.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name,)
    with smtplib.SMTP("smtp.gmail.com",587) as smtp:
     smtp.starttls()
     smtp.login(user,password)
     smtp.send_message(msg)
     messagebox.showinfo("Congratulations","Qr-code Successfully Sending....")
   except:
     messagebox.showerror("Error","1)Plaese Excute Your Qr-Code First\n\n2)Then Sending Your Qr-Code ")
 window2 = tk.Tk()
 window2.resizable(0,0)
 window2.geometry("800x600+400+100")   
 window2.title("Qr-Code")  
 window2.iconbitmap('app-photos/qr.ico')
 window2.attributes('-topmost', True)
 window2.configure(bg="#121212")
 #main compononts....
 user_link1=tk.Entry(window2,font=("Arial",15,"bold"),bg='white',width=45)
 user_link1.place(x=140,y=60)
 insert_link=user_link1.clipboard_get()
 user_link1.insert(0,insert_link)
 get_name=tk.Entry(window2,font=("Arial",15,"bold"),bg='white',width=45)
 get_name.place(x=140,y=140)
 user_location=tk.Entry(window2,font=("Arial",15,"bold"),bg='white',width=45)
 user_location.place(x=140,y=100)
 user_location.configure(state=DISABLED)
 button1=tk.Button(window2,font=("Arial",10,"bold"),height=1,width=18,text='Make Qr_Code',relief="groove",fg="#8E44AD",background="#121212",activeforeground="#8E44AD",activebackground="#121212",command=lambda:my_generate_2())
 button1.place(x=645,y=60)
 button2=tk.Button(window2,font=("Arial",10,"bold"),height=1,width=18,text='Clear',fg="#8E44AD",relief="groove",background="#121212",activeforeground="#8E44AD",activebackground="#121212",command=lambda:clear())
 button2.place(x=645,y=140)
 button3=tk.Button(window2,font=("Arial",10,"bold"),height=1,width=18,text='location',fg="#8E44AD",relief="groove",background="#121212",activeforeground="#8E44AD",activebackground="#121212",command=lambda:file_location())
 button3.place(x=645,y=100)
 button4=tk.Button(window2,font=("Arial",10,"bold"),height=1,width=18,text='Send Qr-Code',fg="#8E44AD",relief="groove",background="#121212",activeforeground="#8E44AD",activebackground="#121212",command=lambda:send_qrcode_to_gmail())
 button4.place(x=645,y=220)
 Label0=tk.Label(window2,text='Input Link:',fg="white",bg="#121212",font=("Bakbak One",15,"bold"))
 Label0.place(x=0,y=60)
 Label1=tk.Label(window2,text='Qr-Name:',fg="white",bg="#121212",font=("Bakbak One",15,"bold"))
 Label1.place(x=0,y=140)
 Label2=tk.Label(window2,text='Qr-Location:',fg="white",bg="#121212",font=("Bakbak One",15,"bold"))
 Label2.place(x=0,y=100)
 Label3=tk.Label(window2,bg="#121212")
 Label3.place(x=295,y=290)
  
 info_Label=tk.Label(window2,text="IF YOU WANT TO SEND QR-CODE TO YOUR MAIL.",fg="#8E44AD",font=("Bakbak One",15,"bold"),bg="#121212")
 info_Label.place(x=150,y=180)
  
 Label4=tk.Label(window2,text='Send Qr_code',fg="white",bg="#121212",font=("Bakbak One",15,"bold"))
 Label4.place(x=0,y=220)
 send_qrcode_entry=tk.Entry(window2,textvariable="ENTER MAIL",font=("Arial",15,"bold"),bg='white',width=45)
 send_qrcode_entry.place(x=140,y=220)
 send_qrcode_entry.insert(0,"Enter Mail")
 send_qrcode_entry.bind("<FocusIn>",pass_enter)
 send_qrcode_entry.bind("<FocusOut>",pass_leave)  
 
 
 Label5=tk.Label(window2,text="My Github Qr-Code",fg="#8E44AD",font=("Bakbak One",15,"bold"),bg="#121212")
 Label5.place(x=302,y=500)

 my_git_locatoin="main-qrcode\\git-qr.png"
 my_git_img=ImageTk.PhotoImage(Image.open(my_git_locatoin).resize((200,200)))
 Label3.configure(image=my_git_img,bg="#121212")
 
 
 
 Label(window2,text="QR-CODE-GENERATOR",fg="#8E44AD",bg="#121212",font=("Amiri",20,"bold")).place(x=245,y=10)
 Frame(window2,width=800,height=50,bg="#0F115B").place(x=0,y=700)
 Label(window2,text="Copyright © 'AHMED RAMADAN' 2023 All Rights Reserved.",fg="#8E44AD",bg="#121212",font=("Bakbak One",10,"bold")).place(x=230,y=550)
#_______________________________________
 def my_generate_2():
    global file_locate
    global my_img
    global my_qr
    if user_link1.get()=="":
      messagebox.showinfo("ENTER LINK","Input Link...",parent=window2)
    elif get_name.get()=="":
      messagebox.showinfo("ENTER NAME","Input Qr-Code Name...",parent=window2)
    elif user_location.get()=="":
      messagebox.showinfo("ENTER NAME","Input Location to Save Qr-Code...",parent=window2)
    else:
     try:
      my_qr = pyqrcode.create(f"{user_link1.get()}") 
      main_image_location="main-qrcode/test.png"
      my_qr.png('main-qrcode/test.png', scale=5, module_color=[0, 0, 0, 255])
      my_qr = my_qr.xbm(scale=5)
      my_img=ImageTk.PhotoImage(Image.open(main_image_location).resize((200,200)))
      Label3.config(image=my_img)
      img = Image.open(f"main-qrcode\\test.png") 
      img = img .save(f"{file_locate}//{get_name.get()}.png")
      Label5.configure(text="       Scan Now    ")
      messagebox.showinfo("Qr-Code","Qr-Code Created Successfully.....",parent=window2)
     except:
       return ""
 def clear():
   clear1=user_link1.delete(0,1000) 
   clear2=get_name.delete(0,1000)
   clear3=user_location.delete(0,1000)
   my_git_locatoin="main-qrcode\\git-qr.png"
   my_git_img=ImageTk.PhotoImage(Image.open(my_git_locatoin).resize((200,200)))
   Label3.configure(image=my_git_img,bg="#121212")
   Label5.configure(text="Clear Done".center(22," "))
   return clear1 ,clear2 ,clear3
 window2.mainloop()
simple_qr_code()
