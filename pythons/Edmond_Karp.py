#Edmonds-Karp Algorithm
import tkinter as Tkinter
import Edmond_Karp_Flow
import Edmond_Karp_Residual
import image_Load

def max_flow(C, s, t):
        n = len(C) # C is the capacity matrix
        F = [[0] * n for i in range(n)]
        Edmond_Karp_Flow.makeGraph(C, F, [], s, t, 0)
        Edmond_Karp_Residual.makeGraph(C, F, s, t)
        image_Load.loadimg()
        path = bfs(C, F, s, t)
        while path != None:
            flow = min(C[u][v] - F[u][v] for u,v in path)
            for u,v in path:
                F[u][v] += flow
                F[v][u] -= flow
            Edmond_Karp_Flow.makeGraph(C, F, path, s, t, flow)
            Edmond_Karp_Residual.makeGraph(C, F, s, t)
            image_Load.loadimg()
            path = bfs(C, F, s, t)
        return sum(F[s][i] for i in range(n))

#find path by using BFS
def bfs(C, F, s, t):
        queue = [s]
        paths = {s:[]}
        if s == t:
            return paths[s]
        while queue: 
            u = queue.pop(0)
            for v in range(len(C)):
                    if(C[u][v]-F[u][v]>0) and v not in paths:
                        paths[v] = paths[u]+[(u,v)]
                        if v == t:
                            return paths[v]
                        queue.append(v)
        return None
    
# make a capacity graph
# node 0  1  2   3
C = [[ 0, 4, 10, 0],  # 0
     [ 0, 0, 2,  7],  # 1
     [ 0, 4, 0,  5],  # 2
     [ 0, 0, 0,  0]]  # 3



source = 0  
sink = 3    
max_flow_value = max_flow(C, source, sink)
print ("Edmonds-Karp algorithm")
print ("max_flow_value is: ", max_flow_value)