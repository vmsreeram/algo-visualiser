from xmlrpc.client import Boolean
import Edmond_Karp
from tkinter import *
from tkinter import filedialog

root = Tk()
root.configure(background='lightyellow')
root.title("edmond-karp-visualiser")
root.geometry('1000x1000')
frame = Frame(root)
frame.pack()

def browse():
	global filename
	filename = filedialog.askopenfilename(initialdir = "",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                        ("all files",
                                                         "*.*")))
	return filename

C=[]
CheckVar1 = BooleanVar(root)
CheckVar1.set(True)

def openInp():
    global C
    filename=browse()
    openedFile = "Opened file : "+str(filename)
    fileLbl = Label(root, text=openedFile, font="arial 15", fg="black")
    fileLbl.pack()
    C1.pack()
    proceedBtn.pack(side=LEFT)
    with open(filename) as textFile:
        Cx = [line.split() for line in textFile]
    C=[]
    for i in range(len(Cx[0])):
        C.append([int(j) for j in Cx[i]])
    
def done():
    print(CheckVar1.get())
    root.destroy()
    Edmond_Karp.Main(C,0,len(C)-1, CheckVar1.get())

browseBtn = Button(frame,
                   text="Browse",
                   fg="green",
                   command=openInp)
browseBtn.pack(side=LEFT)

exitBtn = Button(frame,
                   text="Exit",
                   fg="green",
                   command=exit)
exitBtn.pack(side=LEFT)

proceedBtn = Button(frame,
                   text="Proceed",
                   fg="green",
                   command=done)

C1 = Checkbutton(root, text = "Hide zero capacity edges with non-zero flow values in visualisation", variable = CheckVar1, height=2, width = 70)


root.mainloop()