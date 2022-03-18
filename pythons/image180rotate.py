# http://effbot.org/imagingbook/image.htm
import tkinter as Tkinter
from PIL import Image, ImageTk

root = Tkinter.Tk()
root.title("algo-visualiser")
root.geometry('3000x6000')
frame = Tkinter.Frame(root)
frame.pack()
global tklc
tklc = Tkinter.Label(root, image=None)

def openImg180():
	im = Image.open('Attachment.png')
	imc=im.transpose(Image.ROTATE_180)
	(x0,y0,x1,y1)=imc.getbbox() # returns (0,0,w,h)
	imc.thumbnail((1+x1/1,1+y1/2)) # changes image in place!
	tkic=ImageTk.PhotoImage(imc)
	tklc=Tkinter.Label(root,image=tkic)
	tklc.place(x=10.0,y=95.0)
	root.mainloop() # Start the GUI
def openImg90():
	im = Image.open('Attachment.png')
	imc=im.transpose(Image.ROTATE_90)
	(x0,y0,x1,y1)=imc.getbbox() # returns (0,0,w,h)
	imc.thumbnail((1+x1/1,1+y1/2)) # changes image in place!
	tkic=ImageTk.PhotoImage(imc)
	tklc=Tkinter.Label(root,image=tkic)
	tklc.place(x=10.0,y=95.0)
	root.mainloop() # Start the GUI
def openImg():
	im = Image.open('Attachment.png')
	imc=im.copy()
	(x0,y0,x1,y1)=imc.getbbox() # returns (0,0,w,h)
	imc.thumbnail((1+x1/1,1+y1/2)) # changes image in place!
	tkic=ImageTk.PhotoImage(imc)
	tklc=Tkinter.Label(root,image=tkic)
	tklc.place(x=10.0,y=95.0)
	root.mainloop() # Start the GUI
slogan = Tkinter.Button(frame,
                   text="Open",
                   fg="green",
                   command=openImg)
slogan.pack(side=Tkinter.LEFT)
# slogan = Tkinter.Button(frame,
#                    text="Open 90",
#                    fg="green",
#                    command=openImg90)
# slogan.pack(side=Tkinter.LEFT)
slogan1 = Tkinter.Button(frame,
                   text="Open 180",
                   fg="green",
                   command=openImg180)
slogan1.pack(side=Tkinter.TOP)
root.configure(background='lightyellow')
root.mainloop()


