#!/usr/bin/env python
# -*- coding: utf-8 -*-

import serial
import time
from Tkinter import *
import PIL
import json

root = Tk()
f = open("conf.json", "r")
json_data = json.loads(f.read())
f.close()

image_path = "spring.gif"
text_file_path = 'C:/Users/Forward-TA/Desktop/time.txt'

c = Canvas(root, width=json_data["width"], height=json_data["height"])
c.pack()

img = PhotoImage(file=image_path)
#c.create_image(0, 0, image=img, anchor="nw")



c.create_rectangle(0,0,json_data["width"],json_data["height"],fill=json_data["color"],outline="blue")

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
                    if attach !=255:
                        if attach > 24:
                            attach = (attach & 127) / 10.0

                        attach = str(attach)

                    else:
                        attach = ""
                    score1 = str(score1)
                    score2 = str(score2)
        
                    #c.create_image(0, 0, image=img, anchor="nw")
                    c.create_rectangle(0,0,json_data["width"],json_data["height"],
                        fill=json_data["color"],outline="blue")

                    c.create_text(json_data["position"][0],json_data["position"][1],text=attach, 
                        font=json_data["font"],anchor="w",justify=CENTER,fill=json_data["colorFill"]) 
        
                    #c.create_text(20,60,text=score1 + ":" + score2, 
                    #    font="Verdana 12",anchor="w",justify=CENTER,fill="red") 
        except:
            pass
    root.after(1, function)

root.after(0, function)
root.overrideredirect(1)
root.mainloop()
