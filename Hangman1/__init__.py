
import random  # calculate random numbers
DICT = ['hello', 'apple', 'phone', 'smell', 'brink']


def loss(attempts, num):  # calculate loss
    if attempts >= num:
        return 'You lost!'
    return 'You won!'


def check(inp, guess, letter, attempts):
    inp = inp[0]
    length = len(letter)
    if inp in letter:
        for j in range(length):
            if letter[j] == inp:
                guess = guess[:j] + inp + guess[j+1:]
        print('Hit!')
        print('The word: '+guess)
    else:
        attempts += 1
        print('Nussed, mistake %d out of %d' % (attempts, length))
    return guess, letter, attempts


def play():
    random.seed(0)
    i = random.randint(0, 4)
    print("GUESS a LETTER:")
    letter = DICT[i]
    length = len(letter)
    guess = '*'*length
    attempts = 0
    while attempts < length:
        inp = input()
        inp = inp[0]
        guess, letter, attempts = check(inp, guess, letter, attempts)
        if guess == letter:
            break
    print(loss(attempts, length)+'\n')
