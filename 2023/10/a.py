import math
data = []

start = [0, 0]

movement = {
    "|": {"N": [ 0,-1, "N"], "S": [ 0, 1, "S"]},
    "-": {"E": [ 1, 0, "E"], "W": [-1, 0, "W"]},
    "F": {"N": [ 1, 0, "E"], "W": [ 0, 1, "S"]},
    "L": {"S": [ 1, 0, "E"], "W": [ 0,-1, "N"]},
    "J": {"E": [ 0,-1, "N"], "S": [-1, 0, "W"]},
    "7": {"N": [-1, 0, "W"], "E": [ 0, 1, "S"]},
}

with open("input.txt", "r") as file:

    x = 0
    y = 0

    for line in file:
        x = 0
        data.append(line.strip())
        for i in line:
            if i == 'S':
                start = [x, y]
                break
            x +=1
        y += 1

startPositions = []
startPositions.append([start[0] - 1, start[1], "W"])
startPositions.append([start[0] + 1, start[1], "E"])
startPositions.append([start[0], start[1] - 1, "N"])
startPositions.append([start[0], start[1] + 1, "S"])

results = []

print(start)
print(startPositions)

for s in startPositions:
    position = s
    moves = 1
    try:
        while True:
            current = data[position[1]][position[0]]
            #print(current)
            move = movement[current][position[2]]
            position[0] += move[0]
            position[1] += move[1]
            position[2] = move[2]
            moves += 1
            
    except Exception as error:
        print(moves / 2)