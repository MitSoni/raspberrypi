from tkinter import *
#import RPi.GPIO as GPIO

#GPIO.setmode(GPIO.BOARD)
#GPIO.setup(40, GPIO.OUT)
#GPIO.output(40, GPIO.LOW)

win = Tk()



def ledON():
	print("LED button pressed")


from tkinter import *
import time
import tkinter.messagebox as tmsg


def myfunc():
    print("ok")


def gui():
    def click(event):
        global scvalue
        text = event.widget.cget("text")
        if text == "Enter":
            if scvalue.get().isdigit():
                value = int(scvalue.get())
                if value > 40:
                    tmsg.showinfo("Error", "Enter the value under the 40")
            else:
                try:
                    value = eval(screen.get())

                except Exception as e:
                    print(e)
                    tmsg.showinfo("Error", "Enter the value between 0 to 40")

            scvalue.set(value)
            screen.update()

        elif text == "C":
            scvalue.set("")
            screen.update()

        else:
            scvalue.set(scvalue.get() + text)
            screen.update()

    root = Tk()
    root.geometry("300x400")
    root.title("Calculator By CodeWithHarry")

    mainmenu = Menu(root)

    m1 = Menu(mainmenu, tearoff=0)

    f = Frame(root, bg="grey")
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

    f = Frame(root, bg="grey")
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

    f = Frame(root, bg="grey")
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

    f = Frame(root, bg="grey")
    b = Button(f, text="0", padx=31, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    b = Button(f, text="Enter", padx=27, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)

    b = Button(f, text="C", padx=26, pady=18, font="lucida 15 bold")
    b.pack(side=LEFT, padx=18, pady=5)
    b.bind("<Button-1>", click)
    f.pack()
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="File", menu=m1)
    m1 = Menu(mainmenu, tearoff=0)
    m1.add_command(label="New project", command=myfunc)
    m1.add_command(label="Save", command=myfunc)
    m1.add_separator()
    m1.add_command(label="Save As", command=myfunc)
    m1.add_command(label="Print", command=myfunc)
    root.config(menu=mainmenu)
    mainmenu.add_cascade(label="File", menu=m1)
    exitButton = Button(root, text="Exit", command=gui, font="Leto", height=2, width=6)
    exitButton.pack(side=BOTTOM)

    ledButton = Button(root, text="LED ON", font="leto", height=2, width=8)
    ledButton.pack()
    root.mainloop()


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "Enter":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
            if value > 40:
                tmsg.showinfo("Error", "Enter the value under the 40")
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                tmsg.showinfo("Error", "Enter the value between 0 to 40")

        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


def timer():
    t = timer()
    t.start()


root = Tk()
root.geometry("644x970")
root.title("Calculator By CodeWithHarry")

mainmenu = Menu(root)

m1 = Menu(mainmenu, tearoff=0)
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="lucida 40 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

f = Frame(root, bg="grey")
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

f = Frame(root, bg="grey")
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

f = Frame(root, bg="grey")
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

f = Frame(root, bg="grey")
b = Button(f, text="0", padx=31, pady=18, font="lucida 15 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="Enter", padx=27, pady=18, font="lucida 15 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)

b = Button(f, text="C", padx=26, pady=18, font="lucida 15 bold")
b.pack(side=LEFT, padx=18, pady=5)
b.bind("<Button-1>", click)
f.pack()
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)
m1 = Menu(mainmenu, tearoff=0)
m1.add_command(label="New project", command=myfunc)
m1.add_command(label="Save", command=myfunc)
m1.add_separator()
m1.add_command(label="Save As", command=myfunc)
m1.add_command(label="Print", command=myfunc)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)
exitButton = Button(root, text="Exit", command=gui, font="Leto", height=2, width=6)
exitButton.pack(side=BOTTOM)

ledButton = Button(root, text="LED ON", command=timer, font="leto", height=2, width=8)
ledButton.pack()
root.mainloop()


def exitProgram():
	print("Exit Button pressed")

	win.quit()


win.title("First GUI")
win.geometry('800x480')
Label(text=scvalue, font="leto 15 bold").pack()
exitButton  = Button(win, text = "Exit", command = exitProgram, height =2 , width = 6)
exitButton.pack(side = BOTTOM)

ledButton = Button(win, text = "LED ON", command = ledON, height = 2, width =8 )
ledButton.pack()

mainloop()
