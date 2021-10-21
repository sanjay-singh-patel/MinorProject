import json

f = open('testRoom.json',)
data = json.load(f)
doors = []
for i in data:
    doors.append(i)
f.close()

print(doors)

def generatePairs(doors):
    pairs = []
    for i in range(len(doors)):
        for j in range(i+1, len(doors)):
            pairs.append([doors[i], doors[j]])
    return pairs

pairs = generatePairs(doors)

def generatePaths(pairs):
    paths = {}
    for pair in pairs:
        print(pair[0])
        path = generatePath(pair)
        paths[tuple([eval(pair[0]),eval(pair[1])])] = path
    return paths

def generatePath(pair):
    
    # To be Coded
    
    return pair

print(generatePaths(pairs))