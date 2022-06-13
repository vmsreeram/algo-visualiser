from tkinter import *
import os

def retry():
    #TODO
    global win
    win.destroy()
    os.system('python3 start.py')

def raiseErr(errmsg):
    global win
    errmsg+="!!"
    win=Tk()
    win.geometry("500x300")
    win.title("Error")

    okBtn=Button(win,text='Exit',command=exit,font='times 15')
    retryBtn=Button(win,text='Retry',command=retry,font='times 15')
    errLbl=Label(win,text=errmsg,font='times 20')
    errLbl.pack()
    okBtn.pack(side=BOTTOM)
    retryBtn.pack(side=BOTTOM)
    win.mainloop()
