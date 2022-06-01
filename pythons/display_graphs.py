import os
from PIL import ImageTk
from tkinter import *
import PIL.Image

win = Tk()
win.title("Edmond-Karp Visualisation")
win.geometry("1500x1000")                 # changed so as to fit whole window (instead of line28, which isn't working on mac)
frame = Frame(win, width=600, height=400)
frame.place(anchor='e', relx=0.5, rely=0.5)

frame2 = Frame(win, width=600, height=400)
frame2.place(anchor='w', relx=0.5, rely=0.5)

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

curr = -1
print("len flow imgs = ")
print(len(flowImgs))
print(" flow imgs = ")
print((flowImgs))
print(" resi imgs = ")
print((residualImgs))

def showImg():
    global curr
    curr+=1
    print(curr,residualImgs[curr] )
    try:
        assert(curr>=0 and curr<len(flowImgs))
    except:
        print("wrong index")
        return
    imgRes = ImageTk.PhotoImage(PIL.Image.open(residualImgs[curr]))
    imgFlo = ImageTk.PhotoImage(PIL.Image.open(flowImgs[curr]))

    for widgets in frame.winfo_children():
      widgets.destroy()
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


# slogan1 = Button(win,
#                 text="Prev",
#                 fg="green",
#                 font="arial 20",
#                 command=showImg(curr-1))
slogan2 = Button(win,
                text="Next",
                fg="green",
                font="arial 20",
                command=showImg)

# slogan1.pack(side=TOP)
slogan2.pack(side=TOP)
win.mainloop()