import os
from PIL import ImageTk
from tkinter import *
import PIL.Image
DimHeight = 600
mul = 0.48611

def displayAllGraphs(max_flow_value):
    win = Tk()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    win.attributes('-fullscreen', True)
    win.title("Edmond-Karp Visualisation")
    win.geometry("1750x1400")                 # changed so as to fit whole window (instead of line28, which isn't working on mac)
    frm_flowImg = Frame(win, width=screen_width*mul, height=screen_height*0.66667)
    frm_flowImg.place(anchor='e', relx=0.5, rely=0.5)

    frm_residImg = Frame(win, width=screen_width*mul, height=screen_height*0.66667)
    frm_residImg.place(anchor='w', relx=0.5, rely=0.5)

    frm_stepLbl = Frame(win, width=screen_width*0.41666, height=screen_height*0.11111)
    frm_stepLbl.place(anchor='n', relx=0.5, rely=0)

    frm_legend = Frame(win, width=screen_width*0.41666, height=screen_width*0.41666)
    frm_legend.place(anchor='nw', relx=0.1, rely=0.9)
    lbllegend = Label(frm_legend, text='C/F on edge represents the edge \nwith capacity C, having flow F', font="arial 20", fg="white", bg='green')
    lbllegend.pack()

    frameanslbl = Frame(win, width=0, height=0)
    frameanslbl.place(anchor='ne', relx=0.9, rely=0.9)
    answerlabeltext = 'Edmonds-Karp algorithm\n The max flow value is: = '+str(max_flow_value)
    anslbl = Label(frameanslbl, text=answerlabeltext, font="arial 20", fg="white", bg='green')

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
            anslbl.pack()
            nextButton.pack_forget()
        if curr >= 1:
            # prevButton.pack(side=TOP, anchor=NW, relx=0.5,rely=0.5)
            prevButton.place(relx=0,rely=0, anchor=NW)
        
        # resize images generated before displaying. By default, height=500 will be made, keeping aspect ratio same.
        # However, if the width exceeds too much (>600), width=600 is made, keeping aspect ratio same.
        global DimHeight
        imgResIm = (PIL.Image.open(residualImgs[curr]))
        widRes, heiRes = imgResIm.size
        ReRatio = widRes/heiRes
        DimWidth = int(ReRatio * DimHeight)
        if DimWidth>screen_width*mul:
            DimWidth=screen_width*mul
            DimHeight=int(DimWidth / ReRatio)
        resized_image= imgResIm.resize((DimWidth,DimHeight), PIL.Image.ANTIALIAS)
        imgRes= ImageTk.PhotoImage(resized_image)

        imgFloIm = (PIL.Image.open(flowImgs[curr]))
        widFlo,heiFlo = imgFloIm.size
        FlRatio = widFlo/heiFlo
        DimWidth = int(FlRatio * DimHeight)
        if DimWidth>screen_width*mul:
            DimWidth=screen_width*mul
            DimHeight=int(DimWidth / FlRatio)
        resized_image= imgFloIm.resize((DimWidth,DimHeight), PIL.Image.ANTIALIAS)
        imgFlo= ImageTk.PhotoImage(resized_image)

        
        # remove current step label, if needed, and place new label
        for widgets in frm_stepLbl.winfo_children():
            widgets.destroy()
        labelstring = 'Step '+str(curr+1)
        step_lbl = Label(frm_stepLbl, text=labelstring, font="arial 25")
        step_lbl.pack()

        # remove image in frm_flowImg
        for widgets in frm_flowImg.winfo_children():
            widgets.destroy()
        flowImg_lbl = Label(frm_flowImg, image = imgFlo)
        flowImg_txt_lbl = Label(frm_flowImg, text='Flow Graph', font="arial 25")
        flowImg_txt_lbl.pack()
        flowImg_lbl.pack()

        # remove image in frm_residImg
        for widgets in frm_residImg.winfo_children():
            widgets.destroy()
        resiImg_lbl = Label(frm_residImg, image=imgRes)
        resiImg_txt_lbl = Label(frm_residImg, text='Residual Graph', font="arial 25")
        resiImg_txt_lbl.pack()
        resiImg_lbl.pack() 
        win.mainloop()

    def showPrevImg():
        global curr
        curr-=1
        if curr == 0:
            # prevButton.pack_forget()
            prevButton.place_forget()
        if curr <= len(flowImgs)-2:
            anslbl.pack_forget()
            nextButton.pack(side=TOP, anchor=NE)
        
        # resize images generated before displaying. By default, height=500 will be made, keeping aspect ratio same.
        # However, if the width exceeds too much (>600), width=600 is made, keeping aspect ratio same.
        global DimHeight
        imgResIm = (PIL.Image.open(residualImgs[curr]))
        widRes, heiRes = imgResIm.size
        ReRatio = widRes/heiRes
        DimWidth = int(ReRatio * DimHeight)
        if DimWidth>screen_width*mul:
            DimWidth=screen_width*mul
            DimHeight=int(DimWidth / ReRatio)
        resized_image= imgResIm.resize((DimWidth,DimHeight), PIL.Image.ANTIALIAS)
        imgRes= ImageTk.PhotoImage(resized_image)

        imgFloIm = (PIL.Image.open(flowImgs[curr]))
        widFlo,heiFlo = imgFloIm.size
        FlRatio = widFlo/heiFlo
        DimWidth = int(FlRatio * DimHeight)
        if DimWidth>screen_width*mul:
            DimWidth=screen_width*mul
            DimHeight=int(DimWidth / FlRatio)
        resized_image= imgFloIm.resize((DimWidth,DimHeight), PIL.Image.ANTIALIAS)
        imgFlo= ImageTk.PhotoImage(resized_image)

        

        # remove current step label, if needed, and place new label
        for widgets in frm_stepLbl.winfo_children():
            widgets.destroy()
        labelstring = 'Step '+str(curr+1)
        step_lbl = Label(frm_stepLbl, text=labelstring, font="arial 25")
        step_lbl.pack()
        ####

        # remove image in frm_flowImg
        for widgets in frm_flowImg.winfo_children():
            widgets.destroy()
        flowImg_lbl = Label(frm_flowImg, image = imgFlo)
        flowImg_txt_lbl = Label(frm_flowImg, text='Flow Graph', font="arial 25")
        flowImg_txt_lbl.pack()
        flowImg_lbl.pack()

        # remove image in frm_residImg
        for widgets in frm_residImg.winfo_children():
            widgets.destroy()
        resiImg_lbl = Label(frm_residImg, image=imgRes)
        resiImg_txt_lbl = Label(frm_residImg, text='Residual Graph', font="arial 25")
        resiImg_txt_lbl.pack()
        resiImg_lbl.pack() 
        win.mainloop()


    prevButton = Button(win,
                    text="<< Prev",
                    fg="green",
                    font="arial 20",
                    command=showPrevImg)
    nextButton = Button(win,
                    text="Next >>",
                    fg="green",
                    font="arial 20",
                    command=showImg)
    exitButton = Button(win,
                    text="Exit",
                    fg="red",
                    font="arial 20",
                    command=exit)                

    nextButton.pack(side=TOP, anchor=NE)
    exitButton.pack(side=BOTTOM)
    showImg()
    win.mainloop()
