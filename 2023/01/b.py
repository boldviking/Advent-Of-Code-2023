import re 

def alphaToInt(alpha):
    match alpha:
        case "one":
            return '1'
        case "two":
            return '2'
        case "three":
            return '3'
        case "four":
            return '4'
        case "five":
            return '5'
        case "six":
            return '6'
        case "seven":
            return '7'
        case "eight":
            return '8'
        case "nine":
            return '9'

with open('b.txt') as f:
    sum = 0

    lines = f.readlines()
    for line in lines:
        r = []
        while True:
            rs = re.findall("[123456789]|one|two|three|four|five|six|seven|eight|nine", line)

            if not rs: 
                break

            line = line[1:]
            r.append(rs[0])

        numbers = []

        try:
            t = int(r[0])
            numbers.append(r[0])
        except:
            numbers.append(alphaToInt(r[0]))

        try:
            t = int(r[-1])
            numbers.append(r[-1])
        except:
            numbers.append(alphaToInt(r[-1]))

        n = int("{}{}".format(numbers[0], numbers[-1]))

        print("{} {} -> {}\n".format(line, r, n))
        sum += n
    
    print(sum)
