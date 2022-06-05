import pydot

def makeGraph(C, F, s, t, fGraphName, hide0cp=False, initdisp=False):
    n = len(C)  
    graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white", sep=3, nodesep=0.9)

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph.add_node(my_node)
    if not initdisp:
        graph.get_node(str(s))[0].set_label("S R C")
        graph.get_node(str(t))[0].set_label("S N K")

    # Forcing source to be at top and sink to be in opposite sides of the graph
    subg=pydot.Subgraph(rank='source')
    subg.add_node(pydot.Node(str(s)))
    graph.add_subgraph(subg)
    subg2=pydot.Subgraph(rank='sink')
    subg2.add_node(pydot.Node(str(t)))
    graph.add_subgraph(subg2)

    if not initdisp:
        # add edges
        for i in range(n):
            for j in range(n):
                if (((C[i][j]!=0) or (F[i][j]!=0)) and not hide0cp) or ((C[i][j]!=0) and hide0cp):
                    graph.add_edge(pydot.Edge(str(i), str(j), label=str(C[i][j])+"/"+str(F[i][j]),fontsize="15.0",arrowhead='vee',penwidth=1.5,color="white" ,fontcolor="white"))
                # if ((C[i][j]!=0) and hide0cp):
                #     graph.add_edge(pydot.Edge(str(i), str(j), label=str(C[i][j])+"/"+str(F[i][j]),fontsize="15.0",arrowhead='vee' ))
    else:                           # for intial graph display only
        for i in range(n):
            for j in range(n):
                if (((C[i][j]!=0) or (F[i][j]!=0)) and not hide0cp) or ((C[i][j]!=0) and hide0cp):
                    graph.add_edge(pydot.Edge(str(i), str(j), label=str(C[i][j]),fontsize="15.0",arrowhead='vee',color="white",fontcolor="white",penwidth=1.5 ))
            
    # fdp fixes nodes' positions
    graph.write(fGraphName, prog='fdp', format='png')
    
