import showGraph
#Dinic Algorithm

#build level graph by using BFS
def Bfs(C, F, s, t):  # C is the capacity matrix
    n = len(C)
    queue = []
    queue.append(s)
    global level
    level = n * [0]  # initialization
    level[s] = 1  
    while queue:
        k = queue.pop(0)
        for i in range(n):
            if (F[k][i] < C[k][i]) and ((level[i] == 0) or (level[i] == level[k] + 1)): # not visited
                levelGraph[k][i] = C[k][i] - F[k][i]
                level[i] = level[k] + 1
                queue.append(i)
    #function call {pass parameter levelGraph}
    showGraph.makeGraph(C,levelGraph)
    return level[t] > 0

#search augmenting path by using DFS
def Dfs(C, F, k, cp,t):
    tmp = cp
    if k == t:
        return cp
    for i in range(len(levelGraph)):
        if (level[i] == level[k] + 1) and (0 < levelGraph[k][i]):
            f = Dfs(C,F,i,min(tmp,levelGraph[k][i]),t)
            F[k][i] = F[k][i] + f
            F[i][k] = F[i][k] - f
            tmp = tmp - f
    return cp - tmp


def advance (path,t,F,flo):
    neighbourAvailable = False
    k = path[-1]
    u = 0
    for i in range(len(levelGraph)):
        if (level[i] == level[k] + 1) and (0 < levelGraph[k][i]):
            path.append(i)
            u = i
            neighbourAvailable = True
            break
    if(neighbourAvailable==False):
        # print("retreat: ",path," t= ", t, flo)
        flo = retreat(path,t,F,flo)
    elif (u == t):
        # print("augment: ",path," t= ", t, flo)
        flo = augment(path,t,F,flo)
    elif (path != []):
        # print("advance: ",path," t= ", t, flo)
        flo = advance(path,t,F,flo)
    return flo

    

def retreat (path,t,F,flo):
    lastEle = path.pop()
    for i in range(len(levelGraph)):
        if levelGraph[i][lastEle] >0:
            levelGraph[i][lastEle] =0
    if(path!=[]):
        # print("advance: ",path," t= ", t, flo)
        flo = advance(path,t,F,flo)
    return flo

def augment(path,t,F,flo):
    pathSize = len(path)
    if (pathSize>1):
        bottleNeckCapacity = levelGraph[path[0]][path[1]]
        bottleNeckEdgeLevels = (0,1)
        for i in range(pathSize-1):
            if(bottleNeckCapacity > levelGraph[path[i]][path[i+1]]):
                bottleNeckEdgeLevels = (i,i+1)
                bottleNeckCapacity = levelGraph[path[i]][path[i+1]]
        
        for i in range(pathSize-1):
            levelGraph[path[i]][path[i+1]] -= bottleNeckCapacity
            F[path[i]][path[i+1]] += bottleNeckCapacity
            F[path[i+1]][path[i]] -= bottleNeckCapacity
        flo += bottleNeckCapacity
        
        del path[bottleNeckEdgeLevels[1]:pathSize]
        # print("advance: ",path," t= ",t, flo,"bedge= ",bottleNeckEdgeLevels)
        flo = advance(path,t,F,flo)
    return flo



#calculate max flow
#_ = float('inf')
def MaxFlow(C,s,t):
    n = len(C)
    F = [n*[0] for i in range(n)] # F is the flow matrix
    flow = 0
    path = [s]
    while(Bfs(C,F,s,t)):
        path = [s]
        flow = flow + advance(path,t,F,0)
    return flow

#-------------------------------------
# make a capacity graph
# node   s   o   p   q   r   t
def Main(C, source, sink, booln=False):
    print ("Dinic's Algorithm")
    n = len(C)
    global path 
    global levelGraph
    levelGraph = [n*[0] for i in range(n)] # initialization of level graph
    path = len(levelGraph)*[0]
    ##added for debugging
    # n = len(C)
    # F = [n*[0] for i in range(n)]
    # Bfs(C,F,source,sink)
    ###############
    max_flow_value = MaxFlow(C, source, sink)
    print ("max_flow_value is", max_flow_value)