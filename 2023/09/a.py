# Recursive descent into madness.
# I did not get lost multiple times in my own recursion
# never happend! There is no evidence of that in here! xD

def r(set):
    print(set)
    if all(s == 0 for s in set):
        return 0

    prev = set[0]
    nSet = []
    for s in set[1:]:
        nSet.append(s - prev)
        prev = s


    ret = r(nSet)
    #print("{} = {} + {}".format(set[-1] + ret, set[-1], ret))
    return set[-1] + ret


with open("input.txt", "r") as file:
    sum = 0
    for line in file:
        set = [int(x) for x in line.split()]
        sum += r(set)

print(sum)
# 715420621 too low
# 1992272679 too low
# 1997718392 too high
# 1997810708
# 1992273652
# 1054315252
