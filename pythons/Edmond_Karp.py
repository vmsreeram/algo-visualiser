#Edmonds-Karp Algorithm
import shutil
import Edmond_Karp_Flow
import Edmond_Karp_Residual
import os
import display_graphs

def max_flow(C, s, t):
        n = len(C) # C is the capacity matrix
        F = [[0] * n for i in range(n)]

        index = 1
        fGraphName = "imgs/flow/flowGraph" +str(index) + ".png"
        rGraphName = "imgs/resi/residualGraph" +str(index) + ".png"

        path = bfs(C, F, s, t)
        while path != None:
            flow = min(C[u][v] - F[u][v] for u,v in path)
            Edmond_Karp_Flow.makeGraph(C, F, s, t, fGraphName)
            Edmond_Karp_Residual.makeGraph(C, F, path, flow, s, t, rGraphName)
            for u,v in path:
                F[u][v] += flow
                F[v][u] -= flow
            index += 1
            fGraphName = "imgs/flow/flowGraph" +str(index) + ".png"
            rGraphName = "imgs/resi/residualGraph" +str(index) + ".png"
            path = bfs(C, F, s, t)
        Edmond_Karp_Flow.makeGraph(C, F, s, t, fGraphName)
        Edmond_Karp_Residual.makeGraph(C, F, path, flow, s, t, rGraphName)
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

""" C = [[ 0, 6, 5],  # 0
     [ 2, 0, 7],  # 1
     [ 3, 1, 0]]  # 3 """

""" C = [[ 0, 6, 4, 10, 9],  # 0
     [ 5, 0, 6, 2,  7],  # 1
     [ 7, 0, 0, 4,  5],  # 2
     [ 3, 8, 4, 0,  5],  # 3
     [ 5, 7, 3, 9,  0]]  # 4 """

source = 0  
sink = 3

# to remove all files in folder = 'imgs/flow' and 'imgs/resi' // assuming imgs, flow, resi exists
folder = 'imgs/flow'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))

folder2 = 'imgs/resi'
for filename in os.listdir(folder2):
    file_path = os.path.join(folder2, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))


max_flow_value = max_flow(C, source, sink)
print ("Edmonds-Karp algorithm")
print ("max_flow_value is: ", max_flow_value)
display_graphs.displayAllGraphs()