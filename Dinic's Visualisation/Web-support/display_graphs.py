import os
from PIL import ImageTk
from tkinter import *
import PIL.Image
mul = 0.47

def displayAllGraphs(max_flow_value, s, t, resiIndices):
    win = Tk()
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()

    win.title("Dinic's Visualisation")
    scrSizeStr=str(int(screen_width))+'x'+str(int(screen_height))
    win.geometry(scrSizeStr)
    frm_flowImg = Frame(win, width=screen_width*mul, height=screen_height*0.66667)
    frm_flowImg.place(anchor='e', relx=0.5, rely=0.5)

    frm_residImg = Frame(win, width=screen_width*mul, height=screen_height*0.66667)
    frm_residImg.place(anchor='w', relx=0.5, rely=0.5)

    frm_stepLbl = Frame(win, width=screen_width*0.41666, height=screen_height*0.11111)
    frm_stepLbl.place(anchor='n', relx=0.5, rely=0)

    levelImgs=[]
    flowImgs=[]

    folder = 'imgs/flow'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        flowImgs.append(str(file_path))

    # folder = 'imgs/level'
    # for filename in os.listdir(folder):
    #     file_path = os.path.join(folder, filename)
    #     levelImgs.append(str(file_path))
    nfiles=len(flowImgs)
    flowImgs.clear()

    for i in range(nfiles):
        levelImgs.append('imgs/level/'+str(i)+'.png')
        flowImgs.append('imgs/flow/'+str(i)+'.png')
    # levelImgs.sort()
    # flowImgs.sort()
    # print(levelImgs)

    imgFloIm = (PIL.Image.open(flowImgs[0]))
    widFlo,heiFlo = imgFloIm.size
    FlRatio1 = widFlo/heiFlo
    DimWidth1=screen_width*mul
    DimHeight1=int(DimWidth1 / FlRatio1)
    if(DimHeight1 > screen_height*0.65):
        DimHeight1 = screen_height*0.65
        DimWidth1 = int(DimHeight1*FlRatio1)

    frm_legend = Frame(win, width=screen_width*0.41666, height=screen_width*0.41666)
    frm_legend.place(anchor='nw', relx = 0.5-(DimWidth1/screen_width), rely=0.9)
    lbllegend = Label(frm_legend, text='•  C/F on edges represent capacity C and flow value F\n•  Zero capacity edges are not shown\n•  Source-Red; Sink-Blue', font="arial 19", fg="white", bg='#204934',justify= LEFT)
    lbllegend.configure(text='•  C/F on edges represent capacity C and flow value F   •  Cyan bordered node is the current node\n•  Zero capacity edges are not shown\n•  Source-Red; Sink-Blue')
    lbllegend.pack()

    global curr
    curr = -1
    def showImg():
        global curr
        curr+=1
        if curr == len(flowImgs)-1:
            nextButton.pack_forget()
            lbllegend.configure(text='The max '+str(s)+'-'+str(t)+' flow value is '+str(max_flow_value)+'\n• Nodes reachable from source- Red; Other nodes- Blue\n• Source and sink are marked in thick border')
            lbllegend.pack()

        if curr >= 1:
            prevButton.place(relx=0,rely=0, anchor=NW)
        
        # resize images generated before displaying. Same width(=screen_width*mul) forced.
        imgResIm = (PIL.Image.open(levelImgs[curr]))
        widRes, heiRes = imgResIm.size
        ReRatio = widRes/heiRes
        DimWidth=screen_width*mul
        DimHeight=int(DimWidth / ReRatio)
        if(DimHeight > screen_height*0.65):
            DimHeight = screen_height*0.65
            DimWidth = int(DimHeight*ReRatio)
        resized_image= imgResIm.resize((int(DimWidth),int(DimHeight)), PIL.Image.ANTIALIAS)
        imgRes= ImageTk.PhotoImage(resized_image)

        imgFloIm = (PIL.Image.open(flowImgs[curr]))
        widFlo,heiFlo = imgFloIm.size
        FlRatio = widFlo/heiFlo
        DimWidth=screen_width*mul
        DimHeight=int(DimWidth / FlRatio)
        if(DimHeight > screen_height*0.65):
            DimHeight = screen_height*0.65
            DimWidth = int(DimHeight*FlRatio)
        resized_image= imgFloIm.resize((int(DimWidth),int(DimHeight)), PIL.Image.ANTIALIAS)
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
        if curr not in resiIndices:
            resiImg_txt_lbl = Label(frm_residImg, text='Level Graph', font="arial 25")
        else:
            resiImg_txt_lbl = Label(frm_residImg, text='Residual Graph', font="arial 25")
        resiImg_txt_lbl.pack()
        resiImg_lbl.pack() 
        win.mainloop()

    def showPrevImg():
        global curr
        curr-=1
        if curr == 0:
            prevButton.place_forget()
        if curr <= len(flowImgs)-2:
            lbllegend.configure(text='•  C/F on edges represent capacity C and flow value F   •  Cyan bordered node is the current node\n•  Zero capacity edges are not shown\n•  Source-Red; Sink-Blue')
            lbllegend.pack()
            nextButton.pack(side=TOP, anchor=NE)
        
        # resize images generated before displaying. Same width(=screen_width*mul) forced.
        global DimHeight
        imgResIm = (PIL.Image.open(levelImgs[curr]))
        widRes, heiRes = imgResIm.size
        ReRatio = widRes/heiRes
        DimWidth=screen_width*mul
        DimHeight=int(DimWidth / ReRatio)
        if(DimHeight > screen_height*0.65):
            DimHeight = screen_height*0.65
            DimWidth = int(DimHeight*ReRatio)
        resized_image= imgResIm.resize((int(DimWidth),int(DimHeight)), PIL.Image.ANTIALIAS)
        imgRes= ImageTk.PhotoImage(resized_image)

        imgFloIm = (PIL.Image.open(flowImgs[curr]))
        widFlo,heiFlo = imgFloIm.size
        FlRatio = widFlo/heiFlo
        DimWidth=screen_width*mul
        DimHeight=int(DimWidth / FlRatio)
        if(DimHeight > screen_height*0.65):
            DimHeight = screen_height*0.65
            DimWidth = int(DimHeight*FlRatio)
        resized_image= imgFloIm.resize((int(DimWidth),int(DimHeight)), PIL.Image.ANTIALIAS)
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
        if curr not in resiIndices:
            resiImg_txt_lbl = Label(frm_residImg, text='Level Graph', font="arial 25")
        else:
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
                    fg="black",
                    font="arial 20",
                    command=exit,bg= "red")                

    nextButton.pack(side=TOP, anchor=NE)
    exitButton.place(rely=1.0, relx=1.0, anchor=SE)

    def leftKey(event):
        # print ("Left key pressed")  
        if(prevButton.winfo_viewable()):
            showPrevImg()

    def rightKey(event):
        # print ("Right key pressed") 
        if(nextButton.winfo_viewable()):
            showImg()
        
    def escpress(event):
        exit()
        
    framee = Frame(win, width=0, height=0)
    framee.bind('<Left>', leftKey)
    framee.bind('<Right>', rightKey)
    framee.bind('<Escape>', escpress)
    framee.focus_set()
    framee.pack()

    showImg()
    win.mainloop()