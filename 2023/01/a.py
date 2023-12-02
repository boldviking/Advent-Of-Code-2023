with open('a.txt') as f:
    sum = 0

    lines = f.readlines()
    for line in lines:
        numbers = []
        for c in line:
            if c.isdigit():
                numbers.append(c)
        sum += int("{}{}".format(numbers[0], numbers[-1]))
    
    print(sum)
