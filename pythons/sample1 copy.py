import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

# Position text in frame
Label(root, text = 'Position image on button', font =('times', 5)).pack(side = TOP, padx = 0, pady = 0)

# Create a photoimage object of the image in the path
photo = PhotoImage(file = "Attachment.png")
# photo = photo1.resize((500,500))

# Resize image to fit on button
photoimage = photo.subsample(1, 1)

# Position image on button
Button(root, image = photoimage).pack(side = BOTTOM, pady = 15)
mainloop()
