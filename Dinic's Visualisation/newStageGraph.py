import pydot
from collections import defaultdict

def makeAugmentGraph (level, C,F,path,L,bottleNeckCapacity,g_no,source,sink, lbltxtlvl="", lbltxtflo=""):
    n = len(C)
    last_node = path[-1]
    
    #making level graph and making its png image
    # graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",sep=3, nodesep=0.9, labelloc="t", label=lbltxtlvl)
    graph = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",labelloc="t", label=lbltxtlvl,rankdir="TB",sep=3, nodesep=0.9)
    graph1 = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",labelloc="t", label=lbltxtflo,rankdir="TB",sep=3, nodesep=0.9)

    #print("graph="+str(g_no))
    #print("makeAugmentGraph")
    #Add nodes
    for i in range(n):
        if(i==last_node):
            my_node = pydot.Node(str(i),fontcolor="white",color="#198BB4", xlabel="l="+str(level[i]))
        else:
            my_node = pydot.Node(str(i),fontcolor="white",color="white", xlabel="l="+str(level[i]))
        graph.add_node(my_node)
    # Add nodes
    for i in range(n):
        my_node = pydot.Node(str(i),fontcolor="white",color="white")
        graph1.add_node(my_node)

    subgs = []
    dicT=defaultdict(list)
    for i in range(max(level)+2):
        subgs.append(pydot.Subgraph(rank='same',rankdir="LR"))

    for i in range(n):
        subgs[level[i]].add_node(graph.get_node(str(i))[0])
        dicT[level[i]].append(i)
        #print("add node#"+str(i)+" lev "+str(level[i]))
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

    #print("\makeAugmentGraph\n\n")
    
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
                        graph.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "red",fontsize="20.0",penwidth=4,fontcolor="orange",constraint=False) )
                    else:
                        graph.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "red",fontsize="20.0",penwidth=1.5,fontcolor="orange",constraint=False) )
                
                else:
                    graph.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",constraint=False) )
            # else:
            #     graph.add_edge( pydot.Edge(str(i), str(j), label= str(L[i][j]),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",style="invis",constraint=False) )
    

    #making flow graph and making its png image
    # graph1 = pydot.Dot("my_graph", graph_type="digraph", bgcolor="#204934",fontcolor="white",sep=3, nodesep=0.9, labelloc="t", label=lbltxtflo)

    graph1.get_node(str(source))[0].set_fillcolor("red4")
    graph1.get_node(str(sink))[0].set_fillcolor("blue4")
    graph1.get_node(str(source))[0].set_style("filled")
    graph1.get_node(str(sink))[0].set_style("filled")
    # add edges
    for i in range(n):
        for j in range(n):
            if(C[i][j]>0):
                graph1.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j]) + "/" + str(F[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",constraint=False) )
            # else:
            #     graph1.add_edge( pydot.Edge(str(i), str(j), label= (str(C[i][j]) + "/" + str(F[i][j])),color = "white",fontsize="20.0",penwidth=1.5,fontcolor="orange",style="invis",constraint=False) )

    # graph.write("imgs/level/"+g_no+".png", prog='fdp', format='png')
    # graph1.write("imgs/flow/"+g_no+".png", prog='fdp', format='png')

    graph.write("imgs/level/"+g_no+".png", format='png')
    graph1.write("imgs/flow/"+g_no+".png", format='png')