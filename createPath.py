import cv2
import json
from pathsolver import solver

f = open('testRoom.json',)
data = json.load(f)
doors = []
for i in data:
    doors.append(i)
f.close()

# print(doors)

frame=cv2.imread("dept.jpg")
frame=cv2.resize(frame, (800,400))
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
th,frame=cv2.threshold(frame,200,255,cv2.THRESH_BINARY)
frame=cv2.bitwise_not(frame)

def draw_route(frame, route):
    for r in route:
        frame[r[0]][r[1]] = 255
    return frame

def generatePairs(doors):
    pairs = []
    for i in range(len(doors)):
        for j in range(i+1, len(doors)):
            pairs.append([doors[i], doors[j]])
    return pairs

pairs = generatePairs(doors)

def generatePaths(pairs):
    solve = solver()
    paths = {}
    for pair in pairs:
        path = generatePath(pair, solve)
        paths[tuple([eval(pair[0]),eval(pair[1])])] = path
    return paths

def generatePath(pair, solve):
    start = eval(pair[0])
    end = eval(pair[1])
    print('checking')
    
    route=solve.astar(start,end,frame)
    if(route==False):
        print("No path")
        return 0
    route+=[start]
    route=route[::-1]
    
    return route

paths = generatePaths(pairs)

for path in paths.values():
    draw_route(frame, path)
    
cv2.imshow( "frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()