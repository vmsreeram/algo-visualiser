from tkinter import *

def raiseErr(errmsg):
    errmsg+="!!"
    win=Tk()
    win.geometry("500x300")
    win.title("Error")
    okBtn=Button(win,text='OK',command=exit,font='times 25')
    errLbl=Label(win,text=errmsg,font='times 50')
    errLbl.pack()
    okBtn.pack(side=BOTTOM)
    win.mainloop()
