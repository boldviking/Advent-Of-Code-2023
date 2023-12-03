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

def extract(x, y):
    #print("{}:{} extract {}".format(x, y, plane[y][x]))
    digita = ""
    digitb = ""
    for z, z_ in reversed(list(enumerate(plane[y][:x]))):
        #print("{}:{} == {}".format(z, y, z_))
        if z_.isdigit():
            digita += z_
        else:
            break
    for z, z_ in enumerate(plane[y][x:]):
        #print("{}:{} == {}".format(z, y, z_))
        if z_.isdigit():
            digitb += z_
        else:
            break
    #print("return {} + {} = {}".format(digita, digitb, digita[::-1] + digitb))
    return digita[::-1] + digitb

for y, y_ in enumerate(plane):
    digits = ""
    serial = False
    for x, x_ in enumerate(y_):
        if x_ == '*':
            #print("{}:{} HIT".format(x, y))
            numbers = []
            for m, m_ in enumerate([-1, 0, 1]):
                serial = False
                for n, n_ in enumerate([-1, 0, 1]):
                    try:
                        value = plane[y + m_][x + n_]
                        if value.isdigit():
                            if not serial:
                                #print("{}:{} {} is digit".format(x + n_, y + m_, value))
                                numbers.append(extract(x + n_, y + m_))
                                serial = True
                        else:
                            serial = False
                    except:
                        pass
            #print(numbers)
            if len(numbers) == 2:
                sum += int(numbers[0]) * int(numbers[1])
    
print(sum)