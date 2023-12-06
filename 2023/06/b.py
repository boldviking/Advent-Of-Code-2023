import math

with open("input.txt", "r") as f:
    # start of with overly complicated number extraction
    # I blame my feverish cold ridden brain for this one xD.
    fileData = f.read().strip()
    preData = fileData.strip().split("\n")
    preData2 = [preData[0].split(":")[1].split(), preData[1].split(":")[1].split()]
    print (preData2)
    
    data = []

    time = ""
    distance = ""

    for d in preData2[0]:
        time += d

    for d in preData2[1]:
        distance += d

    time = int(time)
    distance = int(distance)

    # the distance traveled will result in a standard curve.
    # something like this
    # 0                  | looser
    # 4                  | looser
    # 6 <-- minimum time | winners
    # 8                  | winners
    # 9                  | winners
    # 8                  | winners
    # 6 <-- maximum time | winners
    # 4                  | looser
    # as such we only need to calculate the minimum time
    # and reapply this from the other side.
    # 
    # We know this function by looking at part a of the puzzle
    #
    # f(x) = x * (t - x)
    # f(x) = -x^2 + xt
    # 
    # now we need to calculate the intersection at winning distance
    # we use a fancy online tool for that since my brain can't math
    # f1(x) = (-t + sqrt(t^2 - 4*x)) / 2 
    # f2(x) = (-t - sqrt(t^2 - 4*x)) / 2
    #
    # for dataset 1 
    # time = 48
    # distance = 296
    # f1(296) = -7.2   
    # f2(296) = -40.73 
    #
    # floor and absolute both values

    minimumTime = -math.floor((-time + math.sqrt(time * time - 4 * distance)) / 2)
    print (minimumTime)
    maximumTime = -math.floor((-time - math.sqrt(time * time - 4 * distance)) / 2)
    print (maximumTime)
    
    print(maximumTime - minimumTime)

    