import tkinter
from tkinter import *
from PIL import Image, ImageTk

root = Tk()

im = Image.open('Attachment.png')
imc=im.transpose(Image.ROTATE_180)
(x0,y0,x1,y1)=imc.getbbox()
imc.thumbnail((1+x1/2,1+y1/1))
im_thumb=imc.copy()

global brand_preview
brand_preview = Label(root, image = None)
brand_preview.place(x = 10, y = 60)

# Thats how the button works
def clear_label_image():
    brand_preview.config(image = "")
    photoimg_brand = ImageTk.PhotoImage(im_thumb)
    brand_preview.image = photoimg_brand
    brand_preview.config(image = photoimg_brand)


# thats the button which have to clear the label image
top_brand = Button(root, text = "clear", bg = "snow3", command=clear_label_image)
top_brand.place(x = 550, y = 60)

# thats how I load a photoimage into the label
photoimg_brand = ImageTk.PhotoImage(im_thumb)
brand_preview.image = photoimg_brand
brand_preview.config(image = photoimg_brand)

