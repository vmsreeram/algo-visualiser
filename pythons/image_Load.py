# Import required libraries
from ctypes import alignment
from tkinter import *
from turtle import bgcolor
from PIL import ImageTk, Image

# Create an instance of tkinter window
def loadimg():
      win = Tk()
      win.title("Edmond-Karp Visualisation")

      # Define the geometry of the window
      win.geometry("1500x1000")                 # changed so as to fit whole window (instead of line28, which isn't working on mac)
      frame = Frame(win, width=600, height=400)
      frame.place(anchor='e', relx=0.5, rely=0.5)

      frame2 = Frame(win, width=600, height=400)
      frame2.place(anchor='w', relx=0.5, rely=0.5)
      # Create an object of tkinter ImageTk
      img = ImageTk.PhotoImage(Image.open("output.png"))
      img2 = ImageTk.PhotoImage(Image.open("output1.png"))

      # Create a Label Widget to display the text or Image
      label = Label(frame, image = img)
      labell = Label(frame, text='Flow Graph', font="arial 15 underline")
      labell.pack()
      label.pack()
      
      label2 = Label(frame2, image=img2)
      label22 = Label(frame2, text='Residual Graph', font="arial 15 underline")
      label22.pack()
      label2.pack()

      # slogan2 = Button(frame,
      #              text="next",
      #              fg="green",
      #              command=win.destroy)
      slogan2 = Button(win,
                   text="Next",
                   fg="green",
                   font="arial 20",
                   command=win.destroy)
      slogan2.pack(side=TOP)

      slogan22 = Button(win,
                   text="Exit",
                   fg = "RED",
                   font="arial 20",
                   command=exit)
      slogan22.pack(side=BOTTOM)

      # win.attributes('-fullscreen', True)
      win.mainloop()