import re

allowed = set('#?')

score = 0

def r(lines, groups, n):
    if not groups:
        if '#' in lines:
            print("{}# in remain".format("\t"*n))
            return 0
        else:
            print("{}valid".format("\t"*n))
            return 1

    ret = 0

    for i in range(len(lines)):
        pre = lines[:i]
        post = lines[i + groups[0]:]
        match = lines[i:groups[0] + i]

        if '#' in pre:
            #print("{}# in pre".format("\t"*n))
            return ret
        
        if len(match) != groups[0]:
            print("{}# group to small".format("\t"*n))
            return ret
        
        try:
            if post[0] == '#':
                # print("{}# touching spring".format("\t"*n))
                continue
        except:
            pass

        if all(ch in allowed for ch in lines[i:groups[0] + i]):
            
            print("{}{}»{}«{}".format("\t"*n, pre, match, post))
            ret += r(post[1:], groups[1:], n + 1)

    return ret

        
sum = 0


with open("input.txt", "r") as file:
    for line in file:
        sLine = line.split(' ')
        springs = sLine[0].strip()
        lgroups = sLine[1].strip().split(',')

        groups = []

        for g in lgroups:
            groups.append(int(g))

        a = r(springs, groups, 0)
        print(a)
        sum += a

print(sum)
        

# 9460 too high
# 8290 too high
# 8028 too high