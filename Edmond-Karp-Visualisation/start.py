import Edmond_Karp
import Edmond_Karp_Flow
from tkinter import *
from tkinter import filedialog
import PIL.Image
from PIL import ImageTk

root = Tk()
root.title("edmond-karp-visualiser")
root.geometry('1250x800')
frame = Frame(root)
frame.pack()

frm_inp_grp = Frame(root, width=750, height=500, highlightbackground="blue", highlightthickness=2)

frm_inp = Frame(root, width=550, height=150, highlightbackground="green", highlightthickness=1)

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
inpTxt = Text(frm_inp, height = 1, width = 5, highlightbackground = "grey", highlightcolor= "grey", highlightthickness=2)
inpTxt.config(font =("Courier", 20))


def openInp():
    global C
    filename=browse()
    # if (len(str(filename))) >= 65:
    #     openedFile = "\nOpened file : "+str(filename)[:20] +" ... "+str(filename)[(len(str(filename))-45):]
    # else:    
    openedFile = "\nOpened file : "+str(filename)
    fileLbl = Label(root, text=openedFile, font="arial 15", fg="black", wraplength=600)
    fileLbl.pack()
    C1.pack()
    browseBtn.pack_forget()
    exitBtn.pack_forget()
    proceedBtn.pack(padx=2, pady=5, side=LEFT)
    exitBtn.pack(padx=2, pady=5, side=LEFT)
    try:
        with open(filename) as textFile:
            Cx = [line.split() for line in textFile]
    except:
        print("Invalid input file contents")
        exit()
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
    
    #########
    F = [[0] * len(C) for i in range(len(C))]
    Edmond_Karp_Flow.makeGraph(C, F, 0, (len(C)-1), 'imgs/inp_grp.png', True, True)
    
    DimHeight=500           # resize forcing this to be image height, keeping aspect ratio (nearly) the same
    imgResIm = (PIL.Image.open('imgs/inp_grp.png'))
    widRes, heiRes = imgResIm.size
    ReRatio = widRes/heiRes
    DimWidth = int(ReRatio * DimHeight)
    resized_image= imgResIm.resize((DimWidth,DimHeight), PIL.Image.ANTIALIAS)
    imgRes= ImageTk.PhotoImage(resized_image)

    lbl_inp_grp = Label(frm_inp_grp, image=imgRes)
    
    # imgRes=ImageTk.PhotoImage(imgResIm)       # uncomment these 2 if resizing is to be overridden
    # lbl_inp_grp = Label(frm_inp_grp, image=imgRes)
    lbl_inp_grp.pack()
    frm_inp_grp.place(anchor='n', relx=0.5, rely=0.15)
    frm_inp.place(anchor='n', relx=0.5, rely=0.8)

    #########

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
        print("Invalid input of src/snk")
        exit()
    root.destroy()
    try:
        Edmond_Karp.Main(C,int(src),int(snk), CheckVar1.get())
    except Exception as e:
            print('Failed to call Edmond_Karp.Main(). Reason: %s' % (e))

browseBtn = Button(frame,
                   text="Choose input graph",
                   fg="black",
                   font="arial 20",
                   command=openInp)
browseBtn.pack(padx=2, pady=5, side=LEFT)

exitBtn = Button(frame,
                   text="Exit",
                   fg="black",
                   font="arial 20",
                   command=exit)
exitBtn.pack(padx=2, pady=5, side=LEFT)

proceedBtn = Button(frame,
                   text="Proceed",
                   fg="black",
                   font="arial 20",
                   command=done)

C1 = Checkbutton(frm_inp, text = " Hide zero capacity edges with non-zero flow values in visualisation", variable = CheckVar1, height=2, width = 50)


# comment
root.mainloop()