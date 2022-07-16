import pydot
from collections import defaultdict

def makeGraph(level,F,L,g_no,C,source,sink,initDisp=False, lbltxtlvl="", lbltxtflo="",levelOrRecidual = 0):
    n = len(F)

    # graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",sep=3, nodesep=0.9, labelloc="t", label=lbltxtflo)
    graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",labelloc="t", label=lbltxtflo,rankdir="TB",sep=3, nodesep=0.9)
    graph1 = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",labelloc="t", label=lbltxtlvl,rankdir="TB",sep=3, nodesep=0.9)

    # Add nodes - flow graph
    for i in range(n):
        my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph.add_node(my_node)
    # Add nodes - level/residual graph
    for i in range(n):
        if (not initDisp) and (levelOrRecidual==0):
            my_node = pydot.Node(str(i),fontcolor="white",color="white", xlabel="l="+str(level[i]))
        else:
            my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph1.add_node(my_node)

    #coloring vertices according to the cut red for nodes reachable from source and blue for rest
    if (level[sink]==0):
        for i in range(n):
            if(level[i]==0):
                graph1.get_node(str(i))[0].set_fillcolor("blue4")
                graph.get_node(str(i))[0].set_fillcolor("blue4")
            else: 
                graph1.get_node(str(i))[0].set_fillcolor("red4")
                graph.get_node(str(i))[0].set_fillcolor("red4")
            graph1.get_node(str(i))[0].set_style("filled")
            graph.get_node(str(i))[0].set_style("filled")


    if not initDisp:
        #print("graph="+str(g_no))
        #print("makeGraph")

        #print("g")
        subgs = []
        dicT=defaultdict(list)
        for i in range(max(level)+2):
            subgs.append(pydot.Subgraph(rank='same',rankdir="LR"))

        for i in range(n):
            subgs[level[i]].add_node(graph.get_node(str(i))[0])
            #print("add node#"+str(i)+" lev "+str(level[i]))
            dicT[level[i]].append(i)


        for i in range(max(level)+2):
            graph.add_subgraph(subgs[i])
        
        #print("g1")
        subgs = []
        for i in range(max(level)+2):
            subgs.append(pydot.Subgraph(rank='same',rankdir="LR"))

        for i in range(n):
            subgs[level[i]].add_node(graph1.get_node(str(i))[0])
            #print("add node#"+str(i)+" lev "+str(level[i]))
        for i in range(max(level)+2):
            graph1.add_subgraph(subgs[i])
        
        #print("dicT=",dicT)
        for i in range(max(level)+2):
            if len(dicT[i]) > 0 and i+1 <= max(level) and len(dicT[i+1]) > 0:
                #print("add edge bw #"+str(dicT[i][0])+" and #"+str(dicT[i+1][0]))
                graph.add_edge( pydot.Edge(str(dicT[i][0]), str(dicT[i+1][0]), style="invis",constraint=True) )
                graph1.add_edge( pydot.Edge(str(dicT[i][0]), str(dicT[i+1][0]), style="invis",constraint=True) )
        #print("\makeGraph\n\n")

    
    
    if not initDisp:
        graph.get_node(str(source))[0].set_fillcolor("red4")
        graph.get_node(str(sink))[0].set_fillcolor("blue4")
        graph.get_node(str(source))[0].set_style("filled")
        graph.get_node(str(sink))[0].set_style("filled")
    
    # changing the node thickness/color of sink and source vertex
    if(level[sink]==0):
        graph1.get_node(str(sink))[0].set_color("#2263e5")
        graph1.get_node(str(source))[0].set_color("red2")
        graph1.get_node(str(sink))[0].set_penwidth(4)
        graph1.get_node(str(source))[0].set_penwidth(4)

        graph.get_node(str(sink))[0].set_color("#2263e5")
        graph.get_node(str(source))[0].set_color("red2")
        graph.get_node(str(sink))[0].set_penwidth(4)
        graph.get_node(str(source))[0].set_penwidth(4)
    
    
    # add edges flow graph
    if not initDisp:
        for i in range(n):
            for j in range(n):
                if(C[i][j]>0):
                    if(level[sink] ==0 and (level[i]>0 and level[j]==0) ):   #if(level[sink] ==0 and ((level[i]>0 and level[j]==0) or (level[i]==0 and level[j]>0)) ):
                        graph.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j]) + "/" + str(F[i][j])),color = "red",fontsize="20.0",penwidth=1.5,fontcolor="orange",constraint=False) )
                    else:
                        graph.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j]) + "/" + str(F[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",constraint=False) )
                # else:
                #     graph.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j]) + "/" + str(F[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",style="invis",constraint=False) )
    else:
        for i in range(n):
            for j in range(n):
                if(C[i][j]>0):
                    graph.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",constraint=False) )
                # else:
                #     graph.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",style="invis",constraint=False) )

    
    
    # graph1 = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",sep=3, nodesep=0.9, labelloc="t", label=lbltxtlvl)

    if not initDisp:
        graph1.get_node(str(source))[0].set_fillcolor("red4")
        graph1.get_node(str(sink))[0].set_fillcolor("blue4")
        graph1.get_node(str(source))[0].set_style("filled")
        graph1.get_node(str(sink))[0].set_style("filled")
    # add edges level graph
    if(levelOrRecidual==0):
        for i in range(n):
            for j in range(n):
                if(L[i][j]>0):
                    graph1.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",constraint=False) )
                # else:
                #     graph1.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",style="invis",constraint=False) )
    elif(levelOrRecidual==1):
        for i in range(n):
            for j in range(n):
                if(C[i][j]-F[i][j]>0):
                    graph1.add_edge( pydot.Edge(str(i), str(j), label= str(C[i][j]-F[i][j]),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",constraint=False) )
    #TODO:Fix nodes' positions
    # graph.write("imgs/flow/"+g_no+".png", prog='fdp', format='png')
    # if not initDisp:
    #     graph1.write("imgs/level/"+g_no+".png", prog='fdp', format='png')

    graph.write("imgs/flow/"+g_no+".png", format='png')
    if not initDisp:
        graph1.write("imgs/level/"+g_no+".png", format='png')
