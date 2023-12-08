m = {"L": 0, "R": 1}

with open("input.txt", "r") as f:
    maps = {}

    steps = f.readline().strip()

    #skip next line
    f.readline()


    # weird bad file parsing again, because I woke up to early xD
    for line in f:
        split = line.split("=")[0].strip()
        lr = line.split("=")[1].strip()[1:-1].split(",")

        maps[split] = [lr[0].strip(), lr[1].strip()]

    # now we have a map :D

    node = maps["AAA"]
    sum = 0

    try:
        while True:
            for step in steps:
                sum += 1
                print ("{}({})->{}".format(node, step, node[m[step]]))
                if node[m[step]] == "ZZZ":
                    raise Exception("We have arrived")
                else:
                    node = maps[node[m[step]]]
    except:
        pass
    print(sum)


        
