from tkinter import *
from matplotlib import style, animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
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
root = Tk()
root.title("7 inch Screen")
f1=plt.figure()
a=f1.add_subplot(111)
c=FigureCanvasTkAgg(f1,root)
c.get_tk_widget().pack()
ani=animation.FuncAnimation(f1,animate,interval=1000)

root.mainloop()