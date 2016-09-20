import tkMessageBox
from Tkinter import *
import sys

def newError(Title, HeadText, SubText, x, y):
     root = Tk()
     root.title(Title)
     root["padx"] = x
     root["pady"] = y

     tkinterLabel = Label(root)
     tkinterLabel["text"] = HeadText
     tkinterLabel.pack()
     tkinterLabel2 = Label(root)
     tkinterLabel2["text"] = SubText
     tkinterLabel2.pack()

     root.mainloop()


def close():
    sys.exit()