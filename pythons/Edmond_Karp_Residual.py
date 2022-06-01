from cProfile import label
from click import style
import pydot

import tkinter as Tkinter
from PIL import Image, ImageTk

def makeGraph(C, F, path, flow, s, t, rGraphName):
    n = len(C)
    if path is not None and path != []:
        # flow = min(C[u][v]-F[u][v] for u,v in path)
        stringg="Length of augmenting path = "+str(len(path))+"\nBottleneck Capacity = "+str(flow)
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="yellow", label=stringg)
    else:
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="yellow", label="No path exists from Source to Sink")

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i))
        graph.add_node(my_node)
    graph.get_node(str(s))[0].set_label("Source")
    graph.get_node(str(t))[0].set_label("Sink")

    for i in range(n-1):
        graph.add_edge(pydot.Edge(str(i), str(i+1), style = 'invis'))
    subg=pydot.Subgraph(rank='source')
    subg.add_node(pydot.Node(str(s)))
    graph.add_subgraph(subg)
    subg2=pydot.Subgraph(rank='sink')
    subg2.add_node(pydot.Node(str(t)))
    graph.add_subgraph(subg2)

    for i in range(n):
        for j in range(n):
            if (C[i][j] - F[i][j])>0 :
                if path is not None and ((i,j) in path):
                    if (C[i][j] - F[i][j] == flow):
                        graph.add_edge(pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]) , color = "red" , penwidth = 3))    #bottleneck edge
                    else:
                        graph.add_edge(pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]) , color = "red" ))                  #augmenting path but not bottleneck
                else:
                    graph.add_edge(pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j])))
    # Or, without using an intermediate variable:

    graph.write_png(rGraphName)
    