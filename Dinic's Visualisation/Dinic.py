import showGraph
#Dinic Algorithm

#build level graph by using BFS
def Bfs(C, F, s, t):  # C is the capacity matrix
    n = len(C)
    queue = []
    queue.append(s)
    global level
    global levelGraph
    levelGraph = [n*[0] for i in range(n)] # initialization of level graph
    level = n * [0]  # initialization
    level[s] = 1  
    while queue:
        k = queue.pop(0)
        for i in range(n):
            if (F[k][i] < C[k][i]) and (level[i] == 0): # not visited
                levelGraph[k][i] = C[k][i] - F[k][i]
                level[i] = level[k] + 1
                queue.append(i)
    #function call {pass parameter levelGraph}
    showGraph.makeGraph(C,levelGraph)
    return level[t] > 0

#search augmenting path by using DFS
def Dfs(C, F, k, cp):
        tmp = cp
        if k == len(C)-1:
            return cp
        for i in range(len(levelGraph)):
            if (level[i] == level[k] + 1) and (0 < levelGraph[k][i]):
                f = Dfs(C,F,i,min(tmp,levelGraph[k][i]))
                F[k][i] = F[k][i] + f
                F[i][k] = F[i][k] - f
                tmp = tmp - f
        return cp - tmp

#calculate max flow
#_ = float('inf')
def MaxFlow(C,s,t):
        n = len(C)
        F = [n*[0] for i in range(n)] # F is the flow matrix
        flow = 0
        while(Bfs(C,F,s,t)):
               flow = flow + Dfs(C,F,s,100000)
        return flow

#-------------------------------------
# make a capacity graph
# node   s   o   p   q   r   t
def Main(C, source, sink, booln=False):
        print ("Dinic's Algorithm")
        ##added for debugging
        n = len(C)
        F = [n*[0] for i in range(n)]
        # Bfs(C,F,source,sink)
        ###############
        max_flow_value = MaxFlow(C, source, sink)
        print ("max_flow_value is", max_flow_value)