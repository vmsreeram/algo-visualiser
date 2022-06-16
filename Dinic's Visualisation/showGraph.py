import pydot

def makeGraph(C):
    n = len(C)

    graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white")

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph.add_node(my_node)

    # add edges
    for i in range(n):
        for j in range(n):
            graph.add_edge( pydot.Edge(str(i), str(j), label= str(C[i][j])) )

    
    graph.write("levelGraph", prog='fdp', format='png')