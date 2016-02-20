#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
from Tkinter import *
import PIL

root = Tk()

image_path = "spring.gif"
text_file_path = 'C:/Users/Forward-TA/Desktop/time.txt'

c = Canvas(root, width=600, height=400)
c.pack()

img = PhotoImage(file=image_path)
#c.create_image(0, 0, image=img, anchor="nw")
c.create_rectangle(0,0,600,400,fill="black",outline="blue")
c.create_text(20,30,text="kefal", font="Verdana 12",anchor="w",justify=CENTER,fill="red") 

def function(ar="kefal"):
    with serial.Serial("COM3", 19200, timeout=1) as ser:
        try:
            x = ser.read()
            y = ser.read()
            z = ser.read()
            e = ser.read()
            data = ser.read(13)

            data = map(ord, data)

            if ord(y) != 1:
                pass
            else:
                s = 0
                for i in data[:-1]:
                    s += i
                res = (s & 255) - data[12]
                if res:
                    pass
                else:
                    summ = ser.read()
                    #print hex(ord(x))
                    #print hex(ord(y))
                    #print hex(ord(z))
                    #print hex(ord(e))
                    minuts = data[1]
                    second = data[2]
                    attach = data[3]
                    score1 = data[4]
                    score2 = data[5]
        
                    minuts_and_seconds = str(minuts) + ":" + str(second)
                    attach = str(attach)
                    score1 = str(score1)
                    score2 = str(score2)
        
                    #c.create_image(0, 0, image=img, anchor="nw")
                    c.create_rectangle(0,0,600,400,fill="black",outline="blue")
                    c.create_text(20,30,text=minuts_and_seconds, 
                        font="Verdana 12",anchor="w",justify=CENTER,fill="red") 
        
                    c.create_text(20,60,text=score1 + ":" + score2, 
                        font="Verdana 12",anchor="w",justify=CENTER,fill="red") 
        except:
            pass
    root.after(1, function)

root.after(0, function)
root.overrideredirect(1)
root.mainloop()
