with open("input.txt", "r") as f:
    # start of with overly complicated number extraction
    # I blame my feverish cold ridden brain for this one xD.
    fileData = f.read().strip()
    preData = fileData.strip().split("\n")
    preData2 = [preData[0].split(":")[1].split(), preData[1].split(":")[1].split()]
    print (preData2)
    
    data = []

    for i, i_ in enumerate(preData2[0]):
        data.append([int(preData2[0][i]), int(preData2[1][i])])

    sum = 1

    for d in data:
        wins = 0
        for i in range(d[0]):
            if (i * (d[0] - i)) > d[1]:
                wins += 1
        sum *= wins
    
    print(sum)

    