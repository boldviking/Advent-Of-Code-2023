from multiprocessing import Pool

allowed = set('#?')

score = 0

def r(data, n = 0):
    if not data[1]:
        if '#' in data[0]:
            # print("{}# in remain".format("\t"*n))
            return 0
        else:
            # print("{}valid".format("\t"*n))
            return 1

    ret = 0

    for i in range(len(data[0])):
        pre = data[0][:i]
        post = data[0][i + data[1][0]:]
        match = data[0][i:data[1][0] + i]

        try:
            if post[0] == '#':
                # print("{}# touching spring".format("\t"*n))
                continue
        except:
            pass

        if '#' in pre:
            # print("{}# in pre".format("\t"*n))
            return ret
        
        if len(match) != data[1][0]:
            # print("{}# group to small".format("\t"*n))
            return ret

        

        if all(ch in allowed for ch in data[0][i:data[1][0] + i]):
            
            # print("{}{}»{}«{}".format("\t"*n, pre, match, post))
            ret += r([post[1:], data[1][1:]], n + 1)

    return ret

sum = 0

data = []

with open("test.txt", "r") as file:
    for line in file:
        sLine = line.split(' ')
        springs = sLine[0].strip()
        lgroups = sLine[1].strip().split(',')

        groups = []

        for g in lgroups:
            groups.append(int(g))

        exGroup = groups.copy()
        exSprings = springs

        for i in range(4):
            for g in groups:
                exGroup.append(g)

        for i in range(4):
            exSprings += '?' + springs

        data.append([exSprings, exGroup])


def r2(data):
    ret = r(data)
    print(ret)
    return ret

pool = Pool(16)
results = pool.map(r2, data)
pool.close()
pool.join()

for i in results:
    sum += i

print(sum)
        
