import Edmond_Karp
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("edmond-karp-visualiser")
root.geometry('750x300')
frame = Frame(root)
frame.pack()
frm_inp = Frame(root, width=700, height=300)
frm_inp.place(anchor='n', relx=0.5, rely=0.4)
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
inpTxtLbl = Label(frm_inp, height = 3, width = 40, text="Enter space separated source and sink vertex indices : ")
inpTxt = Text(frm_inp, height = 1, width = 10)
inpTxt.config(font =("Courier", 20))


def openInp():
    global C
    filename=browse()
    openedFile = "\nOpened file : ..."+str(filename)[(len(str(filename))-45):]
    fileLbl = Label(root, text=openedFile, font="arial 15", fg="black")
    fileLbl.pack()
    C1.pack()
    browseBtn.pack_forget()
    exitBtn.pack_forget()
    proceedBtn.pack(padx=2, pady=5, side=LEFT)
    exitBtn.pack(padx=2, pady=5, side=LEFT)
    with open(filename) as textFile:
        Cx = [line.split() for line in textFile]
    C=[]
    for lst in C:
        if len(lst) is not len(Cx[0]):
            print("Invalid input file contents")
            exit()
    try:
        for i in range(len(Cx[0])):
            C.append([int(j) for j in Cx[i]])
    except:
        print("Invalid input file contents")
        exit()
    
    defVals='0 '+str(len(Cx[0])-1)
    inpTxt.insert(END, defVals)
    inpTxtLbl.pack(padx=2, pady=10, side=LEFT)
    inpTxt.pack(padx=2, pady=10, side=LEFT)
    
def done():
    INPUT = inpTxt.get("1.0", "end-1c")
    src, snk = INPUT.split(' ')
    if int(src) <0 or int(src) >=len(C) or int(snk) <0 or int(snk) >=len(C) or int(snk)==int(src):
        print("Invalid input of src/snk")
        exit()
    root.destroy()
    # exit()
    Edmond_Karp.Main(C,int(src),int(snk), CheckVar1.get())

browseBtn = Button(frame,
                   text="Browse",
                   fg="green",
                   command=openInp)
browseBtn.pack(padx=2, pady=5, side=LEFT)

exitBtn = Button(frame,
                   text="Exit",
                   fg="green",
                   command=exit)
exitBtn.pack(padx=2, pady=5, side=LEFT)

proceedBtn = Button(frame,
                   text="Proceed",
                   fg="green",
                   command=done)

C1 = Checkbutton(frm_inp, text = " Hide zero capacity edges with non-zero flow values in visualisation", variable = CheckVar1, height=2, width = 50)



root.mainloop()