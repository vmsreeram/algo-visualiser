import tkinter as tk

render = None
def write_slogan():
    # get image and display
    image = tk.PhotoImage(file = "Attachment.png")
    imageLabel.configure(image = image)
    imageLabel.image = image    

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="QUIT", 
                   fg="red",
                   command=quit)
button.pack(side=tk.TOP)
slogan = tk.Button(frame,
                   text="Open",
                   fg="green",
                   command=write_slogan)
slogan.pack(side=tk.TOP)

imageLabel = tk.Label(frame)
imageLabel.pack(side=tk.LEFT)
w = tk.Label(root, text="Hello Tkinter!", fg="green")
w.pack()

root.mainloop()
