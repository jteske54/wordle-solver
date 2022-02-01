import wordlefreq as wf
import logging

logging.basicConfig(filename="debug.log",level=logging.DEBUG)

def main(letters_remaining,letter_status):
    words = wf.scored("wordle.txt")
    for q in range(6):
        space(8)
        best_guesses(words)
        space(3)
        letters_remaining, letter_status, words = guess(letters_remaining,letter_status,words)
        
    
    
# Done
def guess(letters_remaining,letter_status,words):
    guess = str(input("Enter your guess: ").lower())
    green = str(input("Enter the indexes of the green letters, separated by a space: "))
    orange = str(input("Enter the indexes of the orange letters, separated by a space: "))
    greys = [0,1,2,3,4]
    if green != '':
        greens = [int(i)-1 for i in green.split(" ")]
        letters_remaining, letter_status =  green_letter(letters_remaining,letter_status,greens,guess)
        for i in greens:
            greys.remove(i)
    if orange != '':
        oranges = [int(i)-1 for i in orange.split(" ")]
        letters_remaining,words = orange_letter(letters_remaining,oranges,guess,words)
        for i in oranges:
            greys.remove(i)
    letters_remaining = grey_letter(letters_remaining,letter_status,greys,guess)
    logging.debug(letters_remaining)
    words = recalc_words(letters_remaining, words)
    return letters_remaining, letter_status, words

# Done
def grey_letter(letters_remaining,letter_status,ind,guess):
    for index, value in enumerate(ind):
        for ind, chars in enumerate(letters_remaining):
            if letter_status[ind] == 'known':
                    continue
            try:
                letters_remaining[ind].remove(guess[index])
                logging.debug(guess[ind])
            except:
                pass
    return letters_remaining

# Done
def green_letter(letters_remaining,letter_status,ind,guess):
    for i in ind:
        letters_remaining[i] = [guess[i]]
        letter_status[i] = 'known'
    return letters_remaining, letter_status

# Done
def orange_letter(letters_remaining,indexes,guess,words):
    result = []
    for index in indexes:
        letters_remaining[index].remove(guess[index])
        for word in words:
            if guess[index] in word:
                result.append(word)
    return letters_remaining, result

# Done
def recalc_words(letters, words):
    result = []
    for word in words:
        all_letters_match = True
        for index, letter in enumerate(word):
            if letter not in letters[index]:
                all_letters_match = False
                break
        if all_letters_match:
            result.append(word)

    return result

# Done
def space(num):
    for a in range(num):
        print()

# Done
def best_guesses(words):
    print(str(len(words)) + " possibilities remaining...")
    print("Best guesses:")
    if len(words) > 10:
        for a in range(10):
            print(words[a])
    else:
        for a in words:
            print(a)

letters = list('abcdefghijklmnopqrstuvwxyz')
letters_remaining = [[letter for letter in letters]for index in range(5)]
letter_status = ['unknown','unknown','unknown','unknown','unknown']

if __name__ == '__main__':
    main(letters_remaining,letter_status)