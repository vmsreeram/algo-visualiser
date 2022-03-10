import tkinter as tk

render = None
def write_slogan():
    # get image and display
    image = tk.PhotoImage(file = "Attachment.png")
    imageLabel.configure(image = image)
    imageLabel.image = image   
    
def write_anotherslogan():
    # get image and display
    image = tk.PhotoImage(file = "MST.png")
    imageLabel.configure(image = image)
    imageLabel.image = image 

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

imageLabel = tk.Label(frame)
imageLabel.pack(side=tk.TOP)
w = tk.Label(root, text="Visualisation Of Graph Algorithms!", fg="green")
w.pack(side=tk.TOP)

button = tk.Button(frame, 
                   text="EXIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.BOTTOM)

slogan = tk.Button(frame,
                   text="View",
                   fg="blue",
                   command=write_slogan)
slogan.pack(side=tk.BOTTOM)

anotherslogan = tk.Button(frame,
                   text="Open",
                   fg="yellow",
                   command=write_anotherslogan)
anotherslogan.pack(side=tk.BOTTOM)

root.mainloop()
