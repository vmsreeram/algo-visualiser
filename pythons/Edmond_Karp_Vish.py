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
def nextt():
    return
def makeGraph(C, F, s, t):
    n = len(C)  
    graph = pydot.Dot("my_graph", graph_type="graph", bgcolor="yellow")

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i))
        graph.add_node(my_node)
    graph.get_node(str(s))[0].set_label("source")
    graph.get_node(str(t))[0].set_label("sink")

    for i in range(n):
        for j in range(n):
            graph.add_edge(pydot.Edge(str(i), str(j), label="C= "+str(C[i][j])+" : F= "+str(F[i][j])))
    # Or, without using an intermediate variable:

    

    graph.write_png('output.png')
    global tklc
    tklc.config(image='')
    
    global im
    im = Image.open('output.png')
    imc=im.copy()
    (x0,y0,x1,y1)=imc.getbbox() # returns (0,0,w,h)
    imc.thumbnail((1+x1/0.5,1+y1/1)) # changes image in place!
    im=imc
    tkic=ImageTk.PhotoImage(imc)
    tklc=Tkinter.Label(root,image=tkic)
    tklc.place(relx=0.5,rely=0.5,anchor="center")
    # tklc.place(x=100.0,y=95.0,anchor="center")
    # root.mainloop()

    slogan2 = Tkinter.Button(frame,
                    text="Next",
                    fg="green",
                    command=nextt)
    slogan2.pack(side=Tkinter.TOP)
    root.mainloop()
    