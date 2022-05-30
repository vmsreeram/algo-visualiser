# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
def loadimg():
      win = Tk()

      # Define the geometry of the window
      win.geometry("1500x1000")                 # changed so as to fit whole window (instead of line28, which isn't working on mac)

      frame = Frame(win, width=600, height=400)
      frame.place(anchor='e', relx=0.5, rely=0.5)

      frame2 = Frame(win, width=600, height=400)
      frame2.place(anchor='w', relx=0.5, rely=0.5)
      # Create an object of tkinter ImageTk
      img = ImageTk.PhotoImage(Image.open("output.png"))
      img2 = ImageTk.PhotoImage(Image.open("arrow.png"))

      # Create a Label Widget to display the text or Image
      label = Label(frame, image = img)
      label.pack()

      label2 = Label(frame2, image=img2)
      label2.pack()

      # slogan2 = Button(frame,
      #              text="next",
      #              fg="green",
      #              command=win.destroy)
      slogan2 = Button(win,
                   text="next",
                   fg="green",
                   command=win.destroy)
      slogan2.pack(side=TOP)

      # win.attributes('-fullscreen', True)
      win.mainloop()