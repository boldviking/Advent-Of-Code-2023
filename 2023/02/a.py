with open('input.txt', 'r') as f:
    redLimit = 12
    greenLimit = 13
    blueLimit = 14

    resultSum = 0

    for line in f:
        try:
            game = line.split(':')
            sets = game[1].split(';')
            for set in sets:
                cubes = set.split(',')
                for cube in cubes:
                    count = int(''.join(filter(str.isdigit, cube)))
                    if "red" in cube:
                        if count > redLimit:
                            raise Exception('Red Exceeded')
                    if "green" in cube:
                        if count > greenLimit:
                            raise Exception('Green Exceeded')
                    if "blue" in cube:
                        if count > blueLimit:
                            raise Exception('Blue Exceeded')
            
            resultSum += int(''.join(filter(str.isdigit, game[0])))
        except:
            pass

    print(resultSum)