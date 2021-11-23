import cv2
import json
import pandas as pd
from pathsolver import solver

f = open('Rooms.json',)
data = json.load(f)
doors = []
for i in data:
    doors.append(i)
print('doors found')
f.close()

# print(doors)

frame=cv2.imread("./images/dept.jpg")
frame=cv2.resize(frame, (800,400))
frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
th,frame=cv2.threshold(frame,200,255,cv2.THRESH_BINARY)
frame=cv2.bitwise_not(frame)

def draw_doors(doors,frame):
    for door in doors:
        print(door)
        cv2.circle(frame, (eval(door)[1],eval(door)[0]), 5, (255,0,0))

def draw_route(frame, route):
    if route == 0: return
    for r in route:
        frame[r[0]][r[1]] = 150
    return frame

def generatePairs(doors):
    pairs = []
    for i in range(len(doors)):
        for j in range(i+1, len(doors)):
            pairs.append([doors[i], doors[j]])
    return pairs


def generatePaths(pairs):
    solve = solver()
    paths = {}
    for pair in pairs:
        print(f"FINDING PATHS {pair}")
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

def createDataFrame(paths):
    source_pd = []
    dest_pd = []
    paths_pd = []
    for key in paths.keys():
        source_pd.append(key[0])
        dest_pd.append(key[1])
    for val in paths.values():
        paths_pd.append(val)
        
    df = {"sources": source_pd, "destinations": dest_pd, "paths": paths_pd}
    dataframe = pd.DataFrame(df, index=None)
    dataframe.to_csv('Paths.csv')
    print(dataframe)

def main():
    solve = solver()
    print("Welcome to Indoor Navigation of CSE department")
    count = 0
    print(list(data.keys()))
    current_location = None
    for i in data.keys():
        print(count, data[i])
        count+=1
    opt = int(input('Select your current location: '))
    current_location = list(data.keys())[opt]
    print(current_location)
    dest_location = None
    count = 0
    for i in data.keys():
        if i == opt: continue
        print(count, data[i])
        count+=1
    dest = int(input('Select your current location: '))
    dest_location = list(data.keys())[dest]
    print(dest_location)
    path = generatePath((current_location, dest_location), solve)
    if path == 0: 
        return
    draw_doors(doors,frame)
    draw_route(frame, path)

main()
print(doors)
# pairs = generatePairs(doors)
# paths = generatePaths(pairs)
# createDataFrame(paths)

# for path in paths.values():
    # draw_route(frame, path)
frame=cv2.cvtColor(frame,cv2.COLOR_GRAY2RGBA)

cv2.imshow( "frame", frame)
cv2.waitKey(0)
cv2.destroyAllWindows()