import sys

with open("input.txt", "r") as f:
    result = sys.maxsize
    rawdata = ""
    for line in f:
        rawdata += line

    rawdata = rawdata.split("\n\n")

    seeds = []
    maps = []

    seeds = rawdata[0].split(":")[1].strip().split()

    for topic in rawdata[1:]:
        data = []
        data1 = topic.split(":")[1].strip()
        data2 = data1.split('\n')
        for d in data2:
            data.append(d.split())
        maps.append(data)

    for seed in seeds:
        number = int(seed)
        for map in maps:
            for line in map:
                if int(line[1]) <= number <= int(line[1]) + int(line[2]):
                    number = int(line[0]) + (number - int(line[1]))
                    break

        result = min(result, number)

print(result)

