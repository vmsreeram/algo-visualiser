import os
from PIL import ImageTk
from tkinter import *
import PIL.Image
DimHeight = 500

def displayAllGraphs():
    win = Tk()
    win.title("Edmond-Karp Visualisation")
    win.geometry("1500x1000")                 # changed so as to fit whole window (instead of line28, which isn't working on mac)
    frame = Frame(win, width=500, height=600)
    frame.place(anchor='e', relx=0.5, rely=0.5)

    frame2 = Frame(win, width=500, height=600)
    frame2.place(anchor='w', relx=0.5, rely=0.5)

    frameLabel = Frame(win, width=600, height=100)
    frameLabel.place(anchor='n', relx=0.5, rely=0)

    frameLegend = Frame(win, width=600, height=600)
    frameLegend.place(anchor='sw', relx=0.1, rely=0.95)
    lbllegend = Label(frameLegend, text='C/F on edge represents the edge \nwith capacity C, having flow F', font="arial 15", fg="black", bg='green')
    lbllegend.pack()
    residualImgs=[]
    flowImgs=[]

    folder = 'imgs/flow'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        flowImgs.append(str(file_path))

    folder = 'imgs/resi'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        residualImgs.append(str(file_path))

    residualImgs.sort()
    flowImgs.sort()

    global curr
    curr = -1
    def showImg():
        global curr
        curr+=1
        if curr == len(flowImgs)-1:
            slogan2.pack_forget()
        if curr >= 1:
            slogan1.pack(side=LEFT)


        if curr>=len(flowImgs):
            print("wrong index")
            return
        
        global DimHeight
        imgResIm = (PIL.Image.open(residualImgs[curr]))
        widRes, heiRes = imgResIm.size
        ReRatio = widRes/heiRes
        DimWidth = int(ReRatio * DimHeight)
        if DimWidth>=600:
            DimWidth=600
            DimHeight=int(DimWidth / ReRatio)
        resized_image= imgResIm.resize((DimWidth,DimHeight), PIL.Image.ANTIALIAS)
        imgRes= ImageTk.PhotoImage(resized_image)

        imgFloIm = (PIL.Image.open(flowImgs[curr]))
        widFlo,heiFlo = imgFloIm.size
        FlRatio = widFlo/heiFlo
        DimWidth = int(FlRatio * DimHeight)
        if DimWidth>=600:
            DimWidth=600
            DimHeight=int(DimWidth / ReRatio)
        resized_image= imgFloIm.resize((DimWidth,DimHeight), PIL.Image.ANTIALIAS)
        imgFlo= ImageTk.PhotoImage(resized_image)


        for widgets in frame.winfo_children():
            widgets.destroy()

        #### 
        for widgets in frameLabel.winfo_children():
            widgets.destroy()
        labelstring = 'Step '+str(curr+1)
        labelll = Label(frameLabel, text=labelstring, font="arial 25 underline")
        labelll.pack()
        ####

        label = Label(frame, image = imgFlo)
        labell = Label(frame, text='Flow Graph', font="arial 15 underline")
        labell.pack()
        label.pack()

        for widgets in frame2.winfo_children():
            widgets.destroy()
        label2 = Label(frame2, image=imgRes)
        label22 = Label(frame2, text='Residual Graph', font="arial 15 underline")
        label22.pack()
        label2.pack() 
        win.mainloop()

    def showPrevImg():
        global curr
        curr-=1
        if curr == 0:
            slogan1.pack_forget()
        if curr <= len(flowImgs)-2:
            slogan2.pack(side=RIGHT)


        try:
            assert(curr>=0 and curr<len(flowImgs))
        except:
            print("wrong index")
            return
        
        global DimHeight
        imgResIm = (PIL.Image.open(residualImgs[curr]))
        widRes, heiRes = imgResIm.size
        ReRatio = widRes/heiRes
        DimWidth = int(ReRatio * DimHeight)
        if DimWidth>=600:
            DimWidth=600
            DimHeight=int(DimWidth / ReRatio)
        resized_image= imgResIm.resize((DimWidth,DimHeight), PIL.Image.ANTIALIAS)
        imgRes= ImageTk.PhotoImage(resized_image)

        imgFloIm = (PIL.Image.open(flowImgs[curr]))
        widFlo,heiFlo = imgFloIm.size
        FlRatio = widFlo/heiFlo
        DimWidth = int(FlRatio * DimHeight)
        if DimWidth>=600:
            DimWidth=600
            DimHeight=int(DimWidth / ReRatio)
        resized_image= imgFloIm.resize((DimWidth,DimHeight), PIL.Image.ANTIALIAS)
        imgFlo= ImageTk.PhotoImage(resized_image)

        for widgets in frame.winfo_children():
            widgets.destroy()

        #### 
        for widgets in frameLabel.winfo_children():
            widgets.destroy()
        labelstring = 'Step '+str(curr+1)
        labelll = Label(frameLabel, text=labelstring, font="arial 25 underline")
        labelll.pack()
        ####
        
        label = Label(frame, image = imgFlo)
        labell = Label(frame, text='Flow Graph', font="arial 15 underline")
        labell.pack()
        label.pack()

        for widgets in frame2.winfo_children():
            widgets.destroy()
        label2 = Label(frame2, image=imgRes)
        label22 = Label(frame2, text='Residual Graph', font="arial 15 underline")
        label22.pack()
        label2.pack() 
        win.mainloop()


    slogan1 = Button(win,
                    text="<< Prev",
                    fg="green",
                    font="arial 20",
                    command=showPrevImg)
    slogan2 = Button(win,
                    text="Next >>",
                    fg="green",
                    font="arial 20",
                    command=showImg)
    slogan3 = Button(win,
                    text="Exit",
                    fg="red",
                    font="arial 20",
                    command=exit)                

    slogan2.pack(side=RIGHT)
    slogan3.pack(side=BOTTOM)
    showImg()
    win.mainloop()