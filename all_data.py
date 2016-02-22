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
 
 
 
 
with serial.Serial("COM3", 19200, timeout=1) as ser:
    while True:
        try:
            c.create_image(0, 0, image=img, anchor="nw")
            c.create_text(20,30,text="kefal", font="Verdana 12",anchor="w",justify=CENTER,fill="red")
            x = ser.read()
            y = ser.read()
            z = ser.read()
            e = ser.read()
            data = ser.read(13)
            summ = ser.read()
            print hex(ord(x))
            print hex(ord(y))
            print hex(ord(z))
            print hex(ord(e))
            print "Minuts:", ord(data[1])
            print "Seconds:", ord(data[2])
            print "Attach time:", ord(data[3])
            print "Scored:", ord(data[4]), " : ", ord(data[5])
            f = open(text_file_path, 'w')
            minuts = str(ord(data[1]))
            if len(minuts) == 1:
                f.write("0")
                f.write(minuts)
            else:
                f.write(minuts)
            f.write(":")
            seconds = str(ord(data[2]))
            if len(seconds) == 1:
                f.write("0")
                f.write(seconds)
            else:
                f.write(seconds)
            f.close()
            root.mainloop()
        except:
            pass
