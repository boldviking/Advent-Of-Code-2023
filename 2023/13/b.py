import math

# We basically need to check for every value that is in
# hemming range 1 once. So we just use xor to see how
# many bits are different. Then count those bits
# if it is more than 1 it is wrong.
# if it exactly one we apply the smudge once
# if it is 0 and we have used smudge it is correct.

def checkPalindrom(line):
    # print(line)
    smudge = False
    for i in range(math.floor(len(line)/2)):
        comp = line[i] ^ line[-i - 1]
        distance = bin(comp).count("1")
        if distance >= 2:
            return False
        elif distance >= 1 and not smudge:
            smudge = True
        elif distance >=1 and smudge:
            return False
    return True and smudge

def checkForAnyPalindrom(line):
    i = 2
    found = False
    while (i < len(line)) and not found:
        found = checkPalindrom(line[:i])
        i += 2

    if found:
        return (i / 2)
    else:
        return -1

data = []

with open("input.txt", "r") as file:
    data.append([])
    for line in file:
        if len(line) == 1:
            data.append([])
            continue

        data[-1].append(line.strip())

sum = 0

for d in data:
    xPlane = []
    yPlane = []

    for l in d:
        l = l.replace(".", "0")
        l = l.replace("#", "1")
        xPlane.append(int(l, 2))

    rotated = list(zip(*d))[::-1]    

    for l in rotated:
        s = ''.join(l)
        s = s.replace(".", "0")
        s = s.replace("#", "1")
        yPlane.append(int(s, 2))

    x = 0
    y = 0

    x = checkForAnyPalindrom(xPlane)
    if x > 0:
        x -= 1

    if x < 0:
        x = checkForAnyPalindrom(xPlane[::-1])
        if x > 0:
            x = len(xPlane) - x + 1

    y = checkForAnyPalindrom(yPlane)
    if y > 0:
        y = len(yPlane) - y + 1

    if y < 0:
        y = checkForAnyPalindrom(yPlane[::-1])
        if y > 0:
            y -= 1

    output = 0


    # add wacky not want to deal with proper logic
    # way of ignoring wrong results :D
    if x < 0:
        x = 50000

    if y < 0:
        y = 50000

    if x < y:
        output += x * 100
    else:
        output += y

    print("answer", x, y)

    print(output)
    sum += output

print(math.floor(sum))

# 19120 too low
# 27587 correct