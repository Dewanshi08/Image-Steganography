# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 19:17:39 2017

@author: dewanshi_yadav
"""


import tkinter
import tkinter as tk
#from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk

import workshop2 as w
 

#from tkinter.filedialog import askopenfilename

import tkinter as tt

import os
from itertools import count

import speech_recognition as sr

    

def display(): 
    global r3
    r3= tkinter.Toplevel(root)
    r3.title("MESSAGE")
    r3.geometry("400x300")
    center(r3)
    
    lbl11 = ImageLabel(r3)
    lbl11.pack()
    lbl11.load('record.gif')
    lbl11.place(x=100, y=120, relwidth=0.5, relheight=0.5)
    
    ww1=tkinter.Label(r3, text="YOUR VOICE IS BEING RECORDED\nSAY SOMETHING !",fg = "white",font = "ariel 12 bold ")
    ww1.grid()
    ww1.place(x=40,y=20)
    button = tkinter.Button(r3,text="OK",width=10,height=2,bg="white",fg="red",cursor="arrow", command=speech2text)
    button.grid()
    button.place(x=150,y=70)
    
def speech2text():   
    r3.destroy()
    
    r = sr.Recognizer()
 
    with sr.Microphone() as source: 
        audio = r.listen(source)  
    try:
        text1.insert(tk.END,r.recognize_google(audio))
        print("The audio file contains: " + r.recognize_google(audio))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google SpeechRecognition service; {0}".format(e))
    
    
 
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))




class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)





    
def output(path):
    path=path[::-1]
    path=path.replace(".",".)tpyrcne(",1)
    path=path[::-1]
    return path


def set_password():
    global text11
    global rt
    rt= tkinter.Toplevel(root)
    
    rt.title("Set Password")
    rt.geometry("400x300")
    rt.option_add("*background", "#201E1E ")
    rt.configure(background='#201E1E ')
     
    center(rt)
    rt.wm_iconbitmap('icon.ico')
    
    lbl11 = ImageLabel(rt)
    lbl11.pack()
    lbl11.load('lock.gif')
    lbl11.place(x=10, y=50, relwidth=1, relheight=1)

    p=tkinter.Label(rt, text="SET PASSWORD:",fg = "white",font = "ariel 10 bold ")
    p.grid()
    p.place(x=10,y=35)
    text11 =tkinter.Text(rt,height=1.5,width=16,font=('verdana','9','bold','italic'),bd=5,fg="#138D75",bg="white",cursor="arrow")
    text11.grid()
    text11.place(x=130,y=30)
    
    
    button = tkinter.Button(rt,text="SUBMIT",width=10,height=2,bg="white",fg="black",cursor="star", command=encode_msg)
    button.grid()
    button.place(x=310,y=30)
    
    


  
def encode_msg():
    
    password =text11.get("1.0",tkinter.END)[:-1]
   
    f = tt.filedialog.askopenfilename()
    file = os.path.abspath(f)
    path = file
    
    i=text1.get("1.0",tkinter.END)[:-1]
    
    img = Image.open(path);
    original_image_file = path
    
    img = Image.open(original_image_file)
    encoded_image_file =  output(path)

    secret_msg = i
    img_encoded = w.encode_image(img, secret_msg, password)

    if img_encoded:
        img_encoded.save(encoded_image_file)
        tkinter.messagebox.showinfo("MESSAGE", "{} saved!".format(encoded_image_file))
        print("{} saved!".format(encoded_image_file))
        
    rt.destroy()

def decode_msg():
    
    pass2 = passw.get("1.0",tkinter.END)[:-1]
    
    rr.destroy()
    
    f = tt.filedialog.askopenfilename()
    file = os.path.abspath(f)
    path = file
    img=Image.open(path)
    
    hidden_text = w.decode_pass(img,pass2)
    
    if hidden_text == "None":
        main.destroy()
        
    elif hidden_text != 'None':
        print("Hidden text:\n{}".format(hidden_text))
        r2= tkinter.Toplevel(main)
        r2.title("HIDDEN MESSAGE")
        r2.geometry("400x300")
        center(r2)
        
    
        p=tkinter.Label(r2, text="HIDDEN TEXT:\n",fg = "white",font = "ariel 12 bold ")
        p.grid()
        p.place(x=6,y=10)
    
        text2 =tkinter.Text(r2,height=5,width=30,font=('verdana','9','bold','italic'),bd=5,fg="black",bg="white",cursor="arrow")
        text2.grid()
        text2.place(x=70,y=40)
        text2.insert(tk.END,"{}".format(hidden_text))
        
        im1 = Image.open('image4.png')
        im1=im1.resize((150,150),Image.ANTIALIAS)
        tkimage1 = ImageTk.PhotoImage(im1)
        myvar1=tkinter.Label(r2,image = tkimage1)
        myvar1.grid()
        myvar1.place(x=0, y=150)
        
   
        
    
    
    
   
def authentication():
    global psw1
    global passw
    
    global rr
    rr= tkinter.Toplevel(main)
    rr.option_add("*background", "#201E1E ")
    rr.configure(background='#201E1E ')
     
    rr.title("AUTHENTICATION")
    rr.geometry("400x300")
    center(rr)
    rr.wm_iconbitmap('icon.ico')
    lbl1 = ImageLabel(rr)
    lbl1.pack()
    lbl1.load('g5.gif')
    lbl1.place(x=0, y=50, relwidth=1, relheight=1)
    p=tkinter.Label(rr, text="ENTER PASSWORD:",fg = "white",font = "ariel 10 bold ")
    p.grid()
    p.place(x=10,y=30)
    
    passw=tkinter.Text(rr,height=1,width=15,font=('ariel','9','bold','italic'),bd=5,fg="#138D75",bg="white",cursor="arrow")
    passw.grid()
    passw.place(x=150,y=30)
    
    
    MyButton1 = tkinter.Button(rr,text="SUBMIT",width=10,height=1,bg="white",fg="red",cursor="arrow", command=decode_msg)
    MyButton1.grid()
    MyButton1.place(x=290,y=30)
    

    
def new_win():
    global text1
    global root
    root = tkinter.Toplevel(main)
    root.title("IMAGE STEGANOGRAPHY")
    root.geometry("860x600")
    root.option_add("*background", "black")
    root.configure(background='black')
    
    
    center(root)

    root.wm_iconbitmap('login.ico')
    
    im1 = Image.open('goldlock.jpg')
    im1=im1.resize((700,400),Image.ANTIALIAS)
    tkimage1 = ImageTk.PhotoImage(im1)
    myvar1=tkinter.Label(root,image = tkimage1)
    myvar1.grid()
    myvar1.place(x=50, y=150)
    
    
    
    ww=tkinter.Label(root, text="ENTER HIDDEN MESSAGE:",fg = "white",font = "ariel 12 bold italic")
    ww.grid()
    ww.place(x=0,y=4)
    
    text1 =tkinter.Text(root,height=3.5,width=50,font=('verdana','9','bold','italic'),bd=5,fg="#138D75",bg="white",cursor="arrow")
    text1.grid()
    text1.place(x=20,y=35) 
    
    button1 =tkinter.Button(root,text = "ENCRYPT",font=('Helvetica', '12','bold'),fg="#5B2C6F",bg="WHITE",bd=5,cursor="star",height=2,width=10,command = set_password)
    button1.grid(row=0,column=3)
    button1.place(x = 600, y = 35)
   

    image=Image.open("mic.bmp")
    image=image.resize((40,40),Image.ANTIALIAS)
    image=ImageTk.PhotoImage(image)
    button3 = tkinter.Button(root,height = 55, width = 55, command = display)
    button3.config(image=image)
    button3.image = image
    button3.grid(row=0,column=3)
    button3.place(x = 500, y = 35)
    
    root.mainloop()
    
    
    
main = tkinter.Tk()
main.title("IMAGE STEGANOGRAPHY")
main.geometry("860x600")
main.option_add("*background", "black")
main.configure(background='black')
    
    
center(main)
main.wm_iconbitmap('login.ico')
    
im = Image.open('image.jpg')
im=im.resize((900,200),Image.ANTIALIAS)
tkimage = ImageTk.PhotoImage(im)
myvar=tkinter.Label(main,image = tkimage)
myvar.place(x=0, y=400)

im1 = Image.open('bluelock.jpg')
im1=im1.resize((600,300),Image.ANTIALIAS)
tkimage1 = ImageTk.PhotoImage(im1)
myvar1=tkinter.Label(main,image = tkimage1)
myvar1.place(x=5, y=30)

button1 =tkinter.Button(text = "ENCRYPT",font=('Helvetica', '15','bold'),fg="#5B2C6F",bg="WHITE",bd=5,cursor="star",height=3,width=10,command = new_win)
button1.grid()
button1.place(x = 670, y =80)
button2 = tkinter.Button(text = "DECRYPT", font=('Helvetica', '15','bold'),fg="#2E86C1",bg="WHITE",bd=5,cursor="star",height=3,width=10,command = authentication)
button2.grid()
button2.place(x = 670, y = 200)

main.mainloop()


