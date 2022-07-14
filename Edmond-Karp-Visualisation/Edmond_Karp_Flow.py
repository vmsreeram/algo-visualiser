import pydot

def makeGraph(C, F, s, t, fGraphName, hide0cp=False, initdisp=False, lastStg=False,path=[]):
    n = len(C)  
    if lastStg:
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white", label="Red - Source, Blue - Sink\nRed edges form min-cut", sep=3, nodesep=0.9)
    elif not initdisp:
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white", label="Red - Source\nBlue - Sink", sep=3, nodesep=0.9)
    else:
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white", sep=3, nodesep=0.9)

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph.add_node(my_node)
    if not initdisp:
        graph.get_node(str(s))[0].set_fillcolor("red4")
        graph.get_node(str(t))[0].set_fillcolor("blue4")
        graph.get_node(str(s))[0].set_style("filled")
        graph.get_node(str(t))[0].set_style("filled")

    reachable=[s]
    if lastStg:
        queue = [s]
        paths = {s:[]}
        while queue: 
            u = queue.pop(0)
            for v in range(len(C)):
                if(C[u][v]-F[u][v]>0) and v not in paths:
                    reachable.append(v)
                    paths[v] = paths[u]+[(u,v)]
                    queue.append(v)    
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

    if lastStg:
        for i in range(n):
            for j in range(n):
                if (((C[i][j]!=0) or (F[i][j]!=0)) and not hide0cp) or ((C[i][j]!=0) and hide0cp):
                    if (i in reachable) and (not (j in reachable)):
                        graph.add_edge(pydot.Edge(str(i), str(j), label=str(C[i][j])+"/"+str(F[i][j]),fontsize="20.0",arrowhead='vee',penwidth=1.5,color="red" ,fontcolor="orange"))
                    else:
                        graph.add_edge(pydot.Edge(str(i), str(j), label=str(C[i][j])+"/"+str(F[i][j]),fontsize="20.0",arrowhead='vee',penwidth=1.5,color="white" ,fontcolor="orange"))
    elif not initdisp:
        # add edges
        for i in range(n):
            for j in range(n):
                if (((C[i][j]!=0) or (F[i][j]!=0)) and not hide0cp) or ((C[i][j]!=0) and hide0cp):
                    graph.add_edge(pydot.Edge(str(i), str(j), label=str(C[i][j])+"/"+str(F[i][j]),fontsize="20.0",arrowhead='vee',penwidth=1.5,color="white" ,fontcolor="orange"))
    else:                           # for intial graph display only
        for i in range(n):
            for j in range(n):
                if (((C[i][j]!=0) or (F[i][j]!=0)) and not hide0cp) or ((C[i][j]!=0) and hide0cp):
                    graph.add_edge(pydot.Edge(str(i), str(j), label=str(C[i][j]),fontsize="20.0",arrowhead='vee',color="white",fontcolor="orange",penwidth=1.5 ))
            
    # fdp fixes nodes' positions
    graph.write(fGraphName, prog='fdp', format='png')
    
