import pydot

def makeGraph(C, F, path, flow, s, t, rGraphName):
    n = len(C)
    if path is not None and path != []:
        stringg="Length of augmenting path = "+str(len(path))+"\nBottleneck Capacity = "+str(flow)
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="yellow", label=stringg, sep=3, nodesep=0.9)
    else:
        graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="yellow", label="No path exists from \nSource to Sink", sep=3, nodesep=0.9)

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i))
        graph.add_node(my_node)
    graph.get_node(str(s))[0].set_label("Source")
    graph.get_node(str(t))[0].set_label("Sink")

    # Forcing source to be at top and sink to be at bottom of the graph
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
                        graph.add_edge(pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]) , fontsize="10.0",color = "red" , penwidth = 3))    #bottleneck edge
                    else:
                        graph.add_edge(pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]) , fontsize="10.0",color = "red",arrowhead='vee' ))                  #augmenting path but not bottleneck
                else:
                    graph.add_edge( pydot.Edge(str(i), str(j), label= str(C[i][j] - F[i][j]),fontsize="10.0",arrowhead='vee') )

    # fdp fixes nodes' positions
    graph.write(rGraphName, prog='fdp', format='png')

    