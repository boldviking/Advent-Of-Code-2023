import string 
plane = []
chars = set('0123456789.')
sum = 0

with open("sample.txt", "r") as f:
    for line in f:
        plane.append(line.strip())

xLen = len(plane[0])
yLen = len(plane)

allowed = set(string.digits + '.')

for y, y_ in enumerate(plane):
    digits = ""
    serial = False
    for x, x_ in enumerate(y_):
        if x_.isdigit():
            digits += x_
            env = ""
            for m, m_ in enumerate([-1, 0, 1]):
                for n, n_ in enumerate([-1, 0, 1]):
                    try:
                        env += plane[y + m_][x + n_]
                    except:
                        pass
            if not all(ch in allowed for ch in env):
                serial = True
        else:
            if serial:
                sum += int(digits)

            digits = ""
            serial = False

    if serial:
        sum += int(digits)
    
print(sum)