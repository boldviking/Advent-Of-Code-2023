import math

def checkPalindrom(line):
    print(line)
    for i in range(math.floor(len(line)/2)):
        if line[i] != line[-i - 1]:
            return False
    print("True")
    return True

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

    print("answer", x, y)

    if x > y:
        output += x * 100
    else:
        output += y

    print(output)
    sum += output

print(math.floor(sum))

#19766.0 too low ...
#68203.0 too high ...
#63252.0 too high ...
#45170 incorrect
#44938 incorrect
#45074 incorrect
#42974 correct