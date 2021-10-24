import cv2
import numpy as np
import json
import matplotlib.pyplot as plt
from pathsolver import solver
solve=solver()


def line(route):
    xc=[]
    yc=[]
    for i in (range(0,len(route))):
        x=route[i][0]
        y=route[i][1]
        xc.append(x)
        yc.append(y)
    return xc,yc


frame=cv2.imread("dept.jpg")
frame=cv2.resize(frame, (800,400))
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
th,frame=cv2.threshold(frame,200,255,cv2.THRESH_BINARY)
frame=cv2.bitwise_not(frame)
frame=cv2.dilate(frame,None,iterations=5)


def main():
    global obj,solve
    grid=frame
    start=(175,652)
    end=(170,560)
    route=solve.astar(start,end,frame)
    if(route==False):
        print("No path")
        return 0
    route+=[start]
    route=route[::-1]

    xc,yc=line(route)
    fig,ax=plt.subplots()
    ax.imshow(grid,cmap=plt.cm.Spectral)
    ax.plot(yc,xc,color="black")
    ax.scatter(start[1],start[0])
    ax.scatter(end[1],end[0])
    plt.show()
    
if(__name__=="__main__"):
    main()
