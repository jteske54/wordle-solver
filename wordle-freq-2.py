import pandas as pd

def main():
    words = word_list("wordle.txt")
    freqs = get_freq(words)
    strength = calc_strength(words, freqs)
    export_csv(strength)




def word_list(listloc):
    with open(listloc,"r") as f:
        words = [l.rstrip('\n') for l in f]
    return words


def get_freq(wordlist):
    freqs = {"1":{},"2":{},"3":{},"4":{},"5":{}}
    for w in wordlist:
        word = list(w)
        for l in range(len(word)):
            try:
                freqs[str(l+1)][word[l]] += 1
            except:
                freqs[str(l+1)][word[l]] = 1
    return freqs

def calc_strength(wordlist, freqs):
    strength = {}
    for w in wordlist:
        word = list(w)
        score = 0
        for l in range(len(word)):
            score += freqs[str(l+1)][word[l]]
        strength[w] = score
    strength_sorted = {k:v for k,v in sorted(strength.items(), key = lambda v: v[1], reverse=True)}
    return strength_sorted

def export_csv(strength):
    df = pd.DataFrame.from_dict(strength, orient="index")
    df.to_csv("out2.csv",header=False)

if __name__ == '__main__':
    main()