from tkinter import *
from PIL import ImageTk, Image

# def destroyFrame(frm):
#     for widgets in frm.winfo_children():
#         widgets.destroy()


def newImage(win):
    print("newImage Called")
    # frame = Frame(win, width=600, height=400)
    # frame.place(anchor='center', relx=0.5, rely=0.5)

    for widgets in frame.winfo_children():
        widgets.destroy()
    img = ImageTk.PhotoImage(Image.open("output.png"))

    # Create a Label Widget to display the text or Image
    label = Label(frame, image = img)
    label.pack()



win = Tk()

# Define the geometry of the window
win.geometry("700x500")

frame = Frame(win, width=600, height=400)
frame.place(anchor='center', relx=0.5, rely=0.5)

# newImage(win)

# Create an object of tkinter ImageTk
img = ImageTk.PhotoImage(Image.open("output.png"))

# Create a Label Widget to display the text or Image
label = Label(frame, image = img)
label.pack()
win.attributes('-fullscreen', True)

# slogan2 = Button(frame,
#             text="next",
#             fg="green",
#             command=win.destroy)
# slogan2.pack(side=TOP)

slogan2 = Button(frame,
            text="exit",
            fg="green",
            command=win.destroy)
slogan2.pack(side=TOP)

win.mainloop()