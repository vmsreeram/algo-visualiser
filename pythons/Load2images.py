import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import os

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.pos = []
        self.master.title("BMP Image GUI")
        self.pack(fill=BOTH, expand=1)

        menu = Menu(self.master)
        self.master.config(menu=menu)

        # File Bar
        file = Menu(menu)
        file.add_command(label="Open Image 1", command=self.openImage1)
        file.add_command(label="Open Image 2", command=self.openImage2)
        menu.add_cascade(label="File", menu=file)

        self.canvas = tk.Canvas(self)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.image = None
        self.image2 = None

    def openImage1(self):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select BMP File",
                                              filetypes=[("BMP Files","*.bmp")])
        if not filename:
            return
        load = Image.open(filename)
        load = load.resize((960, 720), Image.ANTIALIAS)

        if self.image is None:
            w, h = load.size
            width, height = root.winfo_screenmmwidth(), root.winfo_screenheight()
            self.render = ImageTk.PhotoImage(load)
            self.image = self.canvas.create_image((w / 2, h / 2), image=self.render)
            root.geometry("%dx%d" % (w, h))
        else:
            w, h = load.size
            width, height = root.winfo_screenmmwidth(), root.winfo_screenheight()
            root.geometry("%dx%d" % (width, height))
            self.canvas.move(self.image, 960, 0)
            self.render2 = ImageTk.PhotoImage(load)
            self.image2 = self.canvas.create_image((w / 2, h / 2), image=self.render2)

    def openImage2(self):
        filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select BMP File",
                                              filetypes=[("BMP Files", "*.bmp")])
        if not filename:
            return
        load = Image.open(filename)
        load = load.resize((960, 720), Image.ANTIALIAS)

        if self.image is None:
            w, h = load.size
            self.render = ImageTk.PhotoImage(load)
            self.image = self.canvas.create_image((w / 2, h / 2), image=self.render)
            root.geometry("%dx%d" % (w, h))
        else:
            w, h = load.size
            width, height = root.winfo_screenmmwidth(), root.winfo_screenheight()
            root.geometry("%dx%d" % (width, height))
            self.render2 = ImageTk.PhotoImage(load)
            self.image2 = self.canvas.create_image((w / 2, h / 2), image=self.render2)
            self.canvas.move(self.image2, 960, 0)

root = tk.Tk()
root.geometry("%dx%d" % (300, 300))
root.title("BMP Image GUI")
app = Window(root)
app.pack(fill=tk.BOTH, expand=1)
root.mainloop()