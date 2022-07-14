import os
import shutil
import newPhaseGraph
import newStageGraph
import display_graphs
#Dinic Algorithm

#build level graph by using BFS
def Bfs(C, F, s, t):  # C is the capacity matrix
    n = len(C)
    queue = []
    queue.append(s)
    global level
    global ctr
    global levelGraph
    levelGraph = [n*[0] for i in range(n)]
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
    global Source,Sink
    
    if(level[t]!=0):
        # new stage for showing residual graph
        newPhaseGraph.makeGraph(level, F,levelGraph,str(ctr),C,Source,Sink, False, "New Phase; s-t Path length="+str(level[t]-1),"\n")
    else:
        # new stage for showing residual graph
        newPhaseGraph.makeGraph(level, F,levelGraph,str(ctr),C,Source,Sink, False, "New Phase; No s-t path","\n")
    ctr+=1
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


def advance (C,path,t,F,flo):
    global ctr
    neighbourAvailable = False
    k = path[-1]
    u = 0
    for i in range(len(levelGraph)):
        if (level[i] == level[k] + 1) and (0 < levelGraph[k][i]):
            path.append(i)
            u = i
            neighbourAvailable = True
            break
    
    if(neighbourAvailable==False): # retreat
        flo = retreat(C,path,t,F,flo)

    elif (u == t):# augment
        flo = augment(C,path,t,F,flo)

    elif (path != []): # advance
        newStageGraph.makeAugmentGraph(level, C,F,path,levelGraph,0,str(ctr),Source,Sink,"After ADVANCING from "+str(k),"\n")
        ctr+=1
        flo = advance(C,path,t,F,flo)
    return flo

    

def retreat (C,path,t,F,flo):
    global ctr
    lastEle = path.pop()
    for i in range(len(levelGraph)):
        if levelGraph[i][lastEle] >0:
            levelGraph[i][lastEle] =0
    
    
    if(path!=[]):
        # print("advance: ",path," t= ", t, flo)
        newStageGraph.makeAugmentGraph(level, C,F,path,levelGraph,0,str(ctr),Source,Sink,"After RETRACT from "+str(lastEle),"\n")
        ctr+=1
        flo = advance(C,path,t,F,flo)
    return flo

def augment(C,path,t,F,flo):
    pathSize = len(path)
    global ctr
    if (pathSize>1):
        bottleNeckCapacity = levelGraph[path[0]][path[1]]
        bottleNeckEdgeLevels = (0,1)
        #finding bottle neck capacity and bottleneck edge
        for i in range(pathSize-2,-1,-1):
            if(bottleNeckCapacity >= levelGraph[path[i]][path[i+1]]):
                bottleNeckEdgeLevels = (i,i+1)
                bottleNeckCapacity = levelGraph[path[i]][path[i+1]]
        
        bottleNeckEdge = (path[bottleNeckEdgeLevels[0]],path[bottleNeckEdgeLevels[1]])
        global Source,Sink
        newStageGraph.makeAugmentGraph(level, C,F,path,levelGraph,bottleNeckCapacity,str(ctr),Source,Sink,"After ADVANCING from "+str(path[-2]),"\n")
        ctr+=1
        for i in range(pathSize-1):
            levelGraph[path[i]][path[i+1]] -= bottleNeckCapacity
            F[path[i]][path[i+1]] += bottleNeckCapacity
            F[path[i+1]][path[i]] -= bottleNeckCapacity
        flo += bottleNeckCapacity
        del path[bottleNeckEdgeLevels[1]:pathSize]
        
        newStageGraph.makeAugmentGraph(level, C,F,path,levelGraph,0,str(ctr),Source,Sink,"After AUGMENTING","\n")
        
        ctr+=1
        # print("advance: ",path," t= ",t, flo,"bedge= ",bottleNeckEdgeLevels)
        flo = advance(C,path,t,F,flo)
    return flo



#calculate max flow
def MaxFlow(C,s,t):
    n = len(C)
    F = [n*[0] for i in range(n)] # F is the flow matrix
    flow = 0
    path = [s]
    while(Bfs(C,F,s,t)):
        path = [s]
        flow = flow + advance(C,path,t,F,0)
    return flow


def Main(C, source, sink, booln=False):
    global Source,Sink
    Source=source
    Sink=sink
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

    # remove existing files from imgs/resi
    folder2 = 'imgs/level'
    for filename in os.listdir(folder2):
        file_path = os.path.join(folder2, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    
    n = len(C)
    global path 
    global levelGraph
    levelGraph = [n*[0] for i in range(n)] # initialization of level graph
    path = len(levelGraph)*[0]

    global ctr
    ctr=0
    max_flow_value = MaxFlow(C, source, sink)
    #print ("max_flow_value is", max_flow_value)
    display_graphs.displayAllGraphs(max_flow_value,source,sink)