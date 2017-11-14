#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 10:59:51 2017
@author: tcs-user
"""

import random  # calculate random numbers
DICT = ['east', 'eats', 'seat', 'teas']


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
                guess = guess[:j] + inp + guess[j + 1:]
        print('Hit!')
        print('The word: ' + guess)
    else:
        attempts += 1
        print('Nussed, mistake %d out of %d' % (attempts, length))
    return guess, letter, attempts


def get_input():
    var = input()
    return var[0]


def gener_random():
    random.seed(0)
    i = random.randint(0, 3)
    print("GUESS a LETTER:")
    return i


def gener_init(i):
    letter = DICT[i]
    length = len(letter)
    guess = '*' * length
    attempts = 0
    return letter, length, guess, attempts


def play():
    i = gener_random()
    letter, length, guess, attempts = gener_init(i)
    while attempts < length and guess != letter:
        inp = get_input()
        guess, letter, attempts = check(inp, guess, letter, attempts)
    print(loss(attempts, length))
    return 0
