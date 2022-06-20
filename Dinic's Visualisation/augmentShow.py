import pydot

def makeAugmentGraph (C,F,path,L,bottleNeckCapacity,g_no,source,sink):
    n = len(C)
    last_node = path[-1]
    
    #making level graph and making its png image
    graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",sep=3, nodesep=0.9)

    #Add nodes
    for i in range(n):
        if(i==last_node):
            my_node = pydot.Node(str(i),fontcolor="white",color="#198BB4")
        else:
            my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph.add_node(my_node)
    
    graph.get_node(str(source))[0].set_fillcolor("red4")
    graph.get_node(str(sink))[0].set_fillcolor("blue4")
    graph.get_node(str(source))[0].set_style("filled")
    graph.get_node(str(sink))[0].set_style("filled")
    #Add edges
    for i in range(n):
        for j in range(n):
            if(L[i][j]>0):
                if (i in path) and (j in path): # this can be optimised by changing the color change of edge later
                    if L[i][j]== bottleNeckCapacity:
                        graph.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "red",fontsize="20.0",penwidth=4,fontcolor="orange") )
                    else:
                        graph.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "red",fontsize="20.0",penwidth=1.5,fontcolor="orange") )
                
                else:
                    graph.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange") )
            else:
                graph.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",style="invis") )
    

    #making flow graph and making its png image
    graph1 = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",sep=3, nodesep=0.9)

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph1.add_node(my_node)
    graph1.get_node(str(source))[0].set_fillcolor("red4")
    graph1.get_node(str(sink))[0].set_fillcolor("blue4")
    graph1.get_node(str(source))[0].set_style("filled")
    graph1.get_node(str(sink))[0].set_style("filled")
    # add edges
    for i in range(n):
        for j in range(n):
            if(C[i][j]>0):
                graph1.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j]) + "/" + str(F[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange") )
            else:
                graph1.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j]) + "/" + str(F[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",style="invis") )

    graph.write("imgs/level/"+g_no+".png", prog='fdp', format='png')
    graph1.write("imgs/flow/"+g_no+".png", prog='fdp', format='png')