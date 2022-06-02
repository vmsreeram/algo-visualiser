from xmlrpc.client import Boolean
import Edmond_Karp
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("edmond-karp-visualiser")
root.geometry('1000x1000')
frame = Frame(root)
frame.pack()
frm_inp = Frame(root, width=600, height=100)
frm_inp.place(anchor='n', relx=0.5, rely=0.5)
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
CheckVar1 = BooleanVar(frm_inp)
CheckVar1.set(True)
inpTxtLbl = Label(frm_inp, height = 3, width = 100, text="\n\nEnter space separated source and sink vertex indices : ")
inpTxt = Text(frm_inp, height = 1, width = 10)
inpTxt.config(font =("Courier", 20))


def openInp():
    global C
    filename=browse()
    openedFile = "Opened file:\n"+str(filename)
    fileLbl = Label(root, text=openedFile, font="arial 15", fg="black")
    fileLbl.pack()
    C1.pack()
    
    proceedBtn.pack(side=LEFT)
    with open(filename) as textFile:
        Cx = [line.split() for line in textFile]
    C=[]
    for i in range(len(Cx[0])):
        C.append([int(j) for j in Cx[i]])
    defVals='0 '+str(len(Cx[0])-1)
    inpTxt.insert(END, defVals)
    inpTxtLbl.pack(anchor='sw')
    inpTxt.pack(anchor='se')
    
def done():
    # print(CheckVar1.get())
    INPUT = inpTxt.get("1.0", "end-1c")
    src, snk = INPUT.split(' ')
    # print((src,snk))
    root.destroy()
    # exit()
    Edmond_Karp.Main(C,int(src),int(snk), CheckVar1.get())

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

C1 = Checkbutton(frm_inp, text = "Hide zero capacity edges with non-zero flow values in visualisation", variable = CheckVar1, height=2, width = 50)



root.mainloop()