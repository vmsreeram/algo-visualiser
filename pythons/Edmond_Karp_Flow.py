from cProfile import label
import pydot

def makeGraph(C, F, s, t, fGraphName):
    n = len(C)  
    graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="yellow", sep=3, nodesep=0.9)

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


    for i in range(n):
        for j in range(n):
            if (C[i][j]!=0) or (F[i][j]!=0):
                graph.add_edge(pydot.Edge(str(i), str(j), label=str(C[i][j])+"/"+str(F[i][j]),fontsize="10.0",arrowhead='vee' ))

    graph.write(fGraphName, prog='fdp', format='png')
    