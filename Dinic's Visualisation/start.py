import Dinic
import showGraph
import ErrorExit
from tkinter import *
from tkinter import filedialog
import PIL.Image
from PIL import ImageTk

root = Tk()
root.title("dinics-visualiser")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
scrSizeStr=str(int(screen_width))+'x'+str(int(screen_height))
root.geometry(scrSizeStr)
frame = Frame(root)
frame.pack()

frm_inp_grp = Frame(root, width=screen_width*0.59208, height=screen_height*0.55556, highlightbackground="blue", highlightthickness=2)

frm_inp = Frame(root, width=screen_width*0.38194, height=screen_height*0.16667, highlightbackground="green", highlightthickness=1)

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
inpTxtLbl = Label(frm_inp, height = 3, width = 75,font="arial 15", text="Enter space separated source and sink vertex indices : ")
inpTxt = Text(frm_inp, height = 1, width = 5, highlightbackground = "grey", highlightcolor= "grey", highlightthickness=2)
inpTxt.config(font =("Courier", 20))


def openInp():
    global C
    filename=browse()
    # C1.pack()
    browseBtn.pack_forget()
    exitBtn.pack_forget()
    proceedBtn.pack(padx=2, pady=5, side=LEFT)
    exitBtn.pack(padx=2, pady=5, side=LEFT)
    try:
        with open(filename) as textFile:
            Cx = [line.split() for line in textFile]
    except:
        root.destroy()
        ErrorExit.raiseErr("Invalid input file contents")
        exit()
    C=[]
    
    for lst in C:
        if len(lst) is not len(Cx[0]):
            root.destroy()
            ErrorExit.raiseErr("Invalid input file contents")
            exit()
    try:
        for i in range(len(Cx[0])):
            C.append([int(j) for j in Cx[i]])
    except:
        root.destroy()
        ErrorExit.raiseErr("Invalid input file contents")
        exit()
    

    F = [[0] * len(C) for i in range(len(C))]
    L = [[0] * len(C) for i in range(len(C))]
    g_no="../inp_grp"
    showGraph.makeGraph(F,L,g_no,C,True)
    
    DimHeight=int(screen_height*0.60556)           #FIXME: change this. Use screen info.    # resize forcing this to be image height, keeping aspect ratio (nearly) the same
    imgResIm = (PIL.Image.open('imgs/inp_grp.png'))
    widRes, heiRes = imgResIm.size
    ReRatio = widRes/heiRes
    DimWidth = int(ReRatio * DimHeight)
    resized_image= imgResIm.resize((DimWidth,DimHeight), PIL.Image.ANTIALIAS)
    imgRes= ImageTk.PhotoImage(resized_image)

    lbl_inp_grp = Label(frm_inp_grp, image=imgRes)
    
    lbl_inp_grp.pack()
    frm_inp_grp.place(anchor='n', relx=0.5, rely=0.07)
    frm_inp.place(anchor='n', relx=0.5, rely=0.8)


    defVals='0 '+str(len(Cx[0])-1)
    inpTxt.insert(END, defVals)
    inpTxtLbl.pack(padx=2, pady=10, side=LEFT)
    inpTxt.pack(padx=2, pady=10, side=LEFT)

    root.mainloop()
    
def done():
    INPUT = inpTxt.get("1.0", "end-1c")
    try:
        src, snk = INPUT.split(' ')
        assert(int(src) >=0 and int(src) <len(C) and int(snk) >=0 and int(snk) <len(C) and int(snk)!=int(src))
    except:
        root.destroy()
        ErrorExit.raiseErr("Invalid input of src/snk")
        exit()
    root.destroy()
    Dinic.Main(C,int(src),int(snk), CheckVar1.get())

browseBtn = Button(frame,
                   text="Choose input graph",
                   fg="blue",
                   font="arial 20",
                   command=openInp)
browseBtn.pack(padx=2, pady=5, side=LEFT)

exitBtn = Button(frame,
                   text="Exit",
                   fg="black",
                   font="arial 20",
                   command=exit, bg= "red")
exitBtn.pack(padx=2, pady=5, side=LEFT)

proceedBtn = Button(frame,
                   text="Proceed",
                   fg="blue",
                   font="arial 20",
                   command=done)
                   
                   
C1 = Checkbutton(frm_inp, text = "Hide zero capacity edges with non-zero flow values in visualisation", variable = CheckVar1, height=2, width = 75,font="arial 15")
root.mainloop()
