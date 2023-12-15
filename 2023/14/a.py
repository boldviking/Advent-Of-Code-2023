data = []

with open("input.txt", "r") as file:
    for line in file:
        data.append(line.strip())

rotated = list(zip(*data))[::-1]

data.clear()

for l in rotated:
    data.append(''.join(l))

print(data)

sum = 0

for line in data:
    print(line)
    subLines = line.split('#')
    position = len(line)
    for subLine in subLines:
        subPosition = position
        for i in range(subLine.count('O')):
            sum += subPosition
            subPosition -= 1
        #print("{} += {} * {}".format(sum, subLine.count('O'), position))
        position -= len(subLine) + 1
        # print("{} -= {} - {}".format(position, len(subLine), 1))


print(sum)
# 103614 first try :D