import sys
import time
import math

# using the sollution from part 1 is not recommended xD. This works in due time ... say
# is that the heat death of the universe over there?

with open("input.txt", "r") as f:
    result = sys.maxsize
    rawdata = ""
    for line in f:
        rawdata += line

    rawdata = rawdata.split("\n\n")

    seeds = []
    maps = []

    preSeeds = rawdata[0].split(":")[1].strip().split()
    for i in range(int(len(preSeeds)/2)):
        seeds.append([preSeeds[i * 2], preSeeds[i * 2 + 1]])

    for topic in rawdata[1:]:
        data = []
        data1 = topic.split(":")[1].strip()
        data2 = data1.split('\n')
        for d in data2:
            data.append(d.split())
        maps.append(data)

    for seed in seeds:
        start = time.time()
        print("seeds: {} to {}: about {}M elements".format(int(seed[0]), int(seed[0]) + int(seed[1]), math.floor(int(seed[1]) / 1000000)))
        for s in range(int(seed[0]), int(seed[0]) + int(seed[1])):
            if s % 1000000 == 0:
                end = time.time()
                print("1M matches took: {}".format(end - start))
                start = time.time()
            number = s
            for map in maps:
                for line in map:
                    if int(line[1]) <= number <= int(line[1]) + int(line[2]):
                        number = int(line[0]) + (number - int(line[1]))
                        break

            prevResult = result
            result = min(result, number)
            if result < prevResult:
                print(prevResult)

print(result)