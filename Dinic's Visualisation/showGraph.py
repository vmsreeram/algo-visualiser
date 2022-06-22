import pydot

def makeGraph(F,L,g_no,C,source,sink,initDisp=False, lbltxtlvl="", lbltxtflo=""):
    n = len(F)

    graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",sep=3, nodesep=0.9, labelloc="t", label=lbltxtflo)

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph.add_node(my_node)
    if not initDisp:
        graph.get_node(str(source))[0].set_fillcolor("red4")
        graph.get_node(str(sink))[0].set_fillcolor("blue4")
        graph.get_node(str(source))[0].set_style("filled")
        graph.get_node(str(sink))[0].set_style("filled")
    # add edges
    if not initDisp:
        for i in range(n):
            for j in range(n):
                if(C[i][j]>0):
                    graph.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j]) + "/" + str(F[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange") )
                else:
                    graph.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j]) + "/" + str(F[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",style="invis") )
    else:
        for i in range(n):
            for j in range(n):
                if(C[i][j]>0):
                    graph.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange") )
                else:
                    graph.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",style="invis") )

    
    
    graph1 = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",sep=3, nodesep=0.9, labelloc="t", label=lbltxtlvl)

    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph1.add_node(my_node)
    if not initDisp:
        graph1.get_node(str(source))[0].set_fillcolor("red4")
        graph1.get_node(str(sink))[0].set_fillcolor("blue4")
        graph1.get_node(str(source))[0].set_style("filled")
        graph1.get_node(str(sink))[0].set_style("filled")
    # add edges
    for i in range(n):
        for j in range(n):
            if(L[i][j]>0):
                graph1.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange") )
            else:
                graph1.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",style="invis") )

    #TODO:Fix nodes' positions
    graph.write("imgs/flow/"+g_no+".png", prog='fdp', format='png')
    if not initDisp:
        graph1.write("imgs/level/"+g_no+".png", prog='fdp', format='png')
