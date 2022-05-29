# Import required libraries
from tkinter import *
from PIL import ImageTk, Image

# Create an instance of tkinter window
def loadimg():
      win = Tk()

      # Define the geometry of the window
      win.geometry("700x500")

      frame = Frame(win, width=600, height=400)
      # frame.pack()
      frame.place(anchor='center', relx=0.5, rely=0.5)

      # Create an object of tkinter ImageTk
      img = ImageTk.PhotoImage(Image.open("output.png"))
      # img1 = ImageTk.PhotoImage(Image.open("minion2.jpg"))

      # Create a Label Widget to display the text or Image
      label = Label(frame, image = img)
      label.pack()

      input("Press any key...")
      # frame.clear_frame()
      for widgets in frame.winfo_children():
            widgets.destroy()
      win.destroy()      
      # label = Label(frame, image = img1)
      # label.pack()

      win.mainloop()