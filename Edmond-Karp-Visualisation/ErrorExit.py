from tkinter import *
import os
# cmd = 'ls -al'
# os.system(cmd)

def retry():
    #TODO
    os.system('python3 start.py')
    exit()
    
    

def raiseErr(errmsg):
    global win
    errmsg+="!!"
    win=Tk()
    win.geometry("500x300")
    win.title("Error")

    okBtn=Button(win,text='Exit',command=exit,font='times 25')
    # retryBtn=Button(win,text='Retry',command=retry,font='times 25')
    errLbl=Label(win,text=errmsg,font='times 50')
    errLbl.pack()
    okBtn.pack(side=BOTTOM)
    # retryBtn.pack(side=BOTTOM)
    win.mainloop()
