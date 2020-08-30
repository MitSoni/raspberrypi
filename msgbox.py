
from tkinter import *
from PIL import  ImageTk, Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if i%100==0 and i!=0:
            final_text += "\n"
    return final_text



root = Tk()
root.title("CodeWithHarry News - Aapka Apna Akhabaar")
root.geometry("1000x1000")

texts = []
photos = []


f0 = Frame(root, width=800, height=70)
Label(f0, text="Code With Harry News", font="lucida 33 bold").pack()
Label(f0, text="January 19, 2050", font="lucida 13 bold").pack()
f0.pack()


f1 = Frame(root, width=900, height=200, pady=14)
Label( text="one", padx=22, pady=22).pack(side="left")

f1.pack(anchor="w")


f2 = Frame(root, width=900, height=200, pady=14, padx=22)
Label(f2, text="two", padx=22, pady=22).pack(side="right")
f2.pack(anchor="w")


f3 = Frame(root, width=900, height=200, pady=34)
Label(f3, text="texts[2]", padx=22, pady=22).pack(side="left")

f3.pack(anchor="w")




root.mainloop()

