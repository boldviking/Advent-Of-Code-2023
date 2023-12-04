with open("input.txt", "r") as f:
    sum = 0
    for line in f:
        game = line.split(':')
        card = game[1][:-1].split('|')
        numbers = card[0].split(' ')
        winners = card[1].split(' ')

        score = 0
        

        for n in numbers:
            try:
                n_ = int(n)
                for m in winners:
                    try:
                        m_ = int(m)
                        if n_ == m_:
                            score = max(1, 2 * score)
                    except:
                        pass
            except:
                pass
        print("{}: {} += {}".format(game[0], sum, score))
        sum += score
    print(sum)

        