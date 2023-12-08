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

    nodes = {}

    # prep list of nodes we want to take a look at.
    # our only interest is start and end nodes.
    
    # Yeah I got confused here at some point xD.
    # This thing can probably run a little more efficient
    # however it gets the result done.
    # Keep in mind the data has some very special
    # features which makes this possible ^^.
    # this would probably break if it where any different.

    for key, value in maps.items():
        if key[-1] == 'A':
            nodes[key] = []
        if key[-1] == 'Z':
            nodes[key] = []

    for key, value in nodes.items():
        node = key
        index = 0
        try:
            while True:
                for step in steps:
                    index += 1
                    node = maps[node][m[step]]
                    if node[-1] == "Z":
                        raise Exception("Terminal found")
        except Exception as error:
            nodes[key] = [node, index]

    # for key, value in nodes.items():
    #     print(key, value, value[1] / 271)

    answer = len(steps)
    for key, value in nodes.items():
        if key[-1] == 'Z':
            answer *= (value[1] / len(steps))

    print(answer)
    
        
