#!/usr/bin/env python3 east eats seat teas
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 11:52:21 2017
@author: tcs-user
"""
from itertools import combinations
from Hangman import check, DICT


def test_check():
    game_situations = []
    for word in DICT:
        for i in range(4):
            current = word
            comb = combinations(word, i)
            for letters in comb:
                for letter in letters:
                    current = current.replace(letter, '*')
            if current not in game_situations:
                game_situations.append(current)

    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(4):
        for word in DICT:
            for lett in alph:
                for guess in game_situations:
                    if lett not in word:
                        assert check(lett, guess, word,
                                     i) == (guess, word, i + 1)
                    else:
                        ind = word.find(lett)
                        guess1 = guess[:ind] + lett + guess[ind + 1:]
                        assert check(lett, guess, word,
                                     i) == (guess1, word, i)


test_check()
