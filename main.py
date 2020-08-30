from tkinter import *

from matplotlib import animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from timer import Timer
import matplotlib.pyplot as plt
import tkinter.messagebox as tmsg
import datetime
from matplotlib.figure import Figure
"""
import time

import board
import busio
import digitalio
import adafruit_max31865
spi = busio.SPI(board.SCK, MOSI=board.MOSI, MISO=board.MISO)
cs = digitalio.DigitalInOut(board.D5)  # Chip select of the MAX31865 board.
sensor = adafruit_max31865.MAX31865(spi, cs, wires=3)
temp = sensor.temperature
relay=digitalio.DigitalInOut(board.D18)
relay1=digitalio.DigitalInOut(board.D13)
relay1.direction=digitalio.Direction.OUTPUT
relay.direction=digitalio.Direction.OUTPUT
while 1:
  print("temp: {0:0.3f}C".format(temp))
  relay.value=False
  time.sleep(1)
  relay.value = True
  time.sleep(1)
  relay1.value=False
  time.sleep(1)
  relay1.value = True
  time.sleep(1)
"""
global xvalueforgraph,m,oldtemp
xvalueforgraph=0
k = 0
root = Tk()
root.geometry("800x700")
def tmp() :
  if lock["text"]=="lock":
    def click(event):
        global scvalue
        text = event.widget.cget("text")
        if text == "Set":
            if scvalue.get().isdigit():
                value = int(scvalue.get())
                if value > 40:
                    value ="0"
                    tmsg.showinfo("Error", "Enter the value under the 40")
                root1.destroy()

            else:
                try:
                    value = eval(screen.get())

                except Exception as e:
                    print(e)
                    value = ""
                    tmsg.showinfo("Error", "Enter the value between 0 to 40")

            scvalue.set(value)
            screen.update()

        elif text == "C":
            scvalue.set("")
            screen.update()

        else:
            scvalue.set(scvalue.get() + text)
            screen.update()
    root1 = Tk()
    root1.title("Set Temperature")
    f = Frame(root1, bg="grey")
    b = Button(f, text="9", padx=28, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    b = Button(f, text="8", padx=28, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    b = Button(f, text="7", padx=28, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(root1, bg="grey")
    b = Button(f, text="6", padx=28, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    b = Button(f, text="5", padx=28, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    b = Button(f, text="4", padx=28, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(root1, bg="grey")
    b = Button(f, text="3", padx=28, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    b = Button(f, text="2", padx=28, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    b = Button(f, text="1", padx=28, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    f.pack()

    f = Frame(root1, bg="grey")
    b = Button(f, text="0", padx=28, pady=14, font="lucida 15 bold")
    b.pack(side=LEFT, padx=16, pady=5)
    b.bind("<Button-1>", click)

    b = Button(f, text="Set", padx=25, pady=14, font="lucida 15 bold")
    b.pack(side=LEFT, padx=16, pady=5)
    b.bind("<Button-1>", click)

    b = Button(f, text="C", padx=25, pady=14, font="lucida 15 bold")
    b.pack(side=LEFT, padx=16, pady=5)
    b.bind("<Button-1>", click)
    f.pack()
    root1.mainloop()
  else:
      tmsg.showinfo("Alert", "screen is locked, unlock first!")
def relay():
    if lock["text"] == "lock":
        #a=sensor.temperature
        a=6
        global m
        b=int(scvalue.get())
        if b > a:

             m=0
             relay.value = False
             tmsg.showinfo("Alert", "Heter is on")
    else:
        tmsg.showinfo("Alert", "screen is locked, unlock first!")
def animate(i):
    pulldata =open("sensordata.txt","r").read()
    datalist = pulldata.split('\n')
    xlist=[]
    ylist=[]
    for eachline in datalist:
        if len(eachline) > 1:
            x,y =eachline.split(',')
            xlist.append(int(x))
            ylist.append(int(y))
    a.clear()
    a.plot(xlist,ylist)
    TextAreatempdata.delete(1.0,END)
    TextAreatempdata.insert(END, pulldata)
def monitor():
    if scvalue.get().isdigit():
        #a = sensor.temperature
        a=6
        global oldtemp, xvalueforgraph,m

        if oldtemp !=a:
            print("ok")
            oldtemp=a
            f = open("sensordata.txt", "a")
            f.write(str(xvalueforgraph)+","+str(a)+"\n")
            f.close()
            xvalueforgraph +=5
        b = int(scvalue.get())

        temp_value.config(text=a)
        if b==a and m==0:
            m +=1
            relay.value = False
            tmsg.showinfo("Alert", "Heter is off")
    temp_value.after(100,monitor)
def clock():
    x = datetime.datetime.now()
    time1 = (x.strftime("%I:%M:%S%p"))
    date1 = (x.strftime("%x"))
    date.config(text="Date : "+ date1)
    time.config(text="Time : "+ time1)
    time.after(100,clock)
def fan_timer():
    if lock["text"] == "lock":
        def timer():
            import os
            global m, s,k
            if k == 0:
                s = 0
                m = 0
            os.system('cls')
            print(m, 'Minutes', s, 'Seconds')
            time1.config(text="Time : " +str(m) +" Minutes "+str(s)+' Seconds')
            s += 1
            k = 1
            if s == 60:
                m += 1
                s = 0
            if ledButton["text"] == "LED OFF":
                time1.after(1000, timer)
            else:
               m=s=k=0
               t=time1["text"]
               f = open("log.txt", "a")
               f.write("\n The fan is on for time of {}".format(t))
               f.close()
               time1.config(text=" ",bg="grey")
               pulldata = open("log.txt", "r").read()
               TextArealog.delete(1.0,END)
               TextArealog.insert(END, pulldata)
        if ledButton["text"] == "LED OFF":
            ledButton["text"] = "LED ON"
            print("on")

        elif ledButton["text"] == "LED ON":
            ledButton["text"] = "LED OFF"
            print("fan on")
            timer()
    else:
        tmsg.showinfo("Alert", "screen is locked, unlock first")
def lockscreen():
    if lock["text"] == "lock":
        lock["text"] = "unlock"
        print("locked")
    elif lock["text"] == "unlock":
        lock["text"]="lock"
        print("unlocked")
def selftest():
    pass
def sensordata():
    print("data added")
    a=9
    f = open("sensordata.txt", "a")
    f.write(str(xvalueforgraph) + "," + str(a) + "\n")
    f.close()
    pulldata = open("sensordata.txt", "r").read()
    TextAreatempdata.delete(1.0, END)
    TextAreatempdata.insert(END, pulldata)
    TextAreatempdata.after(300000, sensordata)


f1 = Frame(root, bg="grey")
f1.pack( fill="both")
date=Label(f1,text=12,relief="solid", font="leto 15 bold")
date.pack(side=LEFT,anchor = "nw", padx=18, pady=5)
time=Label(f1,text=12,relief="solid", font="leto 15 bold")
time.pack(side=RIGHT,anchor = "ne", padx=18, pady=5)
lock = Button(f1, text="lock",command=lockscreen, font="lucida 10 bold")
lock.pack(side=RIGHT,anchor = "ne", padx=70, pady=5)
selftest= Button(f1, text="selftest",command=selftest, font="lucida 10 bold")
selftest.pack(side=LEFT,anchor = "nw", padx=70, pady=5)
t = Timer()
t.start()
f2 = Frame(root, bg="grey")
f2.pack(fill="both")
temp=Label( f2,text="Temperature", padx=22, pady=22, font="leto 25 bold")
temp.pack(side=LEFT,anchor = "ne", padx=18, pady=50)
settemp=Label( f2,text=" Set Temperature", padx=22, pady=22, font="leto 25 bold")
settemp.pack(side=RIGHT,anchor = "nw", padx=18, pady=50)


f3 = Frame(root, bg="grey")
f3.pack(fill="both")
temp_value=Label( f3,text="0", padx=22, pady=22, font="leto 25 bold",relief=SUNKEN)
temp_value.pack(side=LEFT,anchor = "ne", padx=80, pady=5)

f4=Frame(height=20,width=50,bg="grey")
f4.pack(fill="both")
scvalue = StringVar()
scvalue.set("")
screen = Entry(f3, textvar=scvalue, font="lucida 25 bold")
screen.pack(side=RIGHT,anchor = "ne",ipadx=8, pady=10, padx=10)
EnterButton = Button(f3,text="Set value",command=relay,font="lucida 15 bold")
EnterButton.pack()
EnterButton = Button(f3,text="Enter value",command=tmp,font="lucida 15 bold")
EnterButton.pack()
f = Figure(figsize=(6,2), dpi=80)
a=f.add_subplot(111)
c=FigureCanvasTkAgg(f,f4)
c.get_tk_widget().pack(side=RIGHT,anchor = "ne")

ledButton = Button(f4,text="LED ON",command=fan_timer,font="lucida 25 bold")
ledButton.pack(pady=20, padx=10)
time1=Label(f4,text=" ",font="leto 10 bold",bg="grey")
time1.pack()


TextArealog = Text(root,height=300,width=400,bg="white", font="lucida 15")
TextArealog.pack(fill="both",side=LEFT,expand=True)
Scroll = Scrollbar(TextArealog)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextArealog.yview)
TextArealog.config(yscrollcommand=Scroll.set)
pulldata =open("log.txt","r").read()
TextArealog.insert(END,pulldata)
TextAreatempdata = Text(root,height=300,width=300,bg="white", font="lucida 15")
TextAreatempdata.pack(fill="both",side=RIGHT,ipadx=60)
m=0
oldtemp=temp_value["text"]
Scroll = Scrollbar(TextAreatempdata)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=TextAreatempdata.yview)
TextAreatempdata.config(yscrollcommand=Scroll.set)
clock()
monitor()
sensordata()
t.stop()
ani=animation.FuncAnimation(f,animate,interval=1000) #for 5 min put 3,00,000
root.mainloop()
