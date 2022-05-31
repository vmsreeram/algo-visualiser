import pydot

import tkinter as Tkinter
from PIL import Image, ImageTk

def makeGraph(C, F, s, t):
    n = len(C)  
    graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="yellow")

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i))
        graph.add_node(my_node)
    graph.get_node(str(s))[0].set_label("Source")
    graph.get_node(str(t))[0].set_label("Sink")

    for i in range(n):
        for j in range(n):
            if (C[i][j] - F[i][j])>0 :
                graph.add_edge(pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j])))
    # Or, without using an intermediate variable:

    graph.write_png('output1.png')
    