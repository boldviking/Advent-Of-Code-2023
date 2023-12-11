import math

data = []

with open("input.txt", "r") as file:
    for line in file:
        cLine = line.strip()
        data.append(cLine)

        if all(c == '.' for c in cLine):
            data.append(''.join(['e'] * len(cLine)))

# rotate galaxy for easier iteration.
# also while rotating the galaxy we need to blow
# up earth, so that the Vogon super intergalactic
# can be build
rotated = list(zip(*data))[::-1]
data.clear()

for x in rotated:
    data.append(x)

    if '#' not in x:
        data.append(''.join(['e'] * len(x)))

rotated.clear()
rotated = list(zip(*data[::-1]))

# rotate again to get everything back in order
# technically this step is not required, as the
# galaxy does not care in which way it is oriented.
# Just don't tell the Vogon's

galaxies = []

for y, y_ in enumerate(rotated):
    for x, x_ in enumerate(y_):
        if x_ == '#':
            galaxies.append([x, y])

distance = 0

for g, g_ in enumerate(galaxies):
    for h, h_ in enumerate(galaxies[g + 1:]):
        x = h_[0] - g_[0]
        y = h_[1] - g_[1]

        # caution c = g_ got reference assigned.
        # that caused quite the chaos xD
        c = [g_[0], g_[1]]
        d = [0, 0]

        for i in range(abs(x)):
            if x > 0:
                c[0] += 1
            else:
                c[0] -= 1
            if rotated[c[1]][c[0]] != 'e':
                d[0] += 1
            else:
                # remember we replace 1 row with 1000000
                d[0] += 1000000 - 1
            
        for i in range(abs(y)):
            if y > 0:
                c[1] += 1
            else:
                c[1] -= 1
            if rotated[c[1]][c[0]] != 'e':
                d[1] += 1
            else:
                # remember we replace 1 row with 1000000
                d[1] += 1000000 - 1
                
        distance += d[0] + d[1]

print(distance)