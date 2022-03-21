# http://effbot.org/imagingbook/image.htm
import tkinter as Tkinter
from PIL import Image, ImageTk
from tkinter import filedialog

root = Tkinter.Tk()
root.configure(background='lightyellow')
root.title("algo-visualiser")
root.geometry('1000x1000')
frame = Tkinter.Frame(root)
frame.pack()
global tklc
tklc = Tkinter.Label(root, image=None)

# global filename
# filename='/'

def browse():
	global filename
	# filename = filedialog.askopenfilename(initialdir = "/",
 #                                          title = "Select a File",
 #                                          filetypes = (("Text files",
 #                                                        "*.png"),
 #                                                       ("all files",
 #                                                        "*.*")))
	filename = filedialog.askopenfilename(initialdir = "",
                                          title = "Select a File",
                                          filetypes = (("all files",
                                                        "*.*"),
                                                        ("all files",
                                                         "*.*")))
	return filename



def openImg():
	# if (filename is '/'):
	global tklc
	tklc.config(image='')
	filename=browse()
	global im
	im = Image.open(filename)
	imc=im.copy()
	(x0,y0,x1,y1)=imc.getbbox() # returns (0,0,w,h)
	imc.thumbnail((1+x1/1,1+y1/2)) # changes image in place!
	im=imc
	tkic=ImageTk.PhotoImage(imc)
	tklc=Tkinter.Label(root,image=tkic)
	tklc.place(relx=0.5,rely=0.5,anchor="center")
	# tklc.place(x=100.0,y=95.0,anchor="center")
	root.mainloop() # Start the GUI

def openImg270():
	# if (filename is '/'):
	# 	filename=browse()
	# im = Image.open(filename)
	global im
	im=im.transpose(Image.ROTATE_270)
	# (x0,y0,x1,y1)=im.getbbox() # returns (0,0,w,h)
	# im.thumbnail((1+x1/1,1+y1/2)) # changes image in place!
	tkic=ImageTk.PhotoImage(im)
	global tklc
	tklc.config(image='')
	tklc=Tkinter.Label(root,image=tkic)
	tklc.place(relx=0.5,rely=0.5,anchor="center")
	# tklc.place(x=100.0,y=95.0,anchor="center")
	root.mainloop() # Start the GUI

def openImg90():
	# if (filename is '/'):
	# 	filename=browse()
	# im = Image.open(filename)
	global im
	im=im.transpose(Image.ROTATE_90)
	# (x0,y0,x1,y1)=im.getbbox() # returns (0,0,w,h)
	# im.thumbnail((1+x1/1,1+y1/2)) # changes image in place!
	tkic=ImageTk.PhotoImage(im)
	global tklc
	tklc.config(image='')
	tklc=Tkinter.Label(root,image=tkic)
	tklc.place(relx=0.5,rely=0.5,anchor="center")
	# tklc.place(x=100.0,y=95.0,anchor="center")
	root.mainloop() # Start the GUI



slogan = Tkinter.Button(frame,
                   text="Browse",
                   fg="green",
                   command=openImg)
slogan.pack(side=Tkinter.LEFT)
# slogan = Tkinter.Button(frame,
#                    text="Open 90",
#                    fg="green",
#                    command=openImg90)
# slogan.pack(side=Tkinter.LEFT)
slogan1 = Tkinter.Button(frame,
                   text="Rotate counter clockwise",
                   fg="green",
                   command=openImg90)
slogan1.pack(side=Tkinter.LEFT)
slogan10 = Tkinter.Button(frame,
                   text="Rotate clockwise",
                   fg="green",
                   command=openImg270)
slogan10.pack(side=Tkinter.LEFT)

slogan2 = Tkinter.Button(frame,
                   text="Exit",
                   fg="green",
                   command=exit)
slogan2.pack(side=Tkinter.LEFT)


root.mainloop()


