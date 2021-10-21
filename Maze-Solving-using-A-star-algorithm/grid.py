import cv2
import numpy as np

class gridmaker:
    def __init__(self,s):
        self.s=s
        self.img=cv2.imread("dept.jpg",0)
        self.h,self.w=self.img.shape
        self.grid=np.zeros(shape=(50,50))
    def iswhite(self,a,b,block):
        h,w=block.shape
        count=0
        for i in range(b,b+50):
            for j in range(a,a+50):
                if(i<960 and j<1629):
                    if(block[i][j]>0):
                        count=count+1                        
        # print(block[i][j])
        if(count>219):
            return True
        return False


    def returnGrid(self):
        for i in range(0,self.w,self.s):
            for j in range(0,self.h,self.s):
                if(self.iswhite(i,j,self.img)):
                    self.grid[int(j/self.s)][int(i/self.s)]=1
                    #cv2.rectangle(frame,(i,j),(i+self.s,j+self.s),(255,0,0),-1)
                #else:
                    #cv2.rectangle(frame,(i,j),(i+self.s,j+self.s),(255,0,0),1)

        return self.grid
