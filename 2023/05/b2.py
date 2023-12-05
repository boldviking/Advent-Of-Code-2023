import sys
import time
import math

with open("input.txt", "r") as f:
    start = time.time()
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

    location = 0

    try:
        while True:
            number = location
            if number % 1000000 == 0:
                print(number)
            for map in maps[::-1]:
                try:
                    for line in map:
                        if number in range(int(line[0]), int(line[0]) + int(line[2])):
                            #print("{} -> {}".format(number, int(line[1]) + (number - int(line[0]))))
                            number = int(line[1]) + (number - int(line[0]))
                            raise Exception("Mapping found")
                        
                    #print("{} -> {}".format(number, number))
                except:
                    pass
                
            for s in seeds:
                #print("{} <= {} <= {}".format(int(s[0]), number, int(s[0]) + int(s[1])))
                if number in range(int(s[0]), int(s[0]) + int(s[1])):
                    print("HIT")
                    raise Exception("Fucking found it")
                            
            location += 1
    except:
        print(location)
        end = time.time()
        print("total duration: {}".format(end - start))
# total duration: 1812.6648514270782


