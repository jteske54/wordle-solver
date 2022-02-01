freq = {}
word_strength = {}

def main():
    global freq
    global word_strength
    words = word_list("wordle.txt")

def scored(wordlist):
    words = word_list(wordlist)
    freq = get_freq(words)
    score = get_score(words,freq)
    return score


def get_freq(words):
    for w in words:
        letts = list(w)
        for l in letts:
            try:
                freq[l] += 1
            except:
                freq[l] = 1
    return freq

def get_score(words,freq):
    for w in words:
        letts = list(set(w))
        score = 0
        for l in letts:
            score += freq[l]
        word_strength[w] = score
    word_strength_sorted = {x : y for x, y in sorted(word_strength.items(), key=lambda y: y[1], reverse=True)}
    return list(word_strength_sorted.keys())

def word_list(listloc):
    with open(listloc,"r") as f:
        words = [l.rstrip('\n') for l in f]
    return words

if __name__ == '__main__':
    main()