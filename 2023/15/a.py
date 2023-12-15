def hash(line):
    retValue = 0
    for c in line:
        retValue += ord(c)
        retValue *= 17
        retValue %= 256 
    return retValue

data = None

with open("input.txt", "r") as file:
    data = file.read().strip()

sum = 0

for d in data.split(','):
    sum += hash(d)

print(sum)

# well that was easy xD.
# I sense danger for part 2