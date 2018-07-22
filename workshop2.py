import tkinter
from PIL import Image
def encode_image(img, msg, psw):
    length = len(msg)
    no_pixle = (length//255)
    mod = length%255
    
    if img.mode != 'RGB':
        print("image mode needs to be RGB")
        return False
    encoded = img.copy()
    width, h = img.size
    index = 0
    #import math
    if length>width :
        height = (length//width)+1
    else:
        height = 1

    for row in range(height):
        for col in range(width):
            r, g, b = img.getpixel((col, row))
            if row == 0 and col == 0 :
                asc = no_pixle
            elif row == 0 and col == 1 :
                asc = mod
            elif index <length:
                c = msg[index]
                asc = ord(c)
                index += 1
            if(index>length):
                break;
            encoded.putpixel((col, row), (asc, g , b))
        if(index>=length):
            break;
    #----password encoding----#
    global pswd
    pswd = psw
    
    length = len(psw)
    w, h = img.size
    index = 0
    for row in range(h-1,h-2,-1):
        #print("h: ",row)
        for col in range(w-1,w-(length+2),-1):
            #print("w: ",col)
            r, g, b = img.getpixel((col, row))
            if row == h-1 and col == w-1 :
                asc = length
             #   print(str(h-1)+str(w-1))
            elif index <length:
                c = psw[index]
                asc = ord(c)
                index += 1
            elif(index>length):
                break;
            encoded.putpixel((col, row), (asc, g , b))
        if(index>=length):
            break;
    return encoded

#----------password decoding--------#

def decode_pass(img,d_pswd):
    w, h = img.size
    #print("width: ",w," height: ",h)
    msg = ""        
    length, g, b = img.getpixel((w-1,h-1))
    #print(str(h-1)+str(w-1)+str(img.getpixel((w-1,h-1))))
    #length = len(pswd)
    #print("length",length)
    index=0
    for row in range(h-1,h-2,-1):
        #print("h: ",row)
        for col in range(w-2,w-(length+2),-1):
            #print("w: ",col)
            if row==w-1:
                continue
            elif index<length:
                r, g, b = img.getpixel((col, row))    
                msg += chr(r)
            #    print(msg)
                index += 1
            else:
                break;
        if index >= length:
            break;
    d_pass=msg
    #print("d_pass: ",d_pass)
    decode = auth(img,d_pass,d_pswd)
    return decode

#----------authentication-------------#

def auth(img,d_pass,d_pswd):
    #print("dpass,dpasswd",d_pass,d_pswd)
    if(d_pass==d_pswd):
        print("password correct")
        tkinter.messagebox.showinfo("ALERT", "AUTHENTICATION successful\nClick OK to Display Hidden Message")
        decode = decode_image(img)
        return decode
    else:
        print("incorrect password")
        tkinter.messagebox.showinfo("ALERT", "AUTHENTICATION FAIL")
        decode="None"
        return decode
        
        

#-----------decoding image------------#
        
def decode_image(img):
    
    width, height = img.size
    msg = ""        
    nop,g,b=img.getpixel((0,0))
    mod,g,b=img.getpixel((1,0))
    length = (nop*255)+mod
    width,height = img.size
    if length>width:
        h = (length//width)+1
    else:
        h=1
    index=0
    w=width
    for row in range(h):
        if(row==h-1):
            w=(length+2)%width
        for col in range(2,w):
            if index<length:
                r, g, b = img.getpixel((col, row))    
                msg += chr(r)
                index += 1
            else:
                break;
        if index >= length:
            break;
    return msg
