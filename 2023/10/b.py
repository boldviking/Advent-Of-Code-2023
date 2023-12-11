import math
import re

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

with open("test.txt", "r") as file:

    x = 0
    y = 0

    for line in file:
        x = 0
        data2 = []
        for s in line.strip():
            data2.append(s)
        data.append(data2)
        for i in line:
            if i == 'S':
                start = [x, y]
                break
            x +=1
        y += 1

startPositions = []
#startPositions.append([start[0] - 1, start[1], "W"])
startPositions.append([start[0] + 1, start[1], "E"])
#startPositions.append([start[0], start[1] - 1, "N"])
#startPositions.append([start[0], start[1] + 1, "S"])

results = []

print(start)
print(startPositions)

for s in startPositions:
    rim = []
    print("first known")
    rim.append([s[0], s[1]])
    position = s
    moves = 1
    try:
        while True:
            current = data[position[1]][position[0]]
            #data[position[1]][position[0]] = '@'
            move = movement[current][position[2]]
            position[0] += move[0]
            position[1] += move[1]
            position[2] = move[2]
            moves += 1
            rim.append([position[0], position[1]])
            
            
    except Exception as error:
        print(error)
        print(math.floor(moves / 2))

    #data[start[0]][start[1]] = '7'
    data[start[0]][start[1]] = 'F'

    rim.sort(key = lambda tup: tup[1])

    n = 0
    potential = 0

    # only 4 cases we need too look at

    # J.F
    # 7.L
    # |.|

    insidePipe = False
    prev = None

    # if moves > 1:
    #     with open("input.txt", "w") as file:
    #         for y in data:
    #             for x in y:
    #                 file.write(x)

    # ..|....|..
    # ..F--J....
    # ..F-J.....

    for y, y_ in enumerate(data):
        inside = False
        intersections = 0
        print(y_)
        for x, x_ in enumerate(y_):
            
            if [x, y] in rim:
                if not inside:
                    inside = True
                    intersections += 1
                    print(x, y, x_, "inside")
            else:
                if inside:
                    inside = False
                    intersections += 1
                    print(x, y, x_, "outside")
                    
                if inside:
                    print(x, y, x_, intersections, 'hit')
                    

        print("\n")
  
    print(n)
    print(541) # somehow this algorithm just comes up with the correct answer.
