import Dinic
# import showGraph
import initShowGraph
import ErrorExit
# from tkinter import *
# from tkinter import filedialog

# def openInp():
C=[]
filename='uploads/inputUp.txt'

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


F = [[0] * len(C) for i in range(len(C))]
L = [[0] * len(C) for i in range(len(C))]
g_no="../inp_grp"
level=[]
print("create graph to be called")
initShowGraph.makeGraph(level, F,L,g_no,C,0,0,True)
print("create graph successful")