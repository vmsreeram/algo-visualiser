# from tkinter import font
import pydot

def makeGraph(C, F, path, flow, s, t, rGraphName):
    n = len(C)
    if path is not None and path != []:
        stringg="Length of augmenting path = "+str(len(path))+"\nBottleneck Capacity = "+str(flow)
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white", label=stringg, sep=3, nodesep=0.9)
    else:
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white", label="No path exists from Source to Sink.\nRed - Reachable vertices from Source, Blue - others", sep=3, nodesep=0.9)

    reachable=[s]
    if path is None or path == []:
        queue = [s]
        paths = {s:[]}
        while queue: 
            u = queue.pop(0)
            for v in range(len(C)):
                if(C[u][v]-F[u][v]>0) and v not in paths:
                    reachable.append(v)
                    paths[v] = paths[u]+[(u,v)]
                    queue.append(v)    
        print("vertices reachable from s :=",reachable)
    # Add nodes
    for i in range(n):
        if (i in reachable) and (path is None or path == []):
            my_node = pydot.Node(str(i),style = 'filled', fillcolor = 'red4',fontcolor="white",color="white")
            graph.add_node(my_node)
        elif (i not in reachable) and (path is None or path == []):
            my_node = pydot.Node(str(i),style = 'filled', fillcolor = 'blue4',fontcolor="white",color="white")
            graph.add_node(my_node)
        else:
            my_node = pydot.Node(str(i),fontcolor="white",color="white")
            graph.add_node(my_node)

    graph.get_node(str(s))[0].set_fillcolor("red4")
    graph.get_node(str(t))[0].set_fillcolor("blue4")
    graph.get_node(str(s))[0].set_style("filled")
    graph.get_node(str(t))[0].set_style("filled")

    # add edges
    for i in range(n):
        for j in range(n):
            if (C[i][j] - F[i][j])>0 :
                if path is not None and ((i,j) in path):
                    if (C[i][j] - F[i][j] == flow):
                        graph.add_edge(pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]) , fontsize="15.0",color = "red" , penwidth = 4,fontcolor="white"))    #bottleneck edge
                    else:
                        graph.add_edge(pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]) , fontsize="15.0",color = "red",arrowhead='vee',penwidth=1.5 ,fontcolor="white"))                  #augmenting path but not bottleneck
                else:
                    graph.add_edge( pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]),fontsize="15.0",color="white",penwidth=1.5,arrowhead='vee',fontcolor="white") )

    # fdp fixes nodes' positions
    graph.write(rGraphName, prog='fdp', format='png')

    
