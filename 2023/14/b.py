data = []
snapshot = []

with open("test.txt", "r") as file:
    for line in file:
        data.append(line.strip())

rotated = list(zip(*data))[::-1]

data.clear()

for l in rotated:
    data.append(''.join(l))
    snapshot.append(''.join(l))

print(data)

sum = 0

preRotated = []

for i in range(10000000):
    if i % 1000000 == 0:
        print("Iteration: {}M".format(i))

    if i % 4 == 0 and i != 0:
        earlyExit = True

        for sn, da in zip(snapshot, data):
            if sn != da:
                earlyExit = False
                break

        if earlyExit:
            print("Early Exit")
            break

        snapshot.clear()
        for l in data:
            snapshot.append(l)

    sum = 0

    # print("Input:")
    # for line in data:
    #     print(line)

    for line in data:
        subLines = line.split('#')
        position = len(line)
        newSubLines = []
        for subLine in subLines:
            subPosition = position
            balls = subLine.count('O')
            for j in range(balls):
                sum += subPosition
                subPosition -= 1

            position -= len(subLine) + 1

            #print(balls, len(subLine))
            newSubLine = 'O' * balls + '.' * (len(subLine) - balls)
            #print("subLine: ", newSubLine)
            newSubLines.append(newSubLine)

        preRotated.append('#'.join(newSubLines))
        #print("newLine: ", newLine)

    # print("Output:")
    # for line in preRotated:
    #     print(line)

    rotated = list(zip(*preRotated[::-1]))

    data.clear()

    for l in rotated:
        data.append(''.join(l))

    preRotated.clear()

    


print(sum)
# 103614 first try :D