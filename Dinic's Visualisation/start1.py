import Dinic
k = input()
filename = 'inputs/input'+k+'.txt'
try:
    with open(filename) as textFile:
        Cx = [line.split() for line in textFile]
except:
    print("Invalid input file contents")
    exit()
C=[]

for lst in C:
    if len(lst) is not len(Cx[0]):
        print("Invalid input file contents")
        exit()
try:
    for i in range(len(Cx[0])):
        C.append([int(j) for j in Cx[i]])
except:
    print("Invalid input file contents")
    exit()

Dinic.Main(C,0,(int(len(C)-1)))