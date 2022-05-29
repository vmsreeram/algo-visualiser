"""
import pydot

graph = pydot.Dot("my_graph", graph_type="graph", bgcolor="yellow")

# Add nodes
my_node = pydot.Node("a", label="Foo")
graph.add_node(my_node)
# Or, without using an intermediate variable:
graph.add_node(pydot.Node("b", shape="circle"))

# Add edges
my_edge = pydot.Edge("a", "b", color="blue")
graph.add_edge(my_edge)
# Or, without using an intermediate variable:
graph.add_edge(pydot.Edge("b", "c", color="blue"))

graph.write_png("output.png")

"""
import pydot
import tkinter as Tkinter
from PIL import Image, ImageTk

root = Tkinter.Tk()
frame = Tkinter.Frame(root)


root.configure(background='lightyellow')
root.title("algo-visualiser")
root.geometry('1000x1000')

frame.pack()

global tklc
tklc = Tkinter.Label(root, image=None)

def openImg():
    graphs = pydot.graph_from_dot_file('file.dot')
    graph = graphs[0]
    graph.write_png('output.png')
    global tklc
    tklc.config(image='')
    
    global im
    im = Image.open('output.png')
    # imc=im.copy()
    # (x0,y0,x1,y1)=imc.getbbox() # returns (0,0,w,h)
    # imc.thumbnail((1+x1/0.5,1+y1/1)) # changes image in place!
    # im=imc
    # tkic=ImageTk.PhotoImage(imc)
    tkic=ImageTk.PhotoImage(im)
    tklc=Tkinter.Label(root,image=tkic)
    tklc.place(relx=0.5,rely=0.5,anchor="center")
    # tklc.place(x=100.0,y=95.0,anchor="center")
    root.mainloop() # Start the GUI

def nextt():
    graphs = pydot.graph_from_dot_file('file.dot')
    graph = graphs[0]
    # graph.get
    graph.get_node("a")[0].set_style("filled")
    graph.write_png('output.png')
    global tklc
    tklc.config(image='')
    
    global im
    im = Image.open('output.png')
    # imc=im.copy()
    # (x0,y0,x1,y1)=imc.getbbox() # returns (0,0,w,h)
    # imc.thumbnail((1+x1/0.5,1+y1/1)) # changes image in place!
    # im=imc
    # tkic=ImageTk.PhotoImage(imc)
    tkic=ImageTk.PhotoImage(im)
    tklc=Tkinter.Label(root,image=tkic)
    tklc.place(relx=0.5,rely=0.5,anchor="center")
    # tklc.place(x=100.0,y=95.0,anchor="center")
    root.mainloop() # Start the GUI

slogan = Tkinter.Button(frame,
                   text="opengraph",
                   fg="green",
                   command=openImg)
slogan.pack(side=Tkinter.LEFT)

slogan2 = Tkinter.Button(frame,
                   text="Exit",
                   fg="green",
                   command=exit)
slogan2.pack(side=Tkinter.TOP)

slogan3 = Tkinter.Button(frame,
                   text="next",
                   fg="green",
                   command=nextt)
slogan3.pack(side=Tkinter.TOP)

root.mainloop()

# graphs = pydot.graph_from_dot_file('file.dot')
# graph = graphs[0]
# graph.write_png('output.png')
