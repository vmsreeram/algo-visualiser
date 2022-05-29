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
    graph.get_node(str(s))[0].set_label("source")
    graph.get_node(str(t))[0].set_label("sink")

    for i in range(n):
        for j in range(n):
            graph.add_edge(pydot.Edge(str(i), str(j), label="C= "+str(C[i][j])+" : F= "+str(F[i][j])))
    # Or, without using an intermediate variable:

    graph.write_png('output.png')
    