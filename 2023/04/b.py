with open("input.txt", "r") as f:
    sum = 0
    scores = []
    cards = []
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
                            score += 1
                    except:
                        pass
            except:
                pass
        #print("{}: {} += {}".format(game[0], sum, score))
        scores.append(score)

    scores.reverse()

    print(scores)

    for i, i_ in enumerate(scores):
        score = 1
        for c in range(i_):
            try:
                score += cards[i - c - 1]
            except:
                pass
        cards.append(score)
            
    print(cards)
    
    for i in cards:
        sum += i

    print(sum)

        