import pydot

def makeGraph(C, F, path, flow, s, t, rGraphName):
    n = len(C)
    if path is not None and path != []:
        stringg="Length of augmenting path = "+str(len(path))+"\nBottleneck Capacity = "+str(flow)
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="yellow", label=stringg, sep=3, nodesep=0.9)
    else:
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="yellow", label="No path exists from Source to Sink.\nThe vertices reachable from Source are now shown in white", sep=3, nodesep=0.9)

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
                    # if v == t:
                    #     return paths[v]
                    queue.append(v)    
        print("vertices reachable from s :=",reachable)
    # Add nodes
    for i in range(n):
        if (i in reachable) and (path is None or path == []):
            my_node = pydot.Node(str(i),style = 'filled', fillcolor = '#fafafa')
            graph.add_node(my_node)
        else:
            my_node = pydot.Node(str(i))
            graph.add_node(my_node)

    graph.get_node(str(s))[0].set_label("Source")
    graph.get_node(str(t))[0].set_label("Sink")

    # Forcing source to be at top and sink to be in opposite sides of the graph
    subg=pydot.Subgraph(rank='source')
    subg.add_node(pydot.Node(str(s)))
    graph.add_subgraph(subg)
    subg2=pydot.Subgraph(rank='sink')
    subg2.add_node(pydot.Node(str(t)))
    graph.add_subgraph(subg2)

    # add edges
    for i in range(n):
        for j in range(n):
            if (C[i][j] - F[i][j])>0 :
                if path is not None and ((i,j) in path):
                    if (C[i][j] - F[i][j] == flow):
                        graph.add_edge(pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]) , fontsize="15.0",color = "red" , penwidth = 3))    #bottleneck edge
                    else:
                        graph.add_edge(pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]) , fontsize="15.0",color = "red",arrowhead='vee' ))                  #augmenting path but not bottleneck
                else:
                    graph.add_edge( pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]),fontsize="15.0",arrowhead='vee') )

    # fdp fixes nodes' positions
    graph.write(rGraphName, prog='fdp', format='png')

    