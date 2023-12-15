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

hashmap = {}

for d in data.split(','):
    print(d)
    done = False

    if d[-1] == '-':
        label = d[:-1]
        hashValue = hash(label)
        try:
            for lens in hashmap[hashValue]:
                if lens[0] == label:
                    hashmap[hashValue].remove(lens)
                    print("Remove Lens")
                    done = True
                    break
        except:
            pass
        print("No such lens")
            

    else:
        label = d[:-2]
        hashValue = hash(label)
        try:
            for lens in hashmap[hashValue]:
                if lens[0] in label:
                    lens[1] = int(d[-1])
                    print("Change lens")
                    done = True
                    break

            if not done:
                hashmap[hashValue].append([label, int(d[-1])])
                print("Append lens")
        except:
            hashmap[hashValue] = [[label, int(d[-1])]]
            print("Add lens")

for key, value in hashmap.items():
    for v, v_ in enumerate(value):
        sum += (1 + key) * (v + 1) * v_[1]
        #print("{} += (1 + {}) * ({} + 1) * {}".format(sum, key, v, v_[1]))
        

print(sum)

        
            

    

