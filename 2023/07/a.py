m = {
    "A": "112",
    "K": "111",
    "Q": "110",
    "J": "102",
    "T": "101",
    "9": "100",
    "8": "022",
    "7": "021",
    "6": "020",
    "5": "012",
    "4": "011",
    "3": "010",
    "2": "002"
    }
    

# We are going to use card grading for this one.
# Every card will be represented as a base 3 number.
# Why base 3 ... well because of 2 of a kind :D.
# Each hand will be represented as a number like this:
# Note the '-' are in here only for clarification
# 0-0-0-0-000-000-000-000-000
# So we got 4 groups of 1 digit and 5 groups of 3 digits.
# Starting from start to end we get:
#   number of 5 of a kind
#   number of 4 of a kind
#   number of 3 of a kind
#   number of 2 of a kind
#   value of first card
#   value of second card
#   value of third card
#   value of fourth card
#   value of fifth card
#
# using this numbering schema we can guarantee that
# a five of a kind is always stronger than any 4 of
# a kind. The same is true for every other pair.
# A full house is automatically stronger than 
# pair and tripple since it will have the value of
# 1 for each of them.
# A two pair will not be stronger than a tripple,
# we are using base 3 so a 2 pair will have a value of 02
# where as the triple will have a value of 10.
#
# finally we just add the cards in order at the end.
# Then we just caluclate the full number into a base10
# value and we can use that to compare.
#
# We could probably leave it at base 3 as well, though
# I am not sure how good python would be in working base 3
# so we just use base 10 to be sure (also easier on the brain)

with open("input.txt", "r") as f:
    data = []
    limit = 0
    for line in f:
        dataline = line.strip().split()
        set = []

        combinations = [0,0,0,0,0]
        prev = None
        streak = 1

        for i in sorted(dataline[0]):

            if prev is not None:
                if i == prev:
                    streak += 1
                else:
                    combinations[-streak] += 1
                    streak = 1

            prev = i

        combinations[-streak] += 1

        s = ''.join(str(x) for x in combinations[:-1])

        for i in dataline[0]:
            s += m[i]

        set.append(int(s, base=3))
        set.append(int(dataline[1]))
        data.append(set)


    data.sort(key=lambda x: x[0])

    rank = 0
    sum = 0

    for hand in data:
        rank += 1

        #print("{} += {} * {}".format(sum, hand[1], rank))
        sum += hand[1] * rank

    print(sum)

    # 247874660 too low
    # 253125840 too high
    # 252054393 too high
    # 252052080 correct