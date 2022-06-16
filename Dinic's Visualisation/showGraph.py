import pydot

def makeGraph(C):
    n = len(C)

    graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",sep=3, nodesep=0.9)

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph.add_node(my_node)

    # add edges
    for i in range(n):
        for j in range(n):
            if(C[i][j]>0):
                graph.add_edge( pydot.Edge(str(i), str(j), label= str(C[i][j]),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange") )

    
    graph.write("levelGraph.png", prog='fdp', format='png')