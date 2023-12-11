data = []

with open("test.txt", "r") as file:
    for line in file:
        cLine = line.strip()
        data.append(cLine)

        if all(c == '.' for c in cLine):
            data.append(cLine)

rotated = list(zip(*data))[::-1]
data.clear()
for x in rotated:
    data.append(x)

    if all(c == '.' for c in x):
        data.append(x)

rotated.clear()
rotated = list(zip(*data[::-1]))

galaxies = []

for y, y_ in enumerate(rotated):
    for x, x_ in enumerate(y_):
        if x_ == '#':
            galaxies.append([x, y])

distance = 0

for g, g_ in enumerate(galaxies):
    for h, h_ in enumerate(galaxies[g + 1:]):
        dis = abs(h_[0] - g_[0]) + abs(h_[1] - g_[1])
        print("distance: {} = abs({} - {}) + abs({} - {})".format(dis, h_[0], g_[0], h_[1], g_[1]))
        distance += dis
        # print(dis)

print(distance)