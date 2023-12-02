with open('input.txt', 'r') as f:
    redLimit = 12
    greenLimit = 13
    blueLimit = 14

    resultSum = 0

    for line in f:
        game = line.split(':')
        sets = game[1].split(';')
        limits = [0, 0, 0]
        for set in sets:
            cubes = set.split(',')
            for cube in cubes:
                count = int(''.join(filter(str.isdigit, cube)))
                if "red" in cube:
                    limits[0] = max(limits[0], count)
                if "green" in cube:
                    limits[1] = max(limits[1], count)
                if "blue" in cube:
                    limits[2] = max(limits[2], count)
        
        resultSum += limits[0] * limits[1] * limits[2]

    print(resultSum)